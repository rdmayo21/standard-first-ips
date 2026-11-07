# v2 q1 engine output (Robin, fictional), 2026-11-07

Inputs: Robin's follow-up decisions (01-standard.md). Configs config-v2-q1*.toml, hashed in manifest-v2.txt before scoring. Engine: `uv run --project <repo>/plugins/standard-first-ips/skills/standard-first-ips/engine ips-engine score <config> --out v2-out/<name>.csv`. CSVs and raw text are in v2-out/. Not investment advice.

# Part A: Robin's combining rule (combine_v2.py), seeds 1-3, every variant

## variant: primary (corr 0.72)

### v2-q1.csv: rule pick = 70/30 market/value
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks | 6/8 | 3/8 | 2/8 | 2.6%-8.1% | 12.0%-18.9% |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2.2%-7.3% | 10.2%-16.6% |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 2.2%-7.1% | 8.8%-14.7% |

### v2-q1-seed2.csv: rule pick = 70/30 market/value
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks | 6/8 | 4/8 | 3/8 | 2.9%-7.8% | 12.1%-18.9% |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2.6%-7.2% | 10.4%-17.1% |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 2.6%-7.0% | 8.7%-14.3% |

### v2-q1-seed3.csv: rule pick = 70/30 market/value
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks | 6/8 | 4/8 | 3/8 | 3.0%-7.8% | 12.2%-18.7% |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2.4%-7.3% | 9.8%-16.7% |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 2.8%-6.9% | 8.6%-14.1% |

Picks across the 3 files: ['70/30 market/value', '70/30 market/value', '70/30 market/value']. Stable: True

## variant: -stress095

### v2-q1-stress095.csv: rule pick = 70/30 market/value
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks | 6/8 | 5/8 | 4/8 | 2.6%-8.1% | 12.0%-18.9% |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2.5%-7.9% | 10.2%-16.9% |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 2.2%-7.1% | 8.8%-14.7% |

### v2-q1-stress095-seed2.csv: rule pick = 70/30 market/value
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks | 6/8 | 4/8 | 4/8 | 2.9%-7.8% | 12.1%-18.9% |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2.8%-7.8% | 10.2%-17.0% |
| 80/20 market/bills | 0/8 | 0/8 | 1/8 | 2.6%-7.0% | 8.7%-14.3% |

### v2-q1-stress095-seed3.csv: rule pick = 70/30 market/value
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks | 6/8 | 5/8 | 4/8 | 3.0%-7.8% | 12.2%-18.7% |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2.6%-7.6% | 10.1%-16.7% |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 2.8%-6.9% | 8.6%-14.1% |

Picks across the 3 files: ['70/30 market/value', '70/30 market/value', '70/30 market/value']. Stable: True

## variant: -billsvol

### v2-q1-billsvol.csv: rule pick = 70/30 market/value
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks | 6/8 | 3/8 | 2/8 | 2.6%-8.1% | 12.0%-18.9% |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2.2%-7.3% | 10.2%-16.6% |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 2.2%-7.2% | 8.9%-14.7% |

### v2-q1-billsvol-seed2.csv: rule pick = 70/30 market/value
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks | 6/8 | 4/8 | 3/8 | 2.9%-7.8% | 12.1%-18.9% |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2.6%-7.2% | 10.4%-17.1% |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 2.6%-7.1% | 9.2%-14.2% |

### v2-q1-billsvol-seed3.csv: rule pick = 70/30 market/value
| candidate | in band k=0.50 | in band k=0.75 | in band k=1.00 | never reaches FI by 85 (range over cells) | run-out (range) |
|---|---|---|---|---|---|
| 100 stocks | 6/8 | 4/8 | 3/8 | 3.0%-7.8% | 12.2%-18.7% |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2.4%-7.3% | 9.8%-16.7% |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 2.8%-7.0% | 8.6%-14.2% |

Picks across the 3 files: ['70/30 market/value', '70/30 market/value', '70/30 market/value']. Stable: True

