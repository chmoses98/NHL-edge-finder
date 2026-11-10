# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 5310 · late records excluded 0 · scored (dressed) 4122 · candidates who did not dress 775 · awaiting the official result 413 · paired with the incumbent's pregame forecast 3894
* **verdict: INCONCLUSIVE AT n=3894 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 3894 | +0.0100 | 1.0064 | 1.2959 | 0.6758 | 0.12934 | 0.805 |
| WORKLOAD_V1_RAW | 3894 | +0.0501 | 1.0119 | 1.2961 | 0.6762 | 0.12941 | 0.805 |
| CHAMPION | 3894 | -0.0689 | 1.0058 | 1.3078 | 0.6817 | 0.13045 | 0.782 |
| BASELINE | 3894 | +0.0389 | 1.0290 | 1.3159 | 0.6882 | 0.13178 | 0.787 |
| CHAMPION_NB | 3894 | -0.0689 | 1.0058 | 1.3078 | 0.6825 | 0.13067 | 0.808 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00034 [-0.00108, +0.00039] | -0.00013 [-0.00155, +0.00128] |
| CHAMPION | -0.00584 [-0.00942, -0.00255] | -0.01189 [-0.01799, -0.00589] |
| BASELINE | -0.01239 [-0.01678, -0.00793] | -0.02003 [-0.02770, -0.01248] |
| CHAMPION_NB | -0.00667 [-0.01013, -0.00334] | -0.01189 [-0.01799, -0.00589] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
