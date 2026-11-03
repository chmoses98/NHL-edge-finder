# NHL THESIS CARD — RESEARCH_ONLY — status **NO_BETS**

generated 2026-11-03T16:50:22Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |
| B thesis-diversified (joint) ← optimiser card | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |
| C best expression per thesis | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |
| R FUNDED research stakes | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |

## UTA @ TOR  ·  10000 joint draws  ·  456 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_UTA_win | p_overtime | goals | shots TOR/UTA | TOR/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.52 | 0.48 | 0.00 | 6.02 | 28.2/28.8 | 25.3/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.113 | 0.52 | 0.48 | 0.00 | 9.41 | 30.0/30.8 | 24.5/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.54 | 0.46 | 0.46 | 5.99 | 28.4/29.1 | 25.8/24.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.101 | 0.43 | 0.57 | 0.00 | 6.06 | 22.8/34.7 | 30.6/19.7 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.49 | 0.51 | 0.47 | 6.01 | 22.9/34.7 | 31.2/19.4 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.086 | 0.44 | 0.56 | 0.00 | 9.37 | 24.0/36.1 | 28.7/18.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ MTL  ·  10000 joint draws  ·  376 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_WPG_win | p_overtime | goals | shots MTL/WPG | MTL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.62 | 0.38 | 0.00 | 5.97 | 26.9/26.9 | 24.0/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.55 | 0.45 | 0.47 | 5.94 | 27.2/27.0 | 23.8/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.61 | 0.39 | 0.00 | 9.27 | 28.8/28.7 | 23.3/22.2 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.070 | 0.70 | 0.30 | 0.00 | 6.05 | 32.1/21.7 | 19.1/27.7 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.069 | 0.56 | 0.44 | 0.00 | 6.01 | 21.6/31.9 | 28.2/18.0 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.51 | 0.49 | 0.44 | 5.91 | 31.9/21.7 | 18.5/28.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ TBL  ·  10000 joint draws  ·  404 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_DET_win | p_overtime | goals | shots TBL/DET | TBL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.73 | 0.27 | 0.00 | 6.0 | 27.2/27.0 | 24.5/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.47 | 5.86 | 27.2/27.3 | 24.1/23.9 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.097 | 0.76 | 0.24 | 0.00 | 6.01 | 31.9/21.3 | 18.9/27.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.71 | 0.29 | 0.00 | 9.32 | 28.6/28.4 | 23.6/21.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.56 | 0.44 | 0.45 | 5.83 | 32.7/21.8 | 18.7/29.3 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.069 | 0.75 | 0.25 | 0.00 | 9.3 | 34.1/22.9 | 18.8/25.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ NYR  ·  10000 joint draws  ·  398 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_STL_win | p_overtime | goals | shots NYR/STL | NYR/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.54 | 0.46 | 0.00 | 6.03 | 26.7/26.8 | 23.5/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.47 | 5.92 | 26.8/26.7 | 23.5/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.54 | 0.46 | 0.00 | 9.31 | 28.3/28.3 | 22.5/22.0 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.069 | 0.61 | 0.39 | 0.00 | 5.97 | 31.5/21.2 | 18.4/27.2 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.066 | 0.50 | 0.50 | 0.00 | 6.1 | 21.4/31.6 | 27.7/18.1 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.48 | 0.52 | 0.47 | 5.89 | 21.4/31.7 | 28.3/18.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ PHI  ·  10000 joint draws  ·  420 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_MIN_win | p_overtime | goals | shots PHI/MIN | PHI/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.54 | 0.46 | 0.00 | 6.0 | 27.0/27.4 | 24.1/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.53 | 0.47 | 0.47 | 5.86 | 27.1/27.6 | 24.4/23.8 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.50 | 0.50 | 0.48 | 5.84 | 21.9/32.7 | 29.3/18.8 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.086 | 0.48 | 0.52 | 0.00 | 5.96 | 21.5/32.4 | 28.2/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.52 | 0.48 | 0.00 | 9.09 | 28.6/29.1 | 23.3/22.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.55 | 0.45 | 0.00 | 3.51 | 25.6/26.0 | 24.2/23.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ PIT  ·  10000 joint draws  ·  422 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_VGK_win | p_overtime | goals | shots PIT/VGK | PIT/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.52 | 0.48 | 0.00 | 6.03 | 27.2/27.3 | 23.9/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.47 | 5.96 | 27.4/27.4 | 24.1/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.51 | 0.49 | 0.00 | 9.35 | 29.0/29.1 | 23.0/22.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.070 | 0.59 | 0.41 | 0.00 | 5.98 | 32.2/21.5 | 18.5/28.0 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.44 | 5.94 | 32.1/21.7 | 18.6/28.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.064 | 0.46 | 0.54 | 0.00 | 6.0 | 21.6/32.0 | 27.9/18.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ WSH  ·  10000 joint draws  ·  422 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_DAL_win | p_overtime | goals | shots WSH/DAL | WSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.59 | 0.41 | 0.00 | 5.98 | 26.0/26.2 | 23.0/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.49 | 5.92 | 26.1/26.2 | 22.8/22.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.62 | 0.38 | 0.00 | 9.21 | 27.5/27.7 | 22.2/20.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.079 | 0.51 | 0.49 | 0.00 | 6.01 | 20.6/30.6 | 26.9/17.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.48 | 0.52 | 0.46 | 5.84 | 20.9/30.9 | 27.6/17.8 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.064 | 0.64 | 0.36 | 0.00 | 6.01 | 30.9/20.8 | 18.1/26.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ CBJ  ·  10000 joint draws  ·  418 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_COL_win | p_overtime | goals | shots CBJ/COL | CBJ/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.48 | 0.52 | 0.00 | 6.02 | 28.1/28.4 | 24.7/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.49 | 0.51 | 0.47 | 5.98 | 28.2/28.8 | 25.5/24.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.094 | 0.43 | 0.57 | 0.00 | 5.99 | 22.3/33.8 | 29.7/19.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.45 | 0.55 | 0.00 | 9.32 | 29.4/29.8 | 23.3/23.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.45 | 0.55 | 0.49 | 5.9 | 22.6/34.1 | 30.7/19.4 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.066 | 0.38 | 0.62 | 0.00 | 9.23 | 23.5/34.8 | 27.6/18.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ NJD  ·  10000 joint draws  ·  420 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_EDM_win | p_overtime | goals | shots NJD/EDM | NJD/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.51 | 0.49 | 0.00 | 6.05 | 27.9/27.6 | 24.0/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.48 | 0.52 | 0.47 | 5.97 | 28.2/28.0 | 24.6/24.9 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.098 | 0.53 | 0.47 | 0.00 | 6.04 | 33.4/22.1 | 18.9/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.50 | 0.50 | 0.00 | 9.41 | 29.7/29.4 | 23.2/23.5 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.53 | 0.47 | 0.47 | 5.98 | 33.6/22.4 | 19.2/30.3 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.078 | 0.56 | 0.44 | 0.00 | 9.42 | 35.2/23.5 | 17.8/28.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ NSH  ·  10000 joint draws  ·  416 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_CAR_win | p_overtime | goals | shots NSH/CAR | NSH/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.148 | 0.38 | 0.62 | 0.00 | 6.08 | 21.8/34.7 | 30.3/18.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.46 | 0.54 | 0.47 | 5.93 | 21.9/34.4 | 31.0/18.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.112 | 0.37 | 0.63 | 0.00 | 9.36 | 23.1/35.9 | 28.1/18.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.45 | 0.55 | 0.00 | 6.06 | 27.4/28.6 | 24.5/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.50 | 0.50 | 0.48 | 6.02 | 27.7/28.8 | 25.3/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.43 | 0.57 | 0.00 | 9.46 | 28.9/30.0 | 23.3/23.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, CAR shot control · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## ANA @ VAN  ·  10000 joint draws  ·  390 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_ANA_win | p_overtime | goals | shots VAN/ANA | VAN/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.126 | 0.40 | 0.60 | 0.00 | 6.06 | 21.5/33.5 | 29.3/18.4 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.112 | 0.39 | 0.61 | 0.00 | 9.42 | 23.3/35.5 | 28.0/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.46 | 0.54 | 0.00 | 9.54 | 28.9/29.9 | 23.3/22.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.49 | 0.51 | 0.00 | 6.07 | 27.0/27.6 | 24.2/23.4 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.49 | 0.51 | 0.48 | 6.0 | 21.8/33.7 | 30.2/18.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.51 | 0.49 | 0.47 | 6.05 | 27.4/28.3 | 24.9/24.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, ANA shot control · high event (8+) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
