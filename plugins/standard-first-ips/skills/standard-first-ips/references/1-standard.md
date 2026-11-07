# Phase 1: the goal and the standard

The standard is the yardstick every later answer is scored against. If it is missing or vague,
every later answer is just the agent's taste.

## Why this comes first

In the run this skill comes from, the agent first proposed a list of "IPS questions" (how much
of each asset, how much leverage, and so on). The person pointed out that the questions were
already biased: he had no standard for answering them. He was right. A question framed by the
agent carries the agent's frame. The fix was to stop and establish the goal and the standard
first, in the person's words.

## How to run the interview

Ask in rounds of two to four short questions. Wait for answers. Expect "I don't know" and treat
it as information: offer two or three concrete pictures to react to, not a definition to accept.

**Round 1: the goal.**
- What is the money for? What would "done" look like? (Example answers: "no longer needing the
  paycheck", "a house in 10 years", "leave X to my kids".)
- As early as possible, or by a date?

**Round 2: failure.** Ask what *real* failure looks like for them. Don't ask about drawdowns yet.
- Offer pictures: "markets fall 50% and you have to work three more years" vs "you lose your
  income and can't cover your life". Which one is the failure they're guarding against?
- What covers them if they can't work: emergency fund (how many months?), disability insurance,
  family? The portfolio should be the last line, and saying so changes the answer.

**Round 3: losses.** Use a concrete, extreme picture: "a 90% loss that you don't know will
recover". What would they do? Work longer? Sell? Have they held through a big loss before? Most
people discover their real tolerance is about *time* (it pushes back the goal), not about the
size of the number.

**Round 4: typical vs bad case.** Score two dates: the typical (median) date and the
1-in-10 bad-case date. Ask: "A year earlier in the typical case is worth how many years in the bad
case?" Turn the answer into a weight k. "One to three years of bad case per typical year" means k
from 1/3 to 1. Report every result at several k values in that range.

**Round 5: what counts as a tie.** "If two options differ by less than about ___ year(s), does it
matter?" Most people say about a year. Then: "within a tie, should the simpler option win?" Make
"simpler" explicit: fewer funds, fewer rules, no leverage over leverage, fewer account moves.

**Round 6: borrowing and caution.** Is borrowing to invest allowed if the math calls for it? How
should uncertainty about future returns count: once (inside the simulation), or again as an
extra haircut? (Counting it twice is a common silent error.)

## Write the standard

Draft a short standard (under 200 words) under these headings: Goal; Growth and caution;
Losses; Failure. Use their words. Show it to them, take edits, and repeat until they say "adopt".

Then write the **operational definitions** the standard leaves open, and ask about each one. The
biggest is usually what counts as reaching the goal:
- first touch of the number;
- the number held N months;
- or "can quit and stay quit", tested by withdrawing from the quit date.

This choice can flip the whole answer. In the source run, with that person's figures and
beliefs, the all-stock candidate tied for best at first touch but lost clearly once "stay quit"
was tested. That is an illustration, not a general result.

The engine scores first reach, or the number held N months. It reports run-out after the quit
next to the score but does not fold it into the score. If the person chooses "quit and stay
quit", show both, and treat a lower run-out at the same date as part of their goal.

**Check for drift between their answers and your draft.** In the source run, the adopted draft
said "two to three" years when the person's answers supported "one to three". Re-read their
answers against the final wording before they adopt, and flag any mismatch.

Record: the standard verbatim, the date, the answers it came from, and each operational
definition with its own date.
