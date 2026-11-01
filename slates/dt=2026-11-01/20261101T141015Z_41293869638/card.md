# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-01T14:10:15Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.10 | +8.12 | +26.00 | 0.694 | -38.03 | -54.78 | 68.60 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +28.44 | +16.21 | +23.63 | 0.655 | -44.67 | -60.73 | 144.75 |
| C best expression per thesis | 118.42 | +20.66 | +10.63 | +14.01 | 0.606 | -41.88 | -54.84 | 92.60 |
| R FUNDED research stakes | 22.00 | +2.55 | +1.33 | +2.18 | 0.569 | -8.83 | -11.49 | 0.00 |

## WPG @ CAR  ·  10000 joint draws  ·  414 bet sides mapped, 14 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WPG_win | p_overtime | goals | shots CAR/WPG | CAR/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.163 | 0.74 | 0.26 | 0.00 | 6.02 | 33.6/20.7 | 18.4/28.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.133 | 0.57 | 0.43 | 0.48 | 5.91 | 34.0/21.0 | 17.9/30.5 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.124 | 0.75 | 0.25 | 0.00 | 9.29 | 35.2/22.2 | 18.0/26.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.089 | 0.67 | 0.33 | 0.00 | 6.04 | 27.4/26.3 | 23.5/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.51 | 0.49 | 0.46 | 6.0 | 27.8/26.8 | 23.5/24.4 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.075 | 0.69 | 0.31 | 0.00 | 3.46 | 32.3/19.6 | 18.3/29.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Iafallo: 1+ goals YES | 11 | 0.152 | 0.141 | +0.035 | +0.024 | $4.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 71 | 0.765 | 0.750 | +0.041 | +0.026 | $13.76 | FUNDED_RESEARCH | $4 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Gabriel Vilardi: 1+ goals YES | 22 | 0.269 | 0.256 | +0.037 | +0.024 | $5.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 66 | 0.710 | 0.695 | +0.035 | +0.019 | $10.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (11.59 vs 6.80 bp); despite a smaller raw edge (+0.035 vs +0.037/contract); relationships: KXNHLGOAL-26NOV01WPGCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV01WPGCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: WPG offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV01WPGCAR-CARSAHO20-1|no; why: higher confidence-adjusted growth (7.22 vs 3.79 bp); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV01WPGCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: CAR offense succeeds (4+ goals)
- **Gabriel Vilardi: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG5|yes; why: higher confidence-adjusted growth (6.80 vs 4.02 bp); despite a smaller raw edge (+0.037 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.95 vs 0.578); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV01WPGCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV01WPGCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: WPG offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV01WPGCAR-CAR2|no; why: higher confidence-adjusted growth (3.79 vs 2.86 bp); despite a smaller raw edge (+0.035 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.006 vs 0.855); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV01WPGCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.12.
- thesis WPG:OFFENSE_4PLUS (p 0.2937): highest fidelity KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.3586): highest fidelity KXNHLSPREAD-26NOV01WPGCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01WPGCAR-CAR2|no (same contract)
- thesis CAR:SUPPRESSED (p 0.2952): highest fidelity KXNHLSPREAD-26NOV01WPGCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01WPGCAR-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4866, phi -0.21)
- KXNHLGOAL-26NOV01WPGCAR-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4954, phi -0.2)
- KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4866, phi -0.258)
- KXNHLGOAL-26NOV01WPGCAR-CARSAHO20-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4954, phi -0.218)

portfolios: A EV +4.20 (adj +0.95) on $30.00, P(profit) 0.5433, adj growth 7.3 bp · B EV +3.77 (adj +2.40) on $34.99, P(profit) 0.3652, adj growth 21.6 bp · C EV +2.97 (adj +1.48) on $27.39, P(profit) 0.577, adj growth 12.9 bp · R EV +0.22 (adj +0.14) on $4.00, P(profit) 0.765, adj growth 5.2 bp

