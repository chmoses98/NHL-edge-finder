# WORKLOAD_V1_LC — results (preregistered in `LEVEL_CALIBRATION_PREREGISTRATION.md`, committed 2026-10-23T02:43Z before the run)

**RESEARCH_ONLY · DEVELOPMENT evidence only.** Nothing is promoted or wired anywhere; there is no Kalshi shots-on-goal market, so nothing here prices or routes a bet. Data: `level_calibration_2023_2024_2025.json`; code: `src/nhl_edge/research/workload_level_cal.py` (constants `H = 60 d`, `K = 1,000` shots, fixed in advance, not tuned); harness: `workload_replication` (derived champion stand-in), game-clustered bootstrap, 2,000 resamples.

## Result

| held-out season | WORKLOAD_V1 bias (uncorrected) | **LC bias** | LC CRPS | CRPS vs CHAMPION (95% CI) | CRPS vs uncorrected WORKLOAD_V1 (95% CI) | 80% coverage | development checks | original 7-check rule |
|---|---:|---:|---:|---|---|---:|---|---|
| 2023-24 (cleanest, but already scored) | +0.0525 | **+0.0009** | 0.7125 | −0.00666 [−0.00776, −0.00559] | −0.00050 [−0.00083, −0.00014] | 0.801 | all 5 pass | **ACCEPTED** (WORKLOAD_V1 itself was REJECTED here by 0.003) |
| 2024-25 (original validation season) | +0.0468 | **−0.0041** | 0.6883 | −0.00587 [−0.00682, −0.00493] | −0.00059 [−0.00093, −0.00026] | 0.799 | all 5 pass | ACCEPTED |
| 2025-26 | +0.0295 | **+0.0000** | 0.6829 | −0.00713 [−0.00820, −0.00606] | −0.00017 [−0.00038, +0.00003] | 0.801 | all 5 pass | ACCEPTED |

Verdict under the registered rule: **DEVELOPMENT-QUALIFIED** (|bias| ≤ 0.02, CRPS vs CHAMPION below zero, no give-back of accuracy (upper bound ≤ +0.0010), 80% coverage in [0.77, 0.83], no position worse than CHAMPION_NB — on each of the three seasons). The unchanged original acceptance rule also passes on all three seasons.

The level factor averages 0.970 / 0.969 / 0.981 (range 0.956–0.987): a 2–3% downward correction that tracks the falling league shot level; in the first week of each season it is already 0.98 because the previous season's outcomes carry over.

## What it does and does not show

* The level error of WORKLOAD_V1 was real, small and removable with one scalar and no tuning: bias goes from +0.03…+0.05 to within ±0.004 shots per skater-game, and CRPS improves slightly (−0.0002 to −0.0006; the 2025-26 interval touches zero).
* **It is development evidence, not confirmation.** All three seasons had already been scored by WORKLOAD_V1 and their biases motivated this design (disclosed in the preregistration); 2022-23 cannot be held out. The "original rule ACCEPTED" statement means the frozen thresholds were met on exposed data. It makes WORKLOAD_V1_LC eligible for a **prospective shadow test only**.
* Remaining structure the factor does not touch (descriptive): overtime games are still under-predicted (−0.04 to −0.07 shots per skater-game) and regulation games over-predicted (+0.01 to +0.02); PP and SH minute accuracy is unchanged; the dressed lineup is still taken from the box score (conditional on dressing).
* Deployment would need the settled box scores of previous days in the same pipeline (the settlement job already produces them); that was not exercised here.
* Independent session note: a separate structural challenger (role-anchored shrinkage, `WORKLOAD_V2`, PR #69) was preregistered and REJECTED by its own frozen rule; it is a different model and is not compared here.

## Evidence still required before any promotion

A frozen prospective shadow record (one scalar per day from settled outcomes), at least a full month of games with bias inside the preregistered limit and no CRPS give-back; a holdout season not used for design (none exists historically); and explicit approval. There is no market to test against, so this can only ever be a projection-quality promotion.
