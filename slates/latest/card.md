# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-13T22:36:16Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +30.63 | +7.14 | +30.08 | 0.865 | -4.85 | -14.59 | 67.34 |
| B thesis-diversified (joint) ← optimiser card | 147.31 | +26.28 | +14.10 | +24.31 | 0.772 | -15.54 | -26.04 | 134.95 |
| C best expression per thesis | 149.02 | +22.16 | +8.58 | +21.40 | 0.819 | -8.62 | -16.64 | 82.82 |
| R FUNDED research stakes | 17.00 | +2.38 | +1.58 | +0.83 | 0.519 | -4.76 | -6.57 | 0.00 |

## WSH @ CAR  ·  10000 joint draws  ·  460 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.582 / away 0.418

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WSH_win | p_overtime | goals | shots CAR/WSH | CAR/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.153 | 0.65 | 0.35 | 0.00 | 6.0 | 33.4/21.1 | 18.2/28.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.137 | 0.57 | 0.43 | 0.46 | 5.88 | 33.6/21.1 | 18.0/30.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.106 | 0.66 | 0.34 | 0.00 | 9.24 | 35.3/22.5 | 17.8/27.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.093 | 0.58 | 0.42 | 0.00 | 6.03 | 27.7/26.8 | 23.4/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.50 | 0.50 | 0.49 | 5.93 | 27.5/26.7 | 23.5/24.1 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.071 | 0.59 | 0.41 | 0.00 | 3.48 | 32.1/19.6 | 18.1/29.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 17 | 0.219 | 0.206 | +0.039 | +0.026 | $2.33 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Jesperi Kotkaniemi: 1+ goals YES | 11 | 0.144 | 0.133 | +0.027 | +0.016 | $1.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Justin Sourdif: 1+ goals YES | 11 | 0.139 | 0.131 | +0.022 | +0.014 | $1.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ assists NO | 54 | 0.659 | 0.578 | +0.101 | +0.021 | $4.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CAR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13WSHCAR-WSHAOVECHKIN8-1|yes; why: higher confidence-adjusted growth (9.78 vs 6.00 bp); despite a smaller raw edge (+0.039 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13WSHCAR-CARJKOTKANIEMI82-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT13WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: WSH offense suppressed (<= 2 goals)
- **Jesperi Kotkaniemi: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13WSHCAR-CARMJANKOWSKI77-1|yes; why: higher confidence-adjusted growth (5.45 vs 1.71 bp); relationships: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT13WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.029); failure: CAR offense suppressed (<= 2 goals)
- **Justin Sourdif: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (9.78 vs 3.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT13WSHCAR-CARJKOTKANIEMI82-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: WSH offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ assists NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13WSHCAR-CARSAHO20-1|no; why: higher confidence-adjusted growth (3.88 vs 0.17 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT13WSHCAR-CARJKOTKANIEMI82-1|yes: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT13WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.11.
- thesis WSH:OFFENSE_4PLUS (p 0.3335): highest fidelity KXNHLAST-26OCT13WSHCAR-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.3404): highest fidelity KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no (same contract)
- thesis CAR:OFFENSE_4PLUS (p 0.4412): highest fidelity KXNHLGOAL-26OCT13WSHCAR-CARMJANKOWSKI77-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13WSHCAR-CARMJANKOWSKI77-1|yes (same contract)
- KXNHLGOAL-26OCT13WSHCAR-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4475, phi -0.226)
- KXNHLGOAL-26OCT13WSHCAR-CARJKOTKANIEMI82-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:SUPPRESSED (p 0.3404, phi -0.156)
- KXNHLGOAL-26OCT13WSHCAR-WSHJSOURDIF34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4475, phi -0.198)
- KXNHLAST-26OCT13WSHCAR-CARSAHO20-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.4 pts; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4412, phi -0.27)

portfolios: A EV +1.90 (adj +0.54) on $11.54, P(profit) 0.5231, adj growth 5.1 bp · B EV +1.80 (adj +0.82) on $9.00, P(profit) 0.4232, adj growth 7.8 bp · C EV +1.50 (adj +0.55) on $10.99, P(profit) 0.6401, adj growth 5.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ PHI  ·  10000 joint draws  ·  510 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.504 / away 0.496

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_SEA_win | p_overtime | goals | shots PHI/SEA | PHI/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.53 | 0.47 | 0.00 | 5.98 | 26.5/26.5 | 23.2/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.48 | 5.88 | 27.0/26.8 | 23.4/23.7 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.082 | 0.64 | 0.36 | 0.00 | 5.94 | 31.7/21.1 | 18.3/27.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.56 | 0.44 | 0.00 | 9.25 | 28.1/28.2 | 22.5/21.7 | even strength |
| PHI shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.54 | 0.46 | 0.47 | 5.89 | 31.4/21.2 | 18.1/28.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.54 | 0.46 | 0.00 | 3.43 | 25.7/25.5 | 23.7/23.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Winterton: 1+ goals YES | 10 | 0.144 | 0.132 | +0.038 | +0.026 | $2.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Jared McCann: 1+ goals NO | 72 | 0.780 | 0.764 | +0.046 | +0.030 | $6.43 | FUNDED_RESEARCH | $2 | SEA:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 16 | 0.204 | 0.192 | +0.035 | +0.022 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 19 | 0.238 | 0.224 | +0.037 | +0.023 | $2.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (14.89 vs 3.53 bp); despite a smaller raw edge (+0.038 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT13SEAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: SEA offense suppressed (<= 2 goals)
- **Jared McCann: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13SEAPHI-SEABMCMANN74-1|no; why: higher confidence-adjusted growth (9.93 vs 8.06 bp); relationships: KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT13SEAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: SEA offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13SEAPHI-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (7.67 vs 6.97 bp); despite a smaller raw edge (+0.035 vs +0.037/contract); relationships: KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT13SEAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (7.67 vs 6.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, PHI shot control · normal event (5-7) · decided (2+) 0.08.
- thesis SEA:SUPPRESSED (p 0.4512): highest fidelity KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3788): highest fidelity KXNHLAST-26OCT13SEAPHI-PHIOTIPPETT74-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13SEAPHI-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.3242): highest fidelity KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13SEAPHI-SEAKKAKKO84-1|yes (same contract)
- KXNHLGOAL-26OCT13SEAPHI-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4512, phi -0.173)
- KXNHLGOAL-26OCT13SEAPHI-SEAJMCCANN19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.3242, phi -0.208)
- KXNHLGOAL-26OCT13SEAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4015, phi -0.225)
- KXNHLGOAL-26OCT13SEAPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4015, phi -0.214)

