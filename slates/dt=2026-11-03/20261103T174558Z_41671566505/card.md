# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-03T17:45:58Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +31.41 | +12.82 | +28.46 | 0.725 | -28.03 | -41.97 | 116.83 |
| B thesis-diversified (joint) ← optimiser card | 149.21 | +31.24 | +17.65 | +28.07 | 0.710 | -30.64 | -45.44 | 163.88 |
| C best expression per thesis | 150.00 | +33.62 | +16.47 | +28.28 | 0.688 | -40.32 | -56.04 | 146.77 |
| R FUNDED research stakes | 21.00 | +3.25 | +1.99 | -0.30 | 0.492 | -8.23 | -9.60 | 0.00 |

## UTA @ TOR  ·  10000 joint draws  ·  458 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.456 / away 0.544

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_UTA_win | p_overtime | goals | shots TOR/UTA | TOR/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.51 | 0.49 | 0.00 | 6.03 | 28.4/28.8 | 25.1/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.53 | 0.47 | 0.00 | 9.45 | 30.1/30.6 | 24.5/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.48 | 0.52 | 0.45 | 6.0 | 28.4/28.9 | 25.5/25.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.101 | 0.48 | 0.52 | 0.00 | 6.03 | 22.7/34.6 | 30.8/19.3 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.092 | 0.43 | 0.57 | 0.00 | 9.33 | 24.2/36.3 | 29.1/18.8 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.46 | 0.54 | 0.49 | 5.95 | 22.9/34.3 | 30.7/19.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.177 | 0.156 | +0.060 | +0.040 | $4.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:WINS_BY_2PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 18 | 0.220 | 0.207 | +0.029 | +0.017 | $2.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Kevin Stenlund: 1+ goals YES | 8 | 0.109 | 0.097 | +0.023 | +0.011 | $1.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 65 | 0.691 | 0.679 | +0.025 | +0.013 | $4.74 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV03UTATOR-UTA4|no; why: higher confidence-adjusted growth (31.97 vs 0.97 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV03UTATOR-UTAKSTENLUND82-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: TOR offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03UTATOR-UTAALEE72-1|yes; why: higher confidence-adjusted growth (3.97 vs 1.50 bp); relationships: KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV03UTATOR-UTAKSTENLUND82-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: UTA offense suppressed (<= 2 goals)
- **Kevin Stenlund: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes has the higher standalone adjusted growth (3.97 vs 3.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: UTA offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV03UTATOR-UTA4|no; why: Player prop expression KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no selected over broad KXNHLTEAMTOTAL-26NOV03UTATOR-UTA4|no because adjusted EV is 0.3 pts higher while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV03UTATOR-UTAKSTENLUND82-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TOR:WINS_BY_2PLUS (p 0.2962): highest fidelity KXNHLTEAMTOTAL-26NOV03UTATOR-UTA4|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:OFFENSE_4PLUS (p 0.4365): highest fidelity KXNHLAST-26NOV03UTATOR-TORECOWAN53-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.4378): highest fidelity KXNHLGOAL-26NOV03UTATOR-UTAALEE72-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3457, phi -0.192)
- KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3487, phi -0.202)
- KXNHLGOAL-26NOV03UTATOR-UTAKSTENLUND82-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3487, phi -0.16)
- KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4378, phi -0.236)
- override: Player prop expression KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no selected over broad KXNHLTEAMTOTAL-26NOV03UTATOR-UTA4|no because adjusted EV is 0.3 pts higher while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.76 (adj +1.72) on $16.38, P(profit) 0.4661, adj growth 15.7 bp · B EV +3.45 (adj +2.15) on $13.51, P(profit) 0.3794, adj growth 19.9 bp · C EV +4.76 (adj +3.06) on $18.73, P(profit) 0.3596, adj growth 27.1 bp · R EV +0.08 (adj +0.04) on $2.00, P(profit) 0.6909, adj growth 1.5 bp

