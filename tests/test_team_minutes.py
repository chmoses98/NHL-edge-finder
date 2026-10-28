"""Team-minute allocation (candidate ``team-minutes-1.0`` vs the published ``team-minutes-0``): physical consistency, registry gate, fallback, comparator pin, and -- through the
real RUN NHL path -- that goals / assists / points / saves are bit-identical under either allocation while the ice-time and shots fields move."""

from __future__ import annotations

import copy
import json
import random
from dataclasses import replace
from pathlib import Path

import pytest

from nhl_edge import projection_registry as PR
from nhl_edge.players import team_minutes as TM

REPO = Path(__file__).resolve().parents[1]
PINNED = json.loads((REPO / "data" / "params" / "team-minutes-1.0.json").read_text())["fingerprint"]
APPROVAL = {"approved_by": "owner", "approved_at_utc": "2026-12-01T00:00:00Z", "evidence": "docs/research/team_minutes/GO_NO_GO.md", "candidate_fingerprint": PINNED}


def _prm() -> TM.AllocationParams:
    return TM.load_params()


def test_legacy_template_is_the_old_literal_verbatim():
    for p in (0.05, 0.1, 0.215, 0.3, 0.45):
        assert TM.legacy(p) == {"ev": 50.6, "pp": 4.4 * p / 0.215, "sh": 4.4, "ea": 0.6, "en": 0.6, "ot": 1.2}


def test_committed_parameters_load_and_are_sane():
    p = _prm()
    assert p.version == "team-minutes-1.0" and p.fingerprint() == json.loads(TM.PARAMS_PATH.read_text())["fingerprint"]
    assert p.provenance["train_seasons"] == [2022, 2023, 2024, 2025]             # completed seasons only: no 2026 game is in the fit
    assert 0.5 < p.ot_min < 1.0 and 1.0 < p.pp_per_ppmin < 1.25 and 4.5 < p.league_pp_min < 5.8 and 0.4 < p.ea_min < 0.8
    assert all(0.7 < v < 1.4 for v in p.kappa.values()) and set(p.kappa) == {"ev", "pp", "sh", "ea", "en"}


def test_a_tampered_parameter_file_is_refused(tmp_path):
    d = json.loads(TM.PARAMS_PATH.read_text())
    d["kappa"]["ev"] = 1.5
    f = tmp_path / "p.json"
    f.write_text(json.dumps(d))
    with pytest.raises(ValueError, match="fingerprint"):
        TM.load_params(f)


def test_clock_is_a_physical_partition_with_the_cross_team_identities():
    """For any matchup: each team's states sum to 60 + E[OT]; A's power play is B's short-handed time; A's empty-net-against time is B's extra-attacker time."""
    prm, rng = _prm(), random.Random(7)
    for _ in range(2000):
        a, b = rng.uniform(2.6, 6.5), rng.uniform(2.6, 6.5)
        ca, cb = TM.clock(a, b, prm), TM.clock(b, a, prm)                        # team A's view and team B's view of the SAME game
        for c in (ca, cb):
            assert abs(c["ev"] + c["pp"] + c["sh"] + c["ea"] + c["en"] - (60.0 + prm.ot_min)) < 1e-9
            assert c["ev"] > 30 and c["fallback"] is False
        assert ca["pp"] == cb["sh"] and ca["sh"] == cb["pp"]                      # PP_A == SH_B, PP_B == SH_A
        assert ca["ea"] == cb["en"] and ca["en"] == cb["ea"]
        assert ca["ev"] == cb["ev"]                                               # even strength is one clock for both teams


def test_overtime_is_a_memo_not_an_addition():
    out = TM.allocate(4.7, 4.7, _prm())
    assert out["ot"] == 0.0 and set(out) == {"ev", "pp", "sh", "ea", "en", "ot"}
    assert sum(out.values()) < sum(TM.legacy(0.215).values()) + 5            # no template adds 1.2 on top of minutes that already contain overtime


