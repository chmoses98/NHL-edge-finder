# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-12T14:21:44Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +26.44 | +7.40 | +24.98 | 0.697 | -35.69 | -50.46 | 61.93 |
| B thesis-diversified (joint) ← optimiser card | 149.10 | +21.07 | +10.40 | +19.14 | 0.672 | -34.18 | -48.98 | 94.11 |
| C best expression per thesis | 145.67 | +23.92 | +11.68 | +20.84 | 0.660 | -42.55 | -58.96 | 102.50 |
| R FUNDED research stakes | 32.00 | +4.09 | +1.88 | +3.21 | 0.642 | -8.91 | -11.80 | 0.00 |

## CAR @ SEA  ·  10000 joint draws  ·  414 bet sides mapped, 26 +EV candidates, 4 on card


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
| Sebastian Aho: 1+ goals NO | 64 | 0.721 | 0.698 | +0.065 | +0.042 | $15.43 | FUNDED_RESEARCH | $4 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 16 | 0.222 | 0.203 | +0.052 | +0.033 | $6.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 49 | 0.634 | 0.537 | +0.127 | +0.030 | $4.38 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 62 | 0.752 | 0.663 | +0.116 | +0.027 | $6.46 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12CARSEA-SEA2|yes; why: higher confidence-adjusted growth (17.20 vs 13.11 bp); despite a smaller raw edge (+0.065 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.028 vs 0.556); relationships: KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26NOV12CARSEA-CAR2|no: REINFORCING (phi 0.158); KXNHLSPREAD-26NOV12CARSEA-CAR3|no: REINFORCING (phi 0.16); failure: CAR offense succeeds (4+ goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes; why: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes has the higher standalone adjusted growth (22.44 vs 16.82 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.203); relationships: KXNHLGOAL-26NOV12CARSEA-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26NOV12CARSEA-CAR2|no: REINFORCING (phi 0.152); KXNHLSPREAD-26NOV12CARSEA-CAR3|no: MOSTLY_INDEPENDENT (phi 0.127); failure: SEA offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes; why: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes has the higher standalone adjusted growth (22.44 vs 7.74 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.321); relationships: KXNHLGOAL-26NOV12CARSEA-CARSAHO20-1|no: REINFORCING (phi 0.158); KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: REINFORCING (phi 0.152); KXNHLSPREAD-26NOV12CARSEA-CAR3|no: DUPLICATIVE (phi 0.756); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes; why: Broad expression KXNHLSPREAD-26NOV12CARSEA-CAR3|no selected over broad KXNHLTEAMTOTAL-26NOV12CARSEA-SEA2|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV12CARSEA-CARSAHO20-1|no: REINFORCING (phi 0.16); KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.127); KXNHLSPREAD-26NOV12CARSEA-CAR2|no: DUPLICATIVE (phi 0.756); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis SEA:OFFENSE_4PLUS (p 0.3713): highest fidelity KXNHLTEAMTOTAL-26NOV12CARSEA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.2174): highest fidelity KXNHLSPREAD-26NOV12CARSEA-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4174): highest fidelity KXNHLSPREAD-26NOV12CARSEA-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes — Broad expression KXNHLSPREAD-26NOV12CARSEA-CAR3|no selected over broad KXNHLTEAMTOTAL-26NOV12CARSEA-SEA2|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26NOV12CARSEA-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4916, phi -0.226)
- KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4045, phi -0.223)
- KXNHLSPREAD-26NOV12CARSEA-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.9 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3658, phi -1.0)
- KXNHLSPREAD-26NOV12CARSEA-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.7 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3658, phi -0.756)
- override: Broad expression KXNHLSPREAD-26NOV12CARSEA-CAR3|no selected over broad KXNHLTEAMTOTAL-26NOV12CARSEA-SEA2|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +6.70 (adj +1.22) on $23.65, P(profit) 0.5368, adj growth 10.2 bp · B EV +5.80 (adj +2.79) on $32.77, P(profit) 0.6532, adj growth 25.4 bp · C EV +6.92 (adj +3.25) on $26.98, P(profit) 0.7784, adj growth 28.8 bp · R EV +1.26 (adj +0.46) on $8.00, P(profit) 0.5732, adj growth 16.7 bp
equivalent contracts collapsed: KXNHLGAME-26NOV12CARSEA-SEA|yes == KXNHLGAME-26NOV12CARSEA-CAR|no