## WPG @ MTL  ·  10000 joint draws  ·  384 bet sides mapped, 4 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.616 / away 0.384

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_WPG_win | p_overtime | goals | shots MTL/WPG | MTL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.63 | 0.37 | 0.00 | 6.01 | 27.1/27.0 | 24.2/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.54 | 0.46 | 0.45 | 5.92 | 27.1/27.2 | 24.1/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.63 | 0.37 | 0.00 | 9.29 | 28.6/28.6 | 23.4/21.6 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.074 | 0.70 | 0.30 | 0.00 | 6.04 | 31.6/21.5 | 18.9/26.9 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.063 | 0.57 | 0.43 | 0.00 | 5.91 | 21.6/32.0 | 28.6/18.0 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.58 | 0.42 | 0.46 | 5.97 | 32.0/21.7 | 18.6/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dylan Samberg: 1+ goals YES | 4 | 0.066 | 0.057 | +0.023 | +0.014 | $1.46 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Cole Perfetti: 1+ assists YES | 30 | 0.374 | 0.329 | +0.059 | +0.015 | $1.51 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
| Mark Scheifele: 1+ goals YES | 27 | 0.306 | 0.296 | +0.022 | +0.012 | $1.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
- **Dylan Samberg: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG6|yes; why: higher confidence-adjusted growth (10.35 vs 6.08 bp); despite a smaller raw edge (+0.023 vs +0.029/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.883 vs 0.337); relationships: KXNHLAST-26NOV03WPGMTL-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi 0.064); KXNHLGOAL-26NOV03WPGMTL-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: WPG offense suppressed (<= 2 goals)
- **Cole Perfetti: 1+ assists YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG6|yes; why: KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG6|yes has the higher standalone adjusted growth (6.08 vs 2.17 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.165); relationships: KXNHLGOAL-26NOV03WPGMTL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi 0.064); KXNHLGOAL-26NOV03WPGMTL-WPGMSCHEIFELE55-1|yes: REINFORCING (phi 0.2); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG6|yes; why: KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG6|yes has the higher standalone adjusted growth (6.08 vs 1.53 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.153); relationships: KXNHLGOAL-26NOV03WPGMTL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26NOV03WPGMTL-WPGCPERFETTI91-1|yes: REINFORCING (phi 0.2); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WPG:OFFENSE_4PLUS (p 0.3256): highest fidelity KXNHLAST-26NOV03WPGMTL-WPGCPERFETTI91-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV03WPGMTL-WPGCPERFETTI91-1|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.2679): highest fidelity KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG6|yes [FRAGILE], best adjusted EV KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG6|yes (same contract)
- KXNHLGOAL-26NOV03WPGMTL-WPGDSAMBERG54-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4516, phi -0.108)
- KXNHLAST-26NOV03WPGMTL-WPGCPERFETTI91-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4516, phi -0.291)
- KXNHLGOAL-26NOV03WPGMTL-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4516, phi -0.257)

