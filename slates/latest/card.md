# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T15:46:20Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.08 | +9.19 | +25.09 | 0.732 | -26.32 | -39.09 | 82.96 |
| B thesis-diversified (joint) ← optimiser card | 149.34 | +25.85 | +14.14 | +23.63 | 0.708 | -28.38 | -40.91 | 132.03 |
| C best expression per thesis | 149.99 | +25.66 | +11.27 | +23.85 | 0.694 | -32.63 | -47.89 | 102.14 |
| R FUNDED research stakes | 25.00 | +2.95 | +1.60 | +2.03 | 0.618 | -6.77 | -8.46 | 0.00 |

## CHI @ BOS  ·  10000 joint draws  ·  456 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_CHI_win | p_overtime | goals | shots BOS/CHI | BOS/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.75 | 0.25 | 0.00 | 6.06 | 27.0/26.5 | 24.1/22.4 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.117 | 0.78 | 0.22 | 0.00 | 6.04 | 32.4/21.0 | 18.8/27.0 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.092 | 0.81 | 0.19 | 0.00 | 9.34 | 34.1/22.5 | 18.5/25.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.56 | 0.44 | 0.48 | 5.91 | 26.9/26.5 | 23.4/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.73 | 0.27 | 0.00 | 9.38 | 28.8/28.4 | 23.7/21.0 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.60 | 0.40 | 0.48 | 5.96 | 32.4/21.4 | 18.3/28.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.265 | 0.247 | +0.043 | +0.026 | $4.31 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 11 | 0.149 | 0.137 | +0.032 | +0.020 | $2.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Hampus Lindholm: 1+ assists YES | 26 | 0.339 | 0.294 | +0.065 | +0.021 | $3.16 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
| Connor Bedard: 1+ assists NO | 57 | 0.654 | 0.607 | +0.067 | +0.020 | $8.16 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CHIBOS-CHIRDONATO8-1|yes; why: higher confidence-adjusted growth (8.41 vs 0.11 bp); alternative not eligible: confidence-adjusted EV +0.0025 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT31CHIBOS-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.167); failure: CHI offense suppressed (<= 2 goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (8.41 vs 8.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT31CHIBOS-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.036); failure: CHI offense suppressed (<= 2 goals)
- **Hampus Lindholm: 1+ assists YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31CHIBOS-BOSFMINTEN93-1|yes; why: higher confidence-adjusted growth (4.75 vs 0.38 bp); alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: BOS offense suppressed (<= 2 goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31CHIBOS-CHIPKANE88-1|no; why: higher confidence-adjusted growth (3.65 vs 2.31 bp); despite a smaller raw edge (+0.067 vs +0.085/contract); relationships: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.167); KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLAST-26OCT31CHIBOS-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, BOS shot control · normal event (5-7) · decided (2+) 0.12, BOS shot control · high event (8+) · decided (2+) 0.09.
- thesis CHI:OFFENSE_4PLUS (p 0.281): highest fidelity KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.5414): highest fidelity KXNHLAST-26OCT31CHIBOS-BOSHLINDHOLM27-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT31CHIBOS-BOSHLINDHOLM27-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.51): highest fidelity KXNHLAST-26OCT31CHIBOS-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.51, phi -0.276)
- KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.51, phi -0.208)
- KXNHLAST-26OCT31CHIBOS-BOSHLINDHOLM27-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.2565, phi -0.211)
- KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.281, phi -0.287)