## MTL @ BOS  ·  10000 joint draws  ·  422 bet sides mapped, 7 +EV candidates, 4 on card


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
| William Borgen: 1+ goals YES | 6 | 0.090 | 0.079 | +0.026 | +0.015 | $2.44 | FUNDED_RESEARCH | $1 | BOS:WINS_BY_2PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Fraser Minten: 1+ goals YES | 19 | 0.226 | 0.215 | +0.025 | +0.014 | $2.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Boston over 4.5 goals scored YES | 24 | 0.305 | 0.267 | +0.052 | +0.015 | $1.97 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | DIRECT (0.62) | EVIDENCE_MIXED | D |
| Nick Suzuki: 1+ assists NO | 52 | 0.639 | 0.552 | +0.101 | +0.014 | $5.94 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes; why: higher confidence-adjusted growth (7.73 vs 2.47 bp); despite a smaller raw edge (+0.026 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.754 vs 0.517); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes: REINFORCING (phi 0.163); KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.027); failure: MTL wins (incl. OT/SO)
- **Fraser Minten: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV12MTLBOS-9|yes; why: higher confidence-adjusted growth (2.58 vs 2.52 bp); despite a smaller raw edge (+0.025 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.843 vs 0.374); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes: REINFORCING (phi 0.2); KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: BOS offense suppressed (<= 2 goals)
- **Boston over 4.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes selected over player prop KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.62 vs 0.42 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: REINFORCING (phi 0.163); KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: REINFORCING (phi 0.2); KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: MTL wins (incl. OT/SO)
- **Nick Suzuki: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12MTLBOS-BOS3|yes; why: higher confidence-adjusted growth (1.81 vs 0.45 bp); wins across more scripts (relative breadth 0.999 vs 0.454); alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:WINS_BY_2PLUS (p 0.3719): highest fidelity KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4927): highest fidelity KXNHLTOTAL-26NOV12MTLBOS-7|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes — Broad expression KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes selected over player prop KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.62 vs 0.42 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:HIGH_EVENT (p 0.3212): highest fidelity KXNHLTOTAL-26NOV12MTLBOS-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:WINS (p 0.4134, phi -0.172)
- KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3043, phi -0.2)
- KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes: FUNDED_RESEARCH; family MIXED; loses 38% of the draws where the thesis happens; opposing: failure thesis MTL:WINS (p 0.4134, phi -0.456)
- KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.4 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3668, phi -0.268)
- override: Broad expression KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes selected over player prop KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.62 vs 0.42 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.06 (adj +0.96) on $23.65, P(profit) 0.5293, adj growth 7.6 bp · B EV +2.87 (adj +1.03) on $13.16, P(profit) 0.3977, adj growth 9.2 bp · C EV +4.28 (adj +1.48) on $19.69, P(profit) 0.3246, adj growth 12.8 bp · R EV +0.61 (adj +0.29) on $2.00, P(profit) 0.3458, adj growth 9.5 bp

## MIN @ TOR  ·  10000 joint draws  ·  394 bet sides mapped, 14 +EV candidates, 4 on card


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
| Kirill Kaprizov: 1+ goals NO | 54 | 0.625 | 0.601 | +0.068 | +0.044 | $15.43 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Minnesota wins by over 2.5 goals NO | 74 | 0.826 | 0.780 | +0.072 | +0.027 | $15.43 | FUNDED_RESEARCH | $4 | TOR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Yakov Trenin: 1+ goals YES | 11 | 0.141 | 0.130 | +0.024 | +0.013 | $2.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ goals YES | 20 | 0.241 | 0.227 | +0.030 | +0.016 | $3.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12MINTOR-MIN3|no; why: higher confidence-adjusted growth (17.10 vs 8.55 bp); despite a smaller raw edge (+0.068 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV12MINTOR-MIN3|no: REINFORCING (phi 0.192); KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: MIN offense succeeds (4+ goals)
- **Minnesota wins by over 2.5 goals NO** — thesis: TOR wins (incl. OT/SO); alternative: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no has the higher standalone adjusted growth (17.10 vs 8.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.192); they share one thesis budget; relationships: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: REINFORCING (phi 0.192); KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.12); KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.121); failure: MIN wins by 2+
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV12MINTOR-MINJBRODIN25-1|yes; why: higher confidence-adjusted growth (3.39 vs 0.00 bp); despite a smaller raw edge (+0.024 vs +0.032/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLSPREAD-26NOV12MINTOR-MIN3|no: INTENTIONAL_DIVERSIFIER (phi -0.12); KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: MIN offense suppressed (<= 2 goals)
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV12MINTOR-MIN3|no; why: Player prop expression KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes selected over broad KXNHLTEAMTOTAL-26NOV12MINTOR-TOR5|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.35 vs 0.57 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26NOV12MINTOR-MIN3|no: MOSTLY_INDEPENDENT (phi 0.121); KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.10.
- thesis MIN:SUPPRESSED (p 0.3784): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS (p 0.5097): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS_BY_2PLUS (p 0.2952): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4038, phi -0.292)
- KXNHLSPREAD-26NOV12MINTOR-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2767, phi -0.743)
- KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3784, phi -0.167)
- KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3606, phi -0.22)
- override: Player prop expression KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes selected over broad KXNHLTEAMTOTAL-26NOV12MINTOR-TOR5|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.35 vs 0.57 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.58 (adj +1.34) on $23.65, P(profit) 0.5497, adj growth 10.2 bp · B EV +4.38 (adj +2.31) on $36.82, P(profit) 0.6093, adj growth 21.1 bp · C EV +4.34 (adj +2.29) on $40.00, P(profit) 0.5512, adj growth 20.5 bp · R EV +0.87 (adj +0.46) on $8.00, P(profit) 0.5512, adj growth 16.8 bp

