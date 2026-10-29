# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-29T16:54:50Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +28.85 | +8.67 | +27.82 | 0.761 | -20.19 | -33.54 | 78.75 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +21.58 | +12.09 | +19.74 | 0.723 | -22.03 | -33.07 | 114.48 |
| C best expression per thesis | 148.53 | +23.45 | +12.07 | +20.60 | 0.681 | -31.32 | -43.47 | 110.98 |
| R FUNDED research stakes | 23.00 | +2.23 | +1.16 | +1.68 | 0.599 | -6.55 | -7.97 | 0.00 |

## WPG @ TBL  ·  10000 joint draws  ·  418 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.675 / away 0.325

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WPG_win | p_overtime | goals | shots TBL/WPG | TBL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.123 | 0.75 | 0.25 | 0.00 | 5.98 | 32.4/21.0 | 18.6/27.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.69 | 0.31 | 0.00 | 5.99 | 27.3/26.8 | 24.0/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.53 | 0.47 | 0.47 | 5.91 | 27.0/26.6 | 23.4/23.7 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.59 | 0.41 | 0.46 | 5.82 | 32.6/21.4 | 18.4/29.1 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.067 | 0.79 | 0.21 | 0.00 | 9.13 | 33.9/22.3 | 18.2/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.066 | 0.71 | 0.29 | 0.00 | 9.18 | 28.6/28.0 | 23.2/21.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charle-Edouard D'Astous: 1+ goals NO | 89 | 0.929 | 0.916 | +0.032 | +0.020 | $8.54 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 25 | 0.290 | 0.279 | +0.027 | +0.016 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 11 | 0.139 | 0.128 | +0.022 | +0.011 | $1.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Tampa Bay over 1.5 goals scored NO | 11 | 0.150 | 0.127 | +0.033 | +0.011 | $1.01 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | FRAGILE (0.45) | EVIDENCE_MIXED | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT29WPGTB-TB2|no; why: higher confidence-adjusted growth (9.27 vs 2.34 bp); despite a smaller raw edge (+0.032 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.001 vs 0.58); relationships: KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLTEAMTOTAL-26OCT29WPGTB-TB2|no: MOSTLY_INDEPENDENT (phi 0.09); failure: TBL offense succeeds (4+ goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (2.77 vs 0.81 bp); alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLTEAMTOTAL-26OCT29WPGTB-TB2|no: INTENTIONAL_DIVERSIFIER (phi 0.008); failure: WPG offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes has the higher standalone adjusted growth (2.77 vs 2.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLTEAMTOTAL-26OCT29WPGTB-TB2|no: INTENTIONAL_DIVERSIFIER (phi -0.003); failure: WPG offense suppressed (<= 2 goals)
- **Tampa Bay over 1.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (2.34 vs 0.15 bp); despite a smaller raw edge (+0.033 vs +0.071/contract); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.09); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: INTENTIONAL_DIVERSIFIER (phi 0.008); KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.003); failure: TBL wins (incl. OT/SO)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.2594): highest fidelity KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.3355): highest fidelity KXNHLTEAMTOTAL-26OCT29WPGTB-TB2|no [FRAGILE], best adjusted EV KXNHLTEAMTOTAL-26OCT29WPGTB-TB2|no (same contract)
- KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4503, phi -0.108)
- KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.535, phi -0.296)
- KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.535, phi -0.191)
- KXNHLTEAMTOTAL-26OCT29WPGTB-TB2|no: FUNDED_RESEARCH; family MIXED; loses 55% of the draws where the thesis happens; opposing: failure thesis TBL:WINS (p 0.6316, phi -0.484)

portfolios: A EV +1.77 (adj +0.79) on $14.52, P(profit) 0.4612, adj growth 7.1 bp · B EV +1.05 (adj +0.53) on $13.00, P(profit) 0.4526, adj growth 5.1 bp · C EV +0.79 (adj +0.34) on $4.85, P(profit) 0.3952, adj growth 3.1 bp · R EV +0.39 (adj +0.16) on $4.00, P(profit) 0.1498, adj growth 5.4 bp

