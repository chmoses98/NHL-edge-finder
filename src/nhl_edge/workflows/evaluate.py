"""Evaluation job: join predictions x settlements x schedule x market observations, then score.

* reads  ``predictions``, ``settlements``, ``context/schedule``, ``kalshi/markets`` (+deltas), ``evaluations`` (dedupe)
* writes ``evaluations`` (append-only; deduped on (prediction_id, settlement_key)), ``eval/report.json``,
         ``eval/report.md`` (derived; overwritten) and ``STATUS_evaluate.json``

Leak rules: ``pregame`` is recomputed from the scheduled start; the prediction instant AND the market observation it
used must both be strictly before the start. Only pregame rows enter any metric. The closing snapshot is the last
market observation strictly before the start.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from nhl_edge.archive.ledger import Ledger
from nhl_edge.archive.reconstruct import iter_market_rows
from nhl_edge.evaluation.authority import eligibility
from nhl_edge.evaluation.clv import closing_snapshot, clv_prob
from nhl_edge.evaluation.metrics import brier, calibration_table, ece, log_loss
from nhl_edge.kalshi.normalize import quote_cents
from nhl_edge.log import get_logger, kv
from nhl_edge.settlement.engine import SettlementOutcome, SettlementRecord
from nhl_edge.timeutil import iso, parse_iso, utcnow
from nhl_edge.workflows.settle import KALSHI_ENGINE_VERSION, coerce, latest_schedule

log = get_logger(__name__)

VIEWS = {"DATA_ONLY_V1": "p_data_only", "MARKET_BASELINE": "p_market", "MARKET_ANCHORED_V1": "p_market_anchored"}
HOUR_BUCKETS = (("<1h", 0.0, 1.0), ("1-6h", 1.0, 6.0), ("6-24h", 6.0, 24.0), (">24h", 24.0, float("inf")))


def _dt(v: Any) -> datetime | None:
    if v is None:
        return None
    try:
        return parse_iso(v) if isinstance(v, str) else v
    except ValueError:
        return None


def best_settlements(ledger: Ledger) -> dict[str, SettlementRecord]:
    """Per ticker: prefer our engine over market-only; then highest stat correction; then latest."""
    best: dict[str, SettlementRecord] = {}
    for row in ledger.iter_rows("settlements"):
        try:
            rec = coerce(SettlementRecord, row)
        except Exception:  # noqa: BLE001
            continue
        cur = best.get(rec.ticker)
        rank = (0 if rec.engine_version == KALSHI_ENGINE_VERSION else 1, rec.stat_correction_version, rec.settled_at_utc)
        if cur is None or rank > (0 if cur.engine_version == KALSHI_ENGINE_VERSION else 1, cur.stat_correction_version, cur.settled_at_utc):
            best[rec.ticker] = rec
    return best


def observations_by_ticker(ledger: Ledger, tickers: set[str]) -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = {t: [] for t in tickers}
    for row in iter_market_rows(ledger):
        tk = row.get("ticker")
        if tk in out:
            q = quote_cents(row)
            out[tk].append({"_observed_at_utc": row.get("_observed_at_utc"), **q})
    return out


def close_price_cents(obs: dict[str, Any] | None) -> float | None:
    if not obs:
        return None
    yb, ya = obs.get("yes_bid"), obs.get("yes_ask")
    if yb is not None and ya is not None:
        return (yb + ya) / 2.0
    lp = obs.get("last_price")
    return float(lp) if lp else None


def build_evaluation_row(pred: dict[str, Any], rec: SettlementRecord, start: datetime, observations: list[dict[str, Any]]) -> dict[str, Any] | None:
    if rec.outcome not in (SettlementOutcome.YES, SettlementOutcome.NO):
        return None
    predicted_at = _dt(pred.get("predicted_at_utc"))
    if predicted_at is None:
        return None
    mkt_at = _dt(pred.get("market_observed_at_utc"))
    pregame = predicted_at < start and (mkt_at is None or mkt_at < start)
    closing = closing_snapshot(observations, start)
    close_c = close_price_cents(closing)
    yes_ask, no_ask = pred.get("market_yes_ask"), pred.get("market_no_ask")
    clv_yes = clv_no = None
    if close_c is not None:
        if yes_ask is not None and 0 <= yes_ask <= 100:
            clv_yes = clv_prob(float(yes_ask), close_c, "yes")
        if no_ask is not None and 0 <= no_ask <= 100:
            clv_no = clv_prob(100.0 - float(no_ask), close_c, "no")
    p_data, p_mkt = pred.get("p_data_only"), pred.get("p_market")
    clv_signed = None
    if p_data is not None and (clv_yes is not None or clv_no is not None):
        ref = 0.5 if p_mkt is None else float(p_mkt)
        clv_signed = clv_yes if float(p_data) > ref else clv_no
    return {
        "prediction_id": pred.get("prediction_id"), "settlement_key": rec.idempotency_key, "ticker": rec.ticker, "game_id": pred.get("game_id") or rec.game_id,
        "family": pred.get("family"), "model_version": pred.get("model_version"), "predicted_at_utc": iso(predicted_at), "start_utc": iso(start), "pregame": bool(pregame),
        "y": 1 if rec.outcome == SettlementOutcome.YES else 0, "p_data_only": p_data, "p_market": p_mkt, "p_market_anchored": pred.get("p_market_anchored"),
        "entry_yes_ask": yes_ask, "entry_no_ask": no_ask, "close_prob": None if close_c is None else close_c / 100.0,
        "close_observed_at_utc": None if closing is None else closing.get("_observed_at_utc"), "clv_yes_prob": clv_yes, "clv_no_prob": clv_no, "clv_signed": clv_signed,
        "hours_before_start": (start - predicted_at).total_seconds() / 3600.0, "horizon_label": pred.get("horizon_label"), "settlement_engine": rec.engine_version,
        "home_goalie_status": pred.get("home_goalie_status"), "away_goalie_status": pred.get("away_goalie_status"),
    }


def view_metrics(rows: list[dict[str, Any]], key: str) -> dict[str, Any]:
    xs = [(float(r[key]), int(r["y"])) for r in rows if r.get(key) is not None]
    if not xs:
        return {"n": 0}
    p = [x[0] for x in xs]
    y = [x[1] for x in xs]
    out = {"n": len(xs), "brier": brier(p, y), "log_loss": log_loss(p, y), "mean_p": sum(p) / len(p), "hit_rate": sum(y) / len(y)}
    if len(xs) >= 20:
        out["ece"] = ece(p, y)
        out["calibration"] = calibration_table(p, y, bins=10 if len(xs) >= 100 else 5)
    return out


def build_report(rows: list[dict[str, Any]], now: datetime, n_new: int) -> dict[str, Any]:
    pregame = [r for r in rows if r.get("pregame")]
    fams = sorted({str(r.get("family")) for r in rows})
    by_fam = {}
    for fam in fams:
        fr = [r for r in pregame if str(r.get("family")) == fam]
        by_fam[fam] = {"n": sum(str(r.get("family")) == fam for r in rows), "n_pregame": len(fr), "views": {v: view_metrics(fr, k) for v, k in VIEWS.items()},
                       "by_horizon": {lab: view_metrics([r for r in fr if lo <= r["hours_before_start"] < hi], "p_data_only") for lab, lo, hi in HOUR_BUCKETS},
                       "authority": eligibility(fr)}
    return {"evaluated_at_utc": iso(now), "authority": "RESEARCH_ONLY", "n_rows": len(rows), "n_pregame": len(pregame), "n_new_rows": n_new,
            "overall": {v: view_metrics(pregame, k) for v, k in VIEWS.items()}, "families": by_fam,
            "note": "The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing."}


def _fmt(x: Any) -> str:
    return "" if x is None else (f"{x:.4f}" if isinstance(x, float) else str(x))


def report_markdown(rep: dict[str, Any]) -> str:
    lines = [f"# NHL evaluation report — {rep['authority']}", "", f"evaluated {rep['evaluated_at_utc']} · rows {rep['n_rows']} · pregame {rep['n_pregame']} · new {rep['n_new_rows']}", "",
             "| scope | view | n | Brier | log loss | ECE | mean p | hit rate |", "|---|---|---:|---:|---:|---:|---:|---:|"]
    for v, m in rep["overall"].items():
        lines.append(f"| ALL | {v} | {m.get('n', 0)} | {_fmt(m.get('brier'))} | {_fmt(m.get('log_loss'))} | {_fmt(m.get('ece'))} | {_fmt(m.get('mean_p'))} | {_fmt(m.get('hit_rate'))} |")
    for fam, fr in rep["families"].items():
        for v, m in fr["views"].items():
            lines.append(f"| {fam} | {v} | {m.get('n', 0)} | {_fmt(m.get('brier'))} | {_fmt(m.get('log_loss'))} | {_fmt(m.get('ece'))} | {_fmt(m.get('mean_p'))} | {_fmt(m.get('hit_rate'))} |")
    lines += ["", rep["note"], ""]
    return "\n".join(lines)


def run_evaluate(out_root: Path, data_root: Path, now: datetime | None = None) -> int:
    now = now or utcnow()
    ledger = Ledger(out_root)
    settlements = best_settlements(ledger)
    schedule = latest_schedule(ledger)
    starts = {gid: parse_iso(g["start_time_utc"]) for gid, g in schedule.items() if g.get("start_time_utc")}
    preds = list(ledger.iter_rows("predictions"))
    seen = {(r.get("prediction_id"), r.get("settlement_key")) for r in ledger.iter_rows("evaluations")}
    existing_rows = list(ledger.iter_rows("evaluations"))
    tickers = {p["ticker"] for p in preds if p.get("ticker") in settlements}
    obs = observations_by_ticker(ledger, tickers) if tickers else {}
    new_rows: list[dict[str, Any]] = []
    for p in preds:
        rec = settlements.get(p.get("ticker"))
        if rec is None:
            continue
        start = starts.get(str(p.get("game_id")))
        if start is None:
            continue
        if (p.get("prediction_id"), rec.idempotency_key) in seen:
            continue
        row = build_evaluation_row(p, rec, start, obs.get(p["ticker"], []))
        if row:
            new_rows.append(row)
            seen.add((row["prediction_id"], row["settlement_key"]))
    if new_rows:
        ledger.append_rows("evaluations", new_rows, observed_at=now)
    all_rows = [r for r in existing_rows] + new_rows
    rep = build_report(all_rows, now, len(new_rows))
    eval_dir = out_root / "eval"
    eval_dir.mkdir(parents=True, exist_ok=True)
    (eval_dir / "report.json").write_text(json.dumps(rep, indent=1, default=str))
    (eval_dir / "report.md").write_text(report_markdown(rep))
    log.info(kv(event="evaluated", rows=len(all_rows), new=len(new_rows)))
    print(report_markdown(rep))
    status: dict[str, Any] = {"evaluated_at_utc": iso(now), "n_rows": len(all_rows), "n_new": len(new_rows), "run_id": ledger.run_id, "steps": {"v1": "OK"}}
    try:
        run_evaluate_player(ledger, settlements, starts, obs_loader=lambda t: observations_by_ticker(ledger, t), now=now)
        status["steps"]["player"] = "OK"
    except Exception as e:  # noqa: BLE001 - the PLAYER_SIM_V1 report never blocks V1's evaluation
        log.warning(kv(event="player_evaluation_failed", err=str(e)[:300]))
        status["steps"]["player"] = f"FAILED: {type(e).__name__}: {str(e)[:200]}"
    try:
        from nhl_edge.workflows.thesis_postmortem import run_thesis_postmortem

        trep = run_thesis_postmortem(ledger, settlements, starts, obs_loader=lambda t: observations_by_ticker(ledger, t), now=now)
        status["steps"]["thesis_postmortem"] = "OK"
        status["thesis_postmortem"] = {d: {"label": v.get("label"), **(v.get("completeness") or {})} for d, v in (trep.get("slates") or {}).items()}
    except Exception as e:  # noqa: BLE001 - the thesis postmortem never blocks V1's evaluation
        log.warning(kv(event="thesis_postmortem_failed", err=str(e)[:300]))
        status["steps"]["thesis_postmortem"] = f"FAILED: {type(e).__name__}: {str(e)[:200]}"
    write_evaluate_status(out_root, status)
    return 0


def write_evaluate_status(out_root: Path, status: dict[str, Any]) -> None:
    """The canonical breadcrumb is ``<archive>/STATUS_evaluate.json`` (the conductor reads it). It is written LAST, after
    every evaluation step, so its timestamp means "the whole evaluate job finished". ``eval/STATUS_evaluate.json`` is a
    legacy location (written there while the job's root was mistakenly ``ARCHIVE/eval``, until 2026-09-30) that kept
    showing 2026-09-30 and misled readers; it is now overwritten with the same content plus a pointer, so both agree."""
    text = json.dumps(status | {"canonical_path": "STATUS_evaluate.json"}, indent=1, default=str)
    (out_root / "STATUS_evaluate.json").write_text(text)
    legacy = out_root / "eval" / "STATUS_evaluate.json"
    legacy.parent.mkdir(parents=True, exist_ok=True)
    legacy.write_text(text)


PLAYER_VIEWS = {"PLAYER_SIM_V1": "p_player", "MARKET_BASELINE": "p_market", "MARKET_ANCHORED_PLAYER_V1": "p_market_anchored"}


def run_evaluate_player(ledger: Ledger, settlements: dict[str, SettlementRecord], starts: dict[str, datetime], obs_loader: Any, now: datetime) -> dict[str, Any]:
    """PLAYER_SIM_V1 shadow rows x official player settlements -> ``evaluations_player`` (append-only) and
    ``eval/report_player.{json,md}``. Same leak rules as V1: only rows predicted AND market-observed before the start."""
    preds = list(ledger.iter_rows("predictions_player"))
    seen = {(r.get("prediction_id"), r.get("settlement_key")) for r in ledger.iter_rows("evaluations_player")}
    existing = list(ledger.iter_rows("evaluations_player"))
    tickers = {p["ticker"] for p in preds if p.get("ticker") in settlements}
    obs = obs_loader(tickers) if tickers else {}
    new_rows: list[dict[str, Any]] = []
    for p in preds:
        rec = settlements.get(p.get("ticker"))
        start = starts.get(str(p.get("game_id")))
        if rec is None or start is None or (p.get("prediction_id"), rec.idempotency_key) in seen:
            continue
        row = build_evaluation_row(p | {"p_data_only": p.get("p_player")}, rec, start, obs.get(p["ticker"], []))
        if row:
            row.update({"p_player": p.get("p_player"), "projection_quality": p.get("meta_projection_quality"), "role_confidence": p.get("meta_role_confidence"),
                        "deployment_source": p.get("meta_deployment_source"), "player_id": p.get("player_id")})
            new_rows.append(row)
            seen.add((row["prediction_id"], row["settlement_key"]))
    if new_rows:
        ledger.append_rows("evaluations_player", new_rows, observed_at=now)
    rows = existing + new_rows
    pre = [r for r in rows if r.get("pregame")]
    fams = sorted({str(r.get("family")) for r in rows})
    rep = {"evaluated_at_utc": iso(now), "authority": "RESEARCH_ONLY", "model_version": "PLAYER_SIM_V1", "n_rows": len(rows), "n_pregame": len(pre), "n_new_rows": len(new_rows),
           "overall": {v: view_metrics(pre, k) for v, k in PLAYER_VIEWS.items()},
           "families": {f: {v: view_metrics([r for r in pre if str(r.get("family")) == f], k) for v, k in PLAYER_VIEWS.items()} for f in fams},
           "by_projection_quality": {q: view_metrics([r for r in pre if r.get("projection_quality") == q], "p_player")
                                     for q in sorted({str(r.get("projection_quality")) for r in pre})},
           "note": "Prospective SHADOW evidence only. The market is the benchmark; a handful of games proves nothing."}
    d = ledger.root / "eval"
    d.mkdir(parents=True, exist_ok=True)
    (d / "report_player.json").write_text(json.dumps(rep, indent=1, default=str))
    lines = [f"# PLAYER_SIM_V1 evaluation — {rep['authority']}", "", f"evaluated {rep['evaluated_at_utc']} · rows {rep['n_rows']} · pregame {rep['n_pregame']}", "",
             "| scope | view | n | Brier | log loss | ECE | mean p | hit rate |", "|---|---|---:|---:|---:|---:|---:|---:|"]
    for scope, views in [("ALL", rep["overall"])] + list(rep["families"].items()):
        for v, m in views.items():
            lines.append(f"| {scope} | {v} | {m.get('n', 0)} | {_fmt(m.get('brier'))} | {_fmt(m.get('log_loss'))} | {_fmt(m.get('ece'))} | {_fmt(m.get('mean_p'))} | {_fmt(m.get('hit_rate'))} |")
    lines += ["", rep["note"], ""]
    (d / "report_player.md").write_text("\n".join(lines))
    log.info(kv(event="player_evaluated", rows=len(rows), new=len(new_rows)))
    return rep