portfolios: A EV +4.22 (adj +1.70) on $13.57, P(profit) 0.4285, adj growth 14.0 bp · B EV +1.18 (adj +0.61) on $4.30, P(profit) 0.5466, adj growth 5.7 bp · C EV +1.08 (adj +0.40) on $1.57, P(profit) 0.072, adj growth 3.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ TBL  ·  10000 joint draws  ·  406 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.700 / away 0.300

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_DET_win | p_overtime | goals | shots TBL/DET | TBL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.73 | 0.27 | 0.00 | 6.0 | 27.2/27.0 | 24.5/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.47 | 5.86 | 27.2/27.3 | 24.1/23.9 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.097 | 0.76 | 0.24 | 0.00 | 6.01 | 31.9/21.3 | 18.9/27.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.71 | 0.29 | 0.00 | 9.32 | 28.6/28.4 | 23.6/21.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.56 | 0.44 | 0.45 | 5.83 | 32.7/21.8 | 18.7/29.3 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.069 | 0.75 | 0.25 | 0.00 | 9.3 | 34.1/22.9 | 18.8/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charle-Edouard D'Astous: 1+ goals NO | 89 | 0.922 | 0.910 | +0.025 | +0.013 | $10.07 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Emmitt Finnie: 1+ assists YES | 26 | 0.329 | 0.292 | +0.056 | +0.019 | $2.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 65 | 0.716 | 0.680 | +0.050 | +0.014 | $5.06 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ilya Mikheyev: 1+ goals YES | 15 | 0.183 | 0.170 | +0.024 | +0.011 | $1.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (4.16 vs 3.04 bp); despite a smaller raw edge (+0.025 vs +0.100/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV03DETTB-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLSPREAD-26NOV03DETTB-TB3|no: MOSTLY_INDEPENDENT (phi 0.087); KXNHLGOAL-26NOV03DETTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: TBL offense succeeds (4+ goals)
- **Emmitt Finnie: 1+ assists YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV03DETTB-TB2|no; why: higher confidence-adjusted growth (3.82 vs 2.68 bp); despite a smaller raw edge (+0.056 vs +0.057/contract); relationships: KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLSPREAD-26NOV03DETTB-TB3|no: REINFORCING (phi 0.159); KXNHLGOAL-26NOV03DETTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: DET offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV03DETTB-TB2|no; why: Broad expression KXNHLSPREAD-26NOV03DETTB-TB3|no selected over player prop KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.70 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.087); KXNHLAST-26NOV03DETTB-DETEFINNIE58-1|yes: REINFORCING (phi 0.159); KXNHLGOAL-26NOV03DETTB-TBIMIKHEYEV95-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.133); failure: TBL wins by 2+
- **Ilya Mikheyev: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV03DETTB-TBACIRELLI71-1|yes; why: higher confidence-adjusted growth (1.80 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26NOV03DETTB-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLSPREAD-26NOV03DETTB-TB3|no: INTENTIONAL_DIVERSIFIER (phi -0.133); failure: TBL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DET:OFFENSE_4PLUS (p 0.2847): highest fidelity KXNHLSPREAD-26NOV03DETTB-TB3|no [DIRECT], best adjusted EV KXNHLAST-26NOV03DETTB-DETEFINNIE58-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.3055): highest fidelity KXNHLSPREAD-26NOV03DETTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no — Broad expression KXNHLSPREAD-26NOV03DETTB-TB3|no selected over player prop KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.70 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:TIGHT (p 0.4097): highest fidelity KXNHLSPREAD-26NOV03DETTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03DETTB-TB2|no (same contract)
- KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4886, phi -0.119)
- KXNHLAST-26NOV03DETTB-DETEFINNIE58-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.5025, phi -0.294)
- KXNHLSPREAD-26NOV03DETTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4151, phi -0.748)
- KXNHLGOAL-26NOV03DETTB-TBIMIKHEYEV95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3055, phi -0.169)
- override: Broad expression KXNHLSPREAD-26NOV03DETTB-TB3|no selected over player prop KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.70 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.85 (adj +0.67) on $16.38, P(profit) 0.6195, adj growth 6.1 bp · B EV +1.46 (adj +0.55) on $19.52, P(profit) 0.4233, adj growth 5.2 bp · C EV +2.58 (adj +0.66) on $13.40, P(profit) 0.535, adj growth 6.0 bp · R EV +0.23 (adj +0.09) on $5.00, P(profit) 0.6702, adj growth 3.3 bp

## STL @ NYR  ·  10000 joint draws  ·  400 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.521 / away 0.479

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_STL_win | p_overtime | goals | shots NYR/STL | NYR/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.54 | 0.46 | 0.00 | 6.02 | 26.9/26.9 | 23.6/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.46 | 5.91 | 26.9/26.9 | 23.6/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.55 | 0.45 | 0.00 | 9.25 | 28.1/28.2 | 22.6/22.1 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.070 | 0.59 | 0.41 | 0.00 | 6.01 | 31.4/21.2 | 18.2/27.3 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.067 | 0.46 | 0.54 | 0.00 | 6.02 | 21.2/31.2 | 27.5/18.0 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.53 | 0.47 | 0.47 | 5.92 | 31.3/21.3 | 18.1/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alexis Lafreniere: 1+ goals YES | 29 | 0.337 | 0.324 | +0.032 | +0.019 | $3.42 | FUNDED_RESEARCH | $1 | NYR:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| Tye Kartye: 1+ goals YES | 16 | 0.192 | 0.180 | +0.023 | +0.011 | $1.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 29 | 0.328 | 0.317 | +0.024 | +0.013 | $2.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
- **Alexis Lafreniere: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03STLNYR-NYRTKARTYE24-1|yes; why: higher confidence-adjusted growth (3.83 vs 1.92 bp); relationships: KXNHLGOAL-26NOV03STLNYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV03STLNYR-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: NYR offense suppressed (<= 2 goals)
- **Tye Kartye: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes has the higher standalone adjusted growth (3.83 vs 1.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV03STLNYR-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: NYR offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV03STLNYR-STLPBROBERG6-1|yes; why: higher confidence-adjusted growth (1.68 vs 0.00 bp); despite a smaller raw edge (+0.024 vs +0.028/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV03STLNYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NYR:OFFENSE_4PLUS (p 0.399): highest fidelity KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3649): highest fidelity KXNHLGOAL-26NOV03STLNYR-STLJSNUGGERUD21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03STLNYR-STLJSNUGGERUD21-1|yes (same contract)
- KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3905, phi -0.278)
- KXNHLGOAL-26NOV03STLNYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3905, phi -0.205)
- KXNHLGOAL-26NOV03STLNYR-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4156, phi -0.279)

