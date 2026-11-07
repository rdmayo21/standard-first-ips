"""Apply Robin's combining rule to engine CSVs (one CSV per seed), and summarize.

Rule (Robin, 2026-11-07): pick the simplest mix that is inside the tie band in at least 75% of
the cells at every k; if none clears that, 100 stocks. Candidates are taken in config order
(simplest first). Also prints, per candidate and k, tie-band counts per seed, and the
never-reaches-FI share and run-out range across cells.

Usage:
    python3 combine_v2.py TIE_YEARS FALLBACK CSV [CSV ...]
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path


def _read(p: Path) -> list[dict[str, str]]:
    with p.open() as fh:
        return list(csv.DictReader(fh))


def pick(rows: list[dict[str, str]], tie: float, fallback: str) -> tuple[str, dict]:
    """Return (pick, counts) where counts[candidate][k] = (in-band cells, total cells)."""
    ks = [c[5:] for c in rows[0] if c.startswith("gap_k")]
    names = list(dict.fromkeys(r["candidate"] for r in rows))
    cells = {(r["sample"], r["scenario"]) for r in rows}
    counts = {
        n: {k: sum(float(r[f"gap_k{k}"]) <= tie + 1e-9 for r in rows if r["candidate"] == n)
            for k in ks}
        for n in names
    }
    for n in names:
        if all(counts[n][k] >= 0.75 * len(cells) for k in ks):
            return n, {"counts": counts, "cells": len(cells), "ks": ks}
    return fallback, {"counts": counts, "cells": len(cells), "ks": ks}


def main(tie: float, fallback: str, paths: list[Path]) -> None:
    """Print one block per CSV and a stability line."""
    picks = []
    for p in paths:
        rows = _read(p)
        name, info = pick(rows, tie, fallback)
        picks.append(name)
        print(f"\n### {p.name}: rule pick = {name}")
        print("| candidate | " + " | ".join(f"in band k={k}" for k in info["ks"])
              + " | never reaches FI by 85 (range over cells) | run-out (range) |")
        print("|---|" + "---|" * (len(info["ks"]) + 2))
        for n, c in info["counts"].items():
            mine = [r for r in rows if r["candidate"] == n]
            nev = [float(r["never_by_cap"]) for r in mine]
            ro = [float(r["runout"]) for r in mine if r["runout"]]
            print(f"| {n} | " + " | ".join(f"{c[k]}/{info['cells']}" for k in info["ks"])
                  + f" | {min(nev):.1%}-{max(nev):.1%} | {min(ro):.1%}-{max(ro):.1%} |")
    print(f"\nPicks across the {len(paths)} files: {picks}. Stable: {len(set(picks)) == 1}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
    main(float(sys.argv[1]), sys.argv[2], [Path(a) for a in sys.argv[3:]])
