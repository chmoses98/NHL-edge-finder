# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-01T11:37:07Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +26.51 | +6.87 | +25.92 | 0.694 | -38.41 | -55.35 | 56.11 |
| B thesis-diversified (joint) ← card | 129.21 | +19.41 | +5.53 | +19.32 | 0.719 | -25.12 | -37.11 | 49.68 |
| C best expression per thesis | 93.38 | +16.54 | +5.34 | +15.04 | 0.658 | -26.83 | -38.80 | 47.23 |

## PHI @ NJD  ·  10000 joint draws  ·  312 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_PHI_win | p_overtime | goals | shots NJD/PHI | NJD/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.60 | 0.40 | 0.00 | 6.02 | 27.0/26.6 | 23.5/23.1 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.109 | 0.63 | 0.37 | 0.00 | 5.94 | 32.1/21.1 | 18.3/27.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.49 | 0.51 | 0.50 | 5.89 | 26.8/26.5 | 23.2/23.5 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.54 | 0.46 | 0.48 | 5.84 | 32.2/21.1 | 18.1/29.0 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.51 | 0.49 | 0.49 | 2.74 | 25.5/25.2 | 23.7/24.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.55 | 0.45 | 0.00 | 3.4 | 25.6/25.2 | 23.6/23.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Sean Couturier: 1+ goals YES | 11 | 0.151 | 0.136 | +0.034 | +0.019 | $4.78 | PHI:OFFENSE_4PLUS | 0.2455 | EVIDENCE_STRONGER | D |
| Anthony Mantha: 1+ assists NO | 74 | 0.879 | 0.772 | +0.125 | +0.019 | $17.21 | NJD:SUPPRESSED | 0.2292 | EVIDENCE_MIXED | D |
| Nico Hischier: 1+ goals NO | 69 | 0.736 | 0.723 | +0.031 | +0.018 | $12.79 | NJD:SUPPRESSED | 0.2251 | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (7.50 vs 0.42 bp); alternative not eligible: confidence-adjusted EV +0.0052 below the 0.010/contract floor; relationships: KXNHLAST-26OCT01PHINJ-NJAMANTHA39-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT01PHINJ-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense suppressed (<= 2 goals)
- **Anthony Mantha: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01PHINJ-NJNHISCHIER13-1|no; why: higher confidence-adjusted growth (4.18 vs 3.59 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT01PHINJ-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: NJD offense succeeds (4+ goals)
- **Nico Hischier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT01PHINJ-NJ4|no; why: higher confidence-adjusted growth (3.59 vs 0.48 bp); despite a smaller raw edge (+0.031 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.989 vs 0.861); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT01PHINJ-NJAMANTHA39-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: NJD offense succeeds (4+ goals)

portfolios: A EV +4.07 (adj +1.50) on $28.70, P(profit) 0.6993, adj growth 13.1 bp · B EV +4.83 (adj +1.54) on $34.78, P(profit) 0.6993, adj growth 13.7 bp · C EV +2.11 (adj +1.20) on $20.69, P(profit) 0.7753, adj growth 10.4 bp

## TBL @ NYR  ·  10000 joint draws  ·  348 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_TBL_win | p_overtime | goals | shots NYR/TBL | NYR/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.54 | 0.46 | 0.00 | 5.98 | 26.0/26.5 | 23.1/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.54 | 0.46 | 0.47 | 5.95 | 26.2/26.6 | 23.5/23.0 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.102 | 0.46 | 0.54 | 0.00 | 5.98 | 21.0/31.9 | 28.1/17.7 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.46 | 0.54 | 0.51 | 5.89 | 21.0/31.7 | 28.2/17.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.54 | 0.46 | 0.00 | 9.17 | 27.7/28.1 | 22.3/21.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.51 | 0.49 | 0.00 | 3.43 | 24.9/25.1 | 23.2/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| John Carlson: 1+ assists NO | 53 | 0.742 | 0.588 | +0.195 | +0.041 | $20.00 | TBL:SUPPRESSED | 0.2264 | EVIDENCE_MIXED | D |
| Tampa Bay wins NO | 43 | 0.514 | 0.469 | +0.066 | +0.022 | $6.85 | NYR:WINS | 0.237 | EVIDENCE_MIXED | D |
| Victor Hedman: 1+ assists NO | 72 | 0.795 | 0.745 | +0.061 | +0.011 | $8.56 | TBL:SUPPRESSED | 0.2291 | EVIDENCE_MIXED | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT01TBNYR-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (14.55 vs 4.94 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGAME-26OCT01TBNYR-TB|no: REINFORCING (phi 0.153); KXNHLAST-26OCT01TBNYR-TBVHEDMAN77-1|no: MOSTLY_INDEPENDENT (phi 0.036); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLGAME-26OCT01TBNYR-NYR|yes; why: higher confidence-adjusted growth (4.33 vs 2.56 bp); relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: REINFORCING (phi 0.153); KXNHLAST-26OCT01TBNYR-TBVHEDMAN77-1|no: MOSTLY_INDEPENDENT (phi 0.147); failure: TBL wins (incl. OT/SO)
- **Victor Hedman: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no; why: second expression of the same thesis: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no has the higher standalone adjusted growth (14.55 vs 1.32 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.036); they share one thesis budget; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.036); KXNHLGAME-26OCT01TBNYR-TB|no: MOSTLY_INDEPENDENT (phi 0.147); failure: TBL offense succeeds (4+ goals)

portfolios: A EV +8.81 (adj +1.68) on $28.88, P(profit) 0.6925, adj growth 14.5 bp · B EV +8.84 (adj +1.95) on $35.42, P(profit) 0.7421, adj growth 17.5 bp · C EV +8.23 (adj +1.86) on $27.55, P(profit) 0.7421, adj growth 16.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01TBNYR-NYR|yes == KXNHLGAME-26OCT01TBNYR-TB|no

## BUF @ CBJ  ·  10000 joint draws  ·  356 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_BUF_win | p_overtime | goals | shots CBJ/BUF | CBJ/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.59 | 0.41 | 0.00 | 6.04 | 28.3/28.1 | 24.8/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.45 | 5.87 | 28.1/28.0 | 24.7/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 9.33 | 29.9/29.7 | 24.1/23.4 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.081 | 0.63 | 0.37 | 0.00 | 5.98 | 33.1/22.5 | 19.7/28.7 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.54 | 0.46 | 0.49 | 5.83 | 33.1/22.5 | 19.3/29.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.55 | 0.45 | 0.00 | 3.46 | 27.0/27.0 | 25.3/24.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Zach Metsa: 1+ goals NO | 93 | 0.962 | 0.950 | +0.027 | +0.016 | $20.00 | DIFFUSE | 0.2381 | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ assists NO | 59 | 0.666 | 0.618 | +0.059 | +0.011 | $7.26 | BUF:SUPPRESSED | 0.2404 | EVIDENCE_MIXED | D |
- **Zach Metsa: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.048); failure: BUF offense succeeds (4+ goals)
- **Tage Thompson: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT01BUFCBJ-BUF|no; why: higher confidence-adjusted growth (1.16 vs 0.34 bp); alternative not eligible: confidence-adjusted EV +0.0062 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01BUFCBJ-BUFZMETSA73-1|no: MOSTLY_INDEPENDENT (phi 0.048); failure: BUF offense succeeds (4+ goals)

