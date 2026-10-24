"""Pregame forecast delivery monitor: alert on forecasts that are actually missing or stale, never on values that merely did not change (RESEARCH_ONLY, read-only).

The projection-foundation archive writes a forecast row only when its content changed, so "no new forecast row for hours" is normal when nothing changed. What matters
before a puck drop is therefore:

* ``MISSING``       no pregame forecast row exists at all for the game (archived at or before ``now``),
* ``STALE_EVAL``    the newest projection run that *evaluated* the game (its ``runs/…_project.json``) is older than ``STALE_EVAL_MIN`` -- whether or not it changed a value,
* ``STALE_LINEUP``  the lineup capture that evaluation used was older than ``STALE_LINEUP_MIN`` when it ran,
* ``OK``            otherwise.

Only games starting within ``WATCH_WITHIN_MIN`` of ``now`` are judged. The same module records, per judged game, the numbers needed to track request-to-publication latency,
lineup freshness and fallback behaviour over time (the evaluation age, the lineup age, the age of the newest forecast row and whether the previous snapshot is what is
being served), so they can be summarised across slates.

    python -m nhl_edge.research.delivery_monitor --pf <projection-data checkout> --schedule <context/schedule file...> [--now ISO] [--out report.json]
"""

from __future__ import annotations

import argparse
import gzip
import json
import sys
from dataclasses import asdict, dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

WATCH_WITHIN_MIN = 90.0
STALE_EVAL_MIN = 120.0
STALE_LINEUP_MIN = 60.0


def _dt(s: Any) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00")).astimezone(UTC)
    except ValueError:
        return None


@dataclass(frozen=True)
class GameStatus:
    game_id: str
    start_utc: str
    minutes_to_start: float
    status: str                          # OK | MISSING | STALE_EVAL | STALE_LINEUP
    n_pregame_rows: int
    newest_row_age_min: float | None
    last_eval_age_min: float | None
    lineup_age_at_eval_min: float | None
    reason: str = ""


def read_forecast_index(pf: Path, now: datetime, days: int = 2) -> dict[str, dict[str, Any]]:
    """game_id -> {n_pregame, newest_archived}. Forecast partitions are keyed by the UTC date of the game's START (not of the archive instant), so the games that matter
    now live in yesterday's, today's and the next days' folders."""
    idx: dict[str, dict[str, Any]] = {}
    for k in range(-1, days + 1):
        day = (now + timedelta(days=k)).strftime("%Y-%m-%d")
        for p in sorted((Path(pf) / "forecasts" / "nhl" / day).glob("*.jsonl.gz")) if (Path(pf) / "forecasts" / "nhl" / day).exists() else []:
            try:
                with gzip.open(p, "rt", encoding="utf-8") as f:
                    for line in f:
                        if not line.strip():
                            continue
                        r = json.loads(line)
                        arch, start = _dt(r.get("archived_utc")), _dt(r.get("game_start_utc"))
                        if arch is None or start is None or arch > now or arch > start:
                            continue
                        e = idx.setdefault(str(r.get("game_id")), {"n_pregame": 0, "newest_archived": arch})
                        e["n_pregame"] += 1
                        e["newest_archived"] = max(e["newest_archived"], arch)
            except (OSError, ValueError):
                continue
    return idx


def read_run_index(pf: Path, now: datetime, days: int = 2) -> dict[str, dict[str, Any]]:
    """game_id -> {evaluated_at, lineup_age_min} from the newest projection run that evaluated the game (run partitions are keyed by the run's own UTC date)."""
    idx: dict[str, dict[str, Any]] = {}
    for k in range(days + 1):
        day = (now - timedelta(days=k)).strftime("%Y-%m-%d")
        d = Path(pf) / "runs" / "nhl" / day
        for p in sorted(d.glob("*_project.json")) if d.exists() else []:
            try:
                r = json.loads(p.read_text())
            except (OSError, ValueError):
                continue
            at = _dt(r.get("archived_at"))
            if at is None or at > now:
                continue
            for gid, ev in ((r.get("coverage") or {}).get("events") or {}).items():
                age = ev.get("newest_age_minutes") if isinstance(ev, dict) else None
                cur = idx.get(str(gid))
                if cur is None or at > cur["evaluated_at"]:
                    idx[str(gid)] = {"evaluated_at": at, "lineup_age_min": None if age is None else float(age)}
    return idx


