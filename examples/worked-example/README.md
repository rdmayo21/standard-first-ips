# Worked example: one fictional investor, start to finish

This folder is a complete run of the standard-first-ips process for **Robin**, a fictional
44-year-old pharmacist. An agent wrote Robin's answers. Everything else is real: the engine
output on public data, both blind critics (Claude and GPT, from different model families), and
every defect they found. Not investment advice. Robin's numbers and beliefs are inputs to the
example, not recommendations.

**The point:** the first answer was wrong, and the critics caught it before Robin saw it.

## What happened, in five steps

1. **Standard** (`01-standard.md`). Six rounds of questions before any question about assets.
   Robin's goal: "Stop needing the pharmacy paycheck, ideally before 55, and not have to go
   back."
2. **Builder** (`02-builder-answer.md`; the v1 configs and results are kept). The plugin's builder scored
   four mixes and two quit-day switches across 2 eras × 4 belief scenarios, 8,000 paired paths
   each. Its first headline: "70/30 market/value is the only mix within a year of the best in all
   8 cells."
3. **Blind critics** (`02-critic-claude.md`, `02-critic-gpt.md`). Claude's verdict: *"Q1 doesn't
   hold."* The questions behind the defaults went back to Robin, the builder re-scored, and a
   confirm pass from both critics followed.
4. **Decisions** (`03-decisions.md`). Robin chose, with the trade-off in years and in the chance
   of running out. Robin also overrode the simplicity rule once, and said why.
5. **IPS** (`04-ips.md`). Drafted, then reviewed blind by both critics ("not sign-ready" from
   both). The gaps went back to Robin (D3–D7), and three more rounds of review followed, until
   both critics said "sign-ready". Then Robin signed.

## What the critics caught

| # | Found by | Defect | What changed |
|---|---|---|---|
| 1 | Claude, GPT | FI ages past **75** counted as 75. That erased the bad case whenever stocks returned 3%, which is how all-stocks earned its ties. Robin never chose the cap. | Robin chose 85 ("Don't hide the bad case"), and the share that never reaches FI is now shown |
| 2 | Claude, GPT | Market and value returns were drawn **independently**, which handed value a diversification edge Robin doesn't believe in ("If stocks disappoint, value disappoints too") | Re-scored at correlation 0.72 (and 0.95 as a stress case) |
| 3 | GPT, Claude | The trend proxy runs at about **1.6× exposure**, and Robin said "no leveraged funds" | Robin excluded trend |
| 4 | Claude | No source that one value fund covers small and large value. Is the tilt one fund or two? | The value tilt is now conditional on one fund; otherwise all stocks |
| 5 | GPT | Tie counts moved with the random seed | Seeds 1–3 reported for every variant |
| 6 | GPT | The quit transfer was described as a pro-rata sale. It isn't one. | Corrected and written into the IPS exactly |
| 7 | Claude, GPT | The IPS draft added an objective and a behavioral rule nobody decided (one of them written by the lead agent) | Removed. Robin's words are quoted instead |
| 8 | Claude, GPT | The draft didn't cover holdings during the fund search, or the fallback's quit-day switch | Robin decided both (D3, D4) |
| 9 | GPT | Operating rules (monthly checks, withdrawal method, January review) were agent defaults | Put to Robin, and adopted (D5) |
| 10 | Claude, GPT | The draft's quit timing was a month off from the engine the evidence came from, and a fund change in the quit month could switch the mix twice | Timing matched to the engine (D6), one move instead of two (D7) |

## Before and after

| | First answer (v1) | After critics and Robin's decisions |
|---|---|---|
| Mix | "Depends on how you combine cells"; trend as a watch item | 70/30 market/value if one fund does it, otherwise 100% stocks |
| How sure | Ties created by a cap nobody chose | 70/30 inside the tie band in 8/8 cells at every k, for every seed and stress case; fragile only if there's no value premium, or at k = 0.5 alone |
| After the quit | Keep the mix (simplest) | Move 20% to T-bills: it lowers the modelled chance of running short by 2.3–4.5 points, and staying quit is half of Robin's goal |

## Read it in this order

`01-standard.md` → `02-critic-claude.md` → `02-builder-answer.md` → `03-decisions.md` →
`04-ips.md`. Each review file sits next to the step it reviewed. The `*-prompt.txt` files are the
exact prompts the critics received.

## Reproduce

From the repository root (the engine data is fetched once):

```bash
E=plugins/standard-first-ips/skills/standard-first-ips/engine
uv run --project "$E" ips-engine fetch --data "$E/data"
cd examples/worked-example
uv run --project "../../$E" ips-engine score config-v2-q1.toml --out /tmp/v2-q1.csv
python3 combine_v2.py 1.0 "100 stocks" /tmp/v2-q1.csv
```

`manifest-v2.txt` holds SHA-256 hashes of every v2 config, written before the v2 scoring.
`config-q*.toml` and `results-q*.md` are the v1 run, kept so you can see what the critics
reviewed.

## Limits

- The engine doesn't model taxes, Social Security, flexible spending, or costs beyond the data,
  and the future isn't a resample of 1927–2026 (`references/engine.md`).
- Robin is fictional, so this shows the process, not anyone's result.
- An agent played Robin. A real person's answers would be messier, and the interview is built
  for that.
