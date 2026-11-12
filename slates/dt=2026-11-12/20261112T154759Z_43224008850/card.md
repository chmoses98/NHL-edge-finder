# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-12T15:47:59Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +29.66 | +9.59 | +28.51 | 0.749 | -24.66 | -38.32 | 86.43 |
| B thesis-diversified (joint) ← optimiser card | 149.39 | +26.39 | +14.15 | +24.34 | 0.727 | -25.67 | -38.24 | 133.21 |
| C best expression per thesis | 150.00 | +37.45 | +19.79 | +30.71 | 0.672 | -50.74 | -69.41 | 172.36 |
| R FUNDED research stakes | 24.00 | +2.41 | +1.26 | +1.81 | 0.612 | -5.92 | -8.26 | 0.00 |

## CAR @ SEA  ·  10000 joint draws  ·  426 bet sides mapped, 33 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CAR_win | p_overtime | goals | shots SEA/CAR | SEA/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.156 | 0.35 | 0.65 | 0.00 | 6.02 | 21.1/34.2 | 29.7/18.4 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.134 | 0.47 | 0.53 | 0.49 | 6.02 | 21.4/34.7 | 31.3/18.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.128 | 0.33 | 0.67 | 0.00 | 9.4 | 22.5/35.9 | 28.1/17.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.090 | 0.42 | 0.58 | 0.00 | 6.13 | 27.0/28.1 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.38 | 0.62 | 0.00 | 9.4 | 28.5/29.8 | 22.9/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.51 | 0.49 | 0.46 | 6.03 | 26.7/28.0 | 24.7/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Berkly Catton: 1+ goals YES | 15 | 0.222 | 0.203 | +0.063 | +0.044 | $5.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 61 | 0.752 | 0.657 | +0.126 | +0.030 | $6.74 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikolaj Ehlers: 1+ goals NO | 72 | 0.773 | 0.758 | +0.039 | +0.024 | $9.00 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes; why: higher confidence-adjusted growth (30.43 vs 22.44 bp); despite a smaller raw edge (+0.063 vs +0.083/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.918 vs 0.579); relationships: KXNHLSPREAD-26NOV12CARSEA-CAR3|no: MOSTLY_INDEPENDENT (phi 0.127); KXNHLGOAL-26NOV12CARSEA-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: SEA offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes; why: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes has the higher standalone adjusted growth (22.44 vs 8.39 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.254); relationships: KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.127); KXNHLGOAL-26NOV12CARSEA-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.141); failure: CAR wins by 2+
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12CARSEA-SEA2|yes; why: KXNHLSPREAD-26NOV12CARSEA-SEA2|yes has the higher standalone adjusted growth (13.11 vs 6.63 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.117); relationships: KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLSPREAD-26NOV12CARSEA-CAR3|no: MOSTLY_INDEPENDENT (phi 0.141); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis SEA:OFFENSE_4PLUS (p 0.3713): highest fidelity KXNHLTEAMTOTAL-26NOV12CARSEA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.2174): highest fidelity KXNHLSPREAD-26NOV12CARSEA-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4174): highest fidelity KXNHLSPREAD-26NOV12CARSEA-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes — Broad expression KXNHLSPREAD-26NOV12CARSEA-CAR2|no selected over broad KXNHLTEAMTOTAL-26NOV12CARSEA-CAR5|no because adjusted EV is 0.7 pts higher while thesis capture is 1.00 vs 0.95 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4045, phi -0.223)
- KXNHLSPREAD-26NOV12CARSEA-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.7 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3658, phi -0.756)
- KXNHLGOAL-26NOV12CARSEA-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4916, phi -0.206)
- override: Broad expression KXNHLSPREAD-26NOV12CARSEA-CAR2|no selected over broad KXNHLTEAMTOTAL-26NOV12CARSEA-CAR5|no because adjusted EV is 0.7 pts higher while thesis capture is 1.00 vs 0.95 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.40 (adj +0.75) on $16.70, P(profit) 0.5979, adj growth 6.7 bp · B EV +3.83 (adj +2.01) on $20.81, P(profit) 0.6759, adj growth 18.9 bp · C EV +7.86 (adj +4.25) on $16.27, P(profit) 0.4135, adj growth 36.9 bp · R EV +0.56 (adj +0.19) on $5.00, P(profit) 0.6069, adj growth 7.3 bp
equivalent contracts collapsed: KXNHLGAME-26NOV12CARSEA-SEA|yes == KXNHLGAME-26NOV12CARSEA-CAR|no

