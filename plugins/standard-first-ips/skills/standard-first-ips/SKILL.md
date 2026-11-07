---
name: standard-first-ips
license: MIT
description: Build or revise a personal Investment Policy Statement (IPS) the rigorous way. First the user writes their own goal and scoring standard. Then every policy question is derived from that standard by a builder agent, attacked by blind critics from two model families, and decided by the user. Includes a simulation engine for FI-date scoring and the lessons from a real run. Use when someone wants to write or overhaul an IPS, settle an asset allocation or rebalancing rule against their own goals, test a strategy idea (trend, bonds, alternatives, leverage) against their plan, or says their past investing research "wasn't systematic". Educational; not investment advice.
---

# Standard-first IPS

A workflow for turning "I've read a lot and done random things" into a written policy whose every
rule traces back to a goal the person stated in their own words, with an independent check on
every claim before they adopt it.

**What this is not.** It is not investment advice, and you (the agent) are not an adviser. You run
a process; the person makes every decision. Say so at the start, and repeat it in one line
with every decision you present.

**Never, in any phase:**
- recommend a security or a transaction ("buy X", "sell Y");
- say an option is suitable for the person;
- present a modeled result as a forecast.

Say "under your standard as written, X scores best", and give the limits beside it.

## The four phases

Run them in order. Don't skip phase 1 even if the person arrives with a portfolio question.

1. **Standard.** Elicit the person's goal and scoring standard *before* any question about
   assets. Read `references/1-standard.md`.
2. **Derive.** For each open policy question, a builder answers it from the standard (with the
   engine where numbers matter) and blind critics attack the answer. Read
   `references/2-derive.md` and `references/critic-prompts.md`; the agents are in the plugin's
   `agents/` folder.
3. **Decide.** Present each answer as the person's call, with the trade-off in plain words. Say
   what their standard selects under the stated scoring rule, and flag every default you set as a
   decision. Read `references/3-decide.md`.
4. **Write the IPS.** Draft, run a blind consistency review, fix, re-check, then the person
   signs. Read `references/4-ips.md` and use `references/ips-template.md`.

Before phase 2, read `references/lessons.md`. It lists the failures a real run hit, and each one
is a check you must apply.

## The engine

`engine/` (inside this skill's folder) is a small Python package. It scores candidate policies on
simulated paths: the person's FI age at median and at the 1-in-10 bad case, plus run-out risk
after quitting.
- Work in the person's own folder, never inside the installed skill or plugin, which an update can
  overwrite.
- Use the engine's absolute path. ENGINE below is this skill's base directory plus `/engine`.

```bash
mkdir -p ~/ips-work && cd ~/ips-work
uv run --project ENGINE ips-engine fetch --data ~/ips-work/data
cp ENGINE/examples/example.toml my_config.toml   # then set [data] dir = "/abs/path/ips-work/data"
uv run --project ENGINE ips-engine score my_config.toml --out results.csv
```

Every number in the example is a placeholder. The config holds the person's figures and
beliefs. Never invent their figures: ask for them, and mark anything
you estimate as an estimate. Read `references/engine.md` for what the engine does and does not
model; quote those limits whenever you report a result.

## Rules that apply throughout

- **The person's words, verbatim.** Record their goal, standard and every decision in their own
  words, with the date. Paraphrase only beside the quote, labelled as your reading.
- **No question before the standard.** Questions framed by you ("how much trend do you want?")
  smuggle in your frame. Ask what they're trying to achieve and how they'd judge success first.
- **Every number has a source.** Live data, their statement, or "estimate (agent)". Never a bare
  figure.
- **Defaults are decisions.** If you pick a default to keep moving, say so in the result and give
  them the alternative. A default you didn't surface can silently overrule what they care about.
- **Read the logs before calling a run failed.** Background tools can hang on input or time out
  silently; the answer may already be in the output.
- **Nothing is traded from this process.** The output is a document. Execution is theirs.
