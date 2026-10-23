# WORKLOAD_V1 historical replication (held-out 2023-24 and 2024-25; 2025-26 re-run as a check)

**Authority: RESEARCH_ONLY. This is a PROJECTION-quality result. Kalshi lists no NHL shots-on-goal market
(`KALSHI_MARKET_MAP.md`), so nothing here prices, sizes or routes any bet, and nothing changes production, stakes, caps,
SIFT contracts or the frozen preregistration.** Everything is HISTORICAL (walk-forward on committed official-API data);
no prospective result exists yet. Data: `workload_v1/replication_2023_2024_2025.json` (run 2026-10-22).
Code: `src/nhl_edge/research/workload_replication.py` (new; no modelling code changed).

## Verdict

| held-out season | what it is | skater-games / games | CRPS vs production (95% CI) | RMSE vs production | WORKLOAD_V1 bias | preregistered rule |
|---|---|---|---|---|---|---|
| **2023-24** | the only truly untouched season (not used to fit or select anything) | 47,221 / 1,312 | **-0.00616** [-0.00742, -0.00498] (-0.86%) | -0.0119 [-0.0143, -0.0097] (-0.87%) | **+0.053** [+0.039, +0.065] | **REJECTED**: 6 of 7 checks pass, `abs(bias) <= 0.05` fails by 0.003 |
| 2024-25 | the preregistration's VALIDATION season: `frozen_params` were selected on it | 47,225 / 1,312 | -0.00527 [-0.00630, -0.00427] (-0.76%) | -0.0083 [-0.0102, -0.0065] (-0.63%) | +0.047 [+0.035, +0.059] | ACCEPTED (7 of 7), **but not independent evidence** (hyperparameters were chosen to minimise CRPS here) |
| 2025-26 (the original) | held-out in the preregistration | 47,231 / 1,312 | -0.00695 [-0.00812, -0.00577] (-1.01%) | -0.0130 [-0.0153, -0.0108] | +0.030 [+0.017, +0.042] | ACCEPTED (7 of 7) |

Plain reading:

* **The accuracy gain replicated on the one clean season.** On 2023-24 WORKLOAD_V1 beats the production expected SOG by
  0.86% in CRPS and 0.87% in RMSE with every CI excluding zero, close to 2025-26 (1.0%). Direction, size and the
  workload-minutes fix all repeat.
* **The preregistered acceptance did not replicate.** The bias check (`|bias| <= 0.05` shots per skater-game) fails on
  2023-24 at +0.0525. The preregistration warned about exactly this (validation bias was +0.047 against the 0.05 limit).
  The 95% CI of the bias, [+0.039, +0.065], straddles the limit, so the miss is small and not statistically distinguishable
  from the limit, but the rule is the rule: **no threshold was moved, and the formal verdict for 2023-24 is REJECTED.**
  Calling this a clean replication would be wrong; calling it a failed one on the strength of 0.003 shots would also
  overstate it. Both statements are true: the gain replicated, the frozen acceptance rule did not pass.
* WORKLOAD_V1 over-predicts in all three seasons (+0.053, +0.047, +0.030 shots per skater-game, 2-3% of the mean; the
  production mean under-predicts in all three: -0.064, -0.040, -0.085). The league mean fell 1.683 -> 1.571 -> 1.546
  shots per skater-game over these seasons, which is consistent with the point-in-time league rates lagging a falling
  level, but that was not tested and is not tuned here.
