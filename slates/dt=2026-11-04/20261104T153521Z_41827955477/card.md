# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-04T15:35:21Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +31.87 | +16.69 | +23.67 | 0.611 | -68.82 | -87.16 | 135.28 |
| B thesis-diversified (joint) ← optimiser card | 131.65 | +29.66 | +18.19 | +20.80 | 0.627 | -52.80 | -71.37 | 157.14 |
| C best expression per thesis | 75.14 | +14.37 | +7.40 | +7.07 | 0.568 | -39.25 | -44.80 | 64.52 |
| R FUNDED research stakes | 16.00 | +3.21 | +2.17 | -1.86 | 0.333 | -9.84 | -9.84 | 0.00 |

## OTT @ BUF  ·  10000 joint draws  ·  406 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_OTT_win | p_overtime | goals | shots BUF/OTT | BUF/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.56 | 0.44 | 0.00 | 6.04 | 27.3/27.3 | 24.0/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.47 | 5.99 | 27.4/27.5 | 24.1/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.56 | 0.44 | 0.00 | 9.38 | 29.0/28.7 | 23.1/22.2 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.073 | 0.61 | 0.39 | 0.00 | 6.02 | 32.2/21.9 | 19.0/28.0 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.55 | 0.45 | 0.43 | 5.93 | 32.2/21.8 | 18.6/28.6 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.061 | 0.48 | 0.52 | 0.00 | 6.04 | 21.9/32.3 | 28.4/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ridly Greig: 1+ goals YES | 15 | 0.207 | 0.192 | +0.048 | +0.033 | $9.29 | FUNDED_RESEARCH | $3 | OTT:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Artem Zub: 1+ goals YES | 4 | 0.060 | 0.055 | +0.018 | +0.013 | $2.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Claude Giroux: 1+ goals YES | 16 | 0.203 | 0.188 | +0.033 | +0.019 | $5.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Thomas Chabot: 1+ assists NO | 67 | 0.737 | 0.698 | +0.051 | +0.013 | $15.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (17.03 vs 5.48 bp); relationships: KXNHLGOAL-26NOV04OTTBUF-OTTAZUB2-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV04OTTBUF-OTTTCHABOT72-1|no: INTENTIONAL_DIVERSIFIER (phi -0.092); failure: OTT offense suppressed (<= 2 goals)
- **Artem Zub: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes has the higher standalone adjusted growth (17.03 vs 8.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26NOV04OTTBUF-OTTTCHABOT72-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: OTT offense suppressed (<= 2 goals)
- **Claude Giroux: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes has the higher standalone adjusted growth (17.03 vs 5.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV04OTTBUF-OTTAZUB2-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26NOV04OTTBUF-OTTTCHABOT72-1|no: INTENTIONAL_DIVERSIFIER (phi -0.086); failure: OTT offense suppressed (<= 2 goals)
- **Thomas Chabot: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26NOV04OTTBUF-4|no; why: higher confidence-adjusted growth (1.66 vs 0.62 bp); wins across more scripts (relative breadth 1.01 vs 0.357); alternative not eligible: confidence-adjusted EV +0.0050 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.092); KXNHLGOAL-26NOV04OTTBUF-OTTAZUB2-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.086); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.3907): highest fidelity KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:OFFENSE_4PLUS (p 0.4457): highest fidelity KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3879): highest fidelity KXNHLAST-26NOV04OTTBUF-OTTTCHABOT72-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04OTTBUF-OTTTCHABOT72-1|no (same contract)
- KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3879, phi -0.205)
- KXNHLGOAL-26NOV04OTTBUF-OTTAZUB2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3879, phi -0.117)
- KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3879, phi -0.213)
- KXNHLAST-26NOV04OTTBUF-OTTTCHABOT72-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3907, phi -0.226)

portfolios: A EV +6.80 (adj +3.77) on $41.85, P(profit) 0.5195, adj growth 31.3 bp · B EV +6.23 (adj +3.66) on $32.96, P(profit) 0.3568, adj growth 31.5 bp · C EV +4.26 (adj +2.35) on $27.16, P(profit) 0.3917, adj growth 20.3 bp · R EV +0.91 (adj +0.61) on $3.00, P(profit) 0.207, adj growth 20.0 bp

## CHI @ FLA  ·  10000 joint draws  ·  410 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_CHI_win | p_overtime | goals | shots FLA/CHI | FLA/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.142 | 0.73 | 0.27 | 0.00 | 6.05 | 32.6/20.8 | 18.3/27.7 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.58 | 0.42 | 0.46 | 5.86 | 33.2/21.1 | 18.0/29.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.62 | 0.38 | 0.00 | 6.01 | 27.2/26.4 | 23.4/23.1 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.103 | 0.75 | 0.25 | 0.00 | 9.31 | 34.2/22.2 | 17.9/25.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.55 | 0.45 | 0.46 | 5.93 | 27.0/26.4 | 23.1/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.63 | 0.37 | 0.00 | 9.43 | 28.8/28.1 | 22.7/21.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 20 | 0.283 | 0.259 | +0.072 | +0.048 | $13.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Ryan Greene: 1+ goals YES | 11 | 0.160 | 0.145 | +0.043 | +0.028 | $7.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 61 | 0.689 | 0.667 | +0.062 | +0.040 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.129 | 0.118 | +0.033 | +0.022 | $5.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes; why: higher confidence-adjusted growth (29.19 vs 16.65 bp); relationships: KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: CHI offense suppressed (<= 2 goals)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (29.19 vs 16.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: CHI offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (15.17 vs 6.05 bp); relationships: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: FLA offense succeeds (4+ goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV04CHIFLA-8|yes; why: higher confidence-adjusted growth (11.83 vs 0.26 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.828 vs 0.333); alternative not eligible: confidence-adjusted EV +0.0048 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.14, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.3154): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.3016): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.3742): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4736, phi -0.276)
- KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4736, phi -0.206)
- KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4927, phi -0.244)
- KXNHLGOAL-26NOV04CHIFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3016, phi -0.148)

