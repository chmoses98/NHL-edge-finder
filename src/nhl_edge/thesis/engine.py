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
from nhl_edge.thesis.expression import FIT_MIN, Econ, compare_expressions, economics, why_chosen
from nhl_edge.thesis.features import DrawFeatures
from nhl_edge.thesis.fidelity import CLASS_RANK, fidelity
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
    optimize_game,
    pair_is_diversifier,
    pnl,
    returns,
    select_and_optimize,
)
from nhl_edge.thesis.reliability import MIXED, STRONGER, THIN, WARNING, bucket_flag, bucket_tables
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
    n_draws = f.n
    CNT = np.rint(PAB * n_draws).astype(np.int64) if len(bets) else np.zeros((0, len(em.events)), np.int64)
    n_ev = np.rint(em.p * n_draws).astype(np.int64)

    def fid(b: Bet, key: str | None) -> dict[str, Any]:
        j = em.index(key) if key and key != "DIFFUSE" else None
        i = idx[b.bet_id]
        if j is None:
            return fidelity(n_draws, int(round(b.p * n_draws)), 0, 0, b.family, None)
        return fidelity(n_draws, int(round(b.p * n_draws)), int(n_ev[j]), int(CNT[i, j]), b.family, key)

    fidel: dict[str, dict[str, Any]] = {}
    for b in short:
        k = profiles[b.bet_id]["primary_thesis"]["key"]
        thesis_of[b.bet_id] = k if k != "DIFFUSE" else f"DIFFUSE:{b.bet_id}"
        fidel[b.bet_id] = fid(b, k)
        profiles[b.bet_id]["expression_fidelity"] = fidel[b.bet_id]
    # ---- expression comparison per thesis -----------------------------------------------------------------------
    expressions = {}
    for k in dict.fromkeys(v for v in thesis_of.values() if not v.startswith("DIFFUSE:")):
        j = em.index(k)
        col = {b.bet_id: float(PHI[i, j]) for i, b in enumerate(bets)}
        pe = float(em.p[j])
        purity = {b.bet_id: _r(PAB[i, j] / b.p) if b.p > 0 else None for i, b in enumerate(bets)}
        cond = {b.bet_id: _r(PAB[i, j] / pe) if pe > 0 else None for i, b in enumerate(bets)}
        ex = compare_expressions(k, em.events[j].label, bets, econ, col, purity, cond, conc, rel, bench)
        by_id = {b.bet_id: b for b in bets}
        for r in ex["rows"]:
            fr = fid(by_id[r["bet_id"]], k)
            r.update({x: fr[x] for x in ("fidelity_class", "thesis_capture", "p_bet_given_not_thesis", "thesis_lift", "relation", "contract_scope", "expression_kind")})
        elig = [b for b in bets if econ[b.bet_id].eligible and col.get(b.bet_id, 0.0) >= FIT_MIN]
        if elig:
            fe = {b.bet_id: fid(b, k) for b in elig}
            hf = max(elig, key=lambda b: (CLASS_RANK[fe[b.bet_id]["fidelity_class"]], fe[b.bet_id]["thesis_capture"] or 0.0, econ[b.bet_id].ev_adj or 0.0, b.bet_id))
            be = max(elig, key=lambda b: (econ[b.bet_id].ev_adj or 0.0, b.bet_id))
            ex["highest_fidelity"] = {"bet_id": hf.bet_id, **{x: fe[hf.bet_id][x] for x in ("fidelity_class", "thesis_capture", "contract_scope")},
                                      "ev_adjusted": _r(econ[hf.bet_id].ev_adj)}
            ex["best_adjusted_ev"] = {"bet_id": be.bet_id, **{x: fe[be.bet_id][x] for x in ("fidelity_class", "thesis_capture", "contract_scope")},
                                      "ev_adjusted": _r(econ[be.bet_id].ev_adj)}
            ex["fidelity_and_ev_agree"] = hf.bet_id == be.bet_id
        expressions[k] = ex
    t["expressions"] = time.perf_counter()
    # ---- joint matrix + portfolios --------------------------------------------------------------------------------
    joint = joint_matrix(short, counts[[idx[b.bet_id] for b in short]] if short else None)
    dup = [(p["a"], p["b"]) for p in joint["pairs"] if p["relationship"] == DUPLICATIVE]
    t["joint"] = time.perf_counter()
    padj = {b.bet_id: econ[b.bet_id].p_adj for b in bets}
    fB, selection = select_and_optimize(short, padj, thesis_of, dup, cfg)
    fB, overrides = prefer_expressions(short, fB, econ, rel, fid, thesis_of, dup, padj, PHI, em, idx, reliability, cfg)
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
            "consensus": consensus, "counts": counts, "reliability": reliability, "buckets": buckets, "equivalents": equivalents, "selection": selection,
            "fidelity": fidel, "overrides": overrides}


