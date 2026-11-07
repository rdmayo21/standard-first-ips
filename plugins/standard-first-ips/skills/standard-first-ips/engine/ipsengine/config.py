"""Read and validate an engine config (TOML)."""

from __future__ import annotations

import math
import tomllib
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class Person:
    """The saver. Money figures are real (today's) dollars."""

    age: float
    start_wealth: float
    annual_saving: float
    quit_number: float
    annual_spending: float
    cap_age: float = 75.0
    horizon_age: float = 95.0
    hold_months: int = 0  # 0 = FI at first reach of quit_number; N = held N months in a row


@dataclass(frozen=True)
class Sleeve:
    """One asset sleeve: its historical shape source and the user's forward belief."""

    name: str
    source: str
    center: float  # real compound (geometric) annual return the user plans on
    center_sd: float  # uncertainty of that center (sd of the long-run mean)
    vol: float  # annual volatility the shape is scaled to


@dataclass(frozen=True)
class Candidate:
    """A policy to score: target weights, an optional quit-day switch, and its band."""

    name: str
    targets: dict[str, float]
    post_quit: dict[str, float] | None = None
    band: float = 0.05  # absolute half-width, e.g. 0.05 = ±5 percentage points


@dataclass(frozen=True)
class Scenario:
    """A belief variant: overrides some sleeve centers."""

    name: str
    centers: dict[str, float] = field(default_factory=dict)


@dataclass(frozen=True)
class Model:
    paths: int = 8000
    seed: int = 1
    block_months: int = 60
    k: tuple[float, ...] = (1 / 3, 1 / 2, 1.0)
    tie_years: float = 1.0
    samples: tuple[tuple[str, str], ...] = (("1927-07", "2100-12"),)
    center_corr: dict[tuple[str, str], float] = field(default_factory=dict)
    batches: int = 16


@dataclass(frozen=True)
class Config:
    person: Person
    model: Model
    sleeves: dict[str, Sleeve]
    candidates: list[Candidate]
    scenarios: list[Scenario]
    data_dir: Path
    base_dir: Path  # the config's folder; relative csv: paths resolve against it


def _check_weights(name: str, w: dict[str, float], sleeves: dict[str, Sleeve]) -> None:
    if not all(math.isfinite(v) for v in w.values()):
        raise ValueError(f"candidate {name!r}: weights must be finite numbers")
    unknown = set(w) - set(sleeves)
    if unknown:
        raise ValueError(f"candidate {name!r}: unknown sleeves {sorted(unknown)}")
    if any(v < 0 for v in w.values()):
        raise ValueError(f"candidate {name!r}: negative weight (leverage is not modeled)")
    if abs(sum(w.values()) - 1.0) > 1e-9:
        raise ValueError(f"candidate {name!r}: weights sum to {sum(w.values())}, not 1")


def load(path: Path) -> Config:
    """Parse a TOML config.

    Raises:
        ValueError: Weights that don't sum to 1, unknown sleeves, or bad settings.
    """
    raw = tomllib.loads(path.read_text())
    person = Person(**raw["person"])
    m = raw.get("model", {})
    samples = tuple(tuple(s.split(":")) for s in m.get("samples", ["1927-07:2100-12"]))
    corr = {tuple(k.split(",")): float(v) for k, v in m.get("center_corr", {}).items()}
    model = Model(
        paths=int(m.get("paths", 8000)),
        seed=int(m.get("seed", 1)),
        block_months=int(m.get("block_months", 60)),
        k=tuple(float(x) for x in m.get("k", [1 / 3, 1 / 2, 1.0])),
        tie_years=float(m.get("tie_years", 1.0)),
        samples=samples,  # type: ignore[arg-type]
        center_corr=corr,  # type: ignore[arg-type]
        batches=int(m.get("batches", 16)),
    )
    if not model.samples or any(len(s) != 2 for s in model.samples):
        raise ValueError('model.samples needs at least one "YYYY-MM:YYYY-MM" entry')
    if not all(math.isfinite(k) and k >= 0 for k in model.k):
        raise ValueError("every k must be a finite, non-negative number")
    if not math.isfinite(model.tie_years):
        raise ValueError("tie_years must be finite")
    if model.batches < 2 or model.paths < model.batches:
        raise ValueError("need paths >= batches >= 2")
    if model.block_months < 1 or model.tie_years < 0 or not model.k:
        raise ValueError("block_months >= 1, tie_years >= 0 and at least one k are required")
    for k, v in vars(person).items():
        if not math.isfinite(float(v)):
            raise ValueError(f"person.{k} must be a finite number")
    if person.start_wealth < 0 or person.annual_saving < 0 or person.annual_spending < 0:
        raise ValueError("wealth, saving and spending must be non-negative")
    if person.quit_number <= 0 or person.hold_months < 0:
        raise ValueError("quit_number must be positive and hold_months non-negative")
    sleeves = {n: Sleeve(name=n, **v) for n, v in raw["sleeves"].items()}
    for sl in sleeves.values():
        vals = (sl.vol, sl.center_sd, sl.center)
        if not all(math.isfinite(float(v)) for v in vals):
            raise ValueError(f"sleeve {sl.name!r}: center, center_sd and vol must be finite")
        if not (sl.vol > 0 and sl.center_sd >= 0 and sl.center > -0.99):
            raise ValueError(f"sleeve {sl.name!r}: need vol > 0, center_sd >= 0, center > -99%")
    for (a, b), rho in corr.items():
        if a == b:
            raise ValueError(f"center_corr {a},{b}: a sleeve's correlation with itself is 1")
        if not -1 < rho < 1:
            raise ValueError(f"center_corr {a},{b}: must be strictly between -1 and 1")
    cands = []
    for c in raw["candidates"]:
        cand = Candidate(
            name=c["name"],
            targets={k: float(v) for k, v in c["targets"].items()},
            post_quit=(
                {k: float(v) for k, v in c["post_quit"].items()} if "post_quit" in c else None
            ),
            band=float(c.get("band", 0.05)),
        )
        _check_weights(cand.name, cand.targets, sleeves)
        if cand.post_quit is not None:
            _check_weights(cand.name + " (post_quit)", cand.post_quit, sleeves)
        if not 0 < cand.band < 0.5:
            raise ValueError(f"candidate {cand.name!r}: band must be in (0, 0.5)")
        cands.append(cand)
    if not cands:
        raise ValueError("no candidates")
    scen = [Scenario(s["name"], dict(s.get("centers", {}))) for s in raw.get("scenarios", [])]
    for s in scen:
        if not all(math.isfinite(float(v)) and float(v) > -0.99 for v in s.centers.values()):
            raise ValueError(f"scenario {s.name!r}: centers must be finite and above -99%")
        bad = set(s.centers) - set(sleeves)
        if bad:
            raise ValueError(f"scenario {s.name!r}: unknown sleeves {sorted(bad)}")
    if not scen:
        scen = [Scenario("base")]
    for a, b in corr:
        if a not in sleeves or b not in sleeves:
            raise ValueError(f"center_corr: unknown sleeve pair {a},{b}")
    data_dir = (path.parent / raw.get("data", {}).get("dir", "data")).resolve()
    return Config(person, model, sleeves, cands, scen, data_dir, path.parent.resolve())
