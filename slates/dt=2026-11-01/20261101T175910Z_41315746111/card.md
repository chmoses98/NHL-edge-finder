# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-01T17:59:10Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +38.57 | +16.13 | +34.52 | 0.699 | -44.75 | -63.81 | 139.44 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +40.20 | +24.93 | +33.04 | 0.672 | -54.63 | -72.17 | 221.03 |
| C best expression per thesis | 118.31 | +32.02 | +18.65 | +23.60 | 0.632 | -57.19 | -69.52 | 160.64 |
| R FUNDED research stakes | 20.00 | +3.86 | +2.43 | +1.86 | 0.574 | -9.50 | -11.03 | 0.00 |

## WPG @ CAR  ·  10000 joint draws  ·  452 bet sides mapped, 24 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.709 / away 0.291

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WPG_win | p_overtime | goals | shots CAR/WPG | CAR/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.167 | 0.72 | 0.28 | 0.00 | 6.02 | 33.6/20.8 | 18.4/28.6 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.127 | 0.59 | 0.41 | 0.45 | 5.88 | 33.7/21.0 | 17.9/30.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.126 | 0.73 | 0.27 | 0.00 | 9.44 | 35.5/22.2 | 17.8/27.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.088 | 0.67 | 0.33 | 0.00 | 6.05 | 27.6/26.6 | 23.8/23.2 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.078 | 0.70 | 0.30 | 0.00 | 3.52 | 32.3/19.6 | 18.3/29.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.57 | 0.43 | 0.47 | 5.92 | 27.5/26.7 | 23.5/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Gabriel Vilardi: 1+ goals YES | 20 | 0.270 | 0.252 | +0.059 | +0.040 | $9.55 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 11 | 0.156 | 0.143 | +0.039 | +0.026 | $5.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ assists NO | 54 | 0.618 | 0.576 | +0.060 | +0.019 | $8.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CAR:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 64 | 0.712 | 0.673 | +0.055 | +0.017 | $2.17 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Gabriel Vilardi: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes; why: higher confidence-adjusted growth (20.96 vs 14.28 bp); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26NOV01WPGCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLSPREAD-26NOV01WPGCAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.143); failure: WPG offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes; why: Player prop expression KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes selected over player prop KXNHLAST-26NOV01WPGCAR-WPGCPERFETTI91-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.27 vs 0.59 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26NOV01WPGCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26NOV01WPGCAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.116); failure: WPG offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ assists NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV01WPGCAR-CAR2|no; why: KXNHLSPREAD-26NOV01WPGCAR-CAR2|no has the higher standalone adjusted growth (5.39 vs 3.17 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.208); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26NOV01WPGCAR-CAR3|no: REINFORCING (phi 0.202); failure: CAR offense succeeds (4+ goals)
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV01WPGCAR-CAR2|no; why: Broad expression KXNHLSPREAD-26NOV01WPGCAR-CAR3|no selected over player prop KXNHLAST-26NOV01WPGCAR-CARSGOSTISBEHERE4-2|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.116); KXNHLAST-26NOV01WPGCAR-CARSAHO20-1|no: REINFORCING (phi 0.202); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis WPG:OFFENSE_4PLUS (p 0.3028): highest fidelity KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes — Player prop expression KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes selected over player prop KXNHLAST-26NOV01WPGCAR-WPGCPERFETTI91-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.27 vs 0.59 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis WPG:WINS (p 0.3612): highest fidelity KXNHLSPREAD-26NOV01WPGCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV01WPGCAR-WPGCPERFETTI91-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.2899): highest fidelity KXNHLSPREAD-26NOV01WPGCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01WPGCAR-CAR2|no — Broad expression KXNHLSPREAD-26NOV01WPGCAR-CAR3|no selected over player prop KXNHLAST-26NOV01WPGCAR-CARSGOSTISBEHERE4-2|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26NOV01WPGCAR-WPGGVILARDI13-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4871, phi -0.258)
- KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4871, phi -0.207)
- KXNHLAST-26NOV01WPGCAR-CARSAHO20-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4987, phi -0.28)
- KXNHLSPREAD-26NOV01WPGCAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.4104, phi -0.763)
- override: Broad expression KXNHLSPREAD-26NOV01WPGCAR-CAR3|no selected over player prop KXNHLAST-26NOV01WPGCAR-CARSGOSTISBEHERE4-2|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes selected over player prop KXNHLAST-26NOV01WPGCAR-WPGCPERFETTI91-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.27 vs 0.59 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.00 (adj +1.73) on $30.00, P(profit) 0.547, adj growth 14.9 bp · B EV +5.56 (adj +3.37) on $25.63, P(profit) 0.3855, adj growth 30.0 bp · C EV +5.79 (adj +3.04) on $24.56, P(profit) 0.428, adj growth 26.3 bp · R EV +0.08 (adj +0.03) on $1.00, P(profit) 0.7115, adj growth 1.0 bp

