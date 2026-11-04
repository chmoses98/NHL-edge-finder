# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-04T21:20:52Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +34.99 | +15.79 | +19.80 | 0.599 | -58.76 | -76.85 | 123.66 |
| B thesis-diversified (joint) ← optimiser card | 114.18 | +24.70 | +13.99 | +17.53 | 0.613 | -46.94 | -61.86 | 121.00 |
| C best expression per thesis | 76.74 | +12.70 | +4.97 | +13.68 | 0.641 | -29.91 | -41.53 | 44.03 |
| R FUNDED research stakes | 15.00 | +2.74 | +1.83 | -0.73 | 0.340 | -8.84 | -8.84 | 0.00 |

## OTT @ BUF  ·  10000 joint draws  ·  482 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.533 / away 0.467

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
| Zach Benson: 1+ goals YES | 26 | 0.305 | 0.292 | +0.031 | +0.019 | $6.38 | FUNDED_RESEARCH | $2 | BUF:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 15 | 0.184 | 0.173 | +0.025 | +0.014 | $3.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Claude Giroux: 1+ goals YES | 17 | 0.203 | 0.191 | +0.023 | +0.011 | $3.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV04OTTBUF-BUFJDOAN91-1|yes; why: higher confidence-adjusted growth (3.94 vs 0.00 bp); despite a smaller raw edge (+0.031 vs +0.037/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: BUF offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (3.18 vs 1.44 bp); alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: OTT offense suppressed (<= 2 goals)
- **Claude Giroux: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (3.18 vs 1.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis BUF:OFFENSE_4PLUS (p 0.4511): highest fidelity KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.3873): highest fidelity KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes (same contract)
- KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3397, phi -0.25)
- KXNHLGOAL-26NOV04OTTBUF-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3917, phi -0.206)
- KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3917, phi -0.206)

portfolios: A EV +2.97 (adj +1.65) on $22.64, P(profit) 0.5513, adj growth 12.9 bp · B EV +1.79 (adj +1.00) on $13.69, P(profit) 0.5513, adj growth 8.7 bp · C EV +1.34 (adj +0.78) on $10.22, P(profit) 0.4316, adj growth 6.8 bp · R EV +0.23 (adj +0.14) on $2.00, P(profit) 0.3049, adj growth 4.6 bp

## CHI @ FLA  ·  10000 joint draws  ·  438 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.687 / away 0.313

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
| Brady Tkachuk: 1+ goals NO | 60 | 0.675 | 0.655 | +0.058 | +0.038 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 11 | 0.158 | 0.142 | +0.041 | +0.025 | $6.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.270 | 0.254 | +0.048 | +0.032 | $9.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.127 | 0.112 | +0.031 | +0.017 | $4.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV04CHIFLA-FLA2|no; why: higher confidence-adjusted growth (13.36 vs 3.90 bp); despite a smaller raw edge (+0.058 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.022 vs 0.894); relationships: KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense succeeds (4+ goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (13.07 vs 12.88 bp); despite a smaller raw edge (+0.041 vs +0.048/contract); relationships: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes; why: higher confidence-adjusted growth (12.88 vs 5.81 bp); despite a smaller raw edge (+0.048 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.909 vs 0.792); relationships: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV04CHIFLA-7|yes; why: higher confidence-adjusted growth (6.93 vs 0.02 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.805 vs 0.678); alternative not eligible: confidence-adjusted EV +0.0016 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.14, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis FLA:SUPPRESSED (p 0.3122): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.3176): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS_BY_2PLUS (p 0.1913): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4856, phi -0.231)
- KXNHLGOAL-26NOV04CHIFLA-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4697, phi -0.184)
- KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4697, phi -0.251)
- KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3122, phi -0.157)

portfolios: A EV +7.11 (adj +2.04) on $44.77, P(profit) 0.4776, adj growth 16.7 bp · B EV +7.55 (adj +4.73) on $40.30, P(profit) 0.4638, adj growth 41.3 bp · C EV +7.11 (adj +3.54) on $50.00, P(profit) 0.6785, adj growth 31.5 bp · R EV +0.47 (adj +0.31) on $5.00, P(profit) 0.6746, adj growth 11.1 bp