portfolios: A EV +1.62 (adj +0.55) on $11.54, P(profit) 0.5119, adj growth 5.2 bp · B EV +1.97 (adj +1.28) on $12.72, P(profit) 0.4163, adj growth 12.3 bp · C EV +1.28 (adj +0.72) on $15.16, P(profit) 0.3807, adj growth 7.0 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.78, adj growth 3.1 bp

## TBL @ NYR  ·  10000 joint draws  ·  488 bet sides mapped, 26 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.409 / away 0.591

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_TBL_win | p_overtime | goals | shots NYR/TBL | NYR/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.53 | 0.47 | 0.00 | 5.98 | 25.7/26.2 | 22.9/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.53 | 0.47 | 0.48 | 5.91 | 25.8/26.3 | 23.0/22.5 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.104 | 0.49 | 0.51 | 0.00 | 5.9 | 20.7/31.4 | 27.7/17.4 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.49 | 0.51 | 0.45 | 5.89 | 20.6/31.7 | 28.2/17.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.068 | 0.53 | 0.47 | 0.00 | 9.29 | 27.2/27.8 | 22.0/21.0 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.061 | 0.43 | 0.57 | 0.00 | 9.13 | 21.8/33.1 | 26.4/16.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Gabe Perreault: 1+ assists YES | 22 | 0.313 | 0.264 | +0.081 | +0.032 | $2.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 76 | 0.842 | 0.799 | +0.070 | +0.026 | $6.43 | FUNDED_RESEARCH | $2 | NYR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jake Guentzel: 1+ goals NO | 65 | 0.700 | 0.686 | +0.034 | +0.020 | $4.33 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Gabe Perreault: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT13TBNYR-TB3|no; why: higher confidence-adjusted growth (12.35 vs 8.43 bp); relationships: KXNHLSPREAD-26OCT13TBNYR-TB3|no: MOSTLY_INDEPENDENT (phi 0.148); KXNHLGOAL-26OCT13TBNYR-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: NYR offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT13TBNYR-TB3|no; why: Broad expression KXNHLSPREAD-26OCT13TBNYR-TB3|no selected over player prop KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.84 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.148); KXNHLGOAL-26OCT13TBNYR-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi 0.136); failure: TBL wins by 2+
- **Jake Guentzel: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no; why: KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no has the higher standalone adjusted growth (10.23 vs 4.11 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.111); relationships: KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26OCT13TBNYR-TB3|no: MOSTLY_INDEPENDENT (phi 0.136); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis NYR:OFFENSE_4PLUS (p 0.3666): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [DIRECT], best adjusted EV KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes — Player prop expression KXNHLGOAL-26OCT13TBNYR-NYRALAFRENIERE13-1|yes selected over player prop KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.46 vs 0.47 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis TBL:SUPPRESSED (p 0.4356): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no — Broad expression KXNHLSPREAD-26OCT13TBNYR-TB3|no selected over player prop KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.84 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYR:WINS (p 0.5135): highest fidelity KXNHLSPREAD-26OCT13TBNYR-TB3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT13TBNYR-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT13TBNYR-NYRGPERREAULT94-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4129, phi -0.285)
- KXNHLSPREAD-26OCT13TBNYR-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2615, phi -0.727)
- KXNHLGOAL-26OCT13TBNYR-TBJGUENTZEL59-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.344, phi -0.241)
- override: Broad expression KXNHLSPREAD-26OCT13TBNYR-TB3|no selected over player prop KXNHLAST-26OCT13TBNYR-TBJCARLSON74-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.84 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26OCT13TBNYR-NYRALAFRENIERE13-1|yes selected over player prop KXNHLAST-26OCT13TBNYR-NYRVGAVRIKOV44-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.46 vs 0.47 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.71 (adj +0.38) on $11.54, P(profit) 0.6384, adj growth 3.6 bp · B EV +1.69 (adj +0.70) on $13.32, P(profit) 0.7077, adj growth 6.7 bp · C EV +2.89 (adj +0.91) on $14.59, P(profit) 0.7142, adj growth 8.8 bp · R EV +0.28 (adj +0.13) on $4.00, P(profit) 0.6124, adj growth 4.9 bp

