"""Goalie state is point-in-time: later observations are invisible; statuses never silently upgrade."""

from datetime import UTC, datetime, timedelta

from nhl_edge.goalies.state import (
    GoalieStatus,
    latest_state,
    mixture_factor,
    parse_dailyfaceoff_next_data,
    status_from_label,
    unknown_state,
)
from nhl_edge.identity.teams import registry

T = datetime(2026, 9, 29, 15, 0, tzinfo=UTC)


def obs(status, minutes, pid=None, team=12, game="2026020001"):
    return {"game_id": game, "team_id": team, "player_id": pid, "player_name": "Frederik Andersen", "status": status,
            "observed_at_utc": (T + timedelta(minutes=minutes)).isoformat().replace("+00:00", "Z"), "source": "dailyfaceoff"}


def test_unknown_when_nothing_observed():
    st = latest_state([], "2026020001", 12, T)
    assert st.status == GoalieStatus.UNKNOWN and st.confidence == 0.0


def test_latest_at_or_before_cutoff_only():
    rows = [obs("PROJECTED", -120), obs("PROBABLE", -30), obs("CONFIRMED", +45)]
    st = latest_state(rows, "2026020001", 12, T)
    assert st.status == GoalieStatus.PROBABLE, "the confirmation 45 min AFTER the cutoff must be invisible"
    later = latest_state(rows, "2026020001", 12, T + timedelta(hours=1))
    assert later.status == GoalieStatus.CONFIRMED


def test_late_change_is_a_new_observation_not_an_edit():
    rows = [obs("CONFIRMED", -60, pid=1), {**obs("CONFIRMED", -5, pid=2), "player_name": "Backup"}]
    st = latest_state(rows, "2026020001", 12, T)
    assert st.player_id == 2 and st.player_name == "Backup"
    assert latest_state(rows, "2026020001", 12, T - timedelta(minutes=30)).player_id == 1


def test_other_team_and_game_are_ignored():
    rows = [obs("CONFIRMED", -10, team=13), obs("CONFIRMED", -10, game="2026020002")]
    assert latest_state(rows, "2026020001", 12, T).status == GoalieStatus.UNKNOWN


def test_status_labels():
    assert status_from_label("Confirmed", True) == GoalieStatus.CONFIRMED
    assert status_from_label("Likely", True) == GoalieStatus.PROBABLE
    assert status_from_label(None, True) == GoalieStatus.PROJECTED
    assert status_from_label("Unconfirmed", True) == GoalieStatus.PROJECTED
    assert status_from_label("Confirmed", False) == GoalieStatus.UNKNOWN


def test_mixture_factor_widens_toward_average_when_unconfirmed():
    factors = {1: 0.85, 2: 1.10}
    conf = latest_state([obs("CONFIRMED", -10, pid=1)], "2026020001", 12, T)
    proj = latest_state([obs("PROJECTED", -10, pid=1)], "2026020001", 12, T)
    f_conf, _ = mixture_factor(conf, factors)
    f_proj, det = mixture_factor(proj, factors)
    assert f_conf < f_proj < 1.0 and det["weight_named"] == 0.70
    assert mixture_factor(unknown_state(12), factors)[0] == 1.0


def test_dailyfaceoff_parser_on_real_shape_strips_nothing_but_never_reads_prices():
    row = {"homeTeamName": "Carolina Hurricanes", "homeGoalieName": "Brandon Bussi", "homeNewsStrengthName": "Confirmed", "homeNewsCreatedAt": "2026-09-29T12:00:00.000Z",
           "awayTeamName": "Florida Panthers", "awayGoalieName": None, "awayNewsStrengthName": None, "date": "2026-09-29", "dateGmt": "2026-09-29T21:00:00.000Z",
           "homeTeamMoneylinePointSpread": -130, "awayTeamMoneylinePointSpread": 110, "pointSpread": 1.5}
    obs_rows, problems = parse_dailyfaceoff_next_data({"data": [row]}, T, lambda n: registry().resolve_name(n).team_id)
    assert problems == []
    home = [o for o in obs_rows if o.team_id == 12][0]
    away = [o for o in obs_rows if o.team_id == 13][0]
    assert home.status == GoalieStatus.CONFIRMED and home.player_name == "Brandon Bussi" and home.source_reported_at_utc is not None
    assert away.status == GoalieStatus.UNKNOWN and away.player_name is None
    assert "moneyline" not in (home.note or "").lower() and "-130" not in (home.note or "")
