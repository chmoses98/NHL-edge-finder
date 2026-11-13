# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-13T01:26:17Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +25.54 | +11.58 | +12.59 | 0.655 | -39.54 | -64.65 | 94.61 |
| B thesis-diversified (joint) ← optimiser card | 61.20 | +19.15 | +10.66 | +16.81 | 0.560 | -31.17 | -34.90 | 93.08 |
| C best expression per thesis | 52.85 | +8.76 | +3.58 | +0.99 | 0.541 | -22.26 | -31.45 | 31.50 |
| R FUNDED research stakes | 5.00 | +1.98 | +1.36 | -5.00 | 0.346 | -5.00 | -5.00 | 0.00 |

## STL @ UTA  ·  10000 joint draws  ·  436 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.457 / away 0.543

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_STL_win | p_overtime | goals | shots UTA/STL | UTA/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.52 | 0.48 | 0.00 | 6.0 | 27.1/27.0 | 23.4/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.49 | 5.94 | 27.3/27.0 | 23.7/24.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.102 | 0.61 | 0.39 | 0.00 | 6.05 | 32.4/21.4 | 18.5/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.52 | 0.48 | 0.00 | 9.34 | 29.1/28.7 | 22.8/23.0 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.56 | 0.44 | 0.45 | 5.92 | 32.6/21.5 | 18.4/29.1 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.071 | 0.64 | 0.36 | 0.00 | 9.2 | 33.9/22.8 | 17.9/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 18 | 0.246 | 0.228 | +0.056 | +0.038 | $11.13 | FUNDED_RESEARCH | $3 | UTA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 13 | 0.182 | 0.168 | +0.044 | +0.030 | $8.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Ross Johnston: 1+ goals YES | 6 | 0.083 | 0.076 | +0.019 | +0.012 | $3.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Liam O'Brien: 1+ goals YES | 7 | 0.095 | 0.087 | +0.020 | +0.013 | $3.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-2|yes; why: higher confidence-adjusted growth (20.21 vs 5.43 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.902 vs 0.747); relationships: KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV12STLUTA-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV12STLUTA-UTALOBRIEN38-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: UTA offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (20.21 vs 16.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV12STLUTA-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26NOV12STLUTA-UTALOBRIEN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: UTA offense suppressed (<= 2 goals)
- **Ross Johnston: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes; why: higher confidence-adjusted growth (5.33 vs 0.80 bp); alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26NOV12STLUTA-UTALOBRIEN38-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: STL offense suppressed (<= 2 goals)
- **Liam O'Brien: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (20.21 vs 4.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV12STLUTA-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.4237): highest fidelity KXNHLSPREAD-26NOV12STLUTA-UTA2|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:WINS_BY_2PLUS (p 0.312): highest fidelity KXNHLSPREAD-26NOV12STLUTA-UTA2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12STLUTA-UTA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.3803): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.231)
- KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.187)
- KXNHLGOAL-26NOV12STLUTA-STLRJOHNSTON49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4013, phi -0.121)
- KXNHLGOAL-26NOV12STLUTA-UTALOBRIEN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.129)

portfolios: A EV +12.62 (adj +6.44) on $50.00, P(profit) 0.5801, adj growth 50.3 bp · B EV +7.68 (adj +5.13) on $25.54, P(profit) 0.4942, adj growth 44.2 bp · C EV +3.52 (adj +2.26) on $12.49, P(profit) 0.2462, adj growth 19.4 bp · R EV +0.88 (adj +0.60) on $3.00, P(profit) 0.2462, adj growth 20.4 bp

## NYI @ LAK  ·  10000 joint draws  ·  364 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.526 / away 0.474

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_NYI_win | p_overtime | goals | shots LAK/NYI | LAK/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 5.98 | 27.8/27.6 | 24.4/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.86 | 27.8/27.5 | 24.4/24.6 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.086 | 0.60 | 0.40 | 0.00 | 5.98 | 32.9/22.3 | 19.3/28.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.56 | 0.44 | 0.50 | 5.87 | 33.1/22.2 | 19.0/29.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.59 | 0.41 | 0.00 | 9.25 | 29.4/29.2 | 23.9/22.7 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.46 | 2.83 | 26.4/26.2 | 24.7/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Andre Lee: 1+ goals YES | 8 | 0.132 | 0.118 | +0.047 | +0.032 | $7.94 | FUNDED_RESEARCH | $2 | LAK:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 1+ assists NO | 65 | 0.851 | 0.717 | +0.185 | +0.051 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Joel Edmundson: 1+ goals YES | 6 | 0.083 | 0.076 | +0.019 | +0.012 | $2.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Trevor Moore: 1+ goals YES | 17 | 0.206 | 0.196 | +0.026 | +0.016 | $4.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12NYILA-LATMOORE12-1|yes; why: higher confidence-adjusted growth (28.42 vs 3.57 bp); relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV12NYILA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: LAK offense suppressed (<= 2 goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no; why: higher confidence-adjusted growth (25.96 vs 2.89 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.043); KXNHLGOAL-26NOV12NYILA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: LAK offense succeeds (4+ goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (5.20 vs 1.29 bp); despite a smaller raw edge (+0.019 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.043); KXNHLGOAL-26NOV12NYILA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: LAK offense suppressed (<= 2 goals)
- **Trevor Moore: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (3.57 vs 2.60 bp); despite a smaller raw edge (+0.026 vs +0.029/contract); relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.386): highest fidelity KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.395): highest fidelity KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no (same contract)
- thesis LAK:WINS_BY_2PLUS (p 0.3124): highest fidelity KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes (same contract)
- KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.16)
- KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.6 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.386, phi -0.181)
- KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.136)
- KXNHLGOAL-26NOV12NYILA-LATMOORE12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.209)

portfolios: A EV +12.92 (adj +5.14) on $50.00, P(profit) 0.7339, adj growth 44.3 bp · B EV +11.47 (adj +5.53) on $35.66, P(profit) 0.3433, adj growth 48.9 bp · C EV +5.23 (adj +1.32) on $40.36, P(profit) 0.7543, adj growth 12.1 bp · R EV +1.10 (adj +0.76) on $2.00, P(profit) 0.1318, adj growth 25.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
