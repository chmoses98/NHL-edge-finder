# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-29T11:52:27Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +26.44 | +5.76 | +25.03 | 0.703 | -33.46 | -48.11 | 46.96 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +21.20 | +9.89 | +17.63 | 0.653 | -37.25 | -50.59 | 87.46 |
| C best expression per thesis | 112.24 | +16.51 | +7.68 | +10.55 | 0.603 | -37.98 | -51.51 | 66.70 |
| R FUNDED research stakes | 32.00 | +3.11 | +1.22 | +3.38 | 0.635 | -8.74 | -12.17 | 0.00 |

## WPG @ TBL  ·  10000 joint draws  ·  376 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WPG_win | p_overtime | goals | shots TBL/WPG | TBL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.69 | 0.31 | 0.00 | 6.03 | 27.0/26.5 | 23.7/22.7 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.118 | 0.73 | 0.27 | 0.00 | 5.98 | 32.4/21.1 | 18.7/27.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.53 | 0.47 | 0.45 | 5.88 | 27.3/26.8 | 23.5/24.0 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.57 | 0.43 | 0.47 | 5.81 | 32.6/21.3 | 18.1/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.69 | 0.31 | 0.00 | 9.27 | 28.7/28.2 | 23.1/21.6 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.071 | 0.75 | 0.25 | 0.00 | 9.21 | 34.2/22.2 | 18.0/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anthony Cirelli: 1+ goals YES | 23 | 0.281 | 0.262 | +0.039 | +0.020 | $6.12 | FUNDED_RESEARCH | $2 | TBL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 25 | 0.296 | 0.278 | +0.033 | +0.015 | $3.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Ilya Mikheyev: 1+ goals YES | 17 | 0.206 | 0.192 | +0.026 | +0.012 | $3.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 1.5 goals NO | 54 | 0.603 | 0.569 | +0.045 | +0.011 | $8.40 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Anthony Cirelli: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes; why: higher confidence-adjusted growth (4.55 vs 2.14 bp); relationships: KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26OCT29WPGTB-TB2|no: INTENTIONAL_DIVERSIFIER (phi -0.191); failure: TBL offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29WPGTB-TB2|no; why: higher confidence-adjusted growth (2.62 vs 1.15 bp); despite a smaller raw edge (+0.033 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT29WPGTB-TB2|no: REINFORCING (phi 0.163); failure: WPG offense suppressed (<= 2 goals)
- **Ilya Mikheyev: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes has the higher standalone adjusted growth (4.55 vs 2.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT29WPGTB-TB2|no: INTENTIONAL_DIVERSIFIER (phi -0.169); failure: TBL offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT29WPGTB-TB3|no; why: higher confidence-adjusted growth (1.15 vs 0.45 bp); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.191); KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: REINFORCING (phi 0.163); KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.169); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:OFFENSE_4PLUS (p 0.4491): highest fidelity KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.2705): highest fidelity KXNHLSPREAD-26OCT29WPGTB-TB2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4282): highest fidelity KXNHLSPREAD-26OCT29WPGTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29WPGTB-TB2|no (same contract)
- KXNHLGOAL-26OCT29WPGTB-TBACIRELLI71-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3364, phi -0.236)
- KXNHLGOAL-26OCT29WPGTB-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.5189, phi -0.281)
- KXNHLGOAL-26OCT29WPGTB-TBIMIKHEYEV95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3364, phi -0.203)
- KXNHLSPREAD-26OCT29WPGTB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3975, phi -1.0)

portfolios: A EV +3.55 (adj +0.98) on $24.19, P(profit) 0.5806, adj growth 8.5 bp · B EV +2.63 (adj +1.12) on $21.75, P(profit) 0.5084, adj growth 9.9 bp · C EV +2.27 (adj +0.96) on $18.98, P(profit) 0.4488, adj growth 8.4 bp · R EV +0.56 (adj +0.22) on $5.00, P(profit) 0.7563, adj growth 7.6 bp

