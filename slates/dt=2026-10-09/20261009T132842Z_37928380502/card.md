# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-09T13:28:42Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 140.78 | +15.77 | +6.16 | +9.69 | 0.604 | -45.23 | -52.61 | 50.25 |
| B thesis-diversified (joint) ← optimiser card | 109.44 | +11.61 | +4.82 | +11.81 | 0.598 | -29.87 | -40.90 | 42.87 |
| C best expression per thesis | 70.24 | +8.06 | +2.99 | +5.71 | 0.603 | -26.66 | -35.42 | 26.07 |
| R FUNDED research stakes | 10.00 | +1.40 | +0.83 | -4.37 | 0.356 | -4.37 | -4.37 | 0.00 |

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

## NYR @ WSH  ·  10000 joint draws  ·  416 bet sides mapped, 3 +EV candidates, 3 on card


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
| Aliaksei Protas: 1+ goals YES | 19 | 0.248 | 0.230 | +0.047 | +0.029 | $8.81 | FUNDED_RESEARCH | $3 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Alex Tuch: 1+ assists NO | 69 | 0.770 | 0.725 | +0.065 | +0.020 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Boone Jenner: 1+ goals YES | 14 | 0.169 | 0.159 | +0.021 | +0.011 | $3.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT09NYRWSH-7|yes; why: higher confidence-adjusted growth (11.30 vs 0.60 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.863 vs 0.679); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no: INTENTIONAL_DIVERSIFIER (phi -0.061); KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: WSH offense suppressed (<= 2 goals)
- **Alex Tuch: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT09NYRWSH-WSHJKYROU25-1|no; why: higher confidence-adjusted growth (4.28 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.061); KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.041); failure: WSH offense succeeds (4+ goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (11.30 vs 1.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.041); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4179): highest fidelity KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes (same contract)
- thesis WSH:SUPPRESSED (p 0.373): highest fidelity KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no (same contract)
- KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.373, phi -0.237)
- KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4179, phi -0.227)
- KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.373, phi -0.17)

portfolios: A EV +6.15 (adj +3.14) on $40.78, P(profit) 0.3422, adj growth 24.9 bp · B EV +4.36 (adj +2.07) on $31.95, P(profit) 0.3422, adj growth 18.1 bp · C EV +3.93 (adj +1.85) on $28.84, P(profit) 0.248, adj growth 16.1 bp · R EV +0.71 (adj +0.43) on $3.00, P(profit) 0.248, adj growth 14.0 bp

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
| Valeri Nichushkin: 1+ assists NO | 71 | 0.793 | 0.747 | +0.069 | +0.022 | $18.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Danton Heinen: 1+ goals YES | 11 | 0.144 | 0.132 | +0.027 | +0.015 | $4.11 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Matthew Knies: 1+ assists NO | 65 | 0.724 | 0.682 | +0.058 | +0.016 | $11.74 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Mathieu Olivier: 1+ goals YES | 17 | 0.208 | 0.193 | +0.029 | +0.013 | $3.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Valeri Nichushkin: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (5.45 vs 2.58 bp); relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: CBJ offense succeeds (4+ goals)
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (4.78 vs 2.39 bp); despite a smaller raw edge (+0.027 vs +0.029/contract); relationships: KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.038); KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: CBJ offense suppressed (<= 2 goals)
- **Matthew Knies: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no; why: higher confidence-adjusted growth (2.58 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.035); failure: CBJ offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (2.39 vs 0.40 bp); alternative not eligible: confidence-adjusted EV +0.0059 below the 0.010/contract floor; relationships: KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no: MOSTLY_INDEPENDENT (phi -0.035); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CBJ:SUPPRESSED (p 0.3355): highest fidelity KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.4501): highest fidelity KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes (same contract)
- thesis PIT:SUPPRESSED (p 0.4131): highest fidelity KXNHLAST-26OCT09PITCBJ-PITSCROSBY87-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09PITCBJ-PITSCROSBY87-1|no (same contract)
- KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4501, phi -0.19)
- KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3355, phi -0.154)
- KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4501, phi -0.228)
- KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3355, phi -0.205)

portfolios: A EV +5.20 (adj +1.65) on $50.00, P(profit) 0.4801, adj growth 13.8 bp · B EV +4.35 (adj +1.65) on $37.98, P(profit) 0.7041, adj growth 14.6 bp · C EV +2.64 (adj +0.82) on $25.42, P(profit) 0.532, adj growth 7.2 bp · R EV +0.47 (adj +0.26) on $2.00, P(profit) 0.1443, adj growth 7.5 bp

## ANA @ WPG  ·  10000 joint draws  ·  404 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_ANA_win | p_overtime | goals | shots WPG/ANA | WPG/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.56 | 0.44 | 0.00 | 6.0 | 27.9/28.2 | 24.9/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.49 | 0.51 | 0.48 | 5.95 | 28.0/28.4 | 25.0/24.7 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.098 | 0.50 | 0.50 | 0.00 | 6.03 | 22.2/33.7 | 29.9/18.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.55 | 0.45 | 0.00 | 9.25 | 29.6/30.1 | 24.0/23.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.50 | 0.50 | 0.50 | 5.9 | 22.4/33.8 | 30.6/19.3 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.060 | 0.50 | 0.50 | 0.00 | 9.3 | 23.8/35.5 | 28.7/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Neal Pionk: 1+ goals NO | 88 | 0.928 | 0.912 | +0.040 | +0.025 | $20.00 | FUNDED_RESEARCH | $5 | WPG:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Morgan Barron: 1+ goals YES | 13 | 0.158 | 0.148 | +0.020 | +0.010 | $2.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Cutter Gauthier: 1+ goals NO | 60 | 0.643 | 0.630 | +0.027 | +0.013 | $8.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Neal Pionk: 1+ assists NO | 57 | 0.678 | 0.598 | +0.091 | +0.011 | $7.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (13.51 vs 1.06 bp); despite a smaller raw edge (+0.040 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: WPG offense succeeds (4+ goals)
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09ANAWPG-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (1.93 vs 0.23 bp); alternative not eligible: confidence-adjusted EV +0.0049 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); failure: WPG offense suppressed (<= 2 goals)
- **Cutter Gauthier: 1+ goals NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT09ANAWPG-ANALCARLSSON91-1|no; why: higher confidence-adjusted growth (1.63 vs 0.10 bp); alternative not eligible: confidence-adjusted EV +0.0032 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT09ANAWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: ANA offense succeeds (4+ goals)
- **Neal Pionk: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09ANAWPG-WPGMSCHEIFELE55-2|no; why: higher confidence-adjusted growth (1.06 vs 0.42 bp); alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT09ANAWPG-WPGMBARRON36-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: WPG offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis ANA:SUPPRESSED (p 0.4004): highest fidelity KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no (same contract)
- thesis WPG:SUPPRESSED (p 0.3725): highest fidelity KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.4151): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.4151, phi -0.115)
- KXNHLGOAL-26OCT09ANAWPG-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3725, phi -0.179)
- KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.3835, phi -0.279)
- KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.3 pts; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.4151, phi -0.237)

portfolios: A EV +4.41 (adj +1.37) on $50.00, P(profit) 0.501, adj growth 11.5 bp · B EV +2.91 (adj +1.10) on $39.51, P(profit) 0.495, adj growth 10.2 bp · C EV +1.49 (adj +0.32) on $15.98, P(profit) 0.4355, adj growth 2.8 bp · R EV +0.23 (adj +0.14) on $5.00, P(profit) 0.9276, adj growth 5.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
