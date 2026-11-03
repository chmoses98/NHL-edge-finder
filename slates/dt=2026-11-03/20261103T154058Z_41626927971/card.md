# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-03T15:40:58Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +26.10 | +10.23 | +24.53 | 0.740 | -23.12 | -36.41 | 94.76 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +23.81 | +13.27 | +21.86 | 0.712 | -25.69 | -36.91 | 125.04 |
| C best expression per thesis | 150.00 | +25.77 | +11.21 | +22.37 | 0.706 | -29.14 | -42.36 | 102.35 |
| R FUNDED research stakes | 23.00 | +2.83 | +1.71 | +0.45 | 0.577 | -6.44 | -8.11 | 0.00 |

## UTA @ TOR  ·  10000 joint draws  ·  430 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_UTA_win | p_overtime | goals | shots TOR/UTA | TOR/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.52 | 0.48 | 0.00 | 6.02 | 28.2/28.8 | 25.3/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.113 | 0.52 | 0.48 | 0.00 | 9.41 | 30.0/30.8 | 24.5/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.54 | 0.46 | 0.46 | 5.99 | 28.4/29.1 | 25.8/24.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.101 | 0.43 | 0.57 | 0.00 | 6.06 | 22.8/34.7 | 30.6/19.7 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.49 | 0.51 | 0.47 | 6.01 | 22.9/34.7 | 31.2/19.4 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.086 | 0.44 | 0.56 | 0.00 | 9.37 | 24.0/36.1 | 28.7/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.177 | 0.159 | +0.060 | +0.042 | $4.56 | FUNDED_RESEARCH | $2 | TOR:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 11 | 0.151 | 0.138 | +0.034 | +0.021 | $2.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 18 | 0.221 | 0.208 | +0.030 | +0.018 | $2.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Anders Lee: 1+ goals YES | 20 | 0.243 | 0.227 | +0.032 | +0.016 | $2.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26NOV03UTATOR-TORMRIELLY44-1|yes; why: higher confidence-adjusted growth (36.84 vs 3.65 bp); despite a smaller raw edge (+0.060 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV03UTATOR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV03UTATOR-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: TOR offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (9.53 vs 4.33 bp); relationships: KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV03UTATOR-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: UTA offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03UTATOR-UTAALEE72-1|yes; why: higher confidence-adjusted growth (4.33 vs 3.39 bp); despite a smaller raw edge (+0.030 vs +0.032/contract); relationships: KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV03UTATOR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV03UTATOR-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: UTA offense suppressed (<= 2 goals)
- **Anders Lee: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes has the higher standalone adjusted growth (4.33 vs 3.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV03UTATOR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.4435): highest fidelity KXNHLAST-26NOV03UTATOR-TORMRIELLY44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.4331): highest fidelity KXNHLGOAL-26NOV03UTATOR-UTAALEE72-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3454, phi -0.212)
- KXNHLGOAL-26NOV03UTATOR-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3383, phi -0.165)
- KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3383, phi -0.208)
- KXNHLGOAL-26NOV03UTATOR-UTAALEE72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3383, phi -0.204)

portfolios: A EV +4.57 (adj +2.58) on $14.56, P(profit) 0.5314, adj growth 23.8 bp · B EV +3.71 (adj +2.44) on $11.19, P(profit) 0.4565, adj growth 22.9 bp · C EV +4.20 (adj +2.88) on $10.55, P(profit) 0.3616, adj growth 25.9 bp · R EV +1.04 (adj +0.73) on $2.00, P(profit) 0.1774, adj growth 25.7 bp

