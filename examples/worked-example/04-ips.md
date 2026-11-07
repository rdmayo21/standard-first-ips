# Investment Policy Statement — Revision 1 (adopted and signed 2026-11-07)

| | |
|---|---|
| **Investor** | Robin (fictional; a worked example of the standard-first-ips process) |
| **Status** | Signed revision 1. First IPS; supersedes nothing. Enacts the decisions in `03-decisions.md` (Decisions 1–2 and D3–D7, 2026-11-07). |
| **Horizon** | Accumulation until FI (ideally before 55, per the standard), then withdrawals to age 95. |

*Not investment advice. This document records the investor's own decisions. Robin and every
figure in it are fictional.*

## 1. The standard (verbatim, adopted 2026-11-07)

> **Goal.** Stop needing the pharmacy paycheck, ideally before 55, and not have to go back.
>
> **Growth and caution.** Earlier is better. A typical-case year is worth one to two bad-case
> years. Uncertainty about returns counts once, inside the ranges I give. No borrowing.
>
> **Losses.** Big drops are acceptable if they only push the date back. Rules should stop me from
> selling at the bottom.
>
> **Failure.** Quitting and then running short, so I'd have to go back to work. The nine-month
> emergency fund and disability cover come first; the portfolio is the last line.

**Operational definitions** (2026-11-07):
- **FI test:** the quit number held for 12 months in a row. Run-out after the quit is read beside
  the score.
- **Quit number:** $1,660,000 in today's dollars ($58,000 a year of spending at 3.5%), owned by
  Robin. Raised with CPI every January (D7); the engine uses a continuous real threshold, so
  this yearly step is a small difference.
- **k range:** 0.5 to 1.0.
- **Tie band:** 1.0 year.
- **Simpler:** fewer funds, then fewer rules.
- **"Never":** FI ages are capped at 85 in scoring, and the share that never reaches FI is
  reported.
- **Leverage:** any fund with more than $1 of exposure per $1 invested is excluded. Robin applied
  this to trend-following funds.

