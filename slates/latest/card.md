# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-01T15:36:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +25.57 | +8.29 | +24.49 | 0.698 | -33.87 | -48.98 | 71.96 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +30.39 | +17.44 | +26.16 | 0.669 | -46.10 | -63.22 | 155.57 |
| C best expression per thesis | 131.28 | +23.86 | +12.00 | +17.65 | 0.640 | -43.08 | -58.58 | 104.52 |
| R FUNDED research stakes | 23.00 | +2.61 | +1.44 | +1.99 | 0.583 | -8.45 | -11.66 | 0.00 |

## WPG @ CAR  ·  10000 joint draws  ·  414 bet sides mapped, 18 +EV candidates, 4 on card


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
| Alex Iafallo: 1+ goals YES | 11 | 0.156 | 0.144 | +0.040 | +0.027 | $5.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Gabriel Vilardi: 1+ goals YES | 21 | 0.269 | 0.253 | +0.047 | +0.031 | $7.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Adam Lowry: 1+ goals YES | 9 | 0.128 | 0.115 | +0.032 | +0.019 | $3.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 71 | 0.765 | 0.750 | +0.041 | +0.026 | $16.15 | FUNDED_RESEARCH | $5 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (14.76 vs 12.05 bp); despite a smaller raw edge (+0.040 vs +0.047/contract); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV01WPGCAR-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV01WPGCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: WPG offense suppressed (<= 2 goals)
- **Gabriel Vilardi: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (12.05 vs 5.24 bp); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV01WPGCAR-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV01WPGCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: WPG offense suppressed (<= 2 goals)
- **Adam Lowry: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes has the higher standalone adjusted growth (12.05 vs 9.02 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV01WPGCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: WPG offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV01WPGCAR-CARSGOSTISBEHERE4-1|no; why: higher confidence-adjusted growth (7.22 vs 4.11 bp); despite a smaller raw edge (+0.041 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV01WPGCAR-WPGALOWRY17-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.12.
- thesis WPG:OFFENSE_4PLUS (p 0.2937): highest fidelity KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.3586): highest fidelity KXNHLSPREAD-26NOV01WPGCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4151): highest fidelity KXNHLSPREAD-26NOV01WPGCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4866, phi -0.208)
- KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4866, phi -0.258)
- KXNHLGOAL-26NOV01WPGCAR-WPGALOWRY17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4866, phi -0.174)
- KXNHLGOAL-26NOV01WPGCAR-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4954, phi -0.2)

portfolios: A EV +3.83 (adj +1.02) on $30.00, P(profit) 0.5395, adj growth 9.1 bp · B EV +5.69 (adj +3.67) on $33.11, P(profit) 0.4623, adj growth 32.7 bp · C EV +5.10 (adj +2.51) on $36.77, P(profit) 0.4121, adj growth 21.9 bp · R EV +0.28 (adj +0.18) on $5.00, P(profit) 0.765, adj growth 6.4 bp

## MIN @ WSH  ·  10000 joint draws  ·  424 bet sides mapped, 6 +EV candidates, 4 on card


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
| Aliaksei Protas: 1+ goals YES | 18 | 0.246 | 0.228 | +0.056 | +0.038 | $8.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 56 | 0.638 | 0.616 | +0.061 | +0.039 | $16.15 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 18 | 0.225 | 0.213 | +0.035 | +0.022 | $5.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Alex Ovechkin: 1+ goals YES | 21 | 0.257 | 0.244 | +0.036 | +0.023 | $5.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (20.05 vs 7.00 bp); relationships: KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV01MINWSH-WSHAOVECHKIN8-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: WSH offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-2|no; why: higher confidence-adjusted growth (13.77 vs 3.67 bp); relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV01MINWSH-WSHAOVECHKIN8-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: MIN offense succeeds (4+ goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (20.05 vs 7.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV01MINWSH-WSHAOVECHKIN8-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: WSH offense suppressed (<= 2 goals)
- **Alex Ovechkin: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (20.05 vs 6.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4234): highest fidelity KXNHLGOAL-26NOV01MINWSH-WSHAOVECHKIN8-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4222): highest fidelity KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.3561): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3628, phi -0.238)
- KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3561, phi -0.285)
- KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3628, phi -0.199)
- KXNHLGOAL-26NOV01MINWSH-WSHAOVECHKIN8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3628, phi -0.229)

portfolios: A EV +5.54 (adj +3.64) on $30.00, P(profit) 0.4667, adj growth 32.7 bp · B EV +6.06 (adj +3.97) on $35.35, P(profit) 0.4667, adj growth 35.6 bp · C EV +5.26 (adj +3.50) on $30.74, P(profit) 0.7228, adj growth 30.5 bp · R EV +0.53 (adj +0.34) on $5.00, P(profit) 0.6385, adj growth 12.2 bp