## STL @ OTT  ·  10000 joint draws  ·  468 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.472 / away 0.528

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_STL_win | p_overtime | goals | shots OTT/STL | OTT/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.51 | 0.49 | 0.00 | 6.01 | 26.8/26.3 | 22.9/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.47 | 5.94 | 26.6/26.2 | 23.0/23.3 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.108 | 0.58 | 0.42 | 0.00 | 6.01 | 31.9/20.7 | 17.6/27.8 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.52 | 0.48 | 0.47 | 5.93 | 32.1/21.0 | 17.9/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.47 | 0.53 | 0.00 | 9.26 | 28.1/27.6 | 21.4/22.1 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.067 | 0.58 | 0.42 | 0.00 | 9.08 | 33.4/22.1 | 17.1/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Michael Amadio: 1+ goals YES | 13 | 0.178 | 0.165 | +0.041 | +0.027 | $2.38 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Stephen Halliday: 1+ goals YES | 11 | 0.148 | 0.138 | +0.031 | +0.021 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Andre Burakovsky: 1+ assists NO | 71 | 0.838 | 0.752 | +0.114 | +0.027 | $6.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Nick Cousins: 1+ goals YES | 9 | 0.118 | 0.110 | +0.023 | +0.014 | $1.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13STLOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (13.36 vs 2.74 bp); despite a smaller raw edge (+0.041 vs +0.120/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT13STLOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT13STLOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: OTT offense suppressed (<= 2 goals)
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13STLOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (8.85 vs 2.74 bp); despite a smaller raw edge (+0.031 vs +0.120/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT13STLOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: OTT offense suppressed (<= 2 goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13STLOTT-OTTABURAKOVSKY95-1|no; why: higher confidence-adjusted growth (8.13 vs 0.45 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT13STLOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT13STLOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: OTT offense succeeds (4+ goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13STLOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (5.05 vs 2.74 bp); despite a smaller raw edge (+0.023 vs +0.120/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT13STLOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.11.
- thesis STL:SUPPRESSED (p 0.3994): highest fidelity KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13STLOTT-STLAJIRICEK36-1|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3723): highest fidelity KXNHLAST-26OCT13STLOTT-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13STLOTT-STLPBROBERG6-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.3877): highest fidelity KXNHLPTS-26OCT13STLOTT-OTTJSPENCE10-1|yes [DIRECT], best adjusted EV KXNHLPTS-26OCT13STLOTT-OTTJSPENCE10-1|yes (same contract)
- KXNHLGOAL-26OCT13STLOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3952, phi -0.198)
- KXNHLGOAL-26OCT13STLOTT-OTTSHALLIDAY34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3952, phi -0.177)
- KXNHLAST-26OCT13STLOTT-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.3 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3877, phi -0.169)
- KXNHLGOAL-26OCT13STLOTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3952, phi -0.157)

portfolios: A EV +2.99 (adj +0.52) on $11.54, P(profit) 0.401, adj growth 4.7 bp · B EV +2.46 (adj +1.20) on $11.75, P(profit) 0.384, adj growth 11.5 bp · C EV +1.89 (adj +0.50) on $15.16, P(profit) 0.4968, adj growth 4.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ NYI  ·  10000 joint draws  ·  418 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.647 / away 0.352

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_VAN_win | p_overtime | goals | shots NYI/VAN | NYI/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NYI shot control · normal event (5-7) · decided (2+) | 0.126 | 0.68 | 0.32 | 0.00 | 6.02 | 32.8/21.2 | 18.5/28.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.63 | 0.37 | 0.00 | 5.99 | 27.4/26.9 | 23.8/23.4 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.55 | 0.45 | 0.49 | 5.92 | 33.2/21.5 | 18.3/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.51 | 0.49 | 0.47 | 5.9 | 27.7/27.2 | 24.0/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.63 | 0.37 | 0.00 | 9.22 | 29.2/28.5 | 23.2/22.4 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.080 | 0.71 | 0.29 | 0.00 | 9.2 | 34.8/22.8 | 18.4/27.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 13 | 0.185 | 0.170 | +0.047 | +0.032 | $2.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 18 | 0.219 | 0.208 | +0.029 | +0.018 | $1.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Kyle Palmieri: 1+ goals NO | 70 | 0.747 | 0.734 | +0.032 | +0.019 | $5.25 | FUNDED_RESEARCH | $2 | NYI:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 12 | 0.150 | 0.141 | +0.023 | +0.014 | $1.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (18.69 vs 4.54 bp); relationships: KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT13VANNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT13VANNYI-NYI3|no; why: higher confidence-adjusted growth (4.54 vs 3.15 bp); despite a smaller raw edge (+0.029 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT13VANNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: VAN offense suppressed (<= 2 goals)
- **Kyle Palmieri: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT13VANNYI-NYI3|no; why: Player prop expression KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no selected over player prop KXNHLAST-26OCT13VANNYI-NYIVEKLUND73-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.87 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT13VANNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: NYI offense succeeds (4+ goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13VANNYI-NYICRITCHIE64-1|yes; why: higher confidence-adjusted growth (3.74 vs 1.70 bp); despite a smaller raw edge (+0.023 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.3174): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:SUPPRESSED (p 0.3313): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no — Player prop expression KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no selected over player prop KXNHLAST-26OCT13VANNYI-NYIVEKLUND73-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.87 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis GAME:TIGHT (p 0.4291): highest fidelity KXNHLSPREAD-26OCT13VANNYI-NYI3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT13VANNYI-NYI3|no (same contract)
- KXNHLGOAL-26OCT13VANNYI-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.465, phi -0.202)
- KXNHLGOAL-26OCT13VANNYI-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.465, phi -0.235)
- KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.4506, phi -0.206)
- KXNHLGOAL-26OCT13VANNYI-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3313, phi -0.149)
- override: Player prop expression KXNHLGOAL-26OCT13VANNYI-NYIKPALMIERI21-1|no selected over player prop KXNHLAST-26OCT13VANNYI-NYIVEKLUND73-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.87 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.29 (adj +0.28) on $11.54, P(profit) 0.6974, adj growth 2.7 bp · B EV +1.66 (adj +1.08) on $10.99, P(profit) 0.3961, adj growth 10.3 bp · C EV +1.04 (adj +0.43) on $11.77, P(profit) 0.7286, adj growth 4.1 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.7465, adj growth 2.0 bp

