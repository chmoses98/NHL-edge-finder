"""Research governance for the thesis card: which recommended bets are FUNDED (tiny real-money research stakes) and which
stay SHADOW_ONLY, and how big a funded research stake is. RESEARCH GOVERNANCE, NOT MODEL TRUTH.

Nothing here changes a model probability, the confidence-adjusted probability, the portfolio optimiser, its caps, or
what is logged prospectively. Every shortlisted decision is still logged with its full state; governance only labels it

    FUNDED_RESEARCH  on the optimiser's card, passes every governance rule, research stake >= $1
    SHADOW_ONLY      a qualifying edge kept for prospective learning with stake $0 (blocked by a rule, or not selected)
    REJECTED         not a separate edge: superseded by a higher-fidelity expression of the same thesis

and computes the research stake. Nothing in this package can place, route or size a real order: the stake is a number in
a report. NHL is in prospective validation (``docs/AUTHORITY.md``); every limit below is configurable and conservative.

Rules, in the order applied (all thresholds fixed a priori, none fitted to a slate):

1. PLAYER-PROP CALIBRATION WARNING. A player prop whose family carries a calibration warning -- the family reliability
   label CALIBRATION_WARNING, a held-out calibration bucket the bet side leans on (``bucket_flag`` against), or a
   family in ``KNOWN_CALIBRATION_CONCERNS`` (documented before the 2026-10-01 slate) -- defaults to SHADOW_ONLY unless
   it clears the stronger corroboration requirement (``warning_min_strong_passes`` STRONG corroboration passes and no
   STRONG failure other than the calibration check itself).
2. MARKET_DISAGREEMENT_REVIEW (player props). When |model - Kalshi mid| >= the family's threshold (default 10 points),
   the bet needs ``disagreement_min_strong_passes`` STRONG corroboration passes and no STRONG failure; under a
   calibration warning it needs ``disagreement_warning_min_strong_passes`` and no failure at all. Otherwise
   SHADOW_ONLY -- LARGE_MARKET_DISAGREEMENT_UNCORROBORATED. Corroboration that is not available is reported as
   UNAVAILABLE and never counted: nothing is faked.
3. At most ``max_funded_player_props_per_game`` funded player props per game (best expression fidelity, then adjusted
   growth, then bet id).
4. At most ``max_funded_low_prob_player_props_per_slate`` funded player props per slate whose confidence-adjusted
   probability is below ``low_prob_threshold`` (highest adjusted growth, then bet id).
5. Research stakes: the optimiser's bankroll fraction x ``research_bankroll``; rounded UP to a whole dollar; never above
   ``max_research_stake`` nor any existing cap (per bet / game / thesis / slate fractions, applied to the research
   bankroll). If rounding up would breach a cap, the largest whole-dollar stake under it is used; below $1 the bet is
   SHADOW_ONLY. SHADOW_ONLY and REJECTED stakes are always exactly 0.

Evidence labels (opponent adjustment). Every piece of evidence that justifies an edge carries ``basis`` and
``authority``. Only statistics that really are opponent-adjusted may be labelled OPPONENT_ADJUSTED; none of this
system's player or team rate inputs are (team ratings are exponentially weighted raw xGF/xGA per 60; player TOI / PP
TOI / shot shares are raw), so they are labelled RAW_NOT_OPPONENT_ADJUSTED, carry WEAK authority, and never count as
corroboration for a large market disagreement. The joint simulation conditions on the opponent (lambda = own offence x
opponent defence) but its inputs are raw; it is labelled MATCHUP_CONDITIONED_MODEL and it is the thing being
corroborated, not a corroborator.
"""

from __future__ import annotations

import json
import math
import os
from dataclasses import asdict, dataclass, field, replace
from typing import Any

from nhl_edge.thesis.fidelity import CLASS_RANK, is_player_prop

FUNDED = "FUNDED_RESEARCH"
SHADOW = "SHADOW_ONLY"
REJECTED = "REJECTED"

# Documented BEFORE the 2026-10-01 slate (docs/HANDOFF_PLAYER_SIM.md section X.1, 2026-09-30; docs/research/THESIS_ENGINE.md
# section 11D, 2026-10-01 06:04Z): held-out 2025-26 assists / points predictions are compressed toward the middle
# (S-shaped calibration, |z| up to 5.8). Governance-only: the model probabilities are not recalibrated.
KNOWN_CALIBRATION_CONCERNS = {
    "player_assists": "held-out 2025-26 assists 1+ calibration is S-shaped (compressed toward the middle; z up to -5.8 / +4.7): HANDOFF_PLAYER_SIM X.1",
    "player_points": "held-out 2025-26 points 1+ calibration is S-shaped (compressed toward the middle; z up to -4.7 / +4.5): HANDOFF_PLAYER_SIM X.1",
}

