# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-29T15:56:43Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +29.82 | +8.86 | +29.01 | 0.768 | -19.38 | -32.88 | 81.12 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +24.42 | +11.94 | +22.26 | 0.742 | -21.40 | -31.87 | 112.87 |
| C best expression per thesis | 149.31 | +22.88 | +11.87 | +20.74 | 0.691 | -28.92 | -41.24 | 109.90 |
| R FUNDED research stakes | 25.00 | +2.98 | +1.58 | +2.15 | 0.620 | -6.76 | -9.05 | 0.00 |

## WPG @ TBL  ·  10000 joint draws  ·  398 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WPG_win | p_overtime | goals | shots TBL/WPG | TBL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.120 | 0.74 | 0.26 | 0.00 | 5.93 | 32.3/20.9 | 18.6/27.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.70 | 0.30 | 0.00 | 5.95 | 27.1/26.7 | 24.0/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.54 | 0.46 | 0.46 | 5.9 | 27.2/26.8 | 23.5/23.9 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.56 | 0.44 | 0.46 | 5.86 | 32.4/21.2 | 18.1/29.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.68 | 0.32 | 0.00 | 9.19 | 28.5/28.0 | 23.0/21.4 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.069 | 0.76 | 0.24 | 0.00 | 9.24 | 34.4/22.4 | 18.2/26.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Elias Salomonsson: 1+ goals NO | 92 | 0.954 | 0.944 | +0.029 | +0.019 | $8.33 | FUNDED_RESEARCH | $3 | WPG:SUPPRESSED | DIRECT (0.98) | EVIDENCE_STRONGER | D |
| Jake Guentzel: 2+ goals YES | 7 | 0.099 | 0.090 | +0.025 | +0.015 | $1.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Anthony Cirelli: 1+ goals YES | 23 | 0.275 | 0.256 | +0.032 | +0.013 | $2.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Tampa Bay over 4.5 goals scored NO | 69 | 0.753 | 0.716 | +0.048 | +0.011 | $8.33 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Elias Salomonsson: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT29WPGTB-6|no; why: higher confidence-adjusted growth (12.05 vs 0.83 bp); despite a smaller raw edge (+0.029 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.997 vs 0.764); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WPGTB-TBJGUENTZEL59-2|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26OCT29WPGTB-TB5|no: MOSTLY_INDEPENDENT (phi 0.001); failure: WPG offense succeeds (4+ goals)
- **Jake Guentzel: 2+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes; why: higher confidence-adjusted growth (6.97 vs 2.15 bp); despite a smaller raw edge (+0.025 vs +0.032/contract); relationships: KXNHLGOAL-26OCT29WPGTB-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLTEAMTOTAL-26OCT29WPGTB-TB5|no: INTENTIONAL_DIVERSIFIER (phi -0.252); failure: TBL offense suppressed (<= 2 goals)
- **Anthony Cirelli: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-TBJGUENTZEL59-2|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29WPGTB-TBJGUENTZEL59-2|yes has the higher standalone adjusted growth (6.97 vs 2.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.018); they share one thesis budget; relationships: KXNHLGOAL-26OCT29WPGTB-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT29WPGTB-TBJGUENTZEL59-2|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLTEAMTOTAL-26OCT29WPGTB-TB5|no: INTENTIONAL_DIVERSIFIER (phi -0.201); failure: TBL offense suppressed (<= 2 goals)
- **Tampa Bay over 4.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT29WPGTB-TB2|no; why: higher confidence-adjusted growth (1.36 vs 0.90 bp); wins across more scripts (relative breadth 0.882 vs 0.605); alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WPGTB-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT29WPGTB-TBJGUENTZEL59-2|yes: INTENTIONAL_DIVERSIFIER (phi -0.252); KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.201); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:OFFENSE_4PLUS (p 0.4451): highest fidelity KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WPGTB-TBJGUENTZEL59-2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.2565): highest fidelity KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.3342): highest fidelity KXNHLTEAMTOTAL-26OCT29WPGTB-TB5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT29WPGTB-TB5|no (same contract)
- KXNHLGOAL-26OCT29WPGTB-WPGESALOMONSSON57-1|no: FUNDED_RESEARCH; family TRUSTED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.2565, phi -0.119)
- KXNHLGOAL-26OCT29WPGTB-TBJGUENTZEL59-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3342, phi -0.206)
- KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3342, phi -0.227)
- KXNHLTEAMTOTAL-26OCT29WPGTB-TB5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4451, phi -0.64)

