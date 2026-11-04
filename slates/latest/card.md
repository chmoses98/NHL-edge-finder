# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-04T20:30:16Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +33.35 | +13.99 | +22.45 | 0.628 | -56.94 | -74.98 | 112.35 |
| B thesis-diversified (joint) ← optimiser card | 117.26 | +27.43 | +15.19 | +21.78 | 0.639 | -50.48 | -66.50 | 131.43 |
| C best expression per thesis | 100.20 | +18.45 | +7.25 | +16.76 | 0.674 | -34.25 | -49.64 | 63.90 |
| R FUNDED research stakes | 10.00 | +2.58 | +1.71 | -1.89 | 0.288 | -10.00 | -10.00 | 0.00 |

## OTT @ BUF  ·  10000 joint draws  ·  482 bet sides mapped, 4 +EV candidates, 4 on card

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
| Zach Benson: 1+ goals YES | 26 | 0.305 | 0.291 | +0.031 | +0.018 | $5.94 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Stephen Halliday: 1+ goals YES | 15 | 0.183 | 0.173 | +0.024 | +0.014 | $4.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 15 | 0.184 | 0.170 | +0.025 | +0.011 | $3.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Claude Giroux: 1+ goals YES | 17 | 0.203 | 0.191 | +0.023 | +0.011 | $3.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV04OTTBUF-BUFJDOAN91-1|yes; why: higher confidence-adjusted growth (3.44 vs 0.00 bp); despite a smaller raw edge (+0.031 vs +0.037/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: BUF offense suppressed (<= 2 goals)
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (3.38 vs 2.15 bp); despite a smaller raw edge (+0.024 vs +0.025/contract); relationships: KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (2.15 vs 0.55 bp); alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV04OTTBUF-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: OTT offense suppressed (<= 2 goals)
- **Claude Giroux: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (2.15 vs 1.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV04OTTBUF-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis BUF:OFFENSE_4PLUS (p 0.4511): highest fidelity KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.3873): highest fidelity KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes (same contract)
- KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3397, phi -0.25)
- KXNHLGOAL-26NOV04OTTBUF-OTTSHALLIDAY34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3917, phi -0.18)
- KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3917, phi -0.206)
- KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3917, phi -0.206)

portfolios: A EV +3.68 (adj +1.95) on $27.23, P(profit) 0.6341, adj growth 15.3 bp · B EV +2.24 (adj +1.20) on $16.63, P(profit) 0.6341, adj growth 10.4 bp · C EV +1.17 (adj +0.61) on $9.05, P(profit) 0.4316, adj growth 5.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ FLA  ·  10000 joint draws  ·  438 bet sides mapped, 17 +EV candidates, 4 on card

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
| Oliver Moore: 1+ goals YES | 11 | 0.158 | 0.144 | +0.041 | +0.028 | $7.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 60 | 0.675 | 0.655 | +0.058 | +0.038 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.270 | 0.254 | +0.048 | +0.032 | $9.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.127 | 0.115 | +0.031 | +0.019 | $4.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (15.76 vs 12.88 bp); despite a smaller raw edge (+0.041 vs +0.048/contract); relationships: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: CHI offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV04CHIFLA-FLA2|no; why: higher confidence-adjusted growth (13.36 vs 3.90 bp); despite a smaller raw edge (+0.058 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.022 vs 0.894); relationships: KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes; why: higher confidence-adjusted growth (12.88 vs 5.81 bp); despite a smaller raw edge (+0.048 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.909 vs 0.792); relationships: KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV04CHIFLA-7|yes; why: higher confidence-adjusted growth (9.14 vs 0.02 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.805 vs 0.678); alternative not eligible: confidence-adjusted EV +0.0016 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.14, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis FLA:SUPPRESSED (p 0.3122): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.3176): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS_BY_2PLUS (p 0.1913): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4697, phi -0.184)
- KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4856, phi -0.231)
- KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4697, phi -0.251)
- KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3122, phi -0.157)

portfolios: A EV +6.01 (adj +1.03) on $42.04, P(profit) 0.6218, adj growth 8.1 bp · B EV +8.04 (adj +5.29) on $41.73, P(profit) 0.4638, adj growth 46.1 bp · C EV +7.09 (adj +3.58) on $50.00, P(profit) 0.6785, adj growth 31.9 bp · R EV +0.47 (adj +0.31) on $5.00, P(profit) 0.6746, adj growth 11.1 bp

