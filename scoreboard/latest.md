# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 1552 · late records excluded 0 · scored (dressed) 1160 · candidates who did not dress 223 · awaiting the official result 169 · paired with the incumbent's pregame forecast 1093
* **verdict: INCONCLUSIVE AT n=1093 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 1093 | +0.0234 | 1.0029 | 1.2812 | 0.6744 | 0.13093 | 0.803 |
| WORKLOAD_V1_RAW | 1093 | +0.0604 | 1.0092 | 1.2831 | 0.6753 | 0.13109 | 0.802 |
| CHAMPION | 1093 | -0.0597 | 1.0046 | 1.2978 | 0.6835 | 0.13279 | 0.782 |
| BASELINE | 1093 | +0.0453 | 1.0233 | 1.2989 | 0.6854 | 0.13317 | 0.790 |
| CHAMPION_NB | 1093 | -0.0597 | 1.0046 | 1.2978 | 0.6843 | 0.13292 | 0.806 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00086 [-0.00219, +0.00035] | -0.00189 [-0.00419, +0.00024] |
| CHAMPION | -0.00914 [-0.01428, -0.00410] | -0.01655 [-0.02570, -0.00686] |
| BASELINE | -0.01101 [-0.01926, -0.00332] | -0.01766 [-0.03062, -0.00440] |
| CHAMPION_NB | -0.00992 [-0.01492, -0.00464] | -0.01654 [-0.02570, -0.00686] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=FAIL, crps_give_back_le_0.001=PASS
