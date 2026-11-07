"""Turn FI months into the user's score and pick the winner under the tie rule."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .config import Person
from .policy import NEVER, RunResult


def fi_ages(res: RunResult, p: Person) -> np.ndarray:
    """FI age per path, censored at cap_age."""
    return np.minimum(
        np.where(res.fi_month < NEVER, p.age + res.fi_month / 12, p.cap_age), p.cap_age
    )


def score(ages: np.ndarray, ks: tuple[float, ...]) -> np.ndarray:
    """S = median FI age + k x 90th-percentile FI age, one value per k. Lower is better."""
    med, p90 = np.median(ages), np.percentile(ages, 90)
    return np.array([med + k * p90 for k in ks])


@dataclass(frozen=True)
class CellRow:
    name: str
    median: float
    p90: float
    s: np.ndarray  # per k
    gap: np.ndarray  # S - best S, per k (0 = best)
    gap_se: np.ndarray  # paired batch SE of the gap
    tie: np.ndarray  # bool per k: within tie_years of the best
    censored: float  # share never reaching FI by cap_age
    runout: float | None  # share of quits that run out before horizon_age (None: no quits)
    quits: int  # paths that reached FI and quit
    turnover: float


def cell(
    results: list[RunResult],
    names: list[str],
    p: Person,
    ks: tuple[float, ...],
    tie_years: float,
    batches: int,
) -> list[CellRow]:
    """Score every candidate in one cell (same paths)."""
    ages = [fi_ages(r, p) for r in results]
    s_all = np.stack([score(a, ks) for a in ages])
    best = s_all.min(axis=0)
    ib = s_all.argmin(axis=0)
    n = len(ages[0])
    parts = np.array_split(np.arange(n), batches)
    s_b = np.stack([np.stack([score(a[ix], ks) for ix in parts]) for a in ages])  # (c, b, k)
    rows = []
    for j, r in enumerate(results):
        gse = np.array(
            [
                (s_b[j, :, q] - s_b[ib[q], :, q]).std(ddof=1) / np.sqrt(batches)
                for q in range(len(ks))
            ]
        )
        reached = r.fi_month < NEVER
        ruined = reached & (r.ruin_month < NEVER)
        rows.append(
            CellRow(
                name=names[j],
                median=float(np.median(ages[j])),
                p90=float(np.percentile(ages[j], 90)),
                s=s_all[j],
                gap=s_all[j] - best,
                gap_se=gse,
                tie=(s_all[j] - best) <= tie_years,
                censored=float((~reached).mean()),
                runout=float(ruined.sum() / reached.sum()) if reached.any() else None,
                quits=int(reached.sum()),
                turnover=float(r.turnover.mean()),
            )
        )
    return rows


def simplest_tie(rows: list[CellRow], q: int) -> str:
    """The first candidate (config order = simplest first) inside the tie band at k index q."""
    return next(r.name for r in rows if r.tie[q])


def lowest_runout_tie(rows: list[CellRow], q: int) -> CellRow | None:
    """The tie-band member with the lowest run-out at k index q (None if no quits)."""
    tied = [r for r in rows if r.tie[q] and r.runout is not None]
    return min(tied, key=lambda r: r.runout) if tied else None
