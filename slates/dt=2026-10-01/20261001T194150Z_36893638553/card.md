# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-01T19:41:50Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +28.99 | +6.93 | +27.95 | 0.770 | -19.25 | -30.95 | 62.13 |
| B thesis-diversified (joint) ← card | 149.08 | +22.55 | +9.84 | +21.51 | 0.744 | -18.75 | -29.70 | 92.99 |
| C best expression per thesis | 149.99 | +18.24 | +8.14 | +16.76 | 0.706 | -21.46 | -31.63 | 76.32 |

## PHI @ NJD  ·  10000 joint draws  ·  318 bet sides mapped, 10 +EV candidates, 4 on card

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
| Cody Glass: 1+ goals YES | 12 | 0.153 | 0.143 | +0.025 | +0.016 | $2.01 | NJD:OFFENSE_4PLUS | 0.2644 | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 15 | 0.185 | 0.175 | +0.026 | +0.016 | $2.08 | PHI:OFFENSE_4PLUS | 0.2392 | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 66 | 0.777 | 0.695 | +0.102 | +0.019 | $8.13 | NJD:SUPPRESSED | 0.224 | EVIDENCE_MIXED | D |
| Porter Martone: 1+ goals NO | 77 | 0.811 | 0.798 | +0.028 | +0.016 | $8.55 | PHI:SUPPRESSED | 0.2272 | EVIDENCE_STRONGER | D |
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes; why: higher confidence-adjusted growth (4.95 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0003 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01PHINJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT01PHINJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26OCT01PHINJ-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: NJD offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (4.27 vs 3.22 bp); relationships: KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT01PHINJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT01PHINJ-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: PHI offense suppressed (<= 2 goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no; why: KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no has the higher standalone adjusted growth (3.96 vs 3.55 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.104); relationships: KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26OCT01PHINJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT01PHINJ-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: NJD offense succeeds (4+ goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT01PHINJ-6|no; why: higher confidence-adjusted growth (3.13 vs 0.70 bp); despite a smaller raw edge (+0.028 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.984 vs 0.753); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT01PHINJ-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT01PHINJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: PHI offense succeeds (4+ goals)

portfolios: A EV +2.04 (adj +0.51) on $18.87, P(profit) 0.6589, adj growth 4.8 bp · B EV +2.27 (adj +0.86) on $20.76, P(profit) 0.7389, adj growth 8.1 bp · C EV +1.42 (adj +0.75) on $23.80, P(profit) 0.686, adj growth 7.0 bp

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
| John Carlson: 1+ assists NO | 55 | 0.742 | 0.607 | +0.174 | +0.040 | $7.86 | TBL:SUPPRESSED | 0.2322 | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ assists NO | 76 | 0.842 | 0.796 | +0.070 | +0.023 | $7.86 | NYR:SUPPRESSED | 0.2366 | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 1.5 goals NO | 66 | 0.746 | 0.700 | +0.070 | +0.025 | $6.99 | NYR:WINS | 0.2753 | EVIDENCE_MIXED | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01TBNYR-TB2|no; why: higher confidence-adjusted growth (14.26 vs 6.09 bp); relationships: KXNHLAST-26OCT01TBNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLSPREAD-26OCT01TBNYR-TB2|no: REINFORCING (phi 0.159); failure: TBL offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT01TBNYR-4|no; why: higher confidence-adjusted growth (6.90 vs 0.15 bp); wins across more scripts (relative breadth 0.999 vs 0.347); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLSPREAD-26OCT01TBNYR-TB2|no: INTENTIONAL_DIVERSIFIER (phi -0.116); failure: NYR offense succeeds (4+ goals)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01TBNYR-TB3|no; why: higher confidence-adjusted growth (6.09 vs 5.49 bp); relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: REINFORCING (phi 0.159); KXNHLAST-26OCT01TBNYR-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.116); failure: TBL wins by 2+

portfolios: A EV +6.74 (adj +1.11) on $18.87, P(profit) 0.7718, adj growth 9.8 bp · B EV +3.84 (adj +1.05) on $22.70, P(profit) 0.7279, adj growth 10.1 bp · C EV +4.06 (adj +1.04) on $18.91, P(profit) 0.5833, adj growth 9.9 bp
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
| Charlie Coyle: 1+ goals YES | 21 | 0.273 | 0.256 | +0.051 | +0.034 | $4.73 | CBJ:OFFENSE_4PLUS | 0.2692 | EVIDENCE_STRONGER | D |
| Noah Ostlund: 1+ goals NO | 83 | 0.865 | 0.855 | +0.025 | +0.015 | $9.08 | BUF:SUPPRESSED | 0.2429 | EVIDENCE_STRONGER | D |
| Sean Monahan: 1+ goals YES | 20 | 0.240 | 0.227 | +0.029 | +0.016 | $2.22 | CBJ:OFFENSE_4PLUS | 0.2503 | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ assists NO | 60 | 0.680 | 0.632 | +0.063 | +0.015 | $4.47 | BUF:SUPPRESSED | 0.2423 | EVIDENCE_MIXED | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes; why: higher confidence-adjusted growth (14.80 vs 3.37 bp); relationships: KXNHLGOAL-26OCT01BUFCBJ-BUFNOSTLUND86-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CBJ offense suppressed (<= 2 goals)
- **Noah Ostlund: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01BUFCBJ-BUF3|no; why: higher confidence-adjusted growth (3.61 vs 2.27 bp); despite a smaller raw edge (+0.025 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.062); failure: BUF offense succeeds (4+ goals)
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (14.80 vs 3.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT01BUFCBJ-BUFNOSTLUND86-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: CBJ offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01BUFCBJ-BUF3|no; why: KXNHLSPREAD-26OCT01BUFCBJ-BUF3|no has the higher standalone adjusted growth (2.27 vs 2.24 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.155); relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT01BUFCBJ-BUFNOSTLUND86-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: BUF offense succeeds (4+ goals)

portfolios: A EV +2.32 (adj +1.17) on $18.87, P(profit) 0.4386, adj growth 10.9 bp · B EV +2.12 (adj +1.18) on $20.50, P(profit) 0.4223, adj growth 11.1 bp · C EV +1.84 (adj +1.06) on $22.18, P(profit) 0.273, adj growth 9.9 bp

## MIN @ NSH  ·  10000 joint draws  ·  344 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.431 / away 0.569

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
| Blake Coleman: 1+ goals YES | 23 | 0.272 | 0.261 | +0.030 | +0.018 | $2.59 | MIN:OFFENSE_4PLUS | 0.2742 | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 23 | 0.271 | 0.260 | +0.029 | +0.017 | $2.44 | MIN:OFFENSE_4PLUS | 0.2646 | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ goals YES | 18 | 0.216 | 0.206 | +0.026 | +0.015 | $2.09 | NSH:OFFENSE_4PLUS | 0.2665 | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 26 | 0.304 | 0.291 | +0.031 | +0.017 | $2.58 | NSH:OFFENSE_4PLUS | 0.2623 | EVIDENCE_STRONGER | D |
- **Blake Coleman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (3.90 vs 3.59 bp); relationships: KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-MINBCOLEMAN20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01MINNSH-MINBCOLEMAN20-1|yes has the higher standalone adjusted growth (3.90 vs 3.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.028); they share one thesis budget; relationships: KXNHLGOAL-26OCT01MINNSH-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: MIN offense suppressed (<= 2 goals)
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (3.38 vs 3.23 bp); despite a smaller raw edge (+0.026 vs +0.031/contract); relationships: KXNHLGOAL-26OCT01MINNSH-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: NSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes has the higher standalone adjusted growth (3.38 vs 3.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT01MINNSH-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: NSH offense suppressed (<= 2 goals)

portfolios: A EV +4.15 (adj +1.15) on $18.87, P(profit) 0.4895, adj growth 9.2 bp · B EV +1.19 (adj +0.70) on $9.70, P(profit) 0.5815, adj growth 6.6 bp · C EV +0.91 (adj +0.55) on $15.77, P(profit) 0.4079, adj growth 5.2 bp

## SEA @ CGY  ·  10000 joint draws  ·  398 bet sides mapped, 3 +EV candidates, 3 on card

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
| Brandon Montour: 1+ goals NO | 84 | 0.893 | 0.877 | +0.043 | +0.028 | $8.58 | SEA:SUPPRESSED | 0.25 | EVIDENCE_STRONGER | D |
| Jacob Melanson: 1+ goals YES | 9 | 0.123 | 0.112 | +0.027 | +0.016 | $1.87 | SEA:OFFENSE_4PLUS | 0.2665 | EVIDENCE_STRONGER | D |
| Jared McCann: 1+ goals NO | 72 | 0.757 | 0.746 | +0.023 | +0.012 | $5.04 | SEA:SUPPRESSED | 0.2482 | EVIDENCE_STRONGER | D |
- **Brandon Montour: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (13.36 vs 1.71 bp); relationships: KXNHLGOAL-26OCT01SEACGY-SEAJMELANSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: SEA offense succeeds (4+ goals)
- **Jacob Melanson: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (6.59 vs 1.29 bp); alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: SEA offense suppressed (<= 2 goals)
- **Jared McCann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (1.71 vs 0.81 bp); despite a smaller raw edge (+0.023 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT01SEACGY-SEAJMELANSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: SEA offense succeeds (4+ goals)

portfolios: A EV +1.41 (adj +0.85) on $17.91, P(profit) 0.7181, adj growth 7.9 bp · B EV +1.12 (adj +0.68) on $15.50, P(profit) 0.7181, adj growth 6.5 bp · C EV +0.19 (adj +0.10) on $6.14, P(profit) 0.7569, adj growth 1.0 bp

## CHI @ UTA  ·  10000 joint draws  ·  320 bet sides mapped, 8 +EV candidates, 4 on card

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
| Ryan Greene: 1+ goals YES | 12 | 0.166 | 0.153 | +0.039 | +0.026 | $3.19 | CHI:OFFENSE_4PLUS | 0.2422 | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 21 | 0.259 | 0.246 | +0.037 | +0.024 | $3.67 | UTA:OFFENSE_4PLUS | 0.2651 | EVIDENCE_STRONGER | D |
| Anders Lee: 1+ goals YES | 23 | 0.273 | 0.261 | +0.030 | +0.018 | $3.14 | UTA:OFFENSE_4PLUS | 0.2847 | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 66 | 0.776 | 0.694 | +0.101 | +0.018 | $8.91 | UTA:SUPPRESSED | 0.2441 | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01CHIUTA-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (13.19 vs 1.40 bp); despite a smaller raw edge (+0.039 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: CHI offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes; why: higher confidence-adjusted growth (7.22 vs 4.06 bp); relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); failure: UTA offense suppressed (<= 2 goals)
- **Anders Lee: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01CHIUTA-UTANSCHMALTZ8-1|yes; why: higher confidence-adjusted growth (4.06 vs 0.29 bp); alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.087); failure: UTA offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT01CHIUTA-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (3.41 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.087); failure: UTA offense succeeds (4+ goals)

portfolios: A EV +3.55 (adj +0.53) on $18.87, P(profit) 0.6438, adj growth 4.8 bp · B EV +3.32 (adj +1.54) on $18.91, P(profit) 0.4743, adj growth 14.4 bp · C EV +2.83 (adj +1.33) on $23.57, P(profit) 0.3827, adj growth 12.4 bp

## EDM @ VAN  ·  10000 joint draws  ·  328 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.352 / away 0.647

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
| Drew O'Connor: 1+ goals YES | 16 | 0.215 | 0.200 | +0.046 | +0.031 | $3.90 | VAN:OFFENSE_4PLUS | 0.2471 | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 69 | 0.831 | 0.736 | +0.126 | +0.031 | $9.08 | EDM:SUPPRESSED | 0.2299 | EVIDENCE_MIXED | D |
| Linus Karlsson: 1+ goals YES | 18 | 0.229 | 0.215 | +0.038 | +0.025 | $3.24 | VAN:OFFENSE_4PLUS | 0.2446 | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 21 | 0.257 | 0.244 | +0.035 | +0.022 | $3.16 | VAN:OFFENSE_4PLUS | 0.2482 | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01EDMVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (14.52 vs 8.62 bp); relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT01EDMVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: VAN offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01EDMVAN-EDM3|no; why: higher confidence-adjusted growth (10.36 vs 8.48 bp); relationships: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT01EDMVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: EDM offense succeeds (4+ goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (14.52 vs 8.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (14.52 vs 6.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT01EDMVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: VAN offense suppressed (<= 2 goals)

portfolios: A EV +5.38 (adj +0.83) on $18.87, P(profit) 0.7053, adj growth 7.5 bp · B EV +3.84 (adj +1.85) on $19.38, P(profit) 0.502, adj growth 17.5 bp · C EV +4.05 (adj +1.61) on $24.02, P(profit) 0.7328, adj growth 15.1 bp
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
| Kiefer Sherwood: 1+ goals YES | 15 | 0.215 | 0.198 | +0.057 | +0.039 | $4.64 | SJS:OFFENSE_4PLUS | 0.2535 | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 76 | 0.852 | 0.803 | +0.079 | +0.031 | $9.08 | SJS:WINS | 0.2381 | EVIDENCE_MIXED | D |
| Aleksander Barkov: 1+ assists NO | 52 | 0.692 | 0.570 | +0.154 | +0.033 | $7.91 | FLA:SUPPRESSED | 0.2433 | EVIDENCE_MIXED | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: higher confidence-adjusted growth (24.17 vs 11.90 bp); despite a smaller raw edge (+0.057 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT01FLASJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.112); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: SJS offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: higher confidence-adjusted growth (11.90 vs 8.24 bp); wins across more scripts (relative breadth 1.017 vs 0.517); relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.112); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: REINFORCING (phi 0.153); failure: FLA wins by 2+
- **Aleksander Barkov: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-FLA3|no has the higher standalone adjusted growth (11.90 vs 9.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.153); they share one thesis budget; relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.153); failure: FLA offense succeeds (4+ goals)

portfolios: A EV +3.40 (adj +0.78) on $18.87, P(profit) 0.6828, adj growth 7.2 bp · B EV +4.85 (adj +1.98) on $21.63, P(profit) 0.6905, adj growth 18.7 bp · C EV +2.93 (adj +1.70) on $15.60, P(profit) 0.2154, adj growth 15.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01FLASJ-SJ|yes == KXNHLGAME-26OCT01FLASJ-FLA|no

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