## UTA @ PIT  ·  10000 joint draws  ·  400 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.459 / away 0.541

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_UTA_win | p_overtime | goals | shots PIT/UTA | PIT/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.51 | 0.49 | 0.00 | 6.06 | 27.2/27.3 | 23.9/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.45 | 6.01 | 27.4/27.5 | 24.2/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.49 | 0.51 | 0.00 | 9.51 | 28.8/29.0 | 22.4/22.6 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.071 | 0.57 | 0.43 | 0.00 | 6.04 | 32.1/21.7 | 18.6/28.2 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.070 | 0.44 | 0.56 | 0.00 | 6.05 | 21.6/32.0 | 27.9/18.5 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.53 | 0.47 | 0.47 | 5.92 | 32.0/21.7 | 18.6/28.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nick Robertson: 1+ goals YES | 17 | 0.251 | 0.228 | +0.071 | +0.048 | $4.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Declan Carlile: 1+ goals YES | 6 | 0.097 | 0.086 | +0.033 | +0.022 | $1.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ goals YES | 32 | 0.381 | 0.365 | +0.046 | +0.029 | $3.71 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 32 | 0.435 | 0.357 | +0.100 | +0.022 | $2.72 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.60) | EVIDENCE_STRONGER | D |
- **Nick Robertson: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (33.77 vs 17.70 bp); relationships: KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: PIT offense suppressed (<= 2 goals)
- **Declan Carlile: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes has the higher standalone adjusted growth (33.77 vs 17.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes; why: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.53 vs 0.27 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.03); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes; why: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.60 vs 0.24 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.03); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4347): highest fidelity KXNHLAST-26OCT29UTAPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes — Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.53 vs 0.27 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis UTA:SUPPRESSED (p 0.3547): highest fidelity KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no (same contract)
- KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.217)
- KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.132)
- KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.267)
- KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 40% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.0 pts; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.284)
- override: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.53 vs 0.27 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.60 vs 0.24 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +6.69 (adj +2.17) on $16.22, P(profit) 0.5189, adj growth 19.9 bp · B EV +4.06 (adj +2.36) on $12.82, P(profit) 0.4336, adj growth 22.5 bp · C EV +3.89 (adj +2.60) on $18.42, P(profit) 0.2509, adj growth 23.7 bp · R EV +0.14 (adj +0.09) on $1.00, P(profit) 0.3812, adj growth 3.3 bp

## CBJ @ CAR  ·  10000 joint draws  ·  430 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.691 / away 0.309

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CBJ_win | p_overtime | goals | shots CAR/CBJ | CAR/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.145 | 0.67 | 0.33 | 0.00 | 6.0 | 33.6/20.9 | 18.2/29.2 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.128 | 0.53 | 0.47 | 0.47 | 5.9 | 33.6/21.3 | 18.0/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.097 | 0.57 | 0.43 | 0.00 | 5.97 | 27.5/26.8 | 23.5/23.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.089 | 0.65 | 0.35 | 0.00 | 9.27 | 35.4/22.7 | 17.8/27.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.50 | 0.50 | 0.45 | 5.94 | 27.8/26.9 | 23.7/24.3 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.075 | 0.52 | 0.48 | 0.46 | 2.78 | 32.5/20.0 | 18.5/30.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie Coyle: 1+ goals YES | 17 | 0.254 | 0.232 | +0.074 | +0.052 | $5.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.186 | 0.170 | +0.048 | +0.033 | $3.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 73 | 0.778 | 0.764 | +0.035 | +0.020 | $7.18 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 67 | 0.722 | 0.705 | +0.036 | +0.020 | $5.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (39.10 vs 19.03 bp); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (39.10 vs 19.03 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.022); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: CBJ offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes; why: KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes has the higher standalone adjusted growth (6.61 vs 4.62 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.131); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: CAR offense succeeds (4+ goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes; why: Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no selected over broad KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR4|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.85 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.3293): highest fidelity KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.2133): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.3571): highest fidelity KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29CBJCAR-CAR2|no — Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no selected over broad KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR4|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.85 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4607, phi -0.264)
- KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4607, phi -0.233)
- KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4247, phi -0.215)
- KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4247, phi -0.214)
- override: Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no selected over broad KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR4|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.85 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.56 (adj +0.78) on $16.22, P(profit) 0.5328, adj growth 6.9 bp · B EV +3.83 (adj +2.58) on $21.05, P(profit) 0.3889, adj growth 24.4 bp · C EV +5.84 (adj +3.81) on $16.12, P(profit) 0.3889, adj growth 34.6 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.7784, adj growth 2.1 bp

