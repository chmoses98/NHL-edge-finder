# OA_RIDGE walk-forward — results

> RESEARCH_ONLY · 2026-10-22 · preregistration `PREREGISTRATION.md` (+ Amendment 1) committed before any unexposed-season result (commit `82fdcd1`, 2026-10-22T18:58:26Z). Data: MoneyPuck team-game rows and official NHL results for seasons 2015–2025 (`data/history`, pulled by the `history-pull` workflow run 39830851451). 9,781 regular-season games scored (2018–2025). Nothing here changes any production number, price, stake, cap or SIFT contract.

## Bottom line

1. **Pre-registered result:** replacing V1's raw-xG team ratings with ridge-regularised, opponent-adjusted ratings (and, for the second primary challenger, recalibrating the spread of totals and margins from prior games) improves win-probability Brier over production V1 by **−0.0026 [−0.0032, −0.0019]** (`OA_SVA`) and **−0.0028 [−0.0036, −0.0019]** (`OA_SVA_C1`) on the 7,157 *unexposed* games of 2018–2023, favourable in all 6 seasons, under both the game and the date-cluster bootstrap (97.5% level for the primary gate). `OA_SVA_C1` passes every historical promotion gate (**SHADOW_MORE**); `OA_SVA` fails the no-regression gate on totals (**RETAIN_INCUMBENT**).
2. **The interpretation is much weaker than the headline.** A post-run control — V1's *own* ratings with the *same* prior-seasons-only tuning budget (`V1_T`) — captures about two thirds of the gain (−0.0018 [−0.0023, −0.0013]). Opponent adjustment on top of a re-tuned V1 adds **−0.0009 [−0.0016, −0.0002]** (`OA_SVA_C1`) / **−0.0007 [−0.0012, −0.0002]** (`OA_SVA`): statistically detectable, below the pre-declared practical threshold (0.0010). Most of the "improvement" is that V1's fixed shrinkage constants are too strong (tuning picks a 10-game prior in 7 of 8 seasons; V1 uses 20).
3. **On the two most recent seasons (exposed: 2024–25) the gain is small and not distinguishable from zero**: `OA_SVA` −0.0010 [−0.0022, +0.0002], `OA_SVA_C1` −0.0007 [−0.0022, +0.0009]; against `V1_T` it is −0.0004 / 0.0000. Those seasons were inspected before this design was finalised, so they cannot confirm anything either way, but they are the closest to the current NHL and market regime.
4. **Nothing beats the market.** On the 1,312 games of 2025-26 with Kalshi history (T-60 min midpoint): winner Brier — market 0.2442, V1 0.2459 (+0.0017, n.s.), `OA_SVA` 0.2448 (+0.0006, n.s.), `OA_SVA_C1` 0.2452 (+0.0010, n.s.). Totals: market better than every independent model at 6.5 and than V1 at 5.5. Blending the market with any model at weight 0.8 moves the Brier by ≤ 0.0004 (indistinguishable): the model contributes no usable information beyond the price.
5. **No promotion.** Tonight's published projections stay on `DATA_ONLY_V1`. `OA_SVA_C1` is a candidate for a *shadow* arm (zero production risk) so that a genuine prospective record accumulates automatically; it is not promoted.

## Design (what was held identical)

Only the rating component of V1 changes: same simulator (`nhl-sim-1.1`), seeds, home advantage, back-to-back terms, V1's finishing ratio, goalie factor off (no point-in-time starters exist for history). Every prediction uses MoneyPuck rows dated strictly before the game date. Hyper-parameters (half-life, ridge, season discount) are chosen **per test season from the two prior seasons only** by Poisson goals log-likelihood; no test season is used to choose anything for itself. `SlopeCalibrator` (the `_C1` arms) fits the slopes of the sum and difference of the two rates on the arm's own *earlier* predictions (burn-in 300 games; same-day games never inform each other). Tests: `tests/test_oa_model.py` (planted-effect recovery, schedule-strength separation, no-lookahead poisoning test, calibrator), `tests/test_promotion.py`.

