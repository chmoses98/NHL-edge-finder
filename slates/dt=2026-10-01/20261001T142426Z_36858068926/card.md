# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-01T14:24:26Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +28.11 | +7.81 | +26.38 | 0.742 | -24.32 | -37.69 | 69.36 |
| B thesis-diversified (joint) ← card | 150.00 | +28.78 | +9.26 | +26.69 | 0.755 | -23.06 | -35.79 | 84.29 |
| C best expression per thesis | 81.89 | +18.94 | +5.65 | +10.55 | 0.699 | -29.60 | -44.68 | 49.34 |

## PHI @ NJD  ·  10000 joint draws  ·  316 bet sides mapped, 5 +EV candidates, 4 on card


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
| Cody Glass: 1+ goals YES | 11 | 0.159 | 0.144 | +0.042 | +0.028 | $5.12 | NJD:OFFENSE_4PLUS | 0.2611 | EVIDENCE_STRONGER | D |
| Noel Acciari: 1+ goals YES | 9 | 0.120 | 0.111 | +0.024 | +0.015 | $2.85 | PHI:OFFENSE_4PLUS | 0.2504 | EVIDENCE_STRONGER | D |
| Anthony Mantha: 1+ assists NO | 74 | 0.861 | 0.772 | +0.107 | +0.019 | $14.29 | NJD:SUPPRESSED | 0.2291 | EVIDENCE_MIXED | D |
| Christian Dvorak: 1+ goals YES | 15 | 0.183 | 0.173 | +0.024 | +0.014 | $2.93 | PHI:OFFENSE_4PLUS | 0.2265 | EVIDENCE_STRONGER | D |
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01PHINJ-NJTMEIER28-1|yes; why: higher confidence-adjusted growth (15.79 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26OCT01PHINJ-NJAMANTHA39-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT01PHINJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NJD offense suppressed (<= 2 goals)
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (5.87 vs 1.06 bp); alternative not eligible: confidence-adjusted EV +0.0074 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26OCT01PHINJ-NJAMANTHA39-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT01PHINJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: PHI offense suppressed (<= 2 goals)
- **Anthony Mantha: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01PHINJ-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (4.27 vs 1.35 bp); relationships: KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT01PHINJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: NJD offense succeeds (4+ goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (3.38 vs 1.06 bp); alternative not eligible: confidence-adjusted EV +0.0074 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT01PHINJ-NJAMANTHA39-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: PHI offense suppressed (<= 2 goals)

portfolios: A EV +4.93 (adj +2.05) on $25.31, P(profit) 0.2624, adj growth 18.5 bp · B EV +5.05 (adj +2.29) on $25.20, P(profit) 0.3797, adj growth 20.8 bp · C EV +1.44 (adj +0.19) on $11.30, P(profit) 0.784, adj growth 1.6 bp

## TBL @ NYR  ·  10000 joint draws  ·  348 bet sides mapped, 10 +EV candidates, 4 on card


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
| John Carlson: 1+ assists NO | 54 | 0.742 | 0.591 | +0.185 | +0.034 | $14.29 | TBL:SUPPRESSED | 0.2264 | EVIDENCE_MIXED | D |
| Tye Kartye: 1+ goals YES | 10 | 0.135 | 0.124 | +0.029 | +0.018 | $2.98 | NYR:OFFENSE_4PLUS | 0.2751 | EVIDENCE_STRONGER | D |
| Tampa Bay wins NO | 43 | 0.514 | 0.469 | +0.066 | +0.022 | $5.08 | NYR:WINS | 0.237 | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ assists NO | 74 | 0.838 | 0.765 | +0.085 | +0.011 | $12.33 | NYR:SUPPRESSED | 0.225 | EVIDENCE_MIXED | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT01TBNYR-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (10.18 vs 6.63 bp); despite a smaller raw edge (+0.185 vs +0.192/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT01TBNYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGAME-26OCT01TBNYR-TB|no: REINFORCING (phi 0.153); KXNHLAST-26OCT01TBNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: TBL offense succeeds (4+ goals)
- **Tye Kartye: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT01TBNYR-NYR|yes; why: higher confidence-adjusted growth (7.01 vs 4.33 bp); despite a smaller raw edge (+0.029 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGAME-26OCT01TBNYR-TB|no: MOSTLY_INDEPENDENT (phi 0.137); KXNHLAST-26OCT01TBNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.047); failure: NYR offense suppressed (<= 2 goals)
- **Tampa Bay wins NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLGAME-26OCT01TBNYR-NYR|yes; why: best adjusted growth among the thesis's expressions; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: REINFORCING (phi 0.153); KXNHLGOAL-26OCT01TBNYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.137); KXNHLAST-26OCT01TBNYR-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.127); failure: TBL wins (incl. OT/SO)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT01TBNYR-4|no; why: higher confidence-adjusted growth (1.46 vs 0.02 bp); wins across more scripts (relative breadth 0.995 vs 0.35); alternative not eligible: confidence-adjusted EV +0.0012 below the 0.010/contract floor; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT01TBNYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGAME-26OCT01TBNYR-TB|no: INTENTIONAL_DIVERSIFIER (phi -0.127); failure: NYR offense succeeds (4+ goals)

portfolios: A EV +6.02 (adj +1.03) on $25.31, P(profit) 0.6934, adj growth 9.6 bp · B EV +7.69 (adj +1.79) on $34.68, P(profit) 0.7393, adj growth 16.4 bp · C EV +6.63 (adj +1.21) on $20.00, P(profit) 0.7421, adj growth 10.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01TBNYR-NYR|yes == KXNHLGAME-26OCT01TBNYR-TB|no

## BUF @ CBJ  ·  10000 joint draws  ·  356 bet sides mapped, 3 +EV candidates, 3 on card


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
| Owen Power: 1+ goals NO | 90 | 0.933 | 0.922 | +0.027 | +0.016 | $14.29 | BUF:SUPPRESSED | 0.2395 | EVIDENCE_STRONGER | D |
| Sean Monahan: 1+ goals YES | 20 | 0.235 | 0.223 | +0.024 | +0.012 | $2.52 | CBJ:OFFENSE_4PLUS | 0.2859 | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ assists NO | 59 | 0.666 | 0.621 | +0.059 | +0.014 | $6.32 | BUF:SUPPRESSED | 0.2404 | EVIDENCE_MIXED | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (6.61 vs 1.73 bp); despite a smaller raw edge (+0.027 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.04); failure: BUF offense succeeds (4+ goals)
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01BUFCBJ-BUF3|no; why: higher confidence-adjusted growth (1.76 vs 1.30 bp); despite a smaller raw edge (+0.024 vs +0.034/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01BUFCBJ-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: CBJ offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01BUFCBJ-BUF3|no; why: higher confidence-adjusted growth (1.73 vs 1.30 bp); alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01BUFCBJ-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.04); KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: BUF offense succeeds (4+ goals)

portfolios: A EV +1.73 (adj +0.62) on $24.13, P(profit) 0.7078, adj growth 5.5 bp · B EV +1.33 (adj +0.53) on $23.14, P(profit) 0.6979, adj growth 5.0 bp · C EV +1.30 (adj +0.40) on $12.67, P(profit) 0.7444, adj growth 3.5 bp

## MIN @ NSH  ·  10000 joint draws  ·  344 bet sides mapped, 1 +EV candidates, 1 on card


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
| Ryan Hartman: 1+ goals YES | 23 | 0.271 | 0.256 | +0.029 | +0.014 | $3.09 | MIN:OFFENSE_4PLUS | 0.2646 | EVIDENCE_STRONGER | D |
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT01MINNSH-9|yes; why: higher confidence-adjusted growth (2.21 vs 1.05 bp); despite a smaller raw edge (+0.029 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.914 vs 0.377); alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: MIN offense suppressed (<= 2 goals)

portfolios: A EV +0.58 (adj +0.27) on $4.85, P(profit) 0.2714, adj growth 2.3 bp · B EV +0.37 (adj +0.17) on $3.09, P(profit) 0.2714, adj growth 1.6 bp · C EV +0.52 (adj +0.24) on $4.32, P(profit) 0.2714, adj growth 2.1 bp

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
| Adam Klapka: 1+ goals YES | 10 | 0.131 | 0.121 | +0.025 | +0.014 | $2.64 | CGY:OFFENSE_4PLUS | 0.2324 | EVIDENCE_STRONGER | D |
- **Adam Klapka: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT01SEACGY-CGYAKLAPKA43-1|yes; why: higher confidence-adjusted growth (4.64 vs 0.00 bp); despite a smaller raw edge (+0.024 vs +0.030/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: CGY offense suppressed (<= 2 goals)

portfolios: A EV +0.80 (adj +0.47) on $3.47, P(profit) 0.1308, adj growth 4.1 bp · B EV +0.61 (adj +0.35) on $2.64, P(profit) 0.1308, adj growth 3.2 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Ryan Greene: 1+ goals YES | 12 | 0.170 | 0.155 | +0.043 | +0.028 | $5.18 | CHI:OFFENSE_4PLUS | 0.26 | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 62 | 0.741 | 0.653 | +0.105 | +0.016 | $9.53 | CHI:SUPPRESSED | 0.2554 | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT01CHIUTA-9|yes; why: higher confidence-adjusted growth (14.68 vs 1.11 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.922 vs 0.368); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.018); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT01CHIUTA-CHIPKANE88-1|no; why: higher confidence-adjusted growth (2.49 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: CHI offense succeeds (4+ goals)

portfolios: A EV +3.73 (adj +1.60) on $16.30, P(profit) 0.17, adj growth 14.1 bp · B EV +3.30 (adj +1.37) on $14.71, P(profit) 0.7882, adj growth 12.3 bp · C EV +4.62 (adj +1.91) on $20.59, P(profit) 0.7882, adj growth 16.5 bp

## EDM @ VAN  ·  10000 joint draws  ·  340 bet sides mapped, 11 +EV candidates, 4 on card


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
| Vancouver wins by over 2.5 goals YES | 10 | 0.148 | 0.122 | +0.042 | +0.015 | $1.81 | VAN:WINS_BY_2PLUS | 0.4525 | EVIDENCE_MIXED | D |
| Drew O'Connor: 1+ goals YES | 17 | 0.213 | 0.196 | +0.034 | +0.016 | $3.02 | VAN:OFFENSE_4PLUS | 0.2334 | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 11 | 0.141 | 0.129 | +0.024 | +0.012 | $2.07 | VAN:OFFENSE_4PLUS | 0.237 | EVIDENCE_STRONGER | D |
| Leon Draisaitl: 2+ points NO | 55 | 0.742 | 0.583 | +0.175 | +0.016 | $6.85 | EDM:SUPPRESSED | 0.2337 | CALIBRATION_WARNING | D |
- **Vancouver wins by over 2.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT01EDMVAN-VAN2|yes; why: higher confidence-adjusted growth (5.42 vs 3.87 bp); despite a smaller raw edge (+0.042 vs +0.049/contract); relationships: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT01EDMVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.111); KXNHLPTS-26OCT01EDMVAN-EDMLDRAISAITL29-2|no: REINFORCING (phi 0.164); failure: EDM wins (incl. OT/SO)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes has the higher standalone adjusted growth (5.42 vs 3.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.135); they share one thesis budget; relationships: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT01EDMVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLPTS-26OCT01EDMVAN-EDMLDRAISAITL29-2|no: MOSTLY_INDEPENDENT (phi -0.004); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes has the higher standalone adjusted growth (5.42 vs 3.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.111); they share one thesis budget; relationships: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes: MOSTLY_INDEPENDENT (phi 0.111); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLPTS-26OCT01EDMVAN-EDMLDRAISAITL29-2|no: MOSTLY_INDEPENDENT (phi 0.007); failure: VAN offense suppressed (<= 2 goals)
- **Leon Draisaitl: 2+ points NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes has the higher standalone adjusted growth (5.42 vs 2.22 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.164); they share one thesis budget; relationships: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes: REINFORCING (phi 0.164); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01EDMVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: EDM offense succeeds (4+ goals)

portfolios: A EV +5.20 (adj +0.79) on $25.31, P(profit) 0.6023, adj growth 6.4 bp · B EV +3.81 (adj +0.95) on $13.75, P(profit) 0.3983, adj growth 8.6 bp · C EV +1.41 (adj +0.52) on $3.56, P(profit) 0.1485, adj growth 4.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01EDMVAN-EDM|no == KXNHLGAME-26OCT01EDMVAN-VAN|yes

## FLA @ SJS  ·  10000 joint draws  ·  366 bet sides mapped, 10 +EV candidates, 4 on card


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
| San Jose wins by over 1.5 goals YES | 24 | 0.334 | 0.284 | +0.081 | +0.032 | $4.55 | SJS:WINS_BY_2PLUS | 0.4038 | EVIDENCE_MIXED | D |
| Aleksander Barkov: 1+ assists NO | 52 | 0.697 | 0.572 | +0.160 | +0.035 | $11.87 | FLA:SUPPRESSED | 0.2565 | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 77 | 0.852 | 0.806 | +0.070 | +0.024 | $13.87 | SJS:WINS | 0.2408 | EVIDENCE_MIXED | D |
| Brady Tkachuk: 1+ assists NO | 63 | 0.749 | 0.659 | +0.103 | +0.012 | $2.50 | FLA:SUPPRESSED | 0.2495 | EVIDENCE_MIXED | D |
- **San Jose wins by over 1.5 goals YES** — thesis: SJS wins by 2+; alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: higher confidence-adjusted growth (11.40 vs 7.29 bp); relationships: KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: REINFORCING (phi 0.163); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.295); KXNHLAST-26OCT01FLASJ-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.144); failure: FLA wins (incl. OT/SO)
- **Aleksander Barkov: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes has the higher standalone adjusted growth (11.40 vs 10.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.163); they share one thesis budget; relationships: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes: REINFORCING (phi 0.163); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.162); KXNHLAST-26OCT01FLASJ-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.098); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes has the higher standalone adjusted growth (11.40 vs 7.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.295); they share one thesis budget; relationships: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes: REINFORCING (phi 0.295); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: REINFORCING (phi 0.162); KXNHLAST-26OCT01FLASJ-FLABTKACHUK8-1|no: REINFORCING (phi 0.151); failure: FLA wins by 2+
- **Brady Tkachuk: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes has the higher standalone adjusted growth (11.40 vs 1.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.144); they share one thesis budget; relationships: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes: MOSTLY_INDEPENDENT (phi 0.144); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: MOSTLY_INDEPENDENT (phi 0.098); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.151); failure: FLA offense succeeds (4+ goals)

portfolios: A EV +5.10 (adj +0.98) on $25.31, P(profit) 0.6207, adj growth 8.8 bp · B EV +6.62 (adj +1.81) on $32.79, P(profit) 0.6864, adj growth 16.5 bp · C EV +3.02 (adj +1.18) on $9.45, P(profit) 0.3336, adj growth 10.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01FLASJ-SJ|yes == KXNHLGAME-26OCT01FLASJ-FLA|no

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