## MIN @ WSH  ·  10000 joint draws  ·  422 bet sides mapped, 6 +EV candidates, 4 on card


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
| Aliaksei Protas: 1+ goals YES | 18 | 0.246 | 0.228 | +0.056 | +0.038 | $8.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 56 | 0.638 | 0.616 | +0.061 | +0.039 | $16.01 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 18 | 0.225 | 0.211 | +0.035 | +0.021 | $4.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 10 | 0.132 | 0.121 | +0.025 | +0.015 | $3.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (20.05 vs 6.24 bp); relationships: KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: WSH offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV01MINWSH-MINQHUGHES43-1|no; why: higher confidence-adjusted growth (13.77 vs 2.15 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: MIN offense succeeds (4+ goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (20.05 vs 6.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: WSH offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV01MINWSH-3|yes; why: higher confidence-adjusted growth (5.09 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.907 vs 0.755); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4234): highest fidelity KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4222): highest fidelity KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.3561): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3628, phi -0.238)
- KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3561, phi -0.285)
- KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3628, phi -0.199)
- KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4222, phi -0.168)

portfolios: A EV +5.49 (adj +2.45) on $30.00, P(profit) 0.6031, adj growth 21.4 bp · B EV +5.84 (adj +3.77) on $32.55, P(profit) 0.4105, adj growth 33.8 bp · C EV +5.26 (adj +3.50) on $30.74, P(profit) 0.7228, adj growth 30.5 bp · R EV +0.53 (adj +0.34) on $5.00, P(profit) 0.6385, adj growth 12.2 bp

## UTA @ PHI  ·  10000 joint draws  ·  404 bet sides mapped, 20 +EV candidates, 4 on card


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
| Sean Couturier: 1+ goals YES | 12 | 0.190 | 0.171 | +0.062 | +0.044 | $8.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Travis Sanheim: 1+ goals YES | 8 | 0.133 | 0.117 | +0.048 | +0.032 | $5.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 18 | 0.253 | 0.231 | +0.063 | +0.041 | $8.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 66 | 0.708 | 0.695 | +0.032 | +0.019 | $10.77 | FUNDED_RESEARCH | $3 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (36.11 vs 22.95 bp); despite a smaller raw edge (+0.062 vs +0.063/contract); relationships: KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: PHI offense suppressed (<= 2 goals)
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (36.11 vs 28.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (36.11 vs 22.95 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV01UTAPHI-UTA2|no; why: Player prop expression KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no selected over broad KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA4|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:OFFENSE_4PLUS (p 0.371): highest fidelity KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2784): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.5027): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01UTAPHI-UTA2|no (same contract)
- KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.235)
- KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.182)
- KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.232)
- KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3616, phi -0.225)
- override: Player prop expression KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no selected over broad KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA4|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.90 (adj +2.44) on $30.00, P(profit) 0.6648, adj growth 21.9 bp · B EV +10.89 (adj +7.32) on $33.99, P(profit) 0.4702, adj growth 64.6 bp · C EV +7.00 (adj +4.28) on $26.05, P(profit) 0.1896, adj growth 36.6 bp · R EV +0.14 (adj +0.08) on $3.00, P(profit) 0.708, adj growth 3.1 bp

## EDM @ NYR  ·  10000 joint draws  ·  416 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_EDM_win | p_overtime | goals | shots NYR/EDM | NYR/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.52 | 0.48 | 0.00 | 6.04 | 27.1/27.6 | 24.1/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.110 | 0.54 | 0.46 | 0.00 | 9.43 | 28.6/29.1 | 23.4/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.51 | 0.49 | 0.47 | 5.98 | 26.9/27.2 | 24.0/23.7 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.092 | 0.44 | 0.56 | 0.00 | 5.96 | 21.3/32.2 | 27.9/18.2 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.46 | 0.54 | 0.47 | 5.99 | 21.8/33.0 | 29.5/18.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.073 | 0.45 | 0.55 | 0.00 | 9.32 | 23.1/34.3 | 27.2/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 12 | 0.165 | 0.151 | +0.038 | +0.024 | $5.11 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 35 | 0.459 | 0.382 | +0.093 | +0.016 | $5.16 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.69) | EVIDENCE_MIXED | D |
| Ryan Nugent-Hopkins: 1+ assists NO | 64 | 0.717 | 0.671 | +0.061 | +0.015 | $9.16 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ assists YES | 28 | 0.355 | 0.307 | +0.060 | +0.013 | $3.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (11.06 vs 1.83 bp); despite a smaller raw edge (+0.038 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.043); KXNHLAST-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.024); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.036); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|no; why: higher confidence-adjusted growth (2.27 vs 2.13 bp); relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.043); KXNHLAST-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi 0.069); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.112); failure: EDM offense succeeds (4+ goals)
- **Ryan Nugent-Hopkins: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no; why: second expression of the same thesis: KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no has the higher standalone adjusted growth (2.27 vs 2.13 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.069); they share one thesis budget; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.069); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|yes; why: higher confidence-adjusted growth (1.83 vs 0.14 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0035 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.036); KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.112); KXNHLAST-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:SUPPRESSED (p 0.355): highest fidelity KXNHLAST-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.4283): highest fidelity KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.4337): highest fidelity KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes (same contract)
- KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.355, phi -0.18)
- KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 31% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.9 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4283, phi -0.323)
- KXNHLAST-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4283, phi -0.216)
- KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.355, phi -0.259)

