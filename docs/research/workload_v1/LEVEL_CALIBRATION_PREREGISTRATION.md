# WORKLOAD_V1_LC — preregistration (2026-10-23): rolling level calibration of the skater shot mean

**Authority: RESEARCH_ONLY.** Nothing is promoted, wired into production, or used for pricing; there is no Kalshi shots-on-goal market. The existing WORKLOAD_V1 acceptance rule (`preregistration.json`, seven checks including `|bias| ≤ 0.05`) is **not changed or weakened**; WORKLOAD_V1 itself stays REJECTED on 2023-24 (`WORKLOAD_V1_REPLICATION.md`). This document registers one new challenger, committed **before** it is run.

## Why

The replication found WORKLOAD_V1's gain over the production expected-SOG replicates in three seasons (CRPS −0.5% … −1.0%) but its mean over-predicts by +0.053 / +0.047 / +0.030 shots per skater-game (2023-24 / 2024-25 / 2025-26; 2–3% of the mean) while the league mean fell 1.683 → 1.571 → 1.546. The model's league-relative rates use a trailing window (10,000 skater-games) and long player memories (half-life 80 games), so they lag a falling level. A level error is a one-dimensional defect: it should be repairable without touching the structure that produced the gain.

## Challenger (fixed in advance; no tuning)

`WORKLOAD_V1_LC` = WORKLOAD_V1's predictive mean for every skater-game multiplied by a scalar `f(D)` that depends only on games dated **strictly before** D:

```
f(D) = ( Σ_i w_i · y_i  +  K ) / ( Σ_i w_i · ŷ_i  +  K ),    w_i = 0.5 ^ ((D − date_i) / H),   i over all scored skater-games dated < D
```

with `H = 60 days` and `K = 1,000` shots (a pseudo-observation of ratio 1, i.e. roughly 0.6 game-days of shots). `ŷ_i` is the **uncorrected** WORKLOAD_V1 mean; `y_i` the official SOG. The calibration history includes the preceding season's games (their outcomes are final before the evaluated season starts), so there is no cold start in October. Nothing else changes: the same frozen parameters, minutes, rates, opponent factor and the same NegBin dispersion rule (fitted on the previous season's residuals of **this arm's** corrected means). `H` and `K` were chosen from first principles (about two months of memory; a prior worth under one game-day) and are **not** tuned on any season.

## Evaluation

Seasons 2023-24, 2024-25 (validation season of the original design: not independent) and 2025-26, with the replication harness (`workload_replication`, derived champion stand-in, game-clustered bootstrap 2,000 resamples, seed 20261012). Arms: CHAMPION, CHAMPION_NB, WORKLOAD_V1, WORKLOAD_V1_LC.

## Decision rules (set before running)

* **DEVELOPMENT-QUALIFIED** only if, on **each** of the three seasons: (a) `|bias| ≤ 0.02` shots per skater-game (stricter than the original 0.05 limit); (b) CRPS vs CHAMPION has a 95% interval entirely below zero; (c) CRPS(LC) − CRPS(WORKLOAD_V1) has an upper bound ≤ +0.0010 (the correction must not give back the accuracy gain); (d) 80% PIT coverage in [0.77, 0.83]; (e) CRPS no worse than CHAMPION_NB for forwards and for defencemen.
* The original seven-check rule is also computed and reported for each season (`accept_skaters` on the LC arm) so that a pass is on the record under the unchanged rule; a pass there is necessary for any shadow-test eligibility, never sufficient for promotion.
* Anything else is reported as NOT QUALIFIED with the numbers.

## Disclosures and limits

* All three seasons have already been scored by WORKLOAD_V1 and their biases were looked at (they motivate this design). Therefore **every historical result here is development evidence**; 2022-23 cannot be held out (no feasible training/dispersion seasons). Confirmation requires a prospective shadow record, which does not exist yet.
* A level factor corrects the *average* error; it can hide a skater-specific mis-allocation. Subgroup biases (position, overtime, home/away) are reported descriptively.
* The correction needs the realised outcomes of earlier games in the same pipeline; in a live setting it needs the settled box scores of the previous days (the settlement job already provides them) — a deployment concern, not tested here.
* Skater shots only; goalie saves (REJECTED originally) are out of scope.
