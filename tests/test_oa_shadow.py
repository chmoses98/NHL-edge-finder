from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

REPO_DATA = Path(__file__).resolve().parents[1] / "data"


@pytest.mark.slow
def test_v1_output_is_identical_with_and_without_the_oa_shadow(tmp_path, monkeypatch):
    from nhl_edge.archive.ledger import Ledger
    from nhl_edge.workflows.simulate import run_simulate
    from tests.archive_fixture import NOW, build_archive

    out = {}
    for flag in ("0", "1"):
        monkeypatch.setenv("NHL_EDGE_OA_SHADOW", flag)
        root = tmp_path / f"a{flag}"
        build_archive(root)
        assert run_simulate(root, REPO_DATA, date="2026-09-29", n_sims=2000, now=NOW) == 0
        rows = sorted(Ledger(root).iter_rows("predictions"), key=lambda r: r["ticker"])
        out[flag] = [{k: v for k, v in r.items() if k not in ("prediction_id", "_run_id", "_observed_at_utc", "input_snapshot_ids")} for r in rows]
        slate = json.loads((root / "slates" / "latest" / "slate.json").read_text())
        if flag == "0":
            assert "oa_shadow" not in slate and not list(Ledger(root).iter_rows("predictions_oa"))
        else:
            oa = slate["oa_shadow"]
            assert "error" not in oa, oa.get("error")
            assert oa["model_version"] == "OA_RIDGE_V1" and oa["role"] == "SHADOW" and oa["authority"] == "RESEARCH_ONLY" and len(oa["blocks"]) == 5
            rows2 = list(Ledger(root).iter_rows("predictions_oa"))
            assert len(rows2) == 10 and {r["arm"] for r in rows2} == {"OA_SVA", "OA_SVA_C1"} and {r["authority"] for r in rows2} == {"RESEARCH_ONLY"}
            assert all(0.05 < r["p_home_win"] < 0.95 and 0.03 < r["p_overtime"] < 0.5 and r["v1_p_home_win"] is not None and r["pregame"] for r in rows2)
            assert all(r["predicted_at_utc"].startswith("2026-09-29T15:00") and r["params_sha256"] for r in rows2)
            assert "oa_shadow" in json.loads((root / "slates" / "latest" / "packet.json").read_text())
    assert out["0"] == out["1"]


def test_oa_failure_never_breaks_v1(tmp_path, monkeypatch):
    from nhl_edge.workflows import shadow_oa
    from nhl_edge.workflows.simulate import run_simulate
    from tests.archive_fixture import NOW, build_archive

    def boom(*a, **k):
        raise RuntimeError("synthetic OA failure")

    monkeypatch.setattr(shadow_oa, "run_shadow", boom)
    monkeypatch.setenv("NHL_EDGE_OA_SHADOW", "1")
    root = tmp_path / "a"
    build_archive(root)
    assert run_simulate(root, REPO_DATA, date="2026-09-29", n_sims=500, now=NOW) == 0
    slate = json.loads((root / "slates" / "latest" / "slate.json").read_text())
    assert slate["coverage"]["contracts_joined"] == 14 and "synthetic OA failure" in slate["oa_shadow"]["error"]
    assert os.environ["NHL_EDGE_OA_SHADOW"] == "1"


def test_calibration_uses_the_frozen_slopes_and_preserves_the_mean_level():
    from nhl_edge.workflows.shadow_oa import _calibrate, load_params

    p = load_params()
    assert p["season"] == 2026 and p["role"] == "SHADOW" and p["authority"] == "RESEARCH_ONLY" and len(p["sha256"]) == 64
    h, a = _calibrate(p, p["mean_sum"] / 2 + p["mean_diff"] / 2, p["mean_sum"] / 2 - p["mean_diff"] / 2)
    assert abs((h + a) - p["mean_sum"]) < 1e-9 and abs((h - a) - p["mean_diff"]) < 1e-9          # at the mean nothing moves
    h2, a2 = _calibrate(p, 3.8, 2.6)
    assert (h2 + a2) < 3.8 + 2.6 and (h2 - a2) > 0                                                  # totals pulled in (slope < 1)


def test_live_rows_are_normalised_to_the_oa_schema():
    from nhl_edge.research.oa_model import build_oa_data
    from nhl_edge.workflows.shadow_oa import normalize_live_team_games

    base = {"situation": "all", "iceTime": 3600.0, "season": 2026, "playoffGame": 0, "xGoalsFor": 3.0, "scoreVenueAdjustedxGoalsFor": 3.1, "goalsFor": 3, "xGoalsAgainst": 2.5}
    rows = [{**base, "team": "BOS", "opp_abbrev": "NSH", "opposingTeam": "NSH", "home_or_away": "HOME", "gameId": 2026020001, "gameDate": 20261010},
            {**base, "team": "NSH", "opp_abbrev": "BOS", "opposingTeam": "BOS", "home_or_away": "AWAY", "gameId": 2026020001, "gameDate": 20261010},
            {**base, "team": "BOS", "opp_abbrev": "NSH", "opposingTeam": "NSH", "home_or_away": "HOME", "gameId": 2026030111, "gameDate": 20261011, "playoffGame": 1}]
    d = normalize_live_team_games(rows)
    assert list(d["game_date"].iloc[:2]) == ["2026-10-10", "2026-10-10"] and list(d["game_type"]) == [2, 2, 3]
    data = build_oa_data(d)                      # only regular-season rows survive
    assert len(data.date) == 2 and sorted(data.teams) == ["BOS", "NSH"] and list(data.home) == [1, 0]
