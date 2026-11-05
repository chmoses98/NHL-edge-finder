# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 4026 · late records excluded 0 · scored (dressed) 2992 · candidates who did not dress 571 · awaiting the official result 463 · paired with the incumbent's pregame forecast 2817
* **verdict: INCONCLUSIVE AT n=2817 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 2817 | +0.0287 | 1.0106 | 1.2948 | 0.6748 | 0.12972 | 0.806 |
| WORKLOAD_V1_RAW | 2817 | +0.0680 | 1.0164 | 1.2958 | 0.6756 | 0.12987 | 0.805 |
| CHAMPION | 2817 | -0.0506 | 1.0083 | 1.3040 | 0.6793 | 0.13061 | 0.784 |
| BASELINE | 2817 | +0.0559 | 1.0333 | 1.3148 | 0.6878 | 0.13229 | 0.788 |
| CHAMPION_NB | 2817 | -0.0506 | 1.0083 | 1.3040 | 0.6798 | 0.13073 | 0.810 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00078 [-0.00160, +0.00005] | -0.00096 [-0.00257, +0.00065] |
| CHAMPION | -0.00454 [-0.00812, -0.00112] | -0.00912 [-0.01545, -0.00279] |
| BASELINE | -0.01298 [-0.01799, -0.00781] | -0.02001 [-0.02840, -0.01114] |
| CHAMPION_NB | -0.00502 [-0.00867, -0.00148] | -0.00912 [-0.01545, -0.00279] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=FAIL, crps_give_back_le_0.001=PASS
