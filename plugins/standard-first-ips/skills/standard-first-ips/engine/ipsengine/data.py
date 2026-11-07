"""Download and read the public data the engine uses, and build real monthly sleeve returns.

Sources (all free, public):
- Ken French data library: US market and risk-free (F-F Research Data Factors, monthly) and the
  six size/book-to-market portfolios (`value` = average of small-value and big-value).
- FRED CPIAUCNS: US CPI, to convert nominal returns to real.
- AQR "Century of Factor Premia" (monthly): asset-class market composites, used to build a paper
  time-series-momentum (trend) proxy back to the 1920s.

Users can bring any other monthly series with `source = "csv:<path>:<column>"`.
"""

from __future__ import annotations

import csv
import io
import shutil
import subprocess
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

FRENCH = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/"
SOURCES = {
    "F-F_Research_Data_Factors.csv": FRENCH + "F-F_Research_Data_Factors_CSV.zip",
    "6_Portfolios_2x3.csv": FRENCH + "6_Portfolios_2x3_CSV.zip",
    "CPIAUCNS.csv": "https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCNS",
    "Century-of-Factor-Premia-Monthly.xlsx": (
        "https://www.aqr.com/-/media/AQR/Documents/Insights/Data-Sets/"
        "Century-of-Factor-Premia-Monthly.xlsx"
    ),
}
USER_AGENT = "standard-first-ips/0.1 (research script)"


def fetch(data_dir: Path, force: bool = False) -> list[str]:
    """Download every source into `data_dir`, logging retrieval times to RETRIEVED.csv.

    Args:
        data_dir: Destination directory (created if missing).
        force: Re-download files that already exist.

    Returns:
        Human-readable status lines, one per file.
    """
    data_dir.mkdir(parents=True, exist_ok=True)
    log = data_dir / "RETRIEVED.csv"
    lines = []
    for name, url in SOURCES.items():
        dest = data_dir / name
        if dest.exists() and not force:
            lines.append(f"kept {name}")
            continue
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = resp.read()
        except OSError as e:
            # Some hosts (FRED) stall urllib clients but serve curl; fall back to it if present.
            got = (
                subprocess.run(["curl", "-sfL", "-m", "120", url], capture_output=True, check=False)
                if shutil.which("curl")
                else None
            )
            if got is None or got.returncode != 0 or not got.stdout:
                lines.append(f"FAILED {name}: {e}. Download {url} by hand into {data_dir}/")
                continue
            body = got.stdout
        if url.endswith(".zip"):
            with zipfile.ZipFile(io.BytesIO(body)) as z:
                inner = next(n for n in z.namelist() if n.lower().endswith(".csv"))
                body = z.read(inner)
        dest.write_bytes(body)
        stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        new = not log.exists()
        with log.open("a", newline="") as f:
            w = csv.writer(f)
            if new:
                w.writerow(["file", "url", "retrieved_utc", "bytes"])
            w.writerow([name, url, stamp, len(body)])
        lines.append(f"fetched {name} ({len(body):,} bytes)")
    return lines


def _month_end(idx: pd.Index) -> pd.DatetimeIndex:
    return pd.DatetimeIndex(idx) + pd.offsets.MonthEnd(0)


def _french_first_table(path: Path, ncols: int) -> pd.DataFrame:
    """First monthly (YYYYMM) table of a French CSV, as decimal returns."""
    rows: list[list[str]] = []
    header: list[str] = []
    with path.open(errors="replace") as f:
        prev: list[str] = []
        for r in csv.reader(f):
            key = r[0].strip() if r else ""
            if key.isdigit() and len(key) == 6:
                if not rows:
                    header = [c.strip() for c in prev[1 : ncols + 1]]
                rows.append(r)
            elif rows:
                break
            prev = r
    idx = _month_end(pd.to_datetime([r[0].strip() for r in rows], format="%Y%m"))
    vals = [[float(v) for v in r[1 : ncols + 1]] for r in rows]
    return pd.DataFrame(vals, index=idx, columns=header) / 100


def read_market(path: Path) -> tuple[pd.Series, pd.Series]:
    """US market total return and risk-free rate, monthly nominal."""
    t = _french_first_table(path, 4)
    return t["Mkt-RF"] + t["RF"], t["RF"]


