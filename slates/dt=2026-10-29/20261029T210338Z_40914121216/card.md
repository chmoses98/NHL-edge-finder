# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-29T21:03:38Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +28.71 | +9.98 | +27.49 | 0.770 | -18.90 | -31.13 | 92.68 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +29.22 | +15.99 | +27.18 | 0.745 | -22.86 | -35.44 | 151.02 |
| C best expression per thesis | 150.00 | +26.01 | +12.27 | +22.83 | 0.694 | -29.63 | -41.68 | 112.24 |
| R FUNDED research stakes | 16.00 | +1.46 | +0.86 | +0.98 | 0.583 | -4.58 | -6.08 | 0.00 |

## WPG @ TBL  ·  10000 joint draws  ·  424 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.657 / away 0.343

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
| Charle-Edouard D'Astous: 1+ goals NO | 88 | 0.929 | 0.915 | +0.041 | +0.028 | $8.56 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Adam Lowry: 1+ goals YES | 9 | 0.118 | 0.110 | +0.022 | +0.014 | $1.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 11 | 0.139 | 0.129 | +0.022 | +0.013 | $1.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Elias Salomonsson: 1+ assists NO | 77 | 0.825 | 0.795 | +0.043 | +0.013 | $7.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (17.38 vs 1.93 bp); despite a smaller raw edge (+0.041 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29WPGTB-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT29WPGTB-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: TBL offense succeeds (4+ goals)
- **Adam Lowry: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (4.99 vs 0.99 bp); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT29WPGTB-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi -0.026); failure: WPG offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (3.30 vs 0.99 bp); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29WPGTB-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT29WPGTB-WPGESALOMONSSON57-1|no: MOSTLY_INDEPENDENT (phi -0.046); failure: WPG offense suppressed (<= 2 goals)
- **Elias Salomonsson: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT29WPGTB-4|no; why: higher confidence-adjusted growth (2.10 vs 0.15 bp); wins across more scripts (relative breadth 0.985 vs 0.355); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29WPGTB-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.046); failure: WPG offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:SUPPRESSED (p 0.3355): highest fidelity KXNHLAST-26OCT29WPGTB-TBJCARLSON74-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29WPGTB-TBNKUCHEROV86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:SUPPRESSED (p 0.535): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis WPG:OFFENSE_4PLUS (p 0.2594): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29WPGTB-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4503, phi -0.108)
- KXNHLGOAL-26OCT29WPGTB-WPGALOWRY17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.535, phi -0.165)
- KXNHLGOAL-26OCT29WPGTB-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.535, phi -0.192)
- KXNHLAST-26OCT29WPGTB-WPGESALOMONSSON57-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.2594, phi -0.173)

portfolios: A EV +1.55 (adj +0.41) on $15.45, P(profit) 0.4671, adj growth 3.9 bp · B EV +1.47 (adj +0.78) on $19.26, P(profit) 0.8246, adj growth 7.5 bp · C EV +0.84 (adj +0.14) on $3.76, P(profit) 0.4979, adj growth 1.2 bp · R EV +0.14 (adj +0.09) on $3.00, P(profit) 0.9286, adj growth 3.7 bp

