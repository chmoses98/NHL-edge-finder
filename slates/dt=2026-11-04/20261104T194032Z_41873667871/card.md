# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-04T19:40:32Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +35.01 | +16.13 | +26.48 | 0.644 | -60.48 | -78.13 | 132.87 |
| B thesis-diversified (joint) ← optimiser card | 133.05 | +32.32 | +20.05 | +23.20 | 0.629 | -55.26 | -77.52 | 172.41 |
| C best expression per thesis | 103.70 | +19.95 | +8.25 | +19.30 | 0.684 | -34.48 | -49.86 | 73.08 |
| R FUNDED research stakes | 16.00 | +3.18 | +2.16 | -1.86 | 0.326 | -9.84 | -9.84 | 0.00 |

## OTT @ BUF  ·  10000 joint draws  ·  482 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.535 / away 0.465

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_OTT_win | p_overtime | goals | shots BUF/OTT | BUF/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 6.09 | 27.5/27.4 | 24.0/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.54 | 0.46 | 0.47 | 5.96 | 27.5/27.6 | 24.3/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.57 | 0.43 | 0.00 | 9.4 | 28.9/28.8 | 23.0/22.3 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.071 | 0.61 | 0.39 | 0.00 | 6.02 | 32.1/21.9 | 19.0/28.1 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.53 | 0.47 | 0.47 | 5.94 | 32.2/21.5 | 18.3/29.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.064 | 0.49 | 0.51 | 0.00 | 6.02 | 22.0/32.6 | 29.1/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Claude Giroux: 1+ goals YES | 15 | 0.203 | 0.189 | +0.044 | +0.030 | $8.21 | FUNDED_RESEARCH | $3 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ridly Greig: 1+ goals YES | 16 | 0.203 | 0.189 | +0.034 | +0.019 | $5.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Stephen Halliday: 1+ goals YES | 15 | 0.183 | 0.173 | +0.024 | +0.014 | $4.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 15 | 0.184 | 0.173 | +0.025 | +0.014 | $3.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Claude Giroux: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (14.06 vs 5.61 bp); relationships: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04OTTBUF-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: OTT offense suppressed (<= 2 goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (5.61 vs 3.18 bp); relationships: KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04OTTBUF-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: OTT offense suppressed (<= 2 goals)
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes has the higher standalone adjusted growth (5.61 vs 3.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes has the higher standalone adjusted growth (5.61 vs 3.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV04OTTBUF-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.3873): highest fidelity KXNHLGOAL-26NOV04OTTBUF-OTTFZETTERLUND20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:OFFENSE_4PLUS (p 0.4511): highest fidelity KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes (same contract)
- KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3917, phi -0.206)
- KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3917, phi -0.206)
- KXNHLGOAL-26NOV04OTTBUF-OTTSHALLIDAY34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3917, phi -0.18)
- KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3917, phi -0.206)

portfolios: A EV +6.34 (adj +3.84) on $32.64, P(profit) 0.4819, adj growth 31.4 bp · B EV +4.57 (adj +2.85) on $21.61, P(profit) 0.5764, adj growth 24.6 bp · C EV +1.70 (adj +0.94) on $10.86, P(profit) 0.4461, adj growth 8.1 bp · R EV +0.83 (adj +0.56) on $3.00, P(profit) 0.203, adj growth 17.8 bp

## CHI @ FLA  ·  10000 joint draws  ·  438 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.685 / away 0.315

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_CHI_win | p_overtime | goals | shots FLA/CHI | FLA/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.138 | 0.70 | 0.30 | 0.00 | 6.02 | 32.6/20.9 | 18.3/27.8 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.56 | 0.44 | 0.44 | 5.91 | 32.8/20.9 | 17.7/29.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.66 | 0.34 | 0.00 | 6.06 | 27.1/26.2 | 23.2/22.8 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.099 | 0.72 | 0.28 | 0.00 | 9.33 | 34.4/22.4 | 17.9/25.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.48 | 0.52 | 0.46 | 5.94 | 27.3/26.5 | 23.3/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.67 | 0.33 | 0.00 | 9.39 | 28.7/28.0 | 22.6/21.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 61 | 0.702 | 0.677 | +0.075 | +0.051 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 11 | 0.158 | 0.143 | +0.041 | +0.026 | $6.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.270 | 0.254 | +0.048 | +0.032 | $9.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.127 | 0.115 | +0.031 | +0.019 | $4.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (24.22 vs 13.36 bp); relationships: KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: FLA offense succeeds (4+ goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (14.38 vs 12.88 bp); despite a smaller raw edge (+0.041 vs +0.048/contract); relationships: KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes; why: higher confidence-adjusted growth (12.88 vs 5.81 bp); despite a smaller raw edge (+0.048 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.909 vs 0.792); relationships: KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV04CHIFLA-7|yes; why: higher confidence-adjusted growth (9.14 vs 0.02 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.805 vs 0.678); alternative not eligible: confidence-adjusted EV +0.0016 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.14, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis FLA:SUPPRESSED (p 0.3122): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.3176): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS_BY_2PLUS (p 0.1913): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4856, phi -0.247)
- KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4697, phi -0.184)
- KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4697, phi -0.251)
- KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3122, phi -0.157)

portfolios: A EV +5.65 (adj +1.38) on $39.37, P(profit) 0.676, adj growth 12.1 bp · B EV +8.36 (adj +5.48) on $41.11, P(profit) 0.4638, adj growth 48.3 bp · C EV +7.56 (adj +3.93) on $50.00, P(profit) 0.6888, adj growth 35.5 bp · R EV +0.60 (adj +0.40) on $5.00, P(profit) 0.7015, adj growth 15.1 bp

