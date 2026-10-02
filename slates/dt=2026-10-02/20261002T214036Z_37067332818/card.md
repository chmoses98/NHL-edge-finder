# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-02T21:40:36Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +30.12 | +11.09 | +24.36 | 0.699 | -31.01 | -44.53 | 98.14 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +28.53 | +16.76 | +21.96 | 0.639 | -48.87 | -62.55 | 148.38 |
| C best expression per thesis | 139.92 | +25.39 | +10.98 | +19.82 | 0.654 | -40.47 | -54.88 | 95.38 |
| R FUNDED research stakes | 19.00 | +3.14 | +1.93 | +0.78 | 0.576 | -10.15 | -13.25 | 0.00 |

## NYR @ DET  ·  10000 joint draws  ·  330 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.543 / away 0.457

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_NYR_win | p_overtime | goals | shots DET/NYR | DET/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.56 | 0.44 | 0.00 | 5.99 | 27.1/26.8 | 23.4/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.46 | 5.89 | 27.1/26.7 | 23.6/23.9 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.107 | 0.63 | 0.37 | 0.00 | 6.03 | 32.6/21.3 | 18.4/28.0 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.56 | 0.44 | 0.49 | 5.92 | 32.3/21.4 | 18.3/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.51 | 0.49 | 0.00 | 9.25 | 28.6/28.2 | 22.1/22.5 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.064 | 0.65 | 0.35 | 0.00 | 9.18 | 34.0/22.3 | 17.8/26.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| J.T. Compher: 1+ goals YES | 14 | 0.184 | 0.172 | +0.036 | +0.024 | $5.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Oliver Bjorkstrand: 1+ goals NO | 82 | 0.863 | 0.851 | +0.033 | +0.021 | $14.53 | FUNDED_RESEARCH | $4 | NYR:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Nate Danielson: 1+ goals YES | 10 | 0.126 | 0.119 | +0.020 | +0.012 | $2.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ assists NO | 72 | 0.825 | 0.750 | +0.091 | +0.016 | $10.73 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT02NYRDET-3|yes; why: higher confidence-adjusted growth (9.39 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.93 vs 0.794); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-NYROBJORKSTRAND28-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: DET offense suppressed (<= 2 goals)
- **Oliver Bjorkstrand: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02NYRDET-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (6.81 vs 0.01 bp); despite a smaller raw edge (+0.033 vs +0.071/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0008 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no: REINFORCING (phi 0.195); failure: NYR offense succeeds (4+ goals)
- **Nate Danielson: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT02NYRDET-3|yes; why: higher confidence-adjusted growth (3.41 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.902 vs 0.794); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT02NYRDET-NYROBJORKSTRAND28-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: DET offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02NYRDET-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (2.89 vs 0.01 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0008 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT02NYRDET-NYROBJORKSTRAND28-1|no: REINFORCING (phi 0.195); KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.11.
- thesis DET:OFFENSE_4PLUS (p 0.3987): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis NYR:SUPPRESSED (p 0.4499): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3796, phi -0.186)
- KXNHLGOAL-26OCT02NYRDET-NYROBJORKSTRAND28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3386, phi -0.178)
- KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3796, phi -0.163)
- KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.5 pts; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3386, phi -0.19)

portfolios: A EV +3.66 (adj +1.74) on $30.00, P(profit) 0.2806, adj growth 15.5 bp · B EV +3.69 (adj +1.75) on $33.27, P(profit) 0.2806, adj growth 15.8 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.16 (adj +0.10) on $4.00, P(profit) 0.8632, adj growth 3.8 bp

## WSH @ CAR  ·  10000 joint draws  ·  364 bet sides mapped, 10 +EV candidates, 4 on card

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
| Justin Sourdif: 1+ goals YES | 10 | 0.150 | 0.136 | +0.044 | +0.030 | $6.31 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 18 | 0.234 | 0.220 | +0.044 | +0.029 | $7.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Alex Tuch: 1+ assists NO | 75 | 0.877 | 0.791 | +0.114 | +0.028 | $16.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| William Carrier: 1+ goals YES | 9 | 0.126 | 0.114 | +0.030 | +0.019 | $3.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
- **Justin Sourdif: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes; why: higher confidence-adjusted growth (20.07 vs 11.89 bp); despite a smaller raw edge (+0.044 vs +0.044/contract); relationships: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: WSH offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (11.89 vs 0.20 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0044 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: WSH offense suppressed (<= 2 goals)
- **Alex Tuch: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT02WSHCAR-WSHRLEONARD9-1|no; why: higher confidence-adjusted growth (9.59 vs 1.85 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: WSH offense succeeds (4+ goals)
- **William Carrier: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-CARKMILLER19-1|yes; why: higher confidence-adjusted growth (8.58 vs 1.37 bp); despite a smaller raw edge (+0.030 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: CAR offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3285): highest fidelity KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes (same contract)
- thesis CAR:SUPPRESSED (p 0.3589): highest fidelity KXNHLAST-26OCT02WSHCAR-CARSAHO20-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT02WSHCAR-CARSAHO20-1|no (same contract)
- thesis WSH:SUPPRESSED (p 0.4491): highest fidelity KXNHLGOAL-26OCT02WSHCAR-WSHRLEONARD9-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT02WSHCAR-WSHRLEONARD9-1|no (same contract)
- KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4491, phi -0.19)
- KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4491, phi -0.262)
- KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.2 pts; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.3285, phi -0.157)
- KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:SUPPRESSED (p 0.3589, phi -0.15)

