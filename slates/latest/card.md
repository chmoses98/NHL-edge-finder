# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-29T07:47:02Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 132.73 | +16.47 | +4.46 | +9.31 | 0.606 | -65.84 | -86.01 | 23.66 |
| B thesis-diversified (joint) ← optimiser card | 40.80 | +4.66 | +1.33 | +5.54 | 0.651 | -19.86 | -26.98 | 11.62 |
| C best expression per thesis | 37.27 | +3.96 | +1.16 | +3.38 | 0.699 | -22.61 | -25.53 | 10.18 |
| R FUNDED research stakes | 13.00 | +1.61 | +0.46 | +1.15 | 0.570 | -6.74 | -8.72 | 0.00 |

## WPG @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WPG_win | p_overtime | goals | shots TBL/WPG | TBL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.69 | 0.31 | 0.00 | 6.03 | 27.0/26.5 | 23.7/22.7 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.118 | 0.73 | 0.27 | 0.00 | 5.98 | 32.4/21.1 | 18.7/27.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.53 | 0.47 | 0.45 | 5.88 | 27.3/26.8 | 23.5/24.0 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.57 | 0.43 | 0.47 | 5.81 | 32.6/21.3 | 18.1/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.69 | 0.31 | 0.00 | 9.27 | 28.7/28.2 | 23.1/21.6 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.071 | 0.75 | 0.25 | 0.00 | 9.21 | 34.2/22.2 | 18.0/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 1.5 goals NO | 54 | 0.603 | 0.569 | +0.045 | +0.011 | $6.55 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT29WPGTB-TB3|no; why: higher confidence-adjusted growth (1.15 vs 0.45 bp); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:TIGHT (p 0.4282): highest fidelity KXNHLSPREAD-26OCT29WPGTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29WPGTB-TB2|no (same contract)
- KXNHLSPREAD-26OCT29WPGTB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3975, phi -1.0)

portfolios: A EV +1.62 (adj +0.41) on $20.00, P(profit) 0.6025, adj growth 2.5 bp · B EV +0.53 (adj +0.13) on $6.55, P(profit) 0.6025, adj growth 1.2 bp · C EV +0.53 (adj +0.13) on $6.55, P(profit) 0.6025, adj growth 1.2 bp · R EV +0.16 (adj +0.04) on $2.00, P(profit) 0.6025, adj growth 1.4 bp

## UTA @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_UTA_win | p_overtime | goals | shots PIT/UTA | PIT/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.53 | 0.47 | 0.00 | 6.1 | 27.1/27.1 | 23.6/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.112 | 0.51 | 0.49 | 0.00 | 9.55 | 29.0/29.0 | 22.8/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.49 | 5.97 | 27.4/27.4 | 24.0/24.0 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.070 | 0.61 | 0.39 | 0.00 | 6.09 | 31.9/21.5 | 18.5/27.7 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.068 | 0.39 | 0.61 | 0.00 | 6.02 | 21.7/31.9 | 27.7/18.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.47 | 0.53 | 0.48 | 5.99 | 21.8/32.2 | 28.7/18.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CBJ @ CAR  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CBJ_win | p_overtime | goals | shots CAR/CBJ | CAR/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.152 | 0.68 | 0.32 | 0.00 | 6.04 | 33.6/21.2 | 18.5/28.8 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.127 | 0.55 | 0.45 | 0.45 | 5.91 | 33.9/21.2 | 18.1/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.60 | 0.40 | 0.00 | 6.01 | 27.7/26.8 | 23.6/23.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.097 | 0.68 | 0.32 | 0.00 | 9.18 | 35.3/22.4 | 17.8/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.52 | 0.48 | 0.46 | 5.98 | 27.8/27.1 | 23.8/24.5 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.069 | 0.63 | 0.37 | 0.00 | 3.45 | 32.5/20.1 | 18.7/30.3 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Columbus wins by over 1.5 goals YES | 16 | 0.212 | 0.183 | +0.042 | +0.014 | $3.72 | FUNDED_RESEARCH | $1 | CBJ:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Columbus wins by over 1.5 goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLSPREAD-26OCT29CBJCAR-CAR3|no; why: higher confidence-adjusted growth (3.00 vs 0.91 bp); despite a smaller raw edge (+0.042 vs +0.053/contract); alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: CAR wins (incl. OT/SO)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CBJ:WINS_BY_2PLUS (p 0.2117): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes (same contract)
- KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5878, phi -0.619)

portfolios: A EV +3.18 (adj +1.05) on $12.73, P(profit) 0.2117, adj growth 5.9 bp · B EV +0.93 (adj +0.31) on $3.72, P(profit) 0.2117, adj growth 2.7 bp · C EV +0.93 (adj +0.31) on $3.72, P(profit) 0.2117, adj growth 2.7 bp · R EV +0.25 (adj +0.08) on $1.00, P(profit) 0.2117, adj growth 2.8 bp

