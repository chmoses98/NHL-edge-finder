# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-02T12:40:45Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +18.58 | +7.28 | +15.06 | 0.647 | -42.07 | -50.05 | 62.23 |
| B thesis-diversified (joint) ← card | 149.99 | +17.02 | +6.88 | +15.68 | 0.636 | -30.84 | -45.35 | 60.83 |
| C best expression per thesis | 70.12 | +9.34 | +3.57 | +7.61 | 0.537 | -29.12 | -43.84 | 31.16 |

## NYR @ DET  ·  10000 joint draws  ·  330 bet sides mapped, 3 +EV candidates, 3 on card


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
| Nate Danielson: 1+ goals YES | 10 | 0.129 | 0.120 | +0.023 | +0.014 | $3.40 | DET:OFFENSE_4PLUS | 0.2411 | EVIDENCE_STRONGER | D |
| Moritz Seider: 1+ goals NO | 84 | 0.875 | 0.863 | +0.025 | +0.014 | $18.74 | DET:SUPPRESSED | 0.225 | EVIDENCE_STRONGER | D |
| Sean Durzi: 1+ goals NO | 91 | 0.935 | 0.926 | +0.019 | +0.010 | $18.74 | NYR:SUPPRESSED | 0.2256 | EVIDENCE_STRONGER | D |
- **Nate Danielson: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02NYRDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (4.58 vs 0.14 bp); alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02NYRDET-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT02NYRDET-NYRSDURZI5-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: DET offense suppressed (<= 2 goals)
- **Moritz Seider: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT02NYRDET-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (3.37 vs 0.00 bp); despite a smaller raw edge (+0.025 vs +0.025/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT02NYRDET-NYRSDURZI5-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: DET offense succeeds (4+ goals)
- **Sean Durzi: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (3.04 vs 0.59 bp); despite a smaller raw edge (+0.019 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT02NYRDET-DETMSEIDER53-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: NYR offense succeeds (4+ goals)

portfolios: A EV +1.64 (adj +0.97) on $32.14, P(profit) 0.129, adj growth 8.5 bp · B EV +1.67 (adj +0.97) on $40.87, P(profit) 0.8384, adj growth 8.7 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| William Carrier: 1+ goals YES | 8 | 0.120 | 0.109 | +0.035 | +0.024 | $5.55 | CAR:OFFENSE_4PLUS | 0.3261 | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 18 | 0.229 | 0.214 | +0.038 | +0.024 | $6.66 | WSH:OFFENSE_4PLUS | 0.2709 | EVIDENCE_STRONGER | D |
| Alex Tuch: 1+ assists NO | 78 | 0.886 | 0.811 | +0.094 | +0.019 | $18.74 | WSH:SUPPRESSED | 0.2784 | EVIDENCE_MIXED | D |
| Justin Sourdif: 1+ goals YES | 12 | 0.145 | 0.138 | +0.018 | +0.011 | $2.73 | WSH:OFFENSE_4PLUS | 0.2646 | EVIDENCE_STRONGER | D |
- **William Carrier: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-CARKMILLER19-1|yes; why: higher confidence-adjusted growth (15.67 vs 0.54 bp); despite a smaller raw edge (+0.035 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0072 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: CAR offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (7.78 vs 0.44 bp); despite a smaller raw edge (+0.038 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: WSH offense suppressed (<= 2 goals)
- **Alex Tuch: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02WSHCAR-WSHATUCH89-1|no; why: higher confidence-adjusted growth (4.64 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi -0.031); failure: WSH offense succeeds (4+ goals)
- **Justin Sourdif: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (7.78 vs 2.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.031); failure: WSH offense suppressed (<= 2 goals)

portfolios: A EV +6.85 (adj +2.88) on $34.67, P(profit) 0.3245, adj growth 25.2 bp · B EV +6.25 (adj +3.05) on $33.68, P(profit) 0.4089, adj growth 26.8 bp · C EV +2.82 (adj +1.04) on $15.35, P(profit) 0.2285, adj growth 9.1 bp

## BOS @ WPG  ·  10000 joint draws  ·  344 bet sides mapped, 3 +EV candidates, 3 on card


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
| Elias Lindholm: 1+ goals YES | 18 | 0.231 | 0.215 | +0.041 | +0.025 | $7.08 | BOS:OFFENSE_4PLUS | 0.2351 | EVIDENCE_STRONGER | D |
| Cole Perfetti: 1+ goals NO | 73 | 0.776 | 0.763 | +0.032 | +0.019 | $17.73 | WPG:SUPPRESSED | 0.2393 | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 72 | 0.840 | 0.749 | +0.106 | +0.015 | $18.74 | BOS:SUPPRESSED | 0.2384 | EVIDENCE_MIXED | D |
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02BOSWPG-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (8.40 vs 0.41 bp); despite a smaller raw edge (+0.041 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0063 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.12); failure: BOS offense suppressed (<= 2 goals)
- **Cole Perfetti: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02BOSWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (4.27 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: WPG offense succeeds (4+ goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (2.46 vs 0.26 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.12); KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: BOS offense succeeds (4+ goals)

portfolios: A EV +4.26 (adj +1.68) on $34.67, P(profit) 0.7429, adj growth 14.7 bp · B EV +4.98 (adj +1.75) on $43.54, P(profit) 0.7308, adj growth 15.4 bp · C EV +2.32 (adj +1.39) on $25.87, P(profit) 0.2314, adj growth 12.1 bp

## STL @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


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
| Dallas wins NO | 37 | 0.459 | 0.412 | +0.073 | +0.026 | $7.03 | STL:WINS | 0.2344 | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 60 | 0.681 | 0.638 | +0.064 | +0.021 | $4.26 | STL:WINS | 0.2731 | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 73 | 0.793 | 0.759 | +0.049 | +0.015 | $3.02 | STL:WINS | 0.2345 | EVIDENCE_MIXED | D |
- **Dallas wins NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT02STLDAL-DAL2|no; why: higher confidence-adjusted growth (6.09 vs 4.09 bp); wins across more scripts (relative breadth 1.033 vs 0.925); relationships: KXNHLSPREAD-26OCT02STLDAL-DAL2|no: DUPLICATIVE (phi 0.631); KXNHLSPREAD-26OCT02STLDAL-DAL3|no: DUPLICATIVE (phi 0.471); failure: DAL wins (incl. OT/SO)
- **Dallas wins by over 1.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: second expression of the same thesis: KXNHLGAME-26OCT02STLDAL-DAL|no has the higher standalone adjusted growth (6.09 vs 4.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.631); they share one thesis budget; relationships: KXNHLGAME-26OCT02STLDAL-DAL|no: DUPLICATIVE (phi 0.631); KXNHLSPREAD-26OCT02STLDAL-DAL3|no: DUPLICATIVE (phi 0.746); failure: DAL wins by 2+
- **Dallas wins by over 2.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: second expression of the same thesis: KXNHLGAME-26OCT02STLDAL-DAL|no has the higher standalone adjusted growth (6.09 vs 2.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.471); they share one thesis budget; relationships: KXNHLGAME-26OCT02STLDAL-DAL|no: DUPLICATIVE (phi 0.471); KXNHLSPREAD-26OCT02STLDAL-DAL2|no: DUPLICATIVE (phi 0.746); failure: DAL wins by 2+

portfolios: A EV +4.13 (adj +1.40) on $34.67, P(profit) 0.4591, adj growth 10.6 bp · B EV +1.96 (adj +0.67) on $14.30, P(profit) 0.4591, adj growth 6.0 bp · C EV +1.91 (adj +0.67) on $10.12, P(profit) 0.4591, adj growth 5.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02STLDAL-STL|yes == KXNHLGAME-26OCT02STLDAL-DAL|no

## ANA @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


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
| Vegas wins 3rd Period by over 1.5 goals NO | 70 | 0.802 | 0.733 | +0.087 | +0.018 | $17.60 | ANA:WINS | 0.2437 | EVIDENCE_THIN | D |
- **Vegas wins 3rd Period by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT02ANAVGK-VGK2|no; why: higher confidence-adjusted growth (3.41 vs 0.17 bp); evidence EVIDENCE_THIN vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.021 vs 0.893); alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: VGK wins by 2+

portfolios: A EV +1.70 (adj +0.35) on $13.87, P(profit) 0.8021, adj growth 3.1 bp · B EV +2.15 (adj +0.44) on $17.60, P(profit) 0.8021, adj growth 3.9 bp · C EV +2.30 (adj +0.47) on $18.78, P(profit) 0.8021, adj growth 4.1 bp

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
