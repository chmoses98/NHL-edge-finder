"""Descriptive 2026-27 starting-goalie confirmation check from the data-archive branch (RESEARCH_ONLY, read-only).

Reads, via ``git show`` (no checkout), the archived ``context/goalie_observations`` (DailyFaceoff status with
``observed_at_utc``), ``context/schedule`` (``start_time_utc``) and ``player_events/goalies`` (official boxscore goalie
lines ingested after the game). For every team-game with a pregame observation (observed strictly before puck drop):
the LAST pregame status and whether the named goalie was the actual starter (the goalie with the most ice time; the
live ``starter`` flag is not used because it is unreliable in early fetches). Names are matched on team + last name.
Also reports, for actual starters, saves and shots against split by the last pregame status. Tiny sample: descriptive.

Run: ``python scripts/research_starter_confirmation.py --ref origin/data-archive --out result.json``
"""

from __future__ import annotations

import argparse
import gzip
import json
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime


def _git(*args: str) -> bytes:
    return subprocess.run(["git", *args], capture_output=True, check=True).stdout


def _rows(ref: str, prefix: str) -> list[dict]:
    names = [n for n in _git("ls-tree", "-r", "--name-only", ref).decode().splitlines() if n.startswith(prefix)]
    out = []
    for n in names:
        raw = _git("show", f"{ref}:{n}")
        try:
            txt = gzip.decompress(raw).decode()
        except OSError:
            txt = raw.decode()
        out.extend(json.loads(x) for x in txt.splitlines() if x.strip())
    return out


def _last(name: str | None) -> str:
    s = unicodedata.normalize("NFKD", str(name or "")).encode("ascii", "ignore").decode().lower().strip()
    return s.replace(".", " ").split()[-1] if s else ""


def _t(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="origin/data-archive")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    obs = _rows(a.ref, "context/goalie_observations/")
    sched = {}
    for r in _rows(a.ref, "context/schedule/"):
        sched[str(r["game_id"])] = r
    gl = _rows(a.ref, "player_events/goalies/")
    played: dict[tuple[str, int], dict] = {}
    for r in gl:
        k = (str(r["game_id"]), int(r["team_id"]))
        if (r.get("toi_s") or 0) > (played.get(k, {}).get("toi_s") or 0):
            played[k] = r
    by = defaultdict(list)
    for o in obs:
        if o.get("source") == "nhl_api_boxscore" or o.get("team_id") is None:
            continue
        by[(str(o["game_id"]), int(o["team_id"]))].append(o)
    last_acc: dict[str, Counter] = defaultdict(Counter)
    saves_by: dict[str, list[tuple[int, int]]] = defaultdict(list)
    n_tg = 0
    for k, starter in played.items():
        s = sched.get(k[0])
        if not s or not s.get("start_time_utc"):
            continue
        t0 = _t(s["start_time_utc"])
        pre = sorted((o for o in by.get(k, []) if _t(o.get("observed_at_utc") or o["_observed_at_utc"]) < t0),
                     key=lambda o: o.get("observed_at_utc") or o["_observed_at_utc"])
        if not pre:
            continue
        n_tg += 1
        last = pre[-1]
        st = last.get("status") or "UNKNOWN"
        hit = _last(last.get("player_name")) == _last(starter.get("name")) and _last(starter.get("name")) != ""
        last_acc[st]["correct" if hit else "wrong"] += 1
        if hit:
            saves_by[st].append((int(starter.get("saves") or 0), int(starter.get("shots_against") or 0)))
    res = {"n_team_games_with_played_goalie": len(played), "n_team_games_with_pregame_observation": n_tg,
           "last_pregame_status_accuracy": {k: {"n": sum(c.values()), "correct": c["correct"],
                                                "accuracy": c["correct"] / sum(c.values()) if sum(c.values()) else None} for k, c in last_acc.items()},
           "named_and_started_saves": {k: {"n": len(v), "mean_saves": sum(x for x, _ in v) / len(v), "mean_shots_against": sum(y for _, y in v) / len(v)}
                                       for k, v in saves_by.items() if v},
           "note": "prospective 2026-27 sample from the data-archive branch; descriptive only, far too small for model comparison"}
    txt = json.dumps(res, indent=1)
    print(txt)
    if a.out:
        with open(a.out, "w") as f:
            f.write(txt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
