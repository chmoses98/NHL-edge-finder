# WORKLOAD_V1_LC — prospective shadow test: registration

> RESEARCH_ONLY · registered 2026-10-23, **before any prospective prediction exists**. The commit time of this file is the registration time. Nothing here changes a model, price, stake, cap, routing or authority; **no promotion is requested**; the published single projection per target is untouched (this arm writes to its own branch and is never read by the app, the packet or any betting path). PASS-only is unchanged. There is no Kalshi shots-on-goal market, so nothing here can price or route a bet.

## What is being tested and what is frozen

* **Model:** `WORKLOAD_V1_LC` exactly as in `src/nhl_edge/research/workload_level_cal.py` — WORKLOAD_V1 with the parameters in `docs/research/workload_v1/preregistration.json` (`frozen_params`, unchanged), constants fitted on the five completed seasons 2021–2025, NegBin dispersion fitted on the 2025 season's residuals of this arm's own corrected means, times a level factor from settled outcomes (half-life 60 days, prior 1,000 shots). **No parameter may change during the test.** The code commit hash and the parameter hashes are written into every prediction record; a prediction whose record names a different hash than the one registered at activation is excluded from the primary analysis and listed.
* **Acceptance rule: unchanged.** The original seven-check rule of `preregistration.json` (CRPS vs CHAMPION and vs CHAMPION_NB with 95% interval upper bound < 0, RMSE vs CHAMPION, ladder Brier vs CHAMPION_NB, `|bias| ≤ 0.05`, 80% PIT coverage in [0.77, 0.83], position CRPS no worse than CHAMPION_NB) is applied to the prospective sample as written. The development checks of `LEVEL_CALIBRATION_PREREGISTRATION.md` (`|bias| ≤ 0.02`, no CRPS give-back beyond +0.0010, coverage band, position check) are reported beside it as the LC-specific reading. Neither is relaxed, and no threshold is chosen after seeing prospective data.
* **Historical results are preserved and not relabelled.** WORKLOAD_V1 was REJECTED on 2023-24 by its frozen rule (bias +0.0525 vs 0.05) and ACCEPTED on 2024-25 (validation season, not independent) and 2025-26; WORKLOAD_V1_LC was DEVELOPMENT-QUALIFIED on all three. Those seasons had been scored by the same family and motivated the LC design; **they are development evidence and are not counted as validation** here or anywhere else.

## Population, timing and provenance

* **Games:** regular-season NHL games with puck drop after the activation timestamp (the first commit of the data branch). Earlier games are never added.
* **Candidates:** for each game and team, every skater who dressed in any of that team's last five settled games at prediction time (point-in-time, outcome-free). One record per (game, player). The test is **conditional on dressing, as the original design was**: a candidate who does not dress is not scored (their count is reported), and a skater who dresses without being a candidate is not scored (count reported). This is a projection-quality test, not a lineup forecast.
* **Pregame rule:** a record counts only if its `predicted_at_utc` precedes the game's puck drop; later records are written, kept and excluded (`late`). Records are write-once files under `dt=<date>/`, listed with their sha256 in a manifest; the workflow refuses to overwrite or delete a record (`archive_guard`-style check).
* **Inputs:** only player-game and team-game events already settled in the archive at prediction time (a game settled after the prediction cannot inform it) plus the five completed seasons of history. Deviation from the retrospective harness, stated in advance: the retrospective harness uses all games dated strictly before the game date, the live job uses all *settled* games, which can omit a game finished late the previous night; the equivalence test in `tests/test_workload_shadow.py` shows identical output when the same games are present.
* **Comparators on the same player-games:** CHAMPION = the production PLAYER_SIM_V1 expected shots from the last pregame forecast in the archive (`predictions_player`) ; uncorrected WORKLOAD_V1 (same job, no level factor); BASELINE (exponentially weighted shots per game). NegBin dispersion for every comparator that is not Poisson is fitted on 2025, as in the original.

## Looks and stopping (set before data)

* **Interim looks at 10,000 and 20,000 scored skater-games are descriptive only.** No early success. Early failure is declared only if, at a look, `|bias| > 0.10` shots per skater-game or CRPS vs CHAMPION has a 95% interval entirely above zero; the test then stops and the failure is reported.
* **Decision look at 30,000 scored skater-games** (about 4 months of play): the registered rule is applied once to everything scored up to that point; a second, final look at 60,000. The decision never uses a different sample than the one the interval was computed on. Game-clustered bootstrap, 2,000 resamples, seed 20261012, exactly as the original.
* The result is one of: `MEETS FROZEN RULE` (eligible for a *recommendation to a human*; never a promotion), `FAILS FROZEN RULE`, or `INCONCLUSIVE AT n`.

## What this does not decide

Whether the arm may replace the production expected-shots projection, or be shown anywhere, is a human decision after the final look, with the calibration/runtime/contract gates of `PROMOTION_SCORECARD.md`. Nothing in this registration, the collection job or the scoreboard moves any published number.

## Operations (kept separate from forecasting research)

A scheduled and manually dispatchable workflow writes predictions and the scoreboard to the orphan branch `workload-shadow-data` only; it has no access to the betting engine, the router or the app contract. A failed run leaves a gap that is reported (coverage table), never filled retroactively.
