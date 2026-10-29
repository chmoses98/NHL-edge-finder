# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-29T05:33:25Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +21.82 | +6.74 | +11.44 | 0.567 | -75.60 | -98.28 | 36.94 |
| B thesis-diversified (joint) ← optimiser card | 62.92 | +7.41 | +2.51 | +10.53 | 0.650 | -27.76 | -36.43 | 22.11 |
| C best expression per thesis | 45.12 | +5.85 | +2.06 | +10.54 | 0.584 | -18.64 | -31.45 | 18.17 |
| R FUNDED research stakes | 20.00 | +2.67 | +0.90 | +1.78 | 0.625 | -9.46 | -12.03 | 0.00 |

## WPG @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WPG_win | p_overtime | goals | shots TBL/WPG | TBL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.68 | 0.32 | 0.00 | 6.01 | 27.0/26.6 | 23.8/22.7 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.118 | 0.73 | 0.27 | 0.00 | 5.99 | 32.5/21.2 | 18.8/27.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.46 | 5.89 | 27.4/26.9 | 23.7/24.1 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.58 | 0.42 | 0.46 | 5.79 | 32.5/21.2 | 18.1/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.70 | 0.30 | 0.00 | 9.3 | 28.6/28.0 | 23.1/21.3 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.068 | 0.75 | 0.25 | 0.00 | 9.16 | 34.0/22.1 | 17.9/26.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_UTA_win | p_overtime | goals | shots PIT/UTA | PIT/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.51 | 0.49 | 0.00 | 6.08 | 27.0/27.1 | 23.4/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.115 | 0.49 | 0.51 | 0.00 | 9.57 | 29.0/29.1 | 22.5/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.48 | 0.52 | 0.48 | 5.99 | 27.2/27.4 | 24.1/23.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.070 | 0.63 | 0.37 | 0.00 | 6.13 | 32.0/21.5 | 18.6/27.7 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.066 | 0.40 | 0.60 | 0.00 | 6.03 | 21.6/31.9 | 27.7/18.6 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.57 | 0.43 | 0.49 | 5.95 | 31.8/21.7 | 18.5/28.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CBJ @ CAR  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CBJ_win | p_overtime | goals | shots CAR/CBJ | CAR/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.150 | 0.68 | 0.32 | 0.00 | 6.02 | 33.7/21.3 | 18.7/29.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.125 | 0.56 | 0.44 | 0.45 | 5.94 | 33.8/21.2 | 18.1/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.59 | 0.41 | 0.00 | 6.04 | 27.6/26.9 | 23.7/23.5 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.094 | 0.69 | 0.31 | 0.00 | 9.17 | 35.3/22.4 | 18.0/27.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.51 | 0.49 | 0.46 | 5.95 | 27.8/26.9 | 23.5/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.60 | 0.40 | 0.00 | 9.26 | 29.2/28.4 | 22.9/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 2.5 goals NO | 67 | 0.758 | 0.712 | +0.073 | +0.026 | $20.00 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Columbus wins by over 1.5 goals YES | 16 | 0.212 | 0.183 | +0.042 | +0.014 | $1.66 | FUNDED_RESEARCH | $1 | CBJ:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Columbus over 3.5 goals scored YES | 26 | 0.328 | 0.289 | +0.054 | +0.015 | $1.10 | FUNDED_RESEARCH | $1 | CBJ:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT29CBJCAR-CAR2|no; why: higher confidence-adjusted growth (7.04 vs 1.53 bp); despite a smaller raw edge (+0.073 vs +0.079/contract); wins across more scripts (relative breadth 1.021 vs 0.895); relationships: KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes: REINFORCING (phi 0.292); KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ4|yes: REINFORCING (phi 0.327); failure: CAR wins by 2+
- **Columbus wins by over 1.5 goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLSPREAD-26OCT29CBJCAR-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29CBJCAR-CAR3|no has the higher standalone adjusted growth (7.04 vs 3.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.292); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29CBJCAR-CAR3|no: REINFORCING (phi 0.292); KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ4|yes: REINFORCING (phi 0.526); failure: CAR wins (incl. OT/SO)
- **Columbus over 3.5 goals scored YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29CBJCAR-CAR3|no has the higher standalone adjusted growth (7.04 vs 2.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.327); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29CBJCAR-CAR3|no: REINFORCING (phi 0.327); KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes: REINFORCING (phi 0.526); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4248): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29CBJCAR-CAR3|no (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.2117): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29CBJCAR-CAR3|no (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.3173): highest fidelity KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29CBJCAR-CAR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT29CBJCAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3635, phi -0.747)
- KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5878, phi -0.619)
- KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CBJ:SUPPRESSED (p 0.4642, phi -0.65)

