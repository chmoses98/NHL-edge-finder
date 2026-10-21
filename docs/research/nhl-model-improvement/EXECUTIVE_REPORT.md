# SIFT NHL — model-improvement research: executive report

> RESEARCH ONLY · 2026-10-21 · branch `claude/nhl-model-improvement-f6kn0k` (stacked on draft PR #52). **No wager was placed, no stake/cap/exposure changed, no challenger activated, no production recommendation changed, nothing merged.** The prospective tier (games starting after 2026-10-21T17:13:05Z) was not read by any development code. A defensible negative result is the deliverable here.

## Bottom line

1. **The prior audit's central finding stands and is now independently reproduced.** A cold re-run of the 20-step pipeline on a later archive snapshot reproduces every committed statistical output *identically* (hypothesis registry, market efficiency, model audit, matchup study, execution walk, sensitivity, wager summary, Oct 20 case). No validated betting strategy exists (0 of 16 hypotheses VALIDATED; under the stricter v1.1 labels: 0 promising, 3 "unprofitable at the ask", 1 point-positive, 12 inconclusive — and 12 of 16 have a tier too small to see an ROI below 10%).
2. **The review found real defects, none of which overturns that finding** but two of which overstated what the audit proved: the shadow expression engine could *never* recommend a bet (a double-counted uncertainty term), so its "PASS in all 151 games" was mechanical; and the registry's PROMISING/REJECTED labels were sign-based, with the prospective tier being evaluated on every pipeline run. All fixed in separate commits. With the engine corrected, the counterfactual that waives the evidence gate and trusts the models at half weight **would have lost 16.5% (95% CI −30.4% to −2.6%) on 190 bets**, against a claimed +5.1% EV per contract; the evidence-gated engine still recommends zero wagers.
3. **Why the models trail the market: not one correctable error.** The hypotheses most often voiced were tested and mostly rejected (table below). V1 has real skill for *who wins and by how much* but **none for how many goals** (its total-goal forecast scores the same as a league-average constant), and the market's information advantage (starter, lineups, injuries, sharper pricing) is not something the archive lets us isolate.
4. **No forecast improvement survived.** Statistically significant calibration slopes (margin 1.39, total 0.37) corrected by a challenger changed no score; strength-uncertainty noise was rejected; no model or challenger beat the Kalshi/sportsbook baseline on any development tier.
5. **October 20 and the 34 routed wagers are consistent with fair-price trading.** The realised −$187.64 is 0.6 SD below the fees-and-spread expectation (−$55.85, reproduced exactly). Almost all of the loss is the player-prop book (−$178.49 of −$187.64; goal-scorer props 0 for 4); game-scoped bets were about break-even net of fees. Three of the four Oct 20 fills were **genuine new entries 6–8 minutes after the scheduled drop** (not cash-outs); the evidence-consistent decision on all four was PASS.

## The operator's questions, answered with evidence

| question | verdict | key number | evidence tier |
|---|---|---|---|
| Misunderstanding matchups? | no evidence | rest/b2b/early-season/season residuals all \|t\| < 1.7 (BH q ≥ 0.32); opponent-adjusted xG etc. fail out of sample | 2,624 games + prior audit |
| Over-valuing recent scoring trends? | marginally | finishing-sum → total residual −0.17 goals/SD (q = 0.003) | EXPLORATORY; immaterial |
| Under-estimating shot quality? | suggestive, early season only | xG − V1 goals +0.30/game [+0.13, +0.49]; finishing −0.20 [−0.58, +0.17] | LIVE-descriptive (140 games) |
| Opponent adjustment? | strengths under-spread (margin slope 1.39), totals over-spread (0.37) | correcting both: **no score improves** (all paired CIs span 0) | EXPLORATORY |
| Goalie assumptions too confident? | **rejected** | CONFIRMED 97.8% vs stated 98.5%; PROBABLE 97.1% vs 85% (under-confident); PROJECTED 76.5% vs 70% | LIVE-descriptive (302 slots) |
| Simulations too narrow / missing 7–9 goal games? | **rejected** | total-goal z² = 0.913 (CI 0.863–0.966): slightly too *wide*; P(≥8) 26.1% pred vs 24.8% obs, P(≥9) 18.4% vs 17.3% | 2,624 games; RPS/CRPS, PIT |
| What *is* mis-shaped | OT and margin | OT 17.4% vs 22.8% (V2 fixes it: Brier −0.003 [−0.0044, −0.0017]); \|margin\| ≥ 3 34.7% vs 39.6% | 2,624 games |
| Player usage assumptions? | biased low; outputs unbiased | TOI +0.41 min, PP time +0.66 min, shots +0.14 per game (CIs exclude 0); points/goals/assists errors ≈ 0; TOI interval too wide (86% vs 80%) | LIVE-descriptive (2,597 player-games) |
| Miscalibrated / distributions too narrow? | no | P(1+ point) calibrated and better than a league rate | |
| Wrong market expression? paying too much? | paying too much, yes | taker ask + fee is 4–5 cents worse than the market's probability (moneyline −4.3% both sides); routed shortfall = fees + spread | strong |
| Bets after information priced in? | capture too slow to tell | our goalie capture lags the source by a median 27.6 min (26% within 15 min); Kalshi moneyline mids show no detectable reaction to 32 goalie changes at 15-minute resolution | LIVE-descriptive |
| Normal variance? | largely yes | 17.2% of LIVE games are "extreme" under the forecast's own distribution vs ≈ 19% expected | descriptive |

## What was tested, what improved, what did not

| experiment | result |
|---|---|
| M-DIST-1 distribution fidelity (2,624 games) | totals not narrow; OT and margin shape mis-specified |
| M-CAL-1 C1 recalibration (rolling-origin) | **NO_IMPROVEMENT** (EVAL_A: ΔRPS total −0.0009 [−0.0059, +0.0042]; ΔBrier win +0.0001 [−0.0010, +0.0013]) |
| M-CAL-2 strength-uncertainty | **REJECTED** (σ = 0 on every date) |
| M-MKT-1 information beyond the Kalshi T-60 mid | **NO_INCREMENTAL_VALUE** (inc − mid: winner +0.0000, total +0.0005, spread +0.0003; all CIs span 0) |
| M-LIVE-1 one look at 151 LIVE games | **LIVE_INCONCLUSIVE** (ΔRPS total +0.0073 worse, ΔBrier win −0.0018 better; neither significant) |
| M-SCAN-1 systematic-error scan | 3 candidate class-A patterns, all immaterial; 14 null |
| M-GOALIE-1 / M-PLAYER-1 / M-SCRIPT-1 / M-INFO-1 | see `PREDICTION_ERROR_AUDIT.md`, `MATCHUP_AND_SCRIPT_STUDY.md`, `INFORMATION_EVENT_ASSESSMENT.md` |
| V2 vs V1 (published) | OT only; moneyline/totals unchanged |

**Did any improvement exceed the market baseline? No.** Model alone vs Kalshi T-60 mid on 2025-26 history: +0.0014 (winner), +0.0014 (total), +0.0017 (spread) Brier worse; LIVE: +0.0036 / +0.0026 / +0.0045 worse (no interval excludes 0 except C1 totals, in the wrong direction). Sportsbook consensus beats V1 (147 games: 0.2275 vs 0.2313). **Does an executable betting advantage exist? None demonstrated**: no family shows a repeatable inefficiency after fee and spread, and no model gap clears its 2–3 point cost of expression.

## Which market expressions look most promising?

None is validated. In the one worked example (TOR @ CBJ) the cheapest expression per point of required edge was a puck-line NO leg (1.7 pts vs 2.2 for moneyline/totals and 3.0 for a thin team total), which says something about *cost*, not about edge. Candidates for further research only: period spreads YES showed +8.3% LIVE ROI (CI −5.5% to +22.2%, unregistered, post-hoc) and the early-goal Under is point-positive (+0.1%, CI ±18 points). Both are the kind of result expected by chance when many family-by-side cells are examined. The default for every thesis remains PASS.

## What is built (all shadow-only, reversible)

Reproducible pregame reconstruction of the 151 LIVE games with lineage (`live_dataset.py`, `build_tables.py`); bit-exact regeneration of V1 predictive distributions (RPS/CRPS, PIT, tail diagnostics); error-attribution pipeline (classes A–F with evidence); rolling-origin challenger harness; market-comparison tools; corrected shadow expression engine with PASS; registry v1.1; append-only hash-chained experiment registry (11 experiment ids — 10 with results, 1 prospective preregistration — 25 entries, chain verified); blinded prospective scorecard + daily ledger (`daily.py`) with a manual-dispatch, `publish=false` workflow; 35 new tests on top of PR #52 (full suite: 656 passed, 2 skipped, 0 failures; `ruff check src tests scripts` clean); generated results tables.

## What remains uncertain

Everything about edges below ≈ 5% ROI or ≈ 0.004 Brier (undetectable at 151 games); whether early-season effects explain the LIVE xG gap; whether the market's information advantage is lineup/goalie news (the archive cannot time when the *market* learned anything); PLAYER_SIM beyond usage; V2/PLAYER_SIM distributions (not regenerated); the unreviewed review items listed as open in `PR52_INDEPENDENT_REVIEW.md`.

## Recommended next actions

1. **Approve** the prospective shadow protocol (`PROSPECTIVE_PROTOCOL.md`: looks at 150/300/450, Lan–DeMets spending, ≤ 3 primary hypotheses) and the manual-dispatch daily workflow (publish=false first).
2. **Approve** the goalie change-log capture proposal (separate draft PR; one conditional poll inside the existing capture worker; 4-week shadow) — the only plausible source of a pregame edge is information timing and our capture is currently too slow to test it.
3. **Approve** adding exchange `action`, order/fill timestamps and an optional owner-supplied recommendation reference to the router's raw record (docs-only note in the router repo).
4. Research (no approval needed): recalibrate V1's tie/OT and margin shape with the V2 score-effects engine on the development tier; re-estimate player usage (TOI/PP) and re-test PLAYER_SIM; extend the matchup study once timestamped lineups exist.
5. Fix the open review items (doc corrections D3/D4, thesis/wager freeze filters, stronger mutation-resistant tests).

## Keep disabled / require explicit approval

Any change to stakes, caps, exposure; any promotion of V2, C1 or the expression engine; enabling either manual workflow's schedule or `publish`; merging PR #52 or the stacked PR; changing production capture; any goal-scorer recommendation (never).

## Evidence bar for future promotion or stake increases

A frozen strategy; prospective positive net ROI after fee and +1c slippage with a positive lower-90% bound at a predeclared look (spending boundary, ≤ 3 hypotheses); calibration no worse than the market baseline; executability from captured depth; a confirming later window; explicit approval. At 151 games a +3% edge needs hundreds to thousands of independent games, so within one season only a much larger edge could qualify.