portfolios: A EV +1.46 (adj +0.69) on $14.87, P(profit) 0.3446, adj growth 6.6 bp · B EV +1.76 (adj +0.81) on $20.91, P(profit) 0.2609, adj growth 7.7 bp · C EV +1.65 (adj +0.76) on $14.22, P(profit) 0.3005, adj growth 7.0 bp · R EV +0.30 (adj +0.11) on $6.00, P(profit) 0.7183, adj growth 4.1 bp

## UTA @ PIT  ·  10000 joint draws  ·  400 bet sides mapped, 16 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_UTA_win | p_overtime | goals | shots PIT/UTA | PIT/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.51 | 0.49 | 0.00 | 6.03 | 27.2/27.1 | 23.6/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.114 | 0.50 | 0.50 | 0.00 | 9.47 | 28.5/28.7 | 22.4/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.53 | 0.47 | 0.47 | 6.04 | 27.3/27.3 | 23.8/24.0 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.065 | 0.55 | 0.45 | 0.00 | 6.08 | 31.9/21.7 | 18.6/27.6 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.063 | 0.45 | 0.55 | 0.00 | 6.07 | 21.5/31.9 | 27.9/18.2 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.45 | 0.55 | 0.48 | 5.96 | 21.9/32.2 | 28.6/18.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Declan Carlile: 1+ goals YES | 6 | 0.099 | 0.088 | +0.035 | +0.024 | $2.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 2+ goals YES | 7 | 0.114 | 0.097 | +0.039 | +0.022 | $1.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ goals YES | 32 | 0.385 | 0.367 | +0.049 | +0.032 | $4.77 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.54) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 32 | 0.443 | 0.360 | +0.108 | +0.025 | $1.93 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_STRONGER | D |
- **Declan Carlile: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes; why: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes has the higher standalone adjusted growth (20.30 vs 19.82 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.021); relationships: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.03); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 2+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes; why: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes has the higher standalone adjusted growth (20.30 vs 14.93 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.017); relationships: KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: DUPLICATIVE (phi 0.402); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes; why: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes because adjusted EV is 0.2 pts higher while thesis capture is 0.54 vs 0.25 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes; why: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.59 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes: DUPLICATIVE (phi 0.402); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4364): highest fidelity KXNHLSPREAD-26OCT29UTAPIT-UTA2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes — Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes because adjusted EV is 0.2 pts higher while thesis capture is 0.54 vs 0.25 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis PIT:WINS (p 0.5054): highest fidelity KXNHLSPREAD-26OCT29UTAPIT-UTA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.3528): highest fidelity KXNHLSPREAD-26OCT29UTAPIT-UTA2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3438, phi -0.13)
- KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3438, phi -0.219)
- KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 46% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3438, phi -0.291)
- KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 41% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.8 pts; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3438, phi -0.279)
- override: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes because adjusted EV is 0.2 pts higher while thesis capture is 0.54 vs 0.25 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.59 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +6.29 (adj +1.21) on $14.87, P(profit) 0.516, adj growth 10.6 bp · B EV +3.50 (adj +1.97) on $10.78, P(profit) 0.5076, adj growth 18.5 bp · C EV +3.28 (adj +2.00) on $18.68, P(profit) 0.4801, adj growth 18.5 bp · R EV +0.29 (adj +0.19) on $2.00, P(profit) 0.3845, adj growth 6.9 bp

