# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-12T16:16:00Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +30.08 | +9.53 | +28.93 | 0.766 | -21.83 | -35.58 | 86.78 |
| B thesis-diversified (joint) ← optimiser card | 149.20 | +24.60 | +12.19 | +22.70 | 0.733 | -22.60 | -34.09 | 114.89 |
| C best expression per thesis | 135.89 | +34.18 | +15.92 | +29.06 | 0.672 | -49.22 | -67.58 | 137.36 |
| R FUNDED research stakes | 25.00 | +2.50 | +1.18 | +1.85 | 0.630 | -5.75 | -7.87 | 0.00 |

## CAR @ SEA  ·  10000 joint draws  ·  462 bet sides mapped, 34 +EV candidates, 4 on card


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
| Carolina wins by over 1.5 goals NO | 49 | 0.634 | 0.537 | +0.127 | +0.030 | $3.86 | FUNDED_RESEARCH | $1 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikolaj Ehlers: 1+ goals NO | 72 | 0.773 | 0.758 | +0.039 | +0.024 | $9.02 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 62 | 0.721 | 0.652 | +0.084 | +0.015 | $4.40 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes; why: higher confidence-adjusted growth (30.43 vs 25.91 bp); despite a smaller raw edge (+0.063 vs +0.083/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.918 vs 0.579); relationships: KXNHLSPREAD-26NOV12CARSEA-CAR2|no: REINFORCING (phi 0.152); KXNHLGOAL-26NOV12CARSEA-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV12CARSEA-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: SEA offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes; why: Broad expression KXNHLSPREAD-26NOV12CARSEA-CAR2|no selected over broad KXNHLTEAMTOTAL-26NOV12CARSEA-CAR5|no because adjusted EV is 0.7 pts higher while thesis capture is 1.00 vs 0.95 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: REINFORCING (phi 0.152); KXNHLGOAL-26NOV12CARSEA-CARNEHLERS27-1|no: REINFORCING (phi 0.151); KXNHLGOAL-26NOV12CARSEA-CARSAHO20-1|no: REINFORCING (phi 0.158); failure: CAR wins by 2+
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12CARSEA-SEA2|yes; why: KXNHLSPREAD-26NOV12CARSEA-SEA2|yes has the higher standalone adjusted growth (10.87 vs 6.63 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.117); relationships: KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLSPREAD-26NOV12CARSEA-CAR2|no: REINFORCING (phi 0.151); KXNHLGOAL-26NOV12CARSEA-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: CAR offense succeeds (4+ goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12CARSEA-SEA2|yes; why: Player prop expression KXNHLGOAL-26NOV12CARSEA-CARSAHO20-1|no selected over player prop KXNHLAST-26NOV12CARSEA-CARSAHO20-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.87 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26NOV12CARSEA-CAR2|no: REINFORCING (phi 0.158); KXNHLGOAL-26NOV12CARSEA-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis SEA:OFFENSE_4PLUS (p 0.3713): highest fidelity KXNHLTEAMTOTAL-26NOV12CARSEA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.2174): highest fidelity KXNHLSPREAD-26NOV12CARSEA-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4174): highest fidelity KXNHLSPREAD-26NOV12CARSEA-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes — Broad expression KXNHLSPREAD-26NOV12CARSEA-CAR2|no selected over broad KXNHLTEAMTOTAL-26NOV12CARSEA-CAR5|no because adjusted EV is 0.7 pts higher while thesis capture is 1.00 vs 0.95 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4045, phi -0.223)
- KXNHLSPREAD-26NOV12CARSEA-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.9 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3658, phi -1.0)
- KXNHLGOAL-26NOV12CARSEA-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4916, phi -0.206)
- KXNHLGOAL-26NOV12CARSEA-CARSAHO20-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 13% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.6 pts; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4916, phi -0.226)
- override: Broad expression KXNHLSPREAD-26NOV12CARSEA-CAR2|no selected over broad KXNHLTEAMTOTAL-26NOV12CARSEA-CAR5|no because adjusted EV is 0.7 pts higher while thesis capture is 1.00 vs 0.95 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26NOV12CARSEA-CARSAHO20-1|no selected over player prop KXNHLAST-26NOV12CARSEA-CARSAHO20-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.87 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.15 (adj +0.84) on $16.14, P(profit) 0.6167, adj growth 7.3 bp · B EV +4.03 (adj +2.02) on $22.35, P(profit) 0.5158, adj growth 19.0 bp · C EV +8.70 (adj +4.75) on $17.44, P(profit) 0.3435, adj growth 40.7 bp · R EV +0.41 (adj +0.16) on $4.00, P(profit) 0.7728, adj growth 6.0 bp
equivalent contracts collapsed: KXNHLGAME-26NOV12CARSEA-SEA|yes == KXNHLGAME-26NOV12CARSEA-CAR|no