## UTA @ PIT  ·  10000 joint draws  ·  398 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_UTA_win | p_overtime | goals | shots PIT/UTA | PIT/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.53 | 0.47 | 0.00 | 6.1 | 27.1/27.1 | 23.6/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.112 | 0.51 | 0.49 | 0.00 | 9.55 | 29.0/29.0 | 22.8/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.49 | 5.97 | 27.4/27.4 | 24.0/24.0 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.070 | 0.61 | 0.39 | 0.00 | 6.09 | 31.9/21.5 | 18.5/27.7 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.068 | 0.39 | 0.61 | 0.00 | 6.02 | 21.7/31.9 | 27.7/18.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.47 | 0.53 | 0.48 | 5.99 | 21.8/32.2 | 28.7/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Rickard Rakell: 2+ goals YES | 7 | 0.116 | 0.098 | +0.041 | +0.024 | $4.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Declan Carlile: 1+ goals YES | 6 | 0.099 | 0.084 | +0.035 | +0.020 | $3.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 63 | 0.692 | 0.675 | +0.046 | +0.029 | $17.54 | FUNDED_RESEARCH | $5 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ goals YES | 33 | 0.383 | 0.369 | +0.038 | +0.023 | $7.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
- **Rickard Rakell: 2+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (16.89 vs 11.66 bp); despite a smaller raw edge (+0.041 vs +0.045/contract); relationships: KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: PIT offense suppressed (<= 2 goals)
- **Declan Carlile: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes has the higher standalone adjusted growth (16.89 vs 14.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PIT offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29UTAPIT-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (8.09 vs 2.29 bp); despite a smaller raw edge (+0.046 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: UTA offense succeeds (4+ goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes; why: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes because adjusted EV differs by only 0.0 pts while thesis capture is 0.53 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4394): highest fidelity KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes — Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes because adjusted EV differs by only 0.0 pts while thesis capture is 0.53 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis UTA:SUPPRESSED (p 0.3574): highest fidelity KXNHLAST-26OCT29UTAPIT-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3425, phi -0.22)
- KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3425, phi -0.141)
- KXNHLGOAL-26OCT29UTAPIT-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4373, phi -0.245)
- KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3425, phi -0.257)
- override: Player prop expression KXNHLGOAL-26OCT29UTAPIT-PITSCROSBY87-1|yes selected over player prop KXNHLGOAL-26OCT29UTAPIT-PITBLIZOTTE46-1|yes because adjusted EV differs by only 0.0 pts while thesis capture is 0.53 vs 0.26 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- override: override declined: the joint re-optimisation gives KXNHLGOAL-26OCT29UTAPIT-PITRRAKELL67-1|yes less than the minimum stake; KXNHLGOAL-26OCT29UTAPIT-PITDCARLILE72-1|yes kept

portfolios: A EV +10.45 (adj +1.69) on $24.19, P(profit) 0.6104, adj growth 13.2 bp · B EV +6.69 (adj +3.95) on $33.47, P(profit) 0.4136, adj growth 34.6 bp · C EV +4.31 (adj +2.55) on $25.25, P(profit) 0.7293, adj growth 22.0 bp · R EV +0.35 (adj +0.22) on $5.00, P(profit) 0.6921, adj growth 7.9 bp

