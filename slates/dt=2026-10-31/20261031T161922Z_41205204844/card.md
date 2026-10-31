# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T16:19:22Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.64 | +9.46 | +24.88 | 0.735 | -24.46 | -37.55 | 86.32 |
| B thesis-diversified (joint) ← optimiser card | 149.29 | +28.34 | +14.71 | +25.90 | 0.727 | -26.57 | -40.13 | 137.28 |
| C best expression per thesis | 149.99 | +29.06 | +13.53 | +26.41 | 0.692 | -37.80 | -53.86 | 121.37 |
| R FUNDED research stakes | 21.00 | +2.50 | +1.43 | +1.40 | 0.571 | -6.91 | -9.04 | 0.00 |

## CHI @ BOS  ·  10000 joint draws  ·  452 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.659 / away 0.341

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_CHI_win | p_overtime | goals | shots BOS/CHI | BOS/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.74 | 0.26 | 0.00 | 6.05 | 27.2/26.8 | 24.3/22.6 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.119 | 0.78 | 0.22 | 0.00 | 6.04 | 32.1/21.1 | 18.9/26.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.53 | 0.47 | 0.47 | 5.93 | 27.4/27.0 | 23.8/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.73 | 0.27 | 0.00 | 9.39 | 28.8/28.3 | 23.7/20.9 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.092 | 0.81 | 0.19 | 0.00 | 9.33 | 34.0/22.5 | 18.5/25.4 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.58 | 0.42 | 0.46 | 5.95 | 32.4/21.4 | 18.1/28.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 20 | 0.269 | 0.251 | +0.058 | +0.040 | $6.13 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Hampus Lindholm: 1+ assists YES | 25 | 0.339 | 0.289 | +0.075 | +0.026 | $3.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
| Ryan Donato: 1+ goals YES | 13 | 0.169 | 0.155 | +0.031 | +0.017 | $2.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ assists NO | 57 | 0.652 | 0.606 | +0.064 | +0.019 | $8.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31CHIBOS-8|yes; why: higher confidence-adjusted growth (20.19 vs 0.03 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.909 vs 0.332); alternative not eligible: confidence-adjusted EV +0.0018 below the 0.010/contract floor; relationships: KXNHLAST-26OCT31CHIBOS-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CHIBOS-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.138); failure: CHI offense suppressed (<= 2 goals)
- **Hampus Lindholm: 1+ assists YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CHIBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (7.64 vs 0.82 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CHIBOS-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: BOS offense suppressed (<= 2 goals)
- **Ryan Donato: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (20.19 vs 5.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT31CHIBOS-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.049); failure: CHI offense suppressed (<= 2 goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31CHIBOS-CHIPKANE88-1|no; why: higher confidence-adjusted growth (3.14 vs 1.62 bp); despite a smaller raw edge (+0.064 vs +0.087/contract); relationships: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.138); KXNHLAST-26OCT31CHIBOS-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT31CHIBOS-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi -0.049); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, BOS shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.2917): highest fidelity KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.5355): highest fidelity KXNHLAST-26OCT31CHIBOS-BOSHLINDHOLM27-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT31CHIBOS-BOSHLINDHOLM27-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4913): highest fidelity KXNHLAST-26OCT31CHIBOS-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4913, phi -0.267)
- KXNHLAST-26OCT31CHIBOS-BOSHLINDHOLM27-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.2638, phi -0.233)
- KXNHLGOAL-26OCT31CHIBOS-CHIRDONATO8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4913, phi -0.21)
- KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2917, phi -0.284)

portfolios: A EV +3.16 (adj +1.30) on $15.73, P(profit) 0.492, adj growth 12.4 bp · B EV +4.22 (adj +2.09) on $20.48, P(profit) 0.5072, adj growth 19.5 bp · C EV +6.75 (adj +3.13) on $35.11, P(profit) 0.6435, adj growth 28.1 bp · R EV +0.55 (adj +0.37) on $2.00, P(profit) 0.2693, adj growth 13.6 bp

