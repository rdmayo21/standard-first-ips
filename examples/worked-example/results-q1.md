# Q1 engine output: accumulation mix (Robin, fictional)

Generated 2026-11-07 by `uv run --project <repo>/plugins/standard-first-ips/skills/standard-first-ips/engine ips-engine score <config> --out <csv>`, run in this folder. Inputs fixed before scoring (see config comments). Not investment advice.

# Part A: main run, config-q1.toml (CSV: results-q1.csv)

## sample 1927-07..2026-02, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.6 | 73.6 | +1.75 (0.13) | +2.33 (0.17) | +2.92 (0.22) | 8.5% | 7318 | 12.1% | 0.0% |
| 70/30 market/value | 60.0 | 71.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 5.9% | 7526 | 10.7% | 0.4% |
| 85/15 market/trend | 61.1 | 72.3 | +1.62 (0.15) | +1.90 (0.20) | +2.17 (0.25) | 6.9% | 7451 | 8.0% | 0.7% |
| 80/20 market/bills | 62.1 | 73.9 | +3.42 (0.15) | +4.08 (0.19) | +4.75 (0.22) | 8.8% | 7293 | 9.0% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.7%), k=0.75: 70/30 market/value (10.7%), k=1.00: 70/30 market/value (10.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-02, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 75.0 | +0.50 (0.10) tie | +0.50 (0.10) tie | +0.50 (0.10) tie | 17.4% | 6610 | 20.1% | 0.0% |
| 70/30 market/value | 62.8 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 13.9% | 6891 | 17.8% | 0.4% |
| 85/15 market/trend | 63.8 | 75.0 | +1.00 (0.09) tie | +1.00 (0.09) tie | +1.00 (0.09) tie | 15.2% | 6781 | 13.7% | 0.7% |
| 80/20 market/bills | 64.8 | 75.0 | +2.08 (0.09) | +2.08 (0.09) | +2.08 (0.09) | 18.1% | 6555 | 14.6% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (13.7%), k=0.75: 85/15 market/trend (13.7%), k=1.00: 85/15 market/trend (13.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-02, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.6 | 73.6 | +1.25 (0.12) | +1.71 (0.16) | +2.17 (0.20) | 8.5% | 7318 | 12.1% | 0.0% |
| 70/30 market/value | 60.2 | 71.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7477 | 11.3% | 0.4% |
| 85/15 market/trend | 61.1 | 72.3 | +1.12 (0.14) | +1.27 (0.18) | +1.42 (0.23) | 6.9% | 7451 | 8.0% | 0.7% |
| 80/20 market/bills | 62.1 | 73.9 | +2.92 (0.14) | +3.46 (0.18) | +4.00 (0.22) | 8.8% | 7293 | 9.0% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (11.3%), k=0.75: 70/30 market/value (11.3%), k=1.00: 70/30 market/value (11.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-02, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 75.0 | +0.25 (0.09) tie | +0.25 (0.09) tie | +0.25 (0.09) tie | 17.4% | 6610 | 20.1% | 0.0% |
| 70/30 market/value | 63.0 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 14.8% | 6814 | 18.7% | 0.4% |
| 85/15 market/trend | 63.8 | 75.0 | +0.75 (0.09) tie | +0.75 (0.09) tie | +0.75 (0.09) tie | 15.2% | 6781 | 13.7% | 0.7% |
| 80/20 market/bills | 64.8 | 75.0 | +1.83 (0.08) | +1.83 (0.08) | +1.83 (0.08) | 18.1% | 6555 | 14.6% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (13.7%), k=0.75: 85/15 market/trend (13.7%), k=1.00: 85/15 market/trend (13.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.1 | 73.8 | +1.37 (0.15) | +1.94 (0.22) | +2.50 (0.28) | 8.6% | 7310 | 13.6% | 0.0% |
| 70/30 market/value | 59.8 | 71.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.3% | 7496 | 10.2% | 0.7% |
| 85/15 market/trend | 60.8 | 72.3 | +1.33 (0.09) | +1.54 (0.14) | +1.75 (0.18) | 6.7% | 7466 | 9.8% | 0.7% |
| 80/20 market/bills | 61.8 | 74.3 | +3.42 (0.14) | +4.12 (0.20) | +4.83 (0.25) | 8.9% | 7286 | 10.6% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.2%), k=0.75: 70/30 market/value (10.2%), k=1.00: 70/30 market/value (10.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.0 | 75.0 | +0.63 (0.06) tie | +0.63 (0.06) tie | +0.63 (0.06) tie | 17.2% | 6626 | 20.6% | 0.0% |
| 70/30 market/value | 62.3 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 13.5% | 6923 | 17.1% | 0.7% |
| 85/15 market/trend | 63.2 | 75.0 | +0.92 (0.06) tie | +0.92 (0.06) tie | +0.92 (0.06) tie | 14.4% | 6847 | 14.7% | 0.7% |
| 80/20 market/bills | 64.5 | 75.0 | +2.17 (0.09) | +2.17 (0.09) | +2.17 (0.09) | 17.8% | 6574 | 16.3% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (14.7%), k=0.75: 85/15 market/trend (14.7%), k=1.00: 85/15 market/trend (14.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.1 | 73.8 | +0.92 (0.14) tie | +1.33 (0.20) | +1.75 (0.26) | 8.6% | 7310 | 13.6% | 0.0% |
| 70/30 market/value | 60.0 | 72.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.8% | 7455 | 10.9% | 0.7% |
| 85/15 market/trend | 60.8 | 72.3 | +0.88 (0.10) tie | +0.94 (0.15) tie | +1.00 (0.20) tie | 6.7% | 7466 | 9.8% | 0.7% |
| 80/20 market/bills | 61.8 | 74.3 | +2.96 (0.14) | +3.52 (0.19) | +4.08 (0.23) | 8.9% | 7286 | 10.6% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (9.8%), k=0.75: 85/15 market/trend (9.8%), k=1.00: 85/15 market/trend (9.8%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.0 | 75.0 | +0.21 (0.06) tie | +0.21 (0.06) tie | +0.21 (0.06) tie | 17.2% | 6626 | 20.6% | 0.0% |
| 70/30 market/value | 62.8 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 14.5% | 6843 | 17.9% | 0.7% |
| 85/15 market/trend | 63.2 | 75.0 | +0.50 (0.06) tie | +0.50 (0.06) tie | +0.50 (0.06) tie | 14.4% | 6847 | 14.7% | 0.7% |
| 80/20 market/bills | 64.5 | 75.0 | +1.75 (0.09) | +1.75 (0.09) | +1.75 (0.09) | 17.8% | 6574 | 16.3% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (14.7%), k=0.75: 85/15 market/trend (14.7%), k=1.00: 85/15 market/trend (14.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks | 5/8 | 4/8 | 4/8 | 5/8 | 4/8 | 4/8 |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 3/8 | 4/8 | 4/8 |
| 85/15 market/trend | 5/8 | 5/8 | 5/8 | 0/8 | 0/8 | 0/8 |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |

# Part B: paired run-out and FI-age differences vs 100 stocks (runout_paired.py config-q1.toml "100 stocks")

## sample 1927-07..2026-02, scenario base (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 12.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 10.72% | -1.36% (0.31%) | -0.58 | -2.33 |
| 85/15 market/trend | 8.01% | -4.07% (0.35%) | +0.50 | -1.25 |
| 80/20 market/bills | 9.02% | -3.06% (0.24%) | +1.50 | +0.33 |

## sample 1927-07..2026-02, scenario stocks 3% (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 20.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 17.79% | -2.28% (0.37%) | -0.50 | +0.00 |
| 85/15 market/trend | 13.69% | -6.39% (0.29%) | +0.50 | +0.00 |
| 80/20 market/bills | 14.61% | -5.46% (0.31%) | +1.58 | +0.00 |

## sample 1927-07..2026-02, scenario no value premium (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 12.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 11.27% | -0.81% (0.35%) | -0.33 | -1.83 |
| 85/15 market/trend | 8.01% | -4.07% (0.35%) | +0.50 | -1.25 |
| 80/20 market/bills | 9.02% | -3.06% (0.24%) | +1.50 | +0.33 |

## sample 1927-07..2026-02, scenario stocks 3% + no value premium (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 20.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 18.65% | -1.42% (0.33%) | -0.25 | +0.00 |
| 85/15 market/trend | 13.69% | -6.39% (0.29%) | +0.50 | +0.00 |
| 80/20 market/bills | 14.61% | -5.46% (0.31%) | +1.58 | +0.00 |

## sample 1990-01..2026-02, scenario base (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 13.56% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 10.21% | -3.35% (0.49%) | -0.25 | -2.25 |
| 85/15 market/trend | 9.75% | -3.81% (0.30%) | +0.67 | -1.42 |
| 80/20 market/bills | 10.61% | -2.95% (0.25%) | +1.75 | +0.58 |

## sample 1990-01..2026-02, scenario stocks 3% (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 20.60% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 17.15% | -3.45% (0.38%) | -0.63 | +0.00 |
| 85/15 market/trend | 14.74% | -5.86% (0.28%) | +0.29 | +0.00 |
| 80/20 market/bills | 16.31% | -4.29% (0.22%) | +1.54 | +0.00 |

## sample 1990-01..2026-02, scenario no value premium (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 13.56% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 10.95% | -2.61% (0.43%) | -0.08 | -1.67 |
| 85/15 market/trend | 9.75% | -3.81% (0.30%) | +0.67 | -1.42 |
| 80/20 market/bills | 10.61% | -2.95% (0.25%) | +1.75 | +0.58 |

## sample 1990-01..2026-02, scenario stocks 3% + no value premium (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 20.60% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 17.90% | -2.70% (0.37%) | -0.21 | +0.00 |
| 85/15 market/trend | 14.74% | -5.86% (0.28%) | +0.29 | +0.00 |
| 80/20 market/bills | 16.31% | -4.29% (0.22%) | +1.54 | +0.00 |

# Part C: pre-declared sensitivity S1, market/value centers correlated 0.8 (config-q1-s1-corr.toml)

## sample 1927-07..2026-02, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.6 | 73.6 | +1.21 (0.10) | +1.56 (0.13) | +1.92 (0.16) | 8.5% | 7318 | 12.1% | 0.0% |
| 70/30 market/value | 60.1 | 72.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.2% | 7420 | 11.1% | 0.4% |
| 85/15 market/trend | 61.1 | 72.3 | +1.08 (0.13) | +1.12 (0.16) | +1.17 (0.20) | 6.9% | 7451 | 8.0% | 0.7% |
| 80/20 market/bills | 62.1 | 73.9 | +2.88 (0.12) | +3.31 (0.14) | +3.75 (0.16) | 8.8% | 7293 | 9.0% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (11.1%), k=0.75: 70/30 market/value (11.1%), k=1.00: 70/30 market/value (11.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-02, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 75.0 | +0.50 (0.09) tie | +0.50 (0.09) tie | +0.50 (0.09) tie | 17.4% | 6610 | 20.1% | 0.0% |
| 70/30 market/value | 62.8 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 15.6% | 6756 | 17.4% | 0.4% |
| 85/15 market/trend | 63.8 | 75.0 | +1.00 (0.09) tie | +1.00 (0.09) tie | +1.00 (0.09) tie | 15.2% | 6781 | 13.7% | 0.7% |
| 80/20 market/bills | 64.8 | 75.0 | +2.08 (0.10) | +2.08 (0.10) | +2.08 (0.10) | 18.1% | 6555 | 14.6% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (13.7%), k=0.75: 85/15 market/trend (13.7%), k=1.00: 85/15 market/trend (13.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-02, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.6 | 73.6 | +0.67 (0.09) tie | +0.88 (0.12) tie | +1.08 (0.15) | 8.5% | 7318 | 12.1% | 0.0% |
| 70/30 market/value | 60.3 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.8% | 7373 | 11.7% | 0.4% |
| 85/15 market/trend | 61.1 | 72.3 | +0.54 (0.11) tie | +0.44 (0.14) tie | +0.33 (0.16) tie | 6.9% | 7451 | 8.0% | 0.7% |
| 80/20 market/bills | 62.1 | 73.9 | +2.33 (0.09) | +2.62 (0.11) | +2.92 (0.13) | 8.8% | 7293 | 9.0% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (8.0%), k=0.75: 85/15 market/trend (8.0%), k=1.00: 85/15 market/trend (8.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-02, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 75.0 | +0.17 (0.09) tie | +0.17 (0.09) tie | +0.17 (0.09) tie | 17.4% | 6610 | 20.1% | 0.0% |
| 70/30 market/value | 63.1 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 16.8% | 6654 | 18.2% | 0.4% |
| 85/15 market/trend | 63.8 | 75.0 | +0.67 (0.10) tie | +0.67 (0.10) tie | +0.67 (0.10) tie | 15.2% | 6781 | 13.7% | 0.7% |
| 80/20 market/bills | 64.8 | 75.0 | +1.75 (0.09) | +1.75 (0.09) | +1.75 (0.09) | 18.1% | 6555 | 14.6% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (13.7%), k=0.75: 85/15 market/trend (13.7%), k=1.00: 85/15 market/trend (13.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.1 | 73.8 | +0.75 (0.12) tie | +1.00 (0.17) tie | +1.25 (0.21) | 8.6% | 7310 | 13.6% | 0.0% |
| 70/30 market/value | 59.8 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.7% | 7387 | 10.8% | 0.7% |
| 85/15 market/trend | 60.8 | 72.3 | +0.71 (0.10) tie | +0.60 (0.14) tie | +0.50 (0.19) tie | 6.7% | 7466 | 9.8% | 0.7% |
| 80/20 market/bills | 61.8 | 74.3 | +2.79 (0.11) | +3.19 (0.15) | +3.58 (0.20) | 8.9% | 7286 | 10.6% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (9.8%), k=0.75: 85/15 market/trend (9.8%), k=1.00: 85/15 market/trend (9.8%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.0 | 75.0 | +0.46 (0.06) tie | +0.46 (0.06) tie | +0.46 (0.06) tie | 17.2% | 6626 | 20.6% | 0.0% |
| 70/30 market/value | 62.5 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 15.3% | 6774 | 17.3% | 0.7% |
| 85/15 market/trend | 63.2 | 75.0 | +0.75 (0.06) tie | +0.75 (0.06) tie | +0.75 (0.06) tie | 14.4% | 6847 | 14.7% | 0.7% |
| 80/20 market/bills | 64.5 | 75.0 | +2.00 (0.09) | +2.00 (0.09) | +2.00 (0.09) | 17.8% | 6574 | 16.3% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (14.7%), k=0.75: 85/15 market/trend (14.7%), k=1.00: 85/15 market/trend (14.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.1 | 73.8 | +0.25 (0.10) tie | +0.40 (0.16) tie | +0.75 (0.21) tie | 8.6% | 7310 | 13.6% | 0.0% |
| 70/30 market/value | 60.1 | 73.2 | +0.00 (0.00) tie | +0.02 (0.12) tie | +0.25 (0.16) tie | 8.3% | 7338 | 11.6% | 0.6% |
| 85/15 market/trend | 60.8 | 72.3 | +0.21 (0.09) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.7% | 7466 | 9.8% | 0.7% |
| 80/20 market/bills | 61.8 | 74.3 | +2.29 (0.09) | +2.58 (0.11) | +3.08 (0.13) | 8.9% | 7286 | 10.6% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (9.8%), k=0.75: 85/15 market/trend (9.8%), k=1.00: 85/15 market/trend (9.8%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.0 | 75.0 | +0.13 (0.07) tie | +0.13 (0.07) tie | +0.13 (0.07) tie | 17.2% | 6626 | 20.6% | 0.0% |
| 70/30 market/value | 62.8 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 16.4% | 6690 | 17.8% | 0.6% |
| 85/15 market/trend | 63.2 | 75.0 | +0.42 (0.06) tie | +0.42 (0.06) tie | +0.42 (0.06) tie | 14.4% | 6847 | 14.7% | 0.7% |
| 80/20 market/bills | 64.5 | 75.0 | +1.67 (0.08) | +1.67 (0.08) | +1.67 (0.08) | 17.8% | 6574 | 16.3% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (14.7%), k=0.75: 85/15 market/trend (14.7%), k=1.00: 85/15 market/trend (14.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks | 7/8 | 7/8 | 5/8 | 7/8 | 7/8 | 5/8 |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 1/8 | 1/8 | 3/8 |
| 85/15 market/trend | 7/8 | 7/8 | 7/8 | 0/8 | 0/8 | 0/8 |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |

## S1 paired vs 100 stocks

## sample 1927-07..2026-02, scenario base (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 12.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 11.08% | -1.00% (0.24%) | -0.50 | -1.42 |
| 85/15 market/trend | 8.01% | -4.07% (0.35%) | +0.50 | -1.25 |
| 80/20 market/bills | 9.02% | -3.06% (0.24%) | +1.50 | +0.33 |

## sample 1927-07..2026-02, scenario stocks 3% (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 20.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 17.44% | -2.64% (0.22%) | -0.50 | +0.00 |
| 85/15 market/trend | 13.69% | -6.39% (0.29%) | +0.50 | +0.00 |
| 80/20 market/bills | 14.61% | -5.46% (0.31%) | +1.58 | +0.00 |

## sample 1927-07..2026-02, scenario no value premium (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 12.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 11.70% | -0.37% (0.27%) | -0.25 | -0.83 |
| 85/15 market/trend | 8.01% | -4.07% (0.35%) | +0.50 | -1.25 |
| 80/20 market/bills | 9.02% | -3.06% (0.24%) | +1.50 | +0.33 |

## sample 1927-07..2026-02, scenario stocks 3% + no value premium (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 20.08% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 18.21% | -1.86% (0.32%) | -0.17 | +0.00 |
| 85/15 market/trend | 13.69% | -6.39% (0.29%) | +0.50 | +0.00 |
| 80/20 market/bills | 14.61% | -5.46% (0.31%) | +1.58 | +0.00 |

## sample 1990-01..2026-02, scenario base (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 13.56% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 10.82% | -2.74% (0.39%) | -0.25 | -1.00 |
| 85/15 market/trend | 9.75% | -3.81% (0.30%) | +0.67 | -1.42 |
| 80/20 market/bills | 10.61% | -2.95% (0.25%) | +1.75 | +0.58 |

## sample 1990-01..2026-02, scenario stocks 3% (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 20.60% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 17.27% | -3.33% (0.35%) | -0.46 | +0.00 |
| 85/15 market/trend | 14.74% | -5.86% (0.28%) | +0.29 | +0.00 |
| 80/20 market/bills | 16.31% | -4.29% (0.22%) | +1.54 | +0.00 |

## sample 1990-01..2026-02, scenario no value premium (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 13.56% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 11.62% | -1.93% (0.35%) | +0.00 | -0.50 |
| 85/15 market/trend | 9.75% | -3.81% (0.30%) | +0.67 | -1.42 |
| 80/20 market/bills | 10.61% | -2.95% (0.25%) | +1.75 | +0.58 |

## sample 1990-01..2026-02, scenario stocks 3% + no value premium (baseline: 100 stocks)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks | 20.60% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30 market/value | 17.82% | -2.78% (0.40%) | -0.13 | +0.00 |
| 85/15 market/trend | 14.74% | -5.86% (0.28%) | +0.29 | +0.00 |
| 80/20 market/bills | 16.31% | -4.29% (0.22%) | +1.54 | +0.00 |

# Part D: pre-declared sensitivity S2, trend vol 0.12 (config-q1-s2-trendvol.toml)

## sample 1927-07..2026-02, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.6 | 73.6 | +1.75 (0.13) | +2.33 (0.17) | +2.92 (0.22) | 8.5% | 7318 | 12.1% | 0.0% |
| 70/30 market/value | 60.0 | 71.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 5.9% | 7526 | 10.7% | 0.4% |
| 85/15 market/trend | 61.0 | 71.9 | +1.33 (0.13) | +1.50 (0.18) | +1.67 (0.22) | 6.3% | 7495 | 7.1% | 1.0% |
| 80/20 market/bills | 62.1 | 73.9 | +3.42 (0.15) | +4.08 (0.19) | +4.75 (0.22) | 8.8% | 7293 | 9.0% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.7%), k=0.75: 70/30 market/value (10.7%), k=1.00: 70/30 market/value (10.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-02, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 75.0 | +0.50 (0.10) tie | +0.50 (0.10) tie | +0.50 (0.10) tie | 17.4% | 6610 | 20.1% | 0.0% |
| 70/30 market/value | 62.8 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 13.9% | 6891 | 17.8% | 0.4% |
| 85/15 market/trend | 63.4 | 75.0 | +0.67 (0.09) tie | +0.67 (0.09) tie | +0.67 (0.09) tie | 14.5% | 6838 | 13.0% | 1.0% |
| 80/20 market/bills | 64.8 | 75.0 | +2.08 (0.09) | +2.08 (0.09) | +2.08 (0.09) | 18.1% | 6555 | 14.6% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (13.0%), k=0.75: 85/15 market/trend (13.0%), k=1.00: 85/15 market/trend (13.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-02, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.6 | 73.6 | +1.25 (0.12) | +1.71 (0.16) | +2.17 (0.20) | 8.5% | 7318 | 12.1% | 0.0% |
| 70/30 market/value | 60.2 | 71.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7477 | 11.3% | 0.4% |
| 85/15 market/trend | 61.0 | 71.9 | +0.83 (0.13) tie | +0.88 (0.18) tie | +0.92 (0.22) tie | 6.3% | 7495 | 7.1% | 1.0% |
| 80/20 market/bills | 62.1 | 73.9 | +2.92 (0.14) | +3.46 (0.18) | +4.00 (0.22) | 8.8% | 7293 | 9.0% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (7.1%), k=0.75: 85/15 market/trend (7.1%), k=1.00: 85/15 market/trend (7.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-02, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 75.0 | +0.25 (0.09) tie | +0.25 (0.09) tie | +0.25 (0.09) tie | 17.4% | 6610 | 20.1% | 0.0% |
| 70/30 market/value | 63.0 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 14.8% | 6814 | 18.7% | 0.4% |
| 85/15 market/trend | 63.4 | 75.0 | +0.42 (0.09) tie | +0.42 (0.09) tie | +0.42 (0.09) tie | 14.5% | 6838 | 13.0% | 1.0% |
| 80/20 market/bills | 64.8 | 75.0 | +1.83 (0.08) | +1.83 (0.08) | +1.83 (0.08) | 18.1% | 6555 | 14.6% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (13.0%), k=0.75: 85/15 market/trend (13.0%), k=1.00: 85/15 market/trend (13.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.1 | 73.8 | +1.37 (0.15) | +1.94 (0.22) | +2.50 (0.28) | 8.6% | 7310 | 13.6% | 0.0% |
| 70/30 market/value | 59.8 | 71.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.3% | 7496 | 10.2% | 0.7% |
| 85/15 market/trend | 60.7 | 71.8 | +0.96 (0.10) tie | +1.02 (0.14) | +1.08 (0.19) | 6.2% | 7500 | 9.2% | 1.0% |
| 80/20 market/bills | 61.8 | 74.3 | +3.42 (0.14) | +4.12 (0.20) | +4.83 (0.25) | 8.9% | 7286 | 10.6% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (9.2%), k=0.75: 70/30 market/value (10.2%), k=1.00: 70/30 market/value (10.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.0 | 75.0 | +0.63 (0.06) tie | +0.63 (0.06) tie | +0.63 (0.06) tie | 17.2% | 6626 | 20.6% | 0.0% |
| 70/30 market/value | 62.3 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 13.5% | 6923 | 17.1% | 0.7% |
| 85/15 market/trend | 63.1 | 75.0 | +0.75 (0.07) tie | +0.75 (0.07) tie | +0.75 (0.07) tie | 13.5% | 6921 | 14.3% | 1.0% |
| 80/20 market/bills | 64.5 | 75.0 | +2.17 (0.09) | +2.17 (0.09) | +2.17 (0.09) | 17.8% | 6574 | 16.3% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (14.3%), k=0.75: 85/15 market/trend (14.3%), k=1.00: 85/15 market/trend (14.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.1 | 73.8 | +0.92 (0.14) tie | +1.33 (0.20) | +1.75 (0.26) | 8.6% | 7310 | 13.6% | 0.0% |
| 70/30 market/value | 60.0 | 72.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.8% | 7455 | 10.9% | 0.7% |
| 85/15 market/trend | 60.7 | 71.8 | +0.50 (0.10) tie | +0.42 (0.15) tie | +0.33 (0.20) tie | 6.2% | 7500 | 9.2% | 1.0% |
| 80/20 market/bills | 61.8 | 74.3 | +2.96 (0.14) | +3.52 (0.19) | +4.08 (0.23) | 8.9% | 7286 | 10.6% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (9.2%), k=0.75: 85/15 market/trend (9.2%), k=1.00: 85/15 market/trend (9.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.0 | 75.0 | +0.21 (0.06) tie | +0.21 (0.06) tie | +0.21 (0.06) tie | 17.2% | 6626 | 20.6% | 0.0% |
| 70/30 market/value | 62.8 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 14.5% | 6843 | 17.9% | 0.7% |
| 85/15 market/trend | 63.1 | 75.0 | +0.33 (0.06) tie | +0.33 (0.06) tie | +0.33 (0.06) tie | 13.5% | 6921 | 14.3% | 1.0% |
| 80/20 market/bills | 64.5 | 75.0 | +1.75 (0.09) | +1.75 (0.09) | +1.75 (0.09) | 17.8% | 6574 | 16.3% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 85/15 market/trend (14.3%), k=0.75: 85/15 market/trend (14.3%), k=1.00: 85/15 market/trend (14.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks | 5/8 | 4/8 | 4/8 | 5/8 | 4/8 | 4/8 |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 3/8 | 4/8 | 4/8 |
| 85/15 market/trend | 7/8 | 6/8 | 6/8 | 0/8 | 0/8 | 0/8 |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |

# Part E: pre-declared sensitivity S3, 'stocks 3%' moving market only (config-q1-s3-stocks3-marketonly.toml)

## sample 1927-07..2026-02, scenario stocks 3%, value unchanged at 5%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 75.0 | +1.58 (0.12) | +1.58 (0.15) | +1.58 (0.18) | 17.4% | 6610 | 20.1% | 0.0% |
| 70/30 market/value | 61.7 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 10.8% | 7139 | 15.4% | 0.5% |
| 85/15 market/trend | 63.8 | 75.0 | +2.08 (0.10) | +2.08 (0.12) | +2.08 (0.15) | 15.2% | 6781 | 13.7% | 0.7% |
| 80/20 market/bills | 64.8 | 75.0 | +3.17 (0.12) | +3.17 (0.14) | +3.17 (0.17) | 18.1% | 6555 | 14.6% | 0.7% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (15.4%), k=0.75: 70/30 market/value (15.4%), k=1.00: 70/30 market/value (15.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-02, scenario stocks 3%, value unchanged at 5%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.0 | 75.0 | +1.46 (0.08) | +1.46 (0.10) | +1.46 (0.12) | 17.2% | 6626 | 20.6% | 0.0% |
| 70/30 market/value | 61.5 | 75.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 10.8% | 7133 | 15.4% | 0.8% |
| 85/15 market/trend | 63.2 | 75.0 | +1.75 (0.07) | +1.75 (0.09) | +1.75 (0.11) | 14.4% | 6847 | 14.7% | 0.7% |
| 80/20 market/bills | 64.5 | 75.0 | +3.00 (0.11) | +3.00 (0.12) | +3.00 (0.14) | 17.8% | 6574 | 16.3% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (15.4%), k=0.75: 70/30 market/value (15.4%), k=1.00: 70/30 market/value (15.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 2 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks | 0/2 | 0/2 | 0/2 | 0/2 | 0/2 | 0/2 |
| 70/30 market/value | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 | 2/2 |
| 85/15 market/trend | 0/2 | 0/2 | 0/2 | 0/2 | 0/2 | 0/2 |
| 80/20 market/bills | 0/2 | 0/2 | 0/2 | 0/2 | 0/2 | 0/2 |