@pytest.mark.parametrize("a,b", [(None, 4.6), (4.6, None), (None, None), (float("nan"), 4.6), (0.0, 4.6), (-1.0, 4.6), (1e9, 4.6), ("x", 4.6), (0.1, 0.1)])
def test_missing_or_broken_inputs_fall_back_to_the_league_clock(a, b):
    prm = _prm()
    c = TM.clock(a, b, prm)
    assert c["fallback"] is True and c["pp"] == c["sh"] == prm.league_pp_min
    assert abs(c["ev"] + c["pp"] + c["sh"] + c["ea"] + c["en"] - (60.0 + prm.ot_min)) < 1e-9
    out = TM.allocate(a, b, prm)
    assert all(v == v and v >= 0 for v in out.values())


def test_allocation_is_deterministic():
    prm = _prm()
    assert TM.allocate(4.9, 4.2, prm) == TM.allocate(4.9, 4.2, prm) == TM.allocate(4.9, 4.2, TM.load_params())


# ---- the registry gate ---------------------------------------------------------------------------------------------------------------------------------
def _registry(tmp_path, published="team-minutes-1.0", approval=None, candidate="team-minutes-1.0"):
    p = tmp_path / "r.json"
    p.write_text(json.dumps({"schema": "projection-registry-1", "targets": {"player_team_minutes": {"published_model": published, "candidate": candidate, "approval": approval}}}))
    return p


def test_the_committed_registry_publishes_the_legacy_template_without_approval():
    d = json.loads((REPO / "data" / "registry" / "projection-registry.json").read_text())
    e = d["targets"]["player_team_minutes"]
    assert e["published_model"] == "team-minutes-0" and e["candidate"] == "team-minutes-1.0" and e["approval"] is None
    assert PR.published_team_minutes() == ("team-minutes-0", None)
    assert PR.published_model("overtime") == ("DATA_ONLY_V1", None)           # the overtime target is untouched


def test_a_request_without_a_complete_approval_is_ignored_and_says_why(tmp_path):
    for appr in (None, {}, {"approved_by": "owner"}, {**APPROVAL, "evidence": " "}, {**APPROVAL, "approved_by": "PENDING owner approval"}, {**APPROVAL, "evidence": "TBD"}):
        model, why = PR.published_team_minutes(_registry(tmp_path, approval=appr))
        assert model == "team-minutes-0" and "no complete approval" in why
    assert PR.published_team_minutes(_registry(tmp_path, published="other", approval=APPROVAL))[0] == "team-minutes-0"
    assert PR.published_team_minutes(tmp_path / "missing.json")[0] == "team-minutes-0"
    assert PR.published_team_minutes(_registry(tmp_path, approval=APPROVAL)) == ("team-minutes-1.0", None)       # approval is the ONLY thing that switches it


def test_rollback_is_one_value_in_one_file(tmp_path):
    p = _registry(tmp_path, approval=APPROVAL)
    assert PR.published_team_minutes(p)[0] == "team-minutes-1.0"
    d = json.loads(p.read_text())
    d["targets"]["player_team_minutes"]["published_model"] = "team-minutes-0"
    p.write_text(json.dumps(d))
    assert PR.published_team_minutes(p) == ("team-minutes-0", None)


def test_resolve_falls_back_to_legacy_when_candidate_parameters_are_unavailable(tmp_path, monkeypatch):
    from nhl_edge.workflows import shadow_player

    monkeypatch.setattr(PR, "REGISTRY_PATH", _registry(tmp_path, approval=APPROVAL))
    pub, prm, why = shadow_player.resolve_team_minutes()
    assert pub == "team-minutes-1.0" and prm is not None and why is None
    monkeypatch.setattr(TM, "PARAMS_PATH", tmp_path / "missing.json")
    pub, prm, why = shadow_player.resolve_team_minutes()
    assert pub == "team-minutes-0" and prm is None and "parameters unavailable" in why
    monkeypatch.setattr(PR, "REGISTRY_PATH", tmp_path / "nope.json")
    assert shadow_player.resolve_team_minutes()[0] == "team-minutes-0"


