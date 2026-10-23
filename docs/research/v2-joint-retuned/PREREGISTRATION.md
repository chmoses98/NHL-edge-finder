# J2 — retuned and recalibrated V1 rates through the V2 simulator: joint game-distribution test (preregistration)

> RESEARCH_ONLY · written 2026-10-23, **committed before any J2 simulation exists**. The commit time is the registration time. Nothing here changes a production number, price, stake, cap, routing or authority; **nothing is promoted** (the scorecard recommends, a human decides). Single published projection per target is unchanged: the arms below are research outputs only.

## Why

Two separate findings point at different defects of the incumbent (V1 rates through the `nhl-sim-1.1` simulator):

* the V2 simulator (`nhl-sim-2.0`) fixes **overtime / the regulation tie** (`docs/research/v2-joint/RESULTS.md`: ΔBrier(OT) −0.0023, 13 of 13 unexposed seasons) but leaves winner and totals unchanged and makes the **goal-margin tails slightly worse** (ΔRPS(margin) +0.0010);
* chronologically retuned shrinkage constants plus slope recalibration (`V1_R_C1`) improve **win probability** in 2018–2024 (−0.0017 pooled 2017–2025) but not in 2010–2016 or 2025 (`docs/research/v1-retune/RESULTS.md`).

They address different targets, and the retuned rates were only ever scored through the V1 simulator. The explicit gap named in both documents is the **combination**: do the retuned/recalibrated rates and the V2 simulator add up, or does one undo the other?

## Arms (same games, same seeds `game_seed(game_id)`, 4,000 draws, goalie factor 1.0)

| arm | rates | simulator |
|---|---|---|
| `V1` (incumbent) | production `DATA_ONLY_V1` | `nhl-sim-1.1` |
| `SIM2` | production V1 | `nhl-sim-2.0` |
| `R_SIM1`, `R_SIM2` | `V1_R` (chronologically retuned constants, registered grid) | 1.1, 2.0 |
| `RC_SIM1` | `V1_R_C1` (retuned + slope recalibration) | 1.1 |
| **`RC_SIM2`** | `V1_R_C1` | **2.0 — the combination** |

The rates are the committed per-game tables of the registered study (`docs/research/v1-retune/data/v1r_games_{main,fresh2}.csv.gz`: columns `V1_R_*`, `V1_R_C1_*`), selected and calibrated strictly inside each training window. V2 parameters are fitted exactly as in `docs/research/v2-joint/PREREGISTRATION.md` (rolling window of the last 4 shot seasons; `env_dispersion` chosen on S−1; `p(OT decided before SO)` from earlier official results). The recalibration slopes were fitted on the *rates*, not on simulator output; whether they are right for V2's different total-goal behaviour is part of what is being tested (mean predicted total vs observed is reported per arm) and a V2-specific recalibration is **not** done here.

## Targets scored together (every arm, every game)

winner (Brier, log loss) · regulation outcome (3-class Brier: home regulation win / regulation tie / away regulation win) · overtime (Brier of "game went past regulation") · totals (RPS of the total-goal pmf; Brier of over 4.5/5.5/6.5/7.5) · team totals (Brier of each team over 1.5/2.5/3.5/4.5, averaged) · goal differential (RPS of the final-margin pmf) · puck lines (Brier of home and of away winning by 2+) · the two **joint** partitions of `joint_eval` (10-cell result × margin, 36-cell result × total; multi-category Brier and log score).

## Tiers

* **DECISION tier `CLEAN2` = 2010–2016**: never scored by any V1-retune-family arm (Amendment 2) and never by the V2 simulator before `v2-joint` (2010–2022). 7,725 games.
* `V2CLEAN_FAMILYSEEN` = 2017–2022: unseen by V2 before `v2-joint`, but seen by the retune family.
* `EXPOSED` = 2023–2025: scored by V2 (`walk_forward_v2`, published) and by the retune family.
* `PROSPECTIVE` (games after 2026-10-21T17:13:05Z): unread.
Pooled 2010–2025 is descriptive only.

## Questions and rules (set before looking)

* **J2-A, additivity.** Using paired differences vs `V1` pooled on `CLEAN2` (game and slate bootstraps): `RC_SIM2` *keeps the win gain* if its ΔBrier(win) is no worse than `RC_SIM1`'s by more than 0.0005, and *keeps the overtime gain* if its ΔBrier(OT) is no worse than `SIM2`'s by more than 0.0005. Both must hold for "additive". The paired `RC_SIM2` − `RC_SIM1` and `RC_SIM2` − `SIM2` intervals are reported.
* **J2-B, scorecards.** The unchanged promotion scorecard (`promotion.score_challenger`, gates G1–G10 plus J1 from `joint_eval`) is applied to `RC_SIM2` vs `V1` for four targets: overtime (primary Brier(OT)), goal margin (RPS(margin)), win probability (Brier(win)) and total goals (RPS(total)); unexposed = `CLEAN2`, exposed = 2017–2025. Verdicts are the scorecard's and promote nothing.
* **J2-C, does anything beat the best single fix?** `RC_SIM2` is called *complementary* only if on `CLEAN2` it is no worse than the better of `{RC_SIM1, SIM2}` on every one of {win, OT, total RPS, margin RPS} beyond the practical thresholds (0.0010 Brier / 0.0050 RPS) **and** its joint 10-cell and 36-cell Brier are not worse than both single fixes with an interval excluding 0.
* **Descriptive (no gate):** team totals, puck lines, regulation 3-class, per-season deltas, pooled 2010–2025, 3-on-3 subgroup (2015–2025), and the market comparison.
* **Market comparison (2025-26 only, matched timestamp).** Kalshi candle-close midpoint at T-60 min, identical instant for every forecaster: winner, total over 5.5/6.5, puck line (win by 2+), team total and overtime where the repository's Kalshi history has quotes (`KXNHLGAME`, `KXNHLTOTAL`, `KXNHLSPREAD`, `KXNHLTEAMTOTAL`, `KXNHLOT`). A midpoint advantage would not be an execution edge; PASS-only is unchanged.

## Limits stated up front

Retrospective vendor shot/xG data; no historical starters; 4-on-4 overtime through 2014; franchise abbreviations unresolved in 2010–2013 (games dropped for every arm alike); differences below ~0.001 Brier are unresolvable per season; the retuned rates inherit the regime dependence found in the retune study (gains 2018–2024, none in 2010–2016 or 2025); team-total and puck-line results come from the same simulations and are not independent evidence.
