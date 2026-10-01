"""Research-only portfolio construction on the simulated joint P/L distribution.

Every bet's per-draw settlement comes from the same joint draw, so a portfolio is evaluated DIRECTLY, never under an
independence assumption:

    profit_draw = sum_k  stake_k * (settle_k(draw) - cost_k) / cost_k        (cost = executable ask + Kalshi fee)

Objective: maximise expected log bankroll growth (Kelly) of the game's portfolio on those draws, then scale by the
fractional-Kelly multiplier. That is expected-return maximisation that accounts for joint outcomes: duplicative bets
end up sharing stake, a negatively related +EV pair is rewarded for lowering variance, and a -EV bet can only reduce
growth (it is excluded upstream anyway: only bets with positive raw AND confidence-adjusted EV are candidates, so no
negative-EV hedge can ever be inserted). It does NOT maximise P(profit).

Conservatism: the optimiser sees each bet's return with its EV haircut to the CONFIDENCE-ADJUSTED probability
(``p_adj``, shrunk toward the Kalshi midpoint by the family's evidence; ``thesis.expression``) -- implemented as an
extra per-contract cost ``p - p_adj`` so the joint dependence structure is untouched.

Constraints (fractions of the nominal bankroll, applied to the final fractional stakes): per bet, per game, per thesis
(bets sharing a primary thesis, or linked by a DUPLICATIVE relationship, share one budget) and per slate.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

import numpy as np

from nhl_edge.thesis.mapping import Bet


@dataclass(frozen=True)
class PortfolioConfig:
    bankroll: float = 1000.0  # nominal research bankroll; stakes are suggestions, never orders
    kelly_multiplier: float = 0.25
    max_bet_frac: float = 0.02
    max_game_frac: float = 0.05
    max_thesis_frac: float = 0.03
    max_slate_frac: float = 0.15
    min_stake: float = 1.0  # dollars: smaller optimal stakes are reported as 0 (not recommended)
    min_ev_adjusted: float = 0.01  # dollars per contract after fees AND the confidence haircut: a candidate floor for model error
    max_bets_per_game: int = 4  # card practicality: greedy selection by marginal (adjusted) log growth when the optimum spreads wider
    loss_frac: float = 0.50  # report P(losing more than this share of the game's allocation)
    iters: int = 400

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def returns(bets: list[Bet], p_adj: dict[str, float] | None = None) -> np.ndarray:
    """(n_draws, n_bets) return per $1 staked; with ``p_adj`` the EV is haircut to the adjusted probability."""
    if not bets:
        return np.zeros((0, 0))
    cols = []
    for b in bets:
        c = float(b.cost)
        delta = 0.0 if p_adj is None else max(0.0, b.p - float(p_adj.get(b.bet_id, b.p)))
        cols.append((b.y.astype(float) - c - delta) / c)
    return np.stack(cols, axis=1)


def _project(f: np.ndarray, bet_cap: float, groups: list[tuple[np.ndarray, float]]) -> np.ndarray:
    f = np.clip(f, 0.0, bet_cap)
    for _ in range(4):
        ok = True
        for idx, cap in groups:
            s = f[idx].sum()
            if s > cap + 1e-12:
                f[idx] *= cap / s
                ok = False
        if ok:
            break
    return f


def kelly_optimize(R: np.ndarray, bet_cap: float, groups: list[tuple[np.ndarray, float]], iters: int = 400) -> np.ndarray:
    """Maximise mean(log(1 + R f)) subject to 0 <= f <= bet_cap and sum(f[group]) <= cap (projected damped
    diagonal-Newton ascent). Caps here are on the FULL-Kelly scale."""
    k = R.shape[1] if R.ndim == 2 else 0
    if k == 0:
        return np.zeros(0)
    f = np.zeros(k)
    for _ in range(iters):
        w = 1.0 + R @ f
        w = np.maximum(w, 1e-9)
        g = (R / w[:, None]).mean(axis=0)
        h = ((R / w[:, None]) ** 2).mean(axis=0) + 1e-9
        step = 0.7 * g / h
        f_new = _project(f + step, bet_cap, groups)
        if np.max(np.abs(f_new - f)) < 1e-7:
            f = f_new
            break
        f = f_new
    return f


def log_growth(R: np.ndarray, f: np.ndarray) -> float:
    if R.size == 0 or not len(f):
        return 0.0
    return float(np.mean(np.log(np.maximum(1.0 + R @ f, 1e-12))))


def exposure_groups(bets: list[Bet], thesis_of: dict[str, str], duplicative: list[tuple[str, str]], cfg: PortfolioConfig,
                    scale: float) -> list[tuple[np.ndarray, float]]:
    """Game cap over all bets, thesis caps over bets sharing a primary thesis, and duplicative clusters (union-find)."""
    idx = {b.bet_id: i for i, b in enumerate(bets)}
    groups: list[tuple[np.ndarray, float]] = [(np.arange(len(bets)), cfg.max_game_frac * scale)]
    by_thesis: dict[str, list[int]] = {}
    for b in bets:
        by_thesis.setdefault(thesis_of.get(b.bet_id, b.bet_id), []).append(idx[b.bet_id])
    parent = list(range(len(bets)))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in duplicative:
        if a in idx and b in idx:
            parent[find(idx[a])] = find(idx[b])
    # a thesis budget also covers everything duplicative with any of its bets
    for members in by_thesis.values():
        for m in members[1:]:
            parent[find(m)] = find(members[0])
    clusters: dict[int, list[int]] = {}
    for i in range(len(bets)):
        clusters.setdefault(find(i), []).append(i)
    for members in clusters.values():
        if len(members) > 1:
            groups.append((np.asarray(members), cfg.max_thesis_frac * scale))
    return groups


def optimize_game(bets: list[Bet], p_adj: dict[str, float], thesis_of: dict[str, str], duplicative: list[tuple[str, str]],
                  cfg: PortfolioConfig) -> np.ndarray:
    """Final fractional stakes (fractions of bankroll) for one game's candidate bets."""
    if not bets:
        return np.zeros(0)
    km = cfg.kelly_multiplier
    R = returns(bets, p_adj)
    groups = exposure_groups(bets, thesis_of, duplicative, cfg, 1.0 / km)
    f = kelly_optimize(R, cfg.max_bet_frac / km, groups, cfg.iters) * km
    f[f * cfg.bankroll < cfg.min_stake] = 0.0
    return f


