# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-01T18:51:49Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +29.11 | +7.46 | +27.97 | 0.748 | -23.64 | -35.97 | 66.03 |
| B thesis-diversified (joint) ← card | 150.00 | +20.49 | +9.68 | +19.10 | 0.722 | -21.80 | -32.22 | 91.21 |
| C best expression per thesis | 149.99 | +19.43 | +9.97 | +17.95 | 0.649 | -37.74 | -52.41 | 89.37 |

## PHI @ NJD  ·  10000 joint draws  ·  318 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.604 / away 0.396

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
| Sean Couturier: 1+ goals YES | 11 | 0.152 | 0.139 | +0.035 | +0.022 | $2.87 | PHI:OFFENSE_4PLUS | 0.2355 | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 12 | 0.153 | 0.143 | +0.025 | +0.016 | $2.15 | NJD:OFFENSE_4PLUS | 0.2644 | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 72 | 0.769 | 0.754 | +0.035 | +0.020 | $9.50 | NJD:SUPPRESSED | 0.2245 | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 77 | 0.811 | 0.798 | +0.028 | +0.016 | $9.44 | PHI:SUPPRESSED | 0.2272 | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT01PHINJ-PHI|yes; why: higher confidence-adjusted growth (10.20 vs 1.88 bp); despite a smaller raw edge (+0.035 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01PHINJ-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: PHI offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes; why: higher confidence-adjusted growth (4.95 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0003 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT01PHINJ-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: NJD offense suppressed (<= 2 goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01PHINJ-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (4.50 vs 3.55 bp); despite a smaller raw edge (+0.035 vs +0.102/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT01PHINJ-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: NJD offense succeeds (4+ goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT01PHINJ-6|no; why: higher confidence-adjusted growth (3.13 vs 0.70 bp); despite a smaller raw edge (+0.028 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.984 vs 0.753); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT01PHINJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT01PHINJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: PHI offense succeeds (4+ goals)

portfolios: A EV +3.09 (adj +1.03) on $20.02, P(profit) 0.4887, adj growth 9.4 bp · B EV +2.08 (adj +1.26) on $23.96, P(profit) 0.7248, adj growth 11.8 bp · C EV +3.11 (adj +1.77) on $40.60, P(profit) 0.6778, adj growth 15.7 bp

## TBL @ NYR  ·  10000 joint draws  ·  350 bet sides mapped, 13 +EV candidates, 3 on card

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
| New York R wins YES | 43 | 0.525 | 0.480 | +0.077 | +0.033 | $6.40 | NYR:WINS | 0.2421 | EVIDENCE_MIXED | B |
| Pavel Dorofeyev: 1+ assists NO | 76 | 0.842 | 0.794 | +0.070 | +0.021 | $9.10 | NYR:SUPPRESSED | 0.2366 | EVIDENCE_MIXED | D |
| Victor Hedman: 1+ assists NO | 71 | 0.822 | 0.746 | +0.097 | +0.021 | $9.10 | TBL:SUPPRESSED | 0.2342 | EVIDENCE_MIXED | D |
- **New York R wins YES** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLGAME-26OCT01TBNYR-TB|no; why: best adjusted growth among the thesis's expressions; relationships: KXNHLAST-26OCT01TBNYR-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.131); KXNHLAST-26OCT01TBNYR-TBVHEDMAN77-1|no: MOSTLY_INDEPENDENT (phi 0.122); failure: TBL wins (incl. OT/SO)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT01TBNYR-4|no; why: higher confidence-adjusted growth (5.50 vs 0.15 bp); wins across more scripts (relative breadth 0.999 vs 0.347); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGAME-26OCT01TBNYR-NYR|yes: INTENTIONAL_DIVERSIFIER (phi -0.131); KXNHLAST-26OCT01TBNYR-TBVHEDMAN77-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: NYR offense succeeds (4+ goals)
- **Victor Hedman: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT01TBNYR-NYR|yes; why: second expression of the same thesis: KXNHLGAME-26OCT01TBNYR-NYR|yes has the higher standalone adjusted growth (9.40 vs 5.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.122); they share one thesis budget; relationships: KXNHLGAME-26OCT01TBNYR-NYR|yes: MOSTLY_INDEPENDENT (phi 0.122); KXNHLAST-26OCT01TBNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: TBL offense succeeds (4+ goals)

portfolios: A EV +4.72 (adj +0.56) on $20.02, P(profit) 0.722, adj growth 4.9 bp · B EV +3.15 (adj +0.98) on $24.60, P(profit) 0.5077, adj growth 9.4 bp · C EV +2.16 (adj +0.91) on $12.47, P(profit) 0.5246, adj growth 8.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01TBNYR-TB|no == KXNHLGAME-26OCT01TBNYR-NYR|yes

## BUF @ CBJ  ·  10000 joint draws  ·  358 bet sides mapped, 3 +EV candidates, 3 on card

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
| Charlie Coyle: 1+ goals YES | 20 | 0.273 | 0.251 | +0.062 | +0.040 | $5.75 | CBJ:OFFENSE_4PLUS | 0.2692 | EVIDENCE_STRONGER | D |
| Sean Monahan: 1+ goals YES | 20 | 0.240 | 0.227 | +0.029 | +0.016 | $2.35 | CBJ:OFFENSE_4PLUS | 0.2503 | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 65 | 0.691 | 0.679 | +0.025 | +0.013 | $4.54 | BUF:SUPPRESSED | 0.2423 | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes; why: higher confidence-adjusted growth (20.47 vs 3.37 bp); relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: CBJ offense suppressed (<= 2 goals)
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (20.47 vs 3.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.024); failure: CBJ offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01BUFCBJ-CBJ2|yes; why: higher confidence-adjusted growth (1.74 vs 1.03 bp); despite a smaller raw edge (+0.025 vs +0.039/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.991 vs 0.517); alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT01BUFCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: BUF offense succeeds (4+ goals)

portfolios: A EV +3.06 (adj +1.90) on $18.86, P(profit) 0.3966, adj growth 17.2 bp · B EV +2.17 (adj +1.35) on $12.64, P(profit) 0.3966, adj growth 12.6 bp · C EV +3.23 (adj +2.05) on $18.16, P(profit) 0.273, adj growth 18.1 bp

## MIN @ NSH  ·  10000 joint draws  ·  344 bet sides mapped, 4 +EV candidates, 4 on card

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
| Ryan O'Reilly: 1+ goals YES | 25 | 0.304 | 0.284 | +0.041 | +0.021 | $2.95 | NSH:OFFENSE_4PLUS | 0.2623 | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 23 | 0.271 | 0.260 | +0.029 | +0.017 | $2.75 | MIN:OFFENSE_4PLUS | 0.2646 | EVIDENCE_STRONGER | D |
| Nashville over 4.5 goals scored YES | 17 | 0.223 | 0.194 | +0.043 | +0.014 | $1.25 | NSH:OFFENSE_4PLUS | 0.3842 | EVIDENCE_MIXED | D |
| Jonathan Marchessault: 1+ assists YES | 26 | 0.358 | 0.285 | +0.085 | +0.011 | $1.03 | NSH:OFFENSE_4PLUS | 0.258 | EVIDENCE_MIXED | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT01MINNSH-NSH5|yes; why: higher confidence-adjusted growth (5.08 vs 3.00 bp); despite a smaller raw edge (+0.041 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.913 vs 0.541); relationships: KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLTEAMTOTAL-26OCT01MINNSH-NSH5|yes: REINFORCING (phi 0.221); KXNHLAST-26OCT01MINNSH-NSHJMARCHESSAULT81-1|yes: MOSTLY_INDEPENDENT (phi 0.083); failure: NSH offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT01MINNSH-9|yes; why: higher confidence-adjusted growth (3.59 vs 1.05 bp); despite a smaller raw edge (+0.029 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.914 vs 0.377); alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLTEAMTOTAL-26OCT01MINNSH-NSH5|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT01MINNSH-NSHJMARCHESSAULT81-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: MIN offense suppressed (<= 2 goals)
- **Nashville over 4.5 goals scored YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes has the higher standalone adjusted growth (5.08 vs 3.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.221); they share one thesis budget; relationships: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: REINFORCING (phi 0.221); KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT01MINNSH-NSHJMARCHESSAULT81-1|yes: REINFORCING (phi 0.24); failure: MIN wins (incl. OT/SO)
- **Jonathan Marchessault: 1+ assists YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes has the higher standalone adjusted growth (5.08 vs 1.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.083); they share one thesis budget; relationships: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLTEAMTOTAL-26OCT01MINNSH-NSH5|yes: REINFORCING (phi 0.24); failure: NSH offense suppressed (<= 2 goals)

portfolios: A EV +4.49 (adj +1.30) on $20.02, P(profit) 0.4891, adj growth 10.5 bp · B EV +1.41 (adj +0.58) on $7.98, P(profit) 0.541, adj growth 5.4 bp · C EV +1.49 (adj +0.82) on $10.66, P(profit) 0.4935, adj growth 7.3 bp

## SEA @ CGY  ·  10000 joint draws  ·  398 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.503 / away 0.497

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
| Brandon Montour: 1+ goals NO | 84 | 0.893 | 0.876 | +0.043 | +0.026 | $9.84 | SEA:SUPPRESSED | 0.25 | EVIDENCE_STRONGER | D |
| Jacob Melanson: 1+ goals YES | 9 | 0.123 | 0.112 | +0.027 | +0.016 | $2.02 | SEA:OFFENSE_4PLUS | 0.2665 | EVIDENCE_STRONGER | D |
- **Brandon Montour: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (12.17 vs 0.94 bp); despite a smaller raw edge (+0.043 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01SEACGY-SEAJMELANSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: SEA offense succeeds (4+ goals)
- **Jacob Melanson: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (6.59 vs 1.29 bp); alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: SEA offense suppressed (<= 2 goals)

portfolios: A EV +1.25 (adj +0.76) on $11.00, P(profit) 0.1227, adj growth 7.0 bp · B EV +1.07 (adj +0.65) on $11.86, P(profit) 0.1227, adj growth 6.2 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ UTA  ·  10000 joint draws  ·  320 bet sides mapped, 6 +EV candidates, 4 on card

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
| Ryan Greene: 1+ goals YES | 12 | 0.166 | 0.153 | +0.039 | +0.026 | $3.46 | CHI:OFFENSE_4PLUS | 0.2422 | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 66 | 0.776 | 0.694 | +0.101 | +0.018 | $8.54 | UTA:SUPPRESSED | 0.2441 | EVIDENCE_MIXED | D |
| Lawson Crouse: 1+ goals YES | 22 | 0.259 | 0.247 | +0.027 | +0.015 | $2.55 | UTA:OFFENSE_4PLUS | 0.2651 | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 63 | 0.745 | 0.661 | +0.099 | +0.014 | $6.16 | CHI:SUPPRESSED | 0.264 | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01CHIUTA-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (13.19 vs 1.40 bp); despite a smaller raw edge (+0.039 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.037); failure: CHI offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT01CHIUTA-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (3.41 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: UTA offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes; why: higher confidence-adjusted growth (2.68 vs 1.02 bp); alternative not eligible: confidence-adjusted EV +0.0094 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: UTA offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01CHIUTA-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (1.97 vs 1.74 bp); relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: CHI offense succeeds (4+ goals)

portfolios: A EV +3.76 (adj +0.57) on $20.02, P(profit) 0.6438, adj growth 5.1 bp · B EV +3.57 (adj +1.24) on $20.71, P(profit) 0.6936, adj growth 11.6 bp · C EV +3.50 (adj +1.47) on $16.83, P(profit) 0.1664, adj growth 13.0 bp

## EDM @ VAN  ·  10000 joint draws  ·  342 bet sides mapped, 20 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.343 / away 0.657

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_EDM_win | p_overtime | goals | shots VAN/EDM | VAN/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.44 | 0.56 | 0.00 | 6.03 | 27.9/28.5 | 24.6/24.6 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.115 | 0.36 | 0.64 | 0.00 | 6.0 | 21.9/33.9 | 29.3/19.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.50 | 0.50 | 0.48 | 5.98 | 27.8/28.3 | 25.0/24.4 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.44 | 0.56 | 0.48 | 6.01 | 22.3/34.2 | 30.8/19.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.41 | 0.59 | 0.00 | 9.33 | 29.4/30.0 | 23.3/23.9 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.085 | 0.36 | 0.64 | 0.00 | 9.42 | 23.6/35.7 | 28.1/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Leon Draisaitl: 1+ goals NO | 54 | 0.633 | 0.609 | +0.076 | +0.051 | $8.75 | EDM:SUPPRESSED | 0.2344 | EVIDENCE_STRONGER | D |
| Edmonton wins by over 2.5 goals NO | 68 | 0.773 | 0.724 | +0.078 | +0.029 | $8.89 | VAN:WINS | 0.254 | EVIDENCE_MIXED | D |
| Connor McDavid: 2+ assists NO | 69 | 0.806 | 0.727 | +0.101 | +0.022 | $6.01 | EDM:SUPPRESSED | 0.2319 | EVIDENCE_MIXED | D |
- **Leon Draisaitl: 1+ goals NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01EDMVAN-EDM3|no; why: higher confidence-adjusted growth (23.37 vs 8.75 bp); despite a smaller raw edge (+0.076 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT01EDMVAN-EDM3|no: REINFORCING (phi 0.161); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.146); failure: EDM offense succeeds (4+ goals)
- **Edmonton wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (8.75 vs 5.28 bp); despite a smaller raw edge (+0.078 vs +0.101/contract); relationships: KXNHLGOAL-26OCT01EDMVAN-EDMLDRAISAITL29-1|no: REINFORCING (phi 0.161); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: REINFORCING (phi 0.237); failure: EDM wins by 2+
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01EDMVAN-EDMLDRAISAITL29-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT01EDMVAN-EDMLDRAISAITL29-1|no has the higher standalone adjusted growth (23.37 vs 5.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.146); they share one thesis budget; relationships: KXNHLGOAL-26OCT01EDMVAN-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLSPREAD-26OCT01EDMVAN-EDM3|no: REINFORCING (phi 0.237); failure: EDM offense succeeds (4+ goals)

portfolios: A EV +5.28 (adj +0.70) on $20.02, P(profit) 0.7074, adj growth 6.0 bp · B EV +3.05 (adj +1.37) on $23.65, P(profit) 0.5948, adj growth 13.0 bp · C EV +4.25 (adj +2.29) on $34.18, P(profit) 0.5223, adj growth 21.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01EDMVAN-VAN|yes == KXNHLGAME-26OCT01EDMVAN-EDM|no

## FLA @ SJS  ·  10000 joint draws  ·  368 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.429 / away 0.571

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_FLA_win | p_overtime | goals | shots SJS/FLA | SJS/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 6.0 | 26.8/26.9 | 23.6/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.47 | 5.94 | 26.8/27.0 | 23.6/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.62 | 0.38 | 0.00 | 9.39 | 28.6/28.6 | 23.1/21.9 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.077 | 0.51 | 0.49 | 0.00 | 5.98 | 21.5/31.9 | 28.2/18.0 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.50 | 0.50 | 0.47 | 5.93 | 21.4/31.7 | 28.4/18.2 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.061 | 0.65 | 0.35 | 0.00 | 6.02 | 31.5/21.5 | 18.9/27.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Kiefer Sherwood: 1+ goals YES | 15 | 0.223 | 0.203 | +0.064 | +0.044 | $4.74 | SJS:OFFENSE_4PLUS | 0.2586 | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 76 | 0.850 | 0.802 | +0.077 | +0.030 | $8.88 | SJS:WINS | 0.2235 | EVIDENCE_MIXED | D |
| San Jose wins by over 1.5 goals YES | 24 | 0.330 | 0.283 | +0.078 | +0.030 | $2.10 | SJS:WINS_BY_2PLUS | 0.3992 | EVIDENCE_MIXED | D |
| Aleksander Barkov: 1+ goals NO | 73 | 0.789 | 0.772 | +0.045 | +0.028 | $8.88 | FLA:SUPPRESSED | 0.2313 | EVIDENCE_STRONGER | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: higher confidence-adjusted growth (31.36 vs 11.06 bp); despite a smaller raw edge (+0.064 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT01FLASJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.111); KXNHLSPREAD-26OCT01FLASJ-SJ2|yes: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT01FLASJ-FLAABARKOV16-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: SJS offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: higher confidence-adjusted growth (11.06 vs 10.28 bp); despite a smaller raw edge (+0.077 vs +0.078/contract); wins across more scripts (relative breadth 1.034 vs 0.521); relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.111); KXNHLSPREAD-26OCT01FLASJ-SJ2|yes: REINFORCING (phi 0.295); KXNHLGOAL-26OCT01FLASJ-FLAABARKOV16-1|no: MOSTLY_INDEPENDENT (phi 0.128); failure: FLA wins by 2+
- **San Jose wins by over 1.5 goals YES** — thesis: SJS wins by 2+; alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-FLA3|no has the higher standalone adjusted growth (11.06 vs 10.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.295); they share one thesis budget; relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.146); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.295); KXNHLGOAL-26OCT01FLASJ-FLAABARKOV16-1|no: MOSTLY_INDEPENDENT (phi 0.135); failure: FLA wins (incl. OT/SO)
- **Aleksander Barkov: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-FLA3|no has the higher standalone adjusted growth (11.06 vs 9.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.128); they share one thesis budget; relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.128); KXNHLSPREAD-26OCT01FLASJ-SJ2|yes: MOSTLY_INDEPENDENT (phi 0.135); failure: FLA offense succeeds (4+ goals)

portfolios: A EV +3.47 (adj +0.64) on $20.02, P(profit) 0.6675, adj growth 5.9 bp · B EV +3.98 (adj +2.25) on $24.60, P(profit) 0.4225, adj growth 21.2 bp · C EV +1.70 (adj +0.66) on $17.09, P(profit) 0.8498, adj growth 6.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01FLASJ-SJ|yes == KXNHLGAME-26OCT01FLASJ-FLA|no

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
