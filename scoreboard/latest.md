# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 917 · late records excluded 0 · scored (dressed) 663 · candidates who did not dress 130 · awaiting the official result 124 · paired with the incumbent's pregame forecast 623
* **verdict: INCONCLUSIVE AT n=623 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 623 | +0.0207 | 1.0018 | 1.2789 | 0.6796 | 0.13210 | 0.798 |
| WORKLOAD_V1_RAW | 623 | +0.0582 | 1.0075 | 1.2812 | 0.6803 | 0.13223 | 0.797 |
| CHAMPION | 623 | -0.0657 | 1.0040 | 1.2940 | 0.6883 | 0.13389 | 0.778 |
| BASELINE | 623 | +0.0372 | 1.0166 | 1.2895 | 0.6860 | 0.13345 | 0.788 |
| CHAMPION_NB | 623 | -0.0657 | 1.0040 | 1.2940 | 0.6893 | 0.13406 | 0.801 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00073 [-0.00269, +0.00108] | -0.00233 [-0.00534, +0.00036] |
| CHAMPION | -0.00877 [-0.01391, -0.00306] | -0.01510 [-0.02472, -0.00374] |
| BASELINE | -0.00648 [-0.01518, +0.00329] | -0.01059 [-0.02550, +0.00594] |
| CHAMPION_NB | -0.00978 [-0.01544, -0.00362] | -0.01510 [-0.02472, -0.00374] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=FAIL, crps_give_back_le_0.001=FAIL