## COL @ OTT  ·  10000 joint draws  ·  416 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_COL_win | p_overtime | goals | shots OTT/COL | OTT/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.50 | 0.50 | 0.00 | 6.03 | 27.8/27.9 | 24.2/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.48 | 5.94 | 27.7/28.1 | 24.8/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.47 | 0.53 | 0.00 | 9.4 | 29.2/29.5 | 23.3/23.2 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.080 | 0.43 | 0.57 | 0.00 | 6.09 | 22.4/33.1 | 29.0/19.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.45 | 0.55 | 0.45 | 5.94 | 22.3/33.3 | 29.9/19.1 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.061 | 0.57 | 0.43 | 0.00 | 6.0 | 32.4/22.2 | 19.1/28.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ NJD  ·  10000 joint draws  ·  420 bet sides mapped, 7 +EV candidates, 4 on card


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
| Aliaksei Protas: 1+ goals YES | 17 | 0.224 | 0.208 | +0.044 | +0.028 | $6.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 13 | 0.172 | 0.158 | +0.034 | +0.020 | $4.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 59 | 0.643 | 0.628 | +0.036 | +0.021 | $10.19 | FUNDED_RESEARCH | $3 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Connor Brown: 1+ goals YES | 19 | 0.230 | 0.216 | +0.029 | +0.016 | $3.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (11.75 vs 0.09 bp); alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV12WSHNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12WSHNJ-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: WSH offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-NJCBROWN16-1|yes; why: higher confidence-adjusted growth (7.30 vs 3.31 bp); relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV12WSHNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV12WSHNJ-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi 0.027); failure: NJD offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV12WSHNJ-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (4.19 vs 1.14 bp); despite a smaller raw edge (+0.036 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV12WSHNJ-NJCBROWN16-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NJD offense succeeds (4+ goals)
- **Connor Brown: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes has the higher standalone adjusted growth (7.30 vs 3.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.027); they share one thesis budget; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26NOV12WSHNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3457): highest fidelity KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.4391): highest fidelity KXNHLAST-26NOV12WSHNJ-NJBPESCE22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.3539): highest fidelity KXNHLAST-26NOV12WSHNJ-NJLEVANGELISTA77-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV12WSHNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4344, phi -0.238)
- KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3539, phi -0.196)
- KXNHLGOAL-26NOV12WSHNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4391, phi -0.264)
- KXNHLGOAL-26NOV12WSHNJ-NJCBROWN16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3539, phi -0.22)

portfolios: A EV +3.09 (adj +1.36) on $23.65, P(profit) 0.4408, adj growth 12.3 bp · B EV +3.66 (adj +2.20) on $23.99, P(profit) 0.4513, adj growth 19.7 bp · C EV +4.07 (adj +2.49) on $26.51, P(profit) 0.3577, adj growth 21.6 bp · R EV +0.18 (adj +0.11) on $3.00, P(profit) 0.6427, adj growth 3.8 bp

