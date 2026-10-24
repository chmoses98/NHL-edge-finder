from __future__ import annotations

import gzip
import json
from datetime import UTC, datetime, timedelta

from nhl_edge.research import delivery_monitor as M

NOW = datetime(2026, 10, 24, 22, 30, tzinfo=UTC)


def _iso(t):
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


def _forecast(pf, day, name, rows):
    d = pf / "forecasts" / "nhl" / day
    d.mkdir(parents=True, exist_ok=True)
    with gzip.open(d / name, "wt") as f:
        f.write("\n".join(json.dumps(r) for r in rows) + "\n")


def _run(pf, day, name, at, ages):
    d = pf / "runs" / "nhl" / day
    d.mkdir(parents=True, exist_ok=True)
    (d / name).write_text(json.dumps({"archived_at": _iso(at), "coverage": {"events": {g: {"newest_age_minutes": a} for g, a in ages.items()}}}))


def _games(*specs):
    return [{"game_id": g, "season_type": "regular", "status": "not_started", "start_time_utc": _iso(NOW + timedelta(minutes=m))} for g, m in specs]


def test_unchanged_values_are_not_an_alert_but_a_missing_or_stale_evaluation_is(tmp_path):
    pf = tmp_path
    start = NOW + timedelta(minutes=45)
    # a forecast row written 4 hours ago and NOT rewritten since (nothing changed) ...
    _forecast(pf, "2026-10-24", "a.jsonl.gz", [{"game_id": "1", "archived_utc": _iso(NOW - timedelta(hours=4)), "game_start_utc": _iso(start)}])
    # ... but a run evaluated the game 20 minutes ago with a fresh lineup: that is OK, however old the row is
    _run(pf, "2026-10-24", "221000Z_project.json", NOW - timedelta(minutes=20), {"1": 8.0})
    g = _games(("1", 45))
    rep = M.report(NOW, g, pf)
    assert rep["alert"] is False and rep["statuses"][0]["status"] == "OK" and rep["statuses"][0]["newest_row_age_min"] == 240.0
    # the same game with no evaluation for 3 hours is stale even though a (still correct) row exists
    for p in (pf / "runs").rglob("*.json"):
        p.unlink()
    _run(pf, "2026-10-24", "192000Z_project.json", NOW - timedelta(hours=3), {"1": 8.0})
    rep = M.report(NOW, g, pf)
    assert rep["alert"] is True and rep["statuses"][0]["status"] == "STALE_EVAL"


def test_missing_forecast_and_stale_lineup_and_the_watch_window(tmp_path):
    pf = tmp_path
    soon, started = NOW + timedelta(minutes=30), NOW - timedelta(minutes=5)
    _forecast(pf, "2026-10-24", "a.jsonl.gz", [{"game_id": "2", "archived_utc": _iso(NOW - timedelta(hours=1)), "game_start_utc": _iso(soon)},
                                                {"game_id": "3", "archived_utc": _iso(NOW + timedelta(minutes=1)), "game_start_utc": _iso(soon)},                   # archived "in the future": ignored
                                                {"game_id": "4", "archived_utc": _iso(NOW - timedelta(hours=1)), "game_start_utc": _iso(NOW - timedelta(hours=2))}])  # archived after its own start: not pregame
    _run(pf, "2026-10-24", "220000Z_project.json", NOW - timedelta(minutes=30), {"2": 75.0, "3": 5.0})
    games = _games(("1", 30), ("2", 30), ("3", 30), ("4", 30), ("5", 300))
    games.append({"game_id": "6", "season_type": "regular", "status": "final", "start_time_utc": _iso(started)})
    got = {s.game_id: s.status for s in M.judge(NOW, games, M.read_forecast_index(pf, NOW), M.read_run_index(pf, NOW))}
    assert got == {"1": "MISSING", "2": "STALE_LINEUP", "3": "MISSING", "4": "MISSING"}          # game 5 is outside the 90-minute window, game 6 has started


def test_the_newest_run_wins_and_unreadable_files_are_skipped(tmp_path):
    pf = tmp_path
    _run(pf, "2026-10-24", "200000Z_project.json", NOW - timedelta(hours=2), {"1": 90.0})
    _run(pf, "2026-10-24", "222500Z_project.json", NOW - timedelta(minutes=5), {"1": 4.0})
    (pf / "runs" / "nhl" / "2026-10-24" / "bad_project.json").write_text("{not json")
    idx = M.read_run_index(pf, NOW)
    assert idx["1"]["lineup_age_min"] == 4.0
    assert M.read_forecast_index(tmp_path / "nowhere", NOW) == {}


def test_forecast_partitions_are_found_by_the_start_date_of_the_game(tmp_path):
    start = NOW + timedelta(minutes=60)                                  # 23:30Z on the 24th ... and a game starting at 00:30Z on the 25th lives in the 25th's folder
    nxt = datetime(2026, 10, 25, 0, 30, tzinfo=UTC)
    _forecast(tmp_path, "2026-10-25", "a.jsonl.gz", [{"game_id": "9", "archived_utc": _iso(NOW - timedelta(hours=2)), "game_start_utc": _iso(nxt)}])
    assert M.read_forecast_index(tmp_path, NOW)["9"]["n_pregame"] == 1 and start > NOW
