# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-10T23:00:11Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +25.21 | +10.98 | +22.38 | 0.685 | -32.91 | -45.87 | 99.28 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +32.83 | +21.47 | +24.68 | 0.668 | -42.29 | -57.82 | 192.49 |
| C best expression per thesis | 150.01 | +25.45 | +14.38 | +21.55 | 0.647 | -41.27 | -55.23 | 129.50 |
| R FUNDED research stakes | 17.00 | +4.24 | +3.17 | +1.55 | 0.505 | -7.73 | -9.67 | 0.00 |

## COL @ TOR  ·  10000 joint draws  ·  428 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.391 / away 0.609

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_COL_win | p_overtime | goals | shots TOR/COL | TOR/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.131 | 0.34 | 0.66 | 0.00 | 6.06 | 22.8/35.9 | 31.1/19.9 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.106 | 0.35 | 0.65 | 0.00 | 9.39 | 24.7/37.8 | 29.7/19.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.42 | 0.58 | 0.00 | 6.08 | 29.2/29.9 | 25.9/25.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.45 | 0.55 | 0.47 | 5.96 | 23.1/36.3 | 32.9/19.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.39 | 0.61 | 0.00 | 9.51 | 30.7/31.7 | 24.5/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.49 | 0.51 | 0.45 | 6.0 | 29.3/30.2 | 26.7/25.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.167 | 0.151 | +0.050 | +0.035 | $5.48 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Dakota Joshua: 1+ goals YES | 11 | 0.151 | 0.140 | +0.034 | +0.023 | $3.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ assists NO | 40 | 0.490 | 0.443 | +0.073 | +0.026 | $6.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.72) | EVIDENCE_MIXED | D |
| Brandon Duhaime: 1+ goals YES | 8 | 0.108 | 0.100 | +0.023 | +0.015 | $2.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10COLTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (24.70 vs 5.29 bp); relationships: KXNHLGOAL-26NOV10COLTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV10COLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense suppressed (<= 2 goals)
- **Dakota Joshua: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (24.70 vs 10.87 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.022); they share one thesis budget; relationships: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV10COLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: TOR offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-2|no; why: higher confidence-adjusted growth (5.98 vs 3.54 bp); relationships: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV10COLTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV10COLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: COL offense succeeds (4+ goals)
- **Brandon Duhaime: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (24.70 vs 5.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV10COLTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, COL shot control · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3729): highest fidelity KXNHLGOAL-26NOV10COLTOR-TORECOWAN53-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.3011): highest fidelity KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.4088): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4088, phi -0.201)
- KXNHLGOAL-26NOV10COLTOR-TORDJOSHUA81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4088, phi -0.171)
- KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 28% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4898, phi -0.308)
- KXNHLGOAL-26NOV10COLTOR-TORBDUHAIME24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4088, phi -0.149)

