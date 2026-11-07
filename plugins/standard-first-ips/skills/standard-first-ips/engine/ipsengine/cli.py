"""Command line: `ips-engine fetch` and `ips-engine score CONFIG`."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import pandas as pd

from . import data, paths, policy, score
from .config import Config, load


def _pct(x: float | None) -> str:
    return "n/a (no quits)" if x is None else f"{x:.1%}"


def _samples(cfg: Config) -> dict[str, pd.DataFrame]:
    srcs = data.build_sources(cfg.data_dir, {s.source for s in cfg.sleeves.values()}, cfg.base_dir)
    joint = pd.concat({name: srcs[s.source] for name, s in cfg.sleeves.items()}, axis=1).dropna()
    out = {}
    for a, b in cfg.model.samples:
        df = joint.loc[a:b]
        if df.empty:
            raise ValueError(f"sample {a}:{b} has no months where every sleeve has data")
        out[f"{df.index[0]:%Y-%m}..{df.index[-1]:%Y-%m}"] = df
    return out


def run_score(cfg: Config) -> tuple[list[list[str]], list[str]]:
    """Score every candidate in every (sample x scenario) cell.

    Returns:
        CSV rows and printable summary lines.
    """
    sleeves = list(cfg.sleeves.values())
    names = [s.name for s in sleeves]
    _, tot = policy.months_for(cfg.person)
    ks = cfg.model.k
    rows: list[list[str]] = []
    lines: list[str] = []
    tie_count = {c.name: [0] * len(ks) for c in cfg.candidates}
    picks: dict[str, list[int]] = {c.name: [0] * len(ks) for c in cfg.candidates}
    n_cells = 0
    for sname, df in _samples(cfg).items():
        for sc in cfg.scenarios:
            n_cells += 1
            rets = paths.make_paths(
                df,
                sleeves,
                sc.centers,
                cfg.model.center_corr,
                cfg.model.paths,
                tot,
                cfg.model.seed,
                cfg.model.block_months,
            )
            res = [policy.run(rets, names, c, cfg.person) for c in cfg.candidates]
            cell = score.cell(
                res,
                [c.name for c in cfg.candidates],
                cfg.person,
                ks,
                cfg.model.tie_years,
                cfg.model.batches,
            )
            lines.append(f"\n## sample {sname}, scenario {sc.name}")
            lines.append(
                "| candidate | median FI | p90 FI | "
                + " | ".join(f"gap k={k:.2f} (SE)" for k in ks)
                + " | never by cap | quits | run out before horizon | turnover/yr |"
            )
            lines.append("|" + "---|" * (7 + len(ks)))
            for r in cell:
                lines.append(
                    f"| {r.name} | {r.median:.1f} | {r.p90:.1f} | "
                    + " | ".join(
                        f"{g:+.2f} ({e:.2f}){' tie' if t else ''}"
                        for g, e, t in zip(r.gap, r.gap_se, r.tie)
                    )
                    + f" | {r.censored:.1%} | {r.quits} | {_pct(r.runout)} | {r.turnover:.1%} |"
                )
                for q in range(len(ks)):
                    tie_count[r.name][q] += int(r.tie[q])
                rows.append(
                    [sname, sc.name, r.name, f"{r.median:.3f}", f"{r.p90:.3f}"]
                    + [f"{x:.3f}" for x in r.s]
                    + [f"{x:.3f}" for x in r.gap]
                    + [f"{x:.3f}" for x in r.gap_se]
                    + [
                        f"{r.censored:.4f}",
                        str(r.quits),
                        "" if r.runout is None else f"{r.runout:.4f}",
                        f"{r.turnover:.4f}",
                    ]
                )
            for q in range(len(ks)):
                picks[score.simplest_tie(cell, q)][q] += 1
            lines.append(
                "Simplest within the tie band: "
                + ", ".join(f"k={k:.2f}: {score.simplest_tie(cell, q)}" for q, k in enumerate(ks))
            )
            low = []
            for q, k in enumerate(ks):
                lr = score.lowest_runout_tie(cell, q)
                low.append(f"k={k:.2f}: {lr.name} ({_pct(lr.runout)})" if lr else f"k={k:.2f}: n/a")
            lines.append(
                "Lowest run-out within the tie band: "
                + ", ".join(low)
                + ". The simplest pick ignores run-out; if your goal includes staying quit,"
                " compare both before accepting it."
            )
    lines.append(f"\n## Summary over {n_cells} cells (candidates listed simplest first)")
    lines.append(
        "| candidate | "
        + " | ".join(f"in tie band k={k:.2f}" for k in ks)
        + " | "
        + " | ".join(f"simplest pick k={k:.2f}" for k in ks)
        + " |"
    )
    lines.append("|" + "---|" * (1 + 2 * len(ks)))
    for c in cfg.candidates:
        lines.append(
            f"| {c.name} | "
            + " | ".join(f"{x}/{n_cells}" for x in tie_count[c.name])
            + " | "
            + " | ".join(f"{x}/{n_cells}" for x in picks[c.name])
            + " |"
        )
    return rows, lines


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(prog="ips-engine", description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch", help="download the public data")
    f.add_argument("--data", type=Path, default=Path("data"))
    f.add_argument("--force", action="store_true")
    s = sub.add_parser("score", help="score the candidates in a config")
    s.add_argument("config", type=Path)
    s.add_argument("--out", type=Path, default=None, help="CSV of every cell row")
    a = ap.parse_args(argv)
    if a.cmd == "fetch":
        lines = data.fetch(a.data, a.force)
        print("\n".join(lines))
        if any(x.startswith("FAILED") for x in lines):
            sys.exit(1)
        return
    try:
        cfg = load(a.config)
        rows, lines = run_score(cfg)
    except (FileNotFoundError, KeyError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)
    print("\n".join(lines))
    if a.out:
        ks = cfg.model.k
        head = (
            ["sample", "scenario", "candidate", "median", "p90"]
            + [f"S_k{k:.2f}" for k in ks]
            + [f"gap_k{k:.2f}" for k in ks]
            + [f"gap_se_k{k:.2f}" for k in ks]
            + ["never_by_cap", "quits", "runout", "turnover"]
        )
        with a.out.open("w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(head)
            w.writerows(rows)


if __name__ == "__main__":
    main()
