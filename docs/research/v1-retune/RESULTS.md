# Retuned V1 + recalibration vs opponent adjustment — results

> RESEARCH_ONLY · 2026-10-23 · preregistration `PREREGISTRATION.md` (commit `8e368035`, 2026-10-23T02:28:50Z, before any arm was run) and `AMENDMENT_2_FRESH_TIER_2010_2016.md` (registered before any V1-family arm was scored on 2010–2016). Frozen code: `claude/nhl-v1-retune` at `3e3c64a` (arms unchanged since `c41e0d65`). **Nothing is promoted; no production number, price, stake, cap or SIFT contract is touched.** Data: `data/` (per-game tables as `.csv.gz`, evaluation JSON/markdown, tuning grids). Reproduce: `oa_walk_forward → v1_tuned_control → v1_retune → retune_evaluate` (deterministic; the per-game pmfs regenerate byte-identically from the same code and seeds).

## Bottom line

1. **No challenger beats the market** (2025-26, Kalshi midpoint at T-60 min): every V1-family arm and `OA_SVA_C1` is indistinguishable from the midpoint on the winner and the −1.5 puck lines and is *behind* it on total-over-6.5 (+0.0028…+0.0032 Brier, intervals exclude 0); retuning narrows but does not close the 5.5/6.5 gaps.
2. **Opponent adjustment adds nothing detectable once V1 is retuned and recalibrated** (R3, both tiers): `OA_SVA_C1` vs `V1_R_C1` −0.0003 [−0.0007, +0.0002] pooled 2017–2025 (5/9 seasons favourable), −0.0002 [−0.0006, +0.0003] on the untouched 2010–2016 tier (3/7). `OA_SVA_C1` also has a tiny but significant overtime-Brier penalty pooled (+0.0002 [+0.0001, +0.0004]). The simpler model is preferred.
3. **The retune gain is regime-dependent, not a general property.** Pooled 2017–2025, `V1_R_C1` improves win-probability Brier over production V1 by **−0.0017 [−0.0023, −0.0011]** (8/9 seasons ≤ 0), but nearly all of it comes from 2020–2023 (−0.0015…−0.0039 per season); 2017 and 2025 are ≈ 0 and on the untouched **2010–2016 tier it is −0.0004 [−0.0009, +0.0001]**, i.e. not distinguishable from V1 and far below the registered 0.0010 practical threshold. Production constants were near-optimal before 2018; a 10-game shrinkage prior and a shorter memory only help in the later regime.
4. **Which candidate "leads" (R4) — honestly: a tie, and nothing leads V1 outside 2018–2023.** Pooled 2017–2025: `V1_R_C1`, `V1_T_C1` and `V1_C1` are tied within the practical threshold (equal complexity; the registration defines no tie-break between them, so none is invented). On 2010–2016 every arm is within the threshold of the best and the simplest, `V1`, "leads". The best Brier overall is `OA_SVA`/`OA_SVA_C1` (0.2382) vs V1 0.2402, but it is statistically tied with the retuned, recalibrated V1.
5. **No promotion is warranted or requested.** Evidence still required is listed at the end.

## Registered decision rules (pooled over the tier's seasons)

| rule | tier 2017–2025 (9 seasons, 11,052 games) | untouched 2010–2016 (7 seasons, 7,725 games) |
|---|---|---|
| R1 `V1_R` better than `V1` | **NOT BETTER** — Brier(win) −0.0014 [−0.0018, −0.0010], 9/9 seasons, size ≥ 0.0010 — but **total-goal RPS worse** (+0.0035 [+0.0022, +0.0049]), which the rule forbids | **NOT BETTER** — −0.0003 [−0.0007, +0.0001], 4/7 |
| R2 `V1_R_C1` better than `V1_R` | **NOT BETTER** — win −0.0003 [−0.0005, +0.0000] (5/9), below threshold; it does repair totals (RPS −0.0022 [−0.0039, −0.0004]) | **NOT BETTER** — win −0.0001, RPS −0.0017 [−0.0033, −0.0002] (but overtime Brier +0.0002 [+0.0000, +0.0003]) |
| R3 `OA_SVA_C1` better than `V1_R_C1` | **NOT BETTER** (−0.0003 [−0.0007, +0.0002]; 5/9) | **NOT BETTER** (−0.0002 [−0.0006, +0.0003]; 3/7) |
| R4 leading candidate | TIE: `V1_R_C1`, `V1_T_C1`, `V1_C1` | `V1` (everything within the threshold) |
| R5 informative features | back-to-back (win Brier +0.0007 [+0.0004, +0.0009] when removed), finishing ratio (total RPS +0.0046 [+0.0021, +0.0070]) | back-to-back +0.0004 [+0.0001, +0.0008]; finishing ratio +0.0011 [+0.0003, +0.0019] |

## Paired Brier(win) vs production V1 by tier (negative = better)

