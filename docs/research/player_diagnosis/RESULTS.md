# Skater projections: where the errors are (ice time, power play, shots, assists, points)

RESEARCH_ONLY. A diagnosis, not a model: nothing here changes a projection, a parameter, a price, a stake, a cap, routing or the contract, and no candidate is promoted. Code: `src/nhl_edge/research/player_diagnosis.py` (tested); data: `diagnosis.json`; reproduce with `python -m nhl_edge.research.player_diagnosis --cache <workload replication cache>/derived --out …`.

**What was measured.** The incumbent rows are the derived champion stand-in of the workload replication (the rows WORKLOAD_V1 and WORKLOAD_V1_LC were scored against), seasons 2022–2025, ~47,200 skater-games each, with realised minutes by game state and shots; assists and points come from the committed PLAYER_SIM_V1 skater rows for 2025-26 (47,231 skater-games). **Every season used here is already exposed** to earlier workload work, so a signal that helps below is a *hypothesis for a pre-registered prospective test*, never validation. Signals are tested **net of a level correction** (a constant multiplier fitted on earlier seasons), each coefficient fitted on earlier seasons only and scored on the later one (2023, 2024, 2025), with game-clustered bootstrap intervals. Where no point-in-time source exists the signal is not tested (listed at the end). Data caveat: 4.3% of 2024-25 skater-games have no shift charts, so their by-state minutes are recorded as zero; all by-state results exclude them.

## 1. How wrong are the incumbent's expectations?

Bias = expected − realised, per skater-game (percent of the realised mean). RMSE in minutes / shots.

| season | total TOI | EV TOI | **PP TOI** | SH TOI | **shots** |
|---|---|---|---|---|---|
| 2022 | −0.21 (−1.3%) | +0.22 (+1.6%) | **−0.29 (−19.0%)** | −0.23 (−19.1%) | −0.086 (−4.9%) |
| 2023 | −0.21 (−1.3%) | +0.20 (+1.4%) | **−0.25 (−17.0%)** | −0.22 (−18.4%) | −0.064 (−3.8%) |
| 2024 | −0.28 (−1.7%) | +0.01 (+0.1%) | **−0.19 (−14.1%)** | −0.11 (−9.9%) | −0.040 (−2.5%) |
| 2025 | −0.38 (−2.3%) | −0.01 (−0.1%) | **−0.23 (−16.5%)** | −0.18 (−15.6%) | −0.085 (−5.5%) |

* **Ice time is nearly unbiased overall; power-play and short-handed time are not.** The incumbent's team power-play minutes run −0.6 to −0.9 per game low (13–16%) in every season (a stale fixed team-minute template); shorthanded time inherits the same level error. Even-strength time is unbiased.
* **Shots are 2.5–5.5% low**, and the shortfall is concentrated in the middle and upper predicted-TOI/PP quintiles and in forwards (2025: forwards −6.5%, defencemen −3.0%; predicted-TOI quintiles 3–4 −7.2…−7.8%, quintile 0 +0.8%). Overtime games are 8% low (more minutes than the template expects).
* WORKLOAD_V1 removes the level errors in minutes and a large part of the shot shortfall (it then over-predicts depth-player shots; see `workload_v2/DIAGNOSIS.md`). The remaining question is what *signal* is still missing, below.

## 2. Is the power-play error predictable?

