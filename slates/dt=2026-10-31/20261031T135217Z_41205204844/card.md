# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T13:52:17Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +24.25 | +8.45 | +23.84 | 0.730 | -26.25 | -38.46 | 76.70 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +29.84 | +16.98 | +26.28 | 0.700 | -34.76 | -49.06 | 155.94 |
| C best expression per thesis | 150.00 | +24.50 | +11.76 | +21.94 | 0.674 | -36.61 | -50.44 | 105.68 |
| R FUNDED research stakes | 20.00 | +2.93 | +1.46 | +0.60 | 0.529 | -5.49 | -8.29 | 0.00 |

## CHI @ BOS  ·  10000 joint draws  ·  434 bet sides mapped, 8 +EV candidates, 4 on card


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
| Casey Mittelstadt: 1+ goals YES | 16 | 0.212 | 0.198 | +0.043 | +0.029 | $4.60 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 11 | 0.149 | 0.135 | +0.032 | +0.018 | $2.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| William Borgen: 1+ goals YES | 6 | 0.084 | 0.077 | +0.020 | +0.013 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | GAME:EMPTY_NET | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 22 | 0.265 | 0.251 | +0.033 | +0.019 | $3.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes; why: higher confidence-adjusted growth (12.42 vs 0.00 bp); despite a smaller raw edge (+0.043 vs +0.043/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CHIBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: BOS offense suppressed (<= 2 goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (7.02 vs 4.51 bp); despite a smaller raw edge (+0.032 vs +0.033/contract); relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CHIBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: CHI offense suppressed (<= 2 goals)
- **William Borgen: 1+ goals YES** — thesis: an empty-net goal is scored; alternative: KXNHL3PTOTAL-26OCT31CHIBOS-3|yes; why: higher confidence-adjusted growth (5.73 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: BOS offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CHIBOS-CHIRDONATO8-1|yes; why: higher confidence-adjusted growth (4.51 vs 0.11 bp); alternative not eligible: confidence-adjusted EV +0.0025 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT31CHIBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, BOS shot control · normal event (5-7) · decided (2+) 0.12, BOS shot control · high event (8+) · decided (2+) 0.09.
- thesis CHI:OFFENSE_4PLUS (p 0.281): highest fidelity KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.51): highest fidelity KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31CHIBOS-CHIPKANE88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.5414): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.2565, phi -0.182)
- KXNHLGOAL-26OCT31CHIBOS-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.51, phi -0.208)
- KXNHLGOAL-26OCT31CHIBOS-BOSWBORGEN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.2565, phi -0.13)
- KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.51, phi -0.276)

portfolios: A EV +2.47 (adj +1.00) on $16.71, P(profit) 0.6951, adj growth 9.4 bp · B EV +2.91 (adj +1.82) on $12.41, P(profit) 0.5444, adj growth 16.7 bp · C EV +0.90 (adj +0.52) on $14.05, P(profit) 0.265, adj growth 4.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ DET  ·  10000 joint draws  ·  398 bet sides mapped, 5 +EV candidates, 4 on card


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
| Jimmy Snuggerud: 1+ goals YES | 27 | 0.329 | 0.313 | +0.045 | +0.029 | $5.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Sheldon Dries: 1+ goals YES | 7 | 0.105 | 0.091 | +0.030 | +0.016 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Lucas Raymond: 1+ assists NO | 58 | 0.657 | 0.616 | +0.060 | +0.019 | $8.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Alex DeBrincat: 1+ goals YES | 36 | 0.408 | 0.395 | +0.032 | +0.019 | $5.22 | FUNDED_RESEARCH | $2 | DET:OFFENSE_4PLUS | DIRECT (0.60) | EVIDENCE_STRONGER | D |
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes; why: higher confidence-adjusted growth (9.21 vs 2.35 bp); despite a smaller raw edge (+0.045 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: STL offense suppressed (<= 2 goals)
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (8.32 vs 3.36 bp); despite a smaller raw edge (+0.030 vs +0.032/contract); relationships: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: DET offense suppressed (<= 2 goals)
- **Lucas Raymond: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31STLDET-DETMSEIDER53-1|no; why: higher confidence-adjusted growth (3.36 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0006 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.174); failure: DET offense succeeds (4+ goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-2|yes; why: higher confidence-adjusted growth (3.36 vs 0.33 bp); alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: INTENTIONAL_DIVERSIFIER (phi -0.174); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.3777): highest fidelity KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4132): highest fidelity KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3659): highest fidelity KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes (same contract)
- KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3999, phi -0.287)
- KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4132, phi -0.171)
- KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3659, phi -0.257)
- KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 40% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4132, phi -0.316)