## CBJ @ CAR  ·  10000 joint draws  ·  430 bet sides mapped, 23 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CBJ_win | p_overtime | goals | shots CAR/CBJ | CAR/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.155 | 0.66 | 0.34 | 0.00 | 5.96 | 33.2/20.9 | 18.2/28.8 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.126 | 0.56 | 0.44 | 0.48 | 5.86 | 33.8/21.2 | 18.0/30.4 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.097 | 0.68 | 0.32 | 0.00 | 9.3 | 35.5/22.6 | 17.8/27.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.097 | 0.59 | 0.41 | 0.00 | 6.02 | 27.9/27.0 | 23.9/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.49 | 0.51 | 0.48 | 5.9 | 27.8/27.1 | 23.7/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.56 | 0.44 | 0.00 | 9.22 | 29.3/28.4 | 22.6/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie Coyle: 1+ goals YES | 17 | 0.254 | 0.232 | +0.074 | +0.052 | $5.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.190 | 0.174 | +0.052 | +0.036 | $3.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 52 | 0.649 | 0.562 | +0.112 | +0.025 | $1.35 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 67 | 0.720 | 0.704 | +0.035 | +0.018 | $5.85 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (38.77 vs 23.42 bp); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26OCT29CBJCAR-CAR2|no: REINFORCING (phi 0.16); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (38.77 vs 23.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26OCT29CBJCAR-CAR2|no: REINFORCING (phi 0.158); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: CBJ offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR5|no; why: Broad expression KXNHLSPREAD-26OCT29CBJCAR-CAR2|no selected over broad KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR5|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: REINFORCING (phi 0.16); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: REINFORCING (phi 0.158); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.149); failure: CAR wins by 2+
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes; why: Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSJARVIS24-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.86 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26OCT29CBJCAR-CAR2|no: MOSTLY_INDEPENDENT (phi 0.149); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.3213): highest fidelity KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.2183): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS (p 0.4267): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29CBJCAR-CAR2|no (same contract)
- KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4603, phi -0.243)
- KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4603, phi -0.239)
- KXNHLSPREAD-26OCT29CBJCAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.4 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3507, phi -1.0)
- KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4349, phi -0.226)
- override: Broad expression KXNHLSPREAD-26OCT29CBJCAR-CAR2|no selected over broad KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR5|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSJARVIS24-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.86 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.07 (adj +1.48) on $14.87, P(profit) 0.5306, adj growth 13.7 bp · B EV +4.44 (adj +2.90) on $16.87, P(profit) 0.3938, adj growth 27.3 bp · C EV +6.14 (adj +3.93) on $22.98, P(profit) 0.3938, adj growth 36.2 bp · R EV +0.31 (adj +0.10) on $3.00, P(profit) 0.4995, adj growth 3.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT29CBJCAR-CBJ|yes == KXNHLGAME-26OCT29CBJCAR-CAR|no

## CHI @ DET  ·  10000 joint draws  ·  422 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_CHI_win | p_overtime | goals | shots DET/CHI | DET/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.148 | 0.71 | 0.29 | 0.00 | 5.97 | 33.3/21.1 | 18.5/28.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.57 | 0.43 | 0.45 | 5.89 | 33.3/21.3 | 18.3/29.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.64 | 0.36 | 0.00 | 6.0 | 27.6/26.7 | 23.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.53 | 0.47 | 0.49 | 5.9 | 27.6/26.8 | 23.6/24.4 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.092 | 0.75 | 0.25 | 0.00 | 9.14 | 34.7/22.2 | 17.9/26.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.63 | 0.37 | 0.00 | 9.26 | 29.6/28.6 | 23.5/22.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Patrick Kane: 1+ assists NO | 57 | 0.712 | 0.613 | +0.124 | +0.026 | $7.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Connor Bedard: 1+ assists NO | 58 | 0.654 | 0.607 | +0.057 | +0.010 | $1.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (6.08 vs 0.94 bp); relationships: KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.107); failure: CHI offense succeeds (4+ goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no; why: second expression of the same thesis: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no has the higher standalone adjusted growth (6.08 vs 0.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.107); they share one thesis budget; relationships: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.107); failure: CHI offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.15, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:SUPPRESSED (p 0.4964): highest fidelity KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no (same contract)
- KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.2 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2874, phi -0.257)
- KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2874, phi -0.271)

