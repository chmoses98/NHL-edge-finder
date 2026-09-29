"""Explicit special-teams decomposition for nhl-features-2.0 (RESEARCH_ONLY; V1's all-situation rates are untouched).

V1 builds a team's expected goals from ALL-situation xG per 60. That folds three different skills into one number:
even-strength play, power-play attack / penalty-kill defence, and how often a team draws or takes penalties. V2
splits them, from MoneyPuck team-game rows by situation (``5on5``, ``5on4`` = own power play, ``4on5`` = own
penalty kill, and ``other`` = all minus those three: 5v3, 4v4, 3v3 OT, goalie-pulled / empty-net play):

    lam_A = [ EV_A + PP_A + SH_A ] * finish_A * goalie_B  +  OTHER_A        (then home / rest adjustments as V1)

    EV_A    = cEV * L_ev60 * (ev_off_A / L_ev60) * (ev_def_B / L_ev60) * ev_min / 60
    PP_A    = cPP * L_pp60 * (pp_off_A / L_pp60) * (pk_def_B / L_pp60) * pp_min_A / 60
    SH_A    = L_sh60 * pp_min_B / 60                           (short-handed goals: league rate, too rare to rate)
    OTHER_A = L_other_goals * (off_all_A / L) * (def_all_B / L)  (V1 all-situation ratings; incl. empty-net goals)
    pp_min_A = L_ppmin * (draw_A / L_ppmin) * (take_B / L_ppmin)   power-play minutes A gets vs this opponent
    ev_min  = L_ev_min - (pp_min_A + pp_min_B - 2 * L_ppmin)       (penalty time comes out of even strength)

``c*`` are league goals-per-xG conversions for the situation; every ``*_off / *_def / draw / take`` is an
exponentially weighted per-team rate shrunk toward the league mean with a prior measured in the situation's own
exposure (power-play rates are shrunk hardest: a team gets ~4 PP minutes a game). Minutes partition the game, so
with league-average teams ``lam`` equals the league all-situation goal rate: nothing is counted twice (tested).

Point-in-time exactly as V1: only rows dated strictly before ``as_of``.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.features.ratings import HALF_LIFE_GAMES, PREV_SEASON_DISCOUNT, _date_int

ST_FEATURE_VERSION = "nhl-features-2.0"
PRIOR_EV_GAMES = 20.0
PRIOR_PP_MINUTES = 180.0  # ~40 games of one team's power-play time: PP/PK rates are noisy
PRIOR_PEN_GAMES = 25.0  # penalty drawing / taking rates
SITS = ("5on5", "5on4", "4on5", "all")


def prepare_situation_log(team_games: pd.DataFrame) -> pd.DataFrame:
    """Wide per team-game frame: ev_*, pp_* (own 5on4), pk_* (own 4on5), all_* and other_* (= all minus the three)."""
    d = team_games[team_games["situation"].isin(SITS)].copy()
    if "team_abbrev" in d.columns:
        d["team"] = d["team_abbrev"].where(d["team_abbrev"].notna(), d.get("mp_team", d.get("team")))
    d["date_int"] = d["gameDate"].map(_date_int)
    gid = "gameId" if "gameId" in d.columns else "game_id"
    for c in ("xGoalsFor", "xGoalsAgainst", "goalsFor", "goalsAgainst", "iceTime"):
        d[c] = pd.to_numeric(d[c], errors="coerce").fillna(0.0)
    keys = ["team", gid, "date_int", "season"] + (["game_type"] if "game_type" in d.columns else [])
    w = d.pivot_table(index=keys, columns="situation", values=["xGoalsFor", "xGoalsAgainst", "goalsFor", "goalsAgainst", "iceTime"], aggfunc="sum")
    w.columns = [f"{m}_{s}" for m, s in w.columns]
    w = w.reset_index().rename(columns={gid: "game_id"})
    for c in [f"{m}_{s}" for m in ("xGoalsFor", "xGoalsAgainst", "goalsFor", "goalsAgainst", "iceTime") for s in SITS]:
        if c not in w.columns:
            w[c] = 0.0
    out = pd.DataFrame({
        "team": w["team"], "game_id": w["game_id"], "date_int": w["date_int"], "season": pd.to_numeric(w["season"], errors="coerce"),
        "ev_min": w["iceTime_5on5"] / 60, "ev_xgf": w["xGoalsFor_5on5"], "ev_xga": w["xGoalsAgainst_5on5"], "ev_gf": w["goalsFor_5on5"], "ev_ga": w["goalsAgainst_5on5"],
        "pp_min": w["iceTime_5on4"] / 60, "pp_xgf": w["xGoalsFor_5on4"], "pp_gf": w["goalsFor_5on4"], "pp_ga": w["goalsAgainst_5on4"],
        "pk_min": w["iceTime_4on5"] / 60, "pk_xga": w["xGoalsAgainst_4on5"], "pk_ga": w["goalsAgainst_4on5"], "pk_gf": w["goalsFor_4on5"],
        "all_min": w["iceTime_all"] / 60, "all_gf": w["goalsFor_all"], "all_ga": w["goalsAgainst_all"],
    })
    out["other_gf"] = (out["all_gf"] - out["ev_gf"] - out["pp_gf"] - out["pk_gf"]).clip(lower=0)
    out["other_min"] = (out["all_min"] - out["ev_min"] - out["pp_min"] - out["pk_min"]).clip(lower=0)
    if "game_type" in w.columns:
        out["game_type"] = w["game_type"]
    out = out[out["all_min"] > 0]
    return out.sort_values(["date_int", "game_id", "team"]).reset_index(drop=True)


@dataclass(frozen=True)
class LeagueST:
    ev_xg60: float
    ev_conv: float  # goals per xG at 5on5
    pp_xg60: float
    pp_conv: float
    sh_g60: float  # short-handed goals per 60 of own PK time
    ppmin: float  # power-play minutes per team-game
    ev_min: float
    other_goals: float  # goals per team-game in 'other' situations
    g60_all: float
    n_team_games: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


DEFAULT_LEAGUE_ST = LeagueST(ev_xg60=2.48, ev_conv=0.965, pp_xg60=7.3, pp_conv=1.0, sh_g60=0.8, ppmin=4.25, ev_min=49.9, other_goals=0.30, g60_all=3.05, n_team_games=0)


def league_st(st: pd.DataFrame, as_of: str, season: int | None = None) -> LeagueST:
    cut = _date_int(as_of)
    d = st[st["date_int"] < cut]
    if season is not None:
        cur = d[d["season"] == season]
        d = cur if len(cur) >= 120 else d[d["season"] >= season - 1]
    if len(d) < 60:
        return DEFAULT_LEAGUE_ST
    s = d[["ev_min", "ev_xgf", "ev_gf", "pp_min", "pp_xgf", "pp_gf", "pk_min", "pk_gf", "all_min", "all_gf", "other_gf"]].sum()
    n = len(d)
    return LeagueST(ev_xg60=float(s.ev_xgf / s.ev_min * 60), ev_conv=float(s.ev_gf / max(s.ev_xgf, 1e-9)), pp_xg60=float(s.pp_xgf / s.pp_min * 60),
                    pp_conv=float(s.pp_gf / max(s.pp_xgf, 1e-9)), sh_g60=float(s.pk_gf / max(s.pk_min, 1e-9) * 60), ppmin=float(s.pp_min / n),
                    ev_min=float(s.ev_min / n), other_goals=float(s.other_gf / n), g60_all=float(s.all_gf / s.all_min * 60), n_team_games=int(n))


@dataclass(frozen=True)
class TeamST:
    team: str
    ev_off: float
    ev_def: float
    pp_off: float
    pk_def: float
    draw: float  # own PP minutes per game
    take: float  # own PK minutes per game
    games_used: float
    raw: dict[str, float]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _w(d: pd.DataFrame, current_season: int | None) -> np.ndarray:
    n = len(d)
    w = 0.5 ** (np.arange(n)[::-1] / HALF_LIFE_GAMES)
    if current_season is not None:
        w = w * np.where(d["season"].to_numpy() == current_season, 1.0, PREV_SEASON_DISCOUNT)
    return w


def team_st(st: pd.DataFrame, team: str, as_of: str, lg: LeagueST, current_season: int | None = None) -> TeamST:
    cut = _date_int(as_of)
    d = st[(st["team"] == team) & (st["date_int"] < cut)]
    if current_season is not None:
        d = d[d["season"] >= current_season - 1]
    d = d.tail(120)
    if d.empty:
        return TeamST(team, lg.ev_xg60, lg.ev_xg60, lg.pp_xg60, lg.pp_xg60, lg.ppmin, lg.ppmin, 0.0, {})
    w = _w(d, current_season)
    n_eff = float(w.sum())

    def ws(c: str) -> float:
        return float((d[c].to_numpy() * w).sum())

    ev_min, pp_min, pk_min = ws("ev_min"), ws("pp_min"), ws("pk_min")
    raw = {"ev_off": ws("ev_xgf") / max(ev_min, 1e-9) * 60, "ev_def": ws("ev_xga") / max(ev_min, 1e-9) * 60,
           "pp_off": ws("pp_xgf") / max(pp_min, 1e-9) * 60 if pp_min > 0 else lg.pp_xg60,
           "pk_def": ws("pk_xga") / max(pk_min, 1e-9) * 60 if pk_min > 0 else lg.pp_xg60,
           "draw": pp_min / n_eff, "take": pk_min / n_eff}
    k_ev = n_eff / (n_eff + PRIOR_EV_GAMES)
    k_pp = pp_min / (pp_min + PRIOR_PP_MINUTES)
    k_pk = pk_min / (pk_min + PRIOR_PP_MINUTES)
    k_pen = n_eff / (n_eff + PRIOR_PEN_GAMES)
    return TeamST(team=team,
                  ev_off=lg.ev_xg60 + k_ev * (raw["ev_off"] - lg.ev_xg60), ev_def=lg.ev_xg60 + k_ev * (raw["ev_def"] - lg.ev_xg60),
                  pp_off=lg.pp_xg60 + k_pp * (raw["pp_off"] - lg.pp_xg60), pk_def=lg.pp_xg60 + k_pk * (raw["pk_def"] - lg.pp_xg60),
                  draw=lg.ppmin + k_pen * (raw["draw"] - lg.ppmin), take=lg.ppmin + k_pen * (raw["take"] - lg.ppmin),
                  games_used=n_eff, raw=raw)


def st_components(home: TeamST, away: TeamST, lg: LeagueST, home_all_ratio: float, away_all_ratio: float) -> dict[str, float]:
    """Expected goals per side by situation BEFORE finishing / goalie / home / rest multipliers.

    ``*_all_ratio`` = (off_all_X / L) * (def_all_Y / L) from the V1 all-situation ratings, used only for the small
    'other' bucket (4v4, 3v3, 5v3, empty net)."""
    ppmin_h = lg.ppmin * (home.draw / lg.ppmin) * (away.take / lg.ppmin)
    ppmin_a = lg.ppmin * (away.draw / lg.ppmin) * (home.take / lg.ppmin)
    ev_min = max(lg.ev_min - (ppmin_h + ppmin_a - 2 * lg.ppmin), 30.0)
    L, P = lg.ev_xg60, lg.pp_xg60
    ev_h = lg.ev_conv * L * (home.ev_off / L) * (away.ev_def / L) * ev_min / 60
    ev_a = lg.ev_conv * L * (away.ev_off / L) * (home.ev_def / L) * ev_min / 60
    pp_h = lg.pp_conv * P * (home.pp_off / P) * (away.pk_def / P) * ppmin_h / 60
    pp_a = lg.pp_conv * P * (away.pp_off / P) * (home.pk_def / P) * ppmin_a / 60
    sh_h = lg.sh_g60 * ppmin_a / 60
    sh_a = lg.sh_g60 * ppmin_h / 60
    oth_h = lg.other_goals * home_all_ratio
    oth_a = lg.other_goals * away_all_ratio
    return {"ev_home": ev_h, "ev_away": ev_a, "pp_home": pp_h, "pp_away": pp_a, "sh_home": sh_h, "sh_away": sh_a, "other_home": oth_h, "other_away": oth_a,
            "ppmin_home": ppmin_h, "ppmin_away": ppmin_a, "ev_min": ev_min}


def expected_goals_v2(home_r: Any, away_r: Any, home_st: TeamST, away_st: TeamST, league: Any, lst: LeagueST, home_goalie_factor: float = 1.0,
                      away_goalie_factor: float = 1.0, home_b2b: bool = False, away_b2b: bool = False, neutral_site: bool = False,
                      use_special_teams: bool = True) -> tuple[float, float, dict[str, Any]]:
    """(lam_home, lam_away, components) for nhl-features-2.0.

    ``home_r``/``away_r`` are V1 :class:`TeamRating` objects (all-situation ratings; used for finishing and the small
    'other' bucket) and ``league`` the V1 :class:`LeagueRates`. The situation sum is normalised so that a league-average
    matchup reproduces ``league.g60`` exactly: V2 changes how teams differ, not the league scoring level (MoneyPuck's
    'all' rows include OT time, which would otherwise leak ~0.1 goals/game into regulation). With
    ``use_special_teams=False`` this reduces to V1's all-situation formula (goalie factor applied the same way)."""
    from nhl_edge.features.ratings import B2B_DEF_ADJ, B2B_OFF_ADJ, HOME_ADJ, MAX_LAMBDA_RATIO

    L = max(league.xg60, 1e-6)
    home_adj = 1.0 if neutral_site else HOME_ADJ
    h_ratio = (home_r.off_xg60 / L) * (away_r.def_xg60 / L)
    a_ratio = (away_r.off_xg60 / L) * (home_r.def_xg60 / L)
    if use_special_teams:
        c = st_components(home_st, away_st, lst, h_ratio, a_ratio)
        avg = TeamST("LG", lst.ev_xg60, lst.ev_xg60, lst.pp_xg60, lst.pp_xg60, lst.ppmin, lst.ppmin, 0.0, {})
        c0 = st_components(avg, avg, lst, 1.0, 1.0)
        base = c0["ev_home"] + c0["pp_home"] + c0["sh_home"] + c0["other_home"]
        norm = league.g60 / max(base, 1e-9)
        skater_h = (c["ev_home"] + c["pp_home"] + c["sh_home"]) * norm
        skater_a = (c["ev_away"] + c["pp_away"] + c["sh_away"]) * norm
        lam_h = skater_h * home_r.finish * away_goalie_factor + c["other_home"] * norm
        lam_a = skater_a * away_r.finish * home_goalie_factor + c["other_away"] * norm
        comp: dict[str, Any] = {k: float(v) for k, v in c.items()} | {"st_norm": norm}
    else:
        lam_h = league.g60 * h_ratio * home_r.finish * away_goalie_factor
        lam_a = league.g60 * a_ratio * away_r.finish * home_goalie_factor
        comp = {}
    lam_h *= home_adj
    lam_a /= home_adj
    if home_b2b:
        lam_h *= B2B_OFF_ADJ
        lam_a *= B2B_DEF_ADJ
    if away_b2b:
        lam_a *= B2B_OFF_ADJ
        lam_h *= B2B_DEF_ADJ
    ratio = lam_h / lam_a
    if ratio > MAX_LAMBDA_RATIO:
        lam_h = lam_a * MAX_LAMBDA_RATIO
    elif ratio < 1 / MAX_LAMBDA_RATIO:
        lam_a = lam_h * MAX_LAMBDA_RATIO
    comp.update({"feature_version": ST_FEATURE_VERSION, "special_teams": use_special_teams, "home_goalie_factor": home_goalie_factor,
                 "away_goalie_factor": away_goalie_factor, "home_adj": home_adj, "home_b2b": home_b2b, "away_b2b": away_b2b,
                 "home_st": home_st.to_dict(), "away_st": away_st.to_dict()})
    return float(lam_h), float(lam_a), comp