## MTL @ BOS  ·  10000 joint draws  ·  422 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_MTL_win | p_overtime | goals | shots BOS/MTL | BOS/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.64 | 0.36 | 0.00 | 6.06 | 27.5/27.4 | 24.5/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.53 | 0.47 | 0.47 | 5.91 | 27.8/27.7 | 24.4/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.65 | 0.35 | 0.00 | 9.44 | 29.3/29.2 | 23.7/22.3 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.080 | 0.66 | 0.34 | 0.00 | 6.05 | 32.6/21.8 | 19.2/28.0 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.066 | 0.70 | 0.30 | 0.00 | 9.46 | 34.5/23.6 | 18.8/26.1 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.53 | 0.47 | 0.47 | 6.05 | 32.6/22.1 | 18.9/29.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Borgen: 1+ goals YES | 6 | 0.090 | 0.082 | +0.026 | +0.018 | $2.00 | FUNDED_RESEARCH | $1 | BOS:WINS_BY_2PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Fraser Minten: 1+ goals YES | 18 | 0.226 | 0.213 | +0.036 | +0.023 | $3.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Nick Suzuki: 2+ assists NO | 86 | 0.922 | 0.884 | +0.054 | +0.015 | $9.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Michael Eyssimont: 1+ goals YES | 14 | 0.167 | 0.159 | +0.019 | +0.011 | $1.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes; why: higher confidence-adjusted growth (12.09 vs 2.47 bp); despite a smaller raw edge (+0.026 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.754 vs 0.517); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-2|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV12MTLBOS-BOSMEYSSIMONT81-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: MTL wins (incl. OT/SO)
- **Fraser Minten: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV12MTLBOS-9|yes; why: higher confidence-adjusted growth (7.42 vs 2.52 bp); despite a smaller raw edge (+0.036 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.843 vs 0.374); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-2|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV12MTLBOS-BOSMEYSSIMONT81-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: BOS offense suppressed (<= 2 goals)
- **Nick Suzuki: 2+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no; why: higher confidence-adjusted growth (4.49 vs 1.81 bp); despite a smaller raw edge (+0.054 vs +0.101/contract); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV12MTLBOS-BOSMEYSSIMONT81-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: MTL offense succeeds (4+ goals)
- **Michael Eyssimont: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes has the higher standalone adjusted growth (7.42 vs 2.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-2|no: MOSTLY_INDEPENDENT (phi -0.0); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:WINS_BY_2PLUS (p 0.3719): highest fidelity KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS4|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4927): highest fidelity KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3212): highest fidelity KXNHLTOTAL-26NOV12MTLBOS-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:WINS (p 0.4134, phi -0.172)
- KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3043, phi -0.2)
- KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3668, phi -0.222)
- KXNHLGOAL-26NOV12MTLBOS-BOSMEYSSIMONT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3043, phi -0.156)

portfolios: A EV +2.71 (adj +0.65) on $16.70, P(profit) 0.4418, adj growth 5.7 bp · B EV +2.12 (adj +1.20) on $15.50, P(profit) 0.4032, adj growth 11.3 bp · C EV +4.84 (adj +2.25) on $20.75, P(profit) 0.3625, adj growth 19.6 bp · R EV +0.41 (adj +0.29) on $1.00, P(profit) 0.0899, adj growth 10.0 bp