## WPG @ MTL  ·  10000 joint draws  ·  366 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_WPG_win | p_overtime | goals | shots MTL/WPG | MTL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.63 | 0.37 | 0.00 | 6.03 | 27.0/27.0 | 24.0/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.56 | 0.44 | 0.47 | 5.89 | 27.1/27.2 | 23.9/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.62 | 0.38 | 0.00 | 9.22 | 28.5/28.5 | 23.2/21.7 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 6.02 | 31.5/21.5 | 18.9/26.9 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.066 | 0.56 | 0.44 | 0.00 | 6.05 | 21.7/32.2 | 28.6/18.2 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.60 | 0.40 | 0.47 | 5.92 | 31.9/21.6 | 18.5/28.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Oliver Kapanen: 1+ goals YES | 15 | 0.192 | 0.180 | +0.033 | +0.022 | $2.59 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Dylan Samberg: 1+ goals YES | 4 | 0.065 | 0.055 | +0.022 | +0.012 | $1.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Phillip Danault: 1+ goals YES | 14 | 0.174 | 0.163 | +0.025 | +0.014 | $1.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 20 | 0.238 | 0.228 | +0.027 | +0.016 | $2.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Oliver Kapanen: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes; why: higher confidence-adjusted growth (7.50 vs 3.57 bp); relationships: KXNHLGOAL-26NOV03WPGMTL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV03WPGMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: MTL offense suppressed (<= 2 goals)
- **Dylan Samberg: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26NOV03WPGMTL-WPGCPERFETTI91-1|yes; why: higher confidence-adjusted growth (7.40 vs 3.98 bp); despite a smaller raw edge (+0.022 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV03WPGMTL-MTLOKAPANEN91-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV03WPGMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: WPG offense suppressed (<= 2 goals)
- **Phillip Danault: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLGOAL-26NOV03WPGMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (3.57 vs 2.66 bp); relationships: KXNHLGOAL-26NOV03WPGMTL-MTLOKAPANEN91-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV03WPGMTL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV03WPGMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: MTL offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes has the higher standalone adjusted growth (3.57 vs 3.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV03WPGMTL-MTLOKAPANEN91-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV03WPGMTL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WPG:OFFENSE_4PLUS (p 0.3258): highest fidelity KXNHLAST-26NOV03WPGMTL-WPGCPERFETTI91-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV03WPGMTL-WPGCPERFETTI91-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4455): highest fidelity KXNHLGOAL-26NOV03WPGMTL-MTLJANDERSON17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03WPGMTL-MTLJANDERSON17-1|yes (same contract)
- thesis MTL:WINS_BY_2PLUS (p 0.3532): highest fidelity KXNHLGOAL-26NOV03WPGMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV03WPGMTL-MTLOKAPANEN91-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3367, phi -0.18)
- KXNHLGOAL-26NOV03WPGMTL-WPGDSAMBERG54-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4533, phi -0.115)
- KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3367, phi -0.194)
- KXNHLGOAL-26NOV03WPGMTL-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3367, phi -0.217)

portfolios: A EV +2.40 (adj +1.16) on $13.39, P(profit) 0.5844, adj growth 10.7 bp · B EV +1.68 (adj +0.99) on $7.54, P(profit) 0.526, adj growth 9.3 bp · C EV +1.31 (adj +0.54) on $7.18, P(profit) 0.4844, adj growth 5.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ TBL  ·  10000 joint draws  ·  404 bet sides mapped, 5 +EV candidates, 4 on card


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
| Charle-Edouard D'Astous: 1+ goals NO | 88 | 0.922 | 0.907 | +0.034 | +0.020 | $8.54 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ assists NO | 35 | 0.476 | 0.388 | +0.110 | +0.022 | $2.99 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 65 | 0.716 | 0.680 | +0.050 | +0.014 | $2.67 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Emmitt Finnie: 1+ assists YES | 27 | 0.329 | 0.297 | +0.045 | +0.013 | $1.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (9.04 vs 4.46 bp); despite a smaller raw edge (+0.034 vs +0.110/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.072); KXNHLSPREAD-26NOV03DETTB-TB3|no: MOSTLY_INDEPENDENT (phi 0.087); KXNHLAST-26NOV03DETTB-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV03DETTB-TB3|no; why: higher confidence-adjusted growth (4.46 vs 2.05 bp); relationships: KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.072); KXNHLSPREAD-26NOV03DETTB-TB3|no: REINFORCING (phi 0.204); KXNHLAST-26NOV03DETTB-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV03DETTB-TB2|no; why: higher confidence-adjusted growth (2.05 vs 1.37 bp); wins across more scripts (relative breadth 1.015 vs 0.859); relationships: KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.087); KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.204); KXNHLAST-26NOV03DETTB-DETEFINNIE58-1|yes: REINFORCING (phi 0.159); failure: TBL wins by 2+
- **Emmitt Finnie: 1+ assists YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV03DETTB-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV03DETTB-TB3|no has the higher standalone adjusted growth (2.05 vs 1.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.159); they share one thesis budget; relationships: KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26NOV03DETTB-TB3|no: REINFORCING (phi 0.159); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TBL:SUPPRESSED (p 0.3055): highest fidelity KXNHLSPREAD-26NOV03DETTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4097): highest fidelity KXNHLSPREAD-26NOV03DETTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03DETTB-TB3|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.2847): highest fidelity KXNHLSPREAD-26NOV03DETTB-TB3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV03DETTB-TB3|no (same contract)
- KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4886, phi -0.119)
- KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.6 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4886, phi -0.294)
- KXNHLSPREAD-26NOV03DETTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4151, phi -0.748)
- KXNHLAST-26NOV03DETTB-DETEFINNIE58-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.5025, phi -0.294)