## CHI @ DET  ·  10000 joint draws  ·  434 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_CHI_win | p_overtime | goals | shots DET/CHI | DET/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.139 | 0.70 | 0.30 | 0.00 | 5.99 | 33.2/21.0 | 18.6/28.5 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.126 | 0.55 | 0.45 | 0.50 | 5.93 | 33.4/21.4 | 18.2/30.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.64 | 0.36 | 0.00 | 5.99 | 27.3/26.6 | 23.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.53 | 0.47 | 0.46 | 5.88 | 27.7/26.8 | 23.7/24.5 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.083 | 0.73 | 0.27 | 0.00 | 9.21 | 34.8/22.5 | 18.2/26.8 | even strength |
| DET shot control · low event (<=4) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 3.44 | 31.5/19.9 | 18.6/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dylan Larkin: 2+ goals NO | 93 | 0.953 | 0.946 | +0.018 | +0.011 | $8.54 | FUNDED_RESEARCH | $3 | DET:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Roman Kantserov: 1+ goals NO | 77 | 0.806 | 0.794 | +0.023 | +0.012 | $4.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 23 | 0.265 | 0.254 | +0.023 | +0.011 | $1.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ assists NO | 58 | 0.655 | 0.607 | +0.058 | +0.010 | $2.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Dylan Larkin: 2+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29CHIDET-DETLRAYMOND23-1|no; why: higher confidence-adjusted growth (4.78 vs 0.09 bp); alternative not eligible: confidence-adjusted EV +0.0029 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: DET offense succeeds (4+ goals)
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no; why: Player prop expression KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.89 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT29CHIDET-DETDLARKIN71-2|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: REINFORCING (phi 0.246); failure: CHI offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CHIDET-CHIRDONATO8-1|yes; why: higher confidence-adjusted growth (1.57 vs 0.03 bp); alternative not eligible: confidence-adjusted EV +0.0012 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29CHIDET-DETDLARKIN71-2|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.185); failure: CHI offense suppressed (<= 2 goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no; why: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no has the higher standalone adjusted growth (2.57 vs 0.96 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.119); relationships: KXNHLGOAL-26OCT29CHIDET-DETDLARKIN71-2|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no: REINFORCING (phi 0.246); KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.185); failure: CHI offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.14, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:SUPPRESSED (p 0.4966): highest fidelity KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no — Player prop expression KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.89 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis CHI:OFFENSE_4PLUS (p 0.2834): highest fidelity KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.3444): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29CHIDET-DETDLARKIN71-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.4373, phi -0.168)
- KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2834, phi -0.195)
- KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4966, phi -0.276)
- KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2834, phi -0.265)
- override: Player prop expression KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.89 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.64 (adj +0.38) on $16.22, P(profit) 0.5496, adj growth 3.5 bp · B EV +0.75 (adj +0.31) on $18.11, P(profit) 0.6599, adj growth 3.0 bp · C EV +1.76 (adj +0.37) on $11.11, P(profit) 0.8115, adj growth 3.4 bp · R EV +0.06 (adj +0.04) on $3.00, P(profit) 0.953, adj growth 1.4 bp