* **The gain is small.** CRPS improves 0.8-1.0%, RMSE 0.6-1.0%. The production mean is itself only about 0.5-0.75% better
  in CRPS than a naive "exponentially weighted SOG per game" baseline; WORKLOAD_V1 is about 1.4-1.6% better than that
  baseline. Most of the error of any pregame model is Poisson-like count noise (`WORKLOAD_AUDIT.md` section 4).
  MAE is worse in all three seasons (+0.004 to +0.005, CI excludes zero); MAE is not a proper score for a mean forecast
  (the champion's under-prediction sits closer to the median of a skewed count) but it is reported as asked.

## Which seasons can be held out without leakage

Cached official-API data (`data/history/players/MANIFEST_*.json`): 2021-22 .. 2025-26, 1,312 regular-season games each, 100%
shift charts except 2024-25 (57 games without shift charts: their state minutes are unknown, so they are in the SOG scoring
but not in the minutes tables). `*_2026` holds 3 games (2026-09-29) and is not a season. V2 walk-forward CSV: 2024 and 2025 only.

The frozen protocol needs training seasons strictly before the evaluated season and a NegBin dispersion season right before
it, and that dispersion season needs its own production-champion frame, so it needs at least one earlier season too.

| held-out | training | dispersion season | feasible |
|---|---|---|---|
| 2021-22 | none | n/a | no |
| 2022-23 | 2021 | 2021 (no earlier season for the champion) | **no** |
| 2023-24 | 2021, 2022 | 2022 | **yes** |
| 2024-25 | 2021-2023 | 2023 | yes, but it is the validation season |
| 2025-26 | 2021-2024 | 2024 | yes (original) |

So exactly one new, uncontaminated season exists (2023-24). It has only two training seasons (the original had four), so
player histories and league constants are thinner there; that is a harder, not an easier, test.

## What was run, and the one thing that was not in the original

`python -m nhl_edge.research.workload_replication --seasons 2023,2024,2025 --leakage-check`. It calls the existing
`workload_experiment.skater_arms / skater_report / accept_skaters` unchanged, with the frozen parameters and acceptance rule
read from the untouched `preregistration.json`, the same arms, metrics, 2,000-resample game-clustered bootstrap (seed
20261012) and the same seven checks. No modelling file, constant, feature, threshold or preregistration file changed;
`workload_experiment.py` still refuses `evaluate` on any season but 2025. Goalie saves (REJECTED originally) were not re-run.

The production champion (PLAYER_SIM_V1 `expected_sog`) needs a walk-forward stand-in for the team's PP share (point-in-time
penalty-minute and PP/PK ratings). The committed CSV has it for 2024 and 2025 only. For 2022 and 2023 I re-derived those
columns with `walk_forward_v2.game_features` (the code that produced the committed rows; no simulation, no market input).
**Before using it, the re-derivation reproduced the committed 2024-25 rows exactly (max abs difference 0.0 on all eight
columns, 1,312 games).** This is the primary ("derived") champion. The champion normalises PP shares by the mean of the rows
it is given; "derived" passes only seasons up to the evaluated one (the original passed 2024 and 2025 together).

Sensitivity ("coded"): `Ctx.wf_for` exactly as written, i.e. the CSV where it has the season and constant NEUTRAL PP minutes
elsewhere. It reproduces the original 2025-26 result to the reported digits (CRPS -0.00656 [-0.00771, -0.00541], bias +0.030),
which confirms the harness and environment are faithful. For 2023-24 it handicaps the champion badly (bias -0.260, CRPS 0.7485,
**worse than the naive baseline 0.7232**) and inflates the gain to -0.0355; that is a straw man and is not used as evidence.
For 2024-25 coded and derived agree (CRPS -0.00502 vs -0.00527; champion 0.6939 vs 0.6942; coded 2024 also matches
`validation_2024.json`: 0.6889 vs 0.6939). Verdicts are the same in both modes for every season.

## Results (primary, derived stand-in)

### 2023-24 (held out; trained on 2021-22; dispersion on 2022-23)

| arm | MAE | RMSE | bias | CRPS | ladder Brier | cov50 | cov80 |
|---|--:|--:|--:|--:|--:|--:|--:|
| BASELINE | 1.0716 | 1.3779 | +0.015 | 0.7232 | 0.13686 | 0.480 | 0.784 |
| CHAMPION | 1.0555 | 1.3731 | -0.064 | 0.7192 | 0.13608 | 0.479 | 0.780 |
| CHAMPION_NB | 1.0555 | 1.3731 | -0.064 | 0.7195 | 0.13620 | 0.504 | 0.805 |
| WORKLOAD_ONLY | 1.0560 | 1.3700 | -0.037 | 0.7175 | 0.13581 | 0.502 | 0.803 |
| EFFICIENCY_ONLY | 1.0538 | 1.3675 | -0.047 | 0.7158 | 0.13549 | 0.502 | 0.804 |
| **WORKLOAD_V1** | 1.0606 | **1.3611** | **+0.053** | **0.7130** | **0.13497** | 0.496 | 0.799 |