portfolios: A EV +1.47 (adj +0.41) on $23.10, P(profit) 0.6453, adj growth 3.6 bp · B EV +1.30 (adj +0.47) on $27.26, P(profit) 0.6453, adj growth 4.4 bp · C EV +1.30 (adj +0.47) on $27.26, P(profit) 0.6453, adj growth 4.4 bp

## MIN @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_MIN_win | p_overtime | goals | shots NSH/MIN | NSH/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.47 | 0.53 | 0.00 | 6.05 | 29.4/29.4 | 25.6/25.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.48 | 0.52 | 0.47 | 5.96 | 29.3/29.5 | 26.0/26.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.48 | 0.52 | 0.00 | 9.37 | 30.8/31.0 | 24.6/24.7 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.074 | 0.42 | 0.58 | 0.00 | 5.98 | 23.6/34.9 | 30.8/20.5 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.48 | 0.52 | 0.48 | 5.95 | 23.3/34.6 | 31.0/20.2 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.060 | 0.53 | 0.47 | 0.00 | 5.97 | 34.0/23.4 | 20.1/30.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_SEA_win | p_overtime | goals | shots CGY/SEA | CGY/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.51 | 0.49 | 0.00 | 5.97 | 28.4/28.3 | 24.8/24.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.49 | 0.51 | 0.46 | 5.91 | 28.4/28.3 | 25.1/25.1 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.082 | 0.57 | 0.43 | 0.00 | 6.0 | 33.4/22.6 | 19.5/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.50 | 0.50 | 0.00 | 9.21 | 29.8/29.6 | 23.4/23.7 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.56 | 0.44 | 0.48 | 5.88 | 33.6/22.9 | 19.8/30.1 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.058 | 0.43 | 0.57 | 0.00 | 5.9 | 22.7/33.2 | 29.3/19.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_CHI_win | p_overtime | goals | shots UTA/CHI | UTA/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| UTA shot control · normal event (5-7) · decided (2+) | 0.125 | 0.76 | 0.24 | 0.00 | 6.02 | 33.2/21.2 | 18.9/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.71 | 0.29 | 0.00 | 6.01 | 27.3/26.8 | 24.3/22.9 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.099 | 0.77 | 0.23 | 0.00 | 9.35 | 34.7/22.4 | 18.2/26.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.55 | 0.45 | 0.49 | 6.04 | 27.6/26.9 | 23.4/24.2 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.56 | 0.44 | 0.48 | 5.88 | 32.8/21.3 | 18.1/29.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.68 | 0.32 | 0.00 | 9.4 | 29.4/28.8 | 23.6/21.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Full Game: Over 6.5 goals scored YES | 44 | 0.501 | 0.468 | +0.044 | +0.011 | $4.87 | GAME:HIGH_EVENT | 0.3774 | EVIDENCE_MIXED | D |
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT01CHIUTA-10|yes; why: higher confidence-adjusted growth (1.00 vs 0.83 bp); wins across more scripts (relative breadth 0.667 vs 0.313); alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: low-event game (<= 4 goals)

