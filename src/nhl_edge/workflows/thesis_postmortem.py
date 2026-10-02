"""Evaluate-job step: thesis-card decisions x official results -> ``thesis_postmortems`` (append-only, deduped on
(decision_id, settlement_key)) and ``eval/report_thesis.{json,md}``. Called from ``nhl evaluate``; never blocks it.

A decision is scored once its contract is settled, the game's official final result exists, and its official goal /
goalie events have been ingested (``player_events/*``, written by the settle job). Only decisions made strictly before
the scheduled start are scored.

Two views, never mixed:

* FINAL_CARD_UNIQUE -- the card P/L view. For each game: the ONE latest complete (card_status COMPLETE or NO_BETS)
  pregame thesis-card SNAPSHOT before the scheduled puck drop, and only the decisions of that exact snapshot. A snapshot
  is one thesis-card generation (one ``nhl simulate`` invocation), identified by ``snapshot_id`` (rows since
  nhl-card-1.1) or, for older rows, by the pair (run_id, decided_at_utc) -- which hashes to the same id
  (``workflows.thesis_card.snapshot_id``). A worker ``run_id`` alone spans many generations and is NOT a snapshot
  identity (the pre-fix report selected by run_id and so summed every generation of the last worker: 23 "final card"
  bets for 3 games on 2026-10-01, where the cap allows at most 12). The snapshot is chosen from ``thesis_games`` (one
  row per game per generation) -- not from decisions -- so a generation with no shortlisted bet is still the final one.
  Every chosen decision must match the snapshot's ``recommended`` list; any duplicate or mismatch marks the game
  AMBIGUOUS_FINAL_SNAPSHOT and excludes it from every P/L figure (fail closed).
* ALL_PROSPECTIVE_DECISIONS -- every scored decision of every pregame generation: calibration research only, with the
  number of unique logical wagers next to the row count so repeated observations are visible as repeats. No P/L.

Completeness is reported per slate (ET date): a slate is COMPLETE only when every scheduled game is final, settled,
has its official events ingested and has its final card fully scored. Until then the slate is labelled
"PARTIAL — k/n games evaluated" and no figure is presented as the slate's final ROI.
"""

from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from datetime import datetime
from typing import Any

from nhl_edge.evaluation.clv import closing_snapshot
from nhl_edge.log import get_logger, kv
from nhl_edge.settlement.engine import SettlementOutcome
from nhl_edge.thesis.features import DrawFeatures
from nhl_edge.thesis.fidelity import expression_kind, from_logged, is_player_prop
from nhl_edge.thesis.postmortem import actual_view, portfolio_result, research_profit, score_decision
from nhl_edge.timeutil import iso, parse_iso

log = get_logger(__name__)

COMPLETE_CARD_STATUSES = ("COMPLETE", "NO_BETS")
DEFAULT_GAME_CAP = 4
AMBIGUOUS = "AMBIGUOUS_FINAL_SNAPSHOT"
TERMINAL_OUTCOMES = (SettlementOutcome.VOID, SettlementOutcome.PUSH, SettlementOutcome.UNSETTLEABLE)


def snapshot_key(row: dict[str, Any]) -> str:
    from nhl_edge.workflows.thesis_card import snapshot_id

    return row.get("snapshot_id") or snapshot_id(str(row.get("run_id")), str(row.get("decided_at_utc")))


def _start_of(gid: str, starts: dict[str, datetime], row: dict[str, Any] | None) -> datetime | None:
    if gid in starts:
        return starts[gid]
    st = ((row or {}).get("meta") or {}).get("start_time_utc") or (row or {}).get("start_time_utc")
    try:
        return parse_iso(st) if st else None
    except ValueError:
        return None


