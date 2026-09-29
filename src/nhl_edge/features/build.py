"""Assemble point-in-time simulation inputs for one game from archived context snapshots.

Everything comes in as rows already read from the ledger by the caller, together with a ``cutoff`` instant. This
module never touches the network or the file system, so a test can prove the cutoff discipline directly.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

import pandas as pd

from nhl_edge import FEATURE_VERSION
from nhl_edge.features.ratings import (
    LeagueRates,
    TeamRating,
    expected_goals,
    goalie_factor,
    goalie_factor_from_savepct,
    last_game_date,
    league_rates,
    prepare_gamelog,
    rest_days,
    team_rating,
)
from nhl_edge.goalies.state import GoalieState, latest_state, mixture_factor
from nhl_edge.sim.engine import TeamParams


@dataclass
class GameInputs:
    game_id: str
    game_date_et: str
    home_team_id: int
    away_team_id: int
    home_abbrev: str
    away_abbrev: str
    cutoff_utc: datetime
    league: LeagueRates
    home_rating: TeamRating
    away_rating: TeamRating
    home_goalie: GoalieState
    away_goalie: GoalieState
    home_goalie_factor: float
    away_goalie_factor: float
    home_goalie_detail: dict[str, Any]
    away_goalie_detail: dict[str, Any]
    home_rest_days: int | None
    away_rest_days: int | None
    home_b2b: bool
    away_b2b: bool
    lam_home: float
    lam_away: float
    components: dict[str, Any]
    trusted: bool
    reasons: list[str] = field(default_factory=list)
    feature_version: str = FEATURE_VERSION

    def team_params(self) -> tuple[TeamParams, TeamParams]:
        return (TeamParams(self.home_team_id, self.home_abbrev, self.lam_home, self.components),
                TeamParams(self.away_team_id, self.away_abbrev, self.lam_away, self.components))

    def to_dict(self) -> dict[str, Any]:
        return {
            "game_id": self.game_id, "cutoff_utc": self.cutoff_utc.isoformat().replace("+00:00", "Z"), "feature_version": self.feature_version,
            "league": self.league.__dict__, "home_rating": self.home_rating.to_dict(), "away_rating": self.away_rating.to_dict(),
            "home_goalie": self.home_goalie.to_dict() | {"factor": self.home_goalie_factor, "detail": self.home_goalie_detail},
            "away_goalie": self.away_goalie.to_dict() | {"factor": self.away_goalie_factor, "detail": self.away_goalie_detail},
            "home_rest_days": self.home_rest_days, "away_rest_days": self.away_rest_days, "home_b2b": self.home_b2b, "away_b2b": self.away_b2b,
            "lam_home": self.lam_home, "lam_away": self.lam_away, "components": self.components, "trusted": self.trusted, "reasons": self.reasons,
        }


def goalie_factor_table(goalie_stat_rows: list[dict[str, Any]], season_id: int) -> dict[int | None, float]:
    """player_id -> regressed goalie factor, preferring MoneyPuck xG-based rows, then NHL stats SV% rows.

    Current-season NHL rows are blended with previous-season rows by shots faced (both regressed), so early in a
    season a goalie's factor is mostly last season's, which is the honest prior."""
    mp: dict[int, tuple[float, float]] = {}
    nhl: dict[int, tuple[float, float]] = {}
    for r in goalie_stat_rows:
        src = r.get("_source")
        try:
            if src == "moneypuck" and r.get("situation") == "all":
                pid = int(r["playerId"])
                g, xg = float(r["goals"]), float(r["xGoals"])
                pg, pxg = mp.get(pid, (0.0, 0.0))
                mp[pid] = (pg + g, pxg + xg)
            elif src == "nhl_stats":
                pid = int(r["playerId"])
                sa, sv = float(r.get("shotsAgainst") or 0), float(r.get("saves") or 0)
                psa, psv = nhl.get(pid, (0.0, 0.0))
                nhl[pid] = (psa + sa, psv + sv)
        except (KeyError, TypeError, ValueError):
            continue
    out: dict[int | None, float] = {}
    mp_g = sum(v[0] for v in mp.values())
    mp_xg = sum(v[1] for v in mp.values())
    ratio = mp_g / mp_xg if mp_xg > 0 else 1.0
    for pid, (g, xg) in mp.items():
        out[pid] = goalie_factor(g, xg, league_ratio=ratio)
    for pid, (sa, sv) in nhl.items():
        if pid not in out and sa > 0:
            out[pid] = goalie_factor_from_savepct(sv / sa, sa)
    return out


def build_game_inputs(game: dict[str, Any], cutoff: datetime, team_game_rows: list[dict[str, Any]], goalie_stat_rows: list[dict[str, Any]],
                      goalie_obs_rows: list[dict[str, Any]], season_id: int, mp_season: int) -> GameInputs:
    reasons: list[str] = []
    home_id, away_id = int(game["home_team_id"]), int(game["away_team_id"])
    home_ab, away_ab = game["home_abbrev"], game["away_abbrev"]
    date = game["game_date_et"]
    log = prepare_gamelog(pd.DataFrame(team_game_rows)) if team_game_rows else pd.DataFrame(columns=["team", "date_int", "season", "xGoalsFor", "xGoalsAgainst", "goalsFor", "goalsAgainst", "minutes", "game_id"])
    if len(log) and "team_abbrev" in log.columns:
        log["team"] = log["team_abbrev"].fillna(log["team"])
    league = league_rates(log, date, season=mp_season) if len(log) else LeagueRates(3.05, 3.05, 0, date)
    hr = team_rating(log, home_ab, date, league, current_season=mp_season) if len(log) else TeamRating(home_ab, league.xg60, league.xg60, 1.0, 1.0, 0.0)
    ar = team_rating(log, away_ab, date, league, current_season=mp_season) if len(log) else TeamRating(away_ab, league.xg60, league.xg60, 1.0, 1.0, 0.0)
    if hr.games_used < 5 or ar.games_used < 5:
        reasons.append(f"thin team history: home {hr.games_used:.1f} / away {ar.games_used:.1f} weighted games (ratings mostly league prior)")
    factors = goalie_factor_table(goalie_stat_rows, season_id)
    hg = latest_state(goalie_obs_rows, game["game_id"], home_id, cutoff)
    ag = latest_state(goalie_obs_rows, game["game_id"], away_id, cutoff)
    hf, hdet = mixture_factor(hg, factors)
    af, adet = mixture_factor(ag, factors)
    for side, st in (("home", hg), ("away", ag)):
        if st.status.value == "UNKNOWN":
            reasons.append(f"{side} goalie UNKNOWN at cutoff: average goaltending assumed")
        elif st.player_id is None:
            reasons.append(f"{side} goalie named ({st.player_name}) but not resolved to an NHL id: average goaltending assumed")
    h_prev = last_game_date(log, home_ab, date) if len(log) else None
    a_prev = last_game_date(log, away_ab, date) if len(log) else None
    h_rest, a_rest = rest_days(h_prev, date), rest_days(a_prev, date)
    h_b2b, a_b2b = h_rest == 1, a_rest == 1
    lam_h, lam_a, comp = expected_goals(hr, ar, league, home_goalie_factor=hf, away_goalie_factor=af, home_b2b=h_b2b, away_b2b=a_b2b,
                                       neutral_site=bool(game.get("neutral_site")))
    trusted = not any("thin team history" in r for r in reasons)
    return GameInputs(game_id=str(game["game_id"]), game_date_et=date, home_team_id=home_id, away_team_id=away_id, home_abbrev=home_ab, away_abbrev=away_ab,
                      cutoff_utc=cutoff, league=league, home_rating=hr, away_rating=ar, home_goalie=hg, away_goalie=ag, home_goalie_factor=hf,
                      away_goalie_factor=af, home_goalie_detail=hdet, away_goalie_detail=adet, home_rest_days=h_rest, away_rest_days=a_rest,
                      home_b2b=h_b2b, away_b2b=a_b2b, lam_home=lam_h, lam_away=lam_a, components=comp, trusted=trusted, reasons=reasons)


def resolve_goalie_ids(goalie_obs_rows: list[dict[str, Any]], roster_rows: list[dict[str, Any]], goalie_stat_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Attach NHL player ids to name-only goalie observations (DailyFaceoff) using roster and stats names."""
    by_name: dict[tuple[int, str], int] = {}
    for r in roster_rows:
        if r.get("position") == "G" and r.get("player_id") and r.get("team_id"):
            by_name[(int(r["team_id"]), f"{r.get('first_name', '')} {r.get('last_name', '')}".strip().lower())] = int(r["player_id"])
    any_team: dict[str, int] = {}
    for r in goalie_stat_rows:
        if r.get("_source") == "nhl_stats" and r.get("playerId") and r.get("goalieFullName"):
            any_team[str(r["goalieFullName"]).lower()] = int(r["playerId"])
        elif r.get("_source") == "moneypuck" and r.get("playerId") and r.get("name"):
            any_team.setdefault(str(r["name"]).lower(), int(r["playerId"]))
    out = []
    for o in goalie_obs_rows:
        if o.get("player_id") is None and o.get("player_name"):
            key = (int(o["team_id"]), str(o["player_name"]).lower())
            pid = by_name.get(key) or any_team.get(str(o["player_name"]).lower())
            o = {**o, "player_id": pid, "note": (o.get("note") or "") + ("" if pid else "; player id unresolved")}
        out.append(o)
    return out
