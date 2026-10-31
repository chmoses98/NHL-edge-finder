# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T14:22:16Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.48 | +9.66 | +25.29 | 0.708 | -32.00 | -46.27 | 86.09 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +28.24 | +16.08 | +25.46 | 0.698 | -33.43 | -47.85 | 148.21 |
| C best expression per thesis | 149.99 | +22.63 | +11.07 | +20.76 | 0.663 | -40.48 | -54.54 | 98.39 |
| R FUNDED research stakes | 19.00 | +2.39 | +1.38 | +0.33 | 0.605 | -7.57 | -7.79 | 0.00 |

## CHI @ BOS  ·  10000 joint draws  ·  434 bet sides mapped, 4 +EV candidates, 4 on card


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
| Casey Mittelstadt: 1+ goals YES | 16 | 0.212 | 0.198 | +0.043 | +0.029 | $4.66 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 11 | 0.149 | 0.138 | +0.032 | +0.021 | $3.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 22 | 0.265 | 0.251 | +0.033 | +0.019 | $3.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ assists NO | 58 | 0.654 | 0.607 | +0.057 | +0.010 | $5.94 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes; why: higher confidence-adjusted growth (12.42 vs 0.00 bp); despite a smaller raw edge (+0.043 vs +0.043/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.026); failure: BOS offense suppressed (<= 2 goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (9.05 vs 4.51 bp); despite a smaller raw edge (+0.032 vs +0.033/contract); relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.036); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CHIBOS-CHIRDONATO8-1|yes; why: higher confidence-adjusted growth (4.51 vs 0.43 bp); alternative not eligible: confidence-adjusted EV +0.0050 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.167); failure: CHI offense suppressed (<= 2 goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31CHIBOS-CHIPKANE88-1|no; why: higher confidence-adjusted growth (0.95 vs 0.33 bp); despite a smaller raw edge (+0.057 vs +0.085/contract); alternative not eligible: confidence-adjusted EV +0.0059 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.167); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, BOS shot control · normal event (5-7) · decided (2+) 0.12, BOS shot control · high event (8+) · decided (2+) 0.09.
- thesis CHI:OFFENSE_4PLUS (p 0.281): highest fidelity KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.51): highest fidelity KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.5414): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.2565, phi -0.182)
- KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.51, phi -0.208)
- KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.51, phi -0.276)
- KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.281, phi -0.287)

portfolios: A EV +2.80 (adj +1.53) on $16.13, P(profit) 0.4216, adj growth 14.3 bp · B EV +3.15 (adj +1.76) on $17.55, P(profit) 0.4216, adj growth 16.2 bp · C EV +1.54 (adj +0.60) on $13.35, P(profit) 0.265, adj growth 5.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ DET  ·  10000 joint draws  ·  400 bet sides mapped, 4 +EV candidates, 4 on card


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
| Jimmy Snuggerud: 1+ goals YES | 27 | 0.329 | 0.313 | +0.045 | +0.029 | $5.36 | FUNDED_RESEARCH | $2 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Sheldon Dries: 1+ goals YES | 7 | 0.105 | 0.090 | +0.030 | +0.015 | $2.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Lucas Raymond: 1+ assists NO | 58 | 0.657 | 0.616 | +0.060 | +0.019 | $7.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Dylan Holloway: 1+ assists YES | 31 | 0.386 | 0.340 | +0.061 | +0.015 | $1.59 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes; why: higher confidence-adjusted growth (9.21 vs 2.35 bp); despite a smaller raw edge (+0.045 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes: REINFORCING (phi 0.258); failure: STL offense suppressed (<= 2 goals)
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-2|yes; why: higher confidence-adjusted growth (7.11 vs 0.33 bp); alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.032); KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: DET offense suppressed (<= 2 goals)
- **Lucas Raymond: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT31STLDET-DETLRAYMOND23-2|no; why: higher confidence-adjusted growth (3.36 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: DET offense succeeds (4+ goals)
- **Dylan Holloway: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes has the higher standalone adjusted growth (9.21 vs 2.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.258); they share one thesis budget; relationships: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: REINFORCING (phi 0.258); KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.3777): highest fidelity KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4132): highest fidelity KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3659): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3999, phi -0.287)
- KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4132, phi -0.171)
- KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3659, phi -0.257)
- KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 43% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3999, phi -0.311)

