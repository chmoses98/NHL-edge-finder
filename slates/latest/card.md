# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-03T14:52:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +24.41 | +9.62 | +23.08 | 0.739 | -21.42 | -33.79 | 89.44 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +23.54 | +12.82 | +21.67 | 0.715 | -25.21 | -37.20 | 120.52 |
| C best expression per thesis | 150.02 | +24.75 | +10.73 | +21.81 | 0.699 | -28.06 | -41.10 | 98.16 |
| R FUNDED research stakes | 22.00 | +2.42 | +1.35 | +1.03 | 0.531 | -6.44 | -7.17 | 0.00 |

## UTA @ TOR  ·  10000 joint draws  ·  430 bet sides mapped, 8 +EV candidates, 4 on card


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
| Teddy Blueger: 1+ goals YES | 11 | 0.177 | 0.159 | +0.060 | +0.042 | $4.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 11 | 0.151 | 0.140 | +0.034 | +0.023 | $2.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 64 | 0.694 | 0.679 | +0.037 | +0.023 | $6.85 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 18 | 0.221 | 0.208 | +0.030 | +0.018 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26NOV03UTATOR-TORMRIELLY44-1|yes; why: higher confidence-adjusted growth (36.84 vs 4.70 bp); despite a smaller raw edge (+0.060 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV03UTATOR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: TOR offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (10.66 vs 4.33 bp); relationships: KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: UTA offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV03UTATOR-UTALCOOLEY92-1|no; why: higher confidence-adjusted growth (5.04 vs 1.30 bp); relationships: KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV03UTATOR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: UTA offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03UTATOR-UTAALEE72-1|yes; why: higher confidence-adjusted growth (4.33 vs 1.13 bp); alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV03UTATOR-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.4435): highest fidelity KXNHLAST-26NOV03UTATOR-TORMRIELLY44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.3383): highest fidelity KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.4331): highest fidelity KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes (same contract)
- KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3454, phi -0.212)
- KXNHLGOAL-26NOV03UTATOR-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3383, phi -0.165)
- KXNHLGOAL-26NOV03UTATOR-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4331, phi -0.24)
- KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3383, phi -0.208)

portfolios: A EV +3.08 (adj +1.70) on $15.14, P(profit) 0.4419, adj growth 16.0 bp · B EV +3.85 (adj +2.60) on $16.17, P(profit) 0.4106, adj growth 24.3 bp · C EV +4.56 (adj +3.08) on $20.13, P(profit) 0.3062, adj growth 27.9 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.6935, adj growth 2.6 bp

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
| Dylan Samberg: 1+ goals YES | 4 | 0.065 | 0.056 | +0.022 | +0.013 | $1.27 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Oliver Kapanen: 1+ goals YES | 15 | 0.192 | 0.180 | +0.033 | +0.022 | $2.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Phillip Danault: 1+ goals YES | 14 | 0.174 | 0.164 | +0.025 | +0.016 | $1.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 20 | 0.238 | 0.228 | +0.027 | +0.016 | $2.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Dylan Samberg: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26NOV03WPGMTL-WPGCPERFETTI91-1|yes; why: higher confidence-adjusted growth (9.00 vs 3.98 bp); despite a smaller raw edge (+0.022 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV03WPGMTL-MTLOKAPANEN91-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV03WPGMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: WPG offense suppressed (<= 2 goals)
- **Oliver Kapanen: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes; why: higher confidence-adjusted growth (7.50 vs 4.21 bp); relationships: KXNHLGOAL-26NOV03WPGMTL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV03WPGMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: MTL offense suppressed (<= 2 goals)
- **Phillip Danault: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLGOAL-26NOV03WPGMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (4.21 vs 3.20 bp); relationships: KXNHLGOAL-26NOV03WPGMTL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV03WPGMTL-MTLOKAPANEN91-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV03WPGMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: MTL offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes has the higher standalone adjusted growth (4.21 vs 3.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV03WPGMTL-WPGDSAMBERG54-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV03WPGMTL-MTLOKAPANEN91-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MTL:OFFENSE_4PLUS (p 0.4455): highest fidelity KXNHLGOAL-26NOV03WPGMTL-MTLJANDERSON17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03WPGMTL-MTLJANDERSON17-1|yes (same contract)
- thesis MTL:WINS_BY_2PLUS (p 0.3532): highest fidelity KXNHLGOAL-26NOV03WPGMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3258): highest fidelity KXNHLAST-26NOV03WPGMTL-WPGCPERFETTI91-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV03WPGMTL-WPGCPERFETTI91-1|yes (same contract)
- KXNHLGOAL-26NOV03WPGMTL-WPGDSAMBERG54-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4533, phi -0.115)
- KXNHLGOAL-26NOV03WPGMTL-MTLOKAPANEN91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3367, phi -0.18)
- KXNHLGOAL-26NOV03WPGMTL-MTLPDANAULT24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3367, phi -0.194)
- KXNHLGOAL-26NOV03WPGMTL-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3367, phi -0.217)

