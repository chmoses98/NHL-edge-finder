"""``nhl context``: snapshot everything a simulation may know, as append-only ledger kinds, with provenance.

Kinds written (all under the archive root; every row carries ``_observed_at_utc`` / ``_run_id`` from the ledger):
    context/schedule            Game rows for the next 8 days incl. today (NHL api-web /schedule/{date})
    context/team_games          MoneyPuck team game log, situation 'all', current + previous season
    context/team_summary        NHL stats team/summary rows (GF/GA, PP%, PK%, shots) for cur + prev season
    context/goalie_stats        NHL stats goalie/summary rows (cur + prev) and MoneyPuck goalie rows (prev season)
    context/rosters             goalies (and skaters) on each club's current roster, with NHL player ids
    context/goalie_observations DailyFaceoff starting-goalie observations resolved to NHL game ids
    context/injuries            ESPN injury feed rows (optional enrichment; never a hard dependency)
    context/sportsbook_odds     the sportsbook lines the NHL schedule feed itself carries. QUARANTINED: research /
                                MARKET_ANCHORED input only; DATA_ONLY must never read this kind.

A failure in any optional source is recorded in STATUS_context.json and the rest of the refresh proceeds.
"""

from __future__ import annotations

import json
from datetime import timedelta
from pathlib import Path
from typing import Any

from nhl_edge.archive.ledger import Ledger
from nhl_edge.data import moneypuck, nhl_api
from nhl_edge.data.goalies import fetch_dailyfaceoff
from nhl_edge.data.http import FetchError, fetch
from nhl_edge.identity.teams import registry
from nhl_edge.log import get_logger, kv
from nhl_edge.schemas.core import Game
from nhl_edge.timeutil import ET, et_date, iso, utcnow

log = get_logger(__name__)

ESPN_INJURIES_URL = "https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/injuries"
SCHEDULE_DAYS_AHEAD = 8


def game_rows(games: list[Game]) -> list[dict[str, Any]]:
    out = []
    for g in games:
        d = g.model_dump(mode="json")
        d["start_time_utc"] = iso(g.start_time_utc)
        out.append(d)
    return out


def sportsbook_rows(payload: dict[str, Any]) -> list[dict[str, Any]]:
    """The schedule feed embeds partner odds per team. Kept in a quarantined kind for market research only."""
    rows = []
    partners = {p.get("partnerId"): p for p in payload.get("oddsPartners") or []}
    for day in payload.get("gameWeek") or []:
        for g in day.get("games") or []:
            for side in ("homeTeam", "awayTeam"):
                for o in (g.get(side) or {}).get("odds") or []:
                    p = partners.get(o.get("providerId")) or {}
                    rows.append({"game_id": str(g.get("id")), "side": side[:4], "team_id": (g.get(side) or {}).get("id"), "provider_id": o.get("providerId"),
                                 "provider": p.get("name"), "value": o.get("value"), "start_time_utc": g.get("startTimeUTC"), "game_state": g.get("gameState")})
    return rows


def fetch_schedule_window(start_date_et: str, days: int = SCHEDULE_DAYS_AHEAD) -> tuple[list[Game], list[dict[str, Any]], list[dict[str, Any]]]:
    """The api-web schedule endpoint returns a week from the requested date; two calls cover 8+ days."""
    games: dict[str, Game] = {}
    metas: list[dict[str, Any]] = []
    odds: list[dict[str, Any]] = []
    d0 = utcnow().astimezone(ET).date() if not start_date_et else __import__("datetime").date.fromisoformat(start_date_et)
    for offset in (0, 7):
        d = (d0 + timedelta(days=offset)).isoformat()
        try:
            url = f"{nhl_api.settings().nhl_api_base_url}/schedule/{d}"
            f = fetch(url)
            payload = f.json()
            for g in nhl_api.parse_schedule(payload):
                games[g.game_id] = g
            odds += sportsbook_rows(payload)
            metas.append({"source": "nhl_api_schedule", "url": url, "fetched_at_utc": f.fetched_at_utc, "sha256": f.sha256, "n": len(games)})
        except (FetchError, ValueError) as e:
            metas.append({"source": "nhl_api_schedule", "date": d, "error": str(e)[:200]})
    end = d0 + timedelta(days=days)
    keep = [g for g in games.values() if d0.isoformat() <= g.game_date_et <= end.isoformat()]
    return sorted(keep, key=lambda g: (g.start_time_utc, g.game_id)), metas, odds


