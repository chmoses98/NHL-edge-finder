# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-12T16:42:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.97 | +30.96 | +11.05 | +28.96 | 0.733 | -28.19 | -42.93 | 99.38 |
| B thesis-diversified (joint) ← optimiser card | 148.20 | +34.41 | +18.79 | +30.75 | 0.712 | -36.03 | -51.48 | 171.43 |
| C best expression per thesis | 142.82 | +32.30 | +17.07 | +27.07 | 0.653 | -49.96 | -69.74 | 147.68 |
| R FUNDED research stakes | 14.00 | +3.04 | +1.62 | +1.12 | 0.548 | -7.14 | -9.33 | 0.00 |

## CAR @ SEA  ·  10000 joint draws  ·  480 bet sides mapped, 33 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CAR_win | p_overtime | goals | shots SEA/CAR | SEA/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.159 | 0.34 | 0.66 | 0.00 | 6.02 | 21.3/34.2 | 29.6/18.5 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.136 | 0.35 | 0.65 | 0.00 | 9.43 | 22.7/36.3 | 28.5/17.8 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.135 | 0.45 | 0.55 | 0.49 | 5.94 | 21.4/34.3 | 30.8/18.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.089 | 0.40 | 0.60 | 0.00 | 6.06 | 26.6/27.8 | 23.7/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.39 | 0.61 | 0.00 | 9.45 | 28.5/29.6 | 22.5/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.49 | 0.51 | 0.47 | 6.01 | 26.9/28.0 | 24.6/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jani Nyman: 1+ goals YES | 9 | 0.150 | 0.132 | +0.055 | +0.036 | $5.30 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 15 | 0.221 | 0.201 | +0.062 | +0.042 | $7.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Kaapo Kakko: 1+ goals YES | 13 | 0.191 | 0.174 | +0.053 | +0.036 | $5.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 62 | 0.751 | 0.662 | +0.114 | +0.026 | $5.26 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Jani Nyman: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes; why: higher confidence-adjusted growth (31.20 vs 28.33 bp); despite a smaller raw edge (+0.055 vs +0.062/contract); relationships: KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV12CARSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26NOV12CARSEA-CAR3|no: MOSTLY_INDEPENDENT (phi 0.103); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12CARSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (28.33 vs 23.71 bp); relationships: KXNHLGOAL-26NOV12CARSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV12CARSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26NOV12CARSEA-CAR3|no: MOSTLY_INDEPENDENT (phi 0.137); failure: SEA offense suppressed (<= 2 goals)
- **Kaapo Kakko: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes has the higher standalone adjusted growth (28.33 vs 23.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26NOV12CARSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26NOV12CARSEA-CAR3|no: MOSTLY_INDEPENDENT (phi 0.124); failure: SEA offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA6|yes; why: Broad expression KXNHLSPREAD-26NOV12CARSEA-CAR3|no selected over player prop KXNHLAST-26NOV12CARSEA-CARSAHO20-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV12CARSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.103); KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.137); KXNHLGOAL-26NOV12CARSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.124); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · high event (8+) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13.
- thesis SEA:OFFENSE_4PLUS (p 0.3669): highest fidelity KXNHLTEAMTOTAL-26NOV12CARSEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.325): highest fidelity KXNHLTEAMTOTAL-26NOV12CARSEA-SEA2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.2215): highest fidelity KXNHLSPREAD-26NOV12CARSEA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12CARSEA-SEAJNYMAN38-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4117, phi -0.182)
- KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4117, phi -0.226)
- KXNHLGOAL-26NOV12CARSEA-SEAKKAKKO84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4117, phi -0.213)
- KXNHLSPREAD-26NOV12CARSEA-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.6 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3676, phi -0.756)
- override: Broad expression KXNHLSPREAD-26NOV12CARSEA-CAR3|no selected over player prop KXNHLAST-26NOV12CARSEA-CARSAHO20-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.86 (adj +0.87) on $17.40, P(profit) 0.5481, adj growth 7.8 bp · B EV +9.01 (adj +5.63) on $23.54, P(profit) 0.4622, adj growth 50.9 bp · C EV +8.12 (adj +4.34) on $15.37, P(profit) 0.3785, adj growth 37.0 bp · R EV +1.50 (adj +0.83) on $4.00, P(profit) 0.1504, adj growth 28.6 bp
equivalent contracts collapsed: KXNHLGAME-26NOV12CARSEA-SEA|yes == KXNHLGAME-26NOV12CARSEA-CAR|no

