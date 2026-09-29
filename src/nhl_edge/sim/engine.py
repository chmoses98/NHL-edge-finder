"""Coherent NHL game simulator (``SIM_VERSION`` in ``nhl_edge``): one joint draw prices every score-derived market.

What one simulated game produces (all integers/booleans, vectorised over ``n_sims``):

    home_reg, away_reg      goals after three periods (includes the empty-net window)
    overtime, shootout      whether the game needed OT / a shootout
    home_final, away_final  official final score (winner of OT/SO is credited one extra goal, as the NHL does)
    winner                  +1 home, -1 away (never 0: NHL games have a winner)
    reg_winner              +1 home, -1 away, 0 regulation tie

Scoring model (V1, deliberately simple and documented in docs/SIMULATION.md):

* Regulation is split into a 57-minute "ordinary" window and a 3-minute "late" window. Ordinary goals are Poisson
  with each team's expected-goal rate. A shared environment multiplier ``E ~ Gamma(k, 1/k)`` (mean 1) can be
  switched on to induce over-dispersion / positive total correlation; V1 ships with it OFF (``env_dispersion=0``)
  because plain Poisson is the empirical baseline that has to be beaten, not assumed.
* Late window: if the margin is 1 or 2 the trailing team is assumed to pull its goalie. The leader's rate is
  multiplied by ``EN_LEADER_MULT`` (empty net), the trailer's by ``PULL_ATTACK_MULT`` (6-on-5). Otherwise ordinary
  rates apply. These multipliers are priors, not estimates, and are the first thing to calibrate from play-by-play
  (the landing feed flags empty-net goals).
* Regulation tie -> overtime. ``P(OT ends in a goal)`` is ``p_ot_goal`` (rest go to the shootout). The OT winner is
  drawn from the strength ratio shrunk toward 0.5 (3-on-3 is high variance); the shootout winner from a further
  shrunk ratio. Either way the winner's final score is regulation + 1.

Everything is driven by a numpy ``Generator`` seeded by the caller, so a slate re-run with the same seed and inputs
reproduces every probability to the last digit.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

import numpy as np

from nhl_edge import SIM_VERSION

# --- priors (documented, crude, to be estimated) --------------------------------------------------
LATE_WINDOW_MIN = 3.0  # minutes of regulation treated as the goalie-pull window
EN_LEADER_MULT = 4.0  # leader's scoring rate multiplier while the trailer's net is empty
PULL_ATTACK_MULT = 1.8  # trailer's scoring rate multiplier at 6-on-5
DEFAULT_P_OT_GOAL = 0.66  # share of overtime games decided before the shootout (NHL 2019-2025 ~ 0.63-0.70)
OT_STRENGTH_SHRINK = 0.55  # OT win prob = 0.5 + shrink * (strength_ratio - 0.5)
SO_STRENGTH_SHRINK = 0.25
DEFAULT_N_SIMS = 20_000


@dataclass(frozen=True)
class TeamParams:
    """Expected regulation goals (60-minute, all situations) for one team in one game, after every adjustment."""

    team_id: int
    abbrev: str
    lam: float  # expected goals for, per 60 minutes, vs this opponent, with this goalie in the other net
    components: dict[str, float] = field(default_factory=dict)  # how lam was built (for the packet)


@dataclass(frozen=True)
class SimConfig:
    n_sims: int = DEFAULT_N_SIMS
    env_dispersion: float = 0.0  # Gamma shape k = 1/env_dispersion; 0 == off (plain Poisson)
    p_ot_goal: float = DEFAULT_P_OT_GOAL
    late_window_min: float = LATE_WINDOW_MIN
    en_leader_mult: float = EN_LEADER_MULT
    pull_attack_mult: float = PULL_ATTACK_MULT
    ot_shrink: float = OT_STRENGTH_SHRINK
    so_shrink: float = SO_STRENGTH_SHRINK


@dataclass
class SimResult:
    home_reg: np.ndarray
    away_reg: np.ndarray
    overtime: np.ndarray
    shootout: np.ndarray
    home_final: np.ndarray
    away_final: np.ndarray
    seed: int
    n_sims: int
    sim_version: str = SIM_VERSION
    config: SimConfig = field(default_factory=SimConfig)
    home: TeamParams | None = None
    away: TeamParams | None = None

    # ---- derived arrays ---------------------------------------------------------------------
    @property
    def winner(self) -> np.ndarray:
        return np.where(self.home_final > self.away_final, 1, -1)

    @property
    def reg_winner(self) -> np.ndarray:
        return np.sign(self.home_reg - self.away_reg)

    @property
    def margin(self) -> np.ndarray:
        """home final minus away final (OT/SO wins are +/-1)."""
        return self.home_final - self.away_final

    @property
    def total(self) -> np.ndarray:
        return self.home_final + self.away_final

    def team_final(self, home: bool) -> np.ndarray:
        return self.home_final if home else self.away_final

    def team_margin(self, home: bool) -> np.ndarray:
        return self.margin if home else -self.margin

    # ---- probabilities (each with a Monte Carlo standard error) ------------------------------
    def p(self, mask: np.ndarray) -> tuple[float, float]:
        m = float(np.mean(mask))
        return m, float(np.sqrt(max(m * (1 - m), 1e-12) / self.n_sims))

    def p_win(self, home: bool) -> tuple[float, float]:
        return self.p(self.winner == (1 if home else -1))

    def p_reg_win(self, home: bool) -> tuple[float, float]:
        return self.p(self.reg_winner == (1 if home else -1))

    def p_reg_tie(self) -> tuple[float, float]:
        return self.p(self.reg_winner == 0)

    def p_overtime(self) -> tuple[float, float]:
        return self.p(self.overtime)

    def p_shootout(self) -> tuple[float, float]:
        return self.p(self.shootout)

    def p_margin_gt(self, home: bool, x: float) -> tuple[float, float]:
        return self.p(self.team_margin(home) > x)

    def p_total_gt(self, x: float) -> tuple[float, float]:
        return self.p(self.total > x)

    def p_team_total_gt(self, home: bool, x: float) -> tuple[float, float]:
        return self.p(self.team_final(home) > x)

    def p_margin_in(self, home: bool, lo: float, hi: float) -> tuple[float, float]:
        m = self.team_margin(home)
        return self.p((m >= lo) & (m <= hi))

    def p_btts(self) -> tuple[float, float]:
        return self.p((self.home_final > 0) & (self.away_final > 0))

    def summary(self) -> dict[str, Any]:
        q = (0.05, 0.25, 0.5, 0.75, 0.95)
        tot = self.total
        mar = self.margin
        return {
            "sim_version": self.sim_version, "n_sims": self.n_sims, "seed": self.seed,
            "config": asdict(self.config),
            "home_lambda": self.home.lam if self.home else None, "away_lambda": self.away.lam if self.away else None,
            "home_goals_mean": float(self.home_final.mean()), "away_goals_mean": float(self.away_final.mean()),
            "home_reg_mean": float(self.home_reg.mean()), "away_reg_mean": float(self.away_reg.mean()),
            "total_mean": float(tot.mean()), "total_sd": float(tot.std()), "total_var_over_mean": float(tot.var() / max(tot.mean(), 1e-9)),
            "margin_mean": float(mar.mean()), "margin_sd": float(mar.std()),
            "p_home_win": self.p_win(True)[0], "p_away_win": self.p_win(False)[0],
            "p_home_reg_win": self.p_reg_win(True)[0], "p_away_reg_win": self.p_reg_win(False)[0], "p_reg_tie": self.p_reg_tie()[0],
            "p_overtime": self.p_overtime()[0], "p_shootout": self.p_shootout()[0], "p_btts": self.p_btts()[0],
            "total_quantiles": {str(k): float(v) for k, v in zip(q, np.quantile(tot, q))},
            "margin_quantiles": {str(k): float(v) for k, v in zip(q, np.quantile(mar, q))},
            "total_ladder": {f"over_{x + 0.5:.1f}": self.p_total_gt(x + 0.5)[0] for x in range(3, 10)},
            "home_puckline_ladder": {f"home_by_more_than_{x + 0.5:.1f}": self.p_margin_gt(True, x + 0.5)[0] for x in range(-3, 3)},
            "home_team_total_ladder": {f"home_over_{x + 0.5:.1f}": self.p_team_total_gt(True, x + 0.5)[0] for x in range(1, 6)},
            "away_team_total_ladder": {f"away_over_{x + 0.5:.1f}": self.p_team_total_gt(False, x + 0.5)[0] for x in range(1, 6)},
            "margin_pmf": {str(int(k)): float(v) for k, v in zip(*np.unique(mar, return_counts=True)) for v in [v / self.n_sims]},
            "total_pmf": {str(int(k)): float(v) for k, v in zip(*np.unique(tot, return_counts=True)) for v in [v / self.n_sims]},
        }


def simulate_game(home: TeamParams, away: TeamParams, seed: int, config: SimConfig = SimConfig()) -> SimResult:
    if home.lam <= 0 or away.lam <= 0:
        raise ValueError("expected goals must be positive")
    n = int(config.n_sims)
    rng = np.random.default_rng(seed)
    env = np.ones(n)
    if config.env_dispersion > 0:
        k = 1.0 / config.env_dispersion
        env = rng.gamma(k, 1.0 / k, n)
    ordinary_min = 60.0 - config.late_window_min
    lam_h = home.lam * env
    lam_a = away.lam * env
    h = rng.poisson(lam_h * ordinary_min / 60.0)
    a = rng.poisson(lam_a * ordinary_min / 60.0)

    # late window: goalie pull when trailing by 1 or 2
    late = config.late_window_min / 60.0
    diff = h - a
    home_trailing = (diff <= -1) & (diff >= -2)
    away_trailing = (diff >= 1) & (diff <= 2)
    mult_h = np.where(home_trailing, config.pull_attack_mult, np.where(away_trailing, config.en_leader_mult, 1.0))
    mult_a = np.where(away_trailing, config.pull_attack_mult, np.where(home_trailing, config.en_leader_mult, 1.0))
    h = h + rng.poisson(lam_h * late * mult_h)
    a = a + rng.poisson(lam_a * late * mult_a)

    tied = h == a
    ot = tied.copy()
    ot_goal = tied & (rng.random(n) < config.p_ot_goal)
    so = tied & ~ot_goal
    ratio = home.lam / (home.lam + away.lam)
    p_home_ot = 0.5 + config.ot_shrink * (ratio - 0.5)
    p_home_so = 0.5 + config.so_shrink * (ratio - 0.5)
    u = rng.random(n)
    home_wins_extra = np.where(ot_goal, u < p_home_ot, u < p_home_so) & tied
    hf = h + (tied & home_wins_extra)
    af = a + (tied & ~home_wins_extra)
    return SimResult(home_reg=h, away_reg=a, overtime=ot, shootout=so, home_final=hf.astype(int), away_final=af.astype(int),
                     seed=seed, n_sims=n, config=config, home=home, away=away)


def ladder_violations(res: SimResult) -> list[str]:
    """Consistency checks a coherent joint draw must satisfy; any violation is a bug, not a model opinion."""
    problems: list[str] = []
    ph, pa = res.p_win(True)[0], res.p_win(False)[0]
    if abs(ph + pa - 1.0) > 1e-9:
        problems.append(f"P(home)+P(away)={ph + pa}")
    rh, ra, rt = res.p_reg_win(True)[0], res.p_reg_win(False)[0], res.p_reg_tie()[0]
    if abs(rh + ra + rt - 1.0) > 1e-9:
        problems.append(f"regulation outcomes sum {rh + ra + rt}")
    if abs(rt - res.p_overtime()[0]) > 1e-9:
        problems.append("P(reg tie) != P(overtime)")
    if res.p_shootout()[0] > res.p_overtime()[0] + 1e-12:
        problems.append("P(shootout) > P(overtime)")
    prev = 2.0
    for x in np.arange(0.5, 12.5, 1.0):
        p = res.p_total_gt(x)[0]
        if p > prev + 1e-12:
            problems.append(f"total ladder not monotone at {x}")
        prev = p
    for home in (True, False):
        prev = 2.0
        for x in np.arange(-6.5, 7.5, 1.0):
            p = res.p_margin_gt(home, x)[0]
            if p > prev + 1e-12:
                problems.append(f"puck-line ladder not monotone at {x} home={home}")
            prev = p
        prev = 2.0
        for x in np.arange(0.5, 9.5, 1.0):
            p = res.p_team_total_gt(home, x)[0]
            if p > prev + 1e-12:
                problems.append(f"team-total ladder not monotone at {x} home={home}")
            prev = p
    return problems
