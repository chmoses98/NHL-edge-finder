"""Prospective goalie-status measurement from the immutable archive (RESEARCH_ONLY; reads, never writes the archive).

For every settled game (``results`` rows carry the boxscore starters) and each team:

* the PREGAME observation history (``context/goalie_observations`` observed strictly before puck drop; name-only
  observations resolved to NHL ids with the same roster / stats lookup the simulator uses);
* whether the named goalie at each status (PROJECTED / PROBABLE / CONFIRMED) was the actual starter, overall and for
  the LAST pregame observation of each team-game;
* transitions: PROJECTED -> CONFIRMED on the same goalie vs a different goalie (a projection that was overturned);
* probability movement: the change in DATA_ONLY_V1 and DATA_ONLY_V2 P(home win) between the last prediction before a
  side's first CONFIRMED observation and the first prediction after it, and whether it moved toward the result.

Run: ``python -m nhl_edge.research.goalie_status_eval --archive data/archive`` (on a checkout of data-archive).
"""

from __future__ import annotations

import argparse
import gzip
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from nhl_edge.archive.ledger import Ledger, entry_observed_at
from nhl_edge.features.build import resolve_goalie_ids
from nhl_edge.timeutil import parse_iso

STATUSES = ("PROJECTED", "PROBABLE", "CONFIRMED")


def _rows(ledger: Ledger, kind: str) -> list[dict[str, Any]]:
    out = []
    for e in ledger.manifest():
        if e.kind != kind:
            continue
        with gzip.open(ledger.root / e.path, "rt", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    r.setdefault("_observed_at_utc", e.observed_at_utc or e.written_at_utc)
                    out.append(r)
    return out


def _latest(ledger: Ledger, kind: str) -> list[dict[str, Any]]:
    es = [e for e in ledger.manifest() if e.kind == kind]
    if not es:
        return []
    e = max(es, key=entry_observed_at)
    with gzip.open(ledger.root / e.path, "rt", encoding="utf-8") as f:
        return [json.loads(x) for x in f if x.strip()]


def evaluate(archive: Path) -> dict[str, Any]:
    ledger = Ledger(Path(archive), run_id="goalie-status-eval")
    results = {str(r["game_id"]): r for r in _rows(ledger, "results")}
    sched = {str(g["game_id"]): g for g in _latest(ledger, "context/schedule")}
    obs = resolve_goalie_ids(_rows(ledger, "context/goalie_observations"), _latest(ledger, "context/rosters"), _latest(ledger, "context/goalie_stats"))
    by_tg: dict[tuple[str, int], list[dict[str, Any]]] = defaultdict(list)
    for o in obs:
        by_tg[(str(o.get("game_id")), int(o.get("team_id") or 0))].append(o)
    acc: dict[str, Counter] = {s: Counter() for s in STATUSES}
    last_acc: dict[str, Counter] = {s: Counter() for s in STATUSES}
    transitions: Counter = Counter()
    confirm_times: dict[tuple[str, int], str] = {}
    team_games = 0
    for gid, res in results.items():
        start = (sched.get(gid) or {}).get("start_time_utc") or res.get("start_time_utc")
        if not start:
            continue
        t0 = parse_iso(start)
        for side in ("home", "away"):
            tid = res.get(f"{side}_team_id")
            actual = res.get(f"{side}_starting_goalie_id")
            if tid is None or actual is None:
                continue
            pre = sorted((o for o in by_tg.get((gid, int(tid)), []) if parse_iso(o["_observed_at_utc"]) < t0 and o.get("source") != "nhl_api_boxscore"),
                         key=lambda o: o["_observed_at_utc"])
            if not pre:
                continue
            team_games += 1
            for o in pre:
                st = o.get("status")
                if st in acc and o.get("player_id") is not None:
                    acc[st]["correct" if int(o["player_id"]) == int(actual) else "wrong"] += 1
            last = pre[-1]
            if last.get("status") in last_acc and last.get("player_id") is not None:
                last_acc[last["status"]]["correct" if int(last["player_id"]) == int(actual) else "wrong"] += 1
            proj = [o for o in pre if o.get("status") in ("PROJECTED", "PROBABLE") and o.get("player_id") is not None]
            conf = [o for o in pre if o.get("status") == "CONFIRMED" and o.get("player_id") is not None]
            if proj and conf:
                transitions["same_goalie" if int(proj[-1]["player_id"]) == int(conf[0]["player_id"]) else "projection_overturned"] += 1
            elif proj:
                transitions["never_confirmed_pregame"] += 1
            if conf:
                confirm_times[(gid, int(tid))] = conf[0]["_observed_at_utc"]
    movement = _movement(ledger, results, confirm_times)
    rate = {s: {"n": sum(c.values()), "accuracy": (c["correct"] / sum(c.values())) if sum(c.values()) else None} for s, c in acc.items()}
    last_rate = {s: {"n": sum(c.values()), "accuracy": (c["correct"] / sum(c.values())) if sum(c.values()) else None} for s, c in last_acc.items()}
    return {"n_settled_games": len(results), "n_team_games_with_pregame_obs": team_games, "accuracy_all_observations": rate,
            "accuracy_last_pregame_observation": last_rate, "transitions": dict(transitions), "probability_movement_on_confirmation": movement,
            "note": "prospective; tiny samples early in the season"}


def _movement(ledger: Ledger, results: dict[str, dict[str, Any]], confirm_times: dict[tuple[str, int], str]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for kind, pcol in (("predictions", "p_data_only"), ("predictions_v2", "p_data_only_v2")):
        rows = [r for r in _rows(ledger, kind) if r.get("family") == "game_winner" and r.get(pcol) is not None]
        series: dict[tuple[str, int], list[tuple[str, float]]] = defaultdict(list)
        for r in rows:
            series[(str(r["game_id"]), int(r.get("team_id") or 0))].append((r["predicted_at_utc"], float(r[pcol])))
        moves, toward = [], 0
        for (gid, tid), ct in confirm_times.items():
            res = results.get(gid)
            if not res:
                continue
            hf, af = res.get("home_final"), res.get("away_final")
            if hf is None or af is None:
                continue
            won = (hf > af) if res.get("home_team_id") == tid else (af > hf)
            s = sorted(series.get((gid, tid), []))
            before = [p for t, p in s if t < ct]
            after = [p for t, p in s if t >= ct]
            if before and after:
                d = after[0] - before[-1]
                moves.append(abs(d))
                toward += int((d > 0) == bool(won)) if d != 0 else 0
        out[kind] = {"n": len(moves), "mean_abs_move": (sum(moves) / len(moves)) if moves else None, "moved_toward_result": toward}
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.goalie_status_eval")
    ap.add_argument("--archive", default="data/archive")
    a = ap.parse_args(argv)
    print(json.dumps(evaluate(Path(a.archive)), indent=1, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
