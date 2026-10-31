# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T23:25:42Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +17.30 | +5.01 | +6.43 | 0.560 | -52.75 | -70.01 | 32.79 |
| B thesis-diversified (joint) ← optimiser card | 96.12 | +17.41 | +10.27 | +11.90 | 0.532 | -41.62 | -46.45 | 89.31 |
| C best expression per thesis | 97.19 | +11.57 | +5.14 | +2.52 | 0.527 | -29.33 | -42.69 | 45.03 |
| R FUNDED research stakes | 10.00 | +2.67 | +1.52 | -0.88 | 0.346 | -7.60 | -10.00 | 0.00 |

## CBJ @ DAL  ·  10000 joint draws  ·  462 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.621 / away 0.379

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_CBJ_win | p_overtime | goals | shots DAL/CBJ | DAL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.56 | 0.44 | 0.00 | 5.97 | 26.1/25.9 | 22.7/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.47 | 5.89 | 26.2/25.9 | 22.7/23.1 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.085 | 0.57 | 0.43 | 0.00 | 5.98 | 31.3/20.7 | 17.6/27.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.58 | 0.42 | 0.46 | 5.86 | 30.9/20.5 | 17.3/27.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.57 | 0.43 | 0.00 | 9.23 | 27.9/27.8 | 21.9/21.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.54 | 0.46 | 0.00 | 3.44 | 25.0/24.8 | 23.0/22.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Damon Severson: 1+ goals YES | 6 | 0.107 | 0.094 | +0.043 | +0.030 | $6.88 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.187 | 0.171 | +0.049 | +0.034 | $8.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 19 | 0.254 | 0.236 | +0.053 | +0.036 | $10.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Valeri Nichushkin: 1+ assists NO | 71 | 0.787 | 0.746 | +0.062 | +0.021 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (30.80 vs 20.18 bp); despite a smaller raw edge (+0.043 vs +0.049/contract); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT31CBJDAL-CBJVNICHUSHKIN43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.09); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (20.18 vs 17.01 bp); despite a smaller raw edge (+0.049 vs +0.053/contract); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT31CBJDAL-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.031); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (20.18 vs 17.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT31CBJDAL-CBJVNICHUSHKIN43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.05); failure: CBJ offense suppressed (<= 2 goals)
- **Valeri Nichushkin: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT31CBJDAL-CBJVNICHUSHKIN43-1|no; why: higher confidence-adjusted growth (5.09 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.05); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3151): highest fidelity KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.249): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS (p 0.468): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL2|no (same contract)
- KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.155)
- KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.225)
- KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.241)
- KXNHLAST-26OCT31CBJDAL-CBJVNICHUSHKIN43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3151, phi -0.219)

portfolios: A EV +5.31 (adj +1.83) on $50.00, P(profit) 0.6933, adj growth 15.6 bp · B EV +12.28 (adj +7.85) on $46.49, P(profit) 0.4593, adj growth 67.4 bp · C EV +6.52 (adj +3.30) on $48.57, P(profit) 0.6818, adj growth 28.9 bp · R EV +1.33 (adj +0.93) on $2.00, P(profit) 0.1066, adj growth 30.2 bp

## CGY @ COL  ·  10000 joint draws  ·  454 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.772 / away 0.228

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_CGY_win | p_overtime | goals | shots COL/CGY | COL/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.156 | 0.81 | 0.19 | 0.00 | 6.02 | 35.6/22.7 | 20.6/30.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.119 | 0.83 | 0.17 | 0.00 | 9.37 | 37.8/24.3 | 20.4/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.78 | 0.22 | 0.00 | 6.04 | 29.7/28.9 | 26.5/24.7 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.60 | 0.40 | 0.47 | 5.95 | 36.6/23.2 | 20.2/33.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.74 | 0.26 | 0.00 | 9.38 | 31.3/30.4 | 25.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.56 | 0.44 | 0.51 | 5.99 | 30.0/29.1 | 25.8/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cale Makar: 1+ goals NO | 73 | 0.803 | 0.783 | +0.059 | +0.040 | $20.00 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Calgary over 3.5 goals scored YES | 20 | 0.283 | 0.239 | +0.072 | +0.028 | $6.85 | FUNDED_RESEARCH | $2 | CGY:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 1.5 goals NO | 40 | 0.523 | 0.440 | +0.107 | +0.023 | $2.78 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Gavin Brindley: 1+ goals NO | 87 | 0.900 | 0.891 | +0.022 | +0.013 | $20.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL2|no; why: higher confidence-adjusted growth (18.32 vs 4.82 bp); despite a smaller raw edge (+0.059 vs +0.107/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.022 vs 0.86); relationships: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLSPREAD-26OCT31CGYCOL-COL2|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT31CGYCOL-COLGBRINDLEY54-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: COL offense succeeds (4+ goals)
- **Calgary over 3.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes; why: higher confidence-adjusted growth (10.00 vs 5.33 bp); relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.025); KXNHLSPREAD-26OCT31CGYCOL-COL2|no: REINFORCING (phi 0.436); KXNHLGOAL-26OCT31CGYCOL-COLGBRINDLEY54-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: CGY offense suppressed (<= 2 goals)
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes; why: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes has the higher standalone adjusted growth (5.33 vs 4.82 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.421); relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: REINFORCING (phi 0.436); KXNHLGOAL-26OCT31CGYCOL-COLGBRINDLEY54-1|no: MOSTLY_INDEPENDENT (phi 0.094); failure: COL wins by 2+
- **Gavin Brindley: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26OCT31CGYCOL-COL2|no: MOSTLY_INDEPENDENT (phi 0.094); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.16, COL shot control · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CGY:OFFENSE_4PLUS (p 0.2746): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes (same contract)
- thesis CGY:WINS (p 0.3041): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.3862): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5689, phi -0.172)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:SUPPRESSED (p 0.5111, phi -0.642)
- KXNHLSPREAD-26OCT31CGYCOL-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.8 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4765, phi -1.0)
- KXNHLGOAL-26OCT31CGYCOL-COLGBRINDLEY54-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5689, phi -0.111)

portfolios: A EV +11.98 (adj +3.18) on $50.00, P(profit) 0.5874, adj growth 17.2 bp · B EV +5.12 (adj +2.42) on $49.63, P(profit) 0.7902, adj growth 21.9 bp · C EV +5.05 (adj +1.84) on $48.62, P(profit) 0.5339, adj growth 16.2 bp · R EV +1.33 (adj +0.59) on $8.00, P(profit) 0.5227, adj growth 20.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
