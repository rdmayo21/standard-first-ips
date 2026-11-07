"""Pure-computation tests for the engine (no network)."""

from __future__ import annotations

import numpy as np

from ipsengine.config import Candidate, Person
from ipsengine.paths import block_indices, shape, shift_table
from ipsengine.policy import NEVER, run
from ipsengine.score import score

P = Person(
    age=40.0,
    start_wealth=100.0,
    annual_saving=0.0,
    quit_number=200.0,
    annual_spending=0.0,
    cap_age=50.0,
    horizon_age=60.0,
)


def test_block_indices_shape_and_contiguity() -> None:
    rng = np.random.default_rng(0)
    idx = block_indices(100, 130, 5, 60, rng)
    assert idx.shape == (5, 130)
    assert ((idx[:, 1:60] - idx[:, :59]) % 100 == 1).all()


def test_shape_hits_target_vol() -> None:
    r = np.random.default_rng(1).normal(0.01, 0.05, 600)
    x = shape(r, 0.12)
    assert abs(x.mean()) < 1e-12
    assert abs(x.std(ddof=1) * 12**0.5 - 0.12) < 1e-12


def test_shift_table_monotone() -> None:
    gs, _ = shift_table(np.random.default_rng(2).normal(0, 0.04, 400))
    assert np.all(np.diff(gs) > 0)


def test_fi_month_at_known_growth() -> None:
    # 1% a month, start 100, quit at 200: crosses in month ceil(log 2 / log 1.01) = 70
    rets = np.full((1, 3, 240), 0.01)
    res = run(rets, ["a"], Candidate("a", {"a": 1.0}), P)
    assert (res.fi_month == 70).all()


def test_never_reaching_is_censored() -> None:
    rets = np.zeros((1, 2, 240))
    res = run(rets, ["a"], Candidate("a", {"a": 1.0}), P)
    assert (res.fi_month == NEVER).all()


def test_band_rebalance_restores_target() -> None:
    rets = np.zeros((2, 1, 240))
    rets[0, 0, 0] = 1.0  # sleeve a doubles in month 1: 0.5/0.5 -> 2/3, 1/3
    res = run(rets, ["a", "b"], Candidate("ab", {"a": 0.5, "b": 0.5}, band=0.05), P, keep_nav=True)
    assert abs(res.nav[0, 0] - 150.0) < 1e-9
    assert res.turnover[0] > 0


def test_withdrawals_run_out() -> None:
    p = Person(
        age=40.0,
        start_wealth=100.0,
        annual_saving=0.0,
        quit_number=100.0,
        annual_spending=120.0,
        cap_age=50.0,
        horizon_age=60.0,
    )
    rets = np.zeros((1, 1, 240))
    res = run(rets, ["a"], Candidate("a", {"a": 1.0}), p)
    assert res.fi_month[0] == 1  # at the number from the start
    assert res.ruin_month[0] < NEVER


def test_quit_day_switch_moves_exact_share() -> None:
    p = Person(
        age=40.0,
        start_wealth=100.0,
        annual_saving=0.0,
        quit_number=100.0,
        annual_spending=0.0,
        cap_age=50.0,
        horizon_age=60.0,
    )
    rets = np.zeros((2, 1, 240))
    c = Candidate("sw", {"a": 1.0}, post_quit={"a": 0.9, "b": 0.1}, band=0.05)
    res = run(rets, ["a", "b"], c, p, keep_nav=True)
    assert abs(res.nav[0, -1] - 100.0) < 1e-9  # wealth conserved through the move


def test_score_formula() -> None:
    ages = np.arange(40, 50, dtype=float)
    s = score(ages, (0.0, 1.0))
    assert s[0] == np.median(ages)
    assert abs(s[1] - (np.median(ages) + np.percentile(ages, 90))) < 1e-12


def test_quit_move_never_shorts() -> None:
    from ipsengine.policy import quit_move

    H = np.array([[46.0], [54.0]])  # drifted from 50/50
    out = quit_move(H, np.array([[0.5], [0.5]]), np.array([[0.0], [1.0]]))
    assert (out >= 0).all()
    assert abs(out.sum() - 100.0) < 1e-9


def test_center_is_compound_not_log() -> None:
    import pandas as pd

    from ipsengine.config import Sleeve
    from ipsengine.paths import make_paths

    r = np.random.default_rng(3).normal(0.005, 0.04, 1200)
    df = pd.DataFrame({"a": r})
    s = Sleeve("a", "x", center=0.10, center_sd=0.0, vol=0.15)
    out = make_paths(df, [s], {}, {}, 4000, 600, 7, 60)
    g = np.expm1(np.log1p(out[0]).mean() * 12)
    assert abs(g - 0.10) < 0.004


def test_bad_correlation_rejected() -> None:
    import pytest

    from ipsengine.config import Sleeve
    from ipsengine.paths import center_draws

    sl = [
        Sleeve("a", "x", 0.05, 0.01, 0.1),
        Sleeve("b", "x", 0.05, 0.01, 0.1),
        Sleeve("c", "x", 0.05, 0.01, 0.1),
    ]
    corr = {("a", "b"): 0.99, ("a", "c"): 0.99, ("b", "c"): -0.99}
    with pytest.raises(ValueError):
        center_draws(sl, {}, corr, 10, np.random.default_rng(0))


def test_fi_age_never_exceeds_cap() -> None:
    from ipsengine.score import fi_ages

    p = Person(
        age=40.05,
        start_wealth=100.0,
        annual_saving=0.0,
        quit_number=200.0,
        annual_spending=0.0,
        cap_age=50.0,
        horizon_age=60.0,
    )
    rets = np.full((1, 2, 240), 0.0058)  # reaches 200 in about month 120, near the cap
    res = run(rets, ["a"], Candidate("a", {"a": 1.0}), p)
    assert (fi_ages(res, p) <= p.cap_age).all()


def test_config_rejects_bad_inputs(tmp_path) -> None:
    import pytest

    from ipsengine.config import load

    base = """
[person]
age = 35.0
start_wealth = 1.0
annual_saving = 1.0
quit_number = 10.0
annual_spending = 1.0
[model]
paths = 32
{model}
[sleeves.a]
source = "market"
center = 0.04
center_sd = 0.01
vol = {vol}
[[candidates]]
name = "a"
targets = {{ a = 1.0 }}
"""
    bad = [
        ("samples = []", "0.17"),
        ("k = [nan]", "0.17"),
        ("", "inf"),
        ('center_corr = { "a,a" = 0.5 }', "0.17"),
    ]
    f = tmp_path / "s.toml"
    f.write_text(
        base.format(model="", vol="0.17") + '\n[[scenarios]]\nname = "x"\ncenters = { a = nan }\n'
    )
    with pytest.raises(ValueError):
        load(f)
    for model, vol in bad:
        f = tmp_path / "c.toml"
        f.write_text(base.format(model=model, vol=vol))
        with pytest.raises(ValueError):
            load(f)


def test_paths_never_lose_more_than_99_pct() -> None:
    import pandas as pd

    from ipsengine.config import Sleeve
    from ipsengine.paths import make_paths

    r = np.random.default_rng(4).standard_t(2, 600) * 0.2
    df = pd.DataFrame({"a": r})
    out = make_paths(df, [Sleeve("a", "x", 0.02, 0.0, 0.9)], {}, {}, 200, 300, 1, 60)
    assert out.min() >= -0.99
