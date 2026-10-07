# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-07T01:52:58Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +11.16 | +2.36 | +12.73 | 0.614 | -25.37 | -30.95 | 20.08 |
| B thesis-diversified (joint) ← optimiser card | 50.00 | +7.67 | +3.39 | +5.39 | 0.751 | -23.11 | -23.11 | 31.25 |
| C best expression per thesis | 50.00 | +4.80 | +2.46 | +9.42 | 0.659 | -12.75 | -32.05 | 23.13 |
| R FUNDED research stakes | 5.00 | +0.54 | +0.37 | +2.19 | 0.770 | -5.00 | -5.00 | 0.00 |

## FLA @ LAK  ·  10000 joint draws  ·  416 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.487 / away 0.513

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_FLA_win | p_overtime | goals | shots LAK/FLA | LAK/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.63 | 0.37 | 0.00 | 5.95 | 27.0/26.9 | 23.9/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.53 | 0.47 | 0.46 | 5.91 | 27.1/27.0 | 23.8/23.8 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.083 | 0.69 | 0.31 | 0.00 | 6.0 | 32.4/21.6 | 18.9/27.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.62 | 0.38 | 0.00 | 9.15 | 29.0/28.7 | 23.5/22.3 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.56 | 0.44 | 0.45 | 5.85 | 31.9/21.8 | 18.7/28.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.067 | 0.52 | 0.48 | 0.46 | 2.81 | 25.6/25.4 | 24.0/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 68 | 0.770 | 0.747 | +0.075 | +0.051 | $18.70 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 1+ assists NO | 64 | 0.786 | 0.685 | +0.130 | +0.028 | $18.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Alex Laferriere: 1+ goals YES | 23 | 0.281 | 0.267 | +0.039 | +0.025 | $7.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Trevor Moore: 1+ goals YES | 19 | 0.230 | 0.218 | +0.029 | +0.017 | $4.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06FLALA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (27.43 vs 20.16 bp); relationships: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: FLA offense succeeds (4+ goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06FLALA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (7.88 vs 6.91 bp); relationships: KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.136); KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: LAK offense succeeds (4+ goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06FLALA-FLA2|no; why: higher confidence-adjusted growth (7.28 vs 5.93 bp); despite a smaller raw edge (+0.039 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.136); KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: LAK offense suppressed (<= 2 goals)
- **Trevor Moore: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes has the higher standalone adjusted growth (7.28 vs 3.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis FLA:SUPPRESSED (p 0.4918): highest fidelity KXNHLTEAMTOTAL-26OCT06FLALA-FLA4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.4049): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.3764): highest fidelity KXNHLAST-26OCT06FLALA-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT06FLALA-LAAPANARIN10-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.2891, phi -0.229)
- KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.6 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4049, phi -0.192)
- KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3764, phi -0.254)
- KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3764, phi -0.224)

portfolios: A EV +11.16 (adj +2.36) on $50.00, P(profit) 0.614, adj growth 20.1 bp · B EV +7.67 (adj +3.39) on $50.00, P(profit) 0.7514, adj growth 31.3 bp · C EV +4.80 (adj +2.46) on $50.00, P(profit) 0.6588, adj growth 23.1 bp · R EV +0.54 (adj +0.37) on $5.00, P(profit) 0.7703, adj growth 14.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
