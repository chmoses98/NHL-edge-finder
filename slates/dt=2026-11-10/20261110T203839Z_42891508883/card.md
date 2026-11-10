# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-10T20:38:39Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +27.22 | +13.37 | +24.15 | 0.682 | -36.58 | -51.57 | 120.74 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +32.36 | +21.89 | +23.43 | 0.669 | -41.41 | -56.40 | 197.72 |
| C best expression per thesis | 150.02 | +24.30 | +14.32 | +20.32 | 0.650 | -39.93 | -53.73 | 129.63 |
| R FUNDED research stakes | 19.00 | +4.16 | +3.16 | -0.91 | 0.452 | -8.09 | -8.39 | 0.00 |

## COL @ TOR  ·  10000 joint draws  ·  428 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.395 / away 0.605

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_COL_win | p_overtime | goals | shots TOR/COL | TOR/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.132 | 0.34 | 0.66 | 0.00 | 6.07 | 23.0/35.9 | 31.5/20.2 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.111 | 0.33 | 0.67 | 0.00 | 9.4 | 24.7/37.8 | 29.3/19.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.41 | 0.59 | 0.00 | 6.06 | 28.9/29.9 | 26.0/25.8 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.44 | 0.56 | 0.47 | 5.95 | 23.4/36.1 | 32.7/20.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.51 | 0.49 | 0.44 | 5.99 | 29.1/30.1 | 26.7/25.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.41 | 0.59 | 0.00 | 9.51 | 30.7/31.9 | 24.8/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.167 | 0.151 | +0.050 | +0.035 | $5.22 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Dakota Joshua: 1+ goals YES | 11 | 0.151 | 0.140 | +0.034 | +0.023 | $3.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Brandon Duhaime: 1+ goals YES | 8 | 0.108 | 0.100 | +0.023 | +0.015 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ goals YES | 19 | 0.232 | 0.221 | +0.032 | +0.020 | $3.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10COLTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (24.70 vs 5.29 bp); relationships: KXNHLGOAL-26NOV10COLTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV10COLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV10COLTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: TOR offense suppressed (<= 2 goals)
- **Dakota Joshua: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (24.70 vs 10.87 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.022); they share one thesis budget; relationships: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV10COLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV10COLTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: TOR offense suppressed (<= 2 goals)
- **Brandon Duhaime: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (24.70 vs 5.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV10COLTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV10COLTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: TOR offense suppressed (<= 2 goals)
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (24.70 vs 5.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.026); they share one thesis budget; relationships: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26NOV10COLTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV10COLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, COL shot control · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3729): highest fidelity KXNHLGOAL-26NOV10COLTOR-TORJTAVARES91-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.3011): highest fidelity KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-1|no (same contract)
- KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4088, phi -0.201)
- KXNHLGOAL-26NOV10COLTOR-TORDJOSHUA81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4088, phi -0.171)
- KXNHLGOAL-26NOV10COLTOR-TORBDUHAIME24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4088, phi -0.149)
- KXNHLGOAL-26NOV10COLTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4088, phi -0.221)