portfolios: A EV +2.27 (adj +0.54) on $14.56, P(profit) 0.5332, adj growth 4.9 bp · B EV +1.70 (adj +0.51) on $15.89, P(profit) 0.5762, adj growth 4.9 bp · C EV +1.84 (adj +0.40) on $10.35, P(profit) 0.4763, adj growth 3.7 bp · R EV +0.19 (adj +0.09) on $4.00, P(profit) 0.6702, adj growth 3.5 bp

## STL @ NYR  ·  10000 joint draws  ·  382 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_STL_win | p_overtime | goals | shots NYR/STL | NYR/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.55 | 0.45 | 0.00 | 6.05 | 26.8/26.7 | 23.3/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.49 | 0.51 | 0.46 | 5.95 | 26.7/26.9 | 23.6/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.55 | 0.45 | 0.00 | 9.29 | 28.6/28.3 | 22.6/22.3 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.075 | 0.60 | 0.40 | 0.00 | 5.99 | 31.5/21.4 | 18.5/27.5 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.066 | 0.47 | 0.54 | 0.00 | 6.03 | 21.2/31.3 | 27.5/18.0 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.48 | 0.52 | 0.48 | 5.89 | 21.3/31.5 | 28.2/18.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tye Kartye: 1+ goals YES | 16 | 0.199 | 0.186 | +0.029 | +0.017 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Alexis Lafreniere: 1+ goals YES | 31 | 0.355 | 0.341 | +0.030 | +0.016 | $2.49 | FUNDED_RESEARCH | $1 | NYR:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Tye Kartye: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes; why: higher confidence-adjusted growth (4.51 vs 2.59 bp); despite a smaller raw edge (+0.029 vs +0.030/contract); relationships: KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: NYR offense suppressed (<= 2 goals)
- **Alexis Lafreniere: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-2|yes; why: higher confidence-adjusted growth (2.59 vs 0.60 bp); wins across more scripts (relative breadth 0.906 vs 0.709); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03STLNYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NYR:OFFENSE_4PLUS (p 0.4098): highest fidelity KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes (same contract)
- KXNHLGOAL-26NOV03STLNYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3712, phi -0.193)
- KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3712, phi -0.294)

portfolios: A EV +0.74 (adj +0.42) on $5.78, P(profit) 0.483, adj growth 3.9 bp · B EV +0.59 (adj +0.33) on $4.57, P(profit) 0.483, adj growth 3.2 bp · C EV +0.35 (adj +0.19) on $3.86, P(profit) 0.3548, adj growth 1.8 bp · R EV +0.09 (adj +0.05) on $1.00, P(profit) 0.3548, adj growth 1.8 bp

