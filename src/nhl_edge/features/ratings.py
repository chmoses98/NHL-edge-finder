"""Team and goalie strength ratings for DATA_ONLY_V1 (``FEATURE_VERSION`` in ``nhl_edge``).

Point-in-time by construction: every function takes the rows it may use and an ``as_of`` date, and uses only rows
dated strictly BEFORE ``as_of``. Callers are responsible for passing rows from snapshots captured before the
prediction instant; nothing here reaches for a file.

Inputs are MoneyPuck team game-by-game rows (situation == 'all') or anything with the same columns:
    team, season, gameId, opposingTeam, home_or_away, gameDate (YYYYMMDD int/str), xGoalsFor, xGoalsAgainst,
    goalsFor, goalsAgainst, iceTime (seconds)

Rating (per team, per 60 minutes, all situations):
    off_xg   exponentially weighted xGF/60            (shot generation x shot quality)
    def_xg   exponentially weighted xGA/60            (shot suppression x quality against)
    finish   regressed GF/xGF ratio                    (finishing above/below expected)
    stop     regressed GA/xGA ratio                    (goaltending + defensive save effects; team-level)
each shrunk toward the league mean with a prior of ``PRIOR_GAMES`` games, and the previous season carried in at a
discount so the first weeks of a season are not pure noise.

Expected goals for team A vs team B (see :func:`expected_goals`)::

    lam_A = league_g60 * (off_A / L) * (def_B / L) * finish_A * stop_B * home_adj * rest_adj

with ``L`` the league xG/60. This is a multiplicative decomposition of shot environment x quality x finishing x
goaltending, which is the architecture the roadmap extends (special teams, lines, RAPM) without changing the sim.
"""

from __future__ import annotations

import math
from dataclasses import asdict, dataclass
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge import FEATURE_VERSION

LEAGUE_G60_FALLBACK = 3.05  # goals per team per 60 min, all situations, recent NHL seasons (2022-2026: 3.0-3.2)
HALF_LIFE_GAMES = 20.0
PRIOR_GAMES = 20.0  # shrinkage weight toward league mean, in games
PREV_SEASON_DISCOUNT = 0.6  # a previous-season game counts this much of a current-season game
FINISH_PRIOR_XG = 60.0  # xG of prior for finishing/stopping ratios (~20 games)
HOME_ADJ = 1.045  # multiplicative on the home team's lambda; away gets 1/HOME_ADJ (home ~53.5% ML)
B2B_OFF_ADJ = 0.965  # second night of a back-to-back: own offense
B2B_DEF_ADJ = 1.025  # ... and own goals against
MAX_LAMBDA_RATIO = 2.5  # sanity clamp on lam_A / lam_B


@dataclass(frozen=True)
class TeamRating:
    team: str
    off_xg60: float
    def_xg60: float
    finish: float
    stop: float
    games_used: float  # effective sample (weighted)
    raw_off_xg60: float | None = None
    raw_def_xg60: float | None = None
    gf60: float | None = None
    ga60: float | None = None
    feature_version: str = FEATURE_VERSION

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class LeagueRates:
    xg60: float
    g60: float
    n_games: int
    as_of: str


def _date_int(v: Any) -> int:
    s = str(v).replace("-", "")[:8]
    return int(s) if s.isdigit() else 0


def prepare_gamelog(df: pd.DataFrame) -> pd.DataFrame:
    """Normalise a MoneyPuck team game log to the columns the ratings use (situation 'all' only)."""
    d = df.copy()
    if "situation" in d.columns:
        d = d[d["situation"] == "all"]
    d = d.rename(columns={"playerTeam": "team_", "gameId": "game_id"})
    if "team" not in d.columns and "team_" in d.columns:
        d["team"] = d["team_"]
    d["date_int"] = d["gameDate"].map(_date_int)
    for c in ("xGoalsFor", "xGoalsAgainst", "goalsFor", "goalsAgainst", "iceTime"):
        d[c] = pd.to_numeric(d[c], errors="coerce")
    d = d.dropna(subset=["xGoalsFor", "xGoalsAgainst", "goalsFor", "goalsAgainst", "iceTime"])
    d = d[d["iceTime"] > 0]
    d["minutes"] = d["iceTime"] / 60.0
    d["season"] = pd.to_numeric(d["season"], errors="coerce").astype("Int64")
    return d.sort_values(["date_int", "game_id"]).reset_index(drop=True)