## PIT @ CHI  ·  10000 joint draws  ·  448 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.415 / away 0.585

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_PIT_win | p_overtime | goals | shots CHI/PIT | CHI/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.43 | 0.57 | 0.00 | 6.02 | 26.9/27.3 | 23.4/23.7 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.113 | 0.38 | 0.62 | 0.00 | 6.02 | 21.2/32.7 | 28.1/18.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.46 | 5.95 | 26.8/27.4 | 24.1/23.5 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.42 | 0.58 | 0.49 | 5.94 | 21.3/32.6 | 29.2/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.46 | 0.54 | 0.00 | 9.34 | 28.2/28.9 | 22.1/22.3 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.075 | 0.32 | 0.68 | 0.00 | 9.27 | 22.7/34.4 | 26.3/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 12 | 0.182 | 0.165 | +0.055 | +0.038 | $3.05 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 53 | 0.735 | 0.595 | +0.188 | +0.048 | $6.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Connor Dewar: 1+ goals YES | 12 | 0.166 | 0.153 | +0.038 | +0.026 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Evgeni Malkin: 1+ assists NO | 55 | 0.640 | 0.593 | +0.073 | +0.025 | $4.74 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes; why: higher confidence-adjusted growth (27.39 vs 2.68 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT13PITCHI-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13PITCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (20.32 vs 4.96 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLAST-26OCT13PITCHI-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: CHI offense succeeds (4+ goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13PITCHI-PITECHINAKHOV59-1|yes; why: higher confidence-adjusted growth (12.82 vs 0.42 bp); despite a smaller raw edge (+0.038 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0063 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLAST-26OCT13PITCHI-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.035); failure: PIT offense suppressed (<= 2 goals)
- **Evgeni Malkin: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13PITCHI-PITEMALKIN71-1|no; why: higher confidence-adjusted growth (5.68 vs 1.31 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.035); failure: PIT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.362): highest fidelity KXNHLAST-26OCT13PITCHI-CHIAFRONDELL16-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4247): highest fidelity KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4347): highest fidelity KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes (same contract)
- KXNHLGOAL-26OCT13PITCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4247, phi -0.214)
- KXNHLAST-26OCT13PITCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 21.5 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.362, phi -0.228)
- KXNHLGOAL-26OCT13PITCHI-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3451, phi -0.191)
- KXNHLAST-26OCT13PITCHI-PITEMALKIN71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4347, phi -0.255)

portfolios: A EV +2.80 (adj +0.61) on $11.54, P(profit) 0.6718, adj growth 5.9 bp · B EV +4.67 (adj +2.08) on $16.08, P(profit) 0.6447, adj growth 20.0 bp · C EV +4.41 (adj +1.96) on $15.16, P(profit) 0.6447, adj growth 18.9 bp · R EV +0.43 (adj +0.30) on $1.00, P(profit) 0.182, adj growth 11.2 bp

