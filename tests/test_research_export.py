"""Research explorer (contract 1.1.0): built from the v1 test archive + a committed slice of real archive rows
(``tests/research_fixture.py``) + the committed history under ``data/history``; verified, deterministic, complete
against the v1 publication, honest about capabilities, packet-ready, secret-free, RESEARCH-preserving and atomic.
A real-data smoke test runs when the data-archive branch is checked out (``NHL_EDGE_ARCHIVE_ROOT``)."""

from __future__ import annotations

import json
import os
import shutil
from pathlib import Path

import pytest
from edge_finder_contract import packet, publish, research, sync

from nhl_edge import app_export, research_export
from nhl_edge.config import REPO_ROOT
from tests.research_fixture import install_slice
from tests.test_app_contract_v1 import make_root

NOW = "2026-10-03T06:30:00Z"  # after the newest row of the slice

#: audit_nhl.md §4 / §10 as published (mixed ratings publish the lower status unless only the higher part is published).
EXPECTED_CAPABILITIES = {
    "team_profiles": "PARTIAL", "player_profiles": "PARTIAL", "event_research": "PARTIAL", "team_metrics": "PARTIAL",
    "player_metrics": "PARTIAL", "team_game_logs": "PARTIAL", "player_game_logs": "PARTIAL", "historical_results": "PARTIAL",
    "opponents": "PARTIAL", "opponent_adjustment": "RESEARCH", "schedule_strength": "RESEARCH",
    "recent_form_windows": "PARTIAL", "usage": "VERIFIED", "lineups": "PARTIAL", "injuries": "PARTIAL", "matchup_metrics": "RESEARCH",
    "projection_distributions": "PARTIAL", "raw_projections": "VERIFIED", "market_prices": "VERIFIED", "market_price_history": "VERIFIED",
    "advanced_stats": "PARTIAL", "situational_splits": "PARTIAL", "player_props": "VERIFIED", "team_props": "VERIFIED",
    "game_markets": "VERIFIED", "play_by_play": "UNAVAILABLE", "weather": "UNAVAILABLE", "venue_effects": "UNAVAILABLE",
    "calibration": "VERIFIED", "historical_accuracy": "VERIFIED", "clv": "VERIFIED", "wager_history": "UNAVAILABLE",
    "rankings": "PARTIAL", "time_series": "PARTIAL", "comparisons": "PARTIAL", "search": "VERIFIED",
}


def _publish(tmp: Path) -> tuple[Path, Path]:
    root, _ = make_root(tmp, with_accounting=False)  # the production ledger is empty
    install_slice(root)
    out = tmp / "app"
    res = app_export.export(root, out, now=NOW, commit_sha="abc1234", workflow_run_id="1")
    assert res["ok"], res.get("error")
    return root, out