* **64–67% of a player's squared PP-minute error is the game-level penalty count** (rescaling every skater by realised/expected team PP minutes cuts the MSE from ≈1.3–1.6 to ≈0.45–0.53 in all four seasons). The rest is allocation among teammates.
* **Team PP minutes are barely predictable.** Incumbent: correlation with realised 0.02–0.09, RMSE 2.66–2.79 minutes against a realised standard deviation of ≈2.65. A point-in-time penalty-rate model (own drawn minutes, opponent's taken minutes, exponentially weighted, fitted on earlier seasons) reaches correlation 0.11–0.18 and RMSE 2.55–2.68, only 0.0–0.10 minutes better than simply using the previous seasons' mean (2.64–2.67). **The controllable part is the level (−0.6…−0.9 minutes); the penalty count itself is close to noise.** Do not build a PP-minutes challenger on this evidence.
* **Recent PP deployment** (last five games' PP minutes vs the incumbent's expectation) improves a player's PP-minute forecast net of level in 2023 (−0.0125 MSE [−0.0165, −0.0084]) and 2024 (−0.0123 [−0.0194, −0.0055]) but not 2025 (−0.0023 [−0.0091, +0.0051]) — a roughly 1% effect on a 1.3–1.5 MSE; not stable enough to matter.

## 3. Shots: which signals add information net of level?

Poisson deviance per skater-game (≈1.25). Negative = the signal helps; "level" is the gain of the constant correction alone, "signal" the extra gain of the signal on top. 95% game-clustered interval in brackets.

| signal (point-in-time) | 2023 | 2024 | 2025 | coefficient (≈) | reading |
|---|---|---|---|---|---|
| level only | −0.0023 | −0.0005 | −0.0044 | — | the biggest single fix in 2025 |
| **opponent shot suppression** (opponent's shots allowed, EW 30 games, vs league) | **−0.0040** [−0.0057, −0.0024] | **−0.0035** [−0.0050, −0.0019] | −0.0011 [−0.0025, +0.0002] | 0.9–1.05 | real and stable in sign; full proportional pass-through; the incumbent's shot mean has no opponent term. One standard deviation of the factor is ±5.7% of expected shots. |
| own team's shot environment | +0.0001 | +0.0001 | −0.0002 | ≈ −0.2 | nothing (already in the player's own rate) |
| **recent usage** (last three games' TOI vs expectation) | **−0.0025** [−0.0033, −0.0016] | **−0.0030** [−0.0039, −0.0021] | **−0.0019** [−0.0029, −0.0009] | 0.42–0.48 | consistent in all three seasons |
| **lagged line-mates** (even-strength co-ice minutes of the last five games × the line-mates' earlier shot rate) | −0.0006 [−0.0009, −0.0003] | −0.0005 [−0.0009, −0.0001] | −0.0006 [−0.0011, −0.0002] | 0.08–0.11 | small, consistent |
| opposing goalie's lagged save % (previous starter as proxy) | −0.0002 | −0.0001 | +0.0002 | — | nothing detectable |

The effects are small in absolute terms (0.1–0.3% of the loss) except usage and the opponent term in 2023–24; none comes close to the level error in size. They are candidates, not findings of a better model: they were estimated on seasons already seen by earlier work, and shots have no market to benchmark against.

## 4. Ice time: recent usage

Recent usage is the one signal with a large effect: the player's last three dressed games' TOI against the incumbent's expectation reduces the total-TOI MSE by **0.25 on 6.1–6.5 (≈4%) in each of 2023, 2024 and 2025** (intervals [−0.28, −0.21] in all three; coefficient 0.39–0.40). The incumbent's 6-game half-life with a position-mean pseudo-game under-reacts to a role change. This is the clearest, most stable miss in the study, and it is a minutes effect, not a rates effect (recent usage also helps shots, §3, by about 0.002–0.003).

## 5. Assists and points (PLAYER_SIM_V1, 2025-26, n = 47,231)

* **Unbiased and at the count-noise floor.** Mean bias +0.9% (assists), +0.8% (points); MSE ÷ mean = 1.00 for goals, assists and points — the squared error equals what a perfectly known Poisson mean would leave. Correlation of expected with realised: goals 0.27, assists 0.28, points 0.36.
* **Compression.** Calibration slope of realised on expected: goals 1.01, **assists 1.09, points 1.12**. Points by predicted quintile (expected / realised): 0.193/0.187, **0.306/0.274**, **0.416/0.379**, 0.571/0.567, **0.835/0.895** — the middle is over-predicted by 10–12%, the top quintile under-predicted by 7%.
* **Position.** Defencemen: goals −7.6% (under), assists **+8.1%** (over), points +4.6%; forwards the opposite sign (goals +2.0%, assists −2.4%, points −0.5%). The split of credit between goals and assists by position is off even though totals are fine.
* **Ice time is not the problem here.** Replacing each skater's expectation by one scaled with his realised TOI changes the MSE by less than 0.1% (and slightly for the worse) for goals, assists and points. **The game's scoring environment is**: scaling by realised team goals would remove 7% / 10% / 17% of the goals / assists / points MSE — but expected team goals correlate only 0.13 with realised, i.e. the reducible part is the unpredictable part.
* A power-law slope correction fitted on the first half of the season and scored on the second half improves the points deviance by 0.0015 [0.0004, 0.0027] and assists by 0.0002 [−0.0000, +0.0005] (not significant; the interval is on the beneficial side of zero up to rounding) — a small, real calibration gain, nowhere near a materially better model.

## 6. What could not be tested (and why)

| signal | status |
|---|---|
| **line assignment as announced** (the actual lines/PP units on the day) | No point-in-time source for 2021–25 (DailyFaceoff archived only from 2026-09-30). Only the lagged-co-ice proxy above could be tested. |
| **the starting goalie as announced** | Same: not archived before 2026-09-30. Only the previous starter was available as a proxy (it equals the true starter's quality with a correlation of ≈0.5). A real test needs the live archive. |
| goalie context for assists/points | Needs the starter and two seasons of PLAYER_SIM_V1 skater rows; only 2025-26 rows are committed. |
| special-teams **unit** assignment (PP1 vs PP2) | Only shares of PP time, which the incumbent already uses. |

## 7. Decisions and what has to happen before anything changes

1. **No player-projection challenger is promoted or registered by this study.** It is a diagnosis on already-exposed seasons.
2. **Highest-value candidate for a pre-registered prospective test:** a shots/TOI model with (a) the level corrected, (b) an opponent-suppression term, (c) recent-usage terms for minutes. These are the only effects that are large relative to their intervals and stable in sign across seasons. Because every historical player season is exposed, the test has to be prospective, like WORKLOAD_V1_LC's: the frozen candidate is registered before any record, scored on records written after activation.
3. **Add minutes to the prospective records.** The LC shadow records store shots only; incumbent TOI/PP-TOI forecasts are not in the archive in a form that can be scored. A separate registration should add expected TOI and PP TOI to the write-once records so the usage effect can be judged on new data.
4. **PP minutes:** correct the level only (the template constant); the penalty count is noise. Do not build a PP-count model.
5. **Assists/points:** at the noise floor; only slope recalibration and the defence/forward assist-credit split are open, both small.