portfolios: A EV +1.10 (adj +0.27) on $11.55, P(profit) 0.5008, adj growth 1.9 bp · B EV +0.46 (adj +0.11) on $4.87, P(profit) 0.5008, adj growth 1.0 bp · C EV +0.46 (adj +0.11) on $4.87, P(profit) 0.5008, adj growth 1.0 bp

## EDM @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_EDM_win | p_overtime | goals | shots VAN/EDM | VAN/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.42 | 0.57 | 0.00 | 6.06 | 27.7/28.4 | 24.5/24.4 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.114 | 0.39 | 0.61 | 0.00 | 6.01 | 22.1/33.9 | 29.7/19.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.48 | 0.52 | 0.43 | 6.0 | 28.0/28.4 | 25.1/24.6 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.41 | 0.59 | 0.46 | 5.96 | 22.5/34.2 | 30.7/19.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.45 | 0.55 | 0.00 | 9.37 | 29.4/30.1 | 23.3/23.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.088 | 0.35 | 0.65 | 0.00 | 9.27 | 23.4/35.7 | 28.2/18.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +4.61 (adj +1.13) on $28.88, P(profit) 0.6624, adj growth 8.6 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +1.41 (adj +0.52) on $3.56, P(profit) 0.1485, adj growth 4.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01EDMVAN-EDM|no == KXNHLGAME-26OCT01EDMVAN-VAN|yes

## FLA @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 8 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_FLA_win | p_overtime | goals | shots SJS/FLA | SJS/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.57 | 0.43 | 0.00 | 6.01 | 27.0/27.0 | 23.8/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.54 | 0.46 | 0.47 | 5.94 | 26.8/27.0 | 23.7/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.61 | 0.39 | 0.00 | 9.38 | 28.3/28.5 | 23.0/21.6 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.079 | 0.54 | 0.46 | 0.00 | 6.02 | 21.3/31.5 | 28.1/17.7 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.47 | 0.53 | 0.50 | 5.93 | 21.5/31.9 | 28.5/18.2 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.060 | 0.67 | 0.33 | 0.00 | 5.97 | 31.3/21.5 | 18.9/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| San Jose wins by over 1.5 goals YES | 24 | 0.334 | 0.284 | +0.081 | +0.032 | $6.88 | SJS:WINS_BY_2PLUS | 0.4038 | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 77 | 0.852 | 0.806 | +0.070 | +0.024 | $20.00 | SJS:WINS | 0.2408 | EVIDENCE_MIXED | D |
- **San Jose wins by over 1.5 goals YES** — thesis: SJS wins by 2+; alternative: KXNHLSPREAD-26OCT01FLASJ-SJ3|yes; why: higher confidence-adjusted growth (11.40 vs 7.87 bp); relationships: KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.295); failure: FLA wins (incl. OT/SO)
- **Florida wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes has the higher standalone adjusted growth (11.40 vs 7.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.295); they share one thesis budget; relationships: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes: REINFORCING (phi 0.295); failure: FLA wins by 2+

portfolios: A EV +6.45 (adj +1.88) on $28.88, P(profit) 0.5527, adj growth 14.4 bp · B EV +3.98 (adj +1.46) on $26.88, P(profit) 0.3336, adj growth 13.1 bp · C EV +3.02 (adj +1.18) on $9.45, P(profit) 0.3336, adj growth 10.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01FLASJ-SJ|yes == KXNHLGAME-26OCT01FLASJ-FLA|no

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