## SJS @ LAK  ·  10000 joint draws  ·  456 bet sides mapped, 10 +EV candidates, 4 on card

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
| Andre Lee: 1+ goals YES | 11 | 0.152 | 0.139 | +0.035 | +0.022 | $5.36 | FUNDED_RESEARCH | $2 | LAK:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Drew Doughty: 1+ assists YES | 28 | 0.365 | 0.320 | +0.071 | +0.026 | $7.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Trevor Moore: 1+ assists YES | 28 | 0.365 | 0.320 | +0.071 | +0.026 | $7.47 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Macklin Celebrini: 1+ assists NO | 47 | 0.612 | 0.513 | +0.124 | +0.026 | $12.81 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.77) | EVIDENCE_MIXED | D |
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes; why: higher confidence-adjusted growth (10.34 vs 7.05 bp); despite a smaller raw edge (+0.035 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes: MOSTLY_INDEPENDENT (phi 0.059); KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi 0.03); KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: LAK offense suppressed (<= 2 goals)
- **Drew Doughty: 1+ assists YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes; why: higher confidence-adjusted growth (7.05 vs 7.02 bp); relationships: KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.059); KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi 0.089); KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: LAK offense suppressed (<= 2 goals)
- **Trevor Moore: 1+ assists YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes has the higher standalone adjusted growth (7.05 vs 7.02 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.089); they share one thesis budget; relationships: KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.03); KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes: MOSTLY_INDEPENDENT (phi 0.089); KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: LAK offense suppressed (<= 2 goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMMARCHMENT27-1|no; why: higher confidence-adjusted growth (5.76 vs 2.22 bp); relationships: KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis LAK:OFFENSE_4PLUS (p 0.4321): highest fidelity KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.4784): highest fidelity KXNHLAST-26NOV04SJLA-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.359): highest fidelity KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no (same contract)
- KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.359, phi -0.166)
- KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.359, phi -0.283)
- KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.359, phi -0.263)
- KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 23% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.2 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3045, phi -0.289)

portfolios: A EV +11.03 (adj +2.83) on $42.04, P(profit) 0.6646, adj growth 24.1 bp · B EV +8.46 (adj +3.00) on $32.97, P(profit) 0.4899, adj growth 26.1 bp · C EV +8.16 (adj +1.82) on $30.53, P(profit) 0.5411, adj growth 15.9 bp · R EV +0.60 (adj +0.38) on $2.00, P(profit) 0.1522, adj growth 12.3 bp

## CGY @ SEA  ·  10000 joint draws  ·  444 bet sides mapped, 5 +EV candidates, 4 on card

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
| Ben Meyers: 1+ goals YES | 10 | 0.160 | 0.142 | +0.053 | +0.036 | $8.75 | FUNDED_RESEARCH | $3 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jani Nyman: 1+ goals YES | 11 | 0.157 | 0.143 | +0.040 | +0.026 | $6.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 18 | 0.231 | 0.217 | +0.041 | +0.026 | $7.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 13 | 0.158 | 0.148 | +0.020 | +0.010 | $2.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes; why: higher confidence-adjusted growth (28.92 vs 9.86 bp); relationships: KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: SEA offense suppressed (<= 2 goals)
- **Jani Nyman: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes; why: higher confidence-adjusted growth (13.74 vs 9.86 bp); despite a smaller raw edge (+0.040 vs +0.041/contract); relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CGYSEA-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (9.86 vs 1.57 bp); relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV04CGYSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: SEA offense suppressed (<= 2 goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes has the higher standalone adjusted growth (9.86 vs 1.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4721): highest fidelity KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.3713): highest fidelity KXNHLGOAL-26NOV04CGYSEA-SEAFGAUDREAU89-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04CGYSEA-SEAFGAUDREAU89-1|yes (same contract)
- KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.321, phi -0.173)
- KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.321, phi -0.159)
- KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.321, phi -0.194)
- KXNHLGOAL-26NOV04CGYSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.321, phi -0.164)

portfolios: A EV +12.62 (adj +8.18) on $38.68, P(profit) 0.4561, adj growth 64.9 bp · B EV +8.70 (adj +5.70) on $25.93, P(profit) 0.4561, adj growth 48.9 bp · C EV +2.02 (adj +1.24) on $10.62, P(profit) 0.3856, adj growth 10.8 bp · R EV +1.51 (adj +1.02) on $3.00, P(profit) 0.1598, adj growth 32.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