## TBL @ CBJ  ·  10000 joint draws  ·  418 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_TBL_win | p_overtime | goals | shots CBJ/TBL | CBJ/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.51 | 0.49 | 0.00 | 6.0 | 27.2/27.5 | 24.0/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.53 | 0.47 | 0.47 | 5.92 | 27.1/27.3 | 24.0/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.49 | 0.51 | 0.00 | 9.37 | 28.5/28.8 | 22.5/22.1 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.082 | 0.48 | 0.52 | 0.00 | 5.93 | 21.5/32.1 | 28.2/18.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.46 | 0.54 | 0.49 | 5.9 | 21.6/32.3 | 28.9/18.4 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.060 | 0.55 | 0.45 | 0.00 | 5.99 | 31.6/21.6 | 18.4/27.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 17 | 0.212 | 0.198 | +0.032 | +0.018 | $3.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Yanni Gourde: 1+ goals NO | 86 | 0.894 | 0.882 | +0.025 | +0.013 | $15.43 | FUNDED_RESEARCH | $4 | TBL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLPTS-26NOV12TBCBJ-TBNKUCHEROV86-2|no; why: higher confidence-adjusted growth (4.81 vs 0.00 bp); despite a smaller raw edge (+0.032 vs +0.076/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense suppressed (<= 2 goals)
- **Yanni Gourde: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26NOV12TBCBJ-4|no; why: higher confidence-adjusted growth (3.39 vs 0.50 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.997 vs 0.354); alternative not eligible: confidence-adjusted EV +0.0051 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:WINS_BY_2PLUS (p 0.2882): highest fidelity KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.4134): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4055, phi -0.244)
- KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3695, phi -0.148)

portfolios: A EV +1.12 (adj +0.61) on $14.14, P(profit) 0.2123, adj growth 5.5 bp · B EV +1.17 (adj +0.64) on $19.41, P(profit) 0.2123, adj growth 5.8 bp · C EV +0.94 (adj +0.52) on $5.20, P(profit) 0.2123, adj growth 4.5 bp · R EV +0.12 (adj +0.06) on $4.00, P(profit) 0.8939, adj growth 2.3 bp

## DET @ FLA  ·  10000 joint draws  ·  416 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_DET_win | p_overtime | goals | shots FLA/DET | FLA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.62 | 0.38 | 0.00 | 5.99 | 27.4/27.3 | 24.3/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.48 | 5.91 | 27.5/27.5 | 24.2/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.59 | 0.41 | 0.00 | 9.28 | 29.2/29.0 | 23.5/22.7 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.080 | 0.65 | 0.35 | 0.00 | 5.97 | 32.2/21.4 | 18.7/27.7 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.55 | 0.45 | 0.51 | 5.92 | 32.8/22.2 | 19.1/29.3 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.060 | 0.52 | 0.48 | 0.00 | 5.95 | 22.2/32.2 | 28.6/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Bennett: 1+ goals YES | 27 | 0.314 | 0.300 | +0.030 | +0.016 | $3.91 | FUNDED_RESEARCH | $1 | FLA:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Aaron Ekblad: 1+ assists YES | 27 | 0.332 | 0.299 | +0.049 | +0.015 | $3.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_MIXED | D |
- **Sam Bennett: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes; why: higher confidence-adjusted growth (2.86 vs 2.37 bp); despite a smaller raw edge (+0.030 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes: MOSTLY_INDEPENDENT (phi 0.11); failure: FLA offense suppressed (<= 2 goals)
- **Aaron Ekblad: 1+ assists YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes has the higher standalone adjusted growth (2.86 vs 2.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.110); they share one thesis budget; relationships: KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi 0.11); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:OFFENSE_4PLUS (p 0.4437): highest fidelity KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3416, phi -0.231)
- KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3416, phi -0.243)

portfolios: A EV +1.88 (adj +0.70) on $12.91, P(profit) 0.5176, adj growth 5.7 bp · B EV +0.98 (adj +0.40) on $7.24, P(profit) 0.5176, adj growth 3.6 bp · C EV +0.58 (adj +0.32) on $5.55, P(profit) 0.3135, adj growth 2.8 bp · R EV +0.10 (adj +0.06) on $1.00, P(profit) 0.3135, adj growth 2.1 bp

