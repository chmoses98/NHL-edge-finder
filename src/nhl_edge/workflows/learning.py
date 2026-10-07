"""NHL learning loop (``nhl-learning-1.0``, RESEARCH_ONLY): score every pregame snapshot once outcomes exist.

Runs inside ``nhl evaluate`` (after settlement), contained like every other evaluate step: a failure is recorded in
``STATUS_evaluate.json`` (``steps.learning``) and in the report's ``status`` and never blocks V1's evaluation.

Writes
* ``script_postmortems`` (append-only ledger kind): one row per settled (script forecast snapshot, game) -- the
  predicted NHL_SCRIPT_V1 distribution, the REALISED script (``scripts_v1.taxonomy.realized`` on the official final;
  postgame only, never written back into any forecast), multiclass Brier / log loss of the forecast and of the league
  base rate, top-script hit, hours before start. Deduped on (snapshot_id, game_id, realized_version).
* ``eval/report_learning.json`` (derived; overwritten): the scorecard SIFT shows, computed from immutable ledgers only.

Population rules (never mixed):
* MODEL vs MARKET probability quality uses DATA_ONLY_V1 ``evaluations`` rows, FINAL PREGAME snapshot per contract
  (the last prediction strictly before the scheduled start, market observed before the start too).
* RESEARCH CANDIDATES (shadow) use ``thesis_postmortems`` + ``script_forecasts``: every shortlisted bet side at the
  game's final pregame thesis snapshot, scored per $1 of contract cost at its executable ask whether or not anything was
  wagered. FUNDED research P/L (nominal research stakes) is reported separately. ACTUAL routed wagers are NOT here:
  they live in the accounting ledger (app ``performance.json``).
* Returns from small samples are reported with their n and never labelled profitable; maturity gates never use ROI.
"""

from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from datetime import datetime
from typing import Any

import numpy as np

from nhl_edge.log import get_logger, kv
from nhl_edge.timeutil import iso, parse_iso

log = get_logger(__name__)

LEARNING_VERSION = "nhl-learning-1.0"
EPS = 1e-6
#: snapshot windows (hours before the scheduled start): label -> (lo, hi); "final" is the last pregame snapshot
WINDOWS = (("~24h", 18.0, 30.0), ("~6h", 4.0, 8.0), ("~90m", 1.0, 2.0), ("~30m", 0.25, 0.75))
EDGE_BUCKETS = ((0.0, 0.02, "0-2c"), (0.02, 0.04, "2-4c"), (0.04, 0.07, "4-7c"), (0.07, 9.0, "7c+"))
SURVIVAL_BUCKETS = ((0.0, 0.45, "<45%"), (0.45, 0.65, "45-65%"), (0.65, 1.01, "65%+"))
MIN_SHOW = 30  # a grouped statistic with fewer observations is published with its n and flagged SMALL_SAMPLE

#: maturity gates (status only; they grant no authority). Thresholds fixed a priori; ROI is never a criterion.
GATES = (
    ("EARLY_LEARNING", "fewer than 100 settled games or 1,000 settled final-pregame contracts", {}),
    ("CALIBRATION_BUILDING", ">= 100 settled games and >= 1,000 settled final-pregame contracts", {"games": 100, "contracts": 1000}),
    ("EVIDENCE_EMERGING", ">= 300 settled games, >= 200 settled script forecasts, >= 500 candidate CLV observations, model Brier within 0.005 of the "
     "market on final pregame contracts in BOTH halves of the sample, and no family with |calibration bias| > 0.03 at n >= 200",
     {"games": 300, "scripts": 200, "clv": 500}),
    ("VALIDATED", ">= 800 settled games (about a full season), >= 600 settled script forecasts, model Brier <= market in both halves, research-"
     "candidate mean CLV > 0 with a 95% interval excluding 0 at n >= 1,000, and script forecasts beating the league base rate",
     {"games": 800, "scripts": 600, "clv": 1000}),
)


def _r(x: Any, n: int = 4) -> float | None:
    if x is None:
        return None
    try:
        f = float(x)
    except (TypeError, ValueError):
        return None
    return None if math.isnan(f) or math.isinf(f) else round(f, n)


