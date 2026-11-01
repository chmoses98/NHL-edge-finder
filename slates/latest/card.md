# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-01T18:24:16Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +38.45 | +16.35 | +34.00 | 0.690 | -48.83 | -67.58 | 139.56 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +39.93 | +24.54 | +33.30 | 0.673 | -52.84 | -75.23 | 216.12 |
| C best expression per thesis | 125.70 | +30.93 | +17.99 | +25.09 | 0.612 | -56.03 | -65.45 | 155.14 |
| R FUNDED research stakes | 19.00 | +3.49 | +2.15 | +1.47 | 0.589 | -9.84 | -10.11 | 0.00 |

## MIN @ WSH  ·  10000 joint draws  ·  426 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.496 / away 0.504

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_MIN_win | p_overtime | goals | shots WSH/MIN | WSH/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.58 | 0.42 | 0.00 | 6.06 | 28.2/28.4 | 25.2/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.53 | 0.47 | 0.52 | 5.96 | 28.2/28.4 | 25.2/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.58 | 0.42 | 0.00 | 9.31 | 29.8/30.0 | 24.5/23.1 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.077 | 0.50 | 0.50 | 0.00 | 5.99 | 22.6/33.5 | 29.9/19.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.48 | 0.52 | 0.45 | 5.9 | 22.6/33.7 | 30.5/19.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.52 | 0.48 | 0.00 | 3.54 | 27.3/27.4 | 25.5/25.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 18 | 0.246 | 0.225 | +0.056 | +0.034 | $8.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 56 | 0.638 | 0.618 | +0.061 | +0.040 | $17.74 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 9 | 0.132 | 0.115 | +0.036 | +0.019 | $4.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 18 | 0.225 | 0.209 | +0.035 | +0.019 | $4.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (16.31 vs 6.23 bp); despite a smaller raw edge (+0.056 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: WSH offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-2|no; why: higher confidence-adjusted growth (14.66 vs 0.45 bp); alternative not eligible: confidence-adjusted EV +0.0042 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: MIN offense succeeds (4+ goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01MINWSH-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (9.21 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0002 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: MIN offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes; why: Player prop expression KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes selected over player prop KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.32 vs 0.46 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4234): highest fidelity KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes — Player prop expression KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes selected over player prop KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.32 vs 0.46 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis MIN:SUPPRESSED (p 0.4222): highest fidelity KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.3561): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3628, phi -0.238)
- KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3561, phi -0.285)
- KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4222, phi -0.168)
- KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3628, phi -0.199)
- override: Player prop expression KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes selected over player prop KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.32 vs 0.46 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +9.14 (adj +4.65) on $37.50, P(profit) 0.5472, adj growth 39.5 bp · B EV +6.76 (adj +4.05) on $34.99, P(profit) 0.4403, adj growth 35.9 bp · C EV +4.91 (adj +3.11) on $29.54, P(profit) 0.7228, adj growth 27.3 bp · R EV +0.53 (adj +0.35) on $5.00, P(profit) 0.6385, adj growth 12.6 bp

## UTA @ PHI  ·  10000 joint draws  ·  408 bet sides mapped, 24 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.383 / away 0.617

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_UTA_win | p_overtime | goals | shots PHI/UTA | PHI/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.50 | 0.50 | 0.00 | 6.02 | 26.4/26.8 | 23.3/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.53 | 0.47 | 0.49 | 5.91 | 26.4/26.7 | 23.4/23.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.092 | 0.44 | 0.56 | 0.00 | 5.94 | 21.0/31.7 | 27.8/17.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.46 | 0.54 | 0.48 | 5.89 | 21.1/32.1 | 28.7/18.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.50 | 0.50 | 0.00 | 9.23 | 27.9/28.5 | 22.4/21.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.55 | 0.45 | 0.00 | 3.48 | 25.7/25.9 | 24.1/23.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sean Couturier: 1+ goals YES | 11 | 0.190 | 0.168 | +0.073 | +0.052 | $10.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 16 | 0.253 | 0.228 | +0.084 | +0.059 | $12.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Cam York: 1+ goals YES | 6 | 0.092 | 0.084 | +0.028 | +0.020 | $3.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 67 | 0.708 | 0.696 | +0.022 | +0.011 | $6.86 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (54.03 vs 52.46 bp); despite a smaller raw edge (+0.073 vs +0.084/contract); relationships: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26NOV01UTAPHI-PHICYORK8-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (54.03 vs 52.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26NOV01UTAPHI-PHICYORK8-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense suppressed (<= 2 goals)
- **Cam York: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (54.03 vs 14.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: PHI offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes; why: Player prop expression KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no selected over player prop KXNHLAST-26NOV01UTAPHI-UTAVTROCHECK16-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.84 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV01UTAPHI-PHICYORK8-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:OFFENSE_4PLUS (p 0.371): highest fidelity KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2784): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.5027): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.235)
- KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.232)
- KXNHLGOAL-26NOV01UTAPHI-PHICYORK8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.138)
- KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3616, phi -0.225)
- override: Player prop expression KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no selected over player prop KXNHLAST-26NOV01UTAPHI-UTAVTROCHECK16-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.84 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +14.24 (adj +8.04) on $37.50, P(profit) 0.6362, adj growth 69.3 bp · B EV +14.44 (adj +10.18) on $33.47, P(profit) 0.4475, adj growth 89.1 bp · C EV +8.77 (adj +5.83) on $15.93, P(profit) 0.3779, adj growth 49.2 bp · R EV +0.07 (adj +0.03) on $2.00, P(profit) 0.708, adj growth 1.1 bp

