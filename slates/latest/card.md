# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T12:59:15Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.97 | +24.40 | +8.42 | +23.66 | 0.715 | -30.36 | -43.62 | 75.23 |
| B thesis-diversified (joint) ← optimiser card | 149.22 | +26.88 | +13.16 | +23.84 | 0.692 | -31.51 | -46.06 | 119.87 |
| C best expression per thesis | 149.99 | +22.01 | +8.64 | +20.22 | 0.691 | -29.95 | -43.85 | 77.71 |
| R FUNDED research stakes | 24.00 | +3.92 | +1.92 | +1.30 | 0.547 | -8.10 | -10.29 | 0.00 |

## CHI @ BOS  ·  10000 joint draws  ·  434 bet sides mapped, 6 +EV candidates, 4 on card


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
| Casey Mittelstadt: 1+ goals YES | 16 | 0.212 | 0.198 | +0.043 | +0.029 | $5.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 22 | 0.265 | 0.251 | +0.033 | +0.019 | $3.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 11 | 0.149 | 0.132 | +0.032 | +0.015 | $2.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Roman Kantserov: 1+ goals NO | 76 | 0.794 | 0.784 | +0.021 | +0.011 | $8.12 | FUNDED_RESEARCH | $3 | CHI:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes; why: higher confidence-adjusted growth (12.42 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: BOS offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT31CHIBOS-2|yes; why: higher confidence-adjusted growth (4.51 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: CHI offense suppressed (<= 2 goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (4.51 vs 4.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense suppressed (<= 2 goals)
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no; why: Player prop expression KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.88 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, BOS shot control · normal event (5-7) · decided (2+) 0.12, BOS shot control · high event (8+) · decided (2+) 0.09.
- thesis CHI:OFFENSE_4PLUS (p 0.281): highest fidelity KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.51): highest fidelity KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no — Player prop expression KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.88 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis BOS:OFFENSE_4PLUS (p 0.5414): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.2565, phi -0.182)
- KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.51, phi -0.276)
- KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.51, phi -0.208)
- KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.281, phi -0.196)
- override: Player prop expression KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.88 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.09 (adj +1.55) on $17.10, P(profit) 0.4216, adj growth 14.4 bp · B EV +2.72 (adj +1.61) on $19.51, P(profit) 0.4683, adj growth 14.7 bp · C EV +2.07 (adj +0.80) on $16.66, P(profit) 0.7811, adj growth 7.2 bp · R EV +0.08 (adj +0.04) on $3.00, P(profit) 0.7937, adj growth 1.5 bp

## STL @ DET  ·  10000 joint draws  ·  378 bet sides mapped, 5 +EV candidates, 4 on card


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
| Sheldon Dries: 1+ goals YES | 7 | 0.105 | 0.091 | +0.030 | +0.016 | $2.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 28 | 0.329 | 0.314 | +0.035 | +0.020 | $4.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Lucas Raymond: 1+ assists NO | 58 | 0.657 | 0.616 | +0.060 | +0.019 | $9.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Alex DeBrincat: 1+ goals YES | 36 | 0.408 | 0.394 | +0.032 | +0.018 | $5.52 | FUNDED_RESEARCH | $2 | DET:OFFENSE_4PLUS | DIRECT (0.60) | EVIDENCE_STRONGER | D |
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (8.32 vs 2.93 bp); despite a smaller raw edge (+0.030 vs +0.032/contract); relationships: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: DET offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes; why: higher confidence-adjusted growth (4.32 vs 2.35 bp); despite a smaller raw edge (+0.035 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: STL offense suppressed (<= 2 goals)
- **Lucas Raymond: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT31STLDET-DETLRAYMOND23-1|no; why: higher confidence-adjusted growth (3.36 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.174); failure: DET offense succeeds (4+ goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PSPREAD-26OCT31STLDET-DET2|yes; why: higher confidence-adjusted growth (2.93 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.91 vs 0.8); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: INTENTIONAL_DIVERSIFIER (phi -0.174); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.3777): highest fidelity KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4132): highest fidelity KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3659): highest fidelity KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes (same contract)
- KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4132, phi -0.171)
- KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3999, phi -0.287)
- KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3659, phi -0.257)
- KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 40% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4132, phi -0.316)

portfolios: A EV +2.19 (adj +0.80) on $17.10, P(profit) 0.5823, adj growth 7.3 bp · B EV +3.04 (adj +1.45) on $22.60, P(profit) 0.4974, adj growth 13.2 bp · C EV +2.48 (adj +1.10) on $24.50, P(profit) 0.4385, adj growth 9.9 bp · R EV +0.17 (adj +0.09) on $2.00, P(profit) 0.4085, adj growth 3.2 bp