portfolios: A EV +1.83 (adj +0.36) on $11.90, P(profit) 0.4887, adj growth 3.4 bp · B EV +1.71 (adj +0.35) on $9.15, P(profit) 0.7117, adj growth 3.3 bp · C EV +2.09 (adj +0.44) on $9.85, P(profit) 0.7117, adj growth 4.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ STL  ·  10000 joint draws  ·  436 bet sides mapped, 5 +EV candidates, 4 on card


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
| Charlie McAvoy: 1+ assists NO | 54 | 0.631 | 0.583 | +0.073 | +0.025 | $6.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Casey Mittelstadt: 1+ goals YES | 14 | 0.177 | 0.165 | +0.029 | +0.017 | $2.11 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 24 | 0.283 | 0.271 | +0.031 | +0.019 | $2.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 29 | 0.330 | 0.318 | +0.025 | +0.014 | $1.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29BOSSTL-BOSDPASTRNAK88-1|no; why: higher confidence-adjusted growth (5.78 vs 1.70 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: BOS offense succeeds (4+ goals)
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT29BOSSTL-3|yes; why: higher confidence-adjusted growth (4.80 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.93 vs 0.773); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: BOS offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (3.99 vs 2.01 bp); relationships: KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (3.99 vs 2.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis BOS:SUPPRESSED (p 0.4059): highest fidelity KXNHLGOAL-26OCT29BOSSTL-BOSDPASTRNAK88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.4174): highest fidelity KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.3722): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT29BOSSTL-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3722, phi -0.279)
- KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4059, phi -0.185)
- KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.369, phi -0.258)
- KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.369, phi -0.27)

portfolios: A EV +1.85 (adj +0.90) on $14.18, P(profit) 0.4833, adj growth 8.5 bp · B EV +1.73 (adj +0.81) on $13.08, P(profit) 0.4833, adj growth 7.7 bp · C EV +1.48 (adj +0.62) on $11.50, P(profit) 0.7326, adj growth 5.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ NSH  ·  10000 joint draws  ·  428 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_WSH_win | p_overtime | goals | shots NSH/WSH | NSH/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.57 | 0.43 | 0.00 | 6.03 | 27.9/27.9 | 24.6/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.48 | 5.95 | 28.0/28.1 | 24.8/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.59 | 0.41 | 0.00 | 9.32 | 29.5/29.4 | 23.7/22.6 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.074 | 0.53 | 0.47 | 0.00 | 6.04 | 22.4/32.9 | 29.3/18.9 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.065 | 0.65 | 0.35 | 0.00 | 6.03 | 33.0/22.5 | 19.8/28.2 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.48 | 0.52 | 0.47 | 5.96 | 22.4/33.1 | 29.7/19.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 17 | 0.233 | 0.216 | +0.053 | +0.036 | $4.25 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 29 | 0.334 | 0.318 | +0.030 | +0.014 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 25 | 0.322 | 0.273 | +0.059 | +0.010 | $1.03 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT29WSHNSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (18.77 vs 1.17 bp); despite a smaller raw edge (+0.053 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLAST-26OCT29WSHNSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.055); failure: WSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes; why: higher confidence-adjusted growth (1.90 vs 0.60 bp); alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLAST-26OCT29WSHNSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: NSH offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (18.77 vs 1.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.055); they share one thesis budget; relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.055); KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3663): highest fidelity KXNHLAST-26OCT29WSHNSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.437): highest fidelity KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes (same contract)
- KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4108, phi -0.249)
- KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3447, phi -0.261)
- KXNHLAST-26OCT29WSHNSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4108, phi -0.258)

portfolios: A EV +3.03 (adj +1.33) on $13.86, P(profit) 0.4686, adj growth 11.9 bp · B EV +1.68 (adj +0.98) on $7.36, P(profit) 0.3124, adj growth 9.2 bp · C EV +1.95 (adj +1.27) on $8.49, P(profit) 0.4925, adj growth 11.7 bp · R EV +0.59 (adj +0.40) on $2.00, P(profit) 0.2327, adj growth 14.2 bp

