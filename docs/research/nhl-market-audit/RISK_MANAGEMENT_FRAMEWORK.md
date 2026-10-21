# Risk-management framework (Phase I)

> Research-stage. Existing NHL research limits are preserved ($250 nominal research bankroll, $5 maximum research stake). **$75 is a possible future unit, not an authorization.** Nothing here raises a stake, cap or bankroll limit, and no strategy is funded automatically.

## 1. Principles the data forces

* **Friction is the whole game.** Round-trip cost on a mid-priced contract is the half-spread (0.5-2c) plus the taker fee (up to 1.75c): 2-4% of stake. No market family in this archive shows a gap larger than that.
* **Probability is not size.** A higher predicted probability is not a reason for a larger bet; only a *demonstrated, out-of-sample, net-of-cost* edge is, and its size is bounded by its lower confidence limit.
* **Zero exposure is a valid output.** The expected outcome today is PASS.
* **The evidence unit is the independent game,** not the bet, the contract or the snapshot.

## 2. Per-position sizing (if and only if a family is VALIDATED)

`stake = min(research_cap, bankroll * 0.25 * max(0, (p_low - ask) / (1 - ask)))` - quarter-Kelly on the LOWER probability bound, never the point estimate; `research_cap` is the existing $5. With `w = 0` the formula returns 0.

## 3. Aggregate limits (research-stage proposals; all are ceilings, never targets)

| limit | proposal | rationale |
|---|---|---|
| per position | existing $5 research cap | unchanged |
| per game | one position per risk factor, at most 2 positions | correlated scripts (Unders on totals, team totals and periods are one bet) |
| per slate | at most 3% of the nominal research bankroll at risk | a single scoring-environment night moves many Unders together (Oct 20: four Unders, one environment) |
| drawdown halt | stop new research positions after a 10% drawdown of the research bankroll until reviewed | |
| consecutive losses | pause after 6 consecutive settled losses and review calibration | a diagnostic, not a probability statement |
| strategy deterioration | auto-demote a strategy to SHADOW if its prospective net ROI lower 80% bound falls below -10% after 100 games, or if calibration (Brier vs market) is significantly worse | |
| liquidity | no order larger than 25% of visible depth at the touch; no position on a quote with no bid | depth exists for four families only |

## 4. Evidence required to move beyond research stakes

All of the following, on the PROSPECTIVE tier, read only at the predeclared looks (150 / 300 / 450 independent games; alpha spent 0.005 / 0.015 / 0.05, one-sided):

1. A registered, frozen strategy (selector, side, horizon, probability policy) - not edited after its first prospective look.
2. Net ROI after fees and +1c slippage positive, with a one-sided bootstrap p below the spent alpha, game-clustered.
3. At least 300 independent prospective games (power analysis in STRATEGY_ROBUSTNESS.md: a +3% edge needs thousands - so only a materially larger edge can qualify).
4. Calibration not worse than the market's, and no day / team / month concentration (leave-one-out sign stable).
5. Executability evidenced from captured depth (not assumed), including the order sizes proposed.
6. Out-of-sample confirmation on a second, later window after any parameter was fixed.
7. An explicit written approval; the framework itself never promotes or funds anything.

A move from the $5 research cap toward a $75 unit would additionally require the strategy's *lower* 90% ROI bound to exceed the cost of ruin analysis for that unit (a $75 unit is 30% of the nominal $250 research bankroll, which is itself not a sensible Kelly size at any edge this archive could support).

## 5. What this framework would have said about the routed wagers

Of 34 routed wagers, 24 have no thesis-card decision behind them and are larger (mean ~$39 vs ~$8 for the covered ones). Under the proposed limits most would have been blocked at the per-position cap, and the Oct-20 slate (four correlated Unders, $115 at risk) would have been one position. This is a design observation, not a criticism of past decisions; the realised P/L is statistically indistinguishable from paying fees at fair prices.
