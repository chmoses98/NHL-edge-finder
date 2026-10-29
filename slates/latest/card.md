# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-29T14:45:05Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +27.55 | +9.09 | +26.15 | 0.759 | -20.65 | -32.55 | 83.60 |
| B thesis-diversified (joint) ← optimiser card | 149.04 | +23.55 | +12.23 | +20.97 | 0.729 | -21.69 | -31.85 | 115.66 |
| C best expression per thesis | 149.98 | +22.57 | +12.07 | +19.93 | 0.692 | -27.97 | -39.95 | 112.59 |
| R FUNDED research stakes | 22.00 | +2.56 | +1.54 | +1.70 | 0.602 | -6.84 | -9.04 | 0.00 |

## WPG @ TBL  ·  10000 joint draws  ·  396 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WPG_win | p_overtime | goals | shots TBL/WPG | TBL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.69 | 0.31 | 0.00 | 6.0 | 27.1/26.6 | 23.9/22.8 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.119 | 0.73 | 0.27 | 0.00 | 5.98 | 32.3/21.0 | 18.5/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.52 | 0.48 | 0.47 | 5.87 | 27.0/26.7 | 23.4/23.7 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.57 | 0.43 | 0.48 | 5.89 | 32.7/21.2 | 18.1/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.67 | 0.33 | 0.00 | 9.12 | 28.8/28.1 | 23.2/21.8 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.067 | 0.75 | 0.25 | 0.00 | 9.2 | 34.4/22.4 | 18.2/26.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ilya Mikheyev: 1+ goals YES | 17 | 0.209 | 0.197 | +0.030 | +0.017 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Charle-Edouard D'Astous: 1+ goals NO | 89 | 0.919 | 0.909 | +0.022 | +0.012 | $8.29 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 11 | 0.138 | 0.129 | +0.021 | +0.012 | $1.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 25 | 0.288 | 0.277 | +0.025 | +0.014 | $1.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
- **Ilya Mikheyev: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes; why: higher confidence-adjusted growth (4.37 vs 1.71 bp); relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: TBL offense suppressed (<= 2 goals)
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT29WPGTB-TB2|no; why: higher confidence-adjusted growth (3.59 vs 1.63 bp); despite a smaller raw edge (+0.022 vs +0.029/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.004 vs 0.595); alternative not eligible: confidence-adjusted EV +0.0088 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: TBL offense succeeds (4+ goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (2.96 vs 2.17 bp); despite a smaller raw edge (+0.021 vs +0.025/contract); relationships: KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29WPGTB-TB3|no; why: higher confidence-adjusted growth (2.17 vs 0.68 bp); despite a smaller raw edge (+0.025 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:OFFENSE_4PLUS (p 0.4474): highest fidelity KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.2621): highest fidelity KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.3387): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3387, phi -0.192)
- KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4474, phi -0.114)
- KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.5209, phi -0.193)
- KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.5209, phi -0.282)

portfolios: A EV +1.09 (adj +0.59) on $13.56, P(profit) 0.5682, adj growth 5.5 bp · B EV +0.96 (adj +0.55) on $13.59, P(profit) 0.4816, adj growth 5.2 bp · C EV +0.68 (adj +0.39) on $5.21, P(profit) 0.4379, adj growth 3.6 bp · R EV +0.07 (adj +0.04) on $3.00, P(profit) 0.9188, adj growth 1.6 bp

