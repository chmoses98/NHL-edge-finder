"""The projection registry: the default publishes exactly what was published before; a switch needs an approval record; fallbacks never mix models."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from nhl_edge import projection_registry as PR

REPO = Path(__file__).resolve().parents[1]


def _games():
    return [{"game_id": "1", "p_reg_tie": 0.18, "p_overtime": 0.18, "p_home_reg_win": 0.41, "p_away_reg_win": 0.41, "p_shootout": 0.06, "p_home_win": 0.5},
            {"game_id": "2", "p_reg_tie": 0.17, "p_overtime": 0.17, "p_home_reg_win": 0.42, "p_away_reg_win": 0.41, "p_shootout": 0.05, "p_home_win": 0.55}]


def _blocks():
    return [{"game_id": "1", "v2": {"p_reg_tie": 0.23, "p_overtime": 0.23, "p_home_reg_win": 0.39, "p_away_reg_win": 0.38, "p_shootout": 0.08, "p_home_win": 0.5}},
            {"game_id": "2", "v2": {"p_reg_tie": float("nan"), "p_overtime": 0.2}}]                # game 2: V2 numbers unusable


def _registry(tmp_path, published="DATA_ONLY_V2", approval=None, candidate="DATA_ONLY_V2"):
    p = tmp_path / "r.json"
    p.write_text(json.dumps({"schema": "projection-registry-1", "targets": {"overtime": {"published_model": published, "candidate": candidate, "approval": approval}}}))
    return p


APPROVAL = {"approved_by": "owner", "approved_at_utc": "2026-12-01T00:00:00Z", "evidence": "docs/research/overtime_promotion/RECOMMENDATION.md"}


def test_the_committed_registry_publishes_the_incumbent_and_carries_no_approval():
    d = json.loads((REPO / "data" / "registry" / "projection-registry.json").read_text())
    assert d["targets"]["overtime"]["published_model"] == "DATA_ONLY_V1" and d["targets"]["overtime"]["approval"] is None
    assert PR.published_model("overtime") == ("DATA_ONLY_V1", None)


def test_default_leaves_every_game_document_byte_identical():
    games, before = _games(), copy.deepcopy(_games())
    rep = PR.apply_overtime(games, _blocks())
    assert games == before and json.dumps(games) == json.dumps(before) and rep["published_model"] == "DATA_ONLY_V1" and rep["from_v2"] == 0


def test_a_switch_without_a_complete_approval_is_ignored_and_says_why(tmp_path):
    for appr in (None, {}, {"approved_by": "owner"}, {**APPROVAL, "evidence": " "}):
        games, before = _games(), copy.deepcopy(_games())
        rep = PR.apply_overtime(games, _blocks(), _registry(tmp_path, approval=appr))
        assert games == before and rep["published_model"] == "DATA_ONLY_V1" and "no complete approval" in rep["default_reason"]
    assert PR.published_model("overtime", _registry(tmp_path, published="SOMETHING_ELSE", approval=APPROVAL))[0] == "DATA_ONLY_V1"
    assert PR.published_model("overtime", tmp_path / "missing.json")[0] == "DATA_ONLY_V1"


def test_an_approved_switch_replaces_all_five_fields_together_and_falls_back_per_game(tmp_path):
    games = _games()
    rep = PR.apply_overtime(games, _blocks(), _registry(tmp_path, approval=APPROVAL))
    g1, g2 = games
    assert (g1["p_reg_tie"], g1["p_overtime"], g1["p_home_reg_win"], g1["p_away_reg_win"], g1["p_shootout"]) == (0.23, 0.23, 0.39, 0.38, 0.08)
    assert g1["p_home_win"] == 0.5 and g1["overtime_model"]["published"] == "DATA_ONLY_V2" and g1["overtime_model"]["v1"]["p_overtime"] == 0.18      # untouched target, V1 kept
    assert g2["p_overtime"] == 0.17 and g2["p_reg_tie"] == 0.17 and g2["overtime_model"]["fallback"] is True and g2["overtime_model"]["published"] == "DATA_ONLY_V1"
    assert rep["from_v2"] == 1 and rep["fallback"] == 1
    assert abs(g1["p_reg_tie"] - g1["p_overtime"]) < 1e-12


def test_missing_v2_blocks_fall_back_for_every_game(tmp_path):
    games, before = _games(), _games()
    PR.apply_overtime(games, None, _registry(tmp_path, approval=APPROVAL))
    assert all(g["overtime_model"]["fallback"] for g in games) and all(g[k] == b[k] for g, b in zip(games, before, strict=True) for k in PR.OVERTIME_FIELDS)


@pytest.mark.parametrize("bad", [-0.1, 1.2, None, "x"])
def test_out_of_range_or_non_numeric_v2_values_are_never_published(tmp_path, bad):
    blocks = _blocks()
    blocks[0]["v2"]["p_overtime"] = bad
    games = _games()
    PR.apply_overtime(games, blocks, _registry(tmp_path, approval=APPROVAL))
    assert games[0]["p_overtime"] == 0.18 and games[0]["overtime_model"]["fallback"] is True