## CBJ @ CAR  ·  10000 joint draws  ·  422 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CBJ_win | p_overtime | goals | shots CAR/CBJ | CAR/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.152 | 0.68 | 0.32 | 0.00 | 6.04 | 33.6/21.2 | 18.5/28.8 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.127 | 0.55 | 0.45 | 0.45 | 5.91 | 33.9/21.2 | 18.1/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.60 | 0.40 | 0.00 | 6.01 | 27.7/26.8 | 23.6/23.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.097 | 0.68 | 0.32 | 0.00 | 9.18 | 35.3/22.4 | 17.8/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.52 | 0.48 | 0.46 | 5.98 | 27.8/27.1 | 23.8/24.5 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.069 | 0.63 | 0.37 | 0.00 | 3.45 | 32.5/20.1 | 18.7/30.3 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie Coyle: 1+ goals YES | 18 | 0.250 | 0.227 | +0.059 | +0.037 | $8.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 67 | 0.758 | 0.712 | +0.073 | +0.026 | $12.65 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mathieu Olivier: 1+ goals YES | 14 | 0.185 | 0.168 | +0.037 | +0.019 | $3.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 67 | 0.716 | 0.702 | +0.030 | +0.016 | $9.42 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CAR3|no; why: higher confidence-adjusted growth (19.04 vs 7.04 bp); despite a smaller raw edge (+0.059 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT29CBJCAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.14); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT29CBJCAR-CAR2|no; why: higher confidence-adjusted growth (7.04 vs 2.43 bp); despite a smaller raw edge (+0.073 vs +0.089/contract); wins across more scripts (relative breadth 1.027 vs 0.9); relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.14); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.131); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.147); failure: CAR wins by 2+
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (19.04 vs 6.41 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.019); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLSPREAD-26OCT29CBJCAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.131); KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29CBJCAR-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29CBJCAR-CAR3|no has the higher standalone adjusted growth (7.04 vs 2.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.147); they share one thesis budget; relationships: KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLSPREAD-26OCT29CBJCAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.3173): highest fidelity KXNHLTEAMTOTAL-26OCT29CBJCAR-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4248): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29CBJCAR-CAR3|no (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.2117): highest fidelity KXNHLSPREAD-26OCT29CBJCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29CBJCAR-CAR3|no (same contract)
- KXNHLGOAL-26OCT29CBJCAR-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4642, phi -0.256)
- KXNHLSPREAD-26OCT29CBJCAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3635, phi -0.747)
- KXNHLGOAL-26OCT29CBJCAR-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4642, phi -0.237)
- KXNHLGOAL-26OCT29CBJCAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.452, phi -0.215)

portfolios: A EV +3.06 (adj +0.66) on $24.19, P(profit) 0.6419, adj growth 5.9 bp · B EV +5.41 (adj +2.88) on $34.58, P(profit) 0.3765, adj growth 25.5 bp · C EV +5.00 (adj +2.60) on $28.19, P(profit) 0.2497, adj growth 22.5 bp · R EV +0.56 (adj +0.22) on $7.00, P(profit) 0.5711, adj growth 8.0 bp

## CHI @ DET  ·  10000 joint draws  ·  420 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_CHI_win | p_overtime | goals | shots DET/CHI | DET/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.139 | 0.69 | 0.31 | 0.00 | 6.0 | 33.1/21.1 | 18.6/28.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.55 | 0.45 | 0.50 | 5.91 | 33.6/21.6 | 18.5/30.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.65 | 0.35 | 0.00 | 6.02 | 27.4/26.7 | 23.8/23.3 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.090 | 0.72 | 0.28 | 0.00 | 9.19 | 34.6/22.2 | 17.8/26.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.52 | 0.48 | 0.50 | 5.9 | 27.5/26.9 | 23.5/24.2 | even strength |
| DET shot control · low event (<=4) · decided (2+) | 0.070 | 0.66 | 0.34 | 0.00 | 3.47 | 31.8/19.8 | 18.4/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Bedard: 1+ assists NO | 57 | 0.650 | 0.602 | +0.062 | +0.015 | $7.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Patrick Kane: 1+ assists NO | 59 | 0.696 | 0.617 | +0.089 | +0.010 | $5.45 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no; why: higher confidence-adjusted growth (2.09 vs 0.96 bp); despite a smaller raw edge (+0.062 vs +0.089/contract); relationships: KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.1); failure: CHI offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no; why: second expression of the same thesis: KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no has the higher standalone adjusted growth (2.09 vs 0.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.100); they share one thesis budget; relationships: KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.1); failure: CHI offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.14, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:SUPPRESSED (p 0.4811): highest fidelity KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT29CHIDET-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2978, phi -0.277)
- KXNHLAST-26OCT29CHIDET-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2978, phi -0.241)

