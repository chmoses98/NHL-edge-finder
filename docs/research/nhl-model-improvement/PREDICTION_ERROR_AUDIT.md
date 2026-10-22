# Prediction-error audit and existing-model failure analysis

> RESEARCH ONLY. Sources: 151 LIVE finals (2026-09-29..10-20, forecasts frozen at T-60 from the last production slate run), 2,624 walk-forward games (2024 and 2025 regular seasons, every parameter fitted on earlier seasons only), 1,312 games of 2025-26 Kalshi history. Every number is in `RESULTS_TABLES.md` (generated from `data/*.json`); experiments are in the append-only `experiment_registry.jsonl`. **No game in the prospective tier (starting after 2026-10-21T17:13:05Z) was read.**

## Scope and an honest limit

Brief questions 1-13 ask *why* the forecasts were wrong. The data support some descriptions firmly, some weakly, and a few not at all. Ex-post decompositions (shots, xG, finishing) describe what happened; they are **not** causal proof, and a post-hoc narrative for any single game is not offered. Evidence tiers used below: **EXPLORATORY** (found or tuned on the walk-forward sample), **LIVE-descriptive** (151 games, one look), **PROSPECTIVE** (not yet available).

## Answers to the operator's questions

| # | question | verdict | key evidence | strength |
|---|---|---|---|---|
| 1 | Misunderstanding NHL matchups? | **No evidence.** Opponent-adjusted xG, rest, back-to-backs, travel, finishing, special teams add nothing beyond the market (prior audit); rest, back-to-back, early-season and season effects on V1 residuals are null (all \|t\| < 1.7, BH q ≥ 0.32). | M-SCAN-1; prior `MATCHUP_FACTOR_STUDY` | moderate (2,624 games) |
| 2 | Over-valuing recent scoring trends? | **Slightly, immaterially.** Total-goal residuals fall with the sum of V1 finishing factors (−0.167 goals per SD, t = −3.6, BH q = 0.003): finishing persistence is over-weighted. | M-SCAN-1 | EXPLORATORY; effect 0.17 goals vs a per-game SD of 2.3 |
| 3 | Under-estimating shot quality? | **Suggestive in the first three weeks.** Ex-post MoneyPuck xG exceeded V1 expected goals by +0.30 goals/game (95% CI +0.13…+0.49, 140 games); realised goals fell short of xG by −0.20 (−0.58…+0.17). | `data/live_game_attribution.csv` | LIVE-descriptive, one early-season window |
| 4 | Opponent-strength adjustment? | **Margin rates are under-dispersed, totals over-dispersed.** Margin on V1 `lam_home − lam_away`: coefficient on residual +0.139/SD (q = 0.016); total on `lam_sum`: −0.173/SD (q = 0.003). Correcting both did **not** improve any score (see below). | M-SCAN-1, M-CAL-1 | EXPLORATORY; immaterial |
| 5 | Goalie assumptions too confident? | **Rejected.** At T-60 the goalie named as CONFIRMED was the goalie of record 97.8% of the time (Wilson 94.5–99.1%, stated 98.5%); PROJECTED 76.5% (63.2–86.0%, stated 70%); PROBABLE 97.1% (89.9–99.2%, stated 85% — *under*-confident). | M-GOALIE-1 | LIVE-descriptive, n = 183/68/51 slots |
| 6 | Simulations missing high/low scoring? | **Not for totals.** V1's total-goal distribution is slightly too *wide* (standardised squared residual 0.913, 95% CI 0.863–0.966); P(total ≥ 7/8/9) are inside the observed intervals; ≥ 10 is over-predicted (8.7% vs 7.2%). What **is** wrong: overtime (17.4% predicted vs 22.8% observed, V2 largely fixes this) and the margin shape (\|margin\| ≥ 3: 34.7% vs 39.6%; ≥ 5: 6.8% vs 5.6%). | M-DIST-1 (CRPS/RPS, PIT) | moderate, 2,624 games |
| 7 | Player usage assumptions incorrect? | **Biased low, outputs unbiased.** For priced players: ice time +0.41 min (CI +0.26…+0.55), PP time +0.66 min (+0.55…+0.78), shots +0.14 per game (+0.09…+0.19) *above* the expectations; points, goals, assists errors indistinguishable from 0. The stated TOI p10–p90 interval is too wide (86% inside vs 80%). Shots are over-dispersed vs Poisson (variance/mean 1.34). 1.0% of priced players did not dress. | M-PLAYER-1 | LIVE-descriptive, 2,597 player-games / 145 games |
| 8 | Miscalibrated? | Only mildly. V1 win-probability logit slope 1.41 (SE 0.17) on the walk-forward sample, but re-scaling does not change Brier (+0.0001). P(1+ point) is calibrated (mean 44.5% vs 44.6% observed) and beats a league-rate forecast (Brier 0.2282 vs 0.2470). | M-CAL-1, M-PLAYER-1 | moderate |
| 9 | Distributions too narrow? | **No** (see 6). | M-DIST-1 | moderate |
| 10 | Wrong markets for the thesis? | Routed wagers: player props −44.5% on $401, game-scoped −1.5% on $611 (n = 34; not significant). Prior audit: no family has an edge. | `ACTUAL_WAGER_AUDIT.md` | weak |
| 11 | Paying too much? | **Yes, mechanically.** Taker ask + fee is 4–5 cents worse than the market's own probability (moneyline ROI −4.3% on both sides). The routed-fill shortfall equals the fees-and-spread expectation (−$55.85; realised −$187.64 is −0.6 SD below it). | prior audit; wager audit | strong |
| 12 | Betting after information was priced in? | **Cannot be established as stated, and our capture is too slow to exploit it.** Median capture lag behind the source's goalie report is 27.6 min (26% within 15 min); Kalshi moneyline mids show no detectable repricing at 15–120 min around 32 goalie *changes* (CHANGE − SAME \|move\| ≈ 0 ± 0.1 cents). Three of four Oct 20 fills were placed *after* the scheduled drop. | M-INFO-1 | LIVE-descriptive |
| 13 | Normal variance? | **Largely yes.** 17.2% of LIVE games are "extreme" under the forecast's own predictive distribution vs ≈ 19% expected from a calibrated model. | `attribution.py` | descriptive |