portfolios: A EV +7.38 (adj +1.94) on $50.00, P(profit) 0.6616, adj growth 10.3 bp · B EV +2.76 (adj +0.96) on $22.76, P(profit) 0.7585, adj growth 8.5 bp · C EV +2.13 (adj +0.77) on $20.00, P(profit) 0.7585, adj growth 6.9 bp · R EV +0.98 (adj +0.33) on $7.00, P(profit) 0.7585, adj growth 10.7 bp

## CHI @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_CHI_win | p_overtime | goals | shots DET/CHI | DET/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.139 | 0.71 | 0.29 | 0.00 | 6.01 | 33.1/21.1 | 18.5/28.3 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.122 | 0.55 | 0.45 | 0.49 | 5.91 | 33.5/21.5 | 18.4/30.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.62 | 0.38 | 0.00 | 6.02 | 27.5/26.8 | 23.7/23.4 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.091 | 0.72 | 0.28 | 0.00 | 9.21 | 34.8/22.5 | 18.2/26.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.53 | 0.47 | 0.52 | 5.91 | 27.6/26.8 | 23.4/24.4 | even strength |
| DET shot control · low event (<=4) · decided (2+) | 0.072 | 0.66 | 0.34 | 0.00 | 3.47 | 31.6/20.0 | 18.6/29.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.14, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_BOS_win | p_overtime | goals | shots STL/BOS | STL/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 6.07 | 27.3/27.0 | 23.7/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.47 | 5.99 | 27.6/27.2 | 23.9/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.55 | 0.45 | 0.00 | 9.41 | 29.0/28.8 | 23.0/22.3 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.090 | 0.59 | 0.41 | 0.00 | 6.02 | 32.2/21.6 | 18.5/28.2 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.54 | 0.46 | 0.50 | 5.88 | 32.4/21.7 | 18.5/29.0 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.065 | 0.66 | 0.34 | 0.00 | 9.41 | 34.1/22.9 | 18.1/26.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_WSH_win | p_overtime | goals | shots NSH/WSH | NSH/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.50 | 0.50 | 0.00 | 6.03 | 28.0/28.0 | 24.4/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.54 | 0.46 | 0.44 | 5.92 | 28.1/28.1 | 24.9/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.50 | 0.50 | 0.00 | 9.33 | 29.6/29.6 | 23.4/23.2 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.072 | 0.45 | 0.55 | 0.00 | 6.02 | 22.0/32.8 | 29.0/18.7 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.069 | 0.58 | 0.42 | 0.00 | 6.0 | 32.7/22.4 | 19.4/28.7 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.48 | 0.52 | 0.46 | 5.92 | 22.4/32.8 | 29.6/19.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MTL @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_MTL_win | p_overtime | goals | shots DAL/MTL | DAL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.56 | 0.44 | 0.00 | 6.02 | 26.3/25.8 | 22.7/22.4 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.114 | 0.67 | 0.33 | 0.00 | 5.99 | 31.4/20.4 | 17.7/27.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.58 | 0.42 | 0.47 | 5.86 | 31.7/20.9 | 17.7/28.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.51 | 0.49 | 0.44 | 5.98 | 26.5/26.0 | 22.7/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.59 | 0.41 | 0.00 | 9.23 | 27.9/27.4 | 21.8/21.3 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.074 | 0.66 | 0.34 | 0.00 | 9.18 | 33.1/21.8 | 17.2/25.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.11, DAL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ MIN  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_NYI_win | p_overtime | goals | shots MIN/NYI | MIN/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.57 | 0.43 | 0.00 | 5.99 | 28.1/27.9 | 24.8/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.53 | 0.47 | 0.48 | 5.94 | 28.3/28.1 | 24.7/24.7 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.088 | 0.66 | 0.34 | 0.00 | 5.98 | 33.3/22.4 | 19.6/28.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.57 | 0.43 | 0.00 | 9.26 | 29.8/29.4 | 23.7/23.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.58 | 0.42 | 0.45 | 5.87 | 33.8/22.3 | 19.2/30.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.055 | 0.53 | 0.47 | 0.00 | 3.51 | 27.1/27.0 | 25.2/25.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York I over 2.5 goals scored YES | 49 | 0.565 | 0.525 | +0.057 | +0.017 | $6.50 | FUNDED_RESEARCH | $2 | NYI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 73 | 0.790 | 0.758 | +0.047 | +0.014 | $10.17 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New York I over 2.5 goals scored YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29NYIMIN-MIN3|no; why: higher confidence-adjusted growth (2.65 vs 2.23 bp); relationships: KXNHLSPREAD-26OCT29NYIMIN-MIN3|no: REINFORCING (phi 0.41); failure: NYI offense suppressed (<= 2 goals)
- **Minnesota wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no; why: higher confidence-adjusted growth (2.23 vs 1.59 bp); despite a smaller raw edge (+0.047 vs +0.053/contract); wins across more scripts (relative breadth 1.0 vs 0.895); relationships: KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes: REINFORCING (phi 0.41); failure: MIN wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:OFFENSE_4PLUS (p 0.3337): highest fidelity KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes (same contract)
- thesis GAME:TIGHT (p 0.4451): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29NYIMIN-MIN3|no (same contract)
- KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:SUPPRESSED (p 0.4457, phi -0.979)
- KXNHLSPREAD-26OCT29NYIMIN-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3206, phi -0.75)