## SJS @ LAK  ·  10000 joint draws  ·  488 bet sides mapped, 5 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.599 / away 0.401

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_SJS_win | p_overtime | goals | shots LAK/SJS | LAK/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.63 | 0.37 | 0.00 | 5.98 | 27.9/27.4 | 24.4/23.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.108 | 0.67 | 0.33 | 0.00 | 6.0 | 33.4/22.2 | 19.5/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.47 | 5.9 | 28.1/27.8 | 24.6/24.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.59 | 0.41 | 0.51 | 5.83 | 33.2/22.2 | 19.2/29.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.63 | 0.37 | 0.00 | 9.23 | 29.3/28.8 | 23.8/22.4 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.064 | 0.71 | 0.29 | 0.00 | 9.13 | 34.7/22.9 | 18.4/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 1+ goals NO | 80 | 0.852 | 0.838 | +0.041 | +0.027 | $20.00 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Macklin Celebrini: 1+ assists NO | 47 | 0.610 | 0.509 | +0.123 | +0.022 | $9.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.76) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 42 | 0.554 | 0.450 | +0.117 | +0.013 | $5.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.75) | CALIBRATION_WARNING | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (10.32 vs 4.18 bp); despite a smaller raw edge (+0.041 vs +0.123/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.136); KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: SJS offense succeeds (4+ goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMMARCHMENT27-1|no; why: higher confidence-adjusted growth (4.18 vs 1.69 bp); relationships: KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.136); KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: SJS offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-LABCLARKE92-1|no; why: higher confidence-adjusted growth (1.43 vs 0.69 bp); evidence CALIBRATION_WARNING vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SJS:SUPPRESSED (p 0.4784): highest fidelity KXNHLAST-26NOV04SJLA-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.359): highest fidelity KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no (same contract)
- KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3045, phi -0.17)
- KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 24% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.5 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3045, phi -0.273)
- KXNHLAST-26NOV04SJLA-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 25% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.9 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4321, phi -0.285)

portfolios: A EV +9.00 (adj +1.39) on $44.77, P(profit) 0.6944, adj growth 10.7 bp · B EV +4.96 (adj +1.26) on $35.33, P(profit) 0.7127, adj growth 11.4 bp · C EV +4.25 (adj +0.65) on $16.52, P(profit) 0.6101, adj growth 5.7 bp · R EV +0.25 (adj +0.16) on $5.00, P(profit) 0.8522, adj growth 6.2 bp

## CGY @ SEA  ·  10000 joint draws  ·  446 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.548 / away 0.452

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CGY_win | p_overtime | goals | shots SEA/CGY | SEA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.64 | 0.36 | 0.00 | 6.03 | 28.2/28.4 | 25.5/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.44 | 5.86 | 28.4/28.3 | 25.2/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.67 | 0.34 | 0.00 | 9.45 | 29.9/30.0 | 24.9/22.5 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.071 | 0.59 | 0.41 | 0.00 | 6.09 | 22.9/34.1 | 30.8/19.1 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.068 | 0.70 | 0.30 | 0.00 | 6.0 | 33.2/22.8 | 20.3/28.3 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.058 | 0.51 | 0.49 | 0.50 | 5.92 | 23.0/34.0 | 30.7/19.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 10 | 0.170 | 0.150 | +0.063 | +0.043 | $10.33 | FUNDED_RESEARCH | $3 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jani Nyman: 1+ goals YES | 11 | 0.162 | 0.146 | +0.045 | +0.029 | $7.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 18 | 0.229 | 0.215 | +0.038 | +0.025 | $7.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (41.63 vs 0.72 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: SEA offense suppressed (<= 2 goals)
- **Jani Nyman: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (17.71 vs 0.72 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04CGYSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (8.78 vs 0.72 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4772): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.171)
- KXNHLGOAL-26NOV04CGYSEA-SEAJNYMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.171)
- KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3127, phi -0.188)

portfolios: A EV +15.92 (adj +10.71) on $37.81, P(profit) 0.4624, adj growth 83.3 bp · B EV +10.40 (adj +7.00) on $24.86, P(profit) 0.4624, adj growth 59.6 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +1.79 (adj +1.22) on $3.00, P(profit) 0.1696, adj growth 40.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
