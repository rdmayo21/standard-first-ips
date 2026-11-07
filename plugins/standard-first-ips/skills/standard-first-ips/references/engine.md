# The engine: what it does and doesn't model

## What it does

- **Paths.**
  - A joint 60-month block bootstrap of historical real monthly returns. History supplies the
    shape: crashes, fat tails, how sleeves move together, regimes that last years.
  - Each path draws its own expected return per sleeve from the person's center (a real compound,
    or geometric, annual return) and its uncertainty, so estimation risk is counted once, inside the
    paths.
  - Every candidate and scenario runs on the same paths, so comparisons are paired.
- **Policy, each month:**
  1. the quit-day move, if any. (post − pre) × NAV moves between sleeves; a sleeve that has
     drifted below what it should give gives only what it holds, so there are no short positions;
  2. returns;
  3. saving to the sleeve furthest below target before the quit, or a pro-rata withdrawal after
     it;
  4. a full rebalance to target when any sleeve leaves its absolute band.
- **FI.**
  - FI is reached at the first month wealth reaches the quit number, or has held it for
    `hold_months`. The quit starts the next month.
  - FI ages past `cap_age` are censored there.
- **Score.**
  - S = median FI age + k × 90th-percentile FI age, at each k.
  - A candidate is in the tie band when within `tie_years` of the best. The simplest is the first
    in config order inside the band.
  - The paired batch SE of each gap is reported.
- **Run-out.** The share of quits whose wealth can't cover the month's spending before
  `horizon_age` ("n/a" when no path quits). It is reported next to the score, not folded into it.
  The "lowest run-out within the tie band" line shows when the simplest pick has more run-out risk
  than another tied option.

## Built-in data sources

| `source` | What it is |
|---|---|
| `market` | US stock market total return (Ken French), real |
| `value` | Average of US small-value and big-value portfolios (Ken French), real |
| `bills` | US T-bills (Ken French RF), real |
| `trend_proxy` | Paper time-series momentum on AQR's equity, bond and commodity composites, plus bills, real. A proxy built from three composites, gross of costs. Not a fund record. |
| `csv:path:column` | Any monthly nominal return series you supply (month-end dates; relative paths resolve against the config's folder) |

## What it does NOT model (quote these limits with every result)

- **Taxes,** of any kind, including withdrawal taxes and account location.
- **Social Security,** pensions, inheritance, or flexible spending after the quit.
- **Leverage and its forced-sale risk.** Weights must be non-negative and sum to 1. Leveraged
  funds can be supplied as a `csv:` series, but their internal financing and deleveraging are only
  as good as that series.
- **Illiquidity and redemption gates** of private funds.
- **Rebalancing signals or "gates."** The engine is bands-only. If you test a gate, extend
  `policy.run` and add a test.
- **Costs** beyond what is in the return series.
- **Correlation between centers.** Draws are independent unless you set `[model.center_corr]`.
- **The sample.** The future is not a resample of 1927–2026. Report at least two samples.
- **"Quit and stay quit" as a score.** FI is first reach, or the number held N months; run-out
  is shown beside the score, not inside it.
- **Signals.** The trend proxy's crisis behavior is paper, from three composites.

## Extending it

Keep pure computation separate from I/O, add a pytest for any new rule, and reproduce an existing
result bit for bit before changing a rule.

Run the tests:

```bash
uv run --project ENGINE --group dev pytest -q ENGINE/tests
```