def read_value(path: Path) -> pd.Series:
    """Average of small-value and big-value portfolios (value-weighted), monthly nominal."""
    t = _french_first_table(path, 6)
    t.columns = ["SL", "SM", "SV", "BL", "BM", "BV"]
    return 0.5 * t.SV + 0.5 * t.BV


def read_cpi_inflation(path: Path) -> pd.Series:
    """Monthly CPI inflation from FRED's date,value CSV."""
    c = pd.read_csv(path)
    c.columns = ["d", "v"]
    c["d"] = pd.to_datetime(c.d) + pd.offsets.MonthEnd(0)
    return pd.to_numeric(c.set_index("d").v, errors="coerce").pct_change().dropna()


def read_century(path: Path) -> pd.DataFrame:
    """AQR Century of Factor Premia, monthly excess returns by column name."""
    raw = pd.read_excel(path, sheet_name=0, header=None)
    hdr = raw.index[raw[0] == "Date"][0]
    df = raw.iloc[hdr + 1 :].copy()
    df.columns = raw.iloc[hdr].tolist()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"]).set_index("Date")
    df.index = _month_end(df.index)
    return df.apply(pd.to_numeric, errors="coerce")


def trend_proxy(century: pd.DataFrame, lookback: int = 12) -> pd.Series:
    """Paper time-series momentum on AQR's equity, bond and commodity composites (excess return).

    Sign of the trailing `lookback`-month excess return, sized to 10% vol by trailing 36-month
    vol, equal-weighted, signal lagged one month. Gross of costs; three composites rather than
    dozens of markets, so it is a proxy, not a fund record.
    """
    cols = ("Equity indices Market", "Fixed income Market", "Commodities Market")
    legs = []
    for c in cols:
        r = century[c]
        sign = np.sign(r.rolling(lookback).sum())
        vol = r.rolling(36, min_periods=12).std()
        legs.append((sign * (0.10 / 12**0.5) / vol).shift(1) * r)
    return pd.concat(legs, axis=1).mean(axis=1, skipna=False).dropna()


def to_real(r: pd.Series, infl: pd.Series) -> pd.Series:
    """Nominal monthly return to real."""
    return ((1 + r) / (1 + infl.reindex(r.index)) - 1).dropna()


def build_sources(
    data_dir: Path, wanted: set[str], base_dir: Path | None = None
) -> dict[str, pd.Series]:
    """Real monthly return series for each named source in `wanted`.

    Built-in names: market, value, bills, trend_proxy. Anything of the form
    `csv:<path>:<column>` is read from the user's CSV (a date column first, nominal decimal
    returns; month-end dates).

    Raises:
        FileNotFoundError: A needed data file is missing (run `ips-engine fetch`).
        KeyError: An unknown source name.
    """
    infl = read_cpi_inflation(data_dir / "CPIAUCNS.csv")
    out: dict[str, pd.Series] = {}
    mkt: pd.Series | None = None
    rf: pd.Series | None = None
    for name in wanted:
        if name in ("market", "bills", "trend_proxy"):
            if mkt is None:
                mkt, rf = read_market(data_dir / "F-F_Research_Data_Factors.csv")
        if name == "market":
            out[name] = to_real(mkt, infl)
        elif name == "bills":
            out[name] = to_real(rf, infl)
        elif name == "value":
            out[name] = to_real(read_value(data_dir / "6_Portfolios_2x3.csv"), infl)
        elif name == "trend_proxy":
            tp = trend_proxy(read_century(data_dir / "Century-of-Factor-Premia-Monthly.xlsx"))
            out[name] = to_real(tp + rf.reindex(tp.index), infl)
        elif name.startswith("csv:"):
            _, path, col = name.split(":", 2)
            fp = Path(path)
            if not fp.is_absolute() and base_dir is not None:
                fp = base_dir / fp
            df = pd.read_csv(fp, index_col=0, parse_dates=True)
            s = pd.to_numeric(df[col], errors="coerce").dropna()
            s.index = _month_end(s.index)
            out[name] = to_real(s, infl)
        else:
            raise KeyError(f"unknown source {name!r}")
    return out