portfolios: A EV +5.37 (adj +3.16) on $21.43, P(profit) 0.3698, adj growth 28.4 bp · B EV +4.41 (adj +2.95) on $14.37, P(profit) 0.511, adj growth 26.9 bp · C EV +3.48 (adj +2.08) on $11.66, P(profit) 0.5745, adj growth 18.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ MTL  ·  10000 joint draws  ·  444 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.464 / away 0.536

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_MIN_win | p_overtime | goals | shots MTL/MIN | MTL/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.53 | 0.47 | 0.00 | 6.03 | 28.2/28.5 | 25.1/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.45 | 5.99 | 28.3/28.5 | 25.3/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.55 | 0.45 | 0.00 | 9.34 | 29.3/29.7 | 23.9/23.1 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.090 | 0.47 | 0.53 | 0.00 | 6.03 | 22.4/33.7 | 30.0/19.1 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.49 | 0.51 | 0.46 | 5.95 | 22.1/33.6 | 30.2/18.9 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.064 | 0.45 | 0.55 | 0.00 | 9.34 | 24.1/35.4 | 28.3/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kirill Kaprizov: 1+ goals NO | 54 | 0.626 | 0.604 | +0.069 | +0.046 | $12.22 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 9 | 0.135 | 0.123 | +0.039 | +0.027 | $4.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Phillip Danault: 1+ goals YES | 11 | 0.159 | 0.145 | +0.042 | +0.028 | $4.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 16 | 0.213 | 0.198 | +0.043 | +0.029 | $4.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10MINMTL-MINQHUGHES43-1|no; why: higher confidence-adjusted growth (18.95 vs 2.79 bp); despite a smaller raw edge (+0.069 vs +0.087/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV10MINMTL-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.021); failure: MIN offense succeeds (4+ goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10MINMTL-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (17.69 vs 2.05 bp); relationships: KXNHLGOAL-26NOV10MINMTL-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: MIN offense suppressed (<= 2 goals)
- **Phillip Danault: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes; why: higher confidence-adjusted growth (16.62 vs 12.88 bp); despite a smaller raw edge (+0.042 vs +0.043/contract); relationships: KXNHLGOAL-26NOV10MINMTL-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26NOV10MINMTL-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.028); failure: MTL offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes has the higher standalone adjusted growth (16.62 vs 12.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.028); they share one thesis budget; relationships: KXNHLGOAL-26NOV10MINMTL-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV10MINMTL-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.028); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:SUPPRESSED (p 0.3778): highest fidelity KXNHLGOAL-26NOV10MINMTL-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV10MINMTL-MINKKAPRIZOV97-1|no (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4298): highest fidelity KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.4022): highest fidelity KXNHLGOAL-26NOV10MINMTL-MINBCOLEMAN20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10MINMTL-MINBCOLEMAN20-1|yes (same contract)
- KXNHLGOAL-26NOV10MINMTL-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4022, phi -0.27)
- KXNHLGOAL-26NOV10MINMTL-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3778, phi -0.149)
- KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.359, phi -0.201)
- KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.359, phi -0.213)

portfolios: A EV +3.78 (adj +1.56) on $21.43, P(profit) 0.5281, adj growth 14.5 bp · B EV +6.00 (adj +4.05) on $25.48, P(profit) 0.4275, adj growth 37.2 bp · C EV +4.52 (adj +2.74) on $28.00, P(profit) 0.5257, adj growth 25.0 bp · R EV +0.50 (adj +0.33) on $4.00, P(profit) 0.6264, adj growth 12.3 bp

## WSH @ OTT  ·  10000 joint draws  ·  436 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.497 / away 0.503

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_WSH_win | p_overtime | goals | shots OTT/WSH | OTT/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.55 | 0.45 | 0.00 | 6.02 | 27.3/27.1 | 23.7/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.45 | 5.96 | 27.1/27.0 | 23.6/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.53 | 0.47 | 0.00 | 9.37 | 28.9/28.3 | 22.3/22.9 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.098 | 0.60 | 0.40 | 0.00 | 5.98 | 32.2/21.5 | 18.5/28.3 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.55 | 0.45 | 0.49 | 5.92 | 32.4/21.8 | 18.7/29.0 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.069 | 0.64 | 0.36 | 0.00 | 9.28 | 34.0/23.2 | 18.3/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 16 | 0.229 | 0.211 | +0.060 | +0.041 | $6.90 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Ridly Greig: 1+ goals YES | 15 | 0.209 | 0.193 | +0.050 | +0.034 | $5.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Fabian Zetterlund: 1+ assists YES | 22 | 0.302 | 0.259 | +0.070 | +0.026 | $3.95 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_MIXED | D |
| Jordan Spence: 1+ goals YES | 6 | 0.088 | 0.079 | +0.024 | +0.015 | $2.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10WSHOTT-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (25.76 vs 4.21 bp); relationships: KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV10WSHOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV10WSHOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: WSH offense suppressed (<= 2 goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26NOV10WSHOTT-OTTFZETTERLUND20-1|yes; why: higher confidence-adjusted growth (18.46 vs 8.57 bp); despite a smaller raw edge (+0.050 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV10WSHOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26NOV10WSHOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: OTT offense suppressed (<= 2 goals)
- **Fabian Zetterlund: 1+ assists YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes has the higher standalone adjusted growth (18.46 vs 8.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.056); they share one thesis budget; relationships: KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26NOV10WSHOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi 0.069); failure: OTT offense suppressed (<= 2 goals)
- **Jordan Spence: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes has the higher standalone adjusted growth (18.46 vs 8.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV10WSHOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi 0.069); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3872): highest fidelity KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4393): highest fidelity KXNHLAST-26NOV10WSHOTT-OTTFZETTERLUND20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:SUPPRESSED (p 0.3438): highest fidelity KXNHLAST-26NOV10WSHOTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV10WSHOTT-OTTJSANDERSON85-1|no (same contract)
- KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4004, phi -0.248)
- KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3438, phi -0.191)
- KXNHLAST-26NOV10WSHOTT-OTTFZETTERLUND20-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3438, phi -0.249)
- KXNHLGOAL-26NOV10WSHOTT-OTTJSPENCE10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3438, phi -0.127)

