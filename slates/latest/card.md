# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-14T22:34:04Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +10.61 | +2.19 | +9.87 | 0.648 | -29.42 | -45.76 | 17.21 |
| B thesis-diversified (joint) ← optimiser card | 88.28 | +7.41 | +3.52 | +5.64 | 0.575 | -26.45 | -37.40 | 31.16 |
| C best expression per thesis | 37.57 | +4.25 | +1.93 | +10.20 | 0.549 | -14.78 | -14.78 | 17.07 |
| R FUNDED research stakes | 9.00 | +0.92 | +0.50 | -2.69 | 0.461 | -9.00 | -9.00 | 0.00 |

## MTL @ WSH  ·  10000 joint draws  ·  512 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_MTL_win | p_overtime | goals | shots WSH/MTL | WSH/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.52 | 0.48 | 0.00 | 6.03 | 27.3/27.0 | 23.5/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.49 | 0.51 | 0.46 | 5.91 | 27.4/27.2 | 24.0/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.53 | 0.47 | 0.00 | 9.25 | 28.9/28.8 | 22.6/22.8 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.090 | 0.60 | 0.40 | 0.00 | 6.02 | 32.5/21.8 | 18.8/28.2 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.54 | 0.46 | 0.45 | 5.93 | 32.3/21.7 | 18.5/28.9 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.059 | 0.62 | 0.38 | 0.00 | 9.2 | 34.4/23.2 | 18.2/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 19 | 0.235 | 0.223 | +0.034 | +0.022 | $7.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Jakob Chychrun: 1+ goals NO | 78 | 0.820 | 0.809 | +0.028 | +0.017 | $16.83 | FUNDED_RESEARCH | $5 | WSH:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Jordan Kyrou: 1+ assists NO | 70 | 0.765 | 0.730 | +0.050 | +0.015 | $13.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Full Game: Over 5.5 goals scored NO | 37 | 0.430 | 0.398 | +0.044 | +0.011 | $4.19 | FUNDED_RESEARCH | $2 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (6.37 vs 1.15 bp); despite a smaller raw edge (+0.034 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT14MTLWSH-WSHJCHYCHRUN6-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.093); KXNHLTOTAL-26OCT14MTLWSH-6|no: INTENTIONAL_DIVERSIFIER (phi -0.14); failure: WSH offense suppressed (<= 2 goals)
- **Jakob Chychrun: 1+ goals NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-5|no; why: higher confidence-adjusted growth (3.88 vs 2.87 bp); despite a smaller raw edge (+0.028 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.009 vs 0.382); relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi 0.052); KXNHLTOTAL-26OCT14MTLWSH-6|no: MOSTLY_INDEPENDENT (phi 0.127); failure: WSH offense succeeds (4+ goals)
- **Jordan Kyrou: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-5|no; why: KXNHLTOTAL-26OCT14MTLWSH-5|no has the higher standalone adjusted growth (2.87 vs 2.54 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.132); relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.093); KXNHLGOAL-26OCT14MTLWSH-WSHJCHYCHRUN6-1|no: MOSTLY_INDEPENDENT (phi 0.052); KXNHLTOTAL-26OCT14MTLWSH-6|no: MOSTLY_INDEPENDENT (phi 0.147); failure: WSH offense succeeds (4+ goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-5|no; why: Broad expression KXNHLTOTAL-26OCT14MTLWSH-6|no selected over broad KXNHLTOTAL-26OCT14MTLWSH-5|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.14); KXNHLGOAL-26OCT14MTLWSH-WSHJCHYCHRUN6-1|no: MOSTLY_INDEPENDENT (phi 0.127); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi 0.147); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4057): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:SUPPRESSED (p 0.3754): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHATUCH89-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:LOW_EVENT (p 0.2337): highest fidelity KXNHLTOTAL-26OCT14MTLWSH-6|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT14MTLWSH-5|no — Broad expression KXNHLTOTAL-26OCT14MTLWSH-6|no selected over broad KXNHLTOTAL-26OCT14MTLWSH-5|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3754, phi -0.215)
- KXNHLGOAL-26OCT14MTLWSH-WSHJCHYCHRUN6-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4057, phi -0.193)
- KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4057, phi -0.22)
- KXNHLTOTAL-26OCT14MTLWSH-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2693, phi -0.528)
- override: Broad expression KXNHLTOTAL-26OCT14MTLWSH-6|no selected over broad KXNHLTOTAL-26OCT14MTLWSH-5|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.76 (adj +1.21) on $50.00, P(profit) 0.5972, adj growth 9.0 bp · B EV +3.22 (adj +1.54) on $41.33, P(profit) 0.4906, adj growth 13.5 bp · C EV +2.24 (adj +1.10) on $11.25, P(profit) 0.4155, adj growth 9.6 bp · R EV +0.41 (adj +0.17) on $7.00, P(profit) 0.3771, adj growth 5.5 bp

## DAL @ COL  ·  10000 joint draws  ·  480 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.563 / away 0.437

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
| Nathan MacKinnon: 3+ assists NO | 92 | 0.970 | 0.942 | +0.044 | +0.017 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nicolas Roy: 1+ goals YES | 10 | 0.134 | 0.124 | +0.027 | +0.018 | $4.55 | FUNDED_RESEARCH | $2 | COL:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 24 | 0.285 | 0.272 | +0.032 | +0.019 | $6.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Tyler Seguin: 1+ assists NO | 71 | 0.780 | 0.740 | +0.056 | +0.016 | $15.78 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 3+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLNMACKINNON29-2|no; why: higher confidence-adjusted growth (9.48 vs 0.95 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.124); KXNHLAST-26OCT14DALCOL-DALTSEGUIN91-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: COL offense succeeds (4+ goals)
- **Nicolas Roy: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (7.11 vs 4.35 bp); despite a smaller raw edge (+0.027 vs +0.032/contract); relationships: KXNHLAST-26OCT14DALCOL-COLNMACKINNON29-3|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT14DALCOL-DALTSEGUIN91-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: COL offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT14DALCOL-COLDTOEWS7-1|yes; why: higher confidence-adjusted growth (4.35 vs 1.00 bp); despite a smaller raw edge (+0.032 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT14DALCOL-COLNMACKINNON29-3|no: INTENTIONAL_DIVERSIFIER (phi -0.124); KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT14DALCOL-DALTSEGUIN91-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: COL offense suppressed (<= 2 goals)
- **Tyler Seguin: 1+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no; why: KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no has the higher standalone adjusted growth (4.77 vs 2.71 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.037); relationships: KXNHLAST-26OCT14DALCOL-COLNMACKINNON29-3|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: DAL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis DAL:SUPPRESSED (p 0.4873): highest fidelity KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT14DALCOL-DALTSEGUIN91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:OFFENSE_4PLUS (p 0.4441): highest fidelity KXNHLAST-26OCT14DALCOL-COLDTOEWS7-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.3357): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT14DALCOL-COLNMACKINNON29-3|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4441, phi -0.166)
- KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.163)
- KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.203)
- KXNHLAST-26OCT14DALCOL-DALTSEGUIN91-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3011, phi -0.23)

portfolios: A EV +4.85 (adj +0.98) on $50.00, P(profit) 0.7465, adj growth 8.2 bp · B EV +4.18 (adj +1.98) on $46.95, P(profit) 0.3764, adj growth 17.6 bp · C EV +2.01 (adj +0.83) on $26.32, P(profit) 0.2646, adj growth 7.5 bp · R EV +0.52 (adj +0.33) on $2.00, P(profit) 0.1337, adj growth 10.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
