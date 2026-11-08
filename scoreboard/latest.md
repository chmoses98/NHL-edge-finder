# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 4897 · late records excluded 0 · scored (dressed) 3910 · candidates who did not dress 734 · awaiting the official result 253 · paired with the incumbent's pregame forecast 3691
* **verdict: INCONCLUSIVE AT n=3691 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 3691 | +0.0156 | 1.0068 | 1.2926 | 0.6749 | 0.12940 | 0.805 |
| WORKLOAD_V1_RAW | 3691 | +0.0556 | 1.0125 | 1.2931 | 0.6754 | 0.12949 | 0.804 |
| CHAMPION | 3691 | -0.0633 | 1.0046 | 1.3023 | 0.6795 | 0.13025 | 0.782 |
| BASELINE | 3691 | +0.0440 | 1.0282 | 1.3104 | 0.6861 | 0.13160 | 0.788 |
| CHAMPION_NB | 3691 | -0.0633 | 1.0046 | 1.3023 | 0.6803 | 0.13046 | 0.808 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00046 [-0.00120, +0.00027] | -0.00043 [-0.00188, +0.00101] |
| CHAMPION | -0.00453 [-0.00781, -0.00105] | -0.00971 [-0.01543, -0.00365] |
| BASELINE | -0.01120 [-0.01567, -0.00684] | -0.01774 [-0.02508, -0.01007] |
| CHAMPION_NB | -0.00534 [-0.00865, -0.00187] | -0.00971 [-0.01543, -0.00365] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
