"""Pure-function tests for the goalie change log (offline; no network)."""

from __future__ import annotations

from datetime import UTC, datetime

from nhl_edge.data.goalie_watch import diff_goalie_state
from nhl_edge.schemas.core import GoalieObservation


def obs(name, status, at, rep=None, team=6, game="g1"):
    return GoalieObservation(game_id=game, team_id=team, player_id=1, player_name=name, status=status, observed_at_utc=datetime(2026, 10, 20, *at, tzinfo=UTC), source="dailyfaceoff",
                             source_reported_at_utc=None if rep is None else datetime(2026, 10, 20, *rep, tzinfo=UTC))


def test_first_seen_then_no_event_when_nothing_changes():
    ev, st = diff_goalie_state({}, [obs("A", "PROJECTED", (10, 0))])
    assert [e["kind"] for e in ev] == ["FIRST_SEEN"]
    ev2, st2 = diff_goalie_state(st, [obs("A", "PROJECTED", (10, 5))])
    assert ev2 == [] and st2 == st


def test_confirmation_of_same_goalie_and_latency():
    _, st = diff_goalie_state({}, [obs("A", "PROJECTED", (10, 0))])
    ev, _ = diff_goalie_state(st, [obs("A", "CONFIRMED", (11, 30), rep=(11, 10))])
    assert ev[0]["kind"] == "CONFIRMED" and ev[0]["latency_min"] == 20.0 and ev[0]["became_confirmed"]


def test_goalie_change_is_distinguished_and_latency_is_never_invented():
    _, st = diff_goalie_state({}, [obs("A", "PROJECTED", (10, 0))])
    ev, st2 = diff_goalie_state(st, [obs("B", "CONFIRMED", (12, 0))])
    assert ev[0]["kind"] == "GOALIE_CHANGE" and ev[0]["latency_min"] is None and ev[0]["previous"]["player_name"] == "A"
    assert st2["g1:6"]["player_name"] == "B"


def test_state_is_not_mutated_for_unchanged_teams():
    _, st = diff_goalie_state({}, [obs("A", "PROJECTED", (10, 0)), obs("C", "PROBABLE", (10, 0), team=7)])
    ev, st2 = diff_goalie_state(st, [obs("A", "CONFIRMED", (11, 0)), obs("C", "PROBABLE", (11, 0), team=7)])
    assert len(ev) == 1 and st2["g1:7"] == st["g1:7"]