portfolios: A EV +5.04 (adj +1.72) on $30.00, P(profit) 0.4945, adj growth 15.4 bp · B EV +7.96 (adj +4.24) on $34.16, P(profit) 0.4299, adj growth 37.8 bp · C EV +4.72 (adj +2.00) on $38.46, P(profit) 0.3716, adj growth 17.4 bp · R EV +0.82 (adj +0.56) on $2.00, P(profit) 0.15, adj growth 19.0 bp

## BOS @ WPG  ·  10000 joint draws  ·  346 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.521 / away 0.479

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
| Marat Khusnutdinov: 1+ goals YES | 9 | 0.145 | 0.130 | +0.049 | +0.034 | $6.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Elias Lindholm: 1+ goals YES | 18 | 0.231 | 0.217 | +0.040 | +0.026 | $6.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 29 | 0.339 | 0.325 | +0.034 | +0.021 | $6.46 | FUNDED_RESEARCH | $2 | WPG:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 63 | 0.669 | 0.658 | +0.023 | +0.012 | $6.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (28.11 vs 9.75 bp); relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: BOS offense suppressed (<= 2 goals)
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes has the higher standalone adjusted growth (28.11 vs 9.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: BOS offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (4.48 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: WPG offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02BOSWPG-BOSJPETERKA10-1|no; why: Player prop expression KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.82 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, WPG shot control · normal event (5-7) · decided (2+) 0.09.
- thesis BOS:OFFENSE_4PLUS (p 0.3523): highest fidelity KXNHLAST-26OCT02BOSWPG-BOSELINDHOLM28-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3661): highest fidelity KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.4201): highest fidelity KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no [DIRECT], best adjusted EV KXNHLPTS-26OCT02BOSWPG-BOSJPETERKA10-1|no — Player prop expression KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.82 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4201, phi -0.189)
- KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4201, phi -0.222)
- KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4128, phi -0.279)
- KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3523, phi -0.26)
- override: Player prop expression KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.82 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.53 (adj +2.80) on $30.00, P(profit) 0.3772, adj growth 24.6 bp · B EV +5.85 (adj +3.91) on $26.51, P(profit) 0.4942, adj growth 34.3 bp · C EV +7.00 (adj +3.64) on $23.17, P(profit) 0.4367, adj growth 31.1 bp · R EV +0.23 (adj +0.14) on $2.00, P(profit) 0.3387, adj growth 4.7 bp

## STL @ DAL  ·  10000 joint draws  ·  334 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.620 / away 0.380

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
| Dallas wins NO | 37 | 0.459 | 0.416 | +0.072 | +0.030 | $5.43 | FUNDED_RESEARCH | $2 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | B |
| Mikko Rantanen: 1+ goals NO | 68 | 0.738 | 0.723 | +0.043 | +0.027 | $15.91 | FUNDED_RESEARCH | $4 | DAL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Dylan Holloway: 1+ goals YES | 26 | 0.312 | 0.298 | +0.039 | +0.025 | $5.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 73 | 0.805 | 0.765 | +0.062 | +0.021 | $8.62 | FUNDED_RESEARCH | $3 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGAME-26OCT02STLDAL-STL|yes; why: best adjusted growth among the thesis's expressions; relationships: KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: REINFORCING (phi 0.19); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: REINFORCING (phi 0.182); KXNHLSPREAD-26OCT02STLDAL-DAL3|no: DUPLICATIVE (phi 0.452); failure: DAL wins (incl. OT/SO)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT02STLDAL-DALMRANTANEN96-2|no; why: KXNHLAST-26OCT02STLDAL-DALMRANTANEN96-2|no has the higher standalone adjusted growth (12.72 vs 7.71 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.006); relationships: KXNHLGAME-26OCT02STLDAL-DAL|no: REINFORCING (phi 0.19); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLSPREAD-26OCT02STLDAL-DAL3|no: REINFORCING (phi 0.152); failure: DAL offense succeeds (4+ goals)
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: second expression of the same thesis: KXNHLGAME-26OCT02STLDAL-DAL|no has the higher standalone adjusted growth (8.37 vs 6.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.182); they share one thesis budget; relationships: KXNHLGAME-26OCT02STLDAL-DAL|no: REINFORCING (phi 0.182); KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLSPREAD-26OCT02STLDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.149); failure: STL offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGAME-26OCT02STLDAL-DAL|no; why: Broad expression KXNHLSPREAD-26OCT02STLDAL-DAL3|no selected over player prop KXNHLAST-26OCT02STLDAL-DALMRANTANEN96-2|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGAME-26OCT02STLDAL-DAL|no: DUPLICATIVE (phi 0.452); KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: REINFORCING (phi 0.152); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.149); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis DAL:SUPPRESSED (p 0.3803): highest fidelity KXNHLSPREAD-26OCT02STLDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-STL|yes — Broad expression KXNHLSPREAD-26OCT02STLDAL-DAL3|no selected over player prop KXNHLAST-26OCT02STLDAL-DALMRANTANEN96-2|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis STL:WINS (p 0.4586): highest fidelity KXNHLGAME-26OCT02STLDAL-STL|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-STL|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3441): highest fidelity KXNHLTEAMTOTAL-26OCT02STLDAL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-STL|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGAME-26OCT02STLDAL-DAL|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.5414, phi -1.0)
- KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4013, phi -0.231)
- KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.432, phi -0.266)
- KXNHLSPREAD-26OCT02STLDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3096, phi -0.734)
- override: Broad expression KXNHLSPREAD-26OCT02STLDAL-DAL3|no selected over player prop KXNHLAST-26OCT02STLDAL-DALMRANTANEN96-2|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.77 (adj +0.74) on $30.00, P(profit) 0.5894, adj growth 6.9 bp · B EV +3.51 (adj +1.80) on $35.56, P(profit) 0.4922, adj growth 16.1 bp · C EV +5.36 (adj +2.55) on $34.92, P(profit) 0.4828, adj growth 22.6 bp · R EV +0.87 (adj +0.40) on $9.00, P(profit) 0.6995, adj growth 14.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02STLDAL-STL|yes == KXNHLGAME-26OCT02STLDAL-DAL|no

