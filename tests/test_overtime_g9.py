"""G9 (publication-contract compatibility) for the overtime target, on the real pipeline: nhl simulate (fixture archive) and the app export."""

from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from nhl_edge import projection_registry as PR

REPO_DATA = Path(__file__).resolve().parents[1] / "data"
APPROVAL = {"approved_by": "owner", "approved_at_utc": "2026-12-01T00:00:00Z", "evidence": "test"}


def _registry(tmp_path, approved: bool):
    p = tmp_path / "reg.json"
    p.write_text(json.dumps({"schema": "projection-registry-1", "targets": {"overtime": {
        "published_model": "DATA_ONLY_V2", "candidate": "DATA_ONLY_V2", "approval": APPROVAL if approved else None}}}))
    return p


def _simulate(tmp_path, monkeypatch, name, registry=None, v2="1"):
    from nhl_edge.workflows.simulate import run_simulate
    from tests.archive_fixture import NOW, build_archive

    monkeypatch.setenv("NHL_EDGE_V2_SHADOW", v2)
    if registry is not None:
        monkeypatch.setattr(PR, "REGISTRY_PATH", registry)
    root = tmp_path / name
    build_archive(root)
    assert run_simulate(root, REPO_DATA, date="2026-09-29", n_sims=2000, now=NOW) == 0
    return root, json.loads((root / "slates" / "latest" / "slate.json").read_text())


@pytest.mark.slow
def test_default_registry_publishes_the_v1_slate_exactly_and_an_approved_switch_changes_only_the_overtime_fields(tmp_path, monkeypatch):
    from nhl_edge.archive.ledger import Ledger

    root0, off = _simulate(tmp_path, monkeypatch, "off", v2="0")                                  # no V2 at all: the pre-change world
    root1, dflt = _simulate(tmp_path, monkeypatch, "default")                                      # shadow on, registry at the committed default
    assert "projection_registry" not in dflt and all("overtime_model" not in g for g in dflt["games"])
    assert dflt["games"] == off["games"]                                                           # the published game documents are identical

    root2, cand = _simulate(tmp_path, monkeypatch, "cand", registry=_registry(tmp_path, True))
    assert cand["projection_registry"]["published_model"] == "DATA_ONLY_V2" and cand["projection_registry"]["from_v2"] == len(cand["games"]) == 5
    blocks = {b["game_id"]: b for b in cand["v2_shadow"]["blocks"]}
    keys = set(PR.OVERTIME_FIELDS)
    for g, base in zip(cand["games"], dflt["games"], strict=True):
        v2 = blocks[g["game_id"]]["v2"]
        assert {k: g[k] for k in keys} == {k: v2[k] for k in keys}                                 # all five from V2, together
        assert g["overtime_model"]["published"] == "DATA_ONLY_V2" and g["overtime_model"]["v1"] == {k: base[k] for k in keys}
        assert {k: v for k, v in g.items() if k not in keys | {"overtime_model"}} == {k: v for k, v in base.items() if k not in keys}     # nothing else moved
        assert abs(g["p_home_reg_win"] + g["p_away_reg_win"] + g["p_overtime"] - 1) < 1e-9 and g["p_reg_tie"] == g["p_overtime"]
        assert 0.05 < g["p_overtime"] < 0.5

    # prices, contracts and the V1 prediction ledger are untouched by the switch
    strip = lambda rows: [{k: v for k, v in r.items() if k not in ("prediction_id", "_run_id", "_observed_at_utc", "input_snapshot_ids")} for r in sorted(rows, key=lambda r: r["ticker"])]  # noqa: E731
    assert strip(Ledger(root1).iter_rows("predictions")) == strip(Ledger(root2).iter_rows("predictions"))
    assert strip(cand["contracts"]) == strip(dflt["contracts"])

    # a switch without an approval record is refused, loudly, and publishes V1
    root3, refused = _simulate(tmp_path, monkeypatch, "refused", registry=_registry(tmp_path, False))
    assert refused["projection_registry"]["published_model"] == "DATA_ONLY_V1" and "no complete approval" in refused["projection_registry"]["default_reason"]
    assert refused["games"] == dflt["games"]
    assert os.environ["NHL_EDGE_V2_SHADOW"] == "1"


@pytest.mark.slow
def test_a_failing_v2_arm_publishes_v1_numbers_even_with_an_approved_switch(tmp_path, monkeypatch):
    from nhl_edge.workflows import shadow_v2

    def boom(*a, **k):
        raise RuntimeError("synthetic V2 failure")

    monkeypatch.setattr(shadow_v2, "run_shadow", boom)
    _, off = _simulate(tmp_path, monkeypatch, "off", v2="0")
    _, s = _simulate(tmp_path, monkeypatch, "boom", registry=_registry(tmp_path, True))
    assert "synthetic V2 failure" in s["v2_shadow"]["error"] and s["games"] == off["games"] and "projection_registry" not in s


def test_the_app_export_carries_the_overtime_provenance_and_still_validates(tmp_path):
    from edge_finder_contract import publish

    from tests.test_app_contract_v1 import _export, _load, make_root

    root, acc = make_root(tmp_path)
    sp = root / "slates" / "latest" / "slate.json"
    slate = json.loads(sp.read_text())
    slate["games"][0].update({"p_overtime": 0.18, "p_reg_tie": 0.18, "p_home_reg_win": 0.41, "p_away_reg_win": 0.41, "p_shootout": 0.06})          # the V1 numbers
    sp.write_text(json.dumps(slate, indent=1))
    base = tmp_path / "base"
    assert _export(root, base, acc)["ok"]
    ev = lambda out: {e["source_ids"]["nhl_game_id"]: e["event_id"] for e in _load(out, "events")["items"]}  # noqa: E731
    gid = next(g for g in ev(base))
    detail0 = _load(base, f"event_detail/{ev(base)[gid]}")

    slate = json.loads(sp.read_text())
    g = slate["games"][0]
    v1 = {k: g.get(k) for k in PR.OVERTIME_FIELDS}
    g.update({"p_overtime": 0.23, "p_reg_tie": 0.23, "p_home_reg_win": 0.39, "p_away_reg_win": 0.38, "p_shootout": 0.08,
              "overtime_model": {"published": "DATA_ONLY_V2", "fallback": False, "v1": v1}})
    sp.write_text(json.dumps(slate, indent=1))
    cand = tmp_path / "cand"
    res = _export(root, cand, acc)
    assert res["ok"], res.get("error")
    assert publish.verify_published(cand) == []                                              # schema-valid, manifest intact
    detail1 = _load(cand, f"event_detail/{ev(cand)[gid]}")
    mg0, mg1 = detail0["context"]["model_game"], detail1["context"]["model_game"]
    assert mg1["p_overtime"] == 0.23 and mg1["overtime_model"]["published"] == "DATA_ONLY_V2"
    assert set(mg1) - set(mg0) == {"overtime_model"}                                        # additive: no field removed or renamed
    for name in ("markets", "model_prices", "recommendations", "board"):                    # prices, recommendations and the board are untouched
        a, b = _load(base, name), _load(cand, name)
        for d in (a, b):
            d.pop("generated_at", None)
            d.pop("run_id", None)
        assert a == b, name
