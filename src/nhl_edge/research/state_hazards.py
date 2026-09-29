"""Estimate nhl-sim-2.0's score-state x game-time scoring multipliers from play-by-play goal times (RESEARCH_ONLY).

Data: MoneyPuck shot rows (``nhl_edge.data.shots``), regular season, regulation (periods 1-3). For every team-game the
regulation timeline is cut at each goal; between goals the score is constant, so each team accumulates EXPOSURE
(minutes) in cells ``(time bucket, own score differential)`` and GOALS in the cell it was in when it scored.

Model: goals of team-game ``i`` in cell ``c`` ~ Poisson(lam_i * m_c * exposure_ic / 60), with ``lam_i`` an exogenous
team-strength control (league rate x team's season GF rate x opponent's season GA rate x venue; see
``team_game_rates``). Closed-form MLE per cell, shrunk toward 1.0 with ``SHRINK_GOALS`` pseudo-goals (the late,
lopsided cells are small). Residual strength not captured by ``lam_i`` biases the table toward "leaders score more",
i.e. AGAINST the score effects we find, so the estimated effects are if anything conservative.

Also reported (diagnostics, the handoff's empty-net section): goals by period, empty-net goals by minute and
margin, goalie-pull detection (first shot while the trailing team's net is empty), OT/SO split.
Everything takes explicit seasons, so the walk-forward trains only on seasons before the one it scores.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.sim.engine_v2 import DIFFS, TIME_EDGES

SHRINK_GOALS = 25.0
N_B = len(TIME_EDGES) - 1
N_D = len(DIFFS)


@dataclass
class HazardData:
    exposure: np.ndarray  # (n_team_games, N_B, N_D) minutes
    goals: np.ndarray  # (n_team_games, N_B, N_D)
    team_games: pd.DataFrame  # game_id, home flag, season, reg goals


def _bucket(t_min: float) -> int:
    return int(min(max(np.searchsorted(TIME_EDGES, t_min, side="right") - 1, 0), N_B - 1))


def regulation_goals(shots: pd.DataFrame) -> pd.DataFrame:
    s = shots[(shots["isPlayoffGame"] == 0) & (shots["goal"] == 1) & (shots["period"].between(1, 3))]
    return s[["nhl_game_id", "season", "time", "isHomeTeam", "period", "homeEmptyNet", "awayEmptyNet", "shotOnEmptyNet",
              "homeSkatersOnIce", "awaySkatersOnIce"]].sort_values(["nhl_game_id", "time"])


def build_hazard_data(shots: pd.DataFrame, seasons: Iterable[int] | None = None) -> HazardData:
    ss = set(int(x) for x in seasons) if seasons is not None else None
    s = shots[shots["isPlayoffGame"] == 0]
    if ss is not None:
        s = s[s["season"].isin(ss)]
    games = s.groupby("nhl_game_id")["season"].first()
    goals = regulation_goals(s)
    by_game = {gid: g for gid, g in goals.groupby("nhl_game_id")}
    n = len(games) * 2
    E = np.zeros((n, N_B, N_D))
    G = np.zeros((n, N_B, N_D))
    rows = []
    cuts = np.asarray(TIME_EDGES)
    for gi, (gid, season) in enumerate(games.items()):
        g = by_game.get(gid)
        times = (g["time"].to_numpy(dtype=float) / 60.0).clip(0, 60) if g is not None else np.zeros(0)
        home = g["isHomeTeam"].to_numpy(dtype=int) if g is not None else np.zeros(0, dtype=int)
        h = a = 0
        t0 = 0.0
        ih, ia = 2 * gi, 2 * gi + 1
        for t, is_home in list(zip(times, home)) + [(60.0, -1)]:
            # exposure from t0 to t in the current score state, split at bucket edges
            lo = t0
            while lo < t - 1e-12:
                b = _bucket(lo + 1e-9)
                hi = min(t, cuts[b + 1])
                dh = int(np.clip(h - a, DIFFS[0], DIFFS[-1])) - DIFFS[0]
                E[ih, b, dh] += hi - lo
                E[ia, b, N_D - 1 - dh] += hi - lo
                lo = hi
            if is_home == -1:
                break
            b = _bucket(t)
            dh = int(np.clip(h - a, DIFFS[0], DIFFS[-1])) - DIFFS[0]
            if is_home == 1:
                G[ih, b, dh] += 1
                h += 1
            else:
                G[ia, b, N_D - 1 - dh] += 1
                a += 1
            t0 = t
        rows.append({"game_id": int(gid), "season": int(season), "home": 1, "reg_goals": h})
        rows.append({"game_id": int(gid), "season": int(season), "home": 0, "reg_goals": a})
    return HazardData(E, G, pd.DataFrame(rows))


def team_game_rates(shots: pd.DataFrame, seasons: Iterable[int] | None = None) -> pd.DataFrame:
    """Exogenous expected regulation goals per team-game: league rate x own season GF rate x opponent season GA rate x
    venue factor (all from regulation goals of the SAME training seasons; this is a control for team strength when
    estimating state effects, never a forecast)."""
    s = shots[shots["isPlayoffGame"] == 0]
    if seasons is not None:
        s = s[s["season"].isin([int(x) for x in seasons])]
    games = s.groupby("nhl_game_id").agg(season=("season", "first"), home=("homeTeamCode", "first"), away=("awayTeamCode", "first")).reset_index()
    g = regulation_goals(s)
    hg = g[g["isHomeTeam"] == 1].groupby("nhl_game_id").size()
    ag = g[g["isHomeTeam"] == 0].groupby("nhl_game_id").size()
    games["hg"] = games["nhl_game_id"].map(hg).fillna(0)
    games["ag"] = games["nhl_game_id"].map(ag).fillna(0)
    rows = []
    for _season, d in games.groupby("season"):
        L = (d["hg"].sum() + d["ag"].sum()) / (2 * len(d))
        home_f = np.sqrt(d["hg"].mean() / max(d["ag"].mean(), 1e-9))
        gf = pd.concat([d.groupby("home")["hg"].sum(), d.groupby("away")["ag"].sum()], axis=1).fillna(0).sum(axis=1)
        ga = pd.concat([d.groupby("home")["ag"].sum(), d.groupby("away")["hg"].sum()], axis=1).fillna(0).sum(axis=1)
        gp = pd.concat([d.groupby("home").size(), d.groupby("away").size()], axis=1).fillna(0).sum(axis=1)
        gfr, gar = gf / gp / L, ga / gp / L
        for r in d.itertuples(index=False):
            rows.append({"game_id": int(r.nhl_game_id), "home": 1, "lam": L * gfr[r.home] * gar[r.away] * home_f})
            rows.append({"game_id": int(r.nhl_game_id), "home": 0, "lam": L * gfr[r.away] * gar[r.home] / home_f})
    return pd.DataFrame(rows)


def fit_multipliers(hd: HazardData, lam: pd.DataFrame, shrink: float = SHRINK_GOALS) -> tuple[np.ndarray, dict[str, Any]]:
    """Closed-form Poisson MLE of the (bucket, diff) table with an EXOGENOUS team-game rate as offset:
    ``m_c = (goals_c + k) / (sum_i lam_i * exposure_ic / 60 + k)``.

    (A team-game fixed effect is NOT used: conditioning on a team's own goal total makes its goals mechanically
    precede its time spent leading and manufactures a huge spurious "trailing teams score more" effect. We tried it
    first; see docs/research/V2_RESEARCH.md.)"""
    key = hd.team_games[["game_id", "home"]].merge(lam, on=["game_id", "home"], how="left")
    lam_i = key["lam"].fillna(key["lam"].mean()).to_numpy()
    E = hd.exposure.reshape(len(hd.exposure), -1)
    G = hd.goals.reshape(len(hd.goals), -1)
    obs = G.sum(axis=0)
    expd = (lam_i[:, None] * E / 60.0).sum(axis=0)
    m = (obs + shrink) / (expd + shrink)
    Eall = E.sum(axis=0)
    norm = (Eall * m).sum() / Eall.sum()
    info = {"n_team_games": int(len(E)), "goals": int(obs.sum()), "expected_goals": round(float(expd.sum()), 1),
            "exposure_min_by_cell": Eall.reshape(N_B, N_D).round(1).tolist(), "goals_by_cell": obs.reshape(N_B, N_D).astype(int).tolist(),
            "expected_by_cell": expd.reshape(N_B, N_D).round(1).tolist(), "shrink_pseudo_goals": shrink, "raw_exposure_weighted_mean": round(float(norm), 4)}
    return m.reshape(N_B, N_D), info


def diagnostics(shots: pd.DataFrame, nhl_games: pd.DataFrame, seasons: Iterable[int]) -> dict[str, Any]:
    ss = [int(x) for x in seasons]
    s = shots[(shots["isPlayoffGame"] == 0) & shots["season"].isin(ss)]
    g = regulation_goals(s)
    out: dict[str, Any] = {"seasons": ss, "n_games": int(s["nhl_game_id"].nunique()), "reg_goals": int(len(g))}
    per = g.groupby("period").size()
    out["goals_by_period"] = {int(k): int(v) for k, v in per.items()}
    out["goals_per_game_by_period"] = {int(k): round(float(v) / out["n_games"], 4) for k, v in per.items()}
    en = g[g["shotOnEmptyNet"] == 1]
    out["empty_net_goals"] = int(len(en))
    out["empty_net_goals_per_game"] = round(len(en) / max(out["n_games"], 1), 4)
    en_min = (60 - en["time"] / 60).clip(lower=0)
    out["empty_net_goals_by_minutes_remaining"] = {f"{lo}-{lo + 1}": int(((en_min >= lo) & (en_min < lo + 1)).sum()) for lo in range(0, 5)} | {
        "5+": int((en_min >= 5).sum())}
    # margin before the empty-net goal, from the scorer's perspective
    # pulled-goalie goals by the trailing (6-skater) team
    six_h = (g["isHomeTeam"] == 1) & (g["homeEmptyNet"] == 1)
    six_a = (g["isHomeTeam"] == 0) & (g["awayEmptyNet"] == 1)
    out["extra_attacker_goals"] = int((six_h | six_a).sum())
    # pull detection: first regulation shot in P3 at which a team's own net is empty (either team shooting)
    p3 = s[(s["period"] == 3)]
    pulls = []
    for side, flag in (("home", "homeEmptyNet"), ("away", "awayEmptyNet")):
        x = p3[p3[flag] == 1].groupby("nhl_game_id")["time"].min()
        pulls.append(pd.DataFrame({"game_id": x.index, "side": side, "t": x.to_numpy() / 60.0}))
    pl = pd.concat(pulls) if pulls else pd.DataFrame(columns=["game_id", "side", "t"])
    out["games_with_detected_pull"] = int(pl["game_id"].nunique())
    out["pull_minutes_remaining_quantiles"] = {str(q): round(float(60 - pl["t"].quantile(q)), 2) for q in (0.1, 0.25, 0.5, 0.75, 0.9)} if len(pl) else {}
    out["pull_note"] = "detected from the first shot (either team) with that team's net empty; a pull with no shot before a goal/whistle is missed"
    ng = nhl_games[(nhl_games["season"].isin(ss)) & (nhl_games["game_type"] == 2) & nhl_games["final"].astype(bool)]
    lp = ng["last_period_type"].value_counts()
    out["ot_so"] = {k: int(v) for k, v in lp.items()}
    n_ex = int(lp.get("OT", 0) + lp.get("SO", 0))
    out["p_regulation_tie"] = round(n_ex / max(len(ng), 1), 4)
    out["p_ot_goal_given_ot"] = round(int(lp.get("OT", 0)) / max(n_ex, 1), 4)
    return out