portfolios: A EV +3.54 (adj +1.82) on $22.15, P(profit) 0.5556, adj growth 16.9 bp · B EV +5.26 (adj +3.16) on $18.30, P(profit) 0.3662, adj growth 28.7 bp · C EV +4.16 (adj +2.41) on $14.33, P(profit) 0.5745, adj growth 21.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ MTL  ·  10000 joint draws  ·  444 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.466 / away 0.534

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_MIN_win | p_overtime | goals | shots MTL/MIN | MTL/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.53 | 0.47 | 0.00 | 6.03 | 28.1/28.4 | 25.1/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.46 | 6.0 | 28.2/28.4 | 25.1/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.54 | 0.46 | 0.00 | 9.33 | 29.5/29.9 | 24.0/23.0 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.087 | 0.46 | 0.54 | 0.00 | 6.04 | 22.5/33.6 | 29.8/19.2 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.48 | 0.52 | 0.46 | 5.96 | 22.4/33.7 | 30.4/19.1 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.061 | 0.45 | 0.55 | 0.00 | 9.35 | 23.9/35.3 | 28.5/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 9 | 0.135 | 0.123 | +0.039 | +0.027 | $4.39 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Phillip Danault: 1+ goals YES | 11 | 0.159 | 0.145 | +0.042 | +0.028 | $4.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 16 | 0.213 | 0.198 | +0.043 | +0.029 | $4.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Adam Engstrom: 1+ goals YES | 4 | 0.059 | 0.057 | +0.016 | +0.014 | $2.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10MINMTL-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (17.69 vs 2.05 bp); relationships: KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV10MINMTL-MTLAENGSTROM42-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: MIN offense suppressed (<= 2 goals)
- **Phillip Danault: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes; why: higher confidence-adjusted growth (16.62 vs 12.88 bp); despite a smaller raw edge (+0.042 vs +0.043/contract); relationships: KXNHLGOAL-26NOV10MINMTL-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV10MINMTL-MTLAENGSTROM42-1|yes: MOSTLY_INDEPENDENT (phi 0.035); failure: MTL offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes has the higher standalone adjusted growth (16.62 vs 12.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.028); they share one thesis budget; relationships: KXNHLGOAL-26NOV10MINMTL-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV10MINMTL-MTLAENGSTROM42-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: MTL offense suppressed (<= 2 goals)
- **Adam Engstrom: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes has the higher standalone adjusted growth (16.62 vs 10.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.035); they share one thesis budget; relationships: KXNHLGOAL-26NOV10MINMTL-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.035); KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis MTL:OFFENSE_4PLUS (p 0.4298): highest fidelity KXNHLTEAMTOTAL-26NOV10MINMTL-MTL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3778): highest fidelity KXNHLAST-26NOV10MINMTL-MINQHUGHES43-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV10MINMTL-MINQHUGHES43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.359): highest fidelity KXNHLAST-26NOV10MINMTL-MTLNSUZUKI14-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV10MINMTL-MTLNSUZUKI14-1|no (same contract)
- KXNHLGOAL-26NOV10MINMTL-MINYTRENIN13-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3778, phi -0.149)
- KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.359, phi -0.201)
- KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.359, phi -0.213)
- KXNHLGOAL-26NOV10MINMTL-MTLAENGSTROM42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.359, phi -0.106)

portfolios: A EV +3.07 (adj +0.65) on $22.15, P(profit) 0.5692, adj growth 5.9 bp · B EV +5.52 (adj +3.88) on $16.06, P(profit) 0.4595, adj growth 35.2 bp · C EV +4.19 (adj +1.94) on $20.33, P(profit) 0.4927, adj growth 17.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ OTT  ·  10000 joint draws  ·  438 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.494 / away 0.506

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_WSH_win | p_overtime | goals | shots OTT/WSH | OTT/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.53 | 0.47 | 0.00 | 6.03 | 27.1/26.9 | 23.5/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.48 | 0.52 | 0.47 | 5.96 | 27.3/27.0 | 23.8/24.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.093 | 0.58 | 0.42 | 0.00 | 6.0 | 32.4/21.5 | 18.4/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.53 | 0.47 | 0.00 | 9.3 | 28.9/28.5 | 22.6/22.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.58 | 0.42 | 0.47 | 5.9 | 32.4/21.5 | 18.4/28.7 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.069 | 0.58 | 0.42 | 0.00 | 9.34 | 34.2/22.8 | 17.7/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 16 | 0.238 | 0.217 | +0.069 | +0.048 | $8.38 | FUNDED_RESEARCH | $3 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Jordan Spence: 1+ goals YES | 6 | 0.086 | 0.078 | +0.022 | +0.014 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Ridly Greig: 1+ goals YES | 16 | 0.203 | 0.190 | +0.034 | +0.021 | $3.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 54 | 0.610 | 0.573 | +0.052 | +0.015 | $6.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26NOV10WSHOTT-WSHAOVECHKIN8-1|yes; why: higher confidence-adjusted growth (35.00 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV10WSHOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV10WSHOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: WSH offense suppressed (<= 2 goals)
- **Jordan Spence: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (7.30 vs 6.50 bp); despite a smaller raw edge (+0.022 vs +0.034/contract); relationships: KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26NOV10WSHOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: OTT offense suppressed (<= 2 goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV10WSHOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (6.50 vs 0.58 bp); despite a smaller raw edge (+0.034 vs +0.083/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV10WSHOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26NOV10WSHOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.105); failure: OTT offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10WSHOTT-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (2.01 vs 0.02 bp); despite a smaller raw edge (+0.052 vs +0.073/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0015 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV10WSHOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.105); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.3849): highest fidelity KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4214): highest fidelity KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3614): highest fidelity KXNHLAST-26NOV10WSHOTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV10WSHOTT-OTTJSANDERSON85-1|no (same contract)
- KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.393, phi -0.251)
- KXNHLGOAL-26NOV10WSHOTT-OTTJSPENCE10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3614, phi -0.116)
- KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3614, phi -0.209)
- KXNHLAST-26NOV10WSHOTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4214, phi -0.262)