portfolios: A EV +2.50 (adj +1.23) on $13.93, P(profit) 0.5844, adj growth 11.3 bp · B EV +1.80 (adj +1.12) on $7.97, P(profit) 0.526, adj growth 10.5 bp · C EV +1.29 (adj +0.56) on $7.08, P(profit) 0.4844, adj growth 5.2 bp · R EV +0.51 (adj +0.31) on $1.00, P(profit) 0.0645, adj growth 9.8 bp

## DET @ TBL  ·  10000 joint draws  ·  404 bet sides mapped, 6 +EV candidates, 4 on card


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
| Charle-Edouard D'Astous: 1+ goals NO | 87 | 0.922 | 0.906 | +0.044 | +0.028 | $8.68 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ assists NO | 35 | 0.476 | 0.388 | +0.110 | +0.022 | $2.89 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 65 | 0.716 | 0.680 | +0.050 | +0.014 | $4.14 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Lucas Raymond: 1+ assists NO | 60 | 0.672 | 0.631 | +0.055 | +0.014 | $4.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (16.82 vs 4.46 bp); despite a smaller raw edge (+0.044 vs +0.110/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.072); KXNHLSPREAD-26NOV03DETTB-TB3|no: MOSTLY_INDEPENDENT (phi 0.087); KXNHLAST-26NOV03DETTB-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-2|no; why: higher confidence-adjusted growth (4.46 vs 2.67 bp); relationships: KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.072); KXNHLSPREAD-26NOV03DETTB-TB3|no: REINFORCING (phi 0.204); KXNHLAST-26NOV03DETTB-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV03DETTB-TB2|no; why: higher confidence-adjusted growth (2.05 vs 1.37 bp); wins across more scripts (relative breadth 1.015 vs 0.859); relationships: KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.087); KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.204); KXNHLAST-26NOV03DETTB-DETLRAYMOND23-1|no: INTENTIONAL_DIVERSIFIER (phi -0.133); failure: TBL wins by 2+
- **Lucas Raymond: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV03DETTB-DETLRAYMOND23-2|no; why: higher confidence-adjusted growth (1.84 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26NOV03DETTB-TB3|no: INTENTIONAL_DIVERSIFIER (phi -0.133); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TBL:SUPPRESSED (p 0.3055): highest fidelity KXNHLSPREAD-26NOV03DETTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4097): highest fidelity KXNHLSPREAD-26NOV03DETTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03DETTB-TB3|no (same contract)
- thesis DET:SUPPRESSED (p 0.5025): highest fidelity KXNHLAST-26NOV03DETTB-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV03DETTB-DETLRAYMOND23-1|no (same contract)
- KXNHLGOAL-26NOV03DETTB-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4886, phi -0.119)
- KXNHLAST-26NOV03DETTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.6 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4886, phi -0.294)
- KXNHLSPREAD-26NOV03DETTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4151, phi -0.748)
- KXNHLAST-26NOV03DETTB-DETLRAYMOND23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.2847, phi -0.259)

