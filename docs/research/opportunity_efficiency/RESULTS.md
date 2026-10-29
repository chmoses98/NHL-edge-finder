# NHL opportunity / efficiency decomposition and NHL_SHOT_VOLUME_V1: results (2026-10-11)

**RESEARCH_ONLY. Verdict: REJECTED** under the preregistered strict rule
(`PREREGISTRATION_SHOT_VOLUME_V1.md`, commit `995e860f1`, code frozen at `caa2ec448`). The incumbent PLAYER_SIM_V1 is
unchanged; nothing is promoted, published or staked.

Audit: `docs/research/NHL_PLAYER_ENGINE_AUDIT.md`. Files: `dev_2024/` (development season), `holdout_2025/` (untouched
2025-26 holdout), `rerun/` (runtime non-leakage proof), `starter_confirmation_2026.json` (2026-27 archive, descriptive).

## 1. Decomposition: where the incumbent's error is (matched player-game rows, game-clustered 95% CIs, B = 2,000)

Baseline RECENT_MEAN_10 = plain mean of the last 10 games strictly before the date. Δ = incumbent − baseline.
Development 2024-25: 45,176 skater-games with shift data, 1,255 games; 2,624 starts. Holdout 2025-26: 47,231 skater-
games, 1,312 games; 2,624 starts (scored only after preregistration).

### Opportunity
| quantity | season | baseline MAE (bias) | incumbent MAE (bias) | ΔMAE [95% CI] |
|---|---|---|---|---|
| total TOI (min) | 2024-25 | 1.893 (+0.02) | 1.879 (−0.23) | −0.014 [−0.023, −0.005] |
| total TOI (min) | 2025-26 | 1.932 (+0.02) | 1.943 (−0.39) | +0.011 [+0.000, +0.022] |
| TOI, OT games | 2025-26 (n 11,736) | 2.044 (−0.39) | 2.204 (−0.80) | +0.161 [+0.141, +0.180] |
| TOI, PP role (prior PP share ≥ 0.40) | 2025-26 (n 14,328) | 1.934 (+0.08) | 1.981 (−0.65) | +0.046 [+0.024, +0.068] |
| TOI, < 10 prior games | 2025-26 (n 1,113) | 2.353 (+0.41) | 2.142 (+0.07) | −0.211 [−0.293, −0.132] |
| PP TOI (min) | 2024-25 | 0.780 (+0.01) | 0.757 (−0.12) | −0.023 [−0.031, −0.015] |
| PP TOI (min) | 2025-26 | 0.815 (+0.00) | 0.788 (−0.21) | −0.027 [−0.036, −0.018] |
| team shots faced | 2024-25 | 5.205 (+0.07) | 4.919 (+0.59) | −0.286 [−0.372, −0.200] |
| team shots faced | 2025-26 | 5.250 (+0.10) | 4.887 (+0.14) | −0.363 [−0.448, −0.281] |

Shot attempts per game (2025-26): recent mean MAE 1.597; recent attempt rate x actual TOI 1.537 (attempt volume is
mostly per-game noise; the incumbent has no attempt model).

### Efficiency
| stage | season | finding |
|---|---|---|
| SOG given attempts (on-net) | 2024-25 / 2025-26 | shrunk player rate vs pooled 47.7%: −0.0026 [−0.0050, −0.0000] / +0.0011 [−0.0013, +0.0036] nats per skater-game: **no player-level on-net skill worth modelling** |
| SOG per 60 given actual TOI | 2025-26 | incumbent rate MAE 0.996 vs recent rate 1.036; Poisson deviance −0.159 [−0.183, −0.138]: the incumbent's shot-generation rate is good |
| goals given SOG | 2025-26 | player shrunk shooting % vs pooled 11.0%: 0.7372 vs 0.7387 nats: negligible |
| saves given shots against | 2025-26 | goalie shrunk save % vs league: −0.0029 [−0.0078, +0.0019] nats per start: negligible |