## MTL @ BOS  ·  10000 joint draws  ·  424 bet sides mapped, 11 +EV candidates, 4 on card


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
| Tanner Jeannot: 1+ goals YES | 8 | 0.115 | 0.103 | +0.029 | +0.018 | $1.94 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Fraser Minten: 1+ goals YES | 18 | 0.226 | 0.213 | +0.036 | +0.023 | $2.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| William Borgen: 1+ goals YES | 6 | 0.090 | 0.077 | +0.026 | +0.013 | $1.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:WINS_BY_2PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Fraser Minten: 1+ assists YES | 23 | 0.305 | 0.262 | +0.062 | +0.020 | $2.22 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_MIXED | D |
- **Tanner Jeannot: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes; why: higher confidence-adjusted growth (9.27 vs 7.42 bp); despite a smaller raw edge (+0.030 vs +0.036/contract); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.054); failure: BOS offense suppressed (<= 2 goals)
- **Fraser Minten: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS6|yes; why: higher confidence-adjusted growth (7.42 vs 6.32 bp); despite a smaller raw edge (+0.036 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.843 vs 0.315); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: BOS offense suppressed (<= 2 goals)
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS6|yes; why: higher confidence-adjusted growth (6.49 vs 6.32 bp); despite a smaller raw edge (+0.026 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.754 vs 0.315); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.062); failure: MTL wins (incl. OT/SO)
- **Fraser Minten: 1+ assists YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes has the higher standalone adjusted growth (7.42 vs 4.69 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.026); they share one thesis budget; relationships: KXNHLGOAL-26NOV12MTLBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.054); KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.062); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.4927): highest fidelity KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS4|yes less than the minimum stake; KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes kept
- thesis BOS:WINS_BY_2PLUS (p 0.3719): highest fidelity KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS4|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS6|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3212): highest fidelity KXNHLTOTAL-26NOV12MTLBOS-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS6|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12MTLBOS-BOSTJEANNOT84-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3043, phi -0.144)
- KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3043, phi -0.2)
- KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:WINS (p 0.4134, phi -0.172)
- KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3043, phi -0.231)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS4|yes less than the minimum stake; KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes kept

