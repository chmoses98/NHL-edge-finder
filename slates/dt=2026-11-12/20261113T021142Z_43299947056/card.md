# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-13T02:11:42Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +12.92 | +5.14 | +10.46 | 0.734 | -35.29 | -35.29 | 44.32 |
| B thesis-diversified (joint) ← optimiser card | 50.00 | +11.71 | +5.36 | +0.85 | 0.891 | -28.84 | -28.84 | 47.93 |
| C best expression per thesis | 40.36 | +5.23 | +1.32 | +1.92 | 0.754 | -18.96 | -18.96 | 12.06 |
| R FUNDED research stakes | 2.00 | +1.10 | +0.76 | -2.00 | 0.132 | -2.00 | -2.00 | 0.00 |

## NYI @ LAK  ·  10000 joint draws  ·  364 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.527 / away 0.473

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
| Andre Lee: 1+ goals YES | 8 | 0.132 | 0.118 | +0.047 | +0.032 | $7.83 | FUNDED_RESEARCH | $2 | LAK:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 1+ assists NO | 65 | 0.851 | 0.717 | +0.185 | +0.051 | $19.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Mats Zuccarello: 2+ assists NO | 93 | 0.989 | 0.954 | +0.054 | +0.020 | $19.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DIFFUSE | NONE | EVIDENCE_MIXED | D |
| Joel Edmundson: 1+ goals YES | 6 | 0.083 | 0.075 | +0.019 | +0.011 | $2.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12NYILA-LATMOORE12-1|yes; why: higher confidence-adjusted growth (28.42 vs 3.57 bp); relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-2|no: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: LAK offense suppressed (<= 2 goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no; why: higher confidence-adjusted growth (25.96 vs 2.89 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-2|no: REINFORCING (phi 0.255); KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.043); failure: LAK offense succeeds (4+ goals)
- **Mats Zuccarello: 2+ assists NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: REINFORCING (phi 0.255); KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: LAK offense succeeds (4+ goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (4.19 vs 1.29 bp); despite a smaller raw edge (+0.019 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.043); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-2|no: MOSTLY_INDEPENDENT (phi -0.016); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.386): highest fidelity KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.395): highest fidelity KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no (same contract)
- thesis LAK:WINS_BY_2PLUS (p 0.3124): highest fidelity KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes (same contract)
- KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.16)
- KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.6 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.386, phi -0.181)
- KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; no single thesis (diffuse); fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.386, phi -0.108)
- KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.136)

portfolios: A EV +12.92 (adj +5.14) on $50.00, P(profit) 0.7339, adj growth 44.3 bp · B EV +11.71 (adj +5.36) on $50.00, P(profit) 0.8915, adj growth 47.9 bp · C EV +5.23 (adj +1.32) on $40.36, P(profit) 0.7543, adj growth 12.1 bp · R EV +1.10 (adj +0.76) on $2.00, P(profit) 0.1318, adj growth 25.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
