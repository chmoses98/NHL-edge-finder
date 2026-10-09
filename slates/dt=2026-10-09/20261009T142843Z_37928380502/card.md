# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-09T14:28:43Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 136.40 | +27.14 | +14.13 | +19.78 | 0.573 | -82.14 | -82.14 | 105.89 |
| B thesis-diversified (joint) ← optimiser card | 86.34 | +15.42 | +7.88 | +8.98 | 0.627 | -37.55 | -49.59 | 68.33 |
| C best expression per thesis | 32.40 | +4.54 | +2.13 | +2.87 | 0.549 | -17.06 | -32.40 | 18.48 |
| R FUNDED research stakes | 7.00 | +1.57 | +0.95 | -1.03 | 0.356 | -7.00 | -7.00 | 0.00 |

## SEA @ DET  ·  10000 joint draws  ·  398 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_SEA_win | p_overtime | goals | shots DET/SEA | DET/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.54 | 0.46 | 0.00 | 6.01 | 27.7/27.3 | 23.9/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.46 | 5.91 | 28.0/27.4 | 24.2/24.7 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.105 | 0.57 | 0.43 | 0.00 | 5.98 | 33.1/21.6 | 18.6/29.1 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.54 | 0.46 | 0.47 | 5.92 | 33.4/21.9 | 18.7/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.51 | 0.49 | 0.00 | 9.37 | 29.5/29.2 | 23.1/23.3 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.065 | 0.59 | 0.41 | 0.00 | 9.17 | 34.9/23.3 | 18.0/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Winterton: 1+ goals YES | 10 | 0.141 | 0.126 | +0.034 | +0.019 | $4.76 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 9 | 0.120 | 0.106 | +0.025 | +0.011 | $2.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09SEADET-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (8.29 vs 0.74 bp); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09SEADET-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09SEADET-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (2.88 vs 0.74 bp); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.3589): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4215, phi -0.175)
- KXNHLGOAL-26OCT09SEADET-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4215, phi -0.176)

portfolios: A EV +4.84 (adj +2.49) on $16.39, P(profit) 0.2438, adj growth 17.6 bp · B EV +2.21 (adj +1.15) on $7.38, P(profit) 0.2438, adj growth 9.9 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Aliaksei Protas: 1+ goals YES | 19 | 0.248 | 0.230 | +0.047 | +0.029 | $8.70 | FUNDED_RESEARCH | $3 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $5.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Alex Tuch: 1+ assists NO | 70 | 0.770 | 0.728 | +0.056 | +0.013 | $15.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT09NYRWSH-7|yes; why: higher confidence-adjusted growth (11.30 vs 0.60 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.863 vs 0.679); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no: INTENTIONAL_DIVERSIFIER (phi -0.061); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (11.30 vs 7.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.041); failure: WSH offense suppressed (<= 2 goals)
- **Alex Tuch: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT09NYRWSH-WSHJKYROU25-1|no; why: higher confidence-adjusted growth (1.79 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.061); KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.041); failure: WSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4179): highest fidelity KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes (same contract)
- thesis WSH:SUPPRESSED (p 0.373): highest fidelity KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no (same contract)
- KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.373, phi -0.237)
- KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.373, phi -0.17)
- KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4179, phi -0.227)

portfolios: A EV +7.05 (adj +3.80) on $43.76, P(profit) 0.3741, adj growth 29.7 bp · B EV +4.46 (adj +2.33) on $29.36, P(profit) 0.3741, adj growth 20.2 bp · C EV +3.16 (adj +1.52) on $22.98, P(profit) 0.248, adj growth 13.2 bp · R EV +0.71 (adj +0.43) on $3.00, P(profit) 0.248, adj growth 14.0 bp

## PIT @ CBJ  ·  10000 joint draws  ·  420 bet sides mapped, 4 +EV candidates, 4 on card


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
| Danton Heinen: 1+ goals YES | 10 | 0.144 | 0.130 | +0.038 | +0.023 | $5.94 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Valeri Nichushkin: 1+ assists NO | 71 | 0.793 | 0.747 | +0.069 | +0.022 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Mathieu Olivier: 1+ goals YES | 16 | 0.208 | 0.185 | +0.039 | +0.016 | $4.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 23 | 0.273 | 0.259 | +0.031 | +0.016 | $5.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (12.09 vs 3.81 bp); despite a smaller raw edge (+0.038 vs +0.039/contract); relationships: KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CBJ offense suppressed (<= 2 goals)
- **Valeri Nichushkin: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (5.45 vs 0.79 bp); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.035); failure: CBJ offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (3.81 vs 3.13 bp); relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (3.81 vs 3.13 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CBJ:OFFENSE_4PLUS (p 0.4501): highest fidelity KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes (same contract)
- thesis CBJ:SUPPRESSED (p 0.3355): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3355, phi -0.154)
- KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4501, phi -0.19)
- KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3355, phi -0.205)
- KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3355, phi -0.221)

portfolios: A EV +9.24 (adj +4.48) on $50.00, P(profit) 0.4682, adj growth 34.0 bp · B EV +5.71 (adj +2.67) on $35.65, P(profit) 0.4419, adj growth 23.3 bp · C EV +0.99 (adj +0.40) on $4.28, P(profit) 0.2085, adj growth 3.4 bp · R EV +0.71 (adj +0.44) on $2.00, P(profit) 0.1443, adj growth 14.1 bp

## ANA @ WPG  ·  10000 joint draws  ·  404 bet sides mapped, 3 +EV candidates, 3 on card


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
| Morgan Barron: 1+ goals YES | 12 | 0.158 | 0.147 | +0.030 | +0.020 | $5.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 7 | 0.104 | 0.090 | +0.030 | +0.015 | $3.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 32 | 0.360 | 0.349 | +0.025 | +0.014 | $5.22 | FUNDED_RESEARCH | $2 | WPG:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09ANAWPG-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (7.41 vs 1.89 bp); relationships: KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT09ANAWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: WPG offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (7.04 vs 0.00 bp); despite a smaller raw edge (+0.030 vs +0.043/contract); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT09ANAWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: ANA offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09ANAWPG-WPGCPERFETTI91-1|yes; why: higher confidence-adjusted growth (1.89 vs 0.04 bp); despite a smaller raw edge (+0.025 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0022 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.4151): highest fidelity KXNHLGOAL-26OCT09ANAWPG-WPGMSCHEIFELE55-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT09ANAWPG-WPGMSCHEIFELE55-1|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.3835): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT09ANAWPG-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3725, phi -0.179)
- KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4004, phi -0.136)
- KXNHLGOAL-26OCT09ANAWPG-WPGMSCHEIFELE55-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3725, phi -0.28)

portfolios: A EV +6.02 (adj +3.36) on $26.25, P(profit) 0.5204, adj growth 24.5 bp · B EV +3.03 (adj +1.73) on $13.95, P(profit) 0.5204, adj growth 14.9 bp · C EV +0.39 (adj +0.21) on $5.14, P(profit) 0.3605, adj growth 1.9 bp · R EV +0.15 (adj +0.08) on $2.00, P(profit) 0.3605, adj growth 2.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
