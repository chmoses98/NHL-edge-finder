"""The research-execution layer on top of the optimiser's card (portfolio B): governance statuses, whole-dollar research
stakes, the per-game CARD REVIEW block and the funded research portfolio (R). RESEARCH_ONLY; see ``thesis.governance``.

The optimiser's card (B, nominal bankroll) is left exactly as it was: the research layer only labels each shortlisted
bet FUNDED_RESEARCH / SHADOW_ONLY / REJECTED and attaches a research stake (0 unless FUNDED_RESEARCH).
"""

from __future__ import annotations

from dataclasses import replace
from typing import Any

import numpy as np

from nhl_edge.thesis import governance as G
from nhl_edge.thesis.fidelity import is_player_prop
from nhl_edge.thesis.joint import (
    DUPLICATIVE,
    INTENTIONAL_DIVERSIFIER,
    MOSTLY_INDEPENDENT,
    PARTIALLY_CONTRADICTORY,
    REINFORCING,
)
from nhl_edge.thesis.portfolio import PortfolioConfig, metrics, pnl

TRUST = {"EVIDENCE_STRONGER": "TRUSTED", "EVIDENCE_MIXED": "MIXED", "EVIDENCE_THIN": "MIXED", "CALIBRATION_WARNING": "WARNING"}
REL_WORD = {DUPLICATIVE: "duplicative", REINFORCING: "reinforcing", MOSTLY_INDEPENDENT: "independent", PARTIALLY_CONTRADICTORY: "contradictory",
            INTENTIONAL_DIVERSIFIER: "diversifying (independent / mildly contradictory, kept on purpose)"}


def _r(x: float | None, n: int = 4) -> float | None:
    return None if x is None else round(float(x), n)


def bet_context(a: dict[str, Any], b: Any, history: dict[str, dict[str, Any]] | None, gov: G.ResearchGovernance) -> dict[str, Any]:
    """Warning, market disagreement and corroboration for one bet side (logged for every shortlisted bet)."""
    m = b.meta
    p_v1 = m.get("p_v1")
    if p_v1 is not None and b.side == "no":
        p_v1 = 1.0 - float(p_v1)
    warn = G.calibration_warning(b.family, a["rel"][b.bet_id], a["buckets"].get(b.bet_id)) if is_player_prop(b.family) else (
        ["reliability label CALIBRATION_WARNING"] if a["rel"][b.bet_id] == "CALIBRATION_WARNING" else [])
    ctx = {"family": b.family, "side": b.side, "p_model": b.p, "p_mid": b.p_mid, "reliability": a["rel"][b.bet_id], "warning": warn, "bucket": a["buckets"].get(b.bet_id),
           "bench": a["bench"][b.bet_id], "p_v1": p_v1, "first_mid": ((history or {}).get(b.bet_id) or {}).get("first_mid"),
           **{k: m.get(k) for k in ("role_confidence", "projection_quality", "deployment_source", "uncertainty_flags", "pp_unit", "expected_toi_min")}}
    return {"warning": warn, "disagreement": G.market_disagreement(b.p, b.p_mid, b.price_cents, b.family, gov), "corroboration": G.corroboration(ctx, gov)}


