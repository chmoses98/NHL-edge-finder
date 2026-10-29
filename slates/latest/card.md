# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-29T19:32:25Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +28.06 | +10.00 | +26.89 | 0.769 | -18.59 | -30.57 | 93.18 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +27.47 | +15.88 | +25.25 | 0.743 | -23.43 | -35.64 | 150.34 |
| C best expression per thesis | 149.04 | +27.73 | +14.34 | +24.40 | 0.690 | -33.99 | -47.94 | 130.67 |
| R FUNDED research stakes | 18.00 | +1.54 | +0.83 | +1.48 | 0.610 | -5.12 | -7.26 | 0.00 |

## WPG @ TBL  ·  10000 joint draws  ·  424 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.655 / away 0.345

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
| Charle-Edouard D'Astous: 1+ goals NO | 89 | 0.929 | 0.918 | +0.032 | +0.021 | $8.35 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ assists NO | 41 | 0.498 | 0.449 | +0.071 | +0.022 | $3.72 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.72) | EVIDENCE_MIXED | D |
| Adam Lowry: 1+ goals YES | 9 | 0.118 | 0.109 | +0.022 | +0.013 | $1.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 25 | 0.290 | 0.279 | +0.027 | +0.016 | $2.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (10.50 vs 4.33 bp); despite a smaller raw edge (+0.032 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.073); KXNHLGOAL-26OCT29WPGTB-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT29WPGTB-TB2|no; why: higher confidence-adjusted growth (4.33 vs 2.34 bp); wins across more scripts (relative breadth 0.99 vs 0.58); relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.073); KXNHLGOAL-26OCT29WPGTB-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: TBL offense succeeds (4+ goals)
- **Adam Lowry: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (4.16 vs 2.74 bp); despite a smaller raw edge (+0.022 vs +0.027/contract); relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (2.74 vs 0.74 bp); alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT29WPGTB-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:SUPPRESSED (p 0.3355): highest fidelity KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.2594): highest fidelity KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes (same contract)
- thesis WPG:SUPPRESSED (p 0.535): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4503, phi -0.108)
- KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 28% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4503, phi -0.307)
- KXNHLGOAL-26OCT29WPGTB-WPGALOWRY17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.535, phi -0.165)
- KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.535, phi -0.296)

portfolios: A EV +1.74 (adj +0.57) on $15.25, P(profit) 0.5191, adj growth 5.2 bp · B EV +1.45 (adj +0.69) on $15.53, P(profit) 0.6496, adj growth 6.6 bp · C EV +1.32 (adj +0.50) on $9.20, P(profit) 0.6419, adj growth 4.6 bp · R EV +0.11 (adj +0.07) on $3.00, P(profit) 0.9286, adj growth 2.7 bp

## UTA @ PIT  ·  10000 joint draws  ·  422 bet sides mapped, 17 +EV candidates, 4 on card

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
| Nick Robertson: 1+ goals YES | 16 | 0.251 | 0.227 | +0.082 | +0.058 | $5.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 14 | 0.223 | 0.201 | +0.074 | +0.052 | $4.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 9 | 0.154 | 0.137 | +0.059 | +0.041 | $3.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 65 | 0.689 | 0.678 | +0.023 | +0.012 | $3.61 | FUNDED_RESEARCH | $1 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Nick Robertson: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (49.87 vs 45.74 bp); relationships: KXNHLGOAL-26OCT29UTAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes has the higher standalone adjusted growth (49.87 vs 45.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes has the higher standalone adjusted growth (49.87 vs 40.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29UTAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: PIT offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29UTAPIT-UTA2|no; why: higher confidence-adjusted growth (1.40 vs 0.64 bp); despite a smaller raw edge (+0.023 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT29UTAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4347): highest fidelity KXNHLAST-26OCT29UTAPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.3547): highest fidelity KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no (same contract)
- KXNHLGOAL-26OCT29UTAPIT-PITNROBERTSON14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.217)
- KXNHLGOAL-26OCT29UTAPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.217)
- KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.195)
- KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4353, phi -0.246)

