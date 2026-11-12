# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-12T13:57:14Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +26.36 | +7.45 | +25.03 | 0.701 | -33.84 | -49.91 | 62.74 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +23.97 | +12.34 | +18.30 | 0.643 | -38.43 | -52.98 | 110.15 |
| C best expression per thesis | 145.41 | +27.76 | +14.43 | +21.53 | 0.636 | -44.93 | -62.04 | 125.27 |
| R FUNDED research stakes | 28.00 | +3.45 | +1.67 | +3.60 | 0.614 | -8.63 | -11.65 | 0.00 |

## CAR @ SEA  ·  10000 joint draws  ·  414 bet sides mapped, 26 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_CAR_win | p_overtime | goals | shots SEA/CAR | SEA/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.159 | 0.35 | 0.65 | 0.00 | 6.05 | 21.2/34.2 | 29.8/18.5 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.132 | 0.47 | 0.53 | 0.47 | 6.01 | 21.4/34.4 | 31.0/18.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.132 | 0.32 | 0.68 | 0.00 | 9.45 | 22.5/35.9 | 28.0/17.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.088 | 0.42 | 0.58 | 0.00 | 6.08 | 26.9/28.1 | 24.1/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.52 | 0.48 | 0.49 | 6.05 | 26.8/28.0 | 24.7/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.38 | 0.62 | 0.00 | 9.32 | 28.4/29.7 | 23.0/22.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Berkly Catton: 1+ goals YES | 14 | 0.222 | 0.200 | +0.073 | +0.052 | $10.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 64 | 0.721 | 0.698 | +0.065 | +0.042 | $16.54 | FUNDED_RESEARCH | $5 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 49 | 0.634 | 0.537 | +0.127 | +0.030 | $3.37 | FUNDED_RESEARCH | $1 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 62 | 0.752 | 0.663 | +0.116 | +0.027 | $6.46 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes; why: higher confidence-adjusted growth (44.71 vs 22.44 bp); despite a smaller raw edge (+0.073 vs +0.083/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.917 vs 0.571); relationships: KXNHLGOAL-26NOV12CARSEA-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26NOV12CARSEA-CAR2|no: REINFORCING (phi 0.152); KXNHLSPREAD-26NOV12CARSEA-CAR3|no: MOSTLY_INDEPENDENT (phi 0.127); failure: SEA offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12CARSEA-SEA2|yes; why: higher confidence-adjusted growth (17.20 vs 13.11 bp); despite a smaller raw edge (+0.065 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.03 vs 0.554); relationships: KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26NOV12CARSEA-CAR2|no: REINFORCING (phi 0.158); KXNHLSPREAD-26NOV12CARSEA-CAR3|no: REINFORCING (phi 0.16); failure: CAR offense succeeds (4+ goals)
- **Carolina wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes; why: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes has the higher standalone adjusted growth (22.44 vs 7.74 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.321); relationships: KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: REINFORCING (phi 0.152); KXNHLGOAL-26NOV12CARSEA-CARSAHO20-1|no: REINFORCING (phi 0.158); KXNHLSPREAD-26NOV12CARSEA-CAR3|no: DUPLICATIVE (phi 0.756); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes; why: Broad expression KXNHLSPREAD-26NOV12CARSEA-CAR3|no selected over player prop KXNHLAST-26NOV12CARSEA-CARSAHO20-1|no because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.82 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.127); KXNHLGOAL-26NOV12CARSEA-CARSAHO20-1|no: REINFORCING (phi 0.16); KXNHLSPREAD-26NOV12CARSEA-CAR2|no: DUPLICATIVE (phi 0.756); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis SEA:OFFENSE_4PLUS (p 0.3713): highest fidelity KXNHLTEAMTOTAL-26NOV12CARSEA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.2174): highest fidelity KXNHLSPREAD-26NOV12CARSEA-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4174): highest fidelity KXNHLSPREAD-26NOV12CARSEA-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12CARSEA-SEA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12CARSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4045, phi -0.223)
- KXNHLGOAL-26NOV12CARSEA-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4916, phi -0.226)
- KXNHLSPREAD-26NOV12CARSEA-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.9 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3658, phi -1.0)
- KXNHLSPREAD-26NOV12CARSEA-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.7 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3658, phi -0.756)
- override: Broad expression KXNHLSPREAD-26NOV12CARSEA-CAR3|no selected over player prop KXNHLAST-26NOV12CARSEA-CARSAHO20-1|no because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.82 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +6.30 (adj +1.15) on $22.25, P(profit) 0.5368, adj growth 9.7 bp · B EV +8.97 (adj +5.27) on $37.14, P(profit) 0.583, adj growth 46.8 bp · C EV +11.68 (adj +7.00) on $37.41, P(profit) 0.3435, adj growth 60.6 bp · R EV +1.11 (adj +0.46) on $8.00, P(profit) 0.5732, adj growth 16.9 bp
equivalent contracts collapsed: KXNHLGAME-26NOV12CARSEA-SEA|yes == KXNHLGAME-26NOV12CARSEA-CAR|no

