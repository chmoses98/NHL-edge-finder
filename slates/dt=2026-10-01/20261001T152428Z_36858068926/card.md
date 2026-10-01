# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-01T15:24:28Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +28.38 | +8.00 | +27.38 | 0.741 | -25.66 | -38.92 | 71.11 |
| B thesis-diversified (joint) ← card | 150.00 | +26.35 | +10.31 | +24.55 | 0.741 | -21.85 | -34.16 | 95.64 |
| C best expression per thesis | 150.01 | +26.44 | +11.26 | +22.70 | 0.681 | -37.62 | -52.27 | 99.02 |

## PHI @ NJD  ·  10000 joint draws  ·  318 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_PHI_win | p_overtime | goals | shots NJD/PHI | NJD/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.56 | 0.44 | 0.00 | 5.94 | 26.7/26.3 | 23.0/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.47 | 5.94 | 27.3/26.9 | 23.6/23.9 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.107 | 0.66 | 0.34 | 0.00 | 5.93 | 31.7/20.8 | 18.2/27.4 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.53 | 0.47 | 0.46 | 5.81 | 32.3/21.2 | 18.0/29.1 | even strength |
| NJD shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.53 | 0.47 | 0.48 | 2.8 | 30.6/19.8 | 18.3/29.0 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.52 | 0.48 | 0.49 | 2.82 | 25.2/24.9 | 23.5/23.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Sean Couturier: 1+ goals YES | 11 | 0.144 | 0.134 | +0.027 | +0.017 | $2.62 | PHI:OFFENSE_4PLUS | 0.2422 | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 12 | 0.155 | 0.145 | +0.027 | +0.017 | $2.74 | NJD:OFFENSE_4PLUS | 0.2534 | EVIDENCE_STRONGER | D |
| Anthony Mantha: 1+ assists NO | 74 | 0.861 | 0.772 | +0.107 | +0.019 | $11.56 | NJD:SUPPRESSED | 0.2271 | EVIDENCE_MIXED | D |
| Noel Acciari: 1+ goals YES | 9 | 0.115 | 0.108 | +0.020 | +0.012 | $1.80 | PHI:OFFENSE_4PLUS | 0.2428 | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (6.16 vs 2.04 bp); relationships: KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT01PHINJ-NJAMANTHA39-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: PHI offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes; why: higher confidence-adjusted growth (5.87 vs 2.15 bp); relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT01PHINJ-NJAMANTHA39-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NJD offense suppressed (<= 2 goals)
- **Anthony Mantha: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no; why: higher confidence-adjusted growth (4.29 vs 1.69 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: NJD offense succeeds (4+ goals)
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (3.59 vs 2.04 bp); despite a smaller raw edge (+0.020 vs +0.020/contract); relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT01PHINJ-NJAMANTHA39-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: PHI offense suppressed (<= 2 goals)

portfolios: A EV +2.64 (adj +0.75) on $22.45, P(profit) 0.6166, adj growth 7.0 bp · B EV +3.20 (adj +1.28) on $18.73, P(profit) 0.3609, adj growth 11.9 bp · C EV +1.74 (adj +0.98) on $41.86, P(profit) 0.2728, adj growth 8.9 bp

## TBL @ NYR  ·  10000 joint draws  ·  350 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_TBL_win | p_overtime | goals | shots NYR/TBL | NYR/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.57 | 0.43 | 0.00 | 5.97 | 26.2/26.6 | 23.3/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.49 | 5.85 | 26.4/26.7 | 23.4/23.2 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.099 | 0.45 | 0.55 | 0.00 | 5.97 | 20.7/31.8 | 27.9/17.5 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.50 | 0.50 | 0.48 | 5.9 | 20.9/31.7 | 28.4/17.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.59 | 0.41 | 0.00 | 9.18 | 27.6/28.1 | 22.5/21.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.56 | 0.44 | 0.00 | 3.44 | 24.8/25.2 | 23.5/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| John Carlson: 1+ assists NO | 54 | 0.749 | 0.600 | +0.191 | +0.043 | $11.56 | TBL:SUPPRESSED | 0.2274 | EVIDENCE_MIXED | D |
| Tye Kartye: 1+ goals YES | 10 | 0.136 | 0.125 | +0.030 | +0.018 | $2.50 | NYR:OFFENSE_4PLUS | 0.2594 | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 1.5 goals NO | 66 | 0.749 | 0.702 | +0.073 | +0.026 | $6.29 | NYR:WINS | 0.282 | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 78 | 0.849 | 0.812 | +0.057 | +0.020 | $5.66 | NYR:WINS | 0.2487 | EVIDENCE_MIXED | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01TBNYR-TB2|no; why: higher confidence-adjusted growth (16.20 vs 6.94 bp); relationships: KXNHLGOAL-26OCT01TBNYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26OCT01TBNYR-TB2|no: REINFORCING (phi 0.151); KXNHLSPREAD-26OCT01TBNYR-TB3|no: MOSTLY_INDEPENDENT (phi 0.134); failure: TBL offense succeeds (4+ goals)
- **Tye Kartye: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01TBNYR-TB2|no; why: higher confidence-adjusted growth (7.56 vs 6.94 bp); despite a smaller raw edge (+0.030 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26OCT01TBNYR-TB2|no: MOSTLY_INDEPENDENT (phi 0.111); KXNHLSPREAD-26OCT01TBNYR-TB3|no: MOSTLY_INDEPENDENT (phi 0.084); failure: NYR offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01TBNYR-TB3|no; why: higher confidence-adjusted growth (6.94 vs 5.43 bp); relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: REINFORCING (phi 0.151); KXNHLGOAL-26OCT01TBNYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.111); KXNHLSPREAD-26OCT01TBNYR-TB3|no: DUPLICATIVE (phi 0.728); failure: TBL wins by 2+
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01TBNYR-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT01TBNYR-TB2|no has the higher standalone adjusted growth (6.94 vs 5.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.728); they share one thesis budget; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.134); KXNHLGOAL-26OCT01TBNYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.084); KXNHLSPREAD-26OCT01TBNYR-TB2|no: DUPLICATIVE (phi 0.728); failure: TBL wins by 2+

