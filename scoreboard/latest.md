# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 6676 · late records excluded 0 · scored (dressed) 5067 · candidates who did not dress 946 · awaiting the official result 663 · paired with the incumbent's pregame forecast 4739
* **verdict: INCONCLUSIVE AT n=4739 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 4739 | +0.0147 | 1.0128 | 1.3029 | 0.6799 | 0.13020 | 0.803 |
| WORKLOAD_V1_RAW | 4739 | +0.0550 | 1.0184 | 1.3033 | 0.6805 | 0.13030 | 0.802 |
| CHAMPION | 4739 | -0.0655 | 1.0111 | 1.3132 | 0.6851 | 0.13119 | 0.779 |
| BASELINE | 4739 | +0.0413 | 1.0336 | 1.3212 | 0.6916 | 0.13250 | 0.785 |
| CHAMPION_NB | 4739 | -0.0655 | 1.0111 | 1.3132 | 0.6857 | 0.13136 | 0.805 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00051 [-0.00122, +0.00024] | -0.00043 [-0.00181, +0.00091] |
| CHAMPION | -0.00517 [-0.00849, -0.00188] | -0.01035 [-0.01611, -0.00471] |
| BASELINE | -0.01166 [-0.01542, -0.00772] | -0.01828 [-0.02475, -0.01141] |
| CHAMPION_NB | -0.00578 [-0.00912, -0.00241] | -0.01035 [-0.01611, -0.00471] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