## MIN @ PHI  ·  10000 joint draws  ·  412 bet sides mapped, 27 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_MIN_win | p_overtime | goals | shots PHI/MIN | PHI/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.53 | 0.47 | 0.00 | 5.98 | 27.1/27.4 | 24.1/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.48 | 5.85 | 27.1/27.4 | 24.1/23.9 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.46 | 0.54 | 0.47 | 5.87 | 21.7/32.6 | 29.2/18.5 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.085 | 0.48 | 0.52 | 0.00 | 5.96 | 21.6/32.6 | 28.7/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.53 | 0.47 | 0.00 | 9.17 | 28.4/28.7 | 23.1/22.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.52 | 0.48 | 0.00 | 3.43 | 25.8/26.0 | 24.2/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Christian Dvorak: 1+ goals YES | 16 | 0.220 | 0.202 | +0.051 | +0.033 | $4.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Philadelphia wins by over 1.5 goals YES | 20 | 0.293 | 0.244 | +0.082 | +0.033 | $3.15 | FUNDED_RESEARCH | $1 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Matt Boldy: 1+ goals NO | 63 | 0.687 | 0.670 | +0.041 | +0.024 | $5.66 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Travis Konecny: 1+ assists NO | 68 | 0.754 | 0.709 | +0.059 | +0.014 | $8.50 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: higher confidence-adjusted growth (16.64 vs 13.81 bp); despite a smaller raw edge (+0.050 vs +0.082/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.935 vs 0.538); relationships: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26NOV03MINPHI-PHITKONECNY11-1|no: INTENTIONAL_DIVERSIFIER (phi -0.248); failure: PHI offense suppressed (<= 2 goals)
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLSPREAD-26NOV03MINPHI-PHI3|yes; why: higher confidence-adjusted growth (13.81 vs 6.71 bp); relationships: KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: REINFORCING (phi 0.192); KXNHLAST-26NOV03MINPHI-PHITKONECNY11-1|no: INTENTIONAL_DIVERSIFIER (phi -0.137); failure: MIN wins (incl. OT/SO)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV03MINPHI-MINKKAPRIZOV97-2|no; why: KXNHLGOAL-26NOV03MINPHI-MINKKAPRIZOV97-2|no has the higher standalone adjusted growth (17.36 vs 5.64 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.009); relationships: KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: REINFORCING (phi 0.192); KXNHLAST-26NOV03MINPHI-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: MIN offense succeeds (4+ goals)
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV03MINPHI-PHITKONECNY11-2|no; why: higher confidence-adjusted growth (2.08 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.248); KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: INTENTIONAL_DIVERSIFIER (phi -0.137); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.09.
- thesis MIN:SUPPRESSED (p 0.4441): highest fidelity KXNHLSPREAD-26NOV03MINPHI-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.363): highest fidelity KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2927): highest fidelity KXNHLSPREAD-26NOV03MINPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes (same contract)
- KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4135, phi -0.213)
- KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.4815, phi -0.62)
- KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3357, phi -0.279)
- KXNHLAST-26NOV03MINPHI-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.363, phi -0.214)

portfolios: A EV +4.38 (adj +0.54) on $14.56, P(profit) 0.6368, adj growth 4.5 bp · B EV +3.49 (adj +1.66) on $21.35, P(profit) 0.4115, adj growth 15.7 bp · C EV +4.22 (adj +1.66) on $32.75, P(profit) 0.3726, adj growth 15.4 bp · R EV +0.51 (adj +0.23) on $3.00, P(profit) 0.7384, adj growth 8.6 bp
equivalent contracts collapsed: KXNHLGAME-26NOV03MINPHI-MIN|no == KXNHLGAME-26NOV03MINPHI-PHI|yes

