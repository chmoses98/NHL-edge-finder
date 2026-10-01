"""Thesis-card engine: one game's joint draw -> scripts -> thesis mapping -> expressions -> joint matrix -> portfolio,
then the slate -> card entries -> completion gate. Pure functions over in-memory draws (IO lives in
``workflows/thesis_card.py``), so every step is testable on synthetic draws.

Performance shape (``docs/research/THESIS_ENGINE.md`` section 8): the full board (every priced contract, both sides) is
mapped with matrix products (bets x draws @ draws x scripts / events) -- no market is hidden or capped; only the
shortlist of eligible candidates (positive raw AND confidence-adjusted EV, executable, pregame) gets pairwise joint
analysis and portfolio optimisation, so nothing is O(N^2) over the 2,000+ market board.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any

import numpy as np

from nhl_edge.thesis import CARD_VERSION, PORTFOLIO_VERSION, THESIS_VERSION
from nhl_edge.thesis.benchmark import CATEGORY_TEXT, book_probability, categorize
from nhl_edge.thesis.card import not_applicable, run_gate, unknown
from nhl_edge.thesis.events import thesis_events
from nhl_edge.thesis.expression import Econ, compare_expressions, economics, why_chosen
from nhl_edge.thesis.features import DrawFeatures
from nhl_edge.thesis.joint import (
    DUPLICATIVE,
    INTENTIONAL_DIVERSIFIER,
    MOSTLY_INDEPENDENT,
    PARTIALLY_CONTRADICTORY,
    joint_matrix,
)
from nhl_edge.thesis.mapping import Bet, EventMatrix, associations, concentration, script_counts, thesis_profile
from nhl_edge.thesis.portfolio import (
    PortfolioConfig,
    independent_stakes,
    log_growth,
    metrics,
    pair_is_diversifier,
    pnl,
    returns,
    select_and_optimize,
)
from nhl_edge.thesis.reliability import THIN, WARNING, bucket_flag, bucket_tables
from nhl_edge.thesis.scripts import build_distribution

SHORTLIST_MAX = 40  # per game; pairwise / portfolio work only. The full board is always mapped and reported.
DIVERSIFIER_MAX_PHI = -0.05
DIVERSIFIER_MAX_OVERLAP = 0.50


@dataclass
class GameDistribution:
    game_id: str
    home: str
    away: str
    home_team_id: int
    away_team_id: int
    features: DrawFeatures
    bets: list[Bet]  # both sides of every contract that has a simulated outcome
    unpriced: list[dict[str, Any]] = field(default_factory=list)  # contracts with no outcome vector, with the reason
    player_points: dict[str, np.ndarray] = field(default_factory=dict)  # top players' 1+ point indicators (script involvement)
    meta: dict[str, Any] = field(default_factory=dict)


def _r(x: float | None, n: int = 4) -> float | None:
    return None if x is None else round(float(x), n)


def analyze_game(gd: GameDistribution, reliability: dict[str, dict[str, Any]], consensus: dict[str, Any] | None, cfg: PortfolioConfig) -> dict[str, Any]:
    t = {"start": time.perf_counter()}
    f = gd.features
    dist = build_distribution(f, gd.player_points)
    em = EventMatrix.build(thesis_events(f))
    t["scripts"] = time.perf_counter()
    bets = gd.bets
    Y = np.stack([b.y for b in bets]) if bets else np.zeros((0, f.n), bool)
    counts = script_counts(Y, dist)
    PHI, PAB, _ = associations(Y, em) if len(bets) else (np.zeros((0, len(em.events))), np.zeros((0, len(em.events))), None)
    rel = {b.bet_id: (reliability.get(b.family) or {}).get("label", THIN) for b in bets}
    tables = bucket_tables()
    buckets: dict[str, dict[str, Any] | None] = {}
    bench, book = {}, {}
    econ: dict[str, Econ] = {}
    for b in bets:
        bf = bucket_flag(tables, b.family, b.meta.get("threshold"), b.p if b.side == "yes" else 1.0 - b.p, b.side)
        buckets[b.bet_id] = bf
        if bf and bf["against_measured_bias"]:
            rel[b.bet_id] = WARNING  # per-bet: this side relies on a measured held-out calibration bias
        bp = book_probability(b, consensus, gd.home)
        book[b.bet_id] = bp
        bench[b.bet_id] = categorize(b.p, b.p_mid, b.cost, bp)
        econ[b.bet_id] = economics(b, rel[b.bet_id], bench[b.bet_id], min_ev_adj=cfg.min_ev_adjusted)
    conc = {b.bet_id: concentration(counts[i], dist.freq) for i, b in enumerate(bets)}
    idx = {b.bet_id: i for i, b in enumerate(bets)}
    t["mapping"] = time.perf_counter()
    # ---- full board (one row per contract; both sides' economics) -------------------------------------------
    board = []
    for i, b in enumerate(bets):
        if b.side != "yes":
            continue
        j = int(np.argmax(PHI[i])) if PHI.shape[1] else None
        no = idx.get(f"{b.ticker}|no")
        top_s = int(np.argmax(counts[i])) if counts[i].sum() else None
        board.append({"ticker": b.ticker, "title": b.title, "family": b.family, "p_yes": _r(b.p), "p_mid_yes": _r(b.p_mid),
                      "yes_ask": b.price_cents, "no_ask": bets[no].price_cents if no is not None else None,
                      "ev_yes_raw": _r(econ[b.bet_id].ev_raw), "ev_yes_adj": _r(econ[b.bet_id].ev_adj),
                      "ev_no_raw": _r(econ[bets[no].bet_id].ev_raw) if no is not None else None, "ev_no_adj": _r(econ[bets[no].bet_id].ev_adj) if no is not None else None,
                      "yes_primary_thesis": em.events[j].key if j is not None and PHI[i, j] >= 0.10 else "DIFFUSE", "yes_thesis_phi": _r(PHI[i, j], 3) if j is not None else None,
                      "yes_top_script": dist.taxonomy.primary_key(top_s) if top_s is not None else None, "yes_concentration_top2": conc[b.bet_id]["top2"],
                      "yes_breadth_rel": conc[b.bet_id]["breadth_rel"], "reliability": rel[b.bet_id], "benchmark": bench[b.bet_id]})
    # ---- candidates and shortlist ------------------------------------------------------------------------------
    cands = [b for b in bets if econ[b.bet_id].eligible]
    cands.sort(key=lambda b: -(econ[b.bet_id].growth_bp or 0))
    # equivalent contracts (identical settlement on every draw, e.g. "NYI wins" YES and "TOR wins" NO): keep the best
    seen_y: dict[bytes, str] = {}
    equivalents = []
    uniq = []
    for b in cands:
        key = np.packbits(b.y).tobytes()
        if key in seen_y:
            equivalents.append({"kept": seen_y[key], "dropped": b.bet_id, "reason": "identical settlement on every draw; the better-priced expression is kept"})
            continue
        seen_y[key] = b.bet_id
        uniq.append(b)
    cands = uniq
    short = cands[:SHORTLIST_MAX]
    profiles = {b.bet_id: thesis_profile(idx[b.bet_id], b, counts, dist, em, PHI, PAB) for b in short}
    thesis_of = {}
    for b in short:
        k = profiles[b.bet_id]["primary_thesis"]["key"]
        thesis_of[b.bet_id] = k if k != "DIFFUSE" else f"DIFFUSE:{b.bet_id}"
    # ---- expression comparison per thesis -----------------------------------------------------------------------
    expressions = {}
    for k in dict.fromkeys(v for v in thesis_of.values() if not v.startswith("DIFFUSE:")):
        j = em.index(k)
        col = {b.bet_id: float(PHI[i, j]) for i, b in enumerate(bets)}
        pe = float(em.p[j])
        purity = {b.bet_id: _r(PAB[i, j] / b.p) if b.p > 0 else None for i, b in enumerate(bets)}
        cond = {b.bet_id: _r(PAB[i, j] / pe) if pe > 0 else None for i, b in enumerate(bets)}
        expressions[k] = compare_expressions(k, em.events[j].label, bets, econ, col, purity, cond, conc, rel, bench)
    t["expressions"] = time.perf_counter()
    # ---- joint matrix + portfolios --------------------------------------------------------------------------------
    joint = joint_matrix(short, counts[[idx[b.bet_id] for b in short]] if short else None)
    dup = [(p["a"], p["b"]) for p in joint["pairs"] if p["relationship"] == DUPLICATIVE]
    t["joint"] = time.perf_counter()
    padj = {b.bet_id: econ[b.bet_id].p_adj for b in bets}
    fB, selection = select_and_optimize(short, padj, thesis_of, dup, cfg)
    best_ids = {e["best"] for e in expressions.values() if e.get("best")} | {b.bet_id for b in short if thesis_of[b.bet_id].startswith("DIFFUSE:")}
    c_bets = [b for b in short if b.bet_id in best_ids]
    fC, _ = select_and_optimize(c_bets, padj, thesis_of, dup, cfg)
    a_n = max(3, int((fB > 0).sum()))
    a_bets = sorted(cands, key=lambda b: -(econ[b.bet_id].ev_raw or 0))[:a_n]
    fA = independent_stakes(a_bets, cfg)
    t["portfolio"] = time.perf_counter()
    timings = {k: round(1000 * (t[k] - t[p]), 1) for p, k in zip(["start", "scripts", "mapping", "expressions", "joint"], ["scripts", "mapping", "expressions", "joint", "portfolio"])}
    events_out = [{"key": e.key, "label": e.label, "category": e.category, "p": _r(e.p)} for e in em.events]
    return {"gd": gd, "dist": dist, "em": em, "bets": bets, "idx": idx, "econ": econ, "rel": rel, "bench": bench, "book": book, "conc": conc, "profiles": profiles,
            "thesis_of": thesis_of, "expressions": expressions, "joint": joint, "dup": dup, "padj": padj, "short": short, "candidates": cands,
            "portfolios": {"A": (a_bets, fA), "B": (short, fB), "C": (c_bets, fC)}, "board": board, "events": events_out, "timings_ms": timings,
            "consensus": consensus, "counts": counts, "reliability": reliability, "buckets": buckets, "equivalents": equivalents, "selection": selection}


def _stake_fraction_total(analyses: list[dict[str, Any]], key: str) -> float:
    return float(sum(a["portfolios"][key][1].sum() for a in analyses))


def finalize_slate(analyses: list[dict[str, Any]], cfg: PortfolioConfig, reliability: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """Slate cap, card entries, pairwise labels, portfolio comparisons, completeness gate."""
    for key in ("A", "B", "C"):
        tot = _stake_fraction_total(analyses, key)
        if tot > cfg.max_slate_frac:
            for a in analyses:
                bets, f = a["portfolios"][key]
                f = f * (cfg.max_slate_frac / tot)
                f[f * cfg.bankroll < cfg.min_stake] = 0.0
                a["portfolios"][key] = (bets, f)
    games_out, entries_by_game, joints, slate_pnl = [], {}, {}, {"A": None, "B": None, "C": None}
    for a in analyses:
        gd: GameDistribution = a["gd"]
        dist = a["dist"]
        names = {s["code"]: s["name"] for s in dist.summaries}
        major = dist.major()
        comp = {}
        for key, label in (("A", "A: highest individual edges (independent stakes)"), ("B", "B: thesis-diversified +EV set (joint optimum)"),
                           ("C", "C: one best expression per thesis (joint optimum)")):
            bets, f = a["portfolios"][key]
            comp[key] = {"label": label} | metrics(bets, f, cfg, a["padj"], dist.labels, names, major, a["thesis_of"])
            x = pnl(bets, f, cfg.bankroll) if len(bets) else np.zeros(gd.features.n)
            slate_pnl[key] = x if slate_pnl[key] is None else slate_pnl[key][: len(x)] + x[: len(slate_pnl[key])]
        short, fB = a["portfolios"]["B"]
        recs = [(b, s) for b, s in zip(short, fB) if s > 0]
        rec_ids = [b.bet_id for b, _ in recs]
        pair_by = {frozenset((p["a"], p["b"])): p for p in a["joint"]["pairs"]}
        for i in range(len(recs)):
            for j in range(i + 1, len(recs)):
                p = pair_by[frozenset((recs[i][0].bet_id, recs[j][0].bet_id))]
                if p["relationship"] in (MOSTLY_INDEPENDENT, PARTIALLY_CONTRADICTORY) and (p["phi"] <= DIVERSIFIER_MAX_PHI or (p.get("script_overlap") or 1) <= DIVERSIFIER_MAX_OVERLAP):
                    ok, info = pair_is_diversifier(recs[i][0], recs[j][0], a["padj"], cfg)
                    p["diversifier_test"] = info
                    if ok:
                        p["base_relationship"] = p["relationship"]
                        p["relationship"] = INTENTIONAL_DIVERSIFIER
        rec_joint = {"bets": rec_ids, "pairs": [pair_by[frozenset((rec_ids[i], rec_ids[j]))] for i in range(len(rec_ids)) for j in range(i + 1, len(rec_ids))]}
        joints[gd.game_id] = rec_joint
        entries = [card_entry(a, b, s, recs, rec_joint, cfg) for b, s in recs]
        entries_by_game[gd.game_id] = entries
        games_out.append({
            "game_id": gd.game_id, "matchup": f"{gd.away} @ {gd.home}", "meta": {k: v for k, v in gd.meta.items() if not k.startswith("_")},
            "n_sims": gd.features.n, "scripts": dist.summaries, "dimensions": dist.dims, "thesis_events": a["events"],
            "sportsbook_consensus": a["consensus"], "full_board": a["board"], "unpriced_contracts": gd.unpriced,
            "n_bets_mapped": len(a["bets"]), "n_candidates": len(a["candidates"]), "n_shortlisted": len(short),
            "candidates_not_shortlisted": [b.bet_id for b in a["candidates"][SHORTLIST_MAX:]],
            "expressions": a["expressions"], "equivalent_contracts": a["equivalents"], "greedy_selection": a["selection"], "joint_matrix_shortlist": a["joint"], "joint_card_check": rec_joint, "portfolios": comp,
            "card": entries, "timings_ms": a["timings_ms"],
        })
    gate = run_gate(entries_by_game, joints)
    slate = {}
    for key in ("A", "B", "C"):
        x = slate_pnl[key]
        tot = sum(g["portfolios"][key].get("total_stake", 0) for g in games_out)
        if x is None or tot <= 0:
            slate[key] = {"total_stake": round(tot, 2), "expected_profit": 0.0}
            continue
        q = np.percentile(x, [5, 10, 25, 50, 75, 95])
        slate[key] = {"total_stake": round(tot, 2), "expected_profit": round(float(x.mean()), 2), "median_profit": round(float(q[3]), 2),
                      "p_profit": round(float((x > 0).mean()), 4), "p05": round(float(q[0]), 2), "p10": round(float(q[1]), 2), "p25": round(float(q[2]), 2),
                      "p95": round(float(q[5]), 2), "expected_log_growth_bp": round(1e4 * float(np.mean(np.log(np.maximum(1 + x / cfg.bankroll, 1e-12)))), 3),
                      "note": "games are independent simulations; slate P/L sums per-game draws"}
    n_rec = sum(len(e) for e in entries_by_game.values())
    status = "NO_BETS" if n_rec == 0 and gate["status"] == "PASS" else ("COMPLETE" if gate["status"] == "PASS" else "INCOMPLETE")
    return {"thesis_version": THESIS_VERSION, "card_version": CARD_VERSION, "portfolio_version": PORTFOLIO_VERSION, "authority": "RESEARCH_ONLY",
            "status": status, "card_emitted": status == "COMPLETE", "gate": gate, "portfolio_config": cfg.to_dict(), "reliability": reliability,
            "slate_portfolios": slate, "recommended_portfolio": "B", "games": games_out,
            "note": ("RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV "
                     "at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes.")}


def card_entry(a: dict[str, Any], b: Bet, stake_frac: float, recs: list[tuple[Bet, float]], rec_joint: dict[str, Any], cfg: PortfolioConfig) -> dict[str, Any]:
    gd: GameDistribution = a["gd"]
    e: Econ = a["econ"][b.bet_id]
    prof = a["profiles"][b.bet_id]
    thesis = a["thesis_of"][b.bet_id]
    stake = stake_frac * cfg.bankroll
    # best alternative from the primary thesis's comparison table
    exp = a["expressions"].get(thesis)
    alt, self_row = None, None
    if exp:
        self_row = next((r for r in exp["rows"] if r["bet_id"] == b.bet_id), None)
        alt = next((r for r in exp["rows"] if r["bet_id"] != b.bet_id and r["eligible"]), None) or next((r for r in exp["rows"] if r["bet_id"] != b.bet_id), None)
    if self_row is None:
        self_row = {"bet_id": b.bet_id, "growth_bp": e.growth_bp, "ev_raw": e.ev_raw, "reliability": a["rel"][b.bet_id], "breadth_rel": a["conc"][b.bet_id]["breadth_rel"], "eligible": True}
    if alt is not None:
        best_alt = {k: alt.get(k) for k in ("bet_id", "title", "price_cents", "p_model", "p_adjusted", "ev_raw", "ev_adjusted", "growth_bp", "thesis_fit_phi", "reliability",
                                            "breadth_rel", "eligible", "reasons")}
        reason = why_chosen(self_row, alt)
    elif thesis.startswith("DIFFUSE:"):
        best_alt = not_applicable("diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of")
        reason = "diffuse script dependence; chosen on its own confidence-adjusted growth"
    else:
        best_alt = not_applicable("no other contract in this game expresses this thesis (phi >= 0.20)")
        reason = "only expression of its thesis on the board"
    # relationships to every other same-game recommended bet
    pairs = {frozenset((p["a"], p["b"])): p for p in rec_joint["pairs"]}
    rel_out: dict[str, Any] = {}
    for o, _ in recs:
        if o.bet_id == b.bet_id:
            continue
        p = pairs.get(frozenset((b.bet_id, o.bet_id)))
        if p is None:
            rel_out[o.bet_id] = unknown("pair missing from the joint matrix")
            continue
        mine_first = p["a"] == b.bet_id
        rel_out[o.bet_id] = {"relationship": p["relationship"], "phi": p["phi"], "p_both": p["p_a_and_b"], "p_both_lose": p["p_both_lose"],
                             "p_this_given_other": p["p_a_given_b"] if mine_first else p["p_b_given_a"], "p_other_given_this": p["p_b_given_a"] if mine_first else p["p_a_given_b"],
                             "script_overlap": p.get("script_overlap")}
    if not rel_out:
        rel_out = not_applicable("only recommended bet in this game")
    game_stake = sum(s for _, s in recs) * cfg.bankroll
    th_stake = sum(s for o, s in recs if a["thesis_of"].get(o.bet_id) == thesis) * cfg.bankroll
    dup_ids = {x for pr in a["dup"] if b.bet_id in pr for x in pr} - {b.bet_id}
    # portfolio impact: the game portfolio with and without this bet (other stakes held)
    short, fB = a["portfolios"]["B"]
    k = next(i for i, x in enumerate(short) if x.bet_id == b.bet_id)
    R = returns(short)
    f_wo = fB.copy()
    f_wo[k] = 0.0
    x_w, x_wo = cfg.bankroll * (R @ fB), cfg.bankroll * (R @ f_wo)
    impact = {"marginal_expected_profit": round(float(x_w.mean() - x_wo.mean()), 2),
              "marginal_log_growth_bp": round(1e4 * (log_growth(R, fB) - log_growth(R, f_wo)), 3),
              "delta_p_profit": round(float((x_w > 0).mean() - ((x_wo > 0).mean() if f_wo.any() else 0.0)), 4),
              "delta_p10": round(float(np.percentile(x_w, 10) - np.percentile(x_wo, 10)), 2)}
    fails = prof.get("failure_thesis")
    is_player = b.family.startswith(("player_", "first_goal", "goalie_"))
    failure = {"p_lose": round(1 - b.p, 4), "failure_thesis": fails, "worst_major_script": prof.get("worst_major_script"),
               "scripts_needed": [s["script"] for s in prof["main_scripts"][:2]],
               "note": ("conditional on the player playing / goalie starting (Kalshi settles a no-show at the pre-game fair price); "
                        if is_player else "") + f"loses {100 * (1 - b.p):.0f}% of simulated games"}
    rel_info = a["rel"][b.bet_id]
    return {
        "bet_id": b.bet_id, "game_id": gd.game_id,
        "contract": {"ticker": b.ticker, "title": b.title, "side": b.side.upper(), "family": b.family},
        "team_opponent": {"team": b.team or "GAME (no single team)", "opponent": b.opponent or "-", "matchup": f"{gd.away} @ {gd.home}"},
        "executable_price": {"ask_cents": b.price_cents, "fee_per_contract": _r(b.fee), "cost_per_contract": _r(b.cost), "observed_at_utc": b.meta.get("market_observed_at_utc")}
        if b.price_cents is not None else unknown("no executable ask"),
        "fair_probability": {"p_model_joint_draw": _r(b.p), "p_confidence_adjusted": _r(e.p_adj), "confidence_k": e.k, "confidence_notes": e.notes or [],
                             "projection": {k: b.meta.get(k) for k in ("projection_quality", "uncertainty_flags", "role_confidence", "deployment_source") if b.meta.get(k) is not None},
                             "p_kalshi_mid": _r(b.p_mid),
                             "p_v1": _r(b.meta.get("p_v1")), "p_sportsbook": _r(a["book"].get(b.bet_id))},
        "estimated_edge": {"ev_raw_per_contract": _r(e.ev_raw), "ev_adjusted_per_contract": _r(e.ev_adj), "roi_adjusted": _r(e.roi_adj), "growth_bp": _r(e.growth_bp, 3)},
        "bet_up_to_price": {"cents_raw": e.bet_up_to_raw, "cents_adjusted": e.bet_up_to_adj} if e.bet_up_to_adj is not None else unknown("no price is +EV under the adjusted probability"),
        "recommended_stake": {"dollars": round(stake, 2), "fraction_of_bankroll": round(stake_frac, 5), "contracts": round(stake / b.cost, 2) if b.cost else None,
                              "nominal_bankroll": cfg.bankroll, "authority": "RESEARCH_ONLY (suggestion; never placed or routed)"},
        "family_reliability": {"label": rel_info, "family_label": (a["reliability"].get(b.family) or {}).get("label", THIN),
                               "family_evidence": (a["reliability"].get(b.family) or {}).get("evidence", "no evaluation artifact"),
                               "flags": (a["reliability"].get(b.family) or {}).get("flags", []),
                               "bucket_calibration": a["buckets"].get(b.bet_id) or "no held-out bucket table for this family / threshold",
                               "benchmark_category": a["bench"][b.bet_id], "benchmark_meaning": CATEGORY_TEXT[a["bench"][b.bet_id]]},
        "primary_thesis": prof["primary_thesis"],
        "secondary_thesis": prof["secondary_thesis"] or not_applicable("no second thesis of a different category with phi >= 0.10"),
        "best_alternative": best_alt, "reason_chosen": reason,
        "thesis_concentration": {**prof["concentration"], "main_scripts": prof["main_scripts"], "other_scripts_pp": prof["other_scripts_pp"],
                                 **({"team_offense": prof["team_offense"]} if prof.get("team_offense") else {})},
        "same_game_relationships": rel_out,
        "same_game_exposure": {"dollars": round(game_stake, 2), "fraction_of_bankroll": round(game_stake / cfg.bankroll, 5), "cap_fraction": cfg.max_game_frac},
        "thesis_exposure": {"thesis": thesis, "dollars": round(th_stake, 2), "fraction_of_bankroll": round(th_stake / cfg.bankroll, 5), "cap_fraction": cfg.max_thesis_frac,
                            "duplicative_with": sorted(dup_ids)},
        "portfolio_impact": impact, "failure_case": failure,
    }


def audit_card(analyses: list[dict[str, Any]], proposals: list[dict[str, Any]], cfg: PortfolioConfig, reliability: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """Run the thesis analysis, joint card check and completion gate on a PROPOSED card (e.g. bets a person placed or is
    about to place), at the proposal's own prices and stakes. ``proposals``: [{bet_id, stake_dollars, price_cents?}].
    Proposed bets are evaluated as they are -- including any that are -EV -- so the audit can say so explicitly."""
    from dataclasses import replace

    from nhl_edge.kalshi.fees import DEFAULT_SCHEDULE, fee_per_contract_dollars

    by_game: dict[str, list[dict[str, Any]]] = {}
    missing = []
    for pr in proposals:
        hit = next((a for a in analyses if pr["bet_id"] in a["idx"]), None)
        if hit is None:
            missing.append({"bet_id": pr["bet_id"], "reason": "no simulated outcome for this contract side on the analysed slate (unsupported, unpriced or not joined)"})
            continue
        by_game.setdefault(hit["gd"].game_id, []).append(pr)
    games, entries_by_game, joints = [], {}, {}
    for a0 in analyses:
        props = by_game.get(a0["gd"].game_id)
        if not props:
            continue
        a = dict(a0)
        a["econ"], a["profiles"], a["thesis_of"] = dict(a0["econ"]), dict(a0["profiles"]), dict(a0["thesis_of"])
        bets, stakes = [], []
        dist, em = a["dist"], a["em"]
        Y = np.stack([b.y for b in a["bets"]])
        PHI, PAB, _ = associations(Y, em)
        for pr in props:
            b0 = a["bets"][a["idx"][pr["bet_id"]]]
            price = pr.get("price_cents") or b0.price_cents
            sched = b0.meta.get("_schedule") or DEFAULT_SCHEDULE
            b = replace(b0, price_cents=int(round(price)), fee=fee_per_contract_dollars(price, sched)) if price is not None else b0
            bets.append(b)
            stakes.append(float(pr.get("stake_dollars") or 0.0) / cfg.bankroll)
            a["econ"][b.bet_id] = economics(b, a["rel"][b.bet_id], a["bench"][b.bet_id], min_ev_adj=0.0)
            if b.bet_id not in a["profiles"]:
                a["profiles"][b.bet_id] = thesis_profile(a["idx"][b.bet_id], b, a["counts"], dist, em, PHI, PAB)
                k = a["profiles"][b.bet_id]["primary_thesis"]["key"]
                a["thesis_of"][b.bet_id] = k if k != "DIFFUSE" else f"DIFFUSE:{b.bet_id}"
        f = np.asarray(stakes)
        a["portfolios"] = dict(a0["portfolios"]) | {"B": (bets, f)}
        jm = joint_matrix(bets, a["counts"][[a["idx"][b.bet_id] for b in bets]])
        a["dup"] = [(p["a"], p["b"]) for p in jm["pairs"] if p["relationship"] == DUPLICATIVE]
        recs = list(zip(bets, f))
        joints[a["gd"].game_id] = jm
        entries = [card_entry(a, b, s, recs, jm, cfg) for b, s in recs]
        engine_recs = {b.bet_id for b, s in zip(*a0["portfolios"]["B"]) if s > 0}
        equiv = {q["dropped"]: q["kept"] for q in a0.get("equivalents") or []}
        for e in entries:
            ec = a["econ"][e["bet_id"]]
            e["audit"] = {"positive_ev_raw": bool((ec.ev_raw or 0) > 0), "positive_ev_adjusted": bool((ec.ev_adj or 0) > 0),
                          "engine_would_recommend": e["bet_id"] in engine_recs or equiv.get(e["bet_id"]) in engine_recs,
                          "equivalent_engine_contract": equiv.get(e["bet_id"]), "violates_principle_1": not bool((ec.ev_raw or 0) > 0)}
        entries_by_game[a["gd"].game_id] = entries
        names = {s["code"]: s["name"] for s in dist.summaries}
        games.append({"game_id": a["gd"].game_id, "matchup": f"{a['gd'].away} @ {a['gd'].home}", "entries": entries, "joint_matrix": jm,
                      "proposed_portfolio": metrics(bets, f, cfg, a["padj"], dist.labels, names, dist.major(), a["thesis_of"]),
                      "engine_portfolio_B": metrics(*a0["portfolios"]["B"], cfg, a0["padj"], dist.labels, names, dist.major(), a0["thesis_of"])})
    gate = run_gate(entries_by_game, joints)
    neg = [e["bet_id"] for g in games for e in g["entries"] if e["audit"]["violates_principle_1"]]
    neg_adj = [e["bet_id"] for g in games for e in g["entries"] if not e["audit"]["positive_ev_adjusted"]]
    if neg:
        verdict = "FAILS: contains bets that are -EV at their executed price under the model"
    elif gate["status"] != "PASS" or missing:
        verdict = "INCOMPLETE"
    elif neg_adj:
        verdict = f"PASSES the completeness / joint check, but {len(neg_adj)} bet(s) are -EV after the confidence adjustment at the executed price (an engine card would not include them)"
    else:
        verdict = "PASSES the completeness / joint check"
    return {"authority": "RESEARCH_ONLY", "gate": gate, "games": games, "missing": missing, "negative_ev_bets": neg, "negative_adjusted_ev_bets": neg_adj, "verdict": verdict}
