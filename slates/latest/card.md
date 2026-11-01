# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-01T13:20:06Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.10 | +10.05 | +23.62 | 0.669 | -44.57 | -63.04 | 84.88 |
| B thesis-diversified (joint) ← optimiser card | 149.02 | +32.41 | +19.00 | +25.58 | 0.652 | -54.27 | -72.76 | 165.33 |
| C best expression per thesis | 111.22 | +18.31 | +10.04 | +9.22 | 0.594 | -41.48 | -54.15 | 87.49 |
| R FUNDED research stakes | 23.00 | +3.95 | +2.26 | +0.47 | 0.601 | -10.19 | -14.11 | 0.00 |

## WPG @ CAR  ·  10000 joint draws  ·  414 bet sides mapped, 13 +EV candidates, 4 on card


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
| Alex Iafallo: 1+ goals YES | 11 | 0.152 | 0.139 | +0.035 | +0.022 | $5.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 26 | 0.310 | 0.296 | +0.036 | +0.023 | $7.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Gabriel Vilardi: 1+ goals YES | 22 | 0.269 | 0.253 | +0.037 | +0.021 | $6.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 66 | 0.710 | 0.695 | +0.035 | +0.019 | $15.68 | FUNDED_RESEARCH | $4 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (10.41 vs 5.57 bp); despite a smaller raw edge (+0.035 vs +0.036/contract); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV01WPGCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (5.57 vs 5.45 bp); despite a smaller raw edge (+0.036 vs +0.037/contract); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV01WPGCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: WPG offense suppressed (<= 2 goals)
- **Gabriel Vilardi: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes has the higher standalone adjusted growth (5.57 vs 5.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.011); they share one thesis budget; relationships: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV01WPGCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: WPG offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV01WPGCAR-CAR2|no; why: higher confidence-adjusted growth (3.79 vs 2.86 bp); despite a smaller raw edge (+0.035 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.006 vs 0.855); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.12.
- thesis WPG:OFFENSE_4PLUS (p 0.2937): highest fidelity KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.3586): highest fidelity KXNHLSPREAD-26NOV01WPGCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.2952): highest fidelity KXNHLSPREAD-26NOV01WPGCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01WPGCAR-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4866, phi -0.21)
- KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4866, phi -0.276)
- KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4866, phi -0.258)
- KXNHLGOAL-26NOV01WPGCAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4954, phi -0.218)

portfolios: A EV +3.86 (adj +0.98) on $30.00, P(profit) 0.5425, adj growth 7.6 bp · B EV +4.65 (adj +2.81) on $35.84, P(profit) 0.4737, adj growth 24.4 bp · C EV +2.29 (adj +1.18) on $26.95, P(profit) 0.5563, adj growth 10.3 bp · R EV +0.20 (adj +0.12) on $4.00, P(profit) 0.7102, adj growth 4.0 bp

## MIN @ WSH  ·  10000 joint draws  ·  422 bet sides mapped, 4 +EV candidates, 4 on card


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
| Aliaksei Protas: 1+ goals YES | 18 | 0.246 | 0.228 | +0.056 | +0.038 | $10.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 56 | 0.638 | 0.616 | +0.061 | +0.039 | $20.00 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 18 | 0.225 | 0.211 | +0.035 | +0.021 | $6.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 10 | 0.132 | 0.121 | +0.025 | +0.015 | $3.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (20.05 vs 6.24 bp); relationships: KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: WSH offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-2|no; why: higher confidence-adjusted growth (13.77 vs 0.45 bp); alternative not eligible: confidence-adjusted EV +0.0042 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: MIN offense succeeds (4+ goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (20.05 vs 6.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: WSH offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV01MINWSH-2|yes; why: higher confidence-adjusted growth (5.09 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4234): highest fidelity KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.4222): highest fidelity KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.3561): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3628, phi -0.238)
- KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3561, phi -0.285)
- KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3628, phi -0.199)
- KXNHLGOAL-26NOV01MINWSH-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4222, phi -0.168)

portfolios: A EV +5.90 (adj +3.80) on $30.00, P(profit) 0.4926, adj growth 33.7 bp · B EV +7.30 (adj +4.71) on $40.66, P(profit) 0.4105, adj growth 41.1 bp · C EV +5.26 (adj +3.50) on $30.74, P(profit) 0.7228, adj growth 30.5 bp · R EV +0.53 (adj +0.34) on $5.00, P(profit) 0.6385, adj growth 12.2 bp