## TBL @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 3 +EV candidates, 2 on card


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
| Ryan O'Reilly: 1+ goals YES | 26 | 0.313 | 0.297 | +0.040 | +0.024 | $4.66 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 74 | 0.809 | 0.772 | +0.056 | +0.019 | $11.70 | FUNDED_RESEARCH | $3 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31TBNSH-TB3|no; why: higher confidence-adjusted growth (6.30 vs 4.09 bp); despite a smaller raw edge (+0.040 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.147); failure: NSH offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31TBNSH-TB2|no; why: higher confidence-adjusted growth (4.09 vs 2.18 bp); relationships: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.147); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NSH:OFFENSE_4PLUS (p 0.3613): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS (p 0.4644): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB3|no (same contract)
- KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4167, phi -0.281)
- KXNHLSPREAD-26OCT31TBNSH-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3117, phi -0.722)

portfolios: A EV +1.62 (adj +0.69) on $17.10, P(profit) 0.7148, adj growth 6.3 bp · B EV +1.54 (adj +0.70) on $16.36, P(profit) 0.3133, adj growth 6.4 bp · C EV +1.89 (adj +0.86) on $20.09, P(profit) 0.3133, adj growth 7.7 bp · R EV +0.22 (adj +0.07) on $3.00, P(profit) 0.8091, adj growth 2.8 bp

## EDM @ NYI  ·  10000 joint draws  ·  420 bet sides mapped, 12 +EV candidates, 4 on card


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
| Mattias Ekholm: 1+ goals YES | 7 | 0.123 | 0.105 | +0.049 | +0.030 | $4.54 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.182 | 0.160 | +0.055 | +0.033 | $5.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 22 | 0.274 | 0.259 | +0.042 | +0.027 | $5.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 33 | 0.449 | 0.368 | +0.104 | +0.023 | $6.49 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.68) | EVIDENCE_MIXED | D |
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31EDMNYI-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (27.97 vs 3.53 bp); despite a smaller raw edge (+0.049 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.121); failure: EDM offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (20.90 vs 8.92 bp); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NYI offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes has the higher standalone adjusted growth (20.90 vs 8.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: NYI offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (5.10 vs 1.09 bp); alternative not eligible: confidence-adjusted EV +0.0100 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.121); KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.4191): highest fidelity KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3425): highest fidelity KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.4481): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLAST-26OCT31EDMNYI-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3425, phi -0.156)
- KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.368, phi -0.212)
- KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.368, phi -0.226)
- KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 32% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.4 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4481, phi -0.309)

portfolios: A EV +4.24 (adj +1.62) on $17.10, P(profit) 0.5062, adj growth 15.0 bp · B EV +8.11 (adj +4.25) on $21.56, P(profit) 0.4749, adj growth 38.5 bp · C EV +6.64 (adj +2.66) on $21.88, P(profit) 0.6179, adj growth 23.7 bp · R EV +1.30 (adj +0.81) on $2.00, P(profit) 0.1232, adj growth 26.6 bp

## BUF @ LAK  ·  10000 joint draws  ·  414 bet sides mapped, 8 +EV candidates, 4 on card


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
| Alex Laferriere: 2+ goals YES | 3 | 0.054 | 0.047 | +0.022 | +0.015 | $2.06 | FUNDED_RESEARCH | $1 | LAK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Corey Perry: 1+ goals YES | 14 | 0.183 | 0.165 | +0.034 | +0.016 | $2.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Andre Lee: 1+ goals YES | 10 | 0.131 | 0.118 | +0.025 | +0.012 | $1.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Scott Laughton: 1+ goals YES | 13 | 0.162 | 0.151 | +0.024 | +0.013 | $2.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Alex Laferriere: 2+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: higher confidence-adjusted growth (14.66 vs 4.54 bp); despite a smaller raw edge (+0.022 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: LAK offense suppressed (<= 2 goals)
- **Corey Perry: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: KXNHLSPREAD-26OCT31BUFLA-BUF3|no has the higher standalone adjusted growth (4.54 vs 4.40 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.091); relationships: KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: LAK offense suppressed (<= 2 goals)
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: KXNHLSPREAD-26OCT31BUFLA-BUF3|no has the higher standalone adjusted growth (4.54 vs 3.29 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.076); relationships: KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: LAK offense suppressed (<= 2 goals)
- **Scott Laughton: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: KXNHLSPREAD-26OCT31BUFLA-BUF3|no has the higher standalone adjusted growth (4.54 vs 3.29 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.091); relationships: KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.4073): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF3|no (same contract)
- thesis LAK:WINS (p 0.5431): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF3|no (same contract)
- thesis BUF:SUPPRESSED (p 0.4342): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF3|no (same contract)
- KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.154)
- KXNHLGOAL-26OCT31BUFLA-LACPERRY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.18)
- KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.162)
- KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.183)