portfolios: A EV +2.86 (adj +0.72) on $16.14, P(profit) 0.4552, adj growth 6.5 bp · B EV +2.33 (adj +1.23) on $8.41, P(profit) 0.5493, adj growth 11.5 bp · C EV +4.84 (adj +1.94) on $19.15, P(profit) 0.3682, adj growth 16.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ TOR  ·  10000 joint draws  ·  390 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_MIN_win | p_overtime | goals | shots TOR/MIN | TOR/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.51 | 0.49 | 0.00 | 6.03 | 29.0/29.5 | 25.9/25.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.51 | 0.49 | 0.46 | 5.97 | 29.1/29.6 | 26.3/25.7 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.100 | 0.48 | 0.52 | 0.00 | 6.04 | 23.3/35.0 | 31.3/20.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.51 | 0.49 | 0.00 | 9.35 | 30.5/31.0 | 24.5/24.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.46 | 0.54 | 0.50 | 5.93 | 23.4/35.3 | 31.8/20.1 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.068 | 0.47 | 0.53 | 0.00 | 9.32 | 24.8/37.0 | 30.3/19.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Easton Cowan: 1+ goals YES | 18 | 0.241 | 0.225 | +0.051 | +0.034 | $3.82 | FUNDED_RESEARCH | $1 | TOR:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Toronto wins by over 1.5 goals YES | 20 | 0.294 | 0.244 | +0.083 | +0.033 | $3.19 | FUNDED_RESEARCH | $1 | TOR:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 73 | 0.823 | 0.774 | +0.079 | +0.030 | $9.02 | FUNDED_RESEARCH | $3 | TOR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Yakov Trenin: 1+ goals YES | 10 | 0.139 | 0.127 | +0.032 | +0.020 | $2.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV12MINTOR-TOR2|yes; why: higher confidence-adjusted growth (16.52 vs 14.24 bp); despite a smaller raw edge (+0.051 vs +0.083/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.925 vs 0.532); relationships: KXNHLSPREAD-26NOV12MINTOR-TOR2|yes: MOSTLY_INDEPENDENT (phi 0.126); KXNHLSPREAD-26NOV12MINTOR-MIN3|no: MOSTLY_INDEPENDENT (phi 0.11); KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: TOR offense suppressed (<= 2 goals)
- **Toronto wins by over 1.5 goals YES** — thesis: TOR wins by 2+; alternative: KXNHLSPREAD-26NOV12MINTOR-MIN3|no; why: higher confidence-adjusted growth (14.24 vs 10.54 bp); relationships: KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.126); KXNHLSPREAD-26NOV12MINTOR-MIN3|no: REINFORCING (phi 0.299); KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.086); failure: MIN wins (incl. OT/SO)
- **Minnesota wins by over 2.5 goals NO** — thesis: TOR wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV12MINTOR-TOR2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV12MINTOR-TOR2|yes has the higher standalone adjusted growth (14.24 vs 10.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.299); they share one thesis budget; relationships: KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.11); KXNHLSPREAD-26NOV12MINTOR-TOR2|yes: REINFORCING (phi 0.299); KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.101); failure: MIN wins by 2+
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12MINTOR-MINJBRODIN25-1|yes; why: higher confidence-adjusted growth (9.24 vs 0.00 bp); despite a smaller raw edge (+0.032 vs +0.036/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26NOV12MINTOR-TOR2|yes: INTENTIONAL_DIVERSIFIER (phi -0.086); KXNHLSPREAD-26NOV12MINTOR-MIN3|no: INTENTIONAL_DIVERSIFIER (phi -0.101); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TOR:OFFENSE_4PLUS (p 0.4136): highest fidelity KXNHLTEAMTOTAL-26NOV12MINTOR-TOR4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV12MINTOR-TOR2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS_BY_2PLUS (p 0.2937): highest fidelity KXNHLSPREAD-26NOV12MINTOR-TOR2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV12MINTOR-TOR2|yes (same contract)
- thesis TOR:WINS (p 0.5075): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV12MINTOR-TOR2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3697, phi -0.199)
- KXNHLSPREAD-26NOV12MINTOR-TOR2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.4925, phi -0.635)
- KXNHLSPREAD-26NOV12MINTOR-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2774, phi -0.749)
- KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3832, phi -0.177)

portfolios: A EV +4.71 (adj +0.71) on $16.14, P(profit) 0.6395, adj growth 6.1 bp · B EV +4.02 (adj +2.05) on $18.63, P(profit) 0.5262, adj growth 19.3 bp · C EV +3.55 (adj +1.43) on $9.08, P(profit) 0.2937, adj growth 12.4 bp · R EV +0.98 (adj +0.46) on $5.00, P(profit) 0.4396, adj growth 17.1 bp
equivalent contracts collapsed: KXNHLGAME-26NOV12MINTOR-TOR|yes == KXNHLGAME-26NOV12MINTOR-MIN|no

## COL @ OTT  ·  10000 joint draws  ·  446 bet sides mapped, 2 +EV candidates, 2 on card


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
| Ridly Greig: 1+ goals YES | 16 | 0.208 | 0.194 | +0.039 | +0.024 | $3.11 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Fabian Zetterlund: 1+ goals YES | 19 | 0.223 | 0.213 | +0.022 | +0.013 | $1.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes; why: higher confidence-adjusted growth (9.13 vs 2.20 bp); relationships: KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: OTT offense suppressed (<= 2 goals)
- **Fabian Zetterlund: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes has the higher standalone adjusted growth (9.13 vs 2.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.4015): highest fidelity KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3855, phi -0.209)
- KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3855, phi -0.214)

