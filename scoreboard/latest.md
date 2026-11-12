# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 6013 · late records excluded 0 · scored (dressed) 4681 · candidates who did not dress 876 · awaiting the official result 456 · paired with the incumbent's pregame forecast 4383
* **verdict: INCONCLUSIVE AT n=4383 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 4383 | +0.0132 | 1.0137 | 1.3056 | 0.6807 | 0.13018 | 0.802 |
| WORKLOAD_V1_RAW | 4383 | +0.0534 | 1.0192 | 1.3058 | 0.6812 | 0.13027 | 0.802 |
| CHAMPION | 4383 | -0.0681 | 1.0120 | 1.3162 | 0.6860 | 0.13116 | 0.779 |
| BASELINE | 4383 | +0.0382 | 1.0357 | 1.3248 | 0.6930 | 0.13258 | 0.784 |
| CHAMPION_NB | 4383 | -0.0681 | 1.0120 | 1.3162 | 0.6865 | 0.13133 | 0.805 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00047 [-0.00126, +0.00029] | -0.00026 [-0.00176, +0.00115] |
| CHAMPION | -0.00524 [-0.00887, -0.00160] | -0.01066 [-0.01672, -0.00427] |
| BASELINE | -0.01225 [-0.01644, -0.00820] | -0.01923 [-0.02642, -0.01236] |
| CHAMPION_NB | -0.00577 [-0.00933, -0.00207] | -0.01066 [-0.01673, -0.00427] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=PASS