portfolios: A EV +2.35 (adj +0.65) on $15.73, P(profit) 0.5249, adj growth 6.0 bp · B EV +3.22 (adj +1.45) on $18.16, P(profit) 0.5205, adj growth 13.5 bp · C EV +4.37 (adj +1.69) on $35.22, P(profit) 0.714, adj growth 15.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ DET  ·  10000 joint draws  ·  406 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_STL_win | p_overtime | goals | shots DET/STL | DET/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.48 | 0.52 | 0.00 | 5.99 | 27.5/27.2 | 23.5/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.51 | 5.93 | 27.5/27.2 | 23.9/24.3 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.100 | 0.52 | 0.48 | 0.00 | 5.99 | 32.4/21.3 | 18.0/28.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.51 | 0.49 | 0.48 | 5.92 | 32.6/21.8 | 18.5/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.47 | 0.53 | 0.00 | 9.24 | 29.1/28.7 | 22.4/23.2 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.060 | 0.58 | 0.42 | 0.00 | 9.13 | 34.3/22.9 | 17.8/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jimmy Snuggerud: 1+ goals YES | 27 | 0.329 | 0.313 | +0.045 | +0.029 | $4.53 | FUNDED_RESEARCH | $2 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Lucas Raymond: 1+ assists NO | 58 | 0.657 | 0.616 | +0.060 | +0.019 | $6.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Dylan Holloway: 1+ assists YES | 31 | 0.386 | 0.340 | +0.061 | +0.015 | $1.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes; why: higher confidence-adjusted growth (9.21 vs 2.35 bp); despite a smaller raw edge (+0.045 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes: REINFORCING (phi 0.258); failure: STL offense suppressed (<= 2 goals)
- **Lucas Raymond: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31STLDET-DETMSEIDER53-1|no; why: higher confidence-adjusted growth (3.36 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0006 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: DET offense succeeds (4+ goals)
- **Dylan Holloway: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes has the higher standalone adjusted growth (9.21 vs 2.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.258); they share one thesis budget; relationships: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: REINFORCING (phi 0.258); KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.3777): highest fidelity KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4132): highest fidelity KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no (same contract)
- KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3999, phi -0.287)
- KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3659, phi -0.257)
- KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 43% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3999, phi -0.311)

portfolios: A EV +2.34 (adj +0.91) on $15.73, P(profit) 0.4795, adj growth 8.2 bp · B EV +1.58 (adj +0.73) on $11.88, P(profit) 0.4624, adj growth 6.8 bp · C EV +2.04 (adj +1.02) on $15.99, P(profit) 0.3292, adj growth 9.3 bp · R EV +0.32 (adj +0.21) on $2.00, P(profit) 0.3292, adj growth 7.4 bp

## TBL @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 7 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_TBL_win | p_overtime | goals | shots NSH/TBL | NSH/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.48 | 0.52 | 0.00 | 6.0 | 27.3/27.8 | 24.2/23.6 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.111 | 0.40 | 0.60 | 0.00 | 5.97 | 21.6/33.3 | 29.0/18.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.51 | 0.49 | 0.48 | 5.96 | 27.5/28.0 | 24.7/24.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.44 | 0.56 | 0.48 | 5.88 | 22.0/33.6 | 30.2/18.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.46 | 0.54 | 0.00 | 9.29 | 29.1/29.5 | 23.5/23.2 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.068 | 0.39 | 0.61 | 0.00 | 9.22 | 22.9/35.0 | 27.6/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charle-Edouard D'Astous: 1+ goals NO | 88 | 0.929 | 0.915 | +0.041 | +0.028 | $9.77 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 25 | 0.313 | 0.295 | +0.050 | +0.032 | $4.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 74 | 0.809 | 0.772 | +0.056 | +0.019 | $6.74 | FUNDED_RESEARCH | $2 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TBNSH-TB3|no; why: higher confidence-adjusted growth (17.57 vs 4.09 bp); despite a smaller raw edge (+0.041 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.096); failure: TBL offense succeeds (4+ goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHL2PSPREAD-26OCT31TBNSH-NSH2|yes; why: higher confidence-adjusted growth (11.34 vs 4.11 bp); despite a smaller raw edge (+0.050 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.94 vs 0.811); relationships: KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.147); failure: NSH offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHL2PSPREAD-26OCT31TBNSH-NSH2|yes; why: KXNHL2PSPREAD-26OCT31TBNSH-NSH2|yes has the higher standalone adjusted growth (4.11 vs 4.09 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.171); relationships: KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.096); KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.147); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NSH:OFFENSE_4PLUS (p 0.3613): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS_BY_2PLUS (p 0.2522): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB3|no (same contract)
- thesis NSH:WINS (p 0.4644): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB3|no (same contract)
- KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4098, phi -0.122)
- KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4167, phi -0.281)
- KXNHLSPREAD-26OCT31TBNSH-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3117, phi -0.722)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT31TBNSH-TB2|no less than the minimum stake; KXNHL2PSPREAD-26OCT31TBNSH-NSH2|yes kept

