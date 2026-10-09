# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-09T15:28:42Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +24.78 | +11.55 | +17.95 | 0.625 | -50.17 | -64.39 | 96.88 |
| B thesis-diversified (joint) ← optimiser card | 142.13 | +25.35 | +13.24 | +20.60 | 0.634 | -43.48 | -60.15 | 115.53 |
| C best expression per thesis | 101.03 | +15.34 | +7.18 | +5.06 | 0.579 | -35.08 | -46.63 | 62.14 |
| R FUNDED research stakes | 11.00 | +2.47 | +1.66 | -5.37 | 0.356 | -5.37 | -5.37 | 0.00 |

## SEA @ DET  ·  10000 joint draws  ·  398 bet sides mapped, 4 +EV candidates, 4 on card


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
| Ryan Winterton: 1+ goals YES | 10 | 0.141 | 0.126 | +0.034 | +0.019 | $4.69 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 9 | 0.120 | 0.108 | +0.025 | +0.012 | $2.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Michael Rasmussen: 1+ goals YES | 11 | 0.144 | 0.130 | +0.028 | +0.013 | $3.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Kaapo Kakko: 1+ assists YES | 29 | 0.349 | 0.315 | +0.044 | +0.010 | $2.89 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SEA:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09SEADET-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (8.29 vs 1.04 bp); despite a smaller raw edge (+0.034 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT09SEADET-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT09SEADET-DETMRASMUSSEN27-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT09SEADET-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.042); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09SEADET-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (3.59 vs 1.04 bp); despite a smaller raw edge (+0.025 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT09SEADET-DETMRASMUSSEN27-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT09SEADET-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.021); failure: SEA offense suppressed (<= 2 goals)
- **Michael Rasmussen: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09SEADET-DETACOPP18-1|yes; why: higher confidence-adjusted growth (3.38 vs 0.40 bp); despite a smaller raw edge (+0.028 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT09SEADET-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT09SEADET-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: DET offense suppressed (<= 2 goals)
- **Kaapo Kakko: 1+ assists YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT09SEADET-DET2|no; why: higher confidence-adjusted growth (1.04 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0021 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.042); KXNHLGOAL-26OCT09SEADET-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT09SEADET-DETMRASMUSSEN27-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.3589): highest fidelity KXNHLAST-26OCT09SEADET-SEAKKAKKO84-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT09SEADET-SEAKKAKKO84-1|yes (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3983): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4215, phi -0.175)
- KXNHLGOAL-26OCT09SEADET-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4215, phi -0.176)
- KXNHLGOAL-26OCT09SEADET-DETMRASMUSSEN27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.388, phi -0.176)
- KXNHLAST-26OCT09SEADET-SEAKKAKKO84-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4215, phi -0.27)

portfolios: A EV +7.11 (adj +3.12) on $31.69, P(profit) 0.5714, adj growth 22.7 bp · B EV +3.45 (adj +1.66) on $13.76, P(profit) 0.3528, adj growth 14.3 bp · C EV +0.50 (adj +0.11) on $3.41, P(profit) 0.3489, adj growth 1.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYR @ WSH  ·  10000 joint draws  ·  416 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_NYR_win | p_overtime | goals | shots WSH/NYR | WSH/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.54 | 0.46 | 0.00 | 6.0 | 26.6/26.3 | 22.9/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.48 | 5.95 | 26.4/26.3 | 23.1/23.2 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.095 | 0.66 | 0.34 | 0.00 | 6.02 | 31.5/21.0 | 18.2/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.57 | 0.43 | 0.00 | 9.23 | 28.1/27.8 | 22.0/21.3 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.54 | 0.46 | 0.46 | 5.87 | 31.5/21.1 | 18.0/28.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.55 | 0.45 | 0.00 | 3.53 | 25.4/25.3 | 23.6/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 17 | 0.251 | 0.230 | +0.071 | +0.050 | $14.07 | FUNDED_RESEARCH | $4 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 13 | 0.173 | 0.160 | +0.035 | +0.022 | $6.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Alex Tuch: 1+ assists NO | 69 | 0.776 | 0.728 | +0.071 | +0.023 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| J.T. Miller: 1+ assists NO | 60 | 0.660 | 0.627 | +0.043 | +0.011 | $5.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09NYRWSH-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (36.05 vs 0.21 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0048 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.04); KXNHLAST-26OCT09NYRWSH-NYRJMILLER8-1|no: MOSTLY_INDEPENDENT (phi 0.027); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (36.05 vs 8.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no: INTENTIONAL_DIVERSIFIER (phi -0.05); KXNHLAST-26OCT09NYRWSH-NYRJMILLER8-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: WSH offense suppressed (<= 2 goals)
- **Alex Tuch: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT09NYRWSH-WSHJKYROU25-1|no; why: higher confidence-adjusted growth (5.63 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.04); KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.05); KXNHLAST-26OCT09NYRWSH-NYRJMILLER8-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: WSH offense succeeds (4+ goals)
- **J.T. Miller: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no; why: KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no has the higher standalone adjusted growth (1.93 vs 1.04 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.088); relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4163): highest fidelity KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes (same contract)
- thesis WSH:SUPPRESSED (p 0.3668): highest fidelity KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no (same contract)
- thesis NYR:SUPPRESSED (p 0.4338): highest fidelity KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3668, phi -0.244)
- KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3668, phi -0.185)
- KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4163, phi -0.199)
- KXNHLAST-26OCT09NYRWSH-NYRJMILLER8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3463, phi -0.283)