portfolios: A EV +6.02 (adj +3.04) on $15.25, P(profit) 0.5189, adj growth 28.9 bp · B EV +6.63 (adj +4.65) on $16.13, P(profit) 0.5032, adj growth 44.1 bp · C EV +4.98 (adj +3.48) on $15.72, P(profit) 0.2509, adj growth 31.5 bp · R EV +0.03 (adj +0.02) on $1.00, P(profit) 0.6888, adj growth 0.7 bp

## CBJ @ CAR  ·  10000 joint draws  ·  446 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.687 / away 0.313

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
| Charlie Coyle: 1+ goals YES | 17 | 0.258 | 0.234 | +0.078 | +0.055 | $4.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.185 | 0.170 | +0.047 | +0.032 | $2.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Seth Jarvis: 1+ goals NO | 70 | 0.751 | 0.737 | +0.036 | +0.022 | $6.09 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 73 | 0.778 | 0.765 | +0.035 | +0.021 | $6.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (43.09 vs 18.34 bp); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (43.09 vs 18.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Seth Jarvis: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CAR2|no; why: KXNHLSPREAD-26OCT29CBJCAR-CAR2|no has the higher standalone adjusted growth (5.67 vs 5.44 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.163); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: CAR offense succeeds (4+ goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CAR2|no; why: Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSAHO20-1|no because adjusted EV is 0.8 pts higher while thesis capture is 0.89 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.3293): highest fidelity KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.2133): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS (p 0.4315): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4607, phi -0.265)
- KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4607, phi -0.225)
- KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4247, phi -0.212)
- KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4247, phi -0.215)
- override: Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARNEHLERS27-1|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSAHO20-1|no because adjusted EV is 0.8 pts higher while thesis capture is 0.89 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.13 (adj +0.59) on $15.25, P(profit) 0.5736, adj growth 5.3 bp · B EV +3.61 (adj +2.47) on $20.04, P(profit) 0.3848, adj growth 23.5 bp · C EV +5.17 (adj +3.07) on $14.86, P(profit) 0.2577, adj growth 27.9 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7512, adj growth 2.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT29CBJCAR-CBJ|yes == KXNHLGAME-26OCT29CBJCAR-CAR|no

