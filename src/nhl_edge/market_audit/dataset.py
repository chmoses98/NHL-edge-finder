"""Assemble the reproducible research tables: contract master (spec + game join) and resolved outcomes."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from nhl_edge.market_audit.games import read_kind
from nhl_edge.market_audit.outcomes import GameFacts, resolve
from nhl_edge.market_audit.taxonomy import ContractSpec, build_spec


def team_uuid_map(specs: list[ContractSpec]) -> tuple[dict[str, int], list[str]]:
    """Kalshi team uuid -> NHL team_id, learned ONLY from game-winner legs (the subject is named in the title).
    Returns (map, conflicts); a uuid that maps to two clubs is reported, never silently picked."""
    seen: dict[str, set[int]] = {}
    for s in specs:
        if s.kind == "winner" and s.team_uuid and s.subject_team_id is not None:
            seen.setdefault(s.team_uuid, set()).add(s.subject_team_id)
    conflicts = [u for u, ids in seen.items() if len(ids) > 1]
    return {u: next(iter(ids)) for u, ids in seen.items() if len(ids) == 1}, conflicts


def load_facts(archive_root: Path, games: pd.DataFrame) -> dict[str, GameFacts]:
    goals = read_kind(archive_root, "player_events/goals")
    players = read_kind(archive_root, "player_events/players")
    goalies = read_kind(archive_root, "player_events/goalies")
    for df in (goals, players, goalies):
        if len(df):
            df["game_id"] = df["game_id"].astype(str)
    gg = {k: v for k, v in goals.groupby("game_id")} if len(goals) else {}
    pp = {k: v for k, v in players.groupby("game_id")} if len(players) else {}
    ge = {k: v for k, v in goalies.groupby("game_id")} if len(goalies) else {}
    out: dict[str, GameFacts] = {}
    for r in games.to_dict("records"):
        gid = str(r["game_id"])
        have = gid in pp and gid in ge
        g = gg.get(gid)
        out[gid] = GameFacts(
            game_id=gid, home_id=int(r["home_team_id"]), away_id=int(r["away_team_id"]), is_final=bool(r["is_final"]),
            home_final=_i(r.get("home_final")), away_final=_i(r.get("away_final")), home_reg=_i(r.get("home_reg")),
            away_reg=_i(r.get("away_reg")), last_period_type=r.get("last_period_type") if isinstance(r.get("last_period_type"), str) else None,
            goals=[{"period": int(x.period), "t_s": float(x.t_s), "team_id": int(x.team_id), "scorer_id": int(x.scorer_id)}
                   for x in g.itertuples()] if g is not None else [],
            skaters=pp[gid][["player_id", "team_id", "name", "sweater", "goals", "assists", "points", "toi_s"]].to_dict("records") if gid in pp else [],
            goalies=ge[gid][["player_id", "team_id", "name", "sweater", "saves", "toi_s"]].to_dict("records") if gid in ge else [],
            have_player_events=have,
        )
    return out


def _i(v: Any) -> int | None:
    try:
        return None if v is None or v != v else int(v)
    except (TypeError, ValueError):
        return None


def build_contract_master(market_static: pd.DataFrame, games: pd.DataFrame) -> tuple[pd.DataFrame, list[ContractSpec], dict[str, Any]]:
    specs = [build_spec(r) for r in market_static.to_dict("records")]
    key = {(g["game_date_et"], frozenset((int(g["home_team_id"]), int(g["away_team_id"])))): str(g["game_id"]) for g in games.to_dict("records")}
    keys_multi = pd.Series(list(key.keys())).duplicated().sum()
    rows = []
    for s in specs:
        d = s.as_dict()
        gid = key.get((s.game_date, frozenset(s.team_ids))) if s.team_ids and s.game_date else None
        d["game_id"] = gid
        rows.append(d)
    cm = pd.DataFrame(rows)
    uu, conflicts = team_uuid_map(specs)
    cm["player_team_id"] = [uu.get(t) if k in ("player_stat", "first_goal") else None for t, k in zip(cm["team_uuid"], cm["kind"])]
    meta = {"n_specs": len(specs), "n_joined_to_schedule_game": int(cm["game_id"].notna().sum()), "n_uuid_teams": len(uu),
            "uuid_conflicts": conflicts, "duplicate_game_keys": int(keys_multi)}
    return cm, specs, meta


def resolve_all(cm: pd.DataFrame, specs: list[ContractSpec], facts: dict[str, GameFacts]) -> pd.DataFrame:
    by_ticker = {s.ticker: s for s in specs}
    out = []
    for r in cm.to_dict("records"):
        gid = r["game_id"]
        f = facts.get(gid) if gid else None
        s = by_ticker[r["ticker"]]
        ptid = r.get("player_team_id")
        res = resolve(s, f, int(ptid) if ptid == ptid and ptid is not None else None)
        out.append({"ticker": r["ticker"], "game_id": gid, "outcome": res.outcome, "value": res.value, "reason": res.reason})
    return pd.DataFrame(out)
