"""thesis_model_audit.toi_prospective and model_research.exp_players are allocation-version-aware: at the default they behave as before; once another team-minute allocation is
published they report the incumbent consistently at the top level and the as-published values per allocation, never pooled."""

from __future__ import annotations

import gzip
import json

import numpy as np
import pandas as pd

from nhl_edge.model_research import exp_players as XP
from nhl_edge.players import team_minutes as TM
from nhl_edge.research import thesis_model_audit as TA


def test_row_allocation_defaults_to_the_published_template():
    for v in (None, float("nan"), "", "nan", "None"):
        assert TM.row_allocation(v) == "team-minutes-0"
    assert TM.row_allocation("team-minutes-1.0") == "team-minutes-1.0"


def test_with_allocation_is_a_no_op_at_the_default_and_pins_the_incumbent_otherwise():
    d = pd.DataFrame({"meta_expected_toi_min": [17.0, 18.4], "meta_expected_pp_toi_min": [2.0, 2.4], "meta_expected_shots": [2.5, 2.6]})
    o = TM.with_allocation(d)
    assert (o["alloc"] == "team-minutes-0").all() and (o["meta_expected_toi_min_incumbent"] == d["meta_expected_toi_min"]).all()
    d2 = d.assign(meta_team_minutes_version=[None, "team-minutes-1.0"], meta_expected_toi_min_legacy=[np.nan, 18.0], meta_expected_pp_toi_min_legacy=[np.nan, 2.0],
                  meta_expected_shots_legacy=[np.nan, 2.5])
    o = TM.with_allocation(d2)
    assert o["alloc"].tolist() == ["team-minutes-0", "team-minutes-1.0"]
    assert o["meta_expected_toi_min_incumbent"].tolist() == [17.0, 18.0] and o["meta_expected_shots_incumbent"].tolist() == [2.5, 2.5]


def _archive(tmp_path, preds, actual):
    root = tmp_path / "arch"
    man = []
    for kind, rows in (("predictions_player", preds), ("player_events/players", actual)):
        f = root / kind / "part.jsonl.gz"
        f.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(f, "wt") as fh:
            fh.write("\n".join(json.dumps(r) for r in rows))
        man.append({"kind": kind, "path": str(f.relative_to(root))})
    (root / "manifest.jsonl").write_text("\n".join(json.dumps(m) for m in man))
    return root


def test_toi_prospective_never_pools_allocations(tmp_path, monkeypatch):
    hist = pd.DataFrame({"player_id": pd.Series([], dtype="int64"), "game_type": pd.Series([], dtype="int64"), "toi_s": pd.Series([], dtype="float64"), "game_date": pd.Series([], dtype="object")})
    monkeypatch.setattr(TA, "load_player_tables", lambda *a, **k: hist)
    preds, actual = [], []
    for i in range(6):
        cand = i >= 3
        r = {"game_id": f"g{i}", "player_id": i, "pregame": True, "predicted_at_utc": "2026-10-30T20:00:00Z", "meta_deployment_source": "LINES_PROJECTED",
             "meta_expected_toi_min": 18.4 if cand else 18.0}
        if cand:
            r |= {"meta_team_minutes_version": "team-minutes-1.0", "meta_expected_toi_min_legacy": 18.0}
        preds.append(r)
        actual.append({"game_id": f"g{i}", "player_id": i, "toi_s": 19 * 60})
    out = TA.toi_prospective(_archive(tmp_path, preds, actual))
    assert out["ALL"]["n"] == 6 and out["ALL"]["bias_model_min"] == -1.0                       # incumbent minutes for every row: 18.0 vs 19.0
    assert set(out["by_allocation"]) == {"team-minutes-0", "team-minutes-1.0"}
    assert out["by_allocation"]["team-minutes-0"]["ALL"]["n"] == 3 and out["by_allocation"]["team-minutes-0"]["ALL"]["bias_model_min"] == -1.0
    assert out["by_allocation"]["team-minutes-1.0"]["ALL"]["bias_model_min"] == -0.6           # as published: 18.4 vs 19.0


def test_toi_prospective_at_the_default_has_one_allocation_block_equal_to_the_top_level(tmp_path, monkeypatch):
    monkeypatch.setattr(TA, "load_player_tables", lambda *a, **k: pd.DataFrame({"player_id": pd.Series([], dtype="int64"), "game_type": pd.Series([], dtype="int64"), "toi_s": pd.Series([], dtype="float64"), "game_date": pd.Series([], dtype="object")}))
    preds = [{"game_id": "g", "player_id": 1, "pregame": True, "predicted_at_utc": "2026-10-30T20:00:00Z", "meta_deployment_source": "X", "meta_expected_toi_min": 17.0}]
    out = TA.toi_prospective(_archive(tmp_path, preds, [{"game_id": "g", "player_id": 1, "toi_s": 1200}]))
    assert list(out["by_allocation"]) == ["team-minutes-0"] and out["by_allocation"]["team-minutes-0"]["ALL"] == out["ALL"]


def test_exp_players_allocation_blocks_do_not_pool():
    rows = []
    for i in range(8):
        cand = i % 2 == 1
        rows.append({"game_id": f"g{i}", "alloc": "team-minutes-1.0" if cand else "team-minutes-0", "toi_min": 19.0, "toi_pp_min": 2.5, "sog": 2,
                     "meta_expected_toi_min": 18.4 if cand else 18.0, "meta_expected_pp_toi_min": 2.4 if cand else 2.0, "meta_expected_shots": 2.1 if cand else 1.9})
    b = XP.allocation_blocks(pd.DataFrame(rows))
    assert set(b) == {"team-minutes-0", "team-minutes-1.0"} and b["team-minutes-0"]["n"] == 4
    assert abs(b["team-minutes-0"]["bias_toi_min"]["mean"] - 1.0) < 1e-12 and abs(b["team-minutes-1.0"]["bias_toi_min"]["mean"] - 0.6) < 1e-12