## MIN @ TOR  ·  10000 joint draws  ·  394 bet sides mapped, 18 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_MIN_win | p_overtime | goals | shots TOR/MIN | TOR/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.52 | 0.48 | 0.00 | 6.12 | 29.0/29.5 | 26.0/25.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.51 | 0.49 | 0.46 | 5.98 | 29.3/29.8 | 26.5/25.8 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.098 | 0.45 | 0.55 | 0.00 | 5.99 | 23.1/35.2 | 31.2/20.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.56 | 0.44 | 0.00 | 9.35 | 30.7/31.1 | 25.1/24.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.50 | 0.50 | 0.46 | 5.96 | 23.1/35.1 | 31.7/19.9 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.070 | 0.47 | 0.53 | 0.00 | 9.34 | 24.9/37.0 | 29.7/19.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 10 | 0.177 | 0.154 | +0.071 | +0.048 | $4.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:WINS_BY_2PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 54 | 0.625 | 0.601 | +0.068 | +0.044 | $9.10 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ goals YES | 18 | 0.241 | 0.225 | +0.051 | +0.034 | $4.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Dakota Joshua: 1+ goals YES | 10 | 0.141 | 0.129 | +0.034 | +0.023 | $2.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR wins by 2+; alternative: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no; why: higher confidence-adjusted growth (50.40 vs 17.10 bp); relationships: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV12MINTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: TOR offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12MINTOR-MIN3|no; why: higher confidence-adjusted growth (17.10 vs 7.03 bp); despite a smaller raw edge (+0.068 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV12MINTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: MIN offense succeeds (4+ goals)
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (50.40 vs 16.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV12MINTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: TOR offense suppressed (<= 2 goals)
- **Dakota Joshua: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (50.40 vs 11.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TOR:WINS_BY_2PLUS (p 0.2952): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:OFFENSE_4PLUS (p 0.4208): highest fidelity KXNHLTEAMTOTAL-26NOV12MINTOR-TOR4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3784): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3606, phi -0.199)
- KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4038, phi -0.292)
- KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3606, phi -0.22)
- KXNHLGOAL-26NOV12MINTOR-TORDJOSHUA81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3606, phi -0.174)

portfolios: A EV +4.18 (adj +0.70) on $16.70, P(profit) 0.6188, adj growth 5.9 bp · B EV +6.42 (adj +4.29) on $21.00, P(profit) 0.4615, adj growth 40.1 bp · C EV +9.08 (adj +6.07) on $28.68, P(profit) 0.6873, adj growth 52.7 bp · R EV +0.36 (adj +0.24) on $3.00, P(profit) 0.625, adj growth 8.9 bp
equivalent contracts collapsed: KXNHLGAME-26NOV12MINTOR-TOR|yes == KXNHLGAME-26NOV12MINTOR-MIN|no

## COL @ OTT  ·  10000 joint draws  ·  434 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_COL_win | p_overtime | goals | shots OTT/COL | OTT/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.45 | 0.55 | 0.00 | 6.03 | 27.7/28.0 | 24.3/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.49 | 0.51 | 0.48 | 6.01 | 27.7/27.9 | 24.5/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.46 | 0.54 | 0.00 | 9.38 | 29.2/29.4 | 23.1/23.4 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.082 | 0.38 | 0.62 | 0.00 | 6.0 | 22.3/33.0 | 28.9/19.4 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.46 | 0.54 | 0.44 | 6.03 | 22.3/33.2 | 29.5/18.9 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.061 | 0.40 | 0.60 | 0.00 | 9.3 | 23.6/34.5 | 27.0/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ridly Greig: 1+ goals YES | 16 | 0.208 | 0.191 | +0.039 | +0.022 | $2.78 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Fabian Zetterlund: 1+ goals YES | 19 | 0.223 | 0.212 | +0.022 | +0.011 | $1.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes; why: higher confidence-adjusted growth (7.36 vs 1.79 bp); relationships: KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: OTT offense suppressed (<= 2 goals)
- **Fabian Zetterlund: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes has the higher standalone adjusted growth (7.36 vs 1.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.4015): highest fidelity KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3855, phi -0.209)
- KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3855, phi -0.214)