## CHI @ DET  ·  10000 joint draws  ·  428 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_CHI_win | p_overtime | goals | shots DET/CHI | DET/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.138 | 0.70 | 0.30 | 0.00 | 5.99 | 33.2/21.0 | 18.5/28.5 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.126 | 0.55 | 0.45 | 0.50 | 5.93 | 33.4/21.4 | 18.2/30.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.64 | 0.36 | 0.00 | 5.99 | 27.3/26.6 | 23.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.52 | 0.48 | 0.46 | 5.88 | 27.7/26.8 | 23.6/24.5 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.083 | 0.73 | 0.27 | 0.00 | 9.21 | 34.8/22.5 | 18.2/26.7 | even strength |
| DET shot control · low event (<=4) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 3.44 | 31.5/19.9 | 18.6/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Patrick Kane: 1+ assists NO | 58 | 0.715 | 0.621 | +0.118 | +0.024 | $7.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Andrew Copp: 1+ goals YES | 18 | 0.216 | 0.206 | +0.026 | +0.015 | $1.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Anton Frondell: 1+ goals YES | 16 | 0.198 | 0.183 | +0.028 | +0.014 | $1.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 41 | 0.451 | 0.439 | +0.024 | +0.012 | $2.23 | FUNDED_RESEARCH | $1 | DET:OFFENSE_4PLUS | DIRECT (0.63) | EVIDENCE_STRONGER | D |
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CHIDET-CHI2|no; why: higher confidence-adjusted growth (5.07 vs 0.35 bp); alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29CHIDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT29CHIDET-CHIAFRONDELL16-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.061); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: CHI offense succeeds (4+ goals)
- **Andrew Copp: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-2|yes; why: KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-2|yes has the higher standalone adjusted growth (8.88 vs 3.32 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.003); relationships: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT29CHIDET-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: DET offense suppressed (<= 2 goals)
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (2.94 vs 1.21 bp); relationships: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.061); KXNHLGOAL-26OCT29CHIDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CHI offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-2|yes; why: Player prop expression KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-2|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.63 vs 0.24 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT29CHIDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT29CHIDET-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.14, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis DET:OFFENSE_4PLUS (p 0.4373): highest fidelity KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-2|yes — Player prop expression KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-2|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.63 vs 0.24 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis CHI:SUPPRESSED (p 0.4966): highest fidelity KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.2834): highest fidelity KXNHLGOAL-26OCT29CHIDET-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29CHIDET-CHIAFRONDELL16-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.5 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2834, phi -0.259)
- KXNHLGOAL-26OCT29CHIDET-DETACOPP18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3444, phi -0.202)
- KXNHLGOAL-26OCT29CHIDET-CHIAFRONDELL16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4966, phi -0.235)
- KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 37% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3444, phi -0.317)
- override: Player prop expression KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-2|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.63 vs 0.24 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +2.68 (adj +0.87) on $15.25, P(profit) 0.6724, adj growth 8.1 bp · B EV +2.07 (adj +0.64) on $12.96, P(profit) 0.5222, adj growth 6.1 bp · C EV +4.27 (adj +1.43) on $23.18, P(profit) 0.6005, adj growth 13.1 bp · R EV +0.06 (adj +0.03) on $1.00, P(profit) 0.4508, adj growth 1.1 bp

## BOS @ STL  ·  10000 joint draws  ·  440 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.503 / away 0.497

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_BOS_win | p_overtime | goals | shots STL/BOS | STL/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.54 | 0.46 | 0.00 | 5.98 | 27.2/26.9 | 23.5/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.49 | 0.51 | 0.47 | 5.97 | 27.3/27.1 | 23.7/24.0 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.089 | 0.61 | 0.39 | 0.00 | 5.98 | 32.3/21.5 | 18.6/28.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.51 | 0.49 | 0.00 | 9.35 | 29.0/28.6 | 22.7/22.5 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.55 | 0.45 | 0.45 | 5.92 | 32.5/21.6 | 18.4/29.2 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.061 | 0.63 | 0.37 | 0.00 | 9.29 | 34.1/23.0 | 18.0/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Casey Mittelstadt: 1+ goals YES | 14 | 0.179 | 0.167 | +0.030 | +0.018 | $2.11 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 24 | 0.282 | 0.271 | +0.030 | +0.018 | $2.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 29 | 0.331 | 0.319 | +0.026 | +0.015 | $2.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT29BOSSTL-9|yes; why: higher confidence-adjusted growth (5.60 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.916 vs 0.374); alternative not eligible: confidence-adjusted EV +0.0010 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: BOS offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (3.67 vs 2.23 bp); relationships: KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (3.67 vs 2.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.4127): highest fidelity KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.3665): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4158, phi -0.197)
- KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3698, phi -0.252)
- KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3698, phi -0.282)

portfolios: A EV +1.15 (adj +0.68) on $8.60, P(profit) 0.6064, adj growth 6.3 bp · B EV +0.90 (adj +0.53) on $6.68, P(profit) 0.6064, adj growth 5.0 bp · C EV +0.43 (adj +0.26) on $3.69, P(profit) 0.2825, adj growth 2.4 bp · R EV +0.20 (adj +0.12) on $1.00, P(profit) 0.1787, adj growth 4.3 bp