# ---- the prospective player-minutes comparators stay on the incumbent ---------------------------------------------------------------------------------------
def test_player_minutes_comparators_read_the_legacy_fields_when_a_new_allocation_is_published():
    from nhl_edge.research.player_minutes_shadow import _incumbent_minutes

    default_row = {"meta_expected_toi_min": 17.2, "meta_expected_pp_toi_min": 2.1}
    assert _incumbent_minutes(default_row) == (17.2, 2.1)                           # the default: unchanged behaviour
    assert _incumbent_minutes({"meta_expected_toi_min": 17.2}) == (17.2, None)
    pinned = {"meta_expected_toi_min": 18.0, "meta_expected_pp_toi_min": 2.6, "meta_expected_toi_min_legacy": 17.2, "meta_expected_pp_toi_min_legacy": 2.1, "meta_team_minutes_version": "team-minutes-1.0"}
    assert _incumbent_minutes(pinned) == (17.2, 2.1)


# ---- the shadow arithmetic is exactly build_roster's -----------------------------------------------------------------------------------------------------
@pytest.mark.skipif(not (REPO / "data" / "history" / "players").exists(), reason="player history not present")
def test_project_player_equals_build_roster_for_any_team_minute_dict():
    import numpy as np

    from nhl_edge.players.features import PlayerBook, PlayerParams, league_priors
    from nhl_edge.players.roster import build_roster
    from nhl_edge.research.player_walk_forward import Data

    data = Data(REPO / "data" / "history", seasons=[2024, 2025], xg_train=(2024,))
    pg = data.pg
    book = PlayerBook(pg, league_priors(pg, data.goals), PlayerParams())
    last = pg[pg["game_id"] == pg["game_id"].max()]
    team = int(last["team_id"].iloc[0])
    ppl = [{"player_id": int(r.player_id), "name": r.name, "position": r.position} for r in last[last["team_id"] == team].itertuples(index=False)]
    di = int(pg["date_int"].max()) + 1
    prm = _prm()
    for tm in (TM.legacy(0.215), TM.legacy(0.3), TM.allocate(4.9, 4.4, prm), TM.allocate(None, None, prm)):
        rb = build_roster(book, team, "T", di, ppl, None, 0.2, 0.03, tm, season=2025)
        for p in ppl:
            pid = p["player_id"]
            m, mine = rb.player_meta[pid], TM.project_player(rb.player_meta[pid]["share"], rb.profiles[pid], book.priors, tm)
            assert mine["toi"] == m["expected_toi_total_min"] and mine["sog"] == m["expected_sog"]
            assert {s: mine[s] for s in TM.STATES} == m["expected_toi_min"]
    # the simulation never reads team minutes: the same roster built under two allocations has identical scorer / assist weights and co-ice
    a = build_roster(book, team, "T", di, ppl, None, 0.2, 0.03, TM.legacy(0.2), season=2025).roster
    b = build_roster(book, team, "T", di, ppl, None, 0.2, 0.03, TM.allocate(4.9, 4.4, prm), season=2025).roster
    for f in ("w_goal", "a1", "a2", "F", "toi_sigma", "p_exit", "unassisted", "no_a2"):
        assert np.array_equal(getattr(a, f), getattr(b, f))
    assert a.p_pp == b.p_pp and a.p_sh == b.p_sh


# ---- the real RUN NHL path -------------------------------------------------------------------------------------------------------------------------------
REPO_DATA = REPO / "data"
slow_needs = pytest.mark.skipif(not (REPO_DATA / "history" / "players").exists() or not (REPO_DATA / "params" / "player-sim-1.0.json").exists(), reason="player history / params not present")


