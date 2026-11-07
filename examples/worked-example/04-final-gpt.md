# GPT final confirm on IPS draft v3 (Codex CLI, blind), 2026-11-07


**Not sign-ready.** One material defect remains:

- **Lines 90–92, 115–136:** Fund conversion still has no position in the monthly sequence. When naming a fund coincides with FI, §5 requires 56/24/20 while §9 separately requires a quit transfer, risking a double switch. **Fix:** specify conversion after cash flow, band check and FI determination; if FI is reached that month, convert directly to 56/24/20 **instead of** the quit transfer. Otherwise use the applicable pre-/post-FI targets.

The ordinary §9 timing matches `policy.py`, apart from the labelled CPI step. Other prior defects are addressed. No advice-like wording found; insufficient-balance handling remains explicitly open.
