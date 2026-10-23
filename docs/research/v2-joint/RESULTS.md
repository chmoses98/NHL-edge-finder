# V2 simulator — joint game-distribution validation: results (RESEARCH_ONLY)

Preregistration: `PREREGISTRATION.md` (committed before any V2 simulation existed for 2010–2022). Raw output: `joint_results.json`, full tables: `joint_results.md`.
Run: four shards of `python -m nhl_edge.research.joint_eval run` (seasons 2010–2025, 4,000 draws, rolling 4-season hazard window), then `evaluate`.
Nothing here changes a model, price, stake, cap or authority. The scorecard recommends; a human decides. **No promotion is requested.**

## Verdicts under the unchanged promotion gates

Games: 18,777 scored (14,841 in the unexposed seasons 2010–2022, 13 seasons; 3,936 in the exposed 2023–2025). Unresolved franchise abbreviations dropped for every arm alike (2010 and 2011–2013 only, `HISTORY_EXTENSION_2008_2014.md`).

| target | SIM2 (V2 simulator on V1 rates) | SIM2_ST (V2 simulator + special-teams rates) |
|---|---|---|
| overtime / regulation tie (primary Brier(OT)) | **SHADOW_MORE**: every history gate G1–G8 and J1 passes; G9, G10 pending | **SHADOW_MORE** (same) |
| goal-margin distribution (primary RPS(margin)) | **RETAIN_INCUMBENT**: G1, G2, G6 fail | **RETAIN_INCUMBENT**: G1, G2, G6 fail |

* **Overtime.** ΔBrier(OT) −0.0023 [−0.0029, −0.0018] (games and slates), favourable in 13 of 13 unexposed seasons and in each of 2023, 2024, 2025; ECE 0.0089 vs 0.0494. Predicted P(OT or SO) 0.2205 vs observed 0.2290 (V1: 0.1800); P(SO | tie) 0.442 vs 0.4035 (V1: 0.340). The shootout cells go from z −11 and −13 (V1) to z −2.5 and −0.7. The same holds in the 4-on-4 seasons 2010–2014 (−0.0027) and the 3-on-3 seasons 2016–2022 (−0.0022).
* **Goal margin.** ΔRPS(margin) **+0.0010** [+0.0002, +0.0018] for SIM2 and **+0.0020** [+0.0009, +0.0031] for SIM2_ST: the V2 margin distribution is slightly *worse* than V1's, favourable in 0 of 13 seasons, and it fails the required −0.0050. The challenger does not pass G1 here.
* **Win probability and totals** are unchanged: ΔBrier(win) −0.0001 [−0.0003, +0.0001]; ΔRPS(total) −0.0005 [−0.0012, +0.0001]; over 5.5 and 6.5 within ±0.0003. In 2023–2025 ΔRPS(total) is +0.0013 (descriptive).
* **Joint distribution (the question the overtime fix has to answer).** Multi-category Brier on the 10-cell result × margin partition: −0.0008 [−0.0012, −0.0003] (SIM2), −0.0006 [−0.0010, −0.0001] (SIM2_ST); on the 36-cell result × total partition: −0.0006 [−0.0008, −0.0004] and −0.0005 [−0.0008, −0.0003]. Log scores improve by 0.012 and 0.011 (margin partition). J1 (non-inferiority, bound +0.0020) passes everywhere. Per season the joint-margin delta is favourable in 11 of 16 seasons and unfavourable in 2010 and in 2015–2017 (+0.0009 to +0.0019): the joint gain is real but small and not uniform.
* **G7** measured at 0.106 s per game with the four shards running concurrently, so a 16-game slate (the maximum in the sample) takes about 1.7 s (limit 300 s). **G8**: season 2012 regenerated from scratch is bit-identical to the shard for every arm (`np.array_equal` on all six cell tables).

## What is wrong with the margin distribution (the actual error source)

Pooled over all 18,777 games, every arm *under-predicts large regulation margins and over-predicts one-goal margins*:

| cell (regulation) | V1 predicted vs observed | SIM2 predicted vs observed |
|---|---|---|
| home win by 1 | 2545 vs 2017 (z −11.3) | 2438 vs 2017 (z −9.1) |
| home win by 3+ | 3596 vs 3905 (z +5.8) | 3421 vs 3905 (z +9.2) |
| away win by 3+ | 2591 vs 2888 (z +6.3) | 2423 vs 2888 (z +10.2) |

(read: first number is the predicted count, second the observed count; the z sign is observed against expected). V2 moves probability mass out of regulation into overtime and the shootout, which is right for those cells but removes it from the regulation tails, which were already too thin. So the overtime fix is a gain in itself and makes the margin shape slightly worse. The margin tail is a separate defect (the tails of the score distribution, empty-net goals and score-state effects are the candidates) and needs its own preregistered challenger; it must not be hidden inside an overtime promotion.

## Caveats stated in advance and kept

* Retrospective vendor shot and xG data; no historical starters; 4-on-4 overtime through 2014 (the 3-on-3 subgroup is reported above and agrees).
* Differences below ≈ 0.001 Brier are unresolvable at about 1,300 games per season.
* The exposed seasons 2023–2025 are reported, never used for selection.
* The 2010–2022 seasons are "unexposed" with respect to the V2 simulator only. The incumbent V1 at production constants is scored on them here; no retuned or opponent-adjusted V1 arm has been (see `docs/research/v1-retune/AMENDMENT_2_FRESH_TIER_2010_2016.md`).

## What is still required before the overtime component could be promoted

1. **G9** SIFT-contract compatibility check and **G10** live non-inferiority over a pre-declared number of shadow games (the prospective tier stays unread until then).
2. A decision on the margin distribution: either ship overtime only with the V1 margin shape (a hybrid is a new model and needs its own registration), or fix the margin tails first. Whichever is chosen, the margin target must pass G1/G2/G6 or be explicitly excluded by the approver.
3. Explicit human approval. This document recommends continued shadowing at most.
