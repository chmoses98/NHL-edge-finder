# NHL THESIS CARD — RESEARCH_ONLY — status **NO_BETS**

generated 2026-10-29T23:19:50Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |
| B thesis-diversified (joint) ← optimiser card | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |
| C best expression per thesis | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |
| R FUNDED research stakes | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |

## CHI @ DET  ·  10000 joint draws  ·  428 bet sides mapped, 0 +EV candidates, 0 on card

sportsbook moneyline consensus (5 books): home 0.586 / away 0.414

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_CHI_win | p_overtime | goals | shots DET/CHI | DET/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.138 | 0.70 | 0.30 | 0.00 | 5.99 | 33.2/21.0 | 18.5/28.5 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.126 | 0.55 | 0.45 | 0.50 | 5.93 | 33.4/21.4 | 18.2/30.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.64 | 0.36 | 0.00 | 5.99 | 27.3/26.6 | 23.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.52 | 0.48 | 0.46 | 5.88 | 27.7/26.8 | 23.6/24.5 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.083 | 0.73 | 0.27 | 0.00 | 9.21 | 34.8/22.5 | 18.2/26.7 | even strength |
| DET shot control · low event (<=4) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 3.44 | 31.5/19.9 | 18.6/29.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.14, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ STL  ·  10000 joint draws  ·  462 bet sides mapped, 0 +EV candidates, 0 on card

sportsbook moneyline consensus (5 books): home 0.508 / away 0.492

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_BOS_win | p_overtime | goals | shots STL/BOS | STL/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.54 | 0.46 | 0.00 | 5.98 | 27.2/26.9 | 23.5/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.49 | 0.51 | 0.47 | 5.97 | 27.3/27.1 | 23.7/24.0 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.089 | 0.61 | 0.39 | 0.00 | 5.98 | 32.3/21.5 | 18.6/28.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.51 | 0.49 | 0.00 | 9.35 | 29.0/28.6 | 22.7/22.5 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.55 | 0.45 | 0.45 | 5.92 | 32.5/21.6 | 18.4/29.2 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.061 | 0.63 | 0.37 | 0.00 | 9.29 | 34.1/23.0 | 18.0/26.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ NSH  ·  10000 joint draws  ·  428 bet sides mapped, 0 +EV candidates, 0 on card

sportsbook moneyline consensus (5 books): home 0.503 / away 0.497

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_WSH_win | p_overtime | goals | shots NSH/WSH | NSH/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.58 | 0.42 | 0.00 | 6.07 | 27.9/28.0 | 24.6/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.49 | 5.93 | 28.0/28.2 | 25.0/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.58 | 0.42 | 0.00 | 9.38 | 29.6/29.7 | 23.8/22.9 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.071 | 0.52 | 0.48 | 0.00 | 5.99 | 22.2/32.8 | 29.5/18.5 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.065 | 0.64 | 0.36 | 0.00 | 6.02 | 33.0/22.4 | 19.6/28.6 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.49 | 0.51 | 0.49 | 5.94 | 22.6/33.0 | 29.7/19.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MTL @ DAL  ·  10000 joint draws  ·  422 bet sides mapped, 0 +EV candidates, 0 on card

sportsbook moneyline consensus (5 books): home 0.609 / away 0.391

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_MTL_win | p_overtime | goals | shots DAL/MTL | DAL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DAL shot control · normal event (5-7) · decided (2+) | 0.122 | 0.64 | 0.36 | 0.00 | 5.96 | 31.4/20.3 | 17.5/27.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.55 | 0.45 | 0.00 | 6.0 | 26.4/25.9 | 22.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.46 | 5.9 | 26.7/26.0 | 22.7/23.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.53 | 0.47 | 0.46 | 5.89 | 31.6/20.8 | 17.7/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.58 | 0.42 | 0.00 | 9.28 | 28.1/27.5 | 21.8/21.6 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.068 | 0.66 | 0.34 | 0.00 | 9.21 | 32.9/21.7 | 17.0/25.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts DAL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ MIN  ·  10000 joint draws  ·  448 bet sides mapped, 0 +EV candidates, 0 on card

sportsbook moneyline consensus (5 books): home 0.631 / away 0.369

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_NYI_win | p_overtime | goals | shots MIN/NYI | MIN/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.57 | 0.43 | 0.00 | 5.99 | 28.1/27.8 | 24.5/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.49 | 5.89 | 28.4/28.2 | 25.0/24.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.091 | 0.65 | 0.35 | 0.00 | 5.93 | 33.2/22.2 | 19.5/28.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.60 | 0.40 | 0.00 | 9.29 | 29.5/29.3 | 23.6/23.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.58 | 0.42 | 0.44 | 5.84 | 33.6/22.5 | 19.4/29.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.59 | 0.41 | 0.00 | 3.45 | 26.7/26.5 | 24.8/24.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ ANA  ·  10000 joint draws  ·  450 bet sides mapped, 0 +EV candidates, 0 on card

sportsbook moneyline consensus (5 books): home 0.436 / away 0.564

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BUF_win | p_overtime | goals | shots ANA/BUF | ANA/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.60 | 0.40 | 0.00 | 6.04 | 28.1/27.8 | 24.6/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.52 | 0.48 | 0.46 | 5.96 | 28.4/28.4 | 25.0/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.59 | 0.41 | 0.00 | 9.48 | 30.0/29.8 | 24.2/23.0 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.080 | 0.61 | 0.39 | 0.00 | 6.04 | 33.2/22.1 | 19.3/28.9 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.57 | 0.43 | 0.44 | 5.98 | 33.2/22.6 | 19.5/29.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.065 | 0.63 | 0.37 | 0.00 | 9.38 | 34.9/23.7 | 18.8/27.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ LAK  ·  10000 joint draws  ·  434 bet sides mapped, 0 +EV candidates, 0 on card

sportsbook moneyline consensus (5 books): home 0.474 / away 0.526

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_OTT_win | p_overtime | goals | shots LAK/OTT | LAK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.57 | 0.43 | 0.00 | 5.99 | 27.0/27.3 | 24.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.46 | 5.91 | 26.8/27.1 | 23.8/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.57 | 0.43 | 0.00 | 9.25 | 28.6/28.6 | 22.9/22.4 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.074 | 0.50 | 0.50 | 0.00 | 5.96 | 21.2/31.9 | 28.4/17.9 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.48 | 0.52 | 0.45 | 5.79 | 21.6/32.1 | 28.8/18.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.50 | 0.50 | 0.52 | 2.82 | 25.5/25.6 | 24.1/24.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ SJS  ·  10000 joint draws  ·  420 bet sides mapped, 0 +EV candidates, 0 on card

sportsbook moneyline consensus (5 books): home 0.602 / away 0.398

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_VAN_win | p_overtime | goals | shots SJS/VAN | SJS/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.58 | 0.42 | 0.00 | 6.06 | 27.9/27.3 | 24.2/24.0 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.109 | 0.63 | 0.37 | 0.00 | 6.04 | 33.0/21.7 | 18.9/28.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.57 | 0.43 | 0.00 | 9.42 | 29.6/29.1 | 23.3/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.51 | 0.49 | 0.47 | 6.0 | 27.7/27.4 | 24.2/24.4 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.56 | 0.44 | 0.47 | 5.96 | 33.1/21.7 | 18.5/29.7 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.086 | 0.69 | 0.31 | 0.00 | 9.37 | 34.5/22.9 | 18.1/26.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
