# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 2933 · late records excluded 0 · scored (dressed) 2321 · candidates who did not dress 448 · awaiting the official result 164 · paired with the incumbent's pregame forecast 2180
* **verdict: INCONCLUSIVE AT n=2180 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 2180 | +0.0244 | 1.0092 | 1.3001 | 0.6765 | 0.12974 | 0.804 |
| WORKLOAD_V1_RAW | 2180 | +0.0628 | 1.0149 | 1.3009 | 0.6772 | 0.12988 | 0.803 |
| CHAMPION | 2180 | -0.0557 | 1.0082 | 1.3111 | 0.6817 | 0.13077 | 0.782 |
| BASELINE | 2180 | +0.0507 | 1.0336 | 1.3224 | 0.6906 | 0.13255 | 0.787 |
| CHAMPION_NB | 2180 | -0.0557 | 1.0082 | 1.3111 | 0.6824 | 0.13094 | 0.808 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00071 [-0.00165, +0.00018] | -0.00080 [-0.00265, +0.00099] |
| CHAMPION | -0.00522 [-0.00927, -0.00118] | -0.01106 [-0.01796, -0.00381] |
| BASELINE | -0.01416 [-0.01963, -0.00870] | -0.02229 [-0.03142, -0.01301] |
| CHAMPION_NB | -0.00597 [-0.01003, -0.00176] | -0.01106 [-0.01796, -0.00381] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=FAIL, crps_give_back_le_0.001=PASS