portfolios: A EV +1.12 (adj +0.69) on $6.03, P(profit) 0.3856, adj growth 6.4 bp · B EV +0.91 (adj +0.56) on $4.85, P(profit) 0.3856, adj growth 5.2 bp · C EV +1.58 (adj +0.99) on $6.88, P(profit) 0.2084, adj growth 8.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ NJD  ·  10000 joint draws  ·  416 bet sides mapped, 4 +EV candidates, 4 on card


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
| Aliaksei Protas: 1+ goals YES | 17 | 0.224 | 0.209 | +0.044 | +0.030 | $3.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 13 | 0.169 | 0.157 | +0.031 | +0.019 | $2.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Luke Hughes: 1+ goals NO | 84 | 0.870 | 0.861 | +0.020 | +0.012 | $9.02 | FUNDED_RESEARCH | $3 | NJD:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 18 | 0.211 | 0.201 | +0.021 | +0.011 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (12.80 vs 1.58 bp); relationships: KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV12WSHNJ-NJLHUGHES43-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: WSH offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12WSHNJ-NJBPESCE22-1|yes; why: higher confidence-adjusted growth (6.44 vs 0.47 bp); despite a smaller raw edge (+0.031 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV12WSHNJ-NJLHUGHES43-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NJD offense suppressed (<= 2 goals)
- **Luke Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV12WSHNJ-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (2.36 vs 0.59 bp); alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: NJD offense succeeds (4+ goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (12.80 vs 1.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV12WSHNJ-NJLHUGHES43-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3457): highest fidelity KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.4391): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis NJD:SUPPRESSED (p 0.3539): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4344, phi -0.238)
- KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3539, phi -0.176)
- KXNHLGOAL-26NOV12WSHNJ-NJLHUGHES43-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4391, phi -0.151)
- KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4344, phi -0.226)

portfolios: A EV +2.12 (adj +1.32) on $15.82, P(profit) 0.4771, adj growth 12.3 bp · B EV +1.87 (adj +1.17) on $16.74, P(profit) 0.4771, adj growth 11.0 bp · C EV +2.10 (adj +1.40) on $8.49, P(profit) 0.2243, adj growth 12.1 bp · R EV +0.07 (adj +0.04) on $3.00, P(profit) 0.8698, adj growth 1.5 bp

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
| Mathieu Olivier: 1+ goals YES | 16 | 0.213 | 0.198 | +0.043 | +0.029 | $3.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Yanni Gourde: 1+ goals NO | 86 | 0.902 | 0.890 | +0.034 | +0.022 | $9.02 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 23 | 0.270 | 0.258 | +0.027 | +0.016 | $2.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Full Game: Over 5.5 goals scored NO | 40 | 0.461 | 0.428 | +0.044 | +0.011 | $3.51 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
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

portfolios: A EV +2.97 (adj +0.85) on $16.14, P(profit) 0.6747, adj growth 7.7 bp · B EV +2.02 (adj +1.17) on $19.08, P(profit) 0.4042, adj growth 11.0 bp · C EV +4.08 (adj +1.65) on $17.65, P(profit) 0.5491, adj growth 14.2 bp · R EV +0.22 (adj +0.10) on $4.00, P(profit) 0.4339, adj growth 3.9 bp

## DET @ FLA  ·  10000 joint draws  ·  416 bet sides mapped, 1 +EV candidates, 1 on card


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
| J.T. Compher: 1+ goals YES | 13 | 0.161 | 0.152 | +0.023 | +0.014 | $1.70 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12DETFLA-DETADEBRINCAT93-2|yes; why: higher confidence-adjusted growth (3.42 vs 1.14 bp); alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis DET:OFFENSE_4PLUS (p 0.3345): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4488, phi -0.193)