## MIN @ WPG  ·  10000 joint draws  ·  474 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_MIN_win | p_overtime | goals | shots WPG/MIN | WPG/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.54 | 0.46 | 0.00 | 5.99 | 28.2/28.1 | 24.7/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.47 | 5.88 | 28.3/28.4 | 25.1/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.55 | 0.45 | 0.00 | 9.28 | 30.0/30.0 | 24.2/23.6 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.070 | 0.56 | 0.44 | 0.00 | 5.98 | 33.1/22.4 | 19.2/29.1 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.070 | 0.45 | 0.55 | 0.00 | 5.96 | 22.7/33.4 | 29.5/19.5 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.45 | 0.55 | 0.47 | 5.83 | 22.4/32.9 | 29.4/19.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Neal Pionk: 1+ goals NO | 87 | 0.932 | 0.914 | +0.054 | +0.036 | $6.43 | FUNDED_RESEARCH | $2 | WPG:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Rieger Lorenz: 1+ goals YES | 10 | 0.135 | 0.125 | +0.029 | +0.019 | $1.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 23 | 0.305 | 0.260 | +0.063 | +0.018 | $1.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Morgan Barron: 1+ goals YES | 11 | 0.138 | 0.130 | +0.021 | +0.013 | $1.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13MINWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (27.65 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0011 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13MINWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: WPG offense succeeds (4+ goals)
- **Rieger Lorenz: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (8.10 vs 3.71 bp); despite a smaller raw edge (+0.029 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13MINWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13MINWPG-MINJSPURGEON46-1|yes; why: higher confidence-adjusted growth (3.71 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT13MINWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: MIN offense suppressed (<= 2 goals)
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13MINWPG-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (3.45 vs 0.48 bp); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:OFFENSE_4PLUS (p 0.3661): highest fidelity KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.4173): highest fidelity KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13MINWPG-MINMBOLDY12-1|no (same contract)
- thesis WPG:SUPPRESSED (p 0.3874): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT13MINWPG-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3878, phi -0.116)
- KXNHLGOAL-26OCT13MINWPG-MINRLORENZ61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4173, phi -0.146)
- KXNHLAST-26OCT13MINWPG-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4173, phi -0.274)
- KXNHLGOAL-26OCT13MINWPG-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3874, phi -0.171)

portfolios: A EV +1.79 (adj +0.70) on $11.54, P(profit) 0.3988, adj growth 6.6 bp · B EV +1.46 (adj +0.79) on $10.78, P(profit) 0.4619, adj growth 7.6 bp · C EV +0.66 (adj +0.26) on $10.46, P(profit) 0.771, adj growth 2.5 bp · R EV +0.12 (adj +0.08) on $2.00, P(profit) 0.9322, adj growth 3.3 bp

## COL @ DAL  ·  10000 joint draws  ·  454 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.517 / away 0.483

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_COL_win | p_overtime | goals | shots DAL/COL | DAL/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.46 | 0.54 | 0.00 | 6.0 | 26.8/27.2 | 23.6/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.48 | 5.9 | 26.9/27.4 | 24.2/23.5 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.101 | 0.40 | 0.60 | 0.00 | 6.01 | 21.2/32.7 | 28.7/18.2 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.44 | 0.56 | 0.48 | 5.88 | 21.5/32.8 | 29.3/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.45 | 0.55 | 0.00 | 9.29 | 28.4/28.9 | 22.6/22.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.067 | 0.41 | 0.59 | 0.00 | 9.18 | 22.7/34.3 | 27.4/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Zachary L'Heureux: 1+ goals YES | 9 | 0.136 | 0.122 | +0.040 | +0.026 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 20 | 0.256 | 0.241 | +0.045 | +0.030 | $2.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 58 | 0.630 | 0.616 | +0.033 | +0.019 | $3.94 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Gabriel Landeskog: 1+ goals YES | 20 | 0.235 | 0.225 | +0.024 | +0.014 | $1.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Zachary L'Heureux: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (16.47 vs 11.33 bp); despite a smaller raw edge (+0.040 vs +0.045/contract); relationships: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13COLDAL-COLGLANDESKOG92-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: COL offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (11.33 vs 2.51 bp); relationships: KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT13COLDAL-COLGLANDESKOG92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: COL offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no; why: Player prop expression KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no because adjusted EV is 0.6 pts higher while thesis capture is 0.81 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT13COLDAL-COLGLANDESKOG92-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: COL offense succeeds (4+ goals)
- **Gabriel Landeskog: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (11.33 vs 2.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4057): highest fidelity KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.3802): highest fidelity KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no — Player prop expression KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no because adjusted EV is 0.6 pts higher while thesis capture is 0.81 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis DAL:SUPPRESSED (p 0.4216): highest fidelity KXNHLAST-26OCT13COLDAL-DALMHEISKANEN4-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13COLDAL-DALMHEISKANEN4-1|no (same contract)
- KXNHLGOAL-26OCT13COLDAL-COLZLHEUREUX68-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3802, phi -0.18)
- KXNHLGOAL-26OCT13COLDAL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3802, phi -0.232)
- KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4057, phi -0.286)
- KXNHLGOAL-26OCT13COLDAL-COLGLANDESKOG92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3802, phi -0.232)
- override: Player prop expression KXNHLGOAL-26OCT13COLDAL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT13COLDAL-COLDTOEWS7-1|no because adjusted EV is 0.6 pts higher while thesis capture is 0.81 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.95 (adj +1.03) on $11.54, P(profit) 0.6354, adj growth 9.9 bp · B EV +1.81 (adj +1.16) on $10.13, P(profit) 0.4479, adj growth 11.1 bp · C EV +0.97 (adj +0.54) on $8.50, P(profit) 0.5449, adj growth 5.2 bp · R EV +0.06 (adj +0.03) on $1.00, P(profit) 0.6302, adj growth 1.2 bp