def apply_research_layer(analyses: list[dict[str, Any]], games_out: list[dict[str, Any]], entries_by_game: dict[str, list[dict[str, Any]]], cfg: PortfolioConfig,
                         gov: G.ResearchGovernance, history: dict[str, dict[str, Any]] | None = None) -> dict[str, Any]:
    items: list[dict[str, Any]] = []
    for gi, a in enumerate(analyses):
        short, fB = a["portfolios"]["B"]
        a["gov_ctx"] = {b.bet_id: bet_context(a, b, history, gov) for b in short}
        for b, s in zip(short, fB):
            if s <= 0:
                continue
            c = a["gov_ctx"][b.bet_id]
            items.append({"bet_id": b.bet_id, "game_id": a["gd"].game_id, "game_order": gi, "family": b.family, "thesis": a["thesis_of"][b.bet_id], "frac": float(s),
                          "p_adj": a["econ"][b.bet_id].p_adj, "growth_bp": a["econ"][b.bet_id].growth_bp,
                          "fidelity_rank": G.fidelity_rank(a["fidelity"].get(b.bet_id, {}).get("fidelity_class")), **c})
    caps = {k: getattr(cfg, k) for k in ("max_bet_frac", "max_game_frac", "max_thesis_frac", "max_slate_frac")}
    res = G.apply(items, gov, caps)
    cfg_r = replace(cfg, bankroll=gov.research_bankroll, min_stake=1.0)
    slate_x = None
    funded_total = 0
    for a, g in zip(analyses, games_out):
        short, fB = a["portfolios"]["B"]
        replaced = {o["replaced"]: o for o in a.get("overrides") or [] if o.get("applied")}
        status: dict[str, dict[str, Any]] = {}
        for b in short:
            c = a["gov_ctx"][b.bet_id]
            if b.bet_id in res:
                r = res[b.bet_id]
            elif b.bet_id in replaced:
                r = {"status": G.REJECTED, "reasons": [f"SUPERSEDED_BY_HIGHER_FIDELITY_EXPRESSION ({replaced[b.bet_id]['selected']})"], "research_stake_dollars": 0,
                     "is_player_prop": is_player_prop(b.family)}
            else:
                r = {"status": G.SHADOW, "reasons": ["NOT_SELECTED_BY_OPTIMIZER"], "research_stake_dollars": 0, "is_player_prop": is_player_prop(b.family)}
            r.setdefault("label", r["status"] + " — " + "; ".join(x.split(" (")[0] for x in r["reasons"]) if r["reasons"] else r["status"])
            status[b.bet_id] = r | {"market_disagreement": c["disagreement"], "calibration_warning": c["warning"], "corroboration": c["corroboration"]}
        a["research"] = status
        f_r = np.array([status[b.bet_id]["research_stake_dollars"] / gov.research_bankroll for b in short]) if short else np.zeros(0)
        funded_total += int(sum(status[b.bet_id]["research_stake_dollars"] for b in short))
        dist = a["dist"]
        names = {sm["code"]: sm["name"] for sm in dist.summaries}
        g["portfolios"]["R"] = {"label": f"R: FUNDED research stakes (${gov.research_bankroll:.0f} research bankroll, whole dollars, max ${gov.max_research_stake:.0f}/bet)"} | (
            metrics(short, f_r, cfg_r, a["padj"], dist.labels, names, dist.major(), a["thesis_of"]) if short else {"n_bets": 0, "total_stake": 0.0, "expected_profit": 0.0})
        x = pnl(short, f_r, gov.research_bankroll) if short else np.zeros(a["gd"].features.n)
        slate_x = x if slate_x is None else slate_x[: len(x)] + x[: len(slate_x)]
        for e in entries_by_game.get(a["gd"].game_id, []):
            st = status[e["bet_id"]]
            e["research_governance"] = {"status": st["status"], "label": st["label"], "reasons": st["reasons"], "research_stake_dollars": st["research_stake_dollars"],
                                        "research_stake": st.get("research_stake"), "is_player_prop": st["is_player_prop"], "market_disagreement": st["market_disagreement"],
                                        "calibration_warning": st["calibration_warning"], "corroboration": st["corroboration"],
                                        "detail": st.get("governance_detail") or {}, "authority": "RESEARCH_ONLY (never placed or routed)"}
        g["research_status"] = {k: {"status": v["status"], "label": v["label"], "research_stake_dollars": v["research_stake_dollars"]} for k, v in status.items()}
        g["review"] = review_block(a, g, status)
    slate_r: dict[str, Any] = {"total_stake": funded_total, "n_funded": sum(1 for a in analyses for v in a["research"].values() if v["status"] == G.FUNDED),
                               "n_shadow_on_card": sum(1 for a in analyses for b, s in zip(*a["portfolios"]["B"]) if s > 0 and a["research"][b.bet_id]["status"] != G.FUNDED)}
    if slate_x is not None and funded_total > 0:
        q = np.percentile(slate_x, [5, 10, 50, 95])
        slate_r |= {"expected_profit": round(float(slate_x.mean()), 2), "median_profit": round(float(q[2]), 2), "p_profit": round(float((slate_x > 0).mean()), 4),
                    "p05": round(float(q[0]), 2), "p10": round(float(q[1]), 2), "p95": round(float(q[3]), 2),
                    "expected_profit_confidence_adjusted": round(sum(g["portfolios"]["R"].get("expected_profit_confidence_adjusted") or 0.0 for g in games_out), 2)}
    return {"governance_config": gov.to_dict(), "slate_portfolio_R": slate_r}


def _relations(a: dict[str, Any], bet_id: str, funded_or_card: list[str]) -> dict[str, str]:
    out = {}
    for p in a["joint"]["pairs"]:
        if bet_id in (p["a"], p["b"]):
            o = p["b"] if p["a"] == bet_id else p["a"]
            if o in funded_or_card:
                out[o] = REL_WORD.get(p["relationship"], p["relationship"].lower())
    return out


