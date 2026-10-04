# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-04T01:31:15Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +17.63 | +6.31 | +20.06 | 0.669 | -29.89 | -37.10 | 57.18 |
| B thesis-diversified (joint) ← optimiser card | 90.04 | +19.54 | +8.78 | +14.87 | 0.588 | -33.53 | -37.78 | 79.08 |
| C best expression per thesis | 59.89 | +17.09 | +7.22 | +1.80 | 0.806 | -31.17 | -31.17 | 64.67 |
| R FUNDED research stakes | 8.00 | +1.58 | +1.09 | -2.11 | 0.197 | -2.11 | -8.00 | 0.00 |

## CGY @ VAN  ·  10000 joint draws  ·  310 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.503 / away 0.497

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CGY_win | p_overtime | goals | shots VAN/CGY | VAN/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.58 | 0.42 | 0.00 | 6.02 | 28.1/28.2 | 24.9/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.94 | 28.4/28.4 | 25.1/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.59 | 0.41 | 0.00 | 9.37 | 29.8/29.9 | 24.3/23.1 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.070 | 0.66 | 0.34 | 0.00 | 6.01 | 32.8/22.3 | 19.6/28.2 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.067 | 0.53 | 0.47 | 0.00 | 6.01 | 22.6/33.3 | 29.5/19.0 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.49 | 0.51 | 0.46 | 5.94 | 22.8/33.6 | 30.2/19.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Zayne Parekh: 1+ goals NO | 84 | 0.900 | 0.884 | +0.050 | +0.034 | $20.00 | FUNDED_RESEARCH | $5 | CGY:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 25 | 0.309 | 0.293 | +0.046 | +0.030 | $10.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 22 | 0.263 | 0.251 | +0.031 | +0.019 | $6.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Drew O'Connor: 1+ goals YES | 19 | 0.223 | 0.213 | +0.022 | +0.012 | $3.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Zayne Parekh: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT03CGYVAN-CGY2|no; why: higher confidence-adjusted growth (20.46 vs 0.30 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0051 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: CGY offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (10.23 vs 4.43 bp); relationships: KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes has the higher standalone adjusted growth (10.23 vs 4.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VAN offense suppressed (<= 2 goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes has the higher standalone adjusted growth (10.23 vs 2.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.022); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.4345): highest fidelity KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes (same contract)
- thesis CGY:SUPPRESSED (p 0.4316): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis VAN:SUPPRESSED (p 0.3529): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.347, phi -0.129)
- KXNHLGOAL-26OCT03CGYVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3529, phi -0.246)
- KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3529, phi -0.236)
- KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3529, phi -0.195)

portfolios: A EV +4.53 (adj +2.93) on $50.00, P(profit) 0.4894, adj growth 25.8 bp · B EV +4.20 (adj +2.70) on $40.04, P(profit) 0.5642, adj growth 24.3 bp · C EV +1.74 (adj +1.14) on $9.89, P(profit) 0.3095, adj growth 9.9 bp · R EV +0.30 (adj +0.20) on $5.00, P(profit) 0.8998, adj growth 7.8 bp

## LAK @ SJS  ·  10000 joint draws  ·  308 bet sides mapped, 16 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.511 / away 0.489

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_LAK_win | p_overtime | goals | shots SJS/LAK | SJS/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.52 | 0.48 | 0.00 | 6.02 | 27.1/27.3 | 23.9/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.47 | 5.92 | 27.4/27.8 | 24.5/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.53 | 0.47 | 0.00 | 9.28 | 29.0/29.4 | 23.6/22.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.080 | 0.50 | 0.50 | 0.00 | 5.99 | 22.0/32.6 | 28.8/18.7 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.47 | 0.53 | 0.52 | 5.9 | 22.0/33.0 | 29.6/18.9 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.065 | 0.59 | 0.41 | 0.00 | 5.93 | 32.2/21.8 | 18.9/28.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mats Zuccarello: 1+ assists NO | 58 | 0.818 | 0.660 | +0.221 | +0.063 | $19.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Kiefer Sherwood: 1+ goals YES | 13 | 0.197 | 0.179 | +0.059 | +0.041 | $10.63 | FUNDED_RESEARCH | $3 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 67 | 0.808 | 0.715 | +0.123 | +0.030 | $19.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (36.20 vs 6.61 bp); relationships: KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: LAK offense succeeds (4+ goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03LASJ-SJCGRAF51-1|yes; why: higher confidence-adjusted growth (29.95 vs 0.94 bp); alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.04); failure: SJS offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no; why: higher confidence-adjusted growth (9.04 vs 2.94 bp); relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.04); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis LAK:SUPPRESSED (p 0.4192): highest fidelity KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3857): highest fidelity KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.4059): highest fidelity KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no (same contract)
- KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 24.3 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3649, phi -0.197)
- KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4059, phi -0.211)
- KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3857, phi -0.212)

portfolios: A EV +13.10 (adj +3.38) on $50.00, P(profit) 0.8437, adj growth 31.4 bp · B EV +15.35 (adj +6.08) on $50.00, P(profit) 0.7324, adj growth 54.8 bp · C EV +15.35 (adj +6.08) on $50.00, P(profit) 0.7324, adj growth 54.8 bp · R EV +1.28 (adj +0.89) on $3.00, P(profit) 0.1968, adj growth 29.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
