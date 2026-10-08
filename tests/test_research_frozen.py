"""Frozen pregame research: once a game starts the simulate job drops it from ``slates/latest/packet.json``; the research
export then keeps the game's LAST PREGAME simulation (sim, components, distributions, NHL_SCRIPT_V1 block) from the
archived slate run, never one generated at or after puck drop, and never lets it leak into the latest-packet team
metrics. FINAL games carry the realised script from ``script_postmortems``."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from nhl_edge import research_export
from nhl_edge.archive.ledger import Ledger
from nhl_edge.research_sift import script_notes, script_outcome
from nhl_edge.scripts_v1.build import game_research
from nhl_edge.timeutil import parse_iso
from tests.test_research_export import NOW, _publish
from tests.test_scripts_v1 import _analysis, mk_bet
from tests.test_thesis_core import synth_features

G1, G2, G3 = "2026020001", "2026020002", "2026020003"  # FLA@CAR 21:00Z, 23:00Z, 00:00Z (2026-09-29 ET slate)
RUN1 = "20260929T145000Z_run1"  # pregame
RUN2 = "20260929T213000Z_run2"  # after G1's puck drop: must never be used for G1


def _scripts_v1() -> dict:
    f = synth_features(3000, seed=5)
    y = f.winner == 1
    a = _analysis(f, [mk_bet("ML|yes", y, 50, mid=0.48), mk_bet("ML|no", ~y, 52, mid=0.52)], {})
    a["short"] = list(a["bets"])
    return game_research(a)


def _packet(at: str, games: list[dict], thesis: list[dict]) -> dict:
    return {"slate": {"generated_at_utc": at, "date_et": "2026-09-29"}, "games": games,
            "thesis_card": {"generated_at_utc": at, "games": thesis}}


def _write(root: Path, rel: str, pk: dict) -> None:
    p = root / rel / "packet.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(pk))


def _relabel(game: dict, ev: dict) -> dict:
    """``game``'s packet block re-labelled onto the published event ``ev`` (its game id, start and both team ids)."""
    g = json.loads(json.dumps(game))
    tid = {p["participant_id"]: p["source_ids"]["nhl_team_id"] for p in ev["participants"]}
    g["identity"] |= {"game_id": ev["source_ids"]["nhl_game_id"], "event_id": ev["source_ids"]["nhl_game_id"], "start_time_utc": ev["start_time_utc"],
                      "home_team_id": tid[ev["home_participant"]], "away_team_id": tid[ev["away_participant"]]}
    return g


# ------------------------------------------------------------------------------------------------ the lookup itself
def test_lookup_takes_the_latest_run_strictly_before_the_start(tmp_path):
    root = tmp_path
    g = lambda gid, p: {"identity": {"game_id": gid}, "model": {"sim": {"p_home_win": p}}}  # noqa: E731
    t = lambda gid: {"game_id": gid, "scripts_v1": {"x": gid}}  # noqa: E731
    _write(root, "slates/dt=2026-10-07/20261007T220000Z_a", _packet("2026-10-07T22:00:00Z", [g("A", 0.1), g("B", 0.1)], [t("A")]))
    _write(root, "slates/dt=2026-10-07/20261007T230400Z_b", _packet("2026-10-07T23:04:00Z", [g("A", 0.2)], [t("A")]))
    # stamped AT the start, and a run whose folder stamp is pregame but whose packet was generated after the start
    _write(root, "slates/dt=2026-10-07/20261007T233000Z_c", _packet("2026-10-07T23:30:00Z", [g("A", 0.9)], [t("A")]))
    _write(root, "slates/dt=2026-10-07/20261007T232900Z_d", _packet("2026-10-07T23:31:00Z", [g("A", 0.8)], [t("A")]))
    _write(root, "slates/dt=2026-10-08/20261008T001000Z_e", _packet("2026-10-08T00:10:00Z", [g("A", 0.7)], [t("A")]))
    latest = _packet("2026-10-08T00:10:00Z", [g("C", 0.5)], [])
    ev = lambda gid, status: {"status": status, "start_time_utc": "2026-10-07T23:30:00Z", "source_ids": {"nhl_game_id": gid},  # noqa: E731
                              "extensions": {"game_date_et": "2026-10-07"}}
    events = [ev("A", "LIVE"), ev("B", "SCHEDULED"), ev("C", "LIVE"), ev("D", "FINAL")]
    out, warn = research_export.load_frozen_pregame(root, events, latest, as_of="2026-10-07T23:00:00Z")
    assert warn == []
    assert set(out) == {"A"}, "B has not started (as_of before its start), C is in the latest packet, D was never simulated"
    assert out["A"]["run"] == "20261007T230400Z_b" and out["A"]["generated_at"] == "2026-10-07T23:04:00Z"
    assert out["A"]["game"]["model"]["sim"]["p_home_win"] == 0.2 and out["A"]["thesis_game"]["scripts_v1"] == {"x": "A"}
    # once B's start has passed it freezes at the newest pregame run that carries it (only run a has B)
    out, _ = research_export.load_frozen_pregame(root, events, latest, as_of="2026-10-08T03:00:00Z")
    assert out["B"]["run"] == "20261007T220000Z_a" and out["B"]["thesis_game"] is None
    # game_date_et absent: the start's ET date is searched
    out, _ = research_export.load_frozen_pregame(root, [ev("A", "LIVE") | {"extensions": {}}], latest)
    assert out["A"]["run"] == "20261007T230400Z_b"