## MTL @ BOS  ·  10000 joint draws  ·  424 bet sides mapped, 11 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_MTL_win | p_overtime | goals | shots BOS/MTL | BOS/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.65 | 0.35 | 0.00 | 6.06 | 27.5/27.4 | 24.3/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.64 | 0.36 | 0.00 | 9.45 | 29.4/29.3 | 23.9/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.51 | 0.49 | 0.49 | 5.95 | 27.7/27.7 | 24.5/24.5 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.080 | 0.67 | 0.33 | 0.00 | 6.03 | 32.6/22.0 | 19.3/27.8 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.067 | 0.72 | 0.28 | 0.00 | 9.37 | 34.5/23.5 | 19.1/26.4 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.59 | 0.41 | 0.46 | 5.99 | 32.8/21.9 | 18.9/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Borgen: 1+ goals YES | 6 | 0.088 | 0.081 | +0.025 | +0.017 | $2.65 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:WINS_BY_2PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Fraser Minten: 1+ goals YES | 18 | 0.225 | 0.213 | +0.035 | +0.022 | $4.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Hampus Lindholm: 1+ goals YES | 6 | 0.081 | 0.075 | +0.017 | +0.011 | $1.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes; why: higher confidence-adjusted growth (10.69 vs 2.69 bp); despite a smaller raw edge (+0.025 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.699 vs 0.512); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV12MTLBOS-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: MTL wins (incl. OT/SO)
- **Fraser Minten: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes; why: higher confidence-adjusted growth (7.04 vs 6.61 bp); despite a smaller raw edge (+0.035 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV12MTLBOS-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: BOS offense suppressed (<= 2 goals)
- **Hampus Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes has the higher standalone adjusted growth (7.04 vs 4.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis BOS:WINS_BY_2PLUS (p 0.3718): highest fidelity KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS4|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4929): highest fidelity KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS4|yes [STRUCTURAL], best adjusted EV KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes — Broad expression KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes selected over player prop KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.62 vs 0.42 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis MTL:SUPPRESSED (p 0.4271): highest fidelity KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no (same contract)
- KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:WINS (p 0.4068, phi -0.151)
- KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3042, phi -0.206)
- KXNHLGOAL-26NOV12MTLBOS-BOSHLINDHOLM27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3042, phi -0.091)
- override: Broad expression KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes selected over player prop KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.62 vs 0.42 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.42 (adj +0.92) on $17.40, P(profit) 0.5601, adj growth 8.0 bp · B EV +2.21 (adj +1.48) on $8.42, P(profit) 0.3504, adj growth 13.4 bp · C EV +5.18 (adj +2.26) on $22.36, P(profit) 0.4005, adj growth 19.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ TOR  ·  10000 joint draws  ·  402 bet sides mapped, 22 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_MIN_win | p_overtime | goals | shots TOR/MIN | TOR/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.52 | 0.48 | 0.00 | 6.05 | 29.0/29.5 | 26.1/25.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.45 | 5.97 | 29.2/29.5 | 26.1/25.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.51 | 0.49 | 0.00 | 9.4 | 30.4/31.2 | 25.2/23.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.095 | 0.48 | 0.52 | 0.00 | 6.05 | 23.3/35.0 | 31.1/19.9 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.49 | 0.51 | 0.47 | 5.88 | 23.4/35.2 | 31.9/20.1 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.069 | 0.45 | 0.55 | 0.00 | 9.31 | 25.0/37.1 | 30.0/19.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kirill Kaprizov: 1+ goals NO | 54 | 0.628 | 0.605 | +0.071 | +0.048 | $13.10 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ goals YES | 18 | 0.243 | 0.226 | +0.052 | +0.035 | $6.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 10 | 0.135 | 0.120 | +0.029 | +0.014 | $2.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Jack Roslovic: 1+ goals YES | 25 | 0.290 | 0.279 | +0.027 | +0.016 | $3.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12MINTOR-TOR2|yes; why: higher confidence-adjusted growth (20.20 vs 11.68 bp); despite a smaller raw edge (+0.071 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.032 vs 0.526); relationships: KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV12MINTOR-TORJROSLOVIC96-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: MIN offense succeeds (4+ goals)
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV12MINTOR-TOR2|yes; why: higher confidence-adjusted growth (17.61 vs 11.68 bp); despite a smaller raw edge (+0.052 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.89 vs 0.526); relationships: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV12MINTOR-TORJROSLOVIC96-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: TOR offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV12MINTOR-MINJBRODIN25-1|yes; why: higher confidence-adjusted growth (4.26 vs 0.00 bp); despite a smaller raw edge (+0.029 vs +0.036/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV12MINTOR-TORJROSLOVIC96-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: MIN offense suppressed (<= 2 goals)
- **Jack Roslovic: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes; why: Player prop expression KXNHLGOAL-26NOV12MINTOR-TORJROSLOVIC96-1|yes selected over player prop KXNHLAST-26NOV12MINTOR-TORECOWAN53-1|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.41 vs 0.57 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:SUPPRESSED (p 0.384): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS (p 0.5074): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:OFFENSE_4PLUS (p 0.411): highest fidelity KXNHLTEAMTOTAL-26NOV12MINTOR-TOR4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes — Player prop expression KXNHLGOAL-26NOV12MINTOR-TORJROSLOVIC96-1|yes selected over player prop KXNHLAST-26NOV12MINTOR-TORECOWAN53-1|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.41 vs 0.57 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3978, phi -0.285)
- KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3739, phi -0.213)
- KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.384, phi -0.163)
- KXNHLGOAL-26NOV12MINTOR-TORJROSLOVIC96-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3739, phi -0.236)
- override: Player prop expression KXNHLGOAL-26NOV12MINTOR-TORJROSLOVIC96-1|yes selected over player prop KXNHLAST-26NOV12MINTOR-TORECOWAN53-1|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.41 vs 0.57 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.47 (adj +1.00) on $17.40, P(profit) 0.6174, adj growth 8.7 bp · B EV +4.45 (adj +2.85) on $25.33, P(profit) 0.4368, adj growth 26.3 bp · C EV +7.45 (adj +4.33) on $37.32, P(profit) 0.4544, adj growth 38.1 bp · R EV +0.51 (adj +0.34) on $4.00, P(profit) 0.6284, adj growth 12.7 bp
equivalent contracts collapsed: KXNHLGAME-26NOV12MINTOR-TOR|yes == KXNHLGAME-26NOV12MINTOR-MIN|no