portfolios: A EV +6.26 (adj +1.09) on $30.00, P(profit) 0.6673, adj growth 8.8 bp · B EV +4.42 (adj +1.55) on $23.12, P(profit) 0.6129, adj growth 13.8 bp · C EV +3.47 (adj +0.59) on $14.24, P(profit) 0.6772, adj growth 5.2 bp · R EV +0.59 (adj +0.38) on $2.00, P(profit) 0.1651, adj growth 12.4 bp

## OTT @ ANA  ·  10000 joint draws  ·  424 bet sides mapped, 12 +EV candidates, 4 on card


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
| Ottawa wins by over 2.5 goals NO | 79 | 0.880 | 0.833 | +0.079 | +0.031 | $13.37 | FUNDED_RESEARCH | $4 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 1.5 goals YES | 29 | 0.381 | 0.333 | +0.076 | +0.029 | $4.22 | FUNDED_RESEARCH | $2 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ottawa over 4.5 goals scored NO | 74 | 0.815 | 0.773 | +0.062 | +0.019 | $6.43 | FUNDED_RESEARCH | $2 | ANA:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
| A.J. Greer: 1+ goals YES | 16 | 0.247 | 0.181 | +0.077 | +0.011 | $1.34 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Ottawa wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-ANA2|yes; why: higher confidence-adjusted growth (13.53 vs 8.33 bp); wins across more scripts (relative breadth 1.028 vs 0.507); relationships: KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: REINFORCING (phi 0.289); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: REINFORCING (phi 0.48); KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.109); failure: OTT wins by 2+
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV01OTTANA-OTT3|no has the higher standalone adjusted growth (13.53 vs 8.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.289); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.289); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: DUPLICATIVE (phi 0.328); KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: REINFORCING (phi 0.188); failure: tight game (one-goal final or OT)
- **Ottawa over 4.5 goals scored NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over player prop KXNHLAST-26NOV01OTTANA-OTTTCHABOT72-1|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.88 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.48); KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: DUPLICATIVE (phi 0.328); KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: OTT offense succeeds (4+ goals)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: Player prop expression KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes selected over player prop KXNHLAST-26NOV01OTTANA-ANAJLACOMBE2-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.34 vs 0.74 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: MOSTLY_INDEPENDENT (phi 0.109); KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: REINFORCING (phi 0.188); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: MOSTLY_INDEPENDENT (phi 0.013); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:WINS (p 0.5889): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.3808): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4926): highest fidelity KXNHLTEAMTOTAL-26NOV01OTTANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no — Player prop expression KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes selected over player prop KXNHLAST-26NOV01OTTANA-ANAJLACOMBE2-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.34 vs 0.74 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLSPREAD-26NOV01OTTANA-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2025, phi -0.731)
- KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:TIGHT (p 0.4167, phi -0.663)
- KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3498, phi -0.649)
- KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 66% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.2 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3002, phi -0.202)
- override: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over player prop KXNHLAST-26NOV01OTTANA-OTTTCHABOT72-1|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.88 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes selected over player prop KXNHLAST-26NOV01OTTANA-ANAJLACOMBE2-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.34 vs 0.74 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.26 (adj +1.19) on $30.00, P(profit) 0.6947, adj growth 9.2 bp · B EV +3.51 (adj +1.17) on $25.35, P(profit) 0.4537, adj growth 10.8 bp · C EV +1.97 (adj +0.78) on $20.00, P(profit) 0.8805, adj growth 7.4 bp · R EV +1.06 (adj +0.39) on $8.00, P(profit) 0.3808, adj growth 14.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
