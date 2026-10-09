# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-09T19:47:39Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.00 | +11.46 | +22.01 | 0.640 | -46.59 | -62.52 | 96.99 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +24.18 | +13.44 | +19.37 | 0.642 | -42.90 | -61.43 | 118.49 |
| C best expression per thesis | 102.08 | +17.09 | +8.82 | +11.85 | 0.620 | -42.63 | -54.54 | 76.35 |
| R FUNDED research stakes | 13.00 | +1.79 | +1.13 | -2.31 | 0.262 | -7.18 | -8.13 | 0.00 |

## SEA @ DET  ·  10000 joint draws  ·  400 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.564 / away 0.436

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
| Ryan Winterton: 1+ goals YES | 10 | 0.141 | 0.128 | +0.034 | +0.022 | $5.25 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Andrew Copp: 1+ goals YES | 17 | 0.209 | 0.198 | +0.029 | +0.018 | $4.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Mackie Samoskevich: 1+ assists NO | 79 | 0.860 | 0.818 | +0.059 | +0.016 | $18.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SEA:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Emmitt Finnie: 1+ assists YES | 25 | 0.325 | 0.278 | +0.062 | +0.015 | $4.04 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09SEADET-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (10.57 vs 1.76 bp); relationships: KXNHLGOAL-26OCT09SEADET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT09SEADET-SEAMSAMOSKEVICH11-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: SEA offense suppressed (<= 2 goals)
- **Andrew Copp: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes; why: higher confidence-adjusted growth (4.87 vs 2.35 bp); despite a smaller raw edge (+0.029 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT09SEADET-SEAMSAMOSKEVICH11-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi 0.04); failure: DET offense suppressed (<= 2 goals)
- **Mackie Samoskevich: 1+ assists NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT09SEADET-SEAMSAMOSKEVICH11-1|no; why: higher confidence-adjusted growth (3.52 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT09SEADET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: SEA offense succeeds (4+ goals)
- **Emmitt Finnie: 1+ assists YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09SEADET-DETACOPP18-1|yes; why: higher confidence-adjusted growth (2.35 vs 0.79 bp); alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT09SEADET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.04); KXNHLAST-26OCT09SEADET-SEAMSAMOSKEVICH11-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DET:OFFENSE_4PLUS (p 0.3983): highest fidelity KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.3589): highest fidelity KXNHLAST-26OCT09SEADET-SEAKKAKKO84-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT09SEADET-SEAKKAKKO84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:SUPPRESSED (p 0.4215): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4215, phi -0.175)
- KXNHLGOAL-26OCT09SEADET-DETACOPP18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.388, phi -0.203)
- KXNHLAST-26OCT09SEADET-SEAMSAMOSKEVICH11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:OFFENSE_4PLUS (p 0.3589, phi -0.161)
- KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.388, phi -0.258)

portfolios: A EV +6.64 (adj +2.28) on $37.50, P(profit) 0.5936, adj growth 18.0 bp · B EV +4.80 (adj +2.15) on $32.96, P(profit) 0.4942, adj growth 18.9 bp · C EV +1.44 (adj +0.44) on $7.63, P(profit) 0.4565, adj growth 3.9 bp · R EV +0.65 (adj +0.41) on $2.00, P(profit) 0.1406, adj growth 13.0 bp

## NYR @ WSH  ·  10000 joint draws  ·  420 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.564 / away 0.436

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_NYR_win | p_overtime | goals | shots WSH/NYR | WSH/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.55 | 0.45 | 0.00 | 5.96 | 26.6/26.4 | 23.2/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.45 | 5.91 | 26.4/26.4 | 23.1/23.2 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.092 | 0.62 | 0.38 | 0.00 | 6.03 | 31.6/20.7 | 17.8/27.4 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.56 | 0.44 | 0.48 | 5.91 | 31.8/21.4 | 18.3/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.57 | 0.43 | 0.00 | 9.23 | 28.3/27.8 | 22.3/21.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.53 | 0.47 | 0.00 | 3.49 | 25.5/25.2 | 23.3/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 18 | 0.242 | 0.225 | +0.051 | +0.035 | $9.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ assists NO | 73 | 0.802 | 0.763 | +0.058 | +0.019 | $18.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Boone Jenner: 1+ goals YES | 14 | 0.168 | 0.160 | +0.019 | +0.011 | $3.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jakob Chychrun: 1+ goals NO | 81 | 0.840 | 0.831 | +0.019 | +0.010 | $13.97 | FUNDED_RESEARCH | $4 | WSH:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09NYRWSH-WSHAOVECHKIN8-1|yes; why: higher confidence-adjusted growth (16.81 vs 0.07 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0027 below the 0.010/contract floor; relationships: KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT09NYRWSH-WSHJCHYCHRUN6-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: WSH offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (4.39 vs 0.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0005 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT09NYRWSH-WSHJCHYCHRUN6-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: NYR offense succeeds (4+ goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (16.81 vs 2.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT09NYRWSH-WSHJCHYCHRUN6-1|no: MOSTLY_INDEPENDENT (phi -0.023); failure: WSH offense suppressed (<= 2 goals)
- **Jakob Chychrun: 1+ goals NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no; why: higher confidence-adjusted growth (1.57 vs 0.46 bp); despite a smaller raw edge (+0.019 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: WSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4086): highest fidelity KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.4371): highest fidelity KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.3412): highest fidelity KXNHLAST-26OCT09NYRWSH-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT09NYRWSH-NYRGPERREAULT94-1|yes (same contract)
- KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3775, phi -0.244)
- KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3412, phi -0.231)
- KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3775, phi -0.166)
- KXNHLGOAL-26OCT09NYRWSH-WSHJCHYCHRUN6-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4086, phi -0.171)

