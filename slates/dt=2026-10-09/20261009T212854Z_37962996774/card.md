# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-09T21:28:54Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +33.42 | +13.59 | +27.85 | 0.674 | -43.05 | -61.47 | 116.38 |
| B thesis-diversified (joint) ← optimiser card | 127.48 | +31.26 | +19.02 | +24.47 | 0.641 | -59.83 | -77.92 | 164.40 |
| C best expression per thesis | 119.08 | +24.75 | +13.15 | +18.05 | 0.622 | -44.72 | -57.61 | 114.01 |
| R FUNDED research stakes | 11.00 | +2.39 | +1.64 | -5.24 | 0.352 | -5.24 | -5.24 | 0.00 |

## SEA @ DET  ·  10000 joint draws  ·  422 bet sides mapped, 8 +EV candidates, 4 on card

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
| Ryan Winterton: 1+ goals YES | 10 | 0.143 | 0.131 | +0.036 | +0.025 | $6.18 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 9 | 0.126 | 0.116 | +0.030 | +0.020 | $4.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Ben Chiarot: 1+ goals YES | 4 | 0.058 | 0.054 | +0.016 | +0.011 | $2.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Andrew Copp: 1+ goals YES | 17 | 0.209 | 0.198 | +0.029 | +0.018 | $5.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09SEADET-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (13.55 vs 4.15 bp); despite a smaller raw edge (+0.036 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT09SEADET-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT09SEADET-DETBCHIAROT8-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT09SEADET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes has the higher standalone adjusted growth (13.55 vs 9.69 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT09SEADET-DETBCHIAROT8-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT09SEADET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: SEA offense suppressed (<= 2 goals)
- **Ben Chiarot: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes; why: higher confidence-adjusted growth (6.42 vs 2.35 bp); despite a smaller raw edge (+0.016 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT09SEADET-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT09SEADET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: DET offense suppressed (<= 2 goals)
- **Andrew Copp: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes; why: higher confidence-adjusted growth (4.87 vs 2.35 bp); despite a smaller raw edge (+0.029 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT09SEADET-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT09SEADET-DETBCHIAROT8-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.3589): highest fidelity KXNHLAST-26OCT09SEADET-SEAKKAKKO84-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:OFFENSE_4PLUS (p 0.3983): highest fidelity KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT09SEADET-DETEFINNIE58-1|yes (same contract)
- thesis SEA:SUPPRESSED (p 0.4215): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT09SEADET-SEARWINTERTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4215, phi -0.189)
- KXNHLGOAL-26OCT09SEADET-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4215, phi -0.159)
- KXNHLGOAL-26OCT09SEADET-DETBCHIAROT8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.388, phi -0.114)
- KXNHLGOAL-26OCT09SEADET-DETACOPP18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.388, phi -0.203)

portfolios: A EV +7.24 (adj +2.72) on $37.50, P(profit) 0.5892, adj growth 22.0 bp · B EV +5.48 (adj +3.66) on $19.04, P(profit) 0.4428, adj growth 31.4 bp · C EV +3.19 (adj +1.69) on $10.69, P(profit) 0.4217, adj growth 14.5 bp · R EV +0.69 (adj +0.46) on $2.00, P(profit) 0.1428, adj growth 15.1 bp

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
| Aliaksei Protas: 1+ goals YES | 17 | 0.242 | 0.223 | +0.062 | +0.043 | $13.04 | FUNDED_RESEARCH | $4 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Gabe Perreault: 1+ assists YES | 23 | 0.304 | 0.265 | +0.062 | +0.022 | $6.78 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Boone Jenner: 1+ goals YES | 14 | 0.168 | 0.160 | +0.019 | +0.011 | $3.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jordan Kyrou: 1+ assists NO | 74 | 0.839 | 0.765 | +0.085 | +0.011 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09NYRWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (26.40 vs 2.46 bp); despite a smaller raw edge (+0.062 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT09NYRWSH-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT09NYRWSH-WSHJKYROU25-1|no: INTENTIONAL_DIVERSIFIER (phi -0.221); failure: WSH offense suppressed (<= 2 goals)
- **Gabe Perreault: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09NYRWSH-NYRALAFRENIERE13-1|yes; why: higher confidence-adjusted growth (5.91 vs 0.51 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT09NYRWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: NYR offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (26.40 vs 2.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT09NYRWSH-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT09NYRWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.019); failure: WSH offense suppressed (<= 2 goals)
- **Jordan Kyrou: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no; why: KXNHLAST-26OCT09NYRWSH-WSHATUCH89-1|no has the higher standalone adjusted growth (2.81 vs 1.50 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.055); relationships: KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.221); KXNHLAST-26OCT09NYRWSH-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: WSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4086): highest fidelity KXNHLAST-26OCT09NYRWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.3412): highest fidelity KXNHLAST-26OCT09NYRWSH-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT09NYRWSH-NYRGPERREAULT94-1|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.4371): highest fidelity KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT09NYRWSH-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT09NYRWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3775, phi -0.244)
- KXNHLAST-26OCT09NYRWSH-NYRGPERREAULT94-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4371, phi -0.266)
- KXNHLGOAL-26OCT09NYRWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3775, phi -0.166)
- KXNHLAST-26OCT09NYRWSH-WSHJKYROU25-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.4 pts; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4086, phi -0.175)

