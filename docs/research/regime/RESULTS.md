# Why does the V1 retune help 2020–2023 and not 2025? A leakage-safe regime map

RESEARCH_ONLY. Descriptive diagnostics, not a test: **16 seasons (2010–2025), about a dozen candidate explanations, and the explanations are correlated with each other and with the calendar.** Nothing here changes a model or a published number, and nothing is promoted. Code: `src/nhl_edge/research/regime_analysis.py` (tested); data: `regime_analysis.json`; inputs are the committed per-game tables of `docs/research/v1-retune/data/` and `data/history` (final results only). Rank correlations are Spearman across the 16 seasons.

## The question
The retuned-and-recalibrated V1 (`V1_R_C1`) beats production V1 on win-probability Brier by −0.0017 pooled over 2017–2025, but the gain is concentrated in 2020–2023 (−0.0036, −0.0039, −0.0029, −0.0019), is about −0.0015 in 2024, and is **+0.0001 in 2025** (and ≈ 0 on the untouched 2010–2016 seasons).

## Finding 1 — the production constants were nearly optimal in 2025 and badly off in 2020–2023
For every season I computed a post hoc *oracle surface*: the Brier a plain V1 with any (half-life, prior-games) pair of the registered 5 × 7 grid would have scored **on that season's own outcomes** (never used to select anything; it overstates what could have been achieved in advance). The headroom is production (20, 20) minus the best cell:

| season | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| oracle headroom (Brier) | .0006 | .0011 | .0016 | .0016 | .0015 | .0007 | .0014 | .0012 | .0021 | .0015 | **.0039** | **.0048** | **.0039** | **.0026** | .0022 | **.0004** |
| gain of `V1_R_C1` | +.0006 | −.0002 | −.0006 | .0000 | −.0009 | −.0003 | −.0013 | −.0003 | −.0008 | −.0009 | **−.0036** | **−.0039** | **−.0029** | **−.0019** | −.0015 | **+.0001** |

Headroom and realised gain move together (rank correlation **−0.85**). In 2025 even the oracle can recover only 0.0004: production V1 was already at its season optimum, so a retune has nothing to find. In 2020–2023 the best cells shift to a long memory and a tiny prior (the best prior is the grid's lower edge, 2.5 games, in 13 of 16 seasons — the edge is binding, as the earlier retune study already reported).

## Finding 2 — what differs in 2020–2023: unusually large real differences between teams
| quantity (per season) | 2010–2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|
| true team-strength spread (SD of team goal difference per game, sampling noise removed) | 0.27–0.46 | 0.57 | **0.66** | **0.67** | 0.58 | 0.47 | 0.41 |
| reliability of season goal difference | 0.51–0.76 | 0.74 | **0.84** | **0.84** | 0.80 | 0.72 | 0.68 |
| production V1's win-margin calibration slope (1 = calibrated; > 1 = under-confident) | 1.08–1.51 | **1.59** | **1.68** | **1.63** | 1.48 | 1.42 | 1.33 |

When teams really are further apart, a 20-game prior that pulls ratings toward the league mean is too strong; the data prefer less shrinkage (and V1's margins come out too compressed, slope 1.5–1.7). Rank correlations with the retune gain (negative = helps more): true spread **−0.79**, reliability **−0.71**, V1 margin slope **−0.62**, big-margin rate −0.61, previous-season persistence −0.54; with the oracle headroom: true spread +0.76, persistence +0.65, margin slope +0.64, reliability +0.64. By 2025 the spread (0.41) and slope (1.33) are back inside the pre-2020 range and the headroom is gone.

## Finding 3 — it was not knowable from last season
The same variables measured in the **previous** season (what a pregame system could have used) correlate much more weakly with the gain (true spread −0.39, reliability −0.35 vs −0.79 and −0.71 in-season). The regime shows up in the season being predicted, not in the one before it. A fixed retune therefore cannot be justified by "the league is now in the high-spread regime"; and a rule that switches regime from last year's data would not have caught 2020–2022.

## Other candidate explanations
* **Schedule.** Season label 2020 (the 2020-21 season) was shortened and division-only (61.6% of games repeated a pairing within 14 days vs 12–27% in other seasons). The repeat-pairing share does not explain the gain (rank correlation +0.25 with it; 2020 is a gain season, but 2021–2023, with normal schedules, gain nearly as much). The back-to-back share has a +0.67 rank correlation with the gain, which I cannot separate from the era with 16 points; I do not read it as a mechanism.
* **Scoring environment / calibration drift.** Goals per game rose from ≈5.5 (2010–2016) to ≈6.0–6.4 (2018–2025). V1 under-predicts total goals in every season (bias −0.08 to −0.39; worst 2021, −0.39); the total-goal slope is far from 1 in several seasons (0.08 in 2020, 0.25 in 2017). Recalibration addresses these, which is why `V1_C1` (recalibration only) captures part of the 2018–2023 gain; they do not track the *size* of the retune gain across seasons (rank correlation with goals per game −0.46).
* **Data definitions.** I did not find a definitional break in the committed results (final scores, overtime flags) that lines up with the pattern, and I did not re-audit the upstream feeds season by season; this is "not detected", not "ruled out".

## What this means
1. The retune gain is a **property of the 2020–2023 league** (high, reliable differences between teams), not a property of the retuned parameters, and it is **gone in 2025 because the league moved back**. Production V1's constants do not need changing for the current regime (headroom 0.0004).
2. The earlier statement that "the production constants are near-optimal before 2018 and in the latest season" is confirmed by the oracle surface rather than assumed.
3. The only hypothesis worth pre-registering from this map: **an adaptive prior** — the number of prior games as a function of the point-in-time estimate of team-strength spread this season (and half-life as a function of its persistence) — tested walk-forward against fixed constants on seasons not used to build it. The untouched tier (2010–2016) cannot validate it (spread is normal there); the only genuine out-of-regime check would be a future high-spread season, so a prospective shadow is the realistic test. No production change is proposed.

## Caveats
Sixteen points; many candidate variables; correlated explanations; oracle surfaces use outcomes of the season they describe (diagnostic only, labelled post hoc); the 2024 and 2025 seasons are exposed to earlier decisions. Treat the correlations as a map of where to look, not as evidence of mechanism.
