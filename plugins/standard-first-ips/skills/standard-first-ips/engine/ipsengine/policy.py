"""Run one rebalancing policy over every path: save, reach FI, quit, withdraw.

Each month, in order:
1. If this is the quit month and the candidate has `post_quit` targets, move (post - pre) x NAV
   between sleeves; other holdings keep their drift. A sleeve that has drifted below the amount
   to be taken gives only what it holds, and the receiving sleeves get the total actually moved,
   pro rata (no short positions).
2. Apply the month's returns.
3. Before the quit: add the month's saving to the sleeve furthest below its target
   (smallest holding / target). After the quit: withdraw the month's spending pro rata.
4. If any sleeve is more than `band` (absolute) from its target, rebalance every sleeve to
   target.

FI is reached at the end of the first month in which NAV has been at or above the quit number
for `hold_months` months in a row (1 month when hold_months is 0, i.e. first reach). The quit
starts the next month. Paths that never reach FI by `cap_age` are censored at `cap_age`.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .config import Candidate, Person

NEVER = 10**7


@dataclass(frozen=True)
class RunResult:
    fi_month: np.ndarray  # months elapsed at FI (NEVER if not reached by cap_age)
    ruin_month: np.ndarray  # first post-quit month NAV can't cover spending (NEVER if none)
    turnover: np.ndarray  # mean yearly traded share of NAV while saving
    nav: np.ndarray | None  # (n, months) if keep_nav


def quit_move(H: np.ndarray, pre: np.ndarray, post: np.ndarray) -> np.ndarray:
    """Holdings after the quit-day move, never below zero. H is (n_sleeves, n)."""
    nav = H.sum(axis=0)
    delta = (post - pre) * nav
    take = np.minimum(-np.minimum(delta, 0), H)  # what each giving sleeve can actually give
    give = np.maximum(delta, 0)
    tot_give = give.sum(axis=0)
    share = np.divide(give, tot_give, out=np.zeros_like(give), where=tot_give > 0)
    return H - take + share * take.sum(axis=0)


def months_for(p: Person) -> tuple[int, int]:
    """(months to cap_age, months to horizon_age)."""
    acc = int(np.ceil((p.cap_age - p.age) * 12))
    tot = int(np.ceil((p.horizon_age - p.age) * 12))
    if acc <= 0 or tot < acc:
        raise ValueError("need age < cap_age <= horizon_age")
    return acc, tot


def run(
    rets: np.ndarray,
    names: list[str],
    cand: Candidate,
    person: Person,
    keep_nav: bool = False,
) -> RunResult:
    """Simulate `cand` on returns of shape (n_sleeves, n, months) ordered like `names`."""
    acc, tot = months_for(person)
    n_s, n, months = rets.shape
    if months < tot:
        raise ValueError(f"paths have {months} months, need {tot}")
    pre = np.array([cand.targets.get(s, 0.0) for s in names])[:, None]
    post = (
        np.array([cand.post_quit.get(s, 0.0) for s in names])[:, None]
        if cand.post_quit is not None
        else pre
    )
    H = person.start_wealth * np.broadcast_to(pre, (n_s, n)).copy()
    fi = np.full(n, NEVER)
    ruin = np.full(n, NEVER)
    run_len = np.zeros(n, dtype=int)
    need = max(1, person.hold_months)
    traded = np.zeros(n)
    saving_months = np.zeros(n)
    nav_rec = np.empty((n, tot)) if keep_nav else None
    save_m, spend_m = person.annual_saving / 12, person.annual_spending / 12
    for i in range(tot):
        quit_now = i >= fi  # quit starts the month after FI
        if cand.post_quit is not None:
            move = i == fi
            if move.any():
                H = np.where(move, quit_move(H, pre, post), H)
        H = H * (1 + rets[:, :, i])
        tgt = np.where(quit_now, post, pre)
        saving = ~quit_now
        if save_m:
            ratio = np.where(tgt > 0, H / np.where(tgt > 0, tgt, 1.0), np.inf)
            pick = ratio.argmin(axis=0)
            add = np.zeros_like(H)
            add[pick, np.arange(n)] = save_m * saving
            H = H + add
        if quit_now.any():
            nav = H.sum(axis=0)
            short = quit_now & (nav < spend_m) & (ruin == NEVER)
            ruin = np.where(short, i + 1, ruin)
            f = np.where(quit_now, np.clip(1 - spend_m / np.maximum(nav, 1e-9), 0, 1), 1.0)
            H = H * f
        nav = H.sum(axis=0)
        w = H / np.maximum(nav, 1e-12)
        out = (np.abs(w - tgt) > cand.band + 1e-12).any(axis=0)
        new = tgt * nav
        traded += np.where(
            out & saving, np.abs(H - new).sum(axis=0) / 2 / np.maximum(nav, 1e-12), 0
        )
        saving_months += saving
        H = np.where(out, new, H)
        nav = H.sum(axis=0)
        if i < acc:
            ok = (nav >= person.quit_number) & (fi == NEVER)
            run_len = np.where(ok, run_len + 1, 0)
            fi = np.where((fi == NEVER) & (run_len >= need), i + 1, fi)
        if nav_rec is not None:
            nav_rec[:, i] = nav
    turnover = traded / np.maximum(saving_months, 1) * 12
    return RunResult(fi, ruin, turnover, nav_rec)
