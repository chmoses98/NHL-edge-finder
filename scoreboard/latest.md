# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 4644 · late records excluded 0 · scored (dressed) 3487 · candidates who did not dress 661 · awaiting the official result 496 · paired with the incumbent's pregame forecast 3292
* **verdict: INCONCLUSIVE AT n=3292 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 3292 | +0.0200 | 1.0095 | 1.2925 | 0.6756 | 0.12997 | 0.804 |
| WORKLOAD_V1_RAW | 3292 | +0.0598 | 1.0153 | 1.2932 | 0.6761 | 0.13008 | 0.804 |
| CHAMPION | 3292 | -0.0592 | 1.0056 | 1.2997 | 0.6786 | 0.13054 | 0.783 |
| BASELINE | 3292 | +0.0486 | 1.0302 | 1.3094 | 0.6864 | 0.13211 | 0.788 |
| CHAMPION_NB | 3292 | -0.0592 | 1.0056 | 1.2997 | 0.6793 | 0.13072 | 0.809 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00057 [-0.00137, +0.00020] | -0.00067 [-0.00219, +0.00079] |
| CHAMPION | -0.00301 [-0.00638, +0.00035] | -0.00714 [-0.01297, -0.00123] |
| BASELINE | -0.01082 [-0.01531, -0.00628] | -0.01689 [-0.02451, -0.00910] |
| CHAMPION_NB | -0.00376 [-0.00726, -0.00037] | -0.00714 [-0.01297, -0.00123] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=FAIL, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