portfolios: A EV +3.06 (adj +0.77) on $15.73, P(profit) 0.5489, adj growth 6.4 bp · B EV +1.82 (adj +1.02) on $21.06, P(profit) 0.3098, adj growth 9.8 bp · C EV +2.75 (adj +1.23) on $18.38, P(profit) 0.3823, adj growth 11.1 bp · R EV +0.29 (adj +0.14) on $5.00, P(profit) 0.7612, adj growth 5.6 bp

## EDM @ NYI  ·  10000 joint draws  ·  422 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_EDM_win | p_overtime | goals | shots NYI/EDM | NYI/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.49 | 0.51 | 0.00 | 6.05 | 27.7/27.7 | 24.0/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.116 | 0.45 | 0.56 | 0.00 | 9.46 | 29.2/29.2 | 22.5/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.48 | 0.52 | 0.46 | 5.98 | 27.7/27.6 | 24.1/24.3 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.078 | 0.53 | 0.47 | 0.00 | 6.06 | 32.4/21.9 | 18.6/28.6 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.063 | 0.38 | 0.62 | 0.00 | 6.03 | 22.2/32.1 | 27.9/19.3 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.54 | 0.46 | 0.44 | 5.88 | 32.3/21.6 | 18.5/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mattias Ekholm: 1+ goals YES | 7 | 0.123 | 0.105 | +0.049 | +0.030 | $3.19 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 13 | 0.178 | 0.165 | +0.041 | +0.027 | $3.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Adam Pelech: 1+ goals YES | 5 | 0.069 | 0.064 | +0.015 | +0.011 | $1.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Anthony Duclair: 1+ goals YES | 15 | 0.187 | 0.175 | +0.028 | +0.017 | $2.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-7|yes; why: higher confidence-adjusted growth (27.97 vs 3.06 bp); despite a smaller raw edge (+0.049 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.822 vs 0.655); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT31EDMNYI-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT31EDMNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-7|yes; why: higher confidence-adjusted growth (13.36 vs 3.06 bp); despite a smaller raw edge (+0.041 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.863 vs 0.655); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT31EDMNYI-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT31EDMNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: EDM offense suppressed (<= 2 goals)
- **Adam Pelech: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (4.92 vs 4.37 bp); despite a smaller raw edge (+0.015 vs +0.031/contract); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT31EDMNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: NYI offense suppressed (<= 2 goals)
- **Anthony Duclair: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (4.44 vs 4.37 bp); despite a smaller raw edge (+0.028 vs +0.031/contract); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT31EDMNYI-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.4191): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.4481): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-7|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.3296): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-7|yes (same contract)
- KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3425, phi -0.156)
- KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3425, phi -0.167)
- KXNHLGOAL-26OCT31EDMNYI-NYIAPELECH3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.368, phi -0.102)
- KXNHLGOAL-26OCT31EDMNYI-NYIADUCLAIR11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.368, phi -0.193)

portfolios: A EV +3.75 (adj +1.54) on $15.73, P(profit) 0.4934, adj growth 14.4 bp · B EV +3.86 (adj +2.47) on $10.17, P(profit) 0.454, adj growth 22.9 bp · C EV +2.35 (adj +0.71) on $14.81, P(profit) 0.3892, adj growth 6.5 bp · R EV +0.65 (adj +0.41) on $1.00, P(profit) 0.1232, adj growth 14.8 bp

