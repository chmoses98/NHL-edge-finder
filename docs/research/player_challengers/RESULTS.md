# Player workload challengers (RESEARCH_ONLY, development evidence)

**Evidence status.** 2022–2025 are exposed development seasons: every number below selects a specification and validates nothing. Only the write-once prospective
records (WORKLOAD_V1_LC for shots, `player-minutes-1.0` for ice time, see `docs/research/player_minutes/PREREGISTRATION.md`) can validate anything. Nothing here
changes a production model, price, stake or route.

Code: `src/nhl_edge/research/player_challengers.py` (`python -m nhl_edge.research.player_challengers --with-workload`); raw output: `challengers.json`.

## Method

Each challenger is the incumbent's expected value times `exp(X·b)`: `b` is fitted on **earlier seasons only** (damped Newton, no scipy), applied to the next season, and
scored on 2023, 2024 and 2025 (pooled n = 141,677 skater-games; 139,628 with valid power-play shifts). Intervals are game-clustered paired bootstrap (2,000 draws).
Stages are added one at a time, each against the previous stage:

| stage | feature(s), all strictly pregame |
|---|---|
| LEVEL | scale only (removes the incumbent's average bias) |
| +ROLL | log actual/predicted over the previous 90 days (strictly earlier days) |
| +USAGE | log((last-3 ice time + 1) / (incumbent ice time + 1)) |
| +ROLE | last 3 vs the 12 games before (role change) |
| +OPP | opponent shot-suppression environment (shots only) |
| +LINEMATES | lagged linemate feature (shots only) |
| +TEAM_ENV | team power-play environment (power-play time only) |

## Ice time: the lift is WORKLOAD_V1 itself; one small usage term remains

Mean squared error in minutes², pooled 2023–25:

| | incumbent PLAYER_SIM_V1 | WORKLOAD_V1 | change (95% CI) | bias (inc → WL) |
|---|---|---|---|---|
| total ice time | 6.405 | 6.120 | −0.285 (−0.305, −0.267) = −4.5% | −0.288 → +0.018 |
| power-play time | 1.423 | 1.309 | −0.114 (−0.128, −0.099) = −8.0% | −0.224 → +0.017 |

Stage ladder on the incumbent (total ice time, MSE): LEVEL 6.310 → +ROLL 6.303 → **+USAGE 6.058** → +ROLE 6.053. Almost all of the gain over the incumbent is the level
fix (bias −0.29 min) plus **recent usage** (−0.245 vs the previous stage, CI −0.265…−0.226, same sign in all three seasons). +ROLL is not stable (worse in 2023, better
2024–25) and +ROLE is within noise.

Stacked on WORKLOAD_V1's own minutes (fit 2023→score 2024, fit 2023–24→score 2025; n = 94,456):

* total ice time: usage term, coefficient 0.226 (2024) / 0.235 (2025), MSE 6.034 → 5.968 (−0.066, −1.1%, CI −0.079…−0.055). Worth carrying as a pre-registered prospective hypothesis (H3).
* power-play time: stacking anything on WORKLOAD_V1 gives −0.0019 (CI −0.0040…+0.0002): nothing to add.

## Shots: the level fix is the gain; opponent and usage add almost nothing on top of LC

Ranked-probability style score (CRPS, lower is better), pooled 2023–25 on the production incumbent:

| CHAMPION | LEVEL | +ROLL | +USAGE | +OPP | +LINEMATES |
|---|---|---|---|---|---|
| 0.7011 | 0.7000 | 0.6999 | 0.6990 | 0.6979 | 0.6978 |

Bias in shots/game: champion −0.063, LEVEL +0.008, +OPP −0.026. Every stage has a CI that excludes zero against the champion; together they are worth 0.0033 CRPS (0.5%).
The incumbent's coverage of its 50%/80% intervals is 0.478/0.778; the negative-binomial reshaping of the same mean fixes that (0.501/0.801) with no change to the mean.

On top of WORKLOAD_V1_LC (2024–25, n = 94,456): LC CRPS 0.68558; LC+USAGE 0.68530 (−0.00028, CI −0.00044…−0.00013); LC+USAGE+OPP 0.68530 (no further gain). Mean absolute
error is unchanged (CI spans 0). The LC base already captures the level, recent form and part of the opponent effect. This is a 0.04% improvement: **do not change the registered
LC shots test**; usage is recorded as an observed input in the new minutes records so it can be tested prospectively.

## Conclusions for the next step

1. The highest-value player-projection improvement already identified is **WORKLOAD_V1 minutes in place of the incumbent minutes** (−4.5% total, −8.0% power-play MSE, bias removed). It is research-only today; the minutes shadow (`player-minutes-1.0`) tests it prospectively.
2. The only incremental term worth pre-registering is recent usage on total ice time (frozen coefficient 0.23). Opponent suppression, role change and linemate terms are not worth a hypothesis on top of WORKLOAD_V1/LC.
3. Confirmed lineup, power-play unit and scratch data (see `docs/research/lineup_sources/FEASIBILITY.md`) are the input most likely to beat these history-only features; they have no history, so they can only be evaluated prospectively. The new records capture them as observed inputs.
