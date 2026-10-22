# Challenger models, market baseline and statistical validation

> RESEARCH ONLY. No challenger is wired to a production path, a recommendation or a stake. Every experiment below was preregistered in the hash-chained `experiment_registry.jsonl` (preregistration commit `2f8a591c` precedes the first result), recorded with its reproduction command, and kept whether it succeeded or failed. Exact tables: `RESULTS_TABLES.md`.

## Protocol (what "chronologically valid" means here)

* **Data.** `walk_forward_*_games.csv` (2024 and 2025 regular seasons, 2,624 games): production V1 expected goals `lam_home`/`lam_away`, seeds and the V2 (SIM2_ST) published ladders, every production parameter fitted on earlier seasons only. `lam` + `seed` regenerate each V1 predictive distribution bit-for-bit (checked: |Δ| = 0).
* **Ordering and leakage.** Games ordered by (date, game id). A prediction for date *D* uses only games with date < *D* (same-day games are not training data). The first 300 games are burn-in. Features are only quantities stamped before the game; the actual starter and final score are labels.
* **Tiers.** EVAL_A = all 2,320 post-burn-in games; EVAL_B = the 1,312-game 2025 season (aligned with Kalshi history); LIVE = 151 finals, **one look**; PROSPECTIVE = not read.
* **Independent unit = game.** Intervals are paired game-level bootstraps (4,000 resamples). Contract ladders (several totals lines per game) are averaged within a game before any interval.
* **Baselines.** (1) production V1; (2) V2 SIM2_ST published probabilities; (3) league-constant Poisson from the same engine; (4) the Kalshi T-60 mid; (5) the mid recalibrated on prior games only; (6) a sportsbook consensus on LIVE.
* **Disclosure that limits every EXPLORATORY label.** Before registration the V1 walk-forward table was inspected descriptively on the full sample (slopes, tail frequencies). The challenger families were *suggested by that inspection*. Rolling-origin fitting removes parameter look-ahead, not selection of the idea. Only the LIVE look and the prospective tier can validate; neither has validated anything.

## Challengers and results

| id | model | decision rule | result |
|---|---|---|---|
| M-DIST-1 | (diagnostic) V1 predictive distribution vs 2,624 games | NARROW / WIDE / CALIBRATED_WIDTH | **WIDE_TOTAL** — operator hypothesis "too narrow" rejected; see `PREDICTION_ERROR_AUDIT.md` |
| M-CAL-1 | **C1 SCALE**: linear recalibration of regulation `s = lam_h + lam_a` and `d = lam_h − lam_a` (expanding-window OLS, slopes clipped to [0.2, 2.0]); re-simulated with the production seed | IMPROVES iff paired CI of RPS(total) **and** Brier(win) are both < 0 on EVAL_A | **NO_IMPROVEMENT** |
| M-CAL-2 | **C2**: C1 + antithetic strength uncertainty σ (grid 0–0.4, rolling log-score choice) | adds value iff RPS(margin) CI vs C1 < 0 | **REJECT_COMPLEXITY** — rolling σ = 0 on every date (total margin log-score is highest at σ = 0) |
| M-MKT-1 | offset-logit `mid + c·(logit p_model − logit mid)`, one `c` per family, refit each date on prior contracts (2025-26, from 2025-12-01) | INCREMENTAL iff it beats both the raw and the recalibrated mid with CI < 0 in ≥ 2 families | **NO_INCREMENTAL_VALUE** (revision 2; a first run that pooled `c` across families, against the protocol, is kept in the registry and superseded) |
| M-LIVE-1 | C1 frozen at its all-walk-forward parameters, one look at 151 LIVE games | DIRECTION_CONFIRMED iff both point deltas < 0 | **LIVE_INCONCLUSIVE** |

### C1 vs V1 on the walk-forward games (paired Δ, negative = C1 better; 95% game-bootstrap CI)

| metric | EVAL_A (2,320) | EVAL_B (1,312) |
|---|---|---|
| RPS total goals | −0.0009 [−0.0059, +0.0042] | −0.0002 [−0.0073, +0.0069] |
| RPS margin | +0.0003 [−0.0041, +0.0046] | −0.0017 [−0.0062, +0.0026] |
| Brier home win | +0.0001 [−0.0010, +0.0013] | +0.0002 [−0.0010, +0.0013] |
| log loss home win | +0.0003 [−0.0021, +0.0026] | +0.0002 [−0.0022, +0.0026] |
| Brier over 5.5 / 6.5 | −0.0001 / −0.0000 | +0.0000 / +0.0004 |