## MTL @ BOS  ·  10000 joint draws  ·  422 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_MTL_win | p_overtime | goals | shots BOS/MTL | BOS/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.63 | 0.37 | 0.00 | 6.04 | 27.6/27.5 | 24.4/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.52 | 0.48 | 0.46 | 5.98 | 27.7/27.7 | 24.2/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.65 | 0.35 | 0.00 | 9.45 | 29.0/28.9 | 23.5/21.8 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.081 | 0.68 | 0.32 | 0.00 | 6.08 | 32.3/21.8 | 19.0/27.6 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.071 | 0.69 | 0.31 | 0.00 | 9.41 | 34.3/23.3 | 18.6/25.9 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.54 | 0.46 | 0.46 | 5.97 | 33.1/22.4 | 19.1/29.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Borgen: 1+ goals YES | 6 | 0.090 | 0.079 | +0.026 | +0.015 | $2.62 | FUNDED_RESEARCH | $1 | BOS:WINS_BY_2PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Fraser Minten: 1+ goals YES | 19 | 0.226 | 0.215 | +0.025 | +0.014 | $3.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Boston over 4.5 goals scored YES | 24 | 0.305 | 0.267 | +0.052 | +0.015 | $2.11 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | DIRECT (0.62) | EVIDENCE_MIXED | D |
| Nick Suzuki: 1+ assists NO | 52 | 0.639 | 0.552 | +0.101 | +0.014 | $6.37 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes; why: higher confidence-adjusted growth (7.73 vs 2.47 bp); despite a smaller raw edge (+0.026 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.712 vs 0.515); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes: REINFORCING (phi 0.163); KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.027); failure: MTL wins (incl. OT/SO)
- **Fraser Minten: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV12MTLBOS-9|yes; why: higher confidence-adjusted growth (2.58 vs 2.52 bp); despite a smaller raw edge (+0.025 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.846 vs 0.372); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes: REINFORCING (phi 0.2); KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: BOS offense suppressed (<= 2 goals)
- **Boston over 4.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes selected over player prop KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.62 vs 0.42 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: REINFORCING (phi 0.163); KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: REINFORCING (phi 0.2); KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: MTL wins (incl. OT/SO)
- **Nick Suzuki: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12MTLBOS-BOS3|yes; why: higher confidence-adjusted growth (1.81 vs 0.45 bp); wins across more scripts (relative breadth 0.994 vs 0.448); alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:WINS_BY_2PLUS (p 0.3719): highest fidelity KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4927): highest fidelity KXNHLTOTAL-26NOV12MTLBOS-7|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes — Broad expression KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes selected over player prop KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.62 vs 0.42 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:HIGH_EVENT (p 0.3212): highest fidelity KXNHLTOTAL-26NOV12MTLBOS-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:WINS (p 0.4134, phi -0.172)
- KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3043, phi -0.2)
- KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes: FUNDED_RESEARCH; family MIXED; loses 38% of the draws where the thesis happens; opposing: failure thesis MTL:WINS (p 0.4134, phi -0.456)
- KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.4 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3668, phi -0.268)
- override: Broad expression KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS5|yes selected over player prop KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.62 vs 0.42 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.81 (adj +0.90) on $22.25, P(profit) 0.5293, adj growth 7.3 bp · B EV +3.08 (adj +1.10) on $14.10, P(profit) 0.3977, adj growth 9.8 bp · C EV +4.28 (adj +1.48) on $19.69, P(profit) 0.3246, adj growth 12.8 bp · R EV +0.61 (adj +0.29) on $2.00, P(profit) 0.3458, adj growth 9.5 bp