def _run(tmp_path, name, monkeypatch, published):
    from nhl_edge.archive.ledger import Ledger
    from nhl_edge.workflows.simulate import run_simulate
    from tests.archive_fixture import NOW, build_archive
    from tests.test_player_shadow import _player_fixture

    monkeypatch.setenv("NHL_EDGE_PLAYER_SHADOW", "1")
    monkeypatch.setenv("NHL_EDGE_V2_SHADOW", "1")
    root = tmp_path / name
    build_archive(root)
    _player_fixture(root)
    if published != "team-minutes-0":
        monkeypatch.setattr(PR, "REGISTRY_PATH", _registry(tmp_path, published=published, approval=APPROVAL))
    else:
        monkeypatch.setattr(PR, "REGISTRY_PATH", REPO / "data" / "registry" / "projection-registry.json")
    assert run_simulate(root, REPO_DATA, date="2026-09-29", n_sims=1000, now=NOW) == 0
    led = Ledger(root)
    strip = lambda rows: sorted(({k: v for k, v in r.items() if k not in ("prediction_id", "_run_id", "run_id", "_observed_at_utc", "input_snapshot_ids")} for r in rows), key=lambda r: json.dumps(r, sort_keys=True, default=str))  # noqa: E731
    return {"player": strip(led.iter_rows("predictions_player")), "shadow": strip(led.iter_rows("player_tm_shadow")), "v1": strip(led.iter_rows("predictions")),
            "v2": strip(led.iter_rows("predictions_v2")), "slate": json.loads((root / "slates" / "latest" / "slate.json").read_text())}


PRICE_FIELDS = ("p_player", "p_player_se", "priced", "p_market_anchored", "player_minus_market", "edge_yes_raw", "edge_no_raw", "edge_yes_after_fee", "edge_no_after_fee")
GOAL_META = ("meta_expected_goals", "meta_expected_assists", "meta_expected_points", "meta_expected_saves", "meta_expected_shots_faced", "meta_pull_risk")


@slow_needs
@pytest.mark.slow
def test_goals_assists_points_and_every_price_are_bit_identical_under_either_allocation(tmp_path, monkeypatch):
    a = _run(tmp_path, "legacy", monkeypatch, "team-minutes-0")
    b = _run(tmp_path, "cand", monkeypatch, "team-minutes-1.0")
    assert a["player"] and len(a["player"]) == len(b["player"])
    assert a["v1"] == b["v1"] and a["v2"] == b["v2"]                                           # V1 / V2 rows: untouched
    for ra, rb in zip(a["player"], b["player"]):
        assert ra["ticker"] == rb["ticker"]
        for k in PRICE_FIELDS + GOAL_META:
            assert ra.get(k) == rb.get(k), (ra["ticker"], k)                                  # prices, edges, goals, assists, points, saves: identical to the last bit
    moved = [(ra, rb) for ra, rb in zip(a["player"], b["player"]) if ra.get("meta_expected_toi_min") is not None]
    assert moved and any(ra["meta_expected_toi_min"] != rb["meta_expected_toi_min"] for ra, rb in moved)           # ... while the ice-time field does move
    assert any(ra["meta_expected_shots"] != rb["meta_expected_shots"] for ra, rb in moved)
    # at the default nothing is added to a published row; once a non-default allocation is published the legacy-equivalent fields appear (comparator pin)
    assert not any(k.startswith("meta_team_minutes") or k.endswith("_legacy") for r in a["player"] for k in r)
    for ra, rb in moved:
        assert rb["meta_team_minutes_version"] == "team-minutes-1.0"
        assert rb["meta_expected_toi_min_legacy"] == ra["meta_expected_toi_min"] and rb["meta_expected_pp_toi_min_legacy"] == ra["meta_expected_pp_toi_min"]
        assert rb["meta_expected_shots_legacy"] == ra["meta_expected_shots"]


