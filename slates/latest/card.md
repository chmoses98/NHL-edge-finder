# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-23T16:53:07Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 70.00 | +13.12 | +4.85 | +1.28 | 0.508 | -27.75 | -48.34 | 36.57 |
| B thesis-diversified (joint) ← optimiser card | 43.17 | +7.47 | +4.32 | +1.25 | 0.556 | -22.12 | -43.16 | 37.00 |
| C best expression per thesis | 38.96 | +3.61 | +1.45 | +1.25 | 0.634 | -19.40 | -19.40 | 12.73 |
| R FUNDED research stakes | 5.00 | +1.65 | +1.15 | -5.00 | 0.349 | -5.00 | -5.00 | 0.00 |

## MTL @ CHI  ·  10000 joint draws  ·  424 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.403 / away 0.597

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_MTL_win | p_overtime | goals | shots CHI/MTL | CHI/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.46 | 0.54 | 0.00 | 6.01 | 26.7/27.1 | 23.4/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.48 | 0.52 | 0.46 | 5.94 | 26.5/27.0 | 23.6/23.3 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.093 | 0.40 | 0.60 | 0.00 | 6.02 | 21.4/32.1 | 28.0/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.48 | 0.52 | 0.00 | 9.24 | 28.5/28.8 | 22.3/22.6 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.48 | 0.52 | 0.46 | 5.93 | 21.6/32.1 | 28.7/18.3 | even strength |
| MTL shot control · high event (8+) · decided (2+) | 0.062 | 0.42 | 0.58 | 0.00 | 9.17 | 22.6/33.4 | 26.5/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 25 | 0.301 | 0.287 | +0.038 | +0.024 | $8.54 | FUNDED_RESEARCH | $3 | CHI:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Anton Frondell: 1+ goals YES | 20 | 0.245 | 0.231 | +0.034 | +0.020 | $6.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Frank Nazar: 1+ goals YES | 21 | 0.250 | 0.238 | +0.029 | +0.016 | $5.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ assists NO | 55 | 0.627 | 0.581 | +0.059 | +0.013 | $11.94 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes; why: higher confidence-adjusted growth (6.27 vs 5.16 bp); relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.145); failure: CHI offense suppressed (<= 2 goals)
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (6.27 vs 5.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.051); failure: CHI offense suppressed (<= 2 goals)
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (6.27 vs 3.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.066); failure: CHI offense suppressed (<= 2 goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (1.63 vs 1.14 bp); despite a smaller raw edge (+0.059 vs +0.082/contract); relationships: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.145); KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.051); KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.066); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MTL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CHI:OFFENSE_4PLUS (p 0.3677): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.4753): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3726): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT23MTLCHI-MTL3|no (same contract)
- KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4104, phi -0.284)
- KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4104, phi -0.239)
- KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4104, phi -0.234)
- KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3677, phi -0.258)

portfolios: A EV +7.55 (adj +1.04) on $50.00, P(profit) 0.5564, adj growth 7.9 bp · B EV +4.12 (adj +2.01) on $31.87, P(profit) 0.5066, adj growth 17.5 bp · C EV +3.24 (adj +1.25) on $34.52, P(profit) 0.6307, adj growth 11.0 bp · R EV +0.43 (adj +0.27) on $3.00, P(profit) 0.3007, adj growth 8.6 bp

## TBL @ COL  ·  10000 joint draws  ·  426 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.532 / away 0.468

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
| Josh Manson: 1+ goals YES | 4 | 0.069 | 0.061 | +0.026 | +0.019 | $4.24 | FUNDED_RESEARCH | $2 | COL:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Parker Kelly: 1+ goals YES | 11 | 0.134 | 0.127 | +0.018 | +0.010 | $2.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 27 | 0.307 | 0.297 | +0.024 | +0.013 | $4.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Josh Manson: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (18.10 vs 1.81 bp); relationships: KXNHLGOAL-26OCT23TBCOL-COLPKELLY17-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: COL offense suppressed (<= 2 goals)
- **Parker Kelly: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (2.18 vs 1.81 bp); despite a smaller raw edge (+0.018 vs +0.024/contract); relationships: KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: COL offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT23TBCOL-TB2|no; why: higher confidence-adjusted growth (1.81 vs 0.87 bp); despite a smaller raw edge (+0.024 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT23TBCOL-COLPKELLY17-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4464): highest fidelity KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes (same contract)
- KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3368, phi -0.105)
- KXNHLGOAL-26OCT23TBCOL-COLPKELLY17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3368, phi -0.161)
- KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3368, phi -0.233)

portfolios: A EV +5.57 (adj +3.81) on $20.00, P(profit) 0.4401, adj growth 28.7 bp · B EV +3.35 (adj +2.31) on $11.30, P(profit) 0.4401, adj growth 19.5 bp · C EV +0.37 (adj +0.20) on $4.44, P(profit) 0.3074, adj growth 1.8 bp · R EV +1.22 (adj +0.88) on $2.00, P(profit) 0.0687, adj growth 25.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
