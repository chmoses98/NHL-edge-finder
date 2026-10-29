"""Goalie-status change log (PROPOSAL, NOT WIRED into any job; RESEARCH_ONLY).

Purpose: record, for every goalie fact, WHEN it first appeared at the source (``source_reported_at_utc``) and WHEN we first saw it, at the cadence of
whatever calls ``watch_once`` (the intent is a conditional poll inside the existing capture-worker cycle during the pregame window, not a new cron).
It stores only CHANGES (an append-only event log) plus a tiny state file, so it costs one GET per poll and a few KB per day.

Nothing here changes the existing ``context/goalie_observations`` capture, any model, any stake or any recommendation. See
``docs/research/nhl-model-improvement/INFORMATION_EVENT_ASSESSMENT.md`` (branch ``claude/nhl-model-improvement-f6kn0k``) for why it is needed.
"""

from __future__ import annotations

import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from nhl_edge.schemas.core import GoalieObservation

EVENT_VERSION = "goalie-events-1.0"


def _key(o: GoalieObservation) -> str:
    return f"{o.game_id}:{o.team_id}"


def _snap(o: GoalieObservation) -> dict[str, Any]:
    return {"player_id": o.player_id, "player_name": o.player_name, "status": str(getattr(o.status, "value", o.status)),
            "source_reported_at_utc": o.source_reported_at_utc.isoformat() if o.source_reported_at_utc else None}


def diff_goalie_state(prev: dict[str, dict[str, Any]], current: Iterable[GoalieObservation]) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    """Events for every (game, team) whose goalie name or status changed since ``prev``; returns (events, new_state).

    ``kind`` is FIRST_SEEN, STATUS_CHANGE (same goalie, new status), GOALIE_CHANGE (a different goalie named) or CONFIRMED (status reaches CONFIRMED).
    ``latency_min`` = first_seen - source_reported when the source supplied a time, else None (never invented).
    """
    events: list[dict[str, Any]] = []
    state = dict(prev)
    for o in current:
        k, s = _key(o), _snap(o)
        old = prev.get(k)
        if old is not None and old["player_name"] == s["player_name"] and old["status"] == s["status"]:
            continue
        if old is None:
            kind = "FIRST_SEEN"
        elif old["player_name"] != s["player_name"]:
            kind = "GOALIE_CHANGE"
        else:
            kind = "STATUS_CHANGE"
        if s["status"] == "CONFIRMED" and (old is None or old["status"] != "CONFIRMED"):
            kind = "CONFIRMED" if kind != "GOALIE_CHANGE" else "GOALIE_CHANGE"
        lat = None
        if o.source_reported_at_utc is not None:
            lat = round((o.observed_at_utc - o.source_reported_at_utc).total_seconds() / 60.0, 2)
        events.append({"version": EVENT_VERSION, "game_id": o.game_id, "team_id": o.team_id, "kind": kind, "previous": old, "current": s, "first_seen_utc": o.observed_at_utc.isoformat(),
                       "latency_min": lat, "became_confirmed": s["status"] == "CONFIRMED" and (old is None or old["status"] != "CONFIRMED")})
        state[k] = s
    return events, state


def watch_once(date_et: str, state_path: Path, out_dir: Path) -> dict[str, Any]:
    """One poll: fetch the source, diff against the saved state, append events. Fail-soft: a failed fetch records nothing and changes no state."""
    from nhl_edge.data.goalies import fetch_dailyfaceoff

    obs, meta = fetch_dailyfaceoff(date_et)
    if not obs:
        return {"date": date_et, "events": 0, "error": meta.get("error")}
    prev = json.loads(state_path.read_text()) if state_path.exists() else {}
    events, state = diff_goalie_state(prev, [o for o in obs if o.source == "dailyfaceoff"])
    if events:
        out_dir.mkdir(parents=True, exist_ok=True)
        with (out_dir / f"goalie_events_{date_et}.jsonl").open("a") as fh:
            for e in events:
                e["response_sha256"] = meta.get("sha256")
                fh.write(json.dumps(e, sort_keys=True) + "\n")
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, sort_keys=True))
    return {"date": date_et, "events": len(events), "n_state": len(state)}