## STL @ DET  ·  10000 joint draws  ·  420 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

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
| Jimmy Snuggerud: 1+ goals YES | 26 | 0.325 | 0.306 | +0.051 | +0.032 | $4.99 | FUNDED_RESEARCH | $2 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| J.T. Compher: 1+ goals YES | 11 | 0.154 | 0.137 | +0.037 | +0.020 | $2.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Lucas Raymond: 1+ assists NO | 58 | 0.657 | 0.616 | +0.060 | +0.019 | $6.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Dylan Holloway: 1+ assists YES | 31 | 0.385 | 0.340 | +0.060 | +0.015 | $1.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes; why: higher confidence-adjusted growth (11.46 vs 2.20 bp); despite a smaller raw edge (+0.051 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31STLDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes: REINFORCING (phi 0.236); failure: STL offense suppressed (<= 2 goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (8.50 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0024 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: DET offense suppressed (<= 2 goals)
- **Lucas Raymond: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT31STLDET-DETMSEIDER53-1|no; why: higher confidence-adjusted growth (3.36 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31STLDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.034); KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: DET offense succeeds (4+ goals)
- **Dylan Holloway: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes has the higher standalone adjusted growth (11.46 vs 2.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.236); they share one thesis budget; relationships: KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: REINFORCING (phi 0.236); KXNHLGOAL-26OCT31STLDET-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.3777): highest fidelity KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4132): highest fidelity KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3659): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT31STLDET-STLJSNUGGERUD21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3999, phi -0.278)
- KXNHLGOAL-26OCT31STLDET-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4132, phi -0.18)
- KXNHLAST-26OCT31STLDET-DETLRAYMOND23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3659, phi -0.257)
- KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3999, phi -0.288)

portfolios: A EV +2.86 (adj +1.26) on $15.73, P(profit) 0.5048, adj growth 11.7 bp · B EV +2.60 (adj +1.29) on $14.89, P(profit) 0.4331, adj growth 12.1 bp · C EV +2.50 (adj +1.28) on $17.68, P(profit) 0.3245, adj growth 11.5 bp · R EV +0.37 (adj +0.24) on $2.00, P(profit) 0.3245, adj growth 8.5 bp

## TBL @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 6 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.394 / away 0.606

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
| Ryan O'Reilly: 1+ goals YES | 25 | 0.313 | 0.296 | +0.050 | +0.033 | $4.90 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 74 | 0.809 | 0.772 | +0.056 | +0.019 | $5.97 | FUNDED_RESEARCH | $2 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ assists NO | 38 | 0.534 | 0.415 | +0.138 | +0.018 | $2.71 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.74) | CALIBRATION_WARNING | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31TBNSH-TB3|no; why: higher confidence-adjusted growth (12.24 vs 4.09 bp); despite a smaller raw edge (+0.050 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLAST-26OCT31TBNSH-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: NSH offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLAST-26OCT31TBNSH-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (4.09 vs 3.06 bp); despite a smaller raw edge (+0.056 vs +0.138/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.147); KXNHLAST-26OCT31TBNSH-TBNKUCHEROV86-1|no: REINFORCING (phi 0.187); failure: TBL wins by 2+
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TBNSH-TB3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31TBNSH-TB3|no has the higher standalone adjusted growth (4.09 vs 3.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.187); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLSPREAD-26OCT31TBNSH-TB3|no: REINFORCING (phi 0.187); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NSH:OFFENSE_4PLUS (p 0.3613): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS (p 0.4644): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB3|no (same contract)
- thesis TBL:SUPPRESSED (p 0.3734): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB3|no (same contract)
- KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4167, phi -0.281)
- KXNHLSPREAD-26OCT31TBNSH-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3117, phi -0.722)
- KXNHLAST-26OCT31TBNSH-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 26% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.9 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4098, phi -0.302)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT31TBNSH-NSH2|yes less than the minimum stake; KXNHLAST-26OCT31TBNSH-TBNKUCHEROV86-1|no kept