portfolios: A EV +0.92 (adj +0.51) on $8.82, P(profit) 0.6407, adj growth 4.7 bp · B EV +0.75 (adj +0.42) on $7.31, P(profit) 0.6407, adj growth 3.9 bp · C EV +0.84 (adj +0.49) on $8.91, P(profit) 0.5572, adj growth 4.4 bp · R EV +0.11 (adj +0.06) on $1.00, P(profit) 0.3366, adj growth 2.3 bp

## MIN @ PHI  ·  10000 joint draws  ·  422 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.383 / away 0.617

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_MIN_win | p_overtime | goals | shots PHI/MIN | PHI/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.54 | 0.46 | 0.00 | 6.0 | 27.0/27.4 | 24.1/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.53 | 0.47 | 0.47 | 5.86 | 27.1/27.6 | 24.4/23.8 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.50 | 0.50 | 0.48 | 5.84 | 21.9/32.7 | 29.3/18.8 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.086 | 0.48 | 0.52 | 0.00 | 5.96 | 21.5/32.4 | 28.2/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.52 | 0.48 | 0.00 | 9.09 | 28.6/29.1 | 23.3/22.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.55 | 0.45 | 0.00 | 3.51 | 25.6/26.0 | 24.2/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Christian Dvorak: 1+ goals YES | 16 | 0.219 | 0.203 | +0.050 | +0.034 | $4.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Philadelphia wins by over 1.5 goals YES | 20 | 0.288 | 0.242 | +0.077 | +0.030 | $2.60 | FUNDED_RESEARCH | $1 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Matt Boldy: 1+ goals NO | 63 | 0.690 | 0.673 | +0.044 | +0.026 | $8.00 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 52 | 0.643 | 0.560 | +0.106 | +0.022 | $4.75 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: higher confidence-adjusted growth (17.15 vs 12.06 bp); despite a smaller raw edge (+0.050 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.961 vs 0.539); relationships: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: REINFORCING (phi 0.155); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV03MINPHI-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: PHI offense suppressed (<= 2 goals)
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLSPREAD-26NOV03MINPHI-MIN2|no; why: higher confidence-adjusted growth (12.06 vs 7.67 bp); despite a smaller raw edge (+0.077 vs +0.123/contract); relationships: KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: REINFORCING (phi 0.155); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: REINFORCING (phi 0.175); KXNHLGOAL-26NOV03MINPHI-MINKKAPRIZOV97-1|no: REINFORCING (phi 0.212); failure: MIN wins (incl. OT/SO)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes has the higher standalone adjusted growth (12.06 vs 6.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.175); they share one thesis budget; relationships: KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: REINFORCING (phi 0.175); KXNHLGOAL-26NOV03MINPHI-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: MIN offense succeeds (4+ goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes has the higher standalone adjusted growth (12.06 vs 4.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.212); they share one thesis budget; relationships: KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: REINFORCING (phi 0.212); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.09.
- thesis PHI:OFFENSE_4PLUS (p 0.3606): highest fidelity KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2884): highest fidelity KXNHLSPREAD-26NOV03MINPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes (same contract)
- thesis PHI:WINS (p 0.5207): highest fidelity KXNHLSPREAD-26NOV03MINPHI-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4139, phi -0.212)
- KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.4793, phi -0.611)
- KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3363, phi -0.262)
- KXNHLGOAL-26NOV03MINPHI-MINKKAPRIZOV97-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.8 pts; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3363, phi -0.324)