portfolios: A EV +2.29 (adj +0.94) on $16.71, P(profit) 0.4747, adj growth 8.7 bp · B EV +3.18 (adj +1.64) on $22.17, P(profit) 0.4974, adj growth 15.1 bp · C EV +2.97 (adj +1.51) on $26.00, P(profit) 0.4888, adj growth 13.6 bp · R EV +0.17 (adj +0.10) on $2.00, P(profit) 0.4085, adj growth 3.5 bp

## TBL @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 4 +EV candidates, 3 on card


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
| Ryan O'Reilly: 1+ goals YES | 26 | 0.313 | 0.299 | +0.040 | +0.025 | $4.43 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 12 | 0.156 | 0.143 | +0.028 | +0.016 | $2.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 74 | 0.809 | 0.772 | +0.056 | +0.019 | $9.13 | FUNDED_RESEARCH | $3 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TBNSH-NSHAEDSTROM84-1|yes; why: higher confidence-adjusted growth (6.98 vs 4.71 bp); relationships: KXNHLGOAL-26OCT31TBNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.147); failure: NSH offense suppressed (<= 2 goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes has the higher standalone adjusted growth (6.98 vs 4.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.105); failure: NSH offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31TBNSH-TB2|no; why: higher confidence-adjusted growth (4.09 vs 2.18 bp); relationships: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT31TBNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.105); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NSH:OFFENSE_4PLUS (p 0.3613): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS (p 0.4644): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB3|no (same contract)
- KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4167, phi -0.281)
- KXNHLGOAL-26OCT31TBNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4167, phi -0.197)
- KXNHLSPREAD-26OCT31TBNSH-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3117, phi -0.722)

portfolios: A EV +1.59 (adj +0.70) on $16.71, P(profit) 0.7148, adj growth 6.3 bp · B EV +1.80 (adj +0.90) on $15.74, P(profit) 0.4193, adj growth 8.3 bp · C EV +1.84 (adj +0.87) on $19.28, P(profit) 0.3133, adj growth 7.8 bp · R EV +0.22 (adj +0.07) on $3.00, P(profit) 0.8091, adj growth 2.8 bp

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
| Mattias Ekholm: 1+ goals YES | 7 | 0.123 | 0.105 | +0.049 | +0.030 | $3.74 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.182 | 0.164 | +0.055 | +0.037 | $5.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 13 | 0.178 | 0.165 | +0.041 | +0.027 | $4.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 22 | 0.274 | 0.259 | +0.042 | +0.027 | $4.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31EDMNYI-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (27.97 vs 4.54 bp); despite a smaller raw edge (+0.049 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: EDM offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (25.84 vs 8.92 bp); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: NYI offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31EDMNYI-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (13.36 vs 4.54 bp); despite a smaller raw edge (+0.041 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: EDM offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes has the higher standalone adjusted growth (25.84 vs 8.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.4191): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.4481): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLAST-26OCT31EDMNYI-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3425): highest fidelity KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no (same contract)
- KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3425, phi -0.156)
- KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.368, phi -0.212)
- KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3425, phi -0.167)
- KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.368, phi -0.226)

portfolios: A EV +4.15 (adj +1.68) on $16.71, P(profit) 0.5062, adj growth 15.7 bp · B EV +6.74 (adj +4.39) on $17.67, P(profit) 0.5652, adj growth 40.1 bp · C EV +6.49 (adj +2.91) on $21.13, P(profit) 0.3978, adj growth 26.0 bp · R EV +0.65 (adj +0.41) on $1.00, P(profit) 0.1232, adj growth 14.8 bp

