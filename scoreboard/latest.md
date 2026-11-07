# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 4644 · late records excluded 0 · scored (dressed) 3558 · candidates who did not dress 669 · awaiting the official result 417 · paired with the incumbent's pregame forecast 3358
* **verdict: INCONCLUSIVE AT n=3358 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 3358 | +0.0193 | 1.0093 | 1.2913 | 0.6752 | 0.12990 | 0.804 |
| WORKLOAD_V1_RAW | 3358 | +0.0592 | 1.0150 | 1.2919 | 0.6758 | 0.13001 | 0.803 |
| CHAMPION | 3358 | -0.0605 | 1.0054 | 1.2989 | 0.6785 | 0.13052 | 0.782 |
| BASELINE | 3358 | +0.0471 | 1.0302 | 1.3085 | 0.6861 | 0.13205 | 0.787 |
| CHAMPION_NB | 3358 | -0.0605 | 1.0054 | 1.2989 | 0.6793 | 0.13071 | 0.808 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00053 [-0.00133, +0.00024] | -0.00059 [-0.00209, +0.00088] |
| CHAMPION | -0.00324 [-0.00665, +0.00015] | -0.00760 [-0.01350, -0.00149] |
| BASELINE | -0.01090 [-0.01552, -0.00613] | -0.01718 [-0.02486, -0.00919] |
| CHAMPION_NB | -0.00404 [-0.00749, -0.00056] | -0.00760 [-0.01350, -0.00150] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=FAIL, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