portfolios: A EV +3.98 (adj +0.81) on $16.38, P(profit) 0.5873, adj growth 7.5 bp · B EV +3.69 (adj +1.75) on $19.66, P(profit) 0.6233, adj growth 16.3 bp · C EV +3.93 (adj +2.10) on $12.08, P(profit) 0.4152, adj growth 18.7 bp · R EV +0.57 (adj +0.27) on $4.00, P(profit) 0.7429, adj growth 9.8 bp
equivalent contracts collapsed: KXNHLGAME-26NOV03MINPHI-MIN|no == KXNHLGAME-26NOV03MINPHI-PHI|yes

## VGK @ PIT  ·  10000 joint draws  ·  422 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.508 / away 0.492

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_VGK_win | p_overtime | goals | shots PIT/VGK | PIT/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.52 | 0.48 | 0.00 | 6.03 | 27.2/27.3 | 23.9/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.47 | 5.96 | 27.4/27.4 | 24.1/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.51 | 0.49 | 0.00 | 9.35 | 29.0/29.1 | 23.0/22.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.070 | 0.59 | 0.41 | 0.00 | 5.98 | 32.2/21.5 | 18.5/28.0 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.44 | 5.94 | 32.1/21.7 | 18.6/28.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.064 | 0.46 | 0.54 | 0.00 | 6.0 | 21.6/32.0 | 27.9/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 13 | 0.164 | 0.154 | +0.026 | +0.016 | $2.25 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Justin Brazeau: 1+ goals YES | 15 | 0.184 | 0.169 | +0.025 | +0.010 | $1.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03VGKPIT-PITRRAKELL67-2|yes; why: higher confidence-adjusted growth (4.85 vs 0.03 bp); alternative not eligible: confidence-adjusted EV +0.0008 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03VGKPIT-PITJBRAZEAU16-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PIT offense suppressed (<= 2 goals)
- **Justin Brazeau: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (4.85 vs 1.76 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4262): highest fidelity KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes (same contract)
- KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3532, phi -0.195)
- KXNHLGOAL-26NOV03VGKPIT-PITJBRAZEAU16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3532, phi -0.179)

portfolios: A EV +0.86 (adj +0.45) on $4.93, P(profit) 0.3176, adj growth 4.1 bp · B EV +0.65 (adj +0.36) on $3.69, P(profit) 0.3176, adj growth 3.4 bp · C EV +0.66 (adj +0.41) on $3.49, P(profit) 0.164, adj growth 3.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ WSH  ·  10000 joint draws  ·  432 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.502 / away 0.498

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_DAL_win | p_overtime | goals | shots WSH/DAL | WSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.60 | 0.40 | 0.00 | 6.01 | 26.0/26.2 | 23.1/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.53 | 0.47 | 0.47 | 5.91 | 26.0/26.1 | 22.9/22.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.58 | 0.42 | 0.00 | 9.19 | 27.6/27.7 | 22.1/21.5 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.075 | 0.52 | 0.48 | 0.00 | 5.96 | 20.9/31.1 | 27.5/17.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.49 | 0.51 | 0.43 | 5.86 | 20.7/31.0 | 27.6/17.6 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.068 | 0.71 | 0.29 | 0.00 | 5.99 | 30.5/20.7 | 18.1/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 16 | 0.238 | 0.217 | +0.068 | +0.048 | $6.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 15 | 0.212 | 0.195 | +0.053 | +0.036 | $4.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Martin Fehervary: 1+ goals YES | 3 | 0.049 | 0.043 | +0.017 | +0.011 | $1.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Miro Heiskanen: 1+ goals NO | 87 | 0.903 | 0.893 | +0.025 | +0.015 | $10.07 | FUNDED_RESEARCH | $3 | DAL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03DALWSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (34.46 vs 21.22 bp); relationships: KXNHLGOAL-26NOV03DALWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV03DALWSH-WSHMFEHERVARY42-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: WSH offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (34.46 vs 21.22 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV03DALWSH-WSHMFEHERVARY42-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: WSH offense suppressed (<= 2 goals)
- **Martin Fehervary: 1+ goals YES** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV03DALWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: WSH offense suppressed (<= 2 goals)
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03DALWSH-DALMHEISKANEN4-1|no; why: higher confidence-adjusted growth (4.97 vs 1.58 bp); despite a smaller raw edge (+0.025 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV03DALWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV03DALWSH-WSHMFEHERVARY42-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis WSH:OFFENSE_4PLUS (p 0.4151): highest fidelity KXNHLGOAL-26NOV03DALWSH-WSHTWILSON43-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:OFFENSE_4PLUS (p 0.3245): highest fidelity KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes (same contract)
- thesis DAL:SUPPRESSED (p 0.4531): highest fidelity KXNHLAST-26NOV03DALWSH-DALMHEISKANEN4-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV03DALWSH-DALMHEISKANEN4-1|no (same contract)
- KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3695, phi -0.23)
- KXNHLGOAL-26NOV03DALWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3695, phi -0.201)
- KXNHLGOAL-26NOV03DALWSH-WSHMFEHERVARY42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3695, phi -0.102)
- KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3245, phi -0.15)

