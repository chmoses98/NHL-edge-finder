"""NHL_SCRIPT_V1: partition, precedence, determinism, realised classification, script-conditioned pricing, survival, ranking,
exposure groups and dependency flags (synthetic draws; no network, no live slate)."""

from __future__ import annotations

import numpy as np
import pytest

from nhl_edge.kalshi.fees import DEFAULT_SCHEDULE, fee_per_contract_dollars
from nhl_edge.scripts_v1 import REALIZED_VERSION, SCRIPT_VERSION
from nhl_edge.scripts_v1.build import forecast_row, game_research
from nhl_edge.scripts_v1.candidates import build_candidates, dependency_flags, exposure_groups
from nhl_edge.scripts_v1.survival import (
    DOES_NOT_SURVIVE,
    FRAGILE,
    MIN_EV,
    MODERATE,
    ROBUST,
    UNAVAILABLE,
    conditional_matrix,
    data_quality,
    game_survival,
    side_survival,
    tier_for,
)
from nhl_edge.scripts_v1.taxonomy import (
    BY_ID,
    N_SCRIPTS,
    SCRIPTS,
    base_rates,
    classify,
    frequencies,
    realized,
    taxonomy_doc,
)
from nhl_edge.thesis.engine import GameDistribution
from nhl_edge.thesis.expression import economics
from nhl_edge.thesis.features import DrawFeatures
from nhl_edge.thesis.mapping import Bet
from tests.test_thesis_core import synth_features


def _games(rows: list[tuple]) -> DrawFeatures:
    """rows: (home goals, away goals, home net faced, away net faced, ot, home pp, away pp). Non-shootout games."""
    n = len(rows)
    a = lambda i, dt=np.int64: np.array([r[i] for r in rows], dtype=dt)  # noqa: E731
    hg, ag, ot = a(0), a(1), a(4, bool)
    z = np.zeros(n, dtype=np.int64)
    return DrawFeatures("HOM", "AWY", 1, 2, hg, ag, hg, ag, hg - (ot & (hg > ag)), ag - (ot & (ag > hg)), ot, np.zeros(n, bool), a(2), a(3),
                        a(5), a(6), z, z, np.ones(n, np.int8), z, z, np.ones(n, bool), a(2) - ag, a(3) - hg)


def mk_bet(bid: str, y: np.ndarray, price: int, mid: float | None = None, family: str = "game_winner", team: str | None = None, **meta) -> Bet:
    side = bid.split("|")[-1]
    return Bet(bid, bid.split("|")[0], side, bid.split("|")[0], family, "G1", y.astype(bool), float(y.mean()), price,
               fee_per_contract_dollars(price, DEFAULT_SCHEDULE), price / 100.0 if mid is None else mid, team, None, dict(meta))


# ------------------------------------------------------------------------------------------------ taxonomy
def test_partition_is_exclusive_exhaustive_and_deterministic():
    f = synth_features(6000)
    a, b = classify(f), classify(f)
    assert np.array_equal(a, b)
    assert a.min() >= 0 and a.max() < N_SCRIPTS
    freq = frequencies(a)
    assert freq.sum() == pytest.approx(1.0, abs=1e-12)
    assert np.bincount(a, minlength=N_SCRIPTS).sum() == f.n  # every draw has exactly one script
    assert [s.code for s in SCRIPTS] == list(range(N_SCRIPTS)) and SCRIPTS[-1].id == "BACK_AND_FORTH"


def test_precedence_rules_on_hand_built_games():
    rows = [
        (3, 1, 25, 25, False, 2, 0),   # home 2 PP of 3 goals -> SPECIAL_TEAMS beats everything
        (5, 4, 30, 30, False, 1, 1),   # 9 goals -> OPEN_GAME
        (2, 1, 30, 30, False, 0, 0),   # 3 goals, one-goal -> TIGHT_LOW_EVENT
        (3, 2, 40, 20, False, 0, 0),   # home wins with 20/(20+40)=33% of shots -> GOALIE_DRIVEN
        (4, 1, 22, 30, False, 0, 0),   # home wins by 3 with 30/52 = 58% of shots -> HOME_CONTROL
        (1, 4, 32, 26, False, 0, 0),   # away wins by 3 with 32/58 = 55% -> AWAY_CONTROL
        (4, 3, 28, 27, False, 0, 0),   # 7 goals, one-goal, even -> BACK_AND_FORTH
        (3, 2, 30, 30, True, 0, 0),    # OT, 5 goals -> BACK_AND_FORTH (not tight-low: 5 > 4)
    ]
    want = ["SPECIAL_TEAMS", "OPEN_GAME", "TIGHT_LOW_EVENT", "GOALIE_DRIVEN", "HOME_CONTROL", "AWAY_CONTROL", "BACK_AND_FORTH", "BACK_AND_FORTH"]
    assert [SCRIPTS[c].id for c in classify(_games(rows))] == want


