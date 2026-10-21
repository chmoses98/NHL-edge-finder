"""Daily research scorecard + longitudinal evidence ledger (Phase J). Reads pipeline outputs only; bounded, idempotent.

Profit is reported PER GROUP and never summed across groups:
    ACTUAL_WAGERS               routed wagers the owner placed (accounting-data ledger, real fills)
    MODEL_RESEARCH_SELECTIONS   what the thesis workflow selected (research stakes; replayed at first-selection prices)
    INDEPENDENT_HANDICAPPING    NOT MEASURABLE: the ledger carries no provenance field (see note)
    BACKTEST_SELECTIONS         pre-registered market-only strategies replayed on history / the one-shot LIVE tier
    PROSPECTIVE_SHADOW          the same frozen strategies on games that STARTED after the registry freeze; read only at fixed looks

The evidence ledger gets one line per distinct archive snapshot (manifest digest): re-running on unchanged data appends nothing.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

GROUPS = ("ACTUAL_WAGERS", "MODEL_RESEARCH_SELECTIONS", "INDEPENDENT_HANDICAPPING", "BACKTEST_SELECTIONS", "PROSPECTIVE_SHADOW")


def _load(d: Path, name: str, default: Any = None) -> Any:
    p = d / name
    return json.loads(p.read_text()) if p.exists() else default


def alarms(d: Path) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    integ = _load(d, "integrity_report.json", {})
    if integ.get("n_problems", 0) or integ.get("duplicate_paths", 0):
        out.append({"level": "CRITICAL", "what": f"ledger integrity: {integ.get('n_problems')} problems, {integ.get('duplicate_paths')} duplicate paths"})
    for kind, v in (integ.get("delta_chains") or {}).items():
        if v.get("n_broken", 0):
            out.append({"level": "CRITICAL", "what": f"{v['n_broken']} broken delta chain(s) in {kind}"})
    cov = _load(d, "coverage_report.json", {})
    if (cov.get("ticks") or {}).get("n_gaps_over_60min", 0):
        out.append({"level": "WARN", "what": f"{cov['ticks']['n_gaps_over_60min']} capture gap(s) over 60 minutes"})
    rec = _load(d, "outcome_reconciliation.json", {})
    prod = rec.get("vs_production_settlement") or {}
    if prod.get("disagreements", 0):
        out.append({"level": "CRITICAL", "what": f"independent resolver disagrees with production settlement on {prod['disagreements']} contracts"})
    if rec.get("games_with_reconciliation_problems"):
        out.append({"level": "WARN", "what": f"{len(rec['games_with_reconciliation_problems'])} game(s) fail final/play-by-play/boxscore reconciliation"})
    bad_spec = [r for r in (rec.get("taxonomy") or []) if r.get("semantics_status") != "PROVEN"]
    if bad_spec:
        out.append({"level": "WARN", "what": f"{sum(r['n'] for r in bad_spec)} contract(s) with unproven semantics (new contract shape?)"})
    ws = _load(d, "wager_summary.json", {})
    if ws.get("ledger_vs_resolver_disagreements", 0):
        out.append({"level": "CRITICAL", "what": f"{ws['ledger_vs_resolver_disagreements']} routed-wager settlement(s) disagree with the independent resolver"})
    if (integ.get("season_level_markets") or {}).get("unresolved"):
        out.append({"level": "INFO", "what": "season-level series without an ontology entry: " + ", ".join(r["series_ticker"] for r in integ["season_level_markets"]["unresolved"])})
    return out


def build_scorecard(d: Path) -> dict[str, Any]:
    integ, cov = _load(d, "integrity_report.json", {}), _load(d, "coverage_report.json", {})
    reg = (_load(d, "hypothesis_results.json", {}) or {}).get("results", {})
    ws = _load(d, "wager_summary.json", {})
    th = _load(d, "thesis_replay.json", {})
    lineage = _load(d, "lineage.json", {})
    classes: dict[str, int] = {}
    for v in reg.values():
        classes[v["class"]] = classes.get(v["class"], 0) + 1
    pro = {k: v["prospective"] for k, v in reg.items() if v.get("prospective")}
    sc: dict[str, Any] = {
        "generated_at_utc": datetime.now(UTC).isoformat(timespec="seconds"), "archive_manifest_sha256": lineage.get("archive_manifest_sha256") or integ.get("manifest_sha256"),
        "audit_version": lineage.get("audit_version"), "code_commit": lineage.get("code_commit"),
        "data": {"independent_final_games": (cov.get("totals") or {}).get("independent_games_final"), "last_tick": (cov.get("ticks") or {}).get("last"),
                 "contracts_on_final_games": (cov.get("totals") or {}).get("contracts_on_final_games"),
                 "decided_contracts_with_usable_pregame_quote": (cov.get("totals") or {}).get("decided_with_usable_pregame_quote")},
        "alarms": alarms(d),
        "groups": {
            "ACTUAL_WAGERS": {k: ws.get(k) for k in ("n", "staked", "net_pl", "roi_on_stake", "wins", "fees", "expected_pl_at_market_mid", "z_realized_vs_expected")},
            "MODEL_RESEARCH_SELECTIONS": {k: th.get(k) for k in ("S1_first_FUNDED|all", "S2_first_chosen|all", "S1_first_FUNDED|ex_goalscorer", "S2_first_chosen|ex_goalscorer")},
            "INDEPENDENT_HANDICAPPING": {"status": "NOT_MEASURABLE", "note": "wager rows carry no provenance; 'no thesis-card decision exists' is only a proxy and is reported inside ACTUAL_WAGERS."},
            "BACKTEST_SELECTIONS": {"registry_classes": classes, "n_hypotheses": len(reg)},
            "PROSPECTIVE_SHADOW": {"hypotheses_with_games": len(pro), "max_games": max((v.get("n_games", 0) for v in pro.values()), default=0),
                                   "status": "ACCUMULATING" if all(v.get("status") == "ACCUMULATING" for v in pro.values()) else "AT_LOOK",
                                   "per_hypothesis": {k: {"n_games": v.get("n_games"), "roi": v.get("roi"), "next_look_at_games": v.get("next_look_at_games")} for k, v in pro.items()}},
        },
    }
    return sc


def append_ledger(ledger: Path, sc: dict[str, Any]) -> bool:
    """Append one line per distinct archive snapshot. Returns False (and writes nothing) if that snapshot is already recorded."""
    ledger.parent.mkdir(parents=True, exist_ok=True)
    key = sc.get("archive_manifest_sha256")
    if ledger.exists():
        for line in ledger.read_text().splitlines():
            if line.strip() and json.loads(line).get("archive_manifest_sha256") == key:
                return False
    with ledger.open("a") as f:
        f.write(json.dumps({k: sc[k] for k in ("generated_at_utc", "archive_manifest_sha256", "audit_version", "code_commit", "data", "alarms", "groups")}, default=str) + "\n")
    return True


def render_md(sc: dict[str, Any]) -> str:
    L = ["# NHL market audit -- daily research scorecard", "", f"archive manifest `{str(sc['archive_manifest_sha256'])[:16]}` · generated {sc['generated_at_utc']}", "",
         "> RESEARCH ONLY. Groups below are never summed together.", "", "## Alarms", ""]
    L += [f"- **{a['level']}** {a['what']}" for a in sc["alarms"]] or ["- none"]
    L += ["", "## Data", "", *[f"- {k}: {v}" for k, v in sc["data"].items()], "", "## Groups", ""]
    for g in GROUPS:
        L += [f"### {g}", "", "```json", json.dumps(sc["groups"][g], indent=1, default=str), "```", ""]
    return "\n".join(L)


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--data", type=Path, required=True, help="pipeline --out directory")
    ap.add_argument("--ledger", type=Path, required=True, help="evidence ledger JSONL (append-only)")
    a = ap.parse_args(argv)
    sc = build_scorecard(a.data)
    (a.data / "scorecard.json").write_text(json.dumps(sc, indent=1, default=str))
    (a.data / "SCORECARD.md").write_text(render_md(sc))
    print("ledger line appended" if append_ledger(a.ledger, sc) else "snapshot already in ledger; nothing appended")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