## MIN @ TOR  ·  10000 joint draws  ·  394 bet sides mapped, 14 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_MIN_win | p_overtime | goals | shots TOR/MIN | TOR/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.51 | 0.49 | 0.00 | 6.03 | 29.1/29.4 | 25.9/25.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.47 | 6.0 | 29.2/29.8 | 26.4/25.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.54 | 0.46 | 0.00 | 9.37 | 30.4/30.8 | 24.9/23.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.097 | 0.47 | 0.53 | 0.00 | 6.05 | 23.3/34.9 | 31.1/19.9 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.49 | 0.51 | 0.46 | 6.0 | 23.4/35.2 | 31.8/20.1 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.071 | 0.49 | 0.51 | 0.00 | 9.28 | 25.1/37.0 | 29.6/19.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kirill Kaprizov: 1+ goals NO | 55 | 0.625 | 0.603 | +0.058 | +0.035 | $14.86 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Minnesota wins by over 2.5 goals NO | 74 | 0.826 | 0.780 | +0.072 | +0.027 | $16.54 | FUNDED_RESEARCH | $5 | TOR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Yakov Trenin: 1+ goals YES | 11 | 0.141 | 0.130 | +0.024 | +0.013 | $3.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ goals YES | 20 | 0.241 | 0.227 | +0.030 | +0.016 | $3.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12MINTOR-MIN3|no; why: higher confidence-adjusted growth (11.05 vs 8.55 bp); despite a smaller raw edge (+0.058 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV12MINTOR-MIN3|no: REINFORCING (phi 0.192); KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: MIN offense succeeds (4+ goals)
- **Minnesota wins by over 2.5 goals NO** — thesis: TOR wins (incl. OT/SO); alternative: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no has the higher standalone adjusted growth (11.05 vs 8.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.192); they share one thesis budget; relationships: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: REINFORCING (phi 0.192); KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.12); KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.121); failure: MIN wins by 2+
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV12MINTOR-MINJBRODIN25-1|yes; why: higher confidence-adjusted growth (3.39 vs 0.00 bp); despite a smaller raw edge (+0.024 vs +0.032/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLSPREAD-26NOV12MINTOR-MIN3|no: INTENTIONAL_DIVERSIFIER (phi -0.12); KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: MIN offense suppressed (<= 2 goals)
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV12MINTOR-MIN3|no; why: Player prop expression KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes selected over broad KXNHLTEAMTOTAL-26NOV12MINTOR-TOR5|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.35 vs 0.57 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26NOV12MINTOR-MIN3|no: MOSTLY_INDEPENDENT (phi 0.121); KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:SUPPRESSED (p 0.3784): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS (p 0.5097): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS_BY_2PLUS (p 0.2952): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4038, phi -0.292)
- KXNHLSPREAD-26NOV12MINTOR-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2767, phi -0.743)
- KXNHLGOAL-26NOV12MINTOR-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3784, phi -0.167)
- KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3606, phi -0.22)
- override: Player prop expression KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes selected over broad KXNHLTEAMTOTAL-26NOV12MINTOR-TOR5|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.35 vs 0.57 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.09 (adj +1.23) on $22.25, P(profit) 0.5497, adj growth 9.5 bp · B EV +4.20 (adj +2.09) on $37.81, P(profit) 0.6766, adj growth 18.9 bp · C EV +3.76 (adj +1.84) on $38.18, P(profit) 0.5512, adj growth 16.4 bp · R EV +0.89 (adj +0.43) on $9.00, P(profit) 0.5512, adj growth 15.3 bp

