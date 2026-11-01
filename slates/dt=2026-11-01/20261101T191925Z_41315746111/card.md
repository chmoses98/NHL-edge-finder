# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-01T19:19:25Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +30.97 | +9.60 | +30.36 | 0.710 | -40.08 | -57.37 | 80.95 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +36.53 | +21.02 | +30.14 | 0.664 | -50.66 | -69.96 | 184.53 |
| C best expression per thesis | 142.58 | +31.42 | +17.94 | +25.38 | 0.621 | -50.67 | -67.84 | 155.09 |
| R FUNDED research stakes | 18.00 | +3.89 | +2.45 | -0.37 | 0.368 | -9.03 | -13.01 | 0.00 |

## MIN @ WSH  ·  10000 joint draws  ·  426 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.496 / away 0.504

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_MIN_win | p_overtime | goals | shots WSH/MIN | WSH/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.60 | 0.40 | 0.00 | 5.99 | 28.0/28.4 | 25.3/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.48 | 5.92 | 28.2/28.6 | 25.4/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.60 | 0.40 | 0.00 | 9.24 | 29.8/30.0 | 24.4/23.0 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.079 | 0.50 | 0.50 | 0.00 | 5.98 | 22.4/33.6 | 30.0/18.9 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.48 | 0.52 | 0.47 | 5.85 | 22.6/33.5 | 30.1/19.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.58 | 0.42 | 0.00 | 3.51 | 27.2/27.0 | 25.4/25.0 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 18 | 0.248 | 0.227 | +0.058 | +0.037 | $10.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 56 | 0.640 | 0.618 | +0.063 | +0.040 | $19.74 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 24 | 0.329 | 0.282 | +0.076 | +0.029 | $8.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Yakov Trenin: 1+ goals YES | 10 | 0.131 | 0.120 | +0.024 | +0.014 | $3.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (19.09 vs 9.78 bp); despite a smaller raw edge (+0.058 vs +0.076/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.038); KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.027); failure: WSH offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-2|no; why: higher confidence-adjusted growth (14.62 vs 8.61 bp); relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: MIN offense succeeds (4+ goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (19.09 vs 9.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.038); they share one thesis budget; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.038); KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: WSH offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV01MINWSH-3|yes; why: higher confidence-adjusted growth (4.55 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.904 vs 0.769); alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4173): highest fidelity KXNHLSPREAD-26NOV01MINWSH-MIN2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4336): highest fidelity KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:WINS (p 0.5547): highest fidelity KXNHLSPREAD-26NOV01MINWSH-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3555, phi -0.233)
- KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3486, phi -0.286)
- KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3555, phi -0.254)
- KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4336, phi -0.183)

portfolios: A EV +6.47 (adj +2.58) on $37.50, P(profit) 0.5591, adj growth 22.5 bp · B EV +8.53 (adj +4.78) on $41.76, P(profit) 0.4583, adj growth 41.9 bp · C EV +5.33 (adj +3.42) on $30.39, P(profit) 0.7255, adj growth 29.9 bp · R EV +0.54 (adj +0.35) on $5.00, P(profit) 0.6401, adj growth 12.6 bp

