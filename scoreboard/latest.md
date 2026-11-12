# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 6013 · late records excluded 0 · scored (dressed) 4472 · candidates who did not dress 838 · awaiting the official result 703 · paired with the incumbent's pregame forecast 4213
* **verdict: INCONCLUSIVE AT n=4213 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 4213 | +0.0151 | 1.0129 | 1.3047 | 0.6799 | 0.12997 | 0.803 |
| WORKLOAD_V1_RAW | 4213 | +0.0552 | 1.0186 | 1.3051 | 0.6804 | 0.13007 | 0.803 |
| CHAMPION | 4213 | -0.0658 | 1.0114 | 1.3154 | 0.6851 | 0.13097 | 0.780 |
| BASELINE | 4213 | +0.0411 | 1.0352 | 1.3241 | 0.6922 | 0.13240 | 0.785 |
| CHAMPION_NB | 4213 | -0.0658 | 1.0114 | 1.3154 | 0.6857 | 0.13114 | 0.806 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00050 [-0.00126, +0.00027] | -0.00031 [-0.00179, +0.00115] |
| CHAMPION | -0.00527 [-0.00876, -0.00177] | -0.01065 [-0.01689, -0.00452] |
| BASELINE | -0.01236 [-0.01658, -0.00837] | -0.01932 [-0.02644, -0.01256] |
| CHAMPION_NB | -0.00581 [-0.00941, -0.00228] | -0.01065 [-0.01689, -0.00452] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