## COL @ OTT  ·  10000 joint draws  ·  446 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_COL_win | p_overtime | goals | shots OTT/COL | OTT/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.51 | 0.49 | 0.00 | 6.05 | 27.5/27.9 | 24.3/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.47 | 5.92 | 27.9/28.1 | 24.7/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.53 | 0.47 | 0.00 | 9.36 | 29.2/29.6 | 23.6/22.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.079 | 0.46 | 0.54 | 0.00 | 5.99 | 22.3/33.1 | 29.1/19.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.48 | 0.52 | 0.46 | 5.92 | 22.3/32.9 | 29.5/19.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.054 | 0.55 | 0.45 | 0.00 | 6.04 | 32.0/22.1 | 18.9/28.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Hayden Hodgson: 1+ goals YES | 6 | 0.096 | 0.083 | +0.032 | +0.019 | $2.84 | FUNDED_RESEARCH | $1 | OTT:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Jordan Spence: 1+ goals YES | 6 | 0.088 | 0.079 | +0.025 | +0.015 | $2.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Ridly Greig: 1+ goals YES | 16 | 0.204 | 0.189 | +0.034 | +0.019 | $3.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Fabian Zetterlund: 1+ goals YES | 19 | 0.223 | 0.212 | +0.022 | +0.011 | $2.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Hayden Hodgson: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (13.08 vs 5.87 bp); despite a smaller raw edge (+0.032 vs +0.034/contract); relationships: KXNHLGOAL-26NOV12COLOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: OTT offense suppressed (<= 2 goals)
- **Jordan Spence: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (7.94 vs 5.87 bp); despite a smaller raw edge (+0.025 vs +0.034/contract); relationships: KXNHLGOAL-26NOV12COLOTT-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: OTT offense suppressed (<= 2 goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes; why: higher confidence-adjusted growth (5.87 vs 1.72 bp); relationships: KXNHLGOAL-26NOV12COLOTT-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV12COLOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: OTT offense suppressed (<= 2 goals)
- **Fabian Zetterlund: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes has the higher standalone adjusted growth (5.87 vs 1.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV12COLOTT-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV12COLOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis OTT:OFFENSE_4PLUS (p 0.406): highest fidelity KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12COLOTT-OTTHHODGSON42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3815, phi -0.139)
- KXNHLGOAL-26NOV12COLOTT-OTTJSPENCE10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3815, phi -0.114)
- KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3815, phi -0.202)
- KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3815, phi -0.205)