## UTA @ PHI  ·  10000 joint draws  ·  408 bet sides mapped, 26 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.383 / away 0.617

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_UTA_win | p_overtime | goals | shots PHI/UTA | PHI/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.52 | 0.48 | 0.00 | 6.01 | 26.4/26.7 | 23.2/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.47 | 5.91 | 26.7/27.0 | 23.6/23.3 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.091 | 0.44 | 0.56 | 0.00 | 5.99 | 21.0/31.8 | 27.8/17.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.46 | 0.54 | 0.46 | 5.87 | 21.1/32.0 | 28.7/17.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.51 | 0.49 | 0.00 | 9.21 | 27.9/28.3 | 22.4/21.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.53 | 0.47 | 0.00 | 3.41 | 25.3/25.6 | 23.7/23.4 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Christian Dvorak: 1+ goals YES | 16 | 0.249 | 0.224 | +0.080 | +0.055 | $10.98 | FUNDED_RESEARCH | $3 | PHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 11 | 0.186 | 0.164 | +0.069 | +0.047 | $8.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Travis Sanheim: 1+ goals YES | 9 | 0.134 | 0.118 | +0.039 | +0.023 | $4.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Matvei Michkov: 1+ goals YES | 26 | 0.318 | 0.301 | +0.044 | +0.027 | $6.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (45.40 vs 44.29 bp); relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV01UTAPHI-PHIMMICHKOV39-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: PHI offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes has the higher standalone adjusted growth (45.40 vs 44.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV01UTAPHI-PHIMMICHKOV39-1|yes: MOSTLY_INDEPENDENT (phi 0.031); failure: PHI offense suppressed (<= 2 goals)
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes has the higher standalone adjusted growth (45.40 vs 12.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV01UTAPHI-PHIMMICHKOV39-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense suppressed (<= 2 goals)
- **Matvei Michkov: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes; why: Player prop expression KXNHLGOAL-26NOV01UTAPHI-PHIMMICHKOV39-1|yes selected over broad KXNHLSPREAD-26NOV01UTAPHI-UTA3|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.42 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.031); KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:OFFENSE_4PLUS (p 0.3661): highest fidelity KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2799): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.5033): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01UTAPHI-UTA3|no (same contract)
- KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4149, phi -0.233)
- KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4149, phi -0.229)
- KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4149, phi -0.175)
- KXNHLGOAL-26NOV01UTAPHI-PHIMMICHKOV39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4149, phi -0.285)
- override: Player prop expression KXNHLGOAL-26NOV01UTAPHI-PHIMMICHKOV39-1|yes selected over broad KXNHLSPREAD-26NOV01UTAPHI-UTA3|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.42 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +9.15 (adj +4.04) on $37.50, P(profit) 0.5877, adj growth 34.6 bp · B EV +12.75 (adj +8.45) on $29.61, P(profit) 0.4677, adj growth 74.9 bp · C EV +14.82 (adj +9.49) on $43.92, P(profit) 0.3862, adj growth 81.0 bp · R EV +1.41 (adj +0.97) on $3.00, P(profit) 0.249, adj growth 34.2 bp

## EDM @ NYR  ·  10000 joint draws  ·  424 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.539 / away 0.461

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_EDM_win | p_overtime | goals | shots NYR/EDM | NYR/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.49 | 0.51 | 0.00 | 6.06 | 27.0/27.4 | 23.8/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.109 | 0.54 | 0.46 | 0.00 | 9.45 | 28.4/28.8 | 22.8/21.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.50 | 0.50 | 0.49 | 6.06 | 27.4/27.7 | 24.4/23.9 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.097 | 0.46 | 0.54 | 0.00 | 6.07 | 21.8/32.8 | 28.9/18.5 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.46 | 0.54 | 0.46 | 5.93 | 21.8/33.2 | 29.7/18.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.074 | 0.47 | 0.53 | 0.00 | 9.37 | 23.0/34.5 | 27.8/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 11 | 0.167 | 0.152 | +0.051 | +0.035 | $8.81 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Filip Hallander: 1+ goals YES | 9 | 0.136 | 0.123 | +0.041 | +0.028 | $6.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Ryan Nugent-Hopkins: 1+ assists NO | 63 | 0.715 | 0.670 | +0.068 | +0.023 | $18.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Vladislav Gavrikov: 1+ assists YES | 26 | 0.375 | 0.294 | +0.102 | +0.020 | $5.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (25.13 vs 1.93 bp); despite a smaller raw edge (+0.051 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.026); KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: EDM offense suppressed (<= 2 goals)
- **Filip Hallander: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (25.13 vs 18.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: EDM offense suppressed (<= 2 goals)
- **Ryan Nugent-Hopkins: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (5.27 vs 4.58 bp); despite a smaller raw edge (+0.068 vs +0.094/contract); relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: EDM offense succeeds (4+ goals)
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26NOV01EDMNYR-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (4.52 vs 0.88 bp); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4261): highest fidelity KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3517): highest fidelity KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.4375): highest fidelity KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes (same contract)
- KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3517, phi -0.187)
- KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3517, phi -0.151)
- KXNHLAST-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4261, phi -0.22)
- KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.5 pts; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3546, phi -0.264)

