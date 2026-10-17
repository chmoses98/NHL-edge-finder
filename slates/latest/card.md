# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T09:51:30Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +26.50 | +8.14 | +25.22 | 0.696 | -36.78 | -53.89 | 69.23 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +26.26 | +9.27 | +25.13 | 0.712 | -31.90 | -48.94 | 81.91 |
| C best expression per thesis | 101.03 | +19.93 | +7.59 | +18.40 | 0.660 | -31.61 | -45.17 | 66.14 |
| R FUNDED research stakes | 37.00 | +5.98 | +2.32 | +5.42 | 0.678 | -10.66 | -13.70 | 0.00 |

## NJD @ WSH  ·  10000 joint draws  ·  424 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_NJD_win | p_overtime | goals | shots WSH/NJD | WSH/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.60 | 0.40 | 0.00 | 5.99 | 27.9/28.2 | 25.2/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.54 | 0.46 | 0.48 | 5.9 | 27.7/28.3 | 25.1/24.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.102 | 0.56 | 0.44 | 0.00 | 6.01 | 22.3/33.6 | 30.2/18.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.53 | 0.47 | 0.47 | 5.87 | 22.3/33.7 | 30.4/19.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.60 | 0.40 | 0.00 | 9.31 | 29.1/29.7 | 24.2/22.4 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.060 | 0.55 | 0.45 | 0.00 | 9.09 | 23.9/35.7 | 29.6/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 18 | 0.244 | 0.228 | +0.054 | +0.038 | $9.84 | FUNDED_RESEARCH | $3 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 17 | 0.204 | 0.198 | +0.024 | +0.018 | $4.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 29 | 0.374 | 0.324 | +0.069 | +0.020 | $4.60 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ assists NO | 54 | 0.647 | 0.571 | +0.089 | +0.013 | $6.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17NJWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (19.95 vs 4.07 bp); despite a smaller raw edge (+0.054 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT17NJWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.046); KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (19.95 vs 4.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT17NJWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.143); KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: WSH offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (19.95 vs 4.07 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.046); they share one thesis budget; relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.046); KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.143); KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: WSH offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17NJWSH-NJ3|no; why: higher confidence-adjusted growth (1.61 vs 0.30 bp); alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT17NJWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4111): highest fidelity KXNHLAST-26OCT17NJWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4554): highest fidelity KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no (same contract)
- KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3661, phi -0.245)
- KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3661, phi -0.202)
- KXNHLAST-26OCT17NJWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3661, phi -0.293)
- KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.7 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3293, phi -0.271)

portfolios: A EV +5.43 (adj +2.36) on $25.86, P(profit) 0.564, adj growth 20.9 bp · B EV +5.50 (adj +2.85) on $25.60, P(profit) 0.4958, adj growth 24.9 bp · C EV +4.31 (adj +2.35) on $18.51, P(profit) 0.2442, adj growth 20.3 bp · R EV +0.85 (adj +0.60) on $3.00, P(profit) 0.2442, adj growth 20.2 bp