## UTA @ PIT  ·  10000 joint draws  ·  422 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.447 / away 0.553

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
| Hendrix Lapierre: 1+ goals YES | 11 | 0.183 | 0.163 | +0.066 | +0.047 | $4.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 14 | 0.223 | 0.199 | +0.074 | +0.051 | $4.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 9 | 0.154 | 0.137 | +0.059 | +0.041 | $3.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 65 | 0.689 | 0.677 | +0.023 | +0.011 | $3.18 | FUNDED_RESEARCH | $1 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Hendrix Lapierre: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (44.20 vs 43.61 bp); despite a smaller raw edge (+0.066 vs +0.074/contract); relationships: KXNHLGOAL-26OCT29UTAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (43.61 vs 40.99 bp); relationships: KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29UTAPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (43.61 vs 40.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT29UTAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: PIT offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29UTAPIT-UTAVTROCHECK16-1|no; why: Player prop expression KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no selected over player prop KXNHLAST-26OCT29UTAPIT-UTAVTROCHECK16-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.84 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT29UTAPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4347): highest fidelity KXNHLAST-26OCT29UTAPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.3547): highest fidelity KXNHLAST-26OCT29UTAPIT-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29UTAPIT-UTAVTROCHECK16-1|no (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.4353): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29UTAPIT-PITHLAPIERRE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.176)
- KXNHLGOAL-26OCT29UTAPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.217)
- KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3459, phi -0.195)
- KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4353, phi -0.246)
- override: Player prop expression KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no selected over player prop KXNHLAST-26OCT29UTAPIT-UTAVTROCHECK16-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.84 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.10 (adj +3.40) on $15.45, P(profit) 0.5241, adj growth 32.0 bp · B EV +7.21 (adj +5.02) on $16.03, P(profit) 0.4622, adj growth 47.2 bp · C EV +5.13 (adj +3.20) on $19.24, P(profit) 0.2226, adj growth 29.0 bp · R EV +0.03 (adj +0.02) on $1.00, P(profit) 0.6888, adj growth 0.6 bp

## CBJ @ CAR  ·  10000 joint draws  ·  446 bet sides mapped, 24 +EV candidates, 4 on card

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
| Charlie Coyle: 1+ goals YES | 17 | 0.258 | 0.234 | +0.078 | +0.055 | $4.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.185 | 0.170 | +0.047 | +0.032 | $2.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 66 | 0.722 | 0.705 | +0.046 | +0.029 | $6.63 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Seth Jarvis: 1+ goals NO | 70 | 0.751 | 0.737 | +0.036 | +0.022 | $6.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (43.09 vs 18.34 bp); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (43.09 vs 18.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: CBJ offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CAR2|no; why: higher confidence-adjusted growth (8.72 vs 5.67 bp); despite a smaller raw edge (+0.046 vs +0.114/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.998 vs 0.885); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: CAR offense succeeds (4+ goals)
- **Seth Jarvis: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no; why: Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSGOSTISBEHERE4-1|no because adjusted EV is 0.5 pts higher while thesis capture is 0.88 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.3293): highest fidelity KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.3571): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no — Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSGOSTISBEHERE4-1|no because adjusted EV is 0.5 pts higher while thesis capture is 0.88 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis CBJ:WINS_BY_2PLUS (p 0.2133): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4607, phi -0.265)
- KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4607, phi -0.225)
- KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4247, phi -0.214)
- KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4247, phi -0.212)
- override: Player prop expression KXNHLGOAL-26OCT29CBJCAR-CARSJARVIS24-1|no selected over player prop KXNHLAST-26OCT29CBJCAR-CARSGOSTISBEHERE4-1|no because adjusted EV is 0.5 pts higher while thesis capture is 0.88 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.17 (adj +0.60) on $15.45, P(profit) 0.5736, adj growth 5.4 bp · B EV +3.83 (adj +2.61) on $20.49, P(profit) 0.3832, adj growth 24.9 bp · C EV +5.90 (adj +3.61) on $27.29, P(profit) 0.4827, adj growth 33.0 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.7219, adj growth 3.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT29CBJCAR-CBJ|yes == KXNHLGAME-26OCT29CBJCAR-CAR|no

