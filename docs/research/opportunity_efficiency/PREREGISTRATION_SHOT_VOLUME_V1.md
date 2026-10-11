# Preregistration: NHL_SHOT_VOLUME_V1 vs PLAYER_SIM_V1 (frozen 2026-10-11, before any 2025-26 scoring)

**RESEARCH_ONLY.** No promotion, authority, staking or publication follows from any outcome.

## Frozen artefacts
* Code commit: `caa2ec448` (branch `claude/w2-nhl-opportunity-efficiency`). Challenger model files hash
  (`shot_volume_v1.model_files()`): `sha256:14dc08c0cd234c6d9f226ba7c6e9ae1312f6dd923b0d2254ebfc78bd062855fa`.
* Incumbent: PLAYER_SIM_V1 as on `origin/main` @ `3b8fcde` (walk-forward harness `research/player_walk_forward.py`,
  parameters refit on seasons < test season, seeds = game ids). Verified to reproduce the committed
  `docs/research/player_sim_v1/*_2025.parquet` exactly.
* Simple baseline: RECENT_MEAN_10 (plain mean of the last 10 official games strictly before the date; Poisson for counts,
  Normal(mean, training residual sd) truncated at 0 for TOI; saves = Poisson(team's last-10 shots against x training
  league save %)).

## Why this challenger (decomposition, 2024-25 development season only; `dev_2024/decomposition_2024.json`)
* Efficiency stages carry little fixable error: shrunk player on-net rate vs pooled −0.0026 nats per skater-game
  (CI −0.0050, −0.0000); goals | SOG player vs pooled 0.7200 vs 0.7227; goalie save % vs league −0.0084 nats per start.
* Saves error is opportunity: incumbent saves MAE 5.30; the incumbent's own saves-per-expected-shot ratio applied to the
  ACTUAL team shots faced gives MAE 2.04. The incumbent's expected shots faced is biased +0.59 shots per team-game
  (league level fell 30.1 → 28.1; absolute 82-game team rates carry the old level).
* TOI: the incumbent beats the plain recent mean (MAE 1.879 vs 1.893, ΔMAE −0.014 [−0.023, −0.005]; PP TOI −0.023
  [−0.031, −0.015]) but is biased −0.23 min (OT minutes excluded from the team-minute budget; −0.64 min in OT games).
  Not addressed here (one challenger); reported as a finding.

## Hypothesis
Expressing team shot generation / suppression in league-relative units with a one-pass opponent adjustment (all
other hyper-parameters the incumbent's) improves the distribution of goalie saves, and allocating the opposing net's
simulated non-goal shots to skaters (weights = incumbent expected SOG minus simulated goal expectation, x the draw's TOI
multiplier) gives skater SOG distributions at least as good as the incumbent's while making the joint draw coherent.
Points, assists and TOI are unchanged by construction (identical draws).

Dev-season disclosure (2024-25, seen before freezing): saves ΔCRPS −0.0099 [−0.0175, −0.0021], ΔMAE −0.015
[−0.028, −0.001], ΔMSE −0.27 [−0.45, −0.09]; SOG ΔCRPS −0.0020 [−0.0028, −0.0012], Δlog −0.0059 [−0.0072, −0.0046],
ΔMSE −0.0084 [−0.0125, −0.0045] but **ΔMAE(mean) +0.0042 [+0.0029, +0.0054]** (the challenger's SOG mean is higher and
nearly unbiased, +0.016 vs −0.030; absolute error of the mean rewards under-prediction of right-skewed counts). Under
the strict rule below this dev result would FAIL; the rule is kept as written anyway.

## Population, split, rows
* Holdout: every 2025-26 regular-season game in `docs/research/walk_forward_v2_wf2_20260929_games.csv` with official
  player tables (expected 1,312 games): every dressed skater (conditional on playing) for `shots_on_goal`, `points`,
  `assists`, `time_on_ice_min`; every starting goalie (conditional on starting) for `goalie_saves`. One row per
  player-game-statistic; never pooled across statistics or ladder rungs. Exclusions counted.
* Train: seasons < 2025 (incumbent procedure; saves NB refit on 2023-24 + 2024-25 for both arms). Development: 2024-25.
  No parameter, weight or rule is changed after this commit.
* Outcomes: official NHL boxscore (sports source), never market settlement.

## Metrics (per statistic; deltas challenger − reference; paired, game-clustered percentile bootstrap, B = 2,000,
seed 20261011; 95% CI)
1. MAE of the mean; 2. MSE of the mean; 3. exact CRPS of the simulated distribution (4,000 draws);
4. log score of the PMF floored at 1/(2·4000) (counts only); 5. Brier at the pure_gate representative rung
(one outcome-blind common strike per player-game, mean probability closest to 0.5; pure_gate's 1,000-replicate
bootstrap). Descriptive (not in the rule): bias, p10–p90 coverage, PIT deciles, pure_gate quantile-CRPS.
Subgroups (descriptive only): Oct–Nov vs Dec onward (all stats); F vs D (skater stats).

## Decision rule (strict)
* **ACCEPTED_CHALLENGER (research only)** iff all hold vs PLAYER_SIM_V1: (a) `goalie_saves` ΔCRPS < 0 with CI
  excluding 0; (b) NO metric 1–5 on ANY of the five statistics worsens with its 95% CI excluding 0; (c) vs
  RECENT_MEAN_10, `goalie_saves` and `shots_on_goal` ΔCRPS < 0 with CI excluding 0; (d) zero coherence violations
  (SOG ≥ goals, Σ skater SOG = goals + opposing net non-goal shots, points = goals + assists) and zero incumbent
  invariant violations; (e) points / assists / TOI rows bit-identical to the incumbent; (f) pure_gate `rerun` verdict
  PASS_RUNTIME_NONLEAKAGE with the market-anchored negative control responding.
* **REJECTED** if (b) fails (any metric worse with CI excluding 0) or (a) is worse with CI excluding 0, or (d)/(e)/(f)
  fail.
* **INCONCLUSIVE** otherwise (nothing worse, primary not significantly better).

Starting-goalie confirmation: no historical timing exists; the holdout is conditional on the actual starter. The
2026-27 archive sample (from 2026-09-29) is reported descriptively only.