## WSH @ NSH  ·  10000 joint draws  ·  428 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.498 / away 0.502

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
| Aliaksei Protas: 1+ goals YES | 17 | 0.223 | 0.209 | +0.043 | +0.029 | $3.83 | FUNDED_RESEARCH | $1 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Adam Wilsby: 1+ goals YES | 5 | 0.076 | 0.068 | +0.022 | +0.015 | $1.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Washington wins by over 1.5 goals NO | 70 | 0.758 | 0.726 | +0.043 | +0.012 | $7.31 | FUNDED_RESEARCH | $2 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mavrik Bourque: 1+ assists NO | 75 | 0.807 | 0.773 | +0.044 | +0.010 | $6.50 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-WSHAOVECHKIN8-1|yes; why: higher confidence-adjusted growth (12.22 vs 0.26 bp); alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WSHNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT29WSHNSH-WSH2|no: INTENTIONAL_DIVERSIFIER (phi -0.195); KXNHLAST-26OCT29WSHNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: WSH offense suppressed (<= 2 goals)
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (9.18 vs 2.44 bp); despite a smaller raw edge (+0.022 vs +0.027/contract); relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT29WSHNSH-WSH2|no: MOSTLY_INDEPENDENT (phi 0.063); KXNHLAST-26OCT29WSHNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.038); failure: NSH offense suppressed (<= 2 goals)
- **Washington wins by over 1.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29WSHNSH-WSH3|no; why: higher confidence-adjusted growth (1.46 vs 0.30 bp); alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.195); KXNHLGOAL-26OCT29WSHNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.063); KXNHLAST-26OCT29WSHNSH-NSHMBOURQUE22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.131); failure: WSH wins by 2+
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT29WSHNSH-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (1.32 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT29WSHNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLSPREAD-26OCT29WSHNSH-WSH2|no: INTENTIONAL_DIVERSIFIER (phi -0.131); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.3679): highest fidelity KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.4437): highest fidelity KXNHLSPREAD-26OCT29WSHNSH-WSH2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS (p 0.5524): highest fidelity KXNHLSPREAD-26OCT29WSHNSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29WSHNSH-WSH2|no (same contract)
- KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4126, phi -0.235)
- KXNHLGOAL-26OCT29WSHNSH-NSHAWILSBY2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3418, phi -0.1)
- KXNHLSPREAD-26OCT29WSHNSH-WSH2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.2423, phi -1.0)
- KXNHLAST-26OCT29WSHNSH-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.4437, phi -0.199)

portfolios: A EV +1.56 (adj +0.78) on $15.25, P(profit) 0.3958, adj growth 7.4 bp · B EV +2.34 (adj +1.21) on $19.05, P(profit) 0.283, adj growth 11.4 bp · C EV +2.22 (adj +1.23) on $18.16, P(profit) 0.4568, adj growth 11.2 bp · R EV +0.36 (adj +0.19) on $3.00, P(profit) 0.2234, adj growth 7.3 bp

## MTL @ DAL  ·  10000 joint draws  ·  422 bet sides mapped, 2 +EV candidates, 2 on card

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

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Chris Kreider: 1+ goals YES | 16 | 0.195 | 0.184 | +0.025 | +0.014 | $1.70 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Alexandre Texier: 1+ goals YES | 11 | 0.138 | 0.127 | +0.021 | +0.011 | $1.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Chris Kreider: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29MTLDAL-MTLJANDERSON17-1|yes; why: higher confidence-adjusted growth (3.11 vs 1.46 bp); alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29MTLDAL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: MTL offense suppressed (<= 2 goals)
- **Alexandre Texier: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29MTLDAL-MTLCKREIDER22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29MTLDAL-MTLCKREIDER22-1|yes has the higher standalone adjusted growth (3.11 vs 2.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT29MTLDAL-MTLCKREIDER22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts DAL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis MTL:OFFENSE_4PLUS (p 0.3288): highest fidelity KXNHLGOAL-26OCT29MTLDAL-MTLCKREIDER22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29MTLDAL-MTLCKREIDER22-1|yes (same contract)
- KXNHLGOAL-26OCT29MTLDAL-MTLCKREIDER22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.4565, phi -0.206)
- KXNHLGOAL-26OCT29MTLDAL-MTLATEXIER85-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.4565, phi -0.186)

