# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-11T01:05:21Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +3.05 | +1.34 | -1.21 | 0.478 | -24.97 | -26.99 | 11.28 |
| B thesis-diversified (joint) ← optimiser card | 48.00 | +2.11 | +1.28 | +1.63 | 0.653 | -19.99 | -26.39 | 11.46 |
| C best expression per thesis | 30.70 | +1.72 | +1.02 | -2.57 | 0.478 | -11.89 | -30.70 | 8.93 |
| R FUNDED research stakes | 5.00 | +0.13 | +0.08 | +0.40 | 0.949 | +0.40 | -5.00 | 0.00 |

## NSH @ LAK  ·  10000 joint draws  ·  436 bet sides mapped, 6 +EV candidates, 3 on card

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
| Steven Stamkos: 2+ goals NO | 92 | 0.949 | 0.940 | +0.024 | +0.015 | $20.00 | FUNDED_RESEARCH | $5 | NSH:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ goals NO | 63 | 0.687 | 0.671 | +0.041 | +0.025 | $18.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Steven Stamkos: 1+ goals NO | 65 | 0.696 | 0.682 | +0.030 | +0.016 | $9.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Steven Stamkos: 2+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no; why: higher confidence-adjusted growth (7.54 vs 2.64 bp); despite a smaller raw edge (+0.024 vs +0.030/contract); relationships: KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: DUPLICATIVE (phi 0.351); failure: NSH offense succeeds (4+ goals)
- **Artemi Panarin: 1+ goals NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10NSHLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (6.09 vs 0.15 bp); despite a smaller raw edge (+0.041 vs +0.084/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-2|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: LAK offense succeeds (4+ goals)
- **Steven Stamkos: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (2.64 vs 1.62 bp); despite a smaller raw edge (+0.030 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-2|no: DUPLICATIVE (phi 0.351); KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis LAK:SUPPRESSED (p 0.3567): highest fidelity KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no (same contract)
- thesis NSH:SUPPRESSED (p 0.4707): highest fidelity KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3177, phi -0.207)
- KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4241, phi -0.258)
- KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3177, phi -0.256)

portfolios: A EV +3.05 (adj +1.34) on $50.00, P(profit) 0.4781, adj growth 11.3 bp · B EV +2.11 (adj +1.28) on $48.00, P(profit) 0.6528, adj growth 11.5 bp · C EV +1.72 (adj +1.02) on $30.70, P(profit) 0.4781, adj growth 8.9 bp · R EV +0.13 (adj +0.08) on $5.00, P(profit) 0.9489, adj growth 3.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
