# GPT critic (Codex CLI 0.159.2, blind), 2026-11-07

Prompt: `critic-prompt.txt`. Final message verbatim:


**Verdict: holds with caveats.** Saved headline arithmetic checks out; seed 2 preserves 70/30’s unique all-cell tie-band membership and every Q2 run-out reduction. Candidates use equal, paired paths and appropriate Q2 baselines. These support conditional educational findings, not an implementable recommendation.

1. **HIGH — `config-q1.toml:13`; `ipsengine/paths.py:56`.** Independent centers give 70/30 approximate center uncertainty of 1.47%, versus market’s 1.8%; correlation 0.8 raises it to 1.91%. This grants value substantial assumption-driven tail diversification. S1 weakens, but does not eliminate, its edge. **Fix:** justify joint beliefs or model market plus uncertain value premium; headline both dependence cases.

2. **HIGH — `ipsengine/score.py:15`; `config-q1.toml:21`.** Never-FI paths become age 75, collapsing p90 differences in pessimistic cells despite differing failure-to-quit rates. That cap is absent from Robin’s operational definitions. **Fix:** label p90 as censored, report nonattainment beside headline scores, and test cap sensitivity before interpreting simplicity wins.

3. **HIGH — `ipsengine/data.py:159`; `02-builder-answer.md:144`.** Trend sizing has no exposure cap; raw proxy median gross exposure is approximately 1.64×. Robin explicitly rejects leveraged funds (`01-standard.md:60`). Weights summing to one do not enforce that constraint. Margin, liquidity and execution stress are absent. Retail availability does not establish an eligible implementation; [actual funds disclose leverage risk](https://www.ishares.com/us/literature/prospectus/pro-ismf-etf.pdf). **Fix:** identify a compliant vehicle, map exposures and costs, and stress-test it; otherwise mark trend eligibility unresolved.

4. **MEDIUM — `02-builder-answer.md:39`.** Exact tie counts are seed-sensitive: seed 2 changes stocks’ k=.5 count from 5 to 6, and trend’s counts from 5/5/5 to 6/6/6. Historical samples also overlap. **Fix:** report repeated-seed classification stability; distinguish cell coverage from independent corroboration.

5. **MEDIUM — `ipsengine/policy.py:41` versus `02-builder-answer.md:124`.** Quit transfers use target-weight differences, not proportional actual holdings: drifted 75/25 becomes 61/19/20, not 60/20/20. **Fix:** implement proportional sales or accurately describe and separately test the existing rule.

6. **MEDIUM — `config-q1.toml:10`; `02-builder-answer.md:129`.** Historical volatility calculations reproduce, but bills alone bypasses the stated rule; pre-scoring chronology is asserted rather than independently established by a frozen manifest. **Fix:** source the exception, test bills at calculated volatility, and preserve timestamped config/data hashes.