portfolios: A EV +2.21 (adj +0.47) on $15.14, P(profit) 0.6304, adj growth 4.4 bp · B EV +2.03 (adj +0.65) on $20.40, P(profit) 0.6298, adj growth 6.3 bp · C EV +2.41 (adj +0.56) on $17.66, P(profit) 0.6609, adj growth 5.1 bp · R EV +0.30 (adj +0.14) on $5.00, P(profit) 0.6702, adj growth 5.4 bp

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
| Tye Kartye: 1+ goals YES | 16 | 0.199 | 0.186 | +0.029 | +0.017 | $2.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Alexis Lafreniere: 1+ goals YES | 31 | 0.355 | 0.341 | +0.030 | +0.016 | $2.53 | FUNDED_RESEARCH | $1 | NYR:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Tye Kartye: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes; why: higher confidence-adjusted growth (4.51 vs 2.59 bp); despite a smaller raw edge (+0.029 vs +0.030/contract); relationships: KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: NYR offense suppressed (<= 2 goals)
- **Alexis Lafreniere: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-2|yes; why: higher confidence-adjusted growth (2.59 vs 0.60 bp); wins across more scripts (relative breadth 0.906 vs 0.709); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03STLNYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NYR:OFFENSE_4PLUS (p 0.4098): highest fidelity KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes (same contract)
- KXNHLGOAL-26NOV03STLNYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3712, phi -0.193)
- KXNHLGOAL-26NOV03STLNYR-NYRALAFRENIERE13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3712, phi -0.294)

portfolios: A EV +0.77 (adj +0.44) on $6.01, P(profit) 0.483, adj growth 4.0 bp · B EV +0.60 (adj +0.34) on $4.65, P(profit) 0.483, adj growth 3.2 bp · C EV +0.34 (adj +0.18) on $3.68, P(profit) 0.3548, adj growth 1.7 bp · R EV +0.09 (adj +0.05) on $1.00, P(profit) 0.3548, adj growth 1.8 bp

## MIN @ PHI  ·  10000 joint draws  ·  412 bet sides mapped, 25 +EV candidates, 4 on card


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
| Philadelphia wins by over 1.5 goals YES | 20 | 0.293 | 0.244 | +0.082 | +0.033 | $3.37 | FUNDED_RESEARCH | $1 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Christian Dvorak: 1+ goals YES | 17 | 0.220 | 0.205 | +0.040 | +0.025 | $3.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Matt Boldy: 1+ goals NO | 63 | 0.687 | 0.670 | +0.041 | +0.024 | $5.74 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Travis Konecny: 1+ assists NO | 68 | 0.754 | 0.707 | +0.059 | +0.012 | $8.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2|no; why: higher confidence-adjusted growth (13.81 vs 11.17 bp); relationships: KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: REINFORCING (phi 0.192); KXNHLAST-26NOV03MINPHI-PHITKONECNY11-1|no: INTENTIONAL_DIVERSIFIER (phi -0.137); failure: MIN wins (incl. OT/SO)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes has the higher standalone adjusted growth (13.81 vs 9.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.146); they share one thesis budget; relationships: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26NOV03MINPHI-PHITKONECNY11-1|no: INTENTIONAL_DIVERSIFIER (phi -0.248); failure: PHI offense suppressed (<= 2 goals)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes has the higher standalone adjusted growth (13.81 vs 5.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.192); they share one thesis budget; relationships: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: REINFORCING (phi 0.192); KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26NOV03MINPHI-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: MIN offense succeeds (4+ goals)
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03MINPHI-PHIOTIPPETT74-1|no; why: higher confidence-adjusted growth (1.41 vs 0.06 bp); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: INTENTIONAL_DIVERSIFIER (phi -0.137); KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.248); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.09.
- thesis PHI:WINS_BY_2PLUS (p 0.2927): highest fidelity KXNHLSPREAD-26NOV03MINPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.4441): highest fidelity KXNHLSPREAD-26NOV03MINPHI-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.363): highest fidelity KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.4815, phi -0.62)
- KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4135, phi -0.213)
- KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3357, phi -0.279)
- KXNHLAST-26NOV03MINPHI-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.363, phi -0.214)

