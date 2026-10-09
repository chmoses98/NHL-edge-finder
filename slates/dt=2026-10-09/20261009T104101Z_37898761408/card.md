# NHL THESIS CARD — RESEARCH_ONLY — status **NO_BETS**

generated 2026-10-09T10:41:01Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |
| B thesis-diversified (joint) ← optimiser card | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |
| C best expression per thesis | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |
| R FUNDED research stakes | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |

## SEA @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_SEA_win | p_overtime | goals | shots DET/SEA | DET/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.51 | 0.49 | 0.00 | 5.98 | 27.8/27.5 | 24.0/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.49 | 0.51 | 0.46 | 5.96 | 27.9/27.3 | 23.9/24.6 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.107 | 0.58 | 0.42 | 0.00 | 6.0 | 32.9/21.8 | 18.7/28.9 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.59 | 0.41 | 0.48 | 5.9 | 33.2/22.0 | 18.8/29.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.52 | 0.48 | 0.00 | 9.21 | 29.3/28.9 | 23.2/23.0 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.069 | 0.60 | 0.40 | 0.00 | 9.15 | 34.8/23.2 | 18.2/28.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYR @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_NYR_win | p_overtime | goals | shots WSH/NYR | WSH/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.54 | 0.46 | 0.00 | 6.05 | 26.4/26.1 | 22.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.48 | 5.94 | 26.9/26.5 | 23.2/23.5 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.090 | 0.61 | 0.39 | 0.00 | 6.0 | 31.5/21.0 | 18.1/27.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.56 | 0.44 | 0.00 | 9.36 | 28.3/27.9 | 22.3/21.8 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.53 | 0.47 | 0.47 | 5.94 | 31.7/21.1 | 17.9/28.3 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.064 | 0.64 | 0.36 | 0.00 | 9.29 | 33.4/22.8 | 18.0/26.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_PIT_win | p_overtime | goals | shots CBJ/PIT | CBJ/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.60 | 0.40 | 0.00 | 6.01 | 27.5/27.4 | 24.4/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.47 | 5.94 | 27.6/27.7 | 24.4/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.59 | 0.41 | 0.00 | 9.45 | 29.4/29.1 | 23.5/22.4 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.070 | 0.63 | 0.37 | 0.00 | 6.05 | 32.1/21.7 | 18.8/27.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.063 | 0.54 | 0.46 | 0.00 | 6.0 | 21.9/32.0 | 28.5/18.5 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.53 | 0.47 | 0.48 | 5.86 | 32.4/22.1 | 18.9/29.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## ANA @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_ANA_win | p_overtime | goals | shots WPG/ANA | WPG/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.54 | 0.46 | 0.00 | 6.06 | 27.9/28.1 | 24.7/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.49 | 5.94 | 28.1/28.6 | 25.3/24.7 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.096 | 0.48 | 0.52 | 0.00 | 6.0 | 22.2/33.7 | 29.9/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.56 | 0.44 | 0.00 | 9.37 | 29.3/29.9 | 24.1/22.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.50 | 0.50 | 0.48 | 5.91 | 22.4/33.7 | 30.1/19.2 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.064 | 0.47 | 0.53 | 0.00 | 9.31 | 23.7/35.3 | 28.1/18.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
