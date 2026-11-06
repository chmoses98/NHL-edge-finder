# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 4148 · late records excluded 0 · scored (dressed) 3384 · candidates who did not dress 642 · awaiting the official result 122 · paired with the incumbent's pregame forecast 3191
* **verdict: INCONCLUSIVE AT n=3191 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 3191 | +0.0195 | 1.0100 | 1.2945 | 0.6759 | 0.13004 | 0.804 |
| WORKLOAD_V1_RAW | 3191 | +0.0592 | 1.0158 | 1.2952 | 0.6765 | 0.13015 | 0.804 |
| CHAMPION | 3191 | -0.0590 | 1.0057 | 1.3012 | 0.6786 | 0.13055 | 0.784 |
| BASELINE | 3191 | +0.0490 | 1.0306 | 1.3115 | 0.6868 | 0.13219 | 0.788 |
| CHAMPION_NB | 3191 | -0.0590 | 1.0057 | 1.3013 | 0.6794 | 0.13072 | 0.810 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00058 [-0.00134, +0.00024] | -0.00069 [-0.00219, +0.00084] |
| CHAMPION | -0.00269 [-0.00613, +0.00079] | -0.00675 [-0.01292, -0.00066] |
| BASELINE | -0.01088 [-0.01555, -0.00600] | -0.01702 [-0.02494, -0.00897] |
| CHAMPION_NB | -0.00342 [-0.00692, +0.00004] | -0.00675 [-0.01292, -0.00066] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=FAIL, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=FAIL, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