def select_and_optimize(bets: list[Bet], p_adj: dict[str, float], thesis_of: dict[str, str], duplicative: list[tuple[str, str]],
                        cfg: PortfolioConfig) -> tuple[np.ndarray, list[dict[str, Any]]]:
    """Joint optimum; if it spreads over more than ``max_bets_per_game`` bets, forward-select (greedy) the subset with the
    largest adjusted log growth, re-optimised jointly at every step. Returns (stakes aligned with ``bets``, selection log)."""
    f_all = optimize_game(bets, p_adj, thesis_of, duplicative, cfg)
    pos = [i for i in range(len(bets)) if f_all[i] > 0]
    if len(pos) <= cfg.max_bets_per_game:
        return f_all, []
    R_all = returns(bets, p_adj)
    chosen: list[int] = []
    g_cur = 0.0
    trail = []
    while len(chosen) < cfg.max_bets_per_game:
        best = None
        for i in pos:
            if i in chosen:
                continue
            sub = chosen + [i]
            f = optimize_game([bets[j] for j in sub], p_adj, thesis_of, duplicative, cfg)
            g = log_growth(R_all[:, sub], f)
            if best is None or g > best[1]:
                best = (i, g)
        if best is None or best[1] - g_cur < 1e-7:
            break
        chosen.append(best[0])
        trail.append({"added": bets[best[0]].bet_id, "adjusted_log_growth_bp": round(1e4 * best[1], 3), "marginal_bp": round(1e4 * (best[1] - g_cur), 3)})
        g_cur = best[1]
    out = np.zeros(len(bets))
    if chosen:
        out[chosen] = optimize_game([bets[j] for j in chosen], p_adj, thesis_of, duplicative, cfg)
    return out, trail


def independent_stakes(bets: list[Bet], cfg: PortfolioConfig) -> np.ndarray:
    """The contract-centric baseline: each bet at its own fractional Kelly (raw model p), capped per bet, then the game
    cap applied proportionally. No joint information, no thesis budget."""
    f = np.array([max(0.0, (b.p - b.cost) / (1.0 - b.cost)) * cfg.kelly_multiplier if b.cost and b.cost < 1 else 0.0 for b in bets])
    f = np.minimum(f, cfg.max_bet_frac)
    if f.sum() > cfg.max_game_frac:
        f *= cfg.max_game_frac / f.sum()
    f[f * cfg.bankroll < cfg.min_stake] = 0.0
    return f


def pnl(bets: list[Bet], f: np.ndarray, bankroll: float) -> np.ndarray:
    """Per-draw dollar P/L at the REAL executable costs (model's joint distribution)."""
    if not bets or not np.any(f):
        n = len(bets[0].y) if bets else 0
        return np.zeros(n)
    return bankroll * (returns(bets) @ f)


