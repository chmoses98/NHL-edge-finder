# NHL THESIS CARD — RESEARCH_ONLY — status **NO_BETS**

generated 2026-10-16T10:28:13Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +7.47 | +1.91 | -11.22 | 0.407 | -50.00 | -50.00 | 0.40 |
| B thesis-diversified (joint) ← optimiser card | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |
| C best expression per thesis | 2.31 | +0.88 | +0.25 | -2.31 | 0.132 | -2.31 | -2.31 | 2.16 |
| R FUNDED research stakes | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |

## PIT @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_PIT_win | p_overtime | goals | shots COL/PIT | COL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.118 | 0.72 | 0.28 | 0.00 | 6.05 | 34.1/22.2 | 19.6/29.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.65 | 0.35 | 0.00 | 6.06 | 28.6/27.9 | 25.0/24.4 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.103 | 0.75 | 0.25 | 0.00 | 9.42 | 35.7/23.6 | 19.2/27.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.47 | 6.01 | 28.6/28.0 | 24.7/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.67 | 0.33 | 0.00 | 9.39 | 30.3/29.4 | 24.2/22.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.57 | 0.43 | 0.47 | 5.97 | 34.2/22.3 | 19.2/30.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BOS_win | p_overtime | goals | shots ANA/BOS | ANA/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.122 | 0.58 | 0.42 | 0.00 | 6.04 | 34.0/22.1 | 18.9/29.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.53 | 0.47 | 0.00 | 6.09 | 28.8/28.2 | 24.8/24.9 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.54 | 0.46 | 0.48 | 5.98 | 34.5/22.3 | 19.1/31.1 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.099 | 0.61 | 0.39 | 0.00 | 9.38 | 35.9/23.7 | 18.5/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.53 | 0.47 | 0.00 | 9.52 | 30.5/29.6 | 23.6/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.51 | 0.49 | 0.48 | 5.98 | 28.5/27.8 | 24.5/25.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:HIGH_EVENT (p 0.3311): highest fidelity KXNHLTOTAL-26OCT16BOSANA-8|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT16BOSANA-8|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4615): highest fidelity KXNHLTOTAL-26OCT16BOSANA-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT16BOSANA-8|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order

portfolios: A EV +7.47 (adj +1.91) on $50.00, P(profit) 0.4069, adj growth 0.4 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.88 (adj +0.25) on $2.31, P(profit) 0.1321, adj growth 2.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