## BOS @ STL  ·  10000 joint draws  ·  436 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.506 / away 0.494

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_BOS_win | p_overtime | goals | shots STL/BOS | STL/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.53 | 0.47 | 0.00 | 6.05 | 27.4/27.2 | 23.8/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.47 | 5.97 | 27.2/27.1 | 23.8/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.54 | 0.46 | 0.00 | 9.31 | 28.9/28.6 | 22.9/22.6 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.088 | 0.62 | 0.38 | 0.00 | 5.98 | 32.3/21.6 | 18.7/27.9 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.51 | 0.49 | 0.45 | 5.9 | 32.7/21.7 | 18.5/29.4 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.064 | 0.64 | 0.36 | 0.00 | 9.2 | 33.9/22.9 | 18.1/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Casey Mittelstadt: 1+ goals YES | 14 | 0.177 | 0.165 | +0.029 | +0.017 | $2.11 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 24 | 0.283 | 0.271 | +0.031 | +0.019 | $2.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Charlie McAvoy: 1+ assists NO | 55 | 0.631 | 0.585 | +0.064 | +0.018 | $4.88 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Jimmy Snuggerud: 1+ goals YES | 29 | 0.330 | 0.318 | +0.025 | +0.014 | $2.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT29BOSSTL-3|yes; why: higher confidence-adjusted growth (4.80 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.93 vs 0.773); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: BOS offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (3.99 vs 2.01 bp); relationships: KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: STL offense suppressed (<= 2 goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29BOSSTL-BOSDPASTRNAK88-1|no; why: higher confidence-adjusted growth (2.92 vs 0.21 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: BOS offense succeeds (4+ goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (3.99 vs 2.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.4174): highest fidelity KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.4059): highest fidelity KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.3722): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4059, phi -0.185)
- KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.369, phi -0.258)
- KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3722, phi -0.279)
- KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.369, phi -0.27)

portfolios: A EV +1.89 (adj +0.89) on $15.46, P(profit) 0.4833, adj growth 8.3 bp · B EV +1.43 (adj +0.68) on $11.61, P(profit) 0.4833, adj growth 6.4 bp · C EV +1.21 (adj +0.49) on $10.47, P(profit) 0.7326, adj growth 4.5 bp · R EV +0.19 (adj +0.11) on $1.00, P(profit) 0.1769, adj growth 4.0 bp

## WSH @ NSH  ·  10000 joint draws  ·  432 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.496 / away 0.504

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_WSH_win | p_overtime | goals | shots NSH/WSH | NSH/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.58 | 0.42 | 0.00 | 6.07 | 27.9/28.0 | 24.6/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.49 | 5.93 | 28.0/28.2 | 25.0/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.58 | 0.42 | 0.00 | 9.38 | 29.6/29.7 | 23.8/22.9 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.071 | 0.52 | 0.48 | 0.00 | 5.99 | 22.2/32.8 | 29.5/18.5 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.065 | 0.64 | 0.36 | 0.00 | 6.02 | 33.0/22.4 | 19.6/28.6 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.49 | 0.51 | 0.49 | 5.94 | 22.6/33.0 | 29.7/19.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 18 | 0.223 | 0.210 | +0.033 | +0.020 | $2.48 | FUNDED_RESEARCH | $1 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 29 | 0.331 | 0.319 | +0.027 | +0.014 | $2.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (5.47 vs 0.14 bp); alternative not eligible: confidence-adjusted EV +0.0032 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: WSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29WSHNSH-WSH3|no; why: higher confidence-adjusted growth (2.06 vs 0.73 bp); despite a smaller raw edge (+0.027 vs +0.030/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.3679): highest fidelity KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.4437): highest fidelity KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes (same contract)
- KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4126, phi -0.235)
- KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3418, phi -0.264)

portfolios: A EV +0.85 (adj +0.49) on $6.46, P(profit) 0.4816, adj growth 4.5 bp · B EV +0.62 (adj +0.36) on $4.61, P(profit) 0.4816, adj growth 3.4 bp · C EV +0.91 (adj +0.52) on $6.80, P(profit) 0.4816, adj growth 4.8 bp · R EV +0.17 (adj +0.10) on $1.00, P(profit) 0.2234, adj growth 3.8 bp

## MTL @ DAL  ·  10000 joint draws  ·  420 bet sides mapped, 0 +EV candidates, 0 on card