## UTA @ PIT  ·  10000 joint draws  ·  398 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_UTA_win | p_overtime | goals | shots PIT/UTA | PIT/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.49 | 0.51 | 0.00 | 6.02 | 27.2/27.0 | 23.6/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.51 | 0.49 | 0.00 | 9.47 | 28.9/28.9 | 22.5/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.47 | 6.01 | 27.1/27.1 | 23.8/23.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.071 | 0.61 | 0.39 | 0.00 | 6.01 | 31.9/21.6 | 18.6/27.7 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.065 | 0.44 | 0.56 | 0.00 | 6.07 | 21.6/31.8 | 27.7/18.5 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.45 | 0.55 | 0.47 | 5.96 | 21.7/32.1 | 28.8/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Blake Lizotte: 1+ goals YES | 10 | 0.163 | 0.141 | +0.057 | +0.035 | $3.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Declan Carlile: 1+ goals YES | 6 | 0.097 | 0.086 | +0.033 | +0.022 | $2.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ goals YES | 32 | 0.386 | 0.368 | +0.051 | +0.033 | $5.00 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 32 | 0.434 | 0.357 | +0.099 | +0.021 | $3.01 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.60) | EVIDENCE_STRONGER | D |
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (27.17 vs 4.51 bp); despite a smaller raw edge (+0.057 vs +0.099/contract); relationships: KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: PIT offense suppressed (<= 2 goals)
- **Declan Carlile: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes; why: higher confidence-adjusted growth (17.67 vs 16.15 bp); despite a smaller raw edge (+0.033 vs +0.035/contract); wins across more scripts (relative breadth 0.88 vs 0.73); relationships: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes; why: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes because adjusted EV is 0.4 pts higher while thesis capture is 0.53 vs 0.27 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes; why: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.60 vs 0.20 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:WINS_BY_2PLUS (p 0.2966): highest fidelity KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.4351): highest fidelity KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes — Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes because adjusted EV is 0.4 pts higher while thesis capture is 0.53 vs 0.27 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis UTA:SUPPRESSED (p 0.3568): highest fidelity KXNHLAST-26OCT29UTAPIT-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3475, phi -0.177)
- KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3475, phi -0.136)
- KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3475, phi -0.265)
- KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 40% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.9 pts; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3475, phi -0.308)
- override: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes because adjusted EV is 0.4 pts higher while thesis capture is 0.53 vs 0.27 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.60 vs 0.20 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +6.16 (adj +1.41) on $14.60, P(profit) 0.6064, adj growth 12.7 bp · B EV +4.56 (adj +2.55) on $13.53, P(profit) 0.5357, adj growth 23.9 bp · C EV +4.55 (adj +2.86) on $17.97, P(profit) 0.2526, adj growth 26.4 bp · R EV +0.30 (adj +0.20) on $2.00, P(profit) 0.386, adj growth 7.2 bp

## CBJ @ CAR  ·  10000 joint draws  ·  428 bet sides mapped, 23 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CBJ_win | p_overtime | goals | shots CAR/CBJ | CAR/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.153 | 0.66 | 0.34 | 0.00 | 6.0 | 33.6/21.2 | 18.4/29.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.127 | 0.54 | 0.46 | 0.47 | 5.91 | 33.9/21.5 | 18.3/30.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.61 | 0.39 | 0.00 | 6.06 | 27.7/26.9 | 23.9/23.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.094 | 0.68 | 0.32 | 0.00 | 9.18 | 35.2/22.5 | 17.9/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.51 | 0.49 | 0.48 | 5.95 | 27.8/26.9 | 23.5/24.4 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.072 | 0.62 | 0.38 | 0.00 | 3.47 | 32.0/19.9 | 18.4/29.8 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie Coyle: 1+ goals YES | 17 | 0.253 | 0.231 | +0.073 | +0.051 | $5.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.183 | 0.169 | +0.046 | +0.031 | $3.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 66 | 0.716 | 0.700 | +0.041 | +0.024 | $7.36 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Seth Jarvis: 1+ goals NO | 70 | 0.741 | 0.730 | +0.026 | +0.015 | $4.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (37.34 vs 17.25 bp); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: MOSTLY_INDEPENDENT (phi 0.024); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (37.34 vs 17.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: MOSTLY_INDEPENDENT (phi 0.029); failure: CBJ offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes; why: KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes has the higher standalone adjusted growth (7.76 vs 5.75 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.138); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: CAR offense succeeds (4+ goals)
- **Seth Jarvis: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes; why: Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.88 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.029); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.3206): highest fidelity KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.2167): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CBJ2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.3455): highest fidelity KXNHLTEAMTOTAL-26OCT29CBJCAR-CAR5|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no — Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.88 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4608, phi -0.243)
- KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4608, phi -0.232)
- KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4423, phi -0.212)
- KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4423, phi -0.231)
- override: Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSGOSTISBEHERE4-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.88 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.01 (adj +1.40) on $14.60, P(profit) 0.5679, adj growth 13.3 bp · B EV +3.92 (adj +2.65) on $20.71, P(profit) 0.3885, adj growth 25.0 bp · C EV +5.25 (adj +3.35) on $20.58, P(profit) 0.3885, adj growth 30.9 bp · R EV +0.12 (adj +0.07) on $2.00, P(profit) 0.7162, adj growth 2.7 bp