## CHI @ DET  ·  10000 joint draws  ·  428 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.586 / away 0.414

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
| Patrick Kane: 1+ assists NO | 57 | 0.715 | 0.617 | +0.128 | +0.030 | $8.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Lucas Raymond: 1+ assists NO | 53 | 0.610 | 0.568 | +0.063 | +0.020 | $5.88 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
| Alex DeBrincat: 2+ goals YES | 10 | 0.128 | 0.117 | +0.022 | +0.011 | $1.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 41 | 0.451 | 0.439 | +0.024 | +0.012 | $1.82 | FUNDED_RESEARCH | $1 | DET:OFFENSE_4PLUS | DIRECT (0.63) | EVIDENCE_STRONGER | D |
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29CHIDET-CHIRKANTSEROV80-1|no; why: higher confidence-adjusted growth (8.27 vs 0.72 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLAST-26OCT29CHIDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-2|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: CHI offense succeeds (4+ goals)
- **Lucas Raymond: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT29CHIDET-DETLRAYMOND23-1|no; why: higher confidence-adjusted growth (3.59 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-2|yes: INTENTIONAL_DIVERSIFIER (phi -0.148); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.178); failure: DET offense succeeds (4+ goals)
- **Alex DeBrincat: 2+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT29CHIDET-DETEFINNIE58-1|yes; why: KXNHLAST-26OCT29CHIDET-DETEFINNIE58-1|yes has the higher standalone adjusted growth (3.17 vs 2.69 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.171); relationships: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT29CHIDET-DETLRAYMOND23-1|no: INTENTIONAL_DIVERSIFIER (phi -0.148); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: DUPLICATIVE (phi 0.423); failure: DET offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT29CHIDET-DETEFINNIE58-1|yes; why: Player prop expression KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT29CHIDET-DETJCOMPHER37-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.63 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT29CHIDET-DETLRAYMOND23-1|no: INTENTIONAL_DIVERSIFIER (phi -0.178); KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-2|yes: DUPLICATIVE (phi 0.423); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.14, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:SUPPRESSED (p 0.4966): highest fidelity KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no (same contract)
- thesis DET:SUPPRESSED (p 0.3444): highest fidelity KXNHLAST-26OCT29CHIDET-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29CHIDET-DETLRAYMOND23-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.4373): highest fidelity KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT29CHIDET-DETEFINNIE58-1|yes — Player prop expression KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT29CHIDET-DETJCOMPHER37-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.63 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.0 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2834, phi -0.259)
- KXNHLAST-26OCT29CHIDET-DETLRAYMOND23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.4373, phi -0.266)
- KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3444, phi -0.237)
- KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 37% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3444, phi -0.317)
- override: Player prop expression KXNHLGOAL-26OCT29CHIDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT29CHIDET-DETJCOMPHER37-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.63 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +2.56 (adj +0.82) on $15.45, P(profit) 0.681, adj growth 7.8 bp · B EV +2.86 (adj +0.82) on $17.38, P(profit) 0.6079, adj growth 7.8 bp · C EV +4.58 (adj +1.28) on $27.38, P(profit) 0.6171, adj growth 11.8 bp · R EV +0.06 (adj +0.03) on $1.00, P(profit) 0.4508, adj growth 1.1 bp

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
| Casey Mittelstadt: 1+ goals YES | 14 | 0.179 | 0.167 | +0.030 | +0.018 | $2.16 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 24 | 0.282 | 0.271 | +0.030 | +0.018 | $2.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 29 | 0.331 | 0.319 | +0.026 | +0.015 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT29BOSSTL-3|yes; why: higher confidence-adjusted growth (5.60 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.916 vs 0.763); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: BOS offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (3.67 vs 2.23 bp); relationships: KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (3.67 vs 2.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.4127): highest fidelity KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.3665): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29BOSSTL-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4158, phi -0.197)
- KXNHLGOAL-26OCT29BOSSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3698, phi -0.252)
- KXNHLGOAL-26OCT29BOSSTL-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3698, phi -0.282)

