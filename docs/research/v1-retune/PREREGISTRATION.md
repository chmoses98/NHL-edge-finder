# V1 re-tune + recalibration vs opponent adjustment — preregistration

> RESEARCH_ONLY · written 2026-10-23, committed **before** any arm of this study is run. The commit time is the registration time. Nothing here changes a production number, price, stake, cap or SIFT contract, and nothing here promotes a model: promotion needs explicit approval and the scorecard in `docs/research/PROMOTION_SCORECARD.md`.

## Why this experiment

The 2026-10-22 opponent-adjusted study (`docs/research/oa-walk-forward/`) found that `OA_SVA_C1` beats production `DATA_ONLY_V1` on win-probability Brier by −0.0028, but that about two thirds of that gain is reproduced by simply re-tuning V1's own shrinkage constants (`V1_T`), and that a re-tuned **and** recalibrated V1 (`V1_T_C1`, no opponent adjustment) is statistically tied with `OA_SVA_C1` (−0.0004 [−0.0009, +0.0001]). The tuning grid of that control hit its lower boundary (prior = 10 games in 7 of 8 seasons), so the control was constrained. This study asks, with the control un-constrained and with its tuning inside each training window:

* **Q1.** How much of V1's deficit is retunable shrinkage / recency / home-ice constants? (`V1_R` vs `V1`)
* **Q2.** Does slope recalibration of the sum and difference of the expected-goal rates add to a retuned V1? (`V1_R_C1` vs `V1_R`)
* **Q3.** Does opponent adjustment add *incremental* value beyond the retuned, recalibrated V1? (`OA_SVA_C1` vs `V1_R_C1`.) If not, the simpler model is preferred.
* **Q4.** Which of V1's matchup features (back-to-back, finishing ratio, home-ice, shrinkage strength) carry measurable value? (ablations of `V1_R`.)
* **Q5.** Against the V2 simulator (overtime/margin shape) and against the Kalshi midpoint at the same timestamp.

## Arms (fixed in advance)

All arms use the same simulator (`nhl-sim-1.1`), 4,000 draws, per-game seeds (`game_seed`), V1's goalie term off (no historical starters), and rating rows dated strictly before the game date.

| arm | definition |
|---|---|
| `V1` | production constants (half-life 20 games, prior 20 games, home 1.045) |
| `V1_R` | V1's own ratings; per test season, half-life ∈ {10, 20, 40, 80, 160} games, shrinkage prior ∈ {2.5, 5, 10, 20, 40, 80, 160} games, home-ice multiplier ∈ {1.0, 1.03, 1.045, 1.06} chosen by Poisson goals log-likelihood on the **two prior seasons** (each validation game rated only from earlier rows). Grid extended below the previous minimum of 10 and above 80. |
| `V1_R_C1` | `V1_R` with the sum and difference of its two rates recalibrated by `SlopeCalibrator` (slope-only, burn-in 300 games, slopes clipped to [0.2, 2.0], same-day games never inform each other), fitted on the arm's own strictly prior predictions |
| `V1_R_noB2B` | `V1_R` with the back-to-back adjustment switched off (ablation, same selected constants) |
| `V1_R_noFIN` | `V1_R` with the finishing ratio fixed at 1.0 (ablation, same selected constants) |
| `V1_T`, `V1_T_C1` | the previous control (old grid) re-run in the same pipeline, for continuity |
| `OA_SVA`, `OA_SVA_C1` | the opponent-adjusted challengers exactly as in `oa_walk_forward` (same grid as Amendment 1) |
| `V1_C1` | V1 + recalibration (reference) |
| `LEAGUE` | league-average rates with home advantage only (reference) |

The ablations reuse the constants that were selected for `V1_R` rather than re-tuning, so that each ablation isolates exactly one feature.

## Test seasons and data tiers

* Source: MoneyPuck team-game rows and official NHL results in `data/history` (retrospective vendor data; see Limits).
* **Test seasons 2017–2025** (MoneyPuck start-year convention). Selection for season *S* uses seasons *S−2* and *S−1* only, so the first testable season is 2017 (selection on 2015–2016).
* **Tier FRESH — 2017 (n ≈ 1,270):** no arm of any earlier study was scored on 2017 (the earlier studies began at 2018). It is the only historical tier in which neither the design nor any family-member result was seen. Power is limited; it is reported as a stability check, not as the gate.
* **Tier FAMILY_SEEN — 2018–2023 (n = 7,157):** the previous study scored `V1`, `V1_T`, `V1_T_C1` and `OA_*` on these seasons. The *new* arm `V1_R` differs from `V1_T` only in a wider grid, so its result is **not independent of what was seen**; this tier is a development tier and is labelled as such.
* **Tier EXPOSED — 2024–2025 (n = 2,624):** inspected by earlier V1/V2 research and the earlier OA study; reported, never used for selection.
* **Tier PROSPECTIVE:** games after `2026-10-21T17:13:05Z`. No code in this study reads them. Their evidence will come only from the live shadow records (see "What this does not decide").