# ------------------------------------------------------------------------------------------------ pure scoring
def multiclass_scores(probs: dict[str, float], realized: str, order: list[str]) -> dict[str, float]:
    p = np.array([float(probs.get(k) or 0.0) for k in order])
    y = np.array([1.0 if k == realized else 0.0 for k in order])
    brier = float(((p - y) ** 2).sum())
    ll = -math.log(max(float(probs.get(realized) or 0.0), EPS))
    top = order[int(np.argmax(p))] if len(p) else None
    return {"brier": brier, "log_loss": ll, "top_hit": 1.0 if top == realized else 0.0, "p_realized": float(probs.get(realized) or 0.0), "top": top}


def binary_metrics(p: list[float], y: list[int], bins: int = 10) -> dict[str, Any]:
    if not p:
        return {"n": 0}
    pa, ya = np.clip(np.array(p, float), EPS, 1 - EPS), np.array(y, float)
    out: dict[str, Any] = {"n": int(len(pa)), "brier": _r(np.mean((pa - ya) ** 2), 5),
                           "log_loss": _r(-np.mean(ya * np.log(pa) + (1 - ya) * np.log(1 - pa)), 5), "mean_p": _r(pa.mean()), "hit_rate": _r(ya.mean())}
    if len(pa) >= 20:
        edges = np.linspace(0, 1, bins + 1)
        idx = np.clip(np.digitize(pa, edges) - 1, 0, bins - 1)
        tab = []
        for b in range(bins):
            m = idx == b
            if m.any():
                tab.append({"lo": _r(edges[b], 2), "hi": _r(edges[b + 1], 2), "n": int(m.sum()), "mean_p": _r(pa[m].mean()), "observed": _r(ya[m].mean())})
        out["calibration"] = tab
        out["bias"] = _r(pa.mean() - ya.mean())
    return out


def mean_ci(xs: list[float]) -> dict[str, Any]:
    if not xs:
        return {"n": 0}
    a = np.array(xs, float)
    m = float(a.mean())
    se = float(a.std(ddof=1) / math.sqrt(len(a))) if len(a) > 1 else None
    return {"n": int(len(a)), "mean": _r(m), "ci95": None if se is None else [_r(m - 1.96 * se), _r(m + 1.96 * se)],
            "small_sample": len(a) < MIN_SHOW, "ci_note": "treats observations as independent; same-game correlation makes the interval too narrow"}


def bucket(x: float | None, buckets: tuple) -> str | None:
    if x is None:
        return None
    for lo, hi, lab in buckets:
        if lo <= x < hi:
            return lab
    return None


def final_pregame(rows: list[dict[str, Any]], key: str, t_key: str, start_of: Any) -> dict[str, dict[str, Any]]:
    """key -> the row with the latest ``t_key`` strictly before its game's start (``start_of(row)``)."""
    best: dict[str, tuple[str, dict[str, Any]]] = {}
    for r in rows:
        st = start_of(r)
        t = r.get(t_key)
        if st is None or not t or parse_iso(t) >= st:
            continue
        k = str(r.get(key))
        if k not in best or t > best[k][0]:
            best[k] = (t, r)
    return {k: v[1] for k, v in best.items()}


def learning_stage(c: dict[str, Any], checks: dict[str, bool]) -> dict[str, Any]:
    games, contracts = c.get("games_settled", 0) or 0, c.get("final_pregame_contracts_settled", 0) or 0
    scripts, clv = c.get("script_forecasts_settled", 0) or 0, c.get("candidate_clv_sample", 0) or 0
    stage = "EARLY_LEARNING"
    if games >= 100 and contracts >= 1000:
        stage = "CALIBRATION_BUILDING"
    if stage == "CALIBRATION_BUILDING" and games >= 300 and scripts >= 200 and clv >= 500 and checks.get("brier_close_both_halves") and checks.get("no_family_bias"):
        stage = "EVIDENCE_EMERGING"
    if (stage == "EVIDENCE_EMERGING" and games >= 800 and scripts >= 600 and clv >= 1000 and checks.get("brier_le_market_both_halves")
            and checks.get("candidate_clv_positive") and checks.get("scripts_beat_base_rate")):
        stage = "VALIDATED"
    nxt = {"EARLY_LEARNING": "CALIBRATION_BUILDING", "CALIBRATION_BUILDING": "EVIDENCE_EMERGING", "EVIDENCE_EMERGING": "VALIDATED"}.get(stage)
    need = {g[0]: g[2] for g in GATES}.get(nxt or "", {})
    progress = {k: {"have": {"games": games, "scripts": scripts, "clv": clv, "contracts": contracts}[k], "need": v} for k, v in need.items()}
    if nxt == "CALIBRATION_BUILDING":
        progress["contracts"] = {"have": contracts, "need": 1000}
    return {"stage": stage, "label": stage.replace("_", " "), "next_stage": nxt, "progress_to_next": progress,
            "gates": [{"stage": s, "rule": rule} for s, rule, _ in GATES], "checks": checks,
            "note": "maturity is a STATUS: it grants no betting authority, and ROI is never a criterion"}