## MIN @ WSH  ·  10000 joint draws  ·  426 bet sides mapped, 6 +EV candidates, 4 on card

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
| Aliaksei Protas: 1+ goals YES | 18 | 0.246 | 0.225 | +0.056 | +0.034 | $7.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 56 | 0.638 | 0.618 | +0.061 | +0.040 | $15.96 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 18 | 0.225 | 0.211 | +0.035 | +0.021 | $4.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 24 | 0.322 | 0.276 | +0.069 | +0.023 | $4.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (16.31 vs 6.24 bp); relationships: KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.052); failure: WSH offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-2|no; why: higher confidence-adjusted growth (14.66 vs 3.67 bp); relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: MIN offense succeeds (4+ goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (16.31 vs 6.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.11); failure: WSH offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (16.31 vs 6.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.052); they share one thesis budget; relationships: KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.052); KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.11); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4234): highest fidelity KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4222): highest fidelity KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV01MINWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3628, phi -0.238)
- KXNHLGOAL-26NOV01MINWSH-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3561, phi -0.285)
- KXNHLGOAL-26NOV01MINWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3628, phi -0.199)
- KXNHLAST-26NOV01MINWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3628, phi -0.251)

portfolios: A EV +5.88 (adj +2.70) on $30.00, P(profit) 0.6589, adj growth 23.8 bp · B EV +5.88 (adj +3.34) on $32.20, P(profit) 0.4822, adj growth 30.1 bp · C EV +4.91 (adj +3.11) on $29.54, P(profit) 0.7228, adj growth 27.3 bp · R EV +0.42 (adj +0.28) on $4.00, P(profit) 0.6385, adj growth 10.3 bp

## UTA @ PHI  ·  10000 joint draws  ·  406 bet sides mapped, 25 +EV candidates, 4 on card

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
| Sean Couturier: 1+ goals YES | 11 | 0.190 | 0.168 | +0.073 | +0.052 | $9.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 16 | 0.253 | 0.228 | +0.084 | +0.059 | $12.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 66 | 0.708 | 0.695 | +0.032 | +0.019 | $10.93 | FUNDED_RESEARCH | $3 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 11 | 0.138 | 0.129 | +0.021 | +0.012 | $2.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (54.03 vs 52.46 bp); despite a smaller raw edge (+0.073 vs +0.084/contract); relationships: KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV01UTAPHI-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (54.03 vs 52.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV01UTAPHI-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes; why: KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes has the higher standalone adjusted growth (8.45 vs 3.63 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.154); relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV01UTAPHI-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: UTA offense succeeds (4+ goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01UTAPHI-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (2.96 vs 0.52 bp); alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:OFFENSE_4PLUS (p 0.371): highest fidelity KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2784): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.5027): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV01UTAPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.235)
- KXNHLGOAL-26NOV01UTAPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4137, phi -0.232)
- KXNHLGOAL-26NOV01UTAPHI-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3616, phi -0.225)
- KXNHLGOAL-26NOV01UTAPHI-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4136, phi -0.192)

portfolios: A EV +11.39 (adj +6.43) on $30.00, P(profit) 0.6362, adj growth 57.2 bp · B EV +13.07 (adj +9.12) on $35.29, P(profit) 0.4511, adj growth 80.2 bp · C EV +8.77 (adj +5.83) on $15.93, P(profit) 0.3779, adj growth 49.2 bp · R EV +0.14 (adj +0.08) on $3.00, P(profit) 0.708, adj growth 3.1 bp