sportsbook moneyline consensus (5 books): home 0.602 / away 0.399

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_MTL_win | p_overtime | goals | shots DAL/MTL | DAL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DAL shot control · normal event (5-7) · decided (2+) | 0.122 | 0.64 | 0.36 | 0.00 | 5.96 | 31.4/20.3 | 17.5/27.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.55 | 0.45 | 0.00 | 6.0 | 26.4/25.9 | 22.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.46 | 5.9 | 26.7/26.0 | 22.7/23.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.53 | 0.47 | 0.46 | 5.89 | 31.6/20.8 | 17.7/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.58 | 0.42 | 0.00 | 9.28 | 28.1/27.5 | 21.8/21.6 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.068 | 0.66 | 0.34 | 0.00 | 9.21 | 32.9/21.7 | 17.0/25.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts DAL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ MIN  ·  10000 joint draws  ·  400 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.631 / away 0.369

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_NYI_win | p_overtime | goals | shots MIN/NYI | MIN/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.59 | 0.41 | 0.00 | 6.01 | 28.2/28.0 | 24.7/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.54 | 0.46 | 0.48 | 5.9 | 28.0/28.0 | 24.8/24.7 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.088 | 0.64 | 0.36 | 0.00 | 5.94 | 33.4/22.5 | 19.6/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.62 | 0.38 | 0.00 | 9.2 | 29.9/29.7 | 24.3/23.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.54 | 0.46 | 0.45 | 5.88 | 33.5/22.5 | 19.2/30.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.58 | 0.42 | 0.00 | 3.46 | 27.3/27.2 | 25.6/25.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden Schenn: 1+ goals YES | 18 | 0.244 | 0.222 | +0.053 | +0.031 | $3.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 53 | 0.606 | 0.586 | +0.058 | +0.038 | $8.54 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 11 | 0.155 | 0.141 | +0.038 | +0.024 | $2.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Olli Maatta: 1+ goals YES | 4 | 0.064 | 0.055 | +0.021 | +0.013 | $1.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes; why: higher confidence-adjusted growth (13.68 vs 3.15 bp); despite a smaller raw edge (+0.053 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT29NYIMIN-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NYI offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no; why: higher confidence-adjusted growth (12.88 vs 2.21 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.989 vs 0.883); relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT29NYIMIN-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: MIN offense succeeds (4+ goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (13.68 vs 12.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: NYI offense suppressed (<= 2 goals)
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT29NYIMIN-2|yes; why: higher confidence-adjusted growth (8.11 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT29NYIMIN-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:OFFENSE_4PLUS (p 0.3232): highest fidelity KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3629): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4447): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29NYIMIN-MIN2|no (same contract)
- KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4527, phi -0.244)
- KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4187, phi -0.294)
- KXNHLGOAL-26OCT29NYIMIN-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4527, phi -0.21)
- KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3629, phi -0.1)

portfolios: A EV +2.31 (adj +1.14) on $16.22, P(profit) 0.4732, adj growth 10.6 bp · B EV +3.38 (adj +2.09) on $16.06, P(profit) 0.4002, adj growth 19.7 bp · C EV +2.89 (adj +1.78) on $18.12, P(profit) 0.7006, adj growth 16.4 bp · R EV +0.32 (adj +0.21) on $3.00, P(profit) 0.6058, adj growth 7.8 bp

