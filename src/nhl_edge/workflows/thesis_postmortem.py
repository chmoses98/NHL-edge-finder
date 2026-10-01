"""Evaluate-job step: thesis-card decisions x official results -> ``thesis_postmortems`` (append-only, deduped on
(decision_id, settlement_key)) and ``eval/report_thesis.{json,md}``. Called from ``nhl evaluate``; never blocks it.

A decision is scored once its contract is settled, the game's official final result exists, and its official goal /
goalie events have been ingested (``player_events/*``, written by the settle job). Only decisions made strictly before
the scheduled start are scored. The report's card-level view uses each game's LAST pregame decision run.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime
from typing import Any

from nhl_edge.evaluation.clv import closing_snapshot
from nhl_edge.log import get_logger, kv
from nhl_edge.settlement.engine import SettlementOutcome
from nhl_edge.thesis.features import DrawFeatures
from nhl_edge.thesis.postmortem import actual_view, portfolio_result, score_decision
from nhl_edge.timeutil import iso, parse_iso

log = get_logger(__name__)


def run_thesis_postmortem(ledger: Any, settlements: dict[str, Any], starts: dict[str, datetime], obs_loader: Any, now: datetime) -> dict[str, Any]:
    from nhl_edge.workflows.evaluate import close_price_cents
    from nhl_edge.workflows.settle import load_final_results

    decisions = list(ledger.iter_rows("thesis_decisions"))
    if not decisions:
        return {"n_rows": 0, "note": "no thesis decisions yet"}
    games = {(r.get("run_id"), str(r.get("game_id"))): r for r in ledger.iter_rows("thesis_games")}
    existing = list(ledger.iter_rows("thesis_postmortems"))
    seen = {(r.get("decision_id"), r.get("settlement_key")) for r in existing}
    finals = load_final_results(ledger)
    need = {str(d["game_id"]) for d in decisions if str(d["game_id"]) in finals}
    goals: dict[str, list[dict[str, Any]]] = defaultdict(list)
    goalies: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for kind, acc in (("player_events/goals", goals), ("player_events/goalies", goalies)):
        for r in ledger.iter_rows(kind):
            g = str(r.get("game_id"))
            if g in need:
                acc[g].append(r)
    actual: dict[str, dict[str, Any]] = {}
    for gid in need:
        if not goalies.get(gid):
            continue  # official events not ingested yet: retry on the next evaluate run
        d0 = next(d for d in decisions if str(d["game_id"]) == gid)
        away, home = str(d0.get("matchup", "AWY @ HOM")).split(" @ ")
        res = finals[gid].model_dump(mode="json")
        try:
            actual[gid] = actual_view(DrawFeatures.from_actual(res, goals.get(gid, []), goalies[gid], home, away))
        except Exception as e:  # noqa: BLE001 - one malformed game never blocks the rest
            log.warning(kv(event="thesis_actual_failed", game=gid, err=str(e)[:200]))
    tickers = {d["ticker"] for d in decisions if str(d["game_id"]) in actual and d["ticker"] in settlements}
    obs = obs_loader(tickers) if tickers else {}
    new_rows = []
    for d in decisions:
        gid = str(d["game_id"])
        rec = settlements.get(d["ticker"])
        start = starts.get(gid)
        if rec is None or gid not in actual or start is None or rec.outcome not in (SettlementOutcome.YES, SettlementOutcome.NO):
            continue
        if parse_iso(d["decided_at_utc"]) >= start or (d["decision_id"], rec.idempotency_key) in seen:
            continue
        close = closing_snapshot(obs.get(d["ticker"], []), start)
        cp = close_price_cents(close)
        row = score_decision(d, actual[gid], rec.outcome == SettlementOutcome.YES, None if cp is None else cp / 100.0)
        row["settlement_key"] = rec.idempotency_key
        row["evaluated_at_utc"] = iso(now)
        new_rows.append(row)
        seen.add((d["decision_id"], rec.idempotency_key))
    if new_rows:
        ledger.append_rows("thesis_postmortems", new_rows, observed_at=now)
    rows = existing + new_rows
    rep = build_report(rows, games, now)
    out = ledger.root / "eval"
    out.mkdir(parents=True, exist_ok=True)
    (out / "report_thesis.json").write_text(json.dumps(rep, indent=1, default=str))
    (out / "report_thesis.md").write_text(report_markdown(rep))
    log.info(kv(event="thesis_postmortem", rows=len(rows), new=len(new_rows)))
    return rep


def build_report(rows: list[dict[str, Any]], games: dict[tuple[str, str], dict[str, Any]], now: datetime) -> dict[str, Any]:
    last_run: dict[str, str] = {}
    for r in rows:
        g = str(r["game_id"])
        if g not in last_run or str(r["decided_at_utc"]) > str(last_run[g][1]):
            last_run[g] = (r["run_id"], r["decided_at_utc"])
    final = [r for r in rows if last_run.get(str(r["game_id"]), (None,))[0] == r["run_id"]]
    chosen = [r for r in final if r["chosen"]]

    def summarize(rs: list[dict[str, Any]]) -> dict[str, Any]:
        if not rs:
            return {"n": 0}
        clv = [r["price_result_clv"] for r in rs if r["price_result_clv"] is not None]
        mr = [r["model_result"] for r in rs]
        bm = [m["brier_kalshi_mid"] for m in mr if m["brier_kalshi_mid"] is not None]
        return {"n": len(rs), "won": sum(r["won"] for r in rs), "expression_results": dict(Counter(r["expression_result"] for r in rs)),
                "thesis_hit_rate": round(sum(1 for r in rs if r["thesis_result"]) / max(1, sum(1 for r in rs if r["thesis_result"] is not None)), 3),
                "mean_clv": round(sum(clv) / len(clv), 4) if clv else None, "n_clv": len(clv),
                "brier_model": round(sum(m["brier_model"] for m in mr) / len(mr), 4), "brier_adjusted": round(sum(m["brier_adjusted"] for m in mr) / len(mr), 4),
                "brier_kalshi_mid": round(sum(bm) / len(bm), 4) if bm else None,
                "realized_profit": round(sum(r["realized_profit"] or 0 for r in rs), 2), "stake": round(sum(r["stake_dollars"] or 0 for r in rs), 2)}

    per_game = {}
    for g in sorted({str(r["game_id"]) for r in final}):
        gr = [r for r in final if str(r["game_id"]) == g]
        per_game[g] = {"realized_script": gr[0]["realized_script_name"], "actual": gr[0]["actual_game"], "decision_run": last_run[g][0],
                       "portfolio_result": portfolio_result(gr, games.get((last_run[g][0], g))),
                       "bets": [{k: r[k] for k in ("bet_id", "chosen", "stake_dollars", "won", "primary_thesis", "thesis_result", "expression_result",
                                                   "model_p_bet_given_thesis_outcome", "model_p_win_in_realized_script", "price_result_clv", "realized_profit")} for r in gr]}
    return {"evaluated_at_utc": iso(now), "authority": "RESEARCH_ONLY", "n_rows_all_runs": len(rows), "n_games": len(per_game),
            "final_card": summarize(chosen), "final_shortlist": summarize(final), "games": per_game,
            "note": ("Prospective thesis-card evidence. THESIS / EXPRESSION / PRICE / MODEL / PORTFOLIO results are kept separate on purpose: a right thesis "
                     "expressed through a contract that lost is not a wrong prediction. A handful of games proves nothing; never tune to one slate.")}


def report_markdown(rep: dict[str, Any]) -> str:
    L = [f"# Thesis-card postmortem — {rep['authority']}", "", f"evaluated {rep['evaluated_at_utc']} · games {rep['n_games']} · rows (all runs) {rep['n_rows_all_runs']}", ""]
    for lab, key in (("Final card (chosen bets, last pregame run)", "final_card"), ("Final shortlist (all shortlisted, last pregame run)", "final_shortlist")):
        s = rep[key]
        L += [f"## {lab}", "", "```", json.dumps(s, indent=1, default=str), "```", ""]
    for g, v in rep["games"].items():
        L += [f"## game {g}: realised script {v['realized_script']}", "", f"portfolio: {json.dumps(v['portfolio_result'], default=str)}", "",
              "| bet | chosen | stake | won | thesis | thesis hit | expression | model P(bet|thesis outcome) | model P(win|realised script) | CLV | P/L |", "|---|---|---:|---|---|---|---|---:|---:|---:|---:|"]
        for b in v["bets"]:
            L.append(f"| {b['bet_id']} | {b['chosen']} | {b['stake_dollars']} | {b['won']} | {b['primary_thesis']} | {b['thesis_result']} | {b['expression_result']} | "
                     f"{b['model_p_bet_given_thesis_outcome']} | {b['model_p_win_in_realized_script']} | {b['price_result_clv']} | {b['realized_profit']} |")
        L.append("")
    L += [f"_{rep['note']}_", ""]
    return "\n".join(L)