# ---------------------------------------------------------------------------------------------------- evidence labels
OPPONENT_ADJUSTED = "OPPONENT_ADJUSTED"
RAW = "RAW_NOT_OPPONENT_ADJUSTED"
EVIDENCE_REGISTRY: dict[str, dict[str, Any]] = {
    "joint_simulation_probability": {"basis": "MATCHUP_CONDITIONED_MODEL", "opponent_adjusted": False, "authority": "SUBJECT",
                                     "text": "PLAYER_SIM_V1 joint draw: lambda = own offence x opponent defence (matchup-conditioned), inputs RAW"},
    "team_xg_rates": {"basis": RAW, "opponent_adjusted": False, "authority": "WEAK", "text": "EW xGF/60 and xGA/60 (no strength-of-schedule adjustment)"},
    "player_toi_pp_role": {"basis": RAW, "opponent_adjusted": False, "authority": "WEAK",
                           "text": "projected TOI / PP TOI / PP unit / shot share from recent deployment (raw, not opponent-adjusted)"},
    "player_opportunity_rates": {"basis": RAW, "opponent_adjusted": False, "authority": "WEAK",
                                 "text": "player shot / point rates (raw per-60; no opponent-adjusted version exists in this system)"},
    "lineup_confirmation": {"basis": "LINEUP_FACT", "opponent_adjusted": None, "authority": "STRONG", "text": "DailyFaceoff confirmed vs projected lines"},
    "held_out_calibration": {"basis": "HELD_OUT_EVALUATION", "opponent_adjusted": None, "authority": "STRONG", "text": "2025-26 walk-forward calibration / Kalshi benchmark"},
    "data_only_v1": {"basis": "INDEPENDENT_MODEL_ARM", "opponent_adjusted": False, "authority": "STRONG", "text": "DATA_ONLY_V1 (separate model family, raw-rate inputs)"},
    "sportsbook_consensus": {"basis": "MARKET", "opponent_adjusted": None, "authority": "STRONG", "text": "de-vigged sportsbook moneyline consensus (game winner only)"},
    "kalshi_market_movement": {"basis": "MARKET", "opponent_adjusted": None, "authority": "STRONG", "text": "Kalshi midpoint movement since the first logged decision today"},
}
OPPONENT_ADJUSTED_AVAILABLE: frozenset[str] = frozenset()  # no opponent-adjusted statistic exists in this system yet


def evidence(name: str, **detail: Any) -> dict[str, Any]:
    """A labelled evidence item. Raises on an unregistered name so no statistic enters the card unlabelled."""
    reg = EVIDENCE_REGISTRY[name]
    adj = name in OPPONENT_ADJUSTED_AVAILABLE
    basis = OPPONENT_ADJUSTED if adj else reg["basis"]
    authority = reg["authority"] if basis != RAW else "WEAK"
    return {"evidence": name, "basis": basis, "opponent_adjusted": adj if reg["opponent_adjusted"] is not None else None,
            "label": "OPPONENT-ADJUSTED" if adj else ("RAW / NOT OPPONENT ADJUSTED" if basis == RAW else basis), "authority": authority, "source": reg["text"]} | detail


# ----------------------------------------------------------------------------------------------------------- config
@dataclass(frozen=True)
class ResearchGovernance:
    research_bankroll: float = 250.0
    max_research_stake: float = 5.0
    max_funded_player_props_per_game: int = 1
    max_funded_low_prob_player_props_per_slate: int = 2
    low_prob_threshold: float = 0.30
    disagreement_threshold: float = 0.10
    disagreement_threshold_by_family: dict[str, float] = field(default_factory=dict)
    disagreement_min_strong_passes: int = 2
    disagreement_warning_min_strong_passes: int = 3
    warning_min_strong_passes: int = 2
    market_move_min: float = 0.02  # Kalshi mid must move >= 2 points toward / away from the model to count either way
    label: str = "RESEARCH GOVERNANCE (not model truth): limits on FUNDED research stakes; shadow logging is unaffected"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def threshold_for(self, family: str) -> float:
        return float(self.disagreement_threshold_by_family.get(family, self.disagreement_threshold))


