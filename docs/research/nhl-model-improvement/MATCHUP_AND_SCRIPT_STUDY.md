# Opponent-adjusted matchup features and game-script calibration

> RESEARCH ONLY. Matchup-feature tests: prior audit (`MATCHUP_FACTOR_STUDY.md`, design committed before results) plus this program's V1-residual scan on 2,624 walk-forward games (`M-SCAN-1`). Script calibration: `M-SCRIPT-1` on 99 LIVE games. Exact tables in `RESULTS_TABLES.md`.

## 1. Does hockey knowledge add information beyond the market?

**Prior audit (re-verified, reproduces identically):** opponent-adjusted xG, rest, back-to-backs, travel, finishing and special teams all fail out of sample: every hold-out interval includes zero; the single in-sample signal (away back-to-back, |z| ≈ 2.4) *worsened* hold-out log loss. The reviewer rebuilt eight features on date-truncated data (no look-ahead; `pp_edge` differs by 0.3% of an SD because league PP/PK means use all games) and noted the hold-out interval half-width (≈ 0.003 log loss) cannot see plausible small edges — "no block helps" is slightly strong because the W1 and T1 point estimates are negative.

**Raw vs adjusted.** On V1 residuals (regulation goals − V1 expected goals, 2,624 games, HC1 SEs, BH over 17 tests) none of the *information the model already holds* explains what it misses, with three exceptions that are statistical but not material:

| feature (per SD) | effect on residual | BH q |
|---|---|---|
| sum of team finishing factors → total goals | −0.167 goals | 0.003 |
| V1 `lam_sum` → total goals | −0.173 goals | 0.003 |
| V1 `lam_diff` → margin | +0.139 goals | 0.016 |
| early season (≤ 15 games used), back-to-back (either/both/home/away), mean rest, rest difference, season, offensive/defensive xG level, finishing difference | all \|coef\| ≤ 0.08, none significant (q ≥ 0.32) | — |

The three exceptions are why correcting V1's rates is *tempting* — and why it does not help: a challenger that rescales them (C1) leaves every score unchanged (`CHALLENGER_MODEL_COMPARISON.md`). **Hockey expertise did not translate into a forecast or a betting advantage here.** Matchup interactions that need player- or line-level data (high-danger offence vs defence, line combinations, goalie vs shot quality) cannot be tested with the archive: it has no timestamped lineups and no per-line deployment.

Goalie-vs-shot-quality: LIVE goalie save totals are archived (e.g., CBJ 14/19 saves on Oct 20) but V1 does not model shots faced, so there is no forecast to evaluate against. Ex-post, finishing/goaltending luck is ≈ all of the unforecastable variance in total goals (`PREDICTION_ERROR_AUDIT.md`).

## 2. Game-script layer (NHL_SCRIPT_V1)

**Definition.** Seven scripts, mutually exclusive by a fixed precedence (SPECIAL_TEAMS, OPEN_GAME ≥ 8 goals, TIGHT_LOW_EVENT ≤ 4 goals and a one-goal final or OT, GOALIE_DRIVEN, HOME_CONTROL, AWAY_CONTROL, catch-all BACK_AND_FORTH). Probabilities are draw shares and sum to 1 exactly (max error 2.2e-16, verified). Thresholds were a-priori and never fit to a slate, price or result; base rates come from 5,248 finals.

**Calibration (99 LIVE games with a forecast at the cut and a postmortem; script forecasts began 2026-10-07):** multiclass Brier 0.8157 vs base-rate 0.8257 (paired Δ −0.0099, 95% CI −0.0207…+0.0001); top-script hit rate 28.3% (the base-rate mode would hit 25.3%).

| script | mean predicted | observed | observed 95% | inside CI |
|---|---|---|---|---|
| SPECIAL_TEAMS | 12.2% | 17.2% | 11.0–25.8% | yes |
| OPEN_GAME | 22.6% | 23.2% | 16.0–32.5% | yes |
| TIGHT_LOW_EVENT | 11.1% | 13.1% | 7.8–21.2% | yes |
| GOALIE_DRIVEN | 7.8% | 6.1% | 2.8–12.6% | yes |
| HOME_CONTROL | 11.6% | 8.1% | 4.2–15.1% | yes |
| AWAY_CONTROL | 8.3% | 7.1% | 3.5–13.9% | yes |
| BACK_AND_FORTH | 26.4% | 25.3% | 17.7–34.6% | yes |

**Reading.** The probabilities are internally coherent and consistent with what occurred, but with 99 games each interval is wide, and the improvement over climatology is marginal (CI touches zero). Two cautions: SPECIAL_TEAMS (12% predicted vs 17% observed) and HOME_CONTROL (12% vs 8%) are the largest gaps, within noise; the documented caveat that simulated shot counts mute score effects (GOALIE_DRIVEN expected to be under-forecast) cannot be judged at this n. The script *labels* correspond to identifiable mechanisms (PP goals, ≥ 8 goals, shot share), so they are meaningful as explanation. **They are not demonstrated to improve market selection**; "script resilience predicts realised betting performance" was untestable because no strategy is validated and the corrected engine selects nothing (`MARKET_FAMILIES_AND_EXPRESSION.md`). Recommendation: keep the layer as an explanatory, descriptive feature ("this game most resembles…"); do not present script-conditioned probabilities or survival as quantitative evidence of value; re-test on ≥ 300 games with the prospective ledger.