## Per-game attribution (151 LIVE games)

Method (`attribution.py`): regenerate the production V1 predictive distribution **bit-for-bit** from the slate's `lam_home`, `lam_away`, `seed`, `n_sims` (max |Δ| in P(home win) vs the archive = 0.0); place the realised score in it (randomised PIT); call a game *extreme* if its total or margin PIT lies outside [0.05, 0.95]; then assign A–F with an evidence string:

| class | meaning | games |
|---|---|---|
| E normal variance | not extreme | **125** (82.8%) |
| F unresolved | extreme, no goalie or tail explanation in the data | 17 |
| D distributional | total in the far tail (PIT < 0.03 or > 0.97), no goalie mismatch | 4 |
| C timing | extreme, goalie of record ≠ goalie named at the cut, correct goalie not public before the cut | 4 |
| B missing information | extreme, goalie mismatch, correct goalie *was* public before the cut | 1 |
| A systematic | not a per-game label — a pattern across games; see M-SCAN-1 / M-DIST-1 (OT rate, margin tail, finishing persistence) | pattern-level |

Reading it honestly: the 26 extreme games are 17.2% of 151 against ≈ 19% expected under calibration, so the count of surprising results needs no explanation beyond variance. Goalie-mismatch games (17) were extreme 29% of the time vs 16% otherwise — a hint (n = 17) that unannounced goalie changes matter, not a finding. Most F games are lopsided margins (4–7 goals), which is exactly where V1's margin shape is weakest. **No game was forced into a narrative**; 17 remain unresolved because the archive contains no lineup, injury-timing or in-game state that would explain them.

Ex-post decomposition of the error in total goals (`volume_quality_err = MoneyPuck team xG − V1 expected goals`, `finishing_err = goals − xG`; 140 games with xG): variance of the total error 5.41 ≈ shot-quality/volume 1.16 + finishing/goaltending 5.55 + 2 × covariance (−0.67 each). **About all of the unforecastable variance in total goals is finishing and goaltending luck**; the part a better shot-generation model could in principle address is ~1.2 goals² per game, and V1 is already unbiased on goals (mean error −0.01 [−0.36, +0.37]).

## Why are our models less accurate than the market?

The gap is small and no single correctable cause was found:

* LIVE Brier (151 games): V1 0.2304 vs Kalshi T-60 mid 0.2268 (+0.0036, CI −0.006…+0.013); totals +0.0026 (CI −0.0001…+0.0054); spreads +0.0045 (−0.0004…+0.0094). 2025-26 history (rolling, 907 games): model alone vs mid +0.0014 (winner), +0.0014 (total), +0.0017 (spread). Sportsbook consensus (147 games) 0.2275 vs V1 0.2313.
* V1 has real forecasting skill over climatology for **who wins and by how much** (Brier 0.2427 vs 0.2483, RPS margin 1.428 vs 1.456; CIs exclude 0) but **none for how many goals**: its total-goal distribution scores the same as a constant league-average Poisson (RPS 1.2847 vs 1.2835, Δ −0.0012, CI −0.008…+0.005). Game totals are priced by the market using information V1 does not have (starter, lineups, injuries, rest nuances) and by participants who know more than archived MoneyPuck rates.
* The model does carry a *little* incremental information on the moneyline (rolling coefficient c ≈ 0.26–0.29), but optimally blending it with the market gives no Brier gain (inc − mid = 0.0000 [−0.0011, +0.0011]). The weight the data justify is small and the estimate noisy.
* What the data cannot say: whether the market's advantage comes from information (lineups, goalie news), better models, or both. That needs timestamped news (see `INFORMATION_EVENT_ASSESSMENT.md`).

## Repeatable, correctable errors found (class A) and what correcting them did

| pattern | size | corrected by | result |
|---|---|---|---|
| overtime/regulation ties under-predicted by V1 (17.4% vs 22.8%) | 5.4 points | already fixed in V2 (OT Brier −0.003 [−0.0044, −0.0017] vs V1 on EVAL_A; −0.0045 on 2025) | **real, already addressed in the shadow arm; no betting relevance shown** (overtime is a small market family and the prior audit found no edge in it) |
| margin shape (\|margin\| ≥ 3 under-predicted by 4.9 points; ≥ 5 over-predicted) | ~5 SE | not attempted beyond the strength-noise challenger C2 (rejected) | open: needs a score-effects / empty-net recalibration; V2's score-effects engine is the right vehicle |
| total rates over-dispersed across games; margin rates under-dispersed | slopes 0.37 and 1.39 | linear recalibration C1 | **statistically significant slopes, no score improvement** (all paired CIs span 0) — significance ≠ improvement |
| player usage under-projected (TOI, PP time, shots) | +0.4 min, +0.7 min, +0.14 | not corrected here | open; point outputs are already unbiased, so the gain is unclear |

## Limits

LIVE is 151 games in the first three weeks of one season (early-season uncertainty is itself a candidate cause and cannot be separated from a general one); effects below ~5% ROI or ~0.004 Brier are undetectable at this sample size; attribution labels are heuristics with evidence strings, not causal claims; per-game xG data is missing for 11 of 151 games.
