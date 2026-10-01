# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-01T17:12:12Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +26.10 | +6.47 | +26.01 | 0.781 | -15.81 | -26.62 | 59.33 |
| B thesis-diversified (joint) ← card | 150.00 | +20.57 | +8.82 | +19.40 | 0.747 | -17.50 | -27.72 | 83.69 |
| C best expression per thesis | 150.00 | +17.57 | +8.36 | +16.60 | 0.701 | -22.03 | -32.31 | 78.68 |

## PHI @ NJD  ·  10000 joint draws  ·  318 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.604 / away 0.396

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_PHI_win | p_overtime | goals | shots NJD/PHI | NJD/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.59 | 0.41 | 0.00 | 5.97 | 27.0/26.6 | 23.5/23.1 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.109 | 0.63 | 0.37 | 0.00 | 5.94 | 31.9/20.9 | 18.1/27.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.49 | 5.83 | 26.9/26.6 | 23.4/23.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.58 | 0.42 | 0.47 | 5.85 | 32.1/21.1 | 18.1/28.8 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.46 | 2.81 | 25.5/25.1 | 23.6/24.0 | even strength |
| NJD shot control · low event (<=4) · decided (2+) | 0.063 | 0.62 | 0.38 | 0.00 | 3.41 | 30.9/19.9 | 18.4/28.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Sean Couturier: 1+ goals YES | 11 | 0.150 | 0.137 | +0.033 | +0.020 | $2.31 | PHI:OFFENSE_4PLUS | 0.2513 | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 12 | 0.153 | 0.144 | +0.026 | +0.017 | $1.95 | NJD:OFFENSE_4PLUS | 0.2547 | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 72 | 0.769 | 0.753 | +0.035 | +0.019 | $8.04 | NJD:SUPPRESSED | 0.2172 | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 77 | 0.810 | 0.798 | +0.028 | +0.015 | $8.04 | PHI:SUPPRESSED | 0.228 | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT01PHINJ-PHI|yes; why: higher confidence-adjusted growth (8.62 vs 1.33 bp); despite a smaller raw edge (+0.033 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT01PHINJ-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: PHI offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes; why: higher confidence-adjusted growth (5.28 vs 0.03 bp); alternative not eligible: confidence-adjusted EV +0.0015 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT01PHINJ-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: NJD offense suppressed (<= 2 goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01PHINJ-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (4.08 vs 2.53 bp); relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT01PHINJ-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: NJD offense succeeds (4+ goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT01PHINJ-6|no; why: higher confidence-adjusted growth (3.01 vs 0.44 bp); despite a smaller raw edge (+0.028 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.985 vs 0.755); alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: PHI offense succeeds (4+ goals)

portfolios: A EV +2.08 (adj +0.48) on $19.89, P(profit) 0.6612, adj growth 4.5 bp · B EV +1.72 (adj +1.02) on $20.33, P(profit) 0.7189, adj growth 9.6 bp · C EV +1.64 (adj +0.92) on $22.67, P(profit) 0.6784, adj growth 8.5 bp

## TBL @ NYR  ·  10000 joint draws  ·  350 bet sides mapped, 17 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.431 / away 0.569

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
| John Carlson: 1+ assists NO | 54 | 0.742 | 0.598 | +0.184 | +0.040 | $8.37 | TBL:SUPPRESSED | 0.2322 | EVIDENCE_MIXED | D |
| New York R wins YES | 43 | 0.525 | 0.480 | +0.077 | +0.033 | $5.33 | NYR:WINS | 0.2421 | EVIDENCE_MIXED | B |
| Pavel Dorofeyev: 1+ assists NO | 76 | 0.842 | 0.794 | +0.070 | +0.021 | $8.37 | NYR:SUPPRESSED | 0.2366 | EVIDENCE_MIXED | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT01TBNYR-NYR|yes; why: higher confidence-adjusted growth (14.32 vs 9.40 bp); relationships: KXNHLGAME-26OCT01TBNYR-NYR|yes: REINFORCING (phi 0.187); KXNHLAST-26OCT01TBNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: TBL offense succeeds (4+ goals)
- **New York R wins YES** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLGAME-26OCT01TBNYR-TB|no; why: best adjusted growth among the thesis's expressions; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: REINFORCING (phi 0.187); KXNHLAST-26OCT01TBNYR-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.131); failure: TBL wins (incl. OT/SO)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT01TBNYR-4|no; why: higher confidence-adjusted growth (5.50 vs 0.15 bp); wins across more scripts (relative breadth 0.999 vs 0.347); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGAME-26OCT01TBNYR-NYR|yes: INTENTIONAL_DIVERSIFIER (phi -0.131); failure: NYR offense succeeds (4+ goals)

portfolios: A EV +5.46 (adj +0.94) on $19.89, P(profit) 0.722, adj growth 8.7 bp · B EV +4.44 (adj +1.22) on $22.06, P(profit) 0.7844, adj growth 11.7 bp · C EV +4.43 (adj +1.18) on $16.28, P(profit) 0.7415, adj growth 11.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01TBNYR-TB|no == KXNHLGAME-26OCT01TBNYR-NYR|yes

## BUF @ CBJ  ·  10000 joint draws  ·  358 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.490 / away 0.510

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
| Zach Metsa: 1+ goals NO | 94 | 0.967 | 0.958 | +0.023 | +0.014 | $8.81 | DIFFUSE | 0.2432 | EVIDENCE_STRONGER | D |
| Kent Johnson: 1+ goals NO | 78 | 0.823 | 0.811 | +0.031 | +0.019 | $8.81 | CBJ:SUPPRESSED | 0.2444 | EVIDENCE_STRONGER | D |
| Sean Monahan: 1+ goals YES | 20 | 0.240 | 0.227 | +0.029 | +0.016 | $2.19 | CBJ:OFFENSE_4PLUS | 0.2503 | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 23 | 0.273 | 0.259 | +0.031 | +0.016 | $2.25 | CBJ:OFFENSE_4PLUS | 0.2692 | EVIDENCE_STRONGER | D |
- **Zach Metsa: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: BUF offense succeeds (4+ goals)
- **Kent Johnson: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01BUFCBJ-CBJVNICHUSHKIN43-1|no; why: higher confidence-adjusted growth (4.87 vs 0.48 bp); despite a smaller raw edge (+0.031 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01BUFCBJ-BUFZMETSA73-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: CBJ offense succeeds (4+ goals)
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (3.37 vs 3.07 bp); despite a smaller raw edge (+0.029 vs +0.031/contract); relationships: KXNHLGOAL-26OCT01BUFCBJ-BUFZMETSA73-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT01BUFCBJ-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes has the higher standalone adjusted growth (3.37 vs 3.07 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT01BUFCBJ-BUFZMETSA73-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT01BUFCBJ-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CBJ offense suppressed (<= 2 goals)

portfolios: A EV +1.79 (adj +0.76) on $19.89, P(profit) 0.4236, adj growth 7.0 bp · B EV +1.14 (adj +0.66) on $22.06, P(profit) 0.3678, adj growth 6.3 bp · C EV +1.07 (adj +0.63) on $25.65, P(profit) 0.6429, adj growth 6.0 bp

## MIN @ NSH  ·  10000 joint draws  ·  344 bet sides mapped, 2 +EV candidates, 2 on card

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
| Jared Spurgeon: 1+ goals NO | 91 | 0.934 | 0.927 | +0.019 | +0.011 | $8.82 | DIFFUSE | 0.2546 | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 23 | 0.271 | 0.260 | +0.029 | +0.017 | $2.44 | MIN:OFFENSE_4PLUS | 0.2646 | EVIDENCE_STRONGER | D |
- **Jared Spurgeon: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: MIN offense succeeds (4+ goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT01MINNSH-9|yes; why: higher confidence-adjusted growth (3.59 vs 1.05 bp); despite a smaller raw edge (+0.029 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.914 vs 0.377); alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: MIN offense suppressed (<= 2 goals)

portfolios: A EV +0.62 (adj +0.37) on $11.76, P(profit) 0.2714, adj growth 3.4 bp · B EV +0.47 (adj +0.28) on $11.26, P(profit) 0.255, adj growth 2.7 bp · C EV +0.55 (adj +0.33) on $13.09, P(profit) 0.255, adj growth 3.1 bp

## SEA @ CGY  ·  10000 joint draws  ·  396 bet sides mapped, 3 +EV candidates, 3 on card

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
| Brandon Montour: 1+ goals NO | 84 | 0.893 | 0.876 | +0.043 | +0.026 | $8.34 | SEA:SUPPRESSED | 0.25 | EVIDENCE_STRONGER | D |
| Jacob Melanson: 1+ goals YES | 9 | 0.123 | 0.112 | +0.027 | +0.016 | $1.82 | SEA:OFFENSE_4PLUS | 0.2665 | EVIDENCE_STRONGER | D |
| Jared McCann: 1+ goals NO | 72 | 0.757 | 0.746 | +0.023 | +0.012 | $4.90 | SEA:SUPPRESSED | 0.2482 | EVIDENCE_STRONGER | D |
- **Brandon Montour: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (12.17 vs 1.71 bp); relationships: KXNHLGOAL-26OCT01SEACGY-SEAJMELANSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: SEA offense succeeds (4+ goals)
- **Jacob Melanson: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (6.59 vs 1.29 bp); alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: SEA offense suppressed (<= 2 goals)
- **Jared McCann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (1.71 vs 0.81 bp); despite a smaller raw edge (+0.023 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT01SEACGY-SEAJMELANSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: SEA offense succeeds (4+ goals)

portfolios: A EV +1.49 (adj +0.89) on $18.88, P(profit) 0.7181, adj growth 8.2 bp · B EV +1.09 (adj +0.65) on $15.06, P(profit) 0.7181, adj growth 6.2 bp · C EV +0.19 (adj +0.10) on $6.10, P(profit) 0.7569, adj growth 1.0 bp

## CHI @ UTA  ·  10000 joint draws  ·  314 bet sides mapped, 5 +EV candidates, 4 on card

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
| Ryan Greene: 1+ goals YES | 12 | 0.166 | 0.153 | +0.039 | +0.026 | $3.13 | CHI:OFFENSE_4PLUS | 0.2422 | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 62 | 0.745 | 0.657 | +0.109 | +0.021 | $7.62 | CHI:SUPPRESSED | 0.264 | EVIDENCE_MIXED | D |
| Vincent Trocheck: 1+ assists NO | 66 | 0.772 | 0.693 | +0.096 | +0.017 | $7.26 | UTA:SUPPRESSED | 0.2452 | EVIDENCE_MIXED | D |
| Anders Lee: 1+ goals YES | 24 | 0.280 | 0.268 | +0.028 | +0.015 | $2.47 | UTA:OFFENSE_4PLUS | 0.2853 | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01CHIUTA-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (13.19 vs 0.86 bp); despite a smaller raw edge (+0.039 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.037); KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01CHIUTA-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (4.14 vs 0.34 bp); alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CHI offense succeeds (4+ goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT01CHIUTA-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (2.84 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.097); failure: UTA offense succeeds (4+ goals)
- **Anders Lee: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01CHIUTA-UTADGUENTHER11-1|yes; why: higher confidence-adjusted growth (2.60 vs 0.21 bp); despite a smaller raw edge (+0.028 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0048 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.097); failure: UTA offense suppressed (<= 2 goals)

portfolios: A EV +3.52 (adj +1.32) on $19.89, P(profit) 0.7426, adj growth 12.3 bp · B EV +3.56 (adj +1.22) on $20.47, P(profit) 0.7426, adj growth 11.5 bp · C EV +3.22 (adj +1.36) on $25.41, P(profit) 0.7447, adj growth 12.8 bp

## EDM @ VAN  ·  10000 joint draws  ·  340 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.342 / away 0.658

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
| Leon Draisaitl: 1+ goals NO | 54 | 0.632 | 0.608 | +0.074 | +0.050 | $8.82 | EDM:SUPPRESSED | 0.2333 | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 21 | 0.261 | 0.247 | +0.039 | +0.025 | $3.42 | VAN:OFFENSE_4PLUS | 0.2435 | EVIDENCE_STRONGER | D |
| Drew O'Connor: 1+ goals YES | 17 | 0.213 | 0.200 | +0.034 | +0.020 | $2.63 | VAN:OFFENSE_4PLUS | 0.2334 | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 33 | 0.441 | 0.365 | +0.095 | +0.020 | $2.29 | EDM:SUPPRESSED | 0.2333 | EVIDENCE_MIXED | D |
- **Leon Draisaitl: 1+ goals NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01EDMVAN-VAN3|yes; why: higher confidence-adjusted growth (22.49 vs 5.42 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.011 vs 0.472); relationships: KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: REINFORCING (phi 0.158); failure: EDM offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes; why: higher confidence-adjusted growth (8.00 vs 5.97 bp); relationships: KXNHLGOAL-26OCT01EDMVAN-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: VAN offense suppressed (<= 2 goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes has the higher standalone adjusted growth (8.00 vs 5.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT01EDMVAN-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: VAN offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01EDMVAN-EDMLDRAISAITL29-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT01EDMVAN-EDMLDRAISAITL29-1|no has the higher standalone adjusted growth (22.49 vs 3.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.158); they share one thesis budget; relationships: KXNHLGOAL-26OCT01EDMVAN-EDMLDRAISAITL29-1|no: REINFORCING (phi 0.158); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: EDM offense succeeds (4+ goals)

portfolios: A EV +5.50 (adj +0.80) on $19.89, P(profit) 0.6111, adj growth 7.1 bp · B EV +2.91 (adj +1.61) on $17.16, P(profit) 0.5142, adj growth 15.3 bp · C EV +2.49 (adj +1.52) on $15.15, P(profit) 0.7278, adj growth 14.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01EDMVAN-EDM|no == KXNHLGAME-26OCT01EDMVAN-VAN|yes

## FLA @ SJS  ·  10000 joint draws  ·  366 bet sides mapped, 20 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.429 / away 0.571

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
| Kiefer Sherwood: 1+ goals YES | 15 | 0.224 | 0.202 | +0.065 | +0.043 | $4.79 | SJS:OFFENSE_4PLUS | 0.2695 | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 76 | 0.852 | 0.804 | +0.079 | +0.031 | $8.82 | SJS:WINS | 0.2408 | EVIDENCE_MIXED | D |
| Aleksander Barkov: 1+ assists NO | 52 | 0.697 | 0.572 | +0.160 | +0.035 | $7.99 | FLA:SUPPRESSED | 0.2565 | EVIDENCE_MIXED | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: higher confidence-adjusted growth (29.37 vs 11.98 bp); despite a smaller raw edge (+0.065 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT01FLASJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.112); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: MOSTLY_INDEPENDENT (phi 0.024); failure: SJS offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: higher confidence-adjusted growth (11.98 vs 11.40 bp); despite a smaller raw edge (+0.079 vs +0.081/contract); wins across more scripts (relative breadth 1.031 vs 0.521); relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.112); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: REINFORCING (phi 0.162); failure: FLA wins by 2+
- **Aleksander Barkov: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01FLASJ-FLAABARKOV16-1|no; why: KXNHLGOAL-26OCT01FLASJ-FLAABARKOV16-1|no has the higher standalone adjusted growth (12.27 vs 10.71 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.006); relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.162); failure: FLA offense succeeds (4+ goals)

portfolios: A EV +5.65 (adj +0.91) on $19.89, P(profit) 0.6294, adj growth 8.1 bp · B EV +5.25 (adj +2.16) on $21.60, P(profit) 0.692, adj growth 20.4 bp · C EV +3.98 (adj +2.32) on $25.65, P(profit) 0.7488, adj growth 21.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01FLASJ-SJ|yes == KXNHLGAME-26OCT01FLASJ-FLA|no

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