# ------------------------------------------------------------------------------------------------ IO
def _realized_by_game(ledger: Any, finals: dict[str, Any], need: set[str], teams: dict[str, tuple[str, str]]) -> dict[str, dict[str, Any]]:
    from nhl_edge.scripts_v1.taxonomy import realized
    from nhl_edge.thesis.features import DrawFeatures

    goals: dict[str, list[dict[str, Any]]] = defaultdict(list)
    goalies: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for kind, acc in (("player_events/goals", goals), ("player_events/goalies", goalies)):
        for r in ledger.iter_rows(kind):
            g = str(r.get("game_id"))
            if g in need:
                acc[g].append(r)
    out = {}
    for gid in need:
        if gid not in finals or not goalies.get(gid):
            continue  # official events not ingested yet: retried next evaluate
        home, away = teams.get(gid, ("HOM", "AWY"))
        try:
            out[gid] = realized(DrawFeatures.from_actual(finals[gid].model_dump(mode="json"), goals.get(gid, []), goalies[gid], home, away))
        except Exception as e:  # noqa: BLE001 - one malformed game never blocks the rest
            log.warning(kv(event="realized_script_failed", game=gid, err=str(e)[:200]))
    return out


def run_learning(ledger: Any, settlements: dict[str, Any], starts: dict[str, datetime], obs_loader: Any, now: datetime) -> dict[str, Any]:
    from nhl_edge.evaluation.clv import closing_snapshot, clv_prob
    from nhl_edge.scripts_v1 import CANDIDATE_RULES_VERSION, REALIZED_VERSION, SCRIPT_VERSION, SURVIVAL_VERSION
    from nhl_edge.scripts_v1.taxonomy import SCRIPTS, base_rates
    from nhl_edge.settlement.engine import SettlementOutcome
    from nhl_edge.workflows.evaluate import close_price_cents
    from nhl_edge.workflows.settle import load_final_results

    order = [s.id for s in SCRIPTS]
    base = base_rates().get("frequency") or {}
    finals = load_final_results(ledger)
    start_of = lambda r: starts.get(str(r.get("game_id")))  # noqa: E731

    # ---- script forecasts -> script_postmortems ----------------------------------------------------------------
    forecasts = list(ledger.iter_rows("script_forecasts"))
    existing = list(ledger.iter_rows("script_postmortems"))
    seen = {(r.get("snapshot_id"), str(r.get("game_id")), r.get("realized_version")) for r in existing}
    need = {str(f["game_id"]) for f in forecasts if str(f["game_id"]) in finals}
    teams = {str(f["game_id"]): (f.get("home"), f.get("away")) for f in forecasts}
    realized = _realized_by_game(ledger, finals, need, teams)
    new_rows = []
    for f in forecasts:
        gid = str(f["game_id"])
        st = starts.get(gid)
        if gid not in realized or st is None or parse_iso(f["decided_at_utc"]) >= st:
            continue
        k = (f.get("snapshot_id"), gid, REALIZED_VERSION)
        if k in seen:
            continue
        rz = realized[gid]
        sc = multiclass_scores(f["script_probabilities"], rz["script_id"], order)
        bs = multiclass_scores(base, rz["script_id"], order)
        new_rows.append({"snapshot_id": f.get("snapshot_id"), "game_id": gid, "decided_at_utc": f["decided_at_utc"], "start_utc": iso(st),
                         "hours_before_start": _r((st - parse_iso(f["decided_at_utc"])).total_seconds() / 3600.0, 3),
                         "script_version": f.get("script_version"), "realized_version": REALIZED_VERSION, "predicted": f["script_probabilities"],
                         "realized_script": rz["script_id"], "realized_metrics": rz["metrics"], "brier": _r(sc["brier"], 5), "log_loss": _r(sc["log_loss"], 5),
                         "top_script": sc["top"], "top_hit": bool(sc["top_hit"]), "p_realized": _r(sc["p_realized"]), "base_rate_brier": _r(bs["brier"], 5),
                         "base_rate_log_loss": _r(bs["log_loss"], 5), "evaluated_at_utc": iso(now), "authority": "RESEARCH_ONLY"})
        seen.add(k)
    if new_rows:
        ledger.append_rows("script_postmortems", new_rows, observed_at=now)
    spm = existing + new_rows
    spm_final = final_pregame(spm, "game_id", "decided_at_utc", start_of)
    scripts_sec = script_section(list(spm_final.values()), order, len(spm))

    # ---- model vs market (DATA_ONLY_V1 evaluations, final pregame per contract) ---------------------------------
    evals = [r for r in ledger.iter_rows("evaluations") if r.get("pregame")]
    fin = final_pregame(evals, "ticker", "predicted_at_utc", start_of)
    probability = probability_section(list(fin.values()))
    windows = window_section(evals)

    # ---- projection quality (expected goals from the final pregame thesis snapshot per game) ---------------------
    tgames = list(ledger.iter_rows("thesis_games"))
    projection = projection_section(final_pregame(tgames, "game_id", "decided_at_utc", start_of), finals)

    # ---- research candidates (shadow, every shortlisted side at the final pregame snapshot) ----------------------
    pms = list(ledger.iter_rows("thesis_postmortems"))
    dec_surv = {}
    for d in ledger.iter_rows("thesis_decisions"):
        if d.get("script_survival"):
            dec_surv[d["decision_id"]] = d["script_survival"]
    snap_final = {gid: r.get("snapshot_id") for gid, r in final_pregame(tgames, "game_id", "decided_at_utc", start_of).items()}
    pm_final = [r for r in pms if r.get("snapshot_id") and snap_final.get(str(r.get("game_id"))) == r.get("snapshot_id")]
    candidates = candidate_section(pm_final, dec_surv)

    # script candidates scored directly from script_forecasts (robustness/survival populations; settles from settlements)
    sf_final = final_pregame(forecasts, "game_id", "decided_at_utc", start_of)
    sc_rows = []
    tickers = {c["ticker"] for f in sf_final.values() for c in f.get("candidates") or []}
    obs = obs_loader({t for t in tickers if t in settlements}) if tickers else {}
    for gid, f in sf_final.items():
        for c in f.get("candidates") or []:
            rec = settlements.get(c["ticker"])
            if rec is None or rec.outcome not in (SettlementOutcome.YES, SettlementOutcome.NO) or c.get("cost") is None:
                continue
            won = (rec.outcome == SettlementOutcome.YES) == (c["side"] == "yes")
            close = close_price_cents(closing_snapshot(obs.get(c["ticker"], []), starts[gid])) if gid in starts else None
            clv = None
            if close is not None and c.get("ask_cents") is not None:
                yes_entry = float(c["ask_cents"]) if c["side"] == "yes" else 100.0 - float(c["ask_cents"])
                if 0 <= yes_entry <= 100:
                    clv = clv_prob(yes_entry, close, c["side"])
            sc_rows.append({**c, "game_id": gid, "won": won, "profit_per_contract": (1.0 if won else 0.0) - float(c["cost"]), "clv": clv})
    script_candidates = script_candidate_section(sc_rows)

    counts = {
        "projection_runs": len({r.get("predicted_at_utc") for r in evals}),
        "games_projected": len({str(r.get("game_id")) for r in tgames} | {str(f["game_id"]) for f in forecasts}
                               | {str(r.get("game_id")) for r in ledger.iter_rows("predictions")}),
        "games_settled": len(finals),
        "contract_evaluations_pregame": len(evals),
        "final_pregame_contracts_settled": len(fin),
        "research_decisions": len({r.get("logical_wager_key") or r.get("decision_id") for r in ledger.iter_rows("thesis_decisions")}),
        "research_decisions_settled_final": len(pm_final),
        "market_snapshots": sum(1 for e in ledger.manifest() if str(e.kind).startswith("kalshi/markets")),
        "script_forecasts": len(forecasts),
        "script_forecast_games": len({str(f["game_id"]) for f in forecasts}),
        "script_forecasts_settled": len(spm),
        "script_games_settled": len(spm_final),
        "candidate_clv_sample": (candidates.get("clv") or {}).get("n", 0) + sum(1 for r in sc_rows if r.get("clv") is not None),
        "supported_families": sorted({str(r.get("family")) for r in fin.values()}),
    }
    checks = gate_checks(list(fin.values()), probability, candidates, scripts_sec)
    rep = {
        "kind": "nhl_learning_report", "version": LEARNING_VERSION, "generated_at_utc": iso(now), "authority": "RESEARCH_ONLY",
        "versions": {"projection_model": "DATA_ONLY_V1 (nhl-sim-1.1, nhl-features-1.0)", "joint_draw": "PLAYER_SIM_V1 on nhl-sim-2.0",
                     "script_model": SCRIPT_VERSION, "realized_script": REALIZED_VERSION, "survival": SURVIVAL_VERSION,
                     "candidate_rules": CANDIDATE_RULES_VERSION, "opponent_adjustment": "nhl-oppadj-1.0", "thesis": "nhl-thesis-1.1"},
        "counts": counts, "stage": learning_stage(counts, checks), "probability": probability, "windows": windows, "projection": projection,
        "scripts": scripts_sec, "research_candidates": candidates, "script_candidates": script_candidates,
        "actual_wagers": {"note": "routed manual wagers are reported only in the accounting ledger / app performance.json; never mixed with research candidates"},
        "unknowns": unknowns(counts, probability, scripts_sec, candidates, script_candidates),
        "rules": {"populations": __doc__.split("Population rules (never mixed):")[1].strip(), "min_show": MIN_SHOW},
    }
    out = ledger.root / "eval"
    out.mkdir(parents=True, exist_ok=True)
    (out / "report_learning.json").write_text(json.dumps(rep, indent=1, default=str, sort_keys=True))
    log.info(kv(event="learning", stage=rep["stage"]["stage"], scripts_settled=len(spm), new=len(new_rows), games=len(finals)))
    return rep