portfolios: A EV +3.69 (adj +0.55) on $15.14, P(profit) 0.6334, adj growth 5.0 bp · B EV +3.12 (adj +1.33) on $21.03, P(profit) 0.7011, adj growth 12.6 bp · C EV +3.10 (adj +1.08) on $15.28, P(profit) 0.2927, adj growth 9.9 bp · R EV +0.51 (adj +0.23) on $3.00, P(profit) 0.7384, adj growth 8.6 bp
equivalent contracts collapsed: KXNHLGAME-26NOV03MINPHI-MIN|no == KXNHLGAME-26NOV03MINPHI-PHI|yes

## VGK @ PIT  ·  10000 joint draws  ·  400 bet sides mapped, 3 +EV candidates, 3 on card


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
| Connor Dewar: 1+ goals YES | 13 | 0.167 | 0.156 | +0.029 | +0.018 | $2.21 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ assists NO | 53 | 0.616 | 0.568 | +0.068 | +0.020 | $5.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Mark Stone: 1+ assists NO | 56 | 0.626 | 0.588 | +0.049 | +0.011 | $2.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLAST-26NOV03VGKPIT-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (6.17 vs 0.00 bp); despite a smaller raw edge (+0.029 vs +0.077/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no: MOSTLY_INDEPENDENT (phi -0.03); KXNHLAST-26NOV03VGKPIT-VGKMSTONE61-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV03VGKPIT-PITSCROSBY87-1|no; why: higher confidence-adjusted growth (3.67 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.03); KXNHLAST-26NOV03VGKPIT-VGKMSTONE61-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: PIT offense succeeds (4+ goals)
- **Mark Stone: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV03VGKPIT-VGKMMARNER93-1|no; why: evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:SUPPRESSED (p 0.3607): highest fidelity KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no (same contract)
- thesis VGK:SUPPRESSED (p 0.391): highest fidelity KXNHLAST-26NOV03VGKPIT-VGKMSTONE61-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV03VGKPIT-VGKMSTONE61-1|no (same contract)
- thesis PIT:WINS_BY_2PLUS (p 0.3005): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3607, phi -0.198)
- KXNHLAST-26NOV03VGKPIT-PITSCROSBY87-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4255, phi -0.256)
- KXNHLAST-26NOV03VGKPIT-VGKMSTONE61-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3943, phi -0.283)

portfolios: A EV +1.79 (adj +0.68) on $14.65, P(profit) 0.4885, adj growth 6.3 bp · B EV +1.33 (adj +0.54) on $10.08, P(profit) 0.4885, adj growth 5.1 bp · C EV +1.25 (adj +0.35) on $11.36, P(profit) 0.6156, adj growth 3.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ WSH  ·  10000 joint draws  ·  402 bet sides mapped, 3 +EV candidates, 3 on card


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
| Aliaksei Protas: 1+ goals YES | 17 | 0.232 | 0.215 | +0.052 | +0.035 | $4.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Miro Heiskanen: 1+ goals NO | 87 | 0.904 | 0.894 | +0.026 | +0.016 | $8.68 | FUNDED_RESEARCH | $3 | DAL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Arttu Hyry: 1+ goals YES | 12 | 0.151 | 0.142 | +0.024 | +0.015 | $1.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03DALWSH-WSHAOVECHKIN8-1|yes; why: higher confidence-adjusted growth (18.00 vs 0.88 bp); alternative not eligible: confidence-adjusted EV +0.0085 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.032); failure: WSH offense suppressed (<= 2 goals)
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03DALWSH-DALWJOHNSTON53-1|no; why: higher confidence-adjusted growth (5.37 vs 0.89 bp); despite a smaller raw edge (+0.026 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: DAL offense succeeds (4+ goals)
- **Arttu Hyry: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV03DALWSH-2|yes; why: higher confidence-adjusted growth (4.15 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4067): highest fidelity KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes (same contract)
- thesis DAL:OFFENSE_4PLUS (p 0.342): highest fidelity KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes (same contract)
- thesis DAL:SUPPRESSED (p 0.4355): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3799, phi -0.235)
- KXNHLGOAL-26NOV03DALWSH-DALMHEISKANEN4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.342, phi -0.153)
- KXNHLGOAL-26NOV03DALWSH-DALAHYRY25-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.4355, phi -0.201)

