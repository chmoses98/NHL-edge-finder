# Overtime timeline fix: what it changes (2026-10-12)

**Scope:** a data-quality fix in `data.player_events` plus an offline before/after study. The committed history
(`data/history/players`) and the deployed parameters (`data/params/player-sim-1.0.json`) are **not** regenerated here.
Regenerating them changes production deployment shares and needs an explicit owner decision. Outputs:
`docs/research/ot_timeline_fix/*.json`. Code: `src/nhl_edge/research/ot_timeline_effect.py`. Tests:
`tests/test_ot_timeline.py`.

## The defect

`derive_game` laid every overtime game out to the end of a 20-minute grid period, so `n_seconds` was 4,800 for all
2,918 regular-season OT team-game rows (1,459 games, 2021-26). `state_timeline` filled the seconds after the final
whistle with the last situation code it had seen. Fixed: `game_length_s` ends the timeline at the last non-shootout
event (the overtime winner, or 3,900 s when a shootout followed the full 5-minute overtime). Schema
`nhl-player-events-1.1`.

Real games (raw official payloads under `tests/fixtures/nhl_games`, fetched on a GitHub runner in run 38196512437),
team seconds before -> after:

| game | type | n_seconds | where the phantom went |
|---|---|---|---|
| 2025020008 | 3-on-3 OT winner at 2:12 | 4,800 -> 3,732 | EN: home 1,101 -> 33, away 1,078 -> 10 |
| 2025020099 | 4-on-3 power-play OT winner at 2:24 | 4,800 -> 3,744 | EN: 1,056 -> 0 both sides |
| 2025020006 | shootout | 4,800 -> 3,900 | home PP / away SH: 1,240 -> 340 |
| 2025020001 | regulation | 3,600 -> 3,600 | unchanged |

## Rebuild check (2021-22 .. 2025-26, all 6,993 games (regular season + playoffs) re-derived with the fix on a runner, scratch only)

`tables.json`. Same games, same row counts, every regular-season OT row changed in exactly **one** state, and every
new timeline sums to the seconds actually played (mean 3,792 s, range 3,604-3,900). Regulation rows are unchanged.

Phantom minutes removed, 2021-26: **EN 32,490**, EV 14,647, PP 745, SH 745, EA 411. Most of the phantom sat in EN
(the end-of-game situation code shows an empty net), not in PP / SH.

Goals, shots and goalie lines are unchanged. In skater lines only 4 rows (2 games) changed: shift-chart shifts that ran
past the final whistle had been counted as EN / OT ice time (up to 247 s). Those rows now match the boxscore TOI exactly.

## Effect on production (PLAYER_SIM_V1), before -> after (walk-forward, paired game-clustered bootstrap, 2,000 resamples)

Production TOI / PP / SOG path: `build_roster` with the production team-minute template (`production_*.json`).
Shift-chart skater-games: n = 45,176 (1,255 games) for 2024-25 and 47,231 (1,312 games) for 2025-26. Each cell is
before -> after, then the difference (after - before) of the per-row loss, with its 95% CI.

| metric | 2024-25 | 2025-26 |
|---|---|---|
| total TOI MAE (min) | 1.879 -> 1.863; -0.017 [-0.022, -0.012] | 1.934 -> 1.897; -0.037 [-0.043, -0.030] |
| total TOI bias | -0.216 -> **+0.152** | -0.336 -> **+0.129** |
| total TOI MAE, OT games | 2.090 -> 1.982 (n 9,071) | 2.182 -> 2.031 (n 11,736) |
| total TOI MAE, regulation games | 1.827 -> 1.833; +0.006 [+0.002, +0.011] | 1.852 -> 1.853; +0.001 [-0.005, +0.007] |
| EV TOI MAE / bias | 1.814 -> 1.812 / +0.011 -> +0.167 | 1.853 -> 1.853 / -0.008 -> **+0.238** |
| PP TOI MAE / bias | 0.757 -> 0.757 / -0.142 -> -0.140 | 0.790 -> 0.789 / -0.193 -> -0.187 |
| SH TOI MAE / bias | 0.646 -> 0.646 / -0.107 -> -0.105 | 0.665 -> 0.665 / -0.179 -> -0.174 |
| PP share MAE | 0.1047 -> 0.1046 (n 43,897) | 0.1041 -> 0.1039; -0.0002 [-0.0003, -0.0001] (n 46,186) |
| SOG MAE | 1.0223 -> 1.0240; +0.0017 [+0.0015, +0.0020] | 1.0110 -> 1.0128; +0.0019 [+0.0016, +0.0021] |
| SOG MSE | -0.0011 [-0.0018, -0.0004] (RMSE 1.3291 -> 1.3287) | -0.0043 [-0.0053, -0.0033] (RMSE 1.3249 -> 1.3233) |
| SOG bias | -0.029 -> -0.014 | -0.079 -> -0.055 |

