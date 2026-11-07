# Phase 3: Robin decides (fictional)

Robin is fictional; the agent wrote Robin's replies. This file shows how `references/3-decide.md`
presents decisions, each with the person's words verbatim. Date: 2026-11-07. Evidence:
`02-builder-answer.md` (v2, after two blind critics and a confirm pass).

## Decision 1: accumulation mix

**As presented to Robin:**
> Under your standard and your combining rule, 70/30 market/value scores best. It is inside the
> tie band in 8 of 8 cells at every k, and 100 stocks fails at k ≥ 0.75. The trade-off: a 1-in-10
> FI age about 1.0–1.2 years earlier, and a median about 0.3 years earlier, for one more fund.
> It rests on your half-point value premium. With no premium, 100 stocks ties. It also needs a
> single value fund that covers small and large value, and none has been sourced yet.
> Not investment advice.
>
> (a) 70/30 market/value; (b) 100 stocks; (c) 70/30 only if you find one fund that does it,
> otherwise 100 stocks.

**Robin:** "(c). I believe the half point, but I won't hold two value funds to get it. If one fund
doesn't do it, all stocks."

*Agent's reading:* 70/30, conditional on one fund that Robin chooses; otherwise 100 stocks. Fund
selection is Robin's, not the agent's.

## Decision 2: quit-day switch

**As presented to Robin:**
> Moving 20% to bills on the quit date can't change your FI date: the score ties exactly. Your
> simplicity rule would therefore pick "keep". But the switch lowers the chance of running short
> after the quit by 2.3–4.5 points in every cell, seed and variant (across the cells, seed 1:
> from 10.2–16.6% to 7.4–12.6%). Staying quit is half your goal. A tie broken by simplicity would discard that.
> Not investment advice.
>
> (a) keep the mix after the quit; (b) move 20% to bills on the quit date.

**Robin:** "(b). 'Not have to go back' is the whole point. Three or four points less chance of
going back is worth one more fund and one rule."

*Agent's reading:* an exception to the simplicity tie-break, decided by Robin for this rule only,
on the grounds of the "Failure" line of the standard. It is not a general change to the tie rule
(lesson 5).

## Defaults surfaced as decisions

| Default (builder's) | Robin |
|---|---|
| "Stocks 3%" lowers value to 3.5% | "Yes, that's what I meant." |
| Bands ±5 points, also after the quit | "Fine." |
| Bills volatility 0.01 (0.02 gives the same pick) | "Fine." |
| Quit transfer = target-weight difference × portfolio value | "Fine. Write it down exactly." |

## What is closed and what is open

- **Closed:** the accumulation mix (conditional) and the quit-day switch.
- **Open:** which value fund, if any (Robin's search); taxes and account location (out of scope
  for this example); Social Security and flexible spending, which the engine doesn't model and
  which would lower every run-out figure.

## Decisions after the blind draft review (2026-11-07)

Both draft reviewers found that the draft relied on choices Robin hadn't made: what to hold during
the fund search, the fallback's quit-day switch, and the operating rules the agent had filled in
(`04-review-claude.md`, `04-review-gpt.md`). Each was put to Robin. These are Robin's words,
written by the agent playing the fictional Robin.

**D3. While searching for a value fund, and if one is found later.**
**Robin:** "Until I name a fund, all stocks. If I name one before I quit, move to 70/30 in one step
at the next month-end. If I name one after I've quit, move to 56/24/20 in one step at the next
month-end."

**D4. The fallback's quit-day switch.** Evidence: from 100 stocks, the switch lowers run-out by 2.6
to 4.2 points in every cell, seed and variant (`02-builder-answer.md` v2, Q2).
**Robin:** "Same reason as before. Under all-stocks, still move 20% to bills on the quit date."

**D5. Operating rules the agent proposed.**

| Proposed rule | Robin |
|---|---|
| Check the bands monthly, at month-end | "Yes." |
| New money goes to the sleeve furthest below target; on a tie, to market | "Yes." |
| Outside a band: rebalance every sleeve to target | "Yes." |
| Monthly order: quit transfer (if due), then contribution or withdrawal, then the band check | "Yes." |
| After the quit: withdraw $58,000 a year in today's dollars, monthly, pro rata across sleeves | "Yes." |
| Review the figures and beliefs every January, and re-score if any has moved | "Yes, January." |
| A trigger in §12 starts a review; it never changes the allocation by itself | "Right. Nothing changes without my signature." |

**Not decided, and left open:** what to do if the portfolio can't cover a month. The standard
names that as the failure; this IPS doesn't set a response.

## D6. Timing and edge cases, after the confirm pass (2026-11-07)

Both confirm reviewers found that §9's timing didn't match the engine, which the evidence comes
from (`policy.py`: FI is set at the month-end when the 12th month in a row completes; the quit
transfer happens right then, before the next month's returns; withdrawals start the following
month-end). They also found three edge cases left open.

**Agent:** Should the policy follow the model's timing exactly? And for the edge cases: (1) a fund
named in the same month you quit; (2) a contribution larger than the gap to target; (3) how the
withdrawal keeps pace with inflation.

**Robin:** "Match the model exactly, so the numbers mean what they say. (1) Go straight to
56/24/20. (2) All of it to the sleeve furthest below, then the band check, like the model. (3)
$58,000 in today's dollars, so raise it with CPI every January."

*Agent's reading:* each answer matches the engine's mechanics, except the yearly CPI step, which
the engine models as continuous real dollars. The difference is small, and it is labelled in
§9.

## D7. Indexing the quit number (2026-11-07, after the final confirm pass)

**Agent:** The engine checks FI against $1,660,000 in today's dollars. In the policy, should the
quit number rise with inflation? And if you name a value fund in the same month you reach FI,
should the change to 56/24/20 replace the quit transfer, so the mix isn't switched twice?

**Robin:** "Raise the quit number with CPI every January, same as the spending. And yes: one move
straight to 56/24/20, not two."

## Signature (2026-11-07)

Shown the five-line summary of `04-ips.md` (mix, fallback, quit switch, operating rules, open item).

**Robin:** "sign v1"