portfolios: A EV +5.49 (adj +3.01) on $21.43, P(profit) 0.5654, adj growth 27.8 bp · B EV +6.14 (adj +3.82) on $18.48, P(profit) 0.4447, adj growth 34.9 bp · C EV +5.41 (adj +3.51) on $20.56, P(profit) 0.3899, adj growth 31.5 bp · R EV +0.70 (adj +0.49) on $2.00, P(profit) 0.2291, adj growth 17.5 bp

## NJD @ WPG  ·  10000 joint draws  ·  434 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.431 / away 0.569

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_NJD_win | p_overtime | goals | shots WPG/NJD | WPG/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.49 | 0.51 | 0.00 | 6.03 | 27.6/28.0 | 24.5/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.44 | 5.87 | 27.8/28.2 | 24.9/24.4 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.100 | 0.44 | 0.56 | 0.00 | 5.98 | 21.8/33.3 | 29.3/18.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.47 | 0.53 | 0.47 | 5.86 | 22.2/33.6 | 30.1/19.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.50 | 0.50 | 0.00 | 9.29 | 28.9/29.4 | 23.2/22.8 | even strength |
| NJD shot control · low event (<=4) · decided (2+) | 0.055 | 0.44 | 0.56 | 0.00 | 3.44 | 20.9/31.9 | 29.9/19.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyrel Bauer: 1+ goals NO | 94 | 0.971 | 0.962 | +0.027 | +0.018 | $12.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 59 | 0.659 | 0.639 | +0.052 | +0.032 | $12.22 | FUNDED_RESEARCH | $4 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 13 | 0.162 | 0.153 | +0.024 | +0.015 | $2.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Amadeus Lombardi: 1+ goals YES | 10 | 0.127 | 0.119 | +0.021 | +0.013 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Tyrel Bauer: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV10NJWPG-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV10NJWPG-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: WPG offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10NJWPG-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (9.61 vs 7.73 bp); despite a smaller raw edge (+0.052 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV10NJWPG-WPGTBAUER77-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV10NJWPG-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV10NJWPG-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NJD offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26NOV10NJWPG-NJAGRITSYUK81-1|yes; why: higher confidence-adjusted growth (4.05 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV10NJWPG-WPGTBAUER77-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV10NJWPG-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: NJD offense suppressed (<= 2 goals)
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26NOV10NJWPG-NJAGRITSYUK81-1|yes; why: higher confidence-adjusted growth (3.58 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV10NJWPG-WPGTBAUER77-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV10NJWPG-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis NJD:SUPPRESSED (p 0.4007): highest fidelity KXNHLTEAMTOTAL-26NOV10NJWPG-NJ4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.4873): highest fidelity KXNHLSPREAD-26NOV10NJWPG-NJ2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV10NJWPG-NJ4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:LOW_EVENT (p 0.2518): highest fidelity KXNHLTEAMTOTAL-26NOV10NJWPG-NJ5|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV10NJWPG-NJ4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV10NJWPG-WPGTBAUER77-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.36, phi -0.086)
- KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3797, phi -0.266)
- KXNHLGOAL-26NOV10NJWPG-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4007, phi -0.191)
- KXNHLGOAL-26NOV10NJWPG-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4007, phi -0.179)