## MTL @ DAL  ·  10000 joint draws  ·  412 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_MTL_win | p_overtime | goals | shots DAL/MTL | DAL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DAL shot control · normal event (5-7) · decided (2+) | 0.117 | 0.66 | 0.34 | 0.00 | 5.98 | 31.5/20.4 | 17.8/26.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.53 | 0.47 | 0.00 | 5.99 | 26.5/25.9 | 22.7/22.9 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.53 | 0.47 | 0.48 | 5.86 | 31.5/20.7 | 17.5/28.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.52 | 0.48 | 0.48 | 5.86 | 26.8/26.3 | 23.1/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.57 | 0.43 | 0.00 | 9.18 | 27.9/27.3 | 21.8/21.6 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.068 | 0.66 | 0.34 | 0.00 | 9.19 | 33.3/21.9 | 17.3/25.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cole Caufield: 1+ assists NO | 61 | 0.681 | 0.638 | +0.055 | +0.011 | $3.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
- **Cole Caufield: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHL3PTOTAL-26OCT29MTLDAL-2|no; why: higher confidence-adjusted growth (1.24 vs 0.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: MTL offense succeeds (4+ goals)

**Review**: scripts DAL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, DAL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis MTL:SUPPRESSED (p 0.4627): highest fidelity KXNHLAST-26OCT29MTLDAL-MTLCCAUFIELD13-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29MTLDAL-MTLCCAUFIELD13-1|no (same contract)
- KXNHLAST-26OCT29MTLDAL-MTLCCAUFIELD13-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3232, phi -0.265)

portfolios: A EV +0.52 (adj +0.11) on $5.95, P(profit) 0.6813, adj growth 1.0 bp · B EV +0.30 (adj +0.06) on $3.41, P(profit) 0.6813, adj growth 0.6 bp · C EV +0.40 (adj +0.08) on $4.54, P(profit) 0.6813, adj growth 0.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ MIN  ·  10000 joint draws  ·  400 bet sides mapped, 7 +EV candidates, 4 on card


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
| Brayden Schenn: 1+ goals YES | 18 | 0.244 | 0.222 | +0.053 | +0.031 | $3.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 53 | 0.606 | 0.586 | +0.058 | +0.038 | $8.36 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.159 | 0.144 | +0.032 | +0.017 | $1.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Anthony Duclair: 1+ goals YES | 13 | 0.159 | 0.149 | +0.021 | +0.011 | $1.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes; why: higher confidence-adjusted growth (13.68 vs 3.15 bp); despite a smaller raw edge (+0.053 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29NYIMIN-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: NYI offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no; why: higher confidence-adjusted growth (12.88 vs 2.21 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.989 vs 0.883); relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29NYIMIN-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: MIN offense succeeds (4+ goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (13.68 vs 5.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29NYIMIN-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.024); failure: NYI offense suppressed (<= 2 goals)
- **Anthony Duclair: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (13.68 vs 2.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.024); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:OFFENSE_4PLUS (p 0.3232): highest fidelity KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3629): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4447): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29NYIMIN-MIN2|no (same contract)
- KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4527, phi -0.244)
- KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4187, phi -0.294)
- KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4527, phi -0.197)
- KXNHLGOAL-26OCT29NYIMIN-NYIADUCLAIR11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4527, phi -0.186)

portfolios: A EV +2.12 (adj +1.04) on $14.87, P(profit) 0.4732, adj growth 9.8 bp · B EV +2.60 (adj +1.55) on $15.26, P(profit) 0.7066, adj growth 14.6 bp · C EV +2.56 (adj +1.58) on $16.02, P(profit) 0.7006, adj growth 14.7 bp · R EV +0.32 (adj +0.21) on $3.00, P(profit) 0.6058, adj growth 7.8 bp

