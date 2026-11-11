# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-11T02:08:16Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +3.55 | +1.73 | -0.89 | 0.478 | -24.60 | -26.68 | 15.18 |
| B thesis-diversified (joint) ← optimiser card | 47.87 | +3.35 | +1.68 | -0.42 | 0.478 | -23.71 | -28.06 | 14.80 |
| C best expression per thesis | 36.66 | +2.28 | +1.41 | -8.46 | 0.478 | -8.57 | -36.66 | 12.40 |
| R FUNDED research stakes | 5.00 | +0.31 | +0.19 | +2.74 | 0.687 | -5.00 | -5.00 | 0.00 |

## NSH @ LAK  ·  10000 joint draws  ·  436 bet sides mapped, 6 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.536 / away 0.464

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
| Artemi Panarin: 1+ goals NO | 63 | 0.687 | 0.671 | +0.041 | +0.025 | $17.87 | FUNDED_RESEARCH | $5 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Steven Stamkos: 1+ goals NO | 64 | 0.696 | 0.681 | +0.040 | +0.025 | $15.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ assists NO | 70 | 0.778 | 0.734 | +0.063 | +0.019 | $14.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Artemi Panarin: 1+ goals NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10NSHLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (6.09 vs 0.15 bp); despite a smaller raw edge (+0.041 vs +0.084/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.022); failure: LAK offense succeeds (4+ goals)
- **Steven Stamkos: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (6.05 vs 4.04 bp); despite a smaller raw edge (+0.040 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no: REINFORCING (phi 0.207); failure: NSH offense succeeds (4+ goals)
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no has the higher standalone adjusted growth (6.05 vs 4.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.207); they share one thesis budget; relationships: KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: REINFORCING (phi 0.207); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis LAK:SUPPRESSED (p 0.3567): highest fidelity KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no (same contract)
- thesis NSH:SUPPRESSED (p 0.4707): highest fidelity KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4241, phi -0.258)
- KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3177, phi -0.256)
- KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3177, phi -0.237)

portfolios: A EV +3.55 (adj +1.73) on $50.00, P(profit) 0.4781, adj growth 15.2 bp · B EV +3.35 (adj +1.68) on $47.87, P(profit) 0.4781, adj growth 14.8 bp · C EV +2.28 (adj +1.41) on $36.66, P(profit) 0.4781, adj growth 12.4 bp · R EV +0.31 (adj +0.19) on $5.00, P(profit) 0.687, adj growth 6.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
