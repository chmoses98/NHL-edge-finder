# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-02T18:23:19Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +38.73 | +15.36 | +31.13 | 0.656 | -56.15 | -75.95 | 124.10 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +38.73 | +21.37 | +32.17 | 0.670 | -57.53 | -74.16 | 185.86 |
| C best expression per thesis | 90.60 | +21.51 | +11.07 | +11.77 | 0.597 | -48.00 | -48.00 | 95.37 |
| R FUNDED research stakes | 8.00 | +2.97 | +2.03 | +2.20 | 0.506 | -8.00 | -8.00 | 0.00 |

## NYR @ DET  ·  10000 joint draws  ·  330 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.541 / away 0.459

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_NYR_win | p_overtime | goals | shots DET/NYR | DET/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.56 | 0.44 | 0.00 | 5.99 | 26.9/26.6 | 23.2/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.45 | 5.83 | 27.2/26.8 | 23.6/24.1 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.104 | 0.61 | 0.39 | 0.00 | 5.95 | 32.5/21.2 | 18.3/28.3 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.55 | 0.45 | 0.48 | 5.94 | 32.3/21.4 | 18.2/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.53 | 0.47 | 0.00 | 9.11 | 28.5/28.2 | 22.4/22.3 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.063 | 0.63 | 0.37 | 0.00 | 9.17 | 34.1/22.5 | 17.7/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| J.T. Compher: 1+ goals YES | 14 | 0.180 | 0.169 | +0.032 | +0.020 | $5.33 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Nate Danielson: 1+ goals YES | 10 | 0.129 | 0.121 | +0.023 | +0.015 | $3.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT02NYRDET-3|yes; why: higher confidence-adjusted growth (7.11 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.909 vs 0.792); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: DET offense suppressed (<= 2 goals)
- **Nate Danielson: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT02NYRDET-3|yes; why: higher confidence-adjusted growth (4.77 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DET:OFFENSE_4PLUS (p 0.3891): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.385, phi -0.188)
- KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.385, phi -0.157)

portfolios: A EV +2.36 (adj +1.50) on $10.96, P(profit) 0.2858, adj growth 12.6 bp · B EV +1.91 (adj +1.22) on $8.90, P(profit) 0.2858, adj growth 10.6 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ CAR  ·  10000 joint draws  ·  364 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.570 / away 0.430

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WSH_win | p_overtime | goals | shots CAR/WSH | CAR/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.139 | 0.64 | 0.36 | 0.00 | 6.01 | 33.0/20.7 | 17.9/28.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.125 | 0.53 | 0.47 | 0.46 | 5.87 | 33.4/21.0 | 17.8/29.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.59 | 0.41 | 0.00 | 6.04 | 27.4/26.6 | 23.4/23.5 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.096 | 0.66 | 0.34 | 0.00 | 9.21 | 35.2/22.3 | 17.5/27.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.50 | 0.50 | 0.48 | 5.91 | 27.2/26.5 | 23.2/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.57 | 0.43 | 0.00 | 9.22 | 28.9/27.9 | 22.4/22.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Carrier: 1+ goals YES | 8 | 0.126 | 0.113 | +0.041 | +0.028 | $6.28 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CAR:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Justin Sourdif: 1+ goals YES | 10 | 0.150 | 0.135 | +0.044 | +0.029 | $6.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 18 | 0.234 | 0.220 | +0.044 | +0.029 | $8.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Alex Tuch: 1+ assists NO | 75 | 0.877 | 0.791 | +0.114 | +0.028 | $18.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
- **William Carrier: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02WSHCAR-CARJMARTINOOK48-1|yes; why: higher confidence-adjusted growth (21.20 vs 0.74 bp); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: CAR offense suppressed (<= 2 goals)
- **Justin Sourdif: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes; why: higher confidence-adjusted growth (18.45 vs 11.89 bp); despite a smaller raw edge (+0.044 vs +0.044/contract); relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.037); failure: WSH offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (11.89 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.033); failure: WSH offense suppressed (<= 2 goals)
- **Alex Tuch: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02WSHCAR-WSHATUCH89-1|no; why: higher confidence-adjusted growth (9.59 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.033); failure: WSH offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3285): highest fidelity KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes (same contract)
- thesis CAR:OFFENSE_4PLUS (p 0.4271): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis WSH:SUPPRESSED (p 0.4491): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:SUPPRESSED (p 0.3589, phi -0.15)
- KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4491, phi -0.19)
- KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4491, phi -0.262)
- KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.2 pts; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.3285, phi -0.157)

