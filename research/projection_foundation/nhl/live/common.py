"""Shared helpers for the NHL live pipeline: archive readers (data-archive context kinds), ET dates, team identity."""
from __future__ import annotations

import glob
import gzip
import json
import os
import re
import unicodedata
from datetime import datetime, timedelta, timezone
from functools import lru_cache
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from nhl import data

SPORT = "NHL"
ET = ZoneInfo("America/New_York")
_TS_RE = re.compile(r"_(\d{8}T\d{6}Z)_")


def parse_ts(x) -> datetime | None:
    if x is None or (isinstance(x, float) and x != x):
        return None
    try:
        d = datetime.fromisoformat(str(x).replace("Z", "+00:00"))
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def iso(d: datetime) -> str:
    return d.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def now_utc(now: str | None = None) -> datetime:
    return parse_ts(now) if now else datetime.now(timezone.utc).replace(microsecond=0)


def et_date(d: datetime) -> str:
    return d.astimezone(ET).strftime("%Y-%m-%d")


def file_ts(path: str) -> datetime | None:
    """Capture time encoded in a data-archive file name (context_lines_20261016T003424Z_<run>.jsonl.gz)."""
    m = _TS_RE.search(os.path.basename(path))
    return datetime.strptime(m.group(1), "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc) if m else None


def archive_files(archive: str | Path, kind: str, since: datetime | None = None, until: datetime | None = None) -> list[str]:
    """Files of one data-archive kind whose capture time is within [since, until] (by file name, then dt= directory)."""
    out = []
    for f in sorted(glob.glob(str(Path(archive) / kind / "dt=*" / "*.jsonl.gz"))):
        t = file_ts(f)
        if t is None:
            continue
        if since is not None and t < since:
            continue
        if until is not None and t > until:
            continue
        out.append(f)
    return out


def read_kind(archive: str | Path, kind: str, since: datetime | None = None, until: datetime | None = None) -> pd.DataFrame:
    parts = []
    for f in archive_files(archive, kind, since, until):
        with gzip.open(f, "rt") as fh:
            rows = [json.loads(x) for x in fh if x.strip()]
        if rows:
            parts.append(pd.DataFrame(rows))
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()


@lru_cache(maxsize=1)
def teams() -> pd.DataFrame:
    return pd.read_csv(data.ROOT / "data" / "identity" / "teams.csv")


def abbrev_by_id() -> dict[int, str]:
    t = teams()
    return dict(zip(t["team_id"].astype(int), t["abbrev"]))


def team_name_by_abbrev() -> dict[str, str]:
    t = teams()
    return dict(zip(t["abbrev"], t["name"]))


def fold(s) -> str:
    s = unicodedata.normalize("NFKD", str(s or ""))
    return re.sub(r"[^a-z]", "", "".join(ch for ch in s if not unicodedata.combining(ch)).lower())


def last_name(name) -> str:
    parts = str(name or "").replace(".", ". ").split()
    return fold(parts[-1]) if parts else ""


def first_initial(name) -> str:
    parts = str(name or "").split()
    return fold(parts[0])[:1] if parts else ""


def schedule_asof(archive: str | Path, now: datetime, back_days: int = 4) -> pd.DataFrame:
    """Newest schedule snapshot per game observed at or before `now` (regular season, NHL game ids)."""
    s = read_kind(archive, "context/schedule", since=now - timedelta(days=back_days), until=now)
    if s.empty:
        return s
    for c in ("game_id", "home_team_id", "away_team_id"):
        s[c] = pd.to_numeric(s[c], errors="coerce")
    s = s.dropna(subset=["game_id"]).copy()
    s["game_id"] = s["game_id"].astype("int64")
    s = s.sort_values("_observed_at_utc").drop_duplicates("game_id", keep="last")
    s["start"] = pd.to_datetime(s["start_time_utc"], utc=True)
    return s.reset_index(drop=True)


def is_regular(game_id: int) -> bool:
    return int(game_id) // 10000 % 100 == 2


def write_json_once(path: str, obj) -> str:
    """Write a JSON file that must not exist yet (run summaries are write-once)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "x") as f:
        json.dump(obj, f, indent=1, sort_keys=True, default=str)
    return path