portfolios: A EV +1.17 (adj +0.69) on $8.72, P(profit) 0.6064, adj growth 6.4 bp · B EV +0.92 (adj +0.55) on $6.85, P(profit) 0.6064, adj growth 5.1 bp · C EV +0.43 (adj +0.26) on $3.67, P(profit) 0.2825, adj growth 2.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ NSH  ·  10000 joint draws  ·  428 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

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
| Aliaksei Protas: 1+ goals YES | 17 | 0.223 | 0.209 | +0.043 | +0.029 | $3.59 | FUNDED_RESEARCH | $1 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Adam Wilsby: 1+ goals YES | 5 | 0.076 | 0.068 | +0.022 | +0.015 | $1.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 14 | 0.171 | 0.161 | +0.023 | +0.012 | $1.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 29 | 0.331 | 0.320 | +0.027 | +0.015 | $2.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (12.22 vs 0.27 bp); alternative not eligible: confidence-adjusted EV +0.0044 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WSHNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: WSH offense suppressed (<= 2 goals)
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes; why: higher confidence-adjusted growth (9.18 vs 2.64 bp); despite a smaller raw edge (+0.022 vs +0.023/contract); relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: NSH offense suppressed (<= 2 goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (2.64 vs 2.44 bp); despite a smaller raw edge (+0.023 vs +0.027/contract); relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT29WSHNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: NSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (2.64 vs 2.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT29WSHNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.3679): highest fidelity KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.4437): highest fidelity KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes (same contract)
- thesis NSH:SUPPRESSED (p 0.3418): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29WSHNSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4126, phi -0.235)
- KXNHLGOAL-26OCT29WSHNSH-NSHAWILSBY2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3418, phi -0.1)
- KXNHLGOAL-26OCT29WSHNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3418, phi -0.197)
- KXNHLGOAL-26OCT29WSHNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3418, phi -0.264)

portfolios: A EV +1.93 (adj +1.07) on $15.33, P(profit) 0.5003, adj growth 9.9 bp · B EV +1.92 (adj +1.23) on $8.89, P(profit) 0.4073, adj growth 11.5 bp · C EV +1.62 (adj +1.04) on $7.54, P(profit) 0.3591, adj growth 9.5 bp · R EV +0.24 (adj +0.16) on $1.00, P(profit) 0.2234, adj growth 6.0 bp

## MTL @ DAL  ·  10000 joint draws  ·  422 bet sides mapped, 1 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.609 / away 0.391

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
| Chris Kreider: 1+ goals YES | 16 | 0.195 | 0.185 | +0.025 | +0.015 | $1.90 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Chris Kreider: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29MTLDAL-DAL3|no; why: higher confidence-adjusted growth (3.68 vs 0.87 bp); despite a smaller raw edge (+0.025 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts DAL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis MTL:OFFENSE_4PLUS (p 0.3288): highest fidelity KXNHLGOAL-26OCT29MTLDAL-MTLCKREIDER22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29MTLDAL-MTLCKREIDER22-1|yes (same contract)
- KXNHLGOAL-26OCT29MTLDAL-MTLCKREIDER22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.4565, phi -0.206)

portfolios: A EV +0.35 (adj +0.22) on $2.36, P(profit) 0.1948, adj growth 2.0 bp · B EV +0.29 (adj +0.17) on $1.90, P(profit) 0.1948, adj growth 1.6 bp · C EV +0.42 (adj +0.26) on $2.81, P(profit) 0.1948, adj growth 2.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ MIN  ·  10000 joint draws  ·  446 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.631 / away 0.369

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_NYI_win | p_overtime | goals | shots MIN/NYI | MIN/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.57 | 0.43 | 0.00 | 5.99 | 28.1/27.8 | 24.5/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.49 | 5.89 | 28.4/28.2 | 25.0/24.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.091 | 0.65 | 0.35 | 0.00 | 5.93 | 33.2/22.2 | 19.5/28.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.60 | 0.40 | 0.00 | 9.29 | 29.5/29.3 | 23.6/23.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.58 | 0.42 | 0.44 | 5.84 | 33.6/22.5 | 19.4/29.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.59 | 0.41 | 0.00 | 3.45 | 26.7/26.5 | 24.8/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Olli Maatta: 1+ goals YES | 4 | 0.067 | 0.058 | +0.024 | +0.015 | $1.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Anthony Duclair: 1+ goals YES | 12 | 0.163 | 0.151 | +0.035 | +0.023 | $2.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 54 | 0.606 | 0.586 | +0.049 | +0.029 | $6.98 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.79) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.158 | 0.144 | +0.030 | +0.017 | $1.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT29NYIMIN-MINJBRODIN25-1|yes; why: higher confidence-adjusted growth (11.46 vs 1.56 bp); despite a smaller raw edge (+0.024 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29NYIMIN-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: MIN offense suppressed (<= 2 goals)
- **Anthony Duclair: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes; why: higher confidence-adjusted growth (10.50 vs 5.62 bp); despite a smaller raw edge (+0.035 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: NYI offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-2|no; why: KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-2|no has the higher standalone adjusted growth (7.63 vs 7.30 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.396); relationships: KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT29NYIMIN-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: MIN offense succeeds (4+ goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes; why: higher confidence-adjusted growth (5.65 vs 5.62 bp); despite a smaller raw edge (+0.030 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT29NYIMIN-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis MIN:SUPPRESSED (p 0.3754): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.442): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:OFFENSE_4PLUS (p 0.3273): highest fidelity KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes (same contract)
- KXNHLGOAL-26OCT29NYIMIN-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3754, phi -0.121)
- KXNHLGOAL-26OCT29NYIMIN-NYIADUCLAIR11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4621, phi -0.191)
- KXNHLGOAL-26OCT29NYIMIN-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4063, phi -0.287)
- KXNHLGOAL-26OCT29NYIMIN-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4621, phi -0.198)

