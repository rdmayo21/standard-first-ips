# Standard-first IPS

A workflow for writing or revising a personal Investment Policy Statement where:
- **you write the goal and the scoring standard first,** in your own words, before anyone asks
  about assets;
- **every policy answer is derived from that standard** by a builder agent;
- **blind critics from two model families attack each answer** before you see it;
- **you decide** every question, with the trade-off in your own units (years until financial
  independence, chance of running out);
- **a written IPS** comes out the end, reviewed and signed.

It comes from one person's rebuild of their own IPS in November 2026. The lessons from that run
are built in as checks (`references/lessons.md`).

**See it run:** [`examples/worked-example/`](examples/worked-example/) takes a fictional investor
from the first interview question to a signed IPS. It includes the engine output and every blind
critic review. In that run, the critics overturned the first answer before the investor saw it.

> **Not investment advice.** This is educational software and a process. It doesn't know your
> situation and doesn't recommend securities. You make and execute every decision. Check
> anything that matters with a qualified professional.

## Three ways to use it

| Form | Use when | Gets you |
|---|---|---|
| **Claude Code plugin** (recommended) | You use Claude Code | The skill, the builder and critic subagents, and the simulation engine in one install |
| **Agent Skill only** | You use another agent that reads `SKILL.md` (several do) | The workflow and the engine. The builder and critic agents aren't included, so start two fresh reviewers yourself, ideally from different model families |
| **Chat prompt** (`PROMPT.md`) | You only use a chat app | The interview, the standard and the IPS draft. No simulations and no second-model review, so treat its numbers as hypotheses |

### Install the plugin (Claude Code)

```
/plugin marketplace add rdmayo21/standard-first-ips
/plugin install standard-first-ips@standard-first-ips
/reload-plugins
```

Then say "help me write my investment policy statement", or run
`/standard-first-ips:standard-first-ips`.

### Use the skill alone

Copy `plugins/standard-first-ips/skills/standard-first-ips/` into your agent's skills folder,
for example `~/.claude/skills/` for Claude Code. Other agents that read `SKILL.md` have their own
folder; check their docs.

**Optional second-model critic:** install the OpenAI Codex CLI. The skill uses
`codex exec ... < /dev/null` as a GPT critic when it's present.

### The engine

Work in your own folder, not inside the plugin:

```bash
ENGINE=/path/to/standard-first-ips/plugins/standard-first-ips/skills/standard-first-ips/engine
mkdir -p ~/ips-work && cd ~/ips-work
uv run --project "$ENGINE" ips-engine fetch --data ~/ips-work/data
cp "$ENGINE/examples/example.toml" my_config.toml   # set [data] dir to ~/ips-work/data (absolute)
uv run --project "$ENGINE" ips-engine score my_config.toml
uv run --project "$ENGINE" --group dev pytest -q "$ENGINE/tests"
```

It needs Python 3.11+ and [uv](https://docs.astral.sh/uv/). The data is public: the Ken French
data library, FRED CPI, and AQR's Century of Factor Premia. `references/engine.md` lists what the
engine doesn't model. Quote those limits with any result.

## The four phases

1. **Standard:** an interview in short rounds that ends in a written, adopted standard and the
   operational definition of "reaching the goal".
2. **Derive:** a builder answers each open question from the standard, using the engine. At least
   two blind critics attack it, the fixes get a confirm pass, and buyability is checked.
3. **Decide:** bottom line first, the trade-off in your units, one-line options, and every agent
   default flagged as yours.
4. **Write:** the IPS from the template, a blind "nothing more than the decisions" review, and
   your signature.

## Layout

```
.claude-plugin/marketplace.json
plugins/standard-first-ips/
  .claude-plugin/plugin.json
  agents/ips-builder.md, ips-critic.md
  skills/standard-first-ips/
    SKILL.md
    references/  1-standard, 2-derive, 3-decide, 4-ips, lessons, critic-prompts, engine, ips-template
    engine/      ipsengine (Python), tests, examples/example.toml
PROMPT.md        chat-only version
```

## License

MIT. See `LICENSE`. Not investment advice; provided as is, without warranty.
