"""Cheap conductor: decide which expensive jobs are worth running right now. Stdlib-only (no install needed).

Inputs: the NHL calendar (from the latest archived schedule snapshot; the api-web schedule feed publishes
``regularSeasonStartDate`` etc. and the snapshot carries every game in the next 8 days) and the ages of the
STATUS_*.json breadcrumbs. Output: key=value lines for ``$GITHUB_OUTPUT`` plus a JSON summary.

Rules (v1):
- capture:  every wake if a game starts within 36h; otherwise one daily futures snapshot (16:00 UTC)
- context:  every wake within 30h of a start when its own snapshot is older than 55 min; always when older than 6h in
            season / 24h otherwise; always when no schedule snapshot exists (bootstrap)
- simulate: if a not-started game starts within 26h and the last sim is older than 45 min (goalie news moves fast)
- settle:   if any game started in the last 36h and settlement is older than 90 min
- evaluate: after settlement, or daily at 10:00 UTC in season
- discover: age-based, once a day
"""

from __future__ import annotations

import gzip
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from nhl_edge.archive.ledger import Ledger
from nhl_edge.archive.status import status_age_minutes
from nhl_edge.timeutil import iso, parse_iso

# Announced NHL calendars (api-web /schedule feed, 2026-09-29: preSeasonStartDate 2026-09-19, regularSeasonStartDate
# 2026-09-29, regularSeasonEndDate 2027-04-10, playoffEndDate 2027-06-10). Add each new season as it is published.
SEASON_CALENDAR = {
    "2026-27": {"preseason_start": "2026-09-19", "regular_start": "2026-09-29", "regular_end": "2027-04-10", "playoffs_end": "2027-06-30"},
}
FALLBACK_SEASON_START_MONTH = 9
FALLBACK_SEASON_END_MONTH = 6


def season_window(today: str) -> tuple[bool, str | None, bool]:
    for label, cal in sorted(SEASON_CALENDAR.items()):
        if cal["preseason_start"] <= today <= cal["playoffs_end"]:
            return True, label, True
    last_known_end = max(cal["playoffs_end"] for cal in SEASON_CALENDAR.values())
    if today <= last_known_end:
        return False, None, True
    month = int(today[5:7])
    return (month >= FALLBACK_SEASON_START_MONTH or month <= FALLBACK_SEASON_END_MONTH), None, False


def _latest_schedule(ledger: Ledger) -> list[dict[str, Any]]:
    entry = ledger.latest("context/schedule")
    if not entry:
        return []
    rows = []
    with gzip.open(ledger.root / entry.path, "rt") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def decide(now: datetime, schedule_rows: list[dict[str, Any]], capture_age_min: float | None, last_sim_age_min: float | None,
           last_settle_age_min: float | None, last_eval_age_min: float | None, last_context_age_min: float | None = None,
           last_discover_age_min: float | None = None) -> dict[str, Any]:
    in_season, season_label, calendar_known = season_window(now.date().isoformat())
    starts = []
    for g in schedule_rows:
        try:
            starts.append((parse_iso(g["start_time_utc"]), g.get("status"), g.get("game_id")))
        except (KeyError, ValueError, TypeError):
            continue
    upcoming = [t for t, st, _ in starts if t > now and st in ("not_started", None)]
    recent_started = [t for t, st, _ in starts if now - timedelta(hours=36) <= t <= now and st not in ("postponed", "canceled")]
    next_h = (min(upcoming) - now).total_seconds() / 3600 if upcoming else None
    hour = now.hour
    active_window = 13 <= hour or hour <= 5  # UTC: 9am ET .. 1am ET (west-coast starts end ~05:30 UTC)
    daily_slot = hour == 16 and (capture_age_min is None or capture_age_min > 20 * 60)

    capture = (in_season and next_h is not None and next_h <= 36) or daily_slot
    context_stale_min = 6 * 60 if in_season else 24 * 60
    context = (
        (in_season and next_h is not None and next_h <= 30 and active_window and (last_context_age_min is None or last_context_age_min > 55))
        or last_context_age_min is None
        or last_context_age_min > context_stale_min
    )
    if not schedule_rows:
        context = True
    simulate = in_season and next_h is not None and next_h <= 26 and (last_sim_age_min is None or last_sim_age_min > 45)
    settle = bool(recent_started) and (last_settle_age_min is None or last_settle_age_min > 90)
    evaluate = settle or (in_season and hour == 10 and (last_eval_age_min is None or last_eval_age_min > 23 * 60))
    discover = last_discover_age_min is None or last_discover_age_min > 23 * 60
    return {
        "now_utc": iso(now), "in_season": in_season, "season": season_label, "calendar_known": calendar_known,
        "next_start_hours": None if next_h is None else round(next_h, 2), "n_upcoming": len(upcoming), "n_recent_started": len(recent_started),
        "capture": bool(capture), "context": bool(context), "simulate": bool(simulate), "settle": bool(settle), "evaluate": bool(evaluate), "discover": bool(discover),
        "capture_age_min": capture_age_min, "context_age_min": last_context_age_min, "sim_age_min": last_sim_age_min, "settle_age_min": last_settle_age_min,
        "discover_age_min": last_discover_age_min,
    }


def _discover_age(data_root: Path) -> float | None:
    ages = [status_age_minutes(root / "discovery_summary.json", "discovered_at") for root in (data_root / "archive" / "catalog", data_root / "catalog")]
    known = [a for a in ages if a is not None]
    return min(known) if known else None


# Writer/reader key pairs. A mistyped key means "age None" which means "run every wake": tests pin these.
STATUS_KEYS = {
    "capture": ("STATUS_capture.json", "last_capture_utc"), "simulate": ("STATUS_simulate.json", "simulated_at_utc"),
    "settle": ("STATUS_settle.json", "settled_at_utc"), "evaluate": ("STATUS_evaluate.json", "evaluated_at_utc"),
    "context": ("STATUS_context.json", "refreshed_at_utc"),
}


def decide_now(data_root: Path) -> dict[str, Any]:
    archive = data_root / "archive"
    ledger = Ledger(archive)
    rows = _latest_schedule(ledger) if archive.exists() else []
    age = lambda job: status_age_minutes(archive / STATUS_KEYS[job][0], STATUS_KEYS[job][1])  # noqa: E731
    return decide(datetime.now(tz=UTC), rows, age("capture"), age("simulate"), age("settle"), age("evaluate"), age("context"), _discover_age(data_root))


def run_conductor(data_root: Path, github_output: str | None = None) -> int:
    d = decide_now(data_root)
    print(json.dumps(d, indent=1))
    if github_output:
        with open(github_output, "a") as f:
            for k in ("capture", "context", "simulate", "settle", "evaluate", "discover", "in_season", "calendar_known"):
                f.write(f"{k}={'true' if d[k] else 'false'}\n")
    return 0


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="nhl-conductor", description=__doc__)
    ap.add_argument("--data", default="data", type=Path)
    ap.add_argument("--github-output", default=None)
    a = ap.parse_args(argv)
    return run_conductor(a.data, a.github_output)


if __name__ == "__main__":
    raise SystemExit(main())
