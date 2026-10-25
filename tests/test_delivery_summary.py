from __future__ import annotations

import json
from datetime import UTC, datetime

from nhl_edge.research import delivery_summary as D


def _d(s):
    return datetime.fromisoformat(s).astimezone(UTC)


def test_summary_uses_the_last_evaluation_before_the_drop_and_flags_missing_and_stale():
    games = [{"game_id": "1", "game_date_et": "2026-10-24", "season_type": "regular", "start_time_utc": "2026-10-24T23:00:00Z"},
             {"game_id": "2", "game_date_et": "2026-10-24", "season_type": "regular", "start_time_utc": "2026-10-24T23:00:00Z"},
             {"game_id": "3", "game_date_et": "2026-10-24", "season_type": "regular", "start_time_utc": "2026-10-25T01:00:00Z"},
             {"game_id": "4", "game_date_et": "2026-10-24", "season_type": "preseason", "start_time_utc": "2026-10-25T01:00:00Z"}]
    ev = {"1": [(_d("2026-10-24T20:00:00+00:00"), 12.0), (_d("2026-10-24T22:30:00+00:00"), 8.0), (_d("2026-10-24T23:10:00+00:00"), 1.0)],     # the post-drop run is ignored
          "3": [(_d("2026-10-25T00:20:00+00:00"), 95.0)]}
    s = D.summarize(games, ev, {"1": 5, "3": 2}, "2026-10-24", "2026-10-24")
    g = {r["game_id"]: r for r in s["games"]}
    assert set(g) == {"1", "2", "3"} and g["1"]["last_eval_lead_min"] == 30.0 and g["1"]["lineup_age_at_last_eval_min"] == 8.0 and g["1"]["status"] == "OK"
    assert g["2"]["status"] == "MISSING" and g["3"]["status"] == "STALE_LINEUP"
    day = s["days"][0]
    assert day["games"] == 3 and day["ok"] == 1 and sorted(day["problems"]) == ["2", "3"] and day["min_last_eval_lead_min"] == 30.0
    assert "2026-10-24" in D.render(s)


def test_evaluations_read_the_raw_run_files(tmp_path):
    d = tmp_path / "runs" / "nhl" / "2026-10-24"
    d.mkdir(parents=True)
    (d / "x_project.json").write_text(json.dumps({"archived_at": "2026-10-24T22:30:00Z", "coverage": {"events": {"7": {"newest_age_minutes": 9.5}}}}))
    got = D.evaluations(tmp_path)
    assert got["7"][0][1] == 9.5 and got["7"][0][0].hour == 22