## VGK @ NSH  ·  10000 joint draws  ·  486 bet sides mapped, 9 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.457 / away 0.543

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_VGK_win | p_overtime | goals | shots NSH/VGK | NSH/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.53 | 0.47 | 0.00 | 6.02 | 27.5/28.0 | 24.5/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.48 | 5.87 | 27.7/28.2 | 24.9/24.5 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.105 | 0.47 | 0.53 | 0.00 | 5.97 | 22.1/33.5 | 29.9/18.9 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.47 | 0.53 | 0.47 | 5.89 | 22.1/33.3 | 29.8/19.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.55 | 0.45 | 0.00 | 9.37 | 29.2/29.5 | 23.8/22.6 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.060 | 0.48 | 0.52 | 0.00 | 9.18 | 23.8/35.0 | 28.2/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 71 | 0.762 | 0.748 | +0.037 | +0.023 | $5.70 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Brady Skjei: 1+ assists YES | 23 | 0.308 | 0.264 | +0.066 | +0.022 | $2.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Jack Eichel: 1+ goals NO | 68 | 0.726 | 0.713 | +0.030 | +0.018 | $3.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13VGKNSH-VGKTCONNELLY24-1|no; why: higher confidence-adjusted growth (5.85 vs 5.05 bp); despite a smaller raw edge (+0.037 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: VGK offense succeeds (4+ goals)
- **Brady Skjei: 1+ assists YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT13VGKNSH-VGK3|no; why: higher confidence-adjusted growth (5.52 vs 0.81 bp); alternative not eligible: confidence-adjusted EV +0.0076 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: NSH offense suppressed (<= 2 goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no; why: Player prop expression KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.86 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.4121): highest fidelity KXNHLAST-26OCT13VGKNSH-VGKTCONNELLY24-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no — Player prop expression KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.86 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NSH:OFFENSE_4PLUS (p 0.3848): highest fidelity KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.3696): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT13VGKNSH-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3696, phi -0.231)
- KXNHLAST-26OCT13VGKNSH-NSHBSKJEI76-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3975, phi -0.259)
- KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3696, phi -0.24)
- override: Player prop expression KXNHLGOAL-26OCT13VGKNSH-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT13VGKNSH-VGKMMARNER93-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.86 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.02 (adj +0.51) on $11.54, P(profit) 0.5595, adj growth 4.8 bp · B EV +1.03 (adj +0.47) on $11.72, P(profit) 0.6688, adj growth 4.5 bp · C EV +0.84 (adj +0.37) on $8.02, P(profit) 0.8364, adj growth 3.5 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7616, adj growth 2.4 bp

## TOR @ UTA  ·  10000 joint draws  ·  478 bet sides mapped, 9 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.590 / away 0.410

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_TOR_win | p_overtime | goals | shots UTA/TOR | UTA/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| UTA shot control · normal event (5-7) · decided (2+) | 0.140 | 0.68 | 0.32 | 0.00 | 6.02 | 34.5/21.9 | 19.3/29.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.57 | 0.43 | 0.49 | 5.95 | 34.7/22.1 | 18.9/31.1 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.106 | 0.71 | 0.29 | 0.00 | 9.33 | 36.2/23.3 | 18.7/27.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.63 | 0.37 | 0.00 | 6.03 | 28.6/27.7 | 24.6/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.54 | 0.46 | 0.47 | 5.97 | 28.7/27.8 | 24.6/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.61 | 0.39 | 0.00 | 9.32 | 30.3/29.3 | 23.8/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Easton Cowan: 1+ assists YES | 24 | 0.310 | 0.270 | +0.057 | +0.017 | $1.78 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
| Dylan Guenther: 1+ goals NO | 62 | 0.669 | 0.655 | +0.032 | +0.019 | $4.23 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ goals NO | 64 | 0.683 | 0.671 | +0.027 | +0.015 | $3.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Easton Cowan: 1+ assists YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13TORUTA-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (3.44 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT13TORUTA-TORAMATTHEWS34-1|no: INTENTIONAL_DIVERSIFIER (phi -0.081); failure: TOR offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT13TORUTA-UTANSCHMALTZ8-1|no; why: Player prop expression KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no selected over player prop KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.83 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT13TORUTA-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: UTA offense succeeds (4+ goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-1|no; why: Player prop expression KXNHLGOAL-26OCT13TORUTA-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-2|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.84 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.081); KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: TOR offense succeeds (4+ goals)

**Review**: scripts UTA shot control · normal event (5-7) · decided (2+) 0.14, UTA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · high event (8+) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3266): highest fidelity KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3113): highest fidelity KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no (same contract)
- thesis TOR:SUPPRESSED (p 0.4531): highest fidelity KXNHLAST-26OCT13TORUTA-TORKMARCHENKO86-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-1|no — Player prop expression KXNHLGOAL-26OCT13TORUTA-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-2|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.84 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLAST-26OCT13TORUTA-TORECOWAN53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4531, phi -0.283)
- KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4845, phi -0.243)
- KXNHLGOAL-26OCT13TORUTA-TORAMATTHEWS34-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3266, phi -0.293)
- override: Player prop expression KXNHLGOAL-26OCT13TORUTA-TORAMATTHEWS34-1|no selected over player prop KXNHLAST-26OCT13TORUTA-TORDRADDYSH43-2|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.84 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT13TORUTA-UTADGUENTHER11-1|no selected over player prop KXNHLAST-26OCT13TORUTA-UTAVTROCHECK16-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.83 vs 0.90 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.56 (adj +0.42) on $11.54, P(profit) 0.5885, adj growth 4.0 bp · B EV +0.77 (adj +0.33) on $9.84, P(profit) 0.5976, adj growth 3.2 bp · C EV +0.73 (adj +0.31) on $9.29, P(profit) 0.5976, adj growth 3.0 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.6686, adj growth 2.2 bp