# ------------------------------------------------------------------------------------------------ sections
def probability_section(rows: list[dict[str, Any]]) -> dict[str, Any]:
    both = [r for r in rows if r.get("p_data_only") is not None and r.get("p_market") is not None]
    model = binary_metrics([float(r["p_data_only"]) for r in both], [int(r["y"]) for r in both])
    market = binary_metrics([float(r["p_market"]) for r in both], [int(r["y"]) for r in both])
    diff = [float(r["p_data_only"]) - float(r["p_market"]) for r in both]
    toward = []
    for r in both:
        if r.get("close_prob") is None:
            continue
        gap = float(r["p_data_only"]) - float(r["p_market"])
        if abs(gap) < 0.01:
            continue
        move = float(r["close_prob"]) - float(r["p_market"])
        toward.append(1.0 if move * gap > 0 else 0.0)
    fams: dict[str, Any] = {}
    for fam in sorted({str(r.get("family")) for r in both}):
        fr = [r for r in both if str(r.get("family")) == fam]
        m = binary_metrics([float(r["p_data_only"]) for r in fr], [int(r["y"]) for r in fr], bins=5)
        k = binary_metrics([float(r["p_market"]) for r in fr], [int(r["y"]) for r in fr], bins=5)
        fams[fam] = {"n": len(fr), "model_brier": m.get("brier"), "market_brier": k.get("brier"), "model_bias": m.get("bias"),
                     "small_sample": len(fr) < MIN_SHOW}
    clv = [float(r["clv_signed"]) for r in both if r.get("clv_signed") is not None]
    return {"population": "DATA_ONLY_V1 final pregame snapshot per contract (settled)", "n": len(both), "model": model, "market": market,
            "brier_diff_model_minus_market": None if not both else _r((model.get("brier") or 0) - (market.get("brier") or 0), 5),
            "mean_signed_model_minus_market": _r(np.mean(diff)) if diff else None, "mean_abs_disagreement": _r(np.mean(np.abs(diff))) if diff else None,
            "market_moved_toward_model": mean_ci(toward), "model_side_clv": mean_ci(clv), "by_family": fams}