## BUF @ ANA  ·  10000 joint draws  ·  444 bet sides mapped, 23 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.439 / away 0.561

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BUF_win | p_overtime | goals | shots ANA/BUF | ANA/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.60 | 0.40 | 0.00 | 6.03 | 28.1/28.0 | 24.7/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.45 | 6.02 | 27.9/27.9 | 24.5/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.58 | 0.42 | 0.00 | 9.51 | 30.1/29.9 | 23.9/23.5 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.089 | 0.65 | 0.35 | 0.00 | 6.02 | 33.2/22.2 | 19.4/28.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.56 | 0.44 | 0.47 | 5.95 | 33.3/22.5 | 19.4/29.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.061 | 0.63 | 0.37 | 0.00 | 9.45 | 34.7/23.8 | 18.5/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Washe: 1+ goals YES | 11 | 0.163 | 0.147 | +0.046 | +0.030 | $2.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 2.5 goals NO | 76 | 0.853 | 0.804 | +0.080 | +0.031 | $8.50 | FUNDED_RESEARCH | $3 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 1.5 goals YES | 25 | 0.345 | 0.295 | +0.082 | +0.032 | $2.30 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ goals NO | 63 | 0.695 | 0.678 | +0.049 | +0.031 | $7.57 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: higher confidence-adjusted growth (19.27 vs 12.22 bp); despite a smaller raw edge (+0.046 vs +0.080/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT29BUFANA-BUF3|no: MOSTLY_INDEPENDENT (phi 0.088); KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: MOSTLY_INDEPENDENT (phi 0.115); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: ANA offense suppressed (<= 2 goals)
- **Buffalo wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: higher confidence-adjusted growth (12.22 vs 11.25 bp); despite a smaller raw edge (+0.080 vs +0.082/contract); wins across more scripts (relative breadth 1.034 vs 0.516); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.088); KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: DUPLICATIVE (phi 0.301); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.157); failure: BUF wins by 2+
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-BUF3|no has the higher standalone adjusted growth (12.22 vs 11.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.301); they share one thesis budget; relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.115); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: DUPLICATIVE (phi 0.301); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.17); failure: BUF wins (incl. OT/SO)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-BUF3|no has the higher standalone adjusted growth (12.22 vs 9.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.157); they share one thesis budget; relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: REINFORCING (phi 0.157); KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: REINFORCING (phi 0.17); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4751): highest fidelity KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5562): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3447): highest fidelity KXNHLSPREAD-26OCT29BUFANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes (same contract)
- KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3186, phi -0.168)
- KXNHLSPREAD-26OCT29BUFANA-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2359, phi -0.748)
- KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4438, phi -0.648)
- KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3848, phi -0.268)

portfolios: A EV +4.95 (adj +1.13) on $16.22, P(profit) 0.4731, adj growth 9.7 bp · B EV +3.35 (adj +1.77) on $21.36, P(profit) 0.673, adj growth 16.7 bp · C EV +1.86 (adj +0.89) on $25.23, P(profit) 0.8264, adj growth 8.7 bp · R EV +0.77 (adj +0.34) on $6.00, P(profit) 0.6864, adj growth 12.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT29BUFANA-ANA|yes == KXNHLGAME-26OCT29BUFANA-BUF|no