portfolios: A EV +2.92 (adj +1.23) on $16.13, P(profit) 0.4775, adj growth 11.2 bp · B EV +2.73 (adj +1.28) on $16.40, P(profit) 0.5216, adj growth 11.9 bp · C EV +2.40 (adj +1.20) on $18.82, P(profit) 0.3292, adj growth 10.7 bp · R EV +0.32 (adj +0.21) on $2.00, P(profit) 0.3292, adj growth 7.4 bp

## TBL @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 6 +EV candidates, 4 on card


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
| Adam Edstrom: 1+ goals YES | 12 | 0.156 | 0.145 | +0.028 | +0.018 | $2.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 26 | 0.313 | 0.297 | +0.040 | +0.024 | $4.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 74 | 0.809 | 0.772 | +0.056 | +0.019 | $8.23 | FUNDED_RESEARCH | $3 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Charle-Edouard D'Astous: 1+ goals NO | 90 | 0.929 | 0.918 | +0.022 | +0.011 | $11.55 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (6.33 vs 6.30 bp); despite a smaller raw edge (+0.028 vs +0.040/contract); relationships: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.105); KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: NSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TBNSH-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TBNSH-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (6.33 vs 6.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TBNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: NSH offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31TBNSH-TB2|no; why: higher confidence-adjusted growth (4.09 vs 2.18 bp); relationships: KXNHLGOAL-26OCT31TBNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.105); KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.096); failure: TBL wins by 2+
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TBNSH-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31TBNSH-TB3|no has the higher standalone adjusted growth (4.09 vs 3.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.096); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TBNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.096); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NSH:OFFENSE_4PLUS (p 0.3613): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS_BY_2PLUS (p 0.2522): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB3|no (same contract)
- thesis NSH:WINS (p 0.4644): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB3|no (same contract)
- KXNHLGOAL-26OCT31TBNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4167, phi -0.197)
- KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4167, phi -0.281)
- KXNHLSPREAD-26OCT31TBNSH-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3117, phi -0.722)
- KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4098, phi -0.122)

portfolios: A EV +1.84 (adj +0.71) on $16.13, P(profit) 0.4213, adj growth 6.3 bp · B EV +2.07 (adj +1.08) on $26.50, P(profit) 0.4, adj growth 10.0 bp · C EV +2.01 (adj +0.93) on $19.66, P(profit) 0.8239, adj growth 8.2 bp · R EV +0.30 (adj +0.11) on $6.00, P(profit) 0.7612, adj growth 4.2 bp

## EDM @ NYI  ·  10000 joint draws  ·  420 bet sides mapped, 10 +EV candidates, 4 on card


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
| Mattias Ekholm: 1+ goals YES | 7 | 0.123 | 0.105 | +0.049 | +0.030 | $3.77 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 13 | 0.178 | 0.165 | +0.041 | +0.027 | $3.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 22 | 0.274 | 0.259 | +0.042 | +0.027 | $4.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Victor Eklund: 1+ goals YES | 17 | 0.214 | 0.200 | +0.034 | +0.021 | $3.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: higher confidence-adjusted growth (27.97 vs 2.55 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.822 vs 0.368); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31EDMNYI-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: higher confidence-adjusted growth (13.36 vs 2.55 bp); despite a smaller raw edge (+0.041 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.863 vs 0.368); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT31EDMNYI-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: EDM offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31EDMNYI-NYIVEKLUND73-1|yes; why: higher confidence-adjusted growth (8.92 vs 6.20 bp); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT31EDMNYI-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NYI offense suppressed (<= 2 goals)
- **Victor Eklund: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (8.92 vs 6.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.4191): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-8|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.4481): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-8|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3296): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-8|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3425, phi -0.156)
- KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3425, phi -0.167)
- KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.368, phi -0.226)
- KXNHLGOAL-26OCT31EDMNYI-NYIVEKLUND73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.368, phi -0.225)