portfolios: A EV +3.34 (adj +1.97) on $11.22, P(profit) 0.491, adj growth 17.8 bp · B EV +3.28 (adj +1.94) on $11.00, P(profit) 0.491, adj growth 17.5 bp · C EV +1.11 (adj +0.64) on $5.51, P(profit) 0.2036, adj growth 5.5 bp · R EV +0.50 (adj +0.30) on $1.00, P(profit) 0.0959, adj growth 10.4 bp

## WSH @ NJD  ·  10000 joint draws  ·  416 bet sides mapped, 3 +EV candidates, 3 on card


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
| Aliaksei Protas: 1+ goals YES | 17 | 0.224 | 0.209 | +0.044 | +0.030 | $5.64 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 13 | 0.169 | 0.155 | +0.031 | +0.018 | $3.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 18 | 0.211 | 0.201 | +0.021 | +0.011 | $2.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (12.80 vs 1.58 bp); relationships: KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: WSH offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-NJCBROWN16-1|yes; why: higher confidence-adjusted growth (5.62 vs 0.25 bp); alternative not eligible: confidence-adjusted EV +0.0044 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NJD offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (12.80 vs 1.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3457): highest fidelity KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.4391): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4344, phi -0.238)
- KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3539, phi -0.176)
- KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4344, phi -0.226)