def final_snapshots(games_rows: list[dict[str, Any]], decisions: list[dict[str, Any]], starts: dict[str, datetime]) -> dict[str, dict[str, Any]]:
    """gid -> the final-card snapshot of that game (see module doc), with its chosen decisions, or a fail-closed status."""
    by_game: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for r in games_rows:
        by_game[str(r.get("game_id"))][snapshot_key(r)].append(r)
    dec_by: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for d in decisions:
        dec_by[(str(d.get("game_id")), snapshot_key(d))].append(d)
    # legacy safety: decisions whose generation has no thesis_games row still define a (weaker) snapshot
    for (gid, sk), ds in dec_by.items():
        if sk not in by_game[gid]:
            by_game[gid][sk] = [{"game_id": gid, "decided_at_utc": ds[0].get("decided_at_utc"), "run_id": ds[0].get("run_id"), "card_status": ds[0].get("card_status"),
                                 "recommended": None, "_synthetic": True, "meta": {"start_time_utc": ds[0].get("start_time_utc")}}]
    out: dict[str, dict[str, Any]] = {}
    for gid, snaps in by_game.items():
        row0 = next(iter(snaps.values()))[0]
        start = _start_of(gid, starts, row0)
        pre = []
        for sk, rows in snaps.items():
            try:
                t = parse_iso(rows[0]["decided_at_utc"])
            except (KeyError, ValueError, TypeError):
                continue
            if start is not None and t < start:
                pre.append((t, sk, rows))
        if start is None:
            out[gid] = {"status": "NO_START_TIME", "reason": "no scheduled start: pregame status cannot be established"}
            continue
        if not pre:
            out[gid] = {"status": "NO_PREGAME_SNAPSHOT", "reason": "no thesis-card generation before the scheduled start"}
            continue
        pre.sort(key=lambda x: (x[0], x[1]))
        complete = [x for x in pre if str(x[2][0].get("card_status")) in COMPLETE_CARD_STATUSES]
        skipped = [x[1] for x in pre if complete and x[0] > complete[-1][0]]
        if not complete:
            out[gid] = {"status": "NO_COMPLETE_PREGAME_SNAPSHOT", "reason": "every pregame generation failed the completion gate (card not emitted)",
                        "n_pregame_snapshots": len(pre)}
            continue
        t, sk, rows = complete[-1]
        same_instant = [x for x in complete if x[0] == t and x[1] != sk]
        ds = dec_by.get((gid, sk), [])
        chosen = [d for d in ds if d.get("chosen")]
        ids = [d["bet_id"] for d in chosen]
        cap = int(((rows[0].get("portfolio_config") or {}).get("max_bets_per_game")) or DEFAULT_GAME_CAP)
        problems = []
        if len(rows) > 1:
            problems.append(f"{len(rows)} thesis_games rows share snapshot {sk}")
        if same_instant:
            problems.append(f"another complete generation has the same decision instant {iso(t)}")
        if len(set(ids)) != len(ids):
            problems.append("a bet appears more than once in one snapshot")
        rec = rows[0].get("recommended")
        if rec is not None and sorted(rec) != sorted(ids):
            problems.append(f"chosen decisions {sorted(ids)} != snapshot recommended {sorted(rec)}")
        if len(ids) > cap:
            problems.append(f"{len(ids)} chosen bets exceed the {cap}-bet game cap")
        info = {"snapshot_id": sk, "decided_at_utc": iso(t), "run_id": rows[0].get("run_id"), "card_status": rows[0].get("card_status"), "game_card_cap": cap,
                "chosen": chosen, "n_chosen": len(chosen), "n_shortlisted": len(ds), "n_pregame_snapshots": len(pre), "later_incomplete_snapshots_skipped": skipped,
                "game_row": rows[0], "start_utc": iso(start), "synthetic_game_row": bool(rows[0].get("_synthetic"))}
        out[gid] = info | ({"status": AMBIGUOUS, "reason": "; ".join(problems)} if problems else {"status": "OK"})
    return out


def run_thesis_postmortem(ledger: Any, settlements: dict[str, Any], starts: dict[str, datetime], obs_loader: Any, now: datetime) -> dict[str, Any]:
    from nhl_edge.workflows.evaluate import close_price_cents
    from nhl_edge.workflows.settle import ingested_player_games, latest_schedule, load_final_results

    decisions = list(ledger.iter_rows("thesis_decisions"))
    if not decisions:
        return {"n_rows": 0, "note": "no thesis decisions yet", "slates": {}}
    games_rows = list(ledger.iter_rows("thesis_games"))
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
            continue  # official events not ingested yet: retried on the next evaluate run
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
    ctx = {"schedule": latest_schedule(ledger), "finals": set(finals), "events": ingested_player_games(ledger) | set(goalies),
           "settled": {str(r.game_id) for r in settlements.values() if getattr(r, "game_id", None)}, "settlements": settlements, "actual": actual}
    rep = build_report(rows, games_rows, decisions, starts, ctx, now)
    out = ledger.root / "eval"
    out.mkdir(parents=True, exist_ok=True)
    (out / "report_thesis.json").write_text(json.dumps(rep, indent=1, default=str))
    (out / "report_thesis.md").write_text(report_markdown(rep))
    log.info(kv(event="thesis_postmortem", rows=len(rows), new=len(new_rows), slates={d: v["label"] for d, v in rep["slates"].items()}))
    return rep