def governance_config() -> ResearchGovernance:
    """Defaults, overridable by ``NHL_EDGE_RESEARCH_BANKROLL``, ``NHL_EDGE_RESEARCH_MAX_STAKE`` and a JSON object in
    ``NHL_EDGE_RESEARCH_GOVERNANCE`` (any field). A malformed override is ignored (defaults are the safe side)."""
    g = ResearchGovernance()
    over: dict[str, Any] = {}
    for env, key in (("NHL_EDGE_RESEARCH_BANKROLL", "research_bankroll"), ("NHL_EDGE_RESEARCH_MAX_STAKE", "max_research_stake")):
        try:
            v = float(os.environ[env])
            if v > 0:
                over[key] = v
        except (KeyError, ValueError):
            pass
    try:
        j = json.loads(os.environ.get("NHL_EDGE_RESEARCH_GOVERNANCE") or "{}")
        if isinstance(j, dict):
            over |= {k: v for k, v in j.items() if k in ResearchGovernance.__dataclass_fields__ and k != "label"}
    except json.JSONDecodeError:
        pass
    try:
        return replace(g, **over)
    except TypeError:
        return g


# ------------------------------------------------------------------------------------------------- disagreement gate
def market_disagreement(p_model: float, p_mid: float | None, price_cents: float | None, family: str, gov: ResearchGovernance) -> dict[str, Any]:
    ref = p_mid if p_mid is not None else (None if price_cents is None else price_cents / 100.0)
    if ref is None:
        return {"reference": None, "gap": None, "abs_gap_pts": None, "threshold_pts": round(100 * gov.threshold_for(family), 1), "large": False,
                "note": "no market reference"}
    gap = p_model - ref
    thr = gov.threshold_for(family)
    return {"reference": "kalshi_mid" if p_mid is not None else "executable_ask", "p_market": round(ref, 4), "gap": round(gap, 4),
            "abs_gap_pts": round(100 * abs(gap), 1), "threshold_pts": round(100 * thr, 1), "large": abs(gap) >= thr - 1e-12}


def calibration_warning(family: str, reliability_label: str, bucket: dict[str, Any] | None) -> list[str]:
    out = []
    if reliability_label == "CALIBRATION_WARNING":
        out.append("reliability label CALIBRATION_WARNING")
    if bucket and bucket.get("against_measured_bias"):
        out.append(f"held-out bucket {bucket.get('bucket')} bias (z {bucket.get('z')}) is the side this bet relies on")
    if family in KNOWN_CALIBRATION_CONCERNS:
        out.append(KNOWN_CALIBRATION_CONCERNS[family])
    return out


def _check(name: str, ev: str, status: str, detail: str, direction: str | None = None) -> dict[str, Any]:
    e = evidence(ev)
    return {"check": name, "status": status, "detail": detail, "direction": direction, **{k: e[k] for k in ("evidence", "basis", "label", "authority", "opponent_adjusted")}}


