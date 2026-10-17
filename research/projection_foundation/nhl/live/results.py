"""Results stage: FINAL box scores (data-archive `player_events`, written by the repo's settle ingestion only when a game is
final) -> pf_core outcome records for every archived forecast key.

  skaters   shots (SOG), goals, assists, points, toi_minutes (toi_s / 60); participated = dressed with toi_s > 0
            (scratched or never entered -> participated False -> the forecast is void, as Kalshi props are)
  goalies   saves; participated = the box-score STARTER (relief appearances are void: the forecast is conditional on starting)
  teams     team_goals = goals scored by the team (regulation + OT, shootout goals excluded, as the training target)

A game counts only if it is in the final-games archive, its schedule status is not a non-final state, and both teams have
skater rows. Stat corrections are picked up because `nhl.data` keeps the newest complete snapshot per game; an outcome is
re-archived only when its value changed (the settle stage then appends a correction, never an overwrite).
"""
from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

import pandas as pd

from pf_core import prospective as pr

from nhl import data

from . import common as C

SOURCE = "nhl_player_events (data-archive, final boxscore)"


def final_games(archive: str, now: datetime, back_days: int) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, set[int]]:
    """(players, goalies, goals, schedule, ids of games safe to settle) for games dated within the look-back window."""
    p = data.load_kind("players")
    g = data.load_kind("goalies")
    goals = data.load_kind("goals")
    since = pd.Timestamp(now - timedelta(days=back_days)).tz_localize(None).normalize()
    p = p[p["game_date"] >= since]
    g = g[g["game_date"] >= since]
    sched = C.schedule_asof(archive, now, back_days=back_days + 2)
    ok = set(p.groupby("game_id")["team_id"].nunique().loc[lambda s: s == 2].index.astype(int))
    if len(sched):
        bad = set(sched.loc[sched["status"].isin(["not_started", "scheduled", "live", "in_progress", "postponed"]), "game_id"].astype(int))
        ok -= bad
    return p, g, goals, sched, ok


def build_outcomes(forecasts: pd.DataFrame, p: pd.DataFrame, g: pd.DataFrame, goals: pd.DataFrame, ok: set[int]) -> list[dict]:
    """One outcome row per (game, entity, family) that we or the incumbent forecast and whose game is settled-safe."""
    if forecasts.empty:
        return []
    keys = forecasts[["game_id", "entity_id", "family"]].drop_duplicates()
    keys = keys[keys["game_id"].astype(int).isin(ok)]
    if keys.empty:
        return []
    abbr = C.abbrev_by_id()
    date_of = p.drop_duplicates("game_id").set_index("game_id")["game_date"].dt.strftime("%Y-%m-%d").to_dict()
    pk = p.assign(pid=p["player_id"].astype(str)).set_index(["game_id", "pid"])
    gk = g[g["starter"].astype(bool) & (g["toi_s"] > 0)].assign(pid=lambda d: d["player_id"].astype(str)).set_index(["game_id", "pid"])
    team_goals = goals.groupby(["game_id", "team_id"]).size()
    teams_by_game = p.groupby("game_id")["team_id"].unique().to_dict()
    out = []
    for r in keys.itertuples():
        gid = int(r.game_id)
        base = {"game_id": str(gid), "entity_id": r.entity_id, "family": r.family, "final": True, "source": SOURCE,
                "game_date": date_of.get(gid)}
        if base["game_date"] is None:
            continue
        if r.family == "team_goals":
            tid = next((t for t in teams_by_game.get(gid, []) if abbr.get(int(t)) == r.entity_id), None)
            if tid is None:
                continue
            out.append({**base, "actual": int(team_goals.get((gid, int(tid)), 0)), "participated": True})
        elif r.family == "saves":
            if (gid, r.entity_id) in gk.index:
                row = gk.loc[(gid, r.entity_id)]
                row = row.iloc[-1] if isinstance(row, pd.DataFrame) else row
                out.append({**base, "actual": int(row["saves"]), "participated": True})
            else:
                out.append({**base, "actual": None, "participated": False})
        else:
            if (gid, r.entity_id) in pk.index:
                row = pk.loc[(gid, r.entity_id)]
                row = row.iloc[-1] if isinstance(row, pd.DataFrame) else row
                if row["toi_s"] > 0:
                    val = {"shots": row["sog"], "goals": row["goals"], "assists": row["assists"], "points": row["points"],
                           "toi_minutes": row["toi_s"] / 60.0}[r.family]
                    out.append({**base, "actual": float(val), "participated": True})
                    continue
            out.append({**base, "actual": None, "participated": False})
    return out


def run(archive: str, out_root: str, now: datetime, back_days: int = 14) -> dict[str, Any]:
    days = [(now - timedelta(days=d)).strftime("%Y-%m-%d") for d in range(back_days + 2, -2, -1)]
    f = pr.load_forecasts(out_root, C.SPORT, days)
    st: dict[str, Any] = {"forecast_keys": 0, "final_games": 0, "candidate_outcomes": 0, "changed_or_new": 0, "written": 0,
                          "rejected_not_final": 0}
    if f.empty:
        return st
    p, g, goals, sched, ok = final_games(archive, now, back_days)
    st["final_games"] = len(ok)
    cand = build_outcomes(f, p, g, goals, ok)
    st["forecast_keys"] = int(len(f[["game_id", "entity_id", "family"]].drop_duplicates()))
    st["candidate_outcomes"] = len(cand)
    # skip outcomes already archived with the same value (idempotent); changed values are re-archived -> correction
    prev = pd.DataFrame(pr._read(out_root, "outcomes", C.SPORT, days))
    last: dict[tuple, tuple] = {}
    if len(prev):
        for r in prev.sort_values("observed_utc").itertuples():
            last[(str(r.game_id), str(r.entity_id), r.family)] = (None if pd.isna(r.actual) else float(r.actual), bool(r.participated))
    new = [r for r in cand if last.get((r["game_id"], r["entity_id"], r["family"])) !=
           (None if r["actual"] is None else float(r["actual"]), bool(r["participated"]))]
    st["changed_or_new"] = len(new)
    if new:
        s = pr.archive_outcomes(new, out_root, C.SPORT, now_utc=C.iso(now))
        st["written"], st["rejected_not_final"] = s["written"], s["rejected_not_final"]
    return st