# Engine output: config-v2-q1.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.5 | 73.7 | +0.91 (0.13) tie | +1.20 (0.17) | +1.49 (0.22) | 2.6% | 7789 | 12.0% | 0.0% |
| 70/30 market/value | 60.2 | 72.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.2% | 7821 | 10.7% | 0.4% |
| 80/20 market/bills | 62.1 | 74.2 | +2.79 (0.13) | +3.22 (0.17) | +3.66 (0.22) | 2.2% | 7827 | 8.8% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.7%), k=0.75: 70/30 market/value (10.7%), k=1.00: 70/30 market/value (10.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.3 | 81.6 | +1.33 (0.13) | +1.75 (0.19) | +2.17 (0.25) | 7.6% | 7392 | 18.1% | 0.0% |
| 70/30 market/value | 62.8 | 79.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.4% | 7486 | 16.2% | 0.4% |
| 80/20 market/bills | 64.9 | 80.8 | +2.50 (0.16) | +2.71 (0.22) | +2.92 (0.29) | 6.6% | 7469 | 13.4% | 0.7% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.2%), k=0.75: 70/30 market/value (16.2%), k=1.00: 70/30 market/value (16.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.5 | 73.7 | +0.29 (0.11) tie | +0.40 (0.15) tie | +0.50 (0.20) tie | 2.6% | 7789 | 12.0% | 0.0% |
| 70/30 market/value | 60.4 | 73.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7792 | 11.0% | 0.4% |
| 80/20 market/bills | 62.1 | 74.2 | +2.17 (0.11) | +2.42 (0.15) | +2.67 (0.19) | 2.2% | 7827 | 8.8% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (11.0%), k=0.75: 70/30 market/value (11.0%), k=1.00: 70/30 market/value (11.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.3 | 81.6 | +0.62 (0.17) tie | +0.85 (0.23) tie | +1.08 (0.29) | 7.6% | 7392 | 18.1% | 0.0% |
| 70/30 market/value | 63.2 | 80.7 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7433 | 16.6% | 0.4% |
| 80/20 market/bills | 64.9 | 80.8 | +1.79 (0.18) | +1.81 (0.25) | +1.83 (0.32) | 6.6% | 7469 | 13.4% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.6%), k=0.75: 70/30 market/value (16.6%), k=1.00: 70/30 market/value (16.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.2 | 73.8 | +0.88 (0.11) tie | +1.12 (0.16) | +1.38 (0.21) | 3.3% | 7735 | 12.3% | 0.0% |
| 70/30 market/value | 59.9 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7791 | 10.2% | 0.6% |
| 80/20 market/bills | 61.8 | 74.2 | +2.62 (0.13) | +2.96 (0.19) | +3.29 (0.25) | 2.7% | 7784 | 9.8% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.2%), k=0.75: 70/30 market/value (10.2%), k=1.00: 70/30 market/value (10.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 82.1 | +1.63 (0.14) | +2.10 (0.21) | +2.58 (0.28) | 8.1% | 7356 | 18.9% | 0.0% |
| 70/30 market/value | 62.5 | 80.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.7% | 7466 | 15.6% | 0.7% |
| 80/20 market/bills | 64.6 | 81.5 | +2.75 (0.14) | +3.09 (0.20) | +3.43 (0.26) | 7.1% | 7430 | 14.7% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (15.6%), k=0.75: 70/30 market/value (15.6%), k=1.00: 70/30 market/value (15.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.2 | 73.8 | +0.46 (0.09) tie | +0.60 (0.12) tie | +0.75 (0.16) tie | 3.3% | 7735 | 12.3% | 0.0% |
| 70/30 market/value | 60.1 | 73.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7776 | 10.7% | 0.6% |
| 80/20 market/bills | 61.8 | 74.2 | +2.21 (0.11) | +2.44 (0.16) | +2.67 (0.21) | 2.7% | 7784 | 9.8% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.7%), k=0.75: 70/30 market/value (10.7%), k=1.00: 70/30 market/value (10.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 82.1 | +0.88 (0.14) tie | +1.15 (0.21) | +1.42 (0.28) | 8.1% | 7356 | 18.9% | 0.0% |
| 70/30 market/value | 62.8 | 81.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7415 | 16.4% | 0.6% |
| 80/20 market/bills | 64.6 | 81.5 | +2.00 (0.15) | +2.13 (0.22) | +2.26 (0.28) | 7.1% | 7430 | 14.7% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.4%), k=0.75: 70/30 market/value (16.4%), k=1.00: 70/30 market/value (16.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks | 6/8 | 3/8 | 2/8 | 6/8 | 3/8 | 2/8 |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2/8 | 5/8 | 6/8 |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |

# Engine output: config-v2-q1-seed2.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.4 | 73.7 | +0.95 (0.10) tie | +1.26 (0.14) | +1.57 (0.18) | 3.0% | 7758 | 12.1% | 0.0% |
| 70/30 market/value | 60.1 | 72.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7791 | 10.7% | 0.4% |
| 80/20 market/bills | 61.9 | 74.0 | +2.62 (0.10) | +3.01 (0.13) | +3.41 (0.17) | 2.6% | 7791 | 8.7% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.7%), k=0.75: 70/30 market/value (10.7%), k=1.00: 70/30 market/value (10.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 81.4 | +1.33 (0.15) | +1.75 (0.21) | +2.17 (0.27) | 7.6% | 7390 | 18.0% | 0.0% |
| 70/30 market/value | 62.8 | 79.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7481 | 16.4% | 0.4% |
| 80/20 market/bills | 64.7 | 80.9 | +2.50 (0.15) | +2.79 (0.21) | +3.08 (0.28) | 6.8% | 7453 | 13.2% | 0.7% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.4%), k=0.75: 70/30 market/value (16.4%), k=1.00: 70/30 market/value (16.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.4 | 73.7 | +0.42 (0.08) tie | +0.58 (0.12) tie | +0.75 (0.16) tie | 3.0% | 7758 | 12.1% | 0.0% |
| 70/30 market/value | 60.3 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7775 | 11.2% | 0.4% |
| 80/20 market/bills | 61.9 | 74.0 | +2.08 (0.11) | +2.33 (0.14) | +2.58 (0.18) | 2.6% | 7791 | 8.7% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (11.2%), k=0.75: 70/30 market/value (11.2%), k=1.00: 70/30 market/value (11.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 81.4 | +0.45 (0.16) tie | +0.60 (0.23) tie | +0.74 (0.31) tie | 7.6% | 7390 | 18.0% | 0.0% |
| 70/30 market/value | 63.1 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7431 | 17.1% | 0.4% |
| 80/20 market/bills | 64.7 | 80.9 | +1.62 (0.14) | +1.64 (0.22) | +1.66 (0.29) | 6.8% | 7453 | 13.2% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (17.1%), k=0.75: 70/30 market/value (17.1%), k=1.00: 70/30 market/value (17.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.3 | 74.1 | +0.92 (0.11) tie | +1.21 (0.15) | +1.50 (0.20) | 2.9% | 7771 | 13.0% | 0.0% |
| 70/30 market/value | 60.0 | 72.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.7% | 7784 | 10.4% | 0.7% |
| 80/20 market/bills | 62.0 | 74.4 | +2.75 (0.12) | +3.13 (0.16) | +3.51 (0.20) | 2.6% | 7795 | 9.5% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.4%), k=0.75: 70/30 market/value (10.4%), k=1.00: 70/30 market/value (10.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 81.8 | +1.41 (0.20) | +1.89 (0.28) | +2.37 (0.35) | 7.8% | 7376 | 18.9% | 0.0% |
| 70/30 market/value | 62.7 | 79.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.6% | 7471 | 15.8% | 0.7% |
| 80/20 market/bills | 64.8 | 81.5 | +2.83 (0.20) | +3.22 (0.28) | +3.62 (0.36) | 7.0% | 7439 | 14.3% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (15.8%), k=0.75: 70/30 market/value (15.8%), k=1.00: 70/30 market/value (15.8%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.3 | 74.1 | +0.46 (0.10) tie | +0.60 (0.14) tie | +0.75 (0.19) tie | 2.9% | 7771 | 13.0% | 0.0% |
| 70/30 market/value | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.9% | 7769 | 10.8% | 0.6% |
| 80/20 market/bills | 62.0 | 74.4 | +2.30 (0.12) | +2.53 (0.16) | +2.76 (0.20) | 2.6% | 7795 | 9.5% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.8%), k=0.75: 70/30 market/value (10.8%), k=1.00: 70/30 market/value (10.8%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 81.8 | +0.70 (0.19) tie | +0.97 (0.26) tie | +1.24 (0.33) | 7.8% | 7376 | 18.9% | 0.0% |
| 70/30 market/value | 63.0 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.2% | 7426 | 16.3% | 0.6% |
| 80/20 market/bills | 64.8 | 81.5 | +2.12 (0.19) | +2.31 (0.26) | +2.49 (0.33) | 7.0% | 7439 | 14.3% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.3%), k=0.75: 70/30 market/value (16.3%), k=1.00: 70/30 market/value (16.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks | 6/8 | 4/8 | 3/8 | 6/8 | 4/8 | 3/8 |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2/8 | 4/8 | 5/8 |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |

# Engine output: config-v2-q1-seed3.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.4 | 74.3 | +1.00 (0.10) | +1.33 (0.14) | +1.67 (0.18) | 3.1% | 7751 | 12.2% | 0.0% |
| 70/30 market/value | 60.1 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.5% | 7803 | 10.6% | 0.4% |
| 80/20 market/bills | 62.1 | 74.6 | +2.79 (0.13) | +3.19 (0.18) | +3.58 (0.23) | 2.8% | 7775 | 8.6% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.6%), k=0.75: 70/30 market/value (10.6%), k=1.00: 70/30 market/value (10.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.3 | 82.1 | +1.67 (0.13) | +2.17 (0.17) | +2.67 (0.21) | 7.8% | 7377 | 17.3% | 0.0% |
| 70/30 market/value | 62.7 | 80.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.6% | 7476 | 16.5% | 0.4% |
| 80/20 market/bills | 64.9 | 81.2 | +2.80 (0.17) | +3.07 (0.22) | +3.34 (0.27) | 6.9% | 7445 | 13.0% | 0.7% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.5%), k=0.75: 70/30 market/value (16.5%), k=1.00: 70/30 market/value (16.5%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.4 | 74.3 | +0.58 (0.10) tie | +0.79 (0.14) tie | +1.00 (0.18) tie | 3.1% | 7751 | 12.2% | 0.0% |
| 70/30 market/value | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7778 | 11.1% | 0.4% |
| 80/20 market/bills | 62.1 | 74.6 | +2.38 (0.12) | +2.65 (0.17) | +2.92 (0.21) | 2.8% | 7775 | 8.6% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (11.1%), k=0.75: 70/30 market/value (11.1%), k=1.00: 70/30 market/value (11.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.3 | 82.1 | +0.75 (0.13) tie | +1.00 (0.17) tie | +1.25 (0.21) | 7.8% | 7377 | 17.3% | 0.0% |
| 70/30 market/value | 63.1 | 81.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7419 | 16.7% | 0.4% |
| 80/20 market/bills | 64.9 | 81.2 | +1.88 (0.17) | +1.90 (0.22) | +1.93 (0.27) | 6.9% | 7445 | 13.0% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.7%), k=0.75: 70/30 market/value (16.7%), k=1.00: 70/30 market/value (16.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.1 | 74.0 | +0.79 (0.11) tie | +1.10 (0.15) | +1.42 (0.20) | 3.0% | 7760 | 12.7% | 0.0% |
| 70/30 market/value | 59.9 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.4% | 7810 | 9.8% | 0.7% |
| 80/20 market/bills | 61.8 | 74.3 | +2.71 (0.09) | +3.10 (0.13) | +3.50 (0.17) | 2.8% | 7779 | 9.5% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (9.8%), k=0.75: 70/30 market/value (9.8%), k=1.00: 70/30 market/value (9.8%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.0 | 81.3 | +1.25 (0.17) | +1.62 (0.23) | +2.00 (0.30) | 7.4% | 7408 | 18.7% | 0.0% |
| 70/30 market/value | 62.5 | 79.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7481 | 15.4% | 0.7% |
| 80/20 market/bills | 64.7 | 80.8 | +2.66 (0.17) | +2.91 (0.24) | +3.16 (0.31) | 6.8% | 7459 | 14.1% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (15.4%), k=0.75: 70/30 market/value (15.4%), k=1.00: 70/30 market/value (15.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.1 | 74.0 | +0.29 (0.12) tie | +0.44 (0.17) tie | +0.58 (0.22) tie | 3.0% | 7760 | 12.7% | 0.0% |
| 70/30 market/value | 60.1 | 73.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7789 | 10.4% | 0.6% |
| 80/20 market/bills | 61.8 | 74.3 | +2.21 (0.10) | +2.44 (0.14) | +2.67 (0.18) | 2.8% | 7779 | 9.5% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.4%), k=0.75: 70/30 market/value (10.4%), k=1.00: 70/30 market/value (10.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.0 | 81.3 | +0.55 (0.17) tie | +0.74 (0.22) tie | +0.93 (0.27) tie | 7.4% | 7408 | 18.7% | 0.0% |
| 70/30 market/value | 62.8 | 80.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.0% | 7437 | 16.1% | 0.6% |
| 80/20 market/bills | 64.7 | 80.8 | +1.96 (0.17) | +2.02 (0.23) | +2.08 (0.29) | 6.8% | 7459 | 14.1% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.1%), k=0.75: 70/30 market/value (16.1%), k=1.00: 70/30 market/value (16.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks | 5/8 | 4/8 | 3/8 | 5/8 | 4/8 | 3/8 |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 3/8 | 4/8 | 5/8 |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |

# Engine output: config-v2-q1-stress095.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.5 | 73.7 | +0.71 (0.10) tie | +0.90 (0.13) tie | +1.08 (0.16) | 2.6% | 7789 | 12.0% | 0.0% |
| 70/30 market/value | 60.2 | 72.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.5% | 7798 | 11.0% | 0.4% |
| 80/20 market/bills | 62.1 | 74.2 | +2.58 (0.11) | +2.92 (0.15) | +3.25 (0.19) | 2.2% | 7827 | 8.8% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (11.0%), k=0.75: 70/30 market/value (11.0%), k=1.00: 70/30 market/value (11.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.3 | 81.6 | +1.12 (0.12) | +1.44 (0.16) | +1.75 (0.21) | 7.6% | 7392 | 18.1% | 0.0% |
| 70/30 market/value | 62.8 | 80.3 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.8% | 7456 | 16.2% | 0.4% |
| 80/20 market/bills | 64.9 | 80.8 | +2.29 (0.12) | +2.40 (0.17) | +2.50 (0.22) | 6.6% | 7469 | 13.4% | 0.7% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.2%), k=0.75: 70/30 market/value (16.2%), k=1.00: 70/30 market/value (16.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.5 | 73.7 | +0.17 (0.10) tie | +0.21 (0.13) tie | +0.25 (0.16) tie | 2.6% | 7789 | 12.0% | 0.0% |
| 70/30 market/value | 60.4 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.9% | 7770 | 11.3% | 0.4% |
| 80/20 market/bills | 62.1 | 74.2 | +2.04 (0.11) | +2.23 (0.15) | +2.42 (0.18) | 2.2% | 7827 | 8.8% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (11.3%), k=0.75: 70/30 market/value (11.3%), k=1.00: 70/30 market/value (11.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.3 | 81.6 | +0.37 (0.15) tie | +0.47 (0.21) tie | +0.57 (0.27) tie | 7.6% | 7392 | 18.1% | 0.0% |
| 70/30 market/value | 63.2 | 81.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.5% | 7402 | 16.8% | 0.4% |
| 80/20 market/bills | 64.9 | 80.8 | +1.54 (0.16) | +1.43 (0.22) | +1.32 (0.28) | 6.6% | 7469 | 13.4% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.8%), k=0.75: 70/30 market/value (16.8%), k=1.00: 70/30 market/value (16.8%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.2 | 73.8 | +0.79 (0.11) tie | +1.02 (0.15) | +1.25 (0.20) | 3.3% | 7735 | 12.3% | 0.0% |
| 70/30 market/value | 59.9 | 72.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7775 | 10.2% | 0.6% |
| 80/20 market/bills | 61.8 | 74.2 | +2.54 (0.13) | +2.85 (0.18) | +3.17 (0.23) | 2.7% | 7784 | 9.8% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.2%), k=0.75: 70/30 market/value (10.2%), k=1.00: 70/30 market/value (10.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 82.1 | +1.20 (0.15) | +1.51 (0.22) | +1.82 (0.28) | 8.1% | 7356 | 18.9% | 0.0% |
| 70/30 market/value | 62.6 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7418 | 15.3% | 0.6% |
| 80/20 market/bills | 64.6 | 81.5 | +2.33 (0.15) | +2.50 (0.21) | +2.67 (0.27) | 7.1% | 7430 | 14.7% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (15.3%), k=0.75: 70/30 market/value (15.3%), k=1.00: 70/30 market/value (15.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.2 | 73.8 | +0.29 (0.09) tie | +0.35 (0.13) tie | +0.42 (0.16) tie | 3.3% | 7735 | 12.3% | 0.0% |
| 70/30 market/value | 60.1 | 73.6 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 3.1% | 7750 | 10.6% | 0.6% |
| 80/20 market/bills | 61.8 | 74.2 | +2.04 (0.11) | +2.19 (0.16) | +2.33 (0.21) | 2.7% | 7784 | 9.8% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.6%), k=0.75: 70/30 market/value (10.6%), k=1.00: 70/30 market/value (10.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 82.1 | +0.33 (0.14) tie | +0.38 (0.21) tie | +0.42 (0.27) tie | 8.1% | 7356 | 18.9% | 0.0% |
| 70/30 market/value | 62.9 | 81.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.9% | 7366 | 16.3% | 0.6% |
| 80/20 market/bills | 64.6 | 81.5 | +1.46 (0.15) | +1.36 (0.21) | +1.26 (0.27) | 7.1% | 7430 | 14.7% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.3%), k=0.75: 70/30 market/value (16.3%), k=1.00: 70/30 market/value (16.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks | 6/8 | 5/8 | 4/8 | 6/8 | 5/8 | 4/8 |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2/8 | 3/8 | 4/8 |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |

# Engine output: config-v2-q1-stress095-seed2.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.4 | 73.7 | +0.79 (0.08) tie | +1.02 (0.10) | +1.25 (0.13) | 3.0% | 7758 | 12.1% | 0.0% |
| 70/30 market/value | 60.1 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7775 | 10.9% | 0.4% |
| 80/20 market/bills | 61.9 | 74.0 | +2.46 (0.10) | +2.77 (0.13) | +3.08 (0.16) | 2.6% | 7791 | 8.7% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.9%), k=0.75: 70/30 market/value (10.9%), k=1.00: 70/30 market/value (10.9%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 81.4 | +1.04 (0.14) | +1.31 (0.21) | +1.57 (0.27) | 7.6% | 7390 | 18.0% | 0.0% |
| 70/30 market/value | 62.8 | 80.3 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7432 | 16.7% | 0.4% |
| 80/20 market/bills | 64.7 | 80.9 | +2.20 (0.16) | +2.35 (0.24) | +2.49 (0.31) | 6.8% | 7453 | 13.2% | 0.7% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.7%), k=0.75: 70/30 market/value (16.7%), k=1.00: 70/30 market/value (16.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.4 | 73.7 | +0.29 (0.07) tie | +0.35 (0.11) tie | +0.42 (0.14) tie | 3.0% | 7758 | 12.1% | 0.0% |
| 70/30 market/value | 60.2 | 73.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 3.1% | 7751 | 11.3% | 0.4% |
| 80/20 market/bills | 61.9 | 74.0 | +1.96 (0.11) | +2.10 (0.16) | +2.25 (0.20) | 2.6% | 7791 | 8.7% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (11.3%), k=0.75: 70/30 market/value (11.3%), k=1.00: 70/30 market/value (11.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 81.4 | +0.12 (0.15) tie | +0.10 (0.21) tie | +0.08 (0.28) tie | 7.6% | 7390 | 18.0% | 0.0% |
| 70/30 market/value | 63.1 | 81.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.8% | 7375 | 17.0% | 0.4% |
| 80/20 market/bills | 64.7 | 80.9 | +1.29 (0.17) | +1.15 (0.23) | +1.00 (0.30) tie | 6.8% | 7453 | 13.2% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (17.0%), k=0.75: 70/30 market/value (17.0%), k=1.00: 80/20 market/bills (13.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.3 | 74.1 | +0.83 (0.08) tie | +1.08 (0.11) | +1.32 (0.14) | 2.9% | 7771 | 13.0% | 0.0% |
| 70/30 market/value | 60.0 | 73.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7779 | 10.2% | 0.7% |
| 80/20 market/bills | 62.0 | 74.4 | +2.67 (0.11) | +3.00 (0.14) | +3.33 (0.16) | 2.6% | 7795 | 9.5% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.2%), k=0.75: 70/30 market/value (10.2%), k=1.00: 70/30 market/value (10.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 81.8 | +1.16 (0.21) | +1.49 (0.29) | +1.82 (0.36) | 7.8% | 7376 | 18.9% | 0.0% |
| 70/30 market/value | 62.7 | 80.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.0% | 7438 | 15.6% | 0.7% |
| 80/20 market/bills | 64.8 | 81.5 | +2.58 (0.20) | +2.83 (0.28) | +3.07 (0.36) | 7.0% | 7439 | 14.3% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (15.6%), k=0.75: 70/30 market/value (15.6%), k=1.00: 70/30 market/value (15.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.3 | 74.1 | +0.29 (0.09) tie | +0.40 (0.12) tie | +0.50 (0.15) tie | 2.9% | 7771 | 13.0% | 0.0% |
| 70/30 market/value | 60.2 | 73.7 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 3.0% | 7758 | 10.7% | 0.6% |
| 80/20 market/bills | 62.0 | 74.4 | +2.13 (0.12) | +2.32 (0.15) | +2.51 (0.19) | 2.6% | 7795 | 9.5% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.7%), k=0.75: 70/30 market/value (10.7%), k=1.00: 70/30 market/value (10.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 81.8 | +0.38 (0.21) tie | +0.48 (0.27) tie | +0.58 (0.34) tie | 7.8% | 7376 | 18.9% | 0.0% |
| 70/30 market/value | 63.0 | 81.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.7% | 7386 | 16.4% | 0.6% |
| 80/20 market/bills | 64.8 | 81.5 | +1.79 (0.21) | +1.81 (0.30) | +1.83 (0.38) | 7.0% | 7439 | 14.3% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.4%), k=0.75: 70/30 market/value (16.4%), k=1.00: 70/30 market/value (16.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks | 6/8 | 4/8 | 4/8 | 6/8 | 4/8 | 4/8 |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2/8 | 4/8 | 4/8 |
| 80/20 market/bills | 0/8 | 0/8 | 1/8 | 0/8 | 0/8 | 0/8 |

# Engine output: config-v2-q1-stress095-seed3.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.4 | 74.3 | +0.79 (0.10) tie | +1.02 (0.14) | +1.25 (0.18) | 3.1% | 7751 | 12.2% | 0.0% |
| 70/30 market/value | 60.1 | 73.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7779 | 10.5% | 0.4% |
| 80/20 market/bills | 62.1 | 74.6 | +2.58 (0.13) | +2.88 (0.17) | +3.17 (0.22) | 2.8% | 7775 | 8.6% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.5%), k=0.75: 70/30 market/value (10.5%), k=1.00: 70/30 market/value (10.5%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.3 | 82.1 | +1.21 (0.14) | +1.52 (0.17) | +1.83 (0.20) | 7.8% | 7377 | 17.3% | 0.0% |
| 70/30 market/value | 62.8 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7435 | 16.4% | 0.4% |
| 80/20 market/bills | 64.9 | 81.2 | +2.34 (0.15) | +2.42 (0.19) | +2.51 (0.23) | 6.9% | 7445 | 13.0% | 0.7% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.4%), k=0.75: 70/30 market/value (16.4%), k=1.00: 70/30 market/value (16.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.4 | 74.3 | +0.21 (0.09) tie | +0.23 (0.13) tie | +0.25 (0.16) tie | 3.1% | 7751 | 12.2% | 0.0% |
| 70/30 market/value | 60.2 | 74.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 3.1% | 7753 | 11.2% | 0.4% |
| 80/20 market/bills | 62.1 | 74.6 | +2.00 (0.13) | +2.08 (0.18) | +2.17 (0.23) | 2.8% | 7775 | 8.6% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (11.2%), k=0.75: 70/30 market/value (11.2%), k=1.00: 70/30 market/value (11.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.3 | 82.1 | +0.45 (0.14) tie | +0.56 (0.18) tie | +0.66 (0.22) tie | 7.8% | 7377 | 17.3% | 0.0% |
| 70/30 market/value | 63.1 | 81.7 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.6% | 7388 | 16.7% | 0.4% |
| 80/20 market/bills | 64.9 | 81.2 | +1.58 (0.16) | +1.46 (0.20) | +1.33 (0.25) | 6.9% | 7445 | 13.0% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.7%), k=0.75: 70/30 market/value (16.7%), k=1.00: 70/30 market/value (16.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.1 | 74.0 | +0.67 (0.10) tie | +0.92 (0.15) tie | +1.17 (0.20) | 3.0% | 7760 | 12.7% | 0.0% |
| 70/30 market/value | 59.9 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7792 | 10.1% | 0.7% |
| 80/20 market/bills | 61.8 | 74.3 | +2.58 (0.09) | +2.92 (0.13) | +3.25 (0.18) | 2.8% | 7779 | 9.5% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.1%), k=0.75: 70/30 market/value (10.1%), k=1.00: 70/30 market/value (10.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.0 | 81.3 | +1.04 (0.16) | +1.31 (0.22) | +1.58 (0.27) | 7.4% | 7408 | 18.7% | 0.0% |
| 70/30 market/value | 62.5 | 80.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.0% | 7444 | 15.5% | 0.7% |
| 80/20 market/bills | 64.7 | 80.8 | +2.45 (0.18) | +2.60 (0.25) | +2.74 (0.31) | 6.8% | 7459 | 14.1% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (15.5%), k=0.75: 70/30 market/value (15.5%), k=1.00: 70/30 market/value (15.5%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.1 | 74.0 | +0.17 (0.11) tie | +0.29 (0.16) tie | +0.42 (0.22) tie | 3.0% | 7760 | 12.7% | 0.0% |
| 70/30 market/value | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.9% | 7772 | 10.5% | 0.6% |
| 80/20 market/bills | 61.8 | 74.3 | +2.08 (0.10) | +2.29 (0.14) | +2.50 (0.19) | 2.8% | 7779 | 9.5% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.5%), k=0.75: 70/30 market/value (10.5%), k=1.00: 70/30 market/value (10.5%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.0 | 81.3 | +0.21 (0.15) tie | +0.24 (0.19) tie | +0.26 (0.24) tie | 7.4% | 7408 | 18.7% | 0.0% |
| 70/30 market/value | 62.8 | 81.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.5% | 7399 | 16.2% | 0.6% |
| 80/20 market/bills | 64.7 | 80.8 | +1.63 (0.17) | +1.52 (0.23) | +1.42 (0.30) | 6.8% | 7459 | 14.1% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.2%), k=0.75: 70/30 market/value (16.2%), k=1.00: 70/30 market/value (16.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks | 6/8 | 5/8 | 4/8 | 6/8 | 5/8 | 4/8 |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2/8 | 3/8 | 4/8 |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |

# Engine output: config-v2-q1-billsvol.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.5 | 73.7 | +0.91 (0.13) tie | +1.20 (0.17) | +1.49 (0.22) | 2.6% | 7789 | 12.0% | 0.0% |
| 70/30 market/value | 60.2 | 72.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.2% | 7821 | 10.7% | 0.4% |
| 80/20 market/bills | 62.1 | 74.3 | +2.83 (0.12) | +3.29 (0.17) | +3.74 (0.22) | 2.2% | 7826 | 8.9% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.7%), k=0.75: 70/30 market/value (10.7%), k=1.00: 70/30 market/value (10.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.3 | 81.6 | +1.33 (0.13) | +1.75 (0.19) | +2.17 (0.25) | 7.6% | 7392 | 18.1% | 0.0% |
| 70/30 market/value | 62.8 | 79.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.4% | 7486 | 16.2% | 0.4% |
| 80/20 market/bills | 64.9 | 81.0 | +2.63 (0.14) | +2.90 (0.19) | +3.17 (0.25) | 6.6% | 7472 | 13.6% | 0.7% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.2%), k=0.75: 70/30 market/value (16.2%), k=1.00: 70/30 market/value (16.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.5 | 73.7 | +0.29 (0.11) tie | +0.40 (0.15) tie | +0.50 (0.20) tie | 2.6% | 7789 | 12.0% | 0.0% |
| 70/30 market/value | 60.4 | 73.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7792 | 11.0% | 0.4% |
| 80/20 market/bills | 62.1 | 74.3 | +2.21 (0.11) | +2.48 (0.16) | +2.75 (0.20) | 2.2% | 7826 | 8.9% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (11.0%), k=0.75: 70/30 market/value (11.0%), k=1.00: 70/30 market/value (11.0%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.3 | 81.6 | +0.62 (0.17) tie | +0.85 (0.23) tie | +1.08 (0.29) | 7.6% | 7392 | 18.1% | 0.0% |
| 70/30 market/value | 63.2 | 80.7 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7433 | 16.6% | 0.4% |
| 80/20 market/bills | 64.9 | 81.0 | +1.92 (0.17) | +2.00 (0.23) | +2.08 (0.30) | 6.6% | 7472 | 13.6% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.6%), k=0.75: 70/30 market/value (16.6%), k=1.00: 70/30 market/value (16.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.2 | 73.8 | +0.88 (0.11) tie | +1.12 (0.16) | +1.38 (0.21) | 3.3% | 7735 | 12.3% | 0.0% |
| 70/30 market/value | 59.9 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7791 | 10.2% | 0.6% |
| 80/20 market/bills | 61.8 | 74.2 | +2.62 (0.13) | +2.96 (0.18) | +3.29 (0.24) | 2.7% | 7785 | 9.7% | 0.5% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.2%), k=0.75: 70/30 market/value (10.2%), k=1.00: 70/30 market/value (10.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 82.1 | +1.63 (0.14) | +2.10 (0.21) | +2.58 (0.28) | 8.1% | 7356 | 18.9% | 0.0% |
| 70/30 market/value | 62.5 | 80.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.7% | 7466 | 15.6% | 0.7% |
| 80/20 market/bills | 64.7 | 81.7 | +2.92 (0.13) | +3.29 (0.20) | +3.67 (0.27) | 7.2% | 7422 | 14.7% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (15.6%), k=0.75: 70/30 market/value (15.6%), k=1.00: 70/30 market/value (15.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.2 | 73.8 | +0.46 (0.09) tie | +0.60 (0.12) tie | +0.75 (0.16) tie | 3.3% | 7735 | 12.3% | 0.0% |
| 70/30 market/value | 60.1 | 73.2 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7776 | 10.7% | 0.6% |
| 80/20 market/bills | 61.8 | 74.2 | +2.21 (0.11) | +2.44 (0.16) | +2.67 (0.21) | 2.7% | 7785 | 9.7% | 0.5% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.7%), k=0.75: 70/30 market/value (10.7%), k=1.00: 70/30 market/value (10.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 82.1 | +0.88 (0.14) tie | +1.15 (0.21) | +1.42 (0.28) | 8.1% | 7356 | 18.9% | 0.0% |
| 70/30 market/value | 62.8 | 81.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7415 | 16.4% | 0.6% |
| 80/20 market/bills | 64.7 | 81.7 | +2.17 (0.14) | +2.33 (0.21) | +2.50 (0.28) | 7.2% | 7422 | 14.7% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.4%), k=0.75: 70/30 market/value (16.4%), k=1.00: 70/30 market/value (16.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks | 6/8 | 3/8 | 2/8 | 6/8 | 3/8 | 2/8 |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2/8 | 5/8 | 6/8 |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |

# Engine output: config-v2-q1-billsvol-seed2.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.4 | 73.7 | +0.95 (0.10) tie | +1.26 (0.14) | +1.57 (0.18) | 3.0% | 7758 | 12.1% | 0.0% |
| 70/30 market/value | 60.1 | 72.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7791 | 10.7% | 0.4% |
| 80/20 market/bills | 62.0 | 74.0 | +2.70 (0.10) | +3.10 (0.14) | +3.49 (0.17) | 2.6% | 7793 | 9.2% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.7%), k=0.75: 70/30 market/value (10.7%), k=1.00: 70/30 market/value (10.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 81.4 | +1.33 (0.15) | +1.75 (0.21) | +2.17 (0.27) | 7.6% | 7390 | 18.0% | 0.0% |
| 70/30 market/value | 62.8 | 79.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7481 | 16.4% | 0.4% |
| 80/20 market/bills | 64.7 | 81.2 | +2.62 (0.16) | +2.98 (0.23) | +3.33 (0.29) | 7.1% | 7435 | 13.3% | 0.7% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.4%), k=0.75: 70/30 market/value (16.4%), k=1.00: 70/30 market/value (16.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.4 | 73.7 | +0.42 (0.08) tie | +0.58 (0.12) tie | +0.75 (0.16) tie | 3.0% | 7758 | 12.1% | 0.0% |
| 70/30 market/value | 60.3 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7775 | 11.2% | 0.4% |
| 80/20 market/bills | 62.0 | 74.0 | +2.17 (0.11) | +2.42 (0.15) | +2.67 (0.20) | 2.6% | 7793 | 9.2% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (11.2%), k=0.75: 70/30 market/value (11.2%), k=1.00: 70/30 market/value (11.2%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 81.4 | +0.45 (0.16) tie | +0.60 (0.23) tie | +0.74 (0.31) tie | 7.6% | 7390 | 18.0% | 0.0% |
| 70/30 market/value | 63.1 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.1% | 7431 | 17.1% | 0.4% |
| 80/20 market/bills | 64.7 | 81.2 | +1.75 (0.15) | +1.83 (0.23) | +1.91 (0.31) | 7.1% | 7435 | 13.3% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (17.1%), k=0.75: 70/30 market/value (17.1%), k=1.00: 70/30 market/value (17.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.3 | 74.1 | +0.92 (0.11) tie | +1.21 (0.15) | +1.50 (0.20) | 2.9% | 7771 | 13.0% | 0.0% |
| 70/30 market/value | 60.0 | 72.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.7% | 7784 | 10.4% | 0.7% |
| 80/20 market/bills | 62.0 | 74.4 | +2.75 (0.11) | +3.12 (0.15) | +3.50 (0.19) | 2.6% | 7791 | 9.7% | 0.5% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.4%), k=0.75: 70/30 market/value (10.4%), k=1.00: 70/30 market/value (10.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 81.8 | +1.41 (0.20) | +1.89 (0.28) | +2.37 (0.35) | 7.8% | 7376 | 18.9% | 0.0% |
| 70/30 market/value | 62.7 | 79.9 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.6% | 7471 | 15.8% | 0.7% |
| 80/20 market/bills | 64.8 | 81.5 | +2.91 (0.21) | +3.31 (0.29) | +3.70 (0.37) | 7.0% | 7436 | 14.2% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (15.8%), k=0.75: 70/30 market/value (15.8%), k=1.00: 70/30 market/value (15.8%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.3 | 74.1 | +0.46 (0.10) tie | +0.60 (0.14) tie | +0.75 (0.19) tie | 2.9% | 7771 | 13.0% | 0.0% |
| 70/30 market/value | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.9% | 7769 | 10.8% | 0.6% |
| 80/20 market/bills | 62.0 | 74.4 | +2.29 (0.12) | +2.52 (0.16) | +2.75 (0.20) | 2.6% | 7791 | 9.7% | 0.5% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.8%), k=0.75: 70/30 market/value (10.8%), k=1.00: 70/30 market/value (10.8%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.2 | 81.8 | +0.70 (0.19) tie | +0.97 (0.26) tie | +1.24 (0.33) | 7.8% | 7376 | 18.9% | 0.0% |
| 70/30 market/value | 63.0 | 80.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.2% | 7426 | 16.3% | 0.6% |
| 80/20 market/bills | 64.8 | 81.5 | +2.20 (0.20) | +2.39 (0.27) | +2.57 (0.35) | 7.0% | 7436 | 14.2% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.3%), k=0.75: 70/30 market/value (16.3%), k=1.00: 70/30 market/value (16.3%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks | 6/8 | 4/8 | 3/8 | 6/8 | 4/8 | 3/8 |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 2/8 | 4/8 | 5/8 |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |

# Engine output: config-v2-q1-billsvol-seed3.toml

## sample 1927-07..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.4 | 74.3 | +1.00 (0.10) | +1.33 (0.14) | +1.67 (0.18) | 3.1% | 7751 | 12.2% | 0.0% |
| 70/30 market/value | 60.1 | 73.0 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.5% | 7803 | 10.6% | 0.4% |
| 80/20 market/bills | 62.1 | 74.7 | +2.83 (0.14) | +3.25 (0.19) | +3.67 (0.25) | 2.9% | 7769 | 8.6% | 0.7% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.6%), k=0.75: 70/30 market/value (10.6%), k=1.00: 70/30 market/value (10.6%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.3 | 82.1 | +1.67 (0.13) | +2.17 (0.17) | +2.67 (0.21) | 7.8% | 7377 | 17.3% | 0.0% |
| 70/30 market/value | 62.7 | 80.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.6% | 7476 | 16.5% | 0.4% |
| 80/20 market/bills | 65.0 | 81.3 | +2.96 (0.16) | +3.27 (0.21) | +3.58 (0.27) | 7.0% | 7440 | 13.0% | 0.7% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.5%), k=0.75: 70/30 market/value (16.5%), k=1.00: 70/30 market/value (16.5%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.4 | 74.3 | +0.58 (0.10) tie | +0.79 (0.14) tie | +1.00 (0.18) tie | 3.1% | 7751 | 12.2% | 0.0% |
| 70/30 market/value | 60.2 | 73.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.8% | 7778 | 11.1% | 0.4% |
| 80/20 market/bills | 62.1 | 74.7 | +2.42 (0.13) | +2.71 (0.18) | +3.00 (0.23) | 2.9% | 7769 | 8.6% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (11.1%), k=0.75: 70/30 market/value (11.1%), k=1.00: 70/30 market/value (11.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1927-07..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.3 | 82.1 | +0.75 (0.13) tie | +1.00 (0.17) tie | +1.25 (0.21) | 7.8% | 7377 | 17.3% | 0.0% |
| 70/30 market/value | 63.1 | 81.1 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.3% | 7419 | 16.7% | 0.4% |
| 80/20 market/bills | 65.0 | 81.3 | +2.04 (0.16) | +2.10 (0.22) | +2.17 (0.28) | 7.0% | 7440 | 13.0% | 0.7% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.7%), k=0.75: 70/30 market/value (16.7%), k=1.00: 70/30 market/value (16.7%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario base
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.1 | 74.0 | +0.79 (0.11) tie | +1.10 (0.15) | +1.42 (0.20) | 3.0% | 7760 | 12.7% | 0.0% |
| 70/30 market/value | 59.9 | 72.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.4% | 7810 | 9.8% | 0.7% |
| 80/20 market/bills | 61.9 | 74.5 | +2.88 (0.11) | +3.31 (0.14) | +3.75 (0.18) | 2.8% | 7778 | 9.5% | 0.5% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (9.8%), k=0.75: 70/30 market/value (9.8%), k=1.00: 70/30 market/value (9.8%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3%
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.0 | 81.3 | +1.25 (0.17) | +1.62 (0.23) | +2.00 (0.30) | 7.4% | 7408 | 18.7% | 0.0% |
| 70/30 market/value | 62.5 | 79.8 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 6.5% | 7481 | 15.4% | 0.7% |
| 80/20 market/bills | 64.7 | 80.8 | +2.66 (0.14) | +2.91 (0.20) | +3.16 (0.26) | 6.8% | 7453 | 14.2% | 0.6% |
Simplest within the tie band: k=0.50: 70/30 market/value, k=0.75: 70/30 market/value, k=1.00: 70/30 market/value
Lowest run-out within the tie band: k=0.50: 70/30 market/value (15.4%), k=0.75: 70/30 market/value (15.4%), k=1.00: 70/30 market/value (15.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 60.1 | 74.0 | +0.29 (0.12) tie | +0.44 (0.17) tie | +0.58 (0.22) tie | 3.0% | 7760 | 12.7% | 0.0% |
| 70/30 market/value | 60.1 | 73.4 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 2.6% | 7789 | 10.4% | 0.6% |
| 80/20 market/bills | 61.9 | 74.5 | +2.38 (0.12) | +2.65 (0.15) | +2.92 (0.19) | 2.8% | 7778 | 9.5% | 0.5% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (10.4%), k=0.75: 70/30 market/value (10.4%), k=1.00: 70/30 market/value (10.4%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## sample 1990-01..2026-09, scenario stocks 3% + no value premium
| candidate | median FI | p90 FI | gap k=0.50 (SE) | gap k=0.75 (SE) | gap k=1.00 (SE) | never by cap | quits | run out before horizon | turnover/yr |
|---|---|---|---|---|---|---|---|---|---|
| 100 stocks | 63.0 | 81.3 | +0.55 (0.17) tie | +0.74 (0.22) tie | +0.93 (0.27) tie | 7.4% | 7408 | 18.7% | 0.0% |
| 70/30 market/value | 62.8 | 80.5 | +0.00 (0.00) tie | +0.00 (0.00) tie | +0.00 (0.00) tie | 7.0% | 7437 | 16.1% | 0.6% |
| 80/20 market/bills | 64.7 | 80.8 | +1.96 (0.13) | +2.02 (0.18) | +2.08 (0.23) | 6.8% | 7453 | 14.2% | 0.6% |
Simplest within the tie band: k=0.50: 100 stocks, k=0.75: 100 stocks, k=1.00: 100 stocks
Lowest run-out within the tie band: k=0.50: 70/30 market/value (16.1%), k=0.75: 70/30 market/value (16.1%), k=1.00: 70/30 market/value (16.1%). The simplest pick ignores run-out; if your goal includes staying quit, compare both before accepting it.

## Summary over 8 cells (candidates listed simplest first)
| candidate | in tie band k=0.50 | in tie band k=0.75 | in tie band k=1.00 | simplest pick k=0.50 | simplest pick k=0.75 | simplest pick k=1.00 |
|---|---|---|---|---|---|---|
| 100 stocks | 5/8 | 4/8 | 3/8 | 5/8 | 4/8 | 3/8 |
| 70/30 market/value | 8/8 | 8/8 | 8/8 | 3/8 | 4/8 | 5/8 |
| 80/20 market/bills | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 | 0/8 |
