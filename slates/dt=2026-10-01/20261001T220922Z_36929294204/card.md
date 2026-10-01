# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-01T22:09:22Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +31.03 | +8.48 | +30.12 | 0.795 | -15.61 | -28.76 | 77.92 |
| B thesis-diversified (joint) ← card | 150.01 | +25.71 | +11.29 | +25.08 | 0.768 | -17.18 | -28.62 | 107.03 |
| C best expression per thesis | 150.01 | +25.24 | +11.02 | +24.03 | 0.747 | -20.79 | -32.71 | 103.39 |

## PHI @ NJD  ·  10000 joint draws  ·  318 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.614 / away 0.386

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_PHI_win | p_overtime | goals | shots NJD/PHI | NJD/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.58 | 0.42 | 0.00 | 5.95 | 27.0/26.5 | 23.4/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.47 | 5.81 | 26.8/26.4 | 23.2/23.6 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.104 | 0.63 | 0.37 | 0.00 | 5.94 | 31.8/20.9 | 18.1/27.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.56 | 0.44 | 0.46 | 5.8 | 32.5/21.3 | 18.3/29.2 | even strength |
| NJD shot control · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.58 | 0.42 | 0.52 | 2.76 | 30.7/19.8 | 18.4/29.1 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.54 | 0.46 | 0.46 | 2.72 | 25.6/25.3 | 23.9/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Dawson Mercer: 1+ goals YES | 13 | 0.192 | 0.175 | +0.054 | +0.037 | $4.28 | NJD:OFFENSE_4PLUS | 0.2773 | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 11 | 0.146 | 0.136 | +0.029 | +0.019 | $2.13 | PHI:OFFENSE_4PLUS | 0.2457 | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 65 | 0.781 | 0.693 | +0.115 | +0.026 | $8.59 | NJD:SUPPRESSED | 0.2233 | EVIDENCE_MIXED | D |
| Cody Glass: 1+ goals YES | 12 | 0.153 | 0.144 | +0.026 | +0.016 | $1.92 | NJD:OFFENSE_4PLUS | 0.2595 | EVIDENCE_STRONGER | D |
- **Dawson Mercer: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01PHINJ-NJTMEIER28-1|yes; why: higher confidence-adjusted growth (24.49 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26OCT01PHINJ-NJLEVANGELISTA77-1|no: INTENTIONAL_DIVERSIFIER (phi -0.05); KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NJD offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (7.27 vs 3.66 bp); relationships: KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26OCT01PHINJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: PHI offense suppressed (<= 2 goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no; why: KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no has the higher standalone adjusted growth (8.19 vs 6.96 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.112); relationships: KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.05); KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.037); failure: NJD offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes has the higher standalone adjusted growth (24.49 vs 5.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT01PHINJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.037); failure: NJD offense suppressed (<= 2 goals)

portfolios: A EV +3.45 (adj +1.45) on $18.78, P(profit) 0.5387, adj growth 13.8 bp · B EV +4.06 (adj +2.08) on $16.92, P(profit) 0.3923, adj growth 19.6 bp · C EV +3.69 (adj +2.31) on $22.36, P(profit) 0.6445, adj growth 21.5 bp