def test_labels_are_team_specific_and_base_rates_are_frozen():
    doc = taxonomy_doc("CAR", "NYR")
    assert {d["id"]: d["label"] for d in doc}["HOME_CONTROL"] == "CAR controls and pulls away"
    assert {d["id"]: d["label"] for d in doc}["AWAY_CONTROL"] == "NYR controls and pulls away"
    br = base_rates()
    assert br["script_version"] == SCRIPT_VERSION and br["n_games"] > 5000
    assert sum(br["frequency"].values()) == pytest.approx(1.0, abs=2e-3)
    assert set(br["frequency"]) == set(BY_ID)
    assert all(0.05 <= v <= 0.30 for v in br["frequency"].values())  # every script is a real, reasonably common game type


def test_realized_classifier_uses_the_pregame_rule_on_one_final():
    res = {"home_team_id": 1, "away_team_id": 2, "home_final": 4, "away_final": 1, "last_period_type": "REG"}
    goals = [{"team_id": 1, "period": p, "period_type": "REG", "t_s": t, "strength": "EV", "empty_net": False} for p, t in ((1, 300), (2, 1500), (3, 2800), (3, 3500))]
    goals.append({"team_id": 2, "period": 2, "period_type": "REG", "t_s": 2000, "strength": "EV", "empty_net": False})
    goalies = [{"team_id": 1, "shots_against": 24, "saves": 23, "starter": True}, {"team_id": 2, "shots_against": 33, "saves": 29, "starter": True}]
    f = DrawFeatures.from_actual(res, goals, goalies, "HOM", "AWY")
    rz = realized(f)
    assert rz["script_id"] == "HOME_CONTROL" and rz["realized_version"] == REALIZED_VERSION
    assert rz["metrics"]["home_shots"] == 33 and rz["metrics"]["total_goals"] == 5
    with pytest.raises(ValueError):
        realized(synth_features(10))


# ------------------------------------------------------------------------------------------------ survival
def test_conditional_matrix_reconciles_and_ev_identity_holds():
    f = synth_features(5000)
    codes = classify(f)
    y = f.winner == 1
    P, counts, n_s = conditional_matrix(np.stack([y, ~y]), codes)
    assert counts.sum(axis=1).tolist() == [int(y.sum()), int((~y).sum())]  # integer counts reconcile to P(bet)
    freq = frequencies(codes)
    assert float(np.nansum(freq * P[0])) == pytest.approx(float(y.mean()), abs=1e-9)
    b = mk_bet("ML|yes", y, 50, mid=0.50)
    e = economics(b, "EVIDENCE_MIXED", "D")
    sv = side_survival(b.bet_id, b.p, P[0], freq, e.p_adj, b.cost, "OK")
    assert sv.expected_ev == pytest.approx(e.ev_adj, abs=1e-9)  # sum_s freq_s EV(b|s) == adjusted EV
    # the home moneyline can never win a script where the away team controls and pulls away
    assert P[0][BY_ID["AWAY_CONTROL"].code] == 0.0 and P[0][BY_ID["HOME_CONTROL"].code] == 1.0


def test_yes_no_sides_use_their_own_ask_and_fee():
    f = synth_features(3000)
    y = f.total >= 7
    yes, no = mk_bet("T|yes", y, 40), mk_bet("T|no", ~y, 64)
    assert yes.cost == pytest.approx(0.40 + fee_per_contract_dollars(40, DEFAULT_SCHEDULE))
    assert no.cost == pytest.approx(0.64 + fee_per_contract_dollars(64, DEFAULT_SCHEDULE))
    surv, P, _ = game_survival([yes, no], {b.bet_id: economics(b, "EVIDENCE_MIXED", "D") for b in (yes, no)}, classify(f))
    assert np.allclose(P[0] + P[1], 1.0, equal_nan=True)
    for b in (yes, no):
        sv = surv[b.bet_id]
        assert sv.cost == pytest.approx(b.cost)
        assert np.allclose(sv.ev_by_script, P[0 if b.side == "yes" else 1] - sv.delta - b.cost, equal_nan=True)
    assert surv["T|yes"].survives[BY_ID["OPEN_GAME"].code] != surv["T|no"].survives[BY_ID["OPEN_GAME"].code]


