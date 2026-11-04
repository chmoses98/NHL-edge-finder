# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 3563 · late records excluded 0 · scored (dressed) 2853 · candidates who did not dress 544 · awaiting the official result 166 · paired with the incumbent's pregame forecast 2686
* **verdict: INCONCLUSIVE AT n=2686 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 2686 | +0.0274 | 1.0125 | 1.2997 | 0.6767 | 0.12992 | 0.805 |
| WORKLOAD_V1_RAW | 2686 | +0.0664 | 1.0184 | 1.3007 | 0.6775 | 0.13008 | 0.804 |
| CHAMPION | 2686 | -0.0501 | 1.0093 | 1.3072 | 0.6804 | 0.13065 | 0.784 |
| BASELINE | 2686 | +0.0560 | 1.0353 | 1.3196 | 0.6898 | 0.13251 | 0.787 |
| CHAMPION_NB | 2686 | -0.0501 | 1.0093 | 1.3072 | 0.6809 | 0.13077 | 0.809 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00081 [-0.00168, +0.00004] | -0.00096 [-0.00274, +0.00068] |
| CHAMPION | -0.00374 [-0.00744, -0.00033] | -0.00745 [-0.01394, -0.00106] |
| BASELINE | -0.01308 [-0.01845, -0.00795] | -0.01988 [-0.02886, -0.01128] |
| CHAMPION_NB | -0.00420 [-0.00786, -0.00063] | -0.00746 [-0.01394, -0.00106] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=FAIL, crps_give_back_le_0.001=PASS