portfolios: A EV +2.22 (adj +0.68) on $17.10, P(profit) 0.4116, adj growth 6.0 bp · B EV +2.95 (adj +1.72) on $9.31, P(profit) 0.439, adj growth 15.5 bp · C EV +1.02 (adj +0.35) on $16.07, P(profit) 0.8629, adj growth 3.3 bp · R EV +0.69 (adj +0.46) on $1.00, P(profit) 0.0541, adj growth 14.7 bp

## OTT @ SJS  ·  10000 joint draws  ·  432 bet sides mapped, 2 +EV candidates, 2 on card


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
| Claude Giroux: 1+ goals YES | 18 | 0.215 | 0.201 | +0.025 | +0.011 | $2.04 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Tyler Toffoli: 1+ assists YES | 25 | 0.325 | 0.275 | +0.062 | +0.012 | $2.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Claude Giroux: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31OTTSJ-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (1.64 vs 0.46 bp); alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: OTT offense suppressed (<= 2 goals)
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31OTTSJ-SJMMISA77-1|yes; why: higher confidence-adjusted growth (1.57 vs 1.03 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis OTT:OFFENSE_4PLUS (p 0.4205): highest fidelity KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.4099): highest fidelity KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes (same contract)
- KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3637, phi -0.206)
- KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.254)

portfolios: A EV +1.94 (adj +0.45) on $9.43, P(profit) 0.4676, adj growth 3.6 bp · B EV +0.81 (adj +0.22) on $4.38, P(profit) 0.4676, adj growth 2.0 bp · C EV +1.00 (adj +0.27) on $5.37, P(profit) 0.4676, adj growth 2.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ MTL  ·  10000 joint draws  ·  432 bet sides mapped, 1 +EV candidates, 1 on card


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
| Connor Dewar: 1+ goals YES | 12 | 0.166 | 0.145 | +0.038 | +0.018 | $2.99 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT31PITMTL-PIT6|yes; why: higher confidence-adjusted growth (6.33 vs 0.33 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.867 vs 0.307); alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4032): highest fidelity KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes (same contract)
- KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.374, phi -0.199)

portfolios: A EV +1.12 (adj +0.53) on $3.74, P(profit) 0.1656, adj growth 4.7 bp · B EV +0.90 (adj +0.42) on $2.99, P(profit) 0.1656, adj growth 3.9 bp · C EV +1.10 (adj +0.52) on $3.67, P(profit) 0.1656, adj growth 4.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ VAN  ·  10000 joint draws  ·  400 bet sides mapped, 10 +EV candidates, 4 on card


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
| Toronto wins by over 2.5 goals NO | 73 | 0.821 | 0.773 | +0.077 | +0.029 | $13.09 | FUNDED_RESEARCH | $4 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Linus Karlsson: 1+ goals YES | 21 | 0.269 | 0.246 | +0.048 | +0.024 | $4.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 20 | 0.247 | 0.231 | +0.035 | +0.020 | $3.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 74 | 0.784 | 0.767 | +0.031 | +0.013 | $7.30 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Toronto wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes; why: higher confidence-adjusted growth (9.91 vs 4.87 bp); wins across more scripts (relative breadth 1.029 vs 0.522); relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.12); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.139); failure: TOR wins by 2+
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31TORVAN-TOR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31TORVAN-TOR3|no has the higher standalone adjusted growth (9.91 vs 7.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.120); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31TORVAN-TOR3|no: MOSTLY_INDEPENDENT (phi 0.12); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31TORVAN-TOR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31TORVAN-TOR3|no has the higher standalone adjusted growth (9.91 vs 5.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.132); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31TORVAN-TOR3|no: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: VAN offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TORVAN-TOR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31TORVAN-TOR3|no has the higher standalone adjusted growth (9.91 vs 2.13 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.139); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31TORVAN-TOR3|no: MOSTLY_INDEPENDENT (phi 0.139); KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:WINS (p 0.4991): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-TOR3|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.4305): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-TOR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-TOR3|no (same contract)
- KXNHLSPREAD-26OCT31TORVAN-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2836, phi -0.742)
- KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.239)
- KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.223)
- KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4235, phi -0.209)

