"""Official NHL web API (api-web.nhle.com/v1) and stats REST (api.nhle.com/stats/rest/en) readers.

Shapes below were written against the API as observed in 2023-2026 and are re-verified by ``scripts/probe_sources.py``
on a network-capable runner (docs/probe/samples/*.json). Every parser is tolerant: a missing optional field
degrades to ``None`` or a skipped row with a logged reason, never an exception that kills a slate.

Endpoints used (all public, no auth):
    /v1/schedule/{YYYY-MM-DD}         week of games from that date: gameWeek[].games[]
    /v1/score/{YYYY-MM-DD}            same day's games with live scores
    /v1/gamecenter/{id}/boxscore      final score, lastPeriodType, goalie lines (starter flag)
    /v1/gamecenter/{id}/landing       scoring summary by period
    /v1/roster/{ABBREV}/current       current roster incl. goalies
    /v1/standings/now                 standings (used for team list sanity)
    /stats/rest/en/team/summary       team season aggregates (GF/GA, PP%, PK%, shots)
    /stats/rest/en/goalie/summary     goalie season aggregates (SV%, GSAA-ish inputs)
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

from nhl_edge.config import settings
from nhl_edge.data.http import Fetched, fetch
from nhl_edge.identity.teams import TeamIdentityError, registry
from nhl_edge.log import get_logger, kv
from nhl_edge.schemas.core import GAME_TYPE_MAP, FinalPeriodType, Game, GameStatus, SeasonType, season_label
from nhl_edge.timeutil import et_date, parse_iso

log = get_logger(__name__)

# gameState (observed): FUT (future), PRE (pregame, ~1h before), LIVE, CRIT (late/close), OFF (final, unofficial),
# FINAL (official). gameScheduleState: OK, PPD (postponed), SUSP (suspended), CNCL (cancelled), TBD.
_STATE_MAP = {
    "FUT": GameStatus.NOT_STARTED, "PRE": GameStatus.NOT_STARTED, "LIVE": GameStatus.LIVE, "CRIT": GameStatus.LIVE,
    "OFF": GameStatus.FINAL, "FINAL": GameStatus.FINAL,
}
_SCHED_STATE_MAP = {"PPD": GameStatus.POSTPONED, "CNCL": GameStatus.CANCELED, "SUSP": GameStatus.SUSPENDED}


def game_status(game_state: str | None, schedule_state: str | None) -> GameStatus:
    ss = (schedule_state or "").upper()
    if ss in _SCHED_STATE_MAP:
        return _SCHED_STATE_MAP[ss]
    return _STATE_MAP.get((game_state or "").upper(), GameStatus.UNKNOWN)


def _default(v: Any) -> str | None:
    """api-web localises strings as {'default': 'Toronto', 'fr': ...}."""
    if isinstance(v, dict):
        return v.get("default")
    return v if isinstance(v, str) else None


def _period_type(v: Any) -> FinalPeriodType | None:
    s = (_default(v) or "").upper()
    return FinalPeriodType(s) if s in ("REG", "OT", "SO") else None


def parse_game(g: dict[str, Any], source: str = "nhl_api_schedule") -> Game | None:
    reg = registry()
    gid = g.get("id")
    if gid is None:
        return None
    try:
        home, away = g["homeTeam"], g["awayTeam"]
        home_t = reg.by_id(home["id"]) if home.get("id") is not None else reg.by_abbrev(home["abbrev"])
        away_t = reg.by_id(away["id"]) if away.get("id") is not None else reg.by_abbrev(away["abbrev"])
        start = parse_iso(g["startTimeUTC"])
    except (KeyError, TeamIdentityError, ValueError) as e:
        log.warning(kv(event="schedule_row_skipped", game_id=gid, err=str(e)[:120]))
        return None
    stype = GAME_TYPE_MAP.get(int(g.get("gameType") or 0), SeasonType.OTHER)
    season = season_label(g.get("season") or str(gid)[:4] + str(int(str(gid)[:4]) + 1))
    outcome = g.get("gameOutcome") or {}
    status = game_status(g.get("gameState"), g.get("gameScheduleState"))
    return Game(
        game_id=str(gid), season=season, season_type=stype, game_date_et=g.get("gameDate") or et_date(start),
        start_time_utc=start, home_team_id=home_t.team_id, away_team_id=away_t.team_id, home_abbrev=home_t.abbrev,
        away_abbrev=away_t.abbrev, status=status, venue=_default(g.get("venue")), neutral_site=bool(g.get("neutralSite", False)),
        source=source, home_score=home.get("score"), away_score=away.get("score"),
        last_period_type=_period_type(outcome.get("lastPeriodType")) if status == GameStatus.FINAL else None,
        source_game_state=f"{g.get('gameState')}/{g.get('gameScheduleState')}",
    )


def parse_schedule(payload: dict[str, Any], source: str = "nhl_api_schedule") -> list[Game]:
    games: list[Game] = []
    for day in payload.get("gameWeek") or []:
        if not isinstance(day, dict):
            continue
        for g in day.get("games") or []:
            if not isinstance(g, dict):
                continue
            if not g.get("gameDate"):
                g = {**g, "gameDate": day.get("date")}
            gm = parse_game(g, source)
            if gm:
                games.append(gm)
    # /v1/score/{date} carries games at the top level
    for g in payload.get("games") or []:
        if not isinstance(g, dict):
            continue
        gm = parse_game(g, source)
        if gm:
            games.append(gm)
    return games


def fetch_schedule(date_et: str, ttl_s: float = 0.0) -> tuple[list[Game], dict[str, Any]]:
    cfg = settings()
    url = f"{cfg.nhl_api_base_url}/schedule/{date_et}"
    f = fetch(url, ttl_s=ttl_s)
    games = parse_schedule(f.json())
    return games, {"source": "nhl_api_schedule", "url": url, "fetched_at_utc": f.fetched_at_utc, "sha256": f.sha256, "n": len(games)}


def fetch_score_day(date_et: str) -> tuple[list[Game], dict[str, Any]]:
    cfg = settings()
    url = f"{cfg.nhl_api_base_url}/score/{date_et}"
    f = fetch(url)
    games = parse_schedule(f.json(), source="nhl_api_score")
    return games, {"source": "nhl_api_score", "url": url, "fetched_at_utc": f.fetched_at_utc, "sha256": f.sha256, "n": len(games)}


# ---- box score / final result ----------------------------------------------------------------


def _goalie_lines(team_stats: dict[str, Any] | None) -> list[dict[str, Any]]:
    out = []
    for gl in (team_stats or {}).get("goalies") or []:
        out.append({
            "player_id": gl.get("playerId"), "name": _default(gl.get("name")), "starter": bool(gl.get("starter", False)),
            "decision": gl.get("decision"), "toi": gl.get("toi"), "shots_against": gl.get("shotsAgainst"),
            "goals_against": gl.get("goalsAgainst"), "save_pct": gl.get("savePctg"),
        })
    return out


def parse_boxscore(payload: dict[str, Any]) -> dict[str, Any]:
    """Final result with regulation score derived from the final score and the last period type.

    NHL scoring: an OT or SO win adds exactly one goal to the winner's final score, so the regulation score is
    ``final - 1`` for the winner and equal for both sides. That derivation needs no play-by-play and cannot be
    wrong for a correctly reported final; ``landing`` scoring summaries are used only as a cross-check.
    """
    reg = registry()
    home, away = payload.get("homeTeam") or {}, payload.get("awayTeam") or {}
    status = game_status(payload.get("gameState"), payload.get("gameScheduleState"))
    lpt = _period_type((payload.get("gameOutcome") or {}).get("lastPeriodType"))
    if lpt is None and status == GameStatus.FINAL:
        pd = payload.get("periodDescriptor") or {}
        lpt = _period_type(pd.get("periodType"))
    hs, as_ = home.get("score"), away.get("score")
    reg_h = reg_a = None
    if status == GameStatus.FINAL and hs is not None and as_ is not None and lpt is not None:
        if lpt == FinalPeriodType.REG:
            reg_h, reg_a = hs, as_
        else:
            reg_h, reg_a = (hs - 1, as_) if hs > as_ else (hs, as_ - 1)
    pbg = payload.get("playerByGameStats") or {}
    try:
        home_t = reg.by_id(home["id"]) if home.get("id") is not None else reg.by_abbrev(home.get("abbrev", ""))
        away_t = reg.by_id(away["id"]) if away.get("id") is not None else reg.by_abbrev(away.get("abbrev", ""))
        home_id, away_id = home_t.team_id, away_t.team_id
    except (TeamIdentityError, KeyError):
        home_id = home.get("id")
        away_id = away.get("id")
    return {
        "game_id": str(payload.get("id")), "status": status.value, "game_state": payload.get("gameState"),
        "schedule_state": payload.get("gameScheduleState"), "home_team_id": home_id, "away_team_id": away_id,
        "home_abbrev": home.get("abbrev"), "away_abbrev": away.get("abbrev"), "home_score": hs, "away_score": as_,
        "last_period_type": lpt.value if lpt else None, "home_reg_score": reg_h, "away_reg_score": reg_a,
        "home_sog": home.get("sog"), "away_sog": away.get("sog"),
        "home_goalies": _goalie_lines(pbg.get("homeTeam")), "away_goalies": _goalie_lines(pbg.get("awayTeam")),
        "start_time_utc": payload.get("startTimeUTC"), "game_date": payload.get("gameDate"),
        "period_number": (payload.get("periodDescriptor") or {}).get("number"),
    }


def fetch_boxscore(game_id: str) -> tuple[dict[str, Any], dict[str, Any]]:
    cfg = settings()
    url = f"{cfg.nhl_api_base_url}/gamecenter/{game_id}/boxscore"
    f = fetch(url)
    box = parse_boxscore(f.json())
    return box, {"source": "nhl_api_boxscore", "url": url, "fetched_at_utc": f.fetched_at_utc, "sha256": f.sha256}


def parse_landing_scoring(payload: dict[str, Any]) -> list[dict[str, Any]]:
    """Per-goal rows from /landing: period, period type, scoring team, situation, empty-net flag, score after."""
    goals = []
    for per in ((payload.get("summary") or {}).get("scoring")) or []:
        pd = per.get("periodDescriptor") or {}
        for g in per.get("goals") or []:
            goals.append({
                "period": pd.get("number"), "period_type": pd.get("periodType"), "team_abbrev": g.get("teamAbbrev") if isinstance(g.get("teamAbbrev"), str) else _default(g.get("teamAbbrev")),
                "time_in_period": g.get("timeInPeriod"), "strength": g.get("strength"), "situation_code": g.get("situationCode"),
                "goal_modifier": g.get("goalModifier"), "home_score": g.get("homeScore"), "away_score": g.get("awayScore"),
                "scorer_id": g.get("playerId"), "empty_net": (g.get("goalModifier") or "").lower().startswith("empty"),
            })
    return goals


# ---- rosters and stats ----------------------------------------------------------------------


def parse_roster(payload: dict[str, Any], team_abbrev: str) -> list[dict[str, Any]]:
    rows = []
    for group in ("forwards", "defensemen", "goalies"):
        for p in payload.get(group) or []:
            rows.append({
                "player_id": p.get("id"), "team_abbrev": team_abbrev, "position": p.get("positionCode") or ("G" if group == "goalies" else None),
                "first_name": _default(p.get("firstName")), "last_name": _default(p.get("lastName")), "sweater": p.get("sweaterNumber"),
                "shoots_catches": p.get("shootsCatches"), "birth_date": p.get("birthDate"),
            })
    return rows


def fetch_roster(team_abbrev: str, ttl_s: float = 0.0) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    cfg = settings()
    url = f"{cfg.nhl_api_base_url}/roster/{team_abbrev}/current"
    f = fetch(url, ttl_s=ttl_s)
    rows = parse_roster(f.json(), team_abbrev)
    return rows, {"source": "nhl_api_roster", "url": url, "fetched_at_utc": f.fetched_at_utc, "sha256": f.sha256, "n": len(rows)}


def stats_rows(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict):
        return [r for r in payload.get("data") or [] if isinstance(r, dict)]
    return [r for r in payload if isinstance(r, dict)] if isinstance(payload, list) else []


def fetch_team_summary(season_id: int | str, game_type: int = 2) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    cfg = settings()
    url = f"{cfg.nhl_stats_base_url}/team/summary?limit=-1&cayenneExp=seasonId={season_id}%20and%20gameTypeId={game_type}"
    f = fetch(url)
    rows = stats_rows(f.json())
    return rows, {"source": "nhl_stats_team_summary", "url": url, "fetched_at_utc": f.fetched_at_utc, "sha256": f.sha256, "n": len(rows)}


def fetch_goalie_summary(season_id: int | str, game_type: int = 2) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    cfg = settings()
    url = f"{cfg.nhl_stats_base_url}/goalie/summary?limit=-1&cayenneExp=seasonId={season_id}%20and%20gameTypeId={game_type}"
    f = fetch(url)
    rows = stats_rows(f.json())
    return rows, {"source": "nhl_stats_goalie_summary", "url": url, "fetched_at_utc": f.fetched_at_utc, "sha256": f.sha256, "n": len(rows)}


def season_id_for(date_et: str) -> int:
    """NHL season id for a calendar date: seasons roll over in July (20262027 for 2026-09-29)."""
    y, m = int(date_et[:4]), int(date_et[5:7])
    start = y if m >= 7 else y - 1
    return int(f"{start}{start + 1}")


def now_utc() -> datetime:
    return datetime.now(tz=UTC)


__all__ = ["Fetched", "fetch_schedule", "fetch_score_day", "fetch_boxscore", "fetch_roster", "fetch_team_summary",
           "fetch_goalie_summary", "parse_schedule", "parse_game", "parse_boxscore", "parse_landing_scoring", "parse_roster",
           "game_status", "season_id_for"]
