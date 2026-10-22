"""Predefined challenger-to-champion promotion scorecard (RESEARCH_ONLY; the scorecard recommends, a human merges).

The gates are fixed here, in code, before any challenger result is read. A challenger is scored *per projection target*
(a target is one published number family: game win probability, overtime probability, total-goal distribution, ...), so
different approved models may serve different targets while exactly one published projection exists per target.

Verdicts
    PROMOTE_CANDIDATE   every gate passes on historical evidence; a human still approves the PR that changes the champion registry
    SHADOW_MORE         historical gates pass but a gate that needs live data (G9/G10) is not yet satisfied
    RETAIN_INCUMBENT    at least one hard gate fails (the failing gates are listed; nothing is hidden)

Inputs are the paired rows produced by :func:`nhl_edge.research.oa_evaluate.compare` (per season and pooled), so the
same bootstrap intervals that were reported are the ones gated.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# --- predefined thresholds (change only with a documented decision, never after seeing a result) -------------------
MIN_UNEXPOSED_SEASONS = 3
MIN_UNEXPOSED_GAMES = 3000
MIN_MEANINGFUL = {"brier_win": 0.0010, "logloss_win": 0.0020, "brier_ot": 0.0010, "rps_total": 0.0050, "rps_margin": 0.0050,
                  "brier_over_5.5": 0.0010, "brier_over_6.5": 0.0010}
NON_INFERIORITY = {"brier_win": 0.0010, "logloss_win": 0.0020, "brier_ot": 0.0010, "rps_total": 0.0050, "rps_margin": 0.0050,
                   "brier_over_5.5": 0.0010, "brier_over_6.5": 0.0010}       # a secondary metric may not be worse by more than this (CI upper bound)
MIN_SEASON_AGREEMENT = 2 / 3     # share of unexposed seasons where the primary point estimate favours the challenger
MAX_ECE_WORSENING = 0.005
COVERAGE_80_BAND = (0.77, 0.83)
MAX_INFERENCE_SECONDS_PER_SLATE = 300.0


@dataclass
class GateResult:
    gate: str
    passed: bool | None            # None == not evaluable yet (needs live data / an artifact)
    detail: str


@dataclass
class Scorecard:
    target: str
    challenger: str
    incumbent: str
    primary_metric: str
    gates: list[GateResult] = field(default_factory=list)

    @property
    def verdict(self) -> str:
        hard = [g for g in self.gates if g.passed is False]
        pending = [g for g in self.gates if g.passed is None]
        if hard:
            return "RETAIN_INCUMBENT"
        return "SHADOW_MORE" if pending else "PROMOTE_CANDIDATE"

    def to_dict(self) -> dict[str, Any]:
        return {"target": self.target, "challenger": self.challenger, "incumbent": self.incumbent, "primary_metric": self.primary_metric, "verdict": self.verdict,
                "gates": [g.__dict__ for g in self.gates]}


def _row(rows: list[dict[str, Any]], challenger: str, metric: str) -> dict[str, Any] | None:
    return next((r for r in rows if r["challenger"] == challenger and r["metric"] == metric), None)


def score_challenger(*, target: str, challenger: str, incumbent: str, primary_metric: str, pooled_unexposed: list[dict[str, Any]],
                     by_season_unexposed: dict[str, list[dict[str, Any]]], exposed: dict[str, list[dict[str, Any]]], n_unexposed_games: int,
                     secondary_metrics: tuple[str, ...] = (), ece: tuple[float, float] | None = None, coverage_80: float | None = None,
                     inference_seconds: float | None = None, reproducible: bool | None = None, contract_compatible: bool | None = None,
                     live_non_inferior: bool | None = None) -> Scorecard:
    sc = Scorecard(target=target, challenger=challenger, incumbent=incumbent, primary_metric=primary_metric)
    p = _row(pooled_unexposed, challenger, primary_metric)
    thr = MIN_MEANINGFUL[primary_metric]

    # G1 proper-score improvement on untouched later periods, under BOTH bootstraps (games and slates)
    if p is None:
        sc.gates.append(GateResult("G1_primary_improvement", False, f"no pooled row for {primary_metric}"))
    else:
        ok = p["better_game_ci"] and p["better_slate_ci"]
        sc.gates.append(GateResult("G1_primary_improvement", bool(ok), f"delta {p['delta']:+.4f} games[{p['lo95']:+.4f},{p['hi95']:+.4f}] slates[{p['lo95_slate']:+.4f},{p['hi95_slate']:+.4f}]"))
        sc.gates.append(GateResult("G2_practically_meaningful", abs(p["delta"]) >= thr and p["delta"] < 0, f"|delta| {abs(p['delta']):.4f} vs required {thr:.4f}"))

    # G3 no material regression elsewhere (non-inferiority on the CI upper bound)
    bad = []
    for m in secondary_metrics:
        r = _row(pooled_unexposed, challenger, m)
        if r is not None and r["hi95"] > NON_INFERIORITY.get(m, 0.0):
            bad.append(f"{m} upper {r['hi95']:+.4f} > {NON_INFERIORITY.get(m, 0.0):.4f}")
    sc.gates.append(GateResult("G3_no_material_regression", not bad, "; ".join(bad) or f"{len(secondary_metrics)} secondary metrics within margin"))

    # G4 calibration / coverage
    if ece is not None:
        sc.gates.append(GateResult("G4a_calibration", ece[0] <= ece[1] + MAX_ECE_WORSENING, f"ECE challenger {ece[0]:.4f} vs incumbent {ece[1]:.4f}"))
    if coverage_80 is not None:
        sc.gates.append(GateResult("G4b_interval_coverage", COVERAGE_80_BAND[0] <= coverage_80 <= COVERAGE_80_BAND[1], f"80% coverage {coverage_80:.3f}"))

    # G5 sample size
    n_seasons = len(by_season_unexposed)
    sc.gates.append(GateResult("G5_sample", n_seasons >= MIN_UNEXPOSED_SEASONS and n_unexposed_games >= MIN_UNEXPOSED_GAMES, f"{n_seasons} unexposed seasons, {n_unexposed_games} games"))

    # G6 stability across seasons: point estimate favours the challenger in enough seasons and no season is significantly worse
    favour, worse = 0, []
    for s, rows in by_season_unexposed.items():
        r = _row(rows, challenger, primary_metric)
        if r is None:
            continue
        favour += r["delta"] < 0
        if r["worse_game_ci"] and r["worse_slate_ci"]:
            worse.append(s)
    share = favour / max(len(by_season_unexposed), 1)
    sc.gates.append(GateResult("G6_season_stability", share >= MIN_SEASON_AGREEMENT and not worse, f"favourable in {favour}/{len(by_season_unexposed)} seasons; significantly worse in {worse or 'none'}"))

    # G6b exposed seasons must not contradict
    contra = [s for s, rows in exposed.items() if (r := _row(rows, challenger, primary_metric)) and r["worse_game_ci"] and r["worse_slate_ci"]]
    sc.gates.append(GateResult("G6b_exposed_not_contradicting", not contra, f"significantly worse in exposed seasons: {contra or 'none'}"))

    # G7 runtime / G8 reproducibility / G9 contract / G10 live non-regression
    if inference_seconds is not None:
        sc.gates.append(GateResult("G7_runtime", inference_seconds <= MAX_INFERENCE_SECONDS_PER_SLATE, f"{inference_seconds:.0f}s per slate (limit {MAX_INFERENCE_SECONDS_PER_SLATE:.0f}s)"))
    else:
        sc.gates.append(GateResult("G7_runtime", None, "not measured"))
    sc.gates.append(GateResult("G8_reproducible", reproducible, "frozen params + seed regenerate predictions bit-for-bit" if reproducible else "not yet demonstrated"))
    sc.gates.append(GateResult("G9_sift_contract", contract_compatible, "published fields unchanged / additive" if contract_compatible else "not yet verified"))
    sc.gates.append(GateResult("G10_live_non_inferior", live_non_inferior, "live shadow rolling delta not significantly worse" if live_non_inferior else "needs live shadow games"))
    return sc
