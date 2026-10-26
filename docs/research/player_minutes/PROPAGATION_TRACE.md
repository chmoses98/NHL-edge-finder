# How ice time propagates through the production player model (PLAYER_SIM_V1), and what correcting it is worth

RESEARCH_ONLY. Development evidence (exposed seasons 2022–2025, each test season scored with factors fitted on earlier seasons only); it selects a specification and validates nothing. The production model, the preregistered `player-minutes-1.0` records and every frozen parameter file are untouched. Code: `src/nhl_edge/research/minutes_propagation.py`; raw output: `propagation_trace.json`.

## 1. The trace (code, not assumption)
1. **Share.** Per player and strength state (EV, PP, SH, own-net-empty EA, opponent-net-empty EN, OT): recency-weighted share of his team's seconds in that state, 6-game half-life, shrunk with 0.5 pseudo-games toward the position mean (`players/features.py`). Tonight's DailyFaceoff slot (when a lines source exists) is blended in with 3 (confirmed) or 1.5 (projected) pseudo-games (`players/roster.py`).
2. **Absolute minutes.** `expected_toi[state] = share[state] × team_minutes[state]` with `team_minutes` **hard-coded** in `workflows/shadow_player.py`: EV 50.6, PP `4.4 × p_pp / 0.215`, SH **4.4 (not matchup-dependent)**, EA 0.6, EN 0.6, OT 1.2 (sum 61.8).
3. **Where minutes are used.** `meta.expected_toi_min` / `expected_pp_toi_min` (published as the incumbent ice-time forecasts) and **expected shots** = Σ over EV/PP/SH of state minutes × the player's shots-per-60 in that state (verified exact: correlation 1.0000 with the archived champion shots). 
4. **Where minutes are NOT used.** Goals, assists and points are allocated from the **shares** and per-state rates (scorer weight = share × xG/60 × finishing × on-ice factor; assists by co-ice fractions); the team's goal count comes from the team simulation. The absolute team-minute constants therefore do not move goals/assists/points; a per-draw lognormal ice-time multiplier (σ 0.16) and a small early-exit probability only reweight who scores.
5. **Role currency.** Shares move with a 6-game memory; the stored lines input can only add a template when a lines source exists. Nothing uses the last game's actual minutes directly.

## 2. Findings
| # | finding | evidence |
|---|---|---|
| F1 | **The team-minute constants are wrong.** League mean team minutes per game 2023–25 (7,872 team-games): EV 50.6, **PP = SH = 5.14** (constants: 4.4, 4.4), EA 0.54, EN 2.98, total **64.4** vs 61.8 in the model. | `propagation_trace.json › team_minutes` |
| F2 | They show up as a **systematic under-prediction**: total ice time −0.29 min/skater-game (−1.7 %), **PP time −16 %, SH −15 %**; PP/SH fixed too low by ~14 %. Worse for heavy-usage players (bias by projected-TOI quintile: −0.04, −0.20, −0.32, −0.42, −0.45 min) and worse each season (−0.21, −0.28, −0.37 in 2023, 2024, 2025). | incumbent frames, 141,677 skater-games |
| F3 | Because shots = minutes × rate, the minutes error is **half of the shots bias** (champion shot bias −0.063 → −0.030 once minutes are recalibrated; the other half is the shot-rate level, which the LC level calibration addresses). | table below |
| F4 | Short-memory role information is missing: after recalibration, the frozen last-3-games usage term still removes a further 3.1 % of total-ice-time MSE. | table below |
| F5 | Goals/assists/points are insulated from F1–F2 by construction (share-based), so the fix does not touch the priced goal/assist/point ladders. | trace 4 |

## 3. What recalibrating and adding usage is worth (paired, game-clustered 95 % intervals; change vs the incumbent)
Per-state factors fitted on earlier seasons (2023: ×0.98 EV, ×1.24 PP, ×1.24 SH; 2024 and 2025 similar); 141,677 skater-games, 2023–25.

| arm | total TOI MSE | PP TOI MSE | shots Poisson deviance | shots bias |
|---|---|---|---|---|
| incumbent | 6.405 | 1.423 | 1.2506 | −0.063 |
| **per-state recalibration only** | −0.127 (−2.0 %) [−0.143, −0.110] | −0.074 (−5.2 %) [−0.090, −0.059] | −0.0047 [−0.0052, −0.0042] | −0.030 |
| recalibration + frozen last-3 usage | **−0.323 (−5.0 %)** [−0.345, −0.302] | −0.079 [−0.095, −0.064] | −0.0061 [−0.0067, −0.0056] | −0.032 |
| WORKLOAD_V1 minutes (champion shot rates) | −0.285 (−4.5 %) [−0.305, −0.267] | **−0.114 (−8.0 %)** [−0.128, −0.099] | −0.0060 [−0.0067, −0.0053] | −0.034 |
| WORKLOAD_V1 + usage | −0.329 (−5.1 %) | −0.114 | −0.0065 [−0.0073, −0.0057] | −0.035 |

Reading: (a) **a recalibration of the constants plus the usage term gets essentially all of WORKLOAD_V1's total-ice-time gain** (−0.323 vs −0.329) with a few lines of change inside the existing model; (b) for **power-play time WORKLOAD_V1 is still clearly better** (−0.114 vs −0.079); (c) for **shots, minutes explain little** (deviance −0.5 % at best): the shot rate level, not minutes, is where the remaining shots error sits (LC's level calibration is the larger lever); (d) the incumbent is **not** missing the minutes→goals connection (it deliberately has none).

## 4. Readiness
| change | evidence | ready for a formal promotion decision? |
|---|---|---|
| Replace the hard-coded team-minute constants by league-calibrated values (and make SH follow the opponent's PP expectation) | measured on 7,872 team-games, walk-forward gain on all three targets, no model re-estimation | **Yes, as a decision to take**, but it changes the published incumbent ice-time, power-play and shots forecasts, so it needs your explicit approval; a draft is described below, not applied. Recommended to accompany it with a prospective shadow arm. |
| Add the frozen last-3 usage term to total ice time | development evidence only here; prospective test is `player-minutes-1.0` H3 | No (wait for H3). |
| WORKLOAD_V1 minutes as the ice-time engine | prospective test `player-minutes-1.0` H1/H2 | No (looks not reached). |

Draft of the constants change (not applied): `team_min = {"ev": 50.6, "pp": 5.14 × p_pp / 0.215, "sh": 5.14 × opp_p_pp / 0.215, "ea": 0.54, "en": 2.98, "ot": …}` with the OT state re-derived from the player frames (the fitted OT factor of ~3.3 says the share×1.2 convention under-counts OT time and is internally inconsistent with the other states); the factors above are the walk-forward estimates, so any final values should come from a registered fit on seasons through 2025.