def corroboration(ctx: dict[str, Any], gov: ResearchGovernance) -> list[dict[str, Any]]:
    """Independent evidence for (or against) the model's disagreement with the market, per bet side.

    ``ctx`` keys: family, side, p_model, p_mid, reliability, warning (list), bucket, bench (A-D), p_v1 (prob of THIS side
    or None), first_mid (earliest logged Kalshi mid of this side today, or None), role_confidence, projection_quality,
    deployment_source, uncertainty_flags, pp_unit, expected_toi_min. Status: PASS | FAIL | NEUTRAL | UNAVAILABLE."""
    fam, side = ctx["family"], ctx["side"]
    p, mid = float(ctx["p_model"]), ctx.get("p_mid")
    out: list[dict[str, Any]] = []
    player = is_player_prop(fam)
    toward = None if mid is None else (1.0 if p > mid else -1.0)
    # 1. lineup / role confirmation (a fact about the inputs, not a statistic)
    if player:
        rc, q, src = ctx.get("role_confidence"), ctx.get("projection_quality"), ctx.get("deployment_source")
        flags = set(ctx.get("uncertainty_flags") or [])
        if rc is None and src is None:
            out.append(_check("CONFIRMED_LINEUP_ROLE", "lineup_confirmation", "UNAVAILABLE", "no deployment metadata for this contract"))
        elif rc == "HIGH" and src == "LINES_CONFIRMED" and not (flags & {"NEW_TEAM", "SMALL_SAMPLE", "NO_HISTORY", "PRIOR_HEAVY"}):
            out.append(_check("CONFIRMED_LINEUP_ROLE", "lineup_confirmation", "PASS", f"confirmed lines, role confidence HIGH, quality {q}"))
        elif rc == "LOW" or q in ("DEGRADED_ROLE", "PRIOR_HEAVY"):
            out.append(_check("CONFIRMED_LINEUP_ROLE", "lineup_confirmation", "FAIL", f"role confidence {rc}, quality {q}, flags {sorted(flags)}"))
        else:
            out.append(_check("CONFIRMED_LINEUP_ROLE", "lineup_confirmation", "NEUTRAL", f"{src or 'unknown source'}: role confidence {rc} (lines not confirmed)"))
    # 2. family calibration quality (held-out evaluation)
    if ctx.get("warning"):
        out.append(_check("FAMILY_CALIBRATION_QUALITY", "held_out_calibration", "FAIL", "; ".join(ctx["warning"])))
    elif ctx.get("reliability") == "EVIDENCE_STRONGER":
        out.append(_check("FAMILY_CALIBRATION_QUALITY", "held_out_calibration", "PASS", "family EVIDENCE_STRONGER (held-out calibrated and ties/beats the Kalshi mid)"))
    else:
        out.append(_check("FAMILY_CALIBRATION_QUALITY", "held_out_calibration", "NEUTRAL", f"family {ctx.get('reliability')} (not STRONGER)"))
    # 3. an independent model arm
    if player:
        out.append(_check("INDEPENDENT_ARM_AGREEMENT", "data_only_v1", "UNAVAILABLE",
                          "no independent player-model arm (MARKET_ANCHORED_PLAYER_V1 is anchored to the market; PLAYER_SIM_V1 is the model itself)"))
    elif ctx.get("p_v1") is None or mid is None:
        out.append(_check("INDEPENDENT_ARM_AGREEMENT", "data_only_v1", "UNAVAILABLE", "no DATA_ONLY_V1 probability for this contract"))
    else:
        v1 = float(ctx["p_v1"])
        if (v1 - mid) * toward >= 0.5 * abs(p - mid):
            out.append(_check("INDEPENDENT_ARM_AGREEMENT", "data_only_v1", "PASS", f"DATA_ONLY_V1 {v1:.3f} is on the model's side of the mid {mid:.3f}"))
        elif (v1 - mid) * toward < 0:
            out.append(_check("INDEPENDENT_ARM_AGREEMENT", "data_only_v1", "FAIL", f"DATA_ONLY_V1 {v1:.3f} sides with the market (mid {mid:.3f})"))
        else:
            out.append(_check("INDEPENDENT_ARM_AGREEMENT", "data_only_v1", "NEUTRAL", f"DATA_ONLY_V1 {v1:.3f} only partly agrees (mid {mid:.3f})"))
    # 4. sportsbook consensus (moneylines only)
    bench = ctx.get("bench")
    if bench in ("A", "B"):
        out.append(_check("SPORTSBOOK_AGREEMENT", "sportsbook_consensus", "PASS", f"category {bench}"))
    elif bench == "C":
        out.append(_check("SPORTSBOOK_AGREEMENT", "sportsbook_consensus", "FAIL", "category C: the sportsbook sides with Kalshi"))
    else:
        out.append(_check("SPORTSBOOK_AGREEMENT", "sportsbook_consensus", "UNAVAILABLE", "no sportsbook price for this family"))
    # 5. Kalshi market movement since the first logged decision today
    fm = ctx.get("first_mid")
    if fm is None or mid is None:
        out.append(_check("MARKET_MOVEMENT_TOWARD_MODEL", "kalshi_market_movement", "UNAVAILABLE", "no earlier logged Kalshi mid for this side today"))
    else:
        mv = (mid - float(fm)) * toward
        st = "PASS" if mv >= gov.market_move_min else "FAIL" if mv <= -gov.market_move_min else "NEUTRAL"
        out.append(_check("MARKET_MOVEMENT_TOWARD_MODEL", "kalshi_market_movement", st, f"mid {float(fm):.3f} -> {mid:.3f} ({100 * mv:+.1f} pts toward the model)"))
    # 6. opponent-adjusted opportunity (does not exist here: never faked)
    if player:
        out.append(_check("OPPONENT_ADJUSTED_OPPORTUNITY", "player_opportunity_rates", "UNAVAILABLE",
                          "no opponent-adjusted player opportunity rates exist in this system; raw rates cannot corroborate"))
        # 7. raw role statistics: reported for direction only, WEAK authority, never counted
        pp, toi = ctx.get("pp_unit"), ctx.get("expected_toi_min")
        if pp is not None or toi is not None:
            usage_high = (pp == "pp1") or (toi is not None and float(toi) >= 18.0)
            scoring = fam in ("player_goals", "player_assists", "player_points", "first_goal")
            if scoring:
                consistent = usage_high == (side == "yes")
                out.append(_check("RAW_ROLE_USAGE", "player_toi_pp_role", "NEUTRAL",
                                  f"PP unit {pp}, projected TOI {toi} min: {'consistent with' if consistent else 'opposes'} the {side.upper()} side "
                                  "(RAW / NOT OPPONENT ADJUSTED: reported, never counted)", "consistent" if consistent else "opposing"))
    return out