portfolios: A EV +2.44 (adj +0.77) on $21.43, P(profit) 0.6043, adj growth 7.2 bp · B EV +2.24 (adj +1.40) on $29.04, P(profit) 0.738, adj growth 13.1 bp · C EV +2.68 (adj +1.17) on $35.50, P(profit) 0.6492, adj growth 10.9 bp · R EV +0.34 (adj +0.21) on $4.00, P(profit) 0.659, adj growth 7.7 bp

## FLA @ CBJ  ·  10000 joint draws  ·  426 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.470 / away 0.530

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_FLA_win | p_overtime | goals | shots CBJ/FLA | CBJ/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.62 | 0.38 | 0.00 | 6.05 | 27.0/27.1 | 24.1/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.48 | 5.95 | 27.1/27.2 | 24.0/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.62 | 0.38 | 0.00 | 9.33 | 28.5/28.6 | 23.4/21.6 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.072 | 0.66 | 0.34 | 0.00 | 6.0 | 32.2/21.8 | 19.1/27.5 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.069 | 0.54 | 0.46 | 0.00 | 6.02 | 21.6/31.9 | 28.2/18.0 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.057 | 0.46 | 0.54 | 0.48 | 5.9 | 21.6/32.1 | 28.7/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 2+ goals YES | 1 | 0.034 | 0.031 | +0.024 | +0.020 | $2.01 | FUNDED_RESEARCH | $1 | CBJ:WINS_BY_2PLUS | FRAGILE (0.08) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 15 | 0.229 | 0.208 | +0.070 | +0.049 | $5.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Dmitri Voronkov: 1+ goals YES | 14 | 0.185 | 0.173 | +0.037 | +0.024 | $4.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 24 | 0.297 | 0.282 | +0.045 | +0.029 | $5.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
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

portfolios: A EV +6.12 (adj +2.85) on $21.43, P(profit) 0.5117, adj growth 24.3 bp · B EV +9.02 (adj +6.88) on $17.63, P(profit) 0.5613, adj growth 59.8 bp · C EV +5.39 (adj +3.44) on $21.60, P(profit) 0.2758, adj growth 30.8 bp · R EV +2.21 (adj +1.87) on $1.00, P(profit) 0.0343, adj growth 56.0 bp

## DET @ STL  ·  10000 joint draws  ·  438 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.564 / away 0.436

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_DET_win | p_overtime | goals | shots STL/DET | STL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.66 | 0.34 | 0.00 | 6.01 | 27.2/27.2 | 24.4/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.54 | 0.46 | 0.48 | 5.95 | 27.2/27.4 | 24.1/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.66 | 0.34 | 0.00 | 9.31 | 28.7/28.8 | 23.6/21.7 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.075 | 0.61 | 0.39 | 0.00 | 5.99 | 21.7/32.4 | 29.1/17.9 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.48 | 0.52 | 0.51 | 5.83 | 21.7/32.4 | 29.1/18.5 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.066 | 0.71 | 0.29 | 0.00 | 5.99 | 31.6/21.6 | 18.9/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pius Suter: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $3.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Cam Fowler: 1+ goals NO | 92 | 0.947 | 0.939 | +0.022 | +0.014 | $12.22 | FUNDED_RESEARCH | $4 | STL:SUPPRESSED | DIRECT (0.98) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 26 | 0.301 | 0.290 | +0.028 | +0.016 | $3.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Philip Broberg: 1+ assists YES | 38 | 0.443 | 0.409 | +0.046 | +0.012 | $2.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_MIXED | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (7.42 vs 2.84 bp); relationships: KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26NOV10DETSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.045); failure: STL offense suppressed (<= 2 goals)
- **Cam Fowler: 1+ goals NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10DETSTL-STLRTHOMAS18-1|no; why: higher confidence-adjusted growth (6.05 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.037/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV10DETSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: STL offense succeeds (4+ goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV10DETSTL-STLPBROBERG6-1|yes; why: higher confidence-adjusted growth (2.84 vs 1.38 bp); despite a smaller raw edge (+0.028 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV10DETSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.138); failure: STL offense suppressed (<= 2 goals)
- **Philip Broberg: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (2.84 vs 1.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.138); they share one thesis budget; relationships: KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.045); KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.138); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.4371): highest fidelity KXNHLAST-26NOV10DETSTL-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:SUPPRESSED (p 0.346): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.346, phi -0.19)
- KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: FUNDED_RESEARCH; family TRUSTED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4371, phi -0.108)
- KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.346, phi -0.253)
- KXNHLAST-26NOV10DETSTL-STLPBROBERG6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.346, phi -0.299)

