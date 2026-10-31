# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 2556 · late records excluded 0 · scored (dressed) 1797 · candidates who did not dress 344 · awaiting the official result 415 · paired with the incumbent's pregame forecast 1695
* **verdict: INCONCLUSIVE AT n=1695 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 1695 | +0.0249 | 1.0100 | 1.2918 | 0.6755 | 0.12994 | 0.803 |
| WORKLOAD_V1_RAW | 1695 | +0.0628 | 1.0159 | 1.2927 | 0.6762 | 0.13008 | 0.802 |
| CHAMPION | 1695 | -0.0560 | 1.0086 | 1.3037 | 0.6816 | 0.13112 | 0.782 |
| BASELINE | 1695 | +0.0495 | 1.0322 | 1.3121 | 0.6885 | 0.13250 | 0.787 |
| CHAMPION_NB | 1695 | -0.0560 | 1.0086 | 1.3037 | 0.6821 | 0.13125 | 0.807 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00070 [-0.00176, +0.00036] | -0.00092 [-0.00294, +0.00103] |
| CHAMPION | -0.00604 [-0.01021, -0.00172] | -0.01191 [-0.01977, -0.00323] |
| BASELINE | -0.01299 [-0.01940, -0.00617] | -0.02027 [-0.03107, -0.00850] |
| CHAMPION_NB | -0.00658 [-0.01092, -0.00213] | -0.01191 [-0.01977, -0.00323] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=FAIL, crps_give_back_le_0.001=PASS
