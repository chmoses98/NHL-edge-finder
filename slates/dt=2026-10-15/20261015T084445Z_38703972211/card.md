# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-15T08:44:45Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 140.00 | +25.96 | +5.01 | +29.23 | 0.659 | -75.35 | -82.39 | 26.64 |
| B thesis-diversified (joint) ← optimiser card | 47.93 | +7.90 | +2.09 | +14.89 | 0.697 | -19.17 | -27.71 | 18.43 |
| C best expression per thesis | 46.01 | +7.78 | +2.06 | +17.14 | 0.585 | -17.24 | -29.49 | 18.21 |
| R FUNDED research stakes | 14.00 | +2.30 | +0.60 | +2.85 | 0.697 | -6.81 | -6.81 | 0.00 |

## BUF @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_BUF_win | p_overtime | goals | shots TOR/BUF | TOR/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.54 | 0.46 | 0.00 | 6.03 | 28.2/28.9 | 25.4/24.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.117 | 0.48 | 0.52 | 0.00 | 6.02 | 22.6/34.2 | 30.5/19.2 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.49 | 0.51 | 0.46 | 5.98 | 22.4/34.1 | 30.6/19.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.54 | 0.46 | 0.50 | 6.01 | 27.9/28.6 | 25.3/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.56 | 0.44 | 0.00 | 9.33 | 29.3/29.9 | 23.9/22.7 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.083 | 0.47 | 0.53 | 0.00 | 9.24 | 23.7/36.2 | 29.3/18.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.12, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NYI_win | p_overtime | goals | shots OTT/NYI | OTT/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.62 | 0.38 | 0.00 | 6.01 | 26.8/26.8 | 23.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.54 | 0.46 | 0.48 | 5.93 | 27.0/26.7 | 23.6/23.6 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.087 | 0.65 | 0.35 | 0.00 | 5.96 | 32.0/21.4 | 18.7/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.61 | 0.39 | 0.00 | 9.27 | 28.3/28.2 | 22.6/21.5 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.56 | 0.44 | 0.46 | 5.88 | 32.0/21.2 | 18.1/28.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.61 | 0.39 | 0.00 | 3.53 | 25.4/25.5 | 23.9/23.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_SEA_win | p_overtime | goals | shots TBL/SEA | TBL/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.131 | 0.65 | 0.35 | 0.00 | 5.98 | 32.7/21.1 | 18.3/28.1 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.57 | 0.43 | 0.47 | 5.94 | 33.2/21.4 | 18.1/29.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.60 | 0.40 | 0.00 | 6.0 | 27.4/26.8 | 23.7/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.51 | 0.49 | 0.43 | 5.9 | 27.5/26.8 | 23.6/24.2 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.081 | 0.69 | 0.30 | 0.00 | 9.07 | 34.6/22.3 | 17.8/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.63 | 0.37 | 0.00 | 9.19 | 29.1/28.4 | 23.1/22.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 2.5 goals NO | 68 | 0.768 | 0.719 | +0.072 | +0.024 | $20.00 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15SEATB-TB2|no; why: higher confidence-adjusted growth (5.79 vs 1.55 bp); despite a smaller raw edge (+0.072 vs +0.089/contract); wins across more scripts (relative breadth 1.009 vs 0.885); relationships: only recommended bet in this game; failure: TBL wins by 2+

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.13, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis GAME:TIGHT (p 0.433): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB3|no (same contract)
- KXNHLSPREAD-26OCT15SEATB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.354, phi -0.743)

portfolios: A EV +5.26 (adj +1.15) on $40.00, P(profit) 0.646, adj growth 7.7 bp · B EV +2.08 (adj +0.68) on $20.00, P(profit) 0.7677, adj growth 6.0 bp · C EV +2.08 (adj +0.68) on $20.00, P(profit) 0.7677, adj growth 6.0 bp · R EV +0.52 (adj +0.17) on $5.00, P(profit) 0.7677, adj growth 6.0 bp

