# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-02T15:40:44Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +24.29 | +8.94 | +20.63 | 0.677 | -34.45 | -47.22 | 78.37 |
| B thesis-diversified (joint) ← card | 150.00 | +20.60 | +9.47 | +18.54 | 0.672 | -30.67 | -43.82 | 85.77 |
| C best expression per thesis | 83.48 | +12.68 | +5.64 | +9.79 | 0.604 | -31.69 | -44.83 | 49.12 |

## NYR @ DET  ·  10000 joint draws  ·  326 bet sides mapped, 4 +EV candidates, 4 on card


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
| Nate Danielson: 1+ goals YES | 10 | 0.129 | 0.121 | +0.023 | +0.015 | $2.87 | DET:OFFENSE_4PLUS | 0.2434 | EVIDENCE_STRONGER | D |
| Sean Durzi: 1+ goals NO | 91 | 0.935 | 0.927 | +0.019 | +0.012 | $11.96 | NYR:SUPPRESSED | 0.2211 | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ assists NO | 72 | 0.825 | 0.750 | +0.091 | +0.016 | $10.67 | NYR:SUPPRESSED | 0.2247 | EVIDENCE_MIXED | D |
| J.T. Compher: 1+ goals YES | 15 | 0.180 | 0.170 | +0.021 | +0.011 | $2.38 | DET:OFFENSE_4PLUS | 0.2399 | EVIDENCE_STRONGER | D |
- **Nate Danielson: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT02NYRDET-3|yes; why: higher confidence-adjusted growth (4.77 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.895 vs 0.785); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-NYRSDURZI5-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: DET offense suppressed (<= 2 goals)
- **Sean Durzi: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02NYRDET-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (3.99 vs 0.00 bp); despite a smaller raw edge (+0.019 vs +0.077/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.04); KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: NYR offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02NYRDET-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (2.95 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT02NYRDET-NYRSDURZI5-1|no: MOSTLY_INDEPENDENT (phi 0.04); KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: NYR offense succeeds (4+ goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT02NYRDET-3|yes; why: higher confidence-adjusted growth (2.02 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.89 vs 0.785); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT02NYRDET-NYRSDURZI5-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.018); failure: DET offense suppressed (<= 2 goals)

portfolios: A EV +2.92 (adj +1.15) on $30.00, P(profit) 0.2831, adj growth 10.2 bp · B EV +2.51 (adj +0.95) on $27.88, P(profit) 0.2812, adj growth 8.7 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ CAR  ·  10000 joint draws  ·  364 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WSH_win | p_overtime | goals | shots CAR/WSH | CAR/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.148 | 0.62 | 0.38 | 0.00 | 5.99 | 33.2/21.0 | 18.1/29.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.131 | 0.54 | 0.46 | 0.51 | 5.89 | 33.4/21.3 | 18.1/30.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.099 | 0.57 | 0.43 | 0.00 | 6.0 | 27.0/26.2 | 23.0/23.1 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.098 | 0.67 | 0.33 | 0.00 | 9.27 | 34.7/22.0 | 17.2/27.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.54 | 0.46 | 0.46 | 5.93 | 27.4/26.6 | 23.2/24.1 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.066 | 0.58 | 0.42 | 0.00 | 3.39 | 31.9/19.7 | 18.1/29.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| William Carrier: 1+ goals YES | 8 | 0.121 | 0.108 | +0.035 | +0.023 | $4.19 | CAR:OFFENSE_4PLUS | 0.3101 | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.224 | 0.209 | +0.044 | +0.029 | $6.49 | WSH:OFFENSE_4PLUS | 0.2837 | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 12 | 0.157 | 0.147 | +0.029 | +0.020 | $4.27 | WSH:OFFENSE_4PLUS | 0.276 | EVIDENCE_STRONGER | D |
| Alex Tuch: 1+ assists NO | 77 | 0.882 | 0.799 | +0.100 | +0.017 | $15.09 | WSH:SUPPRESSED | 0.2794 | EVIDENCE_MIXED | D |
- **William Carrier: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-CARKMILLER19-1|yes; why: higher confidence-adjusted growth (14.19 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT02WSHCAR-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: CAR offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (12.73 vs 0.56 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT02WSHCAR-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.031); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (12.73 vs 7.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: INTENTIONAL_DIVERSIFIER (phi -0.07); failure: WSH offense suppressed (<= 2 goals)
- **Alex Tuch: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02WSHCAR-WSHATUCH89-1|no; why: higher confidence-adjusted growth (3.75 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT02WSHCAR-WSHBJENNER38-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.07); failure: WSH offense succeeds (4+ goals)

portfolios: A EV +6.24 (adj +2.68) on $30.00, P(profit) 0.319, adj growth 23.9 bp · B EV +6.24 (adj +3.19) on $30.04, P(profit) 0.4272, adj growth 28.7 bp · C EV +3.29 (adj +1.54) on $15.93, P(profit) 0.2242, adj growth 13.3 bp

## BOS @ WPG  ·  10000 joint draws  ·  344 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_BOS_win | p_overtime | goals | shots WPG/BOS | WPG/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.52 | 0.48 | 0.00 | 5.98 | 27.3/27.2 | 23.7/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.50 | 0.50 | 0.45 | 5.85 | 27.3/27.2 | 23.9/24.1 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.086 | 0.59 | 0.41 | 0.00 | 5.96 | 32.3/21.6 | 18.7/28.2 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.49 | 0.51 | 0.50 | 5.81 | 32.4/21.7 | 18.5/29.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.53 | 0.47 | 0.00 | 9.32 | 29.4/29.0 | 23.2/23.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.48 | 0.52 | 0.00 | 3.47 | 26.1/25.8 | 23.9/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Elias Lindholm: 1+ goals YES | 18 | 0.231 | 0.217 | +0.041 | +0.027 | $5.92 | BOS:OFFENSE_4PLUS | 0.2351 | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 13 | 0.166 | 0.157 | +0.028 | +0.019 | $3.84 | WPG:OFFENSE_4PLUS | 0.2621 | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 28 | 0.331 | 0.317 | +0.036 | +0.023 | $5.95 | WPG:OFFENSE_4PLUS | 0.2429 | EVIDENCE_STRONGER | D |
| Cole Perfetti: 1+ goals NO | 73 | 0.776 | 0.763 | +0.032 | +0.019 | $14.44 | WPG:SUPPRESSED | 0.2393 | EVIDENCE_STRONGER | D |
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02BOSWPG-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (10.19 vs 0.41 bp); despite a smaller raw edge (+0.041 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0063 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02BOSWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: BOS offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (6.41 vs 5.35 bp); despite a smaller raw edge (+0.028 vs +0.036/contract); relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-WPGAIAFALLO9-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02BOSWPG-WPGAIAFALLO9-1|yes has the higher standalone adjusted growth (6.41 vs 5.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT02BOSWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense suppressed (<= 2 goals)
- **Cole Perfetti: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02BOSWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (4.27 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT02BOSWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense succeeds (4+ goals)

portfolios: A EV +3.69 (adj +1.70) on $30.00, P(profit) 0.4824, adj growth 15.5 bp · B EV +3.41 (adj +2.19) on $30.15, P(profit) 0.5026, adj growth 19.7 bp · C EV +3.52 (adj +2.29) on $32.01, P(profit) 0.3574, adj growth 19.9 bp

## STL @ DAL  ·  10000 joint draws  ·  340 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_STL_win | p_overtime | goals | shots DAL/STL | DAL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.57 | 0.43 | 0.00 | 5.98 | 26.1/25.8 | 22.6/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.49 | 5.92 | 25.8/25.6 | 22.4/22.6 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.094 | 0.62 | 0.38 | 0.00 | 6.01 | 30.6/20.2 | 17.3/26.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.57 | 0.43 | 0.00 | 9.25 | 27.7/27.3 | 21.7/21.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.55 | 0.45 | 0.47 | 5.84 | 31.3/20.6 | 17.5/27.9 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.058 | 0.65 | 0.35 | 0.00 | 9.29 | 32.8/22.2 | 17.6/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Miro Heiskanen: 1+ goals NO | 85 | 0.893 | 0.881 | +0.034 | +0.022 | $13.84 | DAL:SUPPRESSED | 0.2362 | EVIDENCE_STRONGER | D |
| Dallas wins NO | 37 | 0.459 | 0.412 | +0.073 | +0.026 | $5.86 | STL:WINS | 0.2344 | EVIDENCE_MIXED | D |
| Jimmy Snuggerud: 1+ goals YES | 25 | 0.298 | 0.285 | +0.035 | +0.022 | $4.18 | STL:OFFENSE_4PLUS | 0.2426 | EVIDENCE_STRONGER | D |
| Mason McTavish: 1+ assists NO | 77 | 0.880 | 0.795 | +0.098 | +0.013 | $13.84 | STL:SUPPRESSED | 0.2338 | EVIDENCE_MIXED | D |
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: higher confidence-adjusted growth (9.12 vs 6.09 bp); despite a smaller raw edge (+0.034 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGAME-26OCT02STLDAL-DAL|no: MOSTLY_INDEPENDENT (phi 0.11); KXNHLGOAL-26OCT02STLDAL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.023); failure: DAL offense succeeds (4+ goals)
- **Dallas wins NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGAME-26OCT02STLDAL-STL|yes; why: higher confidence-adjusted growth (6.09 vs 3.86 bp); relationships: KXNHLGOAL-26OCT02STLDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.11); KXNHLGOAL-26OCT02STLDAL-STLJSNUGGERUD21-1|yes: REINFORCING (phi 0.2); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: INTENTIONAL_DIVERSIFIER (phi -0.112); failure: DAL wins (incl. OT/SO)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: second expression of the same thesis: KXNHLGAME-26OCT02STLDAL-DAL|no has the higher standalone adjusted growth (6.09 vs 5.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.200); they share one thesis budget; relationships: KXNHLGOAL-26OCT02STLDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGAME-26OCT02STLDAL-DAL|no: REINFORCING (phi 0.2); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.049); failure: STL offense suppressed (<= 2 goals)
- **Mason McTavish: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02STLDAL-STLMMCTAVISH83-1|no; why: higher confidence-adjusted growth (2.23 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02STLDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGAME-26OCT02STLDAL-DAL|no: INTENTIONAL_DIVERSIFIER (phi -0.112); KXNHLGOAL-26OCT02STLDAL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.049); failure: STL offense succeeds (4+ goals)

portfolios: A EV +3.44 (adj +0.91) on $30.00, P(profit) 0.639, adj growth 8.1 bp · B EV +3.94 (adj +1.33) on $37.71, P(profit) 0.4877, adj growth 12.3 bp · C EV +1.91 (adj +0.67) on $10.12, P(profit) 0.4591, adj growth 5.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02STLDAL-STL|yes == KXNHLGAME-26OCT02STLDAL-DAL|no

## ANA @ VGK  ·  10000 joint draws  ·  354 bet sides mapped, 5 +EV candidates, 4 on card


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
| Tim Washe: 1+ goals YES | 8 | 0.113 | 0.103 | +0.028 | +0.017 | $3.11 | ANA:OFFENSE_4PLUS | 0.2593 | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 68 | 0.736 | 0.718 | +0.041 | +0.023 | $15.07 | VGK:SUPPRESSED | 0.2479 | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ assists YES | 23 | 0.362 | 0.263 | +0.120 | +0.021 | $4.05 | ANA:OFFENSE_4PLUS | 0.25 | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.083 | 0.075 | +0.019 | +0.011 | $1.99 | VGK:OFFENSE_4PLUS | 0.2947 | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (8.32 vs 5.12 bp); despite a smaller raw edge (+0.028 vs +0.120/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02ANAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLGOAL-26OCT02ANAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: ANA offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT02ANAVGK-ANA|yes; why: higher confidence-adjusted growth (5.53 vs 0.78 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT02ANAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: VGK offense succeeds (4+ goals)
- **Alex Killorn: 1+ assists YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02ANAVGK-ANA|yes; why: higher confidence-adjusted growth (5.12 vs 0.78 bp); alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLGOAL-26OCT02ANAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT02ANAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: ANA offense suppressed (<= 2 goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-VGKRANDERSSON4-1|yes; why: higher confidence-adjusted growth (4.07 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT02ANAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: VGK offense suppressed (<= 2 goals)

portfolios: A EV +7.99 (adj +2.50) on $30.00, P(profit) 0.5115, adj growth 20.7 bp · B EV +4.50 (adj +1.81) on $24.22, P(profit) 0.3994, adj growth 16.3 bp · C EV +3.96 (adj +1.14) on $25.42, P(profit) 0.7361, adj growth 10.0 bp

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