portfolios: A EV +1.16 (adj +0.64) on $6.24, P(profit) 0.3856, adj growth 5.8 bp · B EV +0.82 (adj +0.45) on $4.36, P(profit) 0.3856, adj growth 4.2 bp · C EV +1.30 (adj +0.73) on $5.63, P(profit) 0.2084, adj growth 6.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ NJD  ·  10000 joint draws  ·  416 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_WSH_win | p_overtime | goals | shots NJD/WSH | NJD/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.126 | 0.63 | 0.37 | 0.00 | 6.05 | 33.6/21.6 | 18.7/29.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.57 | 0.43 | 0.00 | 6.07 | 28.1/27.5 | 24.2/24.2 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.55 | 0.45 | 0.47 | 5.9 | 33.9/22.0 | 18.9/30.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.51 | 0.49 | 0.49 | 5.97 | 28.2/27.5 | 24.2/24.8 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.083 | 0.64 | 0.36 | 0.00 | 9.29 | 35.3/23.1 | 18.2/27.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.58 | 0.41 | 0.00 | 9.34 | 29.9/29.0 | 23.3/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cody Glass: 1+ goals YES | 12 | 0.169 | 0.154 | +0.042 | +0.027 | $3.23 | FUNDED_RESEARCH | $1 | NJD:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.224 | 0.209 | +0.044 | +0.030 | $3.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12WSHNJ-NJBPESCE22-1|yes; why: higher confidence-adjusted growth (13.90 vs 0.47 bp); despite a smaller raw edge (+0.042 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: NJD offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-WSHAOVECHKIN8-1|yes; why: higher confidence-adjusted growth (12.80 vs 1.01 bp); alternative not eligible: confidence-adjusted EV +0.0088 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3457): highest fidelity KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.4391): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3539, phi -0.176)
- KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4344, phi -0.238)

portfolios: A EV +2.42 (adj +1.58) on $8.50, P(profit) 0.3584, adj growth 14.6 bp · B EV +2.02 (adj +1.32) on $7.14, P(profit) 0.3584, adj growth 12.4 bp · C EV +1.93 (adj +1.29) on $7.82, P(profit) 0.2243, adj growth 11.2 bp · R EV +0.33 (adj +0.21) on $1.00, P(profit) 0.169, adj growth 7.7 bp