| arm | FRESH 2017 (1,271) | FAMILY_SEEN 2018–23 (7,157) | EXPOSED 2024–25 (2,624) | **FRESH2 2010–16 (7,725)** | FRESH2 3-on-3 only 2015–16 (2,460) |
|---|---|---|---|---|---|
| `V1_R` | −0.0006 [−0.0013, +0.0001] | −0.0018 [−0.0023, −0.0013] | −0.0009 [−0.0021, +0.0003] | −0.0003 [−0.0007, +0.0001] | −0.0009 [−0.0016, −0.0002] |
| `V1_R_C1` | −0.0003 [−0.0010, +0.0004] | −0.0023 [−0.0030, −0.0016] | −0.0007 [−0.0023, +0.0010] | −0.0004 [−0.0009, +0.0001] | −0.0008 [−0.0018, +0.0002] |
| `V1_C1` (recalibration only) | +0.0001 [−0.0004, +0.0005] | −0.0014 [−0.0019, −0.0009] | −0.0005 [−0.0014, +0.0006] | −0.0005 [−0.0008, −0.0001] | −0.0003 [−0.0010, +0.0003] |
| `OA_SVA` | −0.0002 [−0.0011, +0.0007] | −0.0026 [−0.0032, −0.0019] | −0.0010 [−0.0022, +0.0002] | −0.0004 [−0.0008, −0.0000] | −0.0005 [−0.0013, +0.0003] |
| `OA_SVA_C1` | +0.0002 [−0.0008, +0.0011] | −0.0028 [−0.0036, −0.0019] | −0.0007 [−0.0022, +0.0009] | −0.0006 [−0.0011, −0.0001] | −0.0006 [−0.0016, +0.0003] |

The per-season table (`data/retune_eval_*.md`) shows the same picture: `V1_R_C1` is ≤ 0 in 8 of 9 seasons of 2017–2025 but within ±0.0010 in all of 2010–2017; the large values are 2020 (−0.0036), 2021 (−0.0039), 2022 (−0.0029), 2023 (−0.0019). Calibration (ECE of the win probability, pooled 2017–2025): V1 0.0228 → `V1_C1` 0.0136, `V1_R_C1` 0.0110, `OA_SVA_C1` 0.0086.

## What the controls say about the earlier finding

* The attribution control from the opponent-adjusted study holds: retuned V1 (`V1_T`/`V1_R`) captures most of the 2018–2023 gain (−0.0018 of −0.0026 for `OA_SVA`), and the widened grid changes almost nothing (`V1_R` ≈ `V1_T`: the earlier 10-game prior floor was binding in only 2 of 9 seasons; the new 2.5/5 prior values were selected once (5 games in 2020 and 2024), the edge 2.5 never).
* Tuning hit a grid edge in a few seasons and is reported as binding, not widened: half-life 160 (the upper edge) in 2021 (main) and 2013 (FRESH2); home-ice multiplier 1.06 (the upper edge) in 2018, 2010 and 2013.
* The fresh tier does not confirm the registered historical gain. The sign is the same everywhere (retuned/recalibrated ≤ V1) but the size on 2010–2016 is 0.0003–0.0006, below the practical threshold and, for `V1_R`/`V1_R_C1`, inside the interval of zero.

## V2 simulator and the market (exploratory, 2023–2025 and 2025-26 only)

* V2's `SIM2` (the V2 simulator on V1's own rates) fixes overtime but not the win probability: overtime Brier −0.0022 [−0.0032, −0.0011], win −0.0002 [−0.0005, +0.0001] vs V1 on 3,936 games; the retuned arms improve win (`V1_R` −0.0011 [−0.0020, −0.0002]) and not overtime. The two fixes address different targets; **their combination (retuned rates through the V2 simulator) was not run** — an explicit gap.
* Against the Kalshi midpoint (2025-26, 1,312 games, T-60 min, no depth/fee/slippage): winner `V1` +0.0017, `V1_R` +0.0015, `V1_R_C1` +0.0018, `OA_SVA_C1` +0.0010 (all intervals include 0); total-over-6.5 market better than every arm (+0.0028…+0.0035, intervals exclude 0); total-over-5.5 market better only than V1. A midpoint advantage would not be an execution edge in any case (executable asks cost 4–5 cents more).

## Limits

Retrospective vendor xG (MoneyPuck refits retroactively); no historical starting goalies/lineups (the live goalie term is off in every arm); 2010–2013 omit 6.7–13.3% of games whose franchise abbreviation cannot be resolved (dropped for every arm alike: 163/82/48/82 games in 2010–2013); pre-2015 overtime rules differ (4-on-4 and shootout), which affects the overtime/tie component, not V1's regulation rates (the 2015–2016 column is the 3-on-3 subgroup); tuning objective (goals likelihood) differs from the evaluation objective; Brier differences below ~0.001 are unresolvable per season. The prospective tier is unread.

## Evidence still required before any promotion

1. A frozen prospective shadow record for the single candidate (the OA shadow arm already writes `OA_SVA`/`OA_SVA_C1` beside V1; a `V1_R_C1`-style arm would need its own frozen parameters and preregistration) — hundreds of settled games, since the effect to resolve is ≈ 0.001–0.002 Brier.
2. A regime argument: why 2018–2023 differs from 2010–2016 and 2025 (e.g., scoring environment, tracking-era xG), and whether the 2025-26/2026-27 regime resembles the favourable one; today the most recent exposed season shows ≈ 0.
3. The joint V2-simulator + retuned-rates test, so that overtime/margin shape and rating quality are fixed together on one set of games, under the existing promotion gates (`PROMOTION_SCORECARD.md`, thresholds unchanged).
4. Calibration/runtime/freshness/SIFT-contract compatibility gates and **explicit approval** — none of which this document requests.