portfolios: A EV +2.12 (adj +1.30) on $10.09, P(profit) 0.4967, adj growth 12.0 bp · B EV +2.34 (adj +1.45) on $10.93, P(profit) 0.4967, adj growth 13.2 bp · C EV +2.10 (adj +1.40) on $8.49, P(profit) 0.2243, adj growth 12.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TBL @ CBJ  ·  10000 joint draws  ·  420 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_TBL_win | p_overtime | goals | shots CBJ/TBL | CBJ/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.56 | 0.44 | 0.00 | 6.0 | 27.0/27.2 | 24.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.52 | 0.48 | 0.47 | 5.88 | 27.3/27.5 | 24.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.55 | 0.45 | 0.00 | 9.24 | 28.7/29.0 | 23.3/22.2 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.079 | 0.47 | 0.53 | 0.00 | 5.94 | 21.6/32.3 | 28.5/18.4 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.47 | 0.53 | 0.45 | 5.85 | 21.5/32.3 | 28.8/18.4 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.059 | 0.60 | 0.40 | 0.00 | 6.0 | 31.5/21.5 | 18.6/27.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 16 | 0.213 | 0.196 | +0.044 | +0.027 | $5.10 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 23 | 0.270 | 0.258 | +0.028 | +0.015 | $3.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ assists YES | 25 | 0.311 | 0.278 | +0.048 | +0.015 | $2.53 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
| Full Game: Over 5.5 goals scored NO | 40 | 0.463 | 0.429 | +0.046 | +0.012 | $6.23 | FUNDED_RESEARCH | $2 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV12TBCBJ-TB4|no; why: higher confidence-adjusted growth (11.02 vs 1.71 bp); despite a smaller raw edge (+0.044 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12TBCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV12TBCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.138); KXNHLTOTAL-26NOV12TBCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.152); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (11.02 vs 2.76 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV12TBCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.102); KXNHLTOTAL-26NOV12TBCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.167); failure: CBJ offense suppressed (<= 2 goals)
- **Damon Severson: 1+ assists YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (11.02 vs 2.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.138); they share one thesis budget; relationships: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.138); KXNHLGOAL-26NOV12TBCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.102); KXNHLTOTAL-26NOV12TBCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.171); failure: CBJ offense suppressed (<= 2 goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTEAMTOTAL-26NOV12TBCBJ-TB4|no; why: KXNHLTEAMTOTAL-26NOV12TBCBJ-TB4|no has the higher standalone adjusted growth (1.71 vs 1.33 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.493); relationships: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.152); KXNHLGOAL-26NOV12TBCBJ-CBJCCOYLE3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.167); KXNHLAST-26NOV12TBCBJ-CBJDSEVERSON78-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.171); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:WINS_BY_2PLUS (p 0.3041): highest fidelity KXNHLTEAMTOTAL-26NOV12TBCBJ-TB4|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:OFFENSE_4PLUS (p 0.3795): highest fidelity KXNHLAST-26NOV12TBCBJ-CBJDSEVERSON78-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.4307): highest fidelity KXNHLTEAMTOTAL-26NOV12TBCBJ-TB4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12TBCBJ-TB4|no (same contract)
- KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3983, phi -0.236)
- KXNHLGOAL-26NOV12TBCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3983, phi -0.223)
- KXNHLAST-26NOV12TBCBJ-CBJDSEVERSON78-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3983, phi -0.237)
- KXNHLTOTAL-26NOV12TBCBJ-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2349, phi -0.514)

portfolios: A EV +2.57 (adj +1.02) on $17.40, P(profit) 0.626, adj growth 9.3 bp · B EV +2.88 (adj +1.36) on $17.45, P(profit) 0.4039, adj growth 12.4 bp · C EV +2.55 (adj +1.34) on $15.12, P(profit) 0.2133, adj growth 11.6 bp · R EV +0.22 (adj +0.06) on $2.00, P(profit) 0.4629, adj growth 1.9 bp

## DET @ FLA  ·  10000 joint draws  ·  418 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_DET_win | p_overtime | goals | shots FLA/DET | FLA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.60 | 0.40 | 0.00 | 6.02 | 27.5/27.4 | 24.3/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.50 | 5.93 | 27.7/27.6 | 24.3/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.63 | 0.37 | 0.00 | 9.38 | 29.3/29.0 | 23.7/22.0 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.084 | 0.68 | 0.32 | 0.00 | 5.98 | 32.1/21.4 | 18.9/27.5 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.57 | 0.43 | 0.48 | 5.89 | 32.5/22.2 | 19.1/29.3 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.059 | 0.54 | 0.46 | 0.00 | 5.98 | 22.1/32.3 | 28.8/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| J.T. Compher: 1+ goals YES | 13 | 0.161 | 0.150 | +0.023 | +0.013 | $2.23 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV12DETFLA-DET5|yes; why: higher confidence-adjusted growth (2.83 vs 0.70 bp); despite a smaller raw edge (+0.023 vs +0.026/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.918 vs 0.55); alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis DET:OFFENSE_4PLUS (p 0.3345): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4488, phi -0.193)

