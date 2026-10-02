"""Thesis card inside RUN NHL: never changes V1 / V2 / PLAYER_SIM_V1 rows, fails contained, is point-in-time safe, logs the
complete decision state, and the postmortem separates thesis from expression."""

from __future__ import annotations

import json
from datetime import timedelta

import numpy as np
import pytest

from nhl_edge.archive.ledger import Ledger
from nhl_edge.thesis.features import DrawFeatures
from nhl_edge.thesis.postmortem import actual_view, expression_label, portfolio_result, score_decision
from nhl_edge.timeutil import parse_iso
from nhl_edge.workflows.simulate import run_simulate
from tests.archive_fixture import NOW, build_archive
from tests.test_player_shadow import REPO_DATA, _player_fixture

pytestmark = pytest.mark.skipif(not (REPO_DATA / "history" / "players").exists(), reason="player history not present")

STRIP = ("prediction_id", "_run_id", "_observed_at_utc", "input_snapshot_ids")


def _rows(led: Ledger, kind: str) -> list[dict]:
    return [{k: v for k, v in r.items() if k not in STRIP} for r in sorted(led.iter_rows(kind), key=lambda r: r["ticker"])]


@pytest.mark.slow
def test_thesis_card_never_changes_model_rows_and_logs_decisions(tmp_path, monkeypatch):
    out = {}
    for flag in ("0", "1"):
        monkeypatch.setenv("NHL_EDGE_THESIS_CARD", flag)
        root = tmp_path / f"a{flag}"
        build_archive(root)
        _player_fixture(root)
        assert run_simulate(root, REPO_DATA, date="2026-09-29", n_sims=2000, now=NOW) == 0
        led = Ledger(root)
        out[flag] = (_rows(led, "predictions"), _rows(led, "predictions_v2"), _rows(led, "predictions_player"))
        slate = json.loads((root / "slates" / "latest" / "slate.json").read_text())
        if flag == "0":
            assert "thesis_card" not in slate and not list(led.iter_rows("thesis_decisions"))
            continue
        tc = slate["thesis_card"]
        assert tc["authority"] == "RESEARCH_ONLY" and tc["status"] in ("COMPLETE", "NO_BETS") and tc["gate"]["status"] == "PASS", tc
        packet = json.loads((root / "slates" / "latest" / "packet.json").read_text())
        g = packet["thesis_card"]["games"][0]
        assert g["scripts"] and abs(sum(s["frequency"] for s in g["scripts"]) - 1) < 1e-3
        assert g["full_board"] and {e["key"] for e in g["thesis_events"]} >= {"CAR:WINS", "FLA:WINS", "GAME:HIGH_EVENT"}
        assert (root / "slates" / "latest" / "card.md").exists()
        dec = list(led.iter_rows("thesis_decisions"))
        games = list(led.iter_rows("thesis_games"))
        assert dec and games
        for d in dec:
            # point-in-time: the decision is stamped at the cutoff and used a market board observed before it
            assert parse_iso(d["decided_at_utc"]) == NOW and parse_iso(d["market_observed_at_utc"]) < NOW
            assert parse_iso(d["decided_at_utc"]) < parse_iso(d["start_time_utc"])
            for k in ("p_model", "p_adjusted", "script_mapping", "p_win_by_script", "primary_thesis", "joint_relationships", "alternatives_considered", "chosen"):
                assert k in d
            assert (d["why_selected"] if d["chosen"] else d["why_rejected"])
            assert d["ev_raw"] > 0 and d["ev_adjusted"] > 0
    assert out["0"] == out["1"]


@pytest.mark.slow
def test_thesis_failure_never_breaks_model_arms(tmp_path, monkeypatch):
    from nhl_edge.workflows import thesis_card

    def boom(*a, **k):
        raise RuntimeError("synthetic thesis failure")

    monkeypatch.setattr(thesis_card, "run_thesis_card", boom)
    root = tmp_path / "a"
    build_archive(root)
    _player_fixture(root)
    assert run_simulate(root, REPO_DATA, date="2026-09-29", n_sims=500, now=NOW) == 0
    slate = json.loads((root / "slates" / "latest" / "slate.json").read_text())
    assert slate["thesis_card"]["status"] == "ERROR" and "synthetic thesis failure" in slate["thesis_card"]["error"]
    led = Ledger(root)
    assert list(led.iter_rows("predictions")) and list(led.iter_rows("predictions_v2")) and list(led.iter_rows("predictions_player"))