## COL @ OTT  ·  10000 joint draws  ·  416 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_COL_win | p_overtime | goals | shots OTT/COL | OTT/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.51 | 0.49 | 0.00 | 6.04 | 27.8/28.0 | 24.4/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.49 | 0.51 | 0.47 | 5.95 | 27.9/28.3 | 24.9/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.47 | 0.53 | 0.00 | 9.46 | 29.3/29.4 | 23.0/23.2 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.078 | 0.44 | 0.56 | 0.00 | 6.07 | 22.2/32.9 | 28.6/19.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.47 | 0.53 | 0.46 | 5.94 | 22.6/33.4 | 29.9/19.3 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.061 | 0.55 | 0.45 | 0.00 | 5.99 | 32.4/22.0 | 18.8/28.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ NJD  ·  10000 joint draws  ·  420 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_WSH_win | p_overtime | goals | shots NJD/WSH | NJD/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.126 | 0.62 | 0.38 | 0.00 | 6.04 | 33.7/21.8 | 18.9/29.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.58 | 0.42 | 0.00 | 6.09 | 28.2/27.4 | 24.1/24.1 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.53 | 0.47 | 0.47 | 5.9 | 33.9/22.1 | 18.9/30.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.52 | 0.48 | 0.50 | 5.98 | 28.2/27.5 | 24.2/24.9 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.084 | 0.65 | 0.35 | 0.00 | 9.29 | 35.1/23.2 | 18.4/27.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.58 | 0.42 | 0.00 | 9.37 | 29.4/29.0 | 23.2/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 17 | 0.224 | 0.207 | +0.044 | +0.027 | $6.37 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 13 | 0.172 | 0.158 | +0.034 | +0.020 | $4.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Amadeus Lombardi: 1+ goals YES | 10 | 0.134 | 0.118 | +0.028 | +0.012 | $2.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 67 | 0.732 | 0.696 | +0.047 | +0.011 | $7.97 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (10.74 vs 0.09 bp); alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV12WSHNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26NOV12WSHNJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: WSH offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12WSHNJ-NJBPESCE22-1|yes; why: higher confidence-adjusted growth (7.30 vs 2.19 bp); despite a smaller raw edge (+0.034 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV12WSHNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26NOV12WSHNJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: NJD offense suppressed (<= 2 goals)
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes has the higher standalone adjusted growth (7.30 vs 3.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26NOV12WSHNJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.031); failure: NJD offense suppressed (<= 2 goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV12WSHNJ-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (1.14 vs 0.16 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV12WSHNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.031); failure: NJD offense succeeds (4+ goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3457): highest fidelity KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.4391): highest fidelity KXNHLAST-26NOV12WSHNJ-NJBPESCE22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.3539): highest fidelity KXNHLAST-26NOV12WSHNJ-NJLEVANGELISTA77-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV12WSHNJ-NJLEVANGELISTA77-1|no (same contract)
- KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4344, phi -0.238)
- KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3539, phi -0.196)
- KXNHLGOAL-26NOV12WSHNJ-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3539, phi -0.16)
- KXNHLAST-26NOV12WSHNJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4391, phi -0.228)

portfolios: A EV +3.86 (adj +1.73) on $22.25, P(profit) 0.5492, adj growth 15.3 bp · B EV +3.85 (adj +1.99) on $21.19, P(profit) 0.4443, adj growth 17.7 bp · C EV +3.86 (adj +2.08) on $22.27, P(profit) 0.3577, adj growth 18.0 bp · R EV +0.49 (adj +0.30) on $2.00, P(profit) 0.2243, adj growth 10.4 bp

