# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 5557 · late records excluded 0 · scored (dressed) 4369 · candidates who did not dress 816 · awaiting the official result 372 · paired with the incumbent's pregame forecast 4121
* **verdict: INCONCLUSIVE AT n=4121 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 4121 | +0.0218 | 1.0112 | 1.3012 | 0.6779 | 0.12967 | 0.803 |
| WORKLOAD_V1_RAW | 4121 | +0.0618 | 1.0171 | 1.3018 | 0.6785 | 0.12980 | 0.803 |
| CHAMPION | 4121 | -0.0586 | 1.0087 | 1.3114 | 0.6828 | 0.13060 | 0.780 |
| BASELINE | 4121 | +0.0480 | 1.0325 | 1.3204 | 0.6899 | 0.13204 | 0.786 |
| CHAMPION_NB | 4121 | -0.0587 | 1.0087 | 1.3114 | 0.6833 | 0.13076 | 0.807 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00064 [-0.00140, +0.00013] | -0.00055 [-0.00214, +0.00093] |
| CHAMPION | -0.00493 [-0.00850, -0.00143] | -0.01018 [-0.01624, -0.00395] |
| BASELINE | -0.01206 [-0.01616, -0.00768] | -0.01914 [-0.02608, -0.01190] |
| CHAMPION_NB | -0.00542 [-0.00901, -0.00183] | -0.01018 [-0.01624, -0.00395] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=FAIL, crps_give_back_le_0.001=PASS
