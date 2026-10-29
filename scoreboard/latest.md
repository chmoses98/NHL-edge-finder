# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 2019 · late records excluded 0 · scored (dressed) 1299 · candidates who did not dress 253 · awaiting the official result 467 · paired with the incumbent's pregame forecast 1225
* **verdict: INCONCLUSIVE AT n=1225 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 1225 | +0.0323 | 0.9994 | 1.2717 | 0.6708 | 0.13045 | 0.806 |
| WORKLOAD_V1_RAW | 1225 | +0.0696 | 1.0058 | 1.2739 | 0.6718 | 0.13063 | 0.805 |
| CHAMPION | 1225 | -0.0517 | 0.9990 | 1.2849 | 0.6779 | 0.13191 | 0.784 |
| BASELINE | 1225 | +0.0506 | 1.0185 | 1.2879 | 0.6810 | 0.13254 | 0.792 |
| CHAMPION_NB | 1225 | -0.0517 | 0.9990 | 1.2849 | 0.6788 | 0.13206 | 0.808 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00100 [-0.00228, +0.00025] | -0.00222 [-0.00441, -0.00015] |
| CHAMPION | -0.00707 [-0.01229, -0.00156] | -0.01314 [-0.02247, -0.00316] |
| BASELINE | -0.01021 [-0.01802, -0.00305] | -0.01623 [-0.02887, -0.00408] |
| CHAMPION_NB | -0.00801 [-0.01323, -0.00243] | -0.01314 [-0.02247, -0.00316] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=FAIL, crps_give_back_le_0.001=PASS