## TBL @ CBJ  ·  10000 joint draws  ·  418 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_TBL_win | p_overtime | goals | shots CBJ/TBL | CBJ/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.51 | 0.49 | 0.00 | 5.98 | 26.9/27.1 | 23.6/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.46 | 5.9 | 27.0/27.3 | 23.9/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.50 | 0.50 | 0.00 | 9.32 | 28.6/28.9 | 22.9/22.3 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.087 | 0.49 | 0.51 | 0.00 | 5.96 | 21.6/32.3 | 28.6/18.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.49 | 0.51 | 0.49 | 5.94 | 21.7/32.6 | 29.3/18.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.057 | 0.51 | 0.49 | 0.00 | 3.46 | 25.9/26.0 | 24.2/24.1 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 17 | 0.212 | 0.198 | +0.032 | +0.018 | $4.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Yanni Gourde: 1+ goals NO | 86 | 0.893 | 0.881 | +0.025 | +0.013 | $16.54 | FUNDED_RESEARCH | $5 | TBL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| John Carlson: 1+ assists NO | 62 | 0.691 | 0.648 | +0.054 | +0.011 | $6.22 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLPTS-26NOV12TBCBJ-TBNKUCHEROV86-2|no; why: higher confidence-adjusted growth (4.81 vs 0.00 bp); despite a smaller raw edge (+0.032 vs +0.082/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26NOV12TBCBJ-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: CBJ offense suppressed (<= 2 goals)
- **Yanni Gourde: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV12TBCBJ-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (3.17 vs 1.24 bp); despite a smaller raw edge (+0.025 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26NOV12TBCBJ-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.063); failure: TBL offense succeeds (4+ goals)
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV12TBCBJ-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (1.24 vs 0.81 bp); despite a smaller raw edge (+0.054 vs +0.119/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi 0.063); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:WINS_BY_2PLUS (p 0.2882): highest fidelity KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.4134): highest fidelity KXNHLAST-26NOV12TBCBJ-TBJCARLSON74-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV12TBCBJ-TBJCARLSON74-1|no (same contract)
- KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4055, phi -0.244)
- KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3695, phi -0.156)
- KXNHLAST-26NOV12TBCBJ-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3695, phi -0.248)

portfolios: A EV +1.81 (adj +0.73) on $22.20, P(profit) 0.7024, adj growth 6.6 bp · B EV +1.77 (adj +0.78) on $26.99, P(profit) 0.6943, adj growth 7.0 bp · C EV +1.63 (adj +0.67) on $13.35, P(profit) 0.2123, adj growth 5.8 bp · R EV +0.14 (adj +0.07) on $5.00, P(profit) 0.8933, adj growth 2.7 bp

## DET @ FLA  ·  10000 joint draws  ·  416 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_DET_win | p_overtime | goals | shots FLA/DET | FLA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.61 | 0.39 | 0.00 | 5.99 | 27.5/27.4 | 24.4/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.93 | 27.6/27.5 | 24.2/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.58 | 0.42 | 0.00 | 9.27 | 29.2/28.9 | 23.6/22.5 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.081 | 0.67 | 0.33 | 0.00 | 5.97 | 32.0/21.5 | 18.9/27.3 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.55 | 0.45 | 0.52 | 5.88 | 32.9/22.2 | 19.1/29.5 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.061 | 0.53 | 0.47 | 0.00 | 5.94 | 21.8/32.0 | 28.5/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Bennett: 1+ goals YES | 27 | 0.314 | 0.300 | +0.030 | +0.016 | $4.19 | FUNDED_RESEARCH | $2 | FLA:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Aaron Ekblad: 1+ assists YES | 27 | 0.332 | 0.299 | +0.049 | +0.015 | $3.58 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_MIXED | D |
- **Sam Bennett: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes; why: higher confidence-adjusted growth (2.86 vs 2.37 bp); despite a smaller raw edge (+0.030 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes: MOSTLY_INDEPENDENT (phi 0.11); failure: FLA offense suppressed (<= 2 goals)
- **Aaron Ekblad: 1+ assists YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes has the higher standalone adjusted growth (2.86 vs 2.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.110); they share one thesis budget; relationships: KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi 0.11); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:OFFENSE_4PLUS (p 0.4437): highest fidelity KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3416, phi -0.231)
- KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3416, phi -0.243)

portfolios: A EV +1.77 (adj +0.66) on $12.15, P(profit) 0.5176, adj growth 5.4 bp · B EV +1.05 (adj +0.43) on $7.77, P(profit) 0.5176, adj growth 3.8 bp · C EV +0.58 (adj +0.32) on $5.55, P(profit) 0.3135, adj growth 2.8 bp · R EV +0.21 (adj +0.12) on $2.00, P(profit) 0.3135, adj growth 3.8 bp