## VAN @ FLA  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_VAN_win | p_overtime | goals | shots FLA/VAN | FLA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.60 | 0.40 | 0.00 | 6.06 | 27.3/26.7 | 23.6/23.3 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.112 | 0.66 | 0.34 | 0.00 | 6.01 | 32.7/21.1 | 18.4/28.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.50 | 0.50 | 0.49 | 5.96 | 27.5/27.0 | 23.6/24.2 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.56 | 0.44 | 0.46 | 5.92 | 32.9/21.2 | 18.0/29.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.60 | 0.40 | 0.00 | 9.32 | 28.8/28.3 | 22.6/22.1 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.086 | 0.67 | 0.33 | 0.00 | 9.17 | 34.3/22.5 | 17.8/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 1.5 goals NO | 50 | 0.652 | 0.550 | +0.134 | +0.032 | $17.62 | FUNDED_RESEARCH | $5 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT15VANFLA-FLA3|no; why: higher confidence-adjusted growth (9.21 vs 4.00 bp); relationships: only recommended bet in this game; failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS (p 0.4271): highest fidelity KXNHLSPREAD-26OCT15VANFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15VANFLA-FLA2|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.2254): highest fidelity KXNHLSPREAD-26OCT15VANFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15VANFLA-FLA2|no (same contract)
- KXNHLSPREAD-26OCT15VANFLA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.7 pts; opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3481, phi -1.0)

portfolios: A EV +14.81 (adj +2.42) on $50.00, P(profit) 0.6519, adj growth 13.1 bp · B EV +4.58 (adj +1.10) on $17.62, P(profit) 0.6519, adj growth 9.7 bp · C EV +4.62 (adj +1.11) on $17.79, P(profit) 0.6519, adj growth 9.8 bp · R EV +1.30 (adj +0.31) on $5.00, P(profit) 0.6519, adj growth 10.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT15VANFLA-VAN|yes == KXNHLGAME-26OCT15VANFLA-FLA|no