def judge(now: datetime, games: list[dict[str, Any]], forecasts: dict[str, dict[str, Any]], runs: dict[str, dict[str, Any]]) -> list[GameStatus]:
    out: list[GameStatus] = []
    for g in games:
        if str(g.get("season_type", "regular")).lower() not in ("regular", "2", "playoffs", "playoff", "3") or g.get("status") not in ("not_started", None):
            continue
        start = _dt(g.get("start_time_utc"))
        if start is None:
            continue
        mins = (start - now).total_seconds() / 60.0
        if not 0 < mins <= WATCH_WITHIN_MIN:
            continue
        gid = str(g["game_id"])
        f, r = forecasts.get(gid), runs.get(gid)
        row_age = None if f is None else (now - f["newest_archived"]).total_seconds() / 60
        eval_age = None if r is None else (now - r["evaluated_at"]).total_seconds() / 60
        lin = None if r is None else r["lineup_age_min"]
        if f is None:
            st, why = "MISSING", "no pregame forecast row exists for this game"
        elif eval_age is None or eval_age > STALE_EVAL_MIN:
            st, why = "STALE_EVAL", f"newest projection run that evaluated the game is {'absent' if eval_age is None else f'{eval_age:.0f} min old'} (limit {STALE_EVAL_MIN:.0f})"
        elif lin is not None and lin > STALE_LINEUP_MIN:
            st, why = "STALE_LINEUP", f"the lineup capture used was {lin:.0f} min old when it ran (limit {STALE_LINEUP_MIN:.0f})"
        else:
            st, why = "OK", ""
        out.append(GameStatus(gid, g["start_time_utc"], round(mins, 1), st, 0 if f is None else int(f["n_pregame"]), None if row_age is None else round(row_age, 1),
                              None if eval_age is None else round(eval_age, 1), None if lin is None else round(lin, 1), why))
    return sorted(out, key=lambda s: s.minutes_to_start)


def load_games(paths: list[Path]) -> list[dict[str, Any]]:
    by: dict[str, dict[str, Any]] = {}
    for p in paths:
        try:
            with (gzip.open(p, "rt") if str(p).endswith(".gz") else open(p)) as f:
                for line in f:
                    if line.strip():
                        try:
                            r = json.loads(line)
                            by[str(r["game_id"])] = r
                        except (ValueError, KeyError, TypeError):
                            continue
        except OSError:
            continue
    return list(by.values())


def report(now: datetime, games: list[dict[str, Any]], pf: Path) -> dict[str, Any]:
    st = judge(now, games, read_forecast_index(pf, now), read_run_index(pf, now))
    bad = [s for s in st if s.status != "OK"]
    return {"now_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "watch_within_min": WATCH_WITHIN_MIN, "games_judged": len(st), "problems": len(bad), "alert": bool(bad),
            "recovered": not bad, "statuses": [asdict(s) for s in st]}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.delivery_monitor")
    ap.add_argument("--pf", required=True)
    ap.add_argument("--schedule", nargs="+", required=True)
    ap.add_argument("--now", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--github-output", default=None)
    a = ap.parse_args(argv)
    now = _dt(a.now) if a.now else datetime.now(UTC)
    rep = report(now, load_games([Path(p) for p in a.schedule]), Path(a.pf))
    print(json.dumps(rep, indent=1))
    if a.out:
        Path(a.out).write_text(json.dumps(rep, indent=1))
    if a.github_output:
        with open(a.github_output, "a") as f:
            f.write(f"fc_alert={'true' if rep['alert'] else 'false'}\nfc_recovered={'true' if rep['recovered'] else 'false'}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