## TBL @ CBJ  ·  10000 joint draws  ·  420 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_TBL_win | p_overtime | goals | shots CBJ/TBL | CBJ/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.54 | 0.46 | 0.00 | 6.0 | 27.1/27.4 | 24.0/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.54 | 0.46 | 0.48 | 5.84 | 27.0/27.4 | 24.3/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.54 | 0.46 | 0.00 | 9.14 | 28.4/28.7 | 23.1/22.4 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.080 | 0.49 | 0.51 | 0.00 | 6.01 | 21.5/32.2 | 28.6/18.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.48 | 0.52 | 0.47 | 5.86 | 21.9/32.5 | 29.1/18.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.51 | 0.49 | 0.00 | 3.49 | 25.9/25.9 | 24.0/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 16 | 0.213 | 0.198 | +0.043 | +0.029 | $3.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Yanni Gourde: 1+ goals NO | 86 | 0.902 | 0.890 | +0.034 | +0.022 | $9.10 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 23 | 0.270 | 0.258 | +0.027 | +0.016 | $2.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Full Game: Over 5.5 goals scored NO | 40 | 0.461 | 0.428 | +0.044 | +0.011 | $3.54 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12TBCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (12.88 vs 3.02 bp); relationships: KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV12TBCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLTOTAL-26NOV12TBCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.163); failure: CBJ offense suppressed (<= 2 goals)
- **Yanni Gourde: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV12TBCBJ-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (9.40 vs 1.72 bp); despite a smaller raw edge (+0.034 vs +0.136/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV12TBCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLTOTAL-26NOV12TBCBJ-6|no: MOSTLY_INDEPENDENT (phi 0.123); failure: TBL offense succeeds (4+ goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (12.88 vs 3.02 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLTOTAL-26NOV12TBCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.164); failure: CBJ offense suppressed (<= 2 goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTEAMTOTAL-26NOV12TBCBJ-TB4|no; why: KXNHLTEAMTOTAL-26NOV12TBCBJ-TB4|no has the higher standalone adjusted growth (1.15 vs 1.11 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.509); relationships: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.163); KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi 0.123); KXNHLGOAL-26NOV12TBCBJ-CBJCCOYLE3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.164); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3803): highest fidelity KXNHLGOAL-26NOV12TBCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.4287): highest fidelity KXNHLTEAMTOTAL-26NOV12TBCBJ-TB4|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV12TBCBJ-TBNKUCHEROV86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:LOW_EVENT (p 0.2556): highest fidelity KXNHLTOTAL-26NOV12TBCBJ-6|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12TBCBJ-TB4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.397, phi -0.232)
- KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3491, phi -0.167)
- KXNHLGOAL-26NOV12TBCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.397, phi -0.238)
- KXNHLTOTAL-26NOV12TBCBJ-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2445, phi -0.526)

portfolios: A EV +3.07 (adj +0.88) on $16.70, P(profit) 0.6747, adj growth 8.0 bp · B EV +2.04 (adj +1.18) on $19.25, P(profit) 0.4042, adj growth 11.1 bp · C EV +3.76 (adj +1.52) on $16.25, P(profit) 0.5491, adj growth 13.3 bp · R EV +0.22 (adj +0.10) on $4.00, P(profit) 0.4339, adj growth 3.9 bp

## DET @ FLA  ·  10000 joint draws  ·  416 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_DET_win | p_overtime | goals | shots FLA/DET | FLA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.62 | 0.38 | 0.00 | 6.03 | 27.3/27.3 | 24.3/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.51 | 0.49 | 0.49 | 6.0 | 27.6/27.6 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.59 | 0.41 | 0.00 | 9.28 | 29.2/28.9 | 23.1/22.4 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.076 | 0.67 | 0.33 | 0.00 | 6.0 | 32.5/21.8 | 19.2/28.0 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.58 | 0.42 | 0.47 | 5.94 | 32.5/22.1 | 18.7/29.0 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.057 | 0.57 | 0.43 | 0.00 | 6.01 | 22.3/32.7 | 29.2/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Bennett: 1+ goals YES | 27 | 0.315 | 0.301 | +0.031 | +0.018 | $2.49 | FUNDED_RESEARCH | $1 | FLA:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Aaron Ekblad: 1+ assists YES | 27 | 0.338 | 0.299 | +0.054 | +0.015 | $1.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| J.T. Compher: 1+ goals YES | 13 | 0.157 | 0.149 | +0.019 | +0.011 | $1.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Sam Bennett: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes; why: higher confidence-adjusted growth (3.32 vs 2.40 bp); despite a smaller raw edge (+0.031 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes: MOSTLY_INDEPENDENT (phi 0.118); KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: FLA offense suppressed (<= 2 goals)
- **Aaron Ekblad: 1+ assists YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes has the higher standalone adjusted growth (3.32 vs 2.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.118); they share one thesis budget; relationships: KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi 0.118); KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: FLA offense suppressed (<= 2 goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12DETFLA-DETACOPP18-1|yes; why: higher confidence-adjusted growth (2.09 vs 0.65 bp); alternative not eligible: confidence-adjusted EV +0.0063 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:OFFENSE_4PLUS (p 0.4406): highest fidelity KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:OFFENSE_4PLUS (p 0.3339): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3371, phi -0.23)
- KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3371, phi -0.242)
- KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4467, phi -0.19)