portfolios: A EV +4.33 (adj +1.23) on $50.00, P(profit) 0.5292, adj growth 7.3 bp · B EV +1.37 (adj +0.41) on $16.67, P(profit) 0.5292, adj growth 3.6 bp · C EV +1.37 (adj +0.41) on $16.67, P(profit) 0.5292, adj growth 3.6 bp · R EV +0.41 (adj +0.12) on $5.00, P(profit) 0.5292, adj growth 4.3 bp

## BUF @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BUF_win | p_overtime | goals | shots ANA/BUF | ANA/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.58 | 0.42 | 0.00 | 6.04 | 28.1/27.9 | 24.6/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.110 | 0.57 | 0.43 | 0.00 | 9.39 | 29.6/29.5 | 23.7/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.51 | 0.49 | 0.48 | 6.02 | 28.1/28.2 | 24.7/24.8 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.078 | 0.63 | 0.37 | 0.00 | 6.03 | 33.5/22.4 | 19.5/29.3 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.49 | 5.94 | 33.5/22.7 | 19.4/30.2 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.065 | 0.66 | 0.34 | 0.00 | 9.32 | 34.7/23.5 | 18.6/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anaheim wins by over 1.5 goals YES | 25 | 0.336 | 0.290 | +0.073 | +0.027 | $4.87 | FUNDED_RESEARCH | $2 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 2.5 goals YES | 16 | 0.227 | 0.191 | +0.057 | +0.021 | $2.00 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | DIRECT (0.67) | EVIDENCE_MIXED | D |
| Buffalo wins by over 1.5 goals NO | 67 | 0.752 | 0.706 | +0.066 | +0.020 | $2.54 | FUNDED_RESEARCH | $1 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 2.5 goals NO | 78 | 0.849 | 0.809 | +0.057 | +0.017 | $14.08 | FUNDED_RESEARCH | $4 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT29BUFANA-ANA3|yes; why: higher confidence-adjusted growth (8.42 vs 7.10 bp); relationships: KXNHLSPREAD-26OCT29BUFANA-ANA3|yes: DUPLICATIVE (phi 0.761); KXNHLSPREAD-26OCT29BUFANA-BUF2|no: DUPLICATIVE (phi 0.409); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: DUPLICATIVE (phi 0.301); failure: BUF wins (incl. OT/SO)
- **Anaheim wins by over 2.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (8.42 vs 7.10 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.761); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: DUPLICATIVE (phi 0.761); KXNHLSPREAD-26OCT29BUFANA-BUF2|no: DUPLICATIVE (phi 0.311); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: REINFORCING (phi 0.229); failure: BUF wins (incl. OT/SO)
- **Buffalo wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (8.42 vs 4.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.409); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: DUPLICATIVE (phi 0.409); KXNHLSPREAD-26OCT29BUFANA-ANA3|yes: DUPLICATIVE (phi 0.311); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: DUPLICATIVE (phi 0.735); failure: BUF wins by 2+
- **Buffalo wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (8.42 vs 4.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.301); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: DUPLICATIVE (phi 0.301); KXNHLSPREAD-26OCT29BUFANA-ANA3|yes: REINFORCING (phi 0.229); KXNHLSPREAD-26OCT29BUFANA-BUF2|no: DUPLICATIVE (phi 0.735); failure: BUF wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis ANA:WINS_BY_2PLUS (p 0.3361): highest fidelity KXNHLSPREAD-26OCT29BUFANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes (same contract)
- thesis ANA:WINS (p 0.5487): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3936): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4513, phi -0.645)
- KXNHLSPREAD-26OCT29BUFANA-ANA3|yes: FUNDED_RESEARCH; family MIXED; loses 33% of the draws where the thesis happens; opposing: failure thesis BUF:WINS (p 0.4513, phi -0.491)
- KXNHLSPREAD-26OCT29BUFANA-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2482, phi -1.0)
- KXNHLSPREAD-26OCT29BUFANA-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2482, phi -0.735)