**How answers are scored** (each is Robin's decision, 2026-11-07):
- S = median FI age + k × 1-in-10 FI age, at k = 0.5, 0.75 and 1.0. Options within 1.0 year of
  the best tie, and the simpler one wins.
- **Combining cells:** the simplest mix inside the tie band in at least 75% of cells at every k.
  If none qualifies, 100 stocks.
- Uncertainty about returns is counted once, inside the simulation's center ranges.
- **Named exception:** the quit-day switch to bills (§9) is kept even though it ties on score,
  because it lowers run-out, and staying quit is part of the goal. The exception applies to that
  rule only (Decisions 2 and D4).

## 2. Profile and constraints

| Item | Value | Source, date |
|---|---|---|
| Age | 44 | Robin, 2026-11-07 |
| Investable wealth (excluding the emergency fund) | $420,000 | Robin, 2026-11-07 |
| Real saving until FI | $32,000 a year | Robin, 2026-11-07 |
| Spending after FI | $58,000 a year | Robin, 2026-11-07 |
| Emergency reserve | 9 months of expenses, held outside this portfolio | Robin, 2026-11-07 |
| Insurance | Employer long-term disability | Robin, 2026-11-07 |
| Borrowing | None (see §6) | Standard |

## 3. Objectives

Reach FI as the standard scores it (§1), with run-out after the quit read beside the score.
Return beliefs are used only inside the scoring. They are neither targets nor forecasts.

## 4. Risk and failure

- **Ruin, per the standard:** running short before 95 after quitting.
- **Modelled run-out** under this policy, among paths that quit (engine figures under the limits
  in Appendix A, not forecasts):
  - **70/30, switching to 56/24/20 at the quit:** 7.4–12.6% (primary run, seed 1);
    7.35–13.0% over all seeds and variants.
  - **Fallback, 100 stocks switching to 80/20 at the quit:** 8.9–14.9% (primary run, seed 1).
- **Drawdowns** are information, not limits. Big drops are acceptable if they only push the date
  back.

## 5. Allocation

**Before FI, once Robin has named a single US value fund (Decision 1, D3):**

| Sleeve | Target | Band | Why (evidence; what reopens it) |
|---|---|---|---|
| US total stock market | 70% | ±5 pts | Of the three mixes tested, 70/30 was the only one inside the tie band in 8/8 cells at every k, across seeds and stress cases (`02-builder-answer.md` v2). Reopens per §12. |
| US value (small + large, one fund) | 30% | ±5 pts | As above. Its return uncertainty is mostly shared with the market (center correlation 0.72). |

**Until a value fund is named, or if none is (fallback):** 100% US total stock market.

**After FI** (§9 gives the switch): 56% market / 24% value / 20% T-bills. Under the fallback:
80% market / 20% T-bills. Bands are ±5 points.

**Moving from the fallback to the value tilt (D3, D6, D7):** the change happens at the
month-end after Robin names a value fund, after that month-end's other steps in §9.
- Before FI: go to 70/30.
- After FI: go to 56/24/20.
- If FI is reached at that same month-end: go to 56/24/20 **in place of** the quit transfer, as
  one move.

## 6. Leverage

None. The standard says "No borrowing", and Robin excludes any fund with more than $1 of exposure
per $1 invested.

## 7. Vehicles

| Role | Vehicle (Robin's choice) | Notes |
|---|---|---|
| US total market | To be chosen by Robin | Some retail index funds track the CRSP US Total Market Index (source: crsp.org) |
| US value | To be chosen by Robin; must be one fund | No matching fund sourced yet. The engine's proxy is a 50/50 mix of French small and big value, and no fund's index matches it |
| T-bills (after FI) | To be chosen by Robin | Individuals can buy them through TreasuryDirect (source: treasurydirect.gov) |

## 8. Account location

Out of scope for this example. Taxes are not modelled.

## 9. Rebalancing and cash flows (D5, D6)

The timing follows the engine exactly, apart from the yearly CPI steps, so the evidence applies
(D6, D7).

**Every month-end, before FI:**
1. **Contribution:** the month's saving, all of it, goes to the sleeve furthest below its
   target. A tie goes to market.
2. **Band check:** if any sleeve is more than 5 points from its target, rebalance every sleeve to
   target.
3. **FI check:** if the portfolio has held the quit number (CPI-indexed, D7) for 12 month-ends
   in a row, FI is reached. That month's contribution is the last one.

**The quit transfer** happens at that same month-end, right after the FI check, before the next
month's returns:
- Move (post-FI target − pre-FI target) × portfolio value between sleeves. From 70/30 that is 14
  points out of market and 6 out of value, into T-bills. Under the fallback, it is 20 points out
  of market into T-bills.
- A sleeve that holds less than it should give gives only what it holds.
- This is a target-weight transfer, not a pro-rata sale: a 70/30 that has drifted to 75/25
  becomes 61/19/20.

**Every month-end after FI**, starting with the month after the quit:
1. **Withdrawal:** $58,000 a year ÷ 12, in today's dollars, raised with CPI every January
   (D6), taken pro rata across sleeves. The engine models continuous real dollars; the yearly
   step is a small difference.
2. **Band check:** as above, against the post-FI targets.

## 10. Monitoring and amendments

- **Every January:** review the figures in §2 and the beliefs in Appendix A. Re-score if any has
  moved (D5).
- **Amendments:** nothing changes without a new revision signed by Robin (D5).

## 11. Behavioral commitments

From the standard, verbatim: "Big drops are acceptable if they only push the date back. Rules
should stop me from selling at the bottom." What this policy sets against that is fixed targets,
the order and bands in §9, and §10: nothing changes without a signed revision. Under the
fallback before FI there is one sleeve, so no band acts, and after FI the pro-rata withdrawals
sell stocks after a fall. No other response to a market fall is set.

## 12. What would trigger a review

A trigger starts a review under this standard. It never changes the allocation by itself (D5).

- **Robin no longer believes in a value premium.** With no premium, 100 stocks ties.
- **Robin's k range narrows to 0.5 only.** At k = 0.5, 100 stocks sits at the 6-of-8 threshold
  in the primary runs. In seed 3 its sixth cell's gap is exactly 1.0 year, so it counts as 5 or 6
  depending on rounding. Under the 0.95 stress case, the pick rests on k = 1.0.
- **A material change in §2:** savings, spending or wealth.
- **Social Security or flexible spending becomes part of the plan.** That would lower every
  run-out figure, and it could change Decisions 2 and D4.

**Left open (`03-decisions.md`):** what to do if the portfolio can't cover a month. The standard
names that as the failure; this IPS doesn't set a response.

## Signature

**Signed: Robin (fictional), 2026-11-07** ("sign v1")

## Appendix A: assumptions (centers and spreads, with sources)

| Sleeve | Real compound center | Uncertainty (sd) | Volatility | Source |
|---|---|---|---|---|
| US market | 4.5% (3.0% pessimistic) | 1.8% | 0.17 | Robin; vol from the brief, 2026-11-07 |
| US value | 5.0% (3.5% when stocks are at 3.0%; equal to the market's center when there is no premium) | 2.5% | 0.22 | Robin; vol by the builder's pre-scoring rule |
| T-bills | 0.5% | 1.0% | 0.01 (0.02 tested; same pick) | Robin; the brief |

- **Market–value center correlation:** 0.72 (the agent's reading of Robin's words). The builder
  tested 0.95 as a stress case.
- **Engine limits:** no taxes, Social Security, flexible spending or costs beyond the data, and
  the future is not a resample of 1927–2026 (`references/engine.md`).

## Appendix B: changelog

- **Signed v1 (2026-11-07):** the CPI-step labels from the last check were added; Robin signed.
- **Draft v4 (2026-11-07):** after the final confirm pass.
  - Quit number CPI-indexed (D7).
  - The fund change's place in the month is set; it replaces the quit transfer when both fall at
    the same month-end.
- **Draft v3 (2026-11-07):** after both confirm passes.
  - §9 timing now matches the engine (D6), with the edge cases set.
  - Rounding note added in §12.
  - §11 now states what the policy does and doesn't do.
  - Source wording and the horizon line corrected.
- **Draft v2 (2026-11-07):** after two blind draft reviews.
  - Removed an added objective and an added behavioral rule.
  - Narrowed the leverage line to Robin's words.
  - Added the fund-search state and the fallback switch (D3, D4).
  - Adopted the operating rules (D5).
  - Widened the run-out figures, added sources and the cap.
- **Draft v1 (2026-11-07):** first draft.
