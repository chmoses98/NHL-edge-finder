# Market-expression engine specification (Phase G)

> SHADOW ONLY, DISABLED BY DEFAULT. `market_audit/expression_engine.py` is a pure module, imported by no production path, with no I/O, no clock and no network. It places no wager, changes no stake or cap, and activates no model.

## What it does, in the order the brief asks

For one game at a decision instant:

1. **Game assessment** - opponent-adjusted context (goalies, rest, back-to-back, expected goals) read from the existing thesis-card inputs.
2. **Scripts and their probabilities** - the existing seven-script forecast (`script_forecasts`).
3. **Eligible expressions** - every Kalshi contract on both sides across winner, puck line, totals, team totals, period markets, overtime, first-10-minutes and supported props (goal-scorer families are modelled but never recommended).
4. **Evaluation across scripts** - `script_survival.mass_survived` from the thesis layer: the share of script probability mass in which the expression stays +EV at its executable price.
5. **Probability and range** - below.
6. **Executable price, fee, friction** - the displayed ask (or a book-walked VWAP where depth was captured), the quadratic taker fee, slippage stress.
7. **Fragility / correlation penalties** - script survival below 50%, thin visible depth (<25 contracts), and one-position-per-risk-factor (a LOW_SCORING Under and a team-total Under are the same bet).
8. **Rank and reject** - eligible expressions ranked by `survival x lower-bound net EV`; everything else carries its explicit reject reasons.
9. **Card** - or PASS.

It does not default to team totals or Unders: ranking uses only lower-bound net EV and robustness, and the candidate set is symmetric (every contract, both sides).

## The probability policy (what the evidence supports)

```
p_hat = mid + w * (p_model - mid)          w = max(0, c - 1.28 * se(c))   -- c from market_audit.model_audit (HIST tier)
se^2  = 0.025^2 + (0.5 |p_V1 - p_V2|)^2 + (w |p_model - mid|)^2
p_low = p_hat - 1.28 * se            max acceptable entry x:  p_low = x + 0.07 x (1-x)
```

Every audited `c` is statistically indistinguishable from zero (or negative), so `w` is 0 (0.005 for the moneyline) and `p_hat` equals the market mid. The market is then the best available estimate, every contract has negative expected value
by exactly half the spread plus the fee, and the engine PASSes. A model earns weight only by demonstrating incremental information out of sample; the weight is then bounded by the lower confidence limit, not the point estimate.

## Card fields (per candidate)

bet name, current price, **maximum acceptable entry price**, estimated probability, uncertainty range, net EV and its lower bound, primary thesis, supporting evidence, main counter-argument, script resilience, correlation warning, research stake
(quarter-Kelly on the LOWER bound, capped by the EXISTING $5 / $250 research limits, zero unless the lower bound is positive), evidence class, eligibility, reject reasons. Zero-bet slates are the normal outcome.

## Evidence gate

A family is eligible only when a registered hypothesis covering it is **VALIDATED** (CANDIDATE_SIGNAL_REGISTRY.md). Today none is, so the strict policy returns PASS for all 151 archived games.
Two counterfactual policies exist only to measure the cost of ignoring evidence: `research_unvalidated` (gate waived, w = 0.5, uncertainty kept) - also PASS for every game - and `naive_ev` (w = 1, uncertainty ignored), which bets in nearly every game and realises a negative
return against a claimed positive edge (WALK_FORWARD_VALIDATION.md section C).

## What is implemented and tested

* `expression_engine.py` and `run_shadow.py` (replay over the archive); `tests/test_market_audit_engine.py` covers: the fee equals the router-verified formula, max entry price is the break-even, strict PASS without a validated family, zero model weight => probability = market,
  goal-scorer never recommended, correlated expressions not double-counted, fragile / thin candidates rejected, stake zero without a positive lower bound and capped by the existing limit, BH adjustment, classification rules, game-clustered resampling.
* NOT implemented: wiring into RUN NHL, the thesis card, or the SIFT contract. That needs an explicit decision (ROADMAP.md).