## VGK @ PIT  ·  10000 joint draws  ·  400 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_VGK_win | p_overtime | goals | shots PIT/VGK | PIT/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.53 | 0.47 | 0.00 | 6.0 | 27.2/27.1 | 23.7/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.50 | 0.50 | 0.46 | 5.97 | 27.4/27.3 | 24.0/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.53 | 0.47 | 0.00 | 9.38 | 29.0/29.1 | 23.3/22.5 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.069 | 0.58 | 0.42 | 0.00 | 6.0 | 31.9/21.4 | 18.4/27.5 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.55 | 0.45 | 0.45 | 5.91 | 32.2/21.9 | 18.8/28.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.065 | 0.49 | 0.51 | 0.00 | 6.05 | 21.8/31.8 | 27.9/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 13 | 0.167 | 0.155 | +0.029 | +0.017 | $2.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ assists NO | 53 | 0.616 | 0.568 | +0.068 | +0.020 | $4.81 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Ville Koivunen: 1+ goals NO | 82 | 0.854 | 0.843 | +0.024 | +0.013 | $7.89 | FUNDED_RESEARCH | $2 | PIT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Mark Stone: 1+ assists NO | 56 | 0.626 | 0.588 | +0.049 | +0.011 | $2.73 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV03VGKPIT-VGK2|no; why: higher confidence-adjusted growth (5.37 vs 0.09 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.877 vs 0.611); alternative not eligible: confidence-adjusted EV +0.0024 below the 0.010/contract floor; relationships: KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26NOV03VGKPIT-PITVKOIVUNEN41-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26NOV03VGKPIT-VGKMSTONE61-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV03VGKPIT-PITSCROSBY87-1|no; why: higher confidence-adjusted growth (3.67 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26NOV03VGKPIT-PITVKOIVUNEN41-1|no: MOSTLY_INDEPENDENT (phi 0.072); KXNHLAST-26NOV03VGKPIT-VGKMSTONE61-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: PIT offense succeeds (4+ goals)
- **Ville Koivunen: 1+ goals NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no; why: second expression of the same thesis: KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no has the higher standalone adjusted growth (3.67 vs 2.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.072); they share one thesis budget; relationships: KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no: MOSTLY_INDEPENDENT (phi 0.072); KXNHLAST-26NOV03VGKPIT-VGKMSTONE61-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: PIT offense succeeds (4+ goals)
- **Mark Stone: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV03VGKPIT-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (1.05 vs 0.77 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV03VGKPIT-PITVKOIVUNEN41-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:SUPPRESSED (p 0.3607): highest fidelity KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no (same contract)
- thesis VGK:SUPPRESSED (p 0.391): highest fidelity KXNHLAST-26NOV03VGKPIT-VGKMSTONE61-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV03VGKPIT-VGKMSTONE61-1|no (same contract)
- thesis PIT:WINS_BY_2PLUS (p 0.3005): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3607, phi -0.198)
- KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4255, phi -0.256)
- KXNHLGOAL-26NOV03VGKPIT-PITVKOIVUNEN41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4255, phi -0.172)
- KXNHLAST-26NOV03VGKPIT-VGKMSTONE61-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3943, phi -0.282)

portfolios: A EV +1.39 (adj +0.53) on $14.56, P(profit) 0.4838, adj growth 5.0 bp · B EV +1.48 (adj +0.60) on $17.44, P(profit) 0.6152, adj growth 5.7 bp · C EV +1.32 (adj +0.37) on $11.99, P(profit) 0.6156, adj growth 3.4 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.8542, adj growth 1.2 bp

## DAL @ WSH  ·  10000 joint draws  ·  402 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_DAL_win | p_overtime | goals | shots WSH/DAL | WSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.58 | 0.42 | 0.00 | 6.0 | 25.9/26.0 | 22.9/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.52 | 0.48 | 0.46 | 5.9 | 26.3/26.4 | 23.1/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.59 | 0.41 | 0.00 | 9.23 | 27.4/27.4 | 21.9/21.0 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.074 | 0.50 | 0.50 | 0.00 | 5.96 | 20.7/31.0 | 27.1/17.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.45 | 0.55 | 0.47 | 5.93 | 20.8/31.2 | 27.8/17.7 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.068 | 0.61 | 0.39 | 0.00 | 5.96 | 30.6/20.6 | 17.9/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 17 | 0.232 | 0.214 | +0.052 | +0.034 | $4.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 16 | 0.211 | 0.197 | +0.042 | +0.028 | $3.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Miro Heiskanen: 1+ goals NO | 87 | 0.904 | 0.894 | +0.026 | +0.016 | $8.54 | FUNDED_RESEARCH | $3 | DAL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Arttu Hyry: 1+ goals YES | 12 | 0.151 | 0.142 | +0.024 | +0.015 | $1.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03DALWSH-WSH5|yes; why: higher confidence-adjusted growth (16.75 vs 0.33 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.868 vs 0.527); alternative not eligible: confidence-adjusted EV +0.0049 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03DALWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.032); failure: WSH offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (16.75 vs 11.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: WSH offense suppressed (<= 2 goals)
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03DALWSH-DALMHEISKANEN4-2|no; why: higher confidence-adjusted growth (5.37 vs 0.84 bp); despite a smaller raw edge (+0.026 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV03DALWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: DAL offense succeeds (4+ goals)
- **Arttu Hyry: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV03DALWSH-2|yes; why: higher confidence-adjusted growth (4.15 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26NOV03DALWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4067): highest fidelity KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes (same contract)
- thesis DAL:OFFENSE_4PLUS (p 0.342): highest fidelity KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes (same contract)
- thesis DAL:SUPPRESSED (p 0.4355): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3799, phi -0.235)
- KXNHLGOAL-26NOV03DALWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3799, phi -0.209)
- KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.342, phi -0.153)
- KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.4355, phi -0.201)

