# Lessons from a real run, as checks

Each lesson comes from something that went wrong, or nearly did, when one person rebuilt their
IPS with this process (Nov 2026). The specific results below come from that person's figures and
beliefs. They illustrate the checks; they are not general findings about any asset. Apply each
as a check.

## About the person and the decision

1. **Standard before questions.** Agent-framed questions carry the agent's frame. *Check:* is
   there an adopted, dated, verbatim standard before any allocation question was asked?
2. **The FI definition decides more than the mix.**
   - At first touch of the number, 100% stocks tied for best.
   - Tested as "quit and stay quit", 85/15 stocks/trend won.
   - *Check:* is the operational definition the person's choice, and was it tested more than one
     way?
3. **A tie on the score can discard what the goal cares about.** Two options reached FI on the
   same date, and the agent let "simpler wins" pick, but one ran out after quitting about 2 points
   less often. *Check:* when a tie is broken by simplicity, did you look at every other part of the
   person's goal first?
4. **Defaults hide decisions.** *Check:* is every default you set listed in the result as the
   person's call?
5. **Agreement to one rule isn't agreement to its neighbour.** *Check:* did you infer a decision
   the person didn't state?
6. **Re-read the wording against their answers.** The standard's draft drifted from "one to
   three" to "two to three". *Check:* does the final text match what they said?

## About the evidence

7. **Test each rule separately.** Two "gates" looked like one rule.
   - One was noise: days of FI time, with the sign flipping by era.
   - The other was a real trade: months of FI time for points of crash depth.
   - *Check:* is each mechanism tested on its own?
8. **Era dependence.**
   - The long-Treasury edge depended on post-2000 negative stock–bond correlation.
   - A gate helped in the 1927–2026 sample and hurt in the post-1990 sample.
   - *Check:* is every result reported in at least two samples, and flagged where they disagree?
9. **Corner wins are watch items.** One fund won by more than a year, but only in one corner of
   the beliefs and savings tested, and its edge came from built-in leverage. *Check:* does a
   "win" hold across cells, and is any leverage scored as leverage?
10. **Changing an input after seeing results is result-chasing.** A builder lowered one asset's
    return center a minute after seeing it win, and applied that skeptical rule to that asset only.
    *Check:* are centers fixed before scoring, and is any revision applied to every asset alike,
    and disclosed?
11. **Proxies and synthetic crisis timing flatter.** Placing an alternative's crisis shocks on
    arbitrary months understates how it moves with stocks in a crash. *Check:* are the proxy's
    limits written next to the result?
12. **Precision words matter.** A critic objected to "noise" for an effect that was small but
    statistically detectable. "Economically small and era-dependent" was the honest wording.
    *Check:* are effect sizes stated in the person's units, with their direction across samples?
13. **Can they buy it?** Many alternatives (interval funds, private credit, reinsurance, VC) were
    closed to non-accredited buyers, adviser-only, or closed outright. *Check:* is every vehicle
    labelled buyable or not, with the source?
14. **Relative bands for small sleeves didn't help.** ±5 points on a 15% sleeve is already ±33%
    relative, and tighter bands traded 30–40% more for nothing. *Check:* test band shapes before
    assuming the intuitive one.

## About the process

15. **Critics from two model families, every round.** Each round found something. *Check:* did at
    least two blind critics, ideally from different model families, review every answer and
    every draft?
16. **Read logs before declaring failure.** GPT critics were reported "timed out" when codex was
    waiting on stdin; the full reports were in the logs. *Check:* `< /dev/null`, and read the
    output before calling a run failed.
17. **Drafts gain unauthorized policy.** Every IPS draft review found an addition nobody decided.
    *Check:* run "nothing more than the decisions" as an explicit review question.
18. **Not investment advice.** The person decides and executes. *Check:* no trade, account change
    or purchase is made by the agent from this process.