## BUF @ ANA  ·  10000 joint draws  ·  444 bet sides mapped, 19 +EV candidates, 4 on card


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
| Tim Washe: 1+ goals YES | 11 | 0.163 | 0.147 | +0.046 | +0.030 | $2.95 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 2.5 goals NO | 76 | 0.853 | 0.804 | +0.080 | +0.031 | $8.36 | FUNDED_RESEARCH | $3 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 1.5 goals YES | 25 | 0.345 | 0.295 | +0.082 | +0.032 | $2.44 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Alex Killorn: 1+ goals YES | 18 | 0.224 | 0.211 | +0.034 | +0.020 | $1.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: higher confidence-adjusted growth (19.27 vs 12.22 bp); despite a smaller raw edge (+0.046 vs +0.080/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT29BUFANA-BUF3|no: MOSTLY_INDEPENDENT (phi 0.088); KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: MOSTLY_INDEPENDENT (phi 0.115); KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: ANA offense suppressed (<= 2 goals)
- **Buffalo wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: higher confidence-adjusted growth (12.22 vs 11.25 bp); despite a smaller raw edge (+0.080 vs +0.082/contract); wins across more scripts (relative breadth 1.034 vs 0.516); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.088); KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: DUPLICATIVE (phi 0.301); KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.099); failure: BUF wins by 2+
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-BUF3|no has the higher standalone adjusted growth (12.22 vs 11.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.301); they share one thesis budget; relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.115); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: DUPLICATIVE (phi 0.301); KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: REINFORCING (phi 0.16); failure: BUF wins (incl. OT/SO)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-BUF3|no has the higher standalone adjusted growth (12.22 vs 5.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.099); they share one thesis budget; relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: MOSTLY_INDEPENDENT (phi 0.099); KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: REINFORCING (phi 0.16); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4751): highest fidelity KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5562): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3447): highest fidelity KXNHLSPREAD-26OCT29BUFANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes (same contract)
- KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3186, phi -0.168)
- KXNHLSPREAD-26OCT29BUFANA-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2359, phi -0.748)
- KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4438, phi -0.648)
- KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3186, phi -0.198)

portfolios: A EV +4.54 (adj +0.98) on $14.87, P(profit) 0.4731, adj growth 8.5 bp · B EV +3.14 (adj +1.61) on $15.71, P(profit) 0.515, adj growth 15.2 bp · C EV +1.15 (adj +0.45) on $11.15, P(profit) 0.8528, adj growth 4.4 bp · R EV +1.02 (adj +0.50) on $5.00, P(profit) 0.4314, adj growth 18.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT29BUFANA-BUF|no == KXNHLGAME-26OCT29BUFANA-ANA|yes

## OTT @ LAK  ·  10000 joint draws  ·  418 bet sides mapped, 5 +EV candidates, 4 on card


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
| Tim Stutzle: 1+ assists NO | 55 | 0.635 | 0.590 | +0.068 | +0.023 | $5.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Jake Sanderson: 1+ assists NO | 58 | 0.703 | 0.613 | +0.105 | +0.016 | $3.62 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Tim Stutzle: 1+ goals NO | 68 | 0.719 | 0.708 | +0.024 | +0.013 | $3.80 | FUNDED_RESEARCH | $1 | OTT:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Erik Gustafsson: 1+ assists NO | 63 | 0.699 | 0.659 | +0.052 | +0.013 | $4.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
- **Tim Stutzle: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (4.63 vs 2.35 bp); despite a smaller raw edge (+0.068 vs +0.105/contract); relationships: KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.088); KXNHLGOAL-26OCT29OTTLA-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: OTT offense succeeds (4+ goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no; why: second expression of the same thesis: KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no has the higher standalone adjusted growth (4.63 vs 2.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.088); they share one thesis budget; relationships: KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.088); KXNHLGOAL-26OCT29OTTLA-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.09); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: OTT offense succeeds (4+ goals)
- **Tim Stutzle: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no; why: second expression of the same thesis: KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no has the higher standalone adjusted growth (4.63 vs 1.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.09); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: OTT offense succeeds (4+ goals)
- **Erik Gustafsson: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29OTTLA-LAQBYFIELD55-1|no; why: higher confidence-adjusted growth (1.64 vs 0.21 bp); alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT29OTTLA-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.08.
- thesis OTT:SUPPRESSED (p 0.4531): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [DIRECT], best adjusted EV KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS (p 0.5343): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.402): highest fidelity KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no (same contract)
- KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3288, phi -0.29)
- KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.8 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3288, phi -0.225)
- KXNHLGOAL-26OCT29OTTLA-OTTTSTUTZLE18-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3288, phi -0.226)
- KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3742, phi -0.245)