portfolios: A EV +4.64 (adj +2.03) on $16.13, P(profit) 0.5411, adj growth 17.5 bp · B EV +5.11 (adj +3.25) on $15.77, P(profit) 0.5831, adj growth 29.7 bp · C EV +1.74 (adj +0.96) on $9.20, P(profit) 0.4234, adj growth 8.5 bp · R EV +0.65 (adj +0.41) on $1.00, P(profit) 0.1232, adj growth 14.8 bp

## BUF @ LAK  ·  10000 joint draws  ·  414 bet sides mapped, 11 +EV candidates, 4 on card


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
| Alex Laferriere: 2+ goals YES | 3 | 0.054 | 0.046 | +0.022 | +0.013 | $1.61 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.079 | 0.070 | +0.025 | +0.017 | $2.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Corey Perry: 1+ goals YES | 14 | 0.183 | 0.167 | +0.034 | +0.018 | $2.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Scott Laughton: 1+ goals YES | 13 | 0.162 | 0.153 | +0.024 | +0.015 | $2.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Alex Laferriere: 2+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: higher confidence-adjusted growth (12.34 vs 4.54 bp); despite a smaller raw edge (+0.022 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: LAK offense suppressed (<= 2 goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: higher confidence-adjusted growth (12.03 vs 4.54 bp); despite a smaller raw edge (+0.025 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: LAK offense suppressed (<= 2 goals)
- **Corey Perry: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: higher confidence-adjusted growth (5.87 vs 4.54 bp); despite a smaller raw edge (+0.034 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: LAK offense suppressed (<= 2 goals)
- **Scott Laughton: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: KXNHLSPREAD-26OCT31BUFLA-BUF3|no has the higher standalone adjusted growth (4.54 vs 3.93 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.091); relationships: KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.4073): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS_BY_2PLUS (p 0.3119): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no (same contract)
- thesis LAK:WINS (p 0.5431): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no (same contract)
- KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.154)
- KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.13)
- KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.18)
- KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.183)

portfolios: A EV +1.78 (adj +0.56) on $16.13, P(profit) 0.6758, adj growth 5.2 bp · B EV +3.22 (adj +1.99) on $9.00, P(profit) 0.4026, adj growth 18.2 bp · C EV +1.08 (adj +0.37) on $16.89, P(profit) 0.8629, adj growth 3.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ SJS  ·  10000 joint draws  ·  432 bet sides mapped, 3 +EV candidates, 3 on card


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
| Tyler Toffoli: 1+ assists YES | 25 | 0.325 | 0.280 | +0.062 | +0.017 | $2.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Collin Graf: 1+ goals YES | 17 | 0.200 | 0.190 | +0.020 | +0.010 | $1.62 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Claude Giroux: 1+ goals YES | 18 | 0.216 | 0.201 | +0.025 | +0.010 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes; why: higher confidence-adjusted growth (3.18 vs 1.56 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: SJS offense suppressed (<= 2 goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes has the higher standalone adjusted growth (3.18 vs 1.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.056); they share one thesis budget; relationships: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: SJS offense suppressed (<= 2 goals)
- **Claude Giroux: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31OTTSJ-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (1.49 vs 0.57 bp); alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4099): highest fidelity KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4205): highest fidelity KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes (same contract)
- KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.254)
- KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.201)
- KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3637, phi -0.204)