portfolios: A EV +3.43 (adj +2.18) on $16.38, P(profit) 0.3995, adj growth 20.7 bp · B EV +5.29 (adj +3.61) on $22.88, P(profit) 0.4304, adj growth 33.5 bp · C EV +6.09 (adj +3.91) on $20.42, P(profit) 0.3363, adj growth 34.6 bp · R EV +0.09 (adj +0.05) on $3.00, P(profit) 0.9029, adj growth 2.0 bp

## COL @ CBJ  ·  10000 joint draws  ·  420 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.468 / away 0.532

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_COL_win | p_overtime | goals | shots CBJ/COL | CBJ/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.48 | 0.52 | 0.00 | 6.02 | 28.1/28.4 | 24.7/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.49 | 0.51 | 0.47 | 5.98 | 28.2/28.8 | 25.5/24.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.094 | 0.43 | 0.57 | 0.00 | 5.99 | 22.3/33.8 | 29.7/19.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.45 | 0.55 | 0.00 | 9.32 | 29.4/29.8 | 23.3/23.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.45 | 0.55 | 0.49 | 5.9 | 22.6/34.1 | 30.7/19.4 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.066 | 0.38 | 0.62 | 0.00 | 9.23 | 23.5/34.8 | 27.6/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 15 | 0.184 | 0.174 | +0.025 | +0.015 | $2.19 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Sean Monahan: 1+ goals YES | 15 | 0.183 | 0.174 | +0.024 | +0.015 | $2.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 9 | 0.119 | 0.107 | +0.024 | +0.011 | $1.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Cole Sillinger: 1+ goals YES | 13 | 0.163 | 0.151 | +0.025 | +0.013 | $1.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03COLCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (3.85 vs 1.46 bp); relationships: KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV03COLCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: CBJ offense suppressed (<= 2 goals)
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (3.85 vs 3.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV03COLCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: CBJ offense suppressed (<= 2 goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (3.85 vs 3.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: CBJ offense suppressed (<= 2 goals)
- **Cole Sillinger: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (3.85 vs 2.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV03COLCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3856): highest fidelity KXNHLGOAL-26NOV03COLCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.3686): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4004, phi -0.225)
- KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4004, phi -0.202)
- KXNHLGOAL-26NOV03COLCBJ-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4004, phi -0.149)
- KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4004, phi -0.188)