portfolios: A EV +0.69 (adj +0.36) on $4.17, P(profit) 0.3069, adj growth 3.3 bp · B EV +0.47 (adj +0.25) on $2.86, P(profit) 0.3069, adj growth 2.3 bp · C EV +0.39 (adj +0.22) on $2.58, P(profit) 0.1948, adj growth 2.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ MIN  ·  10000 joint draws  ·  446 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.631 / away 0.369

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_NYI_win | p_overtime | goals | shots MIN/NYI | MIN/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.59 | 0.41 | 0.00 | 5.96 | 28.1/27.9 | 24.8/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.46 | 5.9 | 28.3/28.2 | 25.0/25.1 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.087 | 0.64 | 0.36 | 0.00 | 5.97 | 33.2/22.3 | 19.6/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.57 | 0.43 | 0.00 | 9.23 | 29.7/29.4 | 23.8/23.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.57 | 0.43 | 0.48 | 5.84 | 33.6/22.8 | 19.6/30.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.59 | 0.41 | 0.00 | 3.46 | 26.9/26.7 | 25.2/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden Schenn: 1+ goals YES | 18 | 0.254 | 0.230 | +0.064 | +0.040 | $4.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Adam Pelech: 1+ goals YES | 3 | 0.056 | 0.048 | +0.024 | +0.016 | $1.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 54 | 0.614 | 0.593 | +0.057 | +0.036 | $8.32 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Anthony Duclair: 1+ goals YES | 12 | 0.162 | 0.149 | +0.034 | +0.021 | $2.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes; why: higher confidence-adjusted growth (22.39 vs 5.35 bp); despite a smaller raw edge (+0.064 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29NYIMIN-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT29NYIMIN-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: NYI offense suppressed (<= 2 goals)
- **Adam Pelech: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (22.39 vs 17.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT29NYIMIN-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: NYI offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-2|no; why: higher confidence-adjusted growth (11.36 vs 4.56 bp); relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT29NYIMIN-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT29NYIMIN-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense succeeds (4+ goals)
- **Anthony Duclair: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (22.39 vs 8.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29NYIMIN-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:OFFENSE_4PLUS (p 0.3313): highest fidelity KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3716): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.4437): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29NYIMIN-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4536, phi -0.244)
- KXNHLGOAL-26OCT29NYIMIN-NYIAPELECH3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4536, phi -0.111)
- KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4048, phi -0.296)
- KXNHLGOAL-26OCT29NYIMIN-NYIADUCLAIR11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4536, phi -0.179)

portfolios: A EV +2.99 (adj +1.43) on $15.25, P(profit) 0.4581, adj growth 13.2 bp · B EV +4.09 (adj +2.62) on $16.77, P(profit) 0.4112, adj growth 24.7 bp · C EV +3.69 (adj +2.33) on $19.89, P(profit) 0.7111, adj growth 21.3 bp · R EV +0.31 (adj +0.19) on $3.00, P(profit) 0.6142, adj growth 7.1 bp

