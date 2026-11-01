# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 2769 · late records excluded 0 · scored (dressed) 2145 · candidates who did not dress 411 · awaiting the official result 213 · paired with the incumbent's pregame forecast 2022
* **verdict: INCONCLUSIVE AT n=2022 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 2022 | +0.0220 | 1.0130 | 1.3091 | 0.6797 | 0.13004 | 0.803 |
| WORKLOAD_V1_RAW | 2022 | +0.0603 | 1.0189 | 1.3099 | 0.6804 | 0.13019 | 0.803 |
| CHAMPION | 2022 | -0.0608 | 1.0117 | 1.3209 | 0.6855 | 0.13119 | 0.781 |
| BASELINE | 2022 | +0.0456 | 1.0371 | 1.3309 | 0.6938 | 0.13285 | 0.786 |
| CHAMPION_NB | 2022 | -0.0608 | 1.0117 | 1.3209 | 0.6861 | 0.13134 | 0.806 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00076 [-0.00172, +0.00030] | -0.00078 [-0.00267, +0.00121] |
| CHAMPION | -0.00581 [-0.00993, -0.00185] | -0.01173 [-0.01902, -0.00448] |
| BASELINE | -0.01413 [-0.02015, -0.00838] | -0.02181 [-0.03162, -0.01217] |
| CHAMPION_NB | -0.00641 [-0.01061, -0.00222] | -0.01173 [-0.01902, -0.00448] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=FAIL, crps_give_back_le_0.001=PASS
