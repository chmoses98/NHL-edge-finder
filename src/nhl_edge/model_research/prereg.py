"""Pre-registrations for the model-improvement program (written and committed BEFORE the corresponding result is computed).

Run once per id; ``registry.append`` refuses a second PREREG for the same id and a RESULT without a PREREG. A changed idea is a new id.

DISCLOSURE (applies to every id below): before this registration the walk-forward V1 table (2,624 games, 2024-25 seasons) was
inspected DESCRIPTIVELY on the full sample (mean/variance of totals, tail frequencies, OT rate, calibration slopes). The challenger
families below were suggested by those descriptive slopes. A rolling-origin evaluation (each prediction uses only strictly earlier
dates) removes parameter look-ahead but NOT the selection of the idea; therefore the in-sample WF evidence is classed EXPLORATORY and
only (a) the single-look LIVE evaluation and (b) the post-freeze PROSPECTIVE tier can validate. The prospective tier (games starting
after 2026-10-21T17:13:05Z) is not read by any code in this package.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from nhl_edge.model_research import registry

COMMON_PROTOCOL = {
    "data_wf": "docs/research/walk_forward_36570274279_games.csv + walk_forward_v2_wf2_20260929_games.csv (2024 & 2025 regular seasons, 2,624 games)",
    "ordering": "by (game_date, game_id); a prediction for date D uses only games with date < D (same-day games are NOT training data)",
    "burn_in": "first 300 games are training only (predictions start ~Dec 2024)",
    "independent_unit": "game (all intervals resample games)",
    "tiers": {"EVAL_A": "all games after burn-in", "EVAL_B": "2025 regular season (aligned with Kalshi candle history)", "LIVE": "151 finals 2026-09-29..2026-10-20, ONE look",
              "PROSPECTIVE": "games starting after 2026-10-21T17:13:05Z - not read"},
}

PREREGS: dict[str, dict[str, Any]] = {
    "M-DIST-1": {
        "hypothesis": "The V1 simulator's predictive distribution is too NARROW: it underestimates 7-9 goal games and over-concentrates totals near 5-6.",
        "motivation": "Operator hypothesis; V1 is independent Poisson with the shared-environment multiplier OFF.",
        "method": "Regenerate each game's V1 distribution from (lam_home, lam_away, seed) with nhl_edge.sim.engine (4,000 draws, bit-exact vs the CSV). Compare "
                  "standardized squared residual (y-mu)^2/sigma^2 (expect 1), P(total>=7/8/9), margin tails P(|margin|>=2/3/4), OT and shutout rates, PIT uniformity, RPS (CRPS).",
        "baseline": "league-constant Poisson from the same CSV (league_poisson_*) and V1 itself",
        "decision_rule": "NARROW if mean z^2 > 1 with 95% game-bootstrap CI excluding 1 AND observed P(total>=8) above predicted with 95% Wilson CI excluding the prediction. "
                         "Symmetrically WIDE. Otherwise CALIBRATED_WIDTH. Reported per statistic, uncorrected, descriptive.",
        "protocol": COMMON_PROTOCOL, "tier": "EXPLORATORY",
    },
    "M-CAL-1": {
        "hypothesis": "A 3-parameter linear recalibration of V1 expected goals corrects a repeatable error: total-goal rates (s = lam_h+lam_a) are too dispersed across games "
                      "(slope < 1) while margin rates (d = lam_h-lam_a) are too compressed (slope > 1).",
        "motivation": "Full-sample descriptive slopes: margin on d = 1.39 (SE 0.13), total on s = 0.37 (SE 0.17), logit(p_home) slope = 1.41 (SE 0.17).",
        "method": "C1 SCALE: s' = sbar + b_s (s - sbar); d' = c + b_d d; lam_h' = (s'+d')/2, lam_a' = (s'-d')/2 with (sbar, b_s, c, b_d) from expanding-window OLS on strictly prior "
                  "games (y_total on s; margin on d), b clipped to [0.2, 2.0]; re-simulate with the SAME seed and 4,000 draws (paired Monte Carlo).",
        "baseline": "V1 as published (primary); V2 SIM2_ST published ladder (secondary); constant-home-rate and league Poisson",
        "metrics": ["RPS total", "RPS margin", "Brier home win", "log loss home win", "Brier over 5.5/6.5", "P(total>=8) calibration"],
        "decision_rule": "IMPROVES_EXPLORATORY if paired game-bootstrap 95% CI of delta(RPS total) AND of delta(Brier home win) are each < 0 on EVAL_A; otherwise NO_IMPROVEMENT or MIXED. "
                         "Any such label is EXPLORATORY until M-LIVE-1 confirms direction and the prospective tier confirms magnitude.",
        "protocol": COMMON_PROTOCOL, "tier": "EXPLORATORY",
    },
    "M-CAL-2": {
        "hypothesis": "Adding antithetic per-game strength uncertainty (lam_h x exp(sigma z), lam_a x exp(-sigma z)) widens margin tails without inflating totals and improves RPS(margin) beyond C1.",
        "motivation": "Home/away goal residual correlation is -0.09 and |margin|>=3 games are 4.9 points more frequent than V1 predicts.",
        "method": "C2 = C1 plus sigma fitted by expanding-window method of moments (match Var(margin) of training games to the simulated variance; sigma in [0, 0.5]); same seeds.",
        "baseline": "C1 (primary), V1",
        "decision_rule": "ADDS_VALUE if delta(RPS margin) vs C1 has 95% CI < 0 on EVAL_A and delta(Brier home win) vs C1 CI includes 0 or is < 0; else REJECT_COMPLEXITY (prefer C1).",
        "protocol": COMMON_PROTOCOL, "tier": "EXPLORATORY",
    },
    "M-MKT-1": {
        "hypothesis": "After conditioning on the Kalshi T-60 mid, V1 / C1 carry incremental information for moneyline, full-game total and puck-line contracts.",
        "motivation": "Prior audit: V1/V2 not better than the market; test whether a recalibrated model is.",
        "method": "Rolling-origin on 2025 (EVAL_B): y ~ offset(logit mid) + c*(logit p_model - logit mid) with c from prior games only, one coefficient per family; compare Brier of "
                  "(a) raw mid, (b) calibrated mid (a+b logit mid, prior games), (c) mid + c-adjustment. Game-clustered bootstrap.",
        "baseline": "Kalshi mid at T-60 (market-implied baseline), calibrated market baseline",
        "decision_rule": "INCREMENTAL if c-adjusted Brier beats BOTH (a) and (b) with 95% game-bootstrap CI < 0 in two or more families; otherwise NO_INCREMENTAL_VALUE.",
        "protocol": COMMON_PROTOCOL, "tier": "EXPLORATORY",
    },
    "M-LIVE-1": {
        "hypothesis": "The C1 (and C2) parameters fitted on ALL 2,624 WF games, frozen, improve on production V1 on the 151 LIVE games in the same direction as M-CAL-1.",
        "motivation": "Only a post-selection look can confirm an idea suggested by descriptive in-sample slopes.",
        "method": "Apply frozen C1/C2 to production lam at the T-60 slate run; re-simulate with the production seed (20,000 draws); compare RPS(total), RPS(margin), Brier(home win) vs "
                  "production V1, V2, sportsbook consensus, Kalshi mid. ONE look; parameters may not change after it.",
        "baseline": "production V1 (primary), V2, sportsbook consensus, Kalshi mid",
        "decision_rule": "DIRECTION_CONFIRMED if delta(RPS total) < 0 and delta(Brier home win) < 0 point estimates; with n=151 this is NOT a significance test. LIVE_INCONCLUSIVE otherwise.",
        "protocol": COMMON_PROTOCOL, "tier": "LIVE_ONE_LOOK",
    },
    "M-GOALIE-1": {
        "hypothesis": "V1's goalie status ladder (named goalie starts w.p. 0.70 PROJECTED / 0.85 PROBABLE / 0.985 CONFIRMED) is miscalibrated at the T-60 cut.",
        "motivation": "Goalie assumptions were suspected of over-confidence.",
        "method": "At the T-60 cut, compare the goalie named by the slate (status at the cut) with the goalie of record (most ice time, post-game boxscore). Report the match rate per status with Wilson 95% intervals; "
                  "also the share of confirmations that were already public at the cut.",
        "baseline": "the stated prior confidences",
        "decision_rule": "MISCALIBRATED if the Wilson interval of the observed match rate per status excludes the stated confidence; otherwise CONSISTENT. n is small (<=151 per side) so a result is descriptive.",
        "protocol": COMMON_PROTOCOL, "tier": "LIVE_DESCRIPTIVE",
    },
}


def register_all(path: Path, repo: Path | None = None, only: list[str] | None = None) -> list[str]:
    done = {e["id"] for e in registry.read(path) if e["type"] == "PREREG"}
    out = []
    for k, v in PREREGS.items():
        if (only and k not in only) or k in done:
            continue
        registry.append(path, "PREREG", k, v, repo)
        out.append(k)
    return out


if __name__ == "__main__":
    import sys

    repo = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    reg = repo / "docs/research/nhl-model-improvement/experiment_registry.jsonl"
    print(register_all(reg, repo))
