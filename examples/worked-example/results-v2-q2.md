# v2 q2 engine output (Robin, fictional), 2026-11-07

Inputs: Robin's follow-up decisions (01-standard.md). Configs config-v2-q2*.toml, hashed in manifest-v2.txt before scoring. Engine: `uv run --project <repo>/plugins/standard-first-ips/skills/standard-first-ips/engine ips-engine score <config> --out v2-out/<name>.csv`. CSVs and raw text are in v2-out/. Not investment advice.

# Part A: Robin's combining rule (combine_v2.py), seeds 1-3, every variant

## variant: primary (corr 0.72)

### v2-q2.csv: rule pick = 70/30, keep
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 3/8 | 2/8 | 2.6%-8.1% | 12.0%-18.9% |
| 100 stocks, 20% to bills at quit | 6/8 | 3/8 | 2/8 | 2.6%-8.1% | 8.9%-14.9% |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2.2%-7.3% | 10.2%-16.6% |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 2.2%-7.3% | 7.4%-12.6% |

### v2-q2-seed2.csv: rule pick = 70/30, keep
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 4/8 | 3/8 | 2.9%-7.8% | 12.1%-18.9% |
| 100 stocks, 20% to bills at quit | 6/8 | 4/8 | 3/8 | 2.9%-7.8% | 9.0%-15.1% |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2.6%-7.2% | 10.4%-17.1% |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 2.6%-7.2% | 7.7%-12.6% |

### v2-q2-seed3.csv: rule pick = 70/30, keep
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 4/8 | 3/8 | 3.0%-7.8% | 12.2%-18.7% |
| 100 stocks, 20% to bills at quit | 6/8 | 4/8 | 3/8 | 3.0%-7.8% | 9.2%-14.7% |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2.4%-7.3% | 9.8%-16.7% |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 2.4%-7.3% | 7.5%-12.7% |

Picks across the 3 files: ['70/30, keep', '70/30, keep', '70/30, keep']. Stable: True

## variant: -stress095

### v2-q2-stress095.csv: rule pick = 70/30, keep
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 5/8 | 4/8 | 2.6%-8.1% | 12.0%-18.9% |
| 100 stocks, 20% to bills at quit | 6/8 | 5/8 | 4/8 | 2.6%-8.1% | 8.9%-14.9% |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2.5%-7.9% | 10.2%-16.9% |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 2.5%-7.9% | 7.6%-12.6% |

### v2-q2-stress095-seed2.csv: rule pick = 70/30, keep
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 4/8 | 4/8 | 2.9%-7.8% | 12.1%-18.9% |
| 100 stocks, 20% to bills at quit | 6/8 | 4/8 | 4/8 | 2.9%-7.8% | 9.0%-15.1% |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2.8%-7.8% | 10.2%-17.0% |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 2.8%-7.8% | 8.0%-12.6% |

### v2-q2-stress095-seed3.csv: rule pick = 70/30, keep
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 5/8 | 4/8 | 3.0%-7.8% | 12.2%-18.7% |
| 100 stocks, 20% to bills at quit | 6/8 | 5/8 | 4/8 | 3.0%-7.8% | 9.2%-14.7% |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2.6%-7.6% | 10.1%-16.7% |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 2.6%-7.6% | 7.4%-13.0% |

Picks across the 3 files: ['70/30, keep', '70/30, keep', '70/30, keep']. Stable: True

## variant: -billsvol

### v2-q2-billsvol.csv: rule pick = 70/30, keep
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 3/8 | 2/8 | 2.6%-8.1% | 12.0%-18.9% |
| 100 stocks, 20% to bills at quit | 6/8 | 3/8 | 2/8 | 2.6%-8.1% | 9.0%-14.8% |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2.2%-7.3% | 10.2%-16.6% |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 2.2%-7.3% | 7.3%-12.7% |

### v2-q2-billsvol-seed2.csv: rule pick = 70/30, keep
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 4/8 | 3/8 | 2.9%-7.8% | 12.1%-18.9% |
| 100 stocks, 20% to bills at quit | 6/8 | 4/8 | 3/8 | 2.9%-7.8% | 9.0%-15.1% |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2.6%-7.2% | 10.4%-17.1% |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 2.6%-7.2% | 7.6%-12.7% |

### v2-q2-billsvol-seed3.csv: rule pick = 70/30, keep
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 4/8 | 3/8 | 3.0%-7.8% | 12.2%-18.7% |
| 100 stocks, 20% to bills at quit | 6/8 | 4/8 | 3/8 | 3.0%-7.8% | 9.3%-14.7% |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2.4%-7.3% | 9.8%-16.7% |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 2.4%-7.3% | 7.5%-12.7% |

Picks across the 3 files: ['70/30, keep', '70/30, keep', '70/30, keep']. Stable: True