## CHI @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_CHI_win | p_overtime | goals | shots DET/CHI | DET/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.139 | 0.69 | 0.31 | 0.00 | 6.0 | 33.1/21.1 | 18.6/28.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.55 | 0.45 | 0.50 | 5.91 | 33.6/21.6 | 18.5/30.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.65 | 0.35 | 0.00 | 6.02 | 27.4/26.7 | 23.8/23.3 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.090 | 0.72 | 0.28 | 0.00 | 9.19 | 34.6/22.2 | 17.8/26.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.52 | 0.48 | 0.50 | 5.9 | 27.5/26.9 | 23.5/24.2 | even strength |
| DET shot control · low event (<=4) · decided (2+) | 0.070 | 0.66 | 0.34 | 0.00 | 3.47 | 31.8/19.8 | 18.4/29.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.14, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_BOS_win | p_overtime | goals | shots STL/BOS | STL/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.53 | 0.47 | 0.00 | 6.05 | 27.1/26.8 | 23.4/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.48 | 5.95 | 27.4/27.3 | 24.0/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.55 | 0.45 | 0.00 | 9.36 | 28.8/28.6 | 22.7/22.6 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.088 | 0.61 | 0.39 | 0.00 | 6.04 | 32.1/21.4 | 18.4/27.8 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.51 | 0.49 | 0.49 | 5.91 | 32.5/21.9 | 18.8/29.2 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.068 | 0.65 | 0.35 | 0.00 | 9.41 | 34.0/23.1 | 18.3/26.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_WSH_win | p_overtime | goals | shots NSH/WSH | NSH/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.51 | 0.49 | 0.00 | 6.02 | 28.0/28.0 | 24.4/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.45 | 5.94 | 28.2/28.0 | 24.7/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.51 | 0.49 | 0.00 | 9.41 | 29.5/29.5 | 23.3/23.0 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.075 | 0.44 | 0.56 | 0.00 | 6.03 | 22.2/32.8 | 28.8/18.9 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.066 | 0.59 | 0.41 | 0.00 | 6.0 | 32.9/22.6 | 19.6/28.8 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.48 | 0.52 | 0.46 | 5.91 | 22.5/33.0 | 29.7/19.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MTL @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_MTL_win | p_overtime | goals | shots DAL/MTL | DAL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.57 | 0.43 | 0.00 | 6.02 | 26.2/25.7 | 22.5/22.3 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.113 | 0.65 | 0.35 | 0.00 | 5.97 | 31.5/20.4 | 17.6/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.46 | 5.96 | 26.5/26.0 | 22.7/23.2 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.56 | 0.44 | 0.45 | 5.88 | 31.8/20.9 | 17.7/28.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.59 | 0.41 | 0.00 | 9.2 | 28.0/27.5 | 22.0/21.4 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.073 | 0.66 | 0.34 | 0.00 | 9.22 | 33.2/22.0 | 17.3/25.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ MIN  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_NYI_win | p_overtime | goals | shots MIN/NYI | MIN/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.58 | 0.42 | 0.00 | 6.0 | 28.3/28.0 | 24.8/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.52 | 0.48 | 0.47 | 5.89 | 28.2/28.0 | 24.7/24.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.086 | 0.63 | 0.37 | 0.00 | 5.98 | 33.3/22.2 | 19.4/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.58 | 0.42 | 0.00 | 9.28 | 29.6/29.4 | 23.8/22.9 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.58 | 0.42 | 0.46 | 5.9 | 33.6/22.5 | 19.5/30.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.055 | 0.53 | 0.47 | 0.00 | 3.51 | 27.0/26.9 | 25.2/24.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Minnesota wins by over 1.5 goals NO | 61 | 0.679 | 0.640 | +0.053 | +0.013 | $3.45 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 73 | 0.790 | 0.755 | +0.047 | +0.011 | $6.19 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I over 2.5 goals scored YES | 49 | 0.565 | 0.520 | +0.057 | +0.012 | $3.62 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Minnesota wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT29NYIMIN-MIN3|no; why: higher confidence-adjusted growth (1.59 vs 1.50 bp); relationships: KXNHLSPREAD-26OCT29NYIMIN-MIN3|no: DUPLICATIVE (phi 0.75); KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes: REINFORCING (phi 0.483); failure: MIN wins by 2+
- **Minnesota wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no has the higher standalone adjusted growth (1.59 vs 1.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.750); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no: DUPLICATIVE (phi 0.75); KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes: REINFORCING (phi 0.41); failure: MIN wins by 2+
- **New York I over 2.5 goals scored YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no has the higher standalone adjusted growth (1.59 vs 1.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.483); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no: REINFORCING (phi 0.483); KXNHLSPREAD-26OCT29NYIMIN-MIN3|no: REINFORCING (phi 0.41); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis GAME:TIGHT (p 0.4451): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29NYIMIN-MIN2|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3337): highest fidelity KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29NYIMIN-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT29NYIMIN-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3206, phi -1.0)
- KXNHLSPREAD-26OCT29NYIMIN-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3206, phi -0.75)
- KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:SUPPRESSED (p 0.4457, phi -0.979)