portfolios: A EV +2.08 (adj +0.66) on $10.99, P(profit) 0.5698, adj growth 5.7 bp · B EV +1.10 (adj +0.37) on $6.30, P(profit) 0.5698, adj growth 3.5 bp · C EV +1.38 (adj +0.42) on $6.99, P(profit) 0.473, adj growth 3.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ MTL  ·  10000 joint draws  ·  432 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_PIT_win | p_overtime | goals | shots MTL/PIT | MTL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.54 | 0.46 | 0.00 | 6.05 | 27.1/27.4 | 24.0/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.113 | 0.56 | 0.44 | 0.00 | 9.37 | 28.9/29.1 | 23.4/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.47 | 5.96 | 27.2/27.7 | 24.3/23.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.083 | 0.50 | 0.50 | 0.00 | 6.06 | 21.7/32.6 | 28.9/18.2 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.49 | 0.51 | 0.46 | 5.98 | 21.9/32.4 | 29.1/18.7 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.064 | 0.50 | 0.50 | 0.00 | 9.3 | 23.3/34.7 | 28.0/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Blake Lizotte: 1+ goals YES | 9 | 0.119 | 0.111 | +0.023 | +0.015 | $2.21 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Jake Evans: 1+ goals YES | 12 | 0.156 | 0.142 | +0.029 | +0.015 | $2.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 13 | 0.166 | 0.153 | +0.028 | +0.015 | $2.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Phillip Danault: 1+ goals YES | 13 | 0.166 | 0.152 | +0.028 | +0.014 | $2.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (5.42 vs 4.11 bp); despite a smaller raw edge (+0.023 vs +0.028/contract); relationships: KXNHLGOAL-26OCT31PITMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: PIT offense suppressed (<= 2 goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes; why: higher confidence-adjusted growth (4.19 vs 3.73 bp); relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: PIT wins (incl. OT/SO)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (4.11 vs 0.31 bp); alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT31PITMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: PIT offense suppressed (<= 2 goals)
- **Phillip Danault: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLGOAL-26OCT31PITMTL-MTLJEVANS71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31PITMTL-MTLJEVANS71-1|yes has the higher standalone adjusted growth (4.19 vs 3.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT31PITMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis MTL:WINS_BY_2PLUS (p 0.3151): highest fidelity KXNHLGOAL-26OCT31PITMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-MTLJEVANS71-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4032): highest fidelity KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes (same contract)
- KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.374, phi -0.159)
- KXNHLGOAL-26OCT31PITMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:WINS (p 0.4726, phi -0.206)
- KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.374, phi -0.199)
- KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3426, phi -0.197)

portfolios: A EV +2.17 (adj +1.18) on $9.97, P(profit) 0.4876, adj growth 10.8 bp · B EV +1.99 (adj +1.10) on $9.13, P(profit) 0.4876, adj growth 10.1 bp · C EV +1.45 (adj +0.77) on $6.84, P(profit) 0.2995, adj growth 6.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ VAN  ·  10000 joint draws  ·  400 bet sides mapped, 18 +EV candidates, 4 on card


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
| Marco Rossi: 1+ goals YES | 18 | 0.247 | 0.228 | +0.056 | +0.037 | $6.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 20 | 0.269 | 0.247 | +0.058 | +0.036 | $5.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 71 | 0.784 | 0.763 | +0.060 | +0.039 | $11.55 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 16 | 0.211 | 0.191 | +0.042 | +0.022 | $3.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (19.30 vs 16.63 bp); despite a smaller raw edge (+0.056 vs +0.058/contract); relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes has the higher standalone adjusted growth (19.30 vs 16.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: VAN offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes; why: higher confidence-adjusted growth (16.62 vs 8.10 bp); despite a smaller raw edge (+0.060 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.014 vs 0.522); relationships: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: TOR offense succeeds (4+ goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes has the higher standalone adjusted growth (19.30 vs 7.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4305): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLSPREAD-26OCT31TORVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3557): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-TOR4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.223)
- KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.239)
- KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4235, phi -0.209)
- KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.212)

