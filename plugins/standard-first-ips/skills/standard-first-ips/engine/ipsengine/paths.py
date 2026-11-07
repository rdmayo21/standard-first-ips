"""Simulated return paths: joint block bootstrap of history, rescaled to the user's beliefs.

History supplies the *shape* (fat tails, crashes, the way sleeves move together, regimes that
last years). The user's beliefs supply the *level*: each path draws its own expected return for
each sleeve from the stated center and its uncertainty, so estimation risk is counted once,
inside the paths, and not again as a separate haircut.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import Sleeve


def shape(r: np.ndarray, vol: float) -> np.ndarray:
    """Demean and scale monthly returns to an annual volatility.

    Raises:
        ValueError: Non-finite data or a series with no variation.
    """
    if not np.isfinite(r).all():
        raise ValueError("historical series has non-finite values")
    sd = r.std(ddof=1)
    if not sd > 0:
        raise ValueError("historical series has no variation; can't scale it")
    return (r - r.mean()) * vol / (sd * 12**0.5)


def shift_table(x0: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Monthly shift m -> annual log growth of x0 + m (monotone in m)."""
    ms = np.linspace(-0.06, 0.06, 2401)
    gs = np.array([np.log1p(np.clip(x0 + m, -0.99, None)).mean() * 12 for m in ms])
    return gs, ms


def block_indices(
    n_obs: int, months: int, n_paths: int, block: int, rng: np.random.Generator
) -> np.ndarray:
    """Circular block bootstrap indices, shape (n_paths, months)."""
    k = int(np.ceil(months / block))
    starts = rng.integers(0, n_obs, size=(n_paths, k))
    return ((starts[:, :, None] + np.arange(block)) % n_obs).reshape(n_paths, -1)[:, :months]


def center_draws(
    sleeves: list[Sleeve],
    centers: dict[str, float],
    corr: dict[tuple[str, str], float],
    n: int,
    rng: np.random.Generator,
) -> np.ndarray:
    """Each path's expected compounded real return per sleeve, shape (n, n_sleeves)."""
    names = [s.name for s in sleeves]
    c = np.eye(len(names))
    for (a, b), rho in corr.items():
        if a == b:
            raise ValueError(f"center_corr {a},{b}: a sleeve's correlation with itself is 1")
        i, j = names.index(a), names.index(b)
        c[i, j] = c[j, i] = rho
    try:
        chol = np.linalg.cholesky(c)
    except np.linalg.LinAlgError as e:
        raise ValueError("center_corr is not a valid correlation matrix") from e
    z = rng.standard_normal((n, len(names))) @ chol.T
    mu = np.array([centers.get(s.name, s.center) for s in sleeves])
    sd = np.array([s.center_sd for s in sleeves])
    return mu + sd * z


def make_paths(
    sample: pd.DataFrame,
    sleeves: list[Sleeve],
    centers: dict[str, float],
    corr: dict[tuple[str, str], float],
    n: int,
    months: int,
    seed: int,
    block: int,
) -> np.ndarray:
    """Real monthly returns, shape (n_sleeves, n, months).

    `sample` holds one column per sleeve (real monthly returns on common dates). The same seed
    gives the same blocks and the same normal draws, so every candidate and scenario is scored
    on paired paths.

    Raises:
        ValueError: The sample is shorter than one block.
    """
    if len(sample) < block:
        raise ValueError(f"sample has {len(sample)} months, fewer than one {block}-month block")
    rng = np.random.default_rng(seed)
    idx = block_indices(len(sample), months, n, block, rng)
    g = center_draws(sleeves, centers, corr, n, rng)
    out = np.empty((len(sleeves), n, months))
    if (g <= -0.99).any():
        raise ValueError("a drawn center is at or below -99%; lower center_sd")
    lg = np.log1p(g)  # centers are compound annual returns; the table is in log growth
    for j, s in enumerate(sleeves):
        x0 = shape(sample[s.name].to_numpy(), s.vol)
        gs, ms = shift_table(x0)
        if lg[:, j].min() < gs[0] or lg[:, j].max() > gs[-1]:
            raise ValueError(f"sleeve {s.name!r}: drawn centers outside the calibration range")
        # same floor as the calibration table: no monthly loss beyond -99%
        out[j] = np.clip(x0[idx] + np.interp(lg[:, j], gs, ms)[:, None], -0.99, None)
    return out