portfolios: A EV +10.04 (adj +5.96) on $34.76, P(profit) 0.4299, adj growth 51.3 bp · B EV +10.45 (adj +5.81) on $40.03, P(profit) 0.4299, adj growth 50.7 bp · C EV +1.96 (adj +1.30) on $8.50, P(profit) 0.2343, adj growth 11.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ WPG  ·  10000 joint draws  ·  346 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.523 / away 0.477

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_BOS_win | p_overtime | goals | shots WPG/BOS | WPG/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.51 | 0.49 | 0.00 | 5.99 | 27.3/27.0 | 23.3/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.52 | 0.48 | 0.47 | 5.9 | 27.2/27.0 | 23.8/24.0 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.088 | 0.56 | 0.44 | 0.00 | 6.01 | 32.4/21.4 | 18.3/28.6 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.53 | 0.47 | 0.49 | 5.92 | 32.4/21.9 | 18.7/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.52 | 0.48 | 0.00 | 9.22 | 29.0/28.7 | 22.8/23.0 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.50 | 0.50 | 0.50 | 2.81 | 26.1/25.8 | 24.3/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Marat Khusnutdinov: 1+ goals YES | 9 | 0.145 | 0.121 | +0.049 | +0.025 | $5.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Elias Lindholm: 1+ goals YES | 18 | 0.231 | 0.217 | +0.040 | +0.026 | $7.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 28 | 0.339 | 0.323 | +0.045 | +0.029 | $9.53 | FUNDED_RESEARCH | $3 | WPG:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 72 | 0.836 | 0.748 | +0.102 | +0.013 | $18.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (15.64 vs 9.75 bp); relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: BOS offense suppressed (<= 2 goals)
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes has the higher standalone adjusted growth (15.64 vs 9.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.12); failure: BOS offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT02BOSWPG-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (8.60 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: WPG offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02BOSWPG-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (2.04 vs 0.14 bp); despite a smaller raw edge (+0.102 vs +0.114/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.12); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, WPG shot control · normal event (5-7) · decided (2+) 0.09.
- thesis BOS:OFFENSE_4PLUS (p 0.3523): highest fidelity KXNHLGOAL-26OCT02BOSWPG-BOSPZACHA18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3661): highest fidelity KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes (same contract)
- thesis WPG:SUPPRESSED (p 0.4128): highest fidelity KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no (same contract)
- KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4201, phi -0.189)
- KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4201, phi -0.222)
- KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4128, phi -0.279)
- KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.6 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3523, phi -0.186)

portfolios: A EV +8.27 (adj +4.05) on $34.76, P(profit) 0.5416, adj growth 34.5 bp · B EV +8.52 (adj +3.80) on $41.82, P(profit) 0.5097, adj growth 33.2 bp · C EV +4.96 (adj +2.78) on $30.74, P(profit) 0.4367, adj growth 24.0 bp · R EV +0.45 (adj +0.29) on $3.00, P(profit) 0.3387, adj growth 9.8 bp

## STL @ DAL  ·  10000 joint draws  ·  334 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.625 / away 0.375

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_STL_win | p_overtime | goals | shots DAL/STL | DAL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.55 | 0.45 | 0.00 | 5.98 | 25.9/25.6 | 22.4/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.47 | 5.95 | 26.0/25.8 | 22.6/22.6 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.093 | 0.61 | 0.39 | 0.00 | 6.0 | 30.9/20.4 | 17.5/26.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.57 | 0.43 | 0.00 | 9.21 | 27.7/27.6 | 22.1/21.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.56 | 0.44 | 0.50 | 5.92 | 31.0/20.5 | 17.4/27.6 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.057 | 0.63 | 0.37 | 0.00 | 9.21 | 32.3/21.7 | 16.9/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pius Suter: 1+ goals YES | 10 | 0.158 | 0.142 | +0.052 | +0.036 | $8.60 | FUNDED_RESEARCH | $3 | STL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Jonatan Berggren: 1+ goals YES | 9 | 0.126 | 0.116 | +0.030 | +0.020 | $4.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Tyler Myers: 1+ goals YES | 4 | 0.063 | 0.056 | +0.020 | +0.013 | $2.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Mason McTavish: 1+ assists NO | 74 | 0.874 | 0.777 | +0.121 | +0.024 | $18.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: higher confidence-adjusted growth (29.11 vs 8.37 bp); despite a smaller raw edge (+0.052 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02STLDAL-STLJBERGGREN29-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT02STLDAL-DALTMYERS57-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: INTENTIONAL_DIVERSIFIER (phi -0.054); failure: STL offense suppressed (<= 2 goals)
- **Jonatan Berggren: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes has the higher standalone adjusted growth (29.11 vs 9.76 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT02STLDAL-DALTMYERS57-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: STL offense suppressed (<= 2 goals)
- **Tyler Myers: 1+ goals YES** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT02STLDAL-STLJBERGGREN29-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: DAL offense suppressed (<= 2 goals)
- **Mason McTavish: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02STLDAL-STLMMCTAVISH83-1|no; why: higher confidence-adjusted growth (6.72 vs 0.26 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.054); KXNHLGOAL-26OCT02STLDAL-STLJBERGGREN29-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT02STLDAL-DALTMYERS57-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: STL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.3441): highest fidelity KXNHLTEAMTOTAL-26OCT02STLDAL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4586): highest fidelity KXNHLGAME-26OCT02STLDAL-DAL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-DAL|no (same contract)
- thesis DAL:SUPPRESSED (p 0.3803): highest fidelity KXNHLSPREAD-26OCT02STLDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-DAL|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.432, phi -0.208)
- KXNHLGOAL-26OCT02STLDAL-STLJBERGGREN29-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.432, phi -0.165)
- KXNHLGOAL-26OCT02STLDAL-DALTMYERS57-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3803, phi -0.099)
- KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.9 pts; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.3441, phi -0.177)

