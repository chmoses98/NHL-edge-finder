# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-23T14:56:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 58.24 | +5.84 | +1.39 | +4.04 | 0.681 | -18.30 | -37.64 | 11.08 |
| B thesis-diversified (joint) ← optimiser card | 28.77 | +3.54 | +1.22 | +4.34 | 0.594 | -11.65 | -28.77 | 10.71 |
| C best expression per thesis | 26.72 | +3.26 | +0.89 | +3.06 | 0.669 | -12.27 | -26.73 | 7.81 |
| R FUNDED research stakes | 4.00 | +0.51 | +0.23 | -4.00 | 0.476 | -4.00 | -4.00 | 0.00 |

## MTL @ CHI  ·  10000 joint draws  ·  406 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_MTL_win | p_overtime | goals | shots CHI/MTL | CHI/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.46 | 0.54 | 0.00 | 6.0 | 26.8/26.9 | 23.3/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.48 | 5.93 | 26.9/27.2 | 24.0/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.46 | 0.54 | 0.00 | 9.29 | 28.2/28.8 | 22.5/22.3 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.088 | 0.38 | 0.62 | 0.00 | 6.02 | 21.2/31.9 | 27.6/18.2 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.46 | 0.54 | 0.46 | 5.85 | 21.7/32.2 | 28.8/18.6 | even strength |
| MTL shot control · high event (8+) · decided (2+) | 0.061 | 0.41 | 0.59 | 0.00 | 9.35 | 22.9/34.1 | 26.7/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anton Frondell: 1+ goals YES | 20 | 0.248 | 0.226 | +0.036 | +0.015 | $4.58 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Frank Nazar: 1+ goals YES | 21 | 0.248 | 0.236 | +0.026 | +0.015 | $4.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 26 | 0.298 | 0.286 | +0.024 | +0.013 | $4.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 59 | 0.689 | 0.618 | +0.082 | +0.011 | $10.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (2.74 vs 2.64 bp); relationships: KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.074); failure: CHI offense suppressed (<= 2 goals)
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes has the higher standalone adjusted growth (2.74 vs 2.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.042); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes has the higher standalone adjusted growth (2.74 vs 1.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.12); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (1.17 vs 1.07 bp); relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.074); KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.12); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.3733): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3673): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL2|no [DIRECT], best adjusted EV KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.4728): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4121, phi -0.233)
- KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4121, phi -0.242)
- KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4121, phi -0.262)
- KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.9 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3733, phi -0.239)

portfolios: A EV +5.15 (adj +1.01) on $50.00, P(profit) 0.5867, adj growth 8.2 bp · B EV +3.17 (adj +1.02) on $24.33, P(profit) 0.4593, adj growth 8.9 bp · C EV +2.89 (adj +0.69) on $22.28, P(profit) 0.5598, adj growth 6.0 bp · R EV +0.34 (adj +0.14) on $2.00, P(profit) 0.2476, adj growth 4.2 bp

## TBL @ COL  ·  10000 joint draws  ·  414 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_TBL_win | p_overtime | goals | shots COL/TBL | COL/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.62 | 0.38 | 0.00 | 6.05 | 28.0/27.9 | 24.8/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.53 | 0.47 | 0.44 | 5.91 | 28.1/27.7 | 24.3/24.8 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.098 | 0.68 | 0.32 | 0.00 | 6.01 | 33.1/22.0 | 19.4/28.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.62 | 0.38 | 0.00 | 9.28 | 29.6/29.2 | 24.1/22.8 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.58 | 0.42 | 0.44 | 5.92 | 33.4/22.4 | 19.2/29.9 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.068 | 0.69 | 0.31 | 0.00 | 9.28 | 35.0/23.6 | 18.9/27.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Artturi Lehkonen: 1+ goals YES | 27 | 0.307 | 0.297 | +0.024 | +0.013 | $4.44 | FUNDED_RESEARCH | $2 | COL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT23TBCOL-TB2|no; why: higher confidence-adjusted growth (1.81 vs 0.87 bp); despite a smaller raw edge (+0.024 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: COL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4464): highest fidelity KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes (same contract)
- KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3368, phi -0.233)

portfolios: A EV +0.69 (adj +0.38) on $8.24, P(profit) 0.3074, adj growth 2.9 bp · B EV +0.37 (adj +0.20) on $4.44, P(profit) 0.3074, adj growth 1.8 bp · C EV +0.37 (adj +0.20) on $4.44, P(profit) 0.3074, adj growth 1.8 bp · R EV +0.17 (adj +0.09) on $2.00, P(profit) 0.3074, adj growth 2.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