## CHI @ DET  ·  10000 joint draws  ·  420 bet sides mapped, 3 +EV candidates, 3 on card


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
| Roman Kantserov: 1+ goals NO | 75 | 0.803 | 0.789 | +0.040 | +0.025 | $5.73 | FUNDED_RESEARCH | $2 | CHI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 57 | 0.712 | 0.616 | +0.124 | +0.029 | $4.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Connor Bedard: 1+ assists NO | 57 | 0.654 | 0.607 | +0.067 | +0.020 | $2.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no; why: higher confidence-adjusted growth (7.91 vs 7.71 bp); despite a smaller raw edge (+0.040 vs +0.124/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: REINFORCING (phi 0.197); KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: REINFORCING (phi 0.267); failure: CHI offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no has the higher standalone adjusted growth (7.91 vs 7.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.197); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no: REINFORCING (phi 0.197); KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.107); failure: CHI offense succeeds (4+ goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no has the higher standalone adjusted growth (7.91 vs 3.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.267); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no: REINFORCING (phi 0.267); KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.107); failure: CHI offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.15, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:SUPPRESSED (p 0.4964): highest fidelity KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2874, phi -0.186)
- KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.7 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2874, phi -0.257)
- KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2874, phi -0.271)

portfolios: A EV +1.84 (adj +0.57) on $14.60, P(profit) 0.771, adj growth 5.5 bp · B EV +1.50 (adj +0.49) on $12.43, P(profit) 0.607, adj growth 4.7 bp · C EV +0.57 (adj +0.36) on $10.81, P(profit) 0.8031, adj growth 3.4 bp · R EV +0.10 (adj +0.07) on $2.00, P(profit) 0.8031, adj growth 2.6 bp

## BOS @ STL  ·  10000 joint draws  ·  436 bet sides mapped, 3 +EV candidates, 3 on card


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
| Casey Mittelstadt: 1+ goals YES | 14 | 0.177 | 0.165 | +0.029 | +0.017 | $1.95 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 24 | 0.283 | 0.271 | +0.031 | +0.019 | $2.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 29 | 0.330 | 0.317 | +0.025 | +0.013 | $1.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT29BOSSTL-8|yes; why: higher confidence-adjusted growth (4.80 vs 0.02 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.93 vs 0.34); alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: BOS offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (3.99 vs 1.67 bp); relationships: KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (3.99 vs 1.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.4174): highest fidelity KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.3722): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4059, phi -0.185)
- KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.369, phi -0.258)
- KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.369, phi -0.27)

portfolios: A EV +1.05 (adj +0.61) on $8.08, P(profit) 0.6052, adj growth 5.6 bp · B EV +0.83 (adj +0.48) on $6.30, P(profit) 0.4131, adj growth 4.6 bp · C EV +0.40 (adj +0.24) on $3.26, P(profit) 0.2835, adj growth 2.2 bp · R EV +0.19 (adj +0.11) on $1.00, P(profit) 0.1769, adj growth 4.0 bp

## WSH @ NSH  ·  10000 joint draws  ·  428 bet sides mapped, 3 +EV candidates, 2 on card


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
| Aliaksei Protas: 1+ goals YES | 16 | 0.233 | 0.213 | +0.063 | +0.044 | $5.00 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 29 | 0.334 | 0.316 | +0.030 | +0.011 | $1.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT29WSHNSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (29.21 vs 1.17 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: WSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes; why: higher confidence-adjusted growth (1.27 vs 0.60 bp); alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3663): highest fidelity KXNHLAST-26OCT29WSHNSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.437): highest fidelity KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes (same contract)
- KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4108, phi -0.249)
- KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3447, phi -0.261)

