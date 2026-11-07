# Critic (Claude): review of 02-builder-answer.md

**Verdict: Q1 doesn't hold. Q2 holds, with caveats.** The Q1 headline rests on two defaults together, neither of them Robin's.

## Defects (most severe first)

1. **High (changes the verdict). `cap_age = 75` is an undisclosed default** (config-q1.toml:21; answer :47-49, missing from Defaults :122-139). The cap erases p90 in the stocks-3% cells, which creates 100 stocks' ties. At cap 85, 100 stocks is in the band in 1/0/0 of 8 cells, and 70/30 is the simplest pick in 7/8/8. **Fix:** list the cap as Robin's call, report cap 85, restate :29-34.
2. **High (changes the verdict). Independent centers contradict Default 2** (:128-129 moves value with the market) **and Robin's "half a point over the market"**, which implies corr ≈ 1.8/2.5 = 0.72 (config-q1.toml:13). At corr 0.72, 100 stocks is the simplest pick in 7/6/5 of 8. With cap 85 and corr 0.72, 70/30 drops out of the band at k ≥ .75 in 1–2 cells. With cap 85 and corr 0.95, **85/15 trend is the only mix in the band in all 8 cells at every k**. **Fix:** report the cap × corr grid, with corr 0.72 as primary. Withdraw "only mix in all 8", and rewrite :55-57: the lead comes from an independence assumption.
3. **Medium. Value fund buyability is unsourced** (:147-148). The "value" series averages small-value and big-value; if that takes two funds, 70/30 is a three-fund mix. **Fix:** cite a fund or broker, and count the funds.
4. **Medium. Trend funds use futures leverage, and Robin said "no leveraged funds"** (:154-155), yet :107 puts trend forward. **Fix:** ask Robin about leverage first.
5. **Low. "Paired" run-out** (:52-53) contradicts :174-175, where the quitter sets differ. **Fix:** "same paths, different quitters."
6. **Low. "At every k"** (:30): k has no effect in 4 of the 8 cells. **Fix:** say so.
7. **Low. The 85/15 count "5/5/5"** (:42) is 6/6/6 at seed 2. **Fix:** "5–6".

## Verified and correct

- Paths are paired, path counts are equal, and the baselines are right.
- The Q1 and S1–S3 numbers and the Q2 run-out ranges match the outputs.
- The Q2 FI gap of 0 holds by construction (policy.py:86-90). It is not a finding.
- 70/30 in 8/8 cells reproduces at seeds 2, 3 and 7.
- The timing of the Q2-S2 run is disclosed.
- Nothing reads as investment advice.