portfolios: A EV +10.12 (adj +3.57) on $50.00, P(profit) 0.3361, adj growth 19.3 bp · B EV +3.28 (adj +1.14) on $23.49, P(profit) 0.3361, adj growth 10.0 bp · C EV +2.34 (adj +0.88) on $8.45, P(profit) 0.3361, adj growth 7.7 bp · R EV +1.28 (adj +0.45) on $8.00, P(profit) 0.3361, adj growth 14.4 bp

## OTT @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_OTT_win | p_overtime | goals | shots LAK/OTT | LAK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.58 | 0.42 | 0.00 | 6.01 | 26.9/26.9 | 23.8/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.53 | 0.47 | 0.45 | 5.9 | 26.9/27.1 | 23.9/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.57 | 0.43 | 0.00 | 9.21 | 28.7/28.8 | 23.3/22.2 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.080 | 0.53 | 0.47 | 0.00 | 5.97 | 21.6/32.0 | 28.5/18.2 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.51 | 0.49 | 0.46 | 5.83 | 21.4/32.2 | 28.9/18.2 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.063 | 0.51 | 0.49 | 0.48 | 2.82 | 25.4/25.3 | 23.8/23.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_VAN_win | p_overtime | goals | shots SJS/VAN | SJS/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.61 | 0.39 | 0.00 | 6.04 | 27.7/27.3 | 24.1/23.8 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.105 | 0.65 | 0.35 | 0.00 | 6.09 | 33.2/21.7 | 18.8/28.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.54 | 0.46 | 0.47 | 5.95 | 27.6/27.1 | 23.9/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.59 | 0.41 | 0.00 | 9.38 | 29.3/28.7 | 23.2/22.4 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.54 | 0.46 | 0.46 | 6.01 | 33.1/21.7 | 18.5/29.7 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.090 | 0.71 | 0.29 | 0.00 | 9.43 | 35.2/23.1 | 18.4/26.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
