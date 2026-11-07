# Phase 2: derive each answer, then attack it

This is a builder/critic loop (sometimes called a gauntlet). One agent builds an answer; fresh
agents that never saw the builder's reasoning try to break it. The person sees only what survives,
plus what the critics changed.

## List the open questions

Write every open policy question as a row: the question; where it came from; what it touches.
Typical rows:
- allocation mix and leverage;
- rebalancing rule (bands, calendar, any trend or "gate" signals);
- each asset class someone has suggested (bonds, TIPS, trend/managed futures, gold, alternatives);
- account location;
- what happens at the goal date (keep the mix, or switch);
- withdrawal rate and fallback cover.

Order them so earlier answers don't depend on later ones. The allocation usually comes after the
FI definition and before location.

## Brief the builder

Write a brief the builder can act on cold (the "intern test": could a capable stranger do it
from this page alone?). It must include:
- the absolute path of the engine (this skill's base directory plus `/engine`) and of the
  person's work folder (subagents don't know where the plugin is installed);
- the standard, verbatim;
- the scoring method;
- the person's figures, each with its source;
- the candidates to score;
- what is out of scope.

Ask for:
- the answer, stated as what the standard selects, not as advice;
- the evidence (engine output, sources);
- what would flip it;
- limits, stated plainly.

The builder is in `agents/ips-builder.md`. Spawn it with the brief. Never hand the builder your
preferred answer; an agent handed a hypothesis tends to return it confirmed.

## Score with the engine

For any question about mix, rebalancing or quit-day switches, use the engine. Score every
candidate on the same paths, across:
- at least two historical samples (e.g. from 1927 and from 1990), because results that hold in
  only one era are fragile;
- the person's belief range, with a scenario per center they consider plausible;
- every k in their range.

Report how many cells each candidate is within the tie band, and the simplest candidate inside
it. A candidate that wins only in one corner (one sample, one belief, one savings path) is a
watch item, not a change. The simplest pick ignores run-out. If the person's goal includes
staying quit, show the run-out column and the "lowest run-out within the tie band" line beside
it. The engine reports staying quit; it does not score it.

Test each rule on its own. In the source run, two "trend gates" looked like one rule.
- **The gate on contributions:** an effect of days, whose sign flipped by era. Noise.
- **The gate on moving trend into stocks in a crash:** a consistent trade, one to three months of
  FI time for 2–9 points less crash depth.

Bundled, they would have been judged together and wrongly.

## Run the critics

Use at least two critics. Use **different model families** where you can: a second family catches
things the first shares blind spots on.
- **Claude critic:** `agents/ips-critic.md`.
- **GPT critic,** if the Codex CLI is installed:
  `codex exec --skip-git-repo-check -C <dir> "<prompt>" < /dev/null > critic.log 2>&1`.
  The `< /dev/null` matters: from a background shell, codex waits on stdin until killed and looks
  like a timeout.

Give critics the files, not your conclusion. Use `references/critic-prompts.md`. Ask for a verdict
and specific defects with file and line.

Then:
- fix what they find;
- run a short confirm pass on the fixes;
- record what each critic changed.

In the source run, critics found something every round, including:
- a return estimate cut right after the builder saw it winning;
- a "buyable winners: none" claim that was false;
- unauthorized policy added to a draft;
- overstated precision ("noise" for an effect that was small but measurable);
- a comparison against the wrong baseline.

## Check access

When the person names a fund or asset class they're considering, check whether they can actually
buy it: accreditation, minimums, broker availability, closures. Score unbuyable ones anyway, but
label them. A great answer they can't buy is not an answer. Don't propose specific funds
yourself; the person chooses vehicles.

## What to hand to phase 3

For each question:
- the answer, in one sentence;
- the trade-off, in plain words;
- the evidence, with caveats;
- what the critics changed;
- what would flip it;
- each default you set, flagged.