portfolios: A EV +2.36 (adj +0.47) on $15.73, P(profit) 0.6198, adj growth 4.2 bp · B EV +2.31 (adj +0.89) on $13.57, P(profit) 0.622, adj growth 8.3 bp · C EV +2.45 (adj +1.30) on $20.72, P(profit) 0.3133, adj growth 11.7 bp · R EV +0.15 (adj +0.05) on $2.00, P(profit) 0.8091, adj growth 1.9 bp

## EDM @ NYI  ·  10000 joint draws  ·  422 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.490 / away 0.510

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
| Mattias Ekholm: 1+ goals YES | 7 | 0.123 | 0.105 | +0.049 | +0.030 | $3.37 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 13 | 0.178 | 0.165 | +0.041 | +0.027 | $3.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Jason Dickinson: 1+ goals YES | 9 | 0.120 | 0.109 | +0.025 | +0.013 | $1.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 34 | 0.449 | 0.375 | +0.093 | +0.019 | $4.58 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.68) | EVIDENCE_MIXED | D |
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: higher confidence-adjusted growth (27.97 vs 2.55 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.822 vs 0.368); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT31EDMNYI-EDMJDICKINSON16-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.121); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: higher confidence-adjusted growth (13.36 vs 2.55 bp); despite a smaller raw edge (+0.041 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.863 vs 0.368); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT31EDMNYI-EDMJDICKINSON16-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.03); failure: EDM offense suppressed (<= 2 goals)
- **Jason Dickinson: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: higher confidence-adjusted growth (4.32 vs 2.55 bp); despite a smaller raw edge (+0.024 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.877 vs 0.368); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31EDMNYI-EDMRNUGENTHOPKINS93-1|no; why: higher confidence-adjusted growth (3.53 vs 3.23 bp); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.121); KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26OCT31EDMNYI-EDMJDICKINSON16-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.4191): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3425): highest fidelity KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.4481): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3425, phi -0.156)
- KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3425, phi -0.167)
- KXNHLGOAL-26OCT31EDMNYI-EDMJDICKINSON16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3425, phi -0.168)
- KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 32% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.4 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4481, phi -0.309)

portfolios: A EV +2.30 (adj +0.52) on $15.73, P(profit) 0.5818, adj growth 5.0 bp · B EV +4.85 (adj +2.53) on $13.08, P(profit) 0.3646, adj growth 23.5 bp · C EV +2.97 (adj +0.92) on $14.06, P(profit) 0.7117, adj growth 8.2 bp · R EV +0.65 (adj +0.41) on $1.00, P(profit) 0.1232, adj growth 14.8 bp

## BUF @ LAK  ·  10000 joint draws  ·  458 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.457 / away 0.543

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BUF_win | p_overtime | goals | shots LAK/BUF | LAK/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 6.02 | 27.9/27.9 | 24.7/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.48 | 5.9 | 28.1/28.2 | 24.8/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.57 | 0.43 | 0.00 | 9.19 | 29.2/29.3 | 23.8/22.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.072 | 0.65 | 0.35 | 0.00 | 6.03 | 32.7/22.2 | 19.5/28.1 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.066 | 0.51 | 0.49 | 0.00 | 5.99 | 22.4/32.9 | 29.4/19.1 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.51 | 0.49 | 0.42 | 5.95 | 32.9/22.4 | 19.1/29.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.080 | 0.067 | +0.027 | +0.014 | $1.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Andre Lee: 1+ goals YES | 9 | 0.125 | 0.110 | +0.029 | +0.014 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 1.5 goals NO | 69 | 0.765 | 0.725 | +0.060 | +0.020 | $6.86 | FUNDED_RESEARCH | $2 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Rasmus Dahlin: 1+ goals NO | 81 | 0.844 | 0.833 | +0.024 | +0.013 | $7.06 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLSPREAD-26OCT31BUFLA-BUF2|no; why: higher confidence-adjusted growth (8.37 vs 4.15 bp); despite a smaller raw edge (+0.027 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT31BUFLA-BUF2|no: MOSTLY_INDEPENDENT (phi 0.061); KXNHLGOAL-26OCT31BUFLA-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: LAK offense suppressed (<= 2 goals)
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF2|no; why: higher confidence-adjusted growth (4.91 vs 4.15 bp); despite a smaller raw edge (+0.029 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT31BUFLA-BUF2|no: MOSTLY_INDEPENDENT (phi 0.09); KXNHLGOAL-26OCT31BUFLA-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.032); failure: LAK offense suppressed (<= 2 goals)
- **Buffalo wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: higher confidence-adjusted growth (4.15 vs 3.57 bp); relationships: KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.061); KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.09); KXNHLGOAL-26OCT31BUFLA-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.134); failure: BUF wins by 2+
- **Rasmus Dahlin: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31BUFLA-BUF2|no has the higher standalone adjusted growth (4.15 vs 2.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.134); they share one thesis budget; relationships: KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLSPREAD-26OCT31BUFLA-BUF2|no: MOSTLY_INDEPENDENT (phi 0.134); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:WINS_BY_2PLUS (p 0.3205): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.4171): highest fidelity KXNHLTEAMTOTAL-26OCT31BUFLA-LA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS (p 0.5446): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no (same contract)
- KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3693, phi -0.122)
- KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3693, phi -0.15)
- KXNHLSPREAD-26OCT31BUFLA-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2354, phi -1.0)
- KXNHLGOAL-26OCT31BUFLA-BUFRDAHLIN26-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3397, phi -0.195)