portfolios: A EV +2.44 (adj +0.41) on $19.35, P(profit) 0.4739, adj growth 3.5 bp · B EV +1.64 (adj +0.30) on $13.36, P(profit) 0.6497, adj growth 2.6 bp · C EV +1.02 (adj +0.25) on $9.62, P(profit) 0.6497, adj growth 2.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_BOS_win | p_overtime | goals | shots STL/BOS | STL/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.53 | 0.47 | 0.00 | 6.05 | 27.1/26.8 | 23.4/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.48 | 5.95 | 27.4/27.3 | 24.0/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.55 | 0.45 | 0.00 | 9.36 | 28.8/28.6 | 22.7/22.6 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.088 | 0.61 | 0.39 | 0.00 | 6.04 | 32.1/21.4 | 18.4/27.8 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.51 | 0.49 | 0.49 | 5.91 | 32.5/21.9 | 18.8/29.2 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.068 | 0.65 | 0.35 | 0.00 | 9.41 | 34.0/23.1 | 18.3/26.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_WSH_win | p_overtime | goals | shots NSH/WSH | NSH/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.51 | 0.49 | 0.00 | 6.02 | 28.0/28.0 | 24.4/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.45 | 5.94 | 28.2/28.0 | 24.7/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.51 | 0.49 | 0.00 | 9.41 | 29.5/29.5 | 23.3/23.0 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.075 | 0.44 | 0.56 | 0.00 | 6.03 | 22.2/32.8 | 28.8/18.9 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.066 | 0.59 | 0.41 | 0.00 | 6.0 | 32.9/22.6 | 19.6/28.8 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.48 | 0.52 | 0.46 | 5.91 | 22.5/33.0 | 29.7/19.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MTL @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_MTL_win | p_overtime | goals | shots DAL/MTL | DAL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.57 | 0.43 | 0.00 | 6.02 | 26.2/25.7 | 22.5/22.3 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.113 | 0.65 | 0.35 | 0.00 | 5.97 | 31.5/20.4 | 17.6/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.46 | 5.96 | 26.5/26.0 | 22.7/23.2 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.56 | 0.44 | 0.45 | 5.88 | 31.8/20.9 | 17.7/28.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.59 | 0.41 | 0.00 | 9.2 | 28.0/27.5 | 22.0/21.4 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.073 | 0.66 | 0.34 | 0.00 | 9.22 | 33.2/22.0 | 17.3/25.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ MIN  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_NYI_win | p_overtime | goals | shots MIN/NYI | MIN/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.58 | 0.42 | 0.00 | 6.0 | 28.3/28.0 | 24.8/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.52 | 0.48 | 0.47 | 5.89 | 28.2/28.0 | 24.7/24.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.086 | 0.63 | 0.37 | 0.00 | 5.98 | 33.3/22.2 | 19.4/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.58 | 0.42 | 0.00 | 9.28 | 29.6/29.4 | 23.8/22.9 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.58 | 0.42 | 0.46 | 5.9 | 33.6/22.5 | 19.5/30.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.055 | 0.53 | 0.47 | 0.00 | 3.51 | 27.0/26.9 | 25.2/24.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Minnesota wins by over 1.5 goals NO | 61 | 0.679 | 0.642 | +0.053 | +0.015 | $3.75 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 73 | 0.790 | 0.758 | +0.047 | +0.014 | $7.37 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I over 2.5 goals scored YES | 49 | 0.565 | 0.520 | +0.057 | +0.012 | $1.66 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Minnesota wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT29NYIMIN-MIN3|no; why: higher confidence-adjusted growth (2.27 vs 2.23 bp); relationships: KXNHLSPREAD-26OCT29NYIMIN-MIN3|no: DUPLICATIVE (phi 0.75); KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes: REINFORCING (phi 0.483); failure: MIN wins by 2+
- **Minnesota wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no has the higher standalone adjusted growth (2.27 vs 2.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.750); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no: DUPLICATIVE (phi 0.75); KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes: REINFORCING (phi 0.41); failure: MIN wins by 2+
- **New York I over 2.5 goals scored YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no has the higher standalone adjusted growth (2.27 vs 1.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.483); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29NYIMIN-MIN2|no: REINFORCING (phi 0.483); KXNHLSPREAD-26OCT29NYIMIN-MIN3|no: REINFORCING (phi 0.41); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis GAME:TIGHT (p 0.4451): highest fidelity KXNHLSPREAD-26OCT29NYIMIN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29NYIMIN-MIN2|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3337): highest fidelity KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29NYIMIN-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT29NYIMIN-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3206, phi -1.0)
- KXNHLSPREAD-26OCT29NYIMIN-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3206, phi -0.75)
- KXNHLTEAMTOTAL-26OCT29NYIMIN-NYI3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:SUPPRESSED (p 0.4457, phi -0.979)