portfolios: A EV +8.32 (adj +4.22) on $41.85, P(profit) 0.4615, adj growth 34.1 bp · B EV +11.15 (adj +7.32) on $46.17, P(profit) 0.4745, adj growth 63.6 bp · C EV +7.42 (adj +4.61) on $35.51, P(profit) 0.3427, adj growth 40.4 bp · R EV +0.50 (adj +0.32) on $5.00, P(profit) 0.6891, adj growth 11.7 bp

## SJS @ LAK  ·  10000 joint draws  ·  378 bet sides mapped, 5 +EV candidates, 4 on card


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
| Ivar Stenberg: 1+ goals NO | 80 | 0.856 | 0.839 | +0.044 | +0.028 | $20.00 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Andre Lee: 1+ goals YES | 11 | 0.153 | 0.140 | +0.036 | +0.023 | $5.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 6 | 0.091 | 0.078 | +0.027 | +0.014 | $3.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Macklin Celebrini: 1+ assists NO | 49 | 0.621 | 0.523 | +0.114 | +0.015 | $6.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (11.35 vs 2.06 bp); despite a smaller raw edge (+0.044 vs +0.114/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV04SJLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.134); failure: SJS offense succeeds (4+ goals)
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes; why: higher confidence-adjusted growth (10.97 vs 1.82 bp); despite a smaller raw edge (+0.036 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV04SJLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: LAK offense suppressed (<= 2 goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes; why: higher confidence-adjusted growth (7.00 vs 1.82 bp); despite a smaller raw edge (+0.027 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: LAK offense suppressed (<= 2 goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV04SJLA-SJMMARCHMENT27-1|no; why: higher confidence-adjusted growth (2.06 vs 0.22 bp); alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.134); KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV04SJLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.4758): highest fidelity KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.4234): highest fidelity KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV04SJLA-LATMOORE12-1|yes (same contract)
- KXNHLGOAL-26NOV04SJLA-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3081, phi -0.178)
- KXNHLGOAL-26NOV04SJLA-LAALEE47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3591, phi -0.16)
- KXNHLGOAL-26NOV04SJLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3591, phi -0.13)
- KXNHLAST-26NOV04SJLA-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.1 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3081, phi -0.284)

portfolios: A EV +7.60 (adj +2.49) on $41.85, P(profit) 0.4368, adj growth 20.5 bp · B EV +5.71 (adj +2.73) on $35.73, P(profit) 0.6553, adj growth 24.0 bp · C EV +2.69 (adj +0.44) on $12.47, P(profit) 0.7574, adj growth 3.8 bp · R EV +0.27 (adj +0.17) on $5.00, P(profit) 0.8556, adj growth 6.5 bp

## CGY @ SEA  ·  10000 joint draws  ·  434 bet sides mapped, 3 +EV candidates, 3 on card


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
| Ben Meyers: 1+ goals YES | 10 | 0.161 | 0.144 | +0.054 | +0.038 | $9.33 | FUNDED_RESEARCH | $3 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Jake Middleton: 1+ goals YES | 4 | 0.059 | 0.054 | +0.017 | +0.012 | $2.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 19 | 0.232 | 0.217 | +0.031 | +0.017 | $4.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV04CGYSEA-CGY2|no; why: higher confidence-adjusted growth (31.91 vs 0.04 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0019 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-CGYJMIDDLETON55-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: SEA offense suppressed (<= 2 goals)
- **Jake Middleton: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV04CGYSEA-7|yes; why: higher confidence-adjusted growth (7.21 vs 0.00 bp); despite a smaller raw edge (+0.017 vs +0.022/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.875 vs 0.672); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: CGY offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV04CGYSEA-CGY2|no; why: higher confidence-adjusted growth (3.80 vs 0.04 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0019 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV04CGYSEA-CGYJMIDDLETON55-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4747): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis CGY:OFFENSE_4PLUS (p 0.3364): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV04CGYSEA-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3069, phi -0.177)
- KXNHLGOAL-26NOV04CGYSEA-CGYJMIDDLETON55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4515, phi -0.123)
- KXNHLGOAL-26NOV04CGYSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3069, phi -0.18)

portfolios: A EV +9.16 (adj +6.21) on $24.44, P(profit) 0.3912, adj growth 49.5 bp · B EV +6.56 (adj +4.48) on $16.79, P(profit) 0.3912, adj growth 38.1 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +1.53 (adj +1.07) on $3.00, P(profit) 0.1606, adj growth 34.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