@pytest.fixture(scope="module")
def published(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("research")
    root, out = _publish(tmp)
    res = research_export.export_explorer(out, root)
    return root, out, res


def _load(out: Path, rel: str) -> dict:
    return json.loads((out / rel).read_text())


def _docs(out: Path, sub: str) -> list[dict]:
    return [json.loads(p.read_text()) for p in sorted((out / "explorer" / sub).glob("*.json"))]


# ----------------------------------------------------------------------------------------------- 1. verified
def test_publishes_a_verified_explorer_after_the_v1_export(published):
    root, out, res = published
    assert sync.check() == []
    assert research.verify_explorer(out) == []
    assert publish.verify_published(out) == [], "the v1 publication is untouched by the explorer"
    manifest = _load(out, "manifest.json")
    index = research.read_index(out)
    assert index["run_id"] == manifest["run_id"] == res["run_id"] and index["base_manifest_run_id"] == manifest["run_id"]
    assert index["generated_at"] == manifest["generated_at"] == NOW
    assert res["counts"]["teams"] == 32 and res["counts"]["events"] == 5 and res["counts"]["players"] > 200
    assert res["counts"]["market_history"] == 5 and res["counts"]["rankings"] > 20 and res["counts"]["series"] > 10
    # real committed history drives the season numbers: every active team has a 2025-26 xGF% with full-league context
    for prof in _docs(out, "teams"):
        obs = [o for o in prof["metrics"] if o["metric_id"] == "met_nhl.xgf_pct" and o["window"]["label"] == "2025-26"]
        assert obs and obs[0]["context"]["universe_size"] == 32 and obs[0]["quality_status"] == "PARTIAL"
        assert 1 <= obs[0]["context"]["rank"] <= 32 and len(prof["extensions"]["game_log"]["rows"]) <= research_export.GAME_LOG_CAP
    bytes_ = research.tree_bytes(out)
    assert bytes_["index.json"] <= 300_000 and bytes_["search_index.json"] <= 300_000
    for sub, cap in (("teams", 150_000), ("players", 150_000), ("events", 150_000), ("market_history", 400_000)):
        assert max(p.stat().st_size for p in (out / "explorer" / sub).glob("*.json")) <= cap, sub


def test_market_history_and_model_probability_series_come_from_the_archive(published):
    _, out, _ = published
    ev = next(e for e in _load(out, "events.json")["items"] if e["source_ids"]["nhl_game_id"] == "2026020001")
    mh = _load(out, f"explorer/market_history/{ev['event_id']}.json")
    winner = next(s for s in mh["series"] if s["kalshi_ticker"] == "KXNHLGAME-26SEP29FLACAR-FLA")
    stamps = [p["captured_at"] for p in winner["points"]]
    assert len(stamps) >= 2 and stamps == sorted(stamps) and all(p["source"].startswith("kalshi/markets") for p in winner["points"])
    model = [s for s in _docs(out, "series") if s["x_axis"] == "RUN"]
    assert model and all(s["entity_type"] == "MARKET" and s["metric_id"] == "met_nhl.model_prob_v1" for s in model)
    assert all(p["quality_status"] == "VERIFIED" and 0 <= p["value"] <= 1 for s in model for p in s["points"])
    team_series = [s for s in _docs(out, "series") if s["x_axis"] == "GAME"]
    assert team_series and all(len(s["points"]) <= research_export.GAME_LOG_CAP and s["rolling_window"] == 10 for s in team_series)
    assert all(p["opponent_id"] and p["event_id"] for s in team_series for p in s["points"])


# -------------------------------------------------------------------------------------------- 2. deterministic
def test_two_publications_of_the_same_inputs_are_byte_identical(tmp_path):
    trees = []
    for name in ("a", "b"):
        root, out = _publish(tmp_path / name)
        research_export.export_explorer(out, root)
        trees.append(research.digest_tree(out))
    assert trees[0] == trees[1]


# ------------------------------------------------------------------------------------------- 3. complete vs v1
def test_every_v1_event_and_participant_is_in_the_explorer(published):
    _, out, _ = published
    index = research.read_index(out)
    for ev in _load(out, "events.json")["items"]:
        assert f"events/{ev['event_id']}.json" in index["files"]
        assert f"market_history/{ev['event_id']}.json" in index["files"]
        er = _load(out, f"explorer/events/{ev['event_id']}.json")
        assert er["event"] == ev and {p["participant_id"] for p in er["participants"]} == {p["participant_id"] for p in ev["participants"]}
        for p in ev["participants"]:
            assert f"teams/{p['participant_id']}.json" in index["files"]
            assert _load(out, f"explorer/teams/{p['participant_id']}.json")["entity"] == p, "the same prt_ identity as v1"
    v1_markets = {m["market_id"] for m in _load(out, "markets.json")["items"] if m.get("event_id")}
    assert v1_markets == {m["market_id"] for er in _docs(out, "events") for m in er["markets"]}


# ---------------------------------------------------------------------------------------- 4. capability honesty
def test_capability_statuses_match_the_audit(published):
    _, out, _ = published
    caps = {c["capability"]: c for c in _load(out, "explorer/capabilities.json")["items"]}
    assert {k: v["status"] for k, v in caps.items()} == EXPECTED_CAPABILITIES
    assert research_export.CAPABILITY_STATUS == EXPECTED_CAPABILITIES
    assert caps["opponent_adjustment"]["reasons"] and caps["schedule_strength"]["reasons"]
    for c in caps.values():
        if c["status"] in ("PARTIAL", "RESEARCH"):
            assert c["limitations"], c["capability"]
    registry = _load(out, "explorer/metrics.json")["items"]
    rankings = {d["metric_id"] for d in _docs(out, "rankings")}
    for m in registry:
        if m["supports"]["rank"]:
            assert m["metric_id"] in rankings, f"{m['metric_id']} claims rank support without a ranking"
        # only the met_nhl.oa_* metrics are opponent-adjusted, and they say so (category, basis, version); nothing raw claims it
        if m["supports"]["opponent_adjustment"] or m["supports"]["schedule_adjustment"]:
            assert m["metric_id"].startswith("met_nhl.oa_") and m["category"] == "opponent_adjusted", m["metric_id"]
            assert m["extensions"]["basis"] == "OPPONENT_ADJUSTED" and m["extensions"]["version"] == "nhl-oppadj-1.0"
        else:
            assert not m["metric_id"].startswith("met_nhl.oa_")


# ------------------------------------------------------------------------------------------------- 5. packet
def test_game_packet_has_markets_and_both_participants(published):
    _, out, _ = published
    ev = next(e for e in _load(out, "events.json")["items"] if e["source_ids"]["nhl_game_id"] == "2026020001")
    pk = packet.build(app_root=out, scope_kind="GAME", event_id=ev["event_id"])
    assert pk["markets"] and all(m["event_id"] == ev["event_id"] for m in pk["markets"])
    evidence = {e["entity_id"] for e in pk["evidence"]}
    assert {p["participant_id"] for p in ev["participants"]} <= evidence
    assert pk["quality"]["missing"] == []
    assert pk["quality"]["capabilities"]["opponent_adjustment"] == "RESEARCH"
    assert packet.build(app_root=out, scope_kind="GAME", event_id=ev["event_id"]) == pk


# --------------------------------------------------------------------------------------------- 6. no secrets
def test_no_secret_shaped_strings(published):
    _, out, _ = published
    assert research.no_secret_shaped_strings(out) == []


# ------------------------------------------------------------------------------------- 7. RESEARCH survives
def test_research_observations_stay_research_in_profiles_and_packets(published):
    _, out, _ = published
    registry = {m["metric_id"]: m for m in _load(out, "explorer/metrics.json")["items"]}
    assert registry["met_nhl.model_expected_goals"]["quality"]["status"] == "RESEARCH"
    found = [o for prof in _docs(out, "teams") for o in prof["metrics"] if o["metric_id"] == "met_nhl.model_expected_goals"]
    assert found and all(o["quality_status"] == "RESEARCH" for o in found)
    ev = next(e for e in _load(out, "events.json")["items"] if e["source_ids"]["nhl_game_id"] == "2026020001")
    er = _load(out, f"explorer/events/{ev['event_id']}.json")
    rows = [r for r in er["matchup"] if r["metric_id"] == "met_nhl.model_expected_goals"]
    assert rows and all(r["home"]["quality_status"] == "RESEARCH" for r in rows)
    pk = packet.build(app_root=out, scope_kind="GAME", event_id=ev["event_id"], max_chars=10_000_000)
    obs = [o for e in pk["evidence"] for o in e["observations"] if o["metric_id"] == "met_nhl.model_expected_goals"]
    assert obs and all(o["quality_status"] == "RESEARCH" for o in obs)
    assert "met_nhl.model_expected_goals" in pk["quality"]["research_only_items"]


# ------------------------------------------------------------------------------------- 8. failure is atomic
def test_a_failing_publish_leaves_the_previous_tree_intact(tmp_path, published):
    root, out, _ = published
    work = tmp_path / "copy"
    shutil.copytree(out, work)
    before = research.digest_tree(work)
    inp = research_export.load_research_inputs(work, root)
    docs, meta = research_export.build_explorer(inp, run_id=inp.manifest["run_id"], generated_at=NOW)
    broken = [d for d in docs if d["kind"] != "metric_registry"]
    with pytest.raises(research.ExplorerError) as exc:
        research.publish_explorer(app_root=work, sport="NHL", run_id=inp.manifest["run_id"], generated_at=NOW, documents=broken,
                                  quality=meta["quality"], as_of=meta["as_of"])
    assert any("metric_registry" in p for p in exc.value.problems)
    assert research.digest_tree(work) == before and research.verify_explorer(work) == []
    # and through the CLI: a missing v1 manifest exits 1 without touching anything
    rc = research_export.main(["--data-root", str(root), "--out", str(tmp_path / "nothing")])
    assert rc == 1 and not (tmp_path / "nothing" / "explorer").exists()


# ------------------------------------------------------------------------------------------- refresh gate
def _cli(root: Path, out: Path, *extra: str) -> tuple[int, dict]:
    import contextlib
    import io

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = research_export.main(["--data-root", str(root), "--out", str(out), *extra])
    return rc, json.loads(buf.getvalue() or "{}")


def test_a_second_export_within_the_interval_is_skipped_and_leaves_the_tree_untouched(tmp_path, published):
    root, out, _ = published
    work = tmp_path / "copy"
    shutil.copytree(out, work)
    before = research.digest_tree(work)
    rc, res = _cli(root, work, "--min-interval-minutes", "60", "--now", "2026-10-03T07:00:00Z")
    assert rc == 0 and res["skipped"] is True and "unchanged" in res["reason"]
    assert research.digest_tree(work) == before
    rc, res = _cli(root, work, "--min-interval-minutes", "60", "--now", "2026-10-03T08:00:00Z")
    assert rc == 0 and not res.get("skipped") and research.read_index(work)["generated_at"] == "2026-10-03T08:00:00Z"
    assert research.verify_explorer(work) == []


def test_a_changed_v1_event_set_triggers_a_rebuild(tmp_path, published):
    root, out, _ = published
    work = tmp_path / "copy"
    shutil.copytree(out, work)
    events = _load(work, "events.json")
    dropped = events["items"].pop()
    events["count"] = len(events["items"])
    (work / "events.json").write_text(json.dumps(events))
    due, reason = research.refresh_due(work, now="2026-10-03T06:40:00Z", min_interval_seconds=3600)
    assert due and "events changed" in reason
    rc, res = _cli(root, work, "--min-interval-minutes", "60", "--now", "2026-10-03T06:40:00Z")
    assert rc == 0 and not res.get("skipped") and res["counts"]["events"] == len(events["items"])
    assert f"events/{dropped['event_id']}.json" not in research.read_index(work)["files"]
    assert research.verify_explorer(work) == []


# ----------------------------------------------------------------------------------------- CLI / workflow / worker
def test_cli_workflow_and_worker_run_the_research_export_after_the_app_export(tmp_path):
    import yaml

    from nhl_edge.cli import build_parser
    from nhl_edge.worker.run import Worker

    args = build_parser().parse_args(["research-export", "--data-root", "x", "--out", "y"])
    assert args.fn.__name__ == "cmd_research_export" and args.data_root == "x" and args.out == "y"
    steps = yaml.safe_load((REPO_ROOT / ".github" / "workflows" / "conductor.yml").read_text())["jobs"]["run"]["steps"]
    ids_ = [s.get("id") for s in steps]
    names = [s.get("name", "") for s in steps]
    i_app, i_res = ids_.index("app_export"), ids_.index("research_export")
    i_push = names.index(next(n for n in names if n.startswith("Verify archive immutability and push")))
    assert i_res == i_app + 1 < i_push and steps[i_res].get("continue-on-error") is True
    assert "nhl research-export --data-root data/archive --out data/archive/app/latest" in steps[i_res]["run"]
    assert "GITHUB_STEP_SUMMARY" in steps[i_res]["run"]
    i_fail = next(i for i, s in enumerate(steps) if "steps.research_export.outcome" in str(s.get("if", "")))
    assert i_fail > i_push and "exit 1" in steps[i_fail]["run"]
    # the capture worker considers the explorer after every successful app export (gated by refresh_due) and records failures
    calls: list[list[str]] = []
    w = Worker.__new__(Worker)
    w.archive_root, w.data_root = tmp_path / "archive", tmp_path
    w.run_cmd = lambda cmd, timeout: (calls.append(cmd), (0, ""))[1]
    jobs_run, jobs_failed = ["app_export"], []
    w._run_research_export(jobs_run, jobs_failed)
    assert jobs_run == ["app_export", "research_export"] and calls[-1][:2] == ["nhl", "research-export"]
    assert calls[-1][-2:] == ["--min-interval-minutes", "60"], "the worker rebuilds at most hourly unless the events change"
    w.run_cmd = lambda cmd, timeout: (calls.append(cmd), (2, "boom"))[1]
    jobs_run, jobs_failed = ["app_export"], []
    w._run_research_export(jobs_run, jobs_failed)
    assert jobs_failed == ["research_export"]
    jobs_run, jobs_failed = ["settle"], []
    n = len(calls)
    w._run_research_export(jobs_run, jobs_failed)
    assert len(calls) == n and jobs_run == ["settle"], "no app export, no explorer re-publication"


# --------------------------------------------------------------------------------------------- real data
def test_real_data_smoke(tmp_path):
    """Against the production archive when it is checked out (data/archive, or NHL_EDGE_ARCHIVE_ROOT)."""
    root = Path(os.environ.get("NHL_EDGE_ARCHIVE_ROOT") or (REPO_ROOT / "data" / "archive"))
    if not (root / "manifest.jsonl").exists() or not (root / "slates" / "latest" / "slate.json").exists():
        pytest.skip("production data lives on the data-archive branch; check it out at data/archive (or set NHL_EDGE_ARCHIVE_ROOT)")
    out = tmp_path / "app"
    assert app_export.export(root, out, now=NOW)["ok"]
    res = research_export.export_explorer(out, root)
    assert research.verify_explorer(out) == [] and research.no_secret_shaped_strings(out) == []
    caps = {c["capability"]: c["status"] for c in _load(out, "explorer/capabilities.json")["items"]}
    assert caps == EXPECTED_CAPABILITIES
    assert res["counts"]["events"] == len(_load(out, "events.json")["items"]) and res["counts"]["teams"] == 32
    ev = _load(out, "events.json")["items"][0]
    pk = packet.build(app_root=out, scope_kind="GAME", event_id=ev["event_id"])
    assert pk["markets"] and pk["quality"]["missing"] == []