## UTA @ PHI  ·  10000 joint draws  ·  404 bet sides mapped, 18 +EV candidates, 4 on card


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
| Sean Couturier: 1+ goals YES | 12 | 0.190 | 0.171 | +0.062 | +0.044 | $9.96 | FUNDED_RESEARCH | $3 | PHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Travis Sanheim: 1+ goals YES | 8 | 0.133 | 0.117 | +0.048 | +0.032 | $6.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 18 | 0.253 | 0.228 | +0.063 | +0.038 | $9.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Cam York: 1+ goals YES | 6 | 0.092 | 0.082 | +0.028 | +0.018 | $3.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (36.11 vs 20.23 bp); despite a smaller raw edge (+0.062 vs +0.063/contract); relationships: KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26NOV01UTAPHI-PHICYORK8-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: PHI offense suppressed (<= 2 goals)
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (36.11 vs 28.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV01UTAPHI-PHICYORK8-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (36.11 vs 20.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV01UTAPHI-PHICYORK8-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PHI offense suppressed (<= 2 goals)
- **Cam York: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (36.11 vs 11.02 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:OFFENSE_4PLUS (p 0.371): highest fidelity KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2784): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.5027): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01UTAPHI-UTA2|no (same contract)
- KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.235)
- KXNHLGOAL-26NOV01UTAPHI-PHITSANHEIM6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.182)
- KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.232)
- KXNHLGOAL-26NOV01UTAPHI-PHICYORK8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.138)

portfolios: A EV +4.90 (adj +2.34) on $30.00, P(profit) 0.6648, adj growth 20.9 bp · B EV +13.47 (adj +8.91) on $30.00, P(profit) 0.5191, adj growth 76.9 bp · C EV +7.00 (adj +4.28) on $26.05, P(profit) 0.1896, adj growth 36.6 bp · R EV +1.46 (adj +1.03) on $3.00, P(profit) 0.1896, adj growth 34.4 bp

## EDM @ NYR  ·  10000 joint draws  ·  416 bet sides mapped, 3 +EV candidates, 3 on card


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
| Alex Formenton: 1+ goals YES | 12 | 0.165 | 0.149 | +0.038 | +0.021 | $5.45 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ assists YES | 28 | 0.355 | 0.307 | +0.060 | +0.013 | $3.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
| Vladislav Gavrikov: 1+ assists YES | 28 | 0.377 | 0.304 | +0.083 | +0.010 | $3.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (8.89 vs 1.83 bp); despite a smaller raw edge (+0.038 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.036); KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|yes; why: higher confidence-adjusted growth (1.83 vs 0.14 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0035 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.036); KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: EDM offense suppressed (<= 2 goals)
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26NOV01EDMNYR-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (1.10 vs 0.07 bp); alternative not eligible: confidence-adjusted EV +0.0025 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4283): highest fidelity KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.4337): highest fidelity KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes (same contract)
- KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.355, phi -0.18)
- KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.355, phi -0.259)
- KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.2 pts; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3512, phi -0.275)

portfolios: A EV +7.66 (adj +2.01) on $30.00, P(profit) 0.6583, adj growth 14.5 bp · B EV +3.31 (adj +1.20) on $12.52, P(profit) 0.4548, adj growth 10.4 bp · C EV +1.79 (adj +0.30) on $7.48, P(profit) 0.5961, adj growth 2.6 bp · R EV +0.59 (adj +0.34) on $2.00, P(profit) 0.1651, adj growth 10.8 bp

## OTT @ ANA  ·  10000 joint draws  ·  424 bet sides mapped, 9 +EV candidates, 3 on card


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
| Ottawa wins by over 2.5 goals NO | 79 | 0.880 | 0.833 | +0.079 | +0.031 | $16.56 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 1.5 goals YES | 29 | 0.381 | 0.333 | +0.076 | +0.029 | $5.63 | FUNDED_RESEARCH | $2 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ottawa over 4.5 goals scored NO | 74 | 0.815 | 0.773 | +0.062 | +0.019 | $7.82 | FUNDED_RESEARCH | $2 | ANA:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Ottawa wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-ANA2|yes; why: higher confidence-adjusted growth (13.53 vs 8.33 bp); wins across more scripts (relative breadth 1.028 vs 0.507); relationships: KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: REINFORCING (phi 0.289); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: REINFORCING (phi 0.48); failure: OTT wins by 2+
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV01OTTANA-OTT3|no has the higher standalone adjusted growth (13.53 vs 8.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.289); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.289); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: DUPLICATIVE (phi 0.328); failure: tight game (one-goal final or OT)
- **Ottawa over 4.5 goals scored NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over player prop KXNHLAST-26NOV01OTTANA-OTTTCHABOT72-1|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.88 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.48); KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: DUPLICATIVE (phi 0.328); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:WINS (p 0.5889): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.3808): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4358): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- KXNHLSPREAD-26NOV01OTTANA-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2025, phi -0.731)
- KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:TIGHT (p 0.4167, phi -0.663)
- KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3498, phi -0.649)
- override: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over player prop KXNHLAST-26NOV01OTTANA-OTTTCHABOT72-1|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.88 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.78 (adj +0.92) on $30.00, P(profit) 0.631, adj growth 8.0 bp · B EV +3.68 (adj +1.37) on $30.00, P(profit) 0.7866, adj growth 12.5 bp · C EV +1.97 (adj +0.78) on $20.00, P(profit) 0.8805, adj growth 7.4 bp · R EV +1.16 (adj +0.43) on $9.00, P(profit) 0.3808, adj growth 15.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