portfolios: A EV +1.69 (adj +0.92) on $9.27, P(profit) 0.508, adj growth 8.4 bp · B EV +1.31 (adj +0.73) on $7.38, P(profit) 0.508, adj growth 6.8 bp · C EV +0.54 (adj +0.33) on $3.40, P(profit) 0.1841, adj growth 3.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ NJD  ·  10000 joint draws  ·  430 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_EDM_win | p_overtime | goals | shots NJD/EDM | NJD/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.50 | 0.50 | 0.00 | 6.06 | 28.1/27.7 | 24.2/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.49 | 0.51 | 0.46 | 6.04 | 28.4/27.9 | 24.6/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.49 | 0.51 | 0.00 | 9.44 | 29.8/29.4 | 23.1/23.5 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.098 | 0.57 | 0.43 | 0.00 | 6.04 | 33.2/22.1 | 19.0/29.2 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.52 | 0.48 | 0.47 | 6.01 | 33.6/22.4 | 19.1/30.1 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.074 | 0.58 | 0.42 | 0.00 | 9.36 | 34.9/23.6 | 18.3/27.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Filip Hallander: 1+ goals YES | 7 | 0.130 | 0.112 | +0.055 | +0.038 | $4.19 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 11 | 0.153 | 0.140 | +0.037 | +0.023 | $2.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 22 | 0.275 | 0.260 | +0.043 | +0.028 | $4.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 36 | 0.467 | 0.391 | +0.091 | +0.015 | $4.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.69) | EVIDENCE_MIXED | D |
- **Filip Hallander: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (42.63 vs 9.52 bp); relationships: KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26NOV03EDMNJ-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (11.25 vs 9.52 bp); despite a smaller raw edge (+0.037 vs +0.043/contract); relationships: KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26NOV03EDMNJ-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.03); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV03EDMNJ-7|yes; why: higher confidence-adjusted growth (9.52 vs 4.74 bp); despite a smaller raw edge (+0.043 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.895 vs 0.684); relationships: KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26NOV03EDMNJ-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.22); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03EDMNJ-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (2.02 vs 0.93 bp); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.22); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.417): highest fidelity KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3077): highest fidelity KXNHLTOTAL-26NOV03EDMNJ-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26NOV03EDMNJ-7|yes (same contract)
- thesis EDM:WINS (p 0.486): highest fidelity KXNHLSPREAD-26NOV03EDMNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3727, phi -0.144)
- KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3727, phi -0.168)
- KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3727, phi -0.257)
- KXNHLAST-26NOV03EDMNJ-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 31% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.7 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.417, phi -0.317)

portfolios: A EV +3.19 (adj +0.66) on $16.38, P(profit) 0.5711, adj growth 6.0 bp · B EV +6.02 (adj +3.47) on $16.56, P(profit) 0.4621, adj growth 32.0 bp · C EV +5.90 (adj +1.99) on $38.41, P(profit) 0.7412, adj growth 17.9 bp · R EV +1.48 (adj +1.01) on $2.00, P(profit) 0.1296, adj growth 34.2 bp

## CAR @ NSH  ·  10000 joint draws  ·  428 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.363 / away 0.637

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_CAR_win | p_overtime | goals | shots NSH/CAR | NSH/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.148 | 0.38 | 0.62 | 0.00 | 6.08 | 21.8/34.7 | 30.3/18.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.46 | 0.54 | 0.47 | 5.93 | 21.9/34.4 | 31.0/18.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.112 | 0.37 | 0.63 | 0.00 | 9.36 | 23.1/35.9 | 28.1/18.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.45 | 0.55 | 0.00 | 6.06 | 27.4/28.6 | 24.5/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.50 | 0.50 | 0.48 | 6.02 | 27.7/28.8 | 25.3/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.43 | 0.57 | 0.00 | 9.46 | 28.9/30.0 | 23.3/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack Drury: 1+ goals YES | 9 | 0.132 | 0.120 | +0.036 | +0.025 | $3.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ assists NO | 50 | 0.641 | 0.546 | +0.124 | +0.029 | $7.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CAR:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
| Adam Edstrom: 1+ goals YES | 13 | 0.171 | 0.156 | +0.033 | +0.018 | $2.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 67 | 0.717 | 0.703 | +0.032 | +0.017 | $7.10 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Jack Drury: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: higher confidence-adjusted growth (14.88 vs 6.68 bp); despite a smaller raw edge (+0.036 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.891 vs 0.367); relationships: KXNHLAST-26NOV03CARNSH-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV03CARNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV03CARNSH-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: NSH offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ assists NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV03CARNSH-CAR2|no; why: higher confidence-adjusted growth (7.26 vs 3.24 bp); relationships: KXNHLGOAL-26NOV03CARNSH-NSHJDRURY18-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV03CARNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV03CARNSH-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: CAR offense succeeds (4+ goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes has the higher standalone adjusted growth (6.68 vs 5.92 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.145); relationships: KXNHLGOAL-26NOV03CARNSH-NSHJDRURY18-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26NOV03CARNSH-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV03CARNSH-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: NSH offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03CARNSH-CARSAHO20-1|no; why: second expression of the same thesis: KXNHLAST-26NOV03CARNSH-CARSAHO20-1|no has the higher standalone adjusted growth (7.26 vs 3.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV03CARNSH-NSHJDRURY18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26NOV03CARNSH-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV03CARNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, CAR shot control · high event (8+) · decided (2+) 0.11.
- thesis CAR:SUPPRESSED (p 0.3293): highest fidelity KXNHLSPREAD-26NOV03CARNSH-CAR3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV03CARNSH-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.3841): highest fidelity KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.3076): highest fidelity KXNHLTEAMTOTAL-26NOV03CARNSH-NSH3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV03CARNSH-NSHJDRURY18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4084, phi -0.176)
- KXNHLAST-26NOV03CARNSH-CARSAHO20-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.6 pts; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4591, phi -0.257)
- KXNHLGOAL-26NOV03CARNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4084, phi -0.197)
- KXNHLGOAL-26NOV03CARNSH-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4591, phi -0.217)