portfolios: A EV +2.59 (adj +0.64) on $15.45, P(profit) 0.5358, adj growth 5.6 bp · B EV +2.58 (adj +1.58) on $12.90, P(profit) 0.3419, adj growth 14.9 bp · C EV +2.83 (adj +1.16) on $29.00, P(profit) 0.4653, adj growth 10.8 bp · R EV +0.18 (adj +0.10) on $2.00, P(profit) 0.6064, adj growth 3.9 bp

## BUF @ ANA  ·  10000 joint draws  ·  450 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.439 / away 0.561

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
| Tim Washe: 1+ goals YES | 11 | 0.166 | 0.147 | +0.049 | +0.030 | $3.19 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| A.J. Greer: 1+ goals YES | 15 | 0.262 | 0.182 | +0.103 | +0.024 | $2.14 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 12 | 0.160 | 0.146 | +0.032 | +0.019 | $2.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 30 | 0.349 | 0.336 | +0.035 | +0.021 | $3.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: higher confidence-adjusted growth (18.50 vs 9.43 bp); despite a smaller raw edge (+0.049 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.869 vs 0.52); relationships: KXNHLGOAL-26OCT29BUFANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT29BUFANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT29BUFANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: ANA offense suppressed (<= 2 goals)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (9.43 vs 8.99 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.200); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT29BUFANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT29BUFANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (9.43 vs 6.79 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.112); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT29BUFANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT29BUFANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: ANA offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (9.43 vs 4.50 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.164); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT29BUFANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT29BUFANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4724): highest fidelity KXNHLTEAMTOTAL-26OCT29BUFANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3393): highest fidelity KXNHLSPREAD-26OCT29BUFANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes (same contract)
- thesis ANA:WINS (p 0.5661): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3183, phi -0.181)
- KXNHLGOAL-26OCT29BUFANA-ANAAGREER18-1|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 63% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.2 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3183, phi -0.226)
- KXNHLGOAL-26OCT29BUFANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3183, phi -0.15)
- KXNHLGOAL-26OCT29BUFANA-ANABSENNECKE45-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3183, phi -0.235)

portfolios: A EV +4.52 (adj +0.96) on $15.45, P(profit) 0.6409, adj growth 8.6 bp · B EV +3.61 (adj +1.66) on $10.66, P(profit) 0.4822, adj growth 15.6 bp · C EV +1.63 (adj +0.62) on $5.64, P(profit) 0.3393, adj growth 5.7 bp · R EV +0.42 (adj +0.26) on $1.00, P(profit) 0.1657, adj growth 9.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT29BUFANA-BUF|no == KXNHLGAME-26OCT29BUFANA-ANA|yes

