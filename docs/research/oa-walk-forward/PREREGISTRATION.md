# OA_RIDGE walk-forward — preregistration

> RESEARCH_ONLY · written 2026-10-22 before any full-sample result of the arms below exists. Committed to git before the full run; the commit time is the registration time. Nothing here changes a production number, a price, a stake or a cap.

## Why this experiment

`DATA_ONLY_V1`'s team ratings (`features/ratings.py::team_rating`) are recency-weighted *raw* xG per 60. They are not adjusted for the opponents a team has faced, and `off_A × def_B` is then multiplied again. The earlier model-improvement work found V1 beats a league-average model for *who wins* and the margin but adds nothing for *how many goals*, and trails the Kalshi mid by ~0.0014–0.0017 Brier. This experiment tests whether replacing **only** the rating component by a ridge-regularised opponent-adjusted fit improves proper scores on historical games. Simulator, home advantage, back-to-back terms, V1's finishing ratio and per-game seeds are held identical, so any difference is attributable to expected goals alone.

## Arms (fixed in advance)

| arm | rating |
|---|---|
| `V1` | incumbent, goalie term off (no point-in-time starters exist for history) |
| `OA_SVA` | **lead challenger.** Weighted ridge on MoneyPuck score- and venue-adjusted xG/60 (`scoreVenueAdjustedxGoalsFor`), team attack + opponent defence effects + home effect |
| `OA_XG` | same on raw `xGoalsFor` (exploratory) |
| `OA_SVA_G25` | `OA_SVA` with 25% of the effect taken from a goals-based fit (exploratory) |
| `LEAGUE` | league-average lambdas + home advantage only (reference) |

Hyper-parameters (half-life, ridge strength, season discount) are chosen **per test season and per arm** from the two seasons *before* it, by Poisson goals log-likelihood of games each rated from earlier rows only (grid in `oa_model.py`, fixed here: half-life {60,120,240,480} d; ridge {5,15,30,60} pseudo-games; season discount {0.25,0.4,0.55,0.7}). A season's own games are never used to choose anything for it.

## Data tiers

* Source: MoneyPuck team game rows and official NHL results in `data/history` (seasons pulled by the `history` workflow; reconstructed-from-archive vs. truly archived: **all of this is retrospective vendor data**, not point-in-time archived snapshots — see Limits).
* **Unexposed test seasons** (no prior V1/V2 analysis looked at them): 2018–2023 (MoneyPuck start-year convention). 2019 (pandemic-shortened) and 2020 (56-game, no-crowd) are kept and reported separately as different regimes, not dropped.
* **Exposed test seasons**: 2024, 2025. The earlier V1/V2 research inspected these descriptively on the full sample, and a 200-game early-2024 smoke run of this code (to check wiring, results not read for decisions) touched them. They are reported, never used for selection, and cannot be the sole basis of a claim.
* **Prospective tier**: 2026-27 games after 2026-10-21T17:13:05Z are not read by any code in this experiment (the earlier M-LIVE-1 look consumed the games before that instant).

## Hypotheses and decision rule (set before looking)

Primary metrics, challenger minus incumbent, paired on the same games, negative = better: H1 Brier of P(home win); H2 RPS of the total-goal distribution; H3 Brier of P(overtime). Only `OA_SVA` is a primary challenger (so three primary tests; the other arms are exploratory and labelled as such).

`OA_SVA` is **DEVELOPMENT-QUALIFIED** only if, pooled over the unexposed seasons: (a) the 95% interval of H1 excludes zero in its favour under *both* the game bootstrap and the date-cluster bootstrap; (b) no primary metric is worse with an interval excluding zero; (c) the H1 point estimate is favourable in at least 4 of the 6 unexposed seasons; (d) the pooled H1 gain is at least 0.0010 Brier ("practically meaningful"); (e) the exposed seasons are not significantly worse. Anything less is reported as NOT QUALIFIED, with the numbers.

Qualification is a precondition for promotion, not promotion: the promotion scorecard (`PROMOTION_SCORECARD.md`) additionally needs calibration, runtime/freshness, SIFT-contract compatibility, a market-matched comparison where Kalshi history exists (2025-26 only), and a prospective non-regression check as the live archive accumulates.

## Reported regardless of outcome

Levels and paired deltas with game- and date-clustered 95% intervals for every arm and metric, per season and pooled; reliability tables; the selected hyper-parameters and the full selection grids; the negative results.

## Limits (stated up front)

* No point-in-time starting goalies for history, so the incumbent's live goalie term is off in every arm; live performance is not what this measures.
* Vendor xG models are refit retroactively; MoneyPuck values for past games are as published today, not as available on the day.
* No market data before 2025-26: this experiment says whether the *independent* model improves, not whether it beats a market (the market comparison is a separate analysis on the 2025-26 Kalshi history).
* NHL game outcomes are very noisy; differences below ~0.001 Brier are unresolvable at these sample sizes and are reported as such.

## Amendment 1 — 2026-10-22, written after a first look at the EXPOSED seasons (2024–2025) and before any unexposed-season result exists

What was seen: a first run of the original arms on 2024–2025 only (exposed by design). Pooled paired deltas vs V1: win-probability Brier −0.0011 [−0.0021, −0.0001] (OA_XG) and −0.0012 [−0.0024, −0.0001] (OA_SVA); but total-goal RPS **worse** by +0.0037 [+0.0003, +0.0072] / +0.0039 [+0.0006, +0.0074]; overtime Brier unchanged. The league-constant arm matched V1 on total-goal RPS (1.2895 vs 1.2896), i.e. total-goal differentiation has no value, and the opponent-adjusted ratings only add spread to totals. This is the same pattern the earlier work reported for V1 (calibration slope ≈ 0.37 on totals, ≈ 1.39 on margins).

Changes (all decided before any unexposed season is run, and therefore **design choices informed by exposed data, not tests of them**):

1. **Grid** extended: ridge {1, 2.5, 5, 15, 30, 60}, season discount {0.1, 0.25, 0.4, 0.55, 0.7} (the validation optimum sat on the old boundary in prior-season tuning). Half-life grid unchanged.
2. **Arm `OA_SVA_G25` dropped** (no gain, worse totals). **Exploratory arms added**: `V1_C1` and `OA_SVA_C1`, which recalibrate the *sum* and *difference* of the two expected-goal rates by slope-only regression on the arm's own strictly prior predictions (`SlopeCalibrator`; slopes clipped to [0.2, 2.0], 300-game burn-in, same-day games never inform each other, no level recalibration). `V1_C1` re-tests the earlier C1 idea on the same machinery so that a gain from calibration is not credited to the new ratings.
3. **Two primary challengers**: `OA_SVA` and `OA_SVA_C1` (H1–H3 for each). To keep family-wise error controlled the DEVELOPMENT-QUALIFIED gate (a) must hold at the **97.5%** level (Bonferroni for two primaries) under both bootstraps; `oa_evaluate` reports those intervals (`lo975/hi975`, `lo975_slate/hi975_slate`). Gates (b)–(e) are unchanged. Plain `OA_SVA` is expected to fail (b) on totals; that is reported, not hidden.
4. `OA_XG`, `V1_C1`, `LEAGUE` remain exploratory/reference.

Nothing else changes: same unexposed seasons, same metrics, same tuning-on-prior-seasons rule, same promotion preconditions.