Differences, WORKLOAD_V1 minus reference (95% game-clustered CI):

| comparison | CRPS | RMSE | ladder Brier | MAE |
|---|---|---|---|---|
| vs CHAMPION | -0.00616 [-0.00742, -0.00498] | -0.0119 [-0.0143, -0.0097] | -0.00111 [-0.00135, -0.00089] | +0.0051 [+0.0032, +0.0070] |
| vs CHAMPION_NB | -0.00646 [-0.00775, -0.00526] | -0.0119 [-0.0143, -0.0097] | -0.00123 [-0.00147, -0.00100] | +0.0051 [+0.0032, +0.0070] |
| vs BASELINE | -0.01015 [-0.01148, -0.00887] | -0.0168 [-0.0195, -0.0143] | -0.00190 [-0.00215, -0.00166] | -0.0110 [-0.0131, -0.0089] |

Seven preregistered checks: CRPS vs CHAMPION yes; CRPS vs CHAMPION_NB yes; RMSE vs CHAMPION yes; ladder Brier vs CHAMPION_NB
yes; **`|bias| 0.0525 <= 0.05` NO**; 80% coverage 0.799 in [0.77, 0.83] yes; CRPS no worse for forwards (0.7586 vs 0.7654)
and defence (0.6235 vs 0.6294) yes. **REJECTED.**

### 2024-25 (validation season; trained on 2021-23; dispersion on 2023-24) - NOT independent

| arm | MAE | RMSE | bias | CRPS | ladder Brier | cov50 | cov80 |
|---|--:|--:|--:|--:|--:|--:|--:|
| BASELINE | 1.0406 | 1.3377 | +0.038 | 0.6994 | 0.13395 | 0.481 | 0.784 |
| CHAMPION | 1.0226 | 1.3300 | -0.040 | 0.6942 | 0.13293 | 0.478 | 0.780 |
| CHAMPION_NB | 1.0226 | 1.3300 | -0.040 | 0.6939 | 0.13291 | 0.499 | 0.801 |
| WORKLOAD_ONLY | 1.0245 | 1.3284 | -0.012 | 0.6927 | 0.13267 | 0.498 | 0.800 |
| EFFICIENCY_ONLY | 1.0176 | 1.3270 | -0.054 | 0.6913 | 0.13239 | 0.500 | 0.801 |
| **WORKLOAD_V1** | 1.0263 | **1.3217** | +0.047 | **0.6889** | **0.13192** | 0.495 | 0.798 |

| comparison | CRPS | RMSE | ladder Brier | MAE |
|---|---|---|---|---|
| vs CHAMPION | -0.00527 [-0.00630, -0.00427] | -0.0083 [-0.0102, -0.0065] | -0.00101 [-0.00121, -0.00082] | +0.0037 [+0.0021, +0.0054] |
| vs CHAMPION_NB | -0.00504 [-0.00611, -0.00400] | -0.0083 [-0.0102, -0.0065] | -0.00099 [-0.00120, -0.00078] | +0.0037 [+0.0021, +0.0054] |
| vs BASELINE | -0.01049 [-0.01176, -0.00923] | -0.0160 [-0.0184, -0.0136] | -0.00203 [-0.00228, -0.00179] | -0.0144 [-0.0164, -0.0123] |

All seven checks pass (bias +0.0468, cov80 0.798; forwards 0.7249 vs 0.7300, defence 0.6179 vs 0.6227). This reproduces the
CRPS in `validation_2024.json` (0.6889) and so measures nothing new: the 48-point skater grid was searched on this season.

### 2025-26 re-run (check only)

