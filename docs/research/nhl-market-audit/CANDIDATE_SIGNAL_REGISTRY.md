# Candidate-signal registry (Phase F)

> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `385fda9c45633413`.

The registry (`market_audit/hypotheses.py`, version `nhl-hypotheses-1.0`) was committed BEFORE the live-tier tests were run (git `627b5fa7`, 2026-10-21T17:13:05Z). One decision horizon (T-60 min), selectors, sides, statistic,
the multiple-comparison correction and the evidence classes were fixed in advance. Each registered test was run **once** on the LIVE tier; the LIVE tier is now closed (games that start after the freeze belong to a separate
PROSPECTIVE tier read only at predeclared looks of 150 / 300 / 450 games).

Tiers: HIST_DISC = first 60% of 2025-26 regular-season games (787 games), HIST_HOLD = last 40% (525), LIVE = 2026-09-29..10-20 (151). Statistic: net ROI
buying the selected side at the displayed ask with the taker fee; game-clustered bootstrap (4,000 resamples). `q` = Benjamini-Hochberg adjusted one-sided p over the LIVE family.

**Disclosure.** Before registration the full 2025-26 season was inspected descriptively (calibration by band, by line, by month). HIST tiers are therefore not clean for hypotheses that look suggested (M6). Only LIVE can validate.

## Result classes

INCONCLUSIVE: 11, PROMISING: 1, REJECTED: 4. **VALIDATED: 0.** The smallest LIVE q-value is 0.976.

## Every registered test, every tier (including failures)

| id | hypothesis | tier | games | contracts | net ROI | 95% CI | gap | ROI at +1c slippage | q (LIVE) | class |
|---|---|---|---|---|---|---|---|---|---|---|
| M1 | Full-game Under | HIST_DISC | 673 | 1417 | -9.0% | [-15.6%, -2.4%] | -1.8% | -10.6% |  |  |
| M1 | Full-game Under | HIST_HOLD | 525 | 1125 | -4.8% | [-12.6%, +3.1%] | -0.1% | -6.6% |  |  |
| M1 | Full-game Under | LIVE | 151 | 320 | -5.4% | [-19.4%, +9.1%] | -0.6% | -7.2% | 0.976 | REJECTED |
| M2 | Full-game Over | HIST_DISC | 673 | 1417 | -2.3% | [-9.0%, +4.3%] | +1.8% | -4.1% |  |  |
| M2 | Full-game Over | HIST_HOLD | 525 | 1125 | -4.3% | [-11.9%, +3.2%] | +0.1% | -6.1% |  |  |
| M2 | Full-game Over | LIVE | 151 | 320 | -3.1% | [-17.3%, +10.6%] | +0.6% | -4.9% | 0.976 | INCONCLUSIVE |
| M3 | Fade longshots | HIST_DISC | 643 | 880 | -4.6% | [-7.6%, -1.7%] | -0.9% | -5.6% |  |  |
| M3 | Fade longshots | HIST_HOLD | 524 | 1410 | -3.2% | [-5.5%, -0.9%] | -1.1% | -4.2% |  |  |
| M3 | Fade longshots | LIVE | 151 | 910 | -0.6% | [-4.0%, +2.7%] | +0.9% | -1.6% | 0.976 | REJECTED |
| M4 | Back favourites | HIST_DISC | 655 | 873 | -3.9% | [-7.1%, -0.9%] | +0.2% | -4.9% |  |  |
| M4 | Back favourites | HIST_HOLD | 522 | 1048 | -0.8% | [-3.3%, +1.6%] | +1.8% | -1.7% |  |  |
| M4 | Back favourites | LIVE | 151 | 627 | +0.6% | [-2.8%, +3.6%] | +1.8% | -0.2% | 0.976 | INCONCLUSIVE |
| M5 | Fade alternate-spread YES | HIST_DISC | 673 | 1334 | -3.8% | [-6.0%, -1.5%] | +0.1% | -4.8% |  |  |
| M5 | Fade alternate-spread YES | HIST_HOLD | 524 | 1025 | -2.0% | [-4.6%, +0.5%] | +0.4% | -3.2% |  |  |
| M5 | Fade alternate-spread YES | LIVE | 151 | 302 | -3.1% | [-7.9%, +1.6%] | -1.0% | -4.2% | 0.976 | REJECTED |
| M6 | Early-season Overs | HIST_DISC | 39 | 147 | +10.9% | [-11.1%, +32.7%] | +12.1% | +9.0% |  |  |
| M6 | Early-season Overs | HIST_HOLD | 0 | 0 | n/a |  |  |  |  |  |
| M6 | Early-season Overs | LIVE | 140 | 544 | -4.3% | [-16.5%, +8.1%] | -0.1% | -6.2% | 0.976 | INCONCLUSIVE |
| M7 | Team-total Under | LIVE | 151 | 571 | -3.3% | [-11.5%, +5.1%] | +0.6% | -5.1% | 0.976 | INCONCLUSIVE |
| M8 | Team-total Over | LIVE | 151 | 571 | -5.8% | [-14.4%, +2.7%] | -0.6% | -7.5% | 0.976 | INCONCLUSIVE |
| M9 | Period-total Under | LIVE | 151 | 695 | -8.0% | [-16.0%, -0.1%] | -1.3% | -9.7% | 0.976 | REJECTED |
| M10 | Period-total Over | LIVE | 151 | 695 | -3.1% | [-11.1%, +4.7%] | +1.3% | -4.9% | 0.976 | INCONCLUSIVE |
| M11 | Late-move continuation | HIST_DISC | 345 | 531 | -1.2% | [-11.4%, +9.2%] | +1.7% | -3.0% |  |  |
| M11 | Late-move continuation | HIST_HOLD | 226 | 356 | -4.4% | [-17.1%, +8.0%] | -0.2% | -6.1% |  |  |
| M11 | Late-move continuation | LIVE | 61 | 94 | +12.9% | [-9.0%, +34.6%] | +9.7% | +11.0% | 0.976 | INCONCLUSIVE |
| M12 | Late-move reversal | HIST_DISC | 345 | 531 | -7.8% | [-18.4%, +2.9%] | -1.7% | -9.5% |  |  |
| M12 | Late-move reversal | HIST_HOLD | 226 | 356 | -4.0% | [-18.0%, +10.0%] | +0.2% | -5.9% |  |  |
| M12 | Late-move reversal | LIVE | 61 | 94 | -25.9% | [-52.7%, +2.0%] | -9.7% | -27.4% | 0.976 | INCONCLUSIVE |
| M13 | Overtime NO | LIVE | 140 | 140 | -4.1% | [-12.9%, +4.0%] | -1.4% | -5.2% | 0.976 | INCONCLUSIVE |
| M14 | Early-goal Under | LIVE | 151 | 151 | +0.1% | [-17.7%, +17.8%] | +2.8% | -2.1% | 0.976 | PROMISING |
| C1 | V1 disagreement | HIST_DISC | 555 | 1674 | -0.5% | [-6.2%, +5.3%] | +2.8% | -2.3% |  |  |
| C1 | V1 disagreement | HIST_HOLD | 317 | 962 | -6.5% | [-15.9%, +2.8%] | -0.8% | -8.5% |  |  |
| C1 | V1 disagreement | LIVE | 109 | 864 | -5.6% | [-18.7%, +7.7%] | -0.5% | -7.5% | 0.976 | INCONCLUSIVE |
| C2 | V2 disagreement | HIST_DISC | 549 | 1681 | +0.2% | [-5.2%, +6.0%] | +3.1% | -1.6% |  |  |
| C2 | V2 disagreement | HIST_HOLD | 326 | 959 | -3.0% | [-12.5%, +6.7%] | +0.8% | -5.0% |  |  |
| C2 | V2 disagreement | LIVE | 105 | 977 | -9.5% | [-23.5%, +4.5%] | -2.1% | -11.5% | 0.976 | INCONCLUSIVE |