## CAR @ WPG  ·  10000 joint draws  ·  396 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_CAR_win | p_overtime | goals | shots WPG/CAR | WPG/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.130 | 0.41 | 0.59 | 0.00 | 6.01 | 20.8/32.9 | 28.8/17.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.46 | 0.54 | 0.50 | 6.02 | 20.9/32.8 | 29.3/17.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.50 | 0.50 | 0.00 | 6.02 | 26.3/27.0 | 23.6/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.51 | 0.49 | 0.49 | 5.93 | 26.5/27.1 | 23.9/23.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.087 | 0.40 | 0.60 | 0.00 | 9.24 | 22.2/34.4 | 27.3/17.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.48 | 0.52 | 0.00 | 9.33 | 28.0/28.9 | 22.7/22.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 2.5 goals NO | 73 | 0.811 | 0.768 | +0.067 | +0.024 | $18.43 | FUNDED_RESEARCH | $5 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 1.5 goals NO | 61 | 0.697 | 0.651 | +0.070 | +0.024 | $2.18 | FUNDED_RESEARCH | $1 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Winnipeg wins by over 1.5 goals YES | 20 | 0.265 | 0.230 | +0.053 | +0.019 | $2.89 | FUNDED_RESEARCH | $1 | WPG:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Winnipeg over 2.5 goals scored YES | 53 | 0.606 | 0.565 | +0.058 | +0.018 | $1.06 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17CARWPG-CAR2|no; why: higher confidence-adjusted growth (6.78 vs 5.61 bp); despite a smaller raw edge (+0.067 vs +0.070/contract); relationships: KXNHLSPREAD-26OCT17CARWPG-CAR2|no: DUPLICATIVE (phi 0.733); KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: REINFORCING (phi 0.29); KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3|yes: REINFORCING (phi 0.391); failure: CAR wins by 2+
- **Carolina wins by over 1.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17CARWPG-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17CARWPG-CAR3|no has the higher standalone adjusted growth (6.78 vs 5.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.733); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17CARWPG-CAR3|no: DUPLICATIVE (phi 0.733); KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: DUPLICATIVE (phi 0.395); KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3|yes: REINFORCING (phi 0.471); failure: CAR wins by 2+
- **Winnipeg wins by over 1.5 goals YES** — thesis: WPG wins by 2+; alternative: KXNHLSPREAD-26OCT17CARWPG-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17CARWPG-CAR3|no has the higher standalone adjusted growth (6.78 vs 4.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.290); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17CARWPG-CAR3|no: REINFORCING (phi 0.29); KXNHLSPREAD-26OCT17CARWPG-CAR2|no: DUPLICATIVE (phi 0.395); KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3|yes: REINFORCING (phi 0.445); failure: CAR wins (incl. OT/SO)
- **Winnipeg over 2.5 goals scored YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17CARWPG-CAR3|no; why: Broad expression KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.54 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT17CARWPG-CAR3|no: REINFORCING (phi 0.391); KXNHLSPREAD-26OCT17CARWPG-CAR2|no: REINFORCING (phi 0.471); KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: REINFORCING (phi 0.445); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis WPG:WINS (p 0.4783): highest fidelity KXNHLSPREAD-26OCT17CARWPG-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR2|no (same contract)
- thesis WPG:WINS_BY_2PLUS (p 0.2647): highest fidelity KXNHLSPREAD-26OCT17CARWPG-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR2|no (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3742): highest fidelity KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR2|no — Broad expression KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.54 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLSPREAD-26OCT17CARWPG-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3028, phi -0.733)
- KXNHLSPREAD-26OCT17CARWPG-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3028, phi -1.0)
- KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5217, phi -0.627)
- KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:SUPPRESSED (p 0.4042, phi -0.979)
- override: Broad expression KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.54 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.52 (adj +1.20) on $25.86, P(profit) 0.5366, adj growth 10.0 bp · B EV +2.76 (adj +0.97) on $24.57, P(profit) 0.811, adj growth 8.7 bp · C EV +1.81 (adj +0.65) on $20.00, P(profit) 0.811, adj growth 5.9 bp · R EV +0.92 (adj +0.32) on $8.00, P(profit) 0.7352, adj growth 11.0 bp