## OTT @ LAK  ·  10000 joint draws  ·  422 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.483 / away 0.517

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_OTT_win | p_overtime | goals | shots LAK/OTT | LAK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.56 | 0.44 | 0.00 | 5.95 | 27.0/27.1 | 24.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.46 | 5.85 | 26.9/27.2 | 24.0/23.6 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.077 | 0.48 | 0.52 | 0.00 | 6.0 | 21.6/31.8 | 28.0/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.57 | 0.43 | 0.00 | 9.15 | 28.2/28.4 | 23.0/21.7 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.48 | 0.52 | 0.47 | 5.84 | 21.5/32.2 | 28.8/18.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.066 | 0.53 | 0.47 | 0.00 | 3.43 | 25.7/25.9 | 24.2/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.074 | 0.066 | +0.021 | +0.012 | $1.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Tim Stutzle: 1+ goals NO | 67 | 0.719 | 0.705 | +0.033 | +0.020 | $6.68 | FUNDED_RESEARCH | $2 | OTT:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Drake Batherson: 1+ goals NO | 69 | 0.735 | 0.722 | +0.030 | +0.017 | $6.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Erik Gustafsson: 1+ assists NO | 63 | 0.699 | 0.659 | +0.052 | +0.013 | $4.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLSPREAD-26OCT29OTTLA-OTT2|no; why: higher confidence-adjusted growth (6.50 vs 1.30 bp); despite a smaller raw edge (+0.021 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29OTTLA-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: LAK offense suppressed (<= 2 goals)
- **Tim Stutzle: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no; why: Player prop expression KXNHLGOAL-26OCT29OTTLA-OTTTSTUTZLE18-1|no selected over player prop KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: OTT offense succeeds (4+ goals)
- **Drake Batherson: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no; why: Player prop expression KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no selected over player prop KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.86 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT29OTTLA-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: OTT offense succeeds (4+ goals)
- **Erik Gustafsson: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT29OTTLA-LAEGUSTAFSSON64-1|no; why: higher confidence-adjusted growth (1.64 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29OTTLA-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.08.
- thesis OTT:SUPPRESSED (p 0.4531): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [DIRECT], best adjusted EV KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no — Player prop expression KXNHLGOAL-26OCT29OTTLA-OTTTSTUTZLE18-1|no selected over player prop KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis LAK:WINS (p 0.5343): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.402): highest fidelity KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no (same contract)
- KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.402, phi -0.132)
- KXNHLGOAL-26OCT29OTTLA-OTTTSTUTZLE18-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3288, phi -0.226)
- KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3288, phi -0.246)
- KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3742, phi -0.245)
- override: Player prop expression KXNHLGOAL-26OCT29OTTLA-OTTTSTUTZLE18-1|no selected over player prop KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no selected over player prop KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.86 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.53 (adj +0.50) on $16.22, P(profit) 0.5927, adj growth 4.6 bp · B EV +1.39 (adj +0.70) on $18.12, P(profit) 0.5596, adj growth 6.7 bp · C EV +3.29 (adj +0.81) on $26.35, P(profit) 0.6492, adj growth 7.5 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7188, adj growth 2.2 bp

## VAN @ SJS  ·  10000 joint draws  ·  410 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.611 / away 0.389

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_VAN_win | p_overtime | goals | shots SJS/VAN | SJS/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.57 | 0.43 | 0.00 | 6.04 | 27.6/27.2 | 23.9/23.7 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.105 | 0.63 | 0.37 | 0.00 | 6.11 | 33.0/21.6 | 18.7/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.57 | 0.43 | 0.00 | 9.45 | 29.6/28.8 | 23.0/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.52 | 0.48 | 0.47 | 6.01 | 27.9/27.5 | 24.1/24.6 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.55 | 0.45 | 0.44 | 5.94 | 33.3/22.2 | 19.1/30.0 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.084 | 0.65 | 0.35 | 0.00 | 9.38 | 34.4/22.9 | 17.9/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Marco Rossi: 1+ goals YES | 17 | 0.208 | 0.198 | +0.029 | +0.018 | $2.23 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 19 | 0.228 | 0.217 | +0.027 | +0.017 | $2.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 13 | 0.160 | 0.151 | +0.022 | +0.013 | $1.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ goals NO | 71 | 0.806 | 0.740 | +0.082 | +0.016 | $7.32 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (4.59 vs 3.67 bp); relationships: KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT29VANSJ-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes has the higher standalone adjusted growth (4.59 vs 3.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT29VANSJ-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: VAN offense suppressed (<= 2 goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes has the higher standalone adjusted growth (4.59 vs 3.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: VAN offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29VANSJ-SJ3|no; why: higher confidence-adjusted growth (2.80 vs 2.36 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT29VANSJ-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3824): highest fidelity KXNHLSPREAD-26OCT29VANSJ-SJ3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.3257): highest fidelity KXNHLSPREAD-26OCT29VANSJ-SJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.444): highest fidelity KXNHLSPREAD-26OCT29VANSJ-SJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29VANSJ-SJ3|no (same contract)
- KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4045, phi -0.203)
- KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4045, phi -0.231)
- KXNHLGOAL-26OCT29VANSJ-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4045, phi -0.192)
- KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.1 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4611, phi -0.199)

portfolios: A EV +2.64 (adj +0.40) on $16.22, P(profit) 0.5833, adj growth 3.6 bp · B EV +1.72 (adj +0.71) on $13.27, P(profit) 0.4188, adj growth 6.7 bp · C EV +1.02 (adj +0.46) on $11.06, P(profit) 0.8036, adj growth 4.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