def corroboration_summary(checks: list[dict[str, Any]], exclude: tuple[str, ...] = ()) -> dict[str, Any]:
    strong = [c for c in checks if c["authority"] == "STRONG" and c["check"] not in exclude]
    return {"strong_passes": [c["check"] for c in strong if c["status"] == "PASS"], "strong_failures": [c["check"] for c in strong if c["status"] == "FAIL"],
            "any_failures": [c["check"] for c in checks if c["status"] == "FAIL" and c["check"] not in exclude],
            "unavailable": [c["check"] for c in checks if c["status"] == "UNAVAILABLE"]}


# ---------------------------------------------------------------------------------------------------- rule application
def gate_player_prop(item: dict[str, Any], gov: ResearchGovernance) -> tuple[bool, list[str], dict[str, Any]]:
    """Rules 1-2 for one player prop. Returns (fundable, reason codes, review detail)."""
    warn = item["warning"]
    dis = item["disagreement"]
    checks = item["corroboration"]
    reasons: list[str] = []
    s_all = corroboration_summary(checks, exclude=("FAMILY_CALIBRATION_QUALITY",) if warn else ())
    detail = {"calibration_warning": warn, "market_disagreement_review": bool(dis.get("large")), "corroboration_summary": s_all}
    if warn and (len(s_all["strong_passes"]) < gov.warning_min_strong_passes or s_all["strong_failures"]):
        reasons.append("CALIBRATION_WARNING_UNCORROBORATED")
    if dis.get("large"):
        need = gov.disagreement_warning_min_strong_passes if warn else gov.disagreement_min_strong_passes
        veto = s_all["any_failures"] if warn else s_all["strong_failures"]
        detail["required_strong_passes"] = need
        if len(s_all["strong_passes"]) < need or veto:
            reasons.append("LARGE_MARKET_DISAGREEMENT_UNCORROBORATED")
    return not reasons, reasons, detail


def research_stakes(items: list[dict[str, Any]], gov: ResearchGovernance, caps: dict[str, float]) -> dict[str, dict[str, Any]]:
    """Whole-dollar research stakes for fundable items ({bet_id, game_id, thesis, frac}, in deterministic order).

    raw = frac x research bankroll; stake = ceil(raw), then lowered to the largest whole dollar that keeps EVERY cap:
    max_research_stake, per-bet / game / thesis / slate fractions of the research bankroll. A stake below $1 is 0."""
    B = gov.research_bankroll
    per_bet = min(gov.max_research_stake, caps["max_bet_frac"] * B)
    game_left: dict[str, float] = {}
    thesis_left: dict[tuple[str, str], float] = {}
    slate_left = caps["max_slate_frac"] * B
    out: dict[str, dict[str, Any]] = {}
    for it in items:
        raw = max(0.0, float(it["frac"])) * B
        g, t = it["game_id"], (it["game_id"], it["thesis"])
        gl = game_left.setdefault(g, caps["max_game_frac"] * B)
        tl = thesis_left.setdefault(t, caps["max_thesis_frac"] * B)
        limit = math.floor(min(per_bet, gl, tl, slate_left) + 1e-9)
        up = math.ceil(raw - 1e-9) if raw > 0 else 0
        stake = min(up, limit) if raw > 0 else 0
        stake = stake if stake >= 1 else 0
        why = "rounded up to a whole dollar" if stake == up else f"rounding up to ${up} would breach a cap; largest valid whole-dollar stake ${stake}"
        if stake:
            game_left[g] = gl - stake
            thesis_left[t] = tl - stake
            slate_left -= stake
        out[it["bet_id"]] = {"raw_dollars": round(raw, 4), "stake_dollars": int(stake), "cap_dollars": int(limit), "rounding": why if stake else
                             "no whole-dollar stake fits under the caps (or the optimiser stake is 0)"}
    return out


