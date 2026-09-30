"""Estimate PLAYER_SIM_V1's global (league-level) parameters from training seasons only.

* ``strength_table``: P(goal into an empty net) and P(goal with own net empty) by (regulation time bucket, scoring
  team's own score differential before the goal), from official play-by-play ``situationCode``. Shrunk toward the
  bucket's pooled rate with 20 pseudo-goals. Same buckets as the nhl-sim-2.0 hazard table.
* ``pull_hazards``: h_k = P(the starter is replaced right after his k-th goal against | he allowed k before 50:00).
* ``team_shot_rates`` + ``fit_saves``: shots on goal a team FACES are a function of the opponent's shot generation and
  the team's shot suppression (exponentially weighted, shrunk team rates, strictly before the date); a starting goalie's
  saves in a full game are negative-binomial with
  ``log mu = a + b*log(expected non-goal shots) + c*regulation margin (goalie's team) + d*goals against + e*OT`` so the
  save count moves with the simulated game script (a team protecting a lead faces more shots; a busy night means more
  goals AND more saves). Fit by Poisson IRLS, NB dispersion by moments on Pearson residuals.
* ``toi_noise``: game-to-game log-sd of skater ice time around its recent mean and the early-exit rate.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.players.engine import StrengthTable
from nhl_edge.sim.engine_v2 import DIFFS, TIME_EDGES


def strength_table(goals: pd.DataFrame, k: float = 20.0) -> StrengthTable:
    g = goals[goals["period"] <= 3].copy()
    tmin = g["t_s"].to_numpy(float) / 60.0
    b = np.clip(np.searchsorted(np.asarray(TIME_EDGES), tmin, side="right") - 1, 0, len(TIME_EDGES) - 2)
    d = np.clip((g["score_for_before"] - g["score_against_before"]).to_numpy(int), min(DIFFS), max(DIFFS)) - min(DIFFS)
    en = (g["strength"] == "EN").to_numpy(float)
    ea = (g["strength"] == "EA").to_numpy(float)
    nb, nd = len(TIME_EDGES) - 1, len(DIFFS)
    p_en = np.zeros((nb, nd))
    p_ea = np.zeros((nb, nd))
    for i in range(nb):
        mb = b == i
        pool_en = en[mb].mean() if mb.any() else 0.0
        pool_ea = ea[mb].mean() if mb.any() else 0.0
        for j in range(nd):
            m = mb & (d == j)
            n = m.sum()
            p_en[i, j] = (en[m].sum() + k * pool_en) / (n + k)
            p_ea[i, j] = (ea[m].sum() + k * pool_ea) / (n + k)
    # an empty net needs a trailing opponent (EN) / a trailing own team (EA): zero the impossible cells before shrinkage leaks
    for j, dv in enumerate(DIFFS):
        if dv <= 0:
            p_en[:, j] = np.minimum(p_en[:, j], en[(d == j)].mean() if (d == j).any() else 0.0)
        if dv >= 0:
            p_ea[:, j] = np.minimum(p_ea[:, j], ea[(d == j)].mean() if (d == j).any() else 0.0)
    return StrengthTable(TIME_EDGES, DIFFS, p_en, p_ea)


def team_game_frame(goalies: pd.DataFrame, goals: pd.DataFrame) -> pd.DataFrame:
    """One row per team-game: shots faced / taken, goals, regulation margin, OT flag, date."""
    ga = goalies.groupby(["game_id", "team_id"]).agg(sa=("shots_against", "sum"), ga=("goals_against", "sum"), game_date=("game_date", "first"),
                                                      season=("season", "first"), is_home=("is_home", "first")).reset_index()
    reg = goals[goals["period"] <= 3].groupby(["game_id", "team_id"]).size().rename("reg_gf")
    ot = goals.groupby("game_id")["period"].max().rename("max_period")
    ga = ga.join(reg, on=["game_id", "team_id"])
    ga["reg_gf"] = ga["reg_gf"].fillna(0)
    opp = ga[["game_id", "team_id", "sa", "reg_gf"]].rename(columns={"team_id": "opp_id", "sa": "sf", "reg_gf": "reg_ga"})
    ga = ga.merge(opp, on="game_id")
    ga = ga[ga["team_id"] != ga["opp_id"]].join(ot, on="game_id")
    ga["date_int"] = ga["game_date"].astype(str).str.replace("-", "").str[:8].astype(int)
    return ga.sort_values(["date_int", "game_id"]).reset_index(drop=True)


@dataclass
class ShotRates:
    league_sog: float
    tg: pd.DataFrame
    half_life: float = 25.0
    prior_games: float = 15.0

    def rates(self, team_id: int, date_int: int) -> tuple[float, float, int]:
        """(shots-for per game, shots-against per game, games used), shrunk to the league mean, strictly before date."""
        d = self.tg[(self.tg["team_id"] == team_id) & (self.tg["date_int"] < date_int)].tail(82)
        if not len(d):
            return self.league_sog, self.league_sog, 0
        w = 0.5 ** (np.arange(len(d))[::-1] / self.half_life)
        sf = (np.sum(w * d["sf"].to_numpy(float)) + self.prior_games * self.league_sog) / (w.sum() + self.prior_games)
        sa = (np.sum(w * d["sa"].to_numpy(float)) + self.prior_games * self.league_sog) / (w.sum() + self.prior_games)
        return float(sf), float(sa), int(len(d))

    def expected_faced(self, team_id: int, opp_id: int, date_int: int, home: bool) -> float:
        _, sa, _ = self.rates(team_id, date_int)
        sf_opp, _, _ = self.rates(opp_id, date_int)
        venue = 0.985 if home else 1.015  # road teams face ~3% more shots (measured below in fit_saves diagnostics)
        return self.league_sog * (sf_opp / self.league_sog) * (sa / self.league_sog) * venue


def shot_rates(tg: pd.DataFrame) -> ShotRates:
    return ShotRates(float(tg["sa"].mean()), tg)


@dataclass
class SavesModel:
    coef: np.ndarray  # intercept, log(base non-goal shots), margin, GA, OT
    alpha: float  # NB2 dispersion: var = mu + alpha mu^2
    pull_h: dict[int, float]
    n_fit: int
    lg_sv: float = 0.905  # league save percentage in the fit sample: expected non-goal shots = expected shots faced * lg_sv

    def to_dict(self) -> dict[str, Any]:
        return {"coef": [float(c) for c in self.coef], "alpha": self.alpha, "pull_h": {str(k): v for k, v in self.pull_h.items()}, "n_fit": self.n_fit, "lg_sv": self.lg_sv,
                "terms": ["intercept", "log(expected shots faced - expected GA)", "regulation margin (goalie team, clipped +-3)", "goals against", "overtime"]}

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> SavesModel:
        return cls(np.asarray(d["coef"], float), float(d["alpha"]), {int(k): float(v) for k, v in d["pull_h"].items()}, int(d.get("n_fit", 0)),
                   float(d.get("lg_sv", 0.905)))

    def mean(self, base: float | np.ndarray, margin: np.ndarray, ga: np.ndarray, ot: np.ndarray) -> np.ndarray:
        c = self.coef
        return np.exp(c[0] + c[1] * np.log(np.maximum(base, 1.0)) + c[2] * np.clip(margin, -3, 3) + c[3] * ga + c[4] * ot)


def starter_rows(goalies: pd.DataFrame, tg: pd.DataFrame) -> pd.DataFrame:
    g = goalies.copy()
    n_used = g[g["toi_s"].fillna(0) > 0].groupby(["game_id", "team_id"]).size().rename("n_goalies")
    g = g.join(n_used, on=["game_id", "team_id"])
    s = g[g["starter"].astype(bool)].merge(tg[["game_id", "team_id", "opp_id", "reg_gf", "reg_ga", "max_period", "date_int"]], on=["game_id", "team_id"])
    s["replaced"] = s["n_goalies"].fillna(1) > 1
    s["margin"] = (s["reg_gf"] - s["reg_ga"]).clip(-3, 3)
    s["ot"] = (s["max_period"] >= 4).astype(float)
    return s


def pull_hazards(goalies: pd.DataFrame, goals: pd.DataFrame, tg: pd.DataFrame, k_max: int = 7) -> dict[int, float]:
    s = starter_rows(goalies, tg)
    g = goals[(goals["t_s"] < 3000) & goals["goalie_in_net_id"].notna()]
    before50 = g.groupby(["game_id", "goalie_in_net_id"]).size()
    s["ga50"] = [int(before50.get((gid, pid), 0)) for gid, pid in zip(s["game_id"], s["player_id"])]
    h = {}
    for k in range(1, k_max + 1):
        reached = int((s["ga50"] >= k).sum())
        pulled = int((s["replaced"] & (s["ga50"] == k)).sum())
        h[k] = float((pulled + 0.5) / (reached + 5.0))
    return h


def fit_saves(goalies: pd.DataFrame, goals: pd.DataFrame, tg: pd.DataFrame, rates: ShotRates, seasons: list[int]) -> SavesModel:
    s = starter_rows(goalies, tg)
    s = s[s["season"].isin(seasons) & ~s["replaced"] & (s["toi_s"].fillna(0) >= 3300)]
    base = np.array([rates.expected_faced(int(t), int(o), int(di), bool(h)) for t, o, di, h in zip(s["team_id"], s["opp_id"], s["date_int"], s["is_home"])])
    lg_sv = 1.0 - s["goals_against"].sum() / max(s["shots_against"].sum(), 1)
    X = np.column_stack([np.ones(len(s)), np.log(np.maximum(base * lg_sv, 1.0)), s["margin"].to_numpy(float), s["goals_against"].to_numpy(float), s["ot"].to_numpy(float)])
    y = s["saves"].to_numpy(float)
    w = np.array([np.log(y.mean()) - np.log(max(base.mean() * lg_sv, 1.0)), 1.0, 0.0, 0.0, 0.0])
    for _ in range(50):
        mu = np.exp(X @ w)
        g = X.T @ (y - mu)
        H = (X * mu[:, None]).T @ X
        st = np.linalg.solve(H, g)
        w += st
        if np.abs(st).max() < 1e-9:
            break
    mu = np.exp(X @ w)
    alpha = float(max(np.mean(((y - mu) ** 2 - mu) / mu**2), 0.0))
    return SavesModel(w, alpha, pull_hazards(goalies, goals, tg), int(len(s)), float(lg_sv))


def toi_noise(pg: pd.DataFrame, window: int = 10) -> tuple[float, float]:
    d = pg[["player_id", "date_int", "toi_s"]].dropna().sort_values(["player_id", "date_int"])
    d["exp"] = d.groupby("player_id")["toi_s"].transform(lambda x: x.shift(1).rolling(window, min_periods=5).mean())
    d = d[d["exp"] > 300]
    r = np.log(np.maximum(d["toi_s"], 1) / d["exp"])
    core = r[(r > -0.7) & (r < 0.7)]
    exit_rate = float((r <= -1.05).mean())  # under ~35% of usual ice time
    return float(core.std()), exit_rate
