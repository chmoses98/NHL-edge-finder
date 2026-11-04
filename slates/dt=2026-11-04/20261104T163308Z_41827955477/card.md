# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-04T16:33:08Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +30.96 | +14.51 | +22.93 | 0.641 | -52.60 | -68.69 | 121.15 |
| B thesis-diversified (joint) ← optimiser card | 125.42 | +28.36 | +17.60 | +21.35 | 0.638 | -52.98 | -72.24 | 152.80 |
| C best expression per thesis | 83.29 | +16.40 | +7.54 | +12.65 | 0.614 | -36.43 | -49.03 | 66.06 |
| R FUNDED research stakes | 16.00 | +3.26 | +2.14 | -1.86 | 0.334 | -9.84 | -9.84 | 0.00 |

## OTT @ BUF  ·  10000 joint draws  ·  406 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_OTT_win | p_overtime | goals | shots BUF/OTT | BUF/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.55 | 0.45 | 0.00 | 6.01 | 27.4/27.2 | 23.9/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.52 | 0.48 | 0.46 | 6.02 | 27.5/27.5 | 24.0/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.56 | 0.44 | 0.00 | 9.42 | 29.2/29.3 | 23.5/22.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.071 | 0.62 | 0.38 | 0.00 | 5.99 | 32.0/21.8 | 19.0/27.6 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.064 | 0.50 | 0.50 | 0.00 | 6.06 | 22.1/32.2 | 28.6/18.6 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.58 | 0.42 | 0.44 | 5.97 | 32.2/21.8 | 18.7/28.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ridly Greig: 1+ goals YES | 15 | 0.207 | 0.190 | +0.048 | +0.031 | $8.51 | FUNDED_RESEARCH | $3 | OTT:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 25 | 0.298 | 0.284 | +0.035 | +0.021 | $7.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Stephen Halliday: 1+ goals YES | 15 | 0.185 | 0.175 | +0.026 | +0.016 | $4.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Claude Giroux: 1+ goals YES | 16 | 0.199 | 0.186 | +0.030 | +0.016 | $4.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTSHALLIDAY34-1|yes; why: higher confidence-adjusted growth (15.61 vs 4.34 bp); relationships: KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV04OTTBUF-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: OTT offense suppressed (<= 2 goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV04OTTBUF-BUFJDOAN91-1|yes; why: higher confidence-adjusted growth (4.72 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV04OTTBUF-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.03); failure: BUF offense suppressed (<= 2 goals)
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes has the higher standalone adjusted growth (15.61 vs 4.34 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: OTT offense suppressed (<= 2 goals)
- **Claude Giroux: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes has the higher standalone adjusted growth (15.61 vs 4.10 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26NOV04OTTBUF-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis OTT:OFFENSE_4PLUS (p 0.3924): highest fidelity KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.4409): highest fidelity KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3947): highest fidelity KXNHLAST-26NOV04OTTBUF-OTTTCHABOT72-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04OTTBUF-OTTTCHABOT72-1|no (same contract)
- KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3947, phi -0.22)
- KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3393, phi -0.252)
- KXNHLGOAL-26NOV04OTTBUF-OTTSHALLIDAY34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3947, phi -0.213)
- KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3947, phi -0.205)

portfolios: A EV +6.33 (adj +3.51) on $38.97, P(profit) 0.4792, adj growth 29.6 bp · B EV +5.07 (adj +3.13) on $24.70, P(profit) 0.6402, adj growth 27.1 bp · C EV +4.52 (adj +2.50) on $28.46, P(profit) 0.389, adj growth 21.6 bp · R EV +0.90 (adj +0.59) on $3.00, P(profit) 0.2068, adj growth 19.0 bp

## CHI @ FLA  ·  10000 joint draws  ·  406 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_CHI_win | p_overtime | goals | shots FLA/CHI | FLA/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.143 | 0.73 | 0.27 | 0.00 | 6.0 | 32.7/20.8 | 18.4/27.9 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.58 | 0.42 | 0.45 | 5.88 | 32.8/21.0 | 18.0/29.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.68 | 0.32 | 0.00 | 6.05 | 27.2/26.3 | 23.5/22.9 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.099 | 0.72 | 0.28 | 0.00 | 9.25 | 34.4/22.3 | 18.0/26.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.51 | 0.49 | 0.46 | 6.0 | 27.0/26.5 | 23.1/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.65 | 0.35 | 0.00 | 9.36 | 29.0/28.1 | 22.8/21.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 20 | 0.273 | 0.253 | +0.062 | +0.041 | $11.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 61 | 0.696 | 0.673 | +0.069 | +0.046 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 11 | 0.159 | 0.143 | +0.042 | +0.026 | $6.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.133 | 0.119 | +0.038 | +0.023 | $5.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes; why: higher confidence-adjusted growth (22.08 vs 14.33 bp); relationships: KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CHI offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (20.23 vs 11.39 bp); relationships: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: FLA offense succeeds (4+ goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (22.08 vs 14.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CHI offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CHIFLA-FLASBENNETT9-1|yes; why: higher confidence-adjusted growth (13.11 vs 0.16 bp); alternative not eligible: confidence-adjusted EV +0.0040 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.14, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3169): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.2938): highest fidelity KXNHLPTS-26NOV04CHIFLA-FLASREINHART13-2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.3774): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4675, phi -0.277)
- KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.5025, phi -0.236)
- KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4675, phi -0.206)
- KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.2938, phi -0.155)

portfolios: A EV +6.63 (adj +3.12) on $38.97, P(profit) 0.4895, adj growth 27.4 bp · B EV +10.32 (adj +6.65) on $44.16, P(profit) 0.4706, adj growth 58.1 bp · C EV +6.65 (adj +4.11) on $34.07, P(profit) 0.3338, adj growth 36.4 bp · R EV +0.55 (adj +0.37) on $5.00, P(profit) 0.6957, adj growth 13.7 bp

