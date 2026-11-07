# Draft review (Claude, blind), 04-ips.md

**Not sign-ready.**

1. **High, :81.** Nothing covers what Robin holds during the fund search, or the move from fallback to 70/30, before or after FI. **Fix:** Robin decides, then add "Until a fund is named, 100% market; if named before FI: [rule]; after FI: [rule]."
2. **Medium, :83-84.** The fallback's 80/20 switch was never decided. Decision 2 used 70/30 figures (lesson 5). **Fix:** get Robin's word, citing builder :112 (−2.6 to −4.2 pts).
3. **Medium, policy nobody decided.**
   - :60-61, "without accepting a higher chance…" is an added constraint. **Fix:** "…scored as in §1; run-out read beside the score."
   - :105 and :120 carry no label. **Fix:** label each "(agent default; Robin's call)".
   - :104, :113 and :118 are still open. **Fix:** Robin decides each in `03-decisions.md` before signing.
4. **Medium, :67.** Covers only 70/30, primary, seed 1. **Fix:** "7.4–12.6% (70/30; 7.35–13.0% over all seeds and variants); 8.9–14.9% under the fallback."
5. **Low, :79.** "Separately uncertain" is left over from independent centers. **Fix:** "uncertainty mostly shared with the market (corr 0.72)."
6. **Low, :88.** "Futures-based funds" widens Robin's rule. **Fix:** "any fund with more than $1 of exposure per $1 invested."
7. **Low, :94-96.** The buyability claims carry no sources. **Fix:** cite crsp.org and treasurydirect.gov; delete "or a broker"; at :95, write "no matching fund sourced".
8. **Low, :78.** **Fix:** "only one of three mixes tested". In §12, add that under the 0.95 stress the pick rests on k=1.0.

No investment advice found.

**Verified:**
- Re-running the combining rule on all nine Q1 CSVs picks 70/30 each time; counts match.
- The Q2 run-out ranges match `v2-q2.csv`.
- The 14/6 split, 75/25→61/19/20, the quit timing, the bands and the pro-rata withdrawals match `policy.py`.
- No cap-75, trend or keep-after-quit leftovers.