portfolios: A EV +2.90 (adj +0.67) on $24.19, P(profit) 0.5152, adj growth 4.3 bp · B EV +0.96 (adj +0.27) on $12.77, P(profit) 0.713, adj growth 2.4 bp · C EV +0.92 (adj +0.27) on $10.91, P(profit) 0.6794, adj growth 2.4 bp · R EV +0.32 (adj +0.09) on $4.00, P(profit) 0.713, adj growth 3.0 bp

## BUF @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BUF_win | p_overtime | goals | shots ANA/BUF | ANA/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.57 | 0.43 | 0.00 | 6.02 | 28.3/28.0 | 24.8/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.52 | 0.48 | 0.50 | 5.99 | 28.1/28.2 | 24.8/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.57 | 0.43 | 0.00 | 9.37 | 29.5/29.5 | 23.6/23.0 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.084 | 0.64 | 0.36 | 0.00 | 6.03 | 33.4/22.6 | 19.8/28.9 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.47 | 5.98 | 33.2/22.5 | 19.3/29.9 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.067 | 0.65 | 0.35 | 0.00 | 9.37 | 34.7/23.6 | 18.7/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anaheim wins by over 1.5 goals YES | 25 | 0.336 | 0.290 | +0.073 | +0.027 | $3.93 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 2.5 goals NO | 77 | 0.849 | 0.807 | +0.066 | +0.024 | $17.54 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 2.5 goals YES | 16 | 0.227 | 0.191 | +0.057 | +0.021 | $1.76 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | DIRECT (0.67) | EVIDENCE_MIXED | D |
| Buffalo wins by over 1.5 goals NO | 67 | 0.752 | 0.708 | +0.066 | +0.023 | $1.33 | FUNDED_RESEARCH | $1 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: higher confidence-adjusted growth (8.42 vs 7.73 bp); relationships: KXNHLSPREAD-26OCT29BUFANA-BUF3|no: DUPLICATIVE (phi 0.301); KXNHLSPREAD-26OCT29BUFANA-ANA3|yes: DUPLICATIVE (phi 0.761); KXNHLSPREAD-26OCT29BUFANA-BUF2|no: DUPLICATIVE (phi 0.409); failure: BUF wins (incl. OT/SO)
- **Buffalo wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (8.42 vs 7.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.301); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: DUPLICATIVE (phi 0.301); KXNHLSPREAD-26OCT29BUFANA-ANA3|yes: REINFORCING (phi 0.229); KXNHLSPREAD-26OCT29BUFANA-BUF2|no: DUPLICATIVE (phi 0.735); failure: BUF wins by 2+
- **Anaheim wins by over 2.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (8.42 vs 7.10 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.761); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: DUPLICATIVE (phi 0.761); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: REINFORCING (phi 0.229); KXNHLSPREAD-26OCT29BUFANA-BUF2|no: DUPLICATIVE (phi 0.311); failure: BUF wins (incl. OT/SO)
- **Buffalo wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes has the higher standalone adjusted growth (8.42 vs 5.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.409); they share one thesis budget; relationships: KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: DUPLICATIVE (phi 0.409); KXNHLSPREAD-26OCT29BUFANA-BUF3|no: DUPLICATIVE (phi 0.735); KXNHLSPREAD-26OCT29BUFANA-ANA3|yes: DUPLICATIVE (phi 0.311); failure: BUF wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis ANA:WINS_BY_2PLUS (p 0.3361): highest fidelity KXNHLSPREAD-26OCT29BUFANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes (same contract)
- thesis ANA:WINS (p 0.5487): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3936): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-ANA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT29BUFANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4513, phi -0.645)
- KXNHLSPREAD-26OCT29BUFANA-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2482, phi -0.735)
- KXNHLSPREAD-26OCT29BUFANA-ANA3|yes: FUNDED_RESEARCH; family MIXED; loses 33% of the draws where the thesis happens; opposing: failure thesis BUF:WINS (p 0.4513, phi -0.491)
- KXNHLSPREAD-26OCT29BUFANA-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2482, phi -1.0)

