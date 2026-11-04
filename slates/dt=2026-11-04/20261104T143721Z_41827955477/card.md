# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-04T14:37:21Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 97.81 | +15.79 | +7.74 | +12.39 | 0.558 | -51.68 | -68.64 | 59.55 |
| B thesis-diversified (joint) ← optimiser card | 70.02 | +14.69 | +9.04 | +10.14 | 0.578 | -49.88 | -49.88 | 78.36 |
| C best expression per thesis | 59.01 | +10.25 | +5.89 | +6.73 | 0.518 | -40.32 | -40.32 | 51.50 |
| R FUNDED research stakes | 7.00 | +0.94 | +0.58 | +0.98 | 0.753 | -7.00 | -7.00 | 0.00 |

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
| Ridly Greig: 1+ goals YES | 16 | 0.207 | 0.192 | +0.038 | +0.022 | $6.53 | FUNDED_RESEARCH | $2 | OTT:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Artem Zub: 1+ goals YES | 4 | 0.060 | 0.053 | +0.018 | +0.010 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Claude Giroux: 1+ goals YES | 17 | 0.203 | 0.191 | +0.023 | +0.011 | $3.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Thomas Chabot: 1+ assists NO | 67 | 0.737 | 0.698 | +0.051 | +0.013 | $13.81 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (7.50 vs 1.75 bp); relationships: KXNHLGOAL-26NOV04OTTBUF-OTTAZUB2-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV04OTTBUF-OTTTCHABOT72-1|no: INTENTIONAL_DIVERSIFIER (phi -0.092); failure: OTT offense suppressed (<= 2 goals)
- **Artem Zub: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes has the higher standalone adjusted growth (7.50 vs 5.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26NOV04OTTBUF-OTTTCHABOT72-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: OTT offense suppressed (<= 2 goals)
- **Claude Giroux: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes has the higher standalone adjusted growth (7.50 vs 1.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV04OTTBUF-OTTAZUB2-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26NOV04OTTBUF-OTTTCHABOT72-1|no: INTENTIONAL_DIVERSIFIER (phi -0.086); failure: OTT offense suppressed (<= 2 goals)
- **Thomas Chabot: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26NOV04OTTBUF-4|no; why: higher confidence-adjusted growth (1.66 vs 0.62 bp); wins across more scripts (relative breadth 1.01 vs 0.357); alternative not eligible: confidence-adjusted EV +0.0050 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.092); KXNHLGOAL-26NOV04OTTBUF-OTTAZUB2-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.086); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.3907): highest fidelity KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:OFFENSE_4PLUS (p 0.4457): highest fidelity KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV04OTTBUF-BUFZBENSON6-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3879): highest fidelity KXNHLAST-26NOV04OTTBUF-OTTTCHABOT72-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV04OTTBUF-OTTTCHABOT72-1|no (same contract)
- KXNHLGOAL-26NOV04OTTBUF-OTTRGREIG71-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3879, phi -0.205)
- KXNHLGOAL-26NOV04OTTBUF-OTTAZUB2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3879, phi -0.117)
- KXNHLGOAL-26NOV04OTTBUF-OTTCGIROUX28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3879, phi -0.213)
- KXNHLAST-26NOV04OTTBUF-OTTTCHABOT72-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3907, phi -0.226)

portfolios: A EV +5.85 (adj +2.70) on $47.81, P(profit) 0.4846, adj growth 20.7 bp · B EV +3.83 (adj +1.84) on $25.95, P(profit) 0.3568, adj growth 15.9 bp · C EV +2.83 (adj +1.28) on $23.50, P(profit) 0.3917, adj growth 11.1 bp · R EV +0.44 (adj +0.26) on $2.00, P(profit) 0.207, adj growth 8.6 bp

## CHI @ FLA  ·  10000 joint draws  ·  410 bet sides mapped, 12 +EV candidates, 4 on card


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
| Tyler Bertuzzi: 1+ goals YES | 20 | 0.283 | 0.259 | +0.072 | +0.048 | $13.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Ryan Greene: 1+ goals YES | 11 | 0.160 | 0.145 | +0.043 | +0.028 | $7.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 61 | 0.689 | 0.667 | +0.062 | +0.040 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Wyatt Kaiser: 1+ goals YES | 4 | 0.063 | 0.057 | +0.020 | +0.015 | $3.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes; why: higher confidence-adjusted growth (29.19 vs 16.65 bp); relationships: KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV04CHIFLA-CHIWKAISER44-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI offense suppressed (<= 2 goals)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (29.19 vs 16.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV04CHIFLA-CHIWKAISER44-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CHI offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV04CHIFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (15.17 vs 6.05 bp); relationships: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV04CHIFLA-CHIWKAISER44-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: FLA offense succeeds (4+ goals)
- **Wyatt Kaiser: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (29.19 vs 10.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.14, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.3154): highest fidelity KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.3016): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.3742): highest fidelity KXNHLSPREAD-26NOV04CHIFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV04CHIFLA-CHI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV04CHIFLA-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4736, phi -0.276)
- KXNHLGOAL-26NOV04CHIFLA-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4736, phi -0.206)
- KXNHLGOAL-26NOV04CHIFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4927, phi -0.244)
- KXNHLGOAL-26NOV04CHIFLA-CHIWKAISER44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4736, phi -0.12)

portfolios: A EV +9.94 (adj +5.04) on $50.00, P(profit) 0.4615, adj growth 38.9 bp · B EV +10.86 (adj +7.20) on $44.07, P(profit) 0.4354, adj growth 62.4 bp · C EV +7.42 (adj +4.61) on $35.51, P(profit) 0.3427, adj growth 40.4 bp · R EV +0.50 (adj +0.32) on $5.00, P(profit) 0.6891, adj growth 11.7 bp

## SJS @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_SJS_win | p_overtime | goals | shots LAK/SJS | LAK/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.60 | 0.40 | 0.00 | 5.97 | 27.9/27.6 | 24.5/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.46 | 5.91 | 28.1/27.6 | 24.3/24.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.104 | 0.67 | 0.33 | 0.00 | 5.99 | 33.5/22.2 | 19.6/28.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.57 | 0.43 | 0.46 | 5.86 | 33.5/22.1 | 18.9/30.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.60 | 0.40 | 0.00 | 9.29 | 29.6/29.0 | 23.6/23.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.61 | 0.39 | 0.00 | 3.44 | 26.3/26.2 | 24.7/24.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CGY @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CGY_win | p_overtime | goals | shots SEA/CGY | SEA/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.66 | 0.34 | 0.00 | 6.07 | 28.2/28.4 | 25.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.55 | 0.45 | 0.48 | 5.98 | 28.3/28.4 | 25.1/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.65 | 0.35 | 0.00 | 9.38 | 30.1/30.2 | 24.9/23.2 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.070 | 0.57 | 0.43 | 0.00 | 5.98 | 22.8/33.6 | 30.3/19.1 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.066 | 0.69 | 0.31 | 0.00 | 6.05 | 33.3/22.7 | 20.0/28.3 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.51 | 0.49 | 0.42 | 5.88 | 22.6/33.5 | 30.2/19.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