## CGY @ ANA  ·  10000 joint draws  ·  480 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.609 / away 0.391

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_CGY_win | p_overtime | goals | shots ANA/CGY | ANA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.132 | 0.72 | 0.28 | 0.00 | 6.0 | 34.5/22.4 | 19.9/29.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.69 | 0.31 | 0.00 | 6.0 | 29.6/28.8 | 26.2/25.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.55 | 0.45 | 0.44 | 5.96 | 35.1/22.8 | 19.7/31.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.52 | 0.48 | 0.49 | 5.96 | 29.2/28.5 | 25.1/25.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.092 | 0.75 | 0.25 | 0.00 | 9.3 | 36.4/23.8 | 19.6/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.69 | 0.31 | 0.00 | 9.37 | 30.9/30.0 | 24.8/23.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 2+ goals YES | 2 | 0.044 | 0.038 | +0.023 | +0.017 | $1.11 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.08) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 9 | 0.140 | 0.126 | +0.044 | +0.030 | $2.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 11 | 0.149 | 0.137 | +0.032 | +0.020 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Nikita Nesterenko: 1+ assists NO | 74 | 0.807 | 0.769 | +0.054 | +0.015 | $6.32 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | ANA:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **A.J. Greer: 2+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (27.05 vs 7.49 bp); despite a smaller raw edge (+0.023 vs +0.092/contract); relationships: KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT13CGYANA-ANANNESTERENKO13-1|no: MOSTLY_INDEPENDENT (phi -0.048); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (22.23 vs 7.49 bp); despite a smaller raw edge (+0.044 vs +0.092/contract); relationships: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT13CGYANA-ANANNESTERENKO13-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: ANA offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (8.25 vs 7.49 bp); despite a smaller raw edge (+0.032 vs +0.092/contract); relationships: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT13CGYANA-ANANNESTERENKO13-1|no: MOSTLY_INDEPENDENT (phi -0.034); failure: ANA offense suppressed (<= 2 goals)
- **Nikita Nesterenko: 1+ assists NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT13CGYANA-ANANNESTERENKO13-1|no; why: higher confidence-adjusted growth (2.73 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-2|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.034); failure: ANA offense succeeds (4+ goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.497): highest fidelity KXNHLAST-26OCT13CGYANA-ANAAKILLORN17-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:SUPPRESSED (p 0.2944): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT13CGYANA-ANAAGREER18-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 92% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2944, phi -0.13)
- KXNHLGOAL-26OCT13CGYANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2944, phi -0.147)
- KXNHLGOAL-26OCT13CGYANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2944, phi -0.137)
- KXNHLAST-26OCT13CGYANA-ANANNESTERENKO13-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.497, phi -0.181)

portfolios: A EV +4.22 (adj +0.75) on $11.54, P(profit) 0.6366, adj growth 6.8 bp · B EV +3.21 (adj +2.05) on $11.55, P(profit) 0.3029, adj growth 19.4 bp · C EV +0.84 (adj +0.21) on $1.65, P(profit) 0.2721, adj growth 2.0 bp · R EV +1.07 (adj +0.79) on $1.00, P(profit) 0.0442, adj growth 24.7 bp

