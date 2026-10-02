# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-02T13:40:41Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +17.04 | +5.54 | +13.74 | 0.657 | -29.46 | -42.45 | 48.20 |
| B thesis-diversified (joint) ← card | 150.00 | +14.61 | +5.90 | +12.50 | 0.658 | -22.86 | -30.06 | 54.35 |
| C best expression per thesis | 63.90 | +8.52 | +3.37 | +4.25 | 0.574 | -23.83 | -32.57 | 29.40 |

## NYR @ DET  ·  10000 joint draws  ·  330 bet sides mapped, 4 +EV candidates, 4 on card


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
| Nate Danielson: 1+ goals YES | 10 | 0.129 | 0.120 | +0.023 | +0.014 | $2.42 | DET:OFFENSE_4PLUS | 0.2411 | EVIDENCE_STRONGER | D |
| Moritz Seider: 1+ goals NO | 84 | 0.875 | 0.865 | +0.025 | +0.015 | $13.86 | DET:SUPPRESSED | 0.225 | EVIDENCE_STRONGER | D |
| Sean Durzi: 1+ goals NO | 91 | 0.935 | 0.926 | +0.019 | +0.010 | $13.86 | NYR:SUPPRESSED | 0.2256 | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ assists NO | 72 | 0.818 | 0.744 | +0.084 | +0.010 | $7.78 | NYR:SUPPRESSED | 0.225 | EVIDENCE_MIXED | D |
- **Nate Danielson: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02NYRDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (4.58 vs 0.00 bp); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT02NYRDET-NYRSDURZI5-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: DET offense suppressed (<= 2 goals)
- **Moritz Seider: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT02NYRDET-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (4.00 vs 0.00 bp); despite a smaller raw edge (+0.025 vs +0.025/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT02NYRDET-NYRSDURZI5-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: DET offense succeeds (4+ goals)
- **Sean Durzi: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (3.04 vs 1.20 bp); despite a smaller raw edge (+0.019 vs +0.084/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT02NYRDET-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.042); failure: NYR offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02NYRDET-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (1.20 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT02NYRDET-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT02NYRDET-NYRSDURZI5-1|no: MOSTLY_INDEPENDENT (phi 0.042); failure: NYR offense succeeds (4+ goals)

portfolios: A EV +2.62 (adj +0.97) on $37.50, P(profit) 0.711, adj growth 8.7 bp · B EV +2.10 (adj +0.84) on $37.91, P(profit) 0.7083, adj growth 7.7 bp · C EV +1.39 (adj +0.17) on $12.19, P(profit) 0.8177, adj growth 1.5 bp

## WSH @ CAR  ·  10000 joint draws  ·  364 bet sides mapped, 7 +EV candidates, 4 on card


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
| William Carrier: 1+ goals YES | 8 | 0.120 | 0.109 | +0.035 | +0.024 | $4.16 | CAR:OFFENSE_4PLUS | 0.3261 | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 18 | 0.229 | 0.214 | +0.038 | +0.024 | $5.03 | WSH:OFFENSE_4PLUS | 0.2709 | EVIDENCE_STRONGER | D |
| Mark Jankowski: 1+ goals NO | 82 | 0.860 | 0.849 | +0.029 | +0.018 | $14.36 | CAR:SUPPRESSED | 0.2767 | EVIDENCE_STRONGER | D |
| Alex Tuch: 1+ assists NO | 78 | 0.886 | 0.811 | +0.094 | +0.019 | $14.36 | WSH:SUPPRESSED | 0.2784 | EVIDENCE_MIXED | D |
- **William Carrier: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-CARKMILLER19-1|yes; why: higher confidence-adjusted growth (15.67 vs 0.54 bp); despite a smaller raw edge (+0.035 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0072 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT02WSHCAR-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CAR offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (7.78 vs 1.50 bp); despite a smaller raw edge (+0.038 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT02WSHCAR-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.031); failure: WSH offense suppressed (<= 2 goals)
- **Mark Jankowski: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT02WSHCAR-CARSAHO20-1|no; why: higher confidence-adjusted growth (5.24 vs 1.61 bp); despite a smaller raw edge (+0.029 vs +0.098/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: CAR offense succeeds (4+ goals)
- **Alex Tuch: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02WSHCAR-WSHATUCH89-1|no; why: higher confidence-adjusted growth (4.64 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT02WSHCAR-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: WSH offense succeeds (4+ goals)

portfolios: A EV +6.16 (adj +1.69) on $37.50, P(profit) 0.4387, adj growth 13.8 bp · B EV +4.95 (adj +2.45) on $37.91, P(profit) 0.3206, adj growth 22.3 bp · C EV +2.82 (adj +1.04) on $15.35, P(profit) 0.2285, adj growth 9.1 bp

## BOS @ WPG  ·  10000 joint draws  ·  344 bet sides mapped, 4 +EV candidates, 4 on card


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
| Elias Lindholm: 1+ goals YES | 18 | 0.231 | 0.216 | +0.041 | +0.026 | $4.19 | BOS:OFFENSE_4PLUS | 0.2351 | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 71 | 0.840 | 0.746 | +0.115 | +0.021 | $11.72 | BOS:SUPPRESSED | 0.2384 | EVIDENCE_MIXED | D |
| Cole Perfetti: 1+ goals NO | 73 | 0.776 | 0.763 | +0.032 | +0.019 | $10.29 | WPG:SUPPRESSED | 0.2393 | EVIDENCE_STRONGER | D |
| Isak Rosen: 1+ goals NO | 85 | 0.884 | 0.873 | +0.025 | +0.014 | $11.72 | WPG:SUPPRESSED | 0.2415 | EVIDENCE_STRONGER | D |
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT02BOSWPG-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (9.28 vs 0.00 bp); despite a smaller raw edge (+0.041 vs +0.071/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.12); KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT02BOSWPG-WPGIROSEN27-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: BOS offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (4.97 vs 0.41 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.12); KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT02BOSWPG-WPGIROSEN27-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: BOS offense succeeds (4+ goals)
- **Cole Perfetti: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02BOSWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (4.27 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT02BOSWPG-WPGIROSEN27-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: WPG offense succeeds (4+ goals)
- **Isak Rosen: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no has the higher standalone adjusted growth (4.27 vs 3.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: WPG offense succeeds (4+ goals)

portfolios: A EV +3.79 (adj +1.62) on $37.50, P(profit) 0.6821, adj growth 14.9 bp · B EV +3.55 (adj +1.36) on $37.91, P(profit) 0.6647, adj growth 12.8 bp · C EV +2.40 (adj +1.49) on $26.24, P(profit) 0.2314, adj growth 12.9 bp

## STL @ DAL  ·  10000 joint draws  ·  340 bet sides mapped, 8 +EV candidates, 4 on card


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
| Dallas wins NO | 37 | 0.459 | 0.412 | +0.073 | +0.026 | $6.58 | STL:WINS | 0.2344 | EVIDENCE_MIXED | D |
| Mikko Rantanen: 1+ goals NO | 68 | 0.734 | 0.718 | +0.039 | +0.023 | $12.45 | DAL:SUPPRESSED | 0.2357 | EVIDENCE_STRONGER | D |
| Mason McTavish: 1+ assists NO | 77 | 0.880 | 0.799 | +0.098 | +0.016 | $15.16 | STL:SUPPRESSED | 0.2338 | EVIDENCE_MIXED | D |
| Dylan Holloway: 1+ goals YES | 27 | 0.308 | 0.295 | +0.024 | +0.011 | $2.08 | STL:OFFENSE_4PLUS | 0.2368 | EVIDENCE_STRONGER | D |
- **Dallas wins NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT02STLDAL-DAL2|no; why: higher confidence-adjusted growth (6.09 vs 4.09 bp); wins across more scripts (relative breadth 1.033 vs 0.925); relationships: KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: REINFORCING (phi 0.185); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: INTENTIONAL_DIVERSIFIER (phi -0.112); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: REINFORCING (phi 0.192); failure: DAL wins (incl. OT/SO)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: second expression of the same thesis: KXNHLGAME-26OCT02STLDAL-DAL|no has the higher standalone adjusted growth (6.09 vs 5.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.185); they share one thesis budget; relationships: KXNHLGAME-26OCT02STLDAL-DAL|no: REINFORCING (phi 0.185); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: DAL offense succeeds (4+ goals)
- **Mason McTavish: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02STLDAL-STLMMCTAVISH83-1|no; why: higher confidence-adjusted growth (3.47 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGAME-26OCT02STLDAL-DAL|no: INTENTIONAL_DIVERSIFIER (phi -0.112); KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.056); failure: STL offense succeeds (4+ goals)
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: second expression of the same thesis: KXNHLGAME-26OCT02STLDAL-DAL|no has the higher standalone adjusted growth (6.09 vs 1.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.192); they share one thesis budget; relationships: KXNHLGAME-26OCT02STLDAL-DAL|no: REINFORCING (phi 0.192); KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: INTENTIONAL_DIVERSIFIER (phi -0.056); failure: STL offense suppressed (<= 2 goals)

portfolios: A EV +4.47 (adj +1.26) on $37.50, P(profit) 0.639, adj growth 10.9 bp · B EV +4.01 (adj +1.25) on $36.27, P(profit) 0.7366, adj growth 11.4 bp · C EV +1.91 (adj +0.67) on $10.12, P(profit) 0.4591, adj growth 5.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02STLDAL-STL|yes == KXNHLGAME-26OCT02STLDAL-DAL|no

## ANA @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_ANA_win | p_overtime | goals | shots VGK/ANA | VGK/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.65 | 0.35 | 0.00 | 6.03 | 28.0/28.1 | 25.3/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.46 | 5.93 | 28.1/28.4 | 25.1/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.63 | 0.37 | 0.00 | 9.38 | 29.7/30.0 | 24.7/22.7 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.078 | 0.59 | 0.41 | 0.00 | 6.02 | 22.4/33.5 | 30.2/18.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.52 | 0.48 | 0.46 | 5.9 | 22.3/33.5 | 30.0/19.1 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.064 | 0.70 | 0.30 | 0.00 | 6.02 | 32.8/22.4 | 19.9/27.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
