"""Goalie saves for PLAYER_SIM_V1: a full distribution per simulated game, driven by the same draw as everything else.

Per draw, for the goalie of team T facing opponent O:

    goals against  = O's simulated goals that were NOT into an empty net (regulation + OT; shootout attempts are not
                     shots on goal and never count)
    full-game saves ~ NegBin(mu, alpha),  log mu = a + b log(expected non-goal shots faced) + c margin_T + d GA + e OT
                     (coefficients: ``players.params.fit_saves``), so the saves move with the simulated game script
    replacement    : after his k-th goal against before 50:00 the starter is replaced with the estimated hazard h_k;
                     he then keeps only the saves of the share of the game he played (binomial thinning at that time)
                     and only the goals against before it.

The Kalshi saves contracts settle on the NAMED goalie's recorded saves once he enters the game ("active but never
enters" settles to the last fair price), so the probability is conditional on him starting; the starter confidence is
reported next to it, not multiplied in.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from nhl_edge.players.engine import PlayerSimResult
from nhl_edge.players.params import SavesModel
from nhl_edge.sim.engine_v2 import SimV2Result


@dataclass
class SavesDraws:
    saves: np.ndarray  # (n_sims,) int
    goals_against: np.ndarray
    shots_faced: np.ndarray
    replaced: np.ndarray  # bool
    expected_faced: float
    mu_full: float
    # full-game shots on goal against this NET (every goalie who played it; before the starter-replacement thinning),
    # i.e. the opponent's shots on goal excluding empty-net goals. Used by the game-script layer; draws nothing extra.
    net_shots_faced: np.ndarray | None = None

    def ladder(self, lo: int = 10, hi: int = 45) -> dict[str, float]:
        return {f"{k}+": float(np.mean(self.saves >= k)) for k in range(lo, hi + 1)}


def simulate_saves(res: SimV2Result, ps: PlayerSimResult, home_goalie: bool, model: SavesModel, expected_faced: float, seed: int) -> SavesDraws:
    rng = np.random.default_rng(seed)
    n = res.n_sims
    ga_full = (ps.ga_home if home_goalie else ps.ga_away).astype(np.int64)
    times = ps.ga_times_home if home_goalie else ps.ga_times_away
    margin = (res.home_reg - res.away_reg) if home_goalie else (res.away_reg - res.home_reg)
    ot = res.overtime.astype(float)
    base = expected_faced * model.lg_sv
    mu = model.mean(base, margin, ga_full, ot)
    if model.alpha > 0:
        lam = rng.gamma(1.0 / model.alpha, mu * model.alpha)
    else:
        lam = mu
    saves = rng.poisson(lam)
    net_faced = saves + ga_full
    # replacement after the k-th goal against before 50:00
    kmax = max(model.pull_h) if model.pull_h else 0
    T = np.full((n, kmax), np.inf)
    for i in np.nonzero(ga_full)[0]:
        t = times[i][:kmax]
        T[i, : len(t)] = t
    replaced = np.zeros(n, dtype=bool)
    t_out = np.full(n, np.inf)
    k_out = np.zeros(n, dtype=np.int64)
    for k in range(1, kmax + 1):
        cand = ~replaced & (T[:, k - 1] < 50.0) & (rng.random(n) < model.pull_h.get(k, 0.0))
        replaced |= cand
        t_out[cand] = T[cand, k - 1]
        k_out[cand] = k
    length = 60.0 + 5.0 * ot
    frac = np.where(replaced, np.clip(t_out / length, 0.0, 1.0), 1.0)
    saves = np.where(replaced, rng.binomial(saves, frac), saves)
    ga = np.where(replaced, k_out, ga_full)
    return SavesDraws(saves.astype(np.int64), ga, saves + ga, replaced, float(expected_faced), float(np.mean(mu)), net_faced.astype(np.int64))