## BUF @ LAK  ·  10000 joint draws  ·  434 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BUF_win | p_overtime | goals | shots LAK/BUF | LAK/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.60 | 0.40 | 0.00 | 6.0 | 27.9/27.9 | 24.8/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.122 | 0.51 | 0.49 | 0.45 | 5.89 | 28.1/27.8 | 24.6/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.57 | 0.43 | 0.00 | 9.21 | 29.4/29.3 | 23.6/22.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.065 | 0.58 | 0.42 | 0.00 | 6.03 | 32.6/22.3 | 19.3/28.4 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.064 | 0.52 | 0.48 | 0.00 | 5.99 | 22.5/32.7 | 29.1/18.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.51 | 0.49 | 0.48 | 5.97 | 33.0/22.4 | 19.1/29.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Andre Lee: 1+ goals YES | 9 | 0.131 | 0.120 | +0.035 | +0.024 | $2.76 | FUNDED_RESEARCH | $1 | LAK:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Corey Perry: 1+ goals YES | 14 | 0.183 | 0.171 | +0.034 | +0.022 | $2.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.079 | 0.067 | +0.025 | +0.013 | $1.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 1.5 goals NO | 68 | 0.765 | 0.720 | +0.070 | +0.025 | $7.72 | FUNDED_RESEARCH | $2 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF2|no; why: higher confidence-adjusted growth (14.00 vs 6.39 bp); despite a smaller raw edge (+0.035 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT31BUFLA-BUF2|no: MOSTLY_INDEPENDENT (phi 0.094); failure: LAK offense suppressed (<= 2 goals)
- **Corey Perry: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF2|no; why: higher confidence-adjusted growth (8.46 vs 6.39 bp); despite a smaller raw edge (+0.034 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT31BUFLA-BUF2|no: MOSTLY_INDEPENDENT (phi 0.107); failure: LAK offense suppressed (<= 2 goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLSPREAD-26OCT31BUFLA-BUF2|no; why: higher confidence-adjusted growth (7.35 vs 6.39 bp); despite a smaller raw edge (+0.025 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT31BUFLA-BUF2|no: MOSTLY_INDEPENDENT (phi 0.083); failure: LAK offense suppressed (<= 2 goals)
- **Buffalo wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: higher confidence-adjusted growth (6.39 vs 4.54 bp); relationships: KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.094); KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: MOSTLY_INDEPENDENT (phi 0.107); KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.083); failure: BUF wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.4073): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS_BY_2PLUS (p 0.3119): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no (same contract)
- thesis LAK:WINS (p 0.5431): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no (same contract)
- KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.162)
- KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.18)
- KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.13)
- KXNHLSPREAD-26OCT31BUFLA-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2349, phi -1.0)

portfolios: A EV +1.80 (adj +0.50) on $15.73, P(profit) 0.6758, adj growth 4.6 bp · B EV +3.05 (adj +1.70) on $14.54, P(profit) 0.3453, adj growth 15.8 bp · C EV +1.44 (adj +0.51) on $14.35, P(profit) 0.7651, adj growth 4.7 bp · R EV +0.57 (adj +0.32) on $3.00, P(profit) 0.1311, adj growth 11.7 bp

## OTT @ SJS  ·  10000 joint draws  ·  444 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_OTT_win | p_overtime | goals | shots SJS/OTT | SJS/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.49 | 0.51 | 0.00 | 6.03 | 27.0/27.3 | 23.7/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.46 | 6.01 | 27.1/27.5 | 24.0/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.51 | 0.49 | 0.00 | 9.44 | 28.6/28.8 | 22.6/22.4 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.091 | 0.46 | 0.54 | 0.00 | 6.03 | 21.5/32.4 | 28.6/18.3 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.44 | 0.56 | 0.44 | 5.89 | 21.6/32.6 | 28.9/18.4 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.064 | 0.45 | 0.55 | 0.00 | 9.37 | 22.9/33.9 | 26.9/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Toffoli: 1+ assists YES | 24 | 0.325 | 0.277 | +0.072 | +0.025 | $3.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ goals NO | 79 | 0.824 | 0.814 | +0.022 | +0.013 | $8.69 | FUNDED_RESEARCH | $3 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Adam Gaudette: 1+ goals YES | 14 | 0.169 | 0.160 | +0.021 | +0.011 | $1.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Collin Graf: 1+ goals YES | 17 | 0.200 | 0.191 | +0.020 | +0.011 | $1.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes; why: higher confidence-adjusted growth (7.00 vs 2.10 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT31OTTSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.063); KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.056); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31OTTSJ-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (2.24 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.068/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: SJS offense succeeds (4+ goals)
- **Adam Gaudette: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes has the higher standalone adjusted growth (7.00 vs 2.10 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.063); they share one thesis budget; relationships: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.063); KXNHLGOAL-26OCT31OTTSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: SJS offense suppressed (<= 2 goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes has the higher standalone adjusted growth (7.00 vs 1.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.056); they share one thesis budget; relationships: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26OCT31OTTSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4099): highest fidelity KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3637): highest fidelity KXNHLAST-26OCT31OTTSJ-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31OTTSJ-OTTJSANDERSON85-1|no (same contract)
- thesis SJS:SUPPRESSED (p 0.3765): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.254)
- KXNHLGOAL-26OCT31OTTSJ-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4099, phi -0.193)
- KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.201)
- KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.201)