portfolios: A EV +1.62 (adj +0.38) on $14.87, P(profit) 0.6382, adj growth 3.6 bp · B EV +1.71 (adj +0.45) on $16.56, P(profit) 0.6235, adj growth 4.3 bp · C EV +1.35 (adj +0.41) on $13.03, P(profit) 0.6352, adj growth 3.9 bp · R EV +0.03 (adj +0.02) on $1.00, P(profit) 0.7188, adj growth 0.7 bp

## VAN @ SJS  ·  10000 joint draws  ·  410 bet sides mapped, 7 +EV candidates, 4 on card


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
| Dmitry Orlov: 1+ goals NO | 90 | 0.932 | 0.920 | +0.026 | +0.014 | $7.34 | FUNDED_RESEARCH | $2 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ goals NO | 70 | 0.806 | 0.734 | +0.091 | +0.019 | $6.67 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| San Jose wins by over 2.5 goals NO | 71 | 0.773 | 0.739 | +0.049 | +0.015 | $3.60 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ assists NO | 60 | 0.720 | 0.632 | +0.103 | +0.015 | $3.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
- **Dmitry Orlov: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLSPREAD-26OCT29VANSJ-SJ3|no: MOSTLY_INDEPENDENT (phi 0.064); KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.075); failure: SJS offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29VANSJ-SJ3|no; why: higher confidence-adjusted growth (3.95 vs 2.36 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29VANSJ-SJDORLOV9-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLSPREAD-26OCT29VANSJ-SJ3|no: MOSTLY_INDEPENDENT (phi 0.118); KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: SJS offense succeeds (4+ goals)
- **San Jose wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLPTS-26OCT29VANSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (2.36 vs 1.65 bp); despite a smaller raw edge (+0.049 vs +0.136/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT29VANSJ-SJDORLOV9-1|no: MOSTLY_INDEPENDENT (phi 0.064); KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.118); KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: REINFORCING (phi 0.166); failure: SJS wins by 2+
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29VANSJ-SJ3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29VANSJ-SJ3|no has the higher standalone adjusted growth (2.36 vs 2.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.166); they share one thesis budget; relationships: KXNHLGOAL-26OCT29VANSJ-SJDORLOV9-1|no: MOSTLY_INDEPENDENT (phi 0.075); KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT29VANSJ-SJ3|no: REINFORCING (phi 0.166); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.3257): highest fidelity KXNHLSPREAD-26OCT29VANSJ-SJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT29VANSJ-SJ5|no less than the minimum stake; KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no kept
- thesis VAN:WINS (p 0.444): highest fidelity KXNHLSPREAD-26OCT29VANSJ-SJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29VANSJ-SJ3|no (same contract)
- KXNHLGOAL-26OCT29VANSJ-SJDORLOV9-1|no: FUNDED_RESEARCH; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4611, phi -0.1)
- KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.1 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4611, phi -0.199)
- KXNHLSPREAD-26OCT29VANSJ-SJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis SJS:WINS_BY_2PLUS (p 0.3397, phi -0.755)
- KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.5 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4611, phi -0.248)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT29VANSJ-SJ5|no less than the minimum stake; KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no kept

portfolios: A EV +2.48 (adj +0.38) on $14.87, P(profit) 0.5833, adj growth 3.5 bp · B EV +1.86 (adj +0.45) on $20.91, P(profit) 0.6904, adj growth 4.3 bp · C EV +0.84 (adj +0.33) on $18.85, P(profit) 0.7274, adj growth 3.1 bp · R EV +0.12 (adj +0.05) on $3.00, P(profit) 0.7274, adj growth 2.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