@slow_needs
@pytest.mark.slow
def test_the_shadow_record_is_allocation_agnostic_and_matches_the_published_fields(tmp_path, monkeypatch):
    a = _run(tmp_path, "legacy", monkeypatch, "team-minutes-0")
    b = _run(tmp_path, "cand", monkeypatch, "team-minutes-1.0")
    assert a["shadow"] and len(a["shadow"]) == len(b["shadow"])
    strip = lambda rows: [{k: v for k, v in r.items() if k != "published_allocation"} for r in rows]  # noqa: E731
    assert strip(a["shadow"]) == strip(b["shadow"])                                           # both arms are recorded identically whichever one is published
    assert {r["published_allocation"] for r in a["shadow"]} == {"team-minutes-0"} and {r["published_allocation"] for r in b["shadow"]} == {"team-minutes-1.0"}
    by = {(r["game_id"], r["player_id"]): r for r in a["shadow"]}
    assert len(by) == len(a["shadow"])                                                        # no duplicate (game, player) in one run
    for r in a["player"]:
        if r.get("meta_expected_toi_min") is None or r.get("player_resolution") is None:
            continue
        s = by.get((r["game_id"], r["player_id"]))
        if s is not None:
            assert round(s["legacy_toi"], 2) == r["meta_expected_toi_min"] and round(s["legacy_pp"], 2) == r["meta_expected_pp_toi_min"] and round(s["legacy_sog"], 2) == r["meta_expected_shots"]
    for r in b["player"]:
        if r.get("meta_expected_toi_min") is None:
            continue
        s = by.get((r["game_id"], r["player_id"]))
        if s is not None:
            assert round(s["cand_toi"], 2) == r["meta_expected_toi_min"] and round(s["cand_pp"], 2) == r["meta_expected_pp_toi_min"] and round(s["cand_sog"], 2) == r["meta_expected_shots"]
    for s in a["shadow"]:
        assert s["authority"] == "RESEARCH_ONLY" and s["role"] == "SHADOW" and s["candidate_version"] == "team-minutes-1.0" and s["pregame"] is True
        assert s["cand_team_pp"] > s["legacy_team_pp"] and 0 < s["minutes_to_start"] <= 360


@slow_needs
@pytest.mark.slow
def test_default_slate_document_gains_no_keys_and_runs_are_reproducible(tmp_path, monkeypatch):
    a1 = _run(tmp_path, "r1", monkeypatch, "team-minutes-0")
    a2 = _run(tmp_path, "r2", monkeypatch, "team-minutes-0")
    assert a1["player"] == a2["player"] and a1["shadow"] == a2["shadow"]                       # deterministic
    ps = a1["slate"]["player_shadow"]
    assert "tm_shadow" not in ps and "tm_info" not in ps and "team_minutes_version" not in json.dumps(a1["slate"])
    assert "projection_registry" not in a1["slate"]


@slow_needs
@pytest.mark.slow
def test_a_failing_candidate_never_changes_the_published_fields(tmp_path, monkeypatch):
    base = _run(tmp_path, "ok", monkeypatch, "team-minutes-0")

    def boom(*a, **k):
        raise RuntimeError("synthetic allocation failure")

    monkeypatch.setattr(TM, "allocate", boom)
    broken = _run(tmp_path, "broken", monkeypatch, "team-minutes-0")
    assert broken["player"] == base["player"] and broken["v1"] == base["v1"] and broken["v2"] == base["v2"]
    assert len(broken["shadow"]) == 1 and broken["shadow"][0]["marker"] is True and broken["shadow"][0]["n_errors"] > 0     # nothing recorded but a visible marker; nothing published differently
    approved = _run(tmp_path, "broken_approved", monkeypatch, "team-minutes-1.0")             # even when the candidate is APPROVED, a per-game allocation failure falls back to legacy
    assert [{k: v for k, v in r.items() if not k.startswith("meta_team_minutes") and not k.endswith("_legacy")} for r in approved["player"]] == base["player"]


def test_approval_must_pin_the_parameter_fingerprint_and_unknown_allocations_are_refused(tmp_path, monkeypatch):
    from nhl_edge.workflows import shadow_player

    monkeypatch.setattr(PR, "REGISTRY_PATH", _registry(tmp_path, approval={k: v for k, v in APPROVAL.items() if k != "candidate_fingerprint"}))
    pub, prm, why = shadow_player.resolve_team_minutes()
    assert pub == "team-minutes-0" and "pin" in why and prm is not None                      # approved, but not for these parameters
    monkeypatch.setattr(PR, "REGISTRY_PATH", _registry(tmp_path, approval={**APPROVAL, "candidate_fingerprint": "0" * 16}))
    assert shadow_player.resolve_team_minutes()[0] == "team-minutes-0"
    monkeypatch.setattr(PR, "REGISTRY_PATH", _registry(tmp_path, published="team-minutes-2.0", candidate="team-minutes-2.0", approval=APPROVAL))
    pub, _, why = shadow_player.resolve_team_minutes()
    assert pub == "team-minutes-0" and "does not implement" in why
    monkeypatch.setattr(PR, "REGISTRY_PATH", _registry(tmp_path, approval=APPROVAL))
    assert shadow_player.resolve_team_minutes()[0] == "team-minutes-1.0"