## BUF @ CHI  ·  10000 joint draws  ·  412 bet sides mapped, 6 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_BUF_win | p_overtime | goals | shots CHI/BUF | CHI/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.51 | 0.49 | 0.00 | 6.03 | 27.0/27.5 | 24.2/23.3 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.111 | 0.44 | 0.56 | 0.00 | 5.96 | 21.5/32.9 | 28.8/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.50 | 0.50 | 0.47 | 5.95 | 27.3/27.9 | 24.5/24.1 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.49 | 0.51 | 0.47 | 5.94 | 21.8/33.5 | 30.2/18.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.48 | 0.52 | 0.00 | 9.26 | 28.7/29.2 | 22.6/22.7 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.076 | 0.44 | 0.56 | 0.00 | 9.17 | 23.0/34.5 | 27.8/17.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BUF:SUPPRESSED (p 0.3929): highest fidelity KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no (same contract)
- thesis CHI:WINS_BY_2PLUS (p 0.2755): highest fidelity KXNHLSPREAD-26NOV12BUFCHI-BUF2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.4925): highest fidelity KXNHLSPREAD-26NOV12BUFCHI-BUF2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order

portfolios: A EV +1.78 (adj +0.45) on $22.25, P(profit) 0.5875, adj growth 3.6 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.70 (adj +0.22) on $2.91, P(profit) 0.1843, adj growth 1.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ DAL  ·  10000 joint draws  ·  398 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_WPG_win | p_overtime | goals | shots DAL/WPG | DAL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.62 | 0.38 | 0.00 | 5.99 | 26.2/25.8 | 22.8/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.54 | 0.46 | 0.49 | 5.92 | 26.2/26.0 | 22.6/23.0 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.091 | 0.69 | 0.31 | 0.00 | 5.96 | 30.8/20.2 | 17.8/26.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.63 | 0.37 | 0.00 | 9.2 | 27.6/27.5 | 22.2/21.0 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.55 | 0.45 | 0.48 | 5.86 | 30.9/20.8 | 17.7/27.5 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.060 | 0.69 | 0.31 | 0.00 | 9.12 | 32.4/21.7 | 17.2/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Arttu Hyry: 1+ goals YES | 15 | 0.192 | 0.180 | +0.033 | +0.022 | $5.00 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DAL:WINS_BY_2PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Arttu Hyry: 1+ goals YES** — thesis: DAL wins by 2+; alternative: KXNHL2PSPREAD-26NOV12WPGDAL-DAL2|yes; why: higher confidence-adjusted growth (7.50 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.85 vs 0.706); alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis DAL:WINS_BY_2PLUS (p 0.3564): highest fidelity KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes (same contract)
- KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3491, phi -0.21)

portfolios: A EV +0.93 (adj +0.60) on $4.41, P(profit) 0.1923, adj growth 5.4 bp · B EV +1.05 (adj +0.68) on $5.00, P(profit) 0.1923, adj growth 6.0 bp · C EV +1.27 (adj +0.82) on $6.05, P(profit) 0.1923, adj growth 7.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_STL_win | p_overtime | goals | shots UTA/STL | UTA/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.52 | 0.48 | 0.00 | 6.02 | 27.4/27.2 | 23.7/23.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.106 | 0.62 | 0.38 | 0.00 | 6.01 | 32.5/21.7 | 18.8/28.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.47 | 5.93 | 27.5/27.1 | 23.8/24.2 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.56 | 0.44 | 0.47 | 5.93 | 32.9/21.7 | 18.6/29.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.53 | 0.47 | 0.00 | 9.3 | 28.8/28.5 | 22.6/22.5 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.079 | 0.61 | 0.39 | 0.00 | 9.26 | 34.3/22.9 | 17.8/27.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, UTA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_NYI_win | p_overtime | goals | shots LAK/NYI | LAK/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.57 | 0.43 | 0.00 | 5.99 | 27.9/27.7 | 24.5/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.53 | 0.47 | 0.48 | 5.88 | 28.0/27.8 | 24.6/24.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.082 | 0.61 | 0.39 | 0.00 | 5.95 | 33.0/22.3 | 19.4/28.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.55 | 0.45 | 0.50 | 5.84 | 33.0/22.2 | 19.1/29.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.60 | 0.40 | 0.00 | 9.26 | 29.2/29.1 | 23.6/22.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.068 | 0.52 | 0.48 | 0.47 | 2.8 | 26.6/26.4 | 25.0/25.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