portfolios: A EV +1.83 (adj +0.70) on $11.72, P(profit) 0.5958, adj growth 6.1 bp · B EV +0.82 (adj +0.36) on $5.73, P(profit) 0.5958, adj growth 3.4 bp · C EV +0.61 (adj +0.34) on $5.50, P(profit) 0.3152, adj growth 3.0 bp · R EV +0.11 (adj +0.06) on $1.00, P(profit) 0.3152, adj growth 2.3 bp

## BUF @ CHI  ·  10000 joint draws  ·  412 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_BUF_win | p_overtime | goals | shots CHI/BUF | CHI/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.51 | 0.49 | 0.00 | 5.99 | 26.9/27.4 | 23.9/23.2 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.110 | 0.44 | 0.56 | 0.00 | 5.98 | 21.6/33.2 | 29.2/18.4 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.48 | 0.52 | 0.47 | 5.98 | 21.5/33.2 | 29.9/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.52 | 0.48 | 0.48 | 5.94 | 27.3/28.0 | 24.6/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.49 | 0.51 | 0.00 | 9.21 | 28.5/29.2 | 23.1/22.6 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.077 | 0.42 | 0.58 | 0.00 | 9.23 | 22.9/34.8 | 27.4/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tage Thompson: 2+ goals NO | 90 | 0.932 | 0.922 | +0.026 | +0.016 | $8.18 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 1.5 goals NO | 64 | 0.709 | 0.672 | +0.053 | +0.016 | $3.21 | FUNDED_RESEARCH | $1 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo over 3.5 goals scored NO | 53 | 0.603 | 0.561 | +0.055 | +0.014 | $1.11 | FUNDED_RESEARCH | $1 | BUF:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 2.5 goals NO | 76 | 0.818 | 0.784 | +0.045 | +0.011 | $1.14 | FUNDED_RESEARCH | $1 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tage Thompson: 2+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no; why: higher confidence-adjusted growth (6.36 vs 2.50 bp); despite a smaller raw edge (+0.026 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: MOSTLY_INDEPENDENT (phi 0.145); KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no: REINFORCING (phi 0.207); KXNHLSPREAD-26NOV12BUFCHI-BUF3|no: MOSTLY_INDEPENDENT (phi 0.146); failure: BUF offense succeeds (4+ goals)
- **Buffalo wins by over 1.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV12BUFCHI-CHI2|yes; why: higher confidence-adjusted growth (2.50 vs 2.14 bp); wins across more scripts (relative breadth 0.935 vs 0.551); relationships: KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-2|no: MOSTLY_INDEPENDENT (phi 0.145); KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no: REINFORCING (phi 0.542); KXNHLSPREAD-26NOV12BUFCHI-BUF3|no: DUPLICATIVE (phi 0.737); failure: BUF wins by 2+
- **Buffalo over 3.5 goals scored NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no; why: Broad expression KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no selected over player prop KXNHLAST-26NOV12BUFCHI-BUFTTHOMPSON72-1|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.82 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-2|no: REINFORCING (phi 0.207); KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: REINFORCING (phi 0.542); KXNHLSPREAD-26NOV12BUFCHI-BUF3|no: DUPLICATIVE (phi 0.502); failure: BUF offense succeeds (4+ goals)
- **Buffalo wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no has the higher standalone adjusted growth (2.50 vs 1.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.737); they share one thesis budget; relationships: KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-2|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: DUPLICATIVE (phi 0.737); KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no: DUPLICATIVE (phi 0.502); failure: BUF wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis BUF:SUPPRESSED (p 0.3929): highest fidelity KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV12BUFCHI-BUF2|no — Broad expression KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no selected over player prop KXNHLAST-26NOV12BUFCHI-BUFTTHOMPSON72-1|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.82 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CHI:WINS (p 0.4925): highest fidelity KXNHLSPREAD-26NOV12BUFCHI-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV12BUFCHI-BUF2|no (same contract)
- thesis CHI:WINS_BY_2PLUS (p 0.2755): highest fidelity KXNHLSPREAD-26NOV12BUFCHI-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV12BUFCHI-BUF2|no (same contract)
- KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3875, phi -0.21)
- KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2907, phi -1.0)
- KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3875, phi -0.979)
- KXNHLSPREAD-26NOV12BUFCHI-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2907, phi -0.737)
- override: Broad expression KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no selected over player prop KXNHLAST-26NOV12BUFCHI-BUFTTHOMPSON72-1|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.82 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.35 (adj +0.35) on $16.70, P(profit) 0.6613, adj growth 3.1 bp · B EV +0.68 (adj +0.26) on $13.65, P(profit) 0.6779, adj growth 2.5 bp · C EV +0.92 (adj +0.28) on $11.38, P(profit) 0.7093, adj growth 2.5 bp · R EV +0.33 (adj +0.12) on $6.00, P(profit) 0.7152, adj growth 4.3 bp