# ------------------------------------------------------------------------------------------------------------- report
def _slate_date(gid: str, sched: dict[str, dict[str, Any]], info: dict[str, Any]) -> str | None:
    g = sched.get(gid) or {}
    if g.get("game_date_et"):
        return str(g["game_date_et"])
    st = info.get("start_utc") or (g.get("start_time_utc"))
    if not st:
        return None
    from datetime import timedelta

    return (parse_iso(st) - timedelta(hours=4)).date().isoformat()  # ET (EDT) evening games; regular season dates only


def _mean(xs: list[float]) -> float | None:
    return round(sum(xs) / len(xs), 4) if xs else None


def _bet_view(d: dict[str, Any], pm: dict[str, Any] | None, settle_rec: Any) -> dict[str, Any]:
    fid = d.get("expression_fidelity") or from_logged(d.get("primary_thesis"), d.get("family", ""))
    out = {"decision_id": d["decision_id"], "game_id": str(d.get("game_id")), "bet_id": d["bet_id"], "family": d.get("family"), "chosen": bool(d.get("chosen")), "stake_dollars": d.get("stake_dollars") or 0.0,
           "research_status": d.get("research_status") or "LEGACY_NO_RESEARCH_LAYER", "research_stake_dollars": d.get("research_stake_dollars"),
           "research_reasons": d.get("research_reasons") or [], "fidelity_class": fid.get("fidelity_class"), "thesis_capture": fid.get("thesis_capture"),
           "expression_kind": expression_kind(d.get("family", "")), "is_player_prop": is_player_prop(d.get("family", "")),
           "primary_thesis": (d.get("primary_thesis") or {}).get("key"), "p_thesis": (d.get("primary_thesis") or {}).get("p_thesis"),
           "entry_price_cents": d.get("executable_price_cents"), "ev_raw": d.get("ev_raw"), "ev_adjusted": d.get("ev_adjusted"), "p_model": d.get("p_model"),
           "p_adjusted": d.get("p_adjusted"), "p_kalshi_mid": d.get("p_kalshi_mid"), "market_disagreement": d.get("market_disagreement"),
           "selection_override": d.get("selection_override"), "joint_relationships": d.get("joint_relationships") or {}, "scored": pm is not None, "outcome": None}
    if pm is not None:
        out.update({k: pm.get(k) for k in ("won", "thesis_result", "expression_result", "price_result_clv", "close_prob_yes", "model_result", "realized_script",
                                           "model_p_bet_given_thesis_outcome", "model_p_win_in_realized_script")})
        out["realized_profit_nominal"] = pm.get("realized_profit") or 0.0
        out["realized_profit_research"] = research_profit(d, bool(pm.get("won"))) if d.get("research_stake_dollars") is not None else None
        out["outcome"] = "YES_NO"
    elif settle_rec is not None and settle_rec.outcome in TERMINAL_OUTCOMES:
        out["outcome"] = settle_rec.outcome.value  # void / push / unsettleable: stake returned, no P/L, not a forecast to score
        out["realized_profit_nominal"] = 0.0
        out["realized_profit_research"] = 0.0 if d.get("research_stake_dollars") is not None else None
    return out


