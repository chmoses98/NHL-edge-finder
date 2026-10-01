# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-01T13:24:26Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +27.30 | +7.24 | +27.79 | 0.682 | -44.29 | -61.77 | 57.65 |
| B thesis-diversified (joint) ← card | 133.77 | +19.94 | +6.70 | +20.55 | 0.674 | -28.59 | -41.03 | 60.20 |
| C best expression per thesis | 65.14 | +13.31 | +3.79 | +8.78 | 0.752 | -31.78 | -33.09 | 33.94 |

## PHI @ NJD  ·  10000 joint draws  ·  316 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_PHI_win | p_overtime | goals | shots NJD/PHI | NJD/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.56 | 0.44 | 0.00 | 5.95 | 26.9/26.5 | 23.3/23.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.109 | 0.66 | 0.34 | 0.00 | 5.97 | 32.3/20.9 | 18.2/27.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.53 | 0.47 | 0.48 | 5.84 | 27.0/26.5 | 23.3/23.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.56 | 0.44 | 0.48 | 5.86 | 32.3/21.2 | 18.1/28.9 | even strength |
| NJD shot control · low event (<=4) · tight (1-goal/OT) | 0.063 | 0.53 | 0.47 | 0.49 | 2.73 | 30.7/19.7 | 18.2/29.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.57 | 0.43 | 0.00 | 3.43 | 25.6/25.3 | 23.6/23.5 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Cody Glass: 1+ goals YES | 12 | 0.159 | 0.146 | +0.032 | +0.018 | $4.94 | NJD:OFFENSE_4PLUS | 0.2611 | EVIDENCE_STRONGER | D |
| Noel Acciari: 1+ goals YES | 9 | 0.120 | 0.110 | +0.024 | +0.014 | $3.60 | PHI:OFFENSE_4PLUS | 0.2504 | EVIDENCE_STRONGER | D |
| Anthony Mantha: 1+ assists NO | 74 | 0.861 | 0.769 | +0.107 | +0.016 | $20.00 | NJD:SUPPRESSED | 0.2291 | EVIDENCE_MIXED | D |
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01PHINJ-NJTMEIER28-1|yes; why: higher confidence-adjusted growth (6.52 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26OCT01PHINJ-NJAMANTHA39-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: NJD offense suppressed (<= 2 goals)
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01PHINJ-NJ2|no; why: higher confidence-adjusted growth (4.96 vs 0.76 bp); despite a smaller raw edge (+0.024 vs +0.039/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26OCT01PHINJ-NJAMANTHA39-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: PHI offense suppressed (<= 2 goals)
- **Anthony Mantha: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT01PHINJ-NJ5|no; why: higher confidence-adjusted growth (2.93 vs 0.85 bp); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: NJD offense succeeds (4+ goals)

portfolios: A EV +4.04 (adj +1.61) on $21.25, P(profit) 0.2624, adj growth 13.9 bp · B EV +4.99 (adj +1.66) on $28.55, P(profit) 0.2624, adj growth 14.5 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TBL @ NYR  ·  10000 joint draws  ·  348 bet sides mapped, 7 +EV candidates, 4 on card


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
| John Carlson: 1+ assists NO | 53 | 0.742 | 0.588 | +0.195 | +0.041 | $15.00 | TBL:SUPPRESSED | 0.2264 | EVIDENCE_MIXED | D |
| Jansen Harkins: 1+ goals NO | 89 | 0.932 | 0.920 | +0.035 | +0.024 | $15.00 | TBL:SUPPRESSED | 0.2253 | EVIDENCE_STRONGER | D |
| Tye Kartye: 1+ goals YES | 10 | 0.135 | 0.124 | +0.029 | +0.018 | $4.06 | NYR:OFFENSE_4PLUS | 0.2751 | EVIDENCE_STRONGER | D |
| Tampa Bay wins NO | 43 | 0.514 | 0.469 | +0.066 | +0.022 | $6.29 | NYR:WINS | 0.237 | EVIDENCE_MIXED | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT01TBNYR-NYR|yes; why: higher confidence-adjusted growth (14.55 vs 4.33 bp); relationships: KXNHLGOAL-26OCT01TBNYR-TBJHARKINS10-1|no: MOSTLY_INDEPENDENT (phi 0.05); KXNHLGOAL-26OCT01TBNYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGAME-26OCT01TBNYR-TB|no: REINFORCING (phi 0.153); failure: TBL offense succeeds (4+ goals)
- **Jansen Harkins: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no; why: second expression of the same thesis: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no has the higher standalone adjusted growth (14.55 vs 13.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.050); they share one thesis budget; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.05); KXNHLGOAL-26OCT01TBNYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGAME-26OCT01TBNYR-TB|no: MOSTLY_INDEPENDENT (phi 0.087); failure: TBL offense succeeds (4+ goals)
- **Tye Kartye: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT01TBNYR-NYR|yes; why: higher confidence-adjusted growth (7.01 vs 4.33 bp); despite a smaller raw edge (+0.029 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT01TBNYR-TBJHARKINS10-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGAME-26OCT01TBNYR-TB|no: MOSTLY_INDEPENDENT (phi 0.137); failure: NYR offense suppressed (<= 2 goals)
- **Tampa Bay wins NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLGAME-26OCT01TBNYR-NYR|yes; why: best adjusted growth among the thesis's expressions; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: REINFORCING (phi 0.153); KXNHLGOAL-26OCT01TBNYR-TBJHARKINS10-1|no: MOSTLY_INDEPENDENT (phi 0.087); KXNHLGOAL-26OCT01TBNYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.137); failure: TBL wins (incl. OT/SO)

portfolios: A EV +8.13 (adj +1.68) on $29.69, P(profit) 0.7373, adj growth 13.8 bp · B EV +7.96 (adj +2.49) on $40.35, P(profit) 0.7485, adj growth 22.6 bp · C EV +7.11 (adj +1.48) on $20.00, P(profit) 0.7421, adj growth 13.5 bp
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
| Zach Metsa: 1+ goals NO | 93 | 0.962 | 0.952 | +0.027 | +0.017 | $20.00 | DIFFUSE | 0.2381 | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ assists NO | 59 | 0.666 | 0.618 | +0.059 | +0.011 | $7.26 | BUF:SUPPRESSED | 0.2404 | EVIDENCE_MIXED | D |
- **Zach Metsa: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.048); failure: BUF offense succeeds (4+ goals)
- **Tage Thompson: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01BUFCBJ-CBJ2|yes; why: higher confidence-adjusted growth (1.16 vs 0.44 bp); wins across more scripts (relative breadth 0.984 vs 0.512); alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01BUFCBJ-BUFZMETSA73-1|no: MOSTLY_INDEPENDENT (phi 0.048); failure: BUF offense succeeds (4+ goals)

portfolios: A EV +1.51 (adj +0.43) on $23.75, P(profit) 0.6453, adj growth 3.9 bp · B EV +1.30 (adj +0.50) on $27.26, P(profit) 0.6453, adj growth 4.7 bp · C EV +1.30 (adj +0.50) on $27.26, P(profit) 0.6453, adj growth 4.7 bp

## MIN @ NSH  ·  10000 joint draws  ·  342 bet sides mapped, 0 +EV candidates, 0 on card


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

## SEA @ CGY  ·  10000 joint draws  ·  396 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_SEA_win | p_overtime | goals | shots CGY/SEA | CGY/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.51 | 0.49 | 0.00 | 5.97 | 28.4/28.3 | 24.8/24.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.49 | 0.51 | 0.46 | 5.91 | 28.4/28.3 | 25.1/25.1 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.082 | 0.57 | 0.43 | 0.00 | 6.0 | 33.4/22.6 | 19.5/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.50 | 0.50 | 0.00 | 9.21 | 29.8/29.6 | 23.4/23.7 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.56 | 0.44 | 0.48 | 5.88 | 33.6/22.9 | 19.8/30.1 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.058 | 0.43 | 0.57 | 0.00 | 5.9 | 22.7/33.2 | 29.3/19.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Adam Klapka: 1+ goals YES | 10 | 0.131 | 0.117 | +0.025 | +0.011 | $2.65 | CGY:OFFENSE_4PLUS | 0.2324 | EVIDENCE_STRONGER | D |
- **Adam Klapka: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT01SEACGY-CGYAKLAPKA43-1|yes; why: higher confidence-adjusted growth (2.54 vs 0.00 bp); despite a smaller raw edge (+0.024 vs +0.061/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: CGY offense suppressed (<= 2 goals)

portfolios: A EV +0.94 (adj +0.40) on $4.07, P(profit) 0.1308, adj growth 3.2 bp · B EV +0.61 (adj +0.26) on $2.65, P(profit) 0.1308, adj growth 2.3 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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

portfolios: A EV +1.13 (adj +0.28) on $11.87, P(profit) 0.5008, adj growth 1.9 bp · B EV +0.46 (adj +0.11) on $4.87, P(profit) 0.5008, adj growth 1.0 bp · C EV +0.46 (adj +0.11) on $4.87, P(profit) 0.5008, adj growth 1.0 bp

## EDM @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_EDM_win | p_overtime | goals | shots VAN/EDM | VAN/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.42 | 0.57 | 0.00 | 6.06 | 27.7/28.4 | 24.5/24.4 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.114 | 0.39 | 0.61 | 0.00 | 6.01 | 22.1/33.9 | 29.7/19.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.48 | 0.52 | 0.43 | 6.0 | 28.0/28.4 | 25.1/24.6 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.41 | 0.59 | 0.46 | 5.96 | 22.5/34.2 | 30.7/19.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.45 | 0.55 | 0.00 | 9.37 | 29.4/30.1 | 23.3/23.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.088 | 0.35 | 0.65 | 0.00 | 9.27 | 23.4/35.7 | 28.2/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Vancouver wins by over 2.5 goals YES | 10 | 0.148 | 0.122 | +0.042 | +0.015 | $1.23 | VAN:WINS_BY_2PLUS | 0.4525 | EVIDENCE_MIXED | D |
| Edmonton over 4.5 goals scored NO | 66 | 0.733 | 0.691 | +0.057 | +0.016 | $1.09 | VAN:WINS | 0.2724 | EVIDENCE_MIXED | D |
- **Vancouver wins by over 2.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT01EDMVAN-VAN2|yes; why: higher confidence-adjusted growth (5.42 vs 3.87 bp); despite a smaller raw edge (+0.042 vs +0.049/contract); relationships: KXNHLTEAMTOTAL-26OCT01EDMVAN-EDM5|no: REINFORCING (phi 0.236); failure: EDM wins (incl. OT/SO)
- **Edmonton over 4.5 goals scored NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes has the higher standalone adjusted growth (5.42 vs 2.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.236); they share one thesis budget; relationships: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes: REINFORCING (phi 0.236); failure: EDM offense succeeds (4+ goals)

portfolios: A EV +5.08 (adj +0.96) on $29.69, P(profit) 0.6624, adj growth 6.7 bp · B EV +0.58 (adj +0.20) on $2.32, P(profit) 0.1485, adj growth 1.9 bp · C EV +1.41 (adj +0.52) on $3.56, P(profit) 0.1485, adj growth 4.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01EDMVAN-EDM|no == KXNHLGAME-26OCT01EDMVAN-VAN|yes

## FLA @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 8 +EV candidates, 3 on card


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
| San Jose wins by over 1.5 goals YES | 24 | 0.334 | 0.284 | +0.081 | +0.032 | $6.68 | SJS:WINS_BY_2PLUS | 0.4038 | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 77 | 0.852 | 0.806 | +0.070 | +0.024 | $20.00 | SJS:WINS | 0.2408 | EVIDENCE_MIXED | D |
| San Jose over 2.5 goals scored YES | 59 | 0.671 | 0.628 | +0.064 | +0.021 | $1.10 | SJS:OFFENSE_4PLUS | 0.2662 | EVIDENCE_MIXED | D |
- **San Jose wins by over 1.5 goals YES** — thesis: SJS wins by 2+; alternative: KXNHLSPREAD-26OCT01FLASJ-SJ3|yes; why: higher confidence-adjusted growth (11.40 vs 7.87 bp); relationships: KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.295); KXNHLTEAMTOTAL-26OCT01FLASJ-SJ3|yes: DUPLICATIVE (phi 0.459); failure: FLA wins (incl. OT/SO)
- **Florida wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes has the higher standalone adjusted growth (11.40 vs 7.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.295); they share one thesis budget; relationships: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes: REINFORCING (phi 0.295); KXNHLTEAMTOTAL-26OCT01FLASJ-SJ3|yes: REINFORCING (phi 0.403); failure: FLA wins by 2+
- **San Jose over 2.5 goals scored YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes has the higher standalone adjusted growth (11.40 vs 4.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.459); they share one thesis budget; relationships: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes: DUPLICATIVE (phi 0.459); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.403); failure: SJS offense suppressed (<= 2 goals)

portfolios: A EV +6.46 (adj +1.88) on $29.69, P(profit) 0.5527, adj growth 14.2 bp · B EV +4.04 (adj +1.48) on $27.77, P(profit) 0.3336, adj growth 13.2 bp · C EV +3.02 (adj +1.18) on $9.45, P(profit) 0.3336, adj growth 10.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01FLASJ-SJ|yes == KXNHLGAME-26OCT01FLASJ-FLA|no

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