## VAN @ TBL  ·  10000 joint draws  ·  382 bet sides mapped, 17 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_VAN_win | p_overtime | goals | shots TBL/VAN | TBL/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.157 | 0.72 | 0.28 | 0.00 | 6.04 | 33.2/20.7 | 18.3/28.4 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.127 | 0.58 | 0.42 | 0.49 | 5.88 | 33.5/21.1 | 17.9/30.1 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.104 | 0.73 | 0.27 | 0.00 | 9.21 | 35.0/22.3 | 18.0/26.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.097 | 0.66 | 0.34 | 0.00 | 6.03 | 27.3/26.5 | 23.7/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.53 | 0.47 | 0.43 | 5.96 | 27.6/26.7 | 23.4/24.3 | even strength |
| TBL shot control · low event (<=4) · decided (2+) | 0.075 | 0.70 | 0.30 | 0.00 | 3.48 | 31.8/19.7 | 18.5/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver over 3.5 goals scored YES | 20 | 0.295 | 0.245 | +0.084 | +0.034 | $7.14 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 56 | 0.722 | 0.614 | +0.145 | +0.036 | $9.48 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| John Carlson: 1+ assists NO | 50 | 0.677 | 0.549 | +0.160 | +0.032 | $13.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Tampa Bay over 4.5 goals scored NO | 59 | 0.722 | 0.633 | +0.115 | +0.026 | $6.93 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver over 3.5 goals scored YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17VANTB-VAN3|yes; why: KXNHLSPREAD-26OCT17VANTB-VAN3|yes has the higher standalone adjusted growth (17.01 vs 14.71 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.454); relationships: KXNHLSPREAD-26OCT17VANTB-TB3|no: REINFORCING (phi 0.336); KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLTEAMTOTAL-26OCT17VANTB-TB5|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VAN offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB2|no; why: higher confidence-adjusted growth (11.80 vs 10.96 bp); wins across more scripts (relative breadth 1.008 vs 0.858); relationships: KXNHLTEAMTOTAL-26OCT17VANTB-VAN4|yes: REINFORCING (phi 0.336); KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no: REINFORCING (phi 0.173); KXNHLTEAMTOTAL-26OCT17VANTB-TB5|no: REINFORCING (phi 0.562); failure: TBL wins by 2+
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17VANTB-VAN3|yes; why: KXNHLSPREAD-26OCT17VANTB-VAN3|yes has the higher standalone adjusted growth (17.01 vs 8.75 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.105); relationships: KXNHLTEAMTOTAL-26OCT17VANTB-VAN4|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT17VANTB-TB3|no: REINFORCING (phi 0.173); KXNHLTEAMTOTAL-26OCT17VANTB-TB5|no: REINFORCING (phi 0.229); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay over 4.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17VANTB-VAN3|yes; why: KXNHLSPREAD-26OCT17VANTB-VAN3|yes has the higher standalone adjusted growth (17.01 vs 6.14 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.204); relationships: KXNHLTEAMTOTAL-26OCT17VANTB-VAN4|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLSPREAD-26OCT17VANTB-TB3|no: REINFORCING (phi 0.562); KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no: REINFORCING (phi 0.229); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.16, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, TBL shot control · high event (8+) · decided (2+) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.1795): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB3|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.2838): highest fidelity KXNHLTEAMTOTAL-26OCT17VANTB-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.3154): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB3|no (same contract)
- KXNHLTEAMTOTAL-26OCT17VANTB-VAN4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VAN:SUPPRESSED (p 0.5034, phi -0.651)
- KXNHLSPREAD-26OCT17VANTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.7 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4006, phi -0.759)
- KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.7 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.473, phi -0.235)
- KXNHLTEAMTOTAL-26OCT17VANTB-TB5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.7 pts; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.473, phi -0.656)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT17VANTB-TB4|no less than the minimum stake; KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no kept

portfolios: A EV +8.25 (adj +1.53) on $25.86, P(profit) 0.6426, adj growth 13.6 bp · B EV +10.65 (adj +2.85) on $36.95, P(profit) 0.6746, adj growth 25.2 bp · C EV +7.72 (adj +2.38) on $22.96, P(profit) 0.7221, adj growth 20.6 bp · R EV +1.92 (adj +0.59) on $7.00, P(profit) 0.7138, adj growth 20.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17VANTB-TB|no == KXNHLGAME-26OCT17VANTB-VAN|yes

## SEA @ FLA  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_SEA_win | p_overtime | goals | shots FLA/SEA | FLA/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.53 | 0.47 | 0.00 | 6.04 | 27.5/27.0 | 23.6/23.8 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.109 | 0.60 | 0.40 | 0.00 | 5.95 | 32.7/21.5 | 18.5/28.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.50 | 0.50 | 0.49 | 5.97 | 27.8/27.4 | 24.1/24.4 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.43 | 5.91 | 33.1/21.7 | 18.5/29.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.53 | 0.47 | 0.00 | 9.24 | 29.0/28.5 | 22.7/23.0 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.074 | 0.57 | 0.43 | 0.00 | 9.23 | 34.5/23.1 | 17.9/27.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 1.5 goals NO | 60 | 0.690 | 0.643 | +0.073 | +0.026 | $6.18 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 72 | 0.799 | 0.757 | +0.065 | +0.023 | $12.76 | FUNDED_RESEARCH | $4 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Seattle wins by over 1.5 goals YES | 19 | 0.254 | 0.219 | +0.053 | +0.018 | $2.86 | FUNDED_RESEARCH | $1 | SEA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA3|no; why: higher confidence-adjusted growth (6.18 vs 5.88 bp); relationships: KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: DUPLICATIVE (phi 0.749); KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes: DUPLICATIVE (phi 0.391); failure: FLA wins by 2+
- **Florida wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no has the higher standalone adjusted growth (6.18 vs 5.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.749); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no: DUPLICATIVE (phi 0.749); KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes: REINFORCING (phi 0.292); failure: FLA wins by 2+
- **Seattle wins by over 1.5 goals YES** — thesis: SEA wins by 2+; alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no has the higher standalone adjusted growth (6.18 vs 4.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.391); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no: DUPLICATIVE (phi 0.391); KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: REINFORCING (phi 0.292); failure: FLA wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:WINS (p 0.4726): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-FLA2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2536): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-FLA2|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.36): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT17SEAFLA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3098, phi -1.0)
- KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3098, phi -0.749)
- KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS (p 0.5274, phi -0.616)

