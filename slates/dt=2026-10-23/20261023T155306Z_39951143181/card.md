# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-23T15:53:06Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 58.24 | +6.38 | +1.70 | +2.80 | 0.712 | -19.91 | -36.58 | 14.12 |
| B thesis-diversified (joint) ← optimiser card | 48.29 | +5.70 | +2.49 | +2.14 | 0.518 | -25.28 | -25.28 | 21.75 |
| C best expression per thesis | 35.33 | +4.61 | +1.70 | +5.50 | 0.613 | -20.13 | -35.33 | 14.92 |
| R FUNDED research stakes | 4.00 | +0.51 | +0.30 | -4.00 | 0.476 | -4.00 | -4.00 | 0.00 |

## MTL @ CHI  ·  10000 joint draws  ·  424 bet sides mapped, 9 +EV candidates, 4 on card


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
| Anton Frondell: 1+ goals YES | 20 | 0.248 | 0.233 | +0.036 | +0.022 | $6.64 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ assists NO | 56 | 0.648 | 0.601 | +0.070 | +0.024 | $13.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 25 | 0.298 | 0.285 | +0.035 | +0.022 | $7.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Oliver Kapanen: 1+ assists NO | 69 | 0.772 | 0.724 | +0.067 | +0.019 | $16.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (6.30 vs 5.21 bp); relationships: KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CHI offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no; why: higher confidence-adjusted growth (5.22 vs 3.67 bp); relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi 0.074); failure: MTL offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes has the higher standalone adjusted growth (6.30 vs 5.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: CHI offense suppressed (<= 2 goals)
- **Oliver Kapanen: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no; why: second expression of the same thesis: KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no has the higher standalone adjusted growth (5.22 vs 3.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.074); they share one thesis budget; relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi 0.074); KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.3733): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3673): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL2|no [DIRECT], best adjusted EV KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.4728): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4121, phi -0.233)
- KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.412, phi -0.266)
- KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4121, phi -0.262)
- KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.412, phi -0.21)

portfolios: A EV +5.69 (adj +1.32) on $50.00, P(profit) 0.6312, adj growth 11.2 bp · B EV +5.33 (adj +2.29) on $43.85, P(profit) 0.7058, adj growth 20.0 bp · C EV +4.24 (adj +1.50) on $30.89, P(profit) 0.5913, adj growth 13.1 bp · R EV +0.34 (adj +0.21) on $2.00, P(profit) 0.2476, adj growth 7.0 bp

## TBL @ COL  ·  10000 joint draws  ·  426 bet sides mapped, 1 +EV candidates, 1 on card


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