portfolios: A EV +2.57 (adj +0.77) on $17.10, P(profit) 0.5523, adj growth 6.8 bp · B EV +3.16 (adj +1.44) on $28.11, P(profit) 0.4208, adj growth 13.3 bp · C EV +1.67 (adj +0.63) on $16.07, P(profit) 0.8211, adj growth 6.0 bp · R EV +0.50 (adj +0.19) on $6.00, P(profit) 0.6658, adj growth 7.2 bp

## CBJ @ DAL  ·  10000 joint draws  ·  408 bet sides mapped, 7 +EV candidates, 3 on card


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
| Charlie Coyle: 1+ goals YES | 21 | 0.261 | 0.246 | +0.039 | +0.024 | $4.34 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 14 | 0.184 | 0.164 | +0.035 | +0.016 | $2.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Dallas wins by over 1.5 goals NO | 61 | 0.690 | 0.648 | +0.064 | +0.021 | $6.63 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (7.28 vs 4.21 bp); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT31CBJDAL-DAL2|no: REINFORCING (phi 0.161); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (7.28 vs 4.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT31CBJDAL-DAL2|no: MOSTLY_INDEPENDENT (phi 0.145); failure: CBJ offense suppressed (<= 2 goals)
- **Dallas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT31CBJDAL-DAL3|no; why: higher confidence-adjusted growth (4.15 vs 2.38 bp); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: REINFORCING (phi 0.161); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.145); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3168): highest fidelity KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4546): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL2|no (same contract)
- thesis CBJ:WINS (p 0.4504): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL2|no (same contract)
- KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.465, phi -0.262)
- KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.465, phi -0.25)
- KXNHLSPREAD-26OCT31CBJDAL-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3096, phi -1.0)

portfolios: A EV +2.05 (adj +0.60) on $17.10, P(profit) 0.7088, adj growth 5.1 bp · B EV +2.01 (adj +0.94) on $13.33, P(profit) 0.3938, adj growth 8.6 bp · C EV +1.94 (adj +0.91) on $15.10, P(profit) 0.7384, adj growth 8.1 bp · R EV +0.20 (adj +0.07) on $2.00, P(profit) 0.6904, adj growth 2.5 bp

## CGY @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 3 on card


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
| Calgary over 3.5 goals scored YES | 21 | 0.280 | 0.240 | +0.058 | +0.018 | $2.14 | FUNDED_RESEARCH | $1 | CGY:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 53 | 0.650 | 0.569 | +0.102 | +0.021 | $4.31 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado over 5.5 goals scored NO | 75 | 0.807 | 0.774 | +0.044 | +0.011 | $4.62 | FUNDED_RESEARCH | $2 | CGY:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Calgary over 3.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL3|no; why: higher confidence-adjusted growth (4.14 vs 4.00 bp); despite a smaller raw edge (+0.058 vs +0.102/contract); relationships: KXNHLSPREAD-26OCT31CGYCOL-COL3|no: REINFORCING (phi 0.361); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: MOSTLY_INDEPENDENT (phi -0.02); failure: CGY offense suppressed (<= 2 goals)
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL2|no; why: higher confidence-adjusted growth (4.00 vs 2.08 bp); wins across more scripts (relative breadth 1.041 vs 0.855); relationships: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: REINFORCING (phi 0.361); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: REINFORCING (phi 0.469); failure: COL wins by 2+
- **Colorado over 5.5 goals scored NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes has the higher standalone adjusted growth (4.14 vs 1.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.020); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLSPREAD-26OCT31CGYCOL-COL3|no: REINFORCING (phi 0.469); failure: high-event game (8+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis CGY:OFFENSE_4PLUS (p 0.2704): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS_BY_2PLUS (p 0.1381): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL3|no (same contract)
- thesis CGY:WINS (p 0.2997): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL3|no (same contract)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:SUPPRESSED (p 0.5114, phi -0.637)
- KXNHLSPREAD-26OCT31CGYCOL-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.5 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4794, phi -0.765)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.3121, phi -0.577)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT31CGYCOL-COL2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no kept
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT31CGYCOL-COL2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes kept

portfolios: A EV +3.35 (adj +0.73) on $17.10, P(profit) 0.5595, adj growth 6.1 bp · B EV +1.63 (adj +0.41) on $11.07, P(profit) 0.6499, adj growth 3.8 bp · C EV +2.20 (adj +0.54) on $10.58, P(profit) 0.6704, adj growth 4.8 bp · R EV +0.75 (adj +0.19) on $5.00, P(profit) 0.6499, adj growth 6.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