portfolios: A EV +2.51 (adj +1.63) on $14.56, P(profit) 0.4816, adj growth 15.4 bp · B EV +2.62 (adj +1.70) on $17.87, P(profit) 0.4816, adj growth 16.0 bp · C EV +2.36 (adj +1.53) on $9.17, P(profit) 0.3526, adj growth 13.9 bp · R EV +0.09 (adj +0.06) on $3.00, P(profit) 0.9037, adj growth 2.1 bp

## COL @ CBJ  ·  10000 joint draws  ·  408 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_COL_win | p_overtime | goals | shots CBJ/COL | CBJ/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.50 | 0.50 | 0.00 | 6.04 | 27.9/28.3 | 24.6/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.48 | 5.91 | 28.1/28.5 | 25.3/24.8 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.091 | 0.43 | 0.57 | 0.00 | 6.01 | 22.4/33.7 | 29.5/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.52 | 0.48 | 0.00 | 9.25 | 29.4/29.8 | 23.9/23.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.47 | 0.53 | 0.49 | 5.94 | 22.4/33.7 | 30.1/19.2 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.062 | 0.43 | 0.57 | 0.00 | 9.16 | 23.7/35.4 | 28.9/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cole Sillinger: 1+ goals YES | 13 | 0.164 | 0.153 | +0.026 | +0.015 | $1.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Sean Monahan: 1+ goals YES | 15 | 0.184 | 0.175 | +0.025 | +0.016 | $1.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Brock Nelson: 1+ goals NO | 77 | 0.811 | 0.799 | +0.029 | +0.017 | $8.54 | FUNDED_RESEARCH | $3 | COL:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 15 | 0.177 | 0.169 | +0.018 | +0.010 | $1.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Cole Sillinger: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes; why: higher confidence-adjusted growth (4.10 vs 3.96 bp); relationships: KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV03COLCBJ-COLBNELSON11-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: CBJ offense suppressed (<= 2 goals)
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes has the higher standalone adjusted growth (4.10 vs 3.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV03COLCBJ-COLBNELSON11-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: CBJ offense suppressed (<= 2 goals)
- **Brock Nelson: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV03COLCBJ-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (3.78 vs 0.17 bp); alternative not eligible: confidence-adjusted EV +0.0042 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: COL offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes has the higher standalone adjusted growth (4.10 vs 1.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.022); they share one thesis budget; relationships: KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV03COLCBJ-COLBNELSON11-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3852): highest fidelity KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.3911): highest fidelity KXNHLGOAL-26NOV03COLCBJ-COLBNELSON11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV03COLCBJ-COLBNELSON11-1|no (same contract)
- KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.404, phi -0.197)
- KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.404, phi -0.204)
- KXNHLGOAL-26NOV03COLCBJ-COLBNELSON11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3831, phi -0.188)
- KXNHLGOAL-26NOV03COLCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.404, phi -0.212)

portfolios: A EV +1.04 (adj +0.61) on $14.56, P(profit) 0.3102, adj growth 5.8 bp · B EV +1.07 (adj +0.63) on $13.29, P(profit) 0.3692, adj growth 6.0 bp · C EV +0.99 (adj +0.58) on $15.89, P(profit) 0.8424, adj growth 5.3 bp · R EV +0.11 (adj +0.07) on $3.00, P(profit) 0.811, adj growth 2.4 bp