CRPS vs CHAMPION -0.00695 [-0.00812, -0.00577], RMSE -0.0130 [-0.0153, -0.0108], bias +0.030, ACCEPTED (derived stand-in).
The original number (-0.00656, coded mode) is reproduced exactly; the 0.0004 difference is the champion's stand-in normalisation.

### Where the gain comes from (all seasons agree)

Arm differences vs CHAMPION_NB, CRPS: WORKLOAD_ONLY -0.0020 / -0.0012 / -0.0018 and EFFICIENCY_ONLY -0.0037 / -0.0027 /
-0.0036 (2023 / 2024 / 2025), all CIs exclude zero, and together they give the full -0.005 to -0.007. Efficiency (league-relative
shrunk rates plus the opponent/venue factor) contributes about twice as much as workload, as in the original. SOG given the
ACTUAL minutes: squared-error difference vs champion rates -0.0347 [-0.0419, -0.0281] (2023), -0.0235 [-0.0296, -0.0180]
(2024), -0.0332 [-0.0392, -0.0269] (2025).

## Workload minutes, scored separately (minutes per skater-game, shift-chart rows)

Cells are MAE / RMSE / bias. "MAE diff" is WORKLOAD_V1 minus champion absolute error with a game-clustered 95% CI.

| season | minutes | champion | WORKLOAD_V1 | MAE diff |
|---|---|---|---|---|
| 2023-24 (n 47,221) | total TOI | 1.933 / 2.556 / -0.207 | 1.883 / 2.508 / +0.045 | -0.050 [-0.055, -0.044] |
| | PP TOI | 0.801 / 1.211 / -0.250 | 0.803 / 1.153 / +0.024 | +0.002 [-0.006, +0.010] |
| | SH TOI | 0.683 / 1.033 / -0.220 | 0.683 / 0.984 / +0.013 | -0.000 [-0.007, +0.006] |
| | EV incl. OT | 1.843 / 2.395 / +0.195 | 1.824 / 2.373 / -0.045 | -0.019 [-0.028, -0.010] |
| 2024-25 (n 45,176) | total TOI | 1.886 / 2.479 / -0.262 | 1.834 / 2.426 / +0.032 | -0.052 [-0.057, -0.046] |
| | PP TOI | 0.758 / 1.150 / -0.188 | 0.766 / 1.109 / +0.044 | +0.008 [+0.000, +0.015] |
| | SH TOI | 0.646 / 0.971 / -0.107 | 0.653 / 0.949 / +0.036 | +0.007 [+0.002, +0.012] |
| | EV incl. OT | 1.815 / 2.362 / +0.012 | 1.795 / 2.337 / -0.102 | -0.020 [-0.028, -0.011] |
| 2025-26 (n 47,231) | total TOI | 1.942 / 2.553 / -0.375 | 1.875 / 2.484 / -0.008 | -0.066 [-0.073, -0.060] |
| | PP TOI | 0.792 / 1.215 / -0.232 | 0.795 / 1.168 / -0.015 | +0.003 [-0.004, +0.010] |
| | SH TOI | 0.665 / 1.020 / -0.179 | 0.671 / 0.987 / -0.016 | +0.005 [+0.000, +0.011] |
| | EV incl. OT | 1.853 / 2.410 / -0.008 | 1.834 / 2.388 / -0.038 | -0.020 [-0.027, -0.012] |

(2025-26 here is the re-run with the derived stand-in; the original doc's champion row differs in the third decimal.)

The workload claim replicates: RMSE falls for total, PP, SH and EV minutes in every season, and total-TOI MAE improves
(-0.05 to -0.07 min). The champion's systematic PP/SH/total under-prediction (total -0.21 to -0.38 min) is mostly removed; the
challenger's total bias is +0.045 / +0.032 / -0.008. **PP and SH MAE do not improve** (2024-25: +0.008 and +0.007, CIs exclude
zero in the wrong direction; 2023-24 and 2025-26: indistinguishable from zero). The RMSE and bias gains are real; there is no
median-accuracy gain on PP/SH minutes.

