# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 5025 · late records excluded 0 · scored (dressed) 3981 · candidates who did not dress 747 · awaiting the official result 297 · paired with the incumbent's pregame forecast 3760
* **verdict: INCONCLUSIVE AT n=3760 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 3760 | +0.0112 | 1.0073 | 1.2953 | 0.6759 | 0.12946 | 0.805 |
| WORKLOAD_V1_RAW | 3760 | +0.0513 | 1.0129 | 1.2955 | 0.6763 | 0.12953 | 0.804 |
| CHAMPION | 3760 | -0.0677 | 1.0056 | 1.3061 | 0.6810 | 0.13042 | 0.782 |
| BASELINE | 3760 | +0.0399 | 1.0287 | 1.3143 | 0.6876 | 0.13176 | 0.788 |
| CHAMPION_NB | 3760 | -0.0677 | 1.0056 | 1.3061 | 0.6819 | 0.13064 | 0.808 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00037 [-0.00113, +0.00039] | -0.00023 [-0.00176, +0.00128] |
| CHAMPION | -0.00511 [-0.00860, -0.00158] | -0.01084 [-0.01667, -0.00451] |
| BASELINE | -0.01172 [-0.01621, -0.00731] | -0.01909 [-0.02650, -0.01172] |
| CHAMPION_NB | -0.00594 [-0.00934, -0.00242] | -0.01084 [-0.01667, -0.00451] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