### What drives the stat errors
* Saves: incumbent MAE 5.35 (2025-26); applying the incumbent's own saves-per-expected-shot ratio to the ACTUAL team
  shots faced: 2.10. Saves error is shot-volume (opportunity), not save % (efficiency).
* Goals / assists / points: swapping the incumbent's TOI for the recent-mean TOI changes Poisson deviance by
  −0.0002 / +0.0002 / −0.0000 (all CIs include 0): the allocation uses shares, so TOI level does not drive them.
* SOG: replacing incumbent TOI by recent-mean TOI changes deviance by −0.0011 [−0.0024, +0.0002]; oracle TOI lowers
  SOG MAE only 1.013 → 0.996.

**Isolated errors:** (i) team shot volume level (+0.59 shots in 2024-25, after the league level fell 30.1 → 28.1;
only +0.14 in 2025-26), the dominant part of saves error; (ii) the TOI minute budget (no OT minutes, fixed PP/SH 4.4
min vs 4.8 accounted): −0.23 / −0.39 min bias, worse than a plain mean in OT games and for PP-role players. Only (i)
was taken forward (one challenger); (ii) is a documented next step.

## 2. Challenger NHL_SHOT_VOLUME_V1 on the untouched 2025-26 holdout

1,312 games, 0 excluded; 47,231 skater rows per skater statistic, 2,624 starting-goalie rows; identical rows across
the three arms. Coherence: 0 violations over 5,248,000 draws (SOG ≥ goals, Σ skater SOG = team goals + opposing net
non-goal shots, points = goals + assists); 0 incumbent invariant violations. Points, assists and TOI rows are
bit-identical to the incumbent (Δ = 0 exactly). Δ = challenger − reference; CIs: paired game-cluster bootstrap.

| statistic | metric | incumbent | challenger | Δ vs incumbent [95% CI] | baseline | Δ vs baseline [95% CI] |
|---|---|---|---|---|---|---|
| goalie_saves | MAE | 5.350 | 5.351 | +0.001 [−0.009, +0.012] | 5.665 | −0.314 [−0.394, −0.235] |
| goalie_saves | MSE (RMSE) | (6.822) | (6.829) | +0.09 [−0.05, +0.24] | (7.220) | −5.50 [−6.71, −4.32] |
| goalie_saves | CRPS | 3.7946 | 3.7963 | **+0.0016 [−0.0046, +0.0080]** | 4.1128 | −0.3166 [−0.3739, −0.2613] |
| goalie_saves | log score | 3.3302 | 3.3277 | −0.0025 [−0.0087, +0.0040] | 3.5299 | −0.2022 [−0.2316, −0.1731] |
| goalie_saves | Brier (pure_gate rung) | 0.24932 | 0.24945 | +0.00013 [−0.00055, +0.00091] | 0.26798 | −0.02327 [−0.02906, −0.01729] |
| goalie_saves | bias | −0.08 | +0.15 | | +0.98 | |
| shots_on_goal | MAE | 1.0111 | 1.0196 | **+0.0085 [+0.0070, +0.0099]** | 1.0563 | −0.0368 [−0.0402, −0.0332] |
| shots_on_goal | MSE (RMSE) | (1.3254) | (1.3199) | −0.0144 [−0.0191, −0.0102] | (1.3693) | −0.1327 [−0.1440, −0.1215] |
| shots_on_goal | CRPS | 0.6899 | 0.6872 | −0.0027 [−0.0036, −0.0018] | 0.7174 | −0.0302 [−0.0325, −0.0279] |
| shots_on_goal | log score | 1.5482 | 1.5417 | −0.0065 [−0.0080, −0.0051] | 1.5935 | −0.0518 [−0.0557, −0.0479] |
| shots_on_goal | Brier (pure_gate rung) | 0.24234 | 0.24161 | −0.00073 [−0.00113, −0.00032] | 0.25277 | −0.01285 [−0.01391, −0.01173] |
| shots_on_goal | bias | −0.081 | +0.013 | | +0.012 | |
| points / assists / TOI | all | identical | identical | 0 (bit-identical) | | |

