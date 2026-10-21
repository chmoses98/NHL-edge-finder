"""Scorecard: group separation, alarm rules and ledger idempotency."""

from __future__ import annotations

import json
from pathlib import Path

from nhl_edge.market_audit.scorecard import GROUPS, alarms, append_ledger, build_scorecard, render_md


def write(d: Path, name: str, obj) -> None:
    (d / name).write_text(json.dumps(obj))


def healthy(d: Path) -> None:
    write(d, "integrity_report.json", {"n_problems": 0, "duplicate_paths": 0, "manifest_sha256": "abc", "delta_chains": {"kalshi/markets": {"n_broken": 0}}})
    write(d, "coverage_report.json", {"ticks": {"n_gaps_over_60min": 0, "last": "t"}, "totals": {"independent_games_final": 151}})
    write(d, "outcome_reconciliation.json", {"vs_production_settlement": {"disagreements": 0}, "games_with_reconciliation_problems": {}, "taxonomy": [{"semantics_status": "PROVEN", "n": 5}]})
    write(d, "wager_summary.json", {"n": 34, "net_pl": -187.6, "ledger_vs_resolver_disagreements": 0})
    write(d, "hypothesis_results.json", {"results": {"M1": {"class": "REJECTED", "prospective": {"n_games": 3, "roi": 0.0, "status": "ACCUMULATING", "next_look_at_games": 150}}}})
    write(d, "lineage.json", {"archive_manifest_sha256": "abc", "audit_version": "v"})


def test_healthy_data_raises_no_alarms(tmp_path):
    healthy(tmp_path)
    assert alarms(tmp_path) == []


def test_every_integrity_and_semantics_failure_is_an_alarm(tmp_path):
    healthy(tmp_path)
    write(tmp_path, "integrity_report.json", {"n_problems": 2, "duplicate_paths": 0, "delta_chains": {"kalshi/markets": {"n_broken": 1}}})
    write(tmp_path, "outcome_reconciliation.json", {"vs_production_settlement": {"disagreements": 3}, "games_with_reconciliation_problems": {"g": ["x"]},
                                                    "taxonomy": [{"semantics_status": "UNRESOLVED", "n": 4}]})
    write(tmp_path, "wager_summary.json", {"ledger_vs_resolver_disagreements": 1})
    levels = [a["level"] for a in alarms(tmp_path)]
    assert levels.count("CRITICAL") == 4 and "WARN" in levels


def test_groups_are_separate_and_independent_handicapping_is_not_measurable(tmp_path):
    healthy(tmp_path)
    sc = build_scorecard(tmp_path)
    assert set(sc["groups"]) == set(GROUPS)
    assert sc["groups"]["INDEPENDENT_HANDICAPPING"]["status"] == "NOT_MEASURABLE"
    assert sc["groups"]["ACTUAL_WAGERS"]["net_pl"] == -187.6
    assert "net_pl" not in sc["groups"]["PROSPECTIVE_SHADOW"]  # no cross-group totals exist
    assert "never summed" in render_md(sc)


def test_ledger_append_is_idempotent_per_archive_snapshot(tmp_path):
    healthy(tmp_path)
    sc = build_scorecard(tmp_path)
    ledger = tmp_path / "ledger" / "evidence.jsonl"
    assert append_ledger(ledger, sc) is True
    assert append_ledger(ledger, sc) is False
    assert len(ledger.read_text().splitlines()) == 1
    sc2 = dict(sc, archive_manifest_sha256="different")
    assert append_ledger(ledger, sc2) is True and len(ledger.read_text().splitlines()) == 2
