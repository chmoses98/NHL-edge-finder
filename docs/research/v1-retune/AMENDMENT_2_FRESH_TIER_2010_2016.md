# Amendment 2 to the V1 re-tune preregistration — second FRESH tier, seasons 2010–2016

> RESEARCH_ONLY · registered 2026-10-23, **before any V1-family arm (`V1_R`, `V1_R_C1`, `V1_T*`, `OA_*`, ablations) has been scored on 2010–2016.** The commit time of this file is the registration time. It changes no arm, no grid, no estimator and no decision rule of `docs/research/v1-retune/PREREGISTRATION.md` (commit `8e368035` on `claude/nhl-v1-retune`). Nothing here changes a production number, price, stake, cap or authority, and nothing is promoted.

## Why

The registered study could only name 2017 as an untouched ("FRESH") tier, which is one season (n ≈ 1,270) and therefore underpowered; every other season had been scored by an earlier member of the family. PR #68 adds MoneyPuck team-game rows and official results for 2008–2014 (`data/history/MANIFEST.json`, `docs/research/HISTORY_EXTENSION_2008_2014.md`). With selection needing seasons S−2 and S−1, seasons 2010–2016 can be tested and have never been scored by any model in this repository's V1/OA/retune family.

## Registration

* **Tier `FRESH2`: test seasons 2010–2016** (MoneyPuck start-year convention; 2012 is the lockout season, 48 games). Selection for season S uses S−2 and S−1 only (for 2010: 2008–2009). `FRESH` (2017) is unchanged and may be pooled with `FRESH2` as a descriptive `FRESH_ALL` (2010–2017); the decision tier for the confirmatory reading is `FRESH2` on its own and `FRESH_ALL` is reported next to it.
* **Games:** every game that `load_team_games` returns for those seasons with a resolved official result. Games whose franchise abbreviation the repository cannot resolve (13.3% of 2010, 6.7% of 2011–2013 per the data-quality table) are dropped for every arm alike; the dropped counts are reported per season.
* **Arms, grids, tuning objective, draws, seeds, calibrator, metrics, bootstrap:** exactly as registered. The code evaluated is the frozen code on `claude/nhl-v1-retune` at the commit that is current when the run starts; the commit hash is recorded in the results. No arm may be added, no grid altered, and a grid boundary hit is reported as binding, not widened.
* **Decision rules R1–R5:** exactly as registered, applied to `FRESH2` separately from every other tier. The only adaptation is that the season-consistency requirement scales with the number of seasons: "at least 6 of 9" becomes **"at least 5 of 7"** (the nearest whole number to the same two-thirds fraction, rounded up). The practical threshold (0.0010 Brier) and the two-bootstrap interval requirement are unchanged.
* **What a `FRESH2` result may say:** it is the first confirmatory reading of R1–R3. If R3 fails on `FRESH2` and on the pooled `FRESH_ALL`, the simpler model (retuned, recalibrated V1) is preferred; if R3 passes on `FRESH2` but not on the other tiers, that disagreement is reported as such and no tier is privileged after the fact. No tier result can promote a model.
* **Old-rules caveat (stated in advance):** overtime was 4-on-4 and the shootout absent in some of these seasons' predecessors; the 2005–2013 rule differences affect the overtime and tie components, not V1's regulation-goals rates. `FRESH2` is therefore also reported for 2015–2016 alone (the first 3-on-3 seasons) as a descriptive subgroup. Nothing is selected on it.

## Disclosure of what has already been looked at

* The V2-simulator joint-distribution study (`docs/research/v2-joint/PREREGISTRATION.md`, a different model family with its own registration) scores the **incumbent `V1` at its production constants** and the V2 simulator on 2010–2022. Its outputs therefore contain V1's level on these games. They contain no retuned, recalibrated or opponent-adjusted arm, and a fixed-constants V1 level does not inform the sign of a retuned-minus-V1 contrast chosen from a grid inside each training window; this is stated so the reader can judge.
* The 2008–2014 data-quality table counts rows and null columns. It scored nothing.
* No `V1_R`, `OA_*` or ablation arm has been run on 2010–2016 by the author of this amendment.

## Run

The owner of the frozen retune code runs `oa_walk_forward`, `v1_tuned_control`, `v1_retune` and `retune_evaluate` on seasons 2010–2016 and reports `FRESH2` separately from `FRESH`, `FAMILY_SEEN` and `EXPOSED`. The `PROSPECTIVE` tier remains unread.
