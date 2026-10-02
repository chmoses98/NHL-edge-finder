# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-02T17:33:17Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +34.14 | +13.60 | +30.15 | 0.685 | -43.97 | -61.53 | 116.45 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +34.46 | +20.49 | +28.14 | 0.636 | -49.60 | -81.61 | 178.66 |
| C best expression per thesis | 86.38 | +19.45 | +9.15 | +11.61 | 0.595 | -40.21 | -51.43 | 78.88 |
| R FUNDED research stakes | 12.00 | +2.56 | +1.73 | -6.54 | 0.472 | -6.54 | -6.54 | 0.00 |

## NYR @ DET  ·  10000 joint draws  ·  330 bet sides mapped, 3 +EV candidates, 3 on card

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
| J.T. Compher: 1+ goals YES | 14 | 0.180 | 0.169 | +0.032 | +0.020 | $5.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Nate Danielson: 1+ goals YES | 10 | 0.129 | 0.121 | +0.023 | +0.015 | $3.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Sean Durzi: 1+ goals NO | 91 | 0.935 | 0.927 | +0.019 | +0.012 | $18.50 | FUNDED_RESEARCH | $5 | NYR:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT02NYRDET-3|yes; why: higher confidence-adjusted growth (7.11 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.909 vs 0.792); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT02NYRDET-NYRSDURZI5-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: DET offense suppressed (<= 2 goals)
- **Nate Danielson: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT02NYRDET-3|yes; why: higher confidence-adjusted growth (4.77 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT02NYRDET-NYRSDURZI5-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: DET offense suppressed (<= 2 goals)
- **Sean Durzi: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02NYRDET-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (3.99 vs 0.00 bp); despite a smaller raw edge (+0.019 vs +0.067/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DET:OFFENSE_4PLUS (p 0.3891): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis NYR:SUPPRESSED (p 0.4444): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.385, phi -0.188)
- KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.385, phi -0.157)
- KXNHLGOAL-26OCT02NYRDET-NYRSDURZI5-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3355, phi -0.148)

portfolios: A EV +2.42 (adj +1.54) on $22.75, P(profit) 0.2858, adj growth 13.3 bp · B EV +2.25 (adj +1.42) on $27.14, P(profit) 0.2858, adj growth 12.6 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.11 (adj +0.06) on $5.00, P(profit) 0.935, adj growth 2.4 bp

## WSH @ CAR  ·  10000 joint draws  ·  364 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.569 / away 0.431

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
| William Carrier: 1+ goals YES | 8 | 0.126 | 0.113 | +0.041 | +0.028 | $6.12 | FUNDED_RESEARCH | $2 | CAR:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Justin Sourdif: 1+ goals YES | 10 | 0.150 | 0.136 | +0.044 | +0.030 | $6.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 18 | 0.234 | 0.220 | +0.044 | +0.029 | $7.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Alex Tuch: 1+ assists NO | 76 | 0.877 | 0.794 | +0.104 | +0.022 | $18.50 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
- **William Carrier: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02WSHCAR-CARJMARTINOOK48-1|yes; why: higher confidence-adjusted growth (21.20 vs 4.37 bp); relationships: KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: CAR offense suppressed (<= 2 goals)
- **Justin Sourdif: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes; why: higher confidence-adjusted growth (20.07 vs 11.89 bp); despite a smaller raw edge (+0.044 vs +0.044/contract); relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.037); failure: WSH offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (11.89 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.033); failure: WSH offense suppressed (<= 2 goals)
- **Alex Tuch: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02WSHCAR-WSHATUCH89-1|no; why: higher confidence-adjusted growth (5.87 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.033); failure: WSH offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3285): highest fidelity KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes (same contract)
- thesis CAR:OFFENSE_4PLUS (p 0.4271): highest fidelity KXNHLGOAL-26OCT02WSHCAR-CARJMARTINOOK48-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT02WSHCAR-CARJMARTINOOK48-1|yes (same contract)
- thesis WSH:SUPPRESSED (p 0.4491): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:SUPPRESSED (p 0.3589, phi -0.15)
- KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4491, phi -0.19)
- KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4491, phi -0.262)
- KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.7 pts; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.3285, phi -0.157)

portfolios: A EV +9.03 (adj +5.44) on $31.81, P(profit) 0.4299, adj growth 47.4 bp · B EV +10.06 (adj +5.67) on $39.38, P(profit) 0.4299, adj growth 49.5 bp · C EV +2.76 (adj +1.79) on $13.06, P(profit) 0.3696, adj growth 15.5 bp · R EV +0.95 (adj +0.66) on $2.00, P(profit) 0.1258, adj growth 21.6 bp

## BOS @ WPG  ·  10000 joint draws  ·  346 bet sides mapped, 9 +EV candidates, 4 on card

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
| Marat Khusnutdinov: 1+ goals YES | 9 | 0.145 | 0.130 | +0.049 | +0.034 | $7.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Mark Kastelic: 1+ goals YES | 8 | 0.118 | 0.107 | +0.033 | +0.022 | $4.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Elias Lindholm: 1+ goals YES | 18 | 0.231 | 0.217 | +0.040 | +0.026 | $6.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 28 | 0.339 | 0.323 | +0.045 | +0.029 | $9.42 | FUNDED_RESEARCH | $3 | WPG:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (28.11 vs 9.75 bp); relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: BOS offense suppressed (<= 2 goals)
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes has the higher standalone adjusted growth (28.11 vs 13.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: BOS offense suppressed (<= 2 goals)
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes has the higher standalone adjusted growth (28.11 vs 9.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT02BOSWPG-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: BOS offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02BOSWPG-WPGCPERFETTI91-1|yes; why: higher confidence-adjusted growth (8.60 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT02BOSWPG-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, WPG shot control · normal event (5-7) · decided (2+) 0.09.
- thesis BOS:OFFENSE_4PLUS (p 0.3523): highest fidelity KXNHLGOAL-26OCT02BOSWPG-BOSPZACHA18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3661): highest fidelity KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes (same contract)
- thesis WPG:SUPPRESSED (p 0.4128): highest fidelity KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no (same contract)
- KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4201, phi -0.189)
- KXNHLGOAL-26OCT02BOSWPG-BOSMKASTELIC47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4201, phi -0.175)
- KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4201, phi -0.222)
- KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4128, phi -0.279)

