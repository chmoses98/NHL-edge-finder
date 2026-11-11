# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-11T02:35:57Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +2.80 | +1.39 | +0.25 | 0.611 | -19.09 | -30.95 | 12.50 |
| B thesis-diversified (joint) ← optimiser card | 42.96 | +6.05 | +3.79 | +12.16 | 0.552 | -15.42 | -42.96 | 32.57 |
| C best expression per thesis | 40.28 | +2.93 | +1.81 | +15.00 | 0.551 | -12.65 | -40.28 | 15.82 |
| R FUNDED research stakes | 5.00 | +0.31 | +0.19 | +2.74 | 0.687 | -5.00 | -5.00 | 0.00 |

## NSH @ LAK  ·  10000 joint draws  ·  436 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.536 / away 0.464

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_NSH_win | p_overtime | goals | shots LAK/NSH | LAK/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.61 | 0.39 | 0.00 | 6.0 | 28.5/28.0 | 24.9/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.49 | 5.91 | 28.3/27.9 | 24.6/25.1 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.103 | 0.68 | 0.32 | 0.00 | 6.02 | 33.3/22.1 | 19.4/28.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.56 | 0.44 | 0.46 | 5.9 | 33.5/22.2 | 19.2/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.60 | 0.40 | 0.00 | 9.24 | 29.9/29.5 | 24.0/23.3 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.065 | 0.71 | 0.29 | 0.00 | 9.16 | 35.5/23.6 | 19.2/27.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Wilsby: 1+ goals YES | 4 | 0.068 | 0.060 | +0.025 | +0.017 | $3.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.079 | 0.068 | +0.026 | +0.015 | $3.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ goals NO | 63 | 0.687 | 0.671 | +0.040 | +0.025 | $17.80 | FUNDED_RESEARCH | $5 | LAK:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Steven Stamkos: 1+ goals NO | 64 | 0.696 | 0.680 | +0.040 | +0.024 | $18.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10NSHLA-NSHAEDSTROM84-1|yes; why: higher confidence-adjusted growth (15.18 vs 4.01 bp); relationships: KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NSH offense suppressed (<= 2 goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (9.15 vs 0.40 bp); alternative not eligible: confidence-adjusted EV +0.0062 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10NSHLA-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: LAK offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ goals NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10NSHLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (5.98 vs 0.11 bp); despite a smaller raw edge (+0.040 vs +0.082/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10NSHLA-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: LAK offense succeeds (4+ goals)
- **Steven Stamkos: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV10NSHLA-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (5.79 vs 1.60 bp); relationships: KXNHLGOAL-26NOV10NSHLA-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis LAK:SUPPRESSED (p 0.3562): highest fidelity KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no (same contract)
- thesis NSH:SUPPRESSED (p 0.4733): highest fidelity KXNHLGOAL-26NOV10NSHLA-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.3128): highest fidelity KXNHLGOAL-26NOV10NSHLA-NSHAEDSTROM84-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10NSHLA-NSHAEDSTROM84-1|yes (same contract)
- KXNHLGOAL-26NOV10NSHLA-NSHAWILSBY2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4733, phi -0.127)
- KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3562, phi -0.127)
- KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4309, phi -0.239)
- KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3128, phi -0.272)

portfolios: A EV +2.80 (adj +1.39) on $50.00, P(profit) 0.6113, adj growth 12.5 bp · B EV +6.05 (adj +3.79) on $42.96, P(profit) 0.5523, adj growth 32.6 bp · C EV +2.93 (adj +1.81) on $40.28, P(profit) 0.5507, adj growth 15.8 bp · R EV +0.31 (adj +0.19) on $5.00, P(profit) 0.6867, adj growth 6.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
