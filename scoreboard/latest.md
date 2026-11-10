# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 5310 · late records excluded 0 · scored (dressed) 4228 · candidates who did not dress 797 · awaiting the official result 285 · paired with the incumbent's pregame forecast 3992
* **verdict: INCONCLUSIVE AT n=3992 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 3992 | +0.0122 | 1.0104 | 1.3005 | 0.6780 | 0.12965 | 0.804 |
| WORKLOAD_V1_RAW | 3992 | +0.0523 | 1.0160 | 1.3007 | 0.6784 | 0.12973 | 0.803 |
| CHAMPION | 3992 | -0.0680 | 1.0092 | 1.3121 | 0.6837 | 0.13072 | 0.780 |
| BASELINE | 3992 | +0.0392 | 1.0325 | 1.3202 | 0.6902 | 0.13204 | 0.786 |
| CHAMPION_NB | 3992 | -0.0680 | 1.0092 | 1.3121 | 0.6843 | 0.13091 | 0.806 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00040 [-0.00119, +0.00039] | -0.00014 [-0.00165, +0.00134] |
| CHAMPION | -0.00567 [-0.00906, -0.00200] | -0.01164 [-0.01763, -0.00520] |
| BASELINE | -0.01221 [-0.01630, -0.00795] | -0.01965 [-0.02668, -0.01247] |
| CHAMPION_NB | -0.00632 [-0.00979, -0.00265] | -0.01164 [-0.01763, -0.00520] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