## EDM @ NJD  ·  10000 joint draws  ·  410 bet sides mapped, 14 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_EDM_win | p_overtime | goals | shots NJD/EDM | NJD/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.50 | 0.50 | 0.00 | 6.07 | 28.1/27.9 | 24.3/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.47 | 0.53 | 0.45 | 5.95 | 28.0/27.7 | 24.3/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.49 | 0.51 | 0.00 | 9.41 | 29.9/29.4 | 23.1/23.5 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.097 | 0.55 | 0.45 | 0.00 | 6.05 | 33.6/22.2 | 18.9/29.5 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.50 | 0.50 | 0.49 | 5.99 | 33.7/22.2 | 18.9/30.2 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.081 | 0.57 | 0.43 | 0.00 | 9.46 | 34.9/23.5 | 18.1/27.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 10 | 0.158 | 0.142 | +0.051 | +0.036 | $3.71 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Filip Hallander: 1+ goals YES | 9 | 0.128 | 0.115 | +0.033 | +0.019 | $1.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 23 | 0.284 | 0.268 | +0.042 | +0.026 | $3.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 65 | 0.734 | 0.689 | +0.068 | +0.023 | $7.60 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (28.41 vs 7.83 bp); relationships: KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26NOV03EDMNJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: EDM offense suppressed (<= 2 goals)
- **Filip Hallander: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (9.09 vs 7.83 bp); despite a smaller raw edge (+0.032 vs +0.042/contract); relationships: KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV03EDMNJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes; why: higher confidence-adjusted growth (7.83 vs 6.03 bp); despite a smaller raw edge (+0.042 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.902 vs 0.539); relationships: KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV03EDMNJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: EDM offense suppressed (<= 2 goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV03EDMNJ-EDM2|yes; why: higher confidence-adjusted growth (5.39 vs 2.38 bp); wins across more scripts (relative breadth 1.024 vs 0.545); relationships: KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4195): highest fidelity KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS_BY_2PLUS (p 0.2881): highest fidelity KXNHLSPREAD-26NOV03EDMNJ-EDM2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3106): highest fidelity KXNHLTOTAL-26NOV03EDMNJ-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3604, phi -0.168)
- KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3604, phi -0.153)
- KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3604, phi -0.249)
- KXNHLAST-26NOV03EDMNJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4214, phi -0.225)

portfolios: A EV +2.67 (adj +0.54) on $14.56, P(profit) 0.7073, adj growth 5.1 bp · B EV +3.81 (adj +2.26) on $16.60, P(profit) 0.418, adj growth 21.2 bp · C EV +4.93 (adj +1.64) on $27.64, P(profit) 0.6133, adj growth 15.1 bp · R EV +0.48 (adj +0.34) on $1.00, P(profit) 0.1577, adj growth 12.5 bp

## CAR @ NSH  ·  10000 joint draws  ·  392 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_CAR_win | p_overtime | goals | shots NSH/CAR | NSH/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.145 | 0.38 | 0.62 | 0.00 | 6.05 | 21.5/34.4 | 30.0/18.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.46 | 0.54 | 0.48 | 5.99 | 22.0/34.8 | 31.1/18.8 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.110 | 0.35 | 0.65 | 0.00 | 9.34 | 23.0/36.5 | 28.5/18.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.094 | 0.48 | 0.52 | 0.00 | 6.06 | 27.6/28.6 | 24.9/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.49 | 0.51 | 0.46 | 6.0 | 27.6/28.6 | 25.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.44 | 0.56 | 0.00 | 9.39 | 29.1/30.3 | 23.6/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack Drury: 1+ goals YES | 9 | 0.130 | 0.119 | +0.034 | +0.023 | $2.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 13 | 0.173 | 0.160 | +0.035 | +0.022 | $2.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 67 | 0.720 | 0.705 | +0.034 | +0.019 | $5.98 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 71 | 0.781 | 0.743 | +0.056 | +0.018 | $4.61 | FUNDED_RESEARCH | $2 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Jack Drury: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: higher confidence-adjusted growth (12.89 vs 9.55 bp); despite a smaller raw edge (+0.034 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.947 vs 0.374); relationships: KXNHLGOAL-26NOV03CARNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV03CARNSH-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26NOV03CARNSH-CAR3|no: MOSTLY_INDEPENDENT (phi 0.102); failure: NSH offense suppressed (<= 2 goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes has the higher standalone adjusted growth (9.55 vs 8.52 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.164); relationships: KXNHLGOAL-26NOV03CARNSH-NSHJDRURY18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV03CARNSH-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26NOV03CARNSH-CAR3|no: MOSTLY_INDEPENDENT (phi 0.102); failure: NSH offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03CARNSH-CARSAHO20-1|no; why: KXNHLAST-26NOV03CARNSH-CARSAHO20-1|no has the higher standalone adjusted growth (4.95 vs 3.79 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.007); relationships: KXNHLGOAL-26NOV03CARNSH-NSHJDRURY18-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV03CARNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26NOV03CARNSH-CAR3|no: MOSTLY_INDEPENDENT (phi 0.133); failure: CAR offense succeeds (4+ goals)
- **Carolina wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: Broad expression KXNHLSPREAD-26NOV03CARNSH-CAR3|no selected over player prop KXNHLAST-26NOV03CARNSH-CARSAHO20-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV03CARNSH-NSHJDRURY18-1|yes: MOSTLY_INDEPENDENT (phi 0.102); KXNHLGOAL-26NOV03CARNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.102); KXNHLGOAL-26NOV03CARNSH-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.133); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, CAR shot control · high event (8+) · decided (2+) 0.11.
- thesis NSH:OFFENSE_4PLUS (p 0.3815): highest fidelity KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV03CARNSH-NSHAEDSTROM84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3104): highest fidelity KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes (same contract)
- thesis NSH:WINS (p 0.4426): highest fidelity KXNHLSPREAD-26NOV03CARNSH-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV03CARNSH-NSHJDRURY18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3979, phi -0.173)
- KXNHLGOAL-26NOV03CARNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3979, phi -0.208)
- KXNHLGOAL-26NOV03CARNSH-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.459, phi -0.221)
- KXNHLSPREAD-26NOV03CARNSH-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3383, phi -0.741)
- override: Broad expression KXNHLSPREAD-26NOV03CARNSH-CAR3|no selected over player prop KXNHLAST-26NOV03CARNSH-CARSAHO20-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.24 (adj +0.60) on $14.56, P(profit) 0.608, adj growth 5.6 bp · B EV +2.09 (adj +1.22) on $15.30, P(profit) 0.2801, adj growth 11.5 bp · C EV +3.36 (adj +0.93) on $10.75, P(profit) 0.6803, adj growth 8.5 bp · R EV +0.26 (adj +0.11) on $4.00, P(profit) 0.5865, adj growth 4.0 bp