## BUF @ LAK  ·  10000 joint draws  ·  414 bet sides mapped, 10 +EV candidates, 4 on card


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
| Alex Laferriere: 2+ goals YES | 3 | 0.054 | 0.047 | +0.022 | +0.015 | $1.76 | FUNDED_RESEARCH | $1 | LAK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.079 | 0.070 | +0.025 | +0.017 | $2.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 2.5 goals NO | 80 | 0.863 | 0.829 | +0.052 | +0.018 | $11.64 | FUNDED_RESEARCH | $3 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Scott Laughton: 1+ goals YES | 13 | 0.162 | 0.153 | +0.024 | +0.015 | $2.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Alex Laferriere: 2+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: higher confidence-adjusted growth (14.66 vs 4.54 bp); despite a smaller raw edge (+0.022 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT31BUFLA-BUF3|no: MOSTLY_INDEPENDENT (phi 0.075); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: LAK offense suppressed (<= 2 goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: higher confidence-adjusted growth (12.03 vs 4.54 bp); despite a smaller raw edge (+0.025 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT31BUFLA-BUF3|no: MOSTLY_INDEPENDENT (phi 0.065); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: LAK offense suppressed (<= 2 goals)
- **Buffalo wins by over 2.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF2|no; why: higher confidence-adjusted growth (4.54 vs 2.54 bp); relationships: KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: MOSTLY_INDEPENDENT (phi 0.075); KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.065); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.091); failure: BUF wins by 2+
- **Scott Laughton: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31BUFLA-BUF3|no has the higher standalone adjusted growth (4.54 vs 3.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.091); they share one thesis budget; relationships: KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLSPREAD-26OCT31BUFLA-BUF3|no: MOSTLY_INDEPENDENT (phi 0.091); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.4073): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF3|no [DIRECT], best adjusted EV KXNHLAST-26OCT31BUFLA-LATMOORE12-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS_BY_2PLUS (p 0.3119): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF3|no (same contract)
- thesis LAK:WINS (p 0.5431): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF3|no (same contract)
- KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.154)
- KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.13)
- KXNHLSPREAD-26OCT31BUFLA-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2349, phi -0.719)
- KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3724, phi -0.183)

portfolios: A EV +1.78 (adj +0.55) on $16.71, P(profit) 0.6758, adj growth 5.0 bp · B EV +3.35 (adj +1.98) on $17.70, P(profit) 0.2585, adj growth 18.1 bp · C EV +0.97 (adj +0.33) on $15.27, P(profit) 0.8629, adj growth 3.1 bp · R EV +0.88 (adj +0.53) on $4.00, P(profit) 0.0541, adj growth 17.1 bp

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
| Tyler Toffoli: 1+ assists YES | 25 | 0.325 | 0.277 | +0.062 | +0.014 | $2.45 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Collin Graf: 1+ goals YES | 17 | 0.200 | 0.190 | +0.020 | +0.010 | $1.64 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes; why: higher confidence-adjusted growth (2.31 vs 1.56 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.056); failure: SJS offense suppressed (<= 2 goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes has the higher standalone adjusted growth (2.31 vs 1.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.056); they share one thesis budget; relationships: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.056); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4099): highest fidelity KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes (same contract)
- KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.254)
- KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.201)

portfolios: A EV +1.80 (adj +0.48) on $8.75, P(profit) 0.4496, adj growth 4.0 bp · B EV +0.76 (adj +0.23) on $4.09, P(profit) 0.4496, adj growth 2.1 bp · C EV +0.79 (adj +0.18) on $3.36, P(profit) 0.3249, adj growth 1.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ MTL  ·  10000 joint draws  ·  432 bet sides mapped, 3 +EV candidates, 3 on card


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
| Blake Lizotte: 1+ goals YES | 9 | 0.119 | 0.111 | +0.023 | +0.015 | $2.20 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 13 | 0.166 | 0.153 | +0.028 | +0.015 | $2.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Phillip Danault: 1+ goals YES | 13 | 0.166 | 0.150 | +0.028 | +0.012 | $1.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (5.42 vs 4.11 bp); despite a smaller raw edge (+0.023 vs +0.028/contract); relationships: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT31PITMTL-PIT6|yes; why: higher confidence-adjusted growth (4.11 vs 0.33 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.867 vs 0.307); alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: PIT offense suppressed (<= 2 goals)
- **Phillip Danault: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLGOAL-26OCT31PITMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (2.54 vs 0.54 bp); alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4032): highest fidelity KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes (same contract)
- thesis MTL:WINS_BY_2PLUS (p 0.3151): highest fidelity KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes (same contract)
- KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.374, phi -0.159)
- KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.374, phi -0.199)
- KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3426, phi -0.197)