def test_script_outcome_prefers_the_published_forecast_and_never_uses_post_start_rows():
    pred = {"OPEN_GAME": 0.3, "BACK_AND_FORTH": 0.4, "GOALIE_DRIVEN": 0.3}
    row = lambda at, p: {"game_id": "g", "decided_at_utc": at, "predicted": p, "realized_script": "GOALIE_DRIVEN", "p_realized": p["GOALIE_DRIVEN"],  # noqa: E731
                         "realized_metrics": {"home_final": 2, "away_final": 3, "overtime": True, "shootout": False}, "top_hit": False}
    rows = [row("2026-10-07T20:00:00Z", pred), row("2026-10-07T22:00:00Z", pred | {"GOALIE_DRIVEN": 0.1, "OPEN_GAME": 0.5}),
            row("2026-10-07T23:30:00Z", pred | {"GOALIE_DRIVEN": 0.9})]
    sc = [{"id": "GOALIE_DRIVEN", "label": "Goaltending steals it"}]
    o = script_outcome(rows, forecast_at="2026-10-07T20:00:00Z", start_time_utc="2026-10-07T23:30:00Z", scripts=sc)
    assert o["forecast_decided_at"] == "2026-10-07T20:00:00Z" and o["scores_published_forecast"] is True
    assert o["p_realized"] == 0.3 and o["realized_rank"] == 2 and o["n_scripts"] == 3 and o["realized_label"] == "Goaltending steals it"
    assert o["final_score"] == {"home": 2, "away": 3} and o["overtime"] is True and o["top_hit"] is False
    assert "brier" not in o, "fields the postmortem does not carry are omitted, never invented"
    # no row for the published forecast: the final pregame row (never the one at the start)
    o = script_outcome(rows, forecast_at="2026-10-07T21:00:00Z", start_time_utc="2026-10-07T23:30:00Z", scripts=sc)
    assert o["forecast_decided_at"] == "2026-10-07T22:00:00Z" and o["scores_published_forecast"] is False and o["realized_rank"] == 3
    assert script_outcome(rows[2:], forecast_at=None, start_time_utc="2026-10-07T23:30:00Z", scripts=sc) is None
    assert script_outcome([], forecast_at=None, start_time_utc=None, scripts=sc) is None