portfolios: A EV +7.69 (adj +3.32) on $31.81, P(profit) 0.3919, adj growth 29.3 bp · B EV +8.70 (adj +5.87) on $28.91, P(profit) 0.6203, adj growth 50.9 bp · C EV +8.14 (adj +4.41) on $40.98, P(profit) 0.4163, adj growth 37.8 bp · R EV +0.45 (adj +0.29) on $3.00, P(profit) 0.3387, adj growth 9.8 bp

## STL @ DAL  ·  10000 joint draws  ·  334 bet sides mapped, 17 +EV candidates, 4 on card

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
| Pius Suter: 1+ goals YES | 11 | 0.157 | 0.143 | +0.040 | +0.026 | $6.07 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Philip Broberg: 1+ goals YES | 7 | 0.098 | 0.090 | +0.023 | +0.015 | $3.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Dylan Holloway: 1+ goals YES | 26 | 0.313 | 0.298 | +0.039 | +0.025 | $7.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Mason McTavish: 1+ assists NO | 75 | 0.869 | 0.782 | +0.106 | +0.019 | $18.50 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: higher confidence-adjusted growth (13.74 vs 8.37 bp); despite a smaller raw edge (+0.040 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02STLDAL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: INTENTIONAL_DIVERSIFIER (phi -0.052); failure: STL offense suppressed (<= 2 goals)
- **Philip Broberg: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes has the higher standalone adjusted growth (13.74 vs 7.02 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.042); failure: STL offense suppressed (<= 2 goals)
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes has the higher standalone adjusted growth (13.74 vs 6.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.025); they share one thesis budget; relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT02STLDAL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: INTENTIONAL_DIVERSIFIER (phi -0.056); failure: STL offense suppressed (<= 2 goals)
- **Mason McTavish: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02STLDAL-STLMMCTAVISH83-1|no; why: higher confidence-adjusted growth (4.25 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT02STLDAL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.056); failure: STL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.3441): highest fidelity KXNHLTEAMTOTAL-26OCT02STLDAL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-DAL|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4586): highest fidelity KXNHLGAME-26OCT02STLDAL-DAL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-DAL|no (same contract)
- thesis STL:WINS_BY_2PLUS (p 0.2496): highest fidelity KXNHLGAME-26OCT02STLDAL-DAL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-DAL|no (same contract)
- KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.432, phi -0.212)
- KXNHLGOAL-26OCT02STLDAL-STLPBROBERG6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.432, phi -0.146)
- KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.432, phi -0.266)
- KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.4 pts; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.3441, phi -0.178)

portfolios: A EV +6.05 (adj +1.68) on $31.81, P(profit) 0.6185, adj growth 14.6 bp · B EV +6.82 (adj +3.19) on $35.74, P(profit) 0.4379, adj growth 28.1 bp · C EV +3.90 (adj +2.09) on $15.92, P(profit) 0.5161, adj growth 18.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## ANA @ VGK  ·  10000 joint draws  ·  358 bet sides mapped, 10 +EV candidates, 4 on card

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
| Tim Washe: 1+ goals YES | 7 | 0.113 | 0.101 | +0.039 | +0.027 | $5.86 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Braeden Bowman: 1+ goals YES | 15 | 0.195 | 0.182 | +0.036 | +0.024 | $6.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 7 | 0.098 | 0.090 | +0.024 | +0.015 | $3.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 8 | 0.113 | 0.101 | +0.027 | +0.015 | $3.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (21.83 vs 6.84 bp); despite a smaller raw edge (+0.039 vs +0.120/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT02ANAVGK-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: ANA offense suppressed (<= 2 goals)
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-VGKRANDERSSON4-1|yes; why: higher confidence-adjusted growth (8.97 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT02ANAVGK-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: VGK offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (7.37 vs 6.84 bp); despite a smaller raw edge (+0.024 vs +0.120/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: ANA offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (6.84 vs 6.59 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.060); relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT02ANAVGK-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3348): highest fidelity KXNHLGAME-26OCT02ANAVGK-VGK|no [DIRECT], best adjusted EV KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.4051): highest fidelity KXNHLGAME-26OCT02ANAVGK-VGK|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:SUPPRESSED (p 0.4499): highest fidelity KXNHLAST-26OCT02ANAVGK-ANALCARLSSON91-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT02ANAVGK-ANALCARLSSON91-1|no (same contract)
- KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4499, phi -0.185)
- KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3161, phi -0.168)
- KXNHLGOAL-26OCT02ANAVGK-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4499, phi -0.149)
- KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4499, phi -0.159)

portfolios: A EV +8.94 (adj +1.62) on $31.81, P(profit) 0.4866, adj growth 11.9 bp · B EV +6.63 (adj +4.34) on $18.84, P(profit) 0.4298, adj growth 37.6 bp · C EV +4.64 (adj +0.86) on $16.42, P(profit) 0.362, adj growth 7.5 bp · R EV +1.04 (adj +0.72) on $2.00, P(profit) 0.1134, adj growth 23.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02ANAVGK-VGK|no == KXNHLGAME-26OCT02ANAVGK-ANA|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
