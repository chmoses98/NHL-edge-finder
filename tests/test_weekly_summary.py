from __future__ import annotations

import json
from datetime import UTC, datetime, timedelta
from pathlib import Path

from nhl_edge.research import weekly_summary as W
from nhl_edge.timeutil import iso

NOW = datetime(2026, 10, 22, 18, 0, tzinfo=UTC)


def _archive(tmp: Path, *, age_h: dict[str, float] | None = None, ece: float = 0.03, n: int = 6000, settle_errors=None, steps=None) -> Path:
    ages = {"STATUS_capture.json": 0.1, "STATUS_simulate.json": 0.5, "STATUS_settle.json": 2.0, "STATUS_evaluate.json": 3.0, "STATUS_context.json": 0.5} | (age_h or {})
    for fname, (key, _) in W.STALE_HOURS.items():
        d = {key: iso(NOW - timedelta(hours=ages[fname]))}
        if fname == "STATUS_settle.json":
            d["errors"] = settle_errors or []
            d["disagreements"] = []
        if fname == "STATUS_evaluate.json":
            d["steps"] = steps or {"v1": "OK"}
        if fname == "STATUS_context.json":
            d["games_today"] = ["2026020154"]
        (tmp / fname).write_text(json.dumps(d))
    (tmp / "eval").mkdir(exist_ok=True)
    (tmp / "eval" / "report.json").write_text(json.dumps({"evaluated_at_utc": iso(NOW), "families": {"game_winner": {"views": {
        "DATA_ONLY_V1": {"n": n, "brier": 0.23, "log_loss": 0.65, "ece": ece}, "MARKET_BASELINE": {"n": n, "brier": 0.228, "log_loss": 0.647, "ece": 0.03}}}}}))
    (tmp / "eval" / "report_learning.json").write_text(json.dumps({"counts": {"games_settled": 151, "games_projected": 153}, "stage": {"stage": "CALIBRATION_BUILDING"}}))
    return tmp


def test_healthy_archive_has_no_alerts(tmp_path):
    assert W.integrity_alerts(_archive(tmp_path), NOW) == []


def test_stale_and_failing_jobs_alert(tmp_path):
    a = _archive(tmp_path, age_h={"STATUS_capture.json": 3.0, "STATUS_evaluate.json": 40.0}, settle_errors=["x"], steps={"v1": "OK", "learning": "FAILED: KeyError: x"})
    codes = {x["code"] for x in W.integrity_alerts(a, NOW)}
    assert {"STATUS_STALE", "SETTLE_PROBLEM", "EVAL_STEP_FAILED"} <= codes


def test_missing_status_is_an_alert_and_offseason_silences_staleness(tmp_path):
    a = _archive(tmp_path, age_h={"STATUS_capture.json": 50.0})
    (a / "STATUS_simulate.json").unlink()
    codes = [x["code"] for x in W.integrity_alerts(a, NOW)]
    assert "STATUS_MISSING" in codes and "STATUS_STALE" in codes
    assert "STATUS_STALE" not in [x["code"] for x in W.integrity_alerts(a, NOW, in_game_season=False)]


def test_calibration_collapse_only_on_large_samples_and_performance_is_never_an_alert(tmp_path):
    assert "CALIBRATION_COLLAPSE" in {x["code"] for x in W.integrity_alerts(_archive(tmp_path, ece=0.2, n=6000), NOW)}
    sub = tmp_path / "small"
    sub.mkdir()
    assert "CALIBRATION_COLLAPSE" not in {x["code"] for x in W.integrity_alerts(_archive(sub, ece=0.2, n=500), NOW)}
    # the model scoring worse than the market (0.23 vs 0.228 above) is not an integrity problem
    assert W.integrity_alerts(_archive(tmp_path / "x" if (tmp_path / "x").mkdir() is None else tmp_path, ece=0.03), NOW) == []


def test_run_writes_files_and_exit_code(tmp_path):
    a = _archive(tmp_path / "a") if (tmp_path / "a").mkdir() is None else None
    out = tmp_path / "out"
    assert W.run(a, out, None, NOW) == 0
    assert "NOT independent games" in (out / "summary.md").read_text() and json.loads((out / "alerts.json").read_text())["alerts"] == []
    (a / "STATUS_capture.json").write_text(json.dumps({"last_capture_utc": iso(NOW - timedelta(hours=9))}))
    assert W.run(a, out, None, NOW) == 2


def test_off_days_do_not_alert_on_staleness_by_default(tmp_path):
    a = _archive(tmp_path, age_h={"STATUS_capture.json": 30.0, "STATUS_simulate.json": 30.0})
    assert "STATUS_STALE" in {x["code"] for x in W.integrity_alerts(a, NOW)}                  # a game day: the worker should be capturing
    ctx = json.loads((a / "STATUS_context.json").read_text())
    ctx["games_today"] = []
    (a / "STATUS_context.json").write_text(json.dumps(ctx))
    assert "STATUS_STALE" not in {x["code"] for x in W.integrity_alerts(a, NOW)}              # no games today: quiet is expected


def test_pf_scorecard_alerts_in_the_published_list_form_are_read():
    from nhl_edge.research.weekly_summary import pf_alert_items

    published = {"alerts": [{"family": "goals", "status": "OK", "what": "within expectations"}, {"family": "saves", "status": "INSUFFICIENT", "what": "32 settled forecasts (< 100)"},
                            {"family": "shots", "status": "ALERT", "what": "bias outside band"}]}
    assert pf_alert_items(published) == ["shots: bias outside band"]
    assert pf_alert_items({"alerts": {"goals": "OK", "shots": "ALERT"}}) == ["shots: ALERT"]
    assert pf_alert_items({"alerts": []}) == [] and pf_alert_items(None) == [] and pf_alert_items({}) == []