Every interval spans zero. **The significant calibration slopes found descriptively (margin 1.39, total 0.37) describe how a narrow band of rates maps to outcomes; correcting them recovers no predictive score.** A 0.18-goal correction per SD of the feature is invisible against a 2.3-goal per-game SD.

### Reference models (V1 vs climatology and V2 vs V1)

* V1 **beats** league-constant Poisson for win probability (Brier −0.0056 [−0.0079, −0.0033] EVAL_A; −0.0040 [−0.0070, −0.0011] EVAL_B) and for the margin distribution (RPS −0.027 [−0.036, −0.018]), but is **indistinguishable from it for total goals** (RPS total −0.0012 [−0.0076, +0.0052]). The model's totals forecasts add no information beyond a league average.
* V2 (SIM2_ST) vs V1: overtime Brier −0.0030 [−0.0044, −0.0017] (EVAL_A) / −0.0045 [−0.0063, −0.0027] (EVAL_B) — V2's tie/OT fix is real; moneyline and totals unchanged (|Δ| ≤ 0.0005, CIs span 0).

### Against the market

2025-26 history, rolling from 2025-12-01 (907 / 903 / 903 games for winner / total / spread; Brier):

| family | Kalshi mid | recalibrated mid | mid + c·gap (V1) | V1 alone | inc − mid [95% CI] | V1 − mid [95% CI] | final c |
|---|---|---|---|---|---|---|---|
| winner | 0.2435 | 0.2435 | 0.2435 | 0.2449 | +0.0000 [−0.0011, +0.0011] | +0.0014 [−0.0022, +0.0049] | 0.29 |
| total | 0.1720 | 0.1721 | 0.1725 | 0.1734 | +0.0005 [−0.0002, +0.0011] | +0.0014 [−0.0000, +0.0028] | 0.28 |
| spread | 0.1796 | 0.1805 | 0.1799 | 0.1814 | +0.0003 [−0.0004, +0.0011] | +0.0017 [−0.0002, +0.0037] | 0.26 |

C1 behaves identically (inc − mid +0.0001, +0.0002, +0.0002). On the LIVE look the market also edges both models (V1 − mid +0.0036 winner, +0.0026 total, +0.0045 spread; C1 total +0.0036 [+0.0012, +0.0059] — the only interval excluding zero, and in the *wrong* direction for C1).

**Verdict:** no challenger improved forecasts beyond the prior production arms, and **no forecast, production or challenger, exceeded the market baseline.** The "model carries a small amount of information" signal (`c` ≈ 0.26–0.29) is real in sign but too small and noisy to change a Brier score.

## Statistical-validation and robustness notes

* **Multiple testing.** M-SCAN-1 uses BH (q = 0.10) over 17 pre-listed tests; the challenger decision rules are single pre-declared criteria per id. The prior audit's 16 hypotheses are BH-controlled over the LIVE family (smallest q = 0.976). The registry has 10 distinct experiment ids; results are reported for all of them.
* **Seeds / Monte Carlo.** Paired simulations share seeds (common random numbers), so Monte Carlo noise cancels in paired deltas. Bootstrap endpoint noise is ≈ ±0.3–0.4 percentage points of ROI at n = 1,000 and larger at 151 games (reviewer measurement), which is why v1.1 requires a one-point margin before labelling a hypothesis unprofitable.
* **Sensitivity.** Burn-in (300 games), σ grid, slope clipping and the 2025-12-01 start for market tests were fixed in advance; they were not tuned. The effect sizes are so small that no reasonable alternative would flip a conclusion; this was **not** exhaustively verified.
* **Sample-size limits.** At 151 games a +3% ROI is undetectable (standard errors 1.6–14 points depending on price); only a much larger edge could be found within a season. Model-quality conclusions on LIVE are about differences of ≈ 0.004–0.01 Brier — below detectability.
* **What failed and stays on the record:** C1 (no gain), C2 (σ = 0), the pooled-`c` first run of M-MKT-1, the first M-INFO-1 run with in-play contamination.

## What would justify promoting a model (proposed bar; nothing is promoted)

1. A frozen model/blend with a pre-registered primary metric; 2. paired Brier / log-loss improvement over the *calibrated market* baseline with a 95% game-bootstrap CI below 0 on the prospective tier at the 300-game look (alpha-spending rule in `PROSPECTIVE_PROTOCOL.md`); 3. the improvement repeats in a later window; 4. executable net ROI after fee and +1c slippage from captured depth; 5. explicit user approval.