Per position / overtime (descriptive; mean error in minutes, champion -> WORKLOAD_V1):

| season | group | total TOI bias | PP bias | SH bias |
|---|---|---|---|---|
| 2023-24 | forwards (31,291) | -0.202 -> +0.056 | -0.284 -> +0.026 | -0.168 -> +0.012 |
| | defence (15,930) | -0.215 -> +0.022 | -0.184 -> +0.021 | -0.324 -> +0.015 |
| | OT games (9,791) | -0.632 -> -0.373 | -0.242 -> +0.028 | -0.213 -> +0.016 |
| | regulation (37,430) | -0.095 -> +0.154 | -0.252 -> +0.023 | -0.222 -> +0.013 |
| 2024-25 | forwards (29,976) | -0.273 -> +0.039 | -0.214 -> +0.048 | -0.083 -> +0.027 |
| | defence (15,200) | -0.240 -> +0.018 | -0.137 -> +0.036 | -0.155 -> +0.053 |
| | OT games (9,071) | -0.670 -> -0.377 | -0.170 -> +0.070 | -0.087 -> +0.063 |
| | regulation (36,105) | -0.160 -> +0.135 | -0.193 -> +0.038 | -0.112 -> +0.029 |
| 2025-26 | forwards (31,370) | -0.374 -> -0.005 | -0.269 -> -0.020 | -0.137 -> -0.011 |
| | defence (15,861) | -0.376 -> -0.012 | -0.160 -> -0.004 | -0.264 -> -0.024 |
| | OT games (11,736) | -0.789 -> -0.418 | -0.240 -> -0.031 | -0.175 -> -0.020 |
| | regulation (35,495) | -0.238 -> +0.128 | -0.230 -> -0.010 | -0.181 -> -0.014 |

SOG by group, CRPS champion -> WORKLOAD_V1 (bias): forwards 0.7649 -> 0.7586 (-0.089 -> +0.065), defence 0.6294 -> 0.6235
(2023-24); 0.7303 -> 0.7249 and 0.6228 -> 0.6179 (2024-25); regulation games 0.7132 -> 0.7083 / 0.6864 -> 0.6824, OT games
0.7423 -> 0.7310 / 0.7239 -> 0.7138. The challenger beats the champion in every position and OT split in every season. It
still under-predicts total minutes in OT games by 0.37-0.42 min (the OT length is a point estimate) and over-predicts in
regulation games by 0.13-0.15 min.

## Leakage audit

Prediction target: shots on goal (official boxscore) of a skater in a regular-season game on date D, for held-out season S.

| input to the WORKLOAD_V1 prediction | source and dating | pregame? |
|---|---|---|
| Which skaters play (the set of rows scored) and their F/D label | **actual dressed skaters from the boxscore** | **NO. Retrospective / conditional.** Production reads warmups/lines; Kalshi settles a non-playing skater at the fair price. The result is P(shots \| player dresses). A pregame product would also need a lineup forecast. |
| Starting goalies | not used by the skater model | n/a (goalie saves were not re-run; the original goalie variant used the actual starter and was REJECTED) |
| Tonight's lines, PP1/PP2 units | not used (no historical source exists; DailyFaceoff is archived only from 2026-09-30) | n/a. PP unit membership is learned only from recent shift shares, so a confirmed PP1/PP2 assignment is untested |
| Player deployment shares by strength state (and OT) | the player's own shift-chart rows from games dated strictly before D (`ew_prior_sums` excludes the row itself; half-life 4 games) | yes |
| Team PP / SH minutes drawn/taken (own and opponent), EA / EN seconds, league level | team rows of earlier games and the last 1,200 team-games strictly before D; OT-timeline repair uses only those earlier games' shift presence | yes |
| Overtime: P(OT), E[OT length], position OT multiplier, venue ratio, position share priors | constants fit on seasons < S only | yes |
| Shot rates by state | the player's earlier shots/minutes (half-life 80 games), league rate by position x state over the last 10,000 skater-games before D | yes |
| Opponent shots-against factor | the opponent's earlier games (half-life 25 team-games) and league level before D | yes |
| Home/away | schedule | yes |
| NegBin dispersion | residuals of season S-1 in full | yes (S-1 is complete before S) |
| Production champion: player profiles, league priors, strength table, TOI noise | rows strictly before D; parameters from seasons < S; actual dressed lineup as above | yes except lineup |
| Champion PP-share stand-in (`wf`) | point-in-time team penalty-minute and PP/PK ratings (`game_features`), reproduced exactly for 2024-25 | yes, with one nuance below |
| Kalshi / sportsbook / any market quantity | none; a test enforces that the research modules import none | n/a |