## EDM @ NYR  ·  10000 joint draws  ·  424 bet sides mapped, 7 +EV candidates, 4 on card

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
| Alex Formenton: 1+ goals YES | 11 | 0.167 | 0.150 | +0.051 | +0.034 | $7.51 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Filip Hallander: 1+ goals YES | 9 | 0.136 | 0.118 | +0.041 | +0.023 | $4.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ assists YES | 26 | 0.355 | 0.305 | +0.081 | +0.032 | $8.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
| Connor McDavid: 2+ assists NO | 73 | 0.819 | 0.769 | +0.075 | +0.026 | $17.74 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (23.39 vs 10.82 bp); despite a smaller raw edge (+0.051 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.046); failure: EDM offense suppressed (<= 2 goals)
- **Filip Hallander: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (23.39 vs 12.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.014); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (23.39 vs 10.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.032); they share one thesis budget; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.103); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (7.55 vs 3.24 bp); despite a smaller raw edge (+0.075 vs +0.092/contract); relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.046); KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.103); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4261): highest fidelity KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3517): highest fidelity KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.4375): highest fidelity KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes (same contract)
- KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3517, phi -0.187)
- KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3517, phi -0.151)
- KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3517, phi -0.269)
- KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4261, phi -0.323)

portfolios: A EV +9.57 (adj +2.57) on $37.50, P(profit) 0.712, adj growth 22.2 bp · B EV +9.72 (adj +4.95) on $38.93, P(profit) 0.4747, adj growth 43.7 bp · C EV +8.87 (adj +3.87) on $46.18, P(profit) 0.424, adj growth 33.7 bp · R EV +0.87 (adj +0.58) on $2.00, P(profit) 0.1674, adj growth 19.9 bp

## OTT @ ANA  ·  10000 joint draws  ·  426 bet sides mapped, 14 +EV candidates, 4 on card

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
| A.J. Greer: 1+ goals YES | 16 | 0.247 | 0.223 | +0.077 | +0.053 | $11.89 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Ottawa wins by over 2.5 goals NO | 79 | 0.880 | 0.833 | +0.079 | +0.031 | $16.08 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jeff Malott: 1+ goals YES | 10 | 0.136 | 0.125 | +0.029 | +0.019 | $4.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Ottawa over 4.5 goals scored NO | 74 | 0.815 | 0.773 | +0.062 | +0.019 | $10.53 | FUNDED_RESEARCH | $2 | ANA:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: higher confidence-adjusted growth (42.62 vs 13.53 bp); despite a smaller raw edge (+0.077 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: MOSTLY_INDEPENDENT (phi 0.109); KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: MOSTLY_INDEPENDENT (phi 0.013); failure: ANA offense suppressed (<= 2 goals)
- **Ottawa wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no; why: higher confidence-adjusted growth (13.53 vs 12.47 bp); wins across more scripts (relative breadth 1.028 vs 0.578); relationships: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.109); KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.077); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: REINFORCING (phi 0.48); failure: OTT wins by 2+
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (42.62 vs 8.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.024); they share one thesis budget; relationships: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLSPREAD-26NOV01OTTANA-OTT3|no: MOSTLY_INDEPENDENT (phi 0.077); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: MOSTLY_INDEPENDENT (phi 0.002); failure: ANA offense suppressed (<= 2 goals)
- **Ottawa over 4.5 goals scored NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over broad KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.48 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.48); KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4926): highest fidelity KXNHLTEAMTOTAL-26NOV01OTTANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5889): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4358): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3002, phi -0.202)
- KXNHLSPREAD-26NOV01OTTANA-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2025, phi -0.731)
- KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3002, phi -0.155)
- KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3498, phi -0.649)
- override: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over broad KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.48 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.50 (adj +1.09) on $37.50, P(profit) 0.6911, adj growth 8.6 bp · B EV +9.00 (adj +5.36) on $42.62, P(profit) 0.346, adj growth 47.4 bp · C EV +8.38 (adj +5.18) on $34.05, P(profit) 0.2467, adj growth 44.9 bp · R EV +2.02 (adj +1.19) on $10.00, P(profit) 0.2467, adj growth 41.9 bp
equivalent contracts collapsed: KXNHLGAME-26NOV01OTTANA-OTT|no == KXNHLGAME-26NOV01OTTANA-ANA|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
