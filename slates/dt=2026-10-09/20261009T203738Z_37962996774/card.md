# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-09T20:37:38Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +30.48 | +12.51 | +25.97 | 0.648 | -53.92 | -72.86 | 103.28 |
| B thesis-diversified (joint) ← optimiser card | 142.94 | +26.64 | +14.42 | +22.84 | 0.636 | -47.50 | -60.91 | 126.01 |
| C best expression per thesis | 118.11 | +17.01 | +9.16 | +14.94 | 0.593 | -45.04 | -50.72 | 80.04 |
| R FUNDED research stakes | 10.00 | +1.86 | +1.22 | -4.18 | 0.350 | -4.18 | -4.18 | 0.00 |

## SEA @ DET  ·  10000 joint draws  ·  422 bet sides mapped, 6 +EV candidates, 4 on card

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
| Ryan Winterton: 1+ goals YES | 10 | 0.141 | 0.129 | +0.034 | +0.023 | $5.87 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Andrew Copp: 1+ goals YES | 17 | 0.209 | 0.198 | +0.029 | +0.018 | $5.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Emmitt Finnie: 1+ assists YES | 25 | 0.325 | 0.278 | +0.062 | +0.015 | $4.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
| Emmitt Finnie: 1+ goals YES | 17 | 0.200 | 0.191 | +0.020 | +0.011 | $3.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09SEADET-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (11.81 vs 1.76 bp); relationships: KXNHLGOAL-26OCT09SEADET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT09SEADET-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: SEA offense suppressed (<= 2 goals)
- **Andrew Copp: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes; why: higher confidence-adjusted growth (4.87 vs 2.35 bp); despite a smaller raw edge (+0.029 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi 0.04); KXNHLGOAL-26OCT09SEADET-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: DET offense suppressed (<= 2 goals)
- **Emmitt Finnie: 1+ assists YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09SEADET-DETACOPP18-1|yes; why: higher confidence-adjusted growth (2.35 vs 0.79 bp); alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT09SEADET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.04); KXNHLGOAL-26OCT09SEADET-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: DET offense suppressed (<= 2 goals)
- **Emmitt Finnie: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes has the higher standalone adjusted growth (2.35 vs 1.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT09SEADET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DET:OFFENSE_4PLUS (p 0.3983): highest fidelity KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.3589): highest fidelity KXNHLAST-26OCT09SEADET-SEAKKAKKO84-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT09SEADET-SEAKKAKKO84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4215, phi -0.175)
- KXNHLGOAL-26OCT09SEADET-DETACOPP18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.388, phi -0.203)
- KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.388, phi -0.258)
- KXNHLGOAL-26OCT09SEADET-DETEFINNIE58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.388, phi -0.192)

portfolios: A EV +7.98 (adj +3.16) on $37.50, P(profit) 0.4604, adj growth 23.8 bp · B EV +4.10 (adj +2.22) on $18.54, P(profit) 0.3622, adj growth 19.2 bp · C EV +1.44 (adj +0.44) on $7.63, P(profit) 0.4565, adj growth 3.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYR @ WSH  ·  10000 joint draws  ·  480 bet sides mapped, 8 +EV candidates, 4 on card

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
| Aliaksei Protas: 1+ goals YES | 18 | 0.242 | 0.223 | +0.051 | +0.032 | $8.80 | FUNDED_RESEARCH | $3 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Gabe Perreault: 1+ assists YES | 23 | 0.304 | 0.265 | +0.062 | +0.022 | $6.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ assists NO | 73 | 0.802 | 0.763 | +0.058 | +0.019 | $18.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Alex Tuch: 1+ assists NO | 70 | 0.772 | 0.731 | +0.057 | +0.016 | $16.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09NYRWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (14.49 vs 2.46 bp); despite a smaller raw edge (+0.051 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT09NYRWSH-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no: INTENTIONAL_DIVERSIFIER (phi -0.07); failure: WSH offense suppressed (<= 2 goals)
- **Gabe Perreault: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09NYRWSH-NYRALAFRENIERE13-1|yes; why: higher confidence-adjusted growth (5.91 vs 0.51 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: NYR offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09NYRWSH-NYRJMILLER8-1|no; why: higher confidence-adjusted growth (4.39 vs 0.24 bp); alternative not eligible: confidence-adjusted EV +0.0051 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT09NYRWSH-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: NYR offense succeeds (4+ goals)
- **Alex Tuch: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT09NYRWSH-WSHJKYROU25-1|no; why: higher confidence-adjusted growth (2.81 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.07); KXNHLAST-26OCT09NYRWSH-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: WSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4086): highest fidelity KXNHLAST-26OCT09NYRWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.3412): highest fidelity KXNHLAST-26OCT09NYRWSH-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT09NYRWSH-NYRGPERREAULT94-1|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.4371): highest fidelity KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3775, phi -0.244)
- KXNHLAST-26OCT09NYRWSH-NYRGPERREAULT94-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4371, phi -0.266)
- KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3412, phi -0.231)
- KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4086, phi -0.219)