portfolios: A EV +10.31 (adj +3.73) on $37.50, P(profit) 0.6413, adj growth 31.6 bp · B EV +8.90 (adj +4.26) on $43.07, P(profit) 0.5304, adj growth 37.0 bp · C EV +7.79 (adj +3.88) on $50.00, P(profit) 0.3917, adj growth 34.3 bp · R EV +1.37 (adj +0.95) on $4.00, P(profit) 0.2417, adj growth 30.9 bp

## PIT @ CBJ  ·  10000 joint draws  ·  458 bet sides mapped, 13 +EV candidates, 4 on card

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
| Danton Heinen: 1+ goals YES | 10 | 0.141 | 0.130 | +0.035 | +0.024 | $6.00 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 11 | 0.146 | 0.136 | +0.030 | +0.019 | $4.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 16 | 0.203 | 0.191 | +0.033 | +0.021 | $6.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ assists YES | 32 | 0.383 | 0.349 | +0.048 | +0.014 | $4.95 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (12.51 vs 6.97 bp); relationships: KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT09PITCBJ-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: CBJ offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09PITCBJ-PITECHINAKHOV59-1|yes; why: higher confidence-adjusted growth (7.74 vs 4.68 bp); despite a smaller raw edge (+0.030 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT09PITCBJ-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.031); failure: PIT offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (6.97 vs 1.91 bp); relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT09PITCBJ-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: CBJ offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ assists YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes; why: Player prop expression KXNHLAST-26OCT09PITCBJ-PITRRAKELL67-1|yes selected over player prop KXNHLAST-26OCT09PITCBJ-PITECHINAKHOV59-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.55 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.031); KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.3934): highest fidelity KXNHLAST-26OCT09PITCBJ-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT09PITCBJ-PITECHINAKHOV59-1|yes — Player prop expression KXNHLAST-26OCT09PITCBJ-PITRRAKELL67-1|yes selected over player prop KXNHLAST-26OCT09PITCBJ-PITECHINAKHOV59-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.55 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CBJ:OFFENSE_4PLUS (p 0.4377): highest fidelity KXNHLAST-26OCT09PITCBJ-CBJDMATEYCHUK5-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:SUPPRESSED (p 0.3426): highest fidelity KXNHLAST-26OCT09PITCBJ-CBJMKNIES23-1|no [DIRECT], best adjusted EV KXNHLPTS-26OCT09PITCBJ-CBJMKNIES23-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT09PITCBJ-CBJDHEINEN58-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3426, phi -0.148)
- KXNHLGOAL-26OCT09PITCBJ-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3934, phi -0.201)
- KXNHLGOAL-26OCT09PITCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3426, phi -0.214)
- KXNHLAST-26OCT09PITCBJ-PITRRAKELL67-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 45% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3934, phi -0.289)
- override: Player prop expression KXNHLAST-26OCT09PITCBJ-PITRRAKELL67-1|yes selected over player prop KXNHLAST-26OCT09PITCBJ-PITECHINAKHOV59-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.55 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +6.93 (adj +1.06) on $37.50, P(profit) 0.615, adj growth 8.7 bp · B EV +5.15 (adj +3.12) on $22.01, P(profit) 0.4156, adj growth 26.9 bp · C EV +5.80 (adj +2.08) on $26.85, P(profit) 0.5551, adj growth 18.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## ANA @ WPG  ·  10000 joint draws  ·  484 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.526 / away 0.474

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
| A.J. Greer: 1+ goals YES | 15 | 0.234 | 0.212 | +0.075 | +0.053 | $14.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Neal Pionk: 1+ goals NO | 86 | 0.926 | 0.908 | +0.058 | +0.040 | $20.00 | FUNDED_RESEARCH | $5 | WPG:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 7 | 0.109 | 0.097 | +0.035 | +0.022 | $5.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 8 | 0.113 | 0.102 | +0.028 | +0.017 | $4.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT09ANAWPG-ANARPOEHLING25-1|yes; why: higher confidence-adjusted growth (44.65 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT09ANAWPG-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: ANA offense suppressed (<= 2 goals)
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT09ANAWPG-WPGNPIONK4-1|no; why: higher confidence-adjusted growth (31.34 vs 0.61 bp); despite a smaller raw edge (+0.058 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT09ANAWPG-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: WPG offense succeeds (4+ goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes has the higher standalone adjusted growth (44.65 vs 15.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT09ANAWPG-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: ANA offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes has the higher standalone adjusted growth (44.65 vs 7.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3873): highest fidelity KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes (same contract)
- thesis ANA:SUPPRESSED (p 0.3956): highest fidelity KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT09ANAWPG-ANACGAUTHIER61-1|no (same contract)
- thesis WPG:SUPPRESSED (p 0.3723): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT09ANAWPG-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3956, phi -0.235)
- KXNHLGOAL-26OCT09ANAWPG-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.4129, phi -0.131)
- KXNHLGOAL-26OCT09ANAWPG-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3956, phi -0.158)
- KXNHLGOAL-26OCT09ANAWPG-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3956, phi -0.143)

portfolios: A EV +8.94 (adj +6.08) on $37.50, P(profit) 0.3162, adj growth 54.0 bp · B EV +11.73 (adj +7.98) on $43.36, P(profit) 0.3943, adj growth 69.2 bp · C EV +7.96 (adj +5.50) on $31.54, P(profit) 0.2343, adj growth 47.1 bp · R EV +0.33 (adj +0.23) on $5.00, P(profit) 0.926, adj growth 9.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