portfolios: A EV +1.63 (adj +0.86) on $7.58, P(profit) 0.3903, adj growth 7.8 bp · B EV +1.39 (adj +0.76) on $6.43, P(profit) 0.3903, adj growth 7.0 bp · C EV +1.13 (adj +0.55) on $5.56, P(profit) 0.3067, adj growth 4.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ VAN  ·  10000 joint draws  ·  400 bet sides mapped, 14 +EV candidates, 4 on card


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
| Marco Rossi: 1+ goals YES | 18 | 0.247 | 0.229 | +0.056 | +0.038 | $6.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 20 | 0.269 | 0.246 | +0.058 | +0.035 | $5.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 72 | 0.784 | 0.764 | +0.050 | +0.030 | $11.64 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 16 | 0.211 | 0.191 | +0.042 | +0.022 | $3.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (20.61 vs 15.50 bp); despite a smaller raw edge (+0.056 vs +0.058/contract); relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes has the higher standalone adjusted growth (20.61 vs 15.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: VAN offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes; why: higher confidence-adjusted growth (10.37 vs 4.87 bp); despite a smaller raw edge (+0.050 vs +0.057/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.014 vs 0.522); relationships: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: TOR offense succeeds (4+ goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes has the higher standalone adjusted growth (20.61 vs 7.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4305): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3557): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-TOR4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31TORVAN-TOR4|no (same contract)
- KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.223)
- KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.239)
- KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4235, phi -0.209)
- KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.212)

portfolios: A EV +2.97 (adj +0.57) on $16.71, P(profit) 0.6025, adj growth 4.9 bp · B EV +5.08 (adj +3.13) on $27.06, P(profit) 0.5411, adj growth 28.9 bp · C EV +4.81 (adj +3.00) on $16.98, P(profit) 0.45, adj growth 26.8 bp · R EV +0.20 (adj +0.12) on $3.00, P(profit) 0.7842, adj growth 4.7 bp

## CBJ @ DAL  ·  10000 joint draws  ·  408 bet sides mapped, 7 +EV candidates, 4 on card


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
| Charlie Coyle: 1+ goals YES | 20 | 0.261 | 0.244 | +0.050 | +0.033 | $5.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.184 | 0.164 | +0.046 | +0.026 | $3.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 73 | 0.805 | 0.765 | +0.061 | +0.021 | $8.19 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mikko Rantanen: 1+ goals NO | 70 | 0.735 | 0.725 | +0.021 | +0.011 | $4.12 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (14.30 vs 12.38 bp); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.144); KXNHLGOAL-26OCT31CBJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (14.30 vs 12.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.116); KXNHLGOAL-26OCT31CBJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT31CBJDAL-DAL2|no; why: higher confidence-adjusted growth (5.27 vs 4.15 bp); despite a smaller raw edge (+0.061 vs +0.064/contract); wins across more scripts (relative breadth 0.993 vs 0.884); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.144); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.116); KXNHLGOAL-26OCT31CBJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.144); failure: DAL wins by 2+
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31CBJDAL-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31CBJDAL-DAL3|no has the higher standalone adjusted growth (5.27 vs 1.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.144); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.144); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3168): highest fidelity KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4546): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL3|no (same contract)
- thesis DAL:SUPPRESSED (p 0.3994): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL3|no (same contract)
- KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.465, phi -0.262)
- KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.465, phi -0.25)
- KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3096, phi -0.734)
- KXNHLGOAL-26OCT31CBJDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.378, phi -0.208)

portfolios: A EV +2.47 (adj +1.07) on $16.71, P(profit) 0.4469, adj growth 9.7 bp · B EV +3.28 (adj +1.84) on $21.35, P(profit) 0.3938, adj growth 16.9 bp · C EV +2.84 (adj +1.52) on $21.32, P(profit) 0.2609, adj growth 13.7 bp · R EV +0.31 (adj +0.12) on $5.00, P(profit) 0.6173, adj growth 4.3 bp

## CGY @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 1 on card


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
| Colorado wins by over 1.5 goals NO | 40 | 0.521 | 0.439 | +0.104 | +0.022 | $5.38 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL3|no; why: Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no because adjusted EV is 1.2 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: only recommended bet in this game; failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:TIGHT (p 0.3825): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.2704): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS_BY_2PLUS (p 0.1381): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no (same contract)
- KXNHLSPREAD-26OCT31CGYCOL-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.6 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4794, phi -1.0)
- override: Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no because adjusted EV is 1.2 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.10 (adj +0.60) on $16.71, P(profit) 0.6128, adj growth 5.2 bp · B EV +1.34 (adj +0.29) on $5.38, P(profit) 0.5206, adj growth 2.6 bp · C EV +1.76 (adj +0.37) on $7.05, P(profit) 0.5206, adj growth 3.4 bp · R EV +0.50 (adj +0.11) on $2.00, P(profit) 0.5206, adj growth 3.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
