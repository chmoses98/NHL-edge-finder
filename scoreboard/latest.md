# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 2141 · late records excluded 0 · scored (dressed) 1691 · candidates who did not dress 328 · awaiting the official result 122 · paired with the incumbent's pregame forecast 1594
* **verdict: INCONCLUSIVE AT n=1594 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 1594 | +0.0253 | 1.0091 | 1.2827 | 0.6745 | 0.13046 | 0.802 |
| WORKLOAD_V1_RAW | 1594 | +0.0631 | 1.0148 | 1.2837 | 0.6752 | 0.13059 | 0.801 |
| CHAMPION | 1594 | -0.0555 | 1.0083 | 1.2963 | 0.6812 | 0.13178 | 0.781 |
| BASELINE | 1594 | +0.0499 | 1.0310 | 1.3038 | 0.6874 | 0.13301 | 0.786 |
| CHAMPION_NB | 1594 | -0.0555 | 1.0083 | 1.2963 | 0.6818 | 0.13190 | 0.806 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00066 [-0.00179, +0.00049] | -0.00105 [-0.00328, +0.00110] |
| CHAMPION | -0.00669 [-0.01134, -0.00208] | -0.01358 [-0.02217, -0.00526] |
| BASELINE | -0.01290 [-0.01956, -0.00622] | -0.02112 [-0.03244, -0.00971] |
| CHAMPION_NB | -0.00726 [-0.01192, -0.00250] | -0.01358 [-0.02217, -0.00526] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=FAIL, crps_give_back_le_0.001=PASS
