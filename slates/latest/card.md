# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-14T21:46:05Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +9.81 | +2.46 | +12.30 | 0.675 | -31.81 | -36.15 | 20.55 |
| B thesis-diversified (joint) ← optimiser card | 88.63 | +8.55 | +3.78 | +5.85 | 0.556 | -25.53 | -41.29 | 33.32 |
| C best expression per thesis | 37.14 | +4.20 | +1.87 | +8.95 | 0.549 | -14.36 | -14.36 | 16.54 |
| R FUNDED research stakes | 9.00 | +0.76 | +0.39 | +2.41 | 0.533 | -3.82 | -9.00 | 0.00 |

## MTL @ WSH  ·  10000 joint draws  ·  512 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.521 / away 0.479

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
| Aliaksei Protas: 1+ goals YES | 19 | 0.235 | 0.223 | +0.034 | +0.022 | $7.27 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 32 | 0.398 | 0.354 | +0.063 | +0.019 | $8.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
| Jordan Kyrou: 1+ assists NO | 70 | 0.765 | 0.730 | +0.050 | +0.015 | $16.57 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Full Game: Over 5.5 goals scored NO | 37 | 0.430 | 0.398 | +0.044 | +0.011 | $6.69 | FUNDED_RESEARCH | $2 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-2|yes; why: higher confidence-adjusted growth (6.37 vs 5.33 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.925 vs 0.738); relationships: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.041); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.093); KXNHLTOTAL-26OCT14MTLWSH-6|no: INTENTIONAL_DIVERSIFIER (phi -0.14); failure: WSH offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes; why: Player prop expression KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes selected over player prop KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-2|yes because adjusted EV is 0.6 pts higher while thesis capture is 0.56 vs 0.18 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.041); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.097); KXNHLTOTAL-26OCT14MTLWSH-6|no: INTENTIONAL_DIVERSIFIER (phi -0.207); failure: WSH offense suppressed (<= 2 goals)
- **Jordan Kyrou: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-5|no; why: KXNHLTOTAL-26OCT14MTLWSH-5|no has the higher standalone adjusted growth (2.87 vs 2.54 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.132); relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.093); KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.097); KXNHLTOTAL-26OCT14MTLWSH-6|no: MOSTLY_INDEPENDENT (phi 0.147); failure: WSH offense succeeds (4+ goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-5|no; why: Broad expression KXNHLTOTAL-26OCT14MTLWSH-6|no selected over broad KXNHLTOTAL-26OCT14MTLWSH-5|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.14); KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.207); KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi 0.147); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4057): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes — Player prop expression KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes selected over player prop KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-2|yes because adjusted EV is 0.6 pts higher while thesis capture is 0.56 vs 0.18 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:LOW_EVENT (p 0.2337): highest fidelity KXNHLTOTAL-26OCT14MTLWSH-6|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT14MTLWSH-5|no — Broad expression KXNHLTOTAL-26OCT14MTLWSH-6|no selected over broad KXNHLTOTAL-26OCT14MTLWSH-5|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis WSH:SUPPRESSED (p 0.3754): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHATUCH89-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3754, phi -0.215)
- KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3754, phi -0.279)
- KXNHLAST-26OCT14MTLWSH-WSHJKYROU25-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4057, phi -0.22)
- KXNHLTOTAL-26OCT14MTLWSH-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2693, phi -0.528)
- override: Broad expression KXNHLTOTAL-26OCT14MTLWSH-6|no selected over broad KXNHLTOTAL-26OCT14MTLWSH-5|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Player prop expression KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes selected over player prop KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-2|yes because adjusted EV is 0.6 pts higher while thesis capture is 0.56 vs 0.18 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +6.21 (adj +1.52) on $50.00, P(profit) 0.5972, adj growth 12.1 bp · B EV +4.68 (adj +1.79) on $38.63, P(profit) 0.6686, adj growth 15.6 bp · C EV +2.24 (adj +1.10) on $11.25, P(profit) 0.4155, adj growth 9.6 bp · R EV +0.57 (adj +0.27) on $4.00, P(profit) 0.5935, adj growth 9.3 bp

## DAL @ COL  ·  10000 joint draws  ·  476 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.554 / away 0.446

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
| Nicolas Roy: 1+ goals YES | 10 | 0.134 | 0.124 | +0.027 | +0.018 | $4.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| T.J. Hughes: 1+ goals NO | 79 | 0.833 | 0.821 | +0.031 | +0.019 | $19.84 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Jason Robertson: 2+ assists NO | 87 | 0.931 | 0.893 | +0.053 | +0.015 | $19.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Artturi Lehkonen: 1+ goals YES | 24 | 0.285 | 0.271 | +0.032 | +0.018 | $5.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Nicolas Roy: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (7.11 vs 3.81 bp); despite a smaller raw edge (+0.027 vs +0.032/contract); relationships: KXNHLGOAL-26OCT14DALCOL-COLTHUGHES13-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: COL offense suppressed (<= 2 goals)
- **T.J. Hughes: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLMNECAS88-1|no; why: higher confidence-adjusted growth (5.10 vs 0.01 bp); alternative not eligible: confidence-adjusted EV +0.0011 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: COL offense succeeds (4+ goals)
- **Jason Robertson: 2+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT14DALCOL-DALMHEISKANEN4-2|no; why: higher confidence-adjusted growth (4.77 vs 4.05 bp); relationships: KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT14DALCOL-COLTHUGHES13-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: DAL offense succeeds (4+ goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT14DALCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (3.81 vs 0.57 bp); despite a smaller raw edge (+0.032 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT14DALCOL-COLTHUGHES13-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no: MOSTLY_INDEPENDENT (phi -0.004); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis DAL:SUPPRESSED (p 0.4873): highest fidelity KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT14DALCOL-DALTSEGUIN91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:OFFENSE_4PLUS (p 0.4441): highest fidelity KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.3357): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT14DALCOL-COLNROY10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.163)
- KXNHLGOAL-26OCT14DALCOL-COLTHUGHES13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4441, phi -0.164)
- KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3011, phi -0.241)
- KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.203)

portfolios: A EV +3.59 (adj +0.94) on $50.00, P(profit) 0.5517, adj growth 8.5 bp · B EV +3.87 (adj +1.99) on $50.00, P(profit) 0.3219, adj growth 17.7 bp · C EV +1.96 (adj +0.77) on $25.89, P(profit) 0.2646, adj growth 7.0 bp · R EV +0.19 (adj +0.12) on $5.00, P(profit) 0.8327, adj growth 4.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