## Hypotheses and decision rules (set before looking)

Primary metrics, challenger minus incumbent, paired on the same games, negative = better: H1 Brier of P(home win); H2 RPS of the total-goal distribution; H3 Brier of P(overtime). Supporting: log loss, RPS of the margin distribution, Brier of totals 5.5/6.5, expected-calibration error, per-season deltas.

* **R1 — retune.** `V1_R` is *better than V1* if the pooled Brier(win) delta over 2017–2025 has a 95% interval below zero under both the game and the date-cluster bootstrap, is favourable in at least 6 of the 9 seasons, and no primary metric is worse with an interval excluding zero. Practical threshold: 0.0010 Brier.
* **R2 — recalibration.** `V1_R_C1` is *better than V1_R* by the same rule, evaluated on H1 and H2 (a recalibration that fixes totals while hurting win probability is not a gain).
* **R3 — incremental value of opponent adjustment.** `OA_SVA_C1` is retained over `V1_R_C1` only if the pooled Brier(win) delta (OA minus V1_R_C1) is ≤ −0.0010, its 95% interval excludes zero under both bootstraps, it is favourable in at least 6 of 9 seasons, and no primary metric is worse. Otherwise the simpler model is preferred and the opponent-adjusted model is reported as not adding value.
* **R4 — leading candidate.** The leading candidate is the arm with the lowest pooled Brier(win) among those that satisfy "no primary metric worse than V1 with an interval excluding zero", with ties (differences inside the practical threshold) broken in favour of the simpler arm. The label "leads" never implies promotion.
* **R5 — features.** A feature ablation is called *informative* when removing it worsens pooled Brier(win) or RPS(total) with a 95% interval excluding zero under both bootstraps; otherwise *not detectable at this sample size*.
* Multiplicity: R1, R2 and R3 are three separate pre-declared questions, each evaluated at 95% on three primary metrics; the intervals are therefore not family-wise corrected, which is why every rule also requires season-level consistency (≥ 6 of 9) and a practical-size threshold. Everything else (ablations, market, V2) is exploratory and labelled so.

## Market and V2 comparisons

* **Market:** for 2025 (2025-26, the only season with Kalshi candle history) the midpoint at T-60 min is compared with `V1`, `V1_R`, `V1_R_C1` and `OA_SVA_C1` on the winner, 5.5 and 6.5 totals, and the −1.5 puck line, same timestamp for every forecaster, paired Brier delta with game and slate bootstraps. Blends with the market are labelled MARKET-INFORMED and are not independent forecasts. A midpoint advantage is not an execution edge.
* **V2 simulator:** the existing `walk_forward_v2` output exists for 2023–2025. `V2_SIM2` (V2 simulator on V1's own rates) is compared with `V1` on win and overtime Brier; the combination "V1_R_C1 rates through the V2 simulator" is *not* run here (V2 needs per-game hazard fits that are only available from 2023); this is an explicit gap and is listed under evidence still required.

## Reported regardless of outcome

Levels and paired deltas with game- and slate-clustered 95% intervals for every arm and metric, pooled and per season; reliability tables and ECE; selected hyper-parameters and the full selection grids; whether any selection sits on a grid boundary (if so the grid is *reported as binding*, not silently widened again); ablations; negative results.

## Limits (stated up front)

* Retrospective vendor xG (MoneyPuck refits retroactively); no historical starting goalies, lineups or injuries; Kalshi history only for 2025-26.
* The tuning objective (goals log-likelihood) is not the evaluation objective (Brier/RPS), as in the OA study; it is kept for comparability.
* NHL outcomes are noisy: differences below ~0.001 Brier are unresolvable per season and are reported as such.
* The FAMILY_SEEN tier cannot confirm anything on its own; only FRESH (low power) and PROSPECTIVE (not yet available) can.

## What this does not decide

This study ranks candidates on history. It does not promote anything. A candidate would additionally need the scorecard gates (calibration, runtime, freshness, SIFT-contract compatibility), a market-matched comparison and a prospective non-regression record from a frozen shadow arm, and explicit approval.