def test_data_quality_gates_and_unsupported_prices_fail_closed():
    assert data_quality({}, None) == "NO_EXECUTABLE_PRICE"
    assert data_quality({"stale": True}, 0.5) == "STALE_QUOTE"
    assert data_quality({"crossed": True}, 0.5) == "CROSSED_BOOK"
    assert data_quality({"not_pregame": True}, 0.5) == "NOT_PREGAME"
    f = synth_features(2000)
    y = f.winner == 1
    stale = mk_bet("S|yes", y, 30, stale=True)
    surv, _, _ = game_survival([stale], {stale.bet_id: economics(stale, "EVIDENCE_MIXED", "D")}, classify(f))
    assert surv[stale.bet_id].tier == UNAVAILABLE and not surv[stale.bet_id].survives.any()
    noprice = Bet("N|yes", "N", "yes", "N", "game_winner", "G1", y, float(y.mean()), None, None, None)
    surv, _, _ = game_survival([noprice], {}, classify(f))
    assert surv["N|yes"].tier == UNAVAILABLE and surv["N|yes"].ev_by_script is None


def test_robustness_tiers_are_mass_based():
    assert tier_for(0.03, 0.80, 4, "OK") == ROBUST
    assert tier_for(0.015, 0.80, 4, "OK") == MODERATE  # a robust spread of scripts with a sub-2c edge is not ROBUST
    assert tier_for(0.05, 0.50, 3, "OK") == MODERATE
    assert tier_for(0.07, 0.30, 1, "OK") == FRAGILE  # big edge, one narrow script
    assert tier_for(0.07, 0.90, 1, "OK") == FRAGILE  # mass from one script alone is not robust
    assert tier_for(-0.01, 0.60, 4, "OK") == DOES_NOT_SURVIVE
    assert tier_for(0.05, 0.9, 5, "STALE_QUOTE") == UNAVAILABLE


# ------------------------------------------------------------------------------------------------ candidates
def _analysis(f: DrawFeatures, bets: list[Bet], statuses: dict[str, str], pairs: list[dict] | None = None) -> dict:
    gd = GameDistribution("G1", "HOM", "AWY", 1, 2, f, bets, [], {}, {"context": {"goalies": {"home": {"status": "CONFIRMED"}, "away": {"status": "UNKNOWN"}}}})
    econ = {b.bet_id: economics(b, "EVIDENCE_MIXED", "D") for b in bets}
    return {"gd": gd, "bets": bets, "econ": econ, "rel": {b.bet_id: "EVIDENCE_MIXED" for b in bets}, "bench": {b.bet_id: "D" for b in bets},
            "short": bets, "research": {b.bet_id: {"status": statuses.get(b.bet_id, "SHADOW_ONLY"), "reasons": [], "research_stake_dollars": 0} for b in bets},
            "joint": {"pairs": pairs or []}, "fidelity": {}, "profiles": {}}


def test_robust_smaller_edge_outranks_fragile_bigger_edge():
    f = synth_features(8000, seed=11)
    codes = classify(f)
    rng = np.random.default_rng(3)
    broad = rng.random(f.n) < 0.55  # wins ~55% everywhere
    narrow = codes == BY_ID["OPEN_GAME"].code  # wins only in the open-game script
    b1 = mk_bet("BROAD|yes", broad, 47, mid=0.47)  # +8c raw, broad
    b2 = mk_bet("NARROW|yes", narrow, int(round(100 * narrow.mean())) - 8, mid=narrow.mean() - 0.07)  # big raw edge, one script
    a = _analysis(f, [b2, b1], {})
    gr_survival, _, _ = game_survival(a["bets"], a["econ"], codes)
    assert gr_survival["NARROW|yes"].tier == FRAGILE and a["econ"]["NARROW|yes"].ev_adj > a["econ"]["BROAD|yes"].ev_adj
    assert gr_survival["BROAD|yes"].tier in (ROBUST, MODERATE)
    cands = build_candidates(a, gr_survival, {"home": "HOM", "away": "AWY", **a["gd"].meta["context"]})
    assert [c["bet_id"] for c in cands][:2] == ["BROAD|yes", "NARROW|yes"]
    c = cands[0]
    assert c["authority"] == "RESEARCH_ONLY" and c["governance"]["stake_kind"].startswith("shadow")
    assert any("Fails mainly if" in o["text"] for o in cands[1]["opposing"])
    assert all(s["basis"] in ("MODEL", "SIMULATION", "MARKET", "CALIBRATION", "HELD_OUT_EVALUATION", "GOVERNANCE") for s in c["supporting"])