portfolios: A EV +5.56 (adj +3.46) on $22.15, P(profit) 0.4467, adj growth 31.5 bp · B EV +5.54 (adj +3.52) on $20.79, P(profit) 0.4467, adj growth 32.0 bp · C EV +5.53 (adj +3.49) on $21.44, P(profit) 0.3929, adj growth 31.3 bp · R EV +1.22 (adj +0.85) on $3.00, P(profit) 0.2383, adj growth 29.6 bp

## NJD @ WPG  ·  10000 joint draws  ·  434 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.434 / away 0.566

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_NJD_win | p_overtime | goals | shots WPG/NJD | WPG/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.50 | 0.50 | 0.00 | 6.01 | 27.5/28.1 | 24.5/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.49 | 0.51 | 0.44 | 5.89 | 27.8/28.4 | 25.2/24.5 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.098 | 0.42 | 0.58 | 0.00 | 6.01 | 21.8/33.4 | 29.4/18.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.48 | 0.52 | 0.49 | 5.87 | 22.2/33.5 | 30.0/19.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.50 | 0.50 | 0.00 | 9.29 | 29.1/29.6 | 23.6/23.1 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.057 | 0.52 | 0.48 | 0.48 | 2.87 | 26.2/26.8 | 25.3/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack Hughes: 1+ goals NO | 59 | 0.659 | 0.638 | +0.052 | +0.031 | $9.72 | FUNDED_RESEARCH | $3 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 71 | 0.759 | 0.745 | +0.035 | +0.021 | $9.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Josh Morrissey: 1+ assists NO | 57 | 0.692 | 0.609 | +0.105 | +0.022 | $8.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| New Jersey wins by over 1.5 goals NO | 65 | 0.713 | 0.679 | +0.047 | +0.013 | $4.13 | FUNDED_RESEARCH | $2 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10NJWPG-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (8.88 vs 7.73 bp); despite a smaller raw edge (+0.052 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV10NJWPG-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26NOV10NJWPG-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLSPREAD-26NOV10NJWPG-NJ2|no: REINFORCING (phi 0.15); failure: NJD offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26NOV10NJWPG-NJTMEIER28-1|no selected over player prop KXNHLAST-26NOV10NJWPG-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26NOV10NJWPG-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26NOV10NJWPG-NJ2|no: REINFORCING (phi 0.164); failure: NJD offense succeeds (4+ goals)
- **Josh Morrissey: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26NOV10NJWPG-6|no; why: higher confidence-adjusted growth (4.46 vs 0.90 bp); wins across more scripts (relative breadth 0.987 vs 0.755); relationships: KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV10NJWPG-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26NOV10NJWPG-NJ2|no: INTENTIONAL_DIVERSIFIER (phi -0.147); failure: WPG offense succeeds (4+ goals)
- **New Jersey wins by over 1.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV10NJWPG-NJ3|no; why: KXNHLSPREAD-26NOV10NJWPG-NJ3|no has the higher standalone adjusted growth (2.22 vs 1.71 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.724); relationships: KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no: REINFORCING (phi 0.15); KXNHLGOAL-26NOV10NJWPG-NJTMEIER28-1|no: REINFORCING (phi 0.164); KXNHLAST-26NOV10NJWPG-WPGJMORRISSEY44-1|no: INTENTIONAL_DIVERSIFIER (phi -0.147); failure: NJD wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis NJD:SUPPRESSED (p 0.4007): highest fidelity KXNHLTEAMTOTAL-26NOV10NJWPG-NJ4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26NOV10NJWPG-NJTMEIER28-1|no selected over player prop KXNHLAST-26NOV10NJWPG-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis WPG:SUPPRESSED (p 0.4169): highest fidelity KXNHLAST-26NOV10NJWPG-WPGJMORRISSEY44-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV10NJWPG-WPGJMORRISSEY44-1|no (same contract)
- thesis WPG:WINS (p 0.4873): highest fidelity KXNHLSPREAD-26NOV10NJWPG-NJ2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV10NJWPG-NJ4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3797, phi -0.266)
- KXNHLGOAL-26NOV10NJWPG-NJTMEIER28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3797, phi -0.24)
- KXNHLAST-26NOV10NJWPG-WPGJMORRISSEY44-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.7 pts; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.36, phi -0.24)
- KXNHLSPREAD-26NOV10NJWPG-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2868, phi -1.0)
- override: Player prop expression KXNHLGOAL-26NOV10NJWPG-NJTMEIER28-1|no selected over player prop KXNHLAST-26NOV10NJWPG-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.89 (adj +0.83) on $22.15, P(profit) 0.5729, adj growth 7.4 bp · B EV +3.01 (adj +1.16) on $31.31, P(profit) 0.6594, adj growth 10.8 bp · C EV +3.27 (adj +1.32) on $36.92, P(profit) 0.4603, adj growth 12.3 bp · R EV +0.40 (adj +0.19) on $5.00, P(profit) 0.5022, adj growth 7.1 bp