## SJS @ LAK  ·  10000 joint draws  ·  378 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_SJS_win | p_overtime | goals | shots LAK/SJS | LAK/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.60 | 0.40 | 0.00 | 5.97 | 27.9/27.6 | 24.5/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.46 | 5.91 | 28.1/27.6 | 24.3/24.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.104 | 0.67 | 0.33 | 0.00 | 5.99 | 33.5/22.2 | 19.6/28.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.57 | 0.43 | 0.46 | 5.86 | 33.5/22.1 | 18.9/30.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.60 | 0.40 | 0.00 | 9.29 | 29.6/29.0 | 23.6/23.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.61 | 0.39 | 0.00 | 3.44 | 26.3/26.2 | 24.7/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 6 | 0.091 | 0.083 | +0.027 | +0.019 | $4.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ goals NO | 80 | 0.856 | 0.841 | +0.044 | +0.029 | $20.00 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Drew Doughty: 1+ assists YES | 28 | 0.362 | 0.316 | +0.068 | +0.022 | $6.01 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Andre Lee: 1+ goals YES | 11 | 0.153 | 0.131 | +0.036 | +0.014 | $3.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes; why: higher confidence-adjusted growth (12.78 vs 5.02 bp); despite a smaller raw edge (+0.027 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: LAK offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (12.40 vs 2.06 bp); despite a smaller raw edge (+0.044 vs +0.114/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV04SJLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: SJS offense succeeds (4+ goals)
- **Drew Doughty: 1+ assists YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes; why: higher confidence-adjusted growth (5.02 vs 0.38 bp); despite a smaller raw edge (+0.068 vs +0.071/contract); alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04SJLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.07); failure: LAK offense suppressed (<= 2 goals)
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes has the higher standalone adjusted growth (5.02 vs 4.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.070); they share one thesis budget; relationships: KXNHLGOAL-26NOV04SJLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes: MOSTLY_INDEPENDENT (phi 0.07); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis LAK:OFFENSE_4PLUS (p 0.4234): highest fidelity KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.4758): highest fidelity KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no (same contract)
- thesis LAK:SUPPRESSED (p 0.3591): highest fidelity KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no (same contract)
- KXNHLGOAL-26NOV04SJLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3591, phi -0.13)
- KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3081, phi -0.178)
- KXNHLAST-26NOV04SJLA-LADDOUGHTY8-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3591, phi -0.264)
- KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3591, phi -0.16)

portfolios: A EV +8.07 (adj +1.62) on $38.97, P(profit) 0.5919, adj growth 13.8 bp · B EV +5.29 (adj +2.85) on $33.57, P(profit) 0.4402, adj growth 25.1 bp · C EV +5.23 (adj +0.93) on $20.76, P(profit) 0.6041, adj growth 8.1 bp · R EV +0.27 (adj +0.18) on $5.00, P(profit) 0.8556, adj growth 6.8 bp

## CGY @ SEA  ·  10000 joint draws  ·  434 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CGY_win | p_overtime | goals | shots SEA/CGY | SEA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.66 | 0.34 | 0.00 | 6.07 | 28.2/28.4 | 25.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.55 | 0.45 | 0.48 | 5.98 | 28.3/28.4 | 25.1/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.65 | 0.35 | 0.00 | 9.38 | 30.1/30.2 | 24.9/23.2 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.070 | 0.57 | 0.43 | 0.00 | 5.98 | 22.8/33.6 | 30.3/19.1 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.066 | 0.69 | 0.31 | 0.00 | 6.05 | 33.3/22.7 | 20.0/28.3 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.51 | 0.49 | 0.42 | 5.88 | 22.6/33.5 | 30.2/19.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 10 | 0.161 | 0.142 | +0.054 | +0.035 | $8.55 | FUNDED_RESEARCH | $3 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 18 | 0.232 | 0.216 | +0.041 | +0.026 | $7.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Jake Middleton: 1+ goals YES | 4 | 0.059 | 0.054 | +0.017 | +0.012 | $2.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Kaapo Kakko: 1+ goals YES | 17 | 0.207 | 0.195 | +0.027 | +0.015 | $4.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (27.90 vs 0.71 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV04CGYSEA-CGYJMIDDLETON55-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (9.44 vs 0.71 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV04CGYSEA-CGYJMIDDLETON55-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: SEA offense suppressed (<= 2 goals)
- **Jake Middleton: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV04CGYSEA-7|yes; why: higher confidence-adjusted growth (7.21 vs 0.00 bp); despite a smaller raw edge (+0.017 vs +0.022/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.875 vs 0.672); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CGY offense suppressed (<= 2 goals)
- **Kaapo Kakko: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (3.34 vs 0.71 bp); despite a smaller raw edge (+0.027 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV04CGYSEA-CGYJMIDDLETON55-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4747): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis CGY:OFFENSE_4PLUS (p 0.3364): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3069, phi -0.177)
- KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3069, phi -0.18)
- KXNHLGOAL-26NOV04CGYSEA-CGYJMIDDLETON55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4515, phi -0.123)
- KXNHLGOAL-26NOV04CGYSEA-SEAKKAKKO84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3069, phi -0.163)

portfolios: A EV +9.94 (adj +6.26) on $33.09, P(profit) 0.5711, adj growth 50.3 bp · B EV +7.67 (adj +4.97) on $22.99, P(profit) 0.5192, adj growth 42.5 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +1.53 (adj +1.00) on $3.00, P(profit) 0.1606, adj growth 31.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
