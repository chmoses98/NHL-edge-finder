# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 1383 · late records excluded 0 · scored (dressed) 770 · candidates who did not dress 147 · awaiting the official result 466 · paired with the incumbent's pregame forecast 723
* **verdict: INCONCLUSIVE AT n=723 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 723 | +0.0138 | 1.0095 | 1.2927 | 0.6837 | 0.13239 | 0.798 |
| WORKLOAD_V1_RAW | 723 | +0.0513 | 1.0158 | 1.2948 | 0.6845 | 0.13254 | 0.797 |
| CHAMPION | 723 | -0.0747 | 1.0120 | 1.3120 | 0.6944 | 0.13454 | 0.777 |
| BASELINE | 723 | +0.0261 | 1.0214 | 1.3067 | 0.6915 | 0.13397 | 0.788 |
| CHAMPION_NB | 723 | -0.0747 | 1.0120 | 1.3120 | 0.6951 | 0.13466 | 0.800 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00079 [-0.00244, +0.00078] | -0.00204 [-0.00470, +0.00041] |
| CHAMPION | -0.01062 [-0.01633, -0.00467] | -0.01929 [-0.03013, -0.00849] |
| BASELINE | -0.00777 [-0.01709, +0.00179] | -0.01393 [-0.02944, +0.00205] |
| CHAMPION_NB | -0.01138 [-0.01721, -0.00558] | -0.01928 [-0.03013, -0.00849] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
