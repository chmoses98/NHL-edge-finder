# Challenger-to-champion promotion scorecard

> RESEARCH_ONLY · predefined 2026-10-22 and implemented in `src/nhl_edge/research/promotion.py` (thresholds are constants in code; they change only by a documented decision, never after a result is seen). The scorecard **recommends**; a human merges the PR that changes a champion. Nothing here touches betting: a projection promotion never changes a price, stake, cap or order path, and expression research stays separate and PASS-by-default.

One published projection per **target**; different approved models may serve different targets; no competing unexplained numbers. A challenger is scored per target against that target's incumbent.

| gate | requirement (all must hold) |
|---|---|
| G1 improvement | paired primary-metric Δ vs incumbent on **unexposed** chronological test seasons, 95% interval excludes 0 in favour under **both** the game bootstrap and the date-cluster bootstrap (97.5% when two primaries are registered) |
| G2 meaningful | \|Δ\| ≥ 0.0010 Brier, 0.0020 log loss, 0.0050 RPS (goals) |
| G3 no regression | every other metric of the family and every other major family: interval upper bound ≤ the same non-inferiority margin |
| G4 calibration | ECE ≤ incumbent + 0.005; 80% interval coverage in [0.77, 0.83] for distributions |
| G5 sample | ≥ 3 unexposed seasons and ≥ 3,000 games (≥ 30,000 player-games for player targets) |
| G6 stability | favourable point estimate in ≥ 2/3 of unexposed seasons, none significantly worse; exposed seasons not significantly worse |
| G7 runtime | ≤ 300 s per slate inside the worker's budget; inputs available at the pregame cutoff |
| G8 reproducible | frozen parameters + seed regenerate predictions bit-for-bit; deterministic training |
| G9 SIFT contract | published fields unchanged or additive per `edge_finder.app.v1`; contract tests pass |
| G10 live non-inferior | from the day a shadow arm runs, the rolling live paired Δ is not significantly worse (automatic demotion if it is) |

Verdicts: `PROMOTE_CANDIDATE` (all pass), `SHADOW_MORE` (history passes; a gate needing live data or an artifact is pending), `RETAIN_INCUMBENT` (a hard gate fails; failing gates are listed). Market-informed forecasts are labelled and compared separately; a model with any market input is never presented as independent.

## Current champion registry (2026-10-22)

| target | published champion | candidate(s) | scorecard | note |
|---|---|---|---|---|
| game win probability | `DATA_ONLY_V1` (market-anchored variant labelled `MARKET_ANCHORED_V1`) | `OA_SVA_C1` | **SHADOW_MORE** — G1–G8 pass on 7,157 unexposed games; G9/G10 pending; but ~2/3 of the gain is re-tuning V1's constants and the exposed seasons show ≈ 0.0007 (n.s.) | `OA_SVA` RETAIN (fails G3 on totals). A re-tuned + recalibrated V1 (`V1_T_C1`) is statistically tied with `OA_SVA_C1` (−0.0004 [−0.0009, +0.0001]); prefer the simpler model if a promotion is ever proposed |
| total-goal distribution | `DATA_ONLY_V1` | `OA_SVA_C1` (neutral) | RETAIN — no improvement | totals carry little signal; V1 beats league avg only in 2018–23 |
| goal-margin distribution | `DATA_ONLY_V1` | `OA_SVA_C1` | G1 passes (RPS −0.0111 unexposed) but exposed n.s. | would ride with the win-probability decision |
| overtime / regulation tie | `DATA_ONLY_V1` (known defect: 17.5% vs 22.0%) | `nhl-sim-2.0` on V1 rates (`SIM2`) | **SHADOW_MORE** — pooled 2023–25 Δ −0.0022 [−0.0032, −0.0011], no regression; only 1 unexposed season (G5 unmet); V2 already in live shadow | highest-value pending fix |
| skater shots / TOI / PP TOI | `PLAYER_SIM_V1` (packet) and `pf-nhl-1.0.0` (projection foundation, shadow) | `WORKLOAD_V1` | **RETAIN** — frozen rule failed on 2023-24 (bias +0.053 vs ≤ 0.05) though CRPS gain replicated (−0.8…−1.0%) | `pf-nhl` reports its own gate/holdout evidence |
| points / assists / goals (distribution input) | `PLAYER_SIM_V1` / `pf-nhl` | — | not re-scored here | goals never drive a betting recommendation |
| goalie saves | `PLAYER_SIM_V1` / `pf-nhl` | `WORKLOAD_V1` (rejected) | RETAIN | pull-hazard mixture is the registered next idea |

If no challenger qualifies the incumbent stays and the reason is recorded here. Nothing was promoted on 2026-10-22.