## WPG @ DAL  ·  10000 joint draws  ·  404 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_WPG_win | p_overtime | goals | shots DAL/WPG | DAL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.63 | 0.37 | 0.00 | 6.0 | 25.8/25.6 | 22.8/21.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.48 | 5.88 | 26.2/25.9 | 22.7/23.0 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.092 | 0.68 | 0.32 | 0.00 | 5.96 | 30.8/20.4 | 17.9/26.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.64 | 0.36 | 0.00 | 9.27 | 27.7/27.5 | 22.2/21.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.57 | 0.43 | 0.47 | 5.89 | 31.0/20.8 | 17.8/27.6 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.059 | 0.69 | 0.31 | 0.00 | 9.07 | 32.3/21.7 | 17.1/25.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Arttu Hyry: 1+ goals YES | 15 | 0.192 | 0.180 | +0.033 | +0.022 | $2.74 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DAL:WINS_BY_2PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Josh Morrissey: 1+ assists NO | 61 | 0.749 | 0.649 | +0.122 | +0.022 | $7.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Arttu Hyry: 1+ goals YES** — thesis: DAL wins by 2+; alternative: KXNHLPTS-26NOV12WPGDAL-DALAHYRY25-1|yes; why: higher confidence-adjusted growth (7.50 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: DAL offense suppressed (<= 2 goals)
- **Josh Morrissey: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12WPGDAL-WPGJMORRISSEY44-1|no; why: higher confidence-adjusted growth (4.61 vs 0.12 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: WPG offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis DAL:WINS_BY_2PLUS (p 0.3564): highest fidelity KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes (same contract)
- thesis WPG:SUPPRESSED (p 0.4789): highest fidelity KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no (same contract)
- KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3491, phi -0.21)
- KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.4 pts; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3045, phi -0.233)