## OTT @ LAK  ·  10000 joint draws  ·  434 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.473 / away 0.527

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
| Joel Edmundson: 1+ goals YES | 5 | 0.075 | 0.067 | +0.022 | +0.013 | $1.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Ottawa wins by over 2.5 goals NO | 80 | 0.861 | 0.828 | +0.049 | +0.017 | $8.17 | FUNDED_RESEARCH | $3 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Drake Batherson: 1+ goals NO | 69 | 0.733 | 0.721 | +0.028 | +0.016 | $4.31 | FUNDED_RESEARCH | $2 | OTT:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 58 | 0.692 | 0.613 | +0.095 | +0.016 | $3.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT3|no; why: higher confidence-adjusted growth (7.38 vs 3.97 bp); despite a smaller raw edge (+0.022 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT29OTTLA-OTT3|no: MOSTLY_INDEPENDENT (phi 0.071); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: LAK offense suppressed (<= 2 goals)
- **Ottawa wins by over 2.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT2|no; why: higher confidence-adjusted growth (3.97 vs 1.35 bp); relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.071); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: REINFORCING (phi 0.16); KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.149); failure: OTT wins by 2+
- **Drake Batherson: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29OTTLA-OTT3|no has the higher standalone adjusted growth (3.97 vs 2.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.160); they share one thesis budget; relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT29OTTLA-OTT3|no: REINFORCING (phi 0.16); KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: REINFORCING (phi 0.159); failure: OTT offense succeeds (4+ goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29OTTLA-OTT3|no has the higher standalone adjusted growth (3.97 vs 2.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.149); they share one thesis budget; relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT29OTTLA-OTT3|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: REINFORCING (phi 0.159); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis LAK:OFFENSE_4PLUS (p 0.3832): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT29OTTLA-OTT3|no (same contract)
- thesis LAK:WINS (p 0.5321): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29OTTLA-OTT3|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4553): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29OTTLA-OTT3|no (same contract)
- KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4032, phi -0.134)
- KXNHLSPREAD-26OCT29OTTLA-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2432, phi -0.71)
- KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3242, phi -0.249)
- KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.2 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3242, phi -0.243)

portfolios: A EV +1.23 (adj +0.33) on $15.45, P(profit) 0.7357, adj growth 3.1 bp · B EV +1.69 (adj +0.66) on $16.94, P(profit) 0.5319, adj growth 6.2 bp · C EV +0.77 (adj +0.26) on $12.65, P(profit) 0.8606, adj growth 2.4 bp · R EV +0.26 (adj +0.11) on $5.00, P(profit) 0.6554, adj growth 4.0 bp

## VAN @ SJS  ·  10000 joint draws  ·  420 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.602 / away 0.398

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
| Marco Rossi: 1+ goals YES | 17 | 0.218 | 0.205 | +0.038 | +0.025 | $3.05 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Tyler Toffoli: 1+ assists YES | 27 | 0.342 | 0.304 | +0.059 | +0.020 | $2.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ goals NO | 71 | 0.807 | 0.741 | +0.083 | +0.016 | $8.10 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 61 | 0.716 | 0.640 | +0.089 | +0.014 | $4.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29VANSJ-VANDOCONNOR18-1|yes; why: higher confidence-adjusted growth (9.17 vs 1.33 bp); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: VAN offense suppressed (<= 2 goals)
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT29VANSJ-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (4.24 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.048); KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.031); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (2.92 vs 1.79 bp); despite a smaller raw edge (+0.083 vs +0.089/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: SJS offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29VANSJ-SJ3|no; why: higher confidence-adjusted growth (1.79 vs 0.56 bp); alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4738): highest fidelity KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3162): highest fidelity KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3799): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3976, phi -0.201)
- KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3162, phi -0.263)
- KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.2 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4738, phi -0.181)
- KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.6 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4738, phi -0.23)

portfolios: A EV +2.53 (adj +0.84) on $15.45, P(profit) 0.4588, adj growth 8.0 bp · B EV +2.83 (adj +0.91) on $18.70, P(profit) 0.4185, adj growth 8.6 bp · C EV +1.83 (adj +0.44) on $11.02, P(profit) 0.3424, adj growth 4.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