## EDM @ NYR  ·  10000 joint draws  ·  424 bet sides mapped, 4 +EV candidates, 4 on card

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
| Filip Hallander: 1+ goals YES | 8 | 0.136 | 0.122 | +0.051 | +0.037 | $7.07 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 12 | 0.167 | 0.152 | +0.040 | +0.024 | $5.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 36 | 0.458 | 0.388 | +0.082 | +0.012 | $4.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.69) | EVIDENCE_MIXED | D |
| Vladislav Gavrikov: 1+ assists YES | 26 | 0.375 | 0.284 | +0.102 | +0.011 | $2.25 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Filip Hallander: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes; why: higher confidence-adjusted growth (37.05 vs 11.50 bp); relationships: KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (11.50 vs 1.10 bp); despite a smaller raw edge (+0.040 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0100 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (1.25 vs 0.92 bp); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: EDM offense succeeds (4+ goals)
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26NOV01EDMNYR-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (1.23 vs 0.88 bp); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4261): highest fidelity KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.3517): highest fidelity KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.4375): highest fidelity KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes (same contract)
- KXNHLGOAL-26NOV01EDMNYR-EDMFHALLANDER11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3517, phi -0.151)
- KXNHLGOAL-26NOV01EDMNYR-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3517, phi -0.187)
- KXNHLAST-26NOV01EDMNYR-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 31% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.8 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4261, phi -0.323)
- KXNHLAST-26NOV01EDMNYR-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.0 pts; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3546, phi -0.264)

portfolios: A EV +10.91 (adj +4.44) on $30.00, P(profit) 0.548, adj growth 38.0 bp · B EV +7.59 (adj +4.28) on $18.54, P(profit) 0.4076, adj growth 37.6 bp · C EV +4.17 (adj +1.49) on $14.23, P(profit) 0.3128, adj growth 12.9 bp · R EV +1.20 (adj +0.87) on $2.00, P(profit) 0.1364, adj growth 29.9 bp

## OTT @ ANA  ·  10000 joint draws  ·  426 bet sides mapped, 16 +EV candidates, 4 on card

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
| A.J. Greer: 1+ goals YES | 16 | 0.247 | 0.223 | +0.077 | +0.053 | $10.70 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Ottawa wins by over 2.5 goals NO | 79 | 0.880 | 0.833 | +0.079 | +0.031 | $14.46 | FUNDED_RESEARCH | $4 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jeff Malott: 1+ goals YES | 10 | 0.136 | 0.125 | +0.029 | +0.019 | $3.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Ottawa over 4.5 goals scored NO | 74 | 0.815 | 0.773 | +0.062 | +0.019 | $9.47 | FUNDED_RESEARCH | $3 | ANA:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: higher confidence-adjusted growth (42.62 vs 13.53 bp); despite a smaller raw edge (+0.077 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: MOSTLY_INDEPENDENT (phi 0.109); KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: MOSTLY_INDEPENDENT (phi 0.013); failure: ANA offense suppressed (<= 2 goals)
- **Ottawa wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-ANA2|yes; why: higher confidence-adjusted growth (13.53 vs 8.33 bp); wins across more scripts (relative breadth 1.028 vs 0.507); relationships: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.109); KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.077); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: REINFORCING (phi 0.48); failure: OTT wins by 2+
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (42.62 vs 8.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.024); they share one thesis budget; relationships: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLSPREAD-26NOV01OTTANA-OTT3|no: MOSTLY_INDEPENDENT (phi 0.077); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: MOSTLY_INDEPENDENT (phi 0.002); failure: ANA offense suppressed (<= 2 goals)
- **Ottawa over 4.5 goals scored NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over player prop KXNHLAST-26NOV01OTTANA-OTTJSANDERSON85-1|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.48); KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4926): highest fidelity KXNHLTEAMTOTAL-26NOV01OTTANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5889): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.3808): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT3|no (same contract)
- KXNHLGOAL-26NOV01OTTANA-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3002, phi -0.202)
- KXNHLSPREAD-26NOV01OTTANA-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2025, phi -0.731)
- KXNHLGOAL-26NOV01OTTANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3002, phi -0.155)
- KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3498, phi -0.649)
- override: Broad expression KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5|no selected over player prop KXNHLAST-26NOV01OTTANA-OTTJSANDERSON85-1|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.79 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.40 (adj +0.83) on $30.00, P(profit) 0.5477, adj growth 5.5 bp · B EV +8.10 (adj +4.82) on $38.33, P(profit) 0.346, adj growth 43.2 bp · C EV +8.38 (adj +5.18) on $34.05, P(profit) 0.2467, adj growth 44.9 bp · R EV +2.01 (adj +1.17) on $10.00, P(profit) 0.2467, adj growth 41.4 bp
equivalent contracts collapsed: KXNHLGAME-26NOV01OTTANA-OTT|no == KXNHLGAME-26NOV01OTTANA-ANA|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