def apply(items: list[dict[str, Any]], gov: ResearchGovernance, caps: dict[str, float]) -> dict[str, dict[str, Any]]:
    """Statuses + research stakes for the optimiser's recommended bets of a whole slate.

    ``items`` (one per recommended bet, in card order): bet_id, game_id, family, thesis, frac (optimiser stake as a
    bankroll fraction), p_adj, growth_bp, fidelity_rank, warning, disagreement, corroboration."""
    res: dict[str, dict[str, Any]] = {}
    fundable: list[dict[str, Any]] = []
    for it in items:
        r = {"status": None, "reasons": [], "is_player_prop": is_player_prop(it["family"]), "governance_detail": {}}
        if r["is_player_prop"]:
            ok, reasons, detail = gate_player_prop(it, gov)
            r["reasons"] += reasons
            r["governance_detail"] = detail
            if not ok:
                r["status"] = SHADOW
        res[it["bet_id"]] = r
        if r["status"] is None:
            fundable.append(it)
    # rule 3: per-game player-prop cap
    by_game: dict[str, list[dict[str, Any]]] = {}
    for it in fundable:
        if is_player_prop(it["family"]):
            by_game.setdefault(it["game_id"], []).append(it)
    for _g, its in by_game.items():
        its.sort(key=lambda x: (-x["fidelity_rank"], -(x["growth_bp"] or 0.0), x["bet_id"]))
        for x in its[gov.max_funded_player_props_per_game:]:
            res[x["bet_id"]]["status"] = SHADOW
            res[x["bet_id"]]["reasons"].append(f"PLAYER_PROP_GAME_CAP (max {gov.max_funded_player_props_per_game} funded player prop per game; kept {its[0]['bet_id']})")
    fundable = [it for it in fundable if res[it["bet_id"]]["status"] is None]
    # rule 4: slate cap on low-probability player props
    low = sorted([it for it in fundable if is_player_prop(it["family"]) and float(it["p_adj"]) < gov.low_prob_threshold],
                 key=lambda x: (-(x["growth_bp"] or 0.0), x["bet_id"]))
    for x in low[gov.max_funded_low_prob_player_props_per_slate:]:
        res[x["bet_id"]]["status"] = SHADOW
        res[x["bet_id"]]["reasons"].append(f"LOW_PROB_PLAYER_PROP_SLATE_CAP (max {gov.max_funded_low_prob_player_props_per_slate} funded player props with "
                                           f"adjusted p < {gov.low_prob_threshold:.2f} per slate)")
    fundable = [it for it in fundable if res[it["bet_id"]]["status"] is None]
    # rule 5: research stakes (deterministic order: card order is game order, then the optimiser's stake, then bet id)
    order = sorted(fundable, key=lambda x: (x["game_order"], -float(x["frac"]), x["bet_id"]))
    stakes = research_stakes(order, gov, caps)
    for it in items:
        r = res[it["bet_id"]]
        st = stakes.get(it["bet_id"])
        r["research_stake"] = st or {"raw_dollars": round(float(it["frac"]) * gov.research_bankroll, 4), "stake_dollars": 0, "rounding": "not fundable"}
        if r["status"] is None:
            if st and st["stake_dollars"] >= 1:
                r["status"] = FUNDED
            else:
                r["status"] = SHADOW
                r["reasons"].append("RESEARCH_STAKE_ZERO_UNDER_CAPS")
        if r["status"] != FUNDED:
            r["research_stake"]["stake_dollars"] = 0
        r["research_stake_dollars"] = int(r["research_stake"]["stake_dollars"])
        r["label"] = r["status"] + ("" if not r["reasons"] else " — " + "; ".join(x.split(" (")[0] for x in r["reasons"]))
    return res


def fidelity_rank(cls: str | None) -> int:
    return CLASS_RANK.get(cls or "NONE", 0)
