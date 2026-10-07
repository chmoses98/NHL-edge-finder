"""Assemble the NHL_SCRIPT_V1 research block of one game from the thesis analysis (pure, deterministic).

Output (``game_research``) is what lands in packet.json ``thesis_card.games[].scripts_v1``, the ``script_forecasts``
ledger kind (immutable, one row per game per thesis snapshot) and, via the research export,
``event_research.extensions.nhl_scripts_v1`` for SIFT.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from nhl_edge.scripts_v1 import AUTHORITY, CANDIDATE_RULES_VERSION, SCRIPT_METHODOLOGY, SCRIPT_VERSION, SURVIVAL_VERSION
from nhl_edge.scripts_v1.candidates import ORDERING, build_candidates
from nhl_edge.scripts_v1.summary import market_effects, script_summaries
from nhl_edge.scripts_v1.survival import MIN_EV, TIER_RANK, TIERS, game_survival
from nhl_edge.scripts_v1.taxonomy import SCRIPTS, classify, methodology, taxonomy_doc


def _r(x: Any, n: int = 4) -> float | None:
    return None if x is None or (isinstance(x, float) and np.isnan(x)) else round(float(x), n)


def _side(sv: Any, price_cents: Any) -> dict[str, Any]:
    return {"ask_cents": price_cents, "cost": _r(sv.cost), "delta": _r(sv.delta), "ev_adjusted": _r(sv.expected_ev),
            "mass_survived": _r(sv.mass), "n_major_survived": sv.n_major_survived,
            "survives": None if sv.survives is None else "".join("1" if x else "0" for x in sv.survives),
            "failure_script": None if sv.failure_script is None else SCRIPTS[sv.failure_script].id, "tier": sv.tier, "data_quality": sv.data_quality}


def game_research(a: dict[str, Any], ctx: dict[str, Any] | None = None) -> dict[str, Any]:
    """``a``: one game's ``thesis.engine.analyze_game`` output after ``finalize_slate`` (research statuses attached).
    ``ctx``: optional pregame context {goalies: {home/away: {status, name, confidence}}, rest/b2b, lambdas}."""
    gd = a["gd"]
    f = gd.features
    home, away = gd.home, gd.away
    ctx = {"home": home, "away": away, **(ctx or gd.meta.get("context") or {})}
    codes = classify(f)
    survival, P, freq = game_survival(a["bets"], a["econ"], codes)
    summaries = script_summaries(f, codes, gd.player_points)
    effects = market_effects(a["bets"], P, freq, survival)
    tax = {t["id"]: t for t in taxonomy_doc(home, away)}
    scripts = []
    for s in summaries:
        scripts.append({**tax[s["id"]], **s, "helps": effects[s["id"]]["helped"], "hurts": effects[s["id"]]["hurt"]})
    scripts.sort(key=lambda s: (-s["probability"], s["code"]))
    for i, s in enumerate(scripts, 1):
        s["rank"] = i
    # market matrix: one row per priced contract (both sides), P(YES | script) aligned to SCRIPTS order
    by_ticker: dict[str, dict[str, Any]] = {}
    for i, b in enumerate(a["bets"]):
        row = by_ticker.setdefault(b.ticker, {"ticker": b.ticker, "title": b.title, "family": b.family, "team": None})
        sv = survival[b.bet_id]
        if b.side == "yes":
            row.update({"p_yes": _r(b.p), "p_yes_mid": _r(b.p_mid), "p_yes_by_script": [_r(x) for x in P[i]], "team": b.team,
                        "yes": _side(sv, b.price_cents)})
        else:
            row["no"] = _side(sv, b.price_cents)
    markets = sorted(by_ticker.values(), key=lambda r: r["ticker"])
    cands = build_candidates(a, survival, ctx)
    tiers = {t: sum(1 for c in cands if c["robustness"] == t and c["governance"]["status"] != "REJECTED") for t in TIER_RANK}
    best = next((c for c in cands if c["governance"]["status"] != "REJECTED" and c["robustness"] in ("ROBUST", "MODERATE")), None)
    return {
        "script_version": SCRIPT_VERSION, "methodology_version": SCRIPT_METHODOLOGY, "survival_version": SURVIVAL_VERSION,
        "candidate_rules_version": CANDIDATE_RULES_VERSION, "authority": AUTHORITY, "game_id": gd.game_id, "home": home, "away": away,
        "n_draws": int(f.n), "draw_source": gd.meta.get("source"), "seed": gd.meta.get("seed"),
        "script_order": [s.id for s in SCRIPTS],
        "scripts": scripts,
        "most_likely": {"id": scripts[0]["id"], "label": scripts[0]["label"], "probability": scripts[0]["probability"]} if scripts else None,
        "probability_check": {"sum": round(float(freq.sum()), 6), "n_scripts_with_draws": int((freq > 0).sum())},
        "markets": markets, "unpriced": [{k: u.get(k) for k in ("ticker", "family", "title", "reason")} for u in gd.unpriced],
        "candidates": cands,
        "candidate_summary": {"n": len(cands), "by_tier": tiers, "best": None if best is None else {k: best[k] for k in ("bet_id", "title", "side", "robustness")}},
        "context": {k: ctx.get(k) for k in ("goalies", "home_rest_days", "away_rest_days", "home_b2b", "away_b2b", "lam_home", "lam_away", "trusted", "input_reasons")},
        "rules": {"min_ev_per_contract": MIN_EV, "tiers": TIERS, "ordering": ORDERING, "taxonomy": methodology(),
                  "conservative_probability": "p_adjusted = mid + k (p - mid) (thesis.expression); per-script EV subtracts delta = p - p_adjusted from P(side | script)"},
    }


def forecast_row(gr: dict[str, Any], *, decided_at: str, run_id: str, snapshot_id: str, start_time_utc: str | None) -> dict[str, Any]:
    """The immutable ``script_forecasts`` ledger row (compact: no market matrix, candidates reduced to decision fields)."""
    return {
        "game_id": gr["game_id"], "decided_at_utc": decided_at, "run_id": run_id, "snapshot_id": snapshot_id, "start_time_utc": start_time_utc,
        "script_version": gr["script_version"], "survival_version": gr["survival_version"], "candidate_rules_version": gr["candidate_rules_version"],
        "home": gr["home"], "away": gr["away"], "n_draws": gr["n_draws"],
        "script_probabilities": {s["id"]: s["probability"] for s in gr["scripts"]},
        "script_summaries": [{k: s.get(k) for k in ("id", "probability", "p_home_win", "home_goals", "away_goals", "total_goals", "total_goals_range")}
                             for s in gr["scripts"]],
        "candidates": [{"bet_id": c["bet_id"], "ticker": c["ticker"], "side": c["side"], "family": c["family"], "rank": c["rank"],
                        "ask_cents": c["price"]["ask_cents"], "cost": c["price"]["cost"], "p_model": c["p_model"], "p_conservative": c["p_conservative"],
                        "p_market_mid": c["p_market_mid"], "ev_adjusted": c["ev_adjusted"], "bet_up_to_cents": c["bet_up_to_cents"],
                        "mass_survived": c["survival"]["mass_survived"], "n_major_survived": c["survival"]["n_major_survived"],
                        "failure_script": c["survival"]["failure_script"], "robustness": c["robustness"], "family_reliability": c["family_reliability"],
                        "governance_status": c["governance"]["status"], "stake_dollars": c["governance"]["stake_dollars"],
                        "exposure_group": c["exposure_group"], "dependencies": [d["flag"] for d in c["dependencies"]]} for c in gr["candidates"]],
        "context": gr["context"], "authority": AUTHORITY,
    }
