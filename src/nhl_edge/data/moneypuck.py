"""MoneyPuck readers (public CSV downloads; shapes verified 2026-09-29 in docs/probe/samples).

    seasonSummary/{year}/regular/teams.csv     team season aggregates by situation (all/5on5/5on4/4on5/other)
    seasonSummary/{year}/regular/goalies.csv   goalie season aggregates by situation: xGoals vs goals (GSAx inputs)
    careers/gameByGame/all_teams.csv           every team-game since 2008 by situation (the ratings' input)

MoneyPuck 'season' 2025 == NHL 2025-26. A season file 404s until the season has games (teams 2026 did on 2026-09-29).
"""

from __future__ import annotations

import io
from typing import Any

import pandas as pd

from nhl_edge.config import settings
from nhl_edge.data.http import FetchError, fetch
from nhl_edge.identity.teams import TeamIdentityError, registry
from nhl_edge.log import get_logger, kv

log = get_logger(__name__)


def mp_season(date_et: str) -> int:
    y, m = int(date_et[:4]), int(date_et[5:7])
    return y if m >= 7 else y - 1


def canonical_abbrev(mp_team: str) -> str | None:
    try:
        return registry().by_abbrev(str(mp_team)).abbrev
    except TeamIdentityError:
        return None


def parse_csv(text: str) -> pd.DataFrame:
    return pd.read_csv(io.StringIO(text))


def fetch_team_summary(season: int) -> tuple[pd.DataFrame | None, dict[str, Any]]:
    url = f"{settings().moneypuck_base_url}/playerData/seasonSummary/{season}/regular/teams.csv"
    try:
        f = fetch(url, ttl_s=1800, max_retries=2)
    except FetchError as e:
        return None, {"source": "moneypuck_teams", "url": url, "error": str(e)[:200]}
    df = parse_csv(f.text())
    df["team_abbrev"] = df["team"].map(canonical_abbrev)
    return df, {"source": "moneypuck_teams", "url": url, "fetched_at_utc": f.fetched_at_utc, "sha256": f.sha256, "n": len(df), "last_modified": f.last_modified}


def fetch_goalie_summary(season: int) -> tuple[pd.DataFrame | None, dict[str, Any]]:
    url = f"{settings().moneypuck_base_url}/playerData/seasonSummary/{season}/regular/goalies.csv"
    try:
        f = fetch(url, ttl_s=1800, max_retries=2)
    except FetchError as e:
        return None, {"source": "moneypuck_goalies", "url": url, "error": str(e)[:200]}
    df = parse_csv(f.text())
    if "team" in df.columns:
        df["team_abbrev"] = df["team"].map(canonical_abbrev)
    return df, {"source": "moneypuck_goalies", "url": url, "fetched_at_utc": f.fetched_at_utc, "sha256": f.sha256, "n": len(df), "last_modified": f.last_modified}


def fetch_team_game_log(min_season: int, situations: tuple[str, ...] = ("all",), ttl_s: float = 3600) -> tuple[pd.DataFrame | None, dict[str, Any]]:
    """all_teams.csv filtered to ``season >= min_season`` and the requested situations. ~40 MB download; cached."""
    url = f"{settings().moneypuck_base_url}/playerData/careers/gameByGame/all_teams.csv"
    try:
        f = fetch(url, ttl_s=ttl_s, timeout=180, max_retries=2)
    except FetchError as e:
        return None, {"source": "moneypuck_all_teams", "url": url, "error": str(e)[:200]}
    df = parse_csv(f.text())
    df["season"] = pd.to_numeric(df["season"], errors="coerce")
    df = df[(df["season"] >= min_season) & (df["situation"].isin(situations))].copy()
    df["team_abbrev"] = df["team"].map(canonical_abbrev)
    df["opp_abbrev"] = df["opposingTeam"].map(canonical_abbrev)
    n_unres = int(df["team_abbrev"].isna().sum())
    if n_unres:
        log.warning(kv(event="moneypuck_unresolved_teams", n=n_unres, sample=sorted(df.loc[df["team_abbrev"].isna(), "team"].unique())[:5]))
    return df, {"source": "moneypuck_all_teams", "url": url, "fetched_at_utc": f.fetched_at_utc, "sha256": f.sha256, "n": len(df),
                "last_modified": f.last_modified, "min_season": min_season, "situations": list(situations), "unresolved_teams": n_unres}


def goalie_factors_from_summary(df: pd.DataFrame | None, prior_xg: float = 60.0) -> dict[int, dict[str, Any]]:
    """MoneyPuck goalie season rows (situation 'all') -> {playerId: {factor, goals, xGoals, games}} via regressed GA/xGA."""
    out: dict[int, dict[str, Any]] = {}
    if df is None or df.empty or "playerId" not in df.columns:
        return out
    d = df[df["situation"] == "all"] if "situation" in df.columns else df
    tot_g, tot_xg = float(d["goals"].sum()), float(d["xGoals"].sum())
    league_ratio = tot_g / tot_xg if tot_xg > 0 else 1.0
    for _, r in d.iterrows():
        try:
            pid = int(r["playerId"])
            g, xg = float(r["goals"]), float(r["xGoals"])
        except (TypeError, ValueError):
            continue
        factor = (g + prior_xg * league_ratio) / (xg + prior_xg) / league_ratio if xg > 0 or g > 0 else 1.0
        out[pid] = {"factor": factor, "goals": g, "xGoals": xg, "games": int(r.get("games_played", 0) or 0), "name": r.get("name"), "team": r.get("team_abbrev") or r.get("team"), "league_ratio": league_ratio}
    return out