portfolios: A EV +0.37 (adj +0.21) on $2.28, P(profit) 0.1605, adj growth 1.9 bp · B EV +0.37 (adj +0.20) on $2.23, P(profit) 0.1605, adj growth 1.8 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ CHI  ·  10000 joint draws  ·  430 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_BUF_win | p_overtime | goals | shots CHI/BUF | CHI/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.51 | 0.49 | 0.00 | 6.02 | 27.2/27.7 | 24.1/23.6 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.115 | 0.45 | 0.55 | 0.00 | 6.01 | 21.6/33.2 | 29.2/18.3 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.49 | 5.94 | 21.7/33.4 | 30.0/18.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.47 | 5.91 | 27.1/27.8 | 24.6/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.47 | 0.53 | 0.00 | 9.24 | 28.3/29.3 | 23.0/22.5 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.076 | 0.43 | 0.57 | 0.00 | 9.26 | 23.0/34.5 | 27.4/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 24 | 0.287 | 0.270 | +0.034 | +0.017 | $3.43 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Buffalo over 3.5 goals scored NO | 52 | 0.600 | 0.555 | +0.062 | +0.017 | $4.97 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 1.5 goals NO | 64 | 0.708 | 0.671 | +0.052 | +0.015 | $2.39 | FUNDED_RESEARCH | $1 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no; why: higher confidence-adjusted growth (3.46 vs 2.31 bp); despite a smaller raw edge (+0.034 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: REINFORCING (phi 0.158); failure: CHI offense suppressed (<= 2 goals)
- **Buffalo over 3.5 goals scored NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no; why: higher confidence-adjusted growth (2.67 vs 2.31 bp); relationships: KXNHLGOAL-26NOV12BUFCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: REINFORCING (phi 0.544); failure: BUF offense succeeds (4+ goals)
- **Buffalo wins by over 1.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no has the higher standalone adjusted growth (2.67 vs 2.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.544); they share one thesis budget; relationships: KXNHLGOAL-26NOV12BUFCHI-CHITBERTUZZI59-1|yes: REINFORCING (phi 0.158); KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no: REINFORCING (phi 0.544); failure: BUF wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3754): highest fidelity KXNHLSPREAD-26NOV12BUFCHI-BUF3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV12BUFCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3878): highest fidelity KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no (same contract)
- thesis CHI:WINS (p 0.4913): highest fidelity KXNHLSPREAD-26NOV12BUFCHI-BUF2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12BUFCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4045, phi -0.253)
- KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3889, phi -0.977)
- KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2919, phi -1.0)

portfolios: A EV +1.61 (adj +0.54) on $17.40, P(profit) 0.6126, adj growth 4.8 bp · B EV +1.23 (adj +0.45) on $10.79, P(profit) 0.6613, adj growth 4.2 bp · C EV +1.85 (adj +0.69) on $15.03, P(profit) 0.7126, adj growth 6.0 bp · R EV +0.31 (adj +0.09) on $3.00, P(profit) 0.5998, adj growth 3.1 bp

## WPG @ DAL  ·  10000 joint draws  ·  404 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_WPG_win | p_overtime | goals | shots DAL/WPG | DAL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.60 | 0.40 | 0.00 | 5.99 | 26.1/25.8 | 22.8/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.47 | 5.9 | 26.1/26.0 | 22.7/22.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.102 | 0.68 | 0.32 | 0.00 | 5.98 | 30.7/20.4 | 17.8/26.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.61 | 0.39 | 0.00 | 9.15 | 27.6/27.2 | 22.0/21.2 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.60 | 0.40 | 0.48 | 5.96 | 31.2/20.9 | 17.9/27.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.61 | 0.39 | 0.00 | 3.47 | 24.8/24.7 | 23.1/22.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Arttu Hyry: 1+ goals YES | 15 | 0.179 | 0.169 | +0.020 | +0.010 | $1.91 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Cole Perfetti: 1+ assists YES | 30 | 0.362 | 0.326 | +0.047 | +0.011 | $2.62 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
- **Arttu Hyry: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes; why: higher confidence-adjusted growth (1.66 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0019 below the 0.010/contract floor; relationships: KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: DAL offense suppressed (<= 2 goals)
- **Cole Perfetti: 1+ assists YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WPGDAL-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (1.30 vs 0.33 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0055 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DAL:OFFENSE_4PLUS (p 0.4274): highest fidelity KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3102): highest fidelity KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes (same contract)
- KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3527, phi -0.199)
- KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4737, phi -0.298)

