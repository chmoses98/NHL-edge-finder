# V2 simulator: joint game-distribution validation — preregistration

> RESEARCH_ONLY · written 2026-10-23 · **committed before any V2 simulation exists for the seasons below** (2010–2022); the commit time is the registration time. Nothing here changes a production number, price, stake, cap or authority, and nothing is promoted: the promotion scorecard (`PROMOTION_SCORECARD.md`) *recommends*, a human decides.

## Why

The only evidence for `nhl-sim-2.0` (the V2 simulator) is 2023–2025 (3 seasons, one of them never scored by anything before), so gate G5 (≥ 3 unexposed seasons, ≥ 3,000 games) was unmet, and every score so far is a *marginal* one (P(win), P(OT), the total pmf, the margin pmf, each on its own). Two things are done here:

1. **More unexposed seasons.** MoneyPuck shot-level data for 2008–2020 was pulled on a network-capable runner (`data/history/shots_extension/`, kept outside `data/history/moneypuck/` so the production `load_shots` never reads it) so the V2 hazards can be fitted, strictly out of sample, for every season 2010–2022. Those 13 seasons have **never been scored by the V2 simulator**; 2023–2025 have.
2. **A joint score.** The overtime fix is only worth shipping if the way a game ends, its margin and its total goals hang together better, not just the overtime rate. Two proper scores on the *joint* outcome are added (definitions in `joint_eval.py`): the 10-cell **result × margin** partition (regulation home/away win by 1, 2, 3+; overtime home/away; shootout home/away) and the 36-cell **result × total-goals bucket** partition. Metric: multi-category Brier score (primary) and log score with probability floor 0.001; plus pooled per-cell reliability and the overtime conditionals (P(OT or SO), P(SO | tie)).

## Arms (identical games, seeds `game_seed(game_id)`, 4,000 draws, goalie factor 1.0)

| arm | rates | simulator |
|---|---|---|
| `V1` (incumbent) | DATA_ONLY_V1 | `nhl-sim-1.1` |
| `SIM2` | DATA_ONLY_V1 | `nhl-sim-2.0` — isolates the simulator (overtime / score state / empty net / periods) |
| `SIM2_ST` | special-teams rates (`nhl-features-2.0`) | `nhl-sim-2.0` — the full valid-pregame V2 |

## Protocol (the published `walk_forward_v2` protocol, with two stated differences)

For each scored season S every V2 parameter is fitted on data strictly before S: hazards on shot seasons, `env_dispersion` chosen on season S-1 with hazards fitted before S-1, `p(OT decided before SO)` from the official results of the same seasons. **Differences:** (a) a rolling window of the **last 4 shot seasons** (the published run used an expanding window from 2021, which is 2–4 seasons for 2023–2025); (b) the earliest usable shots season is 2008. Everything else — nested validation, the dispersion grid, seeds, draw counts — is `walk_forward_v2`'s, and `tests/test_joint_eval.py` pins that the defaults of the modified functions reproduce the published ranges exactly. The old-rules caveat: overtime was 4-on-4 through 2014 and 3-on-3 from 2015; hazards and the OT-vs-shootout share are fitted on the window only, and the **3-on-3 era (2016–2022)** is reported separately as a pre-declared subgroup because it is the one that resembles today's game.

Games whose franchise abbreviation the repository cannot resolve (13.3% in 2010, 6.7% in 2011–2013; `HISTORY_EXTENSION_2008_2014.md`) are dropped for every arm alike.

## Gates (unchanged scorecard + one added) and what counts as a result

* **Overtime / regulation-tie target** (primary metric Brier(OT)), **goal-margin target** (RPS(margin)): the ten gates of `promotion.score_challenger` exactly as coded (G1 improvement under both bootstraps, G2 ≥ 0.0010 Brier / 0.0050 RPS, G3 non-inferiority of the other metrics, G4 ECE, G5 ≥ 3 unexposed seasons and ≥ 3,000 games, G6 ≥ 2/3 seasons favourable and none significantly worse, G6b exposed seasons not contradicting, G7 runtime ≤ 300 s/slate, G8 reproducibility, G9 contract, G10 live non-inferiority). **Unexposed = 2010–2022; exposed = 2023–2025.** G7 is measured on a representative slate, G8 by regenerating one season bit-for-bit, G9/G10 stay pending (they need the live shadow).
* **Added gate J1 (joint non-inferiority):** the upper 95% bound of Δ multi-category Brier (challenger − incumbent) on the joint margin partition and on the joint total partition must each be ≤ +0.0020. A joint *improvement* (interval below 0) is reported, not required.
* Verdicts are the scorecard's: `RETAIN_INCUMBENT` (a hard gate fails), `SHADOW_MORE` (history passes, G9/G10 pending), `PROMOTE_CANDIDATE`. None of them promotes anything. Pre-declared subgroups (3-on-3 era 2016–2022; the lockout season 2012; each season) are descriptive.

## Limits stated up front

Retrospective vendor shot and xG data; no historical starters (goalie term off); the pre-2015 overtime rules differ from today's; MoneyPuck's shot mirror, not an official feed; differences below ≈ 0.001 Brier are unresolvable at ~1,300 games per season.