portfolios: A EV +3.67 (adj +1.78) on $14.46, P(profit) 0.4686, adj growth 16.1 bp · B EV +2.03 (adj +1.36) on $6.71, P(profit) 0.2327, adj growth 12.8 bp · C EV +2.67 (adj +1.78) on $8.80, P(profit) 0.2327, adj growth 16.5 bp · R EV +0.75 (adj +0.52) on $2.00, P(profit) 0.2327, adj growth 18.7 bp

## MTL @ DAL  ·  10000 joint draws  ·  412 bet sides mapped, 2 +EV candidates, 2 on card


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
| Cole Caufield: 1+ assists NO | 60 | 0.681 | 0.633 | +0.065 | +0.016 | $4.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Thomas Harley: 1+ assists YES | 36 | 0.429 | 0.390 | +0.053 | +0.013 | $2.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DAL:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_MIXED | D |
- **Cole Caufield: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHL3PTOTAL-26OCT29MTLDAL-2|no; why: higher confidence-adjusted growth (2.48 vs 0.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT29MTLDAL-DALTHARLEY55-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: MTL offense succeeds (4+ goals)
- **Thomas Harley: 1+ assists YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29MTLDAL-DALJROBERTSON21-1|yes; why: higher confidence-adjusted growth (1.69 vs 0.06 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0025 below the 0.010/contract floor; relationships: KXNHLAST-26OCT29MTLDAL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts DAL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, DAL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis MTL:SUPPRESSED (p 0.4627): highest fidelity KXNHLAST-26OCT29MTLDAL-MTLCCAUFIELD13-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29MTLDAL-MTLCCAUFIELD13-1|no (same contract)
- thesis DAL:OFFENSE_4PLUS (p 0.407): highest fidelity KXNHLAST-26OCT29MTLDAL-DALTHARLEY55-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT29MTLDAL-DALTHARLEY55-1|yes (same contract)
- KXNHLAST-26OCT29MTLDAL-MTLCCAUFIELD13-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3232, phi -0.265)
- KXNHLAST-26OCT29MTLDAL-DALTHARLEY55-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3775, phi -0.293)

portfolios: A EV +1.43 (adj +0.36) on $11.68, P(profit) 0.4292, adj growth 3.2 bp · B EV +0.80 (adj +0.20) on $6.88, P(profit) 0.6813, adj growth 1.9 bp · C EV +1.04 (adj +0.26) on $8.97, P(profit) 0.6813, adj growth 2.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ MIN  ·  10000 joint draws  ·  400 bet sides mapped, 6 +EV candidates, 4 on card


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
| Kirill Kaprizov: 1+ goals NO | 52 | 0.606 | 0.583 | +0.068 | +0.046 | $8.29 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Olli Maatta: 1+ goals YES | 4 | 0.064 | 0.055 | +0.021 | +0.013 | $1.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.159 | 0.147 | +0.032 | +0.020 | $2.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 20 | 0.244 | 0.228 | +0.033 | +0.017 | $2.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no; why: higher confidence-adjusted growth (18.35 vs 2.21 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.989 vs 0.883); relationships: KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: MIN offense succeeds (4+ goals)
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT29NYIMIN-2|yes; why: higher confidence-adjusted growth (8.11 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: MIN offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (7.43 vs 3.62 bp); despite a smaller raw edge (+0.032 vs +0.033/contract); relationships: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NYI offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes; why: higher confidence-adjusted growth (3.62 vs 3.15 bp); despite a smaller raw edge (+0.033 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.3629): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:OFFENSE_4PLUS (p 0.3232): highest fidelity KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes (same contract)
- thesis GAME:TIGHT (p 0.4447): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29NYIMIN-MIN2|no (same contract)
- KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4187, phi -0.294)
- KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3629, phi -0.1)
- KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4527, phi -0.197)
- KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4527, phi -0.244)

portfolios: A EV +1.72 (adj +0.78) on $14.60, P(profit) 0.5634, adj growth 7.4 bp · B EV +2.47 (adj +1.53) on $13.63, P(profit) 0.6909, adj growth 14.6 bp · C EV +1.90 (adj +1.16) on $14.94, P(profit) 0.6058, adj growth 10.9 bp · R EV +0.38 (adj +0.25) on $3.00, P(profit) 0.6058, adj growth 9.6 bp

