# WORKLOAD_V1 preregistration (2026-10-12)

**Authority: RESEARCH_ONLY.** Whatever the result, nothing is promoted, nothing is wired into production, and no
wagering, staking, routing or authority code changes. "ACCEPTED" would only make WORKLOAD_V1 eligible for a
prospective shadow test.

Machine-readable copy (the one the evaluator reads): `docs/research/workload_v1/preregistration.json`.
This file and that JSON were committed **before** the challenger was evaluated on 2025-26 and before the 2025-26
champion audit was run. Code: `src/nhl_edge/research/workload_v1.py` (challenger), `workload_audit.py` (champion and
decomposition), `workload_eval.py` (metrics, bootstrap), `workload_experiment.py` (driver, acceptance rule).

## Why this challenger

The 2024-25 development audit (`docs/research/workload_v1/audit_2024.json`, champion = production PLAYER_SIM_V1,
walk-forward) said:

* **Skater SOG** (45,176 skater-games with shift charts, 1,255 games): total MSE 1.766 against a Poisson floor of 1.541
  (the variance a perfectly-known Poisson mean would still leave). Giving the model the actual minutes removes 0.073
  (4.2% of the MSE, about a third of the reducible part); the rest of the reducible error is rates and omitted states.
  Workload biases: PP minutes -0.142 / skater-game (-10.7%), SH -0.107; overtime shots (0.096 per skater in OT games)
  are never counted; and the expected TOI adds `share_ot x 1.2` minutes that its EV template already holds.
* **Root cause of the PP/SH bias:** `team_states` stretches every overtime game's timeline to 80:00 (n_seconds = 4800
  for all 2,918 regular-season OT games, 2021-26) and books the phantom 20 minutes minus the real OT to whatever
  strength state was last seen. Deployment shares (player seconds / team seconds) are therefore deflated in a quarter of
  all games; skater on-ice ratios drop from 4.99 to 4.51 at EV in OT games (2025-26).
* **Goalie saves** (2,624 starts): 94% of the MSE disappears if the shots faced are known (workload); saves given the
  actual shots have RMSE 1.62. Shots-faced bias +0.53, saves bias +0.42; pulled starters (5.3%) carry a fifth of the
  MSE.

So: fix the workload (repaired shares, matchup PP / SH / EV minutes, explicit OT minutes and shots), make the rates
league-relative and opponent-adjusted (the league fell from 31.6 to 27.7 shots per team-game over 2021-26, so long
memories run high), and give the goalie side a shorter, schedule-adjusted shots-against memory plus a save fraction.

## Hypotheses

* **H1 (skaters):** WORKLOAD_V1 beats the production expected SOG on 2025-26 regular-season skater shots on goal.
* **H2 (goalies):** WORKLOAD_V1 beats the production saves simulation on 2025-26 regular-season starter saves.

## Data and chronology

* Official NHL api-web boxscores, play-by-play and stats shift charts, as cached in `data/history/players`
  (`nhl-player-events-1.0`, 2021-22 .. 2025-26, 100% of games parsed). No sportsbook, Kalshi or other market input,
  directly or through another model (the DATA_ONLY_V2 lambdas are not used by WORKLOAD_V1). A test enforces that the
  research modules import no Kalshi / pricing / execution code.
* Validation season 2024-25 (constants fit on 2021-24, dispersion on 2023-24). Held-out season **2025-26** (constants
  fit on 2021-25, dispersion on 2024-25). Every player / team / goalie feature at date D uses rows strictly before D.
* Targets: every dressed skater-game with a champion row (official SOG incl. OT); every starting goalie (official saves),
  **CONDITIONAL_ON_ACTUAL_STARTER**: no point-in-time starter source exists for 2021-26 (DailyFaceoff is archived only
  from 2026-09-30), and the challenger's save-fraction term uses the actual starter's identity.

## Arms