# ------------------------------------------------------------------------------------------- expression preference
# When two expressions of one thesis offer similar confidence-adjusted value, prefer the one that more directly cashes
# when the thesis happens. "Similar" = the alternative's adjusted EV per contract is no more than ONE PRICE TICK (1c =
# 1 probability point) below the incumbent's: differences smaller than a tick are inside execution noise. The preference
# is lexicographic and fixed a priori (docs/research/THESIS_ENGINE.md section 15):
#   1. positive confidence-adjusted EV at the executable ask (mandatory: only eligible candidates are considered)
#   2. market-family reliability (EVIDENCE_STRONGER > MIXED > THIN > CALIBRATION_WARNING, per bet incl. bucket warnings)
#   3. expression fidelity to the thesis (STRUCTURAL > DIRECT > FRAGILE)
#   4. prospective calibration evidence (no SMALL_PROSPECTIVE_SAMPLE flag > flag)
#   5. joint portfolio contribution (the swap is re-optimised jointly and must keep a stake)
#   6. adjusted expected growth
#   7. executable spread (narrower first)
# An override happens only when the alternative is strictly better on 2 or 3 (reliability, then fidelity); ties on both
# leave the optimiser's choice alone. Nothing is forced: a broad market that is not +EV after adjustment never enters.
SIMILAR_EDGE = 0.01
REL_TIER = {STRONGER: 3, MIXED: 2, THIN: 1, WARNING: 0}


def _pref_key(b: Bet, econ: dict[str, Econ], rel: dict[str, str], fid_b: dict[str, Any], reliability: dict[str, dict[str, Any]]) -> tuple:
    fl = (reliability.get(b.family) or {}).get("flags") or []
    return (REL_TIER.get(rel.get(b.bet_id, THIN), 1), CLASS_RANK.get(fid_b["fidelity_class"], 0), 0 if "SMALL_PROSPECTIVE_SAMPLE" in fl else 1,
            econ[b.bet_id].growth_bp or 0.0, -(b.meta.get("spread_cents") or 99), b.bet_id)


def _kind_text(kind: str, family: str) -> str:
    return {"BROAD": "broad", "FRAGILE_PLAYER": "goalie prop" if family == "goalie_saves" else "player prop"}.get(kind, family)


def prefer_expressions(short: list[Bet], fB: np.ndarray, econ: dict[str, Econ], rel: dict[str, str], fid_fn: Any, thesis_of: dict[str, str],
                       dup: list[tuple[str, str]], padj: dict[str, float], PHI: np.ndarray, em: Any, idx: dict[str, int], reliability: dict[str, dict[str, Any]],
                       cfg: PortfolioConfig) -> tuple[np.ndarray, list[dict[str, Any]]]:
    """Swap a recommended bet for a higher-fidelity (or more reliable) expression of the SAME thesis when their adjusted
    value is similar; every swap is re-optimised jointly and documented. Returns (stakes aligned with ``short``, log)."""
    fB = np.asarray(fB, dtype=float).copy()
    log: list[dict[str, Any]] = []
    pos = {b.bet_id: i for i, b in enumerate(short)}
    considered: set[str] = set()
    order = sorted([i for i in range(len(short)) if fB[i] > 0], key=lambda i: (-fB[i], short[i].bet_id))
    for i in order:
        b = short[i]
        if fB[i] <= 0 or b.bet_id in considered:
            continue
        considered.add(b.bet_id)
        T = thesis_of.get(b.bet_id, "")
        if T.startswith("DIFFUSE"):
            continue
        j = em.index(T)
        if j is None:
            continue
        fi = fid_fn(b, T)
        kb = _pref_key(b, econ, rel, fi, reliability)
        e_b = econ[b.bet_id].ev_adj or 0.0
        alts = []
        for a in short:
            k = pos[a.bet_id]
            if fB[k] > 0 or a.bet_id == b.bet_id or a.bet_id in considered or PHI[idx[a.bet_id], j] < FIT_MIN:
                continue
            if (econ[a.bet_id].ev_adj or 0.0) < e_b - SIMILAR_EDGE - 1e-12:
                continue
            fa_ = fid_fn(a, T)
            ka = _pref_key(a, econ, rel, fa_, reliability)
            if ka[:2] > kb[:2]:
                alts.append((ka, a, fa_))
        if not alts:
            continue
        alts.sort(key=lambda x: x[0], reverse=True)
        a, fa = alts[0][1], alts[0][2]
        chosen = [k for k in range(len(short)) if fB[k] > 0 and k != i] + [pos[a.bet_id]]
        sub = [short[k] for k in chosen]
        f_sub = optimize_game(sub, padj, thesis_of, dup, cfg)
        d_pts = 100.0 * ((econ[a.bet_id].ev_adj or 0.0) - e_b)
        ka = alts[0][0]
        basis = "family reliability" if ka[0] > kb[0] else "expression fidelity"
        diff_txt = f"differs by only {abs(d_pts):.1f} pts" if d_pts < 0 else f"is {d_pts:.1f} pts higher"
        text = (f"{_kind_text(fa['expression_kind'], a.family).capitalize()} expression {a.bet_id} selected over {_kind_text(fi['expression_kind'], b.family)} "
                f"{b.bet_id} because adjusted EV {diff_txt} while thesis capture is {fa['thesis_capture'] or 0:.2f} vs {fi['thesis_capture'] or 0:.2f} "
                f"({fa['fidelity_class']} vs {fi['fidelity_class']}; reliability {rel.get(a.bet_id)} vs {rel.get(b.bet_id)}; decided on {basis})")
        rec = {"thesis": T, "replaced": b.bet_id, "selected": a.bet_id, "ev_adjusted_replaced": _r(e_b), "ev_adjusted_selected": _r(econ[a.bet_id].ev_adj),
               "edge_difference_pts": round(d_pts, 2), "thesis_capture_replaced": fi["thesis_capture"], "thesis_capture_selected": fa["thesis_capture"],
               "fidelity_replaced": fi["fidelity_class"], "fidelity_selected": fa["fidelity_class"], "reliability_replaced": rel.get(b.bet_id),
               "reliability_selected": rel.get(a.bet_id), "growth_bp_replaced": _r(econ[b.bet_id].growth_bp, 3), "growth_bp_selected": _r(econ[a.bet_id].growth_bp, 3),
               "decided_on": basis, "rule": f"similar adjusted value (within {100 * SIMILAR_EDGE:.0f} pt) -> prefer reliability, then fidelity"}
        ka_pos = chosen.index(pos[a.bet_id])
        if f_sub[ka_pos] <= 0:
            log.append(rec | {"applied": False, "text": f"override declined: the joint re-optimisation gives {a.bet_id} less than the minimum stake; {b.bet_id} kept"})
            continue
        fB[:] = 0.0
        for k, fk in zip(chosen, f_sub):
            fB[k] = fk
        considered.add(a.bet_id)
        log.append(rec | {"applied": True, "text": text})
    return fB, log


