"""nhl-sim-2.0: state-dependent, period-resolved NHL game simulator (RESEARCH_ONLY shadow arm; V1 is untouched).

Why a new simulator (docs/research/V2_RESEARCH.md has the evidence): nhl-sim-1.1 draws regulation goals as two
independent Poissons plus a 3-minute goalie-pull window with prior multipliers (leader x4.0, trailer x1.8). It
under-predicts regulation ties (17.4% vs 22.8% observed in the 2024-26 walk-forward). Real scoring is not
state-free: trailing teams press, leading teams sit back, tied teams late in the third play for the point, and
the trailing team pulls its goalie. All four push probability mass toward ties and toward specific margins.

What one draw does (vectorised over ``n_sims``; ``step_min`` minutes per step, default 0.5):

* A team's scoring rate in step ``s`` is ``lam * env * scale * m[b(s), d]`` where ``lam`` is its expected
  regulation goals per 60 minutes (the same quantity V1 feeds its simulator), ``b(s)`` the time bucket the step
  falls in and ``d`` the team's OWN score differential at the start of the step (clipped to -3..+3). The
  multiplier table ``m`` is ESTIMATED from play-by-play goal times (MoneyPuck shots, team-game fixed effects so
  team strength cannot leak into it) -- see ``nhl_edge.research.state_hazards``. Empty-net goals are inside the
  table (the leader's rate at d=+1 in the final minutes), so there is no separate pull window and no double count.
* Goals are credited to the period the step belongs to, so ``P1 + P2 + P3 == regulation`` on every draw by
  construction (tested), and the third period interacts with score effects and the pull because it IS where the
  state-dependent buckets live.
* ``env ~ Gamma(k, 1/k)`` (mean 1) is an optional shared game environment (over-dispersion / positive total
  correlation); its dispersion is chosen on a validation season, 0 disables it.
* Regulation tie -> overtime: 3-on-3 decided before the shootout with probability ``p_ot_goal`` (estimated from
  history), OT/SO winner from the shrunk strength ratio as in V1. The winner is credited one goal (NHL convention).

The table is a parameter file (``data/params/nhl-sim-2.0.json``) with its training seasons recorded, never tuned on
the evaluation games. Same seed + same inputs + same params reproduce every probability exactly.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import numpy as np

from nhl_edge import SIM_V2_VERSION
from nhl_edge.config import REPO_ROOT
from nhl_edge.sim.engine import SimResult, TeamParams

# regulation minute edges of the hazard buckets: P1, P2, then the third period cut finer where the game changes
TIME_EDGES: tuple[float, ...] = (0.0, 20.0, 40.0, 50.0, 55.0, 57.0, 58.0, 59.0, 60.0)
DIFFS: tuple[int, ...] = (-3, -2, -1, 0, 1, 2, 3)
PARAMS_PATH = REPO_ROOT / "data" / "params" / "nhl-sim-2.0.json"


@dataclass(frozen=True)
class SimV2Params:
    mult: tuple[tuple[float, ...], ...] = tuple(tuple(1.0 for _ in DIFFS) for _ in range(len(TIME_EDGES) - 1))
    scale: float = 1.0
    env_dispersion: float = 0.0
    p_ot_goal: float = 0.66
    ot_shrink: float = 0.55
    so_shrink: float = 0.25
    time_edges: tuple[float, ...] = TIME_EDGES
    diffs: tuple[int, ...] = DIFFS
    provenance: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["mult"] = [list(r) for r in self.mult]
        return d

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> SimV2Params:
        return cls(mult=tuple(tuple(float(x) for x in r) for r in d["mult"]), scale=float(d.get("scale", 1.0)),
                   env_dispersion=float(d.get("env_dispersion", 0.0)), p_ot_goal=float(d.get("p_ot_goal", 0.66)),
                   ot_shrink=float(d.get("ot_shrink", 0.55)), so_shrink=float(d.get("so_shrink", 0.25)),
                   time_edges=tuple(float(x) for x in d.get("time_edges", TIME_EDGES)), diffs=tuple(int(x) for x in d.get("diffs", DIFFS)),
                   provenance=dict(d.get("provenance") or {}))

    def replace(self, **kw: Any) -> SimV2Params:
        return SimV2Params.from_dict(self.to_dict() | kw)


def load_params(path: Path | None = None) -> SimV2Params:
    p = Path(path) if path else PARAMS_PATH
    return SimV2Params.from_dict(json.loads(p.read_text())) if p.exists() else SimV2Params()


@dataclass
class SimV2Result(SimResult):
    """A :class:`SimResult` (so every V1 pricer works unchanged) plus per-period goals."""

    home_periods: np.ndarray | None = None  # (n_sims, 3)
    away_periods: np.ndarray | None = None
    params: SimV2Params | None = None
    step_min: float = 0.5

    def period_goals(self, period: int, home: bool) -> np.ndarray:
        arr = self.home_periods if home else self.away_periods
        return arr[:, period - 1]

    def p_period_win(self, period: int, home: bool) -> tuple[float, float]:
        h, a = self.period_goals(period, True), self.period_goals(period, False)
        return self.p(h > a) if home else self.p(a > h)

    def p_period_tie(self, period: int) -> tuple[float, float]:
        return self.p(self.period_goals(period, True) == self.period_goals(period, False))

    def p_period_total_gt(self, period: int, x: float) -> tuple[float, float]:
        return self.p(self.period_goals(period, True) + self.period_goals(period, False) > x)

    def p_period_margin_gt(self, period: int, home: bool, x: float) -> tuple[float, float]:
        m = self.period_goals(period, True) - self.period_goals(period, False)
        return self.p((m if home else -m) > x)

    def summary(self) -> dict[str, Any]:
        s = super().summary()
        s["sim_version"] = SIM_V2_VERSION
        s["config"] = {"step_min": self.step_min, "params": {k: v for k, v in (self.params.to_dict() if self.params else {}).items() if k != "mult"}}
        for p in (1, 2, 3):
            h, a = self.period_goals(p, True), self.period_goals(p, False)
            s[f"p{p}"] = {"home_goals_mean": float(h.mean()), "away_goals_mean": float(a.mean()), "total_mean": float((h + a).mean()),
                          "p_home_win": float(np.mean(h > a)), "p_away_win": float(np.mean(a > h)), "p_tie": float(np.mean(h == a)),
                          "total_ladder": {f"over_{x + 0.5:.1f}": float(np.mean(h + a > x + 0.5)) for x in range(0, 4)}}
        return s


def simulate_game_v2(home: TeamParams, away: TeamParams, seed: int, n_sims: int = 20_000, params: SimV2Params | None = None,
                     step_min: float = 0.5) -> SimV2Result:
    if home.lam <= 0 or away.lam <= 0:
        raise ValueError("expected goals must be positive")
    prm = params or load_params()
    n = int(n_sims)
    rng = np.random.default_rng(seed)
    env = np.ones(n)
    if prm.env_dispersion > 0:
        k = 1.0 / prm.env_dispersion
        env = rng.gamma(k, 1.0 / k, n)
    mult = np.asarray(prm.mult, dtype=float)  # (n_buckets, n_diffs)
    edges = np.asarray(prm.time_edges, dtype=float)
    dmin, dmax = min(prm.diffs), max(prm.diffs)
    base_h = home.lam * env * prm.scale * step_min / 60.0
    base_a = away.lam * env * prm.scale * step_min / 60.0
    h = np.zeros(n, dtype=np.int64)
    a = np.zeros(n, dtype=np.int64)
    hp = np.zeros((n, 3), dtype=np.int64)
    ap = np.zeros((n, 3), dtype=np.int64)
    n_steps = int(round(60.0 / step_min))
    for s in range(n_steps):
        t_mid = (s + 0.5) * step_min
        b = int(np.searchsorted(edges, t_mid, side="right") - 1)
        b = min(max(b, 0), mult.shape[0] - 1)
        per = min(int(t_mid // 20.0), 2)
        d = np.clip(h - a, dmin, dmax) - dmin
        gh = rng.poisson(base_h * mult[b, d])
        ga = rng.poisson(base_a * mult[b, (dmax - dmin) - d])  # the away team's own differential is the mirror image
        h += gh
        a += ga
        hp[:, per] += gh
        ap[:, per] += ga
    tied = h == a
    ot_goal = tied & (rng.random(n) < prm.p_ot_goal)
    so = tied & ~ot_goal
    ratio = home.lam / (home.lam + away.lam)
    p_home_ot = 0.5 + prm.ot_shrink * (ratio - 0.5)
    p_home_so = 0.5 + prm.so_shrink * (ratio - 0.5)
    u = rng.random(n)
    home_wins_extra = np.where(ot_goal, u < p_home_ot, u < p_home_so) & tied
    hf = h + (tied & home_wins_extra)
    af = a + (tied & ~home_wins_extra)
    return SimV2Result(home_reg=h, away_reg=a, overtime=tied.copy(), shootout=so, home_final=hf.astype(int), away_final=af.astype(int),
                       seed=seed, n_sims=n, sim_version=SIM_V2_VERSION, home=home, away=away, home_periods=hp, away_periods=ap, params=prm, step_min=step_min)


def period_violations(res: SimV2Result) -> list[str]:
    """Coherence checks specific to the period model (on top of ``engine.ladder_violations``)."""
    out = []
    if not np.array_equal(res.home_periods.sum(axis=1), res.home_reg):
        out.append("home P1+P2+P3 != regulation")
    if not np.array_equal(res.away_periods.sum(axis=1), res.away_reg):
        out.append("away P1+P2+P3 != regulation")
    if (res.home_periods < 0).any() or (res.away_periods < 0).any():
        out.append("negative period goals")
    return out