portfolios: A EV +2.00 (adj +0.69) on $9.99, P(profit) 0.7967, adj growth 6.4 bp · B EV +2.12 (adj +0.65) on $10.65, P(profit) 0.7967, adj growth 6.1 bp · C EV +4.29 (adj +1.32) on $21.56, P(profit) 0.7967, adj growth 11.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ UTA  ·  10000 joint draws  ·  400 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_STL_win | p_overtime | goals | shots UTA/STL | UTA/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.52 | 0.48 | 0.00 | 6.0 | 27.1/27.0 | 23.4/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.49 | 5.94 | 27.3/27.0 | 23.7/24.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.102 | 0.61 | 0.39 | 0.00 | 6.05 | 32.4/21.4 | 18.5/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.52 | 0.48 | 0.00 | 9.34 | 29.1/28.7 | 22.8/23.0 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.56 | 0.44 | 0.45 | 5.92 | 32.6/21.5 | 18.4/29.1 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.071 | 0.64 | 0.36 | 0.00 | 9.2 | 33.9/22.8 | 17.9/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 19 | 0.246 | 0.230 | +0.045 | +0.029 | $3.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 14 | 0.182 | 0.171 | +0.034 | +0.022 | $2.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 13 | 0.162 | 0.151 | +0.024 | +0.014 | $1.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Daniil But: 1+ goals NO | 81 | 0.846 | 0.835 | +0.025 | +0.014 | $9.10 | FUNDED_RESEARCH | $3 | UTA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12STLUTA-UTABHAYTON27-1|yes; why: higher confidence-adjusted growth (11.23 vs 1.77 bp); despite a smaller raw edge (+0.045 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV12STLUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: UTA offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (11.23 vs 8.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12STLUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: UTA offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV12STLUTA-STL6|yes; why: higher confidence-adjusted growth (3.36 vs 0.36 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.885 vs 0.339); alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12STLUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: STL offense suppressed (<= 2 goals)
- **Daniil But: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV12STLUTA-UTACKELLER9-1|no; why: higher confidence-adjusted growth (2.88 vs 0.00 bp); despite a smaller raw edge (+0.025 vs +0.065/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.4237): highest fidelity KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.3803): highest fidelity KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3627): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.231)
- KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.187)
- KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4013, phi -0.208)
- KXNHLGOAL-26NOV12STLUTA-UTADBUT19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4237, phi -0.192)

portfolios: A EV +3.22 (adj +1.38) on $16.70, P(profit) 0.7102, adj growth 12.4 bp · B EV +2.09 (adj +1.29) on $17.43, P(profit) 0.4701, adj growth 12.1 bp · C EV +2.38 (adj +1.47) on $11.28, P(profit) 0.3691, adj growth 12.9 bp · R EV +0.09 (adj +0.05) on $3.00, P(profit) 0.8462, adj growth 1.9 bp

## NYI @ LAK  ·  10000 joint draws  ·  384 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_NYI_win | p_overtime | goals | shots LAK/NYI | LAK/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 5.98 | 27.8/27.6 | 24.4/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.86 | 27.8/27.5 | 24.4/24.6 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.086 | 0.60 | 0.40 | 0.00 | 5.98 | 32.9/22.3 | 19.3/28.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.56 | 0.44 | 0.50 | 5.87 | 33.1/22.2 | 19.0/29.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.59 | 0.41 | 0.00 | 9.25 | 29.4/29.2 | 23.9/22.7 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.46 | 2.83 | 26.4/26.2 | 24.7/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mats Zuccarello: 1+ assists NO | 66 | 0.851 | 0.717 | +0.175 | +0.041 | $9.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Andre Lee: 1+ goals YES | 9 | 0.132 | 0.115 | +0.036 | +0.019 | $2.21 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Alex Laferriere: 1+ goals YES | 27 | 0.312 | 0.299 | +0.029 | +0.016 | $2.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no; why: higher confidence-adjusted growth (17.21 vs 0.03 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0019 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.061); failure: LAK offense succeeds (4+ goals)
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (9.28 vs 2.60 bp); relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: LAK offense suppressed (<= 2 goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (2.60 vs 0.00 bp); despite a smaller raw edge (+0.029 vs +0.050/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.061); KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.386): highest fidelity KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes (same contract)
- thesis LAK:SUPPRESSED (p 0.395): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.6 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.386, phi -0.181)
- KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.16)
- KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.261)

portfolios: A EV +3.32 (adj +1.27) on $13.36, P(profit) 0.3569, adj growth 11.8 bp · B EV +3.45 (adj +1.14) on $13.87, P(profit) 0.3569, adj growth 11.0 bp · C EV +0.49 (adj +0.27) on $4.88, P(profit) 0.3125, adj growth 2.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