def resolve_goalie_observations(obs_rows: list[dict[str, Any]], games: list[Game]) -> tuple[list[dict[str, Any]], list[str]]:
    """DailyFaceoff rows carry (date, team); map to the NHL game id from the schedule snapshot."""
    by_key: dict[tuple[str, int], Game] = {}
    for g in games:
        by_key[(g.game_date_et, g.home_team_id)] = g
        by_key[(g.game_date_et, g.away_team_id)] = g
    out, problems = [], []
    for o in obs_rows:
        gid = str(o.get("game_id", ""))
        if gid.startswith("dfo:"):
            _, date, tid = gid.split(":")
            g = by_key.get((date, int(tid)))
            if g is None:
                problems.append(f"no NHL game for team {tid} on {date}")
                continue
            o = {**o, "game_id": g.game_id, "game_date_et": date}
        out.append(o)
    return out, problems


def run_context_refresh(out_root: Path, date_et: str | None = None, with_dfo: bool = True, with_injuries: bool = True,
                        with_moneypuck: bool = True) -> int:
    now = utcnow()
    today = date_et or et_date(now)
    ledger = Ledger(out_root)
    status: dict[str, Any] = {"refreshed_at_utc": iso(now), "date_et": today, "run_id": ledger.run_id, "sources": {}, "errors": []}
    reg = registry()

    games, metas, odds = fetch_schedule_window(today)
    status["sources"]["schedule"] = metas
    status["n_games"] = len(games)
    status["games_today"] = [g.game_id for g in games if g.game_date_et == today]
    if games:
        e = ledger.append_rows("context/schedule", game_rows(games), observed_at=now, meta={"sources": metas})
        status["schedule_path"] = e.path
    else:
        status["errors"].append("schedule: no games returned (source error or off-season)")
    if odds:
        ledger.append_rows("context/sportsbook_odds", odds, observed_at=now, meta={"quarantine": "MARKET input only; never DATA_ONLY"})
    status["n_sportsbook_rows"] = len(odds)

    season_id = nhl_api.season_id_for(today)
    prev_season_id = int(f"{int(str(season_id)[:4]) - 1}{int(str(season_id)[:4])}")
    # team summaries (official)
    ts_rows: list[dict[str, Any]] = []
    for sid in (prev_season_id, season_id):
        try:
            rows, meta = nhl_api.fetch_team_summary(sid)
            ts_rows += [{**r, "_season_id": sid} for r in rows]
            status["sources"][f"team_summary_{sid}"] = meta
        except (FetchError, ValueError) as e:
            status["errors"].append(f"team_summary_{sid}: {str(e)[:160]}")
    if ts_rows:
        ledger.append_rows("context/team_summary", ts_rows, observed_at=now)
    # goalie summaries (official)
    gs_rows: list[dict[str, Any]] = []
    for sid in (prev_season_id, season_id):
        try:
            rows, meta = nhl_api.fetch_goalie_summary(sid)
            gs_rows += [{**r, "_season_id": sid, "_source": "nhl_stats"} for r in rows]
            status["sources"][f"goalie_summary_{sid}"] = meta
        except (FetchError, ValueError) as e:
            status["errors"].append(f"goalie_summary_{sid}: {str(e)[:160]}")
    # MoneyPuck
    mp_season = moneypuck.mp_season(today)
    if with_moneypuck:
        for s in (mp_season - 1, mp_season):
            df, meta = moneypuck.fetch_goalie_summary(s)
            status["sources"][f"moneypuck_goalies_{s}"] = meta
            if df is not None and len(df):
                gs_rows += [{**{k: (None if (isinstance(v, float) and v != v) else v) for k, v in r.items()}, "_season_mp": s, "_source": "moneypuck"} for r in df.to_dict("records")]
        df, meta = moneypuck.fetch_team_game_log(mp_season - 1)
        status["sources"]["moneypuck_team_games"] = meta
        if df is not None and len(df):
            recs = [{k: (None if (isinstance(v, float) and v != v) else v) for k, v in r.items()} for r in df.to_dict("records")]
            ledger.append_rows("context/team_games", recs, observed_at=now, meta={k: v for k, v in meta.items() if k != "url"})
        else:
            status["errors"].append(f"moneypuck_team_games: {meta.get('error')}")
    if gs_rows:
        ledger.append_rows("context/goalie_stats", gs_rows, observed_at=now)
    # rosters for teams playing in the window
    team_ids = sorted({t for g in games for t in (g.home_team_id, g.away_team_id)})
    roster_rows: list[dict[str, Any]] = []
    n_roster_err = 0
    for tid in team_ids:
        ab = reg.by_id(tid).abbrev
        try:
            rows, _ = nhl_api.fetch_roster(ab, ttl_s=6 * 3600)
            roster_rows += [{**r, "team_id": tid} for r in rows]
        except (FetchError, ValueError) as e:
            n_roster_err += 1
            status["errors"].append(f"roster_{ab}: {str(e)[:120]}")
    if roster_rows:
        ledger.append_rows("context/rosters", roster_rows, observed_at=now, meta={"teams": len(team_ids), "errors": n_roster_err})
    # goalie observations (DailyFaceoff, today + tomorrow)
    if with_dfo:
        obs_rows: list[dict[str, Any]] = []
        raw_pages: list[dict[str, Any]] = []
        for offset in (0, 1):
            d = (__import__("datetime").date.fromisoformat(today) + timedelta(days=offset)).isoformat()
            obs, meta = fetch_dailyfaceoff(d)
            status["sources"][f"dailyfaceoff_{d}"] = {k: v for k, v in meta.items() if k != "raw_rows"}
            raw_pages.append({"date": d, "meta": {k: v for k, v in meta.items() if k != "raw_rows"}, "rows": meta.get("raw_rows", [])})
            obs_rows += [o.model_dump(mode="json") for o in obs]
        resolved, problems = resolve_goalie_observations(obs_rows, games)
        status["goalie_observation_problems"] = problems
        status["n_goalie_observations"] = len(resolved)
        if resolved:
            ledger.append_rows("context/goalie_observations", resolved, observed_at=now)
        ledger.write_blob("context/dailyfaceoff_raw", json.dumps(raw_pages, default=str).encode(), observed_at=now)
    # injuries (ESPN, optional)
    if with_injuries:
        try:
            f = fetch(ESPN_INJURIES_URL, max_retries=1)
            rows = parse_espn_injuries(f.json())
            status["sources"]["espn_injuries"] = {"url": ESPN_INJURIES_URL, "fetched_at_utc": f.fetched_at_utc, "n": len(rows), "sha256": f.sha256}
            if rows:
                ledger.append_rows("context/injuries", rows, observed_at=now)
        except (FetchError, ValueError) as e:
            status["errors"].append(f"espn_injuries: {str(e)[:160]}")
    (out_root / "STATUS_context.json").write_text(json.dumps(status, indent=1, default=str))
    log.info(kv(event="context_refreshed", games=len(games), errors=len(status["errors"])))
    print(json.dumps({k: v for k, v in status.items() if k != "sources"}, indent=1, default=str))
    return 0


def parse_espn_injuries(payload: dict[str, Any]) -> list[dict[str, Any]]:
    reg = registry()
    out = []
    for team in payload.get("injuries") or []:
        tname = team.get("displayName") or team.get("team", {}).get("displayName")
        t = reg.resolve_name(tname or "")
        for inj in team.get("injuries") or []:
            ath = inj.get("athlete") or {}
            out.append({
                "team_name": tname, "team_id": t.team_id if t else None, "player_name": ath.get("displayName"), "espn_id": ath.get("id"),
                "position": (ath.get("position") or {}).get("abbreviation"), "status": inj.get("status"), "type": (inj.get("type") or {}).get("description"),
                "detail": (inj.get("details") or {}).get("type"), "return_date": (inj.get("details") or {}).get("returnDate"),
                "reported": inj.get("date"), "long_comment": (inj.get("longComment") or "")[:300], "source": "espn_injuries",
            })
    return out
