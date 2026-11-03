# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 3397 · late records excluded 0 · scored (dressed) 2463 · candidates who did not dress 470 · awaiting the official result 464 · paired with the incumbent's pregame forecast 2317
* **verdict: INCONCLUSIVE AT n=2317 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 2317 | +0.0298 | 1.0091 | 1.3001 | 0.6760 | 0.12965 | 0.804 |
| WORKLOAD_V1_RAW | 2317 | +0.0684 | 1.0150 | 1.3011 | 0.6768 | 0.12982 | 0.804 |
| CHAMPION | 2317 | -0.0509 | 1.0066 | 1.3095 | 0.6803 | 0.13048 | 0.783 |
| BASELINE | 2317 | +0.0561 | 1.0328 | 1.3223 | 0.6900 | 0.13243 | 0.787 |
| CHAMPION_NB | 2317 | -0.0509 | 1.0066 | 1.3095 | 0.6809 | 0.13064 | 0.809 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00086 [-0.00176, +0.00003] | -0.00102 [-0.00277, +0.00067] |
| CHAMPION | -0.00427 [-0.00817, -0.00028] | -0.00948 [-0.01649, -0.00233] |
| BASELINE | -0.01406 [-0.01972, -0.00852] | -0.02229 [-0.03190, -0.01266] |
| CHAMPION_NB | -0.00492 [-0.00900, -0.00085] | -0.00948 [-0.01649, -0.00233] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=FAIL, crps_give_back_le_0.001=PASS
