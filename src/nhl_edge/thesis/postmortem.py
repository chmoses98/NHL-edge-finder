"""Postmortem: score the prospective pregame decision state against what actually happened, keeping separate

* THESIS RESULT      did the bet's primary (and secondary) thesis event happen in the real game?
* EXPRESSION RESULT  given the thesis outcome, did the chosen contract win? ("PIT offense dominated, Rakell did not
                     score" is THESIS_RIGHT_EXPRESSION_LOST, not "prediction wrong"), with the model's own
                     P(bet | thesis) at decision time so an expected miss is visible as expected;
* PRICE RESULT       closing-line value: Kalshi closing midpoint (last observation strictly before the start) vs our
                     executable entry price, from the side we took;
* MODEL RESULT       Brier / log loss of the model probability and the confidence-adjusted one;
* PORTFOLIO RESULT   per game: realised card P/L vs the simulated distribution, stake concentration, and whether
                     several bets failed together on one thesis.

The realised game is classified by EXACTLY the functions used pregame (``DrawFeatures.from_actual`` +
``thesis_events`` + ``primary_labels``). Only decisions made before the scheduled start are scored.
"""

from __future__ import annotations

import math
from collections import defaultdict
from typing import Any

from nhl_edge.thesis.events import thesis_events
from nhl_edge.thesis.features import DrawFeatures
from nhl_edge.thesis.scripts import Taxonomy, primary_labels


def actual_view(f: DrawFeatures) -> dict[str, Any]:
    ev = {e.key: bool(e.mask[0]) for e in thesis_events(f)}
    code = int(primary_labels(f)[0])
    tx = Taxonomy(f.home_abbrev, f.away_abbrev)
    return {"events": ev, "script_key": tx.primary_key(code), "script": tx.primary_name(code),
            "summary": {"home_goals": int(f.home_goals[0]), "away_goals": int(f.away_goals[0]), "home_shots": int(f.home_shots[0]), "away_shots": int(f.away_shots[0]),
                        "ot": bool(f.ot[0]), "home_pp": int(f.home_pp[0]), "away_pp": int(f.away_pp[0]), "home_en": int(f.home_en[0]), "away_en": int(f.away_en[0])}}


def expression_label(thesis_hit: bool | None, won: bool) -> str:
    if thesis_hit is None:
        return "NO_THESIS_" + ("WON" if won else "LOST")
    return f"THESIS_{'RIGHT' if thesis_hit else 'WRONG'}_EXPRESSION_{'WON' if won else 'LOST'}"