portfolios: A EV +2.11 (adj +0.74) on $15.73, P(profit) 0.4218, adj growth 6.9 bp · B EV +1.60 (adj +0.67) on $14.98, P(profit) 0.4603, adj growth 6.3 bp · C EV +1.95 (adj +0.62) on $10.30, P(profit) 0.3249, adj growth 5.6 bp · R EV +0.08 (adj +0.05) on $3.00, P(profit) 0.8241, adj growth 1.7 bp

## PIT @ MTL  ·  10000 joint draws  ·  446 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_PIT_win | p_overtime | goals | shots MTL/PIT | MTL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.56 | 0.43 | 0.00 | 6.04 | 27.4/27.7 | 24.5/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.46 | 5.96 | 27.2/27.4 | 24.1/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.57 | 0.43 | 0.00 | 9.44 | 28.8/29.2 | 23.5/22.0 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.084 | 0.50 | 0.50 | 0.00 | 6.05 | 21.9/32.5 | 28.8/18.3 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.49 | 0.51 | 0.46 | 6.06 | 22.0/33.0 | 29.7/18.6 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.071 | 0.43 | 0.57 | 0.00 | 9.35 | 23.1/34.1 | 27.1/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Blake Lizotte: 1+ goals YES | 9 | 0.129 | 0.117 | +0.033 | +0.021 | $2.60 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Phillip Danault: 1+ goals YES | 12 | 0.165 | 0.148 | +0.037 | +0.021 | $2.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 13 | 0.162 | 0.151 | +0.024 | +0.013 | $1.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (10.99 vs 3.21 bp); relationships: KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PIT offense suppressed (<= 2 goals)
- **Phillip Danault: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes; why: higher confidence-adjusted growth (8.64 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: MTL offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31PITMTL-PITECHINAKHOV59-1|yes; why: higher confidence-adjusted growth (3.21 vs 0.00 bp); despite a smaller raw edge (+0.024 vs +0.047/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis MTL:OFFENSE_4PLUS (p 0.4491): highest fidelity KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4097): highest fidelity KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes (same contract)
- KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.375, phi -0.186)
- KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3365, phi -0.192)
- KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.375, phi -0.196)