def metrics(bets: list[Bet], f: np.ndarray, cfg: PortfolioConfig, p_adj: dict[str, float] | None = None, script_labels: np.ndarray | None = None,
            script_names: dict[int, str] | None = None, major: list[int] | None = None, thesis_of: dict[str, str] | None = None) -> dict[str, Any]:
    stake = f * cfg.bankroll
    total = float(stake.sum())
    x = pnl(bets, f, cfg.bankroll)
    out: dict[str, Any] = {"n_bets": int((stake > 0).sum()), "total_stake": round(total, 2)}
    if total <= 0 or not len(x):
        return out | {"expected_profit": 0.0, "note": "no stake"}
    q = np.percentile(x, [5, 10, 25, 50, 75, 95])
    ev_adj = None
    if p_adj is not None:
        ev_adj = float(sum(s * (p_adj.get(b.bet_id, b.p) - b.cost) / b.cost for s, b in zip(stake, bets) if s > 0))
    out |= {"expected_profit": round(float(x.mean()), 2), "expected_roi": round(float(x.mean()) / total, 4),
            "expected_profit_confidence_adjusted": None if ev_adj is None else round(ev_adj, 2),
            "median_profit": round(float(q[3]), 2), "p_profit": round(float((x > 0).mean()), 4), "p_loss": round(float((x < 0).mean()), 4),
            f"p_lose_more_than_{int(cfg.loss_frac * 100)}pct_of_allocation": round(float((x < -cfg.loss_frac * total).mean()), 4),
            "p05": round(float(q[0]), 2), "p10": round(float(q[1]), 2), "p25": round(float(q[2]), 2), "p75": round(float(q[4]), 2), "p95": round(float(q[5]), 2),
            "worst_draw": round(float(x.min()), 2), "best_draw": round(float(x.max()), 2),
            "expected_log_growth_bp": round(1e4 * float(np.mean(np.log(np.maximum(1 + x / cfg.bankroll, 1e-12)))), 3),
            "adjusted_log_growth_bp": None if p_adj is None else round(1e4 * log_growth(returns(bets, p_adj), f), 3)}
    if script_labels is not None and major:
        per = {int(s): float(x[script_labels == s].mean()) for s in major if (script_labels == s).any()}
        if per:
            w, b = min(per, key=per.get), max(per, key=per.get)
            nm = script_names or {}
            out["worst_major_script"] = {"script": nm.get(w, str(w)), "mean_profit": round(per[w], 2)}
            out["best_major_script"] = {"script": nm.get(b, str(b)), "mean_profit": round(per[b], 2)}
    conc_t: dict[str, float] = {}
    conc_f: dict[str, float] = {}
    for s, bt in zip(stake, bets):
        if s > 0:
            conc_t[(thesis_of or {}).get(bt.bet_id, "?")] = conc_t.get((thesis_of or {}).get(bt.bet_id, "?"), 0.0) + s / total
            conc_f[bt.family] = conc_f.get(bt.family, 0.0) + s / total
    out["concentration_by_thesis"] = {k: round(float(v), 3) for k, v in sorted(conc_t.items(), key=lambda kv: -kv[1])}
    out["concentration_by_family"] = {k: round(float(v), 3) for k, v in sorted(conc_f.items(), key=lambda kv: -kv[1])}
    out["stakes"] = {bt.bet_id: round(float(s), 2) for s, bt in zip(stake, bets) if s > 0}
    return out


def pair_is_diversifier(a: Bet, b: Bet, p_adj: dict[str, float], cfg: PortfolioConfig) -> tuple[bool, dict[str, float]]:
    """Both +EV (adjusted), both keep positive stake in the two-bet joint optimum, and the pair's growth beats either
    alone (unconstrained by thesis budgets: the question is whether the COMBINATION improves the distribution)."""
    km = cfg.kelly_multiplier
    R2 = returns([a, b], p_adj)
    f2 = kelly_optimize(R2, cfg.max_bet_frac / km, [(np.arange(2), cfg.max_game_frac / km)], cfg.iters)
    ga = log_growth(R2[:, :1], kelly_optimize(R2[:, :1], cfg.max_bet_frac / km, [], cfg.iters))
    gb = log_growth(R2[:, 1:], kelly_optimize(R2[:, 1:], cfg.max_bet_frac / km, [], cfg.iters))
    g2 = log_growth(R2, f2)
    pos = bool(f2[0] > 1e-6 and f2[1] > 1e-6)
    ev_ok = all(p_adj.get(x.bet_id, x.p) - x.cost > 0 for x in (a, b))
    return bool(pos and ev_ok and g2 > max(ga, gb) * 1.02), {"growth_pair_bp": round(1e4 * g2, 3), "growth_a_bp": round(1e4 * ga, 3), "growth_b_bp": round(1e4 * gb, 3)}