## TBL @ NYR  ·  10000 joint draws  ·  350 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.429 / away 0.571

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_TBL_win | p_overtime | goals | shots NYR/TBL | NYR/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.56 | 0.44 | 0.00 | 6.01 | 26.2/26.6 | 23.3/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.47 | 5.89 | 26.1/26.6 | 23.4/22.8 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.103 | 0.50 | 0.50 | 0.00 | 6.01 | 20.7/31.7 | 27.8/17.4 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.47 | 0.53 | 0.49 | 5.84 | 20.8/31.5 | 28.1/17.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.55 | 0.45 | 0.00 | 9.14 | 27.9/28.5 | 23.0/21.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.53 | 0.47 | 0.00 | 3.47 | 25.0/25.3 | 23.6/22.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| John Carlson: 2+ assists NO | 88 | 0.967 | 0.921 | +0.080 | +0.034 | $6.44 | TBL:SUPPRESSED | 0.23 | EVIDENCE_MIXED | D |
| John Carlson: 1+ assists NO | 56 | 0.745 | 0.615 | +0.168 | +0.038 | $6.44 | TBL:SUPPRESSED | 0.2284 | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 1.5 goals NO | 66 | 0.748 | 0.702 | +0.073 | +0.026 | $4.19 | NYR:WINS | 0.2785 | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 78 | 0.848 | 0.811 | +0.056 | +0.019 | $3.99 | NYR:WINS | 0.2458 | EVIDENCE_MIXED | D |
- **John Carlson: 2+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (25.84 vs 12.79 bp); despite a smaller raw edge (+0.080 vs +0.168/contract); relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: DUPLICATIVE (phi 0.314); KXNHLSPREAD-26OCT01TBNYR-TB2|no: MOSTLY_INDEPENDENT (phi 0.092); KXNHLSPREAD-26OCT01TBNYR-TB3|no: MOSTLY_INDEPENDENT (phi 0.089); failure: TBL scoring driven by the power play (2+ PP goals, >= half)
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01TBNYR-TB2|no; why: higher confidence-adjusted growth (12.79 vs 6.78 bp); relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-2|no: DUPLICATIVE (phi 0.314); KXNHLSPREAD-26OCT01TBNYR-TB2|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLSPREAD-26OCT01TBNYR-TB3|no: MOSTLY_INDEPENDENT (phi 0.129); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01TBNYR-TB3|no; why: higher confidence-adjusted growth (6.78 vs 5.08 bp); relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-2|no: MOSTLY_INDEPENDENT (phi 0.092); KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLSPREAD-26OCT01TBNYR-TB3|no: DUPLICATIVE (phi 0.73); failure: TBL wins by 2+
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01TBNYR-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT01TBNYR-TB2|no has the higher standalone adjusted growth (6.78 vs 5.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.730); they share one thesis budget; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-2|no: MOSTLY_INDEPENDENT (phi 0.089); KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.129); KXNHLSPREAD-26OCT01TBNYR-TB2|no: DUPLICATIVE (phi 0.73); failure: TBL wins by 2+

portfolios: A EV +5.21 (adj +0.89) on $18.78, P(profit) 0.7712, adj growth 8.1 bp · B EV +3.18 (adj +0.93) on $21.06, P(profit) 0.6519, adj growth 9.0 bp · C EV +3.93 (adj +1.02) on $19.34, P(profit) 0.5851, adj growth 9.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01TBNYR-TB|no == KXNHLGAME-26OCT01TBNYR-NYR|yes