def review_block(a: dict[str, Any], g: dict[str, Any], status: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """Machine-readable CARD REVIEW for one game (the markdown shows a short summary of it)."""
    short, fB = a["portfolios"]["B"]
    on_card = [b.bet_id for b, s in zip(short, fB) if s > 0]
    scripts = [{"script": s["name"], "frequency": s["frequency"]} for s in (g.get("scripts") or [])[:3]]
    theses = []
    for k, ex in sorted(a["expressions"].items(), key=lambda kv: -max([r.get("growth_bp") or 0 for r in kv[1]["rows"] if r.get("eligible")] or [0]))[:4]:
        hf, be = ex.get("highest_fidelity"), ex.get("best_adjusted_ev")
        ov = next((o for o in a.get("overrides") or [] if o["thesis"] == k), None)
        if hf and be and hf["bet_id"] != be["bet_id"]:
            choice = ov["text"] if ov else ("the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV "
                                           "or is not more reliable / higher fidelity on the preference order")
        else:
            choice = "the highest-fidelity expression is also the best adjusted-EV expression" if hf else "no eligible expression"
        p_thesis = next((e["p"] for e in a["events"] if e["key"] == k), None)
        theses.append({"thesis": k, "label": ex["label"], "p_thesis": p_thesis, "n_expressions": ex["n_expressions"], "n_eligible": ex["n_eligible"],
                       "highest_fidelity": hf, "best_adjusted_ev": be, "same_contract": bool(hf and be and hf["bet_id"] == be["bet_id"]), "choice": choice,
                       "on_card": [b for b in on_card if a["thesis_of"].get(b) == k]})
    bets = []
    idx = {b.bet_id: b for b in short}
    for bid in on_card:
        b = idx[bid]
        st = status[bid]
        fd = a["fidelity"].get(bid) or {}
        prof = a["profiles"][bid]
        opposing = []
        if prof.get("failure_thesis"):
            ft = prof["failure_thesis"]
            opposing.append(f"failure thesis {ft['key']} (p {ft['p_thesis']}, phi {ft['phi']})")
        opposing += [f"{c['check']}: {c['detail']}" for c in st["corroboration"] if c["status"] == "FAIL" or c.get("direction") == "opposing"]
        if a["bench"][bid] == "C":
            opposing.append("sportsbook sides with Kalshi (category C)")
        cap = fd.get("thesis_capture")
        fail_text = ("cannot lose if the thesis happens (settles from it)" if fd.get("fidelity_class") == "STRUCTURAL" else
                     f"loses {100 * (1 - cap):.0f}% of the draws where the thesis happens" if cap is not None else "no single thesis (diffuse)")
        bets.append({"bet_id": bid, "expression_kind": fd.get("expression_kind"), "contract_scope": fd.get("contract_scope"), "fidelity_class": fd.get("fidelity_class"),
                     "thesis": a["thesis_of"][bid], "thesis_capture": cap, "thesis_lift": fd.get("thesis_lift"), "relation": fd.get("relation"),
                     "script_breadth_rel": (prof.get("concentration") or {}).get("breadth_rel"), "script_concentration_top2": (prof.get("concentration") or {}).get("top2"),
                     "market_disagreement_pts": st["market_disagreement"].get("abs_gap_pts"), "large_disagreement": bool(st["market_disagreement"].get("large")),
                     "family_trust": TRUST.get(a["rel"][bid], "MIXED"), "reliability_label": a["rel"][bid], "status": st["status"], "status_label": st["label"],
                     "research_stake_dollars": st["research_stake_dollars"], "fails_even_if_thesis_right": fail_text, "opposing_evidence": opposing,
                     "evidence": [G.evidence("joint_simulation_probability", value=_r(b.p)),
                                  *([G.evidence("player_toi_pp_role", pp_unit=b.meta.get("pp_unit"), expected_toi_min=b.meta.get("expected_toi_min"))]
                                    if is_player_prop(b.family) and (b.meta.get("pp_unit") or b.meta.get("expected_toi_min")) else [])],
                     "relationships": _relations(a, bid, on_card)})
    overrides = a.get("overrides") or []
    return {"top_scripts": scripts, "theses": theses, "bets": bets, "overrides": overrides,
            "summary": {"n_on_card": len(on_card), "n_funded": sum(1 for x in bets if x["status"] == G.FUNDED), "n_shadow": sum(1 for x in bets if x["status"] != G.FUNDED),
                        "n_player_props_on_card": sum(1 for x in bets if x["expression_kind"] == "FRAGILE_PLAYER"),
                        "n_large_disagreement": sum(1 for x in bets if x["large_disagreement"]), "n_overrides_applied": sum(1 for o in overrides if o.get("applied"))}}
