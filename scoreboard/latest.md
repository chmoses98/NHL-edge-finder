# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 2769 · late records excluded 0 · scored (dressed) 2181 · candidates who did not dress 417 · awaiting the official result 171 · paired with the incumbent's pregame forecast 2055
* **verdict: INCONCLUSIVE AT n=2055 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 2055 | +0.0195 | 1.0134 | 1.3083 | 0.6799 | 0.13018 | 0.803 |
| WORKLOAD_V1_RAW | 2055 | +0.0578 | 1.0192 | 1.3090 | 0.6806 | 0.13031 | 0.802 |
| CHAMPION | 2055 | -0.0622 | 1.0121 | 1.3198 | 0.6855 | 0.13128 | 0.781 |
| BASELINE | 2055 | +0.0447 | 1.0373 | 1.3299 | 0.6938 | 0.13294 | 0.786 |
| CHAMPION_NB | 2055 | -0.0622 | 1.0121 | 1.3198 | 0.6861 | 0.13144 | 0.806 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00069 [-0.00168, +0.00032] | -0.00070 [-0.00263, +0.00116] |
| CHAMPION | -0.00561 [-0.00960, -0.00166] | -0.01146 [-0.01861, -0.00402] |
| BASELINE | -0.01390 [-0.01944, -0.00827] | -0.02161 [-0.03113, -0.01227] |
| CHAMPION_NB | -0.00625 [-0.01021, -0.00219] | -0.01146 [-0.01861, -0.00402] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