| target | arm | definition |
|---|---|---|
| SOG | BASELINE | Poisson(EW SOG per game, half-life 10, 5 pseudo-games of the position mean) |
| SOG | CHAMPION | production `expected_sog` (production code and team-minute template), Poisson: production emits only a mean |
| SOG | CHAMPION_NB | same mean, NegBin fit on 2024-25 (separates the distribution from the mean) |
| SOG | WORKLOAD_ONLY | WORKLOAD_V1 minutes x champion rates |
| SOG | EFFICIENCY_ONLY | champion minutes x WORKLOAD_V1 rates and opponent / venue factor |
| SOG | WORKLOAD_V1 | the challenger |
| saves | BASELINE | Poisson(own EW shots against x league save fraction) |
| saves | CHAMPION | production saves draws (nhl-sim-2.0 + `simulate_players` + `simulate_saves`), walk-forward |
| saves | WORKLOAD_ONLY | WORKLOAD_V1 shots against x champion implied save fraction |
| saves | EFFICIENCY_ONLY | champion expected shots faced x WORKLOAD_V1 save fraction |
| saves | WORKLOAD_V1 | the challenger |

Frozen parameters (chosen on 2024-25 by lowest WORKLOAD_V1 CRPS over a 48-point skater grid and a 24-point goalie grid,
`validation_2024.json`): minutes from shares, share half-life 4 games, rate half-life 80 games, league rate window
10,000 skater-games, opponent exponent 1.0; goalies: shots memory half-life 15 team-games, schedule-adjusted, 1,000
shots of prior on the save fraction, league window 400 team-games. Validation CRPS: SOG 0.6889 vs champion 0.6939;
saves 3.7945 vs champion 3.7985.

## Metrics

MAE, RMSE, bias of the predictive mean; discrete CRPS; ladder Brier (SOG 1+..5+, saves 14+..40+); exact PIT coverage of
the central 50% and 80% intervals. 95% CIs from a game-clustered bootstrap (2,000 resamples of games, seed 20261012).
Secondary: TOI MAE (total / PP / SH / EV) and shots-faced squared error, champion vs challenger (workload); SOG given
the actual minutes and saves given the actual shots (efficiency); position and OT / regulation subgroups.

## Primary objective and acceptance (all checks required, per target)

Skaters: CRPS vs CHAMPION, CI upper < 0; CRPS vs CHAMPION_NB, CI upper < 0; RMSE vs CHAMPION, CI upper < 0; ladder Brier
vs CHAMPION_NB, CI upper < 0; |bias| <= 0.05 shots; 80% coverage in [0.77, 0.83]; CRPS no worse than CHAMPION_NB for
forwards and for defencemen.

Goalies: CRPS vs CHAMPION, CI upper < 0; RMSE vs CHAMPION, CI upper < 0; ladder Brier vs CHAMPION, CI upper < 0;
|bias| <= 0.5 saves; 80% coverage in [0.77, 0.83].

Otherwise REJECTED. No threshold, arm, parameter or row filter changes after the held-out run.

## Disclosures

* The 2024-25 champion decomposition was looked at before the challenger was designed (it is the validation season).
* The `team_states` data-quality check (OT timelines of 4,800 s, on-ice ratios) was run on the raw tables of every
  season including 2025-26; no forecast was scored on 2025-26.
* On validation the skater challenger's bias was +0.047 (limit 0.05) and the goalie challenger's 80% coverage 0.771
  (band from 0.77): both could fail on 2025-26. The limits were set from first principles and stay.
* The goalie optimum (half-life 15) is at the edge of its grid; the grid was not extended.
* 2025-26 was a held-out season for earlier PLAYER_SIM_V1 work (goals / assists / points / saves); nothing was tuned on it.
* The champion's PP-minute scaling uses DATA_ONLY_V2 goal components that are not stored historically; the walk-forward
  stand-in (`team_pp_shares`) is used, as in `player_walk_forward`.