portfolios: A EV +2.37 (adj +1.41) on $8.43, P(profit) 0.3944, adj growth 12.9 bp · B EV +2.02 (adj +1.20) on $7.13, P(profit) 0.3944, adj growth 11.2 bp · C EV +1.61 (adj +0.91) on $6.60, P(profit) 0.3014, adj growth 8.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ VAN  ·  10000 joint draws  ·  414 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_TOR_win | p_overtime | goals | shots VAN/TOR | VAN/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.50 | 0.50 | 0.00 | 6.05 | 28.3/28.4 | 24.9/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.49 | 0.51 | 0.47 | 5.96 | 28.5/28.7 | 25.3/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.109 | 0.51 | 0.49 | 0.00 | 9.38 | 29.9/30.0 | 23.7/23.6 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.073 | 0.47 | 0.53 | 0.00 | 6.06 | 22.3/33.3 | 29.2/19.0 | even strength |
| TOR shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.46 | 0.54 | 0.47 | 6.0 | 22.9/33.4 | 30.1/19.7 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.061 | 0.55 | 0.45 | 0.00 | 6.05 | 33.0/22.8 | 19.6/29.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Linus Karlsson: 1+ goals YES | 19 | 0.269 | 0.244 | +0.069 | +0.044 | $5.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Vancouver wins by over 1.5 goals YES | 20 | 0.289 | 0.242 | +0.078 | +0.031 | $2.22 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Gavin McKenna: 1+ goals NO | 72 | 0.784 | 0.764 | +0.050 | +0.030 | $9.77 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 16 | 0.211 | 0.187 | +0.042 | +0.018 | $1.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes; why: higher confidence-adjusted growth (25.64 vs 12.30 bp); despite a smaller raw edge (+0.069 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.855 vs 0.522); relationships: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes: REINFORCING (phi 0.218); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: VAN offense suppressed (<= 2 goals)
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (25.64 vs 12.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.218); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: REINFORCING (phi 0.218); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.125); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: REINFORCING (phi 0.204); failure: TOR wins (incl. OT/SO)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes has the higher standalone adjusted growth (12.30 vs 10.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.125); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT31TORVAN-VAN2|yes: MOSTLY_INDEPENDENT (phi 0.125); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: TOR offense succeeds (4+ goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (25.64 vs 4.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLSPREAD-26OCT31TORVAN-VAN2|yes: REINFORCING (phi 0.204); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4305): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLSPREAD-26OCT31TORVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3557): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-TOR5|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.239)
- KXNHLSPREAD-26OCT31TORVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS (p 0.5009, phi -0.639)
- KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4235, phi -0.209)
- KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.212)

portfolios: A EV +3.70 (adj +0.89) on $15.73, P(profit) 0.4991, adj growth 7.7 bp · B EV +3.86 (adj +2.15) on $19.44, P(profit) 0.4935, adj growth 20.1 bp · C EV +4.39 (adj +2.41) on $12.50, P(profit) 0.4368, adj growth 21.7 bp · R EV +0.57 (adj +0.27) on $4.00, P(profit) 0.8233, adj growth 10.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT31TORVAN-VAN|yes == KXNHLGAME-26OCT31TORVAN-TOR|no

## CBJ @ DAL  ·  10000 joint draws  ·  414 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_CBJ_win | p_overtime | goals | shots DAL/CBJ | DAL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.56 | 0.44 | 0.00 | 6.0 | 26.0/25.9 | 22.7/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.47 | 5.9 | 26.5/26.2 | 22.8/23.1 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.090 | 0.62 | 0.38 | 0.00 | 5.91 | 31.0/20.5 | 17.6/26.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.55 | 0.45 | 0.49 | 5.85 | 30.8/20.8 | 17.6/27.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.57 | 0.43 | 0.00 | 9.26 | 28.1/27.7 | 22.2/21.7 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.060 | 0.54 | 0.46 | 0.47 | 2.84 | 24.6/24.4 | 22.9/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie Coyle: 1+ goals YES | 19 | 0.261 | 0.241 | +0.060 | +0.040 | $5.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.184 | 0.165 | +0.046 | +0.027 | $3.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 74 | 0.805 | 0.770 | +0.052 | +0.017 | $3.66 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jason Robertson: 1+ goals NO | 60 | 0.642 | 0.631 | +0.026 | +0.014 | $4.05 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (21.33 vs 13.58 bp); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.144); KXNHLGOAL-26OCT31CBJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (21.33 vs 13.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.116); KXNHLGOAL-26OCT31CBJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: CBJ offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT31CBJDAL-DAL2|no; why: KXNHLSPREAD-26OCT31CBJDAL-DAL2|no has the higher standalone adjusted growth (4.15 vs 3.29 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.734); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.144); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.116); KXNHLGOAL-26OCT31CBJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi 0.14); failure: DAL wins by 2+
- **Jason Robertson: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31CBJDAL-DAL2|no; why: KXNHLSPREAD-26OCT31CBJDAL-DAL2|no has the higher standalone adjusted growth (4.15 vs 1.77 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.162); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.14); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3168): highest fidelity KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4546): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL2|no (same contract)
- thesis DAL:SUPPRESSED (p 0.3994): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.465, phi -0.262)
- KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.465, phi -0.25)
- KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3096, phi -0.734)
- KXNHLGOAL-26OCT31CBJDAL-DALJROBERTSON21-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.378, phi -0.259)

