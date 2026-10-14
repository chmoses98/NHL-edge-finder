# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-14T15:24:06Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +10.41 | +3.42 | +9.58 | 0.616 | -36.27 | -44.86 | 28.34 |
| B thesis-diversified (joint) ← optimiser card | 66.36 | +8.81 | +3.88 | +4.09 | 0.593 | -26.38 | -43.31 | 33.70 |
| C best expression per thesis | 51.75 | +5.66 | +2.22 | -0.65 | 0.465 | -20.13 | -32.27 | 19.36 |
| R FUNDED research stakes | 6.00 | +0.87 | +0.48 | -0.96 | 0.390 | -6.00 | -6.00 | 0.00 |

## MTL @ WSH  ·  10000 joint draws  ·  426 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_MTL_win | p_overtime | goals | shots WSH/MTL | WSH/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.56 | 0.44 | 0.00 | 6.0 | 27.4/27.3 | 24.0/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.44 | 5.9 | 27.3/27.2 | 24.0/24.1 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 5.99 | 32.2/21.4 | 18.4/28.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.55 | 0.45 | 0.00 | 9.33 | 29.1/28.6 | 22.8/22.5 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.51 | 0.49 | 0.45 | 5.83 | 32.8/21.7 | 18.6/29.4 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.058 | 0.62 | 0.38 | 0.00 | 9.28 | 34.4/23.2 | 18.3/27.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Leonard: 1+ assists YES | 31 | 0.399 | 0.350 | +0.074 | +0.025 | $9.80 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
| Ethen Frank: 1+ goals YES | 12 | 0.144 | 0.140 | +0.016 | +0.013 | $3.88 | FUNDED_RESEARCH | $1 | WSH:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Jordan Kyrou: 1+ assists NO | 70 | 0.769 | 0.727 | +0.054 | +0.012 | $12.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Full Game: Over 5.5 goals scored NO | 38 | 0.441 | 0.408 | +0.044 | +0.011 | $6.94 | FUNDED_RESEARCH | $2 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes; why: higher confidence-adjusted growth (6.00 vs 0.18 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT14MTLWSH-WSHEFRANK53-1|yes: MOSTLY_INDEPENDENT (phi 0.034); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLTOTAL-26OCT14MTLWSH-6|no: INTENTIONAL_DIVERSIFIER (phi -0.203); failure: WSH offense suppressed (<= 2 goals)
- **Ethen Frank: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes has the higher standalone adjusted growth (6.00 vs 3.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.034); they share one thesis budget; relationships: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.034); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.048); KXNHLTOTAL-26OCT14MTLWSH-6|no: INTENTIONAL_DIVERSIFIER (phi -0.114); failure: WSH offense suppressed (<= 2 goals)
- **Jordan Kyrou: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-6|no; why: higher confidence-adjusted growth (1.59 vs 1.21 bp); wins across more scripts (relative breadth 1.008 vs 0.777); relationships: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26OCT14MTLWSH-WSHEFRANK53-1|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLTOTAL-26OCT14MTLWSH-6|no: REINFORCING (phi 0.153); failure: WSH offense succeeds (4+ goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-4|no; why: higher confidence-adjusted growth (1.21 vs 1.11 bp); wins across more scripts (relative breadth 0.777 vs 0.355); alternative not eligible: confidence-adjusted EV +0.0072 below the 0.010/contract floor; relationships: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.203); KXNHLGOAL-26OCT14MTLWSH-WSHEFRANK53-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.114); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: REINFORCING (phi 0.153); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4077): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes (same contract)
- thesis WSH:SUPPRESSED (p 0.3766): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no (same contract)
- thesis GAME:LOW_EVENT (p 0.2339): highest fidelity KXNHLTOTAL-26OCT14MTLWSH-6|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT14MTLWSH-6|no (same contract)
- KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3766, phi -0.29)
- KXNHLGOAL-26OCT14MTLWSH-WSHEFRANK53-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3766, phi -0.175)
- KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4077, phi -0.217)
- KXNHLTOTAL-26OCT14MTLWSH-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2602, phi -0.527)

portfolios: A EV +5.50 (adj +1.69) on $50.00, P(profit) 0.6198, adj growth 14.0 bp · B EV +4.42 (adj +1.54) on $32.71, P(profit) 0.6421, adj growth 13.4 bp · C EV +3.81 (adj +1.12) on $27.57, P(profit) 0.6666, adj growth 9.8 bp · R EV +0.35 (adj +0.16) on $3.00, P(profit) 0.5412, adj growth 5.4 bp

## DAL @ COL  ·  10000 joint draws  ·  390 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_DAL_win | p_overtime | goals | shots COL/DAL | COL/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.129 | 0.70 | 0.30 | 0.00 | 5.99 | 32.7/21.1 | 18.6/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.64 | 0.36 | 0.00 | 6.0 | 27.1/26.7 | 23.9/23.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.55 | 0.45 | 0.49 | 5.9 | 32.9/21.2 | 18.1/29.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.53 | 0.47 | 0.48 | 5.9 | 27.5/26.9 | 23.5/24.2 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.077 | 0.70 | 0.30 | 0.00 | 9.25 | 34.6/22.6 | 18.1/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.63 | 0.37 | 0.00 | 9.26 | 28.9/28.3 | 23.0/22.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Artturi Lehkonen: 1+ goals YES | 23 | 0.285 | 0.269 | +0.042 | +0.026 | $8.22 | FUNDED_RESEARCH | $3 | COL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Nicolas Roy: 1+ goals YES | 10 | 0.134 | 0.124 | +0.027 | +0.018 | $4.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Fedor Svechkov: 1+ goals YES | 10 | 0.126 | 0.118 | +0.020 | +0.012 | $3.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| T.J. Hughes: 1+ assists NO | 73 | 0.790 | 0.755 | +0.046 | +0.011 | $17.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (8.02 vs 2.21 bp); relationships: KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT14DALCOL-COLTHUGHES13-1|no: MOSTLY_INDEPENDENT (phi -0.024); failure: COL offense suppressed (<= 2 goals)
- **Nicolas Roy: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (8.02 vs 7.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT14DALCOL-COLTHUGHES13-1|no: INTENTIONAL_DIVERSIFIER (phi -0.052); failure: COL offense suppressed (<= 2 goals)
- **Fedor Svechkov: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (8.02 vs 3.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT14DALCOL-COLTHUGHES13-1|no: INTENTIONAL_DIVERSIFIER (phi -0.166); failure: COL offense suppressed (<= 2 goals)
- **T.J. Hughes: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (1.48 vs 0.14 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0040 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.166); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4441): highest fidelity KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes (same contract)
- thesis DAL:SUPPRESSED (p 0.4873): highest fidelity KXNHLGOAL-26OCT14DALCOL-DALJHRYCKOWIAN49-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.3357): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.203)
- KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.163)
- KXNHLGOAL-26OCT14DALCOL-COLFSVECHKOV9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.149)
- KXNHLAST-26OCT14DALCOL-COLTHUGHES13-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4441, phi -0.198)

portfolios: A EV +4.91 (adj +1.73) on $50.00, P(profit) 0.5467, adj growth 14.4 bp · B EV +4.39 (adj +2.34) on $33.65, P(profit) 0.4559, adj growth 20.3 bp · C EV +1.85 (adj +1.10) on $24.18, P(profit) 0.2846, adj growth 9.6 bp · R EV +0.52 (adj +0.32) on $3.00, P(profit) 0.2846, adj growth 10.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
