# J2 — retuned + recalibrated V1 rates through the V2 simulator: results

RESEARCH_ONLY. Nothing here promotes a model, changes a published projection, a price, a stake, a cap, routing or the app contract. Pre-registered in `PREREGISTRATION.md` (commit fe9d1ac6, before any arm was run); the decision tier, the arms and the three rules below are exactly as registered. Raw tables: `j2_results.md` / `j2_results.json`; per-game probabilities of every arm: `data/j2_games.csv.gz` (18,777 games, 2010–2025).

## What was run

The chronologically retuned V1 rates (`V1_R`) and the retuned-and-slope-recalibrated rates (`V1_R_C1`, 300-game burn-in) were taken from the committed `v1-retune` game files and fed to the unchanged V2 simulator (`nhl-sim-2.0`, hazards re-fitted per season on the previous four seasons; seasons 2010–2011 have only 2–3 training seasons, so the earliest simulator fits are weaker than the later ones). Every arm yields one joint distribution per game from which winner, regulation/overtime, total goals, team totals, goal differential, the regulation 3-class result and the puck line (win by 2+) are all derived from the *same* simulated games. Arms: `V1` (incumbent), `SIM2` (V2 simulator on the incumbent's rates), `R_SIM1`/`R_SIM2` (retuned rates through simulator 1.1 / 2.0), `RC_SIM1`/`RC_SIM2` (retuned + recalibrated). Tiers: **CLEAN2** 2010–2016 (decision; untouched by any earlier decision), SEEN 2017–2022, EXPOSED 2023–2025.

## Registered rules (CLEAN2, n = 7,725)

| rule | outcome | evidence |
|---|---|---|
| **J2-A additive** (RC_SIM2 keeps the win gain of RC_SIM1 and the overtime gain of SIM2, slack 0.0005) | **TRUE** | Δ Brier(win) vs V1: RC_SIM2 −0.0004, RC_SIM1 −0.0004 · Δ Brier(OT): RC_SIM2 −0.0025, SIM2 −0.0025 |
| **J2-B scorecards** (unchanged gates G1–G10, J1) | **overtime: SHADOW_MORE · margin, win, total: RETAIN_INCUMBENT** | below |
| **J2-C complementary** (no worse than the better single fix by the practical threshold; joint scores not worse than both) | **TRUE (as a no-harm test)** | gap to the best single fix: win +0.0000, OT −0.0001, total RPS −0.0000, margin RPS +0.0005 — all far inside the practical thresholds |

The rules are *no-conflict* tests: they say the two fixes do not undo each other. They do not say the combination is worth publishing, and on CLEAN2 it is not for three of the four targets.

### J2-B in detail (RC_SIM2 vs V1, CLEAN2; 95% games | slates)

| target (primary metric) | Δ | interval | practical threshold | verdict |
|---|---:|---|---:|---|
| overtime (Brier OT) | −0.0025 | [−0.0033, −0.0017] \| [−0.0033, −0.0017] | 0.0010 | **SHADOW_MORE** (G1–G6b and J1 pass; G7–G10 need live data) |
| win probability (Brier) | −0.0004 | [−0.0009, +0.0002] \| [−0.0009, +0.0001] | 0.0010 | RETAIN_INCUMBENT (G1, G2 fail) |
| goal margin (RPS) | −0.0007 | [−0.0026, +0.0012] \| [−0.0025, +0.0011] | 0.0050 | RETAIN_INCUMBENT (G1, G2, G6 fail: better in 4/7 seasons) |
| total goals (RPS) | −0.0015 | [−0.0033, +0.0003] \| [−0.0033, +0.0003] | 0.0050 | RETAIN_INCUMBENT (G1, G2 fail; G6b: significantly worse in exposed 2018 and 2021) |

**The overtime pass is the V2 simulator, not the retuning.** `SIM2` alone is −0.0025 on the same metric; adding the retuned rates changes nothing (RC_SIM2 − SIM2: −0.0001 [−0.0002, +0.0001]). That finding was already established (V2 hazards fix the overtime under-prediction: V1 predicts 18.7% of CLEAN2 games to need overtime against 23.7% observed; the V2 arms predict 22.6%, still about one point low). Retuning/recalibration of the *rates* does not touch overtime (RC_SIM1 − V1: +0.0001).

## Joint distribution

Joint scores (all derived from one simulated distribution; negative = better than V1):

| CLEAN2 | Δ vs V1 | 95% (games) |
|---|---:|---|
| regulation 3-class Brier | −0.0044 | [−0.0058, −0.0030] |
| joint (margin × OT) Brier | −0.0011 | [−0.0019, −0.0003] |
| joint (total × OT) Brier | −0.0010 | [−0.0013, −0.0006] |
| joint margin log-score | −0.0172 | [−0.0234, −0.0113] |
| joint total log-score | −0.0211 | [−0.0274, −0.0149] |
| puck line Brier | −0.0002 | [−0.0005, +0.0002] |
| team-total Brier | −0.0003 | [−0.0005, −0.0001] |

Most of the joint gain is the overtime component again (SIM2 alone: reg3 −0.0036, joint total −0.0007). What the retuned rates add on top of the simulator is small: RC_SIM2 − SIM2 on CLEAN2 is win −0.0004 [−0.0009, +0.0001], margin RPS −0.0017 [−0.0033, +0.0001] (slate interval [−0.0034, −0.0000]), joint margin Brier −0.0005 [−0.0010, −0.0001], joint total −0.0003 [−0.0006, +0.0000]. Directionally consistent, statistically borderline, and far below the registered practical thresholds.

## By tier — the retuning effect depends on the era

RC_SIM2 vs V1 (negative = better):

| tier | Δ win | Δ OT | Δ total RPS | Δ margin RPS | Δ joint margin |
|---|---:|---:|---:|---:|---:|
| CLEAN2 2010–16 (7,725) | −0.0004 (ns) | −0.0025 | −0.0015 (ns) | −0.0007 (ns) | −0.0011 |
| SEEN 2017–22 (7,116) | **−0.0022** | −0.0024 | +0.0022 (ns) | **−0.0071** | −0.0026 |
| EXPOSED 2023–25 (3,936) | −0.0009 (ns) | −0.0022 | −0.0017 (ns) | −0.0031 (ns) | −0.0032 |
| pooled 2010–25 (18,777) | −0.0012 | −0.0024 | −0.0002 (ns) | −0.0036 | −0.0021 |

In 2017–2022 the retuned rates give clear win and margin gains; the per-season table (`j2_results.md`) shows these come from 2020–2022 (Δ win −0.0043 / −0.0042 / −0.0032, Δ margin RPS −0.0140 / −0.0135 / −0.0147). In 2010–2016 the same rates are about neutral, and in 2025 the win Brier is +0.0004 (the latest season shows no gain, consistent with the V1-retune result). See `docs/research/regime/RESULTS.md` for the regime analysis of why. Total-goals RPS is the one target where the retuned+recalibrated arms are *worse* in 2018 and 2021 (+0.0052, +0.0101), which is what blocks the total-goals scorecard (G6b).

## Against the market (Kalshi midpoint at T−60 min, season 2025, no depth/fee/slippage)

| market (n) | V1 | SIM2 | RC_SIM1 | RC_SIM2 |
|---|---|---|---|---|
| home win (1,312) | +0.0017 ind. | +0.0016 ind. | +0.0018 ind. | +0.0021 ind. |
| total over 5.5 (1,196) | +0.0025 **market better** | +0.0026 **market better** | +0.0019 ind. | +0.0018 ind. |
| total over 6.5 (1,194) | +0.0035 **market better** | +0.0031 **market better** | +0.0029 **market better** | +0.0020 ind. |
| puck line away −1.5 (1,181) | +0.0012 ind. | +0.0017 ind. | +0.0012 ind. | +0.0016 ind. |
| puck line home −1.5 (1,181) | +0.0014 ind. | +0.0010 ind. | +0.0001 ind. | +0.0000 ind. |

(Brier minus market Brier; positive = model worse than the market.) **No forecaster beats the market on any contract.** On totals the market is better than V1, and RC_SIM2 narrows the gap to "indistinguishable" — but that is the difference between two intervals, not a tested difference between forecasters, and a midpoint comparison is not an execution edge. Team totals cannot be compared (the Kalshi history has no team-total markets) and overtime has 49 playoff markets only. Nothing here supports any wager; PASS-only stands.

## Conclusion

* The joint-distribution hypothesis ("retuned rates plus the V2 simulator is better than either alone") is supported only in the weak sense that the two fixes are additive and do not conflict (J2-A, J2-C). The combination is not practically better than the better single fix on the untouched tier.
* **Overtime** reaches SHADOW_MORE through the V2 simulator alone; no new evidence was needed to know that, and it is still not promoted (G7–G10 are open).
* **Win, margin and total** remain with the incumbent on CLEAN2. The retuned rates are worth carrying forward as a regime-dependent improvement (2020–2022 strong, 2010–2016 and 2025 neutral), not as a general upgrade.
* No promotion, no change to any published projection. Decisions on promotion stay with a human.

## Reproduce

`python -m nhl_edge.research.joint_retuned run --seasons … --out …` (four shards, ~40 min each) then `python -m nhl_edge.research.joint_retuned_eval --dirs out/j2/shard* --out docs/research/v2-joint-retuned --history data/history`. The shard folders (`cells.npz`, `pmfs.npz`) are regenerable and are not committed; `data/j2_games.csv.gz` holds every arm's per-game probabilities.
