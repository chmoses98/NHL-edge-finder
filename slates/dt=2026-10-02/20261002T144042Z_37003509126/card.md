# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-02T14:40:42Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +25.73 | +9.53 | +24.05 | 0.669 | -39.41 | -55.68 | 81.92 |
| B thesis-diversified (joint) ← card | 150.00 | +20.13 | +8.69 | +16.78 | 0.664 | -29.52 | -42.75 | 78.74 |
| C best expression per thesis | 112.12 | +16.55 | +6.63 | +15.29 | 0.635 | -32.48 | -47.51 | 57.81 |

## NYR @ DET  ·  10000 joint draws  ·  326 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_NYR_win | p_overtime | goals | shots DET/NYR | DET/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.53 | 0.47 | 0.00 | 6.03 | 27.2/26.7 | 23.3/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.49 | 5.89 | 27.0/26.7 | 23.3/23.8 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.108 | 0.61 | 0.39 | 0.00 | 5.96 | 32.2/21.0 | 18.2/27.9 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.55 | 0.45 | 0.45 | 5.9 | 32.4/21.5 | 18.2/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.55 | 0.45 | 0.00 | 9.28 | 28.9/28.4 | 22.4/22.6 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.062 | 0.61 | 0.39 | 0.00 | 9.23 | 34.0/22.8 | 17.9/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Nate Danielson: 1+ goals YES | 10 | 0.129 | 0.120 | +0.023 | +0.014 | $2.71 | DET:OFFENSE_4PLUS | 0.2411 | EVIDENCE_STRONGER | D |
| Moritz Seider: 1+ goals NO | 84 | 0.875 | 0.865 | +0.025 | +0.015 | $15.14 | DET:SUPPRESSED | 0.225 | EVIDENCE_STRONGER | D |
| J.T. Compher: 1+ goals YES | 15 | 0.184 | 0.174 | +0.025 | +0.015 | $3.15 | DET:OFFENSE_4PLUS | 0.2482 | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ assists NO | 72 | 0.820 | 0.749 | +0.086 | +0.015 | $12.73 | NYR:SUPPRESSED | 0.2246 | EVIDENCE_MIXED | D |
- **Nate Danielson: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02NYRDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (4.58 vs 0.00 bp); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: DET offense suppressed (<= 2 goals)
- **Moritz Seider: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT02NYRDET-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (4.00 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: DET offense succeeds (4+ goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02NYRDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (3.70 vs 0.00 bp); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT02NYRDET-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: DET offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02NYRDET-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (2.35 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT02NYRDET-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: NYR offense succeeds (4+ goals)

portfolios: A EV +3.07 (adj +1.30) on $30.28, P(profit) 0.2833, adj growth 11.5 bp · B EV +3.01 (adj +1.18) on $33.73, P(profit) 0.7877, adj growth 10.7 bp · C EV +1.99 (adj +0.33) on $16.95, P(profit) 0.8202, adj growth 2.9 bp

## WSH @ CAR  ·  10000 joint draws  ·  364 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WSH_win | p_overtime | goals | shots CAR/WSH | CAR/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.146 | 0.63 | 0.37 | 0.00 | 6.0 | 33.1/20.9 | 18.0/28.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.129 | 0.55 | 0.45 | 0.46 | 5.93 | 33.2/21.0 | 17.8/29.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.59 | 0.41 | 0.00 | 5.98 | 27.4/26.4 | 23.3/23.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.097 | 0.63 | 0.37 | 0.00 | 9.24 | 35.0/22.3 | 17.4/27.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.52 | 0.48 | 0.49 | 5.89 | 27.3/26.6 | 23.4/24.0 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.069 | 0.61 | 0.39 | 0.00 | 3.48 | 31.8/19.8 | 18.2/29.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| William Carrier: 1+ goals YES | 8 | 0.120 | 0.109 | +0.035 | +0.024 | $4.48 | CAR:OFFENSE_4PLUS | 0.3261 | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.229 | 0.213 | +0.049 | +0.033 | $7.26 | WSH:OFFENSE_4PLUS | 0.2709 | EVIDENCE_STRONGER | D |
| Alex Tuch: 1+ assists NO | 78 | 0.886 | 0.807 | +0.094 | +0.015 | $15.14 | WSH:SUPPRESSED | 0.2784 | EVIDENCE_MIXED | D |
| Boone Jenner: 1+ goals YES | 12 | 0.154 | 0.139 | +0.027 | +0.012 | $2.39 | WSH:OFFENSE_4PLUS | 0.27 | EVIDENCE_STRONGER | D |
- **William Carrier: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-CARKMILLER19-2|yes; why: higher confidence-adjusted growth (15.67 vs 1.35 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT02WSHCAR-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: CAR offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (15.64 vs 0.44 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT02WSHCAR-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: WSH offense suppressed (<= 2 goals)
- **Alex Tuch: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02WSHCAR-WSHATUCH89-1|no; why: higher confidence-adjusted growth (3.16 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT02WSHCAR-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.034); failure: WSH offense succeeds (4+ goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (15.64 vs 2.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.034); failure: WSH offense suppressed (<= 2 goals)

portfolios: A EV +6.48 (adj +2.94) on $30.28, P(profit) 0.3245, adj growth 26.4 bp · B EV +6.12 (adj +3.10) on $29.27, P(profit) 0.414, adj growth 27.8 bp · C EV +3.96 (adj +1.89) on $17.76, P(profit) 0.2285, adj growth 16.4 bp

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
| Elias Lindholm: 1+ goals YES | 18 | 0.231 | 0.216 | +0.041 | +0.026 | $5.74 | BOS:OFFENSE_4PLUS | 0.2351 | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 13 | 0.166 | 0.155 | +0.028 | +0.018 | $3.44 | WPG:OFFENSE_4PLUS | 0.2621 | EVIDENCE_STRONGER | D |
| Cole Perfetti: 1+ goals NO | 73 | 0.776 | 0.763 | +0.032 | +0.019 | $13.94 | WPG:SUPPRESSED | 0.2393 | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 72 | 0.840 | 0.749 | +0.106 | +0.015 | $14.72 | BOS:SUPPRESSED | 0.2384 | EVIDENCE_MIXED | D |
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT02BOSWPG-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (9.28 vs 0.00 bp); despite a smaller raw edge (+0.041 vs +0.071/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02BOSWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.12); failure: BOS offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (5.58 vs 0.20 bp); alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: WPG offense suppressed (<= 2 goals)
- **Cole Perfetti: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02BOSWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (4.27 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT02BOSWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: WPG offense succeeds (4+ goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (2.46 vs 0.41 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.12); KXNHLGOAL-26OCT02BOSWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: BOS offense succeeds (4+ goals)

portfolios: A EV +4.03 (adj +1.82) on $30.28, P(profit) 0.3543, adj growth 16.4 bp · B EV +4.64 (adj +1.87) on $37.84, P(profit) 0.7736, adj growth 17.0 bp · C EV +3.36 (adj +2.09) on $31.25, P(profit) 0.3574, adj growth 18.2 bp

## STL @ DAL  ·  10000 joint draws  ·  340 bet sides mapped, 11 +EV candidates, 4 on card


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
| Miro Heiskanen: 1+ goals NO | 85 | 0.893 | 0.881 | +0.034 | +0.022 | $11.67 | DAL:SUPPRESSED | 0.2362 | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 1+ goals NO | 68 | 0.734 | 0.720 | +0.039 | +0.024 | $11.03 | DAL:SUPPRESSED | 0.2357 | EVIDENCE_STRONGER | D |
| Dylan Holloway: 1+ goals YES | 26 | 0.308 | 0.295 | +0.034 | +0.021 | $5.29 | STL:OFFENSE_4PLUS | 0.2368 | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 12 | 0.156 | 0.140 | +0.028 | +0.013 | $2.51 | STL:OFFENSE_4PLUS | 0.2352 | EVIDENCE_STRONGER | D |
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no; why: higher confidence-adjusted growth (9.12 vs 6.14 bp); despite a smaller raw edge (+0.034 vs +0.039/contract); relationships: KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: DAL offense succeeds (4+ goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: higher confidence-adjusted growth (6.14 vs 6.09 bp); despite a smaller raw edge (+0.039 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02STLDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: DAL offense succeeds (4+ goals)
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: KXNHLGAME-26OCT02STLDAL-DAL|no has the higher standalone adjusted growth (6.09 vs 4.89 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.192); relationships: KXNHLGOAL-26OCT02STLDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: KXNHLGAME-26OCT02STLDAL-DAL|no has the higher standalone adjusted growth (6.09 vs 3.32 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.154); relationships: KXNHLGOAL-26OCT02STLDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: STL offense suppressed (<= 2 goals)

portfolios: A EV +4.13 (adj +1.33) on $30.28, P(profit) 0.4591, adj growth 10.2 bp · B EV +2.31 (adj +1.36) on $30.50, P(profit) 0.4044, adj growth 12.6 bp · C EV +2.57 (adj +1.17) on $25.83, P(profit) 0.3779, adj growth 10.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02STLDAL-STL|yes == KXNHLGAME-26OCT02STLDAL-DAL|no

## ANA @ VGK  ·  10000 joint draws  ·  354 bet sides mapped, 3 +EV candidates, 3 on card


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
| Alex Killorn: 1+ assists YES | 22 | 0.362 | 0.260 | +0.130 | +0.028 | $5.55 | ANA:OFFENSE_4PLUS | 0.25 | EVIDENCE_MIXED | D |
| Braeden Bowman: 1+ goals YES | 16 | 0.195 | 0.185 | +0.026 | +0.016 | $3.38 | VGK:OFFENSE_4PLUS | 0.2954 | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 69 | 0.736 | 0.720 | +0.031 | +0.015 | $9.74 | VGK:SUPPRESSED | 0.2479 | EVIDENCE_STRONGER | D |
- **Alex Killorn: 1+ assists YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT02ANAVGK-VGK3|no; why: higher confidence-adjusted growth (9.49 vs 0.31 bp); alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT02ANAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: ANA offense suppressed (<= 2 goals)
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-VGKRANDERSSON4-1|yes; why: higher confidence-adjusted growth (3.75 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT02ANAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT02ANAVGK-VGK3|no; why: higher confidence-adjusted growth (2.25 vs 0.31 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: VGK offense succeeds (4+ goals)

portfolios: A EV +8.02 (adj +2.14) on $28.89, P(profit) 0.4551, adj growth 17.4 bp · B EV +4.05 (adj +1.18) on $18.66, P(profit) 0.4871, adj growth 10.7 bp · C EV +4.68 (adj +1.15) on $20.33, P(profit) 0.362, adj growth 10.0 bp

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