# ------------------------------------------------------------------------------------------------ through the export
@pytest.fixture(scope="module")
def frozen_export(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("frozen")
    root, out = _publish(tmp)
    latest_path = root / "slates" / "latest" / "packet.json"
    pk = json.loads(latest_path.read_text())
    base = pk["games"][0]
    assert base["identity"]["game_id"] == G1
    sv = _scripts_v1()
    evs = json.loads((out / "events.json").read_text())
    g2 = _relabel(base, next(e for e in evs["items"] if e["source_ids"]["nhl_game_id"] == G2))
    assert g2["identity"]["home_team_id"] != base["identity"]["home_team_id"]
    # run 1 (pregame for G1): G1 with its real fixture sim and a script layer
    run1 = _packet("2026-09-29T14:50:00Z", [base], [{"game_id": G1, "scripts_v1": sv}])
    _write(root, f"slates/dt=2026-09-29/{RUN1}", run1)
    # run 2 (after G1 started): a different G1 simulation that must never be published for G1
    late = json.loads(json.dumps(base))
    late["model"]["sim"]["p_home_win"] = 0.987
    _write(root, f"slates/dt=2026-09-29/{RUN2}", _packet("2026-09-29T21:30:00Z", [late, g2],
                                                         [{"game_id": G1, "scripts_v1": sv}, {"game_id": G2, "scripts_v1": sv}]))
    # the latest packet: G1 has started and is gone; G2 is still pregame in it
    latest = _packet("2026-09-29T22:00:00Z", [g2], [{"game_id": G2, "scripts_v1": sv}])
    latest["slate"] = pk["slate"] | {"generated_at_utc": "2026-09-29T22:00:00Z"}
    latest_path.write_text(json.dumps(latest))
    (root / "slates" / "latest" / "slate.json").write_text(json.dumps({"generated_at_utc": "2026-09-29T22:00:00Z"}))
    # G1 and G2 final; postmortems for both (G2 is in the latest packet, so its block is not frozen -- still FINAL here)
    for e in evs["items"]:
        if e["source_ids"]["nhl_game_id"] == G1:
            e["status"] = "FINAL"
    (out / "events.json").write_text(json.dumps(evs))
    predicted = {s["id"]: s["probability"] for s in sv["scripts"]}
    realized = sv["scripts"][-1]["id"]
    pm = lambda gid, at: {"snapshot_id": f"snap-{at}", "game_id": gid, "decided_at_utc": at, "predicted": predicted, "realized_script": realized,  # noqa: E731
                          "realized_metrics": {"home_final": 4, "away_final": 3, "overtime": True, "shootout": False}, "p_realized": predicted[realized],
                          "top_script": sv["scripts"][0]["id"], "top_hit": False, "brier": 0.9, "log_loss": 2.0, "evaluated_at_utc": "2026-09-30T06:00:00Z",
                          "realized_version": "nhl-realized-script-1.0", "authority": "RESEARCH_ONLY"}
    Ledger(root, run_id="pm").append_rows("script_postmortems", [pm(G1, "2026-09-29T14:50:00Z"), pm(G1, "2026-09-29T21:30:00Z"),
                                                                 pm(G2, "2026-09-29T14:50:00Z")], observed_at=parse_iso("2026-09-30T06:00:00Z"))
    inp = research_export.load_research_inputs(out, root)
    docs, _meta = research_export.build_explorer(inp, run_id=inp.manifest["run_id"], generated_at=NOW)
    events = {d["extensions"]["nhl_game_id"]: d for d in docs if "nhl_scripts_v1" in (d.get("extensions") or {})}
    return inp, docs, events, base, sv, realized


def test_a_started_game_gone_from_the_latest_packet_keeps_its_last_pregame_research(frozen_export):
    inp, _docs, events, base, sv, _ = frozen_export
    assert inp.frozen[G1]["run"] == RUN1
    x = events[G1]["extensions"]
    sx = x["nhl_scripts_v1"]
    assert sx["status"] == "OK" and sx["pregame"] is True and sx["generated_at"] == "2026-09-29T14:50:00Z"
    assert sx["frozen"] is True and sx["frozen_from_run"] == RUN1 and sx["frozen_reason"] == research_export.FROZEN_REASON
    assert [s["id"] for s in sx["scripts"]] == [s["id"] for s in sv["scripts"]]
    assert x["sim_frozen"] is True and x["sim"]["p_home_win"] == pytest.approx(base["model"]["sim"]["p_home_win"], abs=1e-5)
    assert x["sim"]["p_home_win"] != 0.987, "a run generated after puck drop is never used"
    assert x["model_components"] == base["model"]["components"]
    dists = events[G1]["distributions"]
    assert dists and all(d["generated_at"] == "2026-09-29T14:50:00Z" and "frozen pregame" in d["source"] for d in dists)
    assert any("frozen at the last pregame simulation" in n for n in events[G1]["context"]["notes"])
    assert len(json.dumps(events[G1]).encode()) < 400_000


def test_latest_packet_games_are_not_frozen_and_unsimulated_games_say_so(frozen_export):
    _inp, _docs, events, _base, _sv, _ = frozen_export
    x = events[G2]["extensions"]
    assert x["nhl_scripts_v1"]["status"] == "OK" and x["nhl_scripts_v1"]["frozen"] is False and "frozen_from_run" not in x["nhl_scripts_v1"]
    assert x["sim_frozen"] is False and all(d["generated_at"] == "2026-09-29T22:00:00Z" for d in events[G2]["distributions"])
    sx3 = events[G3]["extensions"]["nhl_scripts_v1"]
    assert sx3["status"] == "NOT_SIMULATED" and "frozen" not in sx3 and "sim" not in events[G3]["extensions"]


def test_frozen_games_never_feed_the_latest_packet_team_metrics(frozen_export):
    inp, docs, events, _base, _sv, _ = frozen_export
    tids = lambda gid: {p["source_ids"]["nhl_team_id"] for p in next(e for e in inp.events if e["source_ids"]["nhl_game_id"] == gid)["participants"]}  # noqa: E731
    run_obs = {}
    for d in docs:
        if d.get("kind") == "entity_profile" and d.get("entity_type") == "TEAM":
            run_obs[int(d["entity"]["source_ids"]["nhl_team_id"])] = [o for o in d["metrics"] if o["window"]["kind"] == "RUN"]
    assert run_obs, "team profiles were found"
    assert all(run_obs.get(int(t)) for t in tids(G2)), "the latest packet's game feeds the run-window ratings"
    assert not any(run_obs.get(int(t)) for t in tids(G1) - tids(G2)), "the frozen game's teams get no run-window ratings"


def test_outcome_is_attached_only_to_final_games_with_a_postmortem(frozen_export):
    _inp, _docs, events, _base, sv, realized = frozen_export
    oc = events[G1]["extensions"]["nhl_scripts_v1"]["outcome"]
    assert oc["realized_script"] == realized and oc["realized_label"] == sv["scripts"][-1]["label"]
    assert oc["forecast_decided_at"] == "2026-09-29T14:50:00Z" and oc["scores_published_forecast"] is True
    assert oc["final_score"] == {"home": 4, "away": 3} and oc["overtime"] is True and oc["realized_rank"] == len(sv["scripts"]) - \
        sum(1 for s in sv["scripts"] if s["probability"] == sv["scripts"][-1]["probability"]) + 1
    assert any(n.startswith("Realised script:") for n in script_notes(events[G1]["extensions"]["nhl_scripts_v1"]))
    assert "outcome" not in events[G2]["extensions"]["nhl_scripts_v1"], "G2 is not FINAL: no outcome even with a postmortem row"