## ANA @ VAN  ·  10000 joint draws  ·  390 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_ANA_win | p_overtime | goals | shots VAN/ANA | VAN/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.126 | 0.40 | 0.60 | 0.00 | 6.06 | 21.5/33.5 | 29.3/18.4 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.112 | 0.39 | 0.61 | 0.00 | 9.42 | 23.3/35.5 | 28.0/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.46 | 0.54 | 0.00 | 9.54 | 28.9/29.9 | 23.3/22.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.49 | 0.51 | 0.00 | 6.07 | 27.0/27.6 | 24.2/23.4 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.49 | 0.51 | 0.48 | 6.0 | 21.8/33.7 | 30.2/18.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.51 | 0.49 | 0.47 | 6.05 | 27.4/28.3 | 24.9/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Washe: 1+ goals YES | 12 | 0.159 | 0.147 | +0.032 | +0.019 | $2.21 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 20 | 0.244 | 0.231 | +0.033 | +0.019 | $2.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 21 | 0.256 | 0.240 | +0.034 | +0.019 | $2.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 17 | 0.207 | 0.195 | +0.027 | +0.015 | $1.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV03ANAVAN-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (7.32 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV03ANAVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (4.85 vs 4.50 bp); despite a smaller raw edge (+0.033 vs +0.034/contract); relationships: KXNHLGOAL-26NOV03ANAVAN-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV03ANAVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes has the higher standalone adjusted growth (4.85 vs 4.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV03ANAVAN-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV03ANAVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: VAN offense suppressed (<= 2 goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes has the higher standalone adjusted growth (4.85 vs 3.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV03ANAVAN-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, ANA shot control · high event (8+) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4302): highest fidelity KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:SUPPRESSED (p 0.3142): highest fidelity KXNHLGOAL-26NOV03ANAVAN-ANACGAUTHIER61-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV03ANAVAN-ANACGAUTHIER61-1|no (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4822): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV03ANAVAN-ANATWASHE42-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3142, phi -0.153)
- KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3559, phi -0.231)
- KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3559, phi -0.237)
- KXNHLGOAL-26NOV03ANAVAN-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3559, phi -0.21)

portfolios: A EV +1.89 (adj +1.08) on $14.34, P(profit) 0.4688, adj growth 10.0 bp · B EV +1.58 (adj +0.93) on $8.95, P(profit) 0.6233, adj growth 8.7 bp · C EV +0.89 (adj +0.49) on $9.87, P(profit) 0.725, adj growth 4.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