def league_rates(log: pd.DataFrame, as_of: str, season: int | None = None) -> LeagueRates:
    cut = _date_int(as_of)
    d = log[log["date_int"] < cut]
    if season is not None:
        d_season = d[d["season"] == season]
        if len(d_season) >= 60:
            d = d_season
        else:
            d = d[d["season"] >= season - 1]
    if d.empty:
        return LeagueRates(xg60=LEAGUE_G60_FALLBACK, g60=LEAGUE_G60_FALLBACK, n_games=0, as_of=as_of)
    minutes = d["minutes"].sum()
    return LeagueRates(xg60=float(d["xGoalsFor"].sum() / minutes * 60), g60=float(d["goalsFor"].sum() / minutes * 60), n_games=int(len(d) // 2), as_of=as_of)


def _weights(d: pd.DataFrame, current_season: int | None, half_life: float) -> np.ndarray:
    n = len(d)
    if n == 0:
        return np.zeros(0)
    age = np.arange(n)[::-1]  # 0 == most recent
    w = 0.5 ** (age / half_life)
    if current_season is not None:
        w = w * np.where(d["season"].to_numpy() == current_season, 1.0, PREV_SEASON_DISCOUNT)
    return w


def team_rating(log: pd.DataFrame, team: str, as_of: str, league: LeagueRates, current_season: int | None = None,
                half_life: float = HALF_LIFE_GAMES, prior_games: float = PRIOR_GAMES) -> TeamRating:
    cut = _date_int(as_of)
    d = log[(log["team"] == team) & (log["date_int"] < cut)]
    if current_season is not None:
        d = d[d["season"] >= current_season - 1]
    d = d.tail(120)
    w = _weights(d, current_season, half_life)
    n_eff = float(w.sum())
    L = league.xg60
    if n_eff <= 0:
        return TeamRating(team=team, off_xg60=L, def_xg60=L, finish=1.0, stop=1.0, games_used=0.0)
    minutes = float((d["minutes"].to_numpy() * w).sum())
    xgf = float((d["xGoalsFor"].to_numpy() * w).sum())
    xga = float((d["xGoalsAgainst"].to_numpy() * w).sum())
    gf = float((d["goalsFor"].to_numpy() * w).sum())
    ga = float((d["goalsAgainst"].to_numpy() * w).sum())
    raw_off = xgf / minutes * 60
    raw_def = xga / minutes * 60
    shrink = n_eff / (n_eff + prior_games)
    off = L + shrink * (raw_off - L)
    dfn = L + shrink * (raw_def - L)
    league_ratio = league.g60 / max(league.xg60, 1e-9)
    finish = (gf + FINISH_PRIOR_XG * league_ratio) / (xgf + FINISH_PRIOR_XG) / league_ratio
    stop = (ga + FINISH_PRIOR_XG * league_ratio) / (xga + FINISH_PRIOR_XG) / league_ratio
    return TeamRating(team=team, off_xg60=off, def_xg60=dfn, finish=finish, stop=stop, games_used=n_eff,
                      raw_off_xg60=raw_off, raw_def_xg60=raw_def, gf60=gf / minutes * 60, ga60=ga / minutes * 60)


def last_game_date(log: pd.DataFrame, team: str, as_of: str) -> int | None:
    cut = _date_int(as_of)
    d = log[(log["team"] == team) & (log["date_int"] < cut)]
    return int(d["date_int"].max()) if len(d) else None


def rest_days(prev_date_int: int | None, game_date: str) -> int | None:
    if prev_date_int is None:
        return None
    p = pd.Timestamp(str(prev_date_int))
    g = pd.Timestamp(game_date)
    return int((g - p).days)


def goalie_factor(goals_against: float | None, xg_against: float | None, league_ratio: float = 1.0, prior_xg: float = FINISH_PRIOR_XG) -> float:
    """Regressed GA/xGA for one goalie (1.0 == league average; < 1 is better). None inputs -> 1.0 (unknown goalie)."""
    if goals_against is None or xg_against is None or xg_against <= 0:
        return 1.0
    return (goals_against + prior_xg * league_ratio) / (xg_against + prior_xg) / league_ratio


def goalie_factor_from_savepct(save_pct: float | None, shots_against: float | None, league_save_pct: float = 0.902, prior_shots: float = 800.0) -> float:
    """Fallback when no xG-based goalie data exists (NHL stats API gives SV% and shots): regressed GA rate ratio."""
    if save_pct is None or shots_against is None or shots_against <= 0:
        return 1.0
    ga = (1 - save_pct) * shots_against
    prior_ga = (1 - league_save_pct) * prior_shots
    rate = (ga + prior_ga) / (shots_against + prior_shots)
    return rate / (1 - league_save_pct)


def expected_goals(home: TeamRating, away: TeamRating, league: LeagueRates, home_goalie_factor: float = 1.0,
                   away_goalie_factor: float = 1.0, home_b2b: bool = False, away_b2b: bool = False,
                   neutral_site: bool = False) -> tuple[float, float, dict[str, Any]]:
    """(lam_home, lam_away, components). Goalie factors apply to the OPPONENT's lambda (they stop the other team)."""
    L = max(league.xg60, 1e-6)
    home_adj = 1.0 if neutral_site else HOME_ADJ
    lam_h = league.g60 * (home.off_xg60 / L) * (away.def_xg60 / L) * home.finish * away_goalie_factor * home_adj
    lam_a = league.g60 * (away.off_xg60 / L) * (home.def_xg60 / L) * away.finish * home_goalie_factor / home_adj
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
    comp = {
        "league_g60": league.g60, "league_xg60": league.xg60, "home_off_xg60": home.off_xg60, "away_def_xg60": away.def_xg60,
        "away_off_xg60": away.off_xg60, "home_def_xg60": home.def_xg60, "home_finish": home.finish, "away_finish": away.finish,
        "home_goalie_factor": home_goalie_factor, "away_goalie_factor": away_goalie_factor, "home_adj": home_adj,
        "home_b2b": home_b2b, "away_b2b": away_b2b, "home_games_used": home.games_used, "away_games_used": away.games_used,
        "feature_version": FEATURE_VERSION,
    }
    return float(lam_h), float(lam_a), comp


def logit(p: float) -> float:
    p = min(max(p, 1e-6), 1 - 1e-6)
    return math.log(p / (1 - p))


def inv_logit(x: float) -> float:
    return 1 / (1 + math.exp(-x))
