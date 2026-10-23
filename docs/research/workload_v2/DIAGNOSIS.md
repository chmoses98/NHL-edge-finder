# Where the WORKLOAD_V1 skater-shots bias comes from

> RESEARCH_ONLY · written 2026-10-23 · V1 predictions only (no WORKLOAD_V2 number exists yet). Data: `diagnosis.json` (`python -m nhl_edge.research.workload_v2 diagnose`-style tables built from the frozen `WORKLOAD_V1` walk-forward of PR #62, seasons 2023-24, 2024-25, 2025-26). Not prospective; nothing is promoted.

WORKLOAD_V1 over-predicts shots on goal by +0.053 / +0.047 / +0.030 per skater-game in 2023-24 / 2024-25 / 2025-26 (PR #62), 2–3% of the mean, which is why the frozen rule (|bias| ≤ 0.05) failed on 2023-24 by 0.003. The question was *which* part of the model produces it.

## Findings (all three seasons agree)

| cut | 2023-24 | 2024-25 | 2025-26 |
|---|---:|---:|---:|
| overall bias | +0.0525 | +0.0468 | +0.0295 |
| forwards / defencemen | +0.065 / +0.028 | +0.056 / +0.029 | +0.033 / +0.022 |
| **lowest predicted-TOI quintile** | **+0.129** | **+0.092** | **+0.087** |
| quintile 2 | +0.071 | +0.056 | +0.069 |
| quintile 3 | +0.037 | +0.032 | 0.000 |
| quintile 4 | +0.024 | +0.044 | +0.003 |
| **highest predicted-TOI quintile** | **+0.002** | **+0.009** | **−0.011** |
| players with 0–5 prior games | +0.305 | +0.301 | +0.221 |
| regulation games / overtime games | +0.072 / −0.022 | +0.062 / −0.013 | +0.042 / −0.008 |
| part of the bias due to minutes (rest is shot rates) | +0.007 | +0.005 | −0.004 |

1. **The bias is a rates problem, not a minutes problem.** Giving the model the minutes actually played removes at most 0.007 of the 0.05.
2. **It is concentrated in depth players and newcomers**: +0.09…+0.13 shots (8–12%) for the lowest-TOI fifth of the lineup, ≈ 0 for the top fifth; +0.22…+0.31 for players with at most five prior games. The pattern is monotone and replicates in three seasons.
3. **Mechanism.** Each player's shot-rate index is `(his shots + k) / (league-rate expected shots + k)`: `k` minutes at the *league position average* anchor every player, so a player with little evidence is pulled toward 1.0. Depth skaters and call-ups shoot below the position average (stars above it); shrinking toward the average inflates the many depth players and deflates the few stars, and because depth players are over-represented in a lineup the net is a positive bias. The same symmetric signature is visible in the calibration by predicted shots (2023-24): the lowest five deciles run +0.03…+0.11 high and the top decile −0.04 low.
4. **Overtime is not the cause**: overtime games are *under*-predicted by 0.01–0.02; the regulation games carry the bias.

## Power-play and total ice time (the other half of the question)

* Team-level power-play minutes are close to unpredictable before the game: predicted vs actual team PP minutes correlate at 0.15 (2023-24), 0.15 (2024-25), RMSE 2.6 minutes — the number of penalties is a random count.
* Consequently **62–66% of the squared error of a player's PP minutes is the game-level penalty count**: with the true team PP minutes known, the player-level MSE falls from 1.33 to 0.50 (2023-24) and from 1.23 to 0.42 (2024-25). What remains (allocation among teammates) is the part a better model could still attack, but it is a minority of an already small error, and no historical line/PP-unit source exists to test it.
* Total TOI is unbiased in WORKLOAD_V1 (bias −0.008 in 2025-26; PR #62); PP and SH minutes have no remaining bias of consequence (|bias| ≤ 0.02).
* Decision: no separate ice-time/PP-time challenger is justified by this evidence. The actionable defect is the shot-rate prior.

## What this implies

A single, structural change targets the cause: anchor the shrinkage at the shooting level of the player's **role** (position × predicted-TOI quintile, estimated on earlier seasons only) instead of at 1.0. That is the `WORKLOAD_V2` preregistered in `PREREGISTRATION.md` in this directory. The existing acceptance threshold is not touched.