portfolios: A EV +1.16 (adj +0.35) on $8.06, P(profit) 0.4795, adj growth 2.9 bp · B EV +0.63 (adj +0.22) on $4.53, P(profit) 0.4795, adj growth 2.0 bp · C EV +0.96 (adj +0.33) on $6.91, P(profit) 0.4795, adj growth 2.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ UTA  ·  10000 joint draws  ·  424 bet sides mapped, 6 +EV candidates, 4 on card


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
| Lawson Crouse: 1+ goals YES | 19 | 0.246 | 0.228 | +0.045 | +0.028 | $5.10 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| MacKenzie Weegar: 1+ assists YES | 29 | 0.367 | 0.326 | +0.062 | +0.021 | $3.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Jack McBain: 1+ goals YES | 14 | 0.182 | 0.164 | +0.034 | +0.016 | $2.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 13 | 0.162 | 0.151 | +0.024 | +0.014 | $2.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-1|yes; why: higher confidence-adjusted growth (10.28 vs 4.77 bp); despite a smaller raw edge (+0.045 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-1|yes: MOSTLY_INDEPENDENT (phi 0.092); KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: UTA offense suppressed (<= 2 goals)
- **MacKenzie Weegar: 1+ assists YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (10.28 vs 4.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.092); they share one thesis budget; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.092); KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.06); KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: UTA offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (10.28 vs 4.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-1|yes: MOSTLY_INDEPENDENT (phi 0.06); KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: UTA offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV12STLUTA-7|yes; why: higher confidence-adjusted growth (3.36 vs 0.69 bp); despite a smaller raw edge (+0.024 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.885 vs 0.683); alternative not eligible: confidence-adjusted EV +0.0088 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.4237): highest fidelity KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.3803): highest fidelity KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3627): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.231)
- KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.259)
- KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.187)
- KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4013, phi -0.208)

portfolios: A EV +3.57 (adj +1.52) on $17.40, P(profit) 0.5873, adj growth 13.7 bp · B EV +2.98 (adj +1.50) on $14.07, P(profit) 0.4844, adj growth 13.7 bp · C EV +2.49 (adj +1.49) on $11.85, P(profit) 0.3691, adj growth 12.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Mats Zuccarello: 1+ assists NO | 66 | 0.851 | 0.717 | +0.175 | +0.041 | $13.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Andre Lee: 1+ goals YES | 9 | 0.132 | 0.116 | +0.036 | +0.021 | $3.41 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Alex Laferriere: 1+ goals YES | 27 | 0.312 | 0.298 | +0.029 | +0.014 | $3.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no; why: higher confidence-adjusted growth (17.21 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.061); failure: LAK offense succeeds (4+ goals)
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (10.50 vs 2.20 bp); relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: LAK offense suppressed (<= 2 goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (2.20 vs 0.00 bp); despite a smaller raw edge (+0.029 vs +0.050/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.061); KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.386): highest fidelity KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes (same contract)
- thesis LAK:SUPPRESSED (p 0.395): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.6 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.386, phi -0.181)
- KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.16)
- KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.261)

portfolios: A EV +3.47 (adj +1.35) on $13.92, P(profit) 0.3569, adj growth 12.6 bp · B EV +5.03 (adj +1.71) on $19.91, P(profit) 0.3569, adj growth 16.0 bp · C EV +0.49 (adj +0.25) on $4.86, P(profit) 0.3125, adj growth 2.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