## BUF @ CHI  ·  10000 joint draws  ·  412 bet sides mapped, 6 +EV candidates, 2 on card


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
| Buffalo wins by over 1.5 goals NO | 63 | 0.709 | 0.667 | +0.063 | +0.021 | $9.97 | FUNDED_RESEARCH | $3 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo over 1.5 goals scored NO | 14 | 0.184 | 0.160 | +0.036 | +0.011 | $1.08 | FUNDED_RESEARCH | $1 | BUF:SUPPRESSED | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Buffalo wins by over 1.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF2|no; why: higher confidence-adjusted growth (4.17 vs 2.16 bp); wins across more scripts (relative breadth 0.935 vs 0.617); relationships: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF2|no: DUPLICATIVE (phi 0.304); failure: BUF wins by 2+
- **Buffalo over 1.5 goals scored NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no has the higher standalone adjusted growth (4.17 vs 2.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.304); they share one thesis budget; relationships: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: DUPLICATIVE (phi 0.304); failure: BUF wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis CHI:WINS (p 0.4925): highest fidelity KXNHLSPREAD-26NOV12BUFCHI-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV12BUFCHI-BUF2|no (same contract)
- thesis BUF:SUPPRESSED (p 0.3929): highest fidelity KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV12BUFCHI-BUF2|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF2|no kept
- thesis CHI:WINS_BY_2PLUS (p 0.2755): highest fidelity KXNHLSPREAD-26NOV12BUFCHI-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV12BUFCHI-BUF2|no (same contract)
- KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2907, phi -1.0)
- KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF2|no: FUNDED_RESEARCH; family MIXED; loses 53% of the draws where the thesis happens; opposing: failure thesis BUF:WINS (p 0.5075, phi -0.439)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF2|no kept
- override: Broad expression KXNHLSPREAD-26NOV12BUFCHI-CHI2|yes selected over broad KXNHLSPREAD-26NOV12BUFCHI-CHI3|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.63 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.02 (adj +0.57) on $23.65, P(profit) 0.5875, adj growth 4.7 bp · B EV +1.23 (adj +0.40) on $11.05, P(profit) 0.7093, adj growth 3.7 bp · C EV +1.53 (adj +0.51) on $15.69, P(profit) 0.7093, adj growth 4.4 bp · R EV +0.53 (adj +0.17) on $4.00, P(profit) 0.7093, adj growth 5.7 bp

## WPG @ DAL  ·  10000 joint draws  ·  398 bet sides mapped, 1 +EV candidates, 1 on card


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
| Arttu Hyry: 1+ goals YES | 15 | 0.192 | 0.180 | +0.033 | +0.022 | $4.66 | FUNDED_RESEARCH | $2 | DAL:WINS_BY_2PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Arttu Hyry: 1+ goals YES** — thesis: DAL wins by 2+; alternative: KXNHL2PSPREAD-26NOV12WPGDAL-DAL2|yes; why: higher confidence-adjusted growth (7.50 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.839 vs 0.711); alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis DAL:WINS_BY_2PLUS (p 0.3564): highest fidelity KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes (same contract)
- KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3491, phi -0.21)

portfolios: A EV +0.99 (adj +0.64) on $4.69, P(profit) 0.1923, adj growth 5.7 bp · B EV +0.98 (adj +0.63) on $4.66, P(profit) 0.1923, adj growth 5.7 bp · C EV +1.27 (adj +0.82) on $6.05, P(profit) 0.1923, adj growth 7.1 bp · R EV +0.42 (adj +0.27) on $2.00, P(profit) 0.1923, adj growth 8.9 bp

## STL @ UTA  ·  10000 joint draws  ·  400 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_STL_win | p_overtime | goals | shots UTA/STL | UTA/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.52 | 0.48 | 0.00 | 6.0 | 27.1/27.0 | 23.4/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.49 | 5.94 | 27.3/27.0 | 23.7/24.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.102 | 0.61 | 0.39 | 0.00 | 6.05 | 32.4/21.4 | 18.5/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.52 | 0.48 | 0.00 | 9.34 | 29.1/28.7 | 22.8/23.0 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.56 | 0.44 | 0.45 | 5.92 | 32.6/21.5 | 18.4/29.1 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.071 | 0.64 | 0.36 | 0.00 | 9.2 | 33.9/22.8 | 17.9/26.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_NYI_win | p_overtime | goals | shots LAK/NYI | LAK/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 5.98 | 27.8/27.6 | 24.4/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.86 | 27.8/27.5 | 24.4/24.6 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.086 | 0.60 | 0.40 | 0.00 | 5.98 | 32.9/22.3 | 19.3/28.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.56 | 0.44 | 0.50 | 5.87 | 33.1/22.2 | 19.0/29.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.59 | 0.41 | 0.00 | 9.25 | 29.4/29.2 | 23.9/22.7 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.46 | 2.83 | 26.4/26.2 | 24.7/24.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