portfolios: A EV +3.47 (adj +1.19) on $24.19, P(profit) 0.5903, adj growth 10.2 bp · B EV +3.30 (adj +1.22) on $24.56, P(profit) 0.3361, adj growth 11.0 bp · C EV +2.34 (adj +0.88) on $8.45, P(profit) 0.3361, adj growth 7.7 bp · R EV +1.14 (adj +0.42) on $8.00, P(profit) 0.3361, adj growth 14.4 bp

## OTT @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_OTT_win | p_overtime | goals | shots LAK/OTT | LAK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.57 | 0.43 | 0.00 | 5.98 | 26.9/27.0 | 23.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.55 | 0.45 | 0.46 | 5.93 | 26.8/27.0 | 23.7/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.55 | 0.45 | 0.00 | 9.17 | 28.4/28.8 | 23.3/22.2 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.077 | 0.53 | 0.47 | 0.00 | 5.98 | 21.6/32.2 | 28.7/18.2 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.51 | 0.49 | 0.45 | 5.82 | 21.4/32.3 | 29.0/18.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.49 | 0.51 | 0.48 | 2.8 | 25.4/25.7 | 24.1/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ottawa wins by over 1.5 goals NO | 70 | 0.757 | 0.726 | +0.043 | +0.011 | $9.51 | FUNDED_RESEARCH | $3 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ottawa wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT3|no; why: higher confidence-adjusted growth (1.42 vs 0.07 bp); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: OTT wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis LAK:WINS (p 0.5494): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29OTTLA-OTT2|no (same contract)
- KXNHLSPREAD-26OCT29OTTLA-OTT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2426, phi -1.0)

portfolios: A EV +0.58 (adj +0.16) on $9.68, P(profit) 0.7574, adj growth 1.4 bp · B EV +0.57 (adj +0.15) on $9.51, P(profit) 0.7574, adj growth 1.4 bp · C EV +0.65 (adj +0.17) on $10.84, P(profit) 0.7574, adj growth 1.5 bp · R EV +0.18 (adj +0.05) on $3.00, P(profit) 0.7574, adj growth 1.7 bp

## VAN @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_VAN_win | p_overtime | goals | shots SJS/VAN | SJS/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.61 | 0.39 | 0.00 | 6.06 | 27.8/27.4 | 24.2/23.6 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.106 | 0.65 | 0.35 | 0.00 | 6.06 | 33.0/21.7 | 18.8/28.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.60 | 0.40 | 0.00 | 9.4 | 29.4/29.0 | 23.4/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.52 | 0.48 | 0.47 | 5.93 | 27.7/27.3 | 24.0/24.4 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.54 | 0.46 | 0.46 | 5.99 | 33.2/21.8 | 18.7/29.8 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.093 | 0.70 | 0.30 | 0.00 | 9.39 | 34.6/23.0 | 18.4/26.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