portfolios: A EV +6.26 (adj +3.40) on $39.44, P(profit) 0.5671, adj growth 30.5 bp · B EV +9.60 (adj +5.64) on $46.11, P(profit) 0.3701, adj growth 48.8 bp · C EV +8.47 (adj +4.79) on $46.80, P(profit) 0.2514, adj growth 41.3 bp · R EV +1.59 (adj +1.11) on $4.00, P(profit) 0.2514, adj growth 37.1 bp

## PIT @ CBJ  ·  10000 joint draws  ·  420 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_PIT_win | p_overtime | goals | shots CBJ/PIT | CBJ/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.55 | 0.45 | 0.00 | 6.01 | 27.6/27.7 | 24.4/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.47 | 5.97 | 27.5/27.5 | 24.2/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.110 | 0.56 | 0.44 | 0.00 | 9.48 | 29.0/29.3 | 23.6/22.7 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.070 | 0.59 | 0.41 | 0.00 | 6.02 | 32.4/22.0 | 18.9/28.1 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.066 | 0.49 | 0.51 | 0.00 | 6.03 | 21.9/32.0 | 28.1/18.5 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.55 | 0.45 | 0.45 | 5.94 | 32.7/22.2 | 18.9/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Danton Heinen: 1+ goals YES | 10 | 0.141 | 0.128 | +0.035 | +0.022 | $5.64 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 16 | 0.207 | 0.194 | +0.037 | +0.025 | $7.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Valeri Nichushkin: 1+ assists NO | 70 | 0.788 | 0.741 | +0.073 | +0.027 | $17.13 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Matthew Knies: 1+ assists NO | 64 | 0.721 | 0.675 | +0.065 | +0.019 | $12.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (10.79 vs 9.22 bp); despite a smaller raw edge (+0.035 vs +0.037/contract); relationships: KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no: MOSTLY_INDEPENDENT (phi -0.034); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (9.22 vs 1.39 bp); relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: CBJ offense suppressed (<= 2 goals)
- **Valeri Nichushkin: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (7.70 vs 3.61 bp); relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CBJ offense succeeds (4+ goals)
- **Matthew Knies: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT09PITCBJ-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (3.61 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis CBJ:OFFENSE_4PLUS (p 0.4448): highest fidelity KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:SUPPRESSED (p 0.3392): highest fidelity KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no (same contract)
- thesis PIT:SUPPRESSED (p 0.3851): highest fidelity KXNHLAST-26OCT09PITCBJ-PITSCROSBY87-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09PITCBJ-PITSCROSBY87-1|no (same contract)
- KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3392, phi -0.155)
- KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3392, phi -0.201)
- KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4448, phi -0.169)
- KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4448, phi -0.225)

portfolios: A EV +4.67 (adj +1.90) on $39.44, P(profit) 0.4752, adj growth 16.9 bp · B EV +6.41 (adj +3.19) on $42.66, P(profit) 0.7031, adj growth 28.1 bp · C EV +3.67 (adj +1.61) on $28.71, P(profit) 0.5521, adj growth 14.0 bp · R EV +0.65 (adj +0.41) on $2.00, P(profit) 0.1409, adj growth 13.2 bp

## ANA @ WPG  ·  10000 joint draws  ·  404 bet sides mapped, 6 +EV candidates, 4 on card


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
| Neal Pionk: 1+ goals NO | 88 | 0.928 | 0.912 | +0.040 | +0.025 | $17.79 | FUNDED_RESEARCH | $5 | WPG:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 7 | 0.104 | 0.092 | +0.030 | +0.018 | $4.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Morgan Barron: 1+ goals YES | 12 | 0.158 | 0.147 | +0.030 | +0.020 | $5.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Neal Pionk: 1+ assists NO | 56 | 0.678 | 0.598 | +0.101 | +0.021 | $12.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (13.51 vs 3.87 bp); despite a smaller raw edge (+0.040 vs +0.101/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT09ANAWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: WPG offense succeeds (4+ goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (9.54 vs 0.00 bp); despite a smaller raw edge (+0.030 vs +0.043/contract); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT09ANAWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: ANA offense suppressed (<= 2 goals)
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09ANAWPG-WPGCPERFETTI91-1|yes; why: higher confidence-adjusted growth (7.41 vs 0.89 bp); despite a smaller raw edge (+0.030 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0098 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); failure: WPG offense suppressed (<= 2 goals)
- **Neal Pionk: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT09ANAWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (3.87 vs 0.59 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT09ANAWPG-WPGMBARRON36-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); failure: WPG offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:SUPPRESSED (p 0.3725): highest fidelity KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no (same contract)
- thesis ANA:SUPPRESSED (p 0.4004): highest fidelity KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.3835): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.4151, phi -0.115)
- KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4004, phi -0.136)
- KXNHLGOAL-26OCT09ANAWPG-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.3725, phi -0.179)
- KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.3 pts; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.4151, phi -0.237)

portfolios: A EV +6.74 (adj +3.13) on $39.44, P(profit) 0.7281, adj growth 26.7 bp · B EV +5.89 (adj +2.75) on $39.60, P(profit) 0.7281, adj growth 24.3 bp · C EV +2.70 (adj +0.67) on $22.11, P(profit) 0.6779, adj growth 5.9 bp · R EV +0.23 (adj +0.14) on $5.00, P(profit) 0.9276, adj growth 5.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
