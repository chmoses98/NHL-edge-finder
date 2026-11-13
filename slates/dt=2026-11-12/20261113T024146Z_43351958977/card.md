# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-13T02:41:46Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +10.00 | +2.15 | +24.39 | 0.795 | -17.99 | -30.05 | 19.63 |
| B thesis-diversified (joint) ← optimiser card | 35.20 | +10.65 | +4.61 | +11.26 | 0.710 | -12.67 | -12.67 | 40.12 |
| C best expression per thesis | 40.00 | +5.44 | +1.39 | +13.10 | 0.761 | -18.81 | -18.81 | 12.95 |
| R FUNDED research stakes | 1.00 | +1.02 | +0.95 | -1.00 | 0.022 | -1.00 | -1.00 | 0.00 |

## NYI @ LAK  ·  10000 joint draws  ·  398 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.526 / away 0.474

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_NYI_win | p_overtime | goals | shots LAK/NYI | LAK/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.57 | 0.43 | 0.00 | 6.02 | 28.0/27.7 | 24.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.51 | 0.49 | 0.48 | 5.89 | 28.0/28.0 | 24.8/24.6 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.084 | 0.64 | 0.36 | 0.00 | 5.96 | 32.8/22.1 | 19.2/28.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.56 | 0.44 | 0.00 | 9.1 | 29.2/28.9 | 23.7/22.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.55 | 0.45 | 0.49 | 5.78 | 32.7/22.0 | 18.8/29.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.55 | 0.45 | 0.00 | 3.46 | 26.5/26.6 | 24.9/24.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mats Zuccarello: 1+ assists NO | 65 | 0.848 | 0.716 | +0.182 | +0.050 | $15.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Andre Lee: First Goalscorer YES | 1 | 0.022 | 0.021 | +0.011 | +0.010 | $2.02 | FUNDED_RESEARCH | $1 | LAK:SCORES_FIRST | FRAGILE (0.04) | EVIDENCE_MIXED | D |
| Kevin Fiala: 1+ assists NO | 61 | 0.769 | 0.662 | +0.142 | +0.036 | $15.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Andre Lee: 1+ goals YES | 8 | 0.115 | 0.105 | +0.029 | +0.019 | $3.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV12NYILA-LAKFIALA22-1|no; why: higher confidence-adjusted growth (24.93 vs 11.91 bp); relationships: KXNHLFIRSTGOAL-26NOV12NYILA-LAALEE47|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV12NYILA-LAKFIALA22-1|no: MOSTLY_INDEPENDENT (phi 0.064); KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.045); failure: LAK offense succeeds (4+ goals)
- **Andre Lee: First Goalscorer YES** — thesis: LAK scores first; alternative: KXNHLFIRSTGOAL-26NOV12NYILA-LAAKEMPE9|yes; why: higher confidence-adjusted growth (19.08 vs 0.00 bp); despite a smaller raw edge (+0.011 vs +0.013/contract); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV12NYILA-LAKFIALA22-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: DUPLICATIVE (phi 0.413); failure: NYI scores first
- **Kevin Fiala: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no; why: higher confidence-adjusted growth (11.91 vs 1.99 bp); despite a smaller raw edge (+0.142 vs +0.142/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.064); KXNHLFIRSTGOAL-26NOV12NYILA-LAALEE47|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.059); failure: LAK offense succeeds (4+ goals)
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHL2PSPREAD-26NOV12NYILA-LA2|yes; why: higher confidence-adjusted growth (10.39 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.904 vs 0.759); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLFIRSTGOAL-26NOV12NYILA-LAALEE47|yes: DUPLICATIVE (phi 0.413); KXNHLAST-26NOV12NYILA-LAKFIALA22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.059); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis LAK:SUPPRESSED (p 0.3942): highest fidelity KXNHLAST-26NOV12NYILA-LAKFIALA22-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV12NYILA-LAKFIALA22-1|no (same contract)
- thesis LAK:SCORES_FIRST (p 0.5227): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis LAK:OFFENSE_4PLUS (p 0.3849): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.3 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3849, phi -0.199)
- KXNHLFIRSTGOAL-26NOV12NYILA-LAALEE47|yes: FUNDED_RESEARCH; family MIXED; loses 96% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SCORES_FIRST (p 0.4758, phi -0.142)
- KXNHLAST-26NOV12NYILA-LAKFIALA22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3849, phi -0.241)
- KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3942, phi -0.158)

portfolios: A EV +10.00 (adj +2.15) on $50.00, P(profit) 0.7948, adj growth 19.6 bp · B EV +10.65 (adj +4.61) on $35.20, P(profit) 0.7102, adj growth 40.1 bp · C EV +5.44 (adj +1.39) on $40.00, P(profit) 0.7606, adj growth 13.0 bp · R EV +1.02 (adj +0.95) on $1.00, P(profit) 0.0216, adj growth 25.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
