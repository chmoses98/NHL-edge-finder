from __future__ import annotations

import copy
import gzip
import json
from datetime import UTC, datetime, timedelta

from nhl_edge.timeutil import iso
from nhl_edge.workflows.slate_check import check_slate, run_slate_check

NOW = datetime(2026, 10, 22, 18, 0, tzinfo=UTC)
START = NOW + timedelta(hours=5)


def _game(gid="2026020154", home="BOS", away="NSH", start=START, g_status="CONFIRMED", market_age=2.0):
    goalie = {"status": g_status, "player_name": "G", "observed_at_utc": iso(NOW - timedelta(minutes=30))}
    return {
        "identity": {"game_id": gid, "home": home, "away": away, "home_team_id": 6, "away_team_id": 18, "start_time_utc": iso(start)},
        "context": {"injury_snapshot": {"age_min": 20}},
        "goaltending": {"home": goalie, "away": dict(goalie)},
        "model": {"sim": {"home_lambda": 3.2, "away_lambda": 2.9, "p_home_win": 0.55, "p_away_win": 0.45, "p_overtime": 0.2, "total_mean": 6.3,
                          "total_ladder": {"over_4.5": 0.8, "over_5.5": 0.6, "over_6.5": 0.4},
                          "home_team_total_ladder": {"home_over_1.5": 0.8, "home_over_2.5": 0.55}, "away_team_total_ladder": {"away_over_1.5": 0.7}},
                  "ladder_violations": [], "inputs_trusted": True, "input_reasons": []},
        "kalshi": {"market_age_min": market_age, "contracts": [{"predicted_at_utc": iso(NOW - timedelta(minutes=10))}],
                   "coverage": {"by_family": {f: 1 for f in ("game_winner", "game_total", "game_spread", "team_total", "game_overtime")}}},
    }


def _packet(*games):
    return {"slate": {"date_et": "2026-10-22", "generated_at_utc": iso(NOW), "model_version": "DATA_ONLY_V1", "coverage": {"games_skipped": []}},
            "games": list(games),
            "v2_shadow": {"blocks": [{"game_id": g["identity"]["game_id"], "v2": {"total_ladder": {"over_5.5": 0.6, "over_6.5": 0.4}}} for g in games]},
            "player_shadow": {"blocks": [{"game_id": g["identity"]["game_id"], "invariant_violations": [], "n_priced": 100,
                                          "lineups": {s: {"deployment_source": "LINES_PROJECTED", "notes": ["lines: x updated (2.0 h old)"]} for s in ("home", "away")}}
                                         for g in games]}}


def _sched(gid="2026020154", home="BOS", away="NSH", start=START, status="not_started"):
    return {"game_id": gid, "game_date_et": "2026-10-22", "home_abbrev": home, "away_abbrev": away, "home_team_id": 6, "away_team_id": 18,
            "start_time_utc": iso(start), "status": status}


def codes(rep):
    return {f["code"] for r in rep["games"] for f in r["findings"]} | {f["code"] for f in rep["slate_findings"]}


def test_clean_slate_is_ready():
    rep = check_slate(_packet(_game()), [_sched()], NOW)
    assert rep["verdict"] == "READY" and rep["n_games"] == 1 and rep["n_scheduled"] == 1


def test_unprojected_scheduled_game_is_not_ready():
    rep = check_slate(_packet(_game()), [_sched(), _sched("2026020155", "TOR", "NYR")], NOW)
    assert rep["verdict"] == "NOT_READY" and "GAME_NOT_PROJECTED" in codes(rep)


def test_final_games_not_demanded():
    rep = check_slate(_packet(_game()), [_sched(), _sched("2026020155", status="final")], NOW)
    assert "GAME_NOT_PROJECTED" not in codes(rep)


def test_identity_mismatch_and_phantom_game():
    rep = check_slate(_packet(_game(home="TOR")), [_sched()], NOW)
    assert "TEAM_IDENTITY" in codes(rep) and rep["verdict"] == "NOT_READY"
    rep = check_slate(_packet(_game("9")), [_sched()], NOW)
    assert "GAME_NOT_SCHEDULED" in codes(rep)


def test_goalie_unconfirmed_close_to_puck_drop_warns_not_far_out():
    far = check_slate(_packet(_game(g_status="PROJECTED")), None, NOW)
    near = check_slate(_packet(_game(g_status="PROJECTED", start=NOW + timedelta(minutes=45))), None, NOW)
    assert "GOALIE_HOME_UNCONFIRMED" not in codes(far)
    assert "GOALIE_HOME_UNCONFIRMED" in codes(near) and near["verdict"] == "DEGRADED"


