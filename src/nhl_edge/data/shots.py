"""MoneyPuck shot-level data -> slim Parquet (research input for nhl-features-2.0 / nhl-sim-2.0).

One row per unblocked/blocked shot attempt, with the game state at the moment of the attempt. From these rows the
V2 research code derives, without any further network access:

* goalie game logs (who faced each shot; xG faced vs goals allowed; the starter = goalie facing the team's first shot);
* goal events with period, game clock, score state, manpower and empty-net flags (score-state / goalie-pull
  hazards, period scoring shape);
* xG by score state (score effects).

Source: ``https://peter-tanner.com/moneypuck/downloads/shots_{season}.zip`` (MoneyPuck's own mirror; the
``moneypuck.com/data/shots`` path 404s, see docs/NHL_DATA_SOURCE_AUDIT.md). ``season`` is MoneyPuck's start year.
Only the columns below are kept (missing ones are recorded in the manifest, never invented). MoneyPuck ``game_id``
is the 5/6-digit in-season number; the NHL id is ``season * 1_000_000 + game_id``.
"""

from __future__ import annotations

import argparse
import io
import json
import sys
import zipfile
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.data.http import FetchError, fetch
from nhl_edge.log import get_logger, kv
from nhl_edge.timeutil import iso, utcnow

log = get_logger(__name__)

URLS = ("https://peter-tanner.com/moneypuck/downloads/shots_{season}.zip", "https://moneypuck.com/moneypuck/data/shots/shots_{season}.zip")
KEEP = ("season", "game_id", "isPlayoffGame", "homeTeamCode", "awayTeamCode", "teamCode", "isHomeTeam", "period", "time", "event", "goal",
        "xGoal", "shotWasOnGoal", "shotOnEmptyNet", "homeTeamGoals", "awayTeamGoals", "homeSkatersOnIce", "awaySkatersOnIce",
        "homeEmptyNet", "awayEmptyNet", "goalieIdForShot", "goalieNameForShot", "shooterPlayerId", "shotID")
FLOAT32 = ("xGoal", "time")
INT_COLS = ("season", "game_id", "isPlayoffGame", "isHomeTeam", "period", "goal", "shotWasOnGoal", "shotOnEmptyNet", "homeTeamGoals",
            "awayTeamGoals", "homeSkatersOnIce", "awaySkatersOnIce", "homeEmptyNet", "awayEmptyNet")


def slim(df: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    missing = [c for c in KEEP if c not in df.columns]
    d = df[[c for c in KEEP if c in df.columns]].copy()
    for c in INT_COLS:
        if c in d.columns:
            d[c] = pd.to_numeric(d[c], errors="coerce").fillna(-1).astype(np.int32)
    for c in FLOAT32:
        if c in d.columns:
            d[c] = pd.to_numeric(d[c], errors="coerce").astype(np.float32)
    for c in ("goalieIdForShot", "shooterPlayerId", "shotID"):
        if c in d.columns:
            d[c] = pd.to_numeric(d[c], errors="coerce").fillna(0).astype(np.int64)
    for c in ("homeTeamCode", "awayTeamCode", "teamCode", "event", "goalieNameForShot"):
        if c in d.columns:
            d[c] = d[c].astype("category")
    if "season" in d.columns and "game_id" in d.columns:
        d["nhl_game_id"] = (d["season"].astype(np.int64) * 1_000_000 + d["game_id"].astype(np.int64)).astype(np.int64)
    return d, missing


def read_zip_csv(blob: bytes) -> pd.DataFrame:
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        names = [n for n in z.namelist() if n.lower().endswith(".csv")]
        if not names:
            raise ValueError("zip has no csv")
        with z.open(names[0]) as f:
            header = pd.read_csv(f, nrows=0).columns
        with z.open(names[0]) as f:
            return pd.read_csv(f, usecols=[c for c in KEEP if c in header], low_memory=False)


def pull_season(season: int, out_dir: Path) -> dict[str, Any]:
    errs = []
    for tmpl in URLS:
        url = tmpl.format(season=season)
        try:
            f = fetch(url, ttl_s=0, timeout=600, max_retries=2)
            df = read_zip_csv(f.content)
        except (FetchError, ValueError, zipfile.BadZipFile, OSError) as e:
            errs.append(f"{url}: {str(e)[:200]}")
            continue
        d, missing = slim(df)
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"shots_{season}.parquet"
        d.to_parquet(path, index=False, compression="zstd")
        return {"season": season, "url": url, "rows": int(len(d)), "games": int(d["nhl_game_id"].nunique()) if "nhl_game_id" in d else None,
                "goals": int((d["goal"] == 1).sum()) if "goal" in d else None, "missing_columns": missing, "file": path.name,
                "bytes_on_disk": path.stat().st_size, "retrieved_at_utc": iso(utcnow()), "sha256": getattr(f, "sha256", None)}
    return {"season": season, "error": errs}


def load_shots(history_root: Path, seasons: list[int] | None = None) -> pd.DataFrame:
    root = Path(history_root) / "moneypuck"
    frames = []
    for p in sorted(root.glob("shots_*.parquet")):
        s = int(p.stem.split("_")[1])
        if seasons is None or s in seasons:
            frames.append(pd.read_parquet(p))
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.data.shots")
    ap.add_argument("--out", default="data/history")
    ap.add_argument("--seasons", default="2021,2022,2023,2024,2025")
    a = ap.parse_args(argv)
    out = Path(a.out) / "moneypuck"
    reps = []
    for s in [int(x) for x in a.seasons.split(",") if x.strip()]:
        rep = pull_season(s, out)
        log.info(kv(event="shots_season", **{k: v for k, v in rep.items() if k != "missing_columns"}))
        reps.append(rep)
    man_path = Path(a.out) / "SHOTS_MANIFEST.json"
    man_path.write_text(json.dumps({"pulled_at_utc": iso(utcnow()), "seasons": reps, "columns_kept": list(KEEP)}, indent=1, default=str))
    print(json.dumps(reps, indent=1, default=str))
    return 0 if any("error" not in r for r in reps) else 1


if __name__ == "__main__":
    sys.exit(main())