## UTA @ PHI  ·  10000 joint draws  ·  404 bet sides mapped, 24 +EV candidates, 4 on card


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
| Sean Couturier: 1+ goals YES | 12 | 0.190 | 0.171 | +0.062 | +0.044 | $8.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 18 | 0.253 | 0.230 | +0.063 | +0.039 | $8.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Noah Cates: 1+ goals YES | 12 | 0.173 | 0.157 | +0.045 | +0.030 | $6.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 66 | 0.708 | 0.695 | +0.032 | +0.019 | $11.24 | FUNDED_RESEARCH | $3 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (36.11 vs 21.57 bp); despite a smaller raw edge (+0.062 vs +0.063/contract); relationships: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26NOV01UTAPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (36.11 vs 21.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26NOV01UTAPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense suppressed (<= 2 goals)
- **Noah Cates: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (36.11 vs 16.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.019); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: PHI offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV01UTAPHI-UTA2|no; why: Player prop expression KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no selected over broad KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA4|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV01UTAPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:OFFENSE_4PLUS (p 0.371): highest fidelity KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2784): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.5027): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01UTAPHI-UTA2|no (same contract)
- KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.235)
- KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.232)
- KXNHLGOAL-26NOV01UTAPHI-PHINCATES27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.201)
- KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3616, phi -0.225)
- override: Player prop expression KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no selected over broad KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA4|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.84 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.08 (adj +1.39) on $30.00, P(profit) 0.6848, adj growth 12.2 bp · B EV +9.73 (adj +6.45) on $34.53, P(profit) 0.4949, adj growth 57.0 bp · C EV +7.00 (adj +4.28) on $26.05, P(profit) 0.1896, adj growth 36.6 bp · R EV +0.14 (adj +0.08) on $3.00, P(profit) 0.708, adj growth 3.1 bp

## EDM @ NYR  ·  10000 joint draws  ·  418 bet sides mapped, 6 +EV candidates, 4 on card


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
| Alex Formenton: 1+ goals YES | 12 | 0.164 | 0.150 | +0.037 | +0.023 | $4.91 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Vladislav Gavrikov: 1+ assists YES | 27 | 0.377 | 0.301 | +0.094 | +0.017 | $3.99 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Connor McDavid: 1+ assists NO | 35 | 0.456 | 0.384 | +0.090 | +0.018 | $6.18 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.69) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ assists YES | 28 | 0.352 | 0.309 | +0.058 | +0.015 | $4.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (10.32 vs 2.22 bp); despite a smaller raw edge (+0.037 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.031); failure: EDM offense suppressed (<= 2 goals)
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26NOV01EDMNYR-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (3.21 vs 0.28 bp); alternative not eligible: confidence-adjusted EV +0.0050 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: NYR offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMRNUGENTHOPKINS93-1|no; why: higher confidence-adjusted growth (3.01 vs 2.02 bp); relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.113); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV01EDMNYR-10|yes; why: higher confidence-adjusted growth (2.22 vs 0.04 bp); wins across more scripts (relative breadth 0.878 vs 0.33); alternative not eligible: confidence-adjusted EV +0.0014 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.031); KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.113); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NYR:OFFENSE_4PLUS (p 0.4337): highest fidelity KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.355): highest fidelity KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.4283): highest fidelity KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes (same contract)
- KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.355, phi -0.177)
- KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.7 pts; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3512, phi -0.275)
- KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 31% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.1 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4283, phi -0.326)
- KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.355, phi -0.26)

portfolios: A EV +5.87 (adj +1.10) on $30.00, P(profit) 0.6335, adj growth 9.2 bp · B EV +5.06 (adj +1.64) on $19.19, P(profit) 0.4494, adj growth 14.6 bp · C EV +4.53 (adj +0.93) on $17.72, P(profit) 0.7914, adj growth 8.1 bp · R EV +0.57 (adj +0.36) on $2.00, P(profit) 0.164, adj growth 11.9 bp

## OTT @ ANA  ·  10000 joint draws  ·  424 bet sides mapped, 14 +EV candidates, 4 on card


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
| Ottawa wins by over 2.5 goals NO | 79 | 0.880 | 0.833 | +0.079 | +0.031 | $13.57 | FUNDED_RESEARCH | $4 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 1.5 goals YES | 29 | 0.381 | 0.333 | +0.076 | +0.029 | $3.94 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jeff Malott: 1+ goals YES | 10 | 0.136 | 0.125 | +0.029 | +0.019 | $3.59 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Ottawa over 4.5 goals scored NO | 74 | 0.815 | 0.773 | +0.062 | +0.019 | $6.72 | FUNDED_RESEARCH | $2 | ANA:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Ottawa wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-ANA2|yes; why: higher confidence-adjusted growth (13.53 vs 8.33 bp); wins across more scripts (relative breadth 1.028 vs 0.507); relationships: KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: REINFORCING (phi 0.289); KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.077); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: REINFORCING (phi 0.48); failure: OTT wins by 2+
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV01OTTANA-OTT3|no has the higher standalone adjusted growth (13.53 vs 8.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.289); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.289); KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.122); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: DUPLICATIVE (phi 0.328); failure: tight game (one-goal final or OT)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV01OTTANA-OTT3|no has the higher standalone adjusted growth (13.53 vs 8.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.077); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: MOSTLY_INDEPENDENT (phi 0.077); KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: MOSTLY_INDEPENDENT (phi 0.122); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: MOSTLY_INDEPENDENT (phi 0.002); failure: ANA offense suppressed (<= 2 goals)
- **Ottawa over 4.5 goals scored NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over player prop KXNHLAST-26NOV01OTTANA-OTTJSANDERSON85-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.48); KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: DUPLICATIVE (phi 0.328); KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:WINS (p 0.5889): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.3808): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4926): highest fidelity KXNHLTEAMTOTAL-26NOV01OTTANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV01OTTANA-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2025, phi -0.731)
- KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:TIGHT (p 0.4167, phi -0.663)
- KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3002, phi -0.155)
- KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3498, phi -0.649)
- override: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over player prop KXNHLAST-26NOV01OTTANA-OTTJSANDERSON85-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +6.26 (adj +1.14) on $30.00, P(profit) 0.6947, adj growth 8.8 bp · B EV +3.86 (adj +1.71) on $27.81, P(profit) 0.4444, adj growth 15.6 bp · C EV +1.97 (adj +0.78) on $20.00, P(profit) 0.8805, adj growth 7.4 bp · R EV +1.08 (adj +0.48) on $8.00, P(profit) 0.4444, adj growth 17.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
