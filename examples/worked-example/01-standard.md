# Phase 1: the standard (fictional investor "Robin")

> **Read this first.** Robin is fictional. An agent wrote Robin's answers, following a plausible
> brief: a 44-year-old hospital pharmacist, single, no children, a US saver. The point is to show
> the process end to end on real data, with real engine output and real critic reviews. Robin's
> numbers and beliefs are inputs to the example, not anyone's real situation, and nothing here is
> investment advice.

Interview dated 2026-11-07, in rounds of two to four questions (`references/1-standard.md`).

## Round 1: the goal

**Agent:** What is the money for? What would "done" look like? As early as possible, or by a
date?

**Robin:** "I want to stop needing the pharmacy job. Not retire to nothing, just not need the
paycheck. Earlier is better, but I'd like it before 55 if that's realistic."

## Round 2: failure

**Agent:** Which is the failure you're guarding against: (a) markets fall 50% and you work three
more years, or (b) you quit, the money runs short, and you have to go back? What covers you if you
can't work?

**Robin:** "(b), easily. Working a few extra years is annoying. Quitting and then having to go
back, at sixty, to a job market that's moved on, is the thing I actually fear. I have nine months
of expenses in savings and long-term disability through work."

## Round 3: losses

**Agent:** Picture a 90% loss that you don't know will recover. What would you do? Have you held
through a big loss before?

**Robin:** "I held through 2020 and 2022 without selling. A 90% loss would mostly mean working
longer, which I can live with. Selling at the bottom is the mistake I'd want rules to stop me
from making."

## Round 4: typical vs bad case

**Agent:** A year earlier in the typical case is worth how many years in the 1-in-10 bad case?

**Robin:** "I'd give up one, maybe two years in the bad case to get a year in the typical case."

*Agent's reading:* one to two years of bad case per typical year, so **k from 1/2 to 1**. The
results are reported at k = 0.5, 0.75 and 1.0.

## Round 5: what counts as a tie

**Agent:** If two options differ by less than about how many years, does it not matter? Within a
tie, should the simpler option win, and what does "simpler" mean to you?

**Robin:** "A year. Inside a year, simpler wins: fewer funds, fewer rules, nothing I'd have to
explain to my sister if she had to take over."

## Round 6: borrowing and caution

**Agent:** Is borrowing to invest allowed if the math calls for it? Should uncertainty about
future returns count once (inside the simulation) or again as an extra haircut?

**Robin:** "No borrowing, no leveraged funds. Count it once. I'll give you honest ranges for what
I expect, and I don't want them shaved again."

## The standard (adopted by Robin 2026-11-07, verbatim)

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

Robin: "Adopt."

*Drift check (lesson 6):* re-read against the round answers. "One, maybe two years" became "one to
two", which matches. No mismatch found.

## Operational definitions (each Robin's call, 2026-11-07)

| Definition | Robin's choice | Robin's words |
|---|---|---|
| FI test | Quit and stay quit: the number held 12 months in a row (`hold_months = 12`), with run-out after the quit read alongside the score | "Touching the number once doesn't count. I want it to hold for a year, and I want to see the chance of running short." |
| Quit number | $1,660,000 real: $58,000 a year of spending at a 3.5% withdrawal rate | "3.5%, not 4%. I might live to 95." |
| k range | 0.5 to 1.0 | (Round 4) |
| Tie band | 1.0 year | (Round 5) |
| Simpler | Fewer funds, then fewer rules | (Round 5) |
| Ruin | Running short before age 95, after quitting | (Round 2) |

## Robin's figures (fictional; each one Robin's statement)

| Figure | Value | Source |
|---|---|---|
| Age | 44 | Robin |
| Investable wealth (excluding the emergency fund) | $420,000 | Robin |
| Real saving per year until the quit | $32,000 | Robin |
| Spending per year after the quit | $58,000 | Robin |
| Emergency fund | 9 months | Robin |
| Disability cover | Employer long-term disability | Robin |

## Robin's beliefs (fixed before any scoring; lesson 10)

Real compound annual returns Robin plans on, with Robin's uncertainty about each center:

| Sleeve | Center | Uncertainty (sd of center) | Robin's reason |
|---|---|---|---|
| US stock market | 4.5% | 1.8% | "Lower than history. Valuations are high." |
| US value (small + large value) | 5.0% | 2.5% | "Maybe half a point over the market, and I'm less sure of it." |
| Trend following (the engine's paper proxy) | 2.5% | 2.0% | "Bills plus a couple of points, after costs, if it works at all." |
| T-bills | 0.5% | 1.0% | |

Belief scenarios Robin considers plausible: stocks at 4.5% (base) and at 3.0% (pessimistic); value
with no premium (5.0% → market's center).

## Open questions (phase 2 order)

1. **Accumulation mix:** 100% stocks, a value tilt, a trend sleeve, or bills? (No leverage, per
   the standard.)
2. **Quit-day switch:** keep the accumulation mix after the quit, or move part into bills on the
   quit date? Robin's goal names staying quit, so run-out is read next to the score.

Out of scope for this example: account location, taxes, vehicles beyond labelling buyability,
withdrawal-rate policy beyond the 3.5% Robin chose.

## Follow-up after the phase-2 critics (2026-11-07)

Both blind critics found that the first answer leaned on defaults Robin never chose
(`02-critic-claude.md`, `02-critic-gpt.md`). A default is a decision, so each one went back to Robin
(lessons 4 and 5). These are Robin's answers, written by the agent playing the fictional Robin.

**Agent:** FI ages past a cap are counted as the cap. The builder used 75, which made the bad case
look the same for every mix when stocks return 3%. What age should count as "never"?

**Robin:** "Don't hide the bad case. Use 85, and show me how often I never get there at all."

**Agent:** You said value is "maybe half a point over the market". Is your doubt about value mostly
the same doubt as about the market, plus a bit? The builder drew them independently.

**Robin:** "Mostly the same doubt. If stocks disappoint, value disappoints too, plus or minus the
half point."
*Agent's reading:* market and value centers correlated about 0.72 (1.8 / 2.5, the share of value's
uncertainty that is market uncertainty). The builder also reports 0.95 as a stress case.

**Agent:** Trend-following funds hold futures, and their gross exposure can exceed 100% (the
engine's proxy runs at about 1.6×). You said "no borrowing, no leveraged funds". Does that include
these?

**Robin:** "Yes. If the fund is running more than a dollar of exposure per dollar I put in, that's
leverage to me. Leave trend out."

**Agent:** The engine's value series averages small value and large value. One total-market value
fund would cover both. Does a value tilt count as one fund?

**Robin:** "One fund, if one fund does it. Label the mismatch."

**Agent:** If the results differ across eras and belief cells, how should they be combined?

**Robin:** "Pick the simplest mix that's inside the tie band in at least three-quarters of the
cells at every k I gave. If nothing clears that, keep it simple: all stocks."

| Definition | Robin's choice (2026-11-07) |
|---|---|
| Cap ("never") | 85; report the share that never reaches FI |
| Market–value center correlation | 0.72 primary; 0.95 stress |
| Trend | Excluded: counts as leverage under the standard |
| Value tilt | One fund; proxy mismatch labelled |
| Combining cells | Simplest mix in the band in ≥ 75% of cells at every k; otherwise 100 stocks |
