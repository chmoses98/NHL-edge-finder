# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 4897 · late records excluded 0 · scored (dressed) 3593 · candidates who did not dress 677 · awaiting the official result 627 · paired with the incumbent's pregame forecast 3392
* **verdict: INCONCLUSIVE AT n=3392 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 3392 | +0.0189 | 1.0081 | 1.2904 | 0.6748 | 0.12982 | 0.804 |
| WORKLOAD_V1_RAW | 3392 | +0.0588 | 1.0138 | 1.2910 | 0.6753 | 0.12992 | 0.804 |
| CHAMPION | 3392 | -0.0611 | 1.0042 | 1.2977 | 0.6779 | 0.13039 | 0.783 |
| BASELINE | 3392 | +0.0462 | 1.0286 | 1.3073 | 0.6855 | 0.13192 | 0.788 |
| CHAMPION_NB | 3392 | -0.0611 | 1.0042 | 1.2977 | 0.6787 | 0.13060 | 0.809 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00051 [-0.00133, +0.00025] | -0.00060 [-0.00206, +0.00085] |
| CHAMPION | -0.00304 [-0.00646, +0.00024] | -0.00731 [-0.01326, -0.00111] |
| BASELINE | -0.01068 [-0.01540, -0.00609] | -0.01692 [-0.02444, -0.00951] |
| CHAMPION_NB | -0.00391 [-0.00735, -0.00064] | -0.00731 [-0.01326, -0.00111] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=FAIL, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