def test_unknown_goalie_inside_two_hours_is_error():
    rep = check_slate(_packet(_game(g_status="UNKNOWN", start=NOW + timedelta(minutes=60))), None, NOW)
    assert "GOALIE_HOME_UNKNOWN" in codes(rep) and rep["verdict"] == "NOT_READY"


def test_stale_market_and_projection():
    g = _game(market_age=45.0, start=NOW + timedelta(hours=2))
    g["kalshi"]["contracts"][0]["predicted_at_utc"] = iso(NOW - timedelta(minutes=200))
    c = codes(check_slate(_packet(g), None, NOW))
    assert {"MARKET_STALE", "PROJECTION_STALE"} <= c


def test_incoherent_model_is_error():
    g = _game()
    g["model"]["sim"]["total_ladder"]["over_6.5"] = 0.9  # not monotone
    g["model"]["sim"]["p_overtime"] = 0.9
    c = codes(check_slate(_packet(g), None, NOW))
    assert {"TOTAL_LADDER_NOT_MONOTONE", "OT_RANGE"} <= c


def test_player_invariants_and_fallback_lines():
    p = _packet(_game())
    p["player_shadow"]["blocks"][0]["invariant_violations"] = ["x"]
    p["player_shadow"]["blocks"][0]["lineups"]["home"]["deployment_source"] = "RECENT_SHIFTS"
    c = codes(check_slate(p, None, NOW))
    assert {"PLAYER_INVARIANTS", "LINES_HOME_FALLBACK"} <= c


def test_run_writes_report_and_exit_code(tmp_path):
    (tmp_path / "packet.json").write_text(json.dumps(_packet(_game())))
    with gzip.open(tmp_path / "sched.jsonl.gz", "wt") as fh:
        fh.write(json.dumps(_sched()) + "\n")
    # NOW is fixed in the past relative to the wall clock: the game has started, which is only INFO
    assert run_slate_check(tmp_path / "packet.json", tmp_path / "sched.jsonl.gz", tmp_path / "out", now=NOW) == 0
    assert json.loads((tmp_path / "out" / "slate_check.json").read_text())["verdict"] == "READY"
    assert (tmp_path / "out" / "slate_check.md").read_text().startswith("# NHL slate readiness")
    bad = copy.deepcopy(_packet(_game()))
    bad["games"][0]["model"]["sim"] = {}
    (tmp_path / "bad.json").write_text(json.dumps(bad))
    assert run_slate_check(tmp_path / "bad.json", None, None, now=NOW) == 2


def test_started_games_are_not_alerts():
    g = _game(start=NOW - timedelta(minutes=30), g_status="UNKNOWN")
    p = _packet(g)
    p["slate"]["coverage"]["games_skipped"] = [{"game_id": "2026020154", "status": "live", "start_time_utc": iso(NOW - timedelta(minutes=30))}]
    rep = check_slate(p, [_sched(start=NOW - timedelta(minutes=30), status="not_started")], NOW)
    assert rep["verdict"] != "NOT_READY", codes(rep)


def test_a_game_that_should_still_be_priced_but_was_skipped_is_an_error():
    p = _packet(_game())
    p["slate"]["coverage"]["games_skipped"] = [{"game_id": "9", "status": "not_started", "start_time_utc": iso(START)}]
    assert "GAMES_SKIPPED" in codes(check_slate(p, None, NOW))


def test_postponed_and_canceled_games_are_not_demanded():
    rep = check_slate(_packet(_game()), [_sched(), _sched("2026020155", status="postponed"), _sched("2026020156", status="canceled")], NOW)
    assert "GAME_NOT_PROJECTED" not in codes(rep)


def test_dead_simulator_is_an_error_and_ages_are_measured_at_check_time():
    g = _game(start=NOW + timedelta(hours=2))
    g["kalshi"]["contracts"][0]["predicted_at_utc"] = iso(NOW - timedelta(minutes=200))
    g["kalshi"]["market_snapshot_at_utc"] = iso(NOW - timedelta(minutes=90))      # market_age_min (2.0) was true when the packet was generated
    rep = check_slate(_packet(g), None, NOW)
    assert "PROJECTION_STALE" in codes(rep) and "MARKET_STALE" in codes(rep) and rep["verdict"] == "NOT_READY"


def test_next_day_slate_not_projected_when_its_first_puck_drop_is_near():
    nxt = _sched("2026020200", "TOR", "NYR", start=NOW + timedelta(hours=3))
    nxt["game_date_et"] = "2026-10-23"
    assert "NEXT_SLATE_NOT_PROJECTED" in codes(check_slate(_packet(_game(start=NOW - timedelta(hours=1))), [_sched(start=NOW - timedelta(hours=1)), nxt], NOW))