Brier rows come from the vendored `pure_gate compare` (its own rung choice per pair and 1,000-replicate bootstrap, seed
20261010); all 15 scorecards and the 15 `validate --require-v1` results (all exit 0) are in
`holdout_2025/shot_volume_eval_2025.json`; a 40-game sample of every sidecar + outcomes is in `holdout_2025/pure_sidecar_sample/`
(full sidecars are regenerable with the commands below).

**Rule check:** (a) saves ΔCRPS < 0 with CI excluding 0 — **fails** (+0.0016, CI spans 0); (b) no metric worse with CI
excluding 0 — **fails** (SOG MAE of the mean +0.0085, CI excludes 0); (c) vs baseline — passes; (d) coherence — passes;
(e) identical points/assists/TOI — passes; (f) rerun — passes. **REJECTED.**

Reading: the level-drift fix that helped in 2024-25 (saves ΔCRPS −0.0099 [−0.0175, −0.0021]) had nothing to fix in
2025-26, when the league shot level moved only 28.1 → 27.6 and the incumbent's saves were already unbiased (−0.08);
the challenger overshoots (+0.15). The coherent SOG allocation is better on every proper score (CRPS, log score,
Brier, MSE; team-level SOG correlation 0.23 → 0.32 on 2024-25) but its mean is higher and nearly unbiased (+0.013 vs
−0.081), and absolute error of the mean rewards under-predicting right-skewed counts, so MAE worsens; this was
disclosed from the development season before freezing and the rule was not changed.

Subgroups (descriptive): SOG ΔCRPS F −0.0038 [−0.0049, −0.0027], D −0.0005 [−0.0019, +0.0009]; saves ΔCRPS Oct–Nov
+0.0030 [−0.0084, +0.0150], Dec+ +0.0010 [−0.0072, +0.0085].

TOI note from the holdout (incumbent vs baseline): TOI MAE +0.0137 [+0.0025, +0.0245], CRPS +0.0366 [+0.0296, +0.0433]:
on 2025-26 the incumbent's TOI is worse than a plain recent mean, which strengthens finding (ii).

## 3. Market independence
* Runtime: vendored `pure_gate rerun` (sift-sports-intelligence@558c592) ran the actual challenger on six 2025-26 games
  with the Kalshi quote file (`rerun/kalshi_player_quotes_T60.csv`, real T-60m mids from the committed Kalshi history)
  normal x2, deleted and randomized x2: model output bit-identical in all five arms (sha256 `9549031f…`); the negative
  control (the existing MARKET_ANCHORED_PLAYER_V1 blend, `--use-market-center`) failed when the file was deleted and
  changed under both randomizations (`7f30aacc…`, `eb0f3b9a…` vs normal `8c3e48b5…`). Verdict
  **PASS_RUNTIME_NONLEAKAGE** (`rerun/rerun_result.json`).
* Indirect: no market-selected population (every dressed skater / every starter), no price-fitted parameter (saves NB
  refit on boxscores; hyper-parameters are the incumbent's), outcomes from the official boxscore. Audit table in the
  audit doc.

## 4. Starting-goalie confirmation (2026-27 archive, descriptive; historical timing does not exist)
146 team-games (73 games to 2026-10-11) with a pregame DailyFaceoff observation: last pregame status CONFIRMED 99/100
named goalie started, PROBABLE 27/29, PROJECTED 13/17 (the model's priors are 0.985 / 0.85 / 0.70). Too small for any
saves comparison; the holdout is conditional on the actual starter.

## 5. Commands
```
python -m nhl_edge.research.opportunity_efficiency --season 2024 --sim-cache <dir> --out <dir>
python -m nhl_edge.research.opportunity_efficiency --season 2025 --sim-cache docs/research/player_sim_v1 --out <dir>
python -m nhl_edge.research.shot_volume_v1 --season 2025 --out <rows dir>
python -m nhl_edge.research.shot_volume_eval --rows <rows dir> --season 2025 --out <dir> --gate-work <dir>
python scripts/research_pure_rerun.py --workdir <dir> --out rerun_result.json
python scripts/research_starter_confirmation.py --ref origin/data-archive --out starter.json
```