@pytest.mark.slow
def test_sportsbook_odds_observed_after_the_cutoff_are_invisible(tmp_path):
    root = tmp_path / "a"
    build_archive(root)
    _player_fixture(root)
    led = Ledger(root, run_id="later")
    odds = [{"game_id": "2026020001", "side": s, "team_id": t, "provider": "DraftKings", "value": v, "game_state": "PRE"}
            for s, t, v in (("home", 12, "-300"), ("away", 13, "+250"))]
    led.append_rows("context/sportsbook_odds", odds, observed_at=NOW + timedelta(minutes=30))
    assert run_simulate(root, REPO_DATA, date="2026-09-29", n_sims=500, now=NOW) == 0
    packet = json.loads((root / "slates" / "latest" / "packet.json").read_text())
    assert packet["thesis_card"]["games"][0]["sportsbook_consensus"] is None
    # observed before the cutoff: used
    root2 = tmp_path / "b"
    build_archive(root2)
    _player_fixture(root2)
    Ledger(root2, run_id="earlier").append_rows("context/sportsbook_odds", odds, observed_at=NOW - timedelta(minutes=30))
    assert run_simulate(root2, REPO_DATA, date="2026-09-29", n_sims=500, now=NOW) == 0
    c = json.loads((root2 / "slates" / "latest" / "packet.json").read_text())["thesis_card"]["games"][0]["sportsbook_consensus"]
    assert c is not None and c["p_home"] > 0.7


# ------------------------------------------------------------------------------------------------ postmortem
def _actual(home_goals: int, away_goals: int) -> dict:
    res = {"home_team_id": 1, "away_team_id": 2, "home_final": home_goals, "away_final": away_goals, "home_reg": home_goals, "away_reg": away_goals, "last_period_type": "REG"}
    goals = [{"team_id": 1, "period": 1 + i % 3, "period_type": "REG", "t_s": 100 + 500 * i, "strength": "EV", "empty_net": False} for i in range(home_goals)]
    goals += [{"team_id": 2, "period": 1, "period_type": "REG", "t_s": 50 + 10 * i, "strength": "EV", "empty_net": False} for i in range(away_goals)]
    goalies = [{"team_id": 1, "shots_against": 22, "saves": 22 - away_goals, "starter": True}, {"team_id": 2, "shots_against": 38, "saves": 38 - home_goals, "starter": True}]
    return actual_view(DrawFeatures.from_actual(res, goals, goalies, "PIT", "PHI"))


def test_postmortem_separates_thesis_from_expression():
    act = _actual(7, 0)  # PIT (home here) scores seven
    d = {"decision_id": "d1", "run_id": "r", "decided_at_utc": "2026-09-30T23:00:00Z", "game_id": "G", "bet_id": "RAKELL|yes", "ticker": "RAKELL", "side": "yes",
         "family": "player_goals", "chosen": True, "stake_dollars": 10.0, "p_model": 0.33, "p_adjusted": 0.30, "p_kalshi_mid": 0.27, "executable_price_cents": 27,
         "cost_per_contract": 0.2838, "primary_thesis": {"key": "PIT:OFFENSE_4PLUS", "p_bet_given_thesis": 0.52, "p_bet_given_not_thesis": 0.21},
         "secondary_thesis": None, "p_win_by_script": {}}
    s = score_decision(d, act, outcome_yes=False, close_prob=0.30)
    assert s["thesis_result"] is True and s["won"] is False
    assert s["expression_result"] == "THESIS_RIGHT_EXPRESSION_LOST"  # not "prediction wrong"
    assert s["model_p_bet_given_thesis_outcome"] == 0.52  # the model expected this expression to miss 48% of the time given the thesis
    assert s["price_result_clv"] == pytest.approx(0.03)
    assert s["realized_profit"] == pytest.approx(-10.0)
    assert expression_label(False, True) == "THESIS_WRONG_EXPRESSION_WON" and expression_label(None, False) == "NO_THESIS_LOST"
    s2 = score_decision(d | {"decision_id": "d2", "bet_id": "X|yes"}, act, outcome_yes=False, close_prob=None)
    pr = portfolio_result([s, s2], None)
    assert pr["theses_with_multiple_losses"] == ["PIT:OFFENSE_4PLUS"]
    assert pr["multiple_losses_on_one_thesis"][0]["thesis_happened"] is True and "expression risk" in pr["multiple_losses_on_one_thesis"][0]["reading"]