def _sections(bets: list[dict[str, Any]], games: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """THESIS / EXPRESSION / PRICE / MODEL / PORTFOLIO / GOVERNANCE for the final card's chosen bets (scored only)."""
    sc = [b for b in bets if b["outcome"] == "YES_NO"]
    funded = [b for b in bets if b["research_status"] == "FUNDED_RESEARCH"]
    # THESIS: one observation per (game, thesis), not per bet
    th = {}
    for b in sc:
        if b["primary_thesis"] and b["primary_thesis"] != "DIFFUSE" and b["thesis_result"] is not None:
            th[(b["game_id"], b["primary_thesis"])] = (b["p_thesis"], bool(b["thesis_result"]))
    tp = [(p, y) for p, y in th.values() if p is not None]
    thesis = {"n_bets_with_thesis": sum(1 for b in sc if b["thesis_result"] is not None), "n_distinct_theses": len(th),
              "thesis_hit_rate": _mean([1.0 if y else 0.0 for _, y in th.values()]), "mean_p_thesis": _mean([p for p, _ in tp]),
              "thesis_brier": _mean([(p - (1.0 if y else 0.0)) ** 2 for p, y in tp]),
              "calibration_note": "few theses: hit rate vs mean predicted probability is descriptive only" if len(tp) < 30 else None,
              "realized_vs_projected_script": {g: v.get("script_check") for g, v in games.items() if v.get("script_check")}}
    ex2 = Counter(b["expression_result"] for b in sc)
    by_cls: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_kind: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for b in sc:
        by_cls[b["fidelity_class"] or "NONE"].append(b)
        by_kind[b["expression_kind"]].append(b)
    perf = lambda rs: {"n": len(rs), "won": sum(1 for r in rs if r["won"]), "hit_rate": _mean([1.0 if r["won"] else 0.0 for r in rs]),  # noqa: E731
                       "mean_p_adjusted": _mean([float(r["p_adjusted"]) for r in rs if r["p_adjusted"] is not None]),
                       "thesis_right_expression_lost": sum(1 for r in rs if r["expression_result"] == "THESIS_RIGHT_EXPRESSION_LOST"),
                       "pl_nominal": round(sum(r["realized_profit_nominal"] for r in rs), 2)}
    expression = {"thesis_right_expression_won": ex2.get("THESIS_RIGHT_EXPRESSION_WON", 0), "thesis_right_expression_lost": ex2.get("THESIS_RIGHT_EXPRESSION_LOST", 0),
                  "thesis_wrong_expression_won": ex2.get("THESIS_WRONG_EXPRESSION_WON", 0), "thesis_wrong_expression_lost": ex2.get("THESIS_WRONG_EXPRESSION_LOST", 0),
                  "no_thesis": {k: v for k, v in ex2.items() if k.startswith("NO_THESIS")},
                  "by_fidelity_class": {k: perf(v) for k, v in sorted(by_cls.items())}, "broad_vs_player": {k: perf(v) for k, v in sorted(by_kind.items())}}
    clv = [b["price_result_clv"] for b in sc if b.get("price_result_clv") is not None]
    price = {"n": len(sc), "mean_clv": _mean(clv), "n_clv": len(clv), "mean_ev_raw_at_entry": _mean([float(b["ev_raw"]) for b in sc if b["ev_raw"] is not None]),
             "mean_ev_adjusted_at_entry": _mean([float(b["ev_adjusted"]) for b in sc if b["ev_adjusted"] is not None]),
             "bets": [{"bet_id": b["bet_id"], "entry_cents": b["entry_price_cents"], "close_prob_yes": b.get("close_prob_yes"), "clv": b.get("price_result_clv"),
                       "ev_adjusted_at_entry": b["ev_adjusted"]} for b in sc]}
    mr = [b["model_result"] for b in sc if b.get("model_result")]
    fam: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for b in sc:
        fam[b["family"]].append(b["model_result"])

    def mstats(ms: list[dict[str, Any]]) -> dict[str, Any]:
        bm = [m["brier_kalshi_mid"] for m in ms if m.get("brier_kalshi_mid") is not None]
        return {"n": len(ms), "brier_model": _mean([m["brier_model"] for m in ms]), "brier_adjusted": _mean([m["brier_adjusted"] for m in ms]),
                "brier_kalshi_mid": _mean(bm), "logloss_model": _mean([m["logloss_model"] for m in ms]), "logloss_adjusted": _mean([m["logloss_adjusted"] for m in ms])}

    model = mstats(mr) | {"by_family": {k: mstats(v) for k, v in sorted(fam.items())}}
    stake_n = sum(float(b["stake_dollars"] or 0) for b in sc)
    pl_n = sum(b["realized_profit_nominal"] for b in sc)
    fsc = [b for b in funded if b["outcome"] is not None]
    stake_r = sum(float(b["research_stake_dollars"] or 0) for b in fsc)
    pl_r = sum(b["realized_profit_research"] or 0.0 for b in fsc)
    phis = [abs(float(v.get("phi"))) for b in sc for o, v in b["joint_relationships"].items() if v.get("phi") is not None and any(o == x["bet_id"] for x in sc)]
    th_share = [g["portfolio_result"].get("largest_thesis_share") for g in games.values() if (g.get("portfolio_result") or {}).get("largest_thesis_share") is not None]
    portfolio = {"nominal_card": {"n_bets": len(sc), "stake": round(stake_n, 2), "pl": round(pl_n, 2), "roi": round(pl_n / stake_n, 4) if stake_n else None,
                                  "basis": "optimiser stakes on the nominal bankroll (B)"},
                 "funded_research": {"n_funded": len(funded), "n_scored": len(fsc), "stake": round(stake_r, 2), "pl": round(pl_r, 2), "roi": round(pl_r / stake_r, 4) if stake_r else None,
                                     "basis": "whole-dollar FUNDED_RESEARCH stakes (research bankroll)"} if any(b["research_stake_dollars"] is not None for b in bets) else
                 {"note": "no evaluated final-card bets yet" if not bets else "no research layer on these decisions (logged before nhl-card-1.1)"},
                 "n_funded": len(funded), "n_shadow_on_card": sum(1 for b in bets if b["research_status"] in ("SHADOW_ONLY", "REJECTED")),
                 "correlation_concentration": {"n_pairs": len(phis) // 2, "mean_abs_phi": _mean(phis), "max_abs_phi": round(max(phis), 3) if phis else None},
                 "thesis_concentration": {"mean_largest_thesis_share": _mean(th_share)},
                 "realized_vs_simulated": {g: (v.get("portfolio_result") or {}).get("realized_vs_simulated") for g, v in games.items()}}
    gov_reasons = Counter(r.split(" (")[0] for b in bets for r in b["research_reasons"])
    governance = {"funded_player_props": [b["bet_id"] for b in funded if b["is_player_prop"]],
                  "shadow_player_props": [b["bet_id"] for b in bets if b["is_player_prop"] and b["research_status"] in ("SHADOW_ONLY", "REJECTED")],
                  "large_disagreement_gates_triggered": gov_reasons.get("LARGE_MARKET_DISAGREEMENT_UNCORROBORATED", 0),
                  "reason_counts": dict(gov_reasons), "overrides": [o for g in games.values() for o in g.get("overrides") or []]}
    return {"THESIS": thesis, "EXPRESSION": expression, "PRICE": price, "MODEL": model, "PORTFOLIO": portfolio, "GOVERNANCE": governance}


def _script_check(game_row: dict[str, Any], realized_key: str | None) -> dict[str, Any] | None:
    scripts = (game_row or {}).get("scripts") or []
    if not scripts or not realized_key:
        return None
    ranked = sorted(scripts, key=lambda s: -float(s.get("frequency") or 0))
    hit = next((i for i, s in enumerate(ranked) if s.get("key") == realized_key), None)
    return {"realized_script": realized_key, "p_projected": next((s.get("frequency") for s in ranked if s.get("key") == realized_key), 0.0),
            "rank": None if hit is None else hit + 1, "n_scripts": len(ranked), "top_projected": ranked[0].get("key")}


def build_report(rows: list[dict[str, Any]], games_rows: list[dict[str, Any]], decisions: list[dict[str, Any]], starts: dict[str, datetime],
                 ctx: dict[str, Any], now: datetime) -> dict[str, Any]:
    pm_by = {}
    for r in rows:
        pm_by[r["decision_id"]] = r  # deduped on (decision_id, settlement_key) upstream; the latest settlement wins
    finals_info = final_snapshots(games_rows, decisions, starts)
    sched = ctx.get("schedule") or {}
    settlements = ctx.get("settlements") or {}
    slates: dict[str, dict[str, Any]] = {}
    by_date: dict[str, list[str]] = defaultdict(list)
    for gid, info in finals_info.items():
        d = _slate_date(gid, sched, info)
        if d:
            by_date[d].append(gid)
    for date in sorted(by_date):
        scheduled = sorted({g for g, r in sched.items() if str(r.get("game_date_et")) == date and r.get("status") not in ("postponed", "canceled")} | set(by_date[date]))
        games: dict[str, dict[str, Any]] = {}
        final_bets: list[dict[str, Any]] = []
        missing: dict[str, str] = {}
        ambiguous = []
        n_eval = 0
        for gid in scheduled:
            info = finals_info.get(gid) or {"status": "NO_PREGAME_SNAPSHOT", "reason": "no thesis-card generation for this game"}
            final, settled, events = gid in ctx["finals"], gid in ctx["settled"], gid in ctx["events"]
            if info["status"] in ("NO_PREGAME_SNAPSHOT", "NO_COMPLETE_PREGAME_SNAPSHOT", "NO_START_TIME"):
                state = "NO_FINAL_CARD" if final else "NOT_FINAL"
                if final:
                    n_eval += 1  # nothing to score: terminal once the game is final
                missing[gid] = f"{info['status']}: {info['reason']}" + ("" if final else " (game not final)")
                games[gid] = {"state": state, "final_snapshot": {k: v for k, v in info.items() if k not in ("chosen", "game_row")}}
                continue
            bets = [_bet_view(d, pm_by.get(d["decision_id"]), settlements.get(d["ticker"])) for d in info["chosen"]]
            unresolved = [b["bet_id"] for b in bets if b["outcome"] is None]
            if info["status"] == AMBIGUOUS:
                state = AMBIGUOUS
                ambiguous.append(gid)
                missing[gid] = f"{AMBIGUOUS}: {info['reason']}"
            elif info.get("start_utc") and parse_iso(info["start_utc"]) > now:
                state, missing[gid] = "NOT_STARTED", "game not started: the snapshot shown is the latest so far, not yet final"
            elif not final:
                state, missing[gid] = "NOT_FINAL", "no official FINAL result yet"
            elif not settled:
                state, missing[gid] = "NOT_SETTLED", "final, but its contracts are not settled yet"
            elif not events:
                state, missing[gid] = "EVENTS_NOT_INGESTED", "official player events not ingested yet"
            elif unresolved:
                state, missing[gid] = "DECISIONS_NOT_SCORED", f"final-card decisions not scored yet: {unresolved}"
            else:
                state = "EVALUATED"
                n_eval += 1
            gr = info["game_row"]
            scored = [b for b in bets if b["outcome"] == "YES_NO"]
            pr_rows = [{"chosen": True, "stake_dollars": b["stake_dollars"], "realized_profit": b["realized_profit_nominal"], "primary_thesis": b["primary_thesis"],
                        "won": b["won"], "thesis_result": b["thesis_result"]} for b in scored]
            realized = ((ctx.get("actual") or {}).get(gid) or {}).get("script_key")
            games[gid] = {"state": state, "matchup": gr.get("matchup"),
                          "final_snapshot": {k: v for k, v in info.items() if k not in ("chosen", "game_row")},
                          "portfolio_result": portfolio_result(pr_rows, gr) if state == "EVALUATED" else None,
                          "script_check": _script_check(gr, realized) if state == "EVALUATED" else None,
                          "overrides": [o for o in gr.get("selection_overrides") or [] if o.get("applied")], "bets": bets}
            if state == "EVALUATED":
                final_bets += bets
        n_sched = len(scheduled)
        ev_games = {g: v for g, v in games.items() if v["state"] == "EVALUATED"}
        caps = sum(int(v["final_snapshot"].get("game_card_cap") or DEFAULT_GAME_CAP) for v in ev_games.values())
        n_card = len(final_bets)
        snap_games = [g for g in scheduled if games[g]["state"] not in ("NO_FINAL_CARD",) and (finals_info.get(g) or {}).get("status") in ("OK", AMBIGUOUS)]
        final_card_complete = bool(snap_games) and all(games[g]["state"] == "EVALUATED" for g in snap_games)
        postmortem_complete = n_eval == n_sched and not ambiguous
        comp = {"games_scheduled": n_sched, "games_final": sum(1 for g in scheduled if g in ctx["finals"]),
                "games_settled": sum(1 for g in scheduled if g in ctx["settled"] and g in ctx["finals"]),
                "games_player_events_ingested": sum(1 for g in scheduled if g in ctx["events"]),
                "games_with_final_card_snapshot": len(snap_games), "games_thesis_evaluated": len(ev_games), "games_terminal": n_eval,
                "games_missing": missing, "games_ambiguous": ambiguous, "final_card_complete": final_card_complete, "postmortem_complete": postmortem_complete}
        label = ("COMPLETE" if postmortem_complete else "PARTIAL") + f" — {n_eval}/{n_sched} games evaluated" + (f" · {len(ambiguous)} {AMBIGUOUS}" if ambiguous else "")
        slates[date] = {"label": label, "completeness": comp,
                        "invariants": {"final_card_n": n_card, "sum_game_card_caps": caps, "holds": n_card <= caps},
                        "FINAL_CARD_UNIQUE": _sections(final_bets, ev_games) | {
                            "interpretation": ("final: every scheduled game evaluated" if postmortem_complete else
                                               f"INTERIM ({label}): covers evaluated games only; NOT the slate's final ROI")},
                        "games": games}
    # ALL_PROSPECTIVE_DECISIONS: calibration research over every scored generation (no P/L)
    dec_by_id = {d["decision_id"]: d for d in decisions}
    allr = [r for r in rows if r["decision_id"] in dec_by_id]
    uniq: dict[str, dict[str, Any]] = {}
    for r in sorted(allr, key=lambda r: str(r.get("decided_at_utc"))):
        uniq[f"{r['game_id']}|{r['bet_id']}"] = r  # last pregame observation of each logical wager
    fams = sorted({str(r.get("family")) for r in allr})

    def brier(rs: list[dict[str, Any]], key: str) -> float | None:
        v = [r["model_result"][key] for r in rs if r.get("model_result") and r["model_result"].get(key) is not None]
        return _mean(v)

    allp = {"basis": "every scored pregame decision of every generation (repeated observations of one wager are NOT independent; no P/L here)",
            "n_rows": len(allr), "n_unique_logical_wagers": len(uniq), "repeat_factor": round(len(allr) / len(uniq), 2) if uniq else None,
            "by_family": {f: {"n_rows": sum(1 for r in allr if str(r.get("family")) == f),
                              "n_unique_wagers": sum(1 for r in uniq.values() if str(r.get("family")) == f),
                              "brier_model_all_rows": brier([r for r in allr if str(r.get("family")) == f], "brier_model"),
                              "brier_model_last_observation": brier([r for r in uniq.values() if str(r.get("family")) == f], "brier_model"),
                              "brier_adjusted_last_observation": brier([r for r in uniq.values() if str(r.get("family")) == f], "brier_adjusted"),
                              "brier_kalshi_mid_last_observation": brier([r for r in uniq.values() if str(r.get("family")) == f], "brier_kalshi_mid")} for f in fams}}
    return {"evaluated_at_utc": iso(now), "authority": "RESEARCH_ONLY", "report_version": "thesis-postmortem-2.0", "n_rows_all_runs": len(rows),
            "slates": slates, "ALL_PROSPECTIVE_DECISIONS": allp,
            "invariants_hold": all(v["invariants"]["holds"] for v in slates.values()),
            "note": ("Prospective thesis-card evidence. All P/L is FINAL_CARD_UNIQUE (one latest complete pregame snapshot per game). THESIS / EXPRESSION / PRICE / "
                     "MODEL / PORTFOLIO / GOVERNANCE are kept separate: a right thesis expressed through a contract that lost is not a wrong prediction. "
                     "A handful of games proves nothing; never tune to one slate.")}


def _fmt(x: Any, n: int = 3) -> str:
    if x is None:
        return "-"
    if isinstance(x, float):
        return f"{x:.{n}f}" if not math.isnan(x) else "-"
    return str(x)


def report_markdown(rep: dict[str, Any]) -> str:
    L = [f"# Thesis-card postmortem — {rep['authority']}", "", f"evaluated {rep['evaluated_at_utc']} · {rep.get('report_version')} · rows (all generations) {rep['n_rows_all_runs']}", "",
         "All P/L below is **FINAL_CARD_UNIQUE**: per game, only the decisions of the ONE latest complete pregame thesis-card snapshot. Repeated generations are "
         "in ALL_PROSPECTIVE_DECISIONS (calibration research, no P/L).", ""]
    for date, s in sorted(rep["slates"].items(), reverse=True):
        c = s["completeness"]
        fc = s["FINAL_CARD_UNIQUE"]
        L += [f"## Slate {date}: **{s['label']}**", "",
              f"scheduled {c['games_scheduled']} · final {c['games_final']} · settled {c['games_settled']} · events ingested {c['games_player_events_ingested']} · "
              f"thesis-evaluated {c['games_thesis_evaluated']} · final_card_complete {c['final_card_complete']} · postmortem_complete {c['postmortem_complete']}", ""]
        if c["games_missing"]:
            L += ["missing / pending:"] + [f"- {g}: {why}" for g, why in c["games_missing"].items()] + [""]
        if not c["postmortem_complete"]:
            L += [f"> {fc['interpretation']}", ""]
        inv = s["invariants"]
        L += [f"invariant final_card_n {inv['final_card_n']} <= sum(game card caps) {inv['sum_game_card_caps']}: {'OK' if inv['holds'] else 'VIOLATED'}", ""]
        p = fc["PORTFOLIO"]
        nc, fr = p["nominal_card"], p["funded_research"]
        L += ["### FINAL_CARD_UNIQUE", "", "| view | bets | stake | P/L | ROI |", "|---|---:|---:|---:|---:|",
              f"| nominal optimiser card (B) | {nc['n_bets']} | {nc['stake']:.2f} | {nc['pl']:+.2f} | {_fmt(nc['roi'])} |"]
        if "stake" in fr:
            L.append(f"| FUNDED research stakes | {fr['n_scored']} | {fr['stake']:.2f} | {fr['pl']:+.2f} | {_fmt(fr['roi'])} |")
        else:
            L.append(f"| FUNDED research stakes | - | - | - | {fr['note']} |")
        t, e, pr, m, gv = fc["THESIS"], fc["EXPRESSION"], fc["PRICE"], fc["MODEL"], fc["GOVERNANCE"]
        L += ["", f"- THESIS: {t['n_distinct_theses']} distinct theses, hit rate {_fmt(t['thesis_hit_rate'])} vs mean p {_fmt(t['mean_p_thesis'])} (Brier {_fmt(t['thesis_brier'])})",
              f"- EXPRESSION: thesis right + won {e['thesis_right_expression_won']} · right + lost {e['thesis_right_expression_lost']} · wrong + won "
              f"{e['thesis_wrong_expression_won']} · wrong + lost {e['thesis_wrong_expression_lost']}",
              "  - by fidelity: " + "; ".join(f"{k} {v['won']}/{v['n']}" for k, v in e["by_fidelity_class"].items()),
              "  - broad vs player: " + "; ".join(f"{k} {v['won']}/{v['n']} (P/L {v['pl_nominal']:+.2f})" for k, v in e["broad_vs_player"].items()),
              f"- PRICE: mean CLV {_fmt(pr['mean_clv'], 4)} (n {pr['n_clv']}), mean adjusted EV at entry {_fmt(pr['mean_ev_adjusted_at_entry'], 4)}",
              f"- MODEL: Brier raw {_fmt(m['brier_model'], 4)} · adjusted {_fmt(m['brier_adjusted'], 4)} · Kalshi mid {_fmt(m['brier_kalshi_mid'], 4)} (n {m['n']})",
              f"- PORTFOLIO: funded {p['n_funded']} · shadow on card {p['n_shadow_on_card']} · mean |phi| among card pairs {_fmt(p['correlation_concentration']['mean_abs_phi'])}"
              f" · mean largest thesis share {_fmt(p['thesis_concentration']['mean_largest_thesis_share'])}",
              f"- GOVERNANCE: funded player props {len(gv['funded_player_props'])} · shadow player props {len(gv['shadow_player_props'])} · large-disagreement gates "
              f"{gv['large_disagreement_gates_triggered']} · overrides {len(gv['overrides'])}", ""]
        for o in gv["overrides"]:
            L.append(f"  - override: {o.get('text')}")
        for g, v in s["games"].items():
            fs = v.get("final_snapshot") or {}
            L += ["", f"#### game {g} {v.get('matchup') or ''}: {v['state']}" + (f" · snapshot {fs.get('snapshot_id')} @ {fs.get('decided_at_utc')}" if fs.get("snapshot_id") else "")]
            if v.get("bets"):
                L += ["", "| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |", "|---|---|---:|---:|---|---|---|---|---:|---:|"]
                for b in v["bets"]:
                    L.append(f"| {b['bet_id']} | {b['research_status']} | {_fmt(b['research_stake_dollars'])} | {_fmt(float(b['stake_dollars']), 2)} | {_fmt(b.get('won'))} | "
                             f"{_fmt(b.get('thesis_result'))} | {_fmt(b.get('expression_result'))} | {b['fidelity_class']} | {_fmt(b.get('price_result_clv'), 4)} | "
                             f"{_fmt(b.get('realized_profit_nominal'), 2)} |")
        L.append("")
    ap = rep["ALL_PROSPECTIVE_DECISIONS"]
    L += ["## ALL_PROSPECTIVE_DECISIONS (calibration research; no P/L)", "", f"{ap['n_rows']} scored rows = {ap['n_unique_logical_wagers']} unique logical wagers "
          f"(repeat factor {ap['repeat_factor']}). {ap['basis']}.", "", "| family | rows | unique | Brier all rows | Brier last obs | adjusted | Kalshi mid |", "|---|---:|---:|---:|---:|---:|---:|"]
    for f, v in ap["by_family"].items():
        L.append(f"| {f} | {v['n_rows']} | {v['n_unique_wagers']} | {_fmt(v['brier_model_all_rows'], 4)} | {_fmt(v['brier_model_last_observation'], 4)} | "
                 f"{_fmt(v['brier_adjusted_last_observation'], 4)} | {_fmt(v['brier_kalshi_mid_last_observation'], 4)} |")
    L += ["", f"_{rep['note']}_", ""]
    return "\n".join(L)