portfolios: A EV +2.12 (adj +1.03) on $21.43, P(profit) 0.5155, adj growth 9.2 bp · B EV +1.60 (adj +0.91) on $20.81, P(profit) 0.4052, adj growth 8.5 bp · C EV +0.39 (adj +0.23) on $3.84, P(profit) 0.3011, adj growth 2.1 bp · R EV +0.09 (adj +0.06) on $4.00, P(profit) 0.9468, adj growth 2.3 bp

## NSH @ LAK  ·  10000 joint draws  ·  386 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.547 / away 0.453

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_NSH_win | p_overtime | goals | shots LAK/NSH | LAK/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.60 | 0.40 | 0.00 | 5.95 | 28.3/27.9 | 24.9/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.48 | 5.89 | 28.3/28.0 | 24.7/25.1 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.107 | 0.67 | 0.33 | 0.00 | 5.97 | 33.5/22.2 | 19.5/29.0 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.55 | 0.45 | 0.46 | 5.89 | 33.5/22.3 | 19.2/30.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.59 | 0.41 | 0.00 | 9.25 | 29.8/29.5 | 23.8/22.7 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.067 | 0.68 | 0.32 | 0.00 | 9.2 | 35.4/23.7 | 19.2/27.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.077 | 0.069 | +0.024 | +0.016 | $2.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ goals NO | 62 | 0.687 | 0.669 | +0.051 | +0.033 | $12.22 | FUNDED_RESEARCH | $4 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Scott Laughton: 1+ goals YES | 11 | 0.144 | 0.134 | +0.027 | +0.017 | $2.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Steven Stamkos: 1+ goals NO | 65 | 0.696 | 0.682 | +0.030 | +0.016 | $6.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (10.60 vs 2.07 bp); despite a smaller raw edge (+0.024 vs +0.025/contract); relationships: KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV10NSHLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.028); failure: LAK offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ goals NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10NSHLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (10.04 vs 0.15 bp); despite a smaller raw edge (+0.051 vs +0.084/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV10NSHLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: LAK offense succeeds (4+ goals)
- **Scott Laughton: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLPTS-26NOV10NSHLA-NSHSSTAMKOS91-1|no; why: higher confidence-adjusted growth (6.21 vs 0.00 bp); despite a smaller raw edge (+0.027 vs +0.061/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.024); failure: LAK offense suppressed (<= 2 goals)
- **Steven Stamkos: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no; why: Player prop expression KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no selected over player prop KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.83 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV10NSHLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.024); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis LAK:SUPPRESSED (p 0.3567): highest fidelity KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no (same contract)
- thesis NSH:SUPPRESSED (p 0.4707): highest fidelity KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.4241): highest fidelity KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes (same contract)
- KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3567, phi -0.129)
- KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4241, phi -0.258)
- KXNHLGOAL-26NOV10NSHLA-LASLAUGHTON21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3567, phi -0.18)
- KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3177, phi -0.256)
- override: Player prop expression KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no selected over player prop KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 0.83 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.91 (adj +0.99) on $21.43, P(profit) 0.4809, adj growth 9.3 bp · B EV +2.94 (adj +1.88) on $24.18, P(profit) 0.5756, adj growth 17.3 bp · C EV +2.42 (adj +1.15) on $28.86, P(profit) 0.5845, adj growth 10.6 bp · R EV +0.32 (adj +0.20) on $4.00, P(profit) 0.687, adj growth 7.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
