# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-09T11:41:01Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 84.77 | +11.81 | +4.44 | -7.19 | 0.469 | -33.77 | -57.88 | 34.99 |
| B thesis-diversified (joint) ← optimiser card | 65.01 | +7.76 | +2.86 | -1.40 | 0.450 | -20.27 | -28.29 | 24.94 |
| C best expression per thesis | 22.16 | +3.49 | +1.71 | -7.83 | 0.405 | -22.16 | -22.16 | 14.81 |
| R FUNDED research stakes | 7.00 | +0.82 | +0.49 | -1.89 | 0.248 | -7.00 | -7.00 | 0.00 |

## SEA @ DET  ·  10000 joint draws  ·  398 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_SEA_win | p_overtime | goals | shots DET/SEA | DET/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.54 | 0.46 | 0.00 | 6.01 | 27.7/27.3 | 23.9/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.46 | 5.91 | 28.0/27.4 | 24.2/24.7 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.105 | 0.57 | 0.43 | 0.00 | 5.98 | 33.1/21.6 | 18.6/29.1 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.54 | 0.46 | 0.47 | 5.92 | 33.4/21.9 | 18.7/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.51 | 0.49 | 0.00 | 9.37 | 29.5/29.2 | 23.1/23.3 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.065 | 0.59 | 0.41 | 0.00 | 9.17 | 34.9/23.3 | 18.0/28.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYR @ WSH  ·  10000 joint draws  ·  416 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_NYR_win | p_overtime | goals | shots WSH/NYR | WSH/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.55 | 0.45 | 0.00 | 6.04 | 26.7/26.4 | 23.0/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.91 | 26.7/26.5 | 23.1/23.5 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.092 | 0.62 | 0.38 | 0.00 | 5.96 | 31.5/20.9 | 18.0/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.56 | 0.44 | 0.00 | 9.31 | 28.1/28.0 | 22.5/21.6 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.55 | 0.46 | 0.44 | 5.91 | 31.9/21.3 | 18.1/28.4 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.063 | 0.62 | 0.38 | 0.00 | 9.28 | 33.3/22.2 | 17.3/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 19 | 0.248 | 0.230 | +0.047 | +0.029 | $9.43 | FUNDED_RESEARCH | $3 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Jordan Kyrou: 1+ assists NO | 73 | 0.837 | 0.755 | +0.094 | +0.011 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT09NYRWSH-7|yes; why: higher confidence-adjusted growth (11.30 vs 0.60 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.863 vs 0.679); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLAST-26OCT09NYRWSH-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.192); failure: WSH offense suppressed (<= 2 goals)
- **Jordan Kyrou: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no; why: higher confidence-adjusted growth (1.34 vs 0.45 bp); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.192); failure: WSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4179): highest fidelity KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes (same contract)
- thesis WSH:SUPPRESSED (p 0.373): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.373, phi -0.237)
- KXNHLAST-26OCT09NYRWSH-WSHJKYROU25-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.7 pts; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4179, phi -0.201)

portfolios: A EV +5.99 (adj +2.42) on $34.77, P(profit) 0.248, adj growth 19.4 bp · B EV +4.74 (adj +1.65) on $29.43, P(profit) 0.248, adj growth 14.4 bp · C EV +2.00 (adj +1.23) on $8.50, P(profit) 0.248, adj growth 10.6 bp · R EV +0.71 (adj +0.43) on $3.00, P(profit) 0.248, adj growth 14.0 bp

## PIT @ CBJ  ·  10000 joint draws  ·  420 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_PIT_win | p_overtime | goals | shots CBJ/PIT | CBJ/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.59 | 0.41 | 0.00 | 6.02 | 27.5/27.4 | 24.2/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.53 | 0.47 | 0.46 | 5.98 | 27.8/27.8 | 24.4/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.60 | 0.40 | 0.00 | 9.32 | 29.1/29.0 | 23.3/22.1 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.074 | 0.65 | 0.35 | 0.00 | 6.01 | 32.3/21.9 | 19.2/27.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.066 | 0.52 | 0.48 | 0.00 | 6.05 | 22.0/32.6 | 28.9/18.6 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.48 | 0.52 | 0.51 | 5.88 | 21.9/32.3 | 28.9/18.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Danton Heinen: 1+ goals YES | 11 | 0.144 | 0.131 | +0.027 | +0.014 | $3.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 17 | 0.208 | 0.194 | +0.029 | +0.014 | $4.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Kent Johnson: 1+ goals NO | 77 | 0.805 | 0.795 | +0.022 | +0.013 | $13.97 | FUNDED_RESEARCH | $4 | CBJ:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Valeri Nichushkin: 1+ assists NO | 72 | 0.793 | 0.747 | +0.059 | +0.013 | $13.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (4.03 vs 2.88 bp); despite a smaller raw edge (+0.027 vs +0.029/contract); relationships: KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT09PITCBJ-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.038); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (2.88 vs 0.40 bp); alternative not eligible: confidence-adjusted EV +0.0059 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT09PITCBJ-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: CBJ offense suppressed (<= 2 goals)
- **Kent Johnson: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (2.00 vs 1.23 bp); despite a smaller raw edge (+0.022 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi 0.036); failure: CBJ offense succeeds (4+ goals)
- **Valeri Nichushkin: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (1.77 vs 1.23 bp); relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT09PITCBJ-CBJKJOHNSON91-1|no: MOSTLY_INDEPENDENT (phi 0.036); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.4501): highest fidelity KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.3355): highest fidelity KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no (same contract)
- KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3355, phi -0.154)
- KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3355, phi -0.205)
- KXNHLGOAL-26OCT09PITCBJ-CBJKJOHNSON91-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4501, phi -0.203)
- KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4501, phi -0.19)

portfolios: A EV +5.82 (adj +2.02) on $50.00, P(profit) 0.7125, adj growth 15.6 bp · B EV +3.03 (adj +1.21) on $35.58, P(profit) 0.7485, adj growth 10.6 bp · C EV +1.49 (adj +0.48) on $13.66, P(profit) 0.7881, adj growth 4.2 bp · R EV +0.11 (adj +0.06) on $4.00, P(profit) 0.8048, adj growth 2.2 bp

## ANA @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_ANA_win | p_overtime | goals | shots WPG/ANA | WPG/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.56 | 0.44 | 0.00 | 6.0 | 27.9/28.2 | 24.9/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.49 | 0.51 | 0.48 | 5.95 | 28.0/28.4 | 25.0/24.7 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.098 | 0.50 | 0.50 | 0.00 | 6.03 | 22.2/33.7 | 29.9/18.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.55 | 0.45 | 0.00 | 9.25 | 29.6/30.1 | 24.0/23.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.50 | 0.50 | 0.50 | 5.9 | 22.4/33.8 | 30.6/19.3 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.060 | 0.50 | 0.50 | 0.00 | 9.3 | 23.8/35.5 | 28.7/18.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