## FLA @ CBJ  ·  10000 joint draws  ·  426 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.470 / away 0.530

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_FLA_win | p_overtime | goals | shots CBJ/FLA | CBJ/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.61 | 0.39 | 0.00 | 6.02 | 27.2/27.2 | 24.1/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.51 | 0.49 | 0.49 | 5.92 | 27.2/27.4 | 24.1/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.60 | 0.40 | 0.00 | 9.33 | 28.5/28.8 | 23.5/21.9 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.070 | 0.70 | 0.30 | 0.00 | 6.04 | 31.7/21.3 | 18.7/27.1 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.070 | 0.52 | 0.48 | 0.00 | 6.04 | 21.9/31.9 | 28.3/18.5 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.56 | 0.44 | 0.47 | 5.97 | 32.4/22.2 | 19.0/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 2+ goals YES | 1 | 0.034 | 0.031 | +0.024 | +0.020 | $2.09 | FUNDED_RESEARCH | $1 | CBJ:WINS_BY_2PLUS | FRAGILE (0.08) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 15 | 0.229 | 0.208 | +0.070 | +0.049 | $5.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Dmitri Voronkov: 1+ goals YES | 14 | 0.185 | 0.173 | +0.037 | +0.024 | $4.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 24 | 0.297 | 0.282 | +0.045 | +0.029 | $6.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 2+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (68.83 vs 38.76 bp); despite a smaller raw edge (+0.024 vs +0.070/contract); relationships: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes: DUPLICATIVE (phi 0.345); KXNHLGOAL-26NOV10FLACBJ-CBJDVORONKOV10-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV10FLACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10FLACBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (38.76 vs 9.68 bp); relationships: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-2|yes: DUPLICATIVE (phi 0.345); KXNHLGOAL-26NOV10FLACBJ-CBJDVORONKOV10-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV10FLACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CBJ offense suppressed (<= 2 goals)
- **Dmitri Voronkov: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (38.76 vs 9.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-2|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV10FLACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (38.76 vs 9.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-2|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV10FLACBJ-CBJDVORONKOV10-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CBJ:WINS_BY_2PLUS (p 0.3474): highest fidelity KXNHLSPREAD-26NOV10FLACBJ-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:OFFENSE_4PLUS (p 0.4468): highest fidelity KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS (p 0.565): highest fidelity KXNHLSPREAD-26NOV10FLACBJ-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 92% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3438, phi -0.129)
- KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3438, phi -0.242)
- KXNHLGOAL-26NOV10FLACBJ-CBJDVORONKOV10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3438, phi -0.164)
- KXNHLGOAL-26NOV10FLACBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3438, phi -0.25)

portfolios: A EV +5.34 (adj +2.64) on $22.15, P(profit) 0.5187, adj growth 22.9 bp · B EV +9.39 (adj +7.17) on $18.36, P(profit) 0.5613, adj growth 61.9 bp · C EV +6.00 (adj +3.83) on $25.49, P(profit) 0.2758, adj growth 34.3 bp · R EV +2.21 (adj +1.87) on $1.00, P(profit) 0.0343, adj growth 56.0 bp

