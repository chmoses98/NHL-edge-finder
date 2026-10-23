# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-23T13:02:53Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +5.61 | +0.97 | +10.49 | 0.631 | -28.35 | -29.40 | 7.72 |
| B thesis-diversified (joint) ← optimiser card | 31.87 | +4.53 | +1.42 | +3.13 | 0.698 | -15.54 | -15.54 | 12.31 |
| C best expression per thesis | 26.92 | +3.31 | +0.65 | +7.15 | 0.662 | -11.95 | -11.95 | 5.68 |
| R FUNDED research stakes | 2.00 | +0.63 | +0.32 | -2.00 | 0.154 | -2.00 | -2.00 | 0.00 |

## MTL @ CHI  ·  10000 joint draws  ·  406 bet sides mapped, 6 +EV candidates, 4 on card


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
| Ryan Greene: 1+ goals YES | 11 | 0.154 | 0.135 | +0.037 | +0.019 | $4.77 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Oliver Kapanen: 1+ assists NO | 67 | 0.772 | 0.699 | +0.087 | +0.014 | $12.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 26 | 0.298 | 0.286 | +0.024 | +0.013 | $4.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ assists NO | 56 | 0.636 | 0.588 | +0.059 | +0.011 | $9.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (7.19 vs 1.70 bp); relationships: KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.078); failure: CHI offense suppressed (<= 2 goals)
- **Oliver Kapanen: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no; why: higher confidence-adjusted growth (1.94 vs 1.27 bp); relationships: KXNHLGOAL-26OCT23MTLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: MTL offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes; why: higher confidence-adjusted growth (1.70 vs 0.78 bp); despite a smaller raw edge (+0.024 vs +0.026/contract); alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT23MTLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.153); failure: CHI offense suppressed (<= 2 goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no; why: KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no has the higher standalone adjusted growth (1.17 vs 1.07 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.116); relationships: KXNHLGOAL-26OCT23MTLCHI-CHIRGREENE20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.078); KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.153); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MTL:SUPPRESSED (p 0.3673): highest fidelity KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3733): highest fidelity KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4121): highest fidelity KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26OCT23MTLCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4121, phi -0.184)
- KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.2 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.412, phi -0.21)
- KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4121, phi -0.262)
- KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3733, phi -0.272)

portfolios: A EV +5.61 (adj +0.97) on $50.00, P(profit) 0.6312, adj growth 7.7 bp · B EV +4.53 (adj +1.42) on $31.87, P(profit) 0.698, adj growth 12.3 bp · C EV +3.31 (adj +0.65) on $26.92, P(profit) 0.6623, adj growth 5.7 bp · R EV +0.63 (adj +0.32) on $2.00, P(profit) 0.1539, adj growth 9.8 bp

## TBL @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_TBL_win | p_overtime | goals | shots COL/TBL | COL/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.62 | 0.38 | 0.00 | 6.05 | 28.0/27.9 | 24.8/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.53 | 0.47 | 0.44 | 5.91 | 28.1/27.7 | 24.3/24.8 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.098 | 0.68 | 0.32 | 0.00 | 6.01 | 33.1/22.0 | 19.4/28.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.62 | 0.38 | 0.00 | 9.28 | 29.6/29.2 | 24.1/22.8 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.58 | 0.42 | 0.44 | 5.92 | 33.4/22.4 | 19.2/29.9 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.068 | 0.69 | 0.31 | 0.00 | 9.28 | 35.0/23.6 | 18.9/27.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
