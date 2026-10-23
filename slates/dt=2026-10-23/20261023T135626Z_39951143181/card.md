# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-23T13:56:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 58.24 | +8.91 | +2.89 | -4.44 | 0.406 | -33.47 | -33.47 | 22.47 |
| B thesis-diversified (joint) ← optimiser card | 39.45 | +5.91 | +1.75 | +1.90 | 0.657 | -20.78 | -21.41 | 15.26 |
| C best expression per thesis | 35.07 | +4.47 | +1.02 | +6.49 | 0.662 | -15.94 | -16.80 | 8.99 |
| R FUNDED research stakes | 3.00 | +0.72 | +0.36 | -3.00 | 0.415 | -3.00 | -3.00 | 0.00 |

## MTL @ CHI  ·  10000 joint draws  ·  406 bet sides mapped, 4 +EV candidates, 4 on card


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
| Ryan Greene: 1+ goals YES | 11 | 0.154 | 0.135 | +0.037 | +0.019 | $4.61 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 58 | 0.689 | 0.615 | +0.092 | +0.018 | $13.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Oliver Kapanen: 1+ assists NO | 67 | 0.772 | 0.699 | +0.087 | +0.014 | $12.80 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 26 | 0.298 | 0.286 | +0.024 | +0.013 | $4.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (7.19 vs 1.70 bp); relationships: KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT23MTLCHI-CHIAFRONDELL16-1|no; why: higher confidence-adjusted growth (2.92 vs 0.14 bp); alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT23MTLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.12); failure: CHI offense succeeds (4+ goals)
- **Oliver Kapanen: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no; why: higher confidence-adjusted growth (1.94 vs 0.79 bp); alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT23MTLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: MTL offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes; why: higher confidence-adjusted growth (1.70 vs 0.78 bp); despite a smaller raw edge (+0.024 vs +0.026/contract); alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT23MTLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.12); KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CHI:SUPPRESSED (p 0.4121): highest fidelity KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no (same contract)
- thesis MTL:SUPPRESSED (p 0.3673): highest fidelity KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3733): highest fidelity KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes (same contract)
- KXNHLGOAL-26OCT23MTLCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4121, phi -0.184)
- KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.4 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3733, phi -0.239)
- KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.2 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.412, phi -0.21)
- KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4121, phi -0.262)

portfolios: A EV +8.23 (adj +2.59) on $50.00, P(profit) 0.7136, adj growth 20.3 bp · B EV +5.61 (adj +1.62) on $35.88, P(profit) 0.7136, adj growth 14.1 bp · C EV +4.17 (adj +0.89) on $31.50, P(profit) 0.6623, adj growth 7.8 bp · R EV +0.63 (adj +0.32) on $2.00, P(profit) 0.1539, adj growth 9.8 bp

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
| Artturi Lehkonen: 1+ goals YES | 27 | 0.307 | 0.294 | +0.024 | +0.011 | $3.57 | FUNDED_RESEARCH | $1 | COL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT23TBCOL-TB2|no; why: higher confidence-adjusted growth (1.18 vs 0.87 bp); despite a smaller raw edge (+0.024 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: COL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4464): highest fidelity KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes (same contract)
- KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3368, phi -0.233)

portfolios: A EV +0.69 (adj +0.30) on $8.24, P(profit) 0.3074, adj growth 2.2 bp · B EV +0.30 (adj +0.13) on $3.57, P(profit) 0.3074, adj growth 1.2 bp · C EV +0.30 (adj +0.13) on $3.57, P(profit) 0.3074, adj growth 1.2 bp · R EV +0.08 (adj +0.04) on $1.00, P(profit) 0.3074, adj growth 1.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