portfolios: A EV +1.71 (adj +0.53) on $15.73, P(profit) 0.4744, adj growth 4.5 bp · B EV +1.95 (adj +0.90) on $16.86, P(profit) 0.7088, adj growth 8.4 bp · C EV +1.22 (adj +0.40) on $14.37, P(profit) 0.7646, adj growth 3.7 bp · R EV +0.23 (adj +0.09) on $4.00, P(profit) 0.6662, adj growth 3.3 bp

## OTT @ SJS  ·  10000 joint draws  ·  444 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.433 / away 0.567

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
| Tyler Toffoli: 1+ assists YES | 24 | 0.325 | 0.275 | +0.072 | +0.022 | $3.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ goals NO | 79 | 0.824 | 0.814 | +0.022 | +0.013 | $8.58 | FUNDED_RESEARCH | $3 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Adam Gaudette: 1+ goals YES | 14 | 0.169 | 0.160 | +0.021 | +0.011 | $1.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Collin Graf: 1+ goals YES | 17 | 0.200 | 0.191 | +0.020 | +0.011 | $1.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes; why: higher confidence-adjusted growth (5.66 vs 2.10 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT31OTTSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.063); KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.056); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT31OTTSJ-SJMCELEBRINI71-2|no; why: higher confidence-adjusted growth (2.24 vs 0.14 bp); despite a smaller raw edge (+0.022 vs +0.080/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: SJS offense succeeds (4+ goals)
- **Adam Gaudette: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes has the higher standalone adjusted growth (5.66 vs 2.10 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.063); they share one thesis budget; relationships: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.063); KXNHLGOAL-26OCT31OTTSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: SJS offense suppressed (<= 2 goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes has the higher standalone adjusted growth (5.66 vs 1.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.056); they share one thesis budget; relationships: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26OCT31OTTSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4099): highest fidelity KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3765): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.254)
- KXNHLGOAL-26OCT31OTTSJ-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4099, phi -0.193)
- KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.201)
- KXNHLGOAL-26OCT31OTTSJ-SJCGRAF51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.201)

portfolios: A EV +2.35 (adj +0.88) on $15.73, P(profit) 0.5015, adj growth 7.9 bp · B EV +1.48 (adj +0.60) on $14.50, P(profit) 0.4603, adj growth 5.7 bp · C EV +1.48 (adj +0.46) on $5.19, P(profit) 0.3249, adj growth 4.1 bp · R EV +0.08 (adj +0.05) on $3.00, P(profit) 0.8241, adj growth 1.7 bp

