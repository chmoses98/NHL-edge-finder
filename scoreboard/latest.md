# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 6094 · late records excluded 0 · scored (dressed) 4717 · candidates who did not dress 881 · awaiting the official result 496 · paired with the incumbent's pregame forecast 4418
* **verdict: INCONCLUSIVE AT n=4418 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 4418 | +0.0167 | 1.0123 | 1.3034 | 0.6795 | 0.12997 | 0.803 |
| WORKLOAD_V1_RAW | 4418 | +0.0569 | 1.0180 | 1.3038 | 0.6800 | 0.13008 | 0.802 |
| CHAMPION | 4418 | -0.0642 | 1.0110 | 1.3143 | 0.6849 | 0.13100 | 0.779 |
| BASELINE | 4418 | +0.0423 | 1.0345 | 1.3229 | 0.6919 | 0.13241 | 0.785 |
| CHAMPION_NB | 4418 | -0.0642 | 1.0110 | 1.3143 | 0.6854 | 0.13116 | 0.805 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00055 [-0.00130, +0.00025] | -0.00038 [-0.00183, +0.00109] |
| CHAMPION | -0.00547 [-0.00891, -0.00207] | -0.01095 [-0.01674, -0.00503] |
| BASELINE | -0.01246 [-0.01655, -0.00834] | -0.01956 [-0.02639, -0.01283] |
| CHAMPION_NB | -0.00596 [-0.00931, -0.00244] | -0.01095 [-0.01674, -0.00503] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