Checked empirically, not just by reading: (1) rebuilding every table from rows of seasons <= S only and recomputing the
WORKLOAD_V1 means gives bit-identical predictions to the full-data run for 2023-24 and 2024-25 (max abs difference 0.0 over
47,221 / 47,225 rows; constants identical); (2) rebuilding the production champion from a `Data` that holds no later season
gives bit-identical `ch_sog` and `ch_toi` for both seasons. (For 2025-26 this check is trivially identical: no later season is loaded.)

Caveats and non-pregame details:

* **The dressed lineup is retrospective** (above). It conditions on the player playing, as the original did.
* The league-rate window in `workload_v1.league_rates` sorts by date with an unstable sort, so which rows of the boundary DATE
  fall inside the 10,000-row window is arbitrary (rate differences of up to ~0.025 shots/60 at EV, ~0.06 on the PP, more in rare states).
  This is a reproducibility wobble among rows that are all dated before D, not leakage; with a deterministic tie order the
  truncation test above is exact. The evaluation itself is deterministic for fixed input and was left as the original.
* The champion's stand-in normalises PP shares by the mean over all rows of the walk-forward frame it is given (seasons <= S
  here, the whole 2024+2025 CSV in the original), a global constant containing later games of the same season. It affects
  only the champion, by about 0.0003 CRPS (derived vs coded, 2024-25).
* `baseline_sog` uses a full-table position mean (BASELINE arm only; not in any acceptance check). `skater_predictions` fills
  the first days of 2021, where no league level exists, with the global mean (no held-out row is affected).
* The xG model used inside the champion's feature book is fit on 2021-22 only, so it is out-of-sample for 2023 and later.
* Frozen parameters were selected on 2024-25. 2023-24 postdates no selection step, but the model's structure was designed after
  looking at the 2024-25 champion audit, as the preregistration discloses. 2023-24 is the cleanest available test, not a perfect one.

## What this does and does not justify

* It does justify saying the WORKLOAD_V1 skater projection is a small, repeatable accuracy improvement over the production
  expected SOG (about 1% CRPS), driven mostly by league-relative shrunk shot rates and by correct PP/SH/OT minutes, in three
  consecutive historical seasons, and that the production template's PP/SH/total TOI under-prediction is real and fixable.
* It does **not** show the frozen acceptance rule passes out of sample: it failed on its only clean test by 0.003 shots. The
  status stays "eligible for a prospective shadow test only"; if the bias check were revisited that must be a new
  preregistration (not an edit of this one), and a persistent +0.03 to +0.05 over-prediction would be the first thing to look at.
* It does **not** justify any betting, sizing or routing change. There is no Kalshi SOG market; the number is a packet-level
  projection. There is no market to test a 1% CRPS gain against, and no evidence here that it would be tradeable.
* It does **not** speak to goalie saves (not re-run), to PP1/PP2 line effects, to who dresses, or to any prospective performance.
* Three seasons are not independent draws of a stable process (same method family, overlapping training data, one season used
  for selection). Do not pool them into a tighter interval.

## Reproduce

```
export PYTHONPATH=$PWD/src
python -m nhl_edge.research.workload_replication --seasons 2023,2024,2025 --leakage-check --out docs/research/workload_v1
```

About ten minutes on 4 cores (champion frames are cached under `out/workload_v1_replication_cache/{derived,coded}`).
