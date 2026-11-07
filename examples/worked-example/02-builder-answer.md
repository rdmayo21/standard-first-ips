# Phase 2 builder answer, v2: Robin (fictional)

Builder, 2026-11-07. Robin is fictional. Replaces v1; v1 files kept (`config-q*.toml`, `results-q*.md`).

## What the critics changed

| Defect (critic) | What I did |
|---|---|
| Cap 75 undisclosed; hid the bad case (Claude 1, GPT 2) | Robin chose 85; never-FI shown beside every score |
| Independent centers gave value an assumed edge (Claude 2, GPT 1) | Correlation 0.72 (agent's reading of Robin's words) primary, 0.95 (builder's stress case); "only mix in all 8" re-tested |
| Trend's ~1.6× exposure vs "no leveraged funds" (Claude 4, GPT 3) | Robin excluded trend; dropped |
| Value buyability unsourced; one fund or two? (Claude 3) | One fund if one fund does it (Robin); none sourced yet, so implementation is conditional; proxy mismatch labelled |
| "Paired" Q1 run-out (Claude 5) | Now "same paths, different quitters" |
| "At every k" when k was inert in 4 cells (Claude 6) | At cap 85, never-FI ≤ 8.1% < 10%, so no p90 is capped; k now enters every cell's score |
| Seed-sensitive counts; overlapping samples (Claude 7, GPT 4) | Seeds 1–3 for every variant; 1990+ lies inside 1927+, so coverage, not independent confirmation |
| Quit transfer called pro-rata (GPT 5) | Corrected (Q2) |
| Bills vol off-rule; chronology only asserted (GPT 6) | Bills at the rule's 0.02 as a sensitivity (v1 wrongly said 0.015); SHA-256 hashes in `manifest-v2.txt` (chronology builder-recorded) |

**Confirm pass** (`02-confirm-claude.md`, `02-confirm-gpt.md`): both "holds with caveats", no verdict change; their wording, scope and labelling fixes are applied here, with no re-scoring and no input changed.

## Question, standard, scoring

**Questions.**
- Q1: which accumulation mix: 100 stocks, 70/30 market/value, or 80/20 market/bills?
- Q2: keep that mix after the quit, or move 20% to bills on the quit date?

**Standard (verbatim).** "Goal. Stop needing the pharmacy paycheck, ideally before 55, and not
have to go back. Growth and caution. Earlier is better. A typical-case year is worth one to two
bad-case years. Uncertainty about returns counts once, inside the ranges I give. No borrowing.
Losses. Big drops are acceptable if they only push the date back. Rules should stop me from
selling at the bottom. Failure. Quitting and then running short, so I'd have to go back to work.
The nine-month emergency fund and disability cover come first; the portfolio is the last line."

**Scoring.**
- FI means $1,660,000 held for 12 months, with the cap at 85.
- S = median FI age + k × p90 FI age, at k = 0.5, 0.75 and 1.0. The tie band is 1.0 year.
- 8 cells per seed: 2 samples × 4 scenarios. 8,000 paths.
- **Robin's combining rule:** the simplest mix inside the band in at least 75% of cells (6 of 8)
  at every k. If none qualifies, 100 stocks.
- Run-out (running short before 95, as a share of quits) is reported beside the score, not in
  it.

---

## Q1: accumulation mix

### 1. Answer

Under Robin's standard and combining rule, **70/30 market/value is selected**. 100 stocks is
inside the band in only 2–5 of 8 cells at k ≥ 0.75, so it fails the rule. 70/30 is inside the
band in 8/8 cells at every k. This holds for every seed, correlation and bills volatility. In the base cells, 70/30's median FI age is about 0.3 years earlier and its 1-in-10
FI age about 1.0–1.2 years earlier. The pick depends on a one-fund value option not yet sourced,
so implementation is conditional.

*This is not investment advice. Robin decides.*

### 2. Scores

Cells in the tie band, as a range over seeds 1–3:

| Mix (simplest first) | Primary (0.72), k = .5 / .75 / 1 | Stress (0.95) | Bills vol 0.02 | Meets the 6/8 rule? |
|---|---|---|---|---|
| 100 stocks | 6 / 3–4 / 2–3 | 6 / 4–5 / 4 | 6 / 3–4 / 2–3 | No (fails at k ≥ 0.75) |
| 70/30 market/value | 8 / 8 / 8 | 8 / 8 / 8 | 8 / 8 / 8 | **Yes, every run** |
| 80/20 market/bills | 0 / 0 / 0 | 0 / 0 / 0–1 | 0 / 0 / 0 | No |

Base cells, primary, seed 1 (1927 / 1990):

| Mix | Gap at k = 0.75, years (paired SE) | Never reaches FI by 85 | Run-out |
|---|---|---|---|
| 100 stocks | +1.20 (0.17) / +1.12 (0.16) | 2.6% / 3.3% | 12.0% / 12.3% |
| 70/30 | best / best | 2.2% / 2.6% | 10.7% / 10.2% |
| 80/20 | +3.22 (0.17) / +2.96 (0.19) | 2.2% / 2.7% | 8.8% / 9.8% |

- **100 stocks drops out (k = 0.75, primary)** in the base and stocks-3% cells, 1.1–2.1 years behind.
- **Where it ties:** both pure no-value-premium cells, at every k.
- **Never-FI and run-out:** never-FI is 2.2–8.1% for every mix. Run-out is 9.8–17.1% for 70/30
  against 12.0–18.9% for 100 stocks (all seeds and variants). Same paths, different quitters.

### 3. What would flip it

- **No value premium.** 100 stocks ties in the pure no-premium cells, so the selection rests on
  Robin's half-point premium.
- **k range.** At k = 0.5 alone, 100 stocks sits exactly at 6/8 and would be selected; in seed 3
  its sixth cell is a gap of exactly 1.000. Under stress, its k = 0.75 drop-outs (1.02–1.08
  years) are within one SE of the band, so the result rests on k = 1.0, where 100 stocks is in
  2–4 of 8 cells.

---

## Q2: quit-day switch (bills only)

### 1. Answer

**The switch cannot move the FI age.** The FI gap is 0.00 in every comparison, so FI ties and
Robin's rule selects **"70/30, keep"**. Moving 20% to bills at the quit lowers run-out in every
cell, for every seed and variant:
- **from 70/30:** by 2.3–4.5 points;
- **from 100 stocks:** by 2.6–4.2 points.

Whether that is worth one more fund and rule is Robin's call.

*This is not investment advice. Robin decides.*

### 2. Scores

Exactly paired against keeping the same base mix (same quit dates).

| Base mix | FI gap | Run-out if kept (primary, seed 1) | Run-out change, primary seed 1 (max SE) | Change over all seeds and variants |
|---|---|---|---|---|
| 70/30 | 0.00 | 10.2–16.6% | −2.8 to −4.2 pts (0.23) | −2.3 to −4.5 pts |
| 100 stocks | 0.00 | 12.0–18.9% | −2.7 to −4.2 pts (0.23) | −2.6 to −4.2 pts |

**Quit transfer:** (post − pre target weights) × NAV, not a pro-rata sale; a drifted 75/25 becomes
61/19/20, not 60/20/20. From 100 stocks the two agree.

### 3. What would flip it

- **Not modelled:** flexible spending and Social Security would lower all run-out, likely the gap too.

---

## 4. Defaults still mine (each is Robin's call)

1. **"Stocks 3%" lowers value to 3.5%**, consistent with Robin's follow-up answer.
2. **Bills vol 0.01 primary** (the brief's); the rule's 0.02 gives the same pick.
3. **±5-point bands**, also after the quit; the 70/30 switch target is 56/24/20.

**Value proxy:** the series is a 50/50 mix of French small-value and big-value; no fund's index
matches it. Robin: one fund if one fund does it; none sourced yet.

**Buyability (general availability, not a fund recommendation):**
- **Broad US market:** the CRSP US Total Market Index underlies retail index funds (source:
  crsp.org).
- **T-bills:** individuals can buy them through TreasuryDirect (source: treasurydirect.gov).
- **One-fund US value covering small and large companies:** **unsourced**; none sourced yet, so
  implementation of 70/30 is conditional.

**Order of events (builder-recorded; hashes show file consistency, not timing):** v1 runs; critics; Robin's follow-up; at 16:41:11Z all 18 v2 configs (both
Q2 base mixes included), `combine_v2.py` and data hashes written to `manifest-v2.txt`; engine
runs; a column-slicing bug in `combine_v2.py` fixed (logged; no input changed); rule tables and
paired Q2 run-out.

Dropping trend lengthened the data window to 2026-09 (the AQR series ends 2026-02).

## 5. Limits

From `references/engine.md`, "What it does NOT model":
- "**Taxes,** of any kind, including withdrawal taxes and account location."
- "**Social Security,** pensions, inheritance, or flexible spending after the quit." Run-out is
  approximately 7–19% across options, larger than any gap between them.
- "**Costs** beyond what is in the return series."
- "**The sample.** The future is not a resample of 1927–2026."
- "**\"Quit and stay quit\" as a score.** … run-out is shown beside the score, not inside it."


## 6. Files and how to reproduce

All files are in `<repo>/examples/worked-example/`:
`config-v2-q1.toml`, `config-v2-q2.toml` (plus `-stress095`, `-billsvol`, `-seed2/3` variants),
`results-v2-q1.md`, `results-v2-q2.md`, `v2-out/` (CSVs), `combine_v2.py`, `runout_paired.py`,
`manifest-v2.txt`.

```bash
E=<repo>/plugins/standard-first-ips/skills/standard-first-ips/engine
cd <repo>/examples/worked-example
uv run --project $E ips-engine score config-v2-q1.toml --out v2-out/v2-q1.csv
python3 combine_v2.py 1.0 "100 stocks" v2-out/v2-q1.csv v2-out/v2-q1-seed2.csv v2-out/v2-q1-seed3.csv
uv run --project $E python runout_paired.py config-v2-q2.toml "70/30, keep"
```
