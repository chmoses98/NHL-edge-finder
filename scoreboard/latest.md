# WORKLOAD_V1_LC — prospective shadow scoreboard

RESEARCH_ONLY · registration: `docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md` · conditional on dressing · interim looks are descriptive

* pregame records 793 · late records excluded 0 · scored (dressed) 526 · candidates who did not dress 103 · awaiting the official result 164 · paired with the incumbent's pregame forecast 493
* **verdict: INCONCLUSIVE AT n=493 (decision look at 30000)**
* registered looks computed so far: none

| arm | n | bias | MAE | RMSE | CRPS | ladder Brier | cov80 |
|---|---:|---:|---:|---:|---:|---:|---:|
| LC | 493 | +0.0135 | 1.0069 | 1.2767 | 0.6804 | 0.13215 | 0.796 |
| WORKLOAD_V1_RAW | 493 | +0.0513 | 1.0122 | 1.2788 | 0.6810 | 0.13227 | 0.795 |
| CHAMPION | 493 | -0.0653 | 1.0101 | 1.2910 | 0.6893 | 0.13392 | 0.776 |
| BASELINE | 493 | +0.0388 | 1.0230 | 1.2883 | 0.6881 | 0.13372 | 0.785 |
| CHAMPION_NB | 493 | -0.0653 | 1.0101 | 1.2910 | 0.6901 | 0.13408 | 0.799 |

| LC minus | CRPS Δ [95%] | RMSE Δ [95%] |
|---|---|---|
| WORKLOAD_V1_RAW | -0.00064 [-0.00291, +0.00132] | -0.00215 [-0.00584, +0.00088] |
| CHAMPION | -0.00888 [-0.01367, -0.00382] | -0.01432 [-0.02330, -0.00421] |
| BASELINE | -0.00769 [-0.01807, +0.00392] | -0.01160 [-0.02899, +0.00760] |
| CHAMPION_NB | -0.00971 [-0.01525, -0.00354] | -0.01432 [-0.02330, -0.00421] |

Frozen original rule: crps_vs_champion_ci_upper_lt_0=PASS, rmse_vs_champion_ci_upper_lt_0=PASS, abs_bias_le_0.05=PASS, coverage80_in_band=PASS, crps_vs_champion_nb_ci_upper_lt_0=PASS, ladder_brier_vs_champion_nb_ci_upper_lt_0=PASS, no_position_worse_crps_than_champion_nb=PASS
LC development checks: abs_bias_le_0.02=PASS, crps_give_back_le_0.001=FAIL