## Reading the classes honestly

* Classes are mechanical. **M14 is labelled PROMISING only because its ROI is +0.1% on its single testable tier** (95% CI roughly +/-18%, p about 0.5, negative after 1c slippage). The preregistered rule ("net ROI > 0 on every
  testable tier") is too lenient for single-tier hypotheses; this is reported as a defect of the rule, not quietly redefined. Registry v1.1 should require the lower 90% bound to be positive for PROMISING.
* **M6 (early-season Overs)** was suggested by October 2025 (positive on 39 games) and was NOT confirmed on the 2026 archive. A post-hoc pattern failing its first real out-of-sample test is the expected outcome of selection.
* **M1 (Unders)** has negative net ROI in all three tiers (HIST_DISC -9.0%, HIST_HOLD -4.8%, LIVE -5.4%); it is REJECTED because the HIST_DISC upper bound is below zero.
* Classes: INCONCLUSIVE: M2, M4, M6, M7, M8, M10, M11, M12, M13, C1, C2; PROMISING: M14; REJECTED: M1, M3, M5, M9.
* Model-disagreement strategies (C1, C2) have negative net ROI on the hold-out and LIVE tiers.
* **Nothing is VALIDATED.** On the 151 LIVE games the standard error of a strategy's net ROI ranges from 1.6 points (high-priced contracts, low variance) to 14.0 points (small samples or even-money bets); a validated claim needs a positive lower 90% bound AND a BH q at most 0.10 AND a positive HIST_HOLD ROI, and no strategy came close.
  (All LIVE q-values are 0.976 or close because most one-sided p-values are near 1.)

Hypotheses that cannot be tested with this archive (UNTESTABLE, no data): goalie-confirmation repricing (no timestamp of when the starter became public), opponent-adjusted offensive mismatches at the player level, line-combination changes, injury news
repricing, multi-expression agreement. They are listed in the roadmap with the data each would need.
