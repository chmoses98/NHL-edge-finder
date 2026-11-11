# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-11T00:39:28Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +16.36 | +4.51 | -1.80 | 0.442 | -49.17 | -57.17 | 28.26 |
| B thesis-diversified (joint) ← optimiser card | 75.93 | +6.67 | +3.92 | +2.00 | 0.602 | -26.86 | -38.84 | 34.17 |
| C best expression per thesis | 48.66 | +3.39 | +1.78 | +4.19 | 0.531 | -24.68 | -34.48 | 15.58 |
| R FUNDED research stakes | 10.00 | +0.43 | +0.26 | +3.14 | 0.650 | -4.60 | -4.60 | 0.00 |

## DET @ STL  ·  10000 joint draws  ·  452 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.561 / away 0.439

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_DET_win | p_overtime | goals | shots STL/DET | STL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.65 | 0.35 | 0.00 | 6.02 | 27.2/27.5 | 24.7/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.53 | 0.47 | 0.48 | 5.89 | 27.0/27.3 | 24.1/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.66 | 0.34 | 0.00 | 9.3 | 28.6/28.8 | 23.3/21.5 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.073 | 0.62 | 0.38 | 0.00 | 5.97 | 21.8/32.5 | 29.5/18.0 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.49 | 0.51 | 0.50 | 5.88 | 21.8/32.4 | 29.1/18.5 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.064 | 0.71 | 0.29 | 0.00 | 6.01 | 31.4/21.6 | 19.1/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pius Suter: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $5.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Cam Fowler: 1+ goals NO | 92 | 0.947 | 0.939 | +0.022 | +0.014 | $20.00 | FUNDED_RESEARCH | $5 | STL:SUPPRESSED | DIRECT (0.98) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 26 | 0.301 | 0.290 | +0.028 | +0.016 | $5.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Andrew Copp: 1+ goals YES | 16 | 0.190 | 0.182 | +0.021 | +0.012 | $3.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (7.42 vs 2.84 bp); relationships: KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV10DETSTL-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: STL offense suppressed (<= 2 goals)
- **Cam Fowler: 1+ goals NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10DETSTL-STLRTHOMAS18-1|no; why: higher confidence-adjusted growth (6.05 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.027/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV10DETSTL-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: STL offense succeeds (4+ goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV10DETSTL-STLJBARRON72-1|yes; why: higher confidence-adjusted growth (2.84 vs 2.56 bp); despite a smaller raw edge (+0.028 vs +0.092/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV10DETSTL-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: STL offense suppressed (<= 2 goals)
- **Andrew Copp: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10DETSTL-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (2.28 vs 0.22 bp); alternative not eligible: confidence-adjusted EV +0.0049 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis STL:OFFENSE_4PLUS (p 0.4371): highest fidelity KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3028): highest fidelity KXNHLGOAL-26NOV10DETSTL-DETACOPP18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10DETSTL-DETACOPP18-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4695): highest fidelity KXNHLAST-26NOV10DETSTL-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV10DETSTL-DETLRAYMOND23-1|no (same contract)
- KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.346, phi -0.19)
- KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: FUNDED_RESEARCH; family TRUSTED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4371, phi -0.108)
- KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.346, phi -0.253)
- KXNHLGOAL-26NOV10DETSTL-DETACOPP18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4695, phi -0.24)

portfolios: A EV +13.70 (adj +3.27) on $50.00, P(profit) 0.4814, adj growth 17.1 bp · B EV +2.72 (adj +1.69) on $34.59, P(profit) 0.5164, adj growth 14.9 bp · C EV +1.67 (adj +0.76) on $17.96, P(profit) 0.4377, adj growth 6.7 bp · R EV +0.12 (adj +0.07) on $5.00, P(profit) 0.9468, adj growth 2.8 bp

## NSH @ LAK  ·  10000 joint draws  ·  436 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.541 / away 0.459

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_NSH_win | p_overtime | goals | shots LAK/NSH | LAK/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.59 | 0.41 | 0.00 | 5.93 | 28.4/27.9 | 24.8/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.47 | 5.94 | 28.5/28.2 | 24.9/25.3 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.105 | 0.69 | 0.31 | 0.00 | 5.98 | 33.5/22.1 | 19.6/28.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.53 | 0.47 | 0.46 | 5.85 | 33.4/22.3 | 19.2/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.61 | 0.39 | 0.00 | 9.18 | 29.5/29.2 | 23.9/22.9 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.065 | 0.67 | 0.33 | 0.00 | 9.21 | 35.4/23.7 | 18.8/27.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.077 | 0.069 | +0.024 | +0.016 | $3.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ goals NO | 63 | 0.687 | 0.671 | +0.041 | +0.025 | $18.65 | FUNDED_RESEARCH | $5 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Steven Stamkos: 1+ goals NO | 65 | 0.696 | 0.682 | +0.030 | +0.016 | $10.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ assists NO | 71 | 0.778 | 0.737 | +0.054 | +0.012 | $8.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (10.60 vs 0.39 bp); alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.028); KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: LAK offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ goals NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV10NSHLA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (6.09 vs 0.28 bp); despite a smaller raw edge (+0.041 vs +0.084/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.022); failure: LAK offense succeeds (4+ goals)
- **Steven Stamkos: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (2.64 vs 1.62 bp); despite a smaller raw edge (+0.030 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no: REINFORCING (phi 0.207); failure: NSH offense succeeds (4+ goals)
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no has the higher standalone adjusted growth (2.64 vs 1.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.207); they share one thesis budget; relationships: KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: REINFORCING (phi 0.207); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis LAK:SUPPRESSED (p 0.3567): highest fidelity KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no (same contract)
- thesis NSH:SUPPRESSED (p 0.4707): highest fidelity KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.4241): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3567, phi -0.129)
- KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4241, phi -0.258)
- KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3177, phi -0.256)
- KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3177, phi -0.237)

portfolios: A EV +2.66 (adj +1.24) on $50.00, P(profit) 0.7552, adj growth 11.1 bp · B EV +3.95 (adj +2.23) on $41.34, P(profit) 0.52, adj growth 19.3 bp · C EV +1.72 (adj +1.02) on $30.70, P(profit) 0.4781, adj growth 8.9 bp · R EV +0.31 (adj +0.19) on $5.00, P(profit) 0.687, adj growth 6.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
