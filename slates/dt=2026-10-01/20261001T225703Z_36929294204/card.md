# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-01T22:57:03Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +29.70 | +7.87 | +30.01 | 0.798 | -15.69 | -28.57 | 72.42 |
| B thesis-diversified (joint) ← card | 150.00 | +26.32 | +11.60 | +24.87 | 0.762 | -19.22 | -31.19 | 109.48 |
| C best expression per thesis | 150.00 | +23.94 | +9.68 | +23.22 | 0.767 | -17.71 | -28.35 | 91.59 |

## PHI @ NJD  ·  10000 joint draws  ·  318 bet sides mapped, 11 +EV candidates, 4 on card

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
| Noel Acciari: 1+ goals YES | 8 | 0.118 | 0.106 | +0.032 | +0.021 | $2.33 | PHI:OFFENSE_4PLUS | 0.2372 | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 11 | 0.146 | 0.136 | +0.029 | +0.019 | $2.25 | PHI:OFFENSE_4PLUS | 0.2457 | EVIDENCE_STRONGER | D |
| Dawson Mercer: 1+ goals YES | 15 | 0.192 | 0.180 | +0.033 | +0.021 | $2.81 | NJD:OFFENSE_4PLUS | 0.2773 | EVIDENCE_STRONGER | D |
| Stefan Noesen: 1+ goals YES | 10 | 0.131 | 0.122 | +0.025 | +0.016 | $1.92 | NJD:OFFENSE_4PLUS | 0.2369 | EVIDENCE_STRONGER | D |
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (11.56 vs 7.27 bp); relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT01PHINJ-NJSNOESEN11-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: PHI offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT01PHINJ-NJ|no; why: higher confidence-adjusted growth (7.27 vs 1.35 bp); despite a smaller raw edge (+0.029 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT01PHINJ-NJSNOESEN11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: PHI offense suppressed (<= 2 goals)
- **Dawson Mercer: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01PHINJ-NJTMEIER28-1|yes; why: higher confidence-adjusted growth (7.09 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT01PHINJ-NJSNOESEN11-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NJD offense suppressed (<= 2 goals)
- **Stefan Noesen: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes has the higher standalone adjusted growth (7.09 vs 5.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NJD offense suppressed (<= 2 goals)

portfolios: A EV +2.49 (adj +0.55) on $19.43, P(profit) 0.5701, adj growth 5.0 bp · B EV +2.47 (adj +1.58) on $9.31, P(profit) 0.4769, adj growth 14.8 bp · C EV +3.13 (adj +1.19) on $18.09, P(profit) 0.6513, adj growth 11.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01PHINJ-PHI|yes == KXNHLGAME-26OCT01PHINJ-NJ|no

## TBL @ NYR  ·  10000 joint draws  ·  350 bet sides mapped, 18 +EV candidates, 3 on card

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
| John Carlson: 1+ assists NO | 55 | 0.745 | 0.615 | +0.178 | +0.048 | $9.14 | TBL:SUPPRESSED | 0.2284 | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 77 | 0.848 | 0.806 | +0.066 | +0.024 | $9.14 | NYR:WINS | 0.2458 | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 1.5 goals NO | 66 | 0.748 | 0.702 | +0.073 | +0.026 | $3.28 | NYR:WINS | 0.2785 | EVIDENCE_MIXED | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01TBNYR-TB3|no; why: higher confidence-adjusted growth (20.29 vs 7.54 bp); relationships: KXNHLSPREAD-26OCT01TBNYR-TB3|no: MOSTLY_INDEPENDENT (phi 0.129); KXNHLSPREAD-26OCT01TBNYR-TB2|no: MOSTLY_INDEPENDENT (phi 0.146); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01TBNYR-TB2|no; why: higher confidence-adjusted growth (7.54 vs 6.78 bp); despite a smaller raw edge (+0.066 vs +0.073/contract); relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.129); KXNHLSPREAD-26OCT01TBNYR-TB2|no: DUPLICATIVE (phi 0.73); failure: TBL wins by 2+
- **Tampa Bay wins by over 1.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01TBNYR-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT01TBNYR-TB3|no has the higher standalone adjusted growth (7.54 vs 6.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.730); they share one thesis budget; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLSPREAD-26OCT01TBNYR-TB3|no: DUPLICATIVE (phi 0.73); failure: TBL wins by 2+

portfolios: A EV +5.90 (adj +1.10) on $19.43, P(profit) 0.699, adj growth 10.0 bp · B EV +3.98 (adj +1.17) on $21.55, P(profit) 0.6519, adj growth 11.3 bp · C EV +3.92 (adj +1.13) on $19.75, P(profit) 0.6519, adj growth 10.9 bp
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
| Charlie Coyle: 1+ goals YES | 21 | 0.273 | 0.256 | +0.051 | +0.034 | $4.65 | CBJ:OFFENSE_4PLUS | 0.2692 | EVIDENCE_STRONGER | D |
| Conor Garland: 1+ goals NO | 82 | 0.853 | 0.844 | +0.023 | +0.013 | $8.98 | CBJ:SUPPRESSED | 0.2438 | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ assists NO | 60 | 0.680 | 0.632 | +0.063 | +0.015 | $4.78 | BUF:SUPPRESSED | 0.2423 | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ goals NO | 65 | 0.691 | 0.679 | +0.025 | +0.013 | $4.43 | BUF:SUPPRESSED | 0.2423 | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT01BUFCBJ-BUF|no; why: higher confidence-adjusted growth (14.80 vs 2.43 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: CBJ offense suppressed (<= 2 goals)
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01BUFCBJ-CBJVNICHUSHKIN43-1|no; why: higher confidence-adjusted growth (2.84 vs 2.08 bp); despite a smaller raw edge (+0.023 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.022); failure: CBJ offense succeeds (4+ goals)
- **Tage Thompson: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT01BUFCBJ-BUF|no; why: KXNHLGAME-26OCT01BUFCBJ-BUF|no has the higher standalone adjusted growth (2.43 vs 2.24 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.198); relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT01BUFCBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: BUF offense succeeds (4+ goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT01BUFCBJ-BUF|no; why: KXNHLGAME-26OCT01BUFCBJ-BUF|no has the higher standalone adjusted growth (2.43 vs 1.74 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.200); relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT01BUFCBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: BUF offense succeeds (4+ goals)

portfolios: A EV +2.34 (adj +1.04) on $19.43, P(profit) 0.4721, adj growth 9.7 bp · B EV +1.98 (adj +1.08) on $22.84, P(profit) 0.5558, adj growth 10.1 bp · C EV +2.10 (adj +1.05) on $16.89, P(profit) 0.536, adj growth 9.8 bp
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
| Ryan O'Reilly: 1+ goals YES | 25 | 0.299 | 0.285 | +0.035 | +0.022 | $3.30 | NSH:OFFENSE_4PLUS | 0.2605 | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 23 | 0.274 | 0.262 | +0.032 | +0.020 | $2.83 | MIN:OFFENSE_4PLUS | 0.2559 | EVIDENCE_STRONGER | D |
| Jared Spurgeon: 1+ goals NO | 91 | 0.935 | 0.927 | +0.019 | +0.012 | $9.14 | MIN:SUPPRESSED | 0.242 | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ goals YES | 18 | 0.212 | 0.203 | +0.022 | +0.013 | $1.70 | NSH:OFFENSE_4PLUS | 0.2658 | EVIDENCE_STRONGER | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes; why: higher confidence-adjusted growth (5.46 vs 2.23 bp); relationships: KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: NSH offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (4.54 vs 1.33 bp); relationships: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: MIN offense suppressed (<= 2 goals)
- **Jared Spurgeon: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT01MINNSH-MINMSHABANOV49-1|no; why: higher confidence-adjusted growth (3.99 vs 0.00 bp); despite a smaller raw edge (+0.019 vs +0.053/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: MIN offense succeeds (4+ goals)
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes has the higher standalone adjusted growth (5.46 vs 2.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NSH offense suppressed (<= 2 goals)

portfolios: A EV +1.68 (adj +1.01) on $14.02, P(profit) 0.5184, adj growth 9.2 bp · B EV +1.21 (adj +0.74) on $16.97, P(profit) 0.5723, adj growth 7.0 bp · C EV +0.88 (adj +0.54) on $6.60, P(profit) 0.4891, adj growth 5.1 bp

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
| Brandon Montour: 1+ goals NO | 83 | 0.892 | 0.875 | +0.052 | +0.036 | $6.90 | SEA:SUPPRESSED | 0.2498 | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 10 | 0.136 | 0.126 | +0.030 | +0.019 | $2.42 | SEA:OFFENSE_4PLUS | 0.2597 | EVIDENCE_STRONGER | D |
| Jared McCann: 1+ assists NO | 64 | 0.731 | 0.683 | +0.074 | +0.027 | $6.80 | SEA:SUPPRESSED | 0.2509 | EVIDENCE_MIXED | D |
| Adam Klapka: 1+ goals YES | 10 | 0.131 | 0.122 | +0.025 | +0.015 | $1.89 | CGY:OFFENSE_4PLUS | 0.2324 | EVIDENCE_STRONGER | D |
- **Brandon Montour: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (21.16 vs 6.93 bp); despite a smaller raw edge (+0.053 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: SEA offense succeeds (4+ goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01SEACGY-SEAMBENIERS10-1|yes; why: higher confidence-adjusted growth (8.48 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no: INTENTIONAL_DIVERSIFIER (phi -0.066); KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: SEA offense suppressed (<= 2 goals)
- **Jared McCann: 1+ assists NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (6.93 vs 1.62 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.066); KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: SEA offense succeeds (4+ goals)
- **Adam Klapka: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01SEACGY-CGYMFROST16-1|yes; why: higher confidence-adjusted growth (5.48 vs 2.08 bp); relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: CGY offense suppressed (<= 2 goals)

portfolios: A EV +2.61 (adj +1.47) on $19.43, P(profit) 0.2516, adj growth 13.9 bp · B EV +2.31 (adj +1.29) on $18.01, P(profit) 0.7514, adj growth 12.3 bp · C EV +2.05 (adj +0.99) on $14.60, P(profit) 0.7772, adj growth 9.3 bp

## CHI @ UTA  ·  10000 joint draws  ·  320 bet sides mapped, 9 +EV candidates, 4 on card

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
| Ryan Greene: 1+ goals YES | 12 | 0.166 | 0.153 | +0.039 | +0.026 | $3.30 | CHI:OFFENSE_4PLUS | 0.2422 | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 21 | 0.259 | 0.246 | +0.038 | +0.024 | $3.53 | UTA:OFFENSE_4PLUS | 0.2642 | EVIDENCE_STRONGER | D |
| Anders Lee: 1+ goals YES | 23 | 0.274 | 0.262 | +0.031 | +0.019 | $2.95 | UTA:OFFENSE_4PLUS | 0.2847 | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 62 | 0.745 | 0.657 | +0.109 | +0.021 | $7.95 | CHI:SUPPRESSED | 0.264 | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01CHIUTA-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (13.19 vs 2.36 bp); despite a smaller raw edge (+0.039 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.037); failure: CHI offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes; why: higher confidence-adjusted growth (7.31 vs 4.30 bp); relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: UTA offense suppressed (<= 2 goals)
- **Anders Lee: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT01CHIUTA-10|yes; why: higher confidence-adjusted growth (4.30 vs 0.37 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.855 vs 0.309); alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: UTA offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01CHIUTA-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (4.14 vs 1.13 bp); relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CHI offense succeeds (4+ goals)

portfolios: A EV +3.74 (adj +0.65) on $19.43, P(profit) 0.6436, adj growth 5.9 bp · B EV +3.35 (adj +1.55) on $17.73, P(profit) 0.4788, adj growth 14.6 bp · C EV +3.20 (adj +1.43) on $24.69, P(profit) 0.3429, adj growth 13.4 bp

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
| Connor McDavid: 1+ assists NO | 31 | 0.476 | 0.365 | +0.151 | +0.040 | $4.50 | EDM:SUPPRESSED | 0.2287 | EVIDENCE_MIXED | D |
| Drew O'Connor: 1+ goals YES | 16 | 0.215 | 0.200 | +0.046 | +0.031 | $3.98 | VAN:OFFENSE_4PLUS | 0.2471 | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 67 | 0.831 | 0.717 | +0.146 | +0.031 | $9.14 | EDM:SUPPRESSED | 0.2297 | EVIDENCE_MIXED | D |
| Marco Rossi: 1+ goals YES | 21 | 0.257 | 0.244 | +0.035 | +0.022 | $3.14 | VAN:OFFENSE_4PLUS | 0.2482 | EVIDENCE_STRONGER | D |
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (15.80 vs 9.94 bp); relationships: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: DUPLICATIVE (phi 0.43); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: EDM offense succeeds (4+ goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01EDMVAN-EDM3|no; why: higher confidence-adjusted growth (14.52 vs 8.48 bp); despite a smaller raw edge (+0.046 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: VAN offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no; why: second expression of the same thesis: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no has the higher standalone adjusted growth (15.80 vs 9.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.430); they share one thesis budget; relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: DUPLICATIVE (phi 0.43); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: EDM offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (14.52 vs 6.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.011); failure: VAN offense suppressed (<= 2 goals)

portfolios: A EV +5.44 (adj +1.08) on $19.43, P(profit) 0.6568, adj growth 10.0 bp · B EV +5.62 (adj +2.01) on $20.75, P(profit) 0.6604, adj growth 18.9 bp · C EV +4.44 (adj +1.66) on $24.69, P(profit) 0.5862, adj growth 15.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01EDMVAN-VAN|yes == KXNHLGAME-26OCT01EDMVAN-EDM|no

## FLA @ SJS  ·  10000 joint draws  ·  368 bet sides mapped, 22 +EV candidates, 3 on card

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
| Aleksander Barkov: 1+ assists NO | 51 | 0.692 | 0.567 | +0.164 | +0.040 | $9.10 | FLA:SUPPRESSED | 0.2433 | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 76 | 0.852 | 0.803 | +0.079 | +0.031 | $9.10 | SJS:WINS | 0.2381 | EVIDENCE_MIXED | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: higher confidence-adjusted growth (24.17 vs 11.90 bp); despite a smaller raw edge (+0.057 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.112); failure: SJS offense suppressed (<= 2 goals)
- **Aleksander Barkov: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: higher confidence-adjusted growth (13.76 vs 11.90 bp); relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.153); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: higher confidence-adjusted growth (11.90 vs 8.24 bp); wins across more scripts (relative breadth 1.017 vs 0.517); relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.112); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: REINFORCING (phi 0.153); failure: FLA wins by 2+

portfolios: A EV +5.51 (adj +0.97) on $19.43, P(profit) 0.6212, adj growth 8.7 bp · B EV +5.41 (adj +2.18) on $22.84, P(profit) 0.6905, adj growth 20.6 bp · C EV +4.22 (adj +1.69) on $24.69, P(profit) 0.6784, adj growth 16.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01FLASJ-FLA|no == KXNHLGAME-26OCT01FLASJ-SJ|yes

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
