"""Paired run-out and FI-age differences vs a baseline candidate, with batch SEs.

The engine reports run-out per candidate without an SE. This reuses the engine's own paths and
policy (same seed, same paired paths) and adds, per cell: run-out difference vs the baseline
(share of quitting paths), its paired batch SE (same 16 batches as the engine), and the
median / p90 FI-age differences. No engine code is changed.

Usage:
    uv run --project ENGINE python runout_paired.py CONFIG BASELINE_NAME
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

from ipsengine import paths, policy, score
from ipsengine.cli import _samples
from ipsengine.config import load


def _runout(res: policy.RunResult, ix: np.ndarray) -> float:
    reached = res.fi_month[ix] < policy.NEVER
    ruined = reached & (res.ruin_month[ix] < policy.NEVER)
    return float(ruined.sum() / max(reached.sum(), 1))


def main(cfg_path: Path, baseline: str) -> None:
    """Print one markdown table per cell."""
    cfg = load(cfg_path)
    sleeves = list(cfg.sleeves.values())
    names = [s.name for s in sleeves]
    _, tot = policy.months_for(cfg.person)
    for sname, df in _samples(cfg).items():
        for sc in cfg.scenarios:
            rets = paths.make_paths(
                df, sleeves, sc.centers, cfg.model.center_corr, cfg.model.paths, tot,
                cfg.model.seed, cfg.model.block_months,
            )
            res = {c.name: policy.run(rets, names, c, cfg.person) for c in cfg.candidates}
            parts = np.array_split(np.arange(cfg.model.paths), cfg.model.batches)
            b = res[baseline]
            ab = score.fi_ages(b, cfg.person)
            print(f"\n## sample {sname}, scenario {sc.name} (baseline: {baseline})")
            print("| candidate | run-out | run-out minus baseline (SE) | "
                  "median FI minus baseline | p90 FI minus baseline |")
            print("|---|---|---|---|---|")
            all_ix = np.arange(cfg.model.paths)
            for name, r in res.items():
                a = score.fi_ages(r, cfg.person)
                d = [_runout(r, ix) - _runout(b, ix) for ix in parts]
                se = float(np.std(d, ddof=1) / np.sqrt(len(parts)))
                diff = _runout(r, all_ix) - _runout(b, all_ix)
                print(f"| {name} | {_runout(r, all_ix):.2%} | {diff:+.2%} ({se:.2%}) | "
                      f"{np.median(a) - np.median(ab):+.2f} | "
                      f"{np.percentile(a, 90) - np.percentile(ab, 90):+.2f} |")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        sys.exit(1)
    main(Path(sys.argv[1]), sys.argv[2])