def window_section(evals: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for lab, lo, hi in WINDOWS:
        best: dict[str, dict[str, Any]] = {}
        mid = (lo + hi) / 2
        for r in evals:
            h = r.get("hours_before_start")
            if h is None or not (lo <= float(h) <= hi) or r.get("p_data_only") is None or r.get("p_market") is None:
                continue
            t = str(r.get("ticker"))
            if t not in best or abs(float(h) - mid) < abs(float(best[t]["hours_before_start"]) - mid):
                best[t] = r
        rows = list(best.values())
        m = binary_metrics([float(r["p_data_only"]) for r in rows], [int(r["y"]) for r in rows], bins=5)
        k = binary_metrics([float(r["p_market"]) for r in rows], [int(r["y"]) for r in rows], bins=5)
        out.append({"window": lab, "hours": [lo, hi], "n": len(rows), "model_brier": m.get("brier"), "market_brier": k.get("brier"),
                    "mean_abs_disagreement": _r(np.mean([abs(float(r["p_data_only"]) - float(r["p_market"])) for r in rows])) if rows else None})
    return out


def projection_section(final_games: dict[str, dict[str, Any]], finals: dict[str, Any]) -> dict[str, Any]:
    tot_err, h_err, a_err = [], [], []
    for gid, g in final_games.items():
        fr = finals.get(gid)
        if fr is None:
            continue
        away, home = str(g.get("matchup") or "A @ H").split(" @ ")
        sc = g.get("scripts") or []
        if not sc:
            continue
        w = sum(float(s.get("frequency") or 0) for s in sc) or 1.0
        et = sum(float(s.get("frequency") or 0) * float(s.get("total_goals") or 0) for s in sc) / w
        eh = sum(float(s.get("frequency") or 0) * float(s.get(f"{home}_goals") or 0) for s in sc) / w
        ea = sum(float(s.get("frequency") or 0) * float(s.get(f"{away}_goals") or 0) for s in sc) / w
        r = fr.model_dump(mode="json")
        hg = int(r.get("home_final") or 0) - (1 if r.get("last_period_type") == "SO" and int(r.get("home_final") or 0) > int(r.get("away_final") or 0) else 0)
        ag = int(r.get("away_final") or 0) - (1 if r.get("last_period_type") == "SO" and int(r.get("away_final") or 0) > int(r.get("home_final") or 0) else 0)
        tot_err.append(et - (hg + ag))
        h_err.append(eh - hg)
        a_err.append(ea - ag)
    if not tot_err:
        return {"n_games": 0}
    t, h, a = np.array(tot_err), np.array(h_err), np.array(a_err)
    return {"population": "final pregame thesis snapshot per settled game (joint draw expected non-shootout goals)", "n_games": int(len(t)),
            "total_mae": _r(np.abs(t).mean(), 3), "total_rmse": _r(np.sqrt((t**2).mean()), 3), "total_bias": _r(t.mean(), 3),
            "team_goals_mae": _r(np.abs(np.concatenate([h, a])).mean(), 3), "home_bias": _r(h.mean(), 3), "away_bias": _r(a.mean(), 3),
            "small_sample": len(t) < MIN_SHOW}


def script_section(rows: list[dict[str, Any]], order: list[str], n_all: int) -> dict[str, Any]:
    if not rows:
        return {"n_games": 0, "n_snapshots": n_all, "note": "no settled NHL_SCRIPT_V1 forecast yet"}
    br = [float(r["brier"]) for r in rows]
    bb = [float(r["base_rate_brier"]) for r in rows]
    conf: dict[str, Counter] = {k: Counter() for k in order}
    pred_mean = {k: float(np.mean([float((r["predicted"] or {}).get(k) or 0) for r in rows])) for k in order}
    real = Counter(r["realized_script"] for r in rows)
    for r in rows:
        conf[r["top_script"]][r["realized_script"]] += 1
    calib = []
    ps, ys = [], []
    for r in rows:
        for k in order:
            ps.append(float((r["predicted"] or {}).get(k) or 0))
            ys.append(1 if r["realized_script"] == k else 0)
    cb = binary_metrics(ps, ys, bins=5).get("calibration") or []
    calib = cb
    return {"population": "final pregame NHL_SCRIPT_V1 forecast per settled game", "n_games": len(rows), "n_snapshots": n_all,
            "multiclass_brier": _r(np.mean(br), 4), "base_rate_brier": _r(np.mean(bb), 4),
            "log_loss": _r(np.mean([float(r["log_loss"]) for r in rows]), 4), "base_rate_log_loss": _r(np.mean([float(r["base_rate_log_loss"]) for r in rows]), 4),
            "top_script_accuracy": _r(np.mean([1.0 if r["top_hit"] else 0.0 for r in rows]), 4),
            "by_script": [{"id": k, "mean_predicted": _r(pred_mean[k]), "realized_share": _r(real.get(k, 0) / len(rows)), "realized_n": real.get(k, 0)} for k in order],
            "confusion": {k: dict(sorted(v.items())) for k, v in conf.items() if v}, "calibration": calib, "small_sample": len(rows) < MIN_SHOW}


def _group(rows: list[dict[str, Any]], key: Any) -> dict[str, Any]:
    g: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in rows:
        k = key(r)
        if k is not None:
            g[str(k)].append(r)
    out = {}
    for k, rs in sorted(g.items()):
        prof = [float(r["profit_per_contract"]) for r in rs if r.get("profit_per_contract") is not None]
        cost = [float(r["cost"]) for r in rs if r.get("cost") is not None]
        out[k] = {"n": len(rs), "hit_rate": _r(np.mean([1.0 if r["won"] else 0.0 for r in rs])), "mean_p": _r(np.mean([float(r["p"]) for r in rs if r.get("p") is not None])) if any(r.get("p") is not None for r in rs) else None,
                  "shadow_return_per_cost": _r(sum(prof) / sum(cost)) if cost and sum(cost) > 0 else None,
                  "mean_clv": _r(np.mean([float(r["clv"]) for r in rs if r.get("clv") is not None])) if any(r.get("clv") is not None for r in rs) else None,
                  "small_sample": len(rs) < MIN_SHOW}
    return out


def candidate_section(pm_rows: list[dict[str, Any]], surv: dict[str, dict[str, Any]]) -> dict[str, Any]:
    rows = []
    for r in pm_rows:
        price = r.get("entry_price_cents")
        if price is None:
            continue
        cost = float(price) / 100.0
        mr = r.get("model_result") or {}
        rows.append({"won": bool(r.get("won")), "cost": cost, "profit_per_contract": (1.0 if r.get("won") else 0.0) - cost, "clv": r.get("price_result_clv"),
                     "family": r.get("family"), "status": r.get("research_status"), "p": mr.get("p_adjusted"), "ev": r.get("ev_adjusted"),
                     "funded_profit": r.get("research_realized_profit") if r.get("research_status") == "FUNDED_RESEARCH" else None,
                     "robustness": (surv.get(r.get("decision_id")) or {}).get("robustness")})
    if not rows:
        return {"n": 0, "note": "no settled research decision yet"}
    funded = [r for r in rows if r["status"] == "FUNDED_RESEARCH"]
    return {"population": "every shortlisted research candidate at the game's final pregame thesis snapshot (shadow: scored whether or not wagered)",
            "n": len(rows), "hit_rate": _r(np.mean([1.0 if r["won"] else 0.0 for r in rows])), "mean_p": _r(np.mean([float(r["p"]) for r in rows if r.get("p") is not None])),
            "shadow_return_per_cost": _r(sum(r["profit_per_contract"] for r in rows) / sum(r["cost"] for r in rows)),
            "clv": mean_ci([float(r["clv"]) for r in rows if r.get("clv") is not None]),
            "by_status": _group(rows, lambda r: r["status"]), "by_family": _group(rows, lambda r: r["family"]),
            "by_edge_bucket": _group(rows, lambda r: bucket(r.get("ev"), EDGE_BUCKETS)),
            "by_robustness": _group(rows, lambda r: r.get("robustness")),
            "funded_research": {"n": len(funded), "nominal_profit_dollars": _r(sum(float(r["funded_profit"] or 0) for r in funded), 2),
                                "note": "nominal research stakes (whole dollars, $250 research bankroll); never placed"},
            "small_sample": len(rows) < MIN_SHOW}


def script_candidate_section(rows: list[dict[str, Any]]) -> dict[str, Any]:
    if not rows:
        return {"n": 0, "note": "no settled NHL_SCRIPT_V1 research candidate yet (the script layer started with this release)"}
    for r in rows:
        r["p"] = r.get("p_conservative")
    return {"population": "NHL_SCRIPT_V1 research candidates at each game's final pregame snapshot, scored per contract at the executable ask",
            "n": len(rows), "clv": mean_ci([float(r["clv"]) for r in rows if r.get("clv") is not None]),
            "by_robustness": _group(rows, lambda r: r.get("robustness")), "by_survival": _group(rows, lambda r: bucket(r.get("mass_survived"), SURVIVAL_BUCKETS)),
            "by_family": _group(rows, lambda r: r.get("family")), "by_status": _group(rows, lambda r: r.get("governance_status")),
            "by_goalie_dependency": _group(rows, lambda r: "goalie unconfirmed" if any(str(d).startswith("GOALIE_") for d in r.get("dependencies") or []) else "goalies confirmed"),
            "small_sample": len(rows) < MIN_SHOW}


def gate_checks(final_rows: list[dict[str, Any]], prob: dict[str, Any], cand: dict[str, Any], scripts: dict[str, Any]) -> dict[str, bool]:
    rows = sorted([r for r in final_rows if r.get("p_data_only") is not None and r.get("p_market") is not None], key=lambda r: str(r.get("predicted_at_utc")))
    halves = [rows[: len(rows) // 2], rows[len(rows) // 2:]] if len(rows) >= 200 else []
    diffs = []
    for h in halves:
        m = binary_metrics([float(r["p_data_only"]) for r in h], [int(r["y"]) for r in h])
        k = binary_metrics([float(r["p_market"]) for r in h], [int(r["y"]) for r in h])
        diffs.append((m.get("brier") or 0) - (k.get("brier") or 0))
    fam_ok = all(abs(v.get("model_bias") or 0) <= 0.03 for v in (prob.get("by_family") or {}).values() if (v.get("n") or 0) >= 200)
    clv = cand.get("clv") or {}
    ci = clv.get("ci95")
    return {"brier_close_both_halves": bool(diffs) and all(d <= 0.005 for d in diffs), "brier_le_market_both_halves": bool(diffs) and all(d <= 0 for d in diffs),
            "no_family_bias": fam_ok, "candidate_clv_positive": bool(ci and ci[0] is not None and ci[0] > 0),
            "scripts_beat_base_rate": bool(scripts.get("n_games") and (scripts.get("multiclass_brier") or 9) < (scripts.get("base_rate_brier") or 0))}


def unknowns(c: dict[str, Any], prob: dict[str, Any], scripts: dict[str, Any], cand: dict[str, Any], sc: dict[str, Any]) -> list[str]:
    out = []
    if (scripts.get("n_games") or 0) < MIN_SHOW:
        out.append(f"Whether the script probabilities are calibrated: {scripts.get('n_games') or 0} settled script forecasts (need {MIN_SHOW}+ to say anything, 200+ to rely on it).")
    if (sc.get("n") or 0) < MIN_SHOW:
        out.append(f"Whether robust candidates outperform fragile ones: {sc.get('n') or 0} settled script-layer candidates.")
    cl = cand.get("clv") or {}
    if (cl.get("n") or 0) < 500:
        out.append(f"Whether research candidates beat the closing line: {cl.get('n') or 0} CLV observations (mean {cl.get('mean')}); far too few to separate skill from noise.")
    if (c.get("games_settled") or 0) < 300:
        out.append(f"Whether the projection model beats the market: {c.get('games_settled')} settled games; model vs market Brier difference "
                   f"{prob.get('brier_diff_model_minus_market')} is within early-season noise.")
    out.append("Whether the opponent adjustment improves betting decisions: it is a RESEARCH layer (walk-forward sanity check only) and is not a model input.")
    return out