portfolios: A EV +2.77 (adj +0.77) on $16.38, P(profit) 0.5025, adj growth 7.0 bp · B EV +3.93 (adj +1.71) on $20.34, P(profit) 0.596, adj growth 15.9 bp · C EV +4.22 (adj +1.10) on $14.01, P(profit) 0.6745, adj growth 9.9 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.7171, adj growth 1.9 bp

## ANA @ VAN  ·  10000 joint draws  ·  390 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.417 / away 0.583

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_ANA_win | p_overtime | goals | shots VAN/ANA | VAN/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.118 | 0.41 | 0.59 | 0.00 | 6.05 | 21.7/34.0 | 29.7/18.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.118 | 0.39 | 0.61 | 0.00 | 9.51 | 23.2/35.5 | 27.9/17.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.50 | 0.50 | 0.00 | 6.05 | 27.2/27.8 | 24.2/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.45 | 0.55 | 0.00 | 9.49 | 29.0/29.8 | 23.1/22.9 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.45 | 0.55 | 0.46 | 6.06 | 21.9/33.9 | 30.3/18.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.52 | 0.48 | 0.46 | 6.01 | 27.3/28.1 | 24.8/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Marco Rossi: 1+ goals YES | 18 | 0.249 | 0.230 | +0.058 | +0.040 | $5.76 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 12 | 0.159 | 0.147 | +0.032 | +0.020 | $2.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 12 | 0.157 | 0.146 | +0.029 | +0.019 | $2.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 20 | 0.245 | 0.231 | +0.034 | +0.020 | $3.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (22.15 vs 5.24 bp); relationships: KXNHLGOAL-26NOV03ANAVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV03ANAVAN-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: VAN offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes has the higher standalone adjusted growth (22.15 vs 7.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV03ANAVAN-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV03ANAVAN-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (6.86 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV03ANAVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.03); failure: ANA offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes has the higher standalone adjusted growth (22.15 vs 5.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV03ANAVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV03ANAVAN-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.03); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, ANA shot control · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4313): highest fidelity KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes (same contract)
- thesis ANA:SUPPRESSED (p 0.3105): highest fidelity KXNHLGOAL-26NOV03ANAVAN-ANACGAUTHIER61-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV03ANAVAN-ANACGAUTHIER61-1|no (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4827): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3512, phi -0.219)
- KXNHLGOAL-26NOV03ANAVAN-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3512, phi -0.176)
- KXNHLGOAL-26NOV03ANAVAN-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3105, phi -0.154)
- KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3512, phi -0.233)

portfolios: A EV +3.74 (adj +2.43) on $15.14, P(profit) 0.6014, adj growth 22.5 bp · B EV +3.51 (adj +2.29) on $14.06, P(profit) 0.6014, adj growth 21.3 bp · C EV +3.02 (adj +2.02) on $15.58, P(profit) 0.2486, adj growth 18.0 bp · R EV +0.61 (adj +0.42) on $2.00, P(profit) 0.2486, adj growth 15.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