def score_decision(d: dict[str, Any], actual: dict[str, Any], outcome_yes: bool, close_prob: float | None) -> dict[str, Any]:
    won = outcome_yes if d["side"] == "yes" else not outcome_yes
    pt = (d.get("primary_thesis") or {}).get("key")
    st = (d.get("secondary_thesis") or {}).get("key") if d.get("secondary_thesis") else None
    hit = actual["events"].get(pt) if pt and pt != "DIFFUSE" else None
    hit2 = actual["events"].get(st) if st else None
    p, pa = float(d["p_model"]), float(d.get("p_adjusted") or d["p_model"])
    y = 1.0 if won else 0.0
    ll = lambda q: -math.log(min(max(q if won else 1 - q, 1e-6), 1.0))  # noqa: E731
    clv = None
    if close_prob is not None and d.get("executable_price_cents") is not None:
        close_side = close_prob if d["side"] == "yes" else 1.0 - close_prob
        clv = round(close_side - d["executable_price_cents"] / 100.0, 4)
    pbt = (d.get("primary_thesis") or {}).get("p_bet_given_thesis")
    pbnt = (d.get("primary_thesis") or {}).get("p_bet_given_not_thesis")
    cost = d.get("cost_per_contract")
    return {
        "decision_id": d["decision_id"], "run_id": d.get("run_id"), "decided_at_utc": d.get("decided_at_utc"), "game_id": d["game_id"], "bet_id": d["bet_id"],
        "ticker": d["ticker"], "side": d["side"], "family": d["family"], "chosen": bool(d.get("chosen")), "stake_dollars": d.get("stake_dollars") or 0.0,
        "won": won, "primary_thesis": pt, "thesis_result": hit, "secondary_thesis": st, "secondary_thesis_result": hit2,
        "expression_result": expression_label(hit, won),
        "model_p_bet_given_thesis_outcome": pbt if hit else pbnt if hit is False else None,
        "realized_script": actual["script_key"], "realized_script_name": actual["script"],
        "model_p_win_in_realized_script": (d.get("p_win_by_script") or {}).get(actual["script_key"]),
        "price_result_clv": clv, "close_prob_yes": close_prob, "entry_price_cents": d.get("executable_price_cents"),
        "model_result": {"p_model": p, "p_adjusted": pa, "p_kalshi_mid": d.get("p_kalshi_mid"), "brier_model": round((p - y) ** 2, 5), "brier_adjusted": round((pa - y) ** 2, 5),
                         "brier_kalshi_mid": None if d.get("p_kalshi_mid") is None else round((float(d["p_kalshi_mid"]) - y) ** 2, 5),
                         "logloss_model": round(ll(p), 5), "logloss_adjusted": round(ll(pa), 5)},
        "realized_profit": None if not cost or not d.get("stake_dollars") else round(d["stake_dollars"] * ((1.0 if won else 0.0) - cost) / cost, 2),
        "actual_game": actual["summary"],
        # snapshot identity / research layer (absent on decisions logged before nhl-card-1.1; the report joins them from the decision row)
        "snapshot_id": d.get("snapshot_id"), "research_status": d.get("research_status"), "research_stake_dollars": d.get("research_stake_dollars"),
        "research_realized_profit": research_profit(d, won),
        "fidelity_class": (d.get("expression_fidelity") or {}).get("fidelity_class"), "ev_raw": d.get("ev_raw"), "ev_adjusted": d.get("ev_adjusted"),
    }


def research_profit(d: dict[str, Any], won: bool) -> float | None:
    """P/L of the FUNDED research stake (0 for SHADOW_ONLY / REJECTED; None for decisions without a research layer)."""
    st = d.get("research_stake_dollars")
    cost = d.get("cost_per_contract")
    if st is None or not cost:
        return None
    return round(float(st) * ((1.0 if won else 0.0) - float(cost)) / float(cost), 2) if st else 0.0


def portfolio_result(scored: list[dict[str, Any]], game_row: dict[str, Any] | None) -> dict[str, Any]:
    chosen = [s for s in scored if s["chosen"] and s["stake_dollars"]]
    pl = sum(s["realized_profit"] or 0.0 for s in chosen)
    stake = sum(s["stake_dollars"] for s in chosen)
    by_thesis: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for s in chosen:
        by_thesis[s["primary_thesis"] or "?"].append(s)
    B = ((game_row or {}).get("portfolios") or {}).get("B") or {}
    pct = None
    if B.get("p05") is not None:
        qs = [(5, B["p05"]), (10, B["p10"]), (25, B["p25"]), (50, B["median_profit"]), (75, B["p75"]), (95, B["p95"])]
        pct = next((f"<= p{q}" for q, v in qs if pl <= v), "> p95")
    return {"n_bets": len(chosen), "stake": round(stake, 2), "realized_profit": round(pl, 2), "expected_profit": B.get("expected_profit"),
            "realized_vs_simulated": pct, "largest_thesis_share": round(max((sum(x["stake_dollars"] for x in v) for v in by_thesis.values()), default=0.0) / stake, 3) if stake else None,
            "n_theses": len(by_thesis), "theses_with_multiple_losses": sorted(k for k, v in by_thesis.items() if sum(1 for x in v if not x["won"]) >= 2),
            "multiple_losses_on_one_thesis": [{"thesis": k, "thesis_happened": v[0]["thesis_result"], "n_lost": sum(1 for x in v if not x["won"]),
                                               "loss": round(sum(-(x["realized_profit"] or 0) for x in v if not x["won"]), 2),
                                               "reading": ("thesis was wrong and several bets shared it: concentration cost" if v[0]["thesis_result"] is False else
                                                           "thesis happened but its expressions missed: expression risk, not a thesis error")}
                                              for k, v in by_thesis.items() if sum(1 for x in v if not x["won"]) >= 2]}