## SJS @ LAK  ·  10000 joint draws  ·  456 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.600 / away 0.400

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_SJS_win | p_overtime | goals | shots LAK/SJS | LAK/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.62 | 0.38 | 0.00 | 5.98 | 27.9/27.5 | 24.5/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.47 | 5.91 | 28.0/27.8 | 24.6/24.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.109 | 0.68 | 0.32 | 0.00 | 6.0 | 33.3/22.1 | 19.4/28.6 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.58 | 0.42 | 0.51 | 5.82 | 33.2/22.3 | 19.1/29.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.62 | 0.38 | 0.00 | 9.21 | 29.3/28.8 | 23.4/22.5 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.064 | 0.72 | 0.28 | 0.00 | 9.14 | 34.7/22.9 | 18.4/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Andre Lee: 1+ goals YES | 11 | 0.152 | 0.139 | +0.035 | +0.022 | $5.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ goals NO | 80 | 0.850 | 0.836 | +0.039 | +0.025 | $19.15 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Trevor Moore: 1+ assists YES | 28 | 0.365 | 0.320 | +0.071 | +0.026 | $8.08 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Macklin Celebrini: 1+ assists NO | 47 | 0.612 | 0.513 | +0.124 | +0.026 | $10.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.77) | EVIDENCE_MIXED | D |
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes; why: higher confidence-adjusted growth (10.34 vs 7.02 bp); despite a smaller raw edge (+0.035 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi 0.03); KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: LAK offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (8.96 vs 5.76 bp); despite a smaller raw edge (+0.039 vs +0.124/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.126); failure: SJS offense succeeds (4+ goals)
- **Trevor Moore: 1+ assists YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes; why: higher confidence-adjusted growth (7.02 vs 5.76 bp); despite a smaller raw edge (+0.071 vs +0.071/contract); relationships: KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.03); KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: LAK offense suppressed (<= 2 goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMMARCHMENT27-1|no; why: higher confidence-adjusted growth (5.76 vs 0.59 bp); alternative not eligible: confidence-adjusted EV +0.0076 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.126); KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis LAK:OFFENSE_4PLUS (p 0.4321): highest fidelity KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.4784): highest fidelity KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no (same contract)
- thesis LAK:SUPPRESSED (p 0.359): highest fidelity KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no (same contract)
- KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.359, phi -0.166)
- KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3045, phi -0.167)
- KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.359, phi -0.263)
- KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 23% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.2 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3045, phi -0.289)

portfolios: A EV +10.32 (adj +2.57) on $39.37, P(profit) 0.6646, adj growth 22.0 bp · B EV +7.30 (adj +2.93) on $43.63, P(profit) 0.7258, adj growth 25.8 bp · C EV +8.05 (adj +1.79) on $30.12, P(profit) 0.5329, adj growth 15.6 bp · R EV +0.24 (adj +0.15) on $5.00, P(profit) 0.8498, adj growth 5.7 bp

## CGY @ SEA  ·  10000 joint draws  ·  444 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.548 / away 0.452

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CGY_win | p_overtime | goals | shots SEA/CGY | SEA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.135 | 0.63 | 0.37 | 0.00 | 6.05 | 28.5/28.4 | 25.5/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.49 | 5.96 | 28.5/28.6 | 25.3/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.65 | 0.35 | 0.00 | 9.45 | 29.8/29.9 | 24.8/22.4 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.067 | 0.69 | 0.31 | 0.00 | 6.01 | 33.3/22.7 | 20.0/28.8 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.067 | 0.58 | 0.42 | 0.00 | 6.01 | 22.9/33.9 | 30.6/19.0 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.52 | 0.48 | 0.47 | 5.96 | 22.8/34.2 | 30.8/19.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 10 | 0.160 | 0.144 | +0.053 | +0.037 | $9.00 | FUNDED_RESEARCH | $3 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Zach Whitecloud: 1+ goals YES | 2 | 0.042 | 0.039 | +0.021 | +0.018 | $3.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.07) | EVIDENCE_STRONGER | D |
| Jani Nyman: 1+ goals YES | 11 | 0.157 | 0.143 | +0.040 | +0.026 | $6.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 18 | 0.231 | 0.216 | +0.041 | +0.025 | $7.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes; why: higher confidence-adjusted growth (30.92 vs 8.96 bp); relationships: KXNHLGOAL-26NOV04CGYSEA-CGYZWHITECLOUD28-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)
- **Zach Whitecloud: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV04CGYSEA-7|yes; why: higher confidence-adjusted growth (29.99 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.86 vs 0.679); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: CGY offense suppressed (<= 2 goals)
- **Jani Nyman: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes; why: higher confidence-adjusted growth (13.74 vs 8.96 bp); despite a smaller raw edge (+0.040 vs +0.041/contract); relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV04CGYSEA-CGYZWHITECLOUD28-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CGYSEA-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (8.96 vs 5.87 bp); relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV04CGYSEA-CGYZWHITECLOUD28-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4721): highest fidelity KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.3713): highest fidelity KXNHLGOAL-26NOV04CGYSEA-SEAFGAUDREAU89-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04CGYSEA-SEAFGAUDREAU89-1|yes (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.335): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.321, phi -0.173)
- KXNHLGOAL-26NOV04CGYSEA-CGYZWHITECLOUD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 93% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4481, phi -0.091)
- KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.321, phi -0.159)
- KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.321, phi -0.194)

portfolios: A EV +12.70 (adj +8.34) on $38.63, P(profit) 0.5648, adj growth 67.4 bp · B EV +12.09 (adj +8.79) on $26.70, P(profit) 0.4783, adj growth 73.7 bp · C EV +2.65 (adj +1.59) on $12.72, P(profit) 0.3856, adj growth 13.8 bp · R EV +1.51 (adj +1.05) on $3.00, P(profit) 0.1598, adj growth 33.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
