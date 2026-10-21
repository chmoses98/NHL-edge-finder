# NHL SIFT historical market audit - executive report

> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `385fda9c45633413`.

## Bottom line

**With the archive that exists, there is no repeatable, executable, statistically defensible betting advantage in the NHL Kalshi markets, and the existing projection engines add no demonstrated value over the market price.** That is a finding about
a 151-game sample and a mature, fee-heavy market; it is not proof that no edge exists anywhere. The honest default for the betting engine is PASS, and the infrastructure built here is what would let a real edge be recognised, prospectively, if one appears.

## What the data actually is

* 151 independent final games (2026-09-29..2026-10-20), 35,992 game-scoped contracts, 26,868 settled contracts with a usable pregame quote, 2,870 board ticks. The "thousands of captures"
  are repeated looks at the same games; the archive branch has 16,769 files, 14,214 of them in the hash-verified ledger (not ~18,000).
* A second, separate tier: 1,312 regular-season games of 2025-26 Kalshi candle history (moneyline / total / puck line, no depth).
* Order-book depth exists for 4 of 14 market families; Kalshi's own settlement is absent for live contracts.

## Answers to the success questions

**A. Which families are most efficiently priced?** Moneylines: net ROI of buying either side at T-60m is -4.3% / -4.3%, i.e. exactly the spread plus fee, with no statistically significant directional, home or favourite bias. Full-game totals and puck lines are
calibrated to within about 2-3 points. Brier improves toward puck drop (price discovery).

**B. Persistent, executable inefficiencies?** None found. Of 16 preregistered hypotheses: 11 INCONCLUSIVE, 1 PROMISING, 4 REJECTED. **VALIDATED: 0.** Before fees the best live full-game strategy is about +1 point and the rest are at or below zero (HIST: all negative); after the taker fee essentially all are negative; liquidity is not the constraint (50-200 contract orders fill fully for ~0.1c).

**C. Matchup factors beyond the market?** None. Opponent-adjusted xG, rest, back-to-backs, travel, finishing and special teams all fail out of sample (every hold-out interval includes zero; the one in-sample signal, away back-to-back |z|~2.4, worsens hold-out log loss).

**D. Which projection engines are useful?** None demonstrably. The model's point estimate is worse than the market in nearly every comparison (nominally significant in 9 of 24, uncorrected and overlapping, Brier gaps of at most a few thousandths) and significantly better in none; 0 families show a significant incremental-information coefficient.

**E. Signals surviving chronological out-of-sample testing?** None. The one pattern suggested by the history (early-season Overs, +10.9% on 39 games) failed its first real out-of-sample test (-4.3% on 140 live games).

**F. How to choose among expression types?** The framework (EXPRESSION_ENGINE_SPEC.md) ranks every contract on both sides by lower-bound net EV and script resilience, de-duplicates correlated risk, and gives the model weight only to the extent its incremental information has been shown. Today that weight is ~0, so it
PASSes all 151 games. Ignoring the evidence ("naive EV") bets in 150 of 151 games, claims +10.5% per contract and realises -7.5% (95% CI [-19.2%, +4.2%]).

**G. Maximum acceptable price?** Each card carries it: the price at which the LOWER probability bound just covers price + fee. With the probability anchored on the market it is below the current ask in every case.

**H. Uncertainty and correlation?** Both enter selection: a 2.5-point calibration floor, widening with V1/V2 disagreement; one position per risk factor (a total Under and a team-total Under are one bet).

**I. Evidence to exceed research stakes?** RISK_MANAGEMENT_FRAMEWORK.md: a frozen strategy, positive net ROI after +1c slippage on the prospective tier at predeclared looks (150/300/450 games), calibration no worse than the market, executability from captured depth, a confirming later window, and explicit approval.
Detecting a +3% edge needs hundreds to thousands of independent games depending on price; only a much larger edge could qualify within a season.

**J. Minimal-intervention operation?** A resumable, idempotent pipeline, a daily scorecard with CRITICAL/WARN alarms and a one-line-per-day evidence ledger, shipped as a manual-dispatch workflow (schedule commented out).

## The existing workflows, measured

* Thesis workflow (research selections, scored once per logical bet at first-selection price): first-chosen -5.8% over 135 games (1393 bets), first-funded -9.1%; it does not beat comparable candidates it rejected, and its claimed EV does not predict realised ROI.
* Routed wagers (34 wagers, real fills, reported separately): staked 1012, net -187.64. The market-implied expectation at the fills was -55.85 (fees and spread); the shortfall is -0.6 standard deviations - indistinguishable from fair-price trading.
* **October 20**: the ledger shows two wins and two losses, not four losses (net -27.29). See OCT20_CASE_STUDY.md.

## Limitations

151 games / ~3 weeks of one season; no live Kalshi settlement or trades; depth for four families; the history tier has no depth; HIST was inspected descriptively before registration (only LIVE could validate); starting-goalie and news timing are untestable; CRPS not computed; sample sizes cannot detect edges under roughly 5-10%.

## Implemented, tested, and gated

Code `src/nhl_edge/market_audit/` (26 modules), tests `tests/test_market_audit_*.py`, workflow `market_audit.yml` (manual only). No production path imports any of it. See IMPLEMENTATION_ROADMAP.md for decisions that need approval.