portfolios: A EV +2.86 (adj +0.53) on $16.13, P(profit) 0.6025, adj growth 4.6 bp · B EV +5.21 (adj +3.24) on $26.87, P(profit) 0.5411, adj growth 30.0 bp · C EV +5.66 (adj +3.40) on $19.63, P(profit) 0.45, adj growth 30.0 bp · R EV +0.25 (adj +0.16) on $3.00, P(profit) 0.7842, adj growth 6.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT31TORVAN-TOR|no == KXNHLGAME-26OCT31TORVAN-VAN|yes

## CBJ @ DAL  ·  10000 joint draws  ·  408 bet sides mapped, 9 +EV candidates, 4 on card


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
| Charlie Coyle: 1+ goals YES | 20 | 0.261 | 0.244 | +0.050 | +0.033 | $5.30 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.184 | 0.162 | +0.046 | +0.024 | $3.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 73 | 0.805 | 0.765 | +0.061 | +0.021 | $8.44 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Damon Severson: 1+ goals YES | 8 | 0.105 | 0.096 | +0.020 | +0.011 | $1.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (14.30 vs 10.15 bp); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.144); KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (14.30 vs 10.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.116); KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CBJ offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT31CBJDAL-DAL2|no; why: higher confidence-adjusted growth (5.27 vs 4.15 bp); despite a smaller raw edge (+0.061 vs +0.064/contract); wins across more scripts (relative breadth 0.993 vs 0.884); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.144); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.116); KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.068); failure: DAL wins by 2+
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (14.30 vs 3.41 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.068); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3168): highest fidelity KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4546): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL3|no (same contract)
- thesis CBJ:WINS (p 0.4504): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL3|no (same contract)
- KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.465, phi -0.262)
- KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.465, phi -0.25)
- KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3096, phi -0.734)
- KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.465, phi -0.151)

portfolios: A EV +2.00 (adj +0.60) on $16.13, P(profit) 0.5033, adj growth 5.2 bp · B EV +3.35 (adj +1.82) on $18.39, P(profit) 0.445, adj growth 16.7 bp · C EV +3.14 (adj +1.68) on $23.58, P(profit) 0.2609, adj growth 14.9 bp · R EV +0.72 (adj +0.40) on $5.00, P(profit) 0.2609, adj growth 14.3 bp

## CGY @ COL  ·  10000 joint draws  ·  434 bet sides mapped, 11 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_CGY_win | p_overtime | goals | shots COL/CGY | COL/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.151 | 0.80 | 0.20 | 0.00 | 6.04 | 35.8/22.7 | 20.5/30.4 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.122 | 0.82 | 0.18 | 0.00 | 9.38 | 37.7/24.0 | 20.1/28.5 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.61 | 0.39 | 0.47 | 5.92 | 36.2/23.1 | 20.0/32.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.77 | 0.23 | 0.00 | 6.06 | 29.8/28.8 | 26.4/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.77 | 0.23 | 0.00 | 9.43 | 31.3/30.2 | 25.6/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.57 | 0.43 | 0.48 | 5.95 | 30.0/29.3 | 26.1/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nathan MacKinnon: 1+ goals NO | 50 | 0.557 | 0.542 | +0.040 | +0.024 | $4.10 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL2|no; why: higher confidence-adjusted growth (5.08 vs 4.41 bp); despite a smaller raw edge (+0.040 vs +0.104/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.057 vs 0.855); relationships: only recommended bet in this game; failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:SUPPRESSED (p 0.2363): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CGYCOL-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.3825): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.2704): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31CGYCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5691, phi -0.284)

portfolios: A EV +3.38 (adj +0.63) on $16.13, P(profit) 0.5718, adj growth 5.3 bp · B EV +0.31 (adj +0.19) on $4.10, P(profit) 0.5571, adj growth 1.8 bp · C EV +2.22 (adj +0.74) on $15.03, P(profit) 0.5571, adj growth 6.6 bp · R EV +0.15 (adj +0.09) on $2.00, P(profit) 0.5571, adj growth 3.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