def _stake_fraction_total(analyses: list[dict[str, Any]], key: str) -> float:
    return float(sum(a["portfolios"][key][1].sum() for a in analyses))


def finalize_slate(analyses: list[dict[str, Any]], cfg: PortfolioConfig, reliability: dict[str, dict[str, Any]], gov: Any = None,
                   history: dict[str, dict[str, Any]] | None = None) -> dict[str, Any]:
    """Slate cap, card entries, pairwise labels, portfolio comparisons, research governance + stakes, completeness gate.

    ``gov``: :class:`thesis.governance.ResearchGovernance` (default from the environment); ``history``: bet_id ->
    {first_mid} from decisions logged earlier today (point-in-time, for the market-movement corroboration check)."""
    from nhl_edge.thesis.governance import governance_config
    from nhl_edge.thesis.research_layer import apply_research_layer

    gov = gov or governance_config()
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
    research = apply_research_layer(analyses, games_out, entries_by_game, cfg, gov, history)
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
                      "adjusted_log_growth_bp_sum_of_games": round(sum(g["portfolios"][key].get("adjusted_log_growth_bp") or 0.0 for g in games_out), 3),
                      "expected_profit_confidence_adjusted": round(sum(g["portfolios"][key].get("expected_profit_confidence_adjusted") or 0.0 for g in games_out), 2),
                      "note": "games are independent simulations; slate P/L sums per-game draws; adjusted growth is the optimiser's objective (sum over games)"}
    n_rec = sum(len(e) for e in entries_by_game.values())
    status = "NO_BETS" if n_rec == 0 and gate["status"] == "PASS" else ("COMPLETE" if gate["status"] == "PASS" else "INCOMPLETE")
    return {"thesis_version": THESIS_VERSION, "card_version": CARD_VERSION, "portfolio_version": PORTFOLIO_VERSION, "authority": "RESEARCH_ONLY",
            "status": status, "card_emitted": status == "COMPLETE", "gate": gate, "portfolio_config": cfg.to_dict(), "reliability": reliability,
            "slate_portfolios": slate | {"R": research["slate_portfolio_R"]}, "recommended_portfolio": "B", "games": games_out,
            "research_governance": research["governance_config"],
            "note": ("RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research "
                     "stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the "
                     "confidence-adjusted probability; the card is emitted only when the completion gate passes.")}


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
        on_card = any(o.bet_id == alt["bet_id"] for o, _ in recs)
        ph_alt = None
        if alt["bet_id"] in a["idx"]:
            ya, yb = a["bets"][a["idx"][alt["bet_id"]]].y, b.y
            pa_, pb_, pab_ = float(ya.mean()), float(yb.mean()), float((ya & yb).mean())
            den = (pa_ * (1 - pa_) * pb_ * (1 - pb_)) ** 0.5
            ph_alt = (pab_ - pa_ * pb_) / den if den > 0 else None
        reason = why_chosen(self_row, alt, on_card, ph_alt)
        ov = next((o for o in a.get("overrides") or [] if o.get("selected") == b.bet_id and o.get("applied")), None)
        if ov:
            reason = ov["text"]
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
        "expression_fidelity": prof.get("expression_fidelity") or not_applicable("no fidelity computed (audit of a proposed bet)"),
        "selection_override": next((o for o in a.get("overrides") or [] if o.get("selected") == b.bet_id and o.get("applied")), None),
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
            b = replace(b0, price_cents=float(price), fee=fee_per_contract_dollars(price, sched)) if price is not None else b0  # executed prices may be fractional
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
