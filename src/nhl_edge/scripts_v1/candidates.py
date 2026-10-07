"""Research candidates (``nhl-candidates-1.0``): the thesis card's shortlist, ranked with script robustness added.

A research candidate is a bet side the existing thesis engine already shortlisted (executable, pregame, quoted from a
board that is neither stale nor crossed, positive fee-adjusted EV at the ask under the model AND under the
confidence-adjusted probability, >= 1c adjusted EV). Nothing here changes who is shortlisted, the optimiser's card,
research governance (FUNDED_RESEARCH / SHADOW_ONLY / REJECTED) or any research stake. This layer ADDS:

* script survival + robustness tier (``scripts_v1.survival``) as a new decision feature, logged with every decision so
  its value can be measured prospectively BEFORE it is ever allowed to gate funding (it does not gate anything in V1);
* a deterministic research ordering for SIFT that ranks robustness above raw edge;
* exposure groups: candidates that are secretly the same bet (DUPLICATIVE on the joint draw, or phi >= 0.50) are
  grouped and the relationship is stated in words;
* structured supporting / opposing findings and dependency flags (no raw team statistic is ever a supporting finding:
  every supporting item here is a model, simulation, availability, calibration or governance output).

Ordering key (descending, lexicographic, fixed a priori):

    1. data quality OK (executable ask, fresh, uncrossed, pregame)
    2. not REJECTED by research governance (superseded expressions sink)
    3. not FRAGILE (a fragile candidate never outranks a moderate or robust one)
    4. research score = adjusted EV (c/contract) x (0.5 + mass survived) x reliability weight x dependency factor
                        x liquidity factor x exposure factor (x 1.10 when governance FUNDED it)

so a +7c edge that survives only one narrow script ranks BELOW a +4c edge that survives most of the probability mass.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from nhl_edge.scripts_v1 import AUTHORITY, CANDIDATE_RULES_VERSION
from nhl_edge.scripts_v1.survival import FRAGILE, TIER_RANK, TIER_WORD, SideSurvival
from nhl_edge.scripts_v1.taxonomy import SCRIPTS

REL_WEIGHT = {"EVIDENCE_STRONGER": 1.0, "EVIDENCE_MIXED": 0.8, "EVIDENCE_THIN": 0.6, "CALIBRATION_WARNING": 0.4}
STATUS_RANK = {"FUNDED_RESEARCH": 3, "SHADOW_ONLY": 2, "REJECTED": 1}
FUNDED_BONUS = 1.10
WIDE_SPREAD_CENTS = 6
EXPOSURE_PHI = 0.50
REINFORCING_PHI = 0.15
GOALIE_DEPENDENT = ("game_winner", "game_spread", "game_total", "team_total", "goalie_saves", "game_overtime", "period_total", "period_winner")
STAKE_KIND = {"FUNDED_RESEARCH": "funded research stake (nominal research bankroll; never placed)", "SHADOW_ONLY": "shadow only — no stake",
              "REJECTED": "rejected — no stake"}
STATUS_WORD = {"FUNDED_RESEARCH": "Research candidate · funded research", "SHADOW_ONLY": "Research candidate · shadow only", "REJECTED": "Rejected"}

ORDERING = ("data quality OK > not REJECTED > not FRAGILE > research score; research score = adjusted EV (c) x (0.5 + mass survived) x "
            "reliability weight x dependency factor x liquidity factor x exposure factor (x1.10 if FUNDED_RESEARCH)")


def _r(x: Any, n: int = 4) -> float | None:
    return None if x is None or (isinstance(x, float) and np.isnan(x)) else round(float(x), n)


def _lc(label: str) -> str:
    """Lower-case a script label for mid-sentence use without breaking team abbreviations ("TOR controls ...")."""
    head = label.split(" ", 1)[0]
    return label if head.isupper() else label[:1].lower() + label[1:]


def dependency_flags(b: Any, ctx: dict[str, Any]) -> list[dict[str, str]]:
    """What the candidate depends on that is not yet known for sure (pregame availability / role / quote)."""
    out = []
    m = b.meta
    if b.family in GOALIE_DEPENDENT or b.family.startswith("player_"):
        for side in ("home", "away"):
            g = (ctx.get("goalies") or {}).get(side) or {}
            st = g.get("status")
            if st and st != "CONFIRMED":
                out.append({"flag": f"GOALIE_{st}_{side.upper()}", "text": f"{ctx.get(side) or side} starter {str(st).lower()}" +
                            (f" ({g.get('name')})" if g.get("name") else "")})
    if b.family.startswith("player_") or b.family in ("first_goal", "goalie_saves"):
        rc, q = m.get("role_confidence"), m.get("projection_quality")
        if rc and str(rc).upper() != "HIGH":
            out.append({"flag": "ROLE_NOT_CONFIRMED", "text": f"player role confidence {str(rc).lower()} (lines not confirmed)"})
        if q and str(q).upper() in ("LOW", "POOR", "THIN"):
            out.append({"flag": "PROJECTION_QUALITY_LOW", "text": f"projection quality {str(q).lower()}"})
    sp = m.get("spread_cents")
    if sp is not None and sp >= WIDE_SPREAD_CENTS:
        out.append({"flag": "WIDE_SPREAD", "text": f"wide quote ({int(sp)}c bid-ask spread)"})
    return out


def _findings(b: Any, e: Any, sv: SideSurvival, rs: dict[str, Any], rel: str, fid: dict[str, Any] | None, home: str, away: str,
              bench: str | None) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    sup: list[dict[str, Any]] = []
    opp: list[dict[str, Any]] = []
    if b.p_mid is not None:
        sup.append({"text": f"Model {b.p:.1%} vs market {b.p_mid:.1%} (adjusted {e.p_adj:.1%} after crediting only part of the gap)",
                    "basis": "MODEL", "source": "PLAYER_SIM_V1 joint draw vs Kalshi midpoint"})
    if sv.survives is not None:
        names = [SCRIPTS[i].name(home, away) for i in range(len(SCRIPTS)) if sv.survives[i]]
        if names:
            sup.append({"text": f"Positive after the conservative adjustment in {len(names)} script{'s' if len(names) != 1 else ''} "
                                f"({sv.mass:.0%} of simulated games): {', '.join(names[:4])}{'…' if len(names) > 4 else ''}",
                        "basis": "SIMULATION", "source": "NHL_SCRIPT_V1 script-conditioned pricing"})
    if bench in ("A", "B"):
        sup.append({"text": "Sportsbook consensus leans the model's way" if bench == "B" else "Sportsbook consensus also prices Kalshi as mispriced",
                    "basis": "MARKET", "source": "sportsbook moneyline consensus (benchmark only)"})
    if fid and fid.get("fidelity_class") in ("STRUCTURAL", "DIRECT"):
        sup.append({"text": f"Direct expression of its thesis (captures {fid.get('thesis_capture', 0):.0%} of it)" if fid.get("thesis_capture") is not None
                    else "Direct expression of its thesis", "basis": "SIMULATION", "source": "thesis.fidelity"})
    for c in rs.get("corroboration") or []:
        if c.get("status") == "PASS":
            sup.append({"text": c.get("detail") or c.get("check"), "basis": str(c.get("basis") or "GOVERNANCE"), "source": f"corroboration {c.get('check')}"})
        elif c.get("status") == "FAIL":
            opp.append({"text": c.get("detail") or c.get("check"), "basis": str(c.get("basis") or "GOVERNANCE"), "source": f"corroboration {c.get('check')}"})
    if sv.failure_script is not None and sv.ev_by_script is not None:
        s = SCRIPTS[sv.failure_script]
        opp.append({"text": f"Fails mainly if: {_lc(s.name(home, away))} (EV {sv.ev_by_script[sv.failure_script] * 100:+.0f}c per contract there)",
                    "basis": "SIMULATION", "source": "NHL_SCRIPT_V1 script-conditioned pricing"})
    md = rs.get("market_disagreement") or {}
    if md.get("large"):
        opp.append({"text": f"Large disagreement with the market ({md.get('abs_gap_pts')} pts): historically the market was closer on large gaps",
                    "basis": "CALIBRATION", "source": "thesis.expression LARGE_DISAGREEMENT cap"})
    for w in rs.get("calibration_warning") or []:
        opp.append({"text": f"Calibration warning: {w}", "basis": "CALIBRATION", "source": "thesis.reliability"})
    if fid and fid.get("fidelity_class") == "FRAGILE":
        opp.append({"text": "Fragile expression: can lose even when its thesis happens", "basis": "SIMULATION", "source": "thesis.fidelity"})
    if sv.tier == FRAGILE:
        opp.append({"text": f"Value concentrated in few scripts (survives {sv.mass:.0%} of simulated games)", "basis": "SIMULATION",
                    "source": "NHL_SCRIPT_V1 survival"})
    return sup, opp


def exposure_groups(ids: list[str], pairs: list[dict[str, Any]]) -> dict[str, str]:
    """bet_id -> group id (union-find over DUPLICATIVE / phi >= 0.50 pairs). Singletons map to themselves."""
    parent = {i: i for i in ids}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for p in pairs:
        a, b = p.get("a"), p.get("b")
        if a in parent and b in parent and (p.get("relationship") == "DUPLICATIVE" or (p.get("phi") or 0) >= EXPOSURE_PHI):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[max(ra, rb)] = min(ra, rb)
    return {i: find(i) for i in ids}


def build_candidates(a: dict[str, Any], survival: dict[str, SideSurvival], ctx: dict[str, Any]) -> list[dict[str, Any]]:
    """Research candidates of one game, ranked. ``a``: the thesis ``analyze_game`` output after ``finalize_slate`` (it
    carries ``research`` = governance status per shortlisted bet); ``ctx``: {home, away, goalies: {home/away: {status, name}}}."""
    gd = a["gd"]
    home, away = gd.home, gd.away
    short = list(a["short"])
    research = a.get("research") or {}
    pairs = (a.get("joint") or {}).get("pairs") or []
    groups = exposure_groups([b.bet_id for b in short], pairs)
    rows = []
    for b in short:
        e = a["econ"][b.bet_id]
        sv = survival[b.bet_id]
        rs = research.get(b.bet_id) or {"status": "SHADOW_ONLY", "reasons": ["NO_GOVERNANCE_RECORD"], "research_stake_dollars": 0}
        rel = a["rel"].get(b.bet_id, "EVIDENCE_THIN")
        fid = (a.get("fidelity") or {}).get(b.bet_id)
        prof = (a.get("profiles") or {}).get(b.bet_id) or {}
        deps = dependency_flags(b, ctx)
        sup, opp = _findings(b, e, sv, rs, rel, fid, home, away, a["bench"].get(b.bet_id))
        dep_factor = 0.85 ** min(len([d for d in deps if d["flag"] != "WIDE_SPREAD"]), 3)
        liq = 0.8 if any(d["flag"] == "WIDE_SPREAD" for d in deps) else 1.0
        ev_c = 100.0 * (e.ev_adj or 0.0)
        score = ev_c * (0.5 + (sv.mass or 0.0)) * REL_WEIGHT.get(rel, 0.6) * dep_factor * liq
        if rs.get("status") == "FUNDED_RESEARCH":
            score *= FUNDED_BONUS
        rows.append({"b": b, "e": e, "sv": sv, "rs": rs, "rel": rel, "fid": fid, "prof": prof, "deps": deps, "sup": sup, "opp": opp, "score": score})

    def key(r: dict[str, Any]) -> tuple:
        return (r["sv"].data_quality == "OK", r["rs"].get("status") != "REJECTED", TIER_RANK.get(r["sv"].tier, 0) > TIER_RANK[FRAGILE], r["score"],
                r["b"].bet_id)

    rows.sort(key=key, reverse=True)
    # exposure: the best-ranked member of a group leads it; the others are flagged and down-weighted, then re-sorted
    lead: dict[str, str] = {}
    for r in rows:
        g = groups[r["b"].bet_id]
        if g not in lead:
            lead[g] = r["b"].bet_id
        elif lead[g] != r["b"].bet_id:
            r["score"] *= 0.6
            r["duplicate_of"] = lead[g]
    rows.sort(key=key, reverse=True)
    pair_by = {frozenset((p["a"], p["b"])): p for p in pairs}
    out = []
    for rank, r in enumerate(rows, 1):
        b, e, sv, rs = r["b"], r["e"], r["sv"], r["rs"]
        rels = []
        for o in rows:
            ob = o["b"]
            if ob.bet_id == b.bet_id:
                continue
            p = pair_by.get(frozenset((b.bet_id, ob.bet_id)))
            if p is None:
                continue
            phi = float(p.get("phi") or 0.0)
            th = (r["prof"].get("primary_thesis") or {}).get("label")
            if p.get("relationship") == "DUPLICATIVE" or phi >= EXPOSURE_PHI:
                text = f"Highly correlated with {ob.title} {ob.side.upper()}" + (f" — same thesis: {th}" if th else "")
                kind = "SAME_EXPOSURE"
            elif phi >= REINFORCING_PHI:
                text = f"Reinforces {ob.title} {ob.side.upper()} (both win in many of the same games)"
                kind = "REINFORCING"
            elif phi <= -REINFORCING_PHI:
                text = f"Partly offsets {ob.title} {ob.side.upper()} (tends to win when it loses)"
                kind = "OFFSETTING"
            else:
                extra = []
                if sv.survives is not None and o["sv"].survives is not None:
                    extra = [SCRIPTS[i].name(home, away) for i in range(len(SCRIPTS)) if sv.survives[i] and not o["sv"].survives[i]
                             and sv.ev_by_script is not None]
                text = (f"Different expression from {ob.title} {ob.side.upper()}: survives {_lc(extra[0])}, which it does not" if extra
                        else f"Mostly independent of {ob.title} {ob.side.upper()}")
                kind = "DIFFERENT_EXPRESSION" if extra else "INDEPENDENT"
            rels.append({"bet_id": ob.bet_id, "kind": kind, "phi": round(phi, 3), "relationship": p.get("relationship"),
                         "script_overlap": p.get("script_overlap"), "text": text})
        rels.sort(key=lambda x: (-abs(x["phi"]), x["bet_id"]))
        status = rs.get("status") or "SHADOW_ONLY"
        stake = int(rs.get("research_stake_dollars") or 0) if status == "FUNDED_RESEARCH" else 0
        md = rs.get("market_disagreement") or {}
        out.append({
            "rank": rank, "bet_id": b.bet_id, "ticker": b.ticker, "side": b.side, "title": b.title, "family": b.family,
            "team": b.team, "opponent": b.opponent,
            "price": {"ask_cents": b.price_cents, "cost": _r(b.cost), "fee": _r(b.fee), "observed_at_utc": b.meta.get("market_observed_at_utc"),
                      "spread_cents": b.meta.get("spread_cents"), "data_quality": sv.data_quality},
            "p_model": _r(b.p), "p_conservative": _r(e.p_adj), "p_market_mid": _r(b.p_mid), "confidence_k": _r(e.k, 2),
            "edge_vs_mid": _r(None if b.p_mid is None else b.p - b.p_mid), "ev_raw": _r(e.ev_raw), "ev_adjusted": _r(e.ev_adj),
            "bet_up_to_cents": e.bet_up_to_adj, "bet_up_to_cents_raw": e.bet_up_to_raw,
            "uncertainty": {"confidence_k": _r(e.k, 2), "large_market_disagreement": bool(md.get("large")), "disagreement_pts": md.get("abs_gap_pts"),
                            "notes": e.notes or []},
            "survival": sv.to_dict(),
            "robustness": sv.tier, "robustness_word": TIER_WORD.get(sv.tier, sv.tier),
            "family_reliability": r["rel"], "benchmark_category": a["bench"].get(b.bet_id),
            "expression_fidelity": (r["fid"] or {}).get("fidelity_class"),
            "primary_thesis": {k: (r["prof"].get("primary_thesis") or {}).get(k) for k in ("key", "label")},
            "thesis_concentration": (r["prof"].get("concentration") or {}).get("top2"),
            "supporting": r["sup"], "opposing": r["opp"], "dependencies": r["deps"],
            "governance": {"status": status, "status_word": STATUS_WORD.get(status, status), "reasons": rs.get("reasons") or [],
                           "label": rs.get("label"), "stake_dollars": stake, "stake_kind": STAKE_KIND.get(status, "no stake")},
            "exposure_group": groups[b.bet_id], "duplicate_of": r.get("duplicate_of"), "relations": rels[:4],
            "research_score": round(r["score"], 3), "authority": AUTHORITY, "rules_version": CANDIDATE_RULES_VERSION,
        })
    return out