portfolios: A EV +4.73 (adj +1.51) on $34.76, P(profit) 0.5711, adj growth 13.2 bp · B EV +10.03 (adj +5.35) on $35.04, P(profit) 0.3097, adj growth 46.5 bp · C EV +7.37 (adj +4.56) on $21.20, P(profit) 0.5536, adj growth 38.9 bp · R EV +1.47 (adj +1.02) on $3.00, P(profit) 0.1583, adj growth 32.7 bp

## ANA @ VGK  ·  10000 joint draws  ·  358 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.633 / away 0.367

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_ANA_win | p_overtime | goals | shots VGK/ANA | VGK/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.65 | 0.35 | 0.00 | 6.01 | 28.0/28.1 | 25.3/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.45 | 5.91 | 28.1/28.3 | 25.0/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.65 | 0.35 | 0.00 | 9.37 | 29.8/29.9 | 24.5/22.6 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.079 | 0.60 | 0.40 | 0.00 | 6.03 | 22.4/33.6 | 30.2/18.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.48 | 5.9 | 22.3/33.3 | 29.9/19.0 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.064 | 0.68 | 0.32 | 0.00 | 6.04 | 32.9/22.3 | 19.8/27.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Washe: 1+ goals YES | 7 | 0.114 | 0.102 | +0.039 | +0.027 | $5.98 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 18 | 0.233 | 0.218 | +0.043 | +0.028 | $7.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Marc Gatcomb: 1+ goals YES | 8 | 0.116 | 0.104 | +0.031 | +0.019 | $4.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Braeden Bowman: 1+ goals YES | 15 | 0.195 | 0.182 | +0.036 | +0.024 | $6.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (22.20 vs 11.12 bp); despite a smaller raw edge (+0.039 vs +0.043/contract); relationships: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT02ANAVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (11.12 vs 8.38 bp); despite a smaller raw edge (+0.043 vs +0.127/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT02ANAVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: ANA offense suppressed (<= 2 goals)
- **Marc Gatcomb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-VGKRANDERSSON4-1|yes; why: higher confidence-adjusted growth (10.11 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: VGK offense suppressed (<= 2 goals)
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-VGKRANDERSSON4-1|yes; why: higher confidence-adjusted growth (8.97 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT02ANAVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3348): highest fidelity KXNHLGAME-26OCT02ANAVGK-VGK|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.4051): highest fidelity KXNHLGAME-26OCT02ANAVGK-VGK|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:SUPPRESSED (p 0.4499): highest fidelity KXNHLAST-26OCT02ANAVGK-ANALCARLSSON91-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT02ANAVGK-ANALCARLSSON91-1|no (same contract)
- KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4499, phi -0.185)
- KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4499, phi -0.245)
- KXNHLGOAL-26OCT02ANAVGK-VGKMGATCOMB17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3161, phi -0.128)
- KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3161, phi -0.168)

portfolios: A EV +13.32 (adj +2.34) on $34.76, P(profit) 0.4754, adj growth 12.5 bp · B EV +7.82 (adj +5.19) on $24.21, P(profit) 0.5163, adj growth 44.8 bp · C EV +7.22 (adj +2.43) on $30.16, P(profit) 0.5159, adj growth 21.1 bp · R EV +1.05 (adj +0.72) on $2.00, P(profit) 0.1137, adj growth 23.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02ANAVGK-VGK|no == KXNHLGAME-26OCT02ANAVGK-ANA|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
