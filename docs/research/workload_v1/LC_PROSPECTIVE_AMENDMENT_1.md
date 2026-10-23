# WORKLOAD_V1_LC prospective test — Amendment 1 (comparator specifics)

Status: written **before the first prospective record exists** (no `activation.json`, no `records/` on `workload-shadow-data` at the time of this commit). It fills in comparator details that the registration (`LC_PROSPECTIVE_REGISTRATION.md`, c0a4df6f) left to the code. It changes **no** threshold, no model parameter and nothing in the original seven-check rule.

## A1.1 CHAMPION
* Expected shots = the `mean` of the incumbent PLAYER_SIM_V1 shots forecast for that (game, player) in the projection-foundation `forecasts` archive, taking the **last forecast whose `archived_utc` precedes the game's `game_start_utc`**. Scored as a Poisson with that mean (the original CHAMPION definition).
* CHAMPION_NB = the same mean with the NegBin dispersion `alpha_champion_nb` frozen in `data/params/workload-lc-1.0.json`. That alpha is fitted on the **2025 season** with the retrospective harness's derived incumbent stand-in (the live archive did not exist for 2025); it is applied unchanged to live incumbent means. If live incumbent means are scaled differently from the stand-in, CHAMPION_NB is mis-dispersed by that amount and the comparison against it is read with that caveat stated in the report; the alpha is **not** refitted on prospective data for the rule.
* Row pairing: the scoreboard, the seven-check rule and every interval are computed on **one sample: scored player-games that also have a pregame incumbent forecast** (so all arms are compared on identical rows). The look counters (10k/20k/30k/60k) count that paired sample, which is the conservative reading of the registration (paired ⊆ scored). The number of scored player-games without a pregame incumbent forecast is reported beside every result. If fewer than **80%** of scored player-games have a pregame incumbent forecast at a decision look, that look is reported as `INCONCLUSIVE (comparator coverage)` and nothing is decided on the covered subset.

## A1.2 BASELINE and uncorrected WORKLOAD_V1
Both are produced by the same job from the same settled inputs. As in the original rule BASELINE and CHAMPION are Poisson; the uncorrected WORKLOAD_V1 arm is scored as a NegBin with `alpha_workload_v1_raw`, frozen in the same parameter file from the 2025 fit (`alpha_baseline` is recorded for information and is not used by the rule).

## A1.3 Frozen parameter file
`data/params/workload-lc-1.0.json` is produced once by `python -m nhl_edge.research.workload_shadow_freeze` (it refuses to overwrite) and is entered into the integrity registry (`docs/research/INTEGRITY_REGISTRY.json`), so a later change fails CI. It records the fitted constants, the three dispersions, the training and dispersion seasons and the sha256 of the original preregistration.

## A1.4 What stays as registered
Population, pregame rule, looks (10k/20k descriptive, 30k decision, 60k final), the early-failure rule, the bootstrap, and the seven-check acceptance rule with its original thresholds. Seasons 2021–2025 remain exposed development data and are never reported as independent validation of this arm; only records written after activation count.
