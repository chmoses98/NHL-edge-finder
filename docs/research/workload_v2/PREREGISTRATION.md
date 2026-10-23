# WORKLOAD_V2 — preregistration (skater shots on goal)

> RESEARCH_ONLY · written 2026-10-23 · **committed before any WORKLOAD_V2 prediction exists**; the commit time is the registration time. Nothing here is wired into production or changes a price, stake, cap, authority or SIFT contract; the machine-readable copy the evaluator reads is `preregistration.json`. "ACCEPTED" would only make the model eligible for a *prospective shadow test*.

## What is being tested

`WORKLOAD_V2` = `WORKLOAD_V1` (all frozen parameters of `workload_v1/preregistration.json` unchanged) with **one** change: the shrinkage of every player's shot-rate index is anchored at the shooting level of his *role* instead of at the league position average (`workload_v2.py`; derivation in `DIAGNOSIS.md`). The role is the point-in-time predicted total TOI quintile within position; the ten multipliers (position × quintile) and the eight edges are estimated on the seasons strictly before the scored season and nothing else is fitted or tuned. The negative-binomial dispersion is fit on the previous season's own residuals, with a role prior fitted on the seasons before *that*, exactly as the V1 protocol fits its dispersion.

**Hypothesis.** The depth-player/newcomer over-prediction and the star under-prediction disappear, the overall bias shrinks inside ±0.05 in every held-out season, and accuracy (CRPS, RMSE, ladder Brier) does not get worse than WORKLOAD_V1's and still beats the production champion.

## Evaluation

* Seasons: 2023-24, 2024-25, 2025-26 (the only seasons feasible under the frozen protocol; constants on all earlier seasons, dispersion on the previous one). Same arms, metrics, 2,000-resample game-clustered bootstrap and shift-chart rows as `workload_experiment`; the production champion is rebuilt with the derived walk-forward stand-in of `workload_replication` (which reproduces the committed 2024-25 rows exactly).
* Acceptance (`preregistration.json`): the **seven frozen WORKLOAD_V1 checks, unchanged** (including |bias| ≤ 0.05 — the threshold is not weakened), **plus one added check**: no predicted-TOI quintile may be biased by more than 0.06 shots per skater-game. ACCEPTED only if every check passes in **every** one of the three seasons. Otherwise REJECTED, and the numbers are reported either way.
* Secondary, descriptive: WORKLOAD_V2 − WORKLOAD_V1 paired differences, bias by predicted-TOI quintile and position for champion / V1 / V2.

## Honest status of the evidence

* **Not independent.** 2023-24, 2024-25 and 2025-26 were all scored by WORKLOAD_V1 evaluations, and the diagnosis that motivates this change was read off them. The single structural choice (a role-conditional anchor, five TOI quintiles per position, one multiplier per cell) was fixed *before* any V2 number was computed and adds no tuned hyper-parameter, but a historical ACCEPTED is development evidence only.
* **Confirmation must be prospective.** The only untouched data is the live record. A shadow arm in the projection pipeline (a separate, approved change) would be scored on its first ≥ 300 games with the same eight checks against the production champion; until then the registry verdict for skater shots stays **RETAIN**.
* No Kalshi shots-on-goal market exists; this is a projection-quality result, not a betting result.
* Power-play and total ice time are **not** retuned: 62–66% of PP-minutes error is the game-level penalty count (`DIAGNOSIS.md`), total TOI is unbiased, and no line/PP-unit source exists to test a finer allocation.
