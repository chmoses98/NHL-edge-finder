# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-01T20:31:50Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +28.94 | +7.92 | +27.47 | 0.770 | -17.83 | -28.85 | 72.46 |
| B thesis-diversified (joint) ← card | 148.16 | +25.61 | +12.00 | +24.03 | 0.739 | -21.61 | -33.36 | 112.80 |
| C best expression per thesis | 149.99 | +19.64 | +9.10 | +17.78 | 0.720 | -19.95 | -29.82 | 86.12 |

## PHI @ NJD  ·  10000 joint draws  ·  318 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.605 / away 0.395

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_PHI_win | p_overtime | goals | shots NJD/PHI | NJD/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.58 | 0.42 | 0.00 | 5.94 | 26.8/26.4 | 23.2/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.49 | 5.88 | 27.1/26.6 | 23.3/23.8 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.110 | 0.63 | 0.37 | 0.00 | 5.93 | 32.0/20.9 | 18.1/27.9 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.56 | 0.44 | 0.49 | 5.85 | 32.2/21.2 | 18.0/28.9 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.50 | 0.50 | 0.50 | 2.82 | 25.4/25.1 | 23.6/23.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.066 | 0.55 | 0.45 | 0.00 | 3.44 | 25.5/25.1 | 23.4/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Sean Couturier: 1+ goals YES | 10 | 0.152 | 0.138 | +0.046 | +0.031 | $3.82 | PHI:OFFENSE_4PLUS | 0.2355 | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 12 | 0.153 | 0.143 | +0.025 | +0.016 | $2.15 | NJD:OFFENSE_4PLUS | 0.2644 | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 72 | 0.769 | 0.754 | +0.035 | +0.020 | $9.10 | NJD:SUPPRESSED | 0.2245 | EVIDENCE_STRONGER | D |
| Noel Acciari: 1+ goals YES | 9 | 0.117 | 0.109 | +0.021 | +0.013 | $1.66 | PHI:OFFENSE_4PLUS | 0.2453 | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (22.10 vs 4.27 bp); relationships: KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: PHI offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes; why: higher confidence-adjusted growth (4.95 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0003 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.027); failure: NJD offense suppressed (<= 2 goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01PHINJ-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (4.50 vs 3.55 bp); despite a smaller raw edge (+0.035 vs +0.102/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: NJD offense succeeds (4+ goals)
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (22.10 vs 4.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: PHI offense suppressed (<= 2 goals)

portfolios: A EV +3.44 (adj +1.43) on $18.75, P(profit) 0.4887, adj growth 13.2 bp · B EV +2.87 (adj +1.88) on $16.74, P(profit) 0.3708, adj growth 17.5 bp · C EV +2.42 (adj +1.53) on $22.78, P(profit) 0.6806, adj growth 14.3 bp

## TBL @ NYR  ·  10000 joint draws  ·  350 bet sides mapped, 19 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.429 / away 0.571

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_TBL_win | p_overtime | goals | shots NYR/TBL | NYR/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.55 | 0.45 | 0.00 | 5.98 | 26.1/26.6 | 23.3/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.52 | 0.48 | 0.47 | 5.9 | 26.1/26.5 | 23.2/22.8 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.106 | 0.49 | 0.51 | 0.00 | 5.95 | 21.0/31.6 | 27.9/17.7 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.49 | 0.51 | 0.49 | 5.87 | 20.8/31.9 | 28.6/17.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.56 | 0.44 | 0.00 | 9.11 | 27.7/28.1 | 22.6/21.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.53 | 0.47 | 0.48 | 2.78 | 24.6/25.2 | 23.7/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| John Carlson: 1+ assists NO | 55 | 0.742 | 0.611 | +0.174 | +0.043 | $8.11 | TBL:SUPPRESSED | 0.2322 | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ assists NO | 76 | 0.842 | 0.796 | +0.070 | +0.023 | $8.11 | NYR:SUPPRESSED | 0.2366 | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 1.5 goals NO | 66 | 0.746 | 0.700 | +0.070 | +0.025 | $6.98 | NYR:WINS | 0.2753 | EVIDENCE_MIXED | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT01TBNYR-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (16.68 vs 7.55 bp); despite a smaller raw edge (+0.174 vs +0.185/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLAST-26OCT01TBNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLSPREAD-26OCT01TBNYR-TB2|no: REINFORCING (phi 0.159); failure: TBL offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT01TBNYR-4|no; why: higher confidence-adjusted growth (6.90 vs 0.15 bp); wins across more scripts (relative breadth 0.999 vs 0.347); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLSPREAD-26OCT01TBNYR-TB2|no: INTENTIONAL_DIVERSIFIER (phi -0.116); failure: NYR offense succeeds (4+ goals)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLPTS-26OCT01TBNYR-TBJCARLSON74-1|no; why: KXNHLPTS-26OCT01TBNYR-TBJCARLSON74-1|no has the higher standalone adjusted growth (7.55 vs 6.09 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.178); relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: REINFORCING (phi 0.159); KXNHLAST-26OCT01TBNYR-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.116); failure: TBL wins by 2+

portfolios: A EV +5.65 (adj +1.14) on $18.75, P(profit) 0.7017, adj growth 10.6 bp · B EV +3.94 (adj +1.12) on $23.20, P(profit) 0.7279, adj growth 10.8 bp · C EV +3.66 (adj +0.99) on $17.03, P(profit) 0.5833, adj growth 9.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01TBNYR-TB|no == KXNHLGAME-26OCT01TBNYR-NYR|yes

## BUF @ CBJ  ·  10000 joint draws  ·  358 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.494 / away 0.506

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_BUF_win | p_overtime | goals | shots CBJ/BUF | CBJ/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.59 | 0.41 | 0.00 | 6.01 | 28.2/28.2 | 25.0/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.46 | 5.9 | 27.9/28.0 | 24.8/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.60 | 0.40 | 0.00 | 9.25 | 29.9/29.7 | 24.1/23.5 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.078 | 0.66 | 0.34 | 0.00 | 5.98 | 33.2/22.3 | 19.5/28.9 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.48 | 5.94 | 33.5/22.5 | 19.3/29.9 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.060 | 0.51 | 0.49 | 0.00 | 5.95 | 22.6/32.8 | 29.0/19.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Zach Metsa: 1+ goals NO | 93 | 0.967 | 0.957 | +0.032 | +0.022 | $9.63 | DIFFUSE | 0.2432 | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 21 | 0.273 | 0.256 | +0.051 | +0.034 | $5.04 | CBJ:OFFENSE_4PLUS | 0.2692 | EVIDENCE_STRONGER | D |
| Sean Monahan: 1+ goals YES | 20 | 0.240 | 0.227 | +0.029 | +0.016 | $2.32 | CBJ:OFFENSE_4PLUS | 0.2503 | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ assists NO | 60 | 0.680 | 0.632 | +0.063 | +0.015 | $4.92 | BUF:SUPPRESSED | 0.2423 | EVIDENCE_MIXED | D |
- **Zach Metsa: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.062); failure: BUF offense succeeds (4+ goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes; why: higher confidence-adjusted growth (14.80 vs 3.37 bp); relationships: KXNHLGOAL-26OCT01BUFCBJ-BUFZMETSA73-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CBJ offense suppressed (<= 2 goals)
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (14.80 vs 3.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT01BUFCBJ-BUFZMETSA73-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: CBJ offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01BUFCBJ-BUF3|no; why: KXNHLSPREAD-26OCT01BUFCBJ-BUF3|no has the higher standalone adjusted growth (2.27 vs 2.24 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.155); relationships: KXNHLGOAL-26OCT01BUFCBJ-BUFZMETSA73-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: BUF offense succeeds (4+ goals)

portfolios: A EV +1.85 (adj +0.94) on $18.75, P(profit) 0.6979, adj growth 8.9 bp · B EV +2.32 (adj +1.31) on $21.91, P(profit) 0.3898, adj growth 12.4 bp · C EV +1.56 (adj +0.92) on $23.26, P(profit) 0.273, adj growth 8.9 bp

## MIN @ NSH  ·  10000 joint draws  ·  344 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.430 / away 0.570

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
| Ryan O'Reilly: 1+ goals YES | 25 | 0.304 | 0.289 | +0.041 | +0.026 | $4.11 | NSH:OFFENSE_4PLUS | 0.2623 | EVIDENCE_STRONGER | D |
| Blake Coleman: 1+ goals YES | 23 | 0.272 | 0.261 | +0.030 | +0.018 | $2.74 | MIN:OFFENSE_4PLUS | 0.2742 | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 23 | 0.271 | 0.260 | +0.029 | +0.017 | $2.59 | MIN:OFFENSE_4PLUS | 0.2646 | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ goals YES | 18 | 0.216 | 0.206 | +0.026 | +0.015 | $2.20 | NSH:OFFENSE_4PLUS | 0.2665 | EVIDENCE_STRONGER | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes; why: higher confidence-adjusted growth (7.73 vs 3.38 bp); relationships: KXNHLGOAL-26OCT01MINNSH-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: NSH offense suppressed (<= 2 goals)
- **Blake Coleman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (3.90 vs 3.59 bp); relationships: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-MINBCOLEMAN20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01MINNSH-MINBCOLEMAN20-1|yes has the higher standalone adjusted growth (3.90 vs 3.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.028); they share one thesis budget; relationships: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01MINNSH-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: MIN offense suppressed (<= 2 goals)
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes has the higher standalone adjusted growth (7.73 vs 3.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT01MINNSH-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: NSH offense suppressed (<= 2 goals)

portfolios: A EV +4.20 (adj +1.31) on $18.75, P(profit) 0.4895, adj growth 11.0 bp · B EV +1.59 (adj +0.98) on $11.64, P(profit) 0.416, adj growth 9.2 bp · C EV +1.14 (adj +0.71) on $15.97, P(profit) 0.4661, adj growth 6.7 bp

## SEA @ CGY  ·  10000 joint draws  ·  398 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.504 / away 0.496

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
| Brandon Montour: 1+ goals NO | 83 | 0.892 | 0.875 | +0.052 | +0.036 | $6.50 | SEA:SUPPRESSED | 0.2498 | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 10 | 0.136 | 0.126 | +0.030 | +0.019 | $2.47 | SEA:OFFENSE_4PLUS | 0.2597 | EVIDENCE_STRONGER | D |
| Jared McCann: 1+ assists NO | 65 | 0.731 | 0.685 | +0.065 | +0.019 | $4.72 | SEA:SUPPRESSED | 0.2509 | EVIDENCE_MIXED | D |
| Jared McCann: 1+ goals NO | 72 | 0.756 | 0.746 | +0.022 | +0.012 | $3.22 | SEA:SUPPRESSED | 0.2484 | EVIDENCE_STRONGER | D |
- **Brandon Montour: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (21.16 vs 3.70 bp); despite a smaller raw edge (+0.053 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: SEA offense succeeds (4+ goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01SEACGY-SEAMBENIERS10-1|yes; why: higher confidence-adjusted growth (8.48 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no: INTENTIONAL_DIVERSIFIER (phi -0.066); KXNHLGOAL-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: SEA offense suppressed (<= 2 goals)
- **Jared McCann: 1+ assists NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (3.70 vs 1.62 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.066); KXNHLGOAL-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: SEA offense succeeds (4+ goals)
- **Jared McCann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no; why: second expression of the same thesis: KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no has the higher standalone adjusted growth (3.70 vs 1.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: SEA offense succeeds (4+ goals)

portfolios: A EV +1.68 (adj +0.90) on $18.75, P(profit) 0.5755, adj growth 8.6 bp · B EV +1.65 (adj +0.92) on $16.91, P(profit) 0.5755, adj growth 8.8 bp · C EV +1.45 (adj +0.67) on $10.38, P(profit) 0.7772, adj growth 6.3 bp

## CHI @ UTA  ·  10000 joint draws  ·  320 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.658 / away 0.342

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_CHI_win | p_overtime | goals | shots UTA/CHI | UTA/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| UTA shot control · normal event (5-7) · decided (2+) | 0.130 | 0.77 | 0.23 | 0.00 | 6.0 | 32.8/21.1 | 18.8/27.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.69 | 0.31 | 0.00 | 6.06 | 27.5/26.9 | 24.1/23.0 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.100 | 0.75 | 0.25 | 0.00 | 9.28 | 34.3/22.5 | 18.2/25.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.57 | 0.43 | 0.46 | 5.93 | 32.9/21.4 | 18.3/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.55 | 0.45 | 0.45 | 5.97 | 27.7/27.1 | 23.8/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.70 | 0.30 | 0.00 | 9.34 | 29.2/28.5 | 23.5/22.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Ryan Greene: 1+ goals YES | 12 | 0.166 | 0.153 | +0.039 | +0.026 | $3.48 | CHI:OFFENSE_4PLUS | 0.2422 | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 21 | 0.259 | 0.246 | +0.038 | +0.024 | $3.72 | UTA:OFFENSE_4PLUS | 0.2642 | EVIDENCE_STRONGER | D |
| Anders Lee: 1+ goals YES | 23 | 0.274 | 0.262 | +0.031 | +0.019 | $3.10 | UTA:OFFENSE_4PLUS | 0.2847 | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 62 | 0.745 | 0.657 | +0.109 | +0.021 | $8.38 | CHI:SUPPRESSED | 0.264 | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01CHIUTA-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (13.19 vs 1.40 bp); despite a smaller raw edge (+0.039 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.037); failure: CHI offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes; why: higher confidence-adjusted growth (7.31 vs 4.30 bp); relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: UTA offense suppressed (<= 2 goals)
- **Anders Lee: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT01CHIUTA-10|yes; why: higher confidence-adjusted growth (4.30 vs 0.37 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.855 vs 0.309); alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: UTA offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01CHIUTA-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (4.14 vs 1.74 bp); relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CHI offense succeeds (4+ goals)

portfolios: A EV +3.61 (adj +0.58) on $18.75, P(profit) 0.6436, adj growth 5.3 bp · B EV +3.53 (adj +1.64) on $18.68, P(profit) 0.4788, adj growth 15.3 bp · C EV +3.02 (adj +1.34) on $23.26, P(profit) 0.3429, adj growth 12.7 bp

## EDM @ VAN  ·  10000 joint draws  ·  328 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.348 / away 0.652

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_EDM_win | p_overtime | goals | shots VAN/EDM | VAN/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.43 | 0.57 | 0.00 | 6.02 | 27.8/28.4 | 24.4/24.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.110 | 0.35 | 0.65 | 0.00 | 6.02 | 22.2/33.9 | 29.6/19.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.48 | 0.52 | 0.46 | 5.93 | 27.9/28.6 | 25.2/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.43 | 0.57 | 0.00 | 9.47 | 29.4/30.1 | 23.4/23.3 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.45 | 0.55 | 0.47 | 5.93 | 22.4/34.3 | 31.1/19.1 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.083 | 0.33 | 0.67 | 0.00 | 9.32 | 23.5/35.6 | 27.5/18.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Drew O'Connor: 1+ goals YES | 16 | 0.215 | 0.200 | +0.046 | +0.031 | $4.11 | VAN:OFFENSE_4PLUS | 0.2471 | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 32 | 0.476 | 0.368 | +0.141 | +0.033 | $5.34 | EDM:SUPPRESSED | 0.2287 | EVIDENCE_MIXED | D |
| Linus Karlsson: 1+ goals YES | 18 | 0.229 | 0.215 | +0.038 | +0.025 | $3.40 | VAN:OFFENSE_4PLUS | 0.2446 | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 21 | 0.257 | 0.244 | +0.035 | +0.022 | $3.31 | VAN:OFFENSE_4PLUS | 0.2482 | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01EDMVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (14.52 vs 8.62 bp); relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT01EDMVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: VAN offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (10.59 vs 10.31 bp); relationships: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT01EDMVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: EDM offense succeeds (4+ goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (14.52 vs 8.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (14.52 vs 6.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01EDMVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: VAN offense suppressed (<= 2 goals)

portfolios: A EV +4.88 (adj +0.92) on $18.75, P(profit) 0.6568, adj growth 8.5 bp · B EV +4.57 (adj +2.05) on $16.15, P(profit) 0.4691, adj growth 19.2 bp · C EV +3.74 (adj +1.41) on $23.26, P(profit) 0.5254, adj growth 13.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01EDMVAN-VAN|yes == KXNHLGAME-26OCT01EDMVAN-EDM|no

## FLA @ SJS  ·  10000 joint draws  ·  368 bet sides mapped, 20 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.427 / away 0.573

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_FLA_win | p_overtime | goals | shots SJS/FLA | SJS/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.58 | 0.42 | 0.00 | 6.0 | 26.7/26.9 | 23.8/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.47 | 5.95 | 27.0/27.0 | 23.7/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.59 | 0.41 | 0.00 | 9.35 | 28.5/28.6 | 23.1/21.8 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.072 | 0.50 | 0.50 | 0.00 | 6.01 | 21.2/31.6 | 27.9/17.9 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.50 | 0.50 | 0.47 | 5.96 | 21.6/32.0 | 28.7/18.4 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.060 | 0.67 | 0.33 | 0.00 | 6.0 | 31.1/21.3 | 18.6/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Kiefer Sherwood: 1+ goals YES | 15 | 0.215 | 0.198 | +0.057 | +0.039 | $4.92 | SJS:OFFENSE_4PLUS | 0.2535 | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 76 | 0.852 | 0.803 | +0.079 | +0.031 | $9.63 | SJS:WINS | 0.2381 | EVIDENCE_MIXED | D |
| Aleksander Barkov: 1+ assists NO | 52 | 0.692 | 0.570 | +0.154 | +0.033 | $8.39 | FLA:SUPPRESSED | 0.2433 | EVIDENCE_MIXED | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: higher confidence-adjusted growth (24.17 vs 11.90 bp); despite a smaller raw edge (+0.057 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT01FLASJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.112); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: SJS offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: higher confidence-adjusted growth (11.90 vs 8.24 bp); wins across more scripts (relative breadth 1.017 vs 0.517); relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.112); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: REINFORCING (phi 0.153); failure: FLA wins by 2+
- **Aleksander Barkov: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-FLA3|no has the higher standalone adjusted growth (11.90 vs 9.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.153); they share one thesis budget; relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.153); failure: FLA offense succeeds (4+ goals)

portfolios: A EV +3.64 (adj +0.70) on $18.75, P(profit) 0.6117, adj growth 6.5 bp · B EV +5.14 (adj +2.10) on $22.93, P(profit) 0.6905, adj growth 19.7 bp · C EV +2.64 (adj +1.53) on $14.05, P(profit) 0.2154, adj growth 14.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01FLASJ-SJ|yes == KXNHLGAME-26OCT01FLASJ-FLA|no

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
