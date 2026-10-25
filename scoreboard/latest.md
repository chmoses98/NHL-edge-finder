# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 793 · late records excluded 0 · scored (dressed) 492 · candidates who did not dress 95 · awaiting the official result 206 · paired with the incumbent's pregame forecast 460
* **verdict: INCONCLUSIVE AT n=460 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 460 | +0.0132 | 1.0209 | 1.2910 | 0.6878 | 0.13337 | 0.792 |
| WORKLOAD_V1_RAW | 460 | +0.0511 | 1.0263 | 1.2930 | 0.6885 | 0.13351 | 0.792 |
| CHAMPION | 460 | -0.0593 | 1.0230 | 1.3045 | 0.6963 | 0.13506 | 0.772 |
| BASELINE | 460 | +0.0444 | 1.0355 | 1.3022 | 0.6953 | 0.13490 | 0.781 |
| CHAMPION_NB | 460 | -0.0593 | 1.0230 | 1.3045 | 0.6965 | 0.13509 | 0.796 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00072 [-0.00321, +0.00154] | -0.00206 [-0.00585, +0.00128] |
| CHAMPION | -0.00853 [-0.01358, -0.00321] | -0.01356 [-0.02301, -0.00310] |
| BASELINE | -0.00755 [-0.01888, +0.00466] | -0.01126 [-0.03059, +0.00862] |
| CHAMPION_NB | -0.00869 [-0.01473, -0.00226] | -0.01356 [-0.02301, -0.00310] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=FAIL