## EDM @ LAK  ·  10000 joint draws  ·  472 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.462 / away 0.538

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_EDM_win | p_overtime | goals | shots LAK/EDM | LAK/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.47 | 0.53 | 0.00 | 6.01 | 27.8/27.9 | 24.2/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.51 | 0.49 | 0.48 | 5.91 | 28.1/28.1 | 24.7/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.45 | 0.55 | 0.00 | 9.36 | 29.4/29.4 | 22.9/23.7 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.077 | 0.43 | 0.57 | 0.00 | 6.02 | 22.2/33.1 | 29.0/19.2 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.46 | 0.54 | 0.48 | 5.96 | 22.3/33.1 | 29.6/19.1 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.059 | 0.54 | 0.46 | 0.00 | 6.03 | 32.6/22.2 | 19.1/28.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Artemi Panarin: 2+ assists NO | 82 | 0.910 | 0.862 | +0.080 | +0.032 | $6.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Andre Lee: 1+ goals YES | 8 | 0.111 | 0.102 | +0.025 | +0.017 | $1.34 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ assists YES | 32 | 0.401 | 0.355 | +0.065 | +0.020 | $2.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
| Alex Laferriere: 1+ goals YES | 25 | 0.286 | 0.276 | +0.023 | +0.013 | $1.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Artemi Panarin: 2+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (16.26 vs 5.80 bp); despite a smaller raw edge (+0.080 vs +0.115/contract); relationships: KXNHLGOAL-26OCT13EDMLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT13EDMLA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT13EDMLA-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.059); failure: LAK offense succeeds (4+ goals)
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13EDMLA-LATMOORE12-1|yes; why: higher confidence-adjusted growth (7.60 vs 6.14 bp); despite a smaller raw edge (+0.026 vs +0.103/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT13EDMLA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT13EDMLA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: LAK offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes; why: Player prop expression KXNHLAST-26OCT13EDMLA-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.57 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT13EDMLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT13EDMLA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: EDM offense suppressed (<= 2 goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13EDMLA-LATMOORE12-1|yes; why: Player prop expression KXNHLGOAL-26OCT13EDMLA-LAALAFERRIERE14-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-LATMOORE12-1|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.43 vs 0.49 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: INTENTIONAL_DIVERSIFIER (phi -0.059); KXNHLGOAL-26OCT13EDMLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT13EDMLA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:SUPPRESSED (p 0.4138): highest fidelity KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.395): highest fidelity KXNHLAST-26OCT13EDMLA-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes — Player prop expression KXNHLAST-26OCT13EDMLA-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.57 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis LAK:OFFENSE_4PLUS (p 0.3679): highest fidelity KXNHLAST-26OCT13EDMLA-LATMOORE12-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT13EDMLA-LATMOORE12-1|yes (same contract)
- KXNHLAST-26OCT13EDMLA-LAAPANARIN10-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3679, phi -0.251)
- KXNHLGOAL-26OCT13EDMLA-LAALEE47-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4138, phi -0.157)
- KXNHLAST-26OCT13EDMLA-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 43% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3893, phi -0.293)
- KXNHLGOAL-26OCT13EDMLA-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4138, phi -0.251)
- override: Player prop expression KXNHLAST-26OCT13EDMLA-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-EDMKKAPANEN42-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.57 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26OCT13EDMLA-LAALAFERRIERE14-1|yes selected over player prop KXNHLAST-26OCT13EDMLA-LATMOORE12-1|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.43 vs 0.49 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.19 (adj +0.47) on $11.54, P(profit) 0.7121, adj growth 4.4 bp · B EV +1.58 (adj +0.71) on $11.43, P(profit) 0.5791, adj growth 6.9 bp · C EV +2.97 (adj +0.78) on $13.11, P(profit) 0.7757, adj growth 7.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ SJS  ·  10000 joint draws  ·  536 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.467 / away 0.533

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_BOS_win | p_overtime | goals | shots SJS/BOS | SJS/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.51 | 0.49 | 0.00 | 6.04 | 27.2/27.2 | 23.6/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.49 | 0.51 | 0.47 | 5.98 | 27.3/27.2 | 23.9/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.47 | 0.53 | 0.00 | 9.37 | 28.6/28.6 | 22.3/22.8 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.081 | 0.54 | 0.46 | 0.00 | 6.03 | 32.1/21.6 | 18.4/28.3 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.55 | 0.45 | 0.45 | 5.94 | 32.3/21.7 | 18.6/29.0 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.059 | 0.44 | 0.56 | 0.00 | 6.04 | 21.7/31.9 | 27.8/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kiefer Sherwood: 1+ goals YES | 16 | 0.215 | 0.200 | +0.046 | +0.031 | $2.78 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Casey Mittelstadt: 1+ goals YES | 14 | 0.185 | 0.172 | +0.036 | +0.024 | $2.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Matthew Poitras: 1+ goals YES | 9 | 0.124 | 0.115 | +0.029 | +0.019 | $1.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Marat Khusnutdinov: 1+ goals YES | 11 | 0.148 | 0.137 | +0.031 | +0.020 | $1.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT13BOSSJ-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (14.59 vs 5.38 bp); despite a smaller raw edge (+0.046 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT13BOSSJ-BOSMPOITRAS51-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: SJS offense suppressed (<= 2 goals)
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT13BOSSJ-BOSNZADOROV91-1|yes; why: higher confidence-adjusted growth (9.81 vs 0.00 bp); despite a smaller raw edge (+0.036 vs +0.042/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT13BOSSJ-BOSMPOITRAS51-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: BOS offense suppressed (<= 2 goals)
- **Matthew Poitras: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes has the higher standalone adjusted growth (9.81 vs 8.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.018); they share one thesis budget; relationships: KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: BOS offense suppressed (<= 2 goals)
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes has the higher standalone adjusted growth (9.81 vs 8.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT13BOSSJ-BOSMPOITRAS51-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4005): highest fidelity KXNHLAST-26OCT13BOSSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.401): highest fidelity KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.385): highest fidelity KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT13BOSSJ-BOSJPETERKA10-1|no (same contract)
- KXNHLGOAL-26OCT13BOSSJ-SJKSHERWOOD44-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3796, phi -0.207)
- KXNHLGOAL-26OCT13BOSSJ-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.385, phi -0.189)
- KXNHLGOAL-26OCT13BOSSJ-BOSMPOITRAS51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.385, phi -0.172)
- KXNHLGOAL-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.385, phi -0.171)

portfolios: A EV +2.59 (adj +0.38) on $11.54, P(profit) 0.6023, adj growth 3.6 bp · B EV +2.16 (adj +1.43) on $8.00, P(profit) 0.5202, adj growth 13.6 bp · C EV +2.14 (adj +1.04) on $15.16, P(profit) 0.3456, adj growth 10.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