## BUF @ ANA  ·  10000 joint draws  ·  428 bet sides mapped, 19 +EV candidates, 4 on card


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
| Zach Metsa: 1+ goals NO | 92 | 0.966 | 0.951 | +0.041 | +0.025 | $8.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 11 | 0.163 | 0.147 | +0.046 | +0.030 | $3.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Anaheim wins by over 1.5 goals YES | 25 | 0.345 | 0.295 | +0.082 | +0.032 | $3.02 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ goals NO | 64 | 0.695 | 0.680 | +0.039 | +0.024 | $6.03 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Zach Metsa: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: MOSTLY_INDEPENDENT (phi 0.044); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: BUF offense succeeds (4+ goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: higher confidence-adjusted growth (19.27 vs 12.22 bp); despite a smaller raw edge (+0.046 vs +0.080/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29BUFANA-BUFZMETSA73-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: MOSTLY_INDEPENDENT (phi 0.115); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: ANA offense suppressed (<= 2 goals)
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: KXNHLSPREAD-26OCT29BUFANA-BUF3|no has the higher standalone adjusted growth (12.22 vs 11.25 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.301); relationships: KXNHLGOAL-26OCT29BUFANA-BUFZMETSA73-1|no: MOSTLY_INDEPENDENT (phi 0.044); KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.115); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.17); failure: BUF wins (incl. OT/SO)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: KXNHLSPREAD-26OCT29BUFANA-BUF3|no has the higher standalone adjusted growth (12.22 vs 5.65 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.157); relationships: KXNHLGOAL-26OCT29BUFANA-BUFZMETSA73-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: REINFORCING (phi 0.17); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4751): highest fidelity KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5562): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3447): highest fidelity KXNHLSPREAD-26OCT29BUFANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes (same contract)
- KXNHLGOAL-26OCT29BUFANA-BUFZMETSA73-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3848, phi -0.068)
- KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3186, phi -0.168)
- KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4438, phi -0.648)
- KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3848, phi -0.268)

portfolios: A EV +4.40 (adj +0.94) on $14.60, P(profit) 0.4731, adj growth 8.2 bp · B EV +2.85 (adj +1.60) on $20.34, P(profit) 0.4304, adj growth 15.2 bp · C EV +1.59 (adj +0.73) on $21.62, P(profit) 0.8264, adj growth 7.2 bp · R EV +0.43 (adj +0.19) on $3.00, P(profit) 0.7632, adj growth 7.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT29BUFANA-BUF|no == KXNHLGAME-26OCT29BUFANA-ANA|yes

## OTT @ LAK  ·  10000 joint draws  ·  418 bet sides mapped, 4 +EV candidates, 4 on card


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
| Jake Sanderson: 1+ assists NO | 57 | 0.703 | 0.607 | +0.115 | +0.019 | $4.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Tim Stutzle: 1+ assists NO | 56 | 0.635 | 0.590 | +0.058 | +0.013 | $2.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Ottawa wins by over 1.5 goals NO | 70 | 0.756 | 0.726 | +0.042 | +0.011 | $3.33 | FUNDED_RESEARCH | $1 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Erik Gustafsson: 1+ assists NO | 63 | 0.699 | 0.657 | +0.052 | +0.011 | $3.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (3.43 vs 1.48 bp); relationships: KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.088); KXNHLSPREAD-26OCT29OTTLA-OTT2|no: REINFORCING (phi 0.158); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: OTT offense succeeds (4+ goals)
- **Tim Stutzle: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no; why: second expression of the same thesis: KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no has the higher standalone adjusted growth (3.43 vs 1.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.088); they share one thesis budget; relationships: KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.088); KXNHLSPREAD-26OCT29OTTLA-OTT2|no: REINFORCING (phi 0.184); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: OTT offense succeeds (4+ goals)
- **Ottawa wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no; why: second expression of the same thesis: KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no has the higher standalone adjusted growth (1.48 vs 1.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.184); they share one thesis budget; relationships: KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: REINFORCING (phi 0.158); KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no: REINFORCING (phi 0.184); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: INTENTIONAL_DIVERSIFIER (phi -0.149); failure: OTT wins by 2+
- **Erik Gustafsson: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT29OTTLA-LAEGUSTAFSSON64-1|no; why: higher confidence-adjusted growth (1.07 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT29OTTLA-OTT2|no: INTENTIONAL_DIVERSIFIER (phi -0.149); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.08.
- thesis OTT:SUPPRESSED (p 0.4531): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [DIRECT], best adjusted EV KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS (p 0.5343): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.402): highest fidelity KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no (same contract)
- KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.8 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3288, phi -0.225)
- KXNHLAST-26OCT29OTTLA-OTTTSTUTZLE18-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3288, phi -0.29)
- KXNHLSPREAD-26OCT29OTTLA-OTT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2436, phi -1.0)
- KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3742, phi -0.245)