def test_exposure_groups_flag_the_same_bet_twice():
    pairs = [{"a": "A|yes", "b": "B|yes", "relationship": "DUPLICATIVE", "phi": 0.8}, {"a": "B|yes", "b": "C|yes", "relationship": "MOSTLY_INDEPENDENT", "phi": 0.05},
             {"a": "C|yes", "b": "D|yes", "relationship": "REINFORCING", "phi": 0.55}]
    g = exposure_groups(["A|yes", "B|yes", "C|yes", "D|yes"], pairs)
    assert g["A|yes"] == g["B|yes"] and g["C|yes"] == g["D|yes"] and g["A|yes"] != g["C|yes"]
    f = synth_features(4000)
    y = f.winner == 1
    a = _analysis(f, [mk_bet("ML|yes", y, 50, mid=0.47), mk_bet("PL|yes", y & (f.final_margin >= 2), 30, mid=0.27, family="game_spread")],
                  {}, [{"a": "ML|yes", "b": "PL|yes", "relationship": "DUPLICATIVE", "phi": 0.62, "script_overlap": 0.7}])
    surv, _, _ = game_survival(a["bets"], a["econ"], classify(f))
    cands = build_candidates(a, surv, {"home": "HOM", "away": "AWY"})
    dup = [c for c in cands if c["duplicate_of"]]
    assert len(dup) == 1 and dup[0]["relations"][0]["kind"] == "SAME_EXPOSURE" and "Highly correlated" in dup[0]["relations"][0]["text"]


def test_unknown_goalie_and_unconfirmed_role_are_dependency_flags():
    f = synth_features(500)
    b = mk_bet("G|yes", f.winner == 1, 50, role_confidence="MEDIUM", spread_cents=7)
    flags = {d["flag"] for d in dependency_flags(b, {"home": "HOM", "away": "AWY", "goalies": {"home": {"status": "UNKNOWN"}, "away": {"status": "CONFIRMED"}}})}
    assert "GOALIE_UNKNOWN_HOME" in flags and "WIDE_SPREAD" in flags and "GOALIE_CONFIRMED_AWAY" not in flags
    p = mk_bet("P|yes", f.winner == 1, 30, family="player_goals", role_confidence="MEDIUM", projection_quality="LOW")
    assert {"ROLE_NOT_CONFIRMED", "PROJECTION_QUALITY_LOW"} <= {d["flag"] for d in dependency_flags(p, {})}


def test_game_research_block_is_complete_deterministic_and_compactly_logged():
    f = synth_features(4000, seed=5)
    y = f.winner == 1
    t = f.total >= 7
    bets = [mk_bet("ML|yes", y, 50, mid=0.48), mk_bet("ML|no", ~y, 52, mid=0.52), mk_bet("TOT|yes", t, 40, mid=0.40, family="game_total"),
            mk_bet("TOT|no", ~t, 62, mid=0.60, family="game_total")]
    a = _analysis(f, bets, {"ML|yes": "FUNDED_RESEARCH"})
    a["short"] = [b for b in bets if a["econ"][b.bet_id].eligible]
    g1, g2 = game_research(a), game_research(a)
    assert g1 == g2
    assert g1["probability_check"]["sum"] == pytest.approx(1.0) and len(g1["scripts"]) == N_SCRIPTS
    assert sum(s["probability"] for s in g1["scripts"]) == pytest.approx(1.0, abs=1e-3)
    assert g1["scripts"][0]["probability"] >= g1["scripts"][-1]["probability"] and g1["most_likely"]["id"] == g1["scripts"][0]["id"]
    for s in g1["scripts"]:
        for k in ("id", "label", "probability", "summary", "needs", "breaks", "rule", "helps", "hurts", "total_goals_range", "league_base_rate"):
            assert k in s
    m = {r["ticker"]: r for r in g1["markets"]}
    assert len(m["ML"]["p_yes_by_script"]) == N_SCRIPTS and m["ML"]["yes"]["tier"] and m["ML"]["no"]["tier"]
    row = forecast_row(g1, decided_at="2026-10-06T22:00:00Z", run_id="r", snapshot_id="snap-x", start_time_utc="2026-10-06T23:00:00Z")
    assert sum(row["script_probabilities"].values()) == pytest.approx(1.0, abs=1e-3) and "markets" not in row
    assert all(c["robustness"] for c in row["candidates"])
    assert MIN_EV == 0.01