## PIT @ MTL  ·  10000 joint draws  ·  498 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.531 / away 0.469

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
| Blake Lizotte: 1+ goals YES | 9 | 0.129 | 0.117 | +0.033 | +0.021 | $2.59 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Phillip Danault: 1+ goals YES | 12 | 0.165 | 0.148 | +0.037 | +0.021 | $2.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 13 | 0.162 | 0.151 | +0.024 | +0.013 | $1.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (10.99 vs 3.21 bp); relationships: KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PIT offense suppressed (<= 2 goals)
- **Phillip Danault: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT31PITMTL-MTLJANDERSON17-1|yes; why: higher confidence-adjusted growth (8.64 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: MTL offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (3.21 vs 0.10 bp); alternative not eligible: confidence-adjusted EV +0.0032 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis MTL:OFFENSE_4PLUS (p 0.4491): highest fidelity KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4097): highest fidelity KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes (same contract)
- KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.375, phi -0.186)
- KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3365, phi -0.192)
- KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.375, phi -0.196)

portfolios: A EV +2.37 (adj +1.41) on $8.43, P(profit) 0.3944, adj growth 12.9 bp · B EV +2.01 (adj +1.20) on $7.09, P(profit) 0.3944, adj growth 11.1 bp · C EV +1.75 (adj +0.99) on $7.18, P(profit) 0.3014, adj growth 8.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ VAN  ·  10000 joint draws  ·  418 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.369 / away 0.631

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
| Linus Karlsson: 1+ goals YES | 19 | 0.269 | 0.244 | +0.069 | +0.044 | $5.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 18 | 0.247 | 0.225 | +0.056 | +0.035 | $4.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 16 | 0.211 | 0.190 | +0.042 | +0.020 | $2.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 73 | 0.784 | 0.765 | +0.040 | +0.021 | $9.72 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (25.64 vs 16.81 bp); relationships: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (25.64 vs 16.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: VAN offense suppressed (<= 2 goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (25.64 vs 6.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VAN offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes; why: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes has the higher standalone adjusted growth (12.30 vs 5.33 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.119); relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4305): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLSPREAD-26OCT31TORVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3557): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-TOR5|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.239)
- KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.223)
- KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.212)
- KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4235, phi -0.203)

portfolios: A EV +4.03 (adj +1.70) on $15.73, P(profit) 0.4368, adj growth 15.8 bp · B EV +4.60 (adj +2.75) on $22.98, P(profit) 0.5372, adj growth 25.7 bp · C EV +4.78 (adj +2.62) on $13.62, P(profit) 0.4368, adj growth 23.4 bp · R EV +0.16 (adj +0.09) on $3.00, P(profit) 0.7837, adj growth 3.2 bp

## CBJ @ DAL  ·  10000 joint draws  ·  436 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.631 / away 0.369

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_CBJ_win | p_overtime | goals | shots DAL/CBJ | DAL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.55 | 0.45 | 0.00 | 6.03 | 26.0/25.8 | 22.5/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.53 | 0.47 | 0.46 | 5.87 | 26.3/25.9 | 22.7/23.0 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.089 | 0.63 | 0.37 | 0.00 | 5.99 | 31.0/20.6 | 17.8/26.8 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.55 | 0.45 | 0.47 | 5.9 | 31.3/20.8 | 17.8/28.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.56 | 0.44 | 0.00 | 9.25 | 27.7/27.5 | 21.8/21.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.52 | 0.48 | 0.00 | 3.48 | 25.0/24.8 | 23.0/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charlie Coyle: 1+ goals YES | 20 | 0.258 | 0.241 | +0.047 | +0.030 | $4.26 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.180 | 0.163 | +0.043 | +0.025 | $3.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ryan Lomberg: 1+ goals YES | 5 | 0.072 | 0.065 | +0.018 | +0.012 | $1.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Cole Sillinger: 1+ goals YES | 12 | 0.150 | 0.141 | +0.023 | +0.014 | $1.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (11.41 vs 11.26 bp); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT31CBJDAL-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (11.41 vs 11.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT31CBJDAL-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CBJ offense suppressed (<= 2 goals)
- **Ryan Lomberg: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (11.41 vs 5.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT31CBJDAL-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: CBJ offense suppressed (<= 2 goals)
- **Cole Sillinger: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (11.41 vs 3.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3192): highest fidelity KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.2429): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS (p 0.4582): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL2|no (same contract)
- KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4629, phi -0.248)
- KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4629, phi -0.223)
- KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4629, phi -0.14)
- KXNHLGOAL-26OCT31CBJDAL-CBJCSILLINGER4-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4629, phi -0.201)