portfolios: A EV +0.35 (adj +0.21) on $2.11, P(profit) 0.1605, adj growth 1.9 bp · B EV +0.28 (adj +0.17) on $1.70, P(profit) 0.1605, adj growth 1.6 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ CHI  ·  10000 joint draws  ·  430 bet sides mapped, 7 +EV candidates, 3 on card


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
| Tage Thompson: 2+ goals NO | 90 | 0.932 | 0.922 | +0.026 | +0.016 | $9.02 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 1.5 goals NO | 64 | 0.709 | 0.672 | +0.053 | +0.016 | $3.44 | FUNDED_RESEARCH | $1 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Chicago wins by over 1.5 goals YES | 22 | 0.276 | 0.245 | +0.043 | +0.013 | $1.07 | FUNDED_RESEARCH | $1 | CHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tage Thompson: 2+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no; why: higher confidence-adjusted growth (6.36 vs 2.50 bp); despite a smaller raw edge (+0.026 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: MOSTLY_INDEPENDENT (phi 0.145); KXNHLSPREAD-26NOV12BUFCHI-CHI2|yes: MOSTLY_INDEPENDENT (phi 0.108); failure: BUF offense succeeds (4+ goals)
- **Buffalo wins by over 1.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV12BUFCHI-CHI2|yes; why: higher confidence-adjusted growth (2.50 vs 2.14 bp); wins across more scripts (relative breadth 0.935 vs 0.551); relationships: KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-2|no: MOSTLY_INDEPENDENT (phi 0.145); KXNHLSPREAD-26NOV12BUFCHI-CHI2|yes: DUPLICATIVE (phi 0.395); failure: BUF wins by 2+
- **Chicago wins by over 1.5 goals YES** — thesis: CHI wins by 2+; alternative: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no; why: Broad expression KXNHLSPREAD-26NOV12BUFCHI-CHI2|yes selected over broad KXNHLSPREAD-26NOV12BUFCHI-CHI3|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.63 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-2|no: MOSTLY_INDEPENDENT (phi 0.108); KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: DUPLICATIVE (phi 0.395); failure: BUF wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis BUF:SUPPRESSED (p 0.3929): highest fidelity KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV12BUFCHI-BUF2|no — Broad expression KXNHLSPREAD-26NOV12BUFCHI-BUF3|no selected over player prop KXNHLAST-26NOV12BUFCHI-BUFTTHOMPSON72-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.82 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CHI:WINS (p 0.4925): highest fidelity KXNHLSPREAD-26NOV12BUFCHI-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV12BUFCHI-BUF2|no (same contract)
- thesis CHI:WINS_BY_2PLUS (p 0.2755): highest fidelity KXNHLSPREAD-26NOV12BUFCHI-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV12BUFCHI-BUF2|no (same contract)
- KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3875, phi -0.21)
- KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2907, phi -1.0)
- KXNHLSPREAD-26NOV12BUFCHI-CHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.5075, phi -0.626)
- override: Broad expression KXNHLSPREAD-26NOV12BUFCHI-BUF3|no selected over player prop KXNHLAST-26NOV12BUFCHI-BUFTTHOMPSON72-1|no because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.82 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26NOV12BUFCHI-CHI2|yes selected over broad KXNHLSPREAD-26NOV12BUFCHI-CHI3|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.63 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.30 (adj +0.32) on $16.14, P(profit) 0.6613, adj growth 2.8 bp · B EV +0.74 (adj +0.30) on $13.53, P(profit) 0.6779, adj growth 2.9 bp · C EV +1.00 (adj +0.30) on $12.36, P(profit) 0.7093, adj growth 2.6 bp · R EV +0.36 (adj +0.13) on $5.00, P(profit) 0.2755, adj growth 4.8 bp

## WPG @ DAL  ·  10000 joint draws  ·  404 bet sides mapped, 3 +EV candidates, 3 on card


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
| Arttu Hyry: 1+ goals YES | 15 | 0.192 | 0.180 | +0.033 | +0.022 | $2.72 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DAL:WINS_BY_2PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Josh Morrissey: 1+ assists NO | 61 | 0.749 | 0.649 | +0.122 | +0.022 | $7.93 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Neal Pionk: 1+ assists YES | 27 | 0.324 | 0.294 | +0.040 | +0.011 | $1.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
- **Arttu Hyry: 1+ goals YES** — thesis: DAL wins by 2+; alternative: KXNHLPTS-26NOV12WPGDAL-DALAHYRY25-1|yes; why: higher confidence-adjusted growth (7.50 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26NOV12WPGDAL-WPGNPIONK4-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: DAL offense suppressed (<= 2 goals)
- **Josh Morrissey: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12WPGDAL-WPGJMORRISSEY44-1|no; why: higher confidence-adjusted growth (4.61 vs 0.87 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26NOV12WPGDAL-WPGNPIONK4-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: WPG offense succeeds (4+ goals)
- **Neal Pionk: 1+ assists YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes; why: higher confidence-adjusted growth (1.18 vs 0.95 bp); despite a smaller raw edge (+0.040 vs +0.044/contract); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi -0.025); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis DAL:WINS_BY_2PLUS (p 0.3564): highest fidelity KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes (same contract)
- thesis WPG:SUPPRESSED (p 0.4789): highest fidelity KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3045): highest fidelity KXNHLAST-26NOV12WPGDAL-WPGNPIONK4-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV12WPGDAL-WPGNPIONK4-1|yes (same contract)
- KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3491, phi -0.21)
- KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.4 pts; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3045, phi -0.233)
- KXNHLAST-26NOV12WPGDAL-WPGNPIONK4-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4789, phi -0.284)

