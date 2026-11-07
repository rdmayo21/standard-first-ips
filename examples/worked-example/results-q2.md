# Q2 engine output: quit-day switch (Robin, fictional)

Generated 2026-11-07 by `uv run --project <repo>/plugins/standard-first-ips/skills/standard-first-ips/engine ips-engine score config-q2.toml --out results-q2.csv`, run in this folder. Inputs identical to config-q1.toml. Not investment advice.

# Part A: main run, config-q2.toml

## sample 1927-07..2026-02, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.6 | 73.6 | +1.75 (0.13) | +2.33 (0.17) | +2.92 (0.22) | 8.5% | 7318 | 12.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.6 | 73.6 | +1.75 (0.13) | +2.33 (0.17) | +2.92 (0.22) | 8.5% | 7318 | 9.2% | 0.0% |
| 100 stocks, 15% to trend at quit | 60.6 | 73.6 | +1.75 (0.13) | +2.33 (0.17) | +2.92 (0.22) | 8.5% | 7318 | 7.8% | 0.0% |
| 70/30 market/value, keep | 60.0 | 71.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 5.9% | 7526 | 10.7% | 0.4% |
| 70/30, 20% to bills at quit | 60.0 | 71.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 5.9% | 7526 | 7.6% | 0.4% |
| 70/30, 15% to trend at quit | 60.0 | 71.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 5.9% | 7526 | 6.4% | 0.4% |
Simplest within the tie band: k=0.50: 70/30 market/value, keep, k=0.75: 70/30 market/value, keep, k=1.00: 70/30 market/value, keep
Lowest run-out within the tie band: k=0.50: 70/30, 15% to trend at quit (6.4%), k=0.75: 70/30, 15% to trend at quit (6.4%), k=1.00: 70/30, 15% to trend at quit (6.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-02, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 75.0 | +0.50 (0.10) tie | +0.50 (0.10) tie | +0.50 (0.10) tie | 17.4% | 6610 | 20.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 75.0 | +0.50 (0.10) tie | +0.50 (0.10) tie | +0.50 (0.10) tie | 17.4% | 6610 | 15.2% | 0.0% |
| 100 stocks, 15% to trend at quit | 63.2 | 75.0 | +0.50 (0.10) tie | +0.50 (0.10) tie | +0.50 (0.10) tie | 17.4% | 6610 | 13.4% | 0.0% |
| 70/30 market/value, keep | 62.8 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 13.9% | 6891 | 17.8% | 0.4% |
| 70/30, 20% to bills at quit | 62.8 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 13.9% | 6891 | 13.1% | 0.4% |
| 70/30, 15% to trend at quit | 62.8 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 13.9% | 6891 | 11.6% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 15% to trend at quit (11.6%), k=0.75: 70/30, 15% to trend at quit (11.6%), k=1.00: 70/30, 15% to trend at quit (11.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-02, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.6 | 73.6 | +1.25 (0.12) | +1.71 (0.16) | +2.17 (0.20) | 8.5% | 7318 | 12.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.6 | 73.6 | +1.25 (0.12) | +1.71 (0.16) | +2.17 (0.20) | 8.5% | 7318 | 9.2% | 0.0% |
| 100 stocks, 15% to trend at quit | 60.6 | 73.6 | +1.25 (0.12) | +1.71 (0.16) | +2.17 (0.20) | 8.5% | 7318 | 7.8% | 0.0% |
| 70/30 market/value, keep | 60.2 | 71.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7477 | 11.3% | 0.4% |
| 70/30, 20% to bills at quit | 60.2 | 71.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7477 | 8.3% | 0.4% |
| 70/30, 15% to trend at quit | 60.2 | 71.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7477 | 6.8% | 0.4% |
Simplest within the tie band: k=0.50: 70/30 market/value, keep, k=0.75: 70/30 market/value, keep, k=1.00: 70/30 market/value, keep
Lowest run-out within the tie band: k=0.50: 70/30, 15% to trend at quit (6.8%), k=0.75: 70/30, 15% to trend at quit (6.8%), k=1.00: 70/30, 15% to trend at quit (6.8%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-02, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 75.0 | +0.25 (0.09) tie | +0.25 (0.09) tie | +0.25 (0.09) tie | 17.4% | 6610 | 20.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 75.0 | +0.25 (0.09) tie | +0.25 (0.09) tie | +0.25 (0.09) tie | 17.4% | 6610 | 15.2% | 0.0% |
| 100 stocks, 15% to trend at quit | 63.2 | 75.0 | +0.25 (0.09) tie | +0.25 (0.09) tie | +0.25 (0.09) tie | 17.4% | 6610 | 13.4% | 0.0% |
| 70/30 market/value, keep | 63.0 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 14.8% | 6814 | 18.7% | 0.4% |
| 70/30, 20% to bills at quit | 63.0 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 14.8% | 6814 | 14.2% | 0.4% |
| 70/30, 15% to trend at quit | 63.0 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 14.8% | 6814 | 12.3% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 15% to trend at quit (12.3%), k=0.75: 70/30, 15% to trend at quit (12.3%), k=1.00: 70/30, 15% to trend at quit (12.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.1 | 73.8 | +1.37 (0.15) | +1.94 (0.22) | +2.50 (0.28) | 8.6% | 7310 | 13.6% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.1 | 73.8 | +1.37 (0.15) | +1.94 (0.22) | +2.50 (0.28) | 8.6% | 7310 | 11.0% | 0.0% |
| 100 stocks, 15% to trend at quit | 60.1 | 73.8 | +1.37 (0.15) | +1.94 (0.22) | +2.50 (0.28) | 8.6% | 7310 | 9.5% | 0.0% |
| 70/30 market/value, keep | 59.8 | 71.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.3% | 7496 | 10.2% | 0.7% |
| 70/30, 20% to bills at quit | 59.8 | 71.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.3% | 7496 | 7.9% | 0.7% |
| 70/30, 15% to trend at quit | 59.8 | 71.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.3% | 7496 | 6.5% | 0.7% |
Simplest within the tie band: k=0.50: 70/30 market/value, keep, k=0.75: 70/30 market/value, keep, k=1.00: 70/30 market/value, keep
Lowest run-out within the tie band: k=0.50: 70/30, 15% to trend at quit (6.5%), k=0.75: 70/30, 15% to trend at quit (6.5%), k=1.00: 70/30, 15% to trend at quit (6.5%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.0 | 75.0 | +0.63 (0.06) tie | +0.63 (0.06) tie | +0.63 (0.06) tie | 17.2% | 6626 | 20.6% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.0 | 75.0 | +0.63 (0.06) tie | +0.63 (0.06) tie | +0.63 (0.06) tie | 17.2% | 6626 | 16.5% | 0.0% |
| 100 stocks, 15% to trend at quit | 63.0 | 75.0 | +0.63 (0.06) tie | +0.63 (0.06) tie | +0.63 (0.06) tie | 17.2% | 6626 | 14.4% | 0.0% |
| 70/30 market/value, keep | 62.3 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 13.5% | 6923 | 17.1% | 0.7% |
| 70/30, 20% to bills at quit | 62.3 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 13.5% | 6923 | 13.6% | 0.7% |
| 70/30, 15% to trend at quit | 62.3 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 13.5% | 6923 | 11.4% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 15% to trend at quit (11.4%), k=0.75: 70/30, 15% to trend at quit (11.4%), k=1.00: 70/30, 15% to trend at quit (11.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.1 | 73.8 | +0.92 (0.14) tie | +1.33 (0.20) | +1.75 (0.26) | 8.6% | 7310 | 13.6% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.1 | 73.8 | +0.92 (0.14) tie | +1.33 (0.20) | +1.75 (0.26) | 8.6% | 7310 | 11.0% | 0.0% |
| 100 stocks, 15% to trend at quit | 60.1 | 73.8 | +0.92 (0.14) tie | +1.33 (0.20) | +1.75 (0.26) | 8.6% | 7310 | 9.5% | 0.0% |
| 70/30 market/value, keep | 60.0 | 72.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.8% | 7455 | 10.9% | 0.7% |
| 70/30, 20% to bills at quit | 60.0 | 72.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.8% | 7455 | 8.4% | 0.7% |
| 70/30, 15% to trend at quit | 60.0 | 72.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.8% | 7455 | 6.9% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30 market/value, keep, k=1.00: 70/30 market/value, keep
Lowest run-out within the tie band: k=0.50: 70/30, 15% to trend at quit (6.9%), k=0.75: 70/30, 15% to trend at quit (6.9%), k=1.00: 70/30, 15% to trend at quit (6.9%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.0 | 75.0 | +0.21 (0.06) tie | +0.21 (0.06) tie | +0.21 (0.06) tie | 17.2% | 6626 | 20.6% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.0 | 75.0 | +0.21 (0.06) tie | +0.21 (0.06) tie | +0.21 (0.06) tie | 17.2% | 6626 | 16.5% | 0.0% |
| 100 stocks, 15% to trend at quit | 63.0 | 75.0 | +0.21 (0.06) tie | +0.21 (0.06) tie | +0.21 (0.06) tie | 17.2% | 6626 | 14.4% | 0.0% |
| 70/30 market/value, keep | 62.8 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 14.5% | 6843 | 17.9% | 0.7% |
| 70/30, 20% to bills at quit | 62.8 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 14.5% | 6843 | 14.0% | 0.7% |
| 70/30, 15% to trend at quit | 62.8 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 14.5% | 6843 | 12.3% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 15% to trend at quit (12.3%), k=0.75: 70/30, 15% to trend at quit (12.3%), k=1.00: 70/30, 15% to trend at quit (12.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks, keep | 5/8 | 4/8 | 4/8 | 5/8 | 4/8 | 4/8 |
| 100 stocks, 20% to bills at quit | 5/8 | 4/8 | 4/8 | 0/8 | 0/8 | 0/8 |
| 100 stocks, 15% to trend at quit | 5/8 | 4/8 | 4/8 | 0/8 | 0/8 | 0/8 |
| 70/30 market/value, keep | 8/8 | 8/8 | 8/8 | 3/8 | 4/8 | 4/8 |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 0/8 | 0/8 | 0/8 |
| 70/30, 15% to trend at quit | 8/8 | 8/8 | 8/8 | 0/8 | 0/8 | 0/8 |

# Part B: paired differences vs each base mix kept (runout_paired.py config-q2.toml "<base>, keep"). Read only rows of the same base mix; cross-mix rows mix Q1 into Q2.

## sample 1927-07..2026-02, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.22% | -2.86% (0.17%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 7.84% | -4.24% (0.24%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 10.72% | -1.36% (0.31%) | -0.58 | -2.33 |
| 70/30, 20% to bills at quit | 7.63% | -4.45% (0.27%) | -0.58 | -2.33 |
| 70/30, 15% to trend at quit | 6.35% | -5.73% (0.30%) | -0.58 | -2.33 |

## sample 1927-07..2026-02, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.23% | -4.84% (0.31%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 13.45% | -6.63% (0.33%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 17.79% | -2.28% (0.37%) | -0.50 | +0.00 |
| 70/30, 20% to bills at quit | 13.13% | -6.94% (0.46%) | -0.50 | +0.00 |
| 70/30, 15% to trend at quit | 11.62% | -8.45% (0.43%) | -0.50 | +0.00 |

## sample 1927-07..2026-02, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.22% | -2.86% (0.17%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 7.84% | -4.24% (0.24%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 11.27% | -0.81% (0.35%) | -0.33 | -1.83 |
| 70/30, 20% to bills at quit | 8.25% | -3.83% (0.30%) | -0.33 | -1.83 |
| 70/30, 15% to trend at quit | 6.78% | -5.30% (0.29%) | -0.33 | -1.83 |

## sample 1927-07..2026-02, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.23% | -4.84% (0.31%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 13.45% | -6.63% (0.33%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 18.65% | -1.42% (0.33%) | -0.25 | +0.00 |
| 70/30, 20% to bills at quit | 14.18% | -5.90% (0.41%) | -0.25 | +0.00 |
| 70/30, 15% to trend at quit | 12.28% | -7.79% (0.44%) | -0.25 | +0.00 |

## sample 1990-01..2026-02, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.56% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 10.97% | -2.59% (0.16%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 9.49% | -4.06% (0.23%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 10.21% | -3.35% (0.49%) | -0.25 | -2.25 |
| 70/30, 20% to bills at quit | 7.90% | -5.66% (0.48%) | -0.25 | -2.25 |
| 70/30, 15% to trend at quit | 6.46% | -7.10% (0.45%) | -0.25 | -2.25 |

## sample 1990-01..2026-02, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.60% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 16.53% | -4.07% (0.16%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 14.37% | -6.23% (0.23%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 17.15% | -3.45% (0.38%) | -0.63 | +0.00 |
| 70/30, 20% to bills at quit | 13.56% | -7.04% (0.55%) | -0.63 | +0.00 |
| 70/30, 15% to trend at quit | 11.38% | -9.22% (0.50%) | -0.63 | +0.00 |

## sample 1990-01..2026-02, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.56% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 10.97% | -2.59% (0.16%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 9.49% | -4.06% (0.23%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 10.95% | -2.61% (0.43%) | -0.08 | -1.67 |
| 70/30, 20% to bills at quit | 8.36% | -5.20% (0.45%) | -0.08 | -1.67 |
| 70/30, 15% to trend at quit | 6.92% | -6.64% (0.45%) | -0.08 | -1.67 |

## sample 1990-01..2026-02, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.60% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 16.53% | -4.07% (0.16%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 14.37% | -6.23% (0.23%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 17.90% | -2.70% (0.37%) | -0.21 | +0.00 |
| 70/30, 20% to bills at quit | 13.97% | -6.63% (0.44%) | -0.21 | +0.00 |
| 70/30, 15% to trend at quit | 12.28% | -8.33% (0.50%) | -0.21 | +0.00 |

## sample 1927-07..2026-02, scenario base (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.08% | +1.36% (0.31%) | +0.58 | +2.33 |
| 100 stocks, 20% to bills at quit | 9.22% | -1.50% (0.32%) | +0.58 | +2.33 |
| 100 stocks, 15% to trend at quit | 7.84% | -2.88% (0.27%) | +0.58 | +2.33 |
| 70/30 market/value, keep | 10.72% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.63% | -3.10% (0.19%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 6.35% | -4.37% (0.28%) | +0.00 | +0.00 |

## sample 1927-07..2026-02, scenario stocks 3% (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.08% | +2.28% (0.37%) | +0.50 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.23% | -2.56% (0.40%) | +0.50 | +0.00 |
| 100 stocks, 15% to trend at quit | 13.45% | -4.34% (0.45%) | +0.50 | +0.00 |
| 70/30 market/value, keep | 17.79% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 13.13% | -4.66% (0.22%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 11.62% | -6.17% (0.31%) | +0.00 | +0.00 |

## sample 1927-07..2026-02, scenario no value premium (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.08% | +0.81% (0.35%) | +0.33 | +1.83 |
| 100 stocks, 20% to bills at quit | 9.22% | -2.05% (0.36%) | +0.33 | +1.83 |
| 100 stocks, 15% to trend at quit | 7.84% | -3.43% (0.29%) | +0.33 | +1.83 |
| 70/30 market/value, keep | 11.27% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.25% | -3.02% (0.16%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 6.78% | -4.49% (0.21%) | +0.00 | +0.00 |

## sample 1927-07..2026-02, scenario stocks 3% + no value premium (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.08% | +1.42% (0.33%) | +0.25 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.23% | -3.42% (0.40%) | +0.25 | +0.00 |
| 100 stocks, 15% to trend at quit | 13.45% | -5.20% (0.46%) | +0.25 | +0.00 |
| 70/30 market/value, keep | 18.65% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 14.18% | -4.48% (0.23%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 12.28% | -6.37% (0.41%) | +0.00 | +0.00 |

## sample 1990-01..2026-02, scenario base (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.56% | +3.35% (0.49%) | +0.25 | +2.25 |
| 100 stocks, 20% to bills at quit | 10.97% | +0.77% (0.41%) | +0.25 | +2.25 |
| 100 stocks, 15% to trend at quit | 9.49% | -0.71% (0.40%) | +0.25 | +2.25 |
| 70/30 market/value, keep | 10.21% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.90% | -2.31% (0.20%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 6.46% | -3.75% (0.22%) | +0.00 | +0.00 |

## sample 1990-01..2026-02, scenario stocks 3% (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.60% | +3.45% (0.38%) | +0.63 | +0.00 |
| 100 stocks, 20% to bills at quit | 16.53% | -0.62% (0.43%) | +0.63 | +0.00 |
| 100 stocks, 15% to trend at quit | 14.37% | -2.78% (0.34%) | +0.63 | +0.00 |
| 70/30 market/value, keep | 17.15% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 13.56% | -3.58% (0.32%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 11.38% | -5.76% (0.32%) | +0.00 | +0.00 |

## sample 1990-01..2026-02, scenario no value premium (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.56% | +2.61% (0.43%) | +0.08 | +1.67 |
| 100 stocks, 20% to bills at quit | 10.97% | +0.03% (0.35%) | +0.08 | +1.67 |
| 100 stocks, 15% to trend at quit | 9.49% | -1.45% (0.36%) | +0.08 | +1.67 |
| 70/30 market/value, keep | 10.95% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.36% | -2.59% (0.15%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 6.92% | -4.02% (0.22%) | +0.00 | +0.00 |

## sample 1990-01..2026-02, scenario stocks 3% + no value premium (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.60% | +2.70% (0.37%) | +0.21 | +0.00 |
| 100 stocks, 20% to bills at quit | 16.53% | -1.38% (0.40%) | +0.21 | +0.00 |
| 100 stocks, 15% to trend at quit | 14.37% | -3.53% (0.31%) | +0.21 | +0.00 |
| 70/30 market/value, keep | 17.90% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 13.97% | -3.93% (0.26%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 12.28% | -5.63% (0.30%) | +0.00 | +0.00 |

# Part C: trend switch vs bills switch, paired (baseline = the bills switch of the same base mix)

## sample 1927-07..2026-02, scenario base (baseline: 100 stocks, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.08% | +2.86% (0.17%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.22% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 7.84% | -1.38% (0.18%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 10.72% | +1.50% (0.32%) | -0.58 | -2.33 |
| 70/30, 20% to bills at quit | 7.63% | -1.60% (0.28%) | -0.58 | -2.33 |
| 70/30, 15% to trend at quit | 6.35% | -2.87% (0.29%) | -0.58 | -2.33 |

## sample 1927-07..2026-02, scenario stocks 3% (baseline: 100 stocks, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.08% | +4.84% (0.31%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.23% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 13.45% | -1.79% (0.19%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 17.79% | +2.56% (0.40%) | -0.50 | +0.00 |
| 70/30, 20% to bills at quit | 13.13% | -2.10% (0.40%) | -0.50 | +0.00 |
| 70/30, 15% to trend at quit | 11.62% | -3.61% (0.40%) | -0.50 | +0.00 |

## sample 1927-07..2026-02, scenario no value premium (baseline: 100 stocks, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.08% | +2.86% (0.17%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.22% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 7.84% | -1.38% (0.18%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 11.27% | +2.05% (0.36%) | -0.33 | -1.83 |
| 70/30, 20% to bills at quit | 8.25% | -0.97% (0.30%) | -0.33 | -1.83 |
| 70/30, 15% to trend at quit | 6.78% | -2.44% (0.29%) | -0.33 | -1.83 |

## sample 1927-07..2026-02, scenario stocks 3% + no value premium (baseline: 100 stocks, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.08% | +4.84% (0.31%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.23% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 13.45% | -1.79% (0.19%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 18.65% | +3.42% (0.40%) | -0.25 | +0.00 |
| 70/30, 20% to bills at quit | 14.18% | -1.06% (0.35%) | -0.25 | +0.00 |
| 70/30, 15% to trend at quit | 12.28% | -2.95% (0.39%) | -0.25 | +0.00 |

## sample 1990-01..2026-02, scenario base (baseline: 100 stocks, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.56% | +2.59% (0.16%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 10.97% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 9.49% | -1.48% (0.16%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 10.21% | -0.77% (0.41%) | -0.25 | -2.25 |
| 70/30, 20% to bills at quit | 7.90% | -3.07% (0.39%) | -0.25 | -2.25 |
| 70/30, 15% to trend at quit | 6.46% | -4.51% (0.37%) | -0.25 | -2.25 |

## sample 1990-01..2026-02, scenario stocks 3% (baseline: 100 stocks, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.60% | +4.07% (0.16%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 16.53% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 14.37% | -2.16% (0.20%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 17.15% | +0.62% (0.43%) | -0.63 | +0.00 |
| 70/30, 20% to bills at quit | 13.56% | -2.96% (0.59%) | -0.63 | +0.00 |
| 70/30, 15% to trend at quit | 11.38% | -5.14% (0.55%) | -0.63 | +0.00 |

## sample 1990-01..2026-02, scenario no value premium (baseline: 100 stocks, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.56% | +2.59% (0.16%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 10.97% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 9.49% | -1.48% (0.16%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 10.95% | -0.03% (0.35%) | -0.08 | -1.67 |
| 70/30, 20% to bills at quit | 8.36% | -2.61% (0.38%) | -0.08 | -1.67 |
| 70/30, 15% to trend at quit | 6.92% | -4.05% (0.38%) | -0.08 | -1.67 |

## sample 1990-01..2026-02, scenario stocks 3% + no value premium (baseline: 100 stocks, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.60% | +4.07% (0.16%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 16.53% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 14.37% | -2.16% (0.20%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 17.90% | +1.38% (0.40%) | -0.21 | +0.00 |
| 70/30, 20% to bills at quit | 13.97% | -2.56% (0.48%) | -0.21 | +0.00 |
| 70/30, 15% to trend at quit | 12.28% | -4.25% (0.54%) | -0.21 | +0.00 |

## sample 1927-07..2026-02, scenario base (baseline: 70/30, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.08% | +4.45% (0.27%) | +0.58 | +2.33 |
| 100 stocks, 20% to bills at quit | 9.22% | +1.60% (0.28%) | +0.58 | +2.33 |
| 100 stocks, 15% to trend at quit | 7.84% | +0.22% (0.29%) | +0.58 | +2.33 |
| 70/30 market/value, keep | 10.72% | +3.10% (0.19%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.63% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 6.35% | -1.28% (0.20%) | +0.00 | +0.00 |

## sample 1927-07..2026-02, scenario stocks 3% (baseline: 70/30, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.08% | +6.94% (0.46%) | +0.50 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.23% | +2.10% (0.40%) | +0.50 | +0.00 |
| 100 stocks, 15% to trend at quit | 13.45% | +0.32% (0.46%) | +0.50 | +0.00 |
| 70/30 market/value, keep | 17.79% | +4.66% (0.22%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 13.13% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 11.62% | -1.51% (0.23%) | +0.00 | +0.00 |

## sample 1927-07..2026-02, scenario no value premium (baseline: 70/30, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.08% | +3.83% (0.30%) | +0.33 | +1.83 |
| 100 stocks, 20% to bills at quit | 9.22% | +0.97% (0.30%) | +0.33 | +1.83 |
| 100 stocks, 15% to trend at quit | 7.84% | -0.41% (0.26%) | +0.33 | +1.83 |
| 70/30 market/value, keep | 11.27% | +3.02% (0.16%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.25% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 6.78% | -1.47% (0.17%) | +0.00 | +0.00 |

## sample 1927-07..2026-02, scenario stocks 3% + no value premium (baseline: 70/30, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.08% | +5.90% (0.41%) | +0.25 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.23% | +1.06% (0.35%) | +0.25 | +0.00 |
| 100 stocks, 15% to trend at quit | 13.45% | -0.73% (0.40%) | +0.25 | +0.00 |
| 70/30 market/value, keep | 18.65% | +4.48% (0.23%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 14.18% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 12.28% | -1.89% (0.29%) | +0.00 | +0.00 |

## sample 1990-01..2026-02, scenario base (baseline: 70/30, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.56% | +5.66% (0.48%) | +0.25 | +2.25 |
| 100 stocks, 20% to bills at quit | 10.97% | +3.07% (0.39%) | +0.25 | +2.25 |
| 100 stocks, 15% to trend at quit | 9.49% | +1.60% (0.37%) | +0.25 | +2.25 |
| 70/30 market/value, keep | 10.21% | +2.31% (0.20%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.90% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 6.46% | -1.44% (0.16%) | +0.00 | +0.00 |

## sample 1990-01..2026-02, scenario stocks 3% (baseline: 70/30, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.60% | +7.04% (0.55%) | +0.63 | +0.00 |
| 100 stocks, 20% to bills at quit | 16.53% | +2.96% (0.59%) | +0.63 | +0.00 |
| 100 stocks, 15% to trend at quit | 14.37% | +0.80% (0.49%) | +0.63 | +0.00 |
| 70/30 market/value, keep | 17.15% | +3.58% (0.32%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 13.56% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 11.38% | -2.18% (0.24%) | +0.00 | +0.00 |

## sample 1990-01..2026-02, scenario no value premium (baseline: 70/30, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.56% | +5.20% (0.45%) | +0.08 | +1.67 |
| 100 stocks, 20% to bills at quit | 10.97% | +2.61% (0.38%) | +0.08 | +1.67 |
| 100 stocks, 15% to trend at quit | 9.49% | +1.14% (0.37%) | +0.08 | +1.67 |
| 70/30 market/value, keep | 10.95% | +2.59% (0.15%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.36% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 6.92% | -1.44% (0.15%) | +0.00 | +0.00 |

## sample 1990-01..2026-02, scenario stocks 3% + no value premium (baseline: 70/30, 20% to bills at quit)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.60% | +6.63% (0.44%) | +0.21 | +0.00 |
| 100 stocks, 20% to bills at quit | 16.53% | +2.56% (0.48%) | +0.21 | +0.00 |
| 100 stocks, 15% to trend at quit | 14.37% | +0.40% (0.38%) | +0.21 | +0.00 |
| 70/30 market/value, keep | 17.90% | +3.93% (0.26%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 13.97% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 12.28% | -1.70% (0.16%) | +0.00 | +0.00 |

# Part D: S2 trend vol 0.12 applied to Q2 (run after seeing Part A; input pre-declared for Q1). config-q2-s2-trendvol.toml

## sample 1927-07..2026-02, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.22% | -2.86% (0.17%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 7.02% | -5.06% (0.26%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 10.72% | -1.36% (0.31%) | -0.58 | -2.33 |
| 70/30, 20% to bills at quit | 7.63% | -4.45% (0.27%) | -0.58 | -2.33 |
| 70/30, 15% to trend at quit | 5.81% | -6.27% (0.27%) | -0.58 | -2.33 |

## sample 1927-07..2026-02, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.23% | -4.84% (0.31%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 12.54% | -7.53% (0.30%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 17.79% | -2.28% (0.37%) | -0.50 | +0.00 |
| 70/30, 20% to bills at quit | 13.13% | -6.94% (0.46%) | -0.50 | +0.00 |
| 70/30, 15% to trend at quit | 11.13% | -8.95% (0.38%) | -0.50 | +0.00 |

## sample 1927-07..2026-02, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.22% | -2.86% (0.17%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 7.02% | -5.06% (0.26%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 11.27% | -0.81% (0.35%) | -0.33 | -1.83 |
| 70/30, 20% to bills at quit | 8.25% | -3.83% (0.30%) | -0.33 | -1.83 |
| 70/30, 15% to trend at quit | 6.31% | -5.77% (0.35%) | -0.33 | -1.83 |

## sample 1927-07..2026-02, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.23% | -4.84% (0.31%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 12.54% | -7.53% (0.30%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 18.65% | -1.42% (0.33%) | -0.25 | +0.00 |
| 70/30, 20% to bills at quit | 14.18% | -5.90% (0.41%) | -0.25 | +0.00 |
| 70/30, 15% to trend at quit | 11.70% | -8.38% (0.41%) | -0.25 | +0.00 |

## sample 1990-01..2026-02, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.56% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 10.97% | -2.59% (0.16%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 8.76% | -4.80% (0.24%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 10.21% | -3.35% (0.49%) | -0.25 | -2.25 |
| 70/30, 20% to bills at quit | 7.90% | -5.66% (0.48%) | -0.25 | -2.25 |
| 70/30, 15% to trend at quit | 6.18% | -7.38% (0.49%) | -0.25 | -2.25 |

## sample 1990-01..2026-02, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.60% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 16.53% | -4.07% (0.16%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 13.93% | -6.67% (0.27%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 17.15% | -3.45% (0.38%) | -0.63 | +0.00 |
| 70/30, 20% to bills at quit | 13.56% | -7.04% (0.55%) | -0.63 | +0.00 |
| 70/30, 15% to trend at quit | 11.12% | -9.48% (0.56%) | -0.63 | +0.00 |

## sample 1990-01..2026-02, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.56% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 10.97% | -2.59% (0.16%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 8.76% | -4.80% (0.24%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 10.95% | -2.61% (0.43%) | -0.08 | -1.67 |
| 70/30, 20% to bills at quit | 8.36% | -5.20% (0.45%) | -0.08 | -1.67 |
| 70/30, 15% to trend at quit | 6.71% | -6.85% (0.42%) | -0.08 | -1.67 |

## sample 1990-01..2026-02, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.60% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 16.53% | -4.07% (0.16%) | +0.00 | +0.00 |
| 100 stocks, 15% to trend at quit | 13.93% | -6.67% (0.27%) | +0.00 | +0.00 |
| 70/30 market/value, keep | 17.90% | -2.70% (0.37%) | -0.21 | +0.00 |
| 70/30, 20% to bills at quit | 13.97% | -6.63% (0.44%) | -0.21 | +0.00 |
| 70/30, 15% to trend at quit | 11.72% | -8.88% (0.48%) | -0.21 | +0.00 |

## sample 1927-07..2026-02, scenario base (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.08% | +1.36% (0.31%) | +0.58 | +2.33 |
| 100 stocks, 20% to bills at quit | 9.22% | -1.50% (0.32%) | +0.58 | +2.33 |
| 100 stocks, 15% to trend at quit | 7.02% | -3.70% (0.31%) | +0.58 | +2.33 |
| 70/30 market/value, keep | 10.72% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.63% | -3.10% (0.19%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 5.81% | -4.92% (0.27%) | +0.00 | +0.00 |

## sample 1927-07..2026-02, scenario stocks 3% (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.08% | +2.28% (0.37%) | +0.50 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.23% | -2.56% (0.40%) | +0.50 | +0.00 |
| 100 stocks, 15% to trend at quit | 12.54% | -5.25% (0.45%) | +0.50 | +0.00 |
| 70/30 market/value, keep | 17.79% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 13.13% | -4.66% (0.22%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 11.13% | -6.66% (0.29%) | +0.00 | +0.00 |

## sample 1927-07..2026-02, scenario no value premium (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.08% | +0.81% (0.35%) | +0.33 | +1.83 |
| 100 stocks, 20% to bills at quit | 9.22% | -2.05% (0.36%) | +0.33 | +1.83 |
| 100 stocks, 15% to trend at quit | 7.02% | -4.25% (0.34%) | +0.33 | +1.83 |
| 70/30 market/value, keep | 11.27% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.25% | -3.02% (0.16%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 6.31% | -4.96% (0.25%) | +0.00 | +0.00 |

## sample 1927-07..2026-02, scenario stocks 3% + no value premium (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.08% | +1.42% (0.33%) | +0.25 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.23% | -3.42% (0.40%) | +0.25 | +0.00 |
| 100 stocks, 15% to trend at quit | 12.54% | -6.11% (0.47%) | +0.25 | +0.00 |
| 70/30 market/value, keep | 18.65% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 14.18% | -4.48% (0.23%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 11.70% | -6.96% (0.39%) | +0.00 | +0.00 |

## sample 1990-01..2026-02, scenario base (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.56% | +3.35% (0.49%) | +0.25 | +2.25 |
| 100 stocks, 20% to bills at quit | 10.97% | +0.77% (0.41%) | +0.25 | +2.25 |
| 100 stocks, 15% to trend at quit | 8.76% | -1.45% (0.38%) | +0.25 | +2.25 |
| 70/30 market/value, keep | 10.21% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.90% | -2.31% (0.20%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 6.18% | -4.03% (0.20%) | +0.00 | +0.00 |

## sample 1990-01..2026-02, scenario stocks 3% (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.60% | +3.45% (0.38%) | +0.63 | +0.00 |
| 100 stocks, 20% to bills at quit | 16.53% | -0.62% (0.43%) | +0.63 | +0.00 |
| 100 stocks, 15% to trend at quit | 13.93% | -3.22% (0.36%) | +0.63 | +0.00 |
| 70/30 market/value, keep | 17.15% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 13.56% | -3.58% (0.32%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 11.12% | -6.02% (0.33%) | +0.00 | +0.00 |

## sample 1990-01..2026-02, scenario no value premium (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.56% | +2.61% (0.43%) | +0.08 | +1.67 |
| 100 stocks, 20% to bills at quit | 10.97% | +0.03% (0.35%) | +0.08 | +1.67 |
| 100 stocks, 15% to trend at quit | 8.76% | -2.19% (0.34%) | +0.08 | +1.67 |
| 70/30 market/value, keep | 10.95% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.36% | -2.59% (0.15%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 6.71% | -4.24% (0.20%) | +0.00 | +0.00 |

## sample 1990-01..2026-02, scenario stocks 3% + no value premium (baseline: 70/30 market/value, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 20.60% | +2.70% (0.37%) | +0.21 | +0.00 |
| 100 stocks, 20% to bills at quit | 16.53% | -1.38% (0.40%) | +0.21 | +0.00 |
| 100 stocks, 15% to trend at quit | 13.93% | -3.97% (0.33%) | +0.21 | +0.00 |
| 70/30 market/value, keep | 17.90% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 13.97% | -3.93% (0.26%) | +0.00 | +0.00 |
| 70/30, 15% to trend at quit | 11.72% | -6.18% (0.32%) | +0.00 | +0.00 |