## BUF @ ANA  ·  10000 joint draws  ·  454 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.441 / away 0.559

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BUF_win | p_overtime | goals | shots ANA/BUF | ANA/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.60 | 0.40 | 0.00 | 6.04 | 28.1/27.8 | 24.6/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.52 | 0.48 | 0.46 | 5.96 | 28.4/28.4 | 25.0/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.59 | 0.41 | 0.00 | 9.48 | 30.0/29.8 | 24.2/23.0 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.080 | 0.61 | 0.39 | 0.00 | 6.04 | 33.2/22.1 | 19.3/28.9 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.57 | 0.43 | 0.44 | 5.98 | 33.2/22.6 | 19.5/29.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.065 | 0.63 | 0.37 | 0.00 | 9.38 | 34.9/23.7 | 18.8/27.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Washe: 1+ goals YES | 11 | 0.166 | 0.147 | +0.049 | +0.030 | $3.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 12 | 0.160 | 0.146 | +0.032 | +0.019 | $2.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 18 | 0.225 | 0.209 | +0.035 | +0.018 | $2.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 63 | 0.683 | 0.667 | +0.036 | +0.021 | $6.26 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: higher confidence-adjusted growth (18.50 vs 9.43 bp); despite a smaller raw edge (+0.049 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.869 vs 0.52); relationships: KXNHLGOAL-26OCT29BUFANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (9.43 vs 6.79 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.112); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (9.43 vs 4.73 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.146); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT29BUFANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: ANA offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (9.43 vs 4.15 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.150); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT29BUFANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4724): highest fidelity KXNHLTEAMTOTAL-26OCT29BUFANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3393): highest fidelity KXNHLSPREAD-26OCT29BUFANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes (same contract)
- thesis ANA:WINS (p 0.5661): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3183, phi -0.181)
- KXNHLGOAL-26OCT29BUFANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3183, phi -0.15)
- KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3183, phi -0.194)
- KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3801, phi -0.236)

portfolios: A EV +4.46 (adj +0.79) on $15.25, P(profit) 0.6409, adj growth 7.0 bp · B EV +2.63 (adj +1.54) on $13.87, P(profit) 0.4088, adj growth 14.5 bp · C EV +1.64 (adj +0.63) on $5.68, P(profit) 0.3393, adj growth 5.7 bp · R EV +0.11 (adj +0.06) on $2.00, P(profit) 0.6828, adj growth 2.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT29BUFANA-BUF|no == KXNHLGAME-26OCT29BUFANA-ANA|yes

## OTT @ LAK  ·  10000 joint draws  ·  434 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.478 / away 0.522

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_OTT_win | p_overtime | goals | shots LAK/OTT | LAK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.57 | 0.43 | 0.00 | 5.99 | 27.0/27.3 | 24.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.46 | 5.91 | 26.8/27.1 | 23.8/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.57 | 0.43 | 0.00 | 9.25 | 28.6/28.6 | 22.9/22.4 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.074 | 0.50 | 0.50 | 0.00 | 5.96 | 21.2/31.9 | 28.4/17.9 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.48 | 0.52 | 0.45 | 5.79 | 21.6/32.1 | 28.8/18.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.50 | 0.50 | 0.52 | 2.82 | 25.5/25.6 | 24.1/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.075 | 0.067 | +0.022 | +0.013 | $1.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Jonas Johansson: 25+ saves NO | 53 | 0.618 | 0.572 | +0.071 | +0.024 | $5.20 | FUNDED_RESEARCH | $2 | OTT:NET_LOW_VOLUME | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Drake Batherson: 1+ goals NO | 69 | 0.733 | 0.721 | +0.028 | +0.016 | $5.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Scott Laughton: 1+ goals YES | 12 | 0.150 | 0.139 | +0.022 | +0.011 | $1.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes; why: higher confidence-adjusted growth (7.38 vs 2.48 bp); despite a smaller raw edge (+0.022 vs +0.022/contract); relationships: KXNHLSAVE-26OCT29OTTLA-OTTJJOHANSSON31-25|no: MOSTLY_INDEPENDENT (phi 0.041); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: LAK offense suppressed (<= 2 goals)
- **Jonas Johansson: 25+ saves NO** — thesis: OTT net faces light volume (<= 25 shots; LAK suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.041); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.039); KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.041); failure: OTT net faces heavy volume (33+ shots; LAK pressure)
- **Drake Batherson: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT3|no; why: higher confidence-adjusted growth (2.74 vs 2.17 bp); despite a smaller raw edge (+0.028 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSAVE-26OCT29OTTLA-OTTJJOHANSSON31-25|no: MOSTLY_INDEPENDENT (phi 0.039); KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: OTT offense succeeds (4+ goals)
- **Scott Laughton: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT3|no; why: higher confidence-adjusted growth (2.48 vs 2.17 bp); despite a smaller raw edge (+0.022 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSAVE-26OCT29OTTLA-OTTJJOHANSSON31-25|no: MOSTLY_INDEPENDENT (phi 0.041); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis OTT:NET_LOW_VOLUME (p 0.4654): highest fidelity KXNHLSAVE-26OCT29OTTLA-OTTJJOHANSSON31-25|no [DIRECT], best adjusted EV KXNHLSAVE-26OCT29OTTLA-OTTJJOHANSSON31-25|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4553): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.3832): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT29OTTLA-OTT3|no (same contract)
- KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4032, phi -0.134)
- KXNHLSAVE-26OCT29OTTLA-OTTJJOHANSSON31-25|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:NET_HIGH_VOLUME (p 0.1456, phi -0.467)
- KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3242, phi -0.249)
- KXNHLGOAL-26OCT29OTTLA-LASLAUGHTON21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4032, phi -0.202)