portfolios: A EV +1.94 (adj +1.28) on $12.89, P(profit) 0.3526, adj growth 12.0 bp · B EV +1.86 (adj +1.23) on $14.89, P(profit) 0.3398, adj growth 11.6 bp · C EV +2.32 (adj +1.55) on $9.00, P(profit) 0.3526, adj growth 14.1 bp · R EV +0.09 (adj +0.06) on $3.00, P(profit) 0.9037, adj growth 2.1 bp

## COL @ CBJ  ·  10000 joint draws  ·  408 bet sides mapped, 4 +EV candidates, 4 on card


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
| Cole Sillinger: 1+ goals YES | 13 | 0.164 | 0.153 | +0.026 | +0.015 | $1.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Sean Monahan: 1+ goals YES | 15 | 0.184 | 0.175 | +0.025 | +0.016 | $1.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Brock Nelson: 1+ goals NO | 77 | 0.808 | 0.797 | +0.026 | +0.015 | $6.64 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ goals NO | 81 | 0.844 | 0.833 | +0.023 | +0.012 | $6.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
- **Cole Sillinger: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes; why: higher confidence-adjusted growth (4.10 vs 3.96 bp); relationships: KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV03COLCBJ-COLBNELSON11-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV03COLCBJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CBJ offense suppressed (<= 2 goals)
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes has the higher standalone adjusted growth (4.10 vs 3.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV03COLCBJ-COLBNELSON11-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV03COLCBJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense suppressed (<= 2 goals)
- **Brock Nelson: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV03COLCBJ-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (2.97 vs 0.16 bp); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV03COLCBJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: COL offense succeeds (4+ goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV03COLCBJ-COLBNELSON11-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV03COLCBJ-COLBNELSON11-1|no has the higher standalone adjusted growth (2.97 vs 2.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV03COLCBJ-COLBNELSON11-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: COL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3852): highest fidelity KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.3911): highest fidelity KXNHLGOAL-26NOV03COLCBJ-COLBNELSON11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV03COLCBJ-COLBNELSON11-1|no (same contract)
- KXNHLGOAL-26NOV03COLCBJ-CBJCSILLINGER4-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.404, phi -0.197)
- KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.404, phi -0.204)
- KXNHLGOAL-26NOV03COLCBJ-COLBNELSON11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3831, phi -0.192)
- KXNHLGOAL-26NOV03COLCBJ-COLCMAKAR8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3831, phi -0.177)

