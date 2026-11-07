# Critic prompts

Give critics files, not conclusions. Fill the brackets, then send the prompt to a fresh agent: the
`ips-critic` agent, or `codex exec ... < /dev/null`.

## Answer review (after a builder round)

> You are a blind, adversarial reviewer. Read [answer file] and the code and outputs it cites in
> [folder]. Don't trust the report's framing; check the code and outputs.
>
> **Context:** the person's standard is [verbatim standard]. Scoring: [FI definition];
> S = median FI age + k × p90 FI age, k in [range]; options within [tie] years of the best tie,
> and the simpler wins.
>
> **Claimed conclusion:** [one sentence].
>
> **Check:**
> 1. Are inputs (return centers, vols, correlations) defensible, sourced, and fixed before
>    scoring? Is any input tilted for or against one option?
> 2. Are there code bugs, or unfair comparisons: paths not paired, different path counts, the
>    wrong baseline?
> 3. Does the result hold across samples and belief cells, or only in a corner?
> 4. Is there leverage, crisis behavior or illiquidity the model doesn't capture?
> 5. Can the person actually buy each option?
> 6. Does the wording overstate the evidence?
>
> Reply in under 400 words: a verdict (holds / doesn't / holds with caveats), then specific defects
> with file:line, each with a fix.

## Draft review (an IPS revision)

> You are a blind reviewer of a policy amendment. [new draft] vs [signed previous version]. The
> person decided, verbatim: [decisions]. Evidence: [files].
>
> **Check:**
> - (a) Does the draft enact exactly those decisions, and nothing more? Flag every addition and
>   say whether it is a necessary specification or overreach.
> - (b) Are there leftovers of retired rules?
> - (c) Is every state covered unambiguously?
> - (d) Do the quoted numbers match the evidence?
>
> Reply in under 300 words: sign-ready or not, then defects with line numbers and exact fixes.

## Confirm pass

> A prior review asked for: [list]. Verify each fix against [file] and [evidence], and look for any
> new contradiction or unauthorized policy. Reply in under 150 words: sign-ready or not, plus any
> remaining defect, with its line and fix.
