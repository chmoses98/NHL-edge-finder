"""RUN NHL end to end on the fixture archive: point-in-time discipline, coherent pricing, packet contract, idempotent reruns."""

import json
from datetime import timedelta

import pytest

from nhl_edge.workflows.simulate import run_simulate
from tests.archive_fixture import NOW, build_archive


@pytest.mark.slow
def test_run_nhl_on_opening_night_fixture(tmp_path):
    root = tmp_path / "archive"
    build_archive(root)
    assert run_simulate(root, tmp_path, date="2026-09-29", n_sims=4000, now=NOW) == 0
    slate = json.loads((root / "slates" / "latest" / "slate.json").read_text())
    assert slate["authority"] == "RESEARCH_ONLY" and slate["sport"] == "NHL"
    assert slate["coverage"]["games_simulated"] == 5 and slate["coverage"]["contracts_joined"] == 14
    g = slate["games"][0]
    assert g["home"] == "CAR" and g["away"] == "FLA"
    # goalie discipline: PROJECTED at the cutoff; the CONFIRMED observation 2h later must not be visible
    assert g["home_goalie"]["status"] == "PROJECTED" and g["away_goalie"]["status"] == "CONFIRMED"
    assert all(gg["ladder_violations"] == [] for gg in slate["games"])
    rows = slate["contracts"]
    by = {r["ticker"]: r for r in rows}
    assert by["KXNHLGAME-26SEP29FLACAR-FLA"]["p_data_only"] + by["KXNHLGAME-26SEP29FLACAR-CAR"]["p_data_only"] == pytest.approx(1.0)
    totals = sorted((r["threshold"], r["p_data_only"]) for r in rows if r["family"] == "game_total")
    assert all(a[1] >= b[1] for a, b in zip(totals, totals[1:])), "alternate totals must be monotone"
    for r in rows:
        assert r["authority"] == "RESEARCH_ONLY" and r["model_version"] == "DATA_ONLY_V1" and r["pregame"] is True
        assert r["executable_p_yes"] == r["market_yes_ask"] / 100
        assert r["p_market_anchored"] is not None and r["market_anchor_weight"] == 0.8
    packet = json.loads((root / "slates" / "latest" / "packet.json").read_text())
    pg = packet["games"][0]
    assert set(pg) == {"identity", "context", "goaltending", "team_state", "model", "kalshi", "authority"}
    assert pg["authority"] == "RESEARCH_ONLY" and pg["identity"]["sport"] == "NHL"
    assert pg["kalshi"]["coverage"]["n_contracts"] == 14


def test_rerun_same_instant_is_refused_by_immutability_not_silently_duplicated(tmp_path):
    from nhl_edge.archive.ledger import ImmutabilityError

    root = tmp_path / "archive"
    build_archive(root)
    run_simulate(root, tmp_path, date="2026-09-29", n_sims=500, now=NOW)
    with pytest.raises(ImmutabilityError):
        run_simulate(root, tmp_path, date="2026-09-29", n_sims=500, now=NOW)


def test_second_run_later_appends_new_rows_and_keeps_old(tmp_path):
    root = tmp_path / "archive"
    build_archive(root)
    run_simulate(root, tmp_path, date="2026-09-29", n_sims=500, now=NOW)
    run_simulate(root, tmp_path, date="2026-09-29", n_sims=500, now=NOW + timedelta(minutes=30))
    from nhl_edge.archive.ledger import Ledger

    preds = list(Ledger(root).iter_rows("predictions"))
    assert len(preds) == 28 and len({p["prediction_id"] for p in preds}) == 28


def test_no_post_start_leakage(tmp_path):
    root = tmp_path / "archive"
    build_archive(root)
    late = NOW + timedelta(hours=7)  # first game started at 21:00Z; late == 22:00Z
    run_simulate(root, tmp_path, date="2026-09-29", n_sims=500, now=late)
    slate = json.loads((root / "slates" / "latest" / "slate.json").read_text())
    assert slate["coverage"]["games_simulated"] == 4 and slate["coverage"]["games_skipped"][0]["game_id"] == "2026020001"


def test_without_market_board_games_still_simulate(tmp_path):
    root = tmp_path / "archive"
    build_archive(root, with_markets=False)
    run_simulate(root, tmp_path, date="2026-09-29", n_sims=500, now=NOW)
    slate = json.loads((root / "slates" / "latest" / "slate.json").read_text())
    assert slate["coverage"]["games_simulated"] == 5 and slate["coverage"]["contracts_joined"] == 0
