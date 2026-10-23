from __future__ import annotations

import gzip
import json
from pathlib import Path

from nhl_edge.research import snapshot_audit as A

START = "2026-10-22T23:00:00Z"


def _gz(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt") as f:
        f.write("\n".join(json.dumps(r) for r in rows) + "\n")


def _build(tmp_path):
    da, pd = tmp_path / "da", tmp_path / "pd"
    v1 = lambda pred, obs, mins, hg="CONFIRMED": {"game_id": "1", "predicted_at_utc": pred, "_observed_at_utc": obs, "data_cutoff_utc": pred, "minutes_to_start": mins,   # noqa: E731
                                                  "home_goalie_status": hg, "away_goalie_status": "PROBABLE", "horizon_label": "x"}
    _gz(da / "predictions/dt=2026-10-22/p1.jsonl.gz", [v1("2026-10-22T22:00:00Z", "2026-10-22T22:00:05Z", 60.0, "PROJECTED"), v1("2026-10-22T22:00:00Z", "2026-10-22T22:00:05Z", 60.0)])
    _gz(da / "predictions/dt=2026-10-22/p2.jsonl.gz", [v1("2026-10-22T22:50:00Z", "2026-10-22T22:50:04Z", 10.0)])
    _gz(da / "predictions/dt=2026-10-23/p3.jsonl.gz", [v1("2026-10-23T00:10:00Z", "2026-10-23T00:10:03Z", -70.0)])         # after the start: not pregame
    pf = lambda gen, arch, role: {"game_id": "1", "game_start_utc": START, "generated_utc": gen, "archived_utc": arch, "data_asof_utc": "2026-10-22T02:00:00Z", "model_role": role}   # noqa: E731
    _gz(pd / "forecasts/nhl/2026-10-22/a.jsonl.gz", [pf("2026-10-22T21:00:00Z", "2026-10-22T21:00:30Z", "challenger"), pf("2026-10-22T21:00:00Z", "2026-10-22T21:00:30Z", "challenger")])
    # generated before the start but archived after it: late-arriving, never "available"
    _gz(pd / "forecasts/nhl/2026-10-22/b.jsonl.gz", [pf("2026-10-22T22:55:00Z", "2026-10-22T23:05:00Z", "challenger"), pf("2026-10-22T22:00:00Z", "2026-10-22T22:01:00Z", "incumbent")])
    (pd / "runs/nhl/2026-10-22").mkdir(parents=True)
    (pd / "runs/nhl/2026-10-22/r.json").write_text(json.dumps({"archived_at": "2026-10-22T22:40:00Z", "assemble": {"rows": 10, "participation": {"CONFIRMED_ACTIVE": 5}},
                                                           "coverage": {"events": {"1": {"newest_age_minutes": 4.0}}}}))
    return da, pd


def test_pregame_means_archived_at_or_before_the_scheduled_start(tmp_path):
    da, pd = _build(tmp_path)
    rep = A.audit("2026-10-22", A.Tree(str(da)), A.Tree(str(pd)))
    assert rep["n_games"] == 1
    g = rep["games"][0]
    assert g["start_utc"] == START
    v1 = g["kinds"]["v1"]
    assert v1["n_pregame"] == 2 and v1["n_post_start"] == 1                              # the duplicate rows of one snapshot count once
    assert v1["last_pregame_archived_utc"] == "2026-10-22T22:50:04Z" and v1["last_pregame_minutes_before_start"] == 9.9
    assert v1["last_pregame_detail"]["home_goalie"] == "CONFIRMED" and v1["first_post_start_archived_utc"] == "2026-10-23T00:10:03Z"
    ch = g["kinds"]["pf_challenger"]
    assert ch["n_pregame"] == 1 and ch["n_post_start"] == 1                               # the 23:05 archive of a 22:55 run is late-arriving
    assert ch["last_pregame_archived_utc"] == "2026-10-22T21:00:30Z"
    assert g["kinds"]["pf_incumbent"]["last_pregame_minutes_before_start"] == 59.0
    ev = g["pf_last_evaluation_before_start"]
    assert ev["minutes_before_start"] == 20.0 and ev["newest_capture_age_min"] == 4.0


def test_markdown_and_cli_write_both_files_and_change_nothing(tmp_path):
    da, pd = _build(tmp_path)
    before = sorted((p, p.stat().st_mtime_ns) for p in tmp_path.rglob("*") if p.is_file())
    rc = A.main(["--date", "2026-10-22", "--data-archive", str(da), "--projection-data", str(pd), "--out", str(tmp_path / "out")])
    assert rc == 0
    md = (tmp_path / "out.md").read_text()
    assert "2026-10-22T23:00:00Z" in md and "CONFIRMED/PROBABLE" in md
    assert json.loads((tmp_path / "out.json").read_text())["n_games"] == 1
    after = sorted((p, p.stat().st_mtime_ns) for p in tmp_path.rglob("*") if p.is_file() and p.name not in ("out.md", "out.json"))
    assert after == before