portfolios: A EV +4.33 (adj +1.01) on $50.00, P(profit) 0.5292, adj growth 5.1 bp · B EV +1.09 (adj +0.26) on $13.25, P(profit) 0.713, adj growth 2.2 bp · C EV +0.77 (adj +0.19) on $9.19, P(profit) 0.6794, adj growth 1.7 bp · R EV +0.32 (adj +0.08) on $4.00, P(profit) 0.713, adj growth 2.6 bp

## BUF @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BUF_win | p_overtime | goals | shots ANA/BUF | ANA/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.57 | 0.43 | 0.00 | 6.02 | 28.3/28.0 | 24.8/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.52 | 0.48 | 0.50 | 5.99 | 28.1/28.2 | 24.8/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.57 | 0.43 | 0.00 | 9.37 | 29.5/29.5 | 23.6/23.0 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.084 | 0.64 | 0.36 | 0.00 | 6.03 | 33.4/22.6 | 19.8/28.9 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.47 | 5.98 | 33.2/22.5 | 19.3/29.9 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.067 | 0.65 | 0.35 | 0.00 | 9.37 | 34.7/23.6 | 18.7/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Buffalo wins by over 1.5 goals NO | 67 | 0.752 | 0.706 | +0.066 | +0.020 | $14.24 | FUNDED_RESEARCH | $4 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 1.5 goals YES | 26 | 0.336 | 0.290 | +0.063 | +0.017 | $1.71 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 2.5 goals YES | 17 | 0.227 | 0.193 | +0.047 | +0.013 | $1.33 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | DIRECT (0.67) | EVIDENCE_MIXED | D |
- **Buffalo wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: higher confidence-adjusted growth (4.25 vs 3.20 bp); wins across more scripts (relative breadth 0.992 vs 0.516); relationships: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: DUPLICATIVE (phi 0.409); KXNHLSPREAD-26OCT29BUFANA-ANA3|yes: DUPLICATIVE (phi 0.311); failure: BUF wins by 2+
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT29BUFANA-BUF2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-BUF2|no has the higher standalone adjusted growth (4.25 vs 3.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.409); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29BUFANA-BUF2|no: DUPLICATIVE (phi 0.409); KXNHLSPREAD-26OCT29BUFANA-ANA3|yes: DUPLICATIVE (phi 0.761); failure: BUF wins (incl. OT/SO)
- **Anaheim wins by over 2.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT29BUFANA-BUF2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-BUF2|no has the higher standalone adjusted growth (4.25 vs 2.69 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.311); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29BUFANA-BUF2|no: DUPLICATIVE (phi 0.311); KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: DUPLICATIVE (phi 0.761); failure: BUF wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis ANA:WINS (p 0.5487): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-BUF2|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.3361): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-BUF2|no (same contract)
- thesis BUF:SUPPRESSED (p 0.3936): highest fidelity KXNHLTEAMTOTAL-26OCT29BUFANA-BUF4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT29BUFANA-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2482, phi -1.0)
- KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4513, phi -0.645)
- KXNHLSPREAD-26OCT29BUFANA-ANA3|yes: FUNDED_RESEARCH; family MIXED; loses 33% of the draws where the thesis happens; opposing: failure thesis BUF:WINS (p 0.4513, phi -0.491)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT29BUFANA-BUF3|no less than the minimum stake; KXNHLSPREAD-26OCT29BUFANA-ANA3|yes kept

portfolios: A EV +7.35 (adj +1.99) on $50.00, P(profit) 0.5903, adj growth 10.1 bp · B EV +2.12 (adj +0.63) on $17.28, P(profit) 0.7518, adj growth 5.5 bp · C EV +1.72 (adj +0.53) on $17.81, P(profit) 0.7518, adj growth 4.7 bp · R EV +0.88 (adj +0.26) on $6.00, P(profit) 0.3361, adj growth 8.0 bp

## OTT @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_OTT_win | p_overtime | goals | shots LAK/OTT | LAK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.57 | 0.43 | 0.00 | 5.98 | 26.9/27.0 | 23.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.55 | 0.45 | 0.46 | 5.93 | 26.8/27.0 | 23.7/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.55 | 0.45 | 0.00 | 9.17 | 28.4/28.8 | 23.3/22.2 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.077 | 0.53 | 0.47 | 0.00 | 5.98 | 21.6/32.2 | 28.7/18.2 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.51 | 0.49 | 0.45 | 5.82 | 21.4/32.3 | 29.0/18.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.49 | 0.51 | 0.48 | 2.8 | 25.4/25.7 | 24.1/23.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_VAN_win | p_overtime | goals | shots SJS/VAN | SJS/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.61 | 0.39 | 0.00 | 6.06 | 27.8/27.4 | 24.2/23.6 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.106 | 0.65 | 0.35 | 0.00 | 6.06 | 33.0/21.7 | 18.8/28.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.60 | 0.40 | 0.00 | 9.4 | 29.4/29.0 | 23.4/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.52 | 0.48 | 0.47 | 5.93 | 27.7/27.3 | 24.0/24.4 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.54 | 0.46 | 0.46 | 5.99 | 33.2/21.8 | 18.7/29.8 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.093 | 0.70 | 0.30 | 0.00 | 9.39 | 34.6/23.0 | 18.4/26.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