## ANA @ VGK  ·  10000 joint draws  ·  358 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.642 / away 0.358

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_ANA_win | p_overtime | goals | shots VGK/ANA | VGK/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.66 | 0.34 | 0.00 | 6.03 | 28.1/28.2 | 25.3/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.54 | 0.46 | 0.50 | 5.97 | 28.0/28.1 | 24.8/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.66 | 0.34 | 0.00 | 9.35 | 29.5/29.6 | 24.3/22.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.076 | 0.62 | 0.38 | 0.00 | 6.04 | 22.5/33.4 | 30.2/18.7 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.48 | 0.52 | 0.47 | 5.9 | 22.5/33.5 | 30.2/19.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.061 | 0.70 | 0.30 | 0.00 | 6.02 | 32.6/22.3 | 19.7/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Washe: 1+ goals YES | 7 | 0.114 | 0.102 | +0.040 | +0.027 | $5.33 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 7 | 0.105 | 0.095 | +0.030 | +0.021 | $4.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 18 | 0.233 | 0.218 | +0.043 | +0.028 | $6.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Marc Gatcomb: 1+ goals YES | 8 | 0.115 | 0.105 | +0.030 | +0.020 | $4.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (22.68 vs 11.06 bp); despite a smaller raw edge (+0.040 vs +0.043/contract); relationships: KXNHLGOAL-26OCT02ANAVGK-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT02ANAVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (12.96 vs 11.06 bp); despite a smaller raw edge (+0.031 vs +0.043/contract); relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT02ANAVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (11.06 vs 9.14 bp); despite a smaller raw edge (+0.043 vs +0.121/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT02ANAVGK-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT02ANAVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: ANA offense suppressed (<= 2 goals)
- **Marc Gatcomb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-VGKRANDERSSON4-1|yes; why: higher confidence-adjusted growth (10.71 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT02ANAVGK-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3325): highest fidelity KXNHLGAME-26OCT02ANAVGK-VGK|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.4029): highest fidelity KXNHLGAME-26OCT02ANAVGK-VGK|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:SUPPRESSED (p 0.4449): highest fidelity KXNHLAST-26OCT02ANAVGK-ANALCARLSSON91-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT02ANAVGK-ANALCARLSSON91-1|no (same contract)
- KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.176)
- KXNHLGOAL-26OCT02ANAVGK-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.145)
- KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.241)
- KXNHLGOAL-26OCT02ANAVGK-VGKMGATCOMB17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3145, phi -0.133)

portfolios: A EV +10.12 (adj +4.09) on $30.00, P(profit) 0.5592, adj growth 35.7 bp · B EV +7.50 (adj +5.06) on $20.51, P(profit) 0.4637, adj growth 44.4 bp · C EV +8.31 (adj +2.79) on $43.37, P(profit) 0.487, adj growth 24.3 bp · R EV +1.06 (adj +0.73) on $2.00, P(profit) 0.1141, adj growth 23.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02ANAVGK-VGK|no == KXNHLGAME-26OCT02ANAVGK-ANA|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
