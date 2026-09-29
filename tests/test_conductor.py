from datetime import UTC, datetime, timedelta
from pathlib import Path

from nhl_edge.workflows import conductor as C

NOW = datetime(2026, 9, 29, 18, 0, tzinfo=UTC)


def rows(hours_ahead, status="not_started"):
    return [{"start_time_utc": (NOW + timedelta(hours=h)).isoformat().replace("+00:00", "Z"), "status": status, "game_id": str(i)} for i, h in enumerate(hours_ahead)]


def test_game_day_runs_everything():
    d = C.decide(NOW, rows([3, 5]), None, None, None, None, None, None)
    assert d["capture"] and d["context"] and d["simulate"] and d["discover"] and d["in_season"]


def test_recent_sim_and_capture_are_not_repeated():
    d = C.decide(NOW, rows([3]), 5, 10, 10, 10, 10, 10)
    assert d["capture"] and not d["simulate"] and not d["context"] and not d["discover"]


def test_settle_after_games_then_stops():
    d = C.decide(NOW, rows([-5, -4], status="final"), 5, 5, None, None, 5, 5)
    assert d["settle"] and d["evaluate"]
    assert not C.decide(NOW, rows([-5], status="final"), 5, 5, 30, 30, 5, 5)["settle"]


def test_postponed_games_do_not_trigger_settlement():
    assert not C.decide(NOW, rows([-5], status="postponed"), 5, 5, None, None, 5, 5)["settle"]


def test_bootstrap_without_schedule_forces_context():
    assert C.decide(NOW, [], None, None, None, None, None, None)["context"]


def test_offseason_is_quiet_except_daily_slot():
    july = datetime(2026, 7, 15, 12, 0, tzinfo=UTC)
    d = C.decide(july, [], 30, 30, 30, 30, 30, 30)
    assert not (d["capture"] or d["simulate"] or d["settle"]) and not d["in_season"]
    assert C.decide(july.replace(hour=16), [], None, 30, 30, 30, 30, 30)["capture"]


def test_status_keys_the_conductor_reads_are_the_keys_the_jobs_write():
    src = Path(__file__).resolve().parents[1] / "src" / "nhl_edge"
    text = "\n".join(p.read_text() for p in src.rglob("*.py"))
    for job, (fname, key) in C.STATUS_KEYS.items():
        assert f'"{fname}"' in text, f"nothing writes {fname}"
        assert f'"{key}"' in text, f"nothing writes key {key} for {job}"


def test_calendar_fallback_flags_itself():
    far = datetime(2031, 11, 1, tzinfo=UTC)
    in_season, label, known = C.season_window(far.date().isoformat())
    assert in_season and label is None and not known


def test_conductor_import_chain_is_stdlib_only():
    import subprocess
    import sys

    code = "import sys; import nhl_edge.workflows.conductor; bad=[m for m in sys.modules if m.split('.')[0] in ('numpy','pandas','httpx','pydantic','yaml','pyarrow')]; print(bad); raise SystemExit(1 if bad else 0)"
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, env={"PYTHONPATH": "src", "PATH": ""})
    assert r.returncode == 0, r.stdout + r.stderr
