"""Game table: one row per NHL game_id, built from archived schedule snapshots and archived finals.

Independent-game accounting lives here. A game's start time is the LATEST value any pre-start schedule snapshot gave
for it (postponed/rescheduled games are flagged with ``start_changed``), and finals come only from the archived
``results`` kind (official boxscore, regulation/OT/SO split).
"""

from __future__ import annotations

import gzip
import json
from pathlib import Path
from typing import Any

import pandas as pd


def read_kind(archive_root: Path, kind: str) -> pd.DataFrame:
    """All rows of a ledger kind, with the source file attached (lineage)."""
    rows: list[dict[str, Any]] = []
    base = Path(archive_root) / kind
    for f in sorted(base.glob("dt=*/*.jsonl.gz")):
        rel = str(f.relative_to(archive_root))
        with gzip.open(f, "rt", encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    r = json.loads(line)
                    r["_file"] = rel
                    rows.append(r)
    return pd.DataFrame(rows)


def build_games(archive_root: Path) -> pd.DataFrame:
    sched = read_kind(archive_root, "context/schedule")
    sched["game_id"] = sched["game_id"].astype(str)
    sched["_obs"] = pd.to_datetime(sched["_observed_at_utc"], utc=True)
    sched["_start"] = pd.to_datetime(sched["start_time_utc"], utc=True)
    sched = sched.sort_values("_obs")
    g = sched.groupby("game_id")
    latest = g.tail(1).set_index("game_id")
    out = pd.DataFrame(
        {
            "game_date_et": latest["game_date_et"],
            "home_team_id": latest["home_team_id"],
            "away_team_id": latest["away_team_id"],
            "home_abbrev": latest["home_abbrev"],
            "away_abbrev": latest["away_abbrev"],
            "season_type": latest["season_type"],
            "start_time_utc": latest["_start"],
            "n_schedule_snapshots": g.size(),
            "first_schedule_seen": g["_obs"].min(),
            "n_distinct_starts": g["_start"].nunique(),
            "first_start_seen": g["_start"].first(),
        }
    )
    out["start_changed"] = out["n_distinct_starts"] > 1
    res = read_kind(archive_root, "results")
    res["game_id"] = res["game_id"].astype(str)
    res = res.sort_values("_observed_at_utc").groupby("game_id").tail(1).set_index("game_id")
    keep = ["status", "home_final", "away_final", "home_reg", "away_reg", "last_period_type", "home_starting_goalie_id",
            "away_starting_goalie_id", "fetched_at_utc", "_file"]
    out = out.join(res[keep].rename(columns={"status": "final_status", "_file": "result_file"}), how="left")
    out["is_final"] = out["final_status"].eq("final")
    return out.reset_index()