def test_actual_classification_uses_the_pregame_functions():
    act = _actual(7, 0)
    assert act["events"]["PIT:OFFENSE_4PLUS"] and act["events"]["PIT:WINS_BY_2PLUS"] and act["events"]["GAME:LOW_EVENT"] is False
    assert act["script_key"] == "CH|EN|MD"  # PIT 38 shots vs 22 -> PIT shot control, 7 goals -> normal, decided
    assert np.isfinite(act["summary"]["home_shots"])


@pytest.mark.slow
def test_replay_is_deterministic_and_rows_carry_snapshot_identity_and_research_state(tmp_path):
    """Two independent RUN NHL replays at one cutoff give byte-identical thesis cards (seeded joint draws, point-in-time
    inputs); every decision row of a generation carries its snapshot id, research status and a $0 stake unless funded."""
    from nhl_edge.workflows.thesis_card import snapshot_id

    cards = []
    for k in ("a", "b"):
        root = tmp_path / k
        build_archive(root)
        _player_fixture(root)
        assert run_simulate(root, REPO_DATA, date="2026-09-29", n_sims=2000, now=NOW) == 0
        tc = json.loads((root / "slates" / "latest" / "packet.json").read_text())["thesis_card"]
        tc.pop("timings_ms", None)
        for g in tc["games"]:
            g.pop("timings_ms", None)
        tc.pop("run_id", None)
        tc.pop("snapshot_id", None)
        cards.append(json.dumps(tc, sort_keys=True, default=str))
        led = Ledger(root)
        dec = list(led.iter_rows("thesis_decisions"))
        games = list(led.iter_rows("thesis_games"))
        sids = {d["snapshot_id"] for d in dec} | {g["snapshot_id"] for g in games}
        assert sids == {snapshot_id(dec[0]["run_id"], dec[0]["decided_at_utc"])}
        for d in dec:
            assert d["research_status"] in ("FUNDED_RESEARCH", "SHADOW_ONLY", "REJECTED") and isinstance(d["research_stake_dollars"], int)
            assert d["research_status"] == "FUNDED_RESEARCH" or d["research_stake_dollars"] == 0
            assert d["research_stake_dollars"] <= 5 and d["expression_fidelity"]["fidelity_class"]
        assert (root / "slates" / "latest" / "card.md").read_text().count("research") >= 1
    assert cards[0] == cards[1]


def test_link_copy_never_modifies_the_source_archive(tmp_path):
    from nhl_edge.research.rules_replay import link_copy

    src = tmp_path / "src"
    led = Ledger(src, run_id="r")
    led.append_rows("context/schedule", [{"game_id": "1"}], observed_at=NOW)
    (src / "STATUS_settle.json").write_text("{}")
    before = {p.relative_to(src): p.read_bytes() for p in src.rglob("*") if p.is_file()}
    dst = link_copy(src, tmp_path / "dst")
    Ledger(dst, run_id="replay").append_rows("context/schedule", [{"game_id": "2"}], observed_at=NOW + timedelta(minutes=1))
    (dst / "STATUS_settle.json").write_text('{"changed": true}')
    after = {p.relative_to(src): p.read_bytes() for p in src.rglob("*") if p.is_file()}
    assert before == after
