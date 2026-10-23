# WORKLOAD_V2 — preregistered held-out result (RESEARCH_ONLY)

Preregistration: `PREREGISTRATION.md` (commit `ecbb5653`, written before any result was computed).
Run: `python -m nhl_edge.research.workload_v2 --seasons 2023,2024,2025` (raw output: `results.json`).
Nothing in this document changes a model, a price, a stake, a cap or an authority. No promotion is requested.

## Verdict under the frozen rule: **REJECTED**

The rule required every check to pass in **every** one of the three held-out seasons.

| Season | Verdict | Failed check |
|---|---|---|
| 2023 | REJECTED | `abs_tier_bias_le_max` (max |tier bias| 0.092 > 0.06, lowest-shot-rate tier) |
| 2024 | ACCEPTED | – |
| 2025 | ACCEPTED | – |

The tier-bias check was added in the preregistration precisely because V1's global bias looked acceptable
while the bias by predicted-shot tier did not. It was not loosened after seeing the 2023 number and is not
loosened here. Any further variant needs a new preregistration; a retrofit would not count as evidence.

## What the data say (development evidence, not a promotion argument)

Signed shot bias by predicted-shot tier (0 = lowest predicted rate, 4 = highest), mean predicted minus actual SOG:

| Season | Arm | T0 | T1 | T2 | T3 | T4 |
|---|---|---|---|---|---|---|
| 2023 | CHAMPION | +0.052 | −0.027 | −0.093 | −0.137 | −0.115 |
| 2023 | WORKLOAD_V1 | +0.129 | +0.071 | +0.037 | +0.024 | +0.002 |
| 2023 | WORKLOAD_V2 | +0.092 | +0.045 | +0.029 | +0.035 | +0.019 |
| 2024 | WORKLOAD_V2 | +0.055 | +0.034 | +0.025 | +0.052 | +0.023 |
| 2025 | WORKLOAD_V2 | +0.048 | +0.044 | −0.008 | +0.008 | +0.003 |

* V2 improves on V1 in every season on every score with bootstrap intervals excluding zero
  (CRPS −0.0008/−0.0006/−0.0008, ladder Brier −0.00016/−0.00013/−0.00015, |bias| −0.009/−0.009/−0.011).
* V2 beats the CHAMPION (negative-binomial) on CRPS in every season, interval excluding zero
  (2023 −0.0073, 2024 −0.0057, 2025 −0.0078 vs CHAMPION_NB), and the CHAMPION's mid/high-tier under-prediction
  (−0.09 to −0.15) is removed.
* The remaining defect is a **low-tier over-prediction** (T0 +0.05 to +0.09): the shrinkage anchor still lifts
  the lowest-usage skaters. 2023 is worst because its training window (2021–22) is shortest and holds the
  fewest role-prior rows. 2024 and 2025 pass with margin of only 0.005–0.012 on that check.
* The error source named in `DIAGNOSIS.md` (the anchor at 1.0 ignoring role) is therefore partly but not fully
  fixed. The ice-time side is already fixed by WORKLOAD_V1's minutes model (total-TOI bias ≈ 0 vs −0.2 to −0.37 min for the champion).

## What would be needed next

1. A **new** preregistered variant targeting low-usage skaters (for example a minutes-conditional floor on the
   shrunk index), registered before it is scored, with the same 0.06 tier threshold.
2. Fresh held-out seasons: 2026 data once available. 2023–2025 are now exposed to this family of models.
3. Only then does the standing promotion scorecard apply; a human decides.

The existing acceptance threshold was not weakened.