# Engine output: config-v2-q2.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.5 | 73.7 | +0.91 (0.13) tie | +1.20 (0.17) | +1.49 (0.22) | 2.6% | 7789 | 12.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.5 | 73.7 | +0.91 (0.13) tie | +1.20 (0.17) | +1.49 (0.22) | 2.6% | 7789 | 8.9% | 0.0% |
| 70/30, keep | 60.2 | 72.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.2% | 7821 | 10.7% | 0.4% |
| 70/30, 20% to bills at quit | 60.2 | 72.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.2% | 7821 | 7.7% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.7%), k=0.75: 70/30, 20% to bills at quit (7.7%), k=1.00: 70/30, 20% to bills at quit (7.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.3 | 81.6 | +1.33 (0.13) | +1.75 (0.19) | +2.17 (0.25) | 7.6% | 7392 | 18.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.3 | 81.6 | +1.33 (0.13) | +1.75 (0.19) | +2.17 (0.25) | 7.6% | 7392 | 13.9% | 0.0% |
| 70/30, keep | 62.8 | 79.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.4% | 7486 | 16.2% | 0.4% |
| 70/30, 20% to bills at quit | 62.8 | 79.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.4% | 7486 | 12.1% | 0.4% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.1%), k=0.75: 70/30, 20% to bills at quit (12.1%), k=1.00: 70/30, 20% to bills at quit (12.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.5 | 73.7 | +0.29 (0.11) tie | +0.40 (0.15) tie | +0.50 (0.20) tie | 2.6% | 7789 | 12.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.5 | 73.7 | +0.29 (0.11) tie | +0.40 (0.15) tie | +0.50 (0.20) tie | 2.6% | 7789 | 8.9% | 0.0% |
| 70/30, keep | 60.4 | 73.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7792 | 11.0% | 0.4% |
| 70/30, 20% to bills at quit | 60.4 | 73.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7792 | 8.0% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.0%), k=0.75: 70/30, 20% to bills at quit (8.0%), k=1.00: 70/30, 20% to bills at quit (8.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.3 | 81.6 | +0.62 (0.17) tie | +0.85 (0.23) tie | +1.08 (0.29) | 7.6% | 7392 | 18.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.3 | 81.6 | +0.62 (0.17) tie | +0.85 (0.23) tie | +1.08 (0.29) | 7.6% | 7392 | 13.9% | 0.0% |
| 70/30, keep | 63.2 | 80.7 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7433 | 16.6% | 0.4% |
| 70/30, 20% to bills at quit | 63.2 | 80.7 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7433 | 12.6% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.6%), k=0.75: 70/30, 20% to bills at quit (12.6%), k=1.00: 70/30, 20% to bills at quit (12.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.2 | 73.8 | +0.88 (0.11) tie | +1.12 (0.16) | +1.38 (0.21) | 3.3% | 7735 | 12.3% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.2 | 73.8 | +0.88 (0.11) tie | +1.12 (0.16) | +1.38 (0.21) | 3.3% | 7735 | 9.6% | 0.0% |
| 70/30, keep | 59.9 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7791 | 10.2% | 0.6% |
| 70/30, 20% to bills at quit | 59.9 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7791 | 7.4% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.4%), k=0.75: 70/30, 20% to bills at quit (7.4%), k=1.00: 70/30, 20% to bills at quit (7.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 82.1 | +1.63 (0.14) | +2.10 (0.21) | +2.58 (0.28) | 8.1% | 7356 | 18.9% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 82.1 | +1.63 (0.14) | +2.10 (0.21) | +2.58 (0.28) | 8.1% | 7356 | 14.9% | 0.0% |
| 70/30, keep | 62.5 | 80.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.7% | 7466 | 15.6% | 0.7% |
| 70/30, 20% to bills at quit | 62.5 | 80.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.7% | 7466 | 11.5% | 0.7% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (11.5%), k=0.75: 70/30, 20% to bills at quit (11.5%), k=1.00: 70/30, 20% to bills at quit (11.5%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.2 | 73.8 | +0.46 (0.09) tie | +0.60 (0.12) tie | +0.75 (0.16) tie | 3.3% | 7735 | 12.3% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.2 | 73.8 | +0.46 (0.09) tie | +0.60 (0.12) tie | +0.75 (0.16) tie | 3.3% | 7735 | 9.6% | 0.0% |
| 70/30, keep | 60.1 | 73.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7776 | 10.7% | 0.6% |
| 70/30, 20% to bills at quit | 60.1 | 73.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7776 | 7.9% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.9%), k=0.75: 70/30, 20% to bills at quit (7.9%), k=1.00: 70/30, 20% to bills at quit (7.9%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 82.1 | +0.88 (0.14) tie | +1.15 (0.21) | +1.42 (0.28) | 8.1% | 7356 | 18.9% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 82.1 | +0.88 (0.14) tie | +1.15 (0.21) | +1.42 (0.28) | 8.1% | 7356 | 14.9% | 0.0% |
| 70/30, keep | 62.8 | 81.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7415 | 16.4% | 0.6% |
| 70/30, 20% to bills at quit | 62.8 | 81.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7415 | 12.3% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.3%), k=0.75: 70/30, 20% to bills at quit (12.3%), k=1.00: 70/30, 20% to bills at quit (12.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 3/8 | 2/8 | 6/8 | 3/8 | 2/8 |
| 100 stocks, 20% to bills at quit | 6/8 | 3/8 | 2/8 | 0/8 | 0/8 | 0/8 |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2/8 | 5/8 | 6/8 |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 0/8 | 0/8 | 0/8 |

## Paired run-out vs keeping the same base mix (runout_paired.py). Read rows of the same base mix only.

## sample 1927-07..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 11.97% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 8.94% | -3.03% (0.23%) | +0.00 | +0.00 |
| 70/30, keep | 10.65% | -1.31% (0.19%) | -0.33 | -1.16 |
| 70/30, 20% to bills at quit | 7.66% | -4.31% (0.26%) | -0.33 | -1.16 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.07% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.91% | -4.17% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 16.15% | -1.92% (0.32%) | -0.50 | -1.67 |
| 70/30, 20% to bills at quit | 12.13% | -5.94% (0.30%) | -0.50 | -1.67 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 11.97% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 8.94% | -3.03% (0.23%) | +0.00 | +0.00 |
| 70/30, keep | 11.02% | -0.94% (0.17%) | -0.08 | -0.42 |
| 70/30, 20% to bills at quit | 7.96% | -4.01% (0.23%) | -0.08 | -0.42 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.07% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.91% | -4.17% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 16.59% | -1.49% (0.34%) | -0.17 | -0.92 |
| 70/30, 20% to bills at quit | 12.59% | -5.48% (0.33%) | -0.17 | -0.92 |

## sample 1990-01..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.31% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.62% | -2.69% (0.17%) | +0.00 | +0.00 |
| 70/30, keep | 10.24% | -2.07% (0.36%) | -0.38 | -1.00 |
| 70/30, 20% to bills at quit | 7.37% | -4.94% (0.41%) | -0.38 | -1.00 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.86% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 14.93% | -3.93% (0.20%) | +0.00 | +0.00 |
| 70/30, keep | 15.63% | -3.22% (0.37%) | -0.67 | -1.92 |
| 70/30, 20% to bills at quit | 11.48% | -7.38% (0.39%) | -0.67 | -1.92 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.31% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.62% | -2.69% (0.17%) | +0.00 | +0.00 |
| 70/30, keep | 10.69% | -1.62% (0.41%) | -0.17 | -0.58 |
| 70/30, 20% to bills at quit | 7.86% | -4.45% (0.46%) | -0.17 | -0.58 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.86% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 14.93% | -3.93% (0.20%) | +0.00 | +0.00 |
| 70/30, keep | 16.44% | -2.42% (0.32%) | -0.33 | -1.08 |
| 70/30, 20% to bills at quit | 12.33% | -6.53% (0.36%) | -0.33 | -1.08 |

## sample 1927-07..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 11.97% | +1.31% (0.19%) | +0.33 | +1.16 |
| 100 stocks, 20% to bills at quit | 8.94% | -1.72% (0.31%) | +0.33 | +1.16 |
| 70/30, keep | 10.65% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.66% | -2.99% (0.19%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.07% | +1.92% (0.32%) | +0.50 | +1.67 |
| 100 stocks, 20% to bills at quit | 13.91% | -2.24% (0.25%) | +0.50 | +1.67 |
| 70/30, keep | 16.15% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.13% | -4.02% (0.23%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 11.97% | +0.94% (0.17%) | +0.08 | +0.42 |
| 100 stocks, 20% to bills at quit | 8.94% | -2.09% (0.27%) | +0.08 | +0.42 |
| 70/30, keep | 11.02% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.96% | -3.07% (0.18%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.07% | +1.49% (0.34%) | +0.17 | +0.92 |
| 100 stocks, 20% to bills at quit | 13.91% | -2.68% (0.26%) | +0.17 | +0.92 |
| 70/30, keep | 16.59% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.59% | -4.00% (0.21%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.31% | +2.07% (0.36%) | +0.38 | +1.00 |
| 100 stocks, 20% to bills at quit | 9.62% | -0.62% (0.33%) | +0.38 | +1.00 |
| 70/30, keep | 10.24% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.37% | -2.88% (0.21%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.86% | +3.22% (0.37%) | +0.67 | +1.92 |
| 100 stocks, 20% to bills at quit | 14.93% | -0.70% (0.35%) | +0.67 | +1.92 |
| 70/30, keep | 15.63% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 11.48% | -4.15% (0.21%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.31% | +1.62% (0.41%) | +0.17 | +0.58 |
| 100 stocks, 20% to bills at quit | 9.62% | -1.07% (0.40%) | +0.17 | +0.58 |
| 70/30, keep | 10.69% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.86% | -2.83% (0.19%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.86% | +2.42% (0.32%) | +0.33 | +1.08 |
| 100 stocks, 20% to bills at quit | 14.93% | -1.51% (0.32%) | +0.33 | +1.08 |
| 70/30, keep | 16.44% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.33% | -4.11% (0.21%) | +0.00 | +0.00 |

# Engine output: config-v2-q2-seed2.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.4 | 73.7 | +0.95 (0.10) tie | +1.26 (0.14) | +1.57 (0.18) | 3.0% | 7758 | 12.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.4 | 73.7 | +0.95 (0.10) tie | +1.26 (0.14) | +1.57 (0.18) | 3.0% | 7758 | 9.0% | 0.0% |
| 70/30, keep | 60.1 | 72.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7791 | 10.7% | 0.4% |
| 70/30, 20% to bills at quit | 60.1 | 72.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7791 | 7.8% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.8%), k=0.75: 70/30, 20% to bills at quit (7.8%), k=1.00: 70/30, 20% to bills at quit (7.8%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 81.4 | +1.33 (0.15) | +1.75 (0.21) | +2.17 (0.27) | 7.6% | 7390 | 18.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 81.4 | +1.33 (0.15) | +1.75 (0.21) | +2.17 (0.27) | 7.6% | 7390 | 14.0% | 0.0% |
| 70/30, keep | 62.8 | 79.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7481 | 16.4% | 0.4% |
| 70/30, 20% to bills at quit | 62.8 | 79.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7481 | 12.1% | 0.4% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.1%), k=0.75: 70/30, 20% to bills at quit (12.1%), k=1.00: 70/30, 20% to bills at quit (12.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.4 | 73.7 | +0.42 (0.08) tie | +0.58 (0.12) tie | +0.75 (0.16) tie | 3.0% | 7758 | 12.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.4 | 73.7 | +0.42 (0.08) tie | +0.58 (0.12) tie | +0.75 (0.16) tie | 3.0% | 7758 | 9.0% | 0.0% |
| 70/30, keep | 60.3 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7775 | 11.2% | 0.4% |
| 70/30, 20% to bills at quit | 60.3 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7775 | 8.4% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.4%), k=0.75: 70/30, 20% to bills at quit (8.4%), k=1.00: 70/30, 20% to bills at quit (8.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 81.4 | +0.45 (0.16) tie | +0.60 (0.23) tie | +0.74 (0.31) tie | 7.6% | 7390 | 18.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 81.4 | +0.45 (0.16) tie | +0.60 (0.23) tie | +0.74 (0.31) tie | 7.6% | 7390 | 14.0% | 0.0% |
| 70/30, keep | 63.1 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7431 | 17.1% | 0.4% |
| 70/30, 20% to bills at quit | 63.1 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7431 | 12.6% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.6%), k=0.75: 70/30, 20% to bills at quit (12.6%), k=1.00: 70/30, 20% to bills at quit (12.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.3 | 74.1 | +0.92 (0.11) tie | +1.21 (0.15) | +1.50 (0.20) | 2.9% | 7771 | 13.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.3 | 74.1 | +0.92 (0.11) tie | +1.21 (0.15) | +1.50 (0.20) | 2.9% | 7771 | 9.9% | 0.0% |
| 70/30, keep | 60.0 | 72.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.7% | 7784 | 10.4% | 0.7% |
| 70/30, 20% to bills at quit | 60.0 | 72.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.7% | 7784 | 7.7% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.7%), k=0.75: 70/30, 20% to bills at quit (7.7%), k=1.00: 70/30, 20% to bills at quit (7.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 81.8 | +1.41 (0.20) | +1.89 (0.28) | +2.37 (0.35) | 7.8% | 7376 | 18.9% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 81.8 | +1.41 (0.20) | +1.89 (0.28) | +2.37 (0.35) | 7.8% | 7376 | 15.1% | 0.0% |
| 70/30, keep | 62.7 | 79.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.6% | 7471 | 15.8% | 0.7% |
| 70/30, 20% to bills at quit | 62.7 | 79.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.6% | 7471 | 11.9% | 0.7% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (11.9%), k=0.75: 70/30, 20% to bills at quit (11.9%), k=1.00: 70/30, 20% to bills at quit (11.9%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.3 | 74.1 | +0.46 (0.10) tie | +0.60 (0.14) tie | +0.75 (0.19) tie | 2.9% | 7771 | 13.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.3 | 74.1 | +0.46 (0.10) tie | +0.60 (0.14) tie | +0.75 (0.19) tie | 2.9% | 7771 | 9.9% | 0.0% |
| 70/30, keep | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.9% | 7769 | 10.8% | 0.6% |
| 70/30, 20% to bills at quit | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.9% | 7769 | 8.1% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.1%), k=0.75: 70/30, 20% to bills at quit (8.1%), k=1.00: 70/30, 20% to bills at quit (8.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 81.8 | +0.70 (0.19) tie | +0.97 (0.26) tie | +1.24 (0.33) | 7.8% | 7376 | 18.9% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 81.8 | +0.70 (0.19) tie | +0.97 (0.26) tie | +1.24 (0.33) | 7.8% | 7376 | 15.1% | 0.0% |
| 70/30, keep | 63.0 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.2% | 7426 | 16.3% | 0.6% |
| 70/30, 20% to bills at quit | 63.0 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.2% | 7426 | 12.6% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.6%), k=0.75: 70/30, 20% to bills at quit (12.6%), k=1.00: 70/30, 20% to bills at quit (12.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 4/8 | 3/8 | 6/8 | 4/8 | 3/8 |
| 100 stocks, 20% to bills at quit | 6/8 | 4/8 | 3/8 | 0/8 | 0/8 | 0/8 |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2/8 | 4/8 | 5/8 |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 0/8 | 0/8 | 0/8 |

## Paired run-out vs keeping the same base mix (runout_paired.py). Read rows of the same base mix only.

## sample 1927-07..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.14% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 8.98% | -3.16% (0.15%) | +0.00 | +0.00 |
| 70/30, keep | 10.67% | -1.48% (0.26%) | -0.33 | -1.24 |
| 70/30, 20% to bills at quit | 7.78% | -4.36% (0.18%) | -0.33 | -1.24 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.96% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.95% | -4.01% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 16.39% | -1.57% (0.31%) | -0.50 | -1.67 |
| 70/30, 20% to bills at quit | 12.07% | -5.89% (0.31%) | -0.50 | -1.67 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.14% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 8.98% | -3.16% (0.15%) | +0.00 | +0.00 |
| 70/30, keep | 11.16% | -0.98% (0.18%) | -0.08 | -0.67 |
| 70/30, 20% to bills at quit | 8.40% | -3.74% (0.16%) | -0.08 | -0.67 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.96% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.95% | -4.01% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 17.06% | -0.89% (0.25%) | -0.17 | -0.57 |
| 70/30, 20% to bills at quit | 12.58% | -5.37% (0.29%) | -0.17 | -0.57 |

## sample 1990-01..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.01% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.95% | -3.06% (0.19%) | +0.00 | +0.00 |
| 70/30, keep | 10.38% | -2.63% (0.29%) | -0.33 | -1.17 |
| 70/30, 20% to bills at quit | 7.67% | -5.34% (0.35%) | -0.33 | -1.17 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.93% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.08% | -3.85% (0.14%) | +0.00 | +0.00 |
| 70/30, keep | 15.77% | -3.16% (0.44%) | -0.46 | -1.91 |
| 70/30, 20% to bills at quit | 11.89% | -7.04% (0.37%) | -0.46 | -1.91 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.01% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.95% | -3.06% (0.19%) | +0.00 | +0.00 |
| 70/30, keep | 10.79% | -2.22% (0.33%) | -0.17 | -0.58 |
| 70/30, 20% to bills at quit | 8.15% | -4.86% (0.37%) | -0.17 | -0.58 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.93% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.08% | -3.85% (0.14%) | +0.00 | +0.00 |
| 70/30, keep | 16.35% | -2.58% (0.44%) | -0.17 | -1.07 |
| 70/30, 20% to bills at quit | 12.56% | -6.36% (0.41%) | -0.17 | -1.07 |

## sample 1927-07..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.14% | +1.48% (0.26%) | +0.33 | +1.24 |
| 100 stocks, 20% to bills at quit | 8.98% | -1.68% (0.24%) | +0.33 | +1.24 |
| 70/30, keep | 10.67% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.78% | -2.89% (0.23%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.96% | +1.57% (0.31%) | +0.50 | +1.67 |
| 100 stocks, 20% to bills at quit | 13.95% | -2.44% (0.28%) | +0.50 | +1.67 |
| 70/30, keep | 16.39% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.07% | -4.32% (0.16%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.14% | +0.98% (0.18%) | +0.08 | +0.67 |
| 100 stocks, 20% to bills at quit | 8.98% | -2.18% (0.20%) | +0.08 | +0.67 |
| 70/30, keep | 11.16% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.40% | -2.77% (0.16%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.96% | +0.89% (0.25%) | +0.17 | +0.57 |
| 100 stocks, 20% to bills at quit | 13.95% | -3.11% (0.24%) | +0.17 | +0.57 |
| 70/30, keep | 17.06% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.58% | -4.48% (0.19%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.01% | +2.63% (0.29%) | +0.33 | +1.17 |
| 100 stocks, 20% to bills at quit | 9.95% | -0.43% (0.27%) | +0.33 | +1.17 |
| 70/30, keep | 10.38% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.67% | -2.71% (0.20%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.93% | +3.16% (0.44%) | +0.46 | +1.91 |
| 100 stocks, 20% to bills at quit | 15.08% | -0.69% (0.41%) | +0.46 | +1.91 |
| 70/30, keep | 15.77% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 11.89% | -3.88% (0.23%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.01% | +2.22% (0.33%) | +0.17 | +0.58 |
| 100 stocks, 20% to bills at quit | 9.95% | -0.84% (0.31%) | +0.17 | +0.58 |
| 70/30, keep | 10.79% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.15% | -2.64% (0.23%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.93% | +2.58% (0.44%) | +0.17 | +1.07 |
| 100 stocks, 20% to bills at quit | 15.08% | -1.27% (0.45%) | +0.17 | +1.07 |
| 70/30, keep | 16.35% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.56% | -3.78% (0.25%) | +0.00 | +0.00 |

# Engine output: config-v2-q2-seed3.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.4 | 74.3 | +1.00 (0.10) | +1.33 (0.14) | +1.67 (0.18) | 3.1% | 7751 | 12.2% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.4 | 74.3 | +1.00 (0.10) | +1.33 (0.14) | +1.67 (0.18) | 3.1% | 7751 | 9.2% | 0.0% |
| 70/30, keep | 60.1 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.5% | 7803 | 10.6% | 0.4% |
| 70/30, 20% to bills at quit | 60.1 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.5% | 7803 | 7.7% | 0.4% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.7%), k=0.75: 70/30, 20% to bills at quit (7.7%), k=1.00: 70/30, 20% to bills at quit (7.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.3 | 82.1 | +1.67 (0.13) | +2.17 (0.17) | +2.67 (0.21) | 7.8% | 7377 | 17.3% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.3 | 82.1 | +1.67 (0.13) | +2.17 (0.17) | +2.67 (0.21) | 7.8% | 7377 | 13.3% | 0.0% |
| 70/30, keep | 62.7 | 80.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.6% | 7476 | 16.5% | 0.4% |
| 70/30, 20% to bills at quit | 62.7 | 80.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.6% | 7476 | 12.6% | 0.4% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.6%), k=0.75: 70/30, 20% to bills at quit (12.6%), k=1.00: 70/30, 20% to bills at quit (12.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.4 | 74.3 | +0.58 (0.10) tie | +0.79 (0.14) tie | +1.00 (0.18) tie | 3.1% | 7751 | 12.2% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.4 | 74.3 | +0.58 (0.10) tie | +0.79 (0.14) tie | +1.00 (0.18) tie | 3.1% | 7751 | 9.2% | 0.0% |
| 70/30, keep | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7778 | 11.1% | 0.4% |
| 70/30, 20% to bills at quit | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7778 | 8.1% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.1%), k=0.75: 70/30, 20% to bills at quit (8.1%), k=1.00: 70/30, 20% to bills at quit (8.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.3 | 82.1 | +0.75 (0.13) tie | +1.00 (0.17) tie | +1.25 (0.21) | 7.8% | 7377 | 17.3% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.3 | 82.1 | +0.75 (0.13) tie | +1.00 (0.17) tie | +1.25 (0.21) | 7.8% | 7377 | 13.3% | 0.0% |
| 70/30, keep | 63.1 | 81.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7419 | 16.7% | 0.4% |
| 70/30, 20% to bills at quit | 63.1 | 81.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7419 | 12.7% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.7%), k=0.75: 70/30, 20% to bills at quit (12.7%), k=1.00: 70/30, 20% to bills at quit (12.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.1 | 74.0 | +0.79 (0.11) tie | +1.10 (0.15) | +1.42 (0.20) | 3.0% | 7760 | 12.7% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.1 | 74.0 | +0.79 (0.11) tie | +1.10 (0.15) | +1.42 (0.20) | 3.0% | 7760 | 10.0% | 0.0% |
| 70/30, keep | 59.9 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.4% | 7810 | 9.8% | 0.7% |
| 70/30, 20% to bills at quit | 59.9 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.4% | 7810 | 7.5% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.5%), k=0.75: 70/30, 20% to bills at quit (7.5%), k=1.00: 70/30, 20% to bills at quit (7.5%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.0 | 81.3 | +1.25 (0.17) | +1.62 (0.23) | +2.00 (0.30) | 7.4% | 7408 | 18.7% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.0 | 81.3 | +1.25 (0.17) | +1.62 (0.23) | +2.00 (0.30) | 7.4% | 7408 | 14.7% | 0.0% |
| 70/30, keep | 62.5 | 79.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7481 | 15.4% | 0.7% |
| 70/30, 20% to bills at quit | 62.5 | 79.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7481 | 11.3% | 0.7% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (11.3%), k=0.75: 70/30, 20% to bills at quit (11.3%), k=1.00: 70/30, 20% to bills at quit (11.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.1 | 74.0 | +0.29 (0.12) tie | +0.44 (0.17) tie | +0.58 (0.22) tie | 3.0% | 7760 | 12.7% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.1 | 74.0 | +0.29 (0.12) tie | +0.44 (0.17) tie | +0.58 (0.22) tie | 3.0% | 7760 | 10.0% | 0.0% |
| 70/30, keep | 60.1 | 73.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7789 | 10.4% | 0.6% |
| 70/30, 20% to bills at quit | 60.1 | 73.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7789 | 7.6% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.6%), k=0.75: 70/30, 20% to bills at quit (7.6%), k=1.00: 70/30, 20% to bills at quit (7.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.0 | 81.3 | +0.55 (0.17) tie | +0.74 (0.22) tie | +0.93 (0.27) tie | 7.4% | 7408 | 18.7% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.0 | 81.3 | +0.55 (0.17) tie | +0.74 (0.22) tie | +0.93 (0.27) tie | 7.4% | 7408 | 14.7% | 0.0% |
| 70/30, keep | 62.8 | 80.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.0% | 7437 | 16.1% | 0.6% |
| 70/30, 20% to bills at quit | 62.8 | 80.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.0% | 7437 | 12.0% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.0%), k=0.75: 70/30, 20% to bills at quit (12.0%), k=1.00: 70/30, 20% to bills at quit (12.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks, keep | 5/8 | 4/8 | 3/8 | 5/8 | 4/8 | 3/8 |
| 100 stocks, 20% to bills at quit | 5/8 | 4/8 | 3/8 | 0/8 | 0/8 | 0/8 |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 3/8 | 4/8 | 5/8 |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 0/8 | 0/8 | 0/8 |

## Paired run-out vs keeping the same base mix (runout_paired.py). Read rows of the same base mix only.

## sample 1927-07..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.24% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.21% | -3.03% (0.28%) | +0.00 | +0.00 |
| 70/30, keep | 10.62% | -1.62% (0.27%) | -0.33 | -1.33 |
| 70/30, 20% to bills at quit | 7.74% | -4.50% (0.29%) | -0.33 | -1.33 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.32% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.31% | -4.01% (0.23%) | +0.00 | +0.00 |
| 70/30, keep | 16.49% | -0.83% (0.33%) | -0.67 | -2.00 |
| 70/30, 20% to bills at quit | 12.57% | -4.75% (0.39%) | -0.67 | -2.00 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.24% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.21% | -3.03% (0.28%) | +0.00 | +0.00 |
| 70/30, keep | 11.11% | -1.14% (0.25%) | -0.17 | -0.83 |
| 70/30, 20% to bills at quit | 8.14% | -4.11% (0.27%) | -0.17 | -0.83 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.32% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.31% | -4.01% (0.23%) | +0.00 | +0.00 |
| 70/30, keep | 16.71% | -0.61% (0.34%) | -0.25 | -1.00 |
| 70/30, 20% to bills at quit | 12.72% | -4.60% (0.32%) | -0.25 | -1.00 |

## sample 1990-01..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.65% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 10.01% | -2.64% (0.19%) | +0.00 | +0.00 |
| 70/30, keep | 9.82% | -2.83% (0.25%) | -0.17 | -1.25 |
| 70/30, 20% to bills at quit | 7.53% | -5.13% (0.28%) | -0.17 | -1.25 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.71% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 14.74% | -3.97% (0.20%) | +0.00 | +0.00 |
| 70/30, keep | 15.36% | -3.35% (0.26%) | -0.50 | -1.50 |
| 70/30, 20% to bills at quit | 11.28% | -7.43% (0.35%) | -0.50 | -1.50 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.65% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 10.01% | -2.64% (0.19%) | +0.00 | +0.00 |
| 70/30, keep | 10.44% | -2.22% (0.24%) | +0.00 | -0.58 |
| 70/30, 20% to bills at quit | 7.63% | -5.03% (0.27%) | +0.00 | -0.58 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.71% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 14.74% | -3.97% (0.20%) | +0.00 | +0.00 |
| 70/30, keep | 16.05% | -2.65% (0.31%) | -0.17 | -0.76 |
| 70/30, 20% to bills at quit | 11.99% | -6.72% (0.37%) | -0.17 | -0.76 |

## sample 1927-07..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.24% | +1.62% (0.27%) | +0.33 | +1.33 |
| 100 stocks, 20% to bills at quit | 9.21% | -1.41% (0.35%) | +0.33 | +1.33 |
| 70/30, keep | 10.62% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.74% | -2.88% (0.21%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.32% | +0.83% (0.33%) | +0.67 | +2.00 |
| 100 stocks, 20% to bills at quit | 13.31% | -3.18% (0.32%) | +0.67 | +2.00 |
| 70/30, keep | 16.49% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.57% | -3.92% (0.26%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.24% | +1.14% (0.25%) | +0.17 | +0.83 |
| 100 stocks, 20% to bills at quit | 9.21% | -1.90% (0.31%) | +0.17 | +0.83 |
| 70/30, keep | 11.11% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.14% | -2.97% (0.19%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.32% | +0.61% (0.34%) | +0.25 | +1.00 |
| 100 stocks, 20% to bills at quit | 13.31% | -3.40% (0.35%) | +0.25 | +1.00 |
| 70/30, keep | 16.71% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.72% | -3.99% (0.21%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.65% | +2.83% (0.25%) | +0.17 | +1.25 |
| 100 stocks, 20% to bills at quit | 10.01% | +0.19% (0.22%) | +0.17 | +1.25 |
| 70/30, keep | 9.82% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.53% | -2.29% (0.18%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.71% | +3.35% (0.26%) | +0.50 | +1.50 |
| 100 stocks, 20% to bills at quit | 14.74% | -0.62% (0.17%) | +0.50 | +1.50 |
| 70/30, keep | 15.36% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 11.28% | -4.08% (0.22%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.65% | +2.22% (0.24%) | +0.00 | +0.58 |
| 100 stocks, 20% to bills at quit | 10.01% | -0.42% (0.20%) | +0.00 | +0.58 |
| 70/30, keep | 10.44% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.63% | -2.81% (0.16%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.71% | +2.65% (0.31%) | +0.17 | +0.76 |
| 100 stocks, 20% to bills at quit | 14.74% | -1.31% (0.27%) | +0.17 | +0.76 |
| 70/30, keep | 16.05% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 11.99% | -4.06% (0.28%) | +0.00 | +0.00 |

# Engine output: config-v2-q2-stress095.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.5 | 73.7 | +0.71 (0.10) tie | +0.90 (0.13) tie | +1.08 (0.16) | 2.6% | 7789 | 12.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.5 | 73.7 | +0.71 (0.10) tie | +0.90 (0.13) tie | +1.08 (0.16) | 2.6% | 7789 | 8.9% | 0.0% |
| 70/30, keep | 60.2 | 72.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.5% | 7798 | 11.0% | 0.4% |
| 70/30, 20% to bills at quit | 60.2 | 72.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.5% | 7798 | 7.8% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.8%), k=0.75: 70/30, 20% to bills at quit (7.8%), k=1.00: 70/30, 20% to bills at quit (7.8%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.3 | 81.6 | +1.12 (0.12) | +1.44 (0.16) | +1.75 (0.21) | 7.6% | 7392 | 18.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.3 | 81.6 | +1.12 (0.12) | +1.44 (0.16) | +1.75 (0.21) | 7.6% | 7392 | 13.9% | 0.0% |
| 70/30, keep | 62.8 | 80.3 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.8% | 7456 | 16.2% | 0.4% |
| 70/30, 20% to bills at quit | 62.8 | 80.3 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.8% | 7456 | 12.3% | 0.4% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.3%), k=0.75: 70/30, 20% to bills at quit (12.3%), k=1.00: 70/30, 20% to bills at quit (12.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.5 | 73.7 | +0.17 (0.10) tie | +0.21 (0.13) tie | +0.25 (0.16) tie | 2.6% | 7789 | 12.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.5 | 73.7 | +0.17 (0.10) tie | +0.21 (0.13) tie | +0.25 (0.16) tie | 2.6% | 7789 | 8.9% | 0.0% |
| 70/30, keep | 60.4 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.9% | 7770 | 11.3% | 0.4% |
| 70/30, 20% to bills at quit | 60.4 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.9% | 7770 | 8.1% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.1%), k=0.75: 70/30, 20% to bills at quit (8.1%), k=1.00: 70/30, 20% to bills at quit (8.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.3 | 81.6 | +0.37 (0.15) tie | +0.47 (0.21) tie | +0.57 (0.27) tie | 7.6% | 7392 | 18.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.3 | 81.6 | +0.37 (0.15) tie | +0.47 (0.21) tie | +0.57 (0.27) tie | 7.6% | 7392 | 13.9% | 0.0% |
| 70/30, keep | 63.2 | 81.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.5% | 7402 | 16.8% | 0.4% |
| 70/30, 20% to bills at quit | 63.2 | 81.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.5% | 7402 | 12.6% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.6%), k=0.75: 70/30, 20% to bills at quit (12.6%), k=1.00: 70/30, 20% to bills at quit (12.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.2 | 73.8 | +0.79 (0.11) tie | +1.02 (0.15) | +1.25 (0.20) | 3.3% | 7735 | 12.3% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.2 | 73.8 | +0.79 (0.11) tie | +1.02 (0.15) | +1.25 (0.20) | 3.3% | 7735 | 9.6% | 0.0% |
| 70/30, keep | 59.9 | 72.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7775 | 10.2% | 0.6% |
| 70/30, 20% to bills at quit | 59.9 | 72.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7775 | 7.7% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.7%), k=0.75: 70/30, 20% to bills at quit (7.7%), k=1.00: 70/30, 20% to bills at quit (7.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 82.1 | +1.20 (0.15) | +1.51 (0.22) | +1.82 (0.28) | 8.1% | 7356 | 18.9% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 82.1 | +1.20 (0.15) | +1.51 (0.22) | +1.82 (0.28) | 8.1% | 7356 | 14.9% | 0.0% |
| 70/30, keep | 62.6 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7418 | 15.3% | 0.6% |
| 70/30, 20% to bills at quit | 62.6 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7418 | 11.6% | 0.6% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (11.6%), k=0.75: 70/30, 20% to bills at quit (11.6%), k=1.00: 70/30, 20% to bills at quit (11.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.2 | 73.8 | +0.29 (0.09) tie | +0.35 (0.13) tie | +0.42 (0.16) tie | 3.3% | 7735 | 12.3% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.2 | 73.8 | +0.29 (0.09) tie | +0.35 (0.13) tie | +0.42 (0.16) tie | 3.3% | 7735 | 9.6% | 0.0% |
| 70/30, keep | 60.1 | 73.6 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 3.1% | 7750 | 10.6% | 0.6% |
| 70/30, 20% to bills at quit | 60.1 | 73.6 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 3.1% | 7750 | 8.0% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.0%), k=0.75: 70/30, 20% to bills at quit (8.0%), k=1.00: 70/30, 20% to bills at quit (8.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 82.1 | +0.33 (0.14) tie | +0.38 (0.21) tie | +0.42 (0.27) tie | 8.1% | 7356 | 18.9% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 82.1 | +0.33 (0.14) tie | +0.38 (0.21) tie | +0.42 (0.27) tie | 8.1% | 7356 | 14.9% | 0.0% |
| 70/30, keep | 62.9 | 81.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.9% | 7366 | 16.3% | 0.6% |
| 70/30, 20% to bills at quit | 62.9 | 81.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.9% | 7366 | 12.2% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.2%), k=0.75: 70/30, 20% to bills at quit (12.2%), k=1.00: 70/30, 20% to bills at quit (12.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 5/8 | 4/8 | 6/8 | 5/8 | 4/8 |
| 100 stocks, 20% to bills at quit | 6/8 | 5/8 | 4/8 | 0/8 | 0/8 | 0/8 |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2/8 | 3/8 | 4/8 |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 0/8 | 0/8 | 0/8 |

## Paired run-out vs keeping the same base mix (runout_paired.py). Read rows of the same base mix only.

## sample 1927-07..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 11.97% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 8.94% | -3.03% (0.23%) | +0.00 | +0.00 |
| 70/30, keep | 10.98% | -0.99% (0.18%) | -0.33 | -0.75 |
| 70/30, 20% to bills at quit | 7.85% | -4.12% (0.17%) | -0.33 | -0.75 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.07% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.91% | -4.17% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 16.17% | -1.90% (0.31%) | -0.50 | -1.25 |
| 70/30, 20% to bills at quit | 12.27% | -5.80% (0.30%) | -0.50 | -1.25 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 11.97% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 8.94% | -3.03% (0.23%) | +0.00 | +0.00 |
| 70/30, keep | 11.31% | -0.65% (0.19%) | -0.08 | -0.17 |
| 70/30, 20% to bills at quit | 8.15% | -3.82% (0.21%) | -0.08 | -0.17 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.07% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.91% | -4.17% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 16.85% | -1.23% (0.39%) | -0.17 | -0.41 |
| 70/30, 20% to bills at quit | 12.62% | -5.46% (0.34%) | -0.17 | -0.41 |

## sample 1990-01..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.31% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.62% | -2.69% (0.17%) | +0.00 | +0.00 |
| 70/30, keep | 10.19% | -2.12% (0.36%) | -0.33 | -0.92 |
| 70/30, 20% to bills at quit | 7.65% | -4.65% (0.45%) | -0.33 | -0.92 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.86% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 14.93% | -3.93% (0.20%) | +0.00 | +0.00 |
| 70/30, keep | 15.33% | -3.53% (0.38%) | -0.58 | -1.24 |
| 70/30, 20% to bills at quit | 11.59% | -7.26% (0.41%) | -0.58 | -1.24 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.31% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.62% | -2.69% (0.17%) | +0.00 | +0.00 |
| 70/30, keep | 10.65% | -1.66% (0.36%) | -0.17 | -0.25 |
| 70/30, 20% to bills at quit | 7.96% | -4.35% (0.39%) | -0.17 | -0.25 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.86% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 14.93% | -3.93% (0.20%) | +0.00 | +0.00 |
| 70/30, keep | 16.33% | -2.52% (0.42%) | -0.25 | -0.17 |
| 70/30, 20% to bills at quit | 12.16% | -6.69% (0.39%) | -0.25 | -0.17 |

## sample 1927-07..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 11.97% | +0.99% (0.18%) | +0.33 | +0.75 |
| 100 stocks, 20% to bills at quit | 8.94% | -2.04% (0.32%) | +0.33 | +0.75 |
| 70/30, keep | 10.98% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.85% | -3.13% (0.17%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.07% | +1.90% (0.31%) | +0.50 | +1.25 |
| 100 stocks, 20% to bills at quit | 13.91% | -2.27% (0.30%) | +0.50 | +1.25 |
| 70/30, keep | 16.17% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.27% | -3.90% (0.18%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 11.97% | +0.65% (0.19%) | +0.08 | +0.17 |
| 100 stocks, 20% to bills at quit | 8.94% | -2.38% (0.31%) | +0.08 | +0.17 |
| 70/30, keep | 11.31% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.15% | -3.17% (0.13%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.07% | +1.23% (0.39%) | +0.17 | +0.41 |
| 100 stocks, 20% to bills at quit | 13.91% | -2.94% (0.34%) | +0.17 | +0.41 |
| 70/30, keep | 16.85% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.62% | -4.23% (0.28%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.31% | +2.12% (0.36%) | +0.33 | +0.92 |
| 100 stocks, 20% to bills at quit | 9.62% | -0.57% (0.33%) | +0.33 | +0.92 |
| 70/30, keep | 10.19% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.65% | -2.53% (0.16%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.86% | +3.53% (0.38%) | +0.58 | +1.24 |
| 100 stocks, 20% to bills at quit | 14.93% | -0.40% (0.38%) | +0.58 | +1.24 |
| 70/30, keep | 15.33% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 11.59% | -3.73% (0.24%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.31% | +1.66% (0.36%) | +0.17 | +0.25 |
| 100 stocks, 20% to bills at quit | 9.62% | -1.03% (0.31%) | +0.17 | +0.25 |
| 70/30, keep | 10.65% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.96% | -2.68% (0.14%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.86% | +2.52% (0.42%) | +0.25 | +0.17 |
| 100 stocks, 20% to bills at quit | 14.93% | -1.41% (0.38%) | +0.25 | +0.17 |
| 70/30, keep | 16.33% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.16% | -4.17% (0.27%) | +0.00 | +0.00 |

# Engine output: config-v2-q2-stress095-seed2.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.4 | 73.7 | +0.79 (0.08) tie | +1.02 (0.10) | +1.25 (0.13) | 3.0% | 7758 | 12.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.4 | 73.7 | +0.79 (0.08) tie | +1.02 (0.10) | +1.25 (0.13) | 3.0% | 7758 | 9.0% | 0.0% |
| 70/30, keep | 60.1 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7775 | 10.9% | 0.4% |
| 70/30, 20% to bills at quit | 60.1 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7775 | 8.0% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.0%), k=0.75: 70/30, 20% to bills at quit (8.0%), k=1.00: 70/30, 20% to bills at quit (8.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 81.4 | +1.04 (0.14) | +1.31 (0.21) | +1.57 (0.27) | 7.6% | 7390 | 18.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 81.4 | +1.04 (0.14) | +1.31 (0.21) | +1.57 (0.27) | 7.6% | 7390 | 14.0% | 0.0% |
| 70/30, keep | 62.8 | 80.3 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7432 | 16.7% | 0.4% |
| 70/30, 20% to bills at quit | 62.8 | 80.3 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7432 | 12.3% | 0.4% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.3%), k=0.75: 70/30, 20% to bills at quit (12.3%), k=1.00: 70/30, 20% to bills at quit (12.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.4 | 73.7 | +0.29 (0.07) tie | +0.35 (0.11) tie | +0.42 (0.14) tie | 3.0% | 7758 | 12.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.4 | 73.7 | +0.29 (0.07) tie | +0.35 (0.11) tie | +0.42 (0.14) tie | 3.0% | 7758 | 9.0% | 0.0% |
| 70/30, keep | 60.2 | 73.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 3.1% | 7751 | 11.3% | 0.4% |
| 70/30, 20% to bills at quit | 60.2 | 73.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 3.1% | 7751 | 8.6% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.6%), k=0.75: 70/30, 20% to bills at quit (8.6%), k=1.00: 70/30, 20% to bills at quit (8.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 81.4 | +0.12 (0.15) tie | +0.10 (0.21) tie | +0.08 (0.28) tie | 7.6% | 7390 | 18.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 81.4 | +0.12 (0.15) tie | +0.10 (0.21) tie | +0.08 (0.28) tie | 7.6% | 7390 | 14.0% | 0.0% |
| 70/30, keep | 63.1 | 81.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.8% | 7375 | 17.0% | 0.4% |
| 70/30, 20% to bills at quit | 63.1 | 81.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.8% | 7375 | 12.6% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.6%), k=0.75: 70/30, 20% to bills at quit (12.6%), k=1.00: 70/30, 20% to bills at quit (12.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.3 | 74.1 | +0.83 (0.08) tie | +1.08 (0.11) | +1.32 (0.14) | 2.9% | 7771 | 13.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.3 | 74.1 | +0.83 (0.08) tie | +1.08 (0.11) | +1.32 (0.14) | 2.9% | 7771 | 9.9% | 0.0% |
| 70/30, keep | 60.0 | 73.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7779 | 10.2% | 0.7% |
| 70/30, 20% to bills at quit | 60.0 | 73.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7779 | 8.0% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.0%), k=0.75: 70/30, 20% to bills at quit (8.0%), k=1.00: 70/30, 20% to bills at quit (8.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 81.8 | +1.16 (0.21) | +1.49 (0.29) | +1.82 (0.36) | 7.8% | 7376 | 18.9% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 81.8 | +1.16 (0.21) | +1.49 (0.29) | +1.82 (0.36) | 7.8% | 7376 | 15.1% | 0.0% |
| 70/30, keep | 62.7 | 80.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.0% | 7438 | 15.6% | 0.7% |
| 70/30, 20% to bills at quit | 62.7 | 80.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.0% | 7438 | 12.0% | 0.7% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.0%), k=0.75: 70/30, 20% to bills at quit (12.0%), k=1.00: 70/30, 20% to bills at quit (12.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.3 | 74.1 | +0.29 (0.09) tie | +0.40 (0.12) tie | +0.50 (0.15) tie | 2.9% | 7771 | 13.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.3 | 74.1 | +0.29 (0.09) tie | +0.40 (0.12) tie | +0.50 (0.15) tie | 2.9% | 7771 | 9.9% | 0.0% |
| 70/30, keep | 60.2 | 73.7 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 3.0% | 7758 | 10.7% | 0.6% |
| 70/30, 20% to bills at quit | 60.2 | 73.7 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 3.0% | 7758 | 8.2% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.2%), k=0.75: 70/30, 20% to bills at quit (8.2%), k=1.00: 70/30, 20% to bills at quit (8.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 81.8 | +0.38 (0.21) tie | +0.48 (0.27) tie | +0.58 (0.34) tie | 7.8% | 7376 | 18.9% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 81.8 | +0.38 (0.21) tie | +0.48 (0.27) tie | +0.58 (0.34) tie | 7.8% | 7376 | 15.1% | 0.0% |
| 70/30, keep | 63.0 | 81.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.7% | 7386 | 16.4% | 0.6% |
| 70/30, 20% to bills at quit | 63.0 | 81.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.7% | 7386 | 12.4% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.4%), k=0.75: 70/30, 20% to bills at quit (12.4%), k=1.00: 70/30, 20% to bills at quit (12.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 4/8 | 4/8 | 6/8 | 4/8 | 4/8 |
| 100 stocks, 20% to bills at quit | 6/8 | 4/8 | 4/8 | 0/8 | 0/8 | 0/8 |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2/8 | 4/8 | 4/8 |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 0/8 | 0/8 | 0/8 |

## Paired run-out vs keeping the same base mix (runout_paired.py). Read rows of the same base mix only.

## sample 1927-07..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.14% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 8.98% | -3.16% (0.15%) | +0.00 | +0.00 |
| 70/30, keep | 10.87% | -1.27% (0.23%) | -0.33 | -0.92 |
| 70/30, 20% to bills at quit | 8.04% | -4.10% (0.23%) | -0.33 | -0.92 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.96% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.95% | -4.01% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 16.67% | -1.29% (0.24%) | -0.50 | -1.07 |
| 70/30, 20% to bills at quit | 12.31% | -5.65% (0.32%) | -0.50 | -1.07 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.14% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 8.98% | -3.16% (0.15%) | +0.00 | +0.00 |
| 70/30, keep | 11.33% | -0.81% (0.25%) | -0.17 | -0.25 |
| 70/30, 20% to bills at quit | 8.55% | -3.59% (0.19%) | -0.17 | -0.25 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.96% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.95% | -4.01% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 16.96% | -0.99% (0.26%) | -0.17 | +0.08 |
| 70/30, 20% to bills at quit | 12.58% | -5.37% (0.30%) | -0.17 | +0.08 |

## sample 1990-01..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.01% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.95% | -3.06% (0.19%) | +0.00 | +0.00 |
| 70/30, keep | 10.25% | -2.76% (0.29%) | -0.33 | -0.99 |
| 70/30, 20% to bills at quit | 8.00% | -5.01% (0.28%) | -0.33 | -0.99 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.93% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.08% | -3.85% (0.14%) | +0.00 | +0.00 |
| 70/30, keep | 15.57% | -3.36% (0.37%) | -0.50 | -1.32 |
| 70/30, 20% to bills at quit | 12.02% | -6.91% (0.33%) | -0.50 | -1.32 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.01% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.95% | -3.06% (0.19%) | +0.00 | +0.00 |
| 70/30, keep | 10.71% | -2.30% (0.29%) | -0.08 | -0.42 |
| 70/30, 20% to bills at quit | 8.21% | -4.80% (0.30%) | -0.08 | -0.42 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.93% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.08% | -3.85% (0.14%) | +0.00 | +0.00 |
| 70/30, keep | 16.38% | -2.54% (0.35%) | -0.17 | -0.42 |
| 70/30, 20% to bills at quit | 12.40% | -6.52% (0.38%) | -0.17 | -0.42 |

## sample 1927-07..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.14% | +1.27% (0.23%) | +0.33 | +0.92 |
| 100 stocks, 20% to bills at quit | 8.98% | -1.88% (0.27%) | +0.33 | +0.92 |
| 70/30, keep | 10.87% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.04% | -2.83% (0.20%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.96% | +1.29% (0.24%) | +0.50 | +1.07 |
| 100 stocks, 20% to bills at quit | 13.95% | -2.72% (0.29%) | +0.50 | +1.07 |
| 70/30, keep | 16.67% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.31% | -4.36% (0.25%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.14% | +0.81% (0.25%) | +0.17 | +0.25 |
| 100 stocks, 20% to bills at quit | 8.98% | -2.34% (0.31%) | +0.17 | +0.25 |
| 70/30, keep | 11.33% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.55% | -2.77% (0.17%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.96% | +0.99% (0.26%) | +0.17 | -0.08 |
| 100 stocks, 20% to bills at quit | 13.95% | -3.01% (0.29%) | +0.17 | -0.08 |
| 70/30, keep | 16.96% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.58% | -4.38% (0.28%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.01% | +2.76% (0.29%) | +0.33 | +0.99 |
| 100 stocks, 20% to bills at quit | 9.95% | -0.30% (0.30%) | +0.33 | +0.99 |
| 70/30, keep | 10.25% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.00% | -2.25% (0.16%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.93% | +3.36% (0.37%) | +0.50 | +1.32 |
| 100 stocks, 20% to bills at quit | 15.08% | -0.49% (0.35%) | +0.50 | +1.32 |
| 70/30, keep | 15.57% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.02% | -3.55% (0.19%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.01% | +2.30% (0.29%) | +0.08 | +0.42 |
| 100 stocks, 20% to bills at quit | 9.95% | -0.76% (0.28%) | +0.08 | +0.42 |
| 70/30, keep | 10.71% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.21% | -2.50% (0.18%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.93% | +2.54% (0.35%) | +0.17 | +0.42 |
| 100 stocks, 20% to bills at quit | 15.08% | -1.31% (0.34%) | +0.17 | +0.42 |
| 70/30, keep | 16.38% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.40% | -3.98% (0.27%) | +0.00 | +0.00 |

# Engine output: config-v2-q2-stress095-seed3.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.4 | 74.3 | +0.79 (0.10) tie | +1.02 (0.14) | +1.25 (0.18) | 3.1% | 7751 | 12.2% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.4 | 74.3 | +0.79 (0.10) tie | +1.02 (0.14) | +1.25 (0.18) | 3.1% | 7751 | 9.2% | 0.0% |
| 70/30, keep | 60.1 | 73.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7779 | 10.5% | 0.4% |
| 70/30, 20% to bills at quit | 60.1 | 73.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7779 | 7.7% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.7%), k=0.75: 70/30, 20% to bills at quit (7.7%), k=1.00: 70/30, 20% to bills at quit (7.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.3 | 82.1 | +1.21 (0.14) | +1.52 (0.17) | +1.83 (0.20) | 7.8% | 7377 | 17.3% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.3 | 82.1 | +1.21 (0.14) | +1.52 (0.17) | +1.83 (0.20) | 7.8% | 7377 | 13.3% | 0.0% |
| 70/30, keep | 62.8 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7435 | 16.4% | 0.4% |
| 70/30, 20% to bills at quit | 62.8 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7435 | 12.3% | 0.4% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.3%), k=0.75: 70/30, 20% to bills at quit (12.3%), k=1.00: 70/30, 20% to bills at quit (12.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.4 | 74.3 | +0.21 (0.09) tie | +0.23 (0.13) tie | +0.25 (0.16) tie | 3.1% | 7751 | 12.2% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.4 | 74.3 | +0.21 (0.09) tie | +0.23 (0.13) tie | +0.25 (0.16) tie | 3.1% | 7751 | 9.2% | 0.0% |
| 70/30, keep | 60.2 | 74.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 3.1% | 7753 | 11.2% | 0.4% |
| 70/30, 20% to bills at quit | 60.2 | 74.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 3.1% | 7753 | 8.2% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.2%), k=0.75: 70/30, 20% to bills at quit (8.2%), k=1.00: 70/30, 20% to bills at quit (8.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.3 | 82.1 | +0.45 (0.14) tie | +0.56 (0.18) tie | +0.66 (0.22) tie | 7.8% | 7377 | 17.3% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.3 | 82.1 | +0.45 (0.14) tie | +0.56 (0.18) tie | +0.66 (0.22) tie | 7.8% | 7377 | 13.3% | 0.0% |
| 70/30, keep | 63.1 | 81.7 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.6% | 7388 | 16.7% | 0.4% |
| 70/30, 20% to bills at quit | 63.1 | 81.7 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.6% | 7388 | 13.0% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (13.0%), k=0.75: 70/30, 20% to bills at quit (13.0%), k=1.00: 70/30, 20% to bills at quit (13.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.1 | 74.0 | +0.67 (0.10) tie | +0.92 (0.15) tie | +1.17 (0.20) | 3.0% | 7760 | 12.7% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.1 | 74.0 | +0.67 (0.10) tie | +0.92 (0.15) tie | +1.17 (0.20) | 3.0% | 7760 | 10.0% | 0.0% |
| 70/30, keep | 59.9 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7792 | 10.1% | 0.7% |
| 70/30, 20% to bills at quit | 59.9 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7792 | 7.4% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.4%), k=0.75: 70/30, 20% to bills at quit (7.4%), k=1.00: 70/30, 20% to bills at quit (7.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.0 | 81.3 | +1.04 (0.16) | +1.31 (0.22) | +1.58 (0.27) | 7.4% | 7408 | 18.7% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.0 | 81.3 | +1.04 (0.16) | +1.31 (0.22) | +1.58 (0.27) | 7.4% | 7408 | 14.7% | 0.0% |
| 70/30, keep | 62.5 | 80.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.0% | 7444 | 15.5% | 0.7% |
| 70/30, 20% to bills at quit | 62.5 | 80.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.0% | 7444 | 11.7% | 0.7% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (11.7%), k=0.75: 70/30, 20% to bills at quit (11.7%), k=1.00: 70/30, 20% to bills at quit (11.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.1 | 74.0 | +0.17 (0.11) tie | +0.29 (0.16) tie | +0.42 (0.22) tie | 3.0% | 7760 | 12.7% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.1 | 74.0 | +0.17 (0.11) tie | +0.29 (0.16) tie | +0.42 (0.22) tie | 3.0% | 7760 | 10.0% | 0.0% |
| 70/30, keep | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.9% | 7772 | 10.5% | 0.6% |
| 70/30, 20% to bills at quit | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.9% | 7772 | 7.6% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.6%), k=0.75: 70/30, 20% to bills at quit (7.6%), k=1.00: 70/30, 20% to bills at quit (7.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.0 | 81.3 | +0.21 (0.15) tie | +0.24 (0.19) tie | +0.26 (0.24) tie | 7.4% | 7408 | 18.7% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.0 | 81.3 | +0.21 (0.15) tie | +0.24 (0.19) tie | +0.26 (0.24) tie | 7.4% | 7408 | 14.7% | 0.0% |
| 70/30, keep | 62.8 | 81.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.5% | 7399 | 16.2% | 0.6% |
| 70/30, 20% to bills at quit | 62.8 | 81.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.5% | 7399 | 12.2% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.2%), k=0.75: 70/30, 20% to bills at quit (12.2%), k=1.00: 70/30, 20% to bills at quit (12.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 5/8 | 4/8 | 6/8 | 5/8 | 4/8 |
| 100 stocks, 20% to bills at quit | 6/8 | 5/8 | 4/8 | 0/8 | 0/8 | 0/8 |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2/8 | 3/8 | 4/8 |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 0/8 | 0/8 | 0/8 |

## Paired run-out vs keeping the same base mix (runout_paired.py). Read rows of the same base mix only.

## sample 1927-07..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.24% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.21% | -3.03% (0.28%) | +0.00 | +0.00 |
| 70/30, keep | 10.48% | -1.77% (0.25%) | -0.33 | -0.92 |
| 70/30, 20% to bills at quit | 7.66% | -4.58% (0.27%) | -0.33 | -0.92 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.32% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.31% | -4.01% (0.23%) | +0.00 | +0.00 |
| 70/30, keep | 16.42% | -0.90% (0.33%) | -0.58 | -1.25 |
| 70/30, 20% to bills at quit | 12.32% | -5.00% (0.29%) | -0.58 | -1.25 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.24% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.21% | -3.03% (0.28%) | +0.00 | +0.00 |
| 70/30, keep | 11.18% | -1.06% (0.24%) | -0.17 | -0.08 |
| 70/30, 20% to bills at quit | 8.20% | -4.04% (0.31%) | -0.17 | -0.08 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.32% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.31% | -4.01% (0.23%) | +0.00 | +0.00 |
| 70/30, keep | 16.73% | -0.59% (0.33%) | -0.25 | -0.41 |
| 70/30, 20% to bills at quit | 13.01% | -4.32% (0.34%) | -0.25 | -0.41 |

## sample 1990-01..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.65% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 10.01% | -2.64% (0.19%) | +0.00 | +0.00 |
| 70/30, keep | 10.13% | -2.53% (0.28%) | -0.17 | -1.00 |
| 70/30, 20% to bills at quit | 7.38% | -5.28% (0.32%) | -0.17 | -1.00 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.71% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 14.74% | -3.97% (0.20%) | +0.00 | +0.00 |
| 70/30, keep | 15.52% | -3.19% (0.33%) | -0.50 | -1.08 |
| 70/30, 20% to bills at quit | 11.67% | -7.04% (0.38%) | -0.50 | -1.08 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.65% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 10.01% | -2.64% (0.19%) | +0.00 | +0.00 |
| 70/30, keep | 10.51% | -2.14% (0.28%) | +0.08 | -0.50 |
| 70/30, 20% to bills at quit | 7.63% | -5.02% (0.30%) | +0.08 | -0.50 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.71% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 14.74% | -3.97% (0.20%) | +0.00 | +0.00 |
| 70/30, keep | 16.18% | -2.53% (0.24%) | -0.17 | -0.09 |
| 70/30, 20% to bills at quit | 12.22% | -6.49% (0.24%) | -0.17 | -0.09 |

## sample 1927-07..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.24% | +1.77% (0.25%) | +0.33 | +0.92 |
| 100 stocks, 20% to bills at quit | 9.21% | -1.27% (0.33%) | +0.33 | +0.92 |
| 70/30, keep | 10.48% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.66% | -2.82% (0.16%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.32% | +0.90% (0.33%) | +0.58 | +1.25 |
| 100 stocks, 20% to bills at quit | 13.31% | -3.11% (0.34%) | +0.58 | +1.25 |
| 70/30, keep | 16.42% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.32% | -4.10% (0.25%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.24% | +1.06% (0.24%) | +0.17 | +0.08 |
| 100 stocks, 20% to bills at quit | 9.21% | -1.97% (0.35%) | +0.17 | +0.08 |
| 70/30, keep | 11.18% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.20% | -2.98% (0.23%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.32% | +0.59% (0.33%) | +0.25 | +0.41 |
| 100 stocks, 20% to bills at quit | 13.31% | -3.42% (0.32%) | +0.25 | +0.41 |
| 70/30, keep | 16.73% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 13.01% | -3.72% (0.23%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.65% | +2.53% (0.28%) | +0.17 | +1.00 |
| 100 stocks, 20% to bills at quit | 10.01% | -0.11% (0.22%) | +0.17 | +1.00 |
| 70/30, keep | 10.13% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.38% | -2.75% (0.17%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.71% | +3.19% (0.33%) | +0.50 | +1.08 |
| 100 stocks, 20% to bills at quit | 14.74% | -0.78% (0.32%) | +0.50 | +1.08 |
| 70/30, keep | 15.52% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 11.67% | -3.84% (0.22%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.65% | +2.14% (0.28%) | -0.08 | +0.50 |
| 100 stocks, 20% to bills at quit | 10.01% | -0.50% (0.21%) | -0.08 | +0.50 |
| 70/30, keep | 10.51% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.63% | -2.88% (0.20%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.71% | +2.53% (0.24%) | +0.17 | +0.09 |
| 100 stocks, 20% to bills at quit | 14.74% | -1.44% (0.27%) | +0.17 | +0.09 |
| 70/30, keep | 16.18% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.22% | -3.96% (0.16%) | +0.00 | +0.00 |

# Engine output: config-v2-q2-billsvol.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.5 | 73.7 | +0.91 (0.13) tie | +1.20 (0.17) | +1.49 (0.22) | 2.6% | 7789 | 12.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.5 | 73.7 | +0.91 (0.13) tie | +1.20 (0.17) | +1.49 (0.22) | 2.6% | 7789 | 9.0% | 0.0% |
| 70/30, keep | 60.2 | 72.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.2% | 7821 | 10.7% | 0.4% |
| 70/30, 20% to bills at quit | 60.2 | 72.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.2% | 7821 | 7.7% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.7%), k=0.75: 70/30, 20% to bills at quit (7.7%), k=1.00: 70/30, 20% to bills at quit (7.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.3 | 81.6 | +1.33 (0.13) | +1.75 (0.19) | +2.17 (0.25) | 7.6% | 7392 | 18.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.3 | 81.6 | +1.33 (0.13) | +1.75 (0.19) | +2.17 (0.25) | 7.6% | 7392 | 14.1% | 0.0% |
| 70/30, keep | 62.8 | 79.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.4% | 7486 | 16.2% | 0.4% |
| 70/30, 20% to bills at quit | 62.8 | 79.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.4% | 7486 | 12.2% | 0.4% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.2%), k=0.75: 70/30, 20% to bills at quit (12.2%), k=1.00: 70/30, 20% to bills at quit (12.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.5 | 73.7 | +0.29 (0.11) tie | +0.40 (0.15) tie | +0.50 (0.20) tie | 2.6% | 7789 | 12.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.5 | 73.7 | +0.29 (0.11) tie | +0.40 (0.15) tie | +0.50 (0.20) tie | 2.6% | 7789 | 9.0% | 0.0% |
| 70/30, keep | 60.4 | 73.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7792 | 11.0% | 0.4% |
| 70/30, 20% to bills at quit | 60.4 | 73.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7792 | 8.0% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.0%), k=0.75: 70/30, 20% to bills at quit (8.0%), k=1.00: 70/30, 20% to bills at quit (8.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.3 | 81.6 | +0.62 (0.17) tie | +0.85 (0.23) tie | +1.08 (0.29) | 7.6% | 7392 | 18.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.3 | 81.6 | +0.62 (0.17) tie | +0.85 (0.23) tie | +1.08 (0.29) | 7.6% | 7392 | 14.1% | 0.0% |
| 70/30, keep | 63.2 | 80.7 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7433 | 16.6% | 0.4% |
| 70/30, 20% to bills at quit | 63.2 | 80.7 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7433 | 12.7% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.7%), k=0.75: 70/30, 20% to bills at quit (12.7%), k=1.00: 70/30, 20% to bills at quit (12.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.2 | 73.8 | +0.88 (0.11) tie | +1.12 (0.16) | +1.38 (0.21) | 3.3% | 7735 | 12.3% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.2 | 73.8 | +0.88 (0.11) tie | +1.12 (0.16) | +1.38 (0.21) | 3.3% | 7735 | 9.5% | 0.0% |
| 70/30, keep | 59.9 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7791 | 10.2% | 0.6% |
| 70/30, 20% to bills at quit | 59.9 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7791 | 7.4% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.4%), k=0.75: 70/30, 20% to bills at quit (7.4%), k=1.00: 70/30, 20% to bills at quit (7.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 82.1 | +1.63 (0.14) | +2.10 (0.21) | +2.58 (0.28) | 8.1% | 7356 | 18.9% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 82.1 | +1.63 (0.14) | +2.10 (0.21) | +2.58 (0.28) | 8.1% | 7356 | 14.8% | 0.0% |
| 70/30, keep | 62.5 | 80.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.7% | 7466 | 15.6% | 0.7% |
| 70/30, 20% to bills at quit | 62.5 | 80.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.7% | 7466 | 11.7% | 0.7% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (11.7%), k=0.75: 70/30, 20% to bills at quit (11.7%), k=1.00: 70/30, 20% to bills at quit (11.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.2 | 73.8 | +0.46 (0.09) tie | +0.60 (0.12) tie | +0.75 (0.16) tie | 3.3% | 7735 | 12.3% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.2 | 73.8 | +0.46 (0.09) tie | +0.60 (0.12) tie | +0.75 (0.16) tie | 3.3% | 7735 | 9.5% | 0.0% |
| 70/30, keep | 60.1 | 73.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7776 | 10.7% | 0.6% |
| 70/30, 20% to bills at quit | 60.1 | 73.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7776 | 7.9% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.9%), k=0.75: 70/30, 20% to bills at quit (7.9%), k=1.00: 70/30, 20% to bills at quit (7.9%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 82.1 | +0.88 (0.14) tie | +1.15 (0.21) | +1.42 (0.28) | 8.1% | 7356 | 18.9% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 82.1 | +0.88 (0.14) tie | +1.15 (0.21) | +1.42 (0.28) | 8.1% | 7356 | 14.8% | 0.0% |
| 70/30, keep | 62.8 | 81.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7415 | 16.4% | 0.6% |
| 70/30, 20% to bills at quit | 62.8 | 81.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7415 | 12.3% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.3%), k=0.75: 70/30, 20% to bills at quit (12.3%), k=1.00: 70/30, 20% to bills at quit (12.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 3/8 | 2/8 | 6/8 | 3/8 | 2/8 |
| 100 stocks, 20% to bills at quit | 6/8 | 3/8 | 2/8 | 0/8 | 0/8 | 0/8 |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2/8 | 5/8 | 6/8 |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 0/8 | 0/8 | 0/8 |

## Paired run-out vs keeping the same base mix (runout_paired.py). Read rows of the same base mix only.

## sample 1927-07..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 11.97% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.01% | -2.95% (0.24%) | +0.00 | +0.00 |
| 70/30, keep | 10.65% | -1.31% (0.19%) | -0.33 | -1.16 |
| 70/30, 20% to bills at quit | 7.68% | -4.28% (0.24%) | -0.33 | -1.16 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.07% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 14.12% | -3.95% (0.23%) | +0.00 | +0.00 |
| 70/30, keep | 16.15% | -1.92% (0.32%) | -0.50 | -1.67 |
| 70/30, 20% to bills at quit | 12.25% | -5.82% (0.25%) | -0.50 | -1.67 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 11.97% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.01% | -2.95% (0.24%) | +0.00 | +0.00 |
| 70/30, keep | 11.02% | -0.94% (0.17%) | -0.08 | -0.42 |
| 70/30, 20% to bills at quit | 8.00% | -3.97% (0.25%) | -0.08 | -0.42 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.07% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 14.12% | -3.95% (0.23%) | +0.00 | +0.00 |
| 70/30, keep | 16.59% | -1.49% (0.34%) | -0.17 | -0.92 |
| 70/30, 20% to bills at quit | 12.66% | -5.41% (0.35%) | -0.17 | -0.92 |

## sample 1990-01..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.31% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.45% | -2.86% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 10.24% | -2.07% (0.36%) | -0.38 | -1.00 |
| 70/30, 20% to bills at quit | 7.35% | -4.95% (0.42%) | -0.38 | -1.00 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.86% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 14.80% | -4.05% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 15.63% | -3.22% (0.37%) | -0.67 | -1.92 |
| 70/30, 20% to bills at quit | 11.75% | -7.11% (0.40%) | -0.67 | -1.92 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.31% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.45% | -2.86% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 10.69% | -1.62% (0.41%) | -0.17 | -0.58 |
| 70/30, 20% to bills at quit | 7.87% | -4.44% (0.46%) | -0.17 | -0.58 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.86% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 14.80% | -4.05% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 16.44% | -2.42% (0.32%) | -0.33 | -1.08 |
| 70/30, 20% to bills at quit | 12.33% | -6.53% (0.40%) | -0.33 | -1.08 |

## sample 1927-07..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 11.97% | +1.31% (0.19%) | +0.33 | +1.16 |
| 100 stocks, 20% to bills at quit | 9.01% | -1.64% (0.31%) | +0.33 | +1.16 |
| 70/30, keep | 10.65% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.68% | -2.97% (0.17%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.07% | +1.92% (0.32%) | +0.50 | +1.67 |
| 100 stocks, 20% to bills at quit | 14.12% | -2.03% (0.20%) | +0.50 | +1.67 |
| 70/30, keep | 16.15% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.25% | -3.90% (0.23%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 11.97% | +0.94% (0.17%) | +0.08 | +0.42 |
| 100 stocks, 20% to bills at quit | 9.01% | -2.01% (0.28%) | +0.08 | +0.42 |
| 70/30, keep | 11.02% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.00% | -3.03% (0.20%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.07% | +1.49% (0.34%) | +0.17 | +0.92 |
| 100 stocks, 20% to bills at quit | 14.12% | -2.46% (0.20%) | +0.17 | +0.92 |
| 70/30, keep | 16.59% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.66% | -3.93% (0.20%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.31% | +2.07% (0.36%) | +0.38 | +1.00 |
| 100 stocks, 20% to bills at quit | 9.45% | -0.79% (0.33%) | +0.38 | +1.00 |
| 70/30, keep | 10.24% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.35% | -2.89% (0.24%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.86% | +3.22% (0.37%) | +0.67 | +1.92 |
| 100 stocks, 20% to bills at quit | 14.80% | -0.83% (0.33%) | +0.67 | +1.92 |
| 70/30, keep | 15.63% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 11.75% | -3.88% (0.21%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.31% | +1.62% (0.41%) | +0.17 | +0.58 |
| 100 stocks, 20% to bills at quit | 9.45% | -1.24% (0.40%) | +0.17 | +0.58 |
| 70/30, keep | 10.69% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.87% | -2.82% (0.22%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.86% | +2.42% (0.32%) | +0.33 | +1.08 |
| 100 stocks, 20% to bills at quit | 14.80% | -1.64% (0.30%) | +0.33 | +1.08 |
| 70/30, keep | 16.44% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.33% | -4.11% (0.23%) | +0.00 | +0.00 |

# Engine output: config-v2-q2-billsvol-seed2.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.4 | 73.7 | +0.95 (0.10) tie | +1.26 (0.14) | +1.57 (0.18) | 3.0% | 7758 | 12.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.4 | 73.7 | +0.95 (0.10) tie | +1.26 (0.14) | +1.57 (0.18) | 3.0% | 7758 | 9.0% | 0.0% |
| 70/30, keep | 60.1 | 72.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7791 | 10.7% | 0.4% |
| 70/30, 20% to bills at quit | 60.1 | 72.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7791 | 7.8% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.8%), k=0.75: 70/30, 20% to bills at quit (7.8%), k=1.00: 70/30, 20% to bills at quit (7.8%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 81.4 | +1.33 (0.15) | +1.75 (0.21) | +2.17 (0.27) | 7.6% | 7390 | 18.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 81.4 | +1.33 (0.15) | +1.75 (0.21) | +2.17 (0.27) | 7.6% | 7390 | 14.0% | 0.0% |
| 70/30, keep | 62.8 | 79.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7481 | 16.4% | 0.4% |
| 70/30, 20% to bills at quit | 62.8 | 79.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7481 | 12.1% | 0.4% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.1%), k=0.75: 70/30, 20% to bills at quit (12.1%), k=1.00: 70/30, 20% to bills at quit (12.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.4 | 73.7 | +0.42 (0.08) tie | +0.58 (0.12) tie | +0.75 (0.16) tie | 3.0% | 7758 | 12.1% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.4 | 73.7 | +0.42 (0.08) tie | +0.58 (0.12) tie | +0.75 (0.16) tie | 3.0% | 7758 | 9.0% | 0.0% |
| 70/30, keep | 60.3 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7775 | 11.2% | 0.4% |
| 70/30, 20% to bills at quit | 60.3 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7775 | 8.3% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.3%), k=0.75: 70/30, 20% to bills at quit (8.3%), k=1.00: 70/30, 20% to bills at quit (8.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 81.4 | +0.45 (0.16) tie | +0.60 (0.23) tie | +0.74 (0.31) tie | 7.6% | 7390 | 18.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 81.4 | +0.45 (0.16) tie | +0.60 (0.23) tie | +0.74 (0.31) tie | 7.6% | 7390 | 14.0% | 0.0% |
| 70/30, keep | 63.1 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7431 | 17.1% | 0.4% |
| 70/30, 20% to bills at quit | 63.1 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7431 | 12.6% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.6%), k=0.75: 70/30, 20% to bills at quit (12.6%), k=1.00: 70/30, 20% to bills at quit (12.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.3 | 74.1 | +0.92 (0.11) tie | +1.21 (0.15) | +1.50 (0.20) | 2.9% | 7771 | 13.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.3 | 74.1 | +0.92 (0.11) tie | +1.21 (0.15) | +1.50 (0.20) | 2.9% | 7771 | 10.0% | 0.0% |
| 70/30, keep | 60.0 | 72.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.7% | 7784 | 10.4% | 0.7% |
| 70/30, 20% to bills at quit | 60.0 | 72.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.7% | 7784 | 7.6% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.6%), k=0.75: 70/30, 20% to bills at quit (7.6%), k=1.00: 70/30, 20% to bills at quit (7.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 81.8 | +1.41 (0.20) | +1.89 (0.28) | +2.37 (0.35) | 7.8% | 7376 | 18.9% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 81.8 | +1.41 (0.20) | +1.89 (0.28) | +2.37 (0.35) | 7.8% | 7376 | 15.1% | 0.0% |
| 70/30, keep | 62.7 | 79.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.6% | 7471 | 15.8% | 0.7% |
| 70/30, 20% to bills at quit | 62.7 | 79.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.6% | 7471 | 12.0% | 0.7% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.0%), k=0.75: 70/30, 20% to bills at quit (12.0%), k=1.00: 70/30, 20% to bills at quit (12.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.3 | 74.1 | +0.46 (0.10) tie | +0.60 (0.14) tie | +0.75 (0.19) tie | 2.9% | 7771 | 13.0% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.3 | 74.1 | +0.46 (0.10) tie | +0.60 (0.14) tie | +0.75 (0.19) tie | 2.9% | 7771 | 10.0% | 0.0% |
| 70/30, keep | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.9% | 7769 | 10.8% | 0.6% |
| 70/30, 20% to bills at quit | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.9% | 7769 | 8.2% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.2%), k=0.75: 70/30, 20% to bills at quit (8.2%), k=1.00: 70/30, 20% to bills at quit (8.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.2 | 81.8 | +0.70 (0.19) tie | +0.97 (0.26) tie | +1.24 (0.33) | 7.8% | 7376 | 18.9% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.2 | 81.8 | +0.70 (0.19) tie | +0.97 (0.26) tie | +1.24 (0.33) | 7.8% | 7376 | 15.1% | 0.0% |
| 70/30, keep | 63.0 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.2% | 7426 | 16.3% | 0.6% |
| 70/30, 20% to bills at quit | 63.0 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.2% | 7426 | 12.7% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.7%), k=0.75: 70/30, 20% to bills at quit (12.7%), k=1.00: 70/30, 20% to bills at quit (12.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks, keep | 6/8 | 4/8 | 3/8 | 6/8 | 4/8 | 3/8 |
| 100 stocks, 20% to bills at quit | 6/8 | 4/8 | 3/8 | 0/8 | 0/8 | 0/8 |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 2/8 | 4/8 | 5/8 |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 0/8 | 0/8 | 0/8 |

## Paired run-out vs keeping the same base mix (runout_paired.py). Read rows of the same base mix only.

## sample 1927-07..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.14% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.05% | -3.09% (0.18%) | +0.00 | +0.00 |
| 70/30, keep | 10.67% | -1.48% (0.26%) | -0.33 | -1.24 |
| 70/30, 20% to bills at quit | 7.83% | -4.31% (0.16%) | -0.33 | -1.24 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.96% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.99% | -3.96% (0.22%) | +0.00 | +0.00 |
| 70/30, keep | 16.39% | -1.57% (0.31%) | -0.50 | -1.67 |
| 70/30, 20% to bills at quit | 12.07% | -5.89% (0.33%) | -0.50 | -1.67 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.14% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.05% | -3.09% (0.18%) | +0.00 | +0.00 |
| 70/30, keep | 11.16% | -0.98% (0.18%) | -0.08 | -0.67 |
| 70/30, 20% to bills at quit | 8.30% | -3.85% (0.14%) | -0.08 | -0.67 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.96% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.99% | -3.96% (0.22%) | +0.00 | +0.00 |
| 70/30, keep | 17.06% | -0.89% (0.25%) | -0.17 | -0.57 |
| 70/30, 20% to bills at quit | 12.58% | -5.37% (0.30%) | -0.17 | -0.57 |

## sample 1990-01..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.01% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 10.01% | -3.00% (0.17%) | +0.00 | +0.00 |
| 70/30, keep | 10.38% | -2.63% (0.29%) | -0.33 | -1.17 |
| 70/30, 20% to bills at quit | 7.64% | -5.37% (0.34%) | -0.33 | -1.17 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.93% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.10% | -3.82% (0.14%) | +0.00 | +0.00 |
| 70/30, keep | 15.77% | -3.16% (0.44%) | -0.46 | -1.91 |
| 70/30, 20% to bills at quit | 12.03% | -6.89% (0.38%) | -0.46 | -1.91 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.01% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 10.01% | -3.00% (0.17%) | +0.00 | +0.00 |
| 70/30, keep | 10.79% | -2.22% (0.33%) | -0.17 | -0.58 |
| 70/30, 20% to bills at quit | 8.19% | -4.82% (0.34%) | -0.17 | -0.58 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.93% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 15.10% | -3.82% (0.14%) | +0.00 | +0.00 |
| 70/30, keep | 16.35% | -2.58% (0.44%) | -0.17 | -1.07 |
| 70/30, 20% to bills at quit | 12.67% | -6.25% (0.40%) | -0.17 | -1.07 |

## sample 1927-07..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.14% | +1.48% (0.26%) | +0.33 | +1.24 |
| 100 stocks, 20% to bills at quit | 9.05% | -1.62% (0.29%) | +0.33 | +1.24 |
| 70/30, keep | 10.67% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.83% | -2.84% (0.20%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.96% | +1.57% (0.31%) | +0.50 | +1.67 |
| 100 stocks, 20% to bills at quit | 13.99% | -2.40% (0.33%) | +0.50 | +1.67 |
| 70/30, keep | 16.39% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.07% | -4.32% (0.16%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.14% | +0.98% (0.18%) | +0.08 | +0.67 |
| 100 stocks, 20% to bills at quit | 9.05% | -2.12% (0.27%) | +0.08 | +0.67 |
| 70/30, keep | 11.16% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.30% | -2.87% (0.13%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.96% | +0.89% (0.25%) | +0.17 | +0.57 |
| 100 stocks, 20% to bills at quit | 13.99% | -3.07% (0.29%) | +0.17 | +0.57 |
| 70/30, keep | 17.06% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.58% | -4.48% (0.20%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.01% | +2.63% (0.29%) | +0.33 | +1.17 |
| 100 stocks, 20% to bills at quit | 10.01% | -0.37% (0.25%) | +0.33 | +1.17 |
| 70/30, keep | 10.38% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.64% | -2.74% (0.20%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.93% | +3.16% (0.44%) | +0.46 | +1.91 |
| 100 stocks, 20% to bills at quit | 15.10% | -0.66% (0.37%) | +0.46 | +1.91 |
| 70/30, keep | 15.77% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.03% | -3.73% (0.25%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 13.01% | +2.22% (0.33%) | +0.17 | +0.58 |
| 100 stocks, 20% to bills at quit | 10.01% | -0.77% (0.30%) | +0.17 | +0.58 |
| 70/30, keep | 10.79% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.19% | -2.60% (0.21%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.93% | +2.58% (0.44%) | +0.17 | +1.07 |
| 100 stocks, 20% to bills at quit | 15.10% | -1.24% (0.40%) | +0.17 | +1.07 |
| 70/30, keep | 16.35% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.67% | -3.68% (0.25%) | +0.00 | +0.00 |

# Engine output: config-v2-q2-billsvol-seed3.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.4 | 74.3 | +1.00 (0.10) | +1.33 (0.14) | +1.67 (0.18) | 3.1% | 7751 | 12.2% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.4 | 74.3 | +1.00 (0.10) | +1.33 (0.14) | +1.67 (0.18) | 3.1% | 7751 | 9.3% | 0.0% |
| 70/30, keep | 60.1 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.5% | 7803 | 10.6% | 0.4% |
| 70/30, 20% to bills at quit | 60.1 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.5% | 7803 | 7.6% | 0.4% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.6%), k=0.75: 70/30, 20% to bills at quit (7.6%), k=1.00: 70/30, 20% to bills at quit (7.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.3 | 82.1 | +1.67 (0.13) | +2.17 (0.17) | +2.67 (0.21) | 7.8% | 7377 | 17.3% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.3 | 82.1 | +1.67 (0.13) | +2.17 (0.17) | +2.67 (0.21) | 7.8% | 7377 | 13.5% | 0.0% |
| 70/30, keep | 62.7 | 80.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.6% | 7476 | 16.5% | 0.4% |
| 70/30, 20% to bills at quit | 62.7 | 80.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.6% | 7476 | 12.6% | 0.4% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.6%), k=0.75: 70/30, 20% to bills at quit (12.6%), k=1.00: 70/30, 20% to bills at quit (12.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.4 | 74.3 | +0.58 (0.10) tie | +0.79 (0.14) tie | +1.00 (0.18) tie | 3.1% | 7751 | 12.2% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.4 | 74.3 | +0.58 (0.10) tie | +0.79 (0.14) tie | +1.00 (0.18) tie | 3.1% | 7751 | 9.3% | 0.0% |
| 70/30, keep | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7778 | 11.1% | 0.4% |
| 70/30, 20% to bills at quit | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7778 | 8.0% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (8.0%), k=0.75: 70/30, 20% to bills at quit (8.0%), k=1.00: 70/30, 20% to bills at quit (8.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.3 | 82.1 | +0.75 (0.13) tie | +1.00 (0.17) tie | +1.25 (0.21) | 7.8% | 7377 | 17.3% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.3 | 82.1 | +0.75 (0.13) tie | +1.00 (0.17) tie | +1.25 (0.21) | 7.8% | 7377 | 13.5% | 0.0% |
| 70/30, keep | 63.1 | 81.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7419 | 16.7% | 0.4% |
| 70/30, 20% to bills at quit | 63.1 | 81.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7419 | 12.7% | 0.4% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.7%), k=0.75: 70/30, 20% to bills at quit (12.7%), k=1.00: 70/30, 20% to bills at quit (12.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.1 | 74.0 | +0.79 (0.11) tie | +1.10 (0.15) | +1.42 (0.20) | 3.0% | 7760 | 12.7% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.1 | 74.0 | +0.79 (0.11) tie | +1.10 (0.15) | +1.42 (0.20) | 3.0% | 7760 | 9.9% | 0.0% |
| 70/30, keep | 59.9 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.4% | 7810 | 9.8% | 0.7% |
| 70/30, 20% to bills at quit | 59.9 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.4% | 7810 | 7.5% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.5%), k=0.75: 70/30, 20% to bills at quit (7.5%), k=1.00: 70/30, 20% to bills at quit (7.5%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.0 | 81.3 | +1.25 (0.17) | +1.62 (0.23) | +2.00 (0.30) | 7.4% | 7408 | 18.7% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.0 | 81.3 | +1.25 (0.17) | +1.62 (0.23) | +2.00 (0.30) | 7.4% | 7408 | 14.7% | 0.0% |
| 70/30, keep | 62.5 | 79.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7481 | 15.4% | 0.7% |
| 70/30, 20% to bills at quit | 62.5 | 79.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7481 | 11.5% | 0.7% |
Simplest within the tie band: k=0.50: 70/30, keep, k=0.75: 70/30, keep, k=1.00: 70/30, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (11.5%), k=0.75: 70/30, 20% to bills at quit (11.5%), k=1.00: 70/30, 20% to bills at quit (11.5%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 60.1 | 74.0 | +0.29 (0.12) tie | +0.44 (0.17) tie | +0.58 (0.22) tie | 3.0% | 7760 | 12.7% | 0.0% |
| 100 stocks, 20% to bills at quit | 60.1 | 74.0 | +0.29 (0.12) tie | +0.44 (0.17) tie | +0.58 (0.22) tie | 3.0% | 7760 | 9.9% | 0.0% |
| 70/30, keep | 60.1 | 73.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7789 | 10.4% | 0.6% |
| 70/30, 20% to bills at quit | 60.1 | 73.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7789 | 7.6% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (7.6%), k=0.75: 70/30, 20% to bills at quit (7.6%), k=1.00: 70/30, 20% to bills at quit (7.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks, keep | 63.0 | 81.3 | +0.55 (0.17) tie | +0.74 (0.22) tie | +0.93 (0.27) tie | 7.4% | 7408 | 18.7% | 0.0% |
| 100 stocks, 20% to bills at quit | 63.0 | 81.3 | +0.55 (0.17) tie | +0.74 (0.22) tie | +0.93 (0.27) tie | 7.4% | 7408 | 14.7% | 0.0% |
| 70/30, keep | 62.8 | 80.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.0% | 7437 | 16.1% | 0.6% |
| 70/30, 20% to bills at quit | 62.8 | 80.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.0% | 7437 | 12.0% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, keep, k=0.75: 100 stocks, keep, k=1.00: 100 stocks, keep
Lowest run-out within the tie band: k=0.50: 70/30, 20% to bills at quit (12.0%), k=0.75: 70/30, 20% to bills at quit (12.0%), k=1.00: 70/30, 20% to bills at quit (12.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks, keep | 5/8 | 4/8 | 3/8 | 5/8 | 4/8 | 3/8 |
| 100 stocks, 20% to bills at quit | 5/8 | 4/8 | 3/8 | 0/8 | 0/8 | 0/8 |
| 70/30, keep | 8/8 | 8/8 | 8/8 | 3/8 | 4/8 | 5/8 |
| 70/30, 20% to bills at quit | 8/8 | 8/8 | 8/8 | 0/8 | 0/8 | 0/8 |

## Paired run-out vs keeping the same base mix (runout_paired.py). Read rows of the same base mix only.

## sample 1927-07..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.24% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.26% | -2.98% (0.24%) | +0.00 | +0.00 |
| 70/30, keep | 10.62% | -1.62% (0.27%) | -0.33 | -1.33 |
| 70/30, 20% to bills at quit | 7.59% | -4.66% (0.29%) | -0.33 | -1.33 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.32% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.47% | -3.85% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 16.49% | -0.83% (0.33%) | -0.67 | -2.00 |
| 70/30, 20% to bills at quit | 12.57% | -4.75% (0.37%) | -0.67 | -2.00 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.24% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.26% | -2.98% (0.24%) | +0.00 | +0.00 |
| 70/30, keep | 11.11% | -1.14% (0.25%) | -0.17 | -0.83 |
| 70/30, 20% to bills at quit | 8.02% | -4.22% (0.27%) | -0.17 | -0.83 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.32% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 13.47% | -3.85% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 16.71% | -0.61% (0.34%) | -0.25 | -1.00 |
| 70/30, 20% to bills at quit | 12.72% | -4.60% (0.32%) | -0.25 | -1.00 |

## sample 1990-01..2026-09, scenario base (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.65% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.95% | -2.71% (0.20%) | +0.00 | +0.00 |
| 70/30, keep | 9.82% | -2.83% (0.25%) | -0.17 | -1.25 |
| 70/30, 20% to bills at quit | 7.54% | -5.11% (0.29%) | -0.17 | -1.25 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.71% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 14.73% | -3.98% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 15.36% | -3.35% (0.26%) | -0.50 | -1.50 |
| 70/30, 20% to bills at quit | 11.46% | -7.25% (0.34%) | -0.50 | -1.50 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.65% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 9.95% | -2.71% (0.20%) | +0.00 | +0.00 |
| 70/30, keep | 10.44% | -2.22% (0.24%) | +0.00 | -0.58 |
| 70/30, 20% to bills at quit | 7.64% | -5.02% (0.25%) | +0.00 | -0.58 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 100 stocks, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.71% | +0.00% (0.00%) | +0.00 | +0.00 |
| 100 stocks, 20% to bills at quit | 14.73% | -3.98% (0.21%) | +0.00 | +0.00 |
| 70/30, keep | 16.05% | -2.65% (0.31%) | -0.17 | -0.76 |
| 70/30, 20% to bills at quit | 11.99% | -6.72% (0.36%) | -0.17 | -0.76 |

## sample 1927-07..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.24% | +1.62% (0.27%) | +0.33 | +1.33 |
| 100 stocks, 20% to bills at quit | 9.26% | -1.36% (0.33%) | +0.33 | +1.33 |
| 70/30, keep | 10.62% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.59% | -3.04% (0.17%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.32% | +0.83% (0.33%) | +0.67 | +2.00 |
| 100 stocks, 20% to bills at quit | 13.47% | -3.02% (0.38%) | +0.67 | +2.00 |
| 70/30, keep | 16.49% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.57% | -3.92% (0.22%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.24% | +1.14% (0.25%) | +0.17 | +0.83 |
| 100 stocks, 20% to bills at quit | 9.26% | -1.84% (0.28%) | +0.17 | +0.83 |
| 70/30, keep | 11.11% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 8.02% | -3.09% (0.18%) | +0.00 | +0.00 |

## sample 1927-07..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 17.32% | +0.61% (0.34%) | +0.25 | +1.00 |
| 100 stocks, 20% to bills at quit | 13.47% | -3.24% (0.40%) | +0.25 | +1.00 |
| 70/30, keep | 16.71% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 12.72% | -3.99% (0.23%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario base (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.65% | +2.83% (0.25%) | +0.17 | +1.25 |
| 100 stocks, 20% to bills at quit | 9.95% | +0.13% (0.22%) | +0.17 | +1.25 |
| 70/30, keep | 9.82% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.54% | -2.28% (0.16%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.71% | +3.35% (0.26%) | +0.50 | +1.50 |
| 100 stocks, 20% to bills at quit | 14.73% | -0.63% (0.15%) | +0.50 | +1.50 |
| 70/30, keep | 15.36% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 11.46% | -3.90% (0.23%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 12.65% | +2.22% (0.24%) | +0.00 | +0.58 |
| 100 stocks, 20% to bills at quit | 9.95% | -0.49% (0.21%) | +0.00 | +0.58 |
| 70/30, keep | 10.44% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 7.64% | -2.80% (0.19%) | +0.00 | +0.00 |

## sample 1990-01..2026-09, scenario stocks 3% + no value premium (baseline: 70/30, keep)
| candidate | run-out | run-out minus baseline (SE) | median FI minus baseline | p90 FI minus baseline |
|---|---|---|---|---|
| 100 stocks, keep | 18.71% | +2.65% (0.31%) | +0.17 | +0.76 |
| 100 stocks, 20% to bills at quit | 14.73% | -1.33% (0.26%) | +0.17 | +0.76 |
| 70/30, keep | 16.05% | +0.00% (0.00%) | +0.00 | +0.00 |
| 70/30, 20% to bills at quit | 11.99% | -4.06% (0.25%) | +0.00 | +0.00 |
