"""Prospective goalie-status measurement: only PREGAME observations count, and accuracy is judged against boxscore starters."""

from datetime import timedelta

from nhl_edge.archive.ledger import Ledger
from nhl_edge.research.goalie_status_eval import evaluate
from nhl_edge.timeutil import iso
from tests.archive_fixture import NOW


def test_accuracy_transitions_and_post_start_observations_ignored(tmp_path):
    led = Ledger(tmp_path, run_id="t")
    start = NOW + timedelta(hours=6)
    led.append_rows("context/schedule", [{"game_id": "G1", "start_time_utc": iso(start), "home_team_id": 1, "away_team_id": 2, "game_date_et": "2026-09-29"}], observed_at=NOW)
    obs = [
        {"game_id": "G1", "team_id": 1, "player_id": 10, "player_name": "A", "status": "PROJECTED", "source": "dailyfaceoff"},
        {"game_id": "G1", "team_id": 2, "player_id": 20, "player_name": "B", "status": "PROJECTED", "source": "dailyfaceoff"},
    ]
    led.append_rows("context/goalie_observations", obs, observed_at=NOW)
    led.append_rows("context/goalie_observations", [
        {"game_id": "G1", "team_id": 1, "player_id": 10, "player_name": "A", "status": "CONFIRMED", "source": "dailyfaceoff"},
        {"game_id": "G1", "team_id": 2, "player_id": 21, "player_name": "C", "status": "CONFIRMED", "source": "dailyfaceoff"},
    ], observed_at=NOW + timedelta(hours=5))
    # post-start boxscore observation must not count as a pregame observation
    led.append_rows("context/goalie_observations", [{"game_id": "G1", "team_id": 2, "player_id": 21, "status": "CONFIRMED", "source": "nhl_api_boxscore"}],
                    observed_at=start + timedelta(hours=3))
    led.append_rows("results", [{"game_id": "G1", "status": "FINAL", "home_team_id": 1, "away_team_id": 2, "home_final": 3, "away_final": 2, "home_reg": 3,
                                 "away_reg": 2, "last_period_type": "REG", "home_starting_goalie_id": 10, "away_starting_goalie_id": 21}],
                    observed_at=start + timedelta(hours=3))
    led.append_rows("predictions", [
        {"family": "game_winner", "game_id": "G1", "team_id": 1, "predicted_at_utc": iso(NOW + timedelta(hours=4)), "p_data_only": 0.55},
        {"family": "game_winner", "game_id": "G1", "team_id": 1, "predicted_at_utc": iso(NOW + timedelta(hours=5, minutes=30)), "p_data_only": 0.58},
    ], observed_at=NOW + timedelta(hours=5, minutes=30))
    r = evaluate(tmp_path)
    assert r["n_team_games_with_pregame_obs"] == 2
    assert r["accuracy_all_observations"]["PROJECTED"] == {"n": 2, "accuracy": 0.5}
    assert r["accuracy_last_pregame_observation"]["CONFIRMED"] == {"n": 2, "accuracy": 1.0}
    assert r["transitions"] == {"same_goalie": 1, "projection_overturned": 1}
    mv = r["probability_movement_on_confirmation"]["predictions"]
    assert mv["n"] == 1 and abs(mv["mean_abs_move"] - 0.03) < 1e-9 and mv["moved_toward_result"] == 1