portfolios: A EV +3.89 (adj +1.37) on $25.86, P(profit) 0.6902, adj growth 11.0 bp · B EV +2.61 (adj +0.92) on $21.80, P(profit) 0.6902, adj growth 8.2 bp · C EV +2.12 (adj +0.75) on $17.84, P(profit) 0.6902, adj growth 6.6 bp · R EV +0.85 (adj +0.30) on $7.00, P(profit) 0.6902, adj growth 10.2 bp

## NYI @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYI_win | p_overtime | goals | shots TOR/NYI | TOR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.53 | 0.47 | 0.00 | 6.02 | 28.0/28.6 | 25.2/24.2 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.115 | 0.49 | 0.51 | 0.00 | 5.99 | 22.2/34.1 | 30.5/18.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.47 | 5.93 | 28.0/28.6 | 25.2/24.7 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.50 | 0.50 | 0.47 | 5.93 | 22.3/34.2 | 30.8/19.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.57 | 0.43 | 0.00 | 9.3 | 29.4/29.9 | 24.1/23.0 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.072 | 0.48 | 0.52 | 0.00 | 9.41 | 23.9/35.9 | 29.1/18.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_BUF_win | p_overtime | goals | shots MTL/BUF | MTL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.56 | 0.44 | 0.00 | 6.0 | 27.1/27.5 | 24.2/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.54 | 0.46 | 0.50 | 5.98 | 27.1/27.4 | 24.1/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.52 | 0.48 | 0.00 | 9.37 | 28.5/28.8 | 22.9/22.2 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.089 | 0.46 | 0.54 | 0.00 | 5.95 | 21.8/32.7 | 28.9/18.4 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.49 | 0.51 | 0.45 | 5.93 | 21.8/32.8 | 29.3/18.6 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.061 | 0.45 | 0.55 | 0.00 | 9.31 | 23.3/34.5 | 27.6/17.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ DET  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_SJS_win | p_overtime | goals | shots DET/SJS | DET/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.51 | 0.49 | 0.00 | 6.06 | 27.7/27.3 | 23.7/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.46 | 5.96 | 27.8/27.4 | 24.2/24.6 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.097 | 0.58 | 0.42 | 0.00 | 6.03 | 32.6/21.7 | 18.7/28.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.52 | 0.48 | 0.44 | 5.92 | 33.1/21.9 | 18.7/29.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.51 | 0.49 | 0.00 | 9.26 | 29.3/29.1 | 23.1/23.2 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.065 | 0.59 | 0.41 | 0.00 | 9.15 | 34.8/23.3 | 18.2/27.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_OTT_win | p_overtime | goals | shots PHI/OTT | PHI/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.52 | 0.48 | 0.00 | 5.96 | 25.7/26.1 | 22.6/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.50 | 0.50 | 0.48 | 5.8 | 25.6/26.1 | 22.9/22.5 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.102 | 0.42 | 0.58 | 0.00 | 5.94 | 20.6/31.3 | 27.2/17.7 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.46 | 0.54 | 0.48 | 5.76 | 20.4/31.3 | 28.1/17.3 | even strength |
| OTT shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.45 | 0.55 | 0.46 | 2.75 | 19.0/29.7 | 28.2/17.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.49 | 0.51 | 0.00 | 3.46 | 24.7/25.2 | 23.3/22.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYR @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_NYR_win | p_overtime | goals | shots CBJ/NYR | CBJ/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CBJ shot control · normal event (5-7) · decided (2+) | 0.120 | 0.66 | 0.34 | 0.00 | 6.02 | 32.0/20.9 | 18.1/27.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.59 | 0.41 | 0.00 | 6.0 | 26.9/26.3 | 23.1/23.0 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.55 | 0.45 | 0.46 | 5.86 | 32.3/21.0 | 17.8/29.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.47 | 0.53 | 0.46 | 5.91 | 26.9/26.5 | 23.3/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.57 | 0.43 | 0.00 | 9.2 | 28.1/27.5 | 22.0/21.8 | even strength |
| CBJ shot control · high event (8+) · decided (2+) | 0.061 | 0.67 | 0.33 | 0.00 | 9.17 | 33.8/22.1 | 17.5/26.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts CBJ shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_DAL_win | p_overtime | goals | shots CHI/DAL | CHI/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.47 | 0.53 | 0.00 | 6.03 | 25.6/26.0 | 22.4/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.50 | 0.50 | 0.48 | 5.86 | 25.4/25.9 | 22.7/22.2 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.105 | 0.38 | 0.62 | 0.00 | 5.99 | 20.0/31.1 | 26.6/17.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.48 | 0.52 | 0.50 | 5.86 | 20.3/31.0 | 27.7/17.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.46 | 0.54 | 0.00 | 9.31 | 27.2/27.8 | 21.5/21.6 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.067 | 0.37 | 0.63 | 0.00 | 9.26 | 21.8/32.9 | 25.8/16.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dallas wins by over 2.5 goals NO | 72 | 0.802 | 0.759 | +0.068 | +0.025 | $18.43 | FUNDED_RESEARCH | $5 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Chicago over 4.5 goals scored YES | 13 | 0.185 | 0.155 | +0.047 | +0.017 | $2.84 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 60 | 0.686 | 0.640 | +0.069 | +0.024 | $2.03 | FUNDED_RESEARCH | $1 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI6|yes; why: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI6|yes has the higher standalone adjusted growth (9.58 vs 6.77 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.141); relationships: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes: REINFORCING (phi 0.219); KXNHLSPREAD-26OCT17DALCHI-DAL2|no: DUPLICATIVE (phi 0.734); failure: DAL wins by 2+
- **Chicago over 4.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI6|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes selected over broad KXNHLTEAMTOTAL-26OCT17DALCHI-CHI6|yes because adjusted EV is 0.3 pts higher while thesis capture is 0.53 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT17DALCHI-DAL3|no: REINFORCING (phi 0.219); KXNHLSPREAD-26OCT17DALCHI-DAL2|no: REINFORCING (phi 0.288); failure: CHI offense suppressed (<= 2 goals)
- **Dallas wins by over 1.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI6|yes; why: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI6|yes has the higher standalone adjusted growth (9.58 vs 5.24 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.190); relationships: KXNHLSPREAD-26OCT17DALCHI-DAL3|no: DUPLICATIVE (phi 0.734); KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes: REINFORCING (phi 0.288); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis GAME:HIGH_EVENT (p 0.2499): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes — Broad expression KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes selected over broad KXNHLTEAMTOTAL-26OCT17DALCHI-CHI6|yes because adjusted EV is 0.3 pts higher while thesis capture is 0.53 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CHI:WINS (p 0.4623): highest fidelity KXNHLSPREAD-26OCT17DALCHI-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-DAL3|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3466): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-DAL3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT17DALCHI-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3139, phi -0.734)
- KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes: FUNDED_RESEARCH; family MIXED; loses 47% of the draws where the thesis happens; opposing: failure thesis CHI:SUPPRESSED (p 0.4371, phi -0.42)
- KXNHLSPREAD-26OCT17DALCHI-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3139, phi -1.0)
- override: Broad expression KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes selected over broad KXNHLTEAMTOTAL-26OCT17DALCHI-CHI6|yes because adjusted EV is 0.3 pts higher while thesis capture is 0.53 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.25 (adj +1.02) on $25.86, P(profit) 0.7096, adj growth 8.3 bp · B EV +2.90 (adj +1.04) on $23.31, P(profit) 0.8022, adj growth 9.3 bp · C EV +1.98 (adj +0.77) on $2.43, P(profit) 0.0776, adj growth 6.6 bp · R EV +0.92 (adj +0.33) on $7.00, P(profit) 0.6922, adj growth 11.3 bp