portfolios: A EV +7.85 (adj +1.82) on $37.50, P(profit) 0.5297, adj growth 14.7 bp · B EV +6.73 (adj +2.92) on $50.00, P(profit) 0.4215, adj growth 25.8 bp · C EV +6.73 (adj +2.92) on $50.00, P(profit) 0.4215, adj growth 25.8 bp · R EV +0.81 (adj +0.51) on $3.00, P(profit) 0.2417, adj growth 16.7 bp

## PIT @ CBJ  ·  10000 joint draws  ·  458 bet sides mapped, 9 +EV candidates, 4 on card

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
| Danton Heinen: 1+ goals YES | 10 | 0.141 | 0.130 | +0.035 | +0.024 | $6.01 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 11 | 0.146 | 0.136 | +0.030 | +0.019 | $5.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 16 | 0.203 | 0.191 | +0.033 | +0.021 | $6.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Valeri Nichushkin: 1+ assists NO | 70 | 0.797 | 0.731 | +0.083 | +0.016 | $17.38 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (12.51 vs 6.97 bp); relationships: KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09PITCBJ-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (7.74 vs 1.84 bp); despite a smaller raw edge (+0.030 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: PIT offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (6.97 vs 1.91 bp); relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.029); failure: CBJ offense suppressed (<= 2 goals)
- **Valeri Nichushkin: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (2.79 vs 0.74 bp); despite a smaller raw edge (+0.083 vs +0.084/contract); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.3934): highest fidelity KXNHLAST-26OCT09PITCBJ-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:OFFENSE_4PLUS (p 0.4377): highest fidelity KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:SUPPRESSED (p 0.3426): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3426, phi -0.148)
- KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3934, phi -0.201)
- KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3426, phi -0.214)
- KXNHLAST-26OCT09PITCBJ-CBJVNICHUSHKIN43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.2 pts; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4377, phi -0.188)

portfolios: A EV +6.61 (adj +2.37) on $37.50, P(profit) 0.5994, adj growth 19.3 bp · B EV +6.47 (adj +3.32) on $34.51, P(profit) 0.4156, adj growth 28.7 bp · C EV +3.00 (adj +1.93) on $31.13, P(profit) 0.3196, adj growth 17.0 bp · R EV +0.66 (adj +0.44) on $2.00, P(profit) 0.1415, adj growth 14.4 bp

## ANA @ WPG  ·  10000 joint draws  ·  484 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

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
| Neal Pionk: 1+ goals NO | 85 | 0.926 | 0.906 | +0.067 | +0.047 | $20.00 | FUNDED_RESEARCH | $5 | WPG:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| A.J. Greer: 1+ goals YES | 16 | 0.234 | 0.213 | +0.065 | +0.044 | $11.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 7 | 0.109 | 0.094 | +0.035 | +0.020 | $4.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 8 | 0.113 | 0.100 | +0.028 | +0.015 | $3.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (40.97 vs 0.61 bp); despite a smaller raw edge (+0.067 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT09ANAWPG-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: WPG offense succeeds (4+ goals)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09ANAWPG-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (29.15 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT09ANAWPG-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: ANA offense suppressed (<= 2 goals)
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

portfolios: A EV +8.03 (adj +5.16) on $37.50, P(profit) 0.3162, adj growth 45.5 bp · B EV +9.34 (adj +5.96) on $39.89, P(profit) 0.3943, adj growth 52.4 bp · C EV +5.83 (adj +3.87) on $29.35, P(profit) 0.2343, adj growth 33.4 bp · R EV +0.39 (adj +0.27) on $5.00, P(profit) 0.926, adj growth 10.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