portfolios: A EV +1.51 (adj +0.36) on $15.25, P(profit) 0.7187, adj growth 3.4 bp · B EV +1.59 (adj +0.76) on $12.94, P(profit) 0.556, adj growth 7.1 bp · C EV +2.01 (adj +0.79) on $25.09, P(profit) 0.4822, adj growth 7.3 bp · R EV +0.26 (adj +0.09) on $2.00, P(profit) 0.6184, adj growth 3.3 bp

## VAN @ SJS  ·  10000 joint draws  ·  420 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.609 / away 0.391

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_VAN_win | p_overtime | goals | shots SJS/VAN | SJS/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.58 | 0.42 | 0.00 | 6.06 | 27.9/27.3 | 24.2/24.0 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.109 | 0.63 | 0.37 | 0.00 | 6.04 | 33.0/21.7 | 18.9/28.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.57 | 0.43 | 0.00 | 9.42 | 29.6/29.1 | 23.3/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.51 | 0.49 | 0.47 | 6.0 | 27.7/27.4 | 24.2/24.4 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.56 | 0.44 | 0.47 | 5.96 | 33.1/21.7 | 18.5/29.7 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.086 | 0.69 | 0.31 | 0.00 | 9.37 | 34.5/22.9 | 18.1/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Marco Rossi: 1+ goals YES | 18 | 0.218 | 0.205 | +0.028 | +0.015 | $1.78 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ goals NO | 71 | 0.807 | 0.741 | +0.083 | +0.016 | $7.67 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 19 | 0.227 | 0.214 | +0.026 | +0.013 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Tyler Toffoli: 1+ assists YES | 28 | 0.342 | 0.309 | +0.048 | +0.015 | $2.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (2.99 vs 2.24 bp); relationships: KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: VAN offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (2.92 vs 1.05 bp); despite a smaller raw edge (+0.083 vs +0.089/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi -0.048); failure: SJS offense succeeds (4+ goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29VANSJ-SJ3|no; why: higher confidence-adjusted growth (2.24 vs 0.56 bp); despite a smaller raw edge (+0.026 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: VAN offense suppressed (<= 2 goals)
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT29VANSJ-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (2.23 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.048); KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3799): highest fidelity KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.4738): highest fidelity KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3162): highest fidelity KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no (same contract)
- KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3976, phi -0.201)
- KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.2 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4738, phi -0.181)
- KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3976, phi -0.202)
- KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3162, phi -0.263)

portfolios: A EV +2.13 (adj +0.53) on $15.25, P(profit) 0.4588, adj growth 4.9 bp · B EV +1.69 (adj +0.52) on $13.17, P(profit) 0.5155, adj growth 4.9 bp · C EV +1.60 (adj +0.40) on $10.99, P(profit) 0.411, adj growth 3.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