## STL @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_STL_win | p_overtime | goals | shots NSH/STL | NSH/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.50 | 0.50 | 0.00 | 6.04 | 27.5/27.5 | 23.8/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.47 | 5.93 | 27.3/27.4 | 24.0/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.51 | 0.49 | 0.00 | 9.35 | 29.0/29.2 | 23.1/22.7 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.072 | 0.58 | 0.42 | 0.00 | 6.02 | 31.9/21.8 | 18.6/27.8 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.069 | 0.43 | 0.57 | 0.00 | 5.95 | 21.8/32.3 | 28.2/18.6 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.46 | 0.54 | 0.45 | 5.87 | 21.9/32.2 | 28.9/18.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BOS_win | p_overtime | goals | shots LAK/BOS | LAK/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.52 | 0.48 | 0.00 | 6.01 | 27.9/27.6 | 24.2/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.49 | 5.86 | 28.0/27.6 | 24.3/24.8 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.107 | 0.58 | 0.42 | 0.00 | 5.99 | 33.1/21.8 | 18.8/29.0 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.58 | 0.42 | 0.49 | 5.9 | 33.6/22.1 | 19.0/30.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.52 | 0.48 | 0.00 | 9.26 | 29.4/29.2 | 23.3/23.4 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.065 | 0.59 | 0.41 | 0.00 | 9.15 | 35.1/23.4 | 18.3/27.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_EDM_win | p_overtime | goals | shots UTA/EDM | UTA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.54 | 0.46 | 0.00 | 6.09 | 27.3/27.3 | 23.9/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.117 | 0.53 | 0.47 | 0.00 | 9.46 | 29.3/29.3 | 23.4/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.47 | 5.98 | 27.5/27.5 | 24.2/24.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.076 | 0.59 | 0.41 | 0.00 | 6.08 | 32.9/22.1 | 19.1/28.7 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.068 | 0.64 | 0.36 | 0.00 | 9.43 | 34.3/23.3 | 18.3/26.7 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.062 | 0.48 | 0.52 | 0.00 | 6.05 | 22.0/32.3 | 28.5/18.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_PIT_win | p_overtime | goals | shots VGK/PIT | VGK/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.65 | 0.35 | 0.00 | 6.03 | 27.6/27.4 | 24.5/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.48 | 5.99 | 27.7/27.5 | 24.3/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.65 | 0.35 | 0.00 | 9.38 | 28.9/28.9 | 23.5/22.0 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.091 | 0.69 | 0.31 | 0.00 | 6.07 | 32.5/21.6 | 19.2/27.7 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.069 | 0.72 | 0.28 | 0.00 | 9.35 | 34.3/23.1 | 18.7/25.8 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.52 | 0.48 | 0.44 | 5.84 | 32.5/21.8 | 18.6/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vegas wins by over 2.5 goals NO | 65 | 0.735 | 0.690 | +0.069 | +0.024 | $17.78 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vegas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17PITVGK-VGK2|no; why: higher confidence-adjusted growth (5.61 vs 2.23 bp); wins across more scripts (relative breadth 1.028 vs 0.91); relationships: only recommended bet in this game; failure: VGK wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.414): highest fidelity KXNHLSPREAD-26OCT17PITVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17PITVGK-VGK3|no (same contract)
- KXNHLSPREAD-26OCT17PITVGK-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.3835, phi -0.762)

portfolios: A EV +2.16 (adj +0.66) on $20.69, P(profit) 0.6165, adj growth 5.5 bp · B EV +1.83 (adj +0.64) on $17.78, P(profit) 0.7345, adj growth 5.7 bp · C EV +1.99 (adj +0.69) on $19.29, P(profit) 0.7345, adj growth 6.1 bp · R EV +0.51 (adj +0.18) on $5.00, P(profit) 0.7345, adj growth 6.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