portfolios: A EV +6.45 (adj +2.97) on $37.50, P(profit) 0.5449, adj growth 24.6 bp · B EV +4.75 (adj +2.63) on $45.40, P(profit) 0.3447, adj growth 23.0 bp · C EV +5.05 (adj +2.54) on $33.87, P(profit) 0.4304, adj growth 22.1 bp · R EV +0.09 (adj +0.05) on $4.00, P(profit) 0.8397, adj growth 1.7 bp

## PIT @ CBJ  ·  10000 joint draws  ·  422 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.517 / away 0.483

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_PIT_win | p_overtime | goals | shots CBJ/PIT | CBJ/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.57 | 0.43 | 0.00 | 6.05 | 27.5/27.5 | 24.3/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.49 | 5.97 | 27.5/27.6 | 24.3/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.53 | 0.47 | 0.00 | 9.29 | 29.1/29.0 | 23.2/23.0 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.066 | 0.62 | 0.38 | 0.00 | 6.04 | 32.3/21.9 | 19.1/28.1 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.56 | 0.44 | 0.45 | 5.96 | 32.6/22.2 | 18.9/29.3 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.063 | 0.46 | 0.54 | 0.00 | 6.01 | 21.9/32.2 | 28.2/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Danton Heinen: 1+ goals YES | 10 | 0.141 | 0.127 | +0.035 | +0.021 | $4.99 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 11 | 0.146 | 0.136 | +0.030 | +0.019 | $4.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Valeri Nichushkin: 1+ assists NO | 71 | 0.797 | 0.749 | +0.073 | +0.024 | $18.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Mathieu Olivier: 1+ goals YES | 16 | 0.203 | 0.190 | +0.033 | +0.020 | $5.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (10.02 vs 6.18 bp); relationships: KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: CBJ offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09PITCBJ-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (7.74 vs 1.84 bp); despite a smaller raw edge (+0.030 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: PIT offense suppressed (<= 2 goals)
- **Valeri Nichushkin: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (6.48 vs 1.39 bp); despite a smaller raw edge (+0.073 vs +0.084/contract); relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: CBJ offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (6.18 vs 1.91 bp); relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.029); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.3934): highest fidelity KXNHLAST-26OCT09PITCBJ-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:OFFENSE_4PLUS (p 0.4377): highest fidelity KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:SUPPRESSED (p 0.3934): highest fidelity KXNHLAST-26OCT09PITCBJ-PITEMALKIN71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09PITCBJ-PITEMALKIN71-1|no (same contract)
- KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3426, phi -0.148)
- KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3934, phi -0.201)
- KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4377, phi -0.188)
- KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3426, phi -0.214)

portfolios: A EV +4.88 (adj +1.05) on $37.50, P(profit) 0.6059, adj growth 8.9 bp · B EV +5.81 (adj +3.04) on $34.01, P(profit) 0.383, adj growth 26.7 bp · C EV +4.76 (adj +1.97) on $31.23, P(profit) 0.6552, adj growth 17.0 bp · R EV +0.66 (adj +0.40) on $2.00, P(profit) 0.1415, adj growth 12.5 bp

## ANA @ WPG  ·  10000 joint draws  ·  400 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.523 / away 0.477

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_ANA_win | p_overtime | goals | shots WPG/ANA | WPG/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.53 | 0.47 | 0.00 | 6.0 | 27.9/28.3 | 24.9/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.45 | 5.92 | 27.9/28.4 | 25.1/24.7 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.098 | 0.48 | 0.52 | 0.00 | 6.1 | 22.5/33.6 | 29.5/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.55 | 0.45 | 0.00 | 9.31 | 29.4/29.7 | 23.7/23.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.48 | 0.52 | 0.45 | 5.91 | 22.4/33.5 | 30.2/19.2 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.069 | 0.49 | 0.51 | 0.00 | 9.3 | 23.8/35.2 | 28.6/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Neal Pionk: 1+ goals NO | 85 | 0.926 | 0.906 | +0.067 | +0.047 | $18.87 | FUNDED_RESEARCH | $5 | WPG:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| A.J. Greer: 1+ goals YES | 16 | 0.234 | 0.213 | +0.065 | +0.044 | $11.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 7 | 0.109 | 0.094 | +0.035 | +0.020 | $4.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 8 | 0.113 | 0.100 | +0.028 | +0.015 | $3.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (40.97 vs 0.61 bp); despite a smaller raw edge (+0.067 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT09ANAWPG-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: WPG offense succeeds (4+ goals)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09ANAWPG-ANARPOEHLING25-1|yes; why: higher confidence-adjusted growth (29.15 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT09ANAWPG-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: ANA offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes has the higher standalone adjusted growth (29.15 vs 12.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT09ANAWPG-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: ANA offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes has the higher standalone adjusted growth (29.15 vs 5.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3873): highest fidelity KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes (same contract)
- thesis ANA:SUPPRESSED (p 0.3956): highest fidelity KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no (same contract)
- thesis WPG:SUPPRESSED (p 0.3723): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.4129, phi -0.131)
- KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3956, phi -0.235)
- KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3956, phi -0.158)
- KXNHLGOAL-26OCT09ANAWPG-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3956, phi -0.143)

portfolios: A EV +8.03 (adj +5.16) on $37.50, P(profit) 0.3162, adj growth 45.5 bp · B EV +8.81 (adj +5.62) on $37.63, P(profit) 0.3943, adj growth 49.8 bp · C EV +5.83 (adj +3.87) on $29.35, P(profit) 0.2343, adj growth 33.4 bp · R EV +0.39 (adj +0.27) on $5.00, P(profit) 0.926, adj growth 10.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