## NYR @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_NYR_win | p_overtime | goals | shots NJD/NYR | NJD/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.130 | 0.54 | 0.46 | 0.00 | 5.94 | 33.0/21.2 | 18.2/29.2 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.53 | 0.47 | 0.45 | 5.87 | 33.1/21.1 | 18.0/29.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.49 | 0.51 | 0.00 | 5.98 | 27.3/26.7 | 23.3/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.49 | 0.51 | 0.48 | 5.88 | 27.6/26.9 | 23.6/24.3 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.078 | 0.57 | 0.43 | 0.00 | 9.11 | 34.4/22.1 | 16.9/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.51 | 0.49 | 0.00 | 9.19 | 28.9/28.1 | 22.1/23.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PHI @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_PHI_win | p_overtime | goals | shots DET/PHI | DET/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.50 | 0.50 | 0.00 | 5.95 | 27.5/27.0 | 23.4/23.9 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.113 | 0.54 | 0.46 | 0.00 | 5.94 | 32.7/21.3 | 18.1/29.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.47 | 5.87 | 27.1/26.6 | 23.3/23.9 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.55 | 0.45 | 0.44 | 5.81 | 32.8/21.2 | 18.1/29.3 | even strength |
| DET shot control · low event (<=4) · tight (1-goal/OT) | 0.068 | 0.50 | 0.50 | 0.47 | 2.76 | 31.4/19.9 | 18.5/29.9 | even strength |
| DET shot control · low event (<=4) · decided (2+) | 0.065 | 0.55 | 0.45 | 0.00 | 3.47 | 31.3/20.1 | 18.4/29.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DET shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_WPG_win | p_overtime | goals | shots CHI/WPG | CHI/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.49 | 0.51 | 0.00 | 5.99 | 26.4/26.7 | 23.2/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.48 | 0.52 | 0.49 | 5.9 | 26.5/26.8 | 23.6/23.3 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.092 | 0.41 | 0.59 | 0.00 | 6.0 | 20.9/31.8 | 27.6/18.0 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.46 | 0.54 | 0.47 | 5.87 | 21.1/32.3 | 28.8/17.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.46 | 0.54 | 0.00 | 9.14 | 27.7/28.2 | 22.2/21.9 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.059 | 0.41 | 0.59 | 0.00 | 9.15 | 22.3/33.6 | 26.6/17.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_SJS_win | p_overtime | goals | shots NSH/SJS | NSH/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 6.05 | 27.6/27.7 | 24.5/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.46 | 5.92 | 27.7/27.7 | 24.5/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.56 | 0.44 | 0.00 | 9.37 | 29.1/29.0 | 23.0/22.3 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.073 | 0.57 | 0.43 | 0.00 | 5.98 | 32.5/22.0 | 19.0/28.7 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.067 | 0.50 | 0.50 | 0.00 | 5.97 | 22.1/32.6 | 29.1/18.8 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.54 | 0.46 | 0.48 | 5.97 | 32.9/22.4 | 19.3/29.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ MIN  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_STL_win | p_overtime | goals | shots MIN/STL | MIN/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.56 | 0.44 | 0.00 | 6.06 | 27.8/27.5 | 24.1/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.44 | 5.92 | 27.8/27.6 | 24.1/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.59 | 0.41 | 0.00 | 9.3 | 29.1/28.8 | 23.2/22.5 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.090 | 0.61 | 0.39 | 0.00 | 6.01 | 32.9/22.1 | 19.3/28.6 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.58 | 0.42 | 0.47 | 5.92 | 33.0/22.1 | 19.1/29.6 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.062 | 0.66 | 0.34 | 0.00 | 9.16 | 34.5/23.5 | 18.9/27.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_UTA_win | p_overtime | goals | shots EDM/UTA | EDM/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.65 | 0.35 | 0.00 | 6.06 | 27.4/27.3 | 24.4/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.121 | 0.62 | 0.38 | 0.00 | 9.55 | 29.5/29.3 | 23.6/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.50 | 0.50 | 0.45 | 5.99 | 27.6/27.7 | 24.5/24.2 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.080 | 0.70 | 0.30 | 0.00 | 6.02 | 32.7/22.0 | 19.4/28.2 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.065 | 0.68 | 0.32 | 0.00 | 9.38 | 34.2/23.2 | 18.6/26.2 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.55 | 0.45 | 0.47 | 5.99 | 33.0/22.3 | 19.1/29.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CGY @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_CGY_win | p_overtime | goals | shots VGK/CGY | VGK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.73 | 0.27 | 0.00 | 6.05 | 28.5/27.8 | 25.3/23.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.116 | 0.79 | 0.21 | 0.00 | 6.01 | 33.6/22.0 | 19.8/28.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.55 | 0.45 | 0.44 | 5.83 | 28.4/27.8 | 24.6/25.0 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.57 | 0.43 | 0.47 | 5.89 | 33.9/21.9 | 18.9/30.4 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.079 | 0.81 | 0.19 | 0.00 | 9.33 | 35.5/23.6 | 19.6/26.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.75 | 0.25 | 0.00 | 9.34 | 29.7/29.1 | 24.4/21.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vegas wins by over 1.5 goals NO | 48 | 0.563 | 0.514 | +0.065 | +0.016 | $5.00 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas wins by over 2.5 goals NO | 62 | 0.691 | 0.650 | +0.054 | +0.014 | $2.76 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas over 3.5 goals scored NO | 42 | 0.497 | 0.451 | +0.060 | +0.014 | $2.55 | FUNDED_RESEARCH | $1 | VGK:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vegas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no; why: higher confidence-adjusted growth (2.35 vs 1.83 bp); relationships: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: DUPLICATIVE (phi 0.759); KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK4|no: REINFORCING (phi 0.575); failure: VGK wins by 2+
- **Vegas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no has the higher standalone adjusted growth (2.35 vs 1.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.759); they share one thesis budget; relationships: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: DUPLICATIVE (phi 0.759); KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK4|no: REINFORCING (phi 0.551); failure: VGK wins by 2+
- **Vegas over 3.5 goals scored NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no has the higher standalone adjusted growth (2.35 vs 1.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.575); they share one thesis budget; relationships: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: REINFORCING (phi 0.575); KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: REINFORCING (phi 0.551); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, VGK shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:TIGHT (p 0.4128): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK2|no (same contract)
- thesis VGK:SUPPRESSED (p 0.2982): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT15CGYVGK-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4373, phi -1.0)
- KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4373, phi -0.759)
- KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4949, phi -0.984)

portfolios: A EV +5.89 (adj +1.44) on $50.00, P(profit) 0.6112, adj growth 5.8 bp · B EV +1.24 (adj +0.31) on $10.31, P(profit) 0.5627, adj growth 2.7 bp · C EV +1.08 (adj +0.27) on $8.22, P(profit) 0.5627, adj growth 2.4 bp · R EV +0.48 (adj +0.12) on $4.00, P(profit) 0.5627, adj growth 3.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
