# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 2556 · late records excluded 0 · scored (dressed) 1866 · candidates who did not dress 354 · awaiting the official result 336 · paired with the incumbent's pregame forecast 1759
* **verdict: INCONCLUSIVE AT n=1759 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 1759 | +0.0188 | 1.0124 | 1.3029 | 0.6789 | 0.13014 | 0.803 |
| WORKLOAD_V1_RAW | 1759 | +0.0568 | 1.0183 | 1.3036 | 0.6796 | 0.13027 | 0.803 |
| CHAMPION | 1759 | -0.0633 | 1.0118 | 1.3157 | 0.6856 | 0.13144 | 0.782 |
| BASELINE | 1759 | +0.0430 | 1.0355 | 1.3241 | 0.6925 | 0.13281 | 0.787 |
| CHAMPION_NB | 1759 | -0.0633 | 1.0118 | 1.3157 | 0.6861 | 0.13158 | 0.807 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00065 [-0.00169, +0.00049] | -0.00073 [-0.00284, +0.00140] |
| CHAMPION | -0.00668 [-0.01091, -0.00222] | -0.01280 [-0.02079, -0.00429] |
| BASELINE | -0.01356 [-0.01997, -0.00677] | -0.02122 [-0.03183, -0.00990] |
| CHAMPION_NB | -0.00721 [-0.01158, -0.00255] | -0.01280 [-0.02079, -0.00429] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
