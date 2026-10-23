"""Pregame audit and daily scoreboard on a synthetic append-only archive: pregame/late split, manifest integrity, pairing, no imputation."""

from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path

from nhl_edge.research import daily_scoreboard as S
from nhl_edge.research import pregame_audit as A


def _write(archive: Path, kind: str, day: str, name: str, rows: list[dict], manifest: bool = True) -> None:
    p = archive / kind / f"dt={day}" / name
    p.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(p, "wt") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    if manifest:
        with (archive / "manifest.jsonl").open("a") as m:
            m.write(json.dumps({"path": str(p.relative_to(archive)), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}) + "\n")


def _row(gid, team, p, at, mts, pregame=True, **kw):
    return {"game_id": gid, "family": "game_winner", "team_id": team, "p_data_only": p, "p_market": 0.5, "predicted_at_utc": at, "minutes_to_start": mts, "pregame": pregame,
            "home_goalie_status": "CONFIRMED", "away_goalie_status": "PROBABLE", **kw}


def _archive(tmp: Path) -> Path:
    a = tmp / "arch"
    # game 1 starts 2026-10-22T23:00Z: forecasts 40 and 10 min before, one late row 5 min after
    _write(a, "predictions", "2026-10-22", "p1.jsonl.gz", [_row("1", 10, 0.60, "2026-10-22T22:20:00Z", 40.0), _row("1", 11, 0.40, "2026-10-22T22:20:00Z", 40.0)])
    _write(a, "predictions", "2026-10-22", "p2.jsonl.gz", [_row("1", 10, 0.70, "2026-10-22T22:50:00Z", 10.0), _row("1", 11, 0.30, "2026-10-22T22:50:00Z", 10.0)])
    _write(a, "predictions", "2026-10-22", "p3.jsonl.gz", [_row("1", 10, 0.99, "2026-10-22T23:05:00Z", -5.0, pregame=False)])
    _write(a, "predictions_v2", "2026-10-22", "v.jsonl.gz", [{"game_id": "1", "family": "game_winner", "team_id": 10, "p_data_only_v2": 0.65, "predicted_at_utc": "2026-10-22T22:50:00Z", "minutes_to_start": 10.0}])
    _write(a, "predictions_oa", "2026-10-22", "o.jsonl.gz", [{"game_id": "1", "arm": "OA_SVA", "p_home_win": 0.62, "predicted_at_utc": "2026-10-22T22:50:00Z", "minutes_to_start": 10.0, "pregame": True},
                                                            {"game_id": "1", "arm": "OA_SVA_C1", "p_home_win": 0.58, "predicted_at_utc": "2026-10-22T22:50:00Z", "minutes_to_start": 10.0, "pregame": True}])
    # game 2: only a late forecast; game 3: no result yet
    _write(a, "predictions", "2026-10-22", "p4.jsonl.gz", [_row("2", 20, 0.5, "2026-10-22T23:35:00Z", -5.0, pregame=False)])
    _write(a, "predictions", "2026-10-22", "p5.jsonl.gz", [_row("3", 30, 0.5, "2026-10-22T22:50:00Z", 70.0)])
    _write(a, "results", "2026-10-23", "r.jsonl.gz", [{"game_id": "1", "status": "final", "home_team_id": 10, "away_team_id": 11, "home_final": 4, "away_final": 2},
                                                      {"game_id": "2", "status": "final", "home_team_id": 20, "away_team_id": 21, "home_final": 1, "away_final": 3}])
    return a


def test_pregame_audit_separates_pregame_from_late_and_verifies_the_manifest(tmp_path):
    a = _archive(tmp_path)
    res = A.audit_day(a, "2026-10-22", utc_dates=["2026-10-22"], kinds=("predictions", "predictions_v2"))
    g1 = res["kinds"]["predictions"]["games"]["1"]
    assert g1["last_pregame_at_utc"] == "2026-10-22T22:50:00Z" and g1["last_pregame_minutes_to_start"] == 10.0 and g1["runs_pregame"] == 2
    assert g1["runs_late"] == 1 and g1["rows_late"] == 1 and g1["goalies_at_last_pregame"] == ["CONFIRMED", "PROBABLE"]
    assert res["kinds"]["predictions"]["games"]["2"]["last_pregame_at_utc"] is None        # only a late row: reported as NONE, never imputed
    assert all(d["integrity"]["mismatch"] == [] and d["integrity"]["verified"] == d["integrity"]["files"] for d in res["kinds"].values())
    assert "NONE" in A.render(res)


def test_pregame_audit_detects_a_rewritten_partition(tmp_path):
    a = _archive(tmp_path)
    p = a / "predictions" / "dt=2026-10-22" / "p1.jsonl.gz"
    with gzip.open(p, "wt") as f:
        f.write(json.dumps(_row("1", 10, 0.01, "2026-10-22T22:20:00Z", 40.0)) + "\n")
    res = A.audit_day(a, "2026-10-22", utc_dates=["2026-10-22"], kinds=("predictions",))
    assert res["kinds"]["predictions"]["integrity"]["mismatch"] == ["predictions/dt=2026-10-22/p1.jsonl.gz"]
    assert A.main(["--archive", str(a), "--date", "2026-10-22"]) == 2


def test_scoreboard_uses_only_the_last_pregame_forecast_and_pairs_models(tmp_path):
    a = _archive(tmp_path)
    built = S.build_games(a, ["2026-10-22", "2026-10-23"])
    g = built["games"]["1"]
    assert g["p"]["V1"] == 0.70 and g["p"]["V2"] == 0.65 and g["p"]["OA_SVA"] == 0.62 and g["p"]["OA_SVA_C1"] == 0.58 and g["y_home_win"] == 1.0   # not the 0.99 late row
    assert built["pending"] == ["3"] and built["no_pregame_or_before_freeze"] == ["2"] and set(built["games"]) == {"1"}
    sc = S.score(built["games"])
    assert abs(sc["models"]["V1"]["brier"] - 0.09) < 1e-9 and sc["paired"]["OA_SVA_C1_minus_V1"]["n"] == 1 and "lo95" not in sc["paired"]["V1_minus_MARKET"]


def test_games_before_the_freeze_are_excluded(tmp_path):
    a = tmp_path / "arch"
    _write(a, "predictions", "2026-10-20", "p.jsonl.gz", [_row("9", 10, 0.6, "2026-10-20T22:50:00Z", 10.0)])
    _write(a, "results", "2026-10-21", "r.jsonl.gz", [{"game_id": "9", "status": "final", "home_team_id": 10, "away_team_id": 11, "home_final": 2, "away_final": 1}])
    built = S.build_games(a, ["2026-10-20", "2026-10-21"])
    assert built["games"] == {} and built["no_pregame_or_before_freeze"] == ["9"]