def test_parameter_file_is_validated(tmp_path):
    d = json.loads(TM.PARAMS_PATH.read_text())
    cases = []
    no_fp = {k: v for k, v in d.items() if k != "fingerprint"}
    cases.append(no_fp)
    nan = json.loads(json.dumps(d))
    nan["kappa"]["pp"] = float("nan")
    cases.append(nan)
    wild = json.loads(json.dumps(d))
    wild["kappa"]["ev"] = 9.0
    p = TM.AllocationParams.from_dict(wild)
    cases.append({**wild, "fingerprint": p.fingerprint()})                                  # a rewritten file with a recomputed fingerprint
    for i, c in enumerate(cases):
        f = tmp_path / f"p{i}.json"
        f.write_text(json.dumps(c))
        with pytest.raises(ValueError):
            TM.load_params(f)


def test_numpy_scalars_are_accepted_and_booleans_are_not():
    import numpy as np

    prm = _prm()
    assert TM.clock(np.float32(4.7), np.float64(4.5), prm)["fallback"] is False
    assert TM.clock(np.int64(5), 5, prm)["fallback"] is False
    assert TM.clock(True, 4.5, prm)["fallback"] is True


def test_kappa_scaled_totals_stay_close_to_the_physical_budget():
    prm, rng = _prm(), random.Random(11)
    for _ in range(500):
        a, b = rng.uniform(2.8, 6.2), rng.uniform(2.8, 6.2)
        tot = sum(v for k, v in TM.allocate(a, b, prm).items() if k != "ot")
        assert 0.97 * (60 + prm.ot_min) < tot < 1.03 * (60 + prm.ot_min)


def test_deepcopy_of_params_is_stable():
    p = _prm()
    q = replace(p, kappa=copy.deepcopy(p.kappa))
    assert q.fingerprint() == p.fingerprint()


def test_the_activation_template_cannot_activate_until_the_owner_fills_the_approval(tmp_path):
    import shutil
    import subprocess

    if shutil.which("patch") is None:
        pytest.skip("patch not installed")
    reg = tmp_path / "data" / "registry"
    reg.mkdir(parents=True)
    shutil.copy(REPO / "data" / "registry" / "projection-registry.json", reg / "projection-registry.json")
    subprocess.run(["patch", "-p1", "-d", str(tmp_path), "-i", str(REPO / "docs" / "research" / "team_minutes" / "ACTIVATION.patch")], check=True, capture_output=True)
    f = reg / "projection-registry.json"
    d = json.loads(f.read_text())
    assert d["targets"]["player_team_minutes"]["published_model"] == "team-minutes-1.0"                  # the template switches the value ...
    model, why = PR.published_team_minutes(f)
    assert model == "team-minutes-0" and "no complete approval" in why                                    # ... but, as committed, the gate still refuses it
    assert PR.published_model("overtime", f) == ("DATA_ONLY_V1", None)                                    # and the overtime target is untouched by it
    d["targets"]["player_team_minutes"]["approval"] = APPROVAL
    f.write_text(json.dumps(d))
    assert PR.published_team_minutes(f) == ("team-minutes-1.0", None)


@slow_needs
@pytest.mark.slow
def test_a_degraded_shadow_leaves_a_visible_marker_and_never_changes_published_rows(tmp_path, monkeypatch):
    base = _run(tmp_path, "ok", monkeypatch, "team-minutes-0")
    monkeypatch.setattr(TM, "PARAMS_PATH", tmp_path / "missing.json")
    broken = _run(tmp_path, "nopar", monkeypatch, "team-minutes-0")
    assert broken["player"] == base["player"] and broken["v1"] == base["v1"] and broken["v2"] == base["v2"]
    assert len(broken["shadow"]) == 1 and broken["shadow"][0]["marker"] is True
    assert broken["shadow"][0]["candidate_available"] is False and "parameters unavailable" in broken["shadow"][0]["default_reason"]