portfolios: A EV +9.85 (adj +1.89) on $37.50, P(profit) 0.712, adj growth 15.3 bp · B EV +10.78 (adj +5.71) on $39.91, P(profit) 0.4736, adj growth 49.1 bp · C EV +8.89 (adj +4.02) on $44.54, P(profit) 0.6624, adj growth 34.7 bp · R EV +1.30 (adj +0.90) on $3.00, P(profit) 0.1674, adj growth 28.8 bp

## OTT @ ANA  ·  10000 joint draws  ·  426 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.483 / away 0.517

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_OTT_win | p_overtime | goals | shots ANA/OTT | ANA/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.66 | 0.34 | 0.00 | 6.05 | 27.4/27.6 | 24.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.49 | 0.51 | 0.47 | 6.0 | 27.4/27.4 | 24.0/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.67 | 0.33 | 0.00 | 9.37 | 29.1/28.9 | 24.0/21.4 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.083 | 0.72 | 0.28 | 0.00 | 6.02 | 32.1/21.5 | 19.0/27.5 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.53 | 0.47 | 0.47 | 5.9 | 32.7/22.0 | 18.8/29.3 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.061 | 0.58 | 0.42 | 0.00 | 6.05 | 22.1/32.2 | 29.1/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ottawa wins by over 2.5 goals NO | 79 | 0.880 | 0.833 | +0.079 | +0.031 | $15.74 | FUNDED_RESEARCH | $4 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jeff Malott: 1+ goals YES | 10 | 0.136 | 0.125 | +0.029 | +0.019 | $4.75 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Ottawa over 4.5 goals scored NO | 74 | 0.815 | 0.773 | +0.062 | +0.019 | $13.87 | FUNDED_RESEARCH | $3 | ANA:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Fabian Zetterlund: 1+ goals YES | 17 | 0.200 | 0.191 | +0.020 | +0.011 | $4.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Ottawa wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no; why: higher confidence-adjusted growth (13.53 vs 12.47 bp); wins across more scripts (relative breadth 1.028 vs 0.578); relationships: KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.077); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: REINFORCING (phi 0.48); KXNHLGOAL-26NOV01OTTANA-OTTFZETTERLUND20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.122); failure: OTT wins by 2+
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV01OTTANA-OTT3|no has the higher standalone adjusted growth (13.53 vs 8.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.077); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: MOSTLY_INDEPENDENT (phi 0.077); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV01OTTANA-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: ANA offense suppressed (<= 2 goals)
- **Ottawa over 4.5 goals scored NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over broad KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.48 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.48); KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV01OTTANA-OTTFZETTERLUND20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.187); failure: OTT offense succeeds (4+ goals)
- **Fabian Zetterlund: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV01OTTANA-OTTFZETTERLUND20-2|yes; why: higher confidence-adjusted growth (1.81 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: INTENTIONAL_DIVERSIFIER (phi -0.122); KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: INTENTIONAL_DIVERSIFIER (phi -0.187); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:WINS (p 0.5889): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4358): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.3808): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- KXNHLSPREAD-26NOV01OTTANA-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2025, phi -0.731)
- KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3002, phi -0.155)
- KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3498, phi -0.649)
- KXNHLGOAL-26NOV01OTTANA-OTTFZETTERLUND20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4358, phi -0.203)
- override: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over broad KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.48 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.50 (adj +1.09) on $37.50, P(profit) 0.6911, adj growth 8.6 bp · B EV +4.47 (adj +2.08) on $38.72, P(profit) 0.2822, adj growth 18.7 bp · C EV +2.38 (adj +1.01) on $23.73, P(profit) 0.8805, adj growth 9.5 bp · R EV +0.64 (adj +0.23) on $7.00, P(profit) 0.7781, adj growth 8.7 bp
equivalent contracts collapsed: KXNHLGAME-26NOV01OTTANA-OTT|no == KXNHLGAME-26NOV01OTTANA-ANA|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