## BUF @ CBJ  ·  10000 joint draws  ·  358 bet sides mapped, 8 +EV candidates, 4 on card

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
| Charlie Coyle: 1+ goals YES | 21 | 0.273 | 0.256 | +0.051 | +0.034 | $4.12 | CBJ:OFFENSE_4PLUS | 0.2692 | EVIDENCE_STRONGER | D |
| Noah Ostlund: 1+ goals NO | 83 | 0.865 | 0.855 | +0.025 | +0.015 | $8.22 | BUF:SUPPRESSED | 0.2429 | EVIDENCE_STRONGER | D |
| Buffalo wins NO | 49 | 0.556 | 0.524 | +0.049 | +0.017 | $2.34 | CBJ:WINS | 0.2411 | EVIDENCE_MIXED | B |
| Valeri Nichushkin: 1+ assists NO | 71 | 0.776 | 0.738 | +0.052 | +0.014 | $6.79 | CBJ:SUPPRESSED | 0.2433 | EVIDENCE_MIXED | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT01BUFCBJ-BUF|no; why: higher confidence-adjusted growth (14.80 vs 2.43 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01BUFCBJ-BUFNOSTLUND86-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGAME-26OCT01BUFCBJ-BUF|no: REINFORCING (phi 0.172); KXNHLAST-26OCT01BUFCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.049); failure: CBJ offense suppressed (<= 2 goals)
- **Noah Ostlund: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT01BUFCBJ-BUF|no; why: higher confidence-adjusted growth (3.61 vs 2.43 bp); despite a smaller raw edge (+0.025 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGAME-26OCT01BUFCBJ-BUF|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLAST-26OCT01BUFCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: BUF offense succeeds (4+ goals)
- **Buffalo wins NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLGAME-26OCT01BUFCBJ-CBJ|yes; why: best adjusted growth among the thesis's expressions; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: REINFORCING (phi 0.172); KXNHLGOAL-26OCT01BUFCBJ-BUFNOSTLUND86-1|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLAST-26OCT01BUFCBJ-CBJVNICHUSHKIN43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.158); failure: BUF wins (incl. OT/SO)
- **Valeri Nichushkin: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01BUFCBJ-CBJKJOHNSON91-1|no; why: higher confidence-adjusted growth (2.08 vs 1.98 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.049); KXNHLGOAL-26OCT01BUFCBJ-BUFNOSTLUND86-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGAME-26OCT01BUFCBJ-BUF|no: INTENTIONAL_DIVERSIFIER (phi -0.158); failure: CBJ offense succeeds (4+ goals)

portfolios: A EV +2.26 (adj +1.01) on $18.78, P(profit) 0.4721, adj growth 9.4 bp · B EV +1.91 (adj +0.99) on $21.47, P(profit) 0.5093, adj growth 9.4 bp · C EV +2.15 (adj +1.08) on $17.31, P(profit) 0.536, adj growth 10.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01BUFCBJ-CBJ|yes == KXNHLGAME-26OCT01BUFCBJ-BUF|no

## MIN @ NSH  ·  10000 joint draws  ·  344 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.427 / away 0.573

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_MIN_win | p_overtime | goals | shots NSH/MIN | NSH/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.45 | 0.55 | 0.00 | 6.01 | 29.2/29.4 | 25.5/25.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.46 | 5.98 | 29.4/29.6 | 26.2/26.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.46 | 0.54 | 0.00 | 9.35 | 30.9/31.1 | 24.5/25.0 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.071 | 0.37 | 0.63 | 0.00 | 6.07 | 23.4/34.5 | 30.1/20.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.45 | 0.55 | 0.50 | 5.92 | 23.7/34.6 | 31.2/20.5 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.49 | 0.51 | 0.43 | 5.94 | 34.3/23.6 | 20.3/30.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Ryan O'Reilly: 1+ goals YES | 25 | 0.299 | 0.285 | +0.035 | +0.022 | $3.10 | NSH:OFFENSE_4PLUS | 0.2605 | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 23 | 0.274 | 0.262 | +0.032 | +0.020 | $2.66 | MIN:OFFENSE_4PLUS | 0.2559 | EVIDENCE_STRONGER | D |
| Jared Spurgeon: 1+ goals NO | 91 | 0.935 | 0.927 | +0.019 | +0.012 | $8.59 | MIN:SUPPRESSED | 0.242 | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ goals YES | 18 | 0.212 | 0.203 | +0.022 | +0.013 | $1.60 | NSH:OFFENSE_4PLUS | 0.2658 | EVIDENCE_STRONGER | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes; why: higher confidence-adjusted growth (5.46 vs 2.23 bp); relationships: KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: NSH offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT01MINNSH-9|yes; why: higher confidence-adjusted growth (4.54 vs 0.51 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.902 vs 0.369); alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: MIN offense suppressed (<= 2 goals)
- **Jared Spurgeon: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT01MINNSH-MINMSHABANOV49-1|no; why: higher confidence-adjusted growth (3.99 vs 0.00 bp); despite a smaller raw edge (+0.019 vs +0.053/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: MIN offense succeeds (4+ goals)
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes has the higher standalone adjusted growth (5.46 vs 2.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NSH offense suppressed (<= 2 goals)

portfolios: A EV +3.73 (adj +1.17) on $18.52, P(profit) 0.4472, adj growth 9.9 bp · B EV +1.13 (adj +0.69) on $15.95, P(profit) 0.5723, adj growth 6.6 bp · C EV +0.90 (adj +0.56) on $6.77, P(profit) 0.4891, adj growth 5.2 bp

## SEA @ CGY  ·  10000 joint draws  ·  398 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.502 / away 0.498

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
| Brandon Montour: 1+ goals NO | 83 | 0.892 | 0.875 | +0.052 | +0.036 | $6.49 | SEA:SUPPRESSED | 0.2498 | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 10 | 0.136 | 0.126 | +0.030 | +0.019 | $2.27 | SEA:OFFENSE_4PLUS | 0.2597 | EVIDENCE_STRONGER | D |
| Jared McCann: 1+ assists NO | 64 | 0.731 | 0.683 | +0.074 | +0.027 | $6.39 | SEA:SUPPRESSED | 0.2509 | EVIDENCE_MIXED | D |
| Adam Klapka: 1+ goals YES | 10 | 0.131 | 0.122 | +0.025 | +0.015 | $1.78 | CGY:OFFENSE_4PLUS | 0.2324 | EVIDENCE_STRONGER | D |
- **Brandon Montour: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (21.16 vs 6.93 bp); despite a smaller raw edge (+0.053 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: SEA offense succeeds (4+ goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01SEACGY-SEAMBENIERS10-1|yes; why: higher confidence-adjusted growth (8.48 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no: INTENTIONAL_DIVERSIFIER (phi -0.066); KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: SEA offense suppressed (<= 2 goals)
- **Jared McCann: 1+ assists NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (6.93 vs 1.62 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.066); KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: SEA offense succeeds (4+ goals)
- **Adam Klapka: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01SEACGY-CGYMFROST16-1|yes; why: higher confidence-adjusted growth (5.48 vs 2.08 bp); relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: CGY offense suppressed (<= 2 goals)

portfolios: A EV +2.52 (adj +1.42) on $18.78, P(profit) 0.2516, adj growth 13.4 bp · B EV +2.17 (adj +1.21) on $16.93, P(profit) 0.7514, adj growth 11.6 bp · C EV +2.10 (adj +1.02) on $14.97, P(profit) 0.7772, adj growth 9.5 bp

## CHI @ UTA  ·  10000 joint draws  ·  320 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.657 / away 0.343

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
| Ryan Greene: 1+ goals YES | 12 | 0.166 | 0.153 | +0.039 | +0.026 | $3.10 | CHI:OFFENSE_4PLUS | 0.2422 | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 21 | 0.259 | 0.246 | +0.038 | +0.024 | $3.32 | UTA:OFFENSE_4PLUS | 0.2642 | EVIDENCE_STRONGER | D |
| Anders Lee: 1+ goals YES | 23 | 0.274 | 0.262 | +0.031 | +0.019 | $2.77 | UTA:OFFENSE_4PLUS | 0.2847 | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 62 | 0.745 | 0.657 | +0.109 | +0.021 | $7.47 | CHI:SUPPRESSED | 0.264 | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01CHIUTA-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (13.19 vs 2.36 bp); despite a smaller raw edge (+0.039 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.037); failure: CHI offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes; why: higher confidence-adjusted growth (7.31 vs 4.30 bp); relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: UTA offense suppressed (<= 2 goals)
- **Anders Lee: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT01CHIUTA-10|yes; why: higher confidence-adjusted growth (4.30 vs 0.37 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.855 vs 0.309); alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: UTA offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01CHIUTA-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (4.14 vs 1.74 bp); relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CHI offense succeeds (4+ goals)

portfolios: A EV +3.61 (adj +0.64) on $18.78, P(profit) 0.6436, adj growth 5.9 bp · B EV +3.15 (adj +1.46) on $16.66, P(profit) 0.4788, adj growth 13.8 bp · C EV +3.28 (adj +1.46) on $25.32, P(profit) 0.3429, adj growth 13.7 bp

## EDM @ VAN  ·  10000 joint draws  ·  328 bet sides mapped, 21 +EV candidates, 4 on card

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
| Connor McDavid: 1+ assists NO | 31 | 0.476 | 0.365 | +0.151 | +0.040 | $4.28 | EDM:SUPPRESSED | 0.2287 | EVIDENCE_MIXED | D |
| Drew O'Connor: 1+ goals YES | 16 | 0.215 | 0.200 | +0.046 | +0.031 | $3.74 | VAN:OFFENSE_4PLUS | 0.2471 | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 69 | 0.831 | 0.736 | +0.126 | +0.031 | $8.59 | EDM:SUPPRESSED | 0.2297 | EVIDENCE_MIXED | D |
| Marco Rossi: 1+ goals YES | 21 | 0.257 | 0.244 | +0.035 | +0.022 | $2.95 | VAN:OFFENSE_4PLUS | 0.2482 | EVIDENCE_STRONGER | D |
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (15.80 vs 10.31 bp); relationships: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: DUPLICATIVE (phi 0.43); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: EDM offense succeeds (4+ goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01EDMVAN-EDM3|no; why: higher confidence-adjusted growth (14.52 vs 8.48 bp); despite a smaller raw edge (+0.046 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: VAN offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no; why: second expression of the same thesis: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no has the higher standalone adjusted growth (15.80 vs 10.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.430); they share one thesis budget; relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: DUPLICATIVE (phi 0.43); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: EDM offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (14.52 vs 6.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.011); failure: VAN offense suppressed (<= 2 goals)

portfolios: A EV +4.91 (adj +0.96) on $18.78, P(profit) 0.6703, adj growth 9.0 bp · B EV +5.01 (adj +1.88) on $19.55, P(profit) 0.6604, adj growth 17.8 bp · C EV +4.85 (adj +1.83) on $18.62, P(profit) 0.529, adj growth 17.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01EDMVAN-VAN|yes == KXNHLGAME-26OCT01EDMVAN-EDM|no

## FLA @ SJS  ·  10000 joint draws  ·  368 bet sides mapped, 24 +EV candidates, 3 on card

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
| Kiefer Sherwood: 1+ goals YES | 15 | 0.215 | 0.198 | +0.057 | +0.039 | $4.36 | SJS:OFFENSE_4PLUS | 0.2535 | EVIDENCE_STRONGER | D |
| Aleksander Barkov: 1+ assists NO | 51 | 0.692 | 0.567 | +0.164 | +0.040 | $8.55 | FLA:SUPPRESSED | 0.2433 | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 76 | 0.852 | 0.803 | +0.079 | +0.031 | $8.55 | SJS:WINS | 0.2381 | EVIDENCE_MIXED | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: higher confidence-adjusted growth (24.17 vs 11.90 bp); despite a smaller raw edge (+0.057 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.112); failure: SJS offense suppressed (<= 2 goals)
- **Aleksander Barkov: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: higher confidence-adjusted growth (13.76 vs 11.90 bp); relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.153); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: higher confidence-adjusted growth (11.90 vs 8.24 bp); wins across more scripts (relative breadth 1.017 vs 0.517); relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.112); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: REINFORCING (phi 0.153); failure: FLA wins by 2+

portfolios: A EV +5.33 (adj +0.94) on $18.78, P(profit) 0.6212, adj growth 8.4 bp · B EV +5.09 (adj +2.05) on $21.47, P(profit) 0.6905, adj growth 19.4 bp · C EV +4.33 (adj +1.74) on $25.32, P(profit) 0.6784, adj growth 16.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01FLASJ-SJ|yes == KXNHLGAME-26OCT01FLASJ-FLA|no

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