portfolios: A EV +1.93 (adj +0.57) on $15.73, P(profit) 0.5047, adj growth 4.9 bp · B EV +2.66 (adj +1.63) on $10.42, P(profit) 0.5172, adj growth 15.2 bp · C EV +3.55 (adj +1.99) on $17.48, P(profit) 0.3916, adj growth 17.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CGY @ COL  ·  10000 joint draws  ·  452 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.777 / away 0.223

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
| Jonathan Castagna: 1+ goals YES | 8 | 0.110 | 0.100 | +0.025 | +0.015 | $1.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ goals NO | 76 | 0.805 | 0.791 | +0.032 | +0.018 | $8.95 | FUNDED_RESEARCH | $3 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Colorado over 3.5 goals scored NO | 34 | 0.421 | 0.376 | +0.066 | +0.020 | $2.91 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mikael Backlund: 1+ goals YES | 15 | 0.181 | 0.172 | +0.022 | +0.013 | $1.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT31CGYCOL-CGY|yes; why: higher confidence-adjusted growth (5.90 vs 5.69 bp); despite a smaller raw edge (+0.025 vs +0.078/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31CGYCOL-CGYMBACKLUND11-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CGY offense suppressed (<= 2 goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT31CGYCOL-CGY|yes; why: KXNHLGAME-26OCT31CGYCOL-CGY|yes has the higher standalone adjusted growth (5.69 vs 4.28 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.129); relationships: KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4|no: REINFORCING (phi 0.175); KXNHLGOAL-26OCT31CGYCOL-CGYMBACKLUND11-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: COL offense succeeds (4+ goals)
- **Colorado over 3.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT31CGYCOL-CGY|yes; why: KXNHLGAME-26OCT31CGYCOL-CGY|yes has the higher standalone adjusted growth (5.69 vs 3.77 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.538); relationships: KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: REINFORCING (phi 0.175); KXNHLGOAL-26OCT31CGYCOL-CGYMBACKLUND11-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: COL offense succeeds (4+ goals)
- **Mikael Backlund: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT31CGYCOL-CGY|yes; why: Player prop expression KXNHLGOAL-26OCT31CGYCOL-CGYMBACKLUND11-1|yes selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.31 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis CGY:OFFENSE_4PLUS (p 0.2704): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no — Player prop expression KXNHLGOAL-26OCT31CGYCOL-CGYMBACKLUND11-1|yes selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.31 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis CGY:WINS (p 0.2997): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no (same contract)
- thesis GAME:TIGHT (p 0.3825): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no (same contract)
- KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5114, phi -0.172)
- KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5691, phi -0.175)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5691, phi -0.98)
- KXNHLGOAL-26OCT31CGYCOL-CGYMBACKLUND11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5114, phi -0.229)
- override: Player prop expression KXNHLGOAL-26OCT31CGYCOL-CGYMBACKLUND11-1|yes selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.31 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.58 (adj +0.82) on $15.73, P(profit) 0.5206, adj growth 7.0 bp · B EV +1.66 (adj +0.83) on $15.42, P(profit) 0.5172, adj growth 7.7 bp · C EV +1.62 (adj +0.44) on $4.58, P(profit) 0.2997, adj growth 4.0 bp · R EV +0.31 (adj +0.13) on $4.00, P(profit) 0.3733, adj growth 4.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT31CGYCOL-COL|no == KXNHLGAME-26OCT31CGYCOL-CGY|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