## DET @ STL  ·  10000 joint draws  ·  452 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.561 / away 0.439

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_DET_win | p_overtime | goals | shots STL/DET | STL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.65 | 0.35 | 0.00 | 6.02 | 27.2/27.5 | 24.7/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.53 | 0.47 | 0.48 | 5.89 | 27.0/27.3 | 24.1/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.66 | 0.34 | 0.00 | 9.3 | 28.6/28.8 | 23.3/21.5 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.073 | 0.62 | 0.38 | 0.00 | 5.97 | 21.8/32.5 | 29.5/18.0 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.49 | 0.51 | 0.50 | 5.88 | 21.8/32.4 | 29.1/18.5 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.064 | 0.71 | 0.29 | 0.00 | 6.01 | 31.4/21.6 | 19.1/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pius Suter: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $3.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Cam Fowler: 1+ goals NO | 92 | 0.947 | 0.939 | +0.022 | +0.014 | $12.73 | FUNDED_RESEARCH | $4 | STL:SUPPRESSED | DIRECT (0.98) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 26 | 0.301 | 0.290 | +0.028 | +0.016 | $3.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (7.42 vs 2.84 bp); relationships: KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: STL offense suppressed (<= 2 goals)
- **Cam Fowler: 1+ goals NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10DETSTL-STLRTHOMAS18-1|no; why: higher confidence-adjusted growth (6.05 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.037/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: STL offense succeeds (4+ goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV10DETSTL-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (2.84 vs 0.51 bp); despite a smaller raw edge (+0.028 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis STL:OFFENSE_4PLUS (p 0.4371): highest fidelity KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes (same contract)
- thesis STL:SUPPRESSED (p 0.346): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.346, phi -0.19)
- KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: FUNDED_RESEARCH; family TRUSTED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4371, phi -0.108)
- KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.346, phi -0.253)

portfolios: A EV +1.54 (adj +0.97) on $17.09, P(profit) 0.4052, adj growth 8.8 bp · B EV +1.43 (adj +0.90) on $19.64, P(profit) 0.4052, adj growth 8.4 bp · C EV +0.40 (adj +0.24) on $3.99, P(profit) 0.3011, adj growth 2.1 bp · R EV +0.09 (adj +0.06) on $4.00, P(profit) 0.9468, adj growth 2.3 bp

## NSH @ LAK  ·  10000 joint draws  ·  436 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.541 / away 0.459

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_NSH_win | p_overtime | goals | shots LAK/NSH | LAK/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.59 | 0.41 | 0.00 | 5.93 | 28.4/27.9 | 24.8/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.47 | 5.94 | 28.5/28.2 | 24.9/25.3 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.105 | 0.69 | 0.31 | 0.00 | 5.98 | 33.5/22.1 | 19.6/28.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.53 | 0.47 | 0.46 | 5.85 | 33.4/22.3 | 19.2/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.61 | 0.39 | 0.00 | 9.18 | 29.5/29.2 | 23.9/22.9 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.065 | 0.67 | 0.33 | 0.00 | 9.21 | 35.4/23.7 | 18.8/27.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.077 | 0.069 | +0.024 | +0.016 | $2.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ goals NO | 62 | 0.687 | 0.669 | +0.051 | +0.033 | $12.73 | FUNDED_RESEARCH | $4 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Steven Stamkos: 1+ goals NO | 65 | 0.696 | 0.682 | +0.030 | +0.016 | $7.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Alex Laferriere: 1+ goals YES | 27 | 0.309 | 0.298 | +0.025 | +0.014 | $2.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (10.60 vs 2.07 bp); despite a smaller raw edge (+0.024 vs +0.025/contract); relationships: KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: LAK offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ goals NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV10NSHLA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (10.04 vs 0.28 bp); despite a smaller raw edge (+0.051 vs +0.084/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: LAK offense succeeds (4+ goals)
- **Steven Stamkos: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (2.64 vs 1.62 bp); despite a smaller raw edge (+0.030 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: NSH offense succeeds (4+ goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV10NSHLA-NSH2|no; why: higher confidence-adjusted growth (2.07 vs 0.08 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis LAK:SUPPRESSED (p 0.3567): highest fidelity KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no (same contract)
- thesis NSH:SUPPRESSED (p 0.4707): highest fidelity KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.4241): highest fidelity KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes (same contract)
- KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3567, phi -0.129)
- KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4241, phi -0.258)
- KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3177, phi -0.256)
- KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3567, phi -0.238)

portfolios: A EV +1.27 (adj +0.61) on $22.15, P(profit) 0.7552, adj growth 5.8 bp · B EV +2.67 (adj +1.68) on $25.55, P(profit) 0.5816, adj growth 15.5 bp · C EV +1.90 (adj +1.15) on $27.51, P(profit) 0.5446, adj growth 10.6 bp · R EV +0.32 (adj +0.20) on $4.00, P(profit) 0.687, adj growth 7.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