portfolios: A EV +1.59 (adj +0.32) on $14.60, P(profit) 0.6382, adj growth 3.0 bp · B EV +1.68 (adj +0.32) on $14.21, P(profit) 0.6382, adj growth 3.1 bp · C EV +2.04 (adj +0.37) on $14.65, P(profit) 0.6305, adj growth 3.5 bp · R EV +0.06 (adj +0.02) on $1.00, P(profit) 0.7564, adj growth 0.6 bp

## VAN @ SJS  ·  10000 joint draws  ·  404 bet sides mapped, 6 +EV candidates, 4 on card


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
| Dmitry Orlov: 1+ goals NO | 89 | 0.932 | 0.918 | +0.035 | +0.021 | $7.39 | FUNDED_RESEARCH | $2 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 60 | 0.720 | 0.635 | +0.103 | +0.019 | $4.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ goals NO | 70 | 0.806 | 0.731 | +0.091 | +0.016 | $5.57 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| San Jose wins by over 2.5 goals NO | 71 | 0.773 | 0.739 | +0.049 | +0.015 | $3.58 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dmitry Orlov: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.075); KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLSPREAD-26OCT29VANSJ-SJ3|no: MOSTLY_INDEPENDENT (phi 0.064); failure: SJS offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29VANSJ-SJ3|no; why: higher confidence-adjusted growth (3.23 vs 2.36 bp); relationships: KXNHLGOAL-26OCT29VANSJ-SJDORLOV9-1|no: MOSTLY_INDEPENDENT (phi 0.075); KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT29VANSJ-SJ3|no: REINFORCING (phi 0.166); failure: SJS offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no; why: second expression of the same thesis: KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no has the higher standalone adjusted growth (3.23 vs 2.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT29VANSJ-SJDORLOV9-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT29VANSJ-SJ3|no: MOSTLY_INDEPENDENT (phi 0.118); failure: SJS offense succeeds (4+ goals)
- **San Jose wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT29VANSJ-SJ5|no; why: higher confidence-adjusted growth (2.36 vs 1.25 bp); wins across more scripts (relative breadth 1.034 vs 0.918); relationships: KXNHLGOAL-26OCT29VANSJ-SJDORLOV9-1|no: MOSTLY_INDEPENDENT (phi 0.064); KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: REINFORCING (phi 0.166); KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.118); failure: SJS wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.3257): highest fidelity KXNHLSPREAD-26OCT29VANSJ-SJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT29VANSJ-SJ5|no less than the minimum stake; KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no kept
- thesis VAN:WINS (p 0.444): highest fidelity KXNHLSPREAD-26OCT29VANSJ-SJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29VANSJ-SJ3|no (same contract)
- KXNHLGOAL-26OCT29VANSJ-SJDORLOV9-1|no: FUNDED_RESEARCH; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4611, phi -0.1)
- KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.0 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4611, phi -0.248)
- KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.6 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4611, phi -0.199)
- KXNHLSPREAD-26OCT29VANSJ-SJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis SJS:WINS_BY_2PLUS (p 0.3397, phi -0.755)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT29VANSJ-SJ5|no less than the minimum stake; KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no kept

portfolios: A EV +1.58 (adj +0.33) on $14.60, P(profit) 0.6948, adj growth 3.1 bp · B EV +1.94 (adj +0.50) on $20.71, P(profit) 0.6904, adj growth 4.8 bp · C EV +1.88 (adj +0.57) on $23.17, P(profit) 0.5582, adj growth 5.4 bp · R EV +0.15 (adj +0.07) on $3.00, P(profit) 0.7274, adj growth 2.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