PLAYER_SIM_V1 walk-forward (`research.player_walk_forward.simulate`, 4,000 draws, same seeds; `walk_forward_*.json`;
47,225 / 47,231 skater-games and 2,624 starts per season):

| metric | 2024-25 | 2025-26 |
|---|---|---|
| goals 1+ Brier | 0.1180 -> 0.1180; diff -0.000004 [-0.000018, +0.000009] | 0.1199 -> 0.1199; diff -0.000016 [-0.000030, -0.000002] |
| assists 1+ Brier | 0.1687 -> 0.1687 | 0.1711 -> 0.1711 |
| points 1+ / 2+ Brier | 0.2020 / 0.0724, unchanged | 0.2035 / 0.0751, unchanged |
| saves mean, ladder 14+..40+ Brier | identical (5.30 MAE, 0.1316) | identical (5.35 MAE, 0.1313) |
| walk-forward expected TOI (its own template, no OT minutes) MAE | 1.882 -> 1.862; -0.020 [-0.022, -0.017] | 1.943 -> 1.902; -0.041 [-0.045, -0.036] |

Saves are identical by construction: goals against come from the team draw, not from deployment shares. Scoring
probabilities barely move because the scorer weights renormalise within the team.

## What this means

* The fix removes the OT under-count. The OT share is no longer ~1/6 of reality, and total-TOI MAE improves in OT
  games.
* **The production team-minute template was calibrated on the defective data.** Its `ev 50.6` is the mean of the
  inflated EV seconds (regulation games: about 48.6), and `ot 1.2` / `en 0.6` now multiply real shares. After the fix the
  template over-states EV minutes (+0.17 / +0.24 min bias) and total TOI in regulation games (+0.27).
* **PP / SH bias is not caused by this defect.** It barely moves (-0.193 -> -0.187). Almost no phantom time sat in
  PP / SH. The cause is the template's PP minutes: `4.4 x p_pp / 0.215` averages 4.45, while teams actually play about
  5.1 PP minutes per regulation game. This corrects the attribution in the workload audit (PR #28), which named the
  timeline as the root cause of the PP / SH bias.
* Net effect on what is priced today: SOG RMSE slightly better and SOG MAE slightly worse; goals / assists / points /
  saves unchanged to four decimals.

## How the deployed parameters would change (`params_diff.json`; computed in memory, file NOT written)

`players.fit.fit_all` on the rebuilt history vs the committed history. 26 of 196 numeric entries change, all
deployment-share priors (the xG model, strength table, saves model and TOI noise are identical up to floating-point
summation order):

| prior | old -> new |
|---|---|
| `share_median` OT (F / D) | 0.027 / 0.029 -> **0.168 / 0.177** (x6.2) |
| `share_median` EN (F / D) | 0.180 / 0.245 -> 0.243 / 0.330 (+35%) |
| `share_median` EV (F / D) | 0.245 / 0.324 -> 0.249 / 0.329 (+1.6%) |
| `share_median` PP, SH, EA | +0.2% to +0.4% |
| `fringe.share` OT / EN / EV | x5.7, +39%, +1.6% (same pattern) |
| `en60` (F / D) | +0.06% / +0.03% |

## Recommended order (owner decisions, not done here)

1. Merge this fix: newly settled games (the settle job derives them live) get correct timelines.
2. Re-derive `data/history/players` with the fix (`player_research_data.yml`), then decide on the parameter refit
   (`python -m nhl_edge.players.fit`). Both change production deployment shares.
3. Recalibrate the production team-minute template from the fixed data at the same time: EV regulation minutes, PP / SH
   minutes per matchup, and OT minutes = P(OT) x mean OT length. Otherwise the fix alone shifts the EV / total TOI bias
   from negative to positive.