portfolios: A EV +5.79 (adj +1.07) on $22.45, P(profit) 0.568, adj growth 9.7 bp · B EV +5.76 (adj +1.70) on $26.00, P(profit) 0.6933, adj growth 16.0 bp · C EV +8.41 (adj +2.13) on $36.34, P(profit) 0.5893, adj growth 19.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01TBNYR-NYR|yes == KXNHLGAME-26OCT01TBNYR-TB|no

## BUF @ CBJ  ·  10000 joint draws  ·  356 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_BUF_win | p_overtime | goals | shots CBJ/BUF | CBJ/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.57 | 0.43 | 0.00 | 6.01 | 28.0/28.0 | 24.8/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.45 | 5.95 | 28.4/28.3 | 24.9/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.59 | 0.41 | 0.00 | 9.19 | 29.6/29.4 | 24.0/23.0 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.077 | 0.66 | 0.34 | 0.00 | 5.97 | 33.4/22.7 | 19.9/28.9 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.57 | 0.43 | 0.49 | 5.91 | 33.1/22.6 | 19.2/29.8 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.062 | 0.54 | 0.46 | 0.00 | 6.01 | 22.5/32.8 | 29.3/19.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Charlie Coyle: 1+ goals YES | 22 | 0.268 | 0.254 | +0.036 | +0.022 | $3.89 | CBJ:OFFENSE_4PLUS | 0.2444 | EVIDENCE_STRONGER | D |
| Sean Monahan: 1+ goals YES | 20 | 0.243 | 0.229 | +0.032 | +0.017 | $3.03 | CBJ:OFFENSE_4PLUS | 0.2535 | EVIDENCE_STRONGER | D |
| Owen Power: 1+ goals NO | 90 | 0.927 | 0.918 | +0.021 | +0.011 | $11.51 | BUF:SUPPRESSED | 0.237 | EVIDENCE_STRONGER | D |
| Conor Garland: 1+ goals NO | 82 | 0.853 | 0.842 | +0.023 | +0.012 | $10.46 | CBJ:SUPPRESSED | 0.234 | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes; why: higher confidence-adjusted growth (5.78 vs 3.90 bp); relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT01BUFCBJ-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT01BUFCBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: CBJ offense suppressed (<= 2 goals)
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (5.78 vs 3.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT01BUFCBJ-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT01BUFCBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: CBJ offense suppressed (<= 2 goals)
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01BUFCBJ-BUF2|no; why: higher confidence-adjusted growth (3.38 vs 1.67 bp); despite a smaller raw edge (+0.021 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT01BUFCBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: BUF offense succeeds (4+ goals)
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01BUFCBJ-CBJVNICHUSHKIN43-1|no; why: higher confidence-adjusted growth (2.22 vs 0.20 bp); despite a smaller raw edge (+0.023 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0042 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT01BUFCBJ-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: CBJ offense succeeds (4+ goals)

portfolios: A EV +2.38 (adj +0.71) on $22.45, P(profit) 0.538, adj growth 6.2 bp · B EV +1.61 (adj +0.91) on $28.90, P(profit) 0.4088, adj growth 8.5 bp · C EV +1.52 (adj +0.73) on $15.34, P(profit) 0.2684, adj growth 6.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01BUFCBJ-CBJ|yes == KXNHLGAME-26OCT01BUFCBJ-BUF|no

## MIN @ NSH  ·  10000 joint draws  ·  344 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_MIN_win | p_overtime | goals | shots NSH/MIN | NSH/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.134 | 0.45 | 0.55 | 0.00 | 6.08 | 29.4/29.5 | 25.4/25.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.44 | 5.97 | 29.2/29.4 | 26.0/25.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.46 | 0.54 | 0.00 | 9.38 | 30.8/31.0 | 24.4/24.5 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.067 | 0.41 | 0.59 | 0.00 | 6.01 | 23.4/34.6 | 30.5/20.4 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.061 | 0.51 | 0.49 | 0.00 | 6.01 | 34.5/23.5 | 20.2/30.7 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.51 | 0.49 | 0.48 | 5.92 | 23.8/34.7 | 31.0/20.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Ryan Hartman: 1+ goals YES | 23 | 0.271 | 0.257 | +0.029 | +0.015 | $2.72 | MIN:OFFENSE_4PLUS | 0.2646 | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ goals YES | 18 | 0.216 | 0.203 | +0.026 | +0.013 | $2.19 | NSH:OFFENSE_4PLUS | 0.2665 | EVIDENCE_STRONGER | D |
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT01MINNSH-9|yes; why: higher confidence-adjusted growth (2.63 vs 1.05 bp); despite a smaller raw edge (+0.029 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.914 vs 0.377); alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: MIN offense suppressed (<= 2 goals)
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT01MINNSH-9|yes; why: higher confidence-adjusted growth (2.38 vs 1.05 bp); despite a smaller raw edge (+0.026 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.907 vs 0.377); alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: NSH offense suppressed (<= 2 goals)

portfolios: A EV +1.00 (adj +0.51) on $7.87, P(profit) 0.4279, adj growth 4.5 bp · B EV +0.62 (adj +0.32) on $4.91, P(profit) 0.4279, adj growth 2.9 bp · C EV +1.02 (adj +0.52) on $8.09, P(profit) 0.4279, adj growth 4.6 bp

## SEA @ CGY  ·  10000 joint draws  ·  396 bet sides mapped, 3 +EV candidates, 3 on card


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
| Brandon Montour: 1+ goals NO | 84 | 0.893 | 0.876 | +0.043 | +0.026 | $11.56 | SEA:SUPPRESSED | 0.25 | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 10 | 0.133 | 0.123 | +0.027 | +0.017 | $2.62 | SEA:OFFENSE_4PLUS | 0.2506 | EVIDENCE_STRONGER | D |
| Adam Klapka: 1+ goals YES | 10 | 0.131 | 0.121 | +0.025 | +0.014 | $2.18 | CGY:OFFENSE_4PLUS | 0.2324 | EVIDENCE_STRONGER | D |
- **Brandon Montour: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (12.17 vs 0.81 bp); despite a smaller raw edge (+0.043 vs +0.085/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: SEA offense succeeds (4+ goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT01SEACGY-SEAMBENIERS10-1|yes; why: higher confidence-adjusted growth (6.64 vs 0.00 bp); despite a smaller raw edge (+0.027 vs +0.027/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi -0.028); failure: SEA offense suppressed (<= 2 goals)
- **Adam Klapka: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT01SEACGY-CGYAKLAPKA43-1|yes; why: higher confidence-adjusted growth (4.64 vs 0.00 bp); despite a smaller raw edge (+0.024 vs +0.030/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.028); failure: CGY offense suppressed (<= 2 goals)

portfolios: A EV +2.00 (adj +1.23) on $15.40, P(profit) 0.2495, adj growth 11.3 bp · B EV +1.75 (adj +1.08) on $16.36, P(profit) 0.2495, adj growth 10.1 bp · C EV +1.06 (adj +0.68) on $4.23, P(profit) 0.1329, adj growth 5.9 bp

## CHI @ UTA  ·  10000 joint draws  ·  314 bet sides mapped, 2 +EV candidates, 2 on card


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
| Ryan Greene: 1+ goals YES | 12 | 0.170 | 0.155 | +0.043 | +0.028 | $4.19 | CHI:OFFENSE_4PLUS | 0.26 | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 62 | 0.741 | 0.653 | +0.105 | +0.016 | $7.71 | CHI:SUPPRESSED | 0.2554 | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT01CHIUTA-9|yes; why: higher confidence-adjusted growth (14.68 vs 1.11 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.922 vs 0.368); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.018); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01CHIUTA-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (2.49 vs 0.28 bp); alternative not eligible: confidence-adjusted EV +0.0052 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: CHI offense succeeds (4+ goals)

portfolios: A EV +3.31 (adj +1.42) on $14.46, P(profit) 0.17, adj growth 12.7 bp · B EV +2.67 (adj +1.10) on $11.90, P(profit) 0.7882, adj growth 10.2 bp · C EV +4.40 (adj +1.82) on $19.58, P(profit) 0.7882, adj growth 15.8 bp

## EDM @ VAN  ·  10000 joint draws  ·  340 bet sides mapped, 12 +EV candidates, 4 on card


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
| Mattias Ekholm: 1+ goals YES | 9 | 0.121 | 0.112 | +0.025 | +0.016 | $2.42 | EDM:OFFENSE_4PLUS | 0.268 | EVIDENCE_STRONGER | D |
| Drew O'Connor: 1+ goals YES | 17 | 0.213 | 0.200 | +0.034 | +0.020 | $3.36 | VAN:OFFENSE_4PLUS | 0.2334 | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 22 | 0.261 | 0.247 | +0.029 | +0.015 | $2.69 | VAN:OFFENSE_4PLUS | 0.2435 | EVIDENCE_STRONGER | D |
| Leon Draisaitl: 2+ points NO | 55 | 0.742 | 0.583 | +0.175 | +0.016 | $6.97 | EDM:SUPPRESSED | 0.2337 | CALIBRATION_WARNING | D |
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01EDMVAN-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (6.51 vs 0.03 bp); despite a smaller raw edge (+0.025 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0016 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLPTS-26OCT01EDMVAN-EDMLDRAISAITL29-2|no: MOSTLY_INDEPENDENT (phi -0.04); failure: EDM offense suppressed (<= 2 goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes; why: higher confidence-adjusted growth (5.97 vs 5.42 bp); despite a smaller raw edge (+0.034 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.923 vs 0.472); relationships: KXNHLGOAL-26OCT01EDMVAN-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLPTS-26OCT01EDMVAN-EDMLDRAISAITL29-2|no: MOSTLY_INDEPENDENT (phi -0.004); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (5.97 vs 2.69 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT01EDMVAN-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLPTS-26OCT01EDMVAN-EDMLDRAISAITL29-2|no: MOSTLY_INDEPENDENT (phi -0.013); failure: VAN offense suppressed (<= 2 goals)
- **Leon Draisaitl: 2+ points NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes; why: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes has the higher standalone adjusted growth (5.42 vs 2.22 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.164); relationships: KXNHLGOAL-26OCT01EDMVAN-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.04); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: EDM offense succeeds (4+ goals)

portfolios: A EV +5.83 (adj +0.85) on $22.45, P(profit) 0.5925, adj growth 7.0 bp · B EV +3.75 (adj +1.15) on $15.43, P(profit) 0.4412, adj growth 10.6 bp · C EV +2.10 (adj +0.99) on $7.93, P(profit) 0.3105, adj growth 8.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01EDMVAN-EDM|no == KXNHLGAME-26OCT01EDMVAN-VAN|yes

## FLA @ SJS  ·  10000 joint draws  ·  366 bet sides mapped, 16 +EV candidates, 4 on card


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
| Kiefer Sherwood: 1+ goals YES | 15 | 0.224 | 0.201 | +0.065 | +0.042 | $5.78 | SJS:OFFENSE_4PLUS | 0.2695 | EVIDENCE_STRONGER | D |
| San Jose wins by over 1.5 goals YES | 24 | 0.334 | 0.284 | +0.081 | +0.032 | $2.65 | SJS:WINS_BY_2PLUS | 0.4038 | EVIDENCE_MIXED | D |
| Aleksander Barkov: 1+ assists NO | 52 | 0.697 | 0.572 | +0.160 | +0.035 | $9.80 | FLA:SUPPRESSED | 0.2565 | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 77 | 0.852 | 0.806 | +0.070 | +0.024 | $9.53 | SJS:WINS | 0.2408 | EVIDENCE_MIXED | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: higher confidence-adjusted growth (27.70 vs 11.40 bp); despite a smaller raw edge (+0.065 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.895 vs 0.521); relationships: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes: REINFORCING (phi 0.168); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.112); failure: SJS offense suppressed (<= 2 goals)
- **San Jose wins by over 1.5 goals YES** — thesis: SJS wins by 2+; alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: higher confidence-adjusted growth (11.40 vs 7.29 bp); relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: REINFORCING (phi 0.168); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: REINFORCING (phi 0.163); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.295); failure: FLA wins (incl. OT/SO)
- **Aleksander Barkov: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes has the higher standalone adjusted growth (11.40 vs 10.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.163); they share one thesis budget; relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLSPREAD-26OCT01FLASJ-SJ2|yes: REINFORCING (phi 0.163); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.162); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes has the higher standalone adjusted growth (11.40 vs 7.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.295); they share one thesis budget; relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.112); KXNHLSPREAD-26OCT01FLASJ-SJ2|yes: REINFORCING (phi 0.295); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: REINFORCING (phi 0.162); failure: FLA wins by 2+

portfolios: A EV +5.43 (adj +1.46) on $22.45, P(profit) 0.4976, adj growth 12.8 bp · B EV +6.99 (adj +2.77) on $27.77, P(profit) 0.692, adj growth 25.6 bp · C EV +6.20 (adj +3.41) on $16.64, P(profit) 0.45, adj growth 29.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01FLASJ-SJ|yes == KXNHLGAME-26OCT01FLASJ-FLA|no

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