Tiers (fixed in the preregistration): **unexposed** 2018–2023 (2019 pandemic-shortened and 2020 no-crowd kept and reported as different regimes); **exposed** 2024–2025 (prior V1/V2 research inspected them; this study's first look also did).

## Results

### Win probability and distributions, paired vs production V1 (negative = better)

| tier | arm | Brier(win) | RPS(total goals) | Brier(OT) | RPS(margin) |
|---|---|---:|---:|---:|---:|
| unexposed 2018–23 (n=7,157) | `V1_T` control (tuned V1) | −0.0018 [−0.0023, −0.0013] | **+0.0039 worse** | 0.0000 | −0.0073 [−0.0092, −0.0053] |
| | `OA_SVA` | **−0.0026** [−0.0032, −0.0019] | +0.0016 [−0.0006, +0.0038] | +0.0001 | −0.0104 [−0.0132, −0.0076] |
| | `OA_SVA_C1` | **−0.0028** [−0.0036, −0.0019] | +0.0003 [−0.0015, +0.0023] | +0.0002 | −0.0111 [−0.0148, −0.0074] |
| | `V1_C1` (calibration only) | −0.0013 [−0.0019, −0.0008] | +0.0002 | +0.0001 | −0.0051 [−0.0074, −0.0029] |
| exposed 2024–25 (n=2,624) | `OA_SVA` | −0.0010 [−0.0022, +0.0002] | **+0.0041 worse** [+0.0006, +0.0078] | 0.0000 | −0.0040 [−0.0088, +0.0012] |
| | `OA_SVA_C1` | −0.0007 [−0.0022, +0.0009] | −0.0016 [−0.0042, +0.0011] | +0.0001 | −0.0033 [−0.0094, +0.0035] |

Win-probability Brier of `OA_SVA_C1` against production V1 by season: 2018 −0.0011, 2019 −0.0010, 2020 −0.0028, 2021 −0.0041, 2022 −0.0043, 2023 −0.0030 | 2024 −0.0008, 2025 −0.0007 (per-season intervals in `data/oa_tiers.md`; most include zero individually). Calibration (ECE, unexposed): V1 0.0284, `OA_SVA_C1` 0.0156.

Overtime probability is not improved by better ratings (Δ ≈ 0): that defect is in the simulator's tie/OT shape, not in team strength (see V2 below). Total-goal forecasts are not improved by better ratings either; raw opponent-adjusted ratings *add* spread to totals that carries no signal, which is why the second primary challenger recalibrates the sum.

### Attribution control (post-run, interpretive only)

`V1_T` = V1 ratings with half-life (games), shrinkage prior (games) and home-ice multiplier chosen per season from the two prior seasons (`v1_tuned_control.py`). Chosen values: prior = 10 games in 7 of 8 seasons (grid minimum), half-life 20–80, home 1.03–1.06. `OA_SVA_C1` vs `V1_T`: unexposed −0.0009 [−0.0016, −0.0002]; exposed 0.0000 [−0.0012, +0.0012]. Totals: `V1_T` is itself worse on total-goal RPS (it also over-spreads totals).

### Against the market (2025-26 only; Kalshi candle-close midpoint at T-60 min; no depth, fee or slippage)

| target | n | market Brier | V1 | OA_SVA | OA_SVA_C1 | model+market (w=0.8) |
|---|---:|---:|---|---|---|---|
| home win | 1,312 | 0.2442 | +0.0017 n.s. | +0.0006 n.s. | +0.0010 n.s. | −0.0002 … −0.0003 n.s. |
| total over 5.5 | 1,196 | 0.2419 | +0.0025 market better | +0.0025 n.s. | +0.0019 n.s. | +0.0001 … +0.0003 n.s. |
| total over 6.5 | 1,194 | 0.2466 | +0.0035 market better | +0.0034 market better | +0.0025 market better | +0.0003 … +0.0004 n.s. |

(puck-line rows in `data/oa_market.md`.) **Question 1** (accuracy): yes — all arms beat a league-average model on win probability and margin. **Question 2** (beat the market as a benchmark): no, not on any target; the best independent model is within noise of the midpoint on the winner and behind it on totals. **Question 3** (overcome spread, fees and slippage): not addressable — there is no midpoint edge to begin with, and executable asks cost 4–5 cents more than the midpoint (earlier audit).

### V1 weaknesses re-tested on all 9,781 games (`v1_diagnostics.py`)

| claim | 2018–23 (7,157) | 2024–25 (2,624) | verdict |
|---|---|---|---|
| overtime under-predicted | 17.5% vs 22.0% realised, gap −4.6 pts [−5.5, −3.6] | 17.4% vs 22.8%, gap −5.3 pts [−6.9, −3.7] | **confirmed**, every season |
| large margins (|margin| ≥ 3) under-predicted | 34.6% vs 39.9%, −5.4 pts [−6.5, −4.2] | 34.7% vs 39.6%, −4.9 pts [−6.7, −3.0] | **confirmed** |
| total-goal distribution too narrow | z² = 0.905 [0.875, 0.937] (too *wide*) | z² = 0.913 [0.865, 0.966] | **rejected** (slightly too wide) |
| V1 totals no better than league average | V1 better: RPS −0.0081 [−0.0120, −0.0040] | −0.0001 [−0.0059, +0.0065] | **true only for 2024–25** |
| home advantage | predicted 54.4% vs 53.4% realised | 54.5% vs 54.2% | V1 slightly high in 2018–23 (2020–21 no-crowd) |

### V2's overtime fix, replicated (`walk_forward_v2`, hazards fitted on earlier seasons only)

`nhl-sim-2.0` on V1's own rates (`SIM2`): overtime Brier **−0.0022 [−0.0032, −0.0011]** pooled over 2023–2025 (3,936 games; 2023 alone, unexposed: −0.0015 [−0.0033, +0.0002]); predicted OT 21.2% vs 22.1% realised (V1: 17.4%); win −0.0002 [−0.0005, +0.0001], totals +0.0003 (n.s.) — no material regression. The full V2 (`SIM2_ST`, special-teams rates) is no better on OT and slightly worse on 2023 totals (+0.0010 [+0.00005, +0.0020] at 5.5). Only one of the three seasons is unexposed and the hazard fit needs shots from 2021, so a 3-unexposed-season gate cannot yet be met; V2 is already running in live shadow.

## Leakage and data-lineage notes

* **Point-in-time by construction, tested:** all rating fits use rows with `date < game date` (poisoning test in `test_oa_model.py`); hyper-parameters and calibrator slopes use only earlier seasons / earlier games.
* **Retrospective vendor data:** MoneyPuck xG values for past games are as published today (the xG model is refit retroactively), not as available on the day. This is the main unquantified lineage risk of every historical result here.
* **No historical starting goalies** (the live model's goalie term is off in every arm) and no historical lineup/injury timestamps; results say nothing about those features.
* **Selection:** the exposed-season look informed Amendment 1 (grid, exploratory C1 arms, two primaries). The control arm was added after the preregistered run. Both are disclosed above and in the preregistration.
* **Multiple comparisons:** two primary challengers → primary gate at 97.5%; everything else exploratory.

## What this does and does not justify

Justifies: shadowing `OA_SVA_C1` prospectively (cost ≈ 1 ms/slate, deterministic); re-examining V1's shrinkage constants (a re-tuned V1 is the cheapest way to capture most of the historical gain, but it also over-spreads totals unless recalibrated); fixing the overtime/margin shape via the V2 simulator.

Does not justify: changing any published projection tonight; any claim of beating the market; any betting expression. At a 0.001 Brier scale and ~1,300 games per season, individual seasons cannot resolve these differences — which is exactly why the multi-season pooled and the prospective shadow evidence matter more than any single-season table.

Artifacts: `data/` (per-game tables, pmfs, hyper-parameter grids in `oa_meta.json`, tier and control JSON). Reproduce: `python -m nhl_edge.research.oa_walk_forward --history data/history --out OUT --test-seasons 2018,...,2025 --workers 4 && python -m nhl_edge.research.oa_evaluate tiers --dir OUT && python -m nhl_edge.research.v1_tuned_control --games OUT/oa_games.csv --out OUT && python -m nhl_edge.research.oa_market --dir OUT && python -m nhl_edge.research.v1_diagnostics OUT`.