portfolios: A EV +2.79 (adj +1.24) on $15.73, P(profit) 0.4531, adj growth 11.1 bp · B EV +3.16 (adj +1.92) on $16.48, P(profit) 0.3938, adj growth 17.9 bp · C EV +3.12 (adj +1.82) on $15.21, P(profit) 0.2609, adj growth 16.4 bp · R EV +0.15 (adj +0.07) on $3.00, P(profit) 0.6425, adj growth 2.4 bp

## CGY @ COL  ·  10000 joint draws  ·  446 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_CGY_win | p_overtime | goals | shots COL/CGY | COL/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.151 | 0.80 | 0.20 | 0.00 | 6.04 | 35.8/22.7 | 20.6/30.3 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.122 | 0.82 | 0.18 | 0.00 | 9.38 | 37.7/23.9 | 20.0/28.5 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.60 | 0.40 | 0.47 | 5.92 | 36.2/23.2 | 20.0/32.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.77 | 0.23 | 0.00 | 6.05 | 29.8/28.8 | 26.4/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.77 | 0.23 | 0.00 | 9.43 | 31.3/30.2 | 25.6/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.57 | 0.43 | 0.48 | 5.94 | 30.0/29.3 | 26.1/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jonathan Castagna: 1+ goals YES | 8 | 0.110 | 0.100 | +0.025 | +0.015 | $1.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ goals NO | 76 | 0.805 | 0.791 | +0.032 | +0.018 | $9.00 | FUNDED_RESEARCH | $3 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Colorado over 3.5 goals scored NO | 34 | 0.421 | 0.376 | +0.066 | +0.020 | $2.93 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mikael Backlund: 1+ goals YES | 15 | 0.181 | 0.172 | +0.022 | +0.013 | $1.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL2|no; why: higher confidence-adjusted growth (5.90 vs 4.41 bp); despite a smaller raw edge (+0.025 vs +0.104/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31CGYCOL-CGYMBACKLUND11-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CGY offense suppressed (<= 2 goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL2|no; why: KXNHLSPREAD-26OCT31CGYCOL-COL2|no has the higher standalone adjusted growth (4.41 vs 4.28 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.135); relationships: KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4|no: REINFORCING (phi 0.175); KXNHLGOAL-26OCT31CGYCOL-CGYMBACKLUND11-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: COL offense succeeds (4+ goals)
- **Colorado over 3.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL2|no; why: KXNHLSPREAD-26OCT31CGYCOL-COL2|no has the higher standalone adjusted growth (4.41 vs 3.77 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.563); relationships: KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: REINFORCING (phi 0.175); KXNHLGOAL-26OCT31CGYCOL-CGYMBACKLUND11-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: COL offense succeeds (4+ goals)
- **Mikael Backlund: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL2|no; why: Player prop expression KXNHLGOAL-26OCT31CGYCOL-CGYMBACKLUND11-1|yes selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.31 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis CGY:OFFENSE_4PLUS (p 0.2704): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no — Player prop expression KXNHLGOAL-26OCT31CGYCOL-CGYMBACKLUND11-1|yes selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.31 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis GAME:TIGHT (p 0.3825): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no (same contract)
- thesis COL:SUPPRESSED (p 0.2363): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5114, phi -0.172)
- KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5691, phi -0.175)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5691, phi -0.98)
- KXNHLGOAL-26OCT31CGYCOL-CGYMBACKLUND11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5114, phi -0.229)
- override: Player prop expression KXNHLGOAL-26OCT31CGYCOL-CGYMBACKLUND11-1|yes selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.31 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.83 (adj +0.54) on $15.73, P(profit) 0.5677, adj growth 4.7 bp · B EV +1.67 (adj +0.83) on $15.50, P(profit) 0.5172, adj growth 7.8 bp · C EV +1.65 (adj +0.35) on $6.63, P(profit) 0.5206, adj growth 3.2 bp · R EV +0.31 (adj +0.13) on $4.00, P(profit) 0.3733, adj growth 4.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