portfolios: A EV +2.56 (adj +0.83) on $14.15, P(profit) 0.4549, adj growth 7.6 bp · B EV +2.35 (adj +0.71) on $12.31, P(profit) 0.7967, adj growth 6.7 bp · C EV +5.21 (adj +1.58) on $27.30, P(profit) 0.7967, adj growth 13.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Lawson Crouse: 1+ goals YES | 19 | 0.246 | 0.230 | +0.045 | +0.029 | $3.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 14 | 0.182 | 0.171 | +0.034 | +0.022 | $2.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 13 | 0.162 | 0.151 | +0.024 | +0.014 | $1.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Daniil But: 1+ goals NO | 81 | 0.846 | 0.835 | +0.025 | +0.014 | $9.02 | FUNDED_RESEARCH | $3 | UTA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-1|yes; why: higher confidence-adjusted growth (11.23 vs 3.73 bp); despite a smaller raw edge (+0.045 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV12STLUTA-UTADBUT19-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: UTA offense suppressed (<= 2 goals)
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

portfolios: A EV +3.31 (adj +1.50) on $16.14, P(profit) 0.5873, adj growth 13.7 bp · B EV +2.07 (adj +1.28) on $17.28, P(profit) 0.4701, adj growth 12.0 bp · C EV +2.58 (adj +1.59) on $12.25, P(profit) 0.3691, adj growth 13.8 bp · R EV +0.09 (adj +0.05) on $3.00, P(profit) 0.8462, adj growth 1.9 bp

## NYI @ LAK  ·  10000 joint draws  ·  384 bet sides mapped, 6 +EV candidates, 4 on card


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
| Mats Zuccarello: 1+ assists NO | 66 | 0.851 | 0.717 | +0.175 | +0.041 | $9.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Andre Lee: 1+ goals YES | 9 | 0.132 | 0.119 | +0.036 | +0.023 | $2.70 | FUNDED_RESEARCH | $1 | LAK:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 6 | 0.083 | 0.075 | +0.019 | +0.011 | $1.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Alex Turcotte: 1+ goals YES | 11 | 0.140 | 0.128 | +0.023 | +0.011 | $1.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no; why: higher confidence-adjusted growth (17.21 vs 0.59 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.043); KXNHLGOAL-26NOV12NYILA-LAATURCOTTE15-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.065); failure: LAK offense succeeds (4+ goals)
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (13.17 vs 2.60 bp); relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV12NYILA-LAATURCOTTE15-1|yes: MOSTLY_INDEPENDENT (phi -0.021); failure: LAK offense suppressed (<= 2 goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLPTS-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (4.19 vs 0.00 bp); despite a smaller raw edge (+0.019 vs +0.041/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.043); KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV12NYILA-LAATURCOTTE15-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: LAK offense suppressed (<= 2 goals)
- **Alex Turcotte: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes has the higher standalone adjusted growth (2.60 vs 2.38 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.000); relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.065); KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.386): highest fidelity KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes (same contract)
- thesis LAK:SUPPRESSED (p 0.395): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis LAK:WINS_BY_2PLUS (p 0.3124): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.6 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.386, phi -0.181)
- KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.16)
- KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.136)
- KXNHLGOAL-26NOV12NYILA-LAATURCOTTE15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.163)

portfolios: A EV +3.63 (adj +1.54) on $15.03, P(profit) 0.4514, adj growth 14.5 bp · B EV +3.99 (adj +1.53) on $14.32, P(profit) 0.294, adj growth 14.6 bp · C EV +0.54 (adj +0.29) on $5.29, P(profit) 0.3125, adj growth 2.5 bp · R EV +0.38 (adj +0.24) on $1.00, P(profit) 0.1318, adj growth 8.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