portfolios: A EV +1.06 (adj +0.62) on $15.14, P(profit) 0.3101, adj growth 5.8 bp · B EV +1.04 (adj +0.61) on $16.72, P(profit) 0.3101, adj growth 5.7 bp · C EV +0.86 (adj +0.50) on $13.95, P(profit) 0.8402, adj growth 4.6 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.8084, adj growth 1.5 bp

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
| Alex Formenton: 1+ goals YES | 10 | 0.158 | 0.142 | +0.051 | +0.036 | $3.86 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 23 | 0.284 | 0.268 | +0.042 | +0.026 | $4.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Filip Hallander: 1+ goals YES | 9 | 0.128 | 0.112 | +0.033 | +0.017 | $1.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 36 | 0.466 | 0.391 | +0.090 | +0.015 | $3.95 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.69) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (28.41 vs 7.83 bp); relationships: KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV03EDMNJ-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.043); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes; why: higher confidence-adjusted growth (7.83 vs 6.03 bp); despite a smaller raw edge (+0.042 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.902 vs 0.539); relationships: KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV03EDMNJ-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.224); failure: EDM offense suppressed (<= 2 goals)
- **Filip Hallander: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (7.83 vs 6.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV03EDMNJ-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV03EDMNJ-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (1.98 vs 0.96 bp); alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.043); KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.224); KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4195): highest fidelity KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS_BY_2PLUS (p 0.2881): highest fidelity KXNHLSPREAD-26NOV03EDMNJ-EDM2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3106): highest fidelity KXNHLTOTAL-26NOV03EDMNJ-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV03EDMNJ-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3604, phi -0.168)
- KXNHLGOAL-26NOV03EDMNJ-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3604, phi -0.249)
- KXNHLGOAL-26NOV03EDMNJ-EDMFHALLANDER11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3604, phi -0.153)
- KXNHLAST-26NOV03EDMNJ-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 31% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.6 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4195, phi -0.312)

portfolios: A EV +3.00 (adj +0.82) on $15.14, P(profit) 0.585, adj growth 7.7 bp · B EV +4.10 (adj +2.18) on $13.59, P(profit) 0.4722, adj growth 20.4 bp · C EV +4.58 (adj +1.49) on $25.16, P(profit) 0.6133, adj growth 13.7 bp · R EV +0.48 (adj +0.34) on $1.00, P(profit) 0.1577, adj growth 12.5 bp

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
| Jack Drury: 1+ goals YES | 9 | 0.130 | 0.119 | +0.034 | +0.023 | $2.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 13 | 0.173 | 0.160 | +0.035 | +0.022 | $2.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 67 | 0.720 | 0.705 | +0.034 | +0.019 | $6.08 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 71 | 0.781 | 0.743 | +0.056 | +0.018 | $4.69 | FUNDED_RESEARCH | $2 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
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

portfolios: A EV +2.33 (adj +0.63) on $15.14, P(profit) 0.608, adj growth 5.8 bp · B EV +2.12 (adj +1.24) on $15.55, P(profit) 0.2801, adj growth 11.6 bp · C EV +3.20 (adj +0.89) on $10.25, P(profit) 0.6803, adj growth 8.1 bp · R EV +0.26 (adj +0.11) on $4.00, P(profit) 0.5865, adj growth 4.0 bp

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
| Tim Washe: 1+ goals YES | 12 | 0.159 | 0.147 | +0.032 | +0.019 | $2.23 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 21 | 0.256 | 0.242 | +0.034 | +0.020 | $2.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 12 | 0.153 | 0.142 | +0.026 | +0.015 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 20 | 0.244 | 0.229 | +0.033 | +0.018 | $2.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV03ANAVAN-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (7.32 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV03ANAVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: ANA offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (5.12 vs 4.25 bp); relationships: KXNHLGOAL-26NOV03ANAVAN-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV03ANAVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (5.12 vs 4.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV03ANAVAN-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (5.12 vs 4.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV03ANAVAN-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV03ANAVAN-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, ANA shot control · high event (8+) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4302): highest fidelity KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4822): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV03ANAVAN-ANATWASHE42-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3142, phi -0.153)
- KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3559, phi -0.237)
- KXNHLGOAL-26NOV03ANAVAN-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3559, phi -0.162)
- KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3559, phi -0.231)

portfolios: A EV +2.05 (adj +1.20) on $11.69, P(profit) 0.6233, adj growth 11.1 bp · B EV +1.68 (adj +0.98) on $8.96, P(profit) 0.5995, adj growth 9.3 bp · C EV +0.84 (adj +0.49) on $16.47, P(profit) 0.2557, adj growth 4.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
