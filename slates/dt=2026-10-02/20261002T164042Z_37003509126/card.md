# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-02T16:40:42Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +31.39 | +11.76 | +26.93 | 0.675 | -43.94 | -61.56 | 99.68 |
| B thesis-diversified (joint) ← card | 150.00 | +28.18 | +14.53 | +23.07 | 0.648 | -41.61 | -59.15 | 128.12 |
| C best expression per thesis | 75.86 | +13.89 | +5.88 | +8.90 | 0.610 | -35.24 | -40.40 | 51.22 |

## NYR @ DET  ·  10000 joint draws  ·  326 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.541 / away 0.459

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_NYR_win | p_overtime | goals | shots DET/NYR | DET/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.55 | 0.45 | 0.00 | 5.99 | 27.0/26.6 | 23.3/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.46 | 5.87 | 27.1/26.9 | 23.5/23.8 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.107 | 0.61 | 0.39 | 0.00 | 5.97 | 32.4/21.3 | 18.4/28.3 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.55 | 0.45 | 0.47 | 5.91 | 32.6/21.4 | 18.2/29.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.55 | 0.45 | 0.00 | 9.11 | 28.5/28.2 | 22.3/22.2 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.061 | 0.62 | 0.38 | 0.00 | 9.24 | 33.8/22.3 | 17.4/26.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Nate Danielson: 1+ goals YES | 10 | 0.129 | 0.121 | +0.023 | +0.015 | $3.47 | DET:OFFENSE_4PLUS | 0.2434 | EVIDENCE_STRONGER | D |
| Oliver Bjorkstrand: 1+ goals NO | 83 | 0.862 | 0.853 | +0.022 | +0.013 | $18.13 | NYR:SUPPRESSED | 0.2218 | EVIDENCE_STRONGER | D |
| J.T. Compher: 1+ goals YES | 15 | 0.180 | 0.170 | +0.021 | +0.011 | $2.88 | DET:OFFENSE_4PLUS | 0.2399 | EVIDENCE_STRONGER | D |
- **Nate Danielson: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT02NYRDET-3|yes; why: higher confidence-adjusted growth (4.77 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.895 vs 0.785); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-NYROBJORKSTRAND28-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: DET offense suppressed (<= 2 goals)
- **Oliver Bjorkstrand: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02NYRDET-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (2.68 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.077/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: NYR offense succeeds (4+ goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT02NYRDET-3|yes; why: higher confidence-adjusted growth (2.02 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.89 vs 0.785); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT02NYRDET-NYROBJORKSTRAND28-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: DET offense suppressed (<= 2 goals)

portfolios: A EV +1.78 (adj +1.05) on $21.11, P(profit) 0.2858, adj growth 9.0 bp · B EV +1.61 (adj +0.95) on $24.47, P(profit) 0.2622, adj growth 8.4 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ CAR  ·  10000 joint draws  ·  364 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.569 / away 0.431

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WSH_win | p_overtime | goals | shots CAR/WSH | CAR/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.141 | 0.65 | 0.35 | 0.00 | 6.02 | 33.1/20.7 | 17.9/28.6 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.126 | 0.54 | 0.46 | 0.47 | 5.87 | 33.4/21.0 | 17.9/29.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.59 | 0.41 | 0.00 | 6.03 | 27.4/26.7 | 23.4/23.5 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.097 | 0.66 | 0.34 | 0.00 | 9.21 | 35.0/22.4 | 17.6/27.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.49 | 0.51 | 0.48 | 5.89 | 27.2/26.6 | 23.3/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.56 | 0.44 | 0.00 | 9.23 | 28.9/27.9 | 22.4/22.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| William Carrier: 1+ goals YES | 8 | 0.126 | 0.113 | +0.041 | +0.028 | $6.09 | CAR:OFFENSE_4PLUS | 0.3156 | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.234 | 0.217 | +0.054 | +0.037 | $9.62 | WSH:OFFENSE_4PLUS | 0.2633 | EVIDENCE_STRONGER | D |
| Alex Tuch: 1+ assists NO | 76 | 0.877 | 0.794 | +0.104 | +0.022 | $18.13 | WSH:SUPPRESSED | 0.2702 | EVIDENCE_MIXED | D |
| Boone Jenner: 1+ goals YES | 11 | 0.151 | 0.134 | +0.034 | +0.017 | $3.88 | WSH:OFFENSE_4PLUS | 0.2736 | EVIDENCE_STRONGER | D |
- **William Carrier: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02WSHCAR-CARJMARTINOOK48-1|yes; why: higher confidence-adjusted growth (21.20 vs 1.04 bp); alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT02WSHCAR-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: CAR offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (20.03 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT02WSHCAR-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: WSH offense suppressed (<= 2 goals)
- **Alex Tuch: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02WSHCAR-WSHATUCH89-1|no; why: higher confidence-adjusted growth (5.87 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT02WSHCAR-WSHBJENNER38-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.056); failure: WSH offense succeeds (4+ goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (20.03 vs 5.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: INTENTIONAL_DIVERSIFIER (phi -0.056); failure: WSH offense suppressed (<= 2 goals)

portfolios: A EV +8.91 (adj +5.06) on $32.22, P(profit) 0.4323, adj growth 43.9 bp · B EV +9.40 (adj +5.04) on $37.72, P(profit) 0.4147, adj growth 44.2 bp · C EV +3.19 (adj +2.17) on $10.54, P(profit) 0.2343, adj growth 18.7 bp

## BOS @ WPG  ·  10000 joint draws  ·  346 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.523 / away 0.477

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_BOS_win | p_overtime | goals | shots WPG/BOS | WPG/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.48 | 0.52 | 0.00 | 6.0 | 27.2/27.0 | 23.4/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.50 | 0.50 | 0.47 | 5.91 | 27.4/27.2 | 23.8/24.1 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 5.98 | 32.5/21.6 | 18.6/28.6 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.55 | 0.45 | 0.50 | 5.8 | 32.7/21.8 | 18.8/29.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.52 | 0.48 | 0.00 | 9.17 | 28.8/28.4 | 22.7/22.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.51 | 0.49 | 0.00 | 3.42 | 26.2/26.0 | 24.1/24.2 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Marat Khusnutdinov: 1+ goals YES | 10 | 0.142 | 0.129 | +0.036 | +0.023 | $5.21 | BOS:OFFENSE_4PLUS | 0.2468 | EVIDENCE_STRONGER | D |
| Elias Lindholm: 1+ goals YES | 18 | 0.233 | 0.218 | +0.042 | +0.028 | $7.80 | BOS:OFFENSE_4PLUS | 0.249 | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 13 | 0.164 | 0.154 | +0.026 | +0.017 | $4.11 | WPG:OFFENSE_4PLUS | 0.2524 | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 72 | 0.841 | 0.749 | +0.107 | +0.015 | $18.13 | BOS:SUPPRESSED | 0.2278 | EVIDENCE_MIXED | D |
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (11.76 vs 10.82 bp); despite a smaller raw edge (+0.036 vs +0.042/contract); relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT02BOSWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.027); failure: BOS offense suppressed (<= 2 goals)
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (10.82 vs 0.92 bp); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT02BOSWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.118); failure: BOS offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (5.03 vs 1.57 bp); despite a smaller raw edge (+0.026 vs +0.026/contract); relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: WPG offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02BOSWPG-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (2.64 vs 2.12 bp); despite a smaller raw edge (+0.107 vs +0.130/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.118); KXNHLGOAL-26OCT02BOSWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: BOS offense succeeds (4+ goals)

portfolios: A EV +7.21 (adj +2.59) on $32.22, P(profit) 0.7857, adj growth 22.8 bp · B EV +6.92 (adj +3.13) on $35.26, P(profit) 0.4348, adj growth 27.6 bp · C EV +5.10 (adj +1.97) on $42.53, P(profit) 0.4016, adj growth 17.3 bp

## STL @ DAL  ·  10000 joint draws  ·  342 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.623 / away 0.378

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_STL_win | p_overtime | goals | shots DAL/STL | DAL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.55 | 0.45 | 0.00 | 6.03 | 26.0/25.7 | 22.3/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.46 | 5.92 | 26.1/25.9 | 22.6/22.8 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.088 | 0.63 | 0.37 | 0.00 | 6.02 | 30.9/20.4 | 17.7/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.54 | 0.46 | 0.00 | 9.27 | 27.3/27.1 | 21.3/20.9 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.51 | 0.49 | 0.45 | 5.88 | 30.7/20.4 | 17.2/27.4 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.056 | 0.67 | 0.33 | 0.00 | 9.4 | 32.4/21.6 | 16.9/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Miro Heiskanen: 1+ goals NO | 85 | 0.901 | 0.887 | +0.042 | +0.028 | $18.13 | DAL:SUPPRESSED | 0.2336 | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 11 | 0.152 | 0.141 | +0.036 | +0.024 | $5.49 | STL:OFFENSE_4PLUS | 0.2466 | EVIDENCE_STRONGER | D |
| Dylan Holloway: 1+ goals YES | 26 | 0.313 | 0.298 | +0.039 | +0.025 | $7.33 | STL:OFFENSE_4PLUS | 0.2394 | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 25 | 0.299 | 0.286 | +0.036 | +0.023 | $6.51 | STL:OFFENSE_4PLUS | 0.2504 | EVIDENCE_STRONGER | D |
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: higher confidence-adjusted growth (14.29 vs 8.21 bp); despite a smaller raw edge (+0.042 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT02STLDAL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: DAL offense succeeds (4+ goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: higher confidence-adjusted growth (11.74 vs 8.21 bp); despite a smaller raw edge (+0.036 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02STLDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT02STLDAL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: STL offense suppressed (<= 2 goals)
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: KXNHLGAME-26OCT02STLDAL-DAL|no has the higher standalone adjusted growth (8.21 vs 6.81 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.199); relationships: KXNHLGOAL-26OCT02STLDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT02STLDAL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: KXNHLGAME-26OCT02STLDAL-DAL|no has the higher standalone adjusted growth (8.21 vs 5.80 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.200); relationships: KXNHLGOAL-26OCT02STLDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: STL offense suppressed (<= 2 goals)

portfolios: A EV +5.23 (adj +1.38) on $32.22, P(profit) 0.5585, adj growth 11.9 bp · B EV +4.51 (adj +2.94) on $37.46, P(profit) 0.5505, adj growth 26.3 bp · C EV +2.19 (adj +0.91) on $11.79, P(profit) 0.4581, adj growth 8.0 bp

## ANA @ VGK  ·  10000 joint draws  ·  354 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.633 / away 0.367

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_ANA_win | p_overtime | goals | shots VGK/ANA | VGK/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.65 | 0.35 | 0.00 | 6.03 | 28.0/28.1 | 25.3/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.46 | 5.93 | 28.1/28.4 | 25.1/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.63 | 0.37 | 0.00 | 9.38 | 29.7/30.0 | 24.7/22.7 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.078 | 0.59 | 0.41 | 0.00 | 6.02 | 22.4/33.5 | 30.2/18.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.52 | 0.48 | 0.46 | 5.9 | 22.3/33.5 | 30.0/19.1 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.064 | 0.70 | 0.30 | 0.00 | 6.02 | 32.8/22.4 | 19.9/27.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Tim Washe: 1+ goals YES | 8 | 0.113 | 0.104 | +0.028 | +0.019 | $4.01 | ANA:OFFENSE_4PLUS | 0.2593 | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 8 | 0.113 | 0.102 | +0.027 | +0.017 | $3.49 | ANA:OFFENSE_4PLUS | 0.2951 | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ assists YES | 23 | 0.362 | 0.267 | +0.120 | +0.024 | $5.25 | ANA:OFFENSE_4PLUS | 0.25 | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.083 | 0.075 | +0.019 | +0.011 | $2.34 | VGK:OFFENSE_4PLUS | 0.2947 | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (9.54 vs 6.84 bp); despite a smaller raw edge (+0.028 vs +0.120/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLGOAL-26OCT02ANAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: ANA offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (7.69 vs 6.84 bp); despite a smaller raw edge (+0.027 vs +0.120/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.06); KXNHLGOAL-26OCT02ANAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ assists YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02ANAVGK-ANA|yes; why: higher confidence-adjusted growth (6.84 vs 3.10 bp); relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.06); KXNHLGOAL-26OCT02ANAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: ANA offense suppressed (<= 2 goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-VGKRANDERSSON4-1|yes; why: higher confidence-adjusted growth (4.07 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: VGK offense suppressed (<= 2 goals)

portfolios: A EV +8.25 (adj +1.68) on $32.22, P(profit) 0.4824, adj growth 12.1 bp · B EV +5.73 (adj +2.47) on $15.09, P(profit) 0.5266, adj growth 21.6 bp · C EV +3.41 (adj +0.83) on $11.00, P(profit) 0.5707, adj growth 7.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02ANAVGK-VGK|no == KXNHLGAME-26OCT02ANAVGK-ANA|yes

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
