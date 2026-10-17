# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T16:28:20Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.96 | +28.15 | +8.09 | +27.43 | 0.794 | -14.42 | -25.87 | 75.26 |
| B thesis-diversified (joint) ← optimiser card | 148.16 | +23.40 | +11.96 | +21.82 | 0.746 | -19.70 | -30.15 | 113.65 |
| C best expression per thesis | 149.98 | +24.31 | +11.45 | +21.76 | 0.710 | -27.18 | -38.87 | 106.20 |
| R FUNDED research stakes | 21.00 | +3.46 | +1.60 | +2.12 | 0.642 | -5.74 | -8.05 | 0.00 |

## NJD @ WSH  ·  10000 joint draws  ·  438 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.515 / away 0.485

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_NJD_win | p_overtime | goals | shots WSH/NJD | WSH/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.61 | 0.39 | 0.00 | 6.05 | 27.6/28.0 | 24.9/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.55 | 0.45 | 0.47 | 5.93 | 27.8/28.2 | 25.0/24.4 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.098 | 0.56 | 0.44 | 0.00 | 5.98 | 22.5/33.9 | 30.6/18.9 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.52 | 0.48 | 0.48 | 5.88 | 22.1/33.6 | 30.4/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.61 | 0.39 | 0.00 | 9.27 | 29.3/29.9 | 24.1/22.8 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.059 | 0.55 | 0.45 | 0.48 | 2.77 | 26.4/26.9 | 25.5/25.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 17 | 0.244 | 0.224 | +0.064 | +0.044 | $4.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 17 | 0.206 | 0.195 | +0.027 | +0.015 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 76 | 0.798 | 0.786 | +0.026 | +0.014 | $5.48 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 12 | 0.146 | 0.138 | +0.018 | +0.011 | $1.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes; why: higher confidence-adjusted growth (28.36 vs 3.31 bp); relationships: KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT17NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (28.36 vs 3.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT17NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: WSH offense suppressed (<= 2 goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NJWSH-NJJBRATT63-1|no; why: higher confidence-adjusted growth (2.32 vs 1.67 bp); despite a smaller raw edge (+0.026 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT17NJWSH-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: NJD offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NJWSH-NJALOMBARDI93-1|yes; why: higher confidence-adjusted growth (2.24 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4117): highest fidelity KXNHLSPREAD-26OCT17NJWSH-NJ2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4673): highest fidelity KXNHLSPREAD-26OCT17NJWSH-NJ2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:OFFENSE_4PLUS (p 0.3188): highest fidelity KXNHLGOAL-26OCT17NJWSH-NJCGLASS12-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17NJWSH-NJCGLASS12-1|yes (same contract)
- KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3653, phi -0.23)
- KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3653, phi -0.201)
- KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3188, phi -0.235)
- KXNHLGOAL-26OCT17NJWSH-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4673, phi -0.204)

portfolios: A EV +2.90 (adj +1.03) on $12.71, P(profit) 0.477, adj growth 9.8 bp · B EV +2.19 (adj +1.44) on $12.71, P(profit) 0.4405, adj growth 13.6 bp · C EV +3.27 (adj +1.99) on $20.22, P(profit) 0.3447, adj growth 18.4 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.7985, adj growth 1.3 bp

## CAR @ WPG  ·  10000 joint draws  ·  396 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.358 / away 0.642

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_CAR_win | p_overtime | goals | shots WPG/CAR | WPG/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.128 | 0.42 | 0.58 | 0.00 | 6.0 | 20.9/32.9 | 28.9/17.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.46 | 0.54 | 0.47 | 5.93 | 20.8/32.7 | 29.2/17.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.48 | 0.52 | 0.00 | 6.03 | 26.4/27.3 | 23.7/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.48 | 0.52 | 0.48 | 5.94 | 26.5/27.2 | 23.8/23.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.088 | 0.39 | 0.61 | 0.00 | 9.3 | 22.2/34.2 | 26.9/17.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.50 | 0.50 | 0.00 | 9.34 | 28.2/28.8 | 22.6/22.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Winnipeg wins by over 1.5 goals YES | 18 | 0.260 | 0.218 | +0.070 | +0.027 | $2.46 | FUNDED_RESEARCH | $1 | WPG:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mike Reilly: 1+ goals YES | 4 | 0.057 | 0.055 | +0.014 | +0.012 | $1.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 73 | 0.777 | 0.764 | +0.033 | +0.020 | $6.08 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Kyle Connor: 1+ goals YES | 37 | 0.412 | 0.400 | +0.025 | +0.014 | $1.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_STRONGER | D |
- **Winnipeg wins by over 1.5 goals YES** — thesis: WPG wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes; why: higher confidence-adjusted growth (10.42 vs 7.54 bp); relationships: KXNHLGOAL-26OCT17CARWPG-CARMREILLY6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.066); KXNHLGOAL-26OCT17CARWPG-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.13); KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: REINFORCING (phi 0.205); failure: CAR wins (incl. OT/SO)
- **Mike Reilly: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17CARWPG-CARMJANKOWSKI77-1|yes; why: higher confidence-adjusted growth (7.99 vs 0.47 bp); alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: INTENTIONAL_DIVERSIFIER (phi -0.066); KXNHLGOAL-26OCT17CARWPG-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CAR offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes has the higher standalone adjusted growth (10.42 vs 4.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.130); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: MOSTLY_INDEPENDENT (phi 0.13); KXNHLGOAL-26OCT17CARWPG-CARMREILLY6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CAR offense succeeds (4+ goals)
- **Kyle Connor: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes; why: Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.54 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: REINFORCING (phi 0.205); KXNHLGOAL-26OCT17CARWPG-CARMREILLY6-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17CARWPG-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:WINS_BY_2PLUS (p 0.2602): highest fidelity KXNHLSPREAD-26OCT17CARWPG-WPG2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-WPG2|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3734): highest fidelity KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-WPG2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.4733): highest fidelity KXNHLSPREAD-26OCT17CARWPG-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-WPG2|yes — Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.54 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5267, phi -0.626)
- KXNHLGOAL-26OCT17CARWPG-CARMREILLY6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:SUPPRESSED (p 0.3699, phi -0.099)
- KXNHLGOAL-26OCT17CARWPG-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4113, phi -0.211)
- KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4046, phi -0.315)
- override: Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.54 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.70 (adj +0.84) on $12.71, P(profit) 0.4221, adj growth 7.6 bp · B EV +1.64 (adj +0.91) on $10.90, P(profit) 0.4862, adj growth 8.6 bp · C EV +1.42 (adj +0.55) on $3.86, P(profit) 0.2602, adj growth 5.1 bp · R EV +0.46 (adj +0.20) on $3.00, P(profit) 0.2602, adj growth 7.3 bp

## VAN @ TBL  ·  10000 joint draws  ·  382 bet sides mapped, 27 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.760 / away 0.239

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_VAN_win | p_overtime | goals | shots TBL/VAN | TBL/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.156 | 0.71 | 0.29 | 0.00 | 5.95 | 33.1/20.7 | 18.2/28.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.55 | 0.45 | 0.48 | 5.9 | 33.4/21.1 | 18.0/30.0 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.105 | 0.73 | 0.27 | 0.00 | 9.3 | 35.0/22.1 | 17.9/26.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.101 | 0.66 | 0.34 | 0.00 | 6.03 | 27.4/26.6 | 23.7/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.54 | 0.46 | 0.48 | 5.9 | 27.4/26.6 | 23.3/24.0 | even strength |
| TBL shot control · low event (<=4) · decided (2+) | 0.069 | 0.68 | 0.32 | 0.00 | 3.44 | 31.8/19.8 | 18.5/29.3 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 1.5 goals NO | 42 | 0.607 | 0.482 | +0.170 | +0.045 | $2.66 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 54 | 0.726 | 0.602 | +0.168 | +0.044 | $5.55 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ goals NO | 58 | 0.647 | 0.627 | +0.050 | +0.030 | $4.94 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Jake Guentzel: 1+ goals NO | 60 | 0.665 | 0.646 | +0.048 | +0.029 | $5.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB3|no; why: higher confidence-adjusted growth (18.13 vs 17.46 bp); relationships: KXNHLSPREAD-26OCT17VANTB-TB3|no: DUPLICATIVE (phi 0.765); KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.208); KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no: REINFORCING (phi 0.168); failure: TBL wins by 2+
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17VANTB-TB2|no has the higher standalone adjusted growth (18.13 vs 17.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.765); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: DUPLICATIVE (phi 0.765); KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.184); KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no: REINFORCING (phi 0.167); failure: TBL wins by 2+
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT17VANTB-TB2|no; why: KXNHLTEAMTOTAL-26OCT17VANTB-TB2|no has the higher standalone adjusted growth (20.57 vs 8.47 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.199); relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: REINFORCING (phi 0.208); KXNHLSPREAD-26OCT17VANTB-TB3|no: REINFORCING (phi 0.184); KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: TBL offense succeeds (4+ goals)
- **Jake Guentzel: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT17VANTB-TB2|no; why: KXNHLTEAMTOTAL-26OCT17VANTB-TB2|no has the higher standalone adjusted growth (20.57 vs 7.93 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.212); relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: REINFORCING (phi 0.168); KXNHLSPREAD-26OCT17VANTB-TB3|no: REINFORCING (phi 0.167); KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.16, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, TBL shot control · high event (8+) · decided (2+) 0.10.
- thesis TBL:SUPPRESSED (p 0.3164): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.1871): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no (same contract)
- thesis VAN:WINS (p 0.3796): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no (same contract)
- KXNHLSPREAD-26OCT17VANTB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 19.2 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3928, phi -1.0)
- KXNHLSPREAD-26OCT17VANTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 19.1 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3928, phi -0.765)
- KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.477, phi -0.25)
- KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.477, phi -0.248)

portfolios: A EV +4.40 (adj +0.89) on $12.71, P(profit) 0.7912, adj growth 8.5 bp · B EV +3.52 (adj +1.21) on $18.32, P(profit) 0.6405, adj growth 11.6 bp · C EV +5.68 (adj +2.30) on $13.11, P(profit) 0.6561, adj growth 21.4 bp · R EV +1.16 (adj +0.36) on $5.00, P(profit) 0.6744, adj growth 13.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17VANTB-TB|no == KXNHLGAME-26OCT17VANTB-VAN|yes

## SEA @ FLA  ·  10000 joint draws  ·  418 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.632 / away 0.368

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_SEA_win | p_overtime | goals | shots FLA/SEA | FLA/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.50 | 0.50 | 0.00 | 6.02 | 27.2/26.9 | 23.2/23.7 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.108 | 0.58 | 0.42 | 0.00 | 6.0 | 32.9/21.5 | 18.5/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.49 | 5.94 | 27.5/27.1 | 23.7/24.2 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.55 | 0.45 | 0.49 | 5.91 | 33.0/21.6 | 18.5/29.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.57 | 0.43 | 0.00 | 9.4 | 29.3/28.8 | 23.2/22.8 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.071 | 0.57 | 0.43 | 0.00 | 9.29 | 34.9/23.1 | 17.8/27.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 10 | 0.148 | 0.133 | +0.042 | +0.027 | $2.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 14 | 0.193 | 0.177 | +0.044 | +0.029 | $2.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 11 | 0.155 | 0.140 | +0.038 | +0.023 | $2.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 64 | 0.709 | 0.690 | +0.052 | +0.034 | $7.33 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes; why: higher confidence-adjusted growth (16.42 vs 11.42 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes; why: higher confidence-adjusted growth (13.82 vs 11.42 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: SEA offense suppressed (<= 2 goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes; why: higher confidence-adjusted growth (11.42 vs 7.37 bp); despite a smaller raw edge (+0.038 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.906 vs 0.535); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: SEA offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17SEAFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (11.32 vs 8.77 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:OFFENSE_4PLUS (p 0.3753): highest fidelity KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4|yes (same contract)
- thesis FLA:SUPPRESSED (p 0.3867): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.2633): highest fidelity KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.183)
- KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.198)
- KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.205)
- KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4008, phi -0.247)

portfolios: A EV +1.99 (adj +0.47) on $12.71, P(profit) 0.6479, adj growth 4.4 bp · B EV +3.05 (adj +1.95) on $14.61, P(profit) 0.4163, adj growth 18.5 bp · C EV +2.46 (adj +1.38) on $15.64, P(profit) 0.7518, adj growth 12.8 bp · R EV +0.16 (adj +0.10) on $2.00, P(profit) 0.7086, adj growth 4.0 bp

## NYI @ TOR  ·  10000 joint draws  ·  428 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.543 / away 0.457

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYI_win | p_overtime | goals | shots TOR/NYI | TOR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.53 | 0.47 | 0.00 | 6.0 | 28.1/28.5 | 25.1/24.5 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.106 | 0.46 | 0.54 | 0.00 | 5.95 | 22.0/34.1 | 30.3/18.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.47 | 5.98 | 28.0/28.6 | 25.4/24.6 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.50 | 0.50 | 0.49 | 5.95 | 22.1/34.2 | 30.9/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.54 | 0.46 | 0.00 | 9.28 | 29.4/30.3 | 24.5/23.2 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.075 | 0.48 | 0.52 | 0.00 | 9.2 | 24.0/36.2 | 29.8/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ondrej Palat: 1+ goals YES | 11 | 0.141 | 0.132 | +0.024 | +0.015 | $1.42 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.243 | 0.234 | +0.022 | +0.012 | $1.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Matias Maccelli: 1+ goals YES | 18 | 0.217 | 0.201 | +0.027 | +0.010 | $1.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (4.57 vs 1.83 bp); relationships: KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT17NYITOR-NYIMMACCELLI63-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: NYI offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NYITOR-NYIMMACCELLI63-1|yes; why: higher confidence-adjusted growth (1.83 vs 1.45 bp); despite a smaller raw edge (+0.022 vs +0.027/contract); relationships: KXNHLGOAL-26OCT17NYITOR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT17NYITOR-NYIMMACCELLI63-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: NYI offense suppressed (<= 2 goals)
- **Matias Maccelli: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (1.83 vs 1.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT17NYITOR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.3878): highest fidelity KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes (same contract)
- KXNHLGOAL-26OCT17NYITOR-NYIOPALAT81-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3934, phi -0.172)
- KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3934, phi -0.236)
- KXNHLGOAL-26OCT17NYITOR-NYIMMACCELLI63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3934, phi -0.217)

portfolios: A EV +0.82 (adj +0.42) on $5.58, P(profit) 0.4862, adj growth 3.9 bp · B EV +0.56 (adj +0.31) on $3.80, P(profit) 0.4862, adj growth 2.9 bp · C EV +0.19 (adj +0.11) on $1.99, P(profit) 0.2432, adj growth 1.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ MTL  ·  10000 joint draws  ·  412 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.558 / away 0.442

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_BUF_win | p_overtime | goals | shots MTL/BUF | MTL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.55 | 0.45 | 0.00 | 6.03 | 27.3/27.6 | 24.2/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.47 | 5.98 | 27.4/27.8 | 24.6/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.55 | 0.45 | 0.00 | 9.28 | 28.7/29.1 | 23.5/22.2 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.086 | 0.49 | 0.51 | 0.00 | 6.07 | 21.7/32.7 | 28.9/18.3 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.50 | 0.50 | 0.43 | 5.91 | 21.6/32.5 | 29.0/18.4 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.063 | 0.45 | 0.55 | 0.00 | 9.21 | 23.3/34.7 | 27.9/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alexandre Carrier: 1+ goals YES | 4 | 0.063 | 0.056 | +0.020 | +0.013 | $1.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 23 | 0.285 | 0.269 | +0.043 | +0.026 | $3.05 | FUNDED_RESEARCH | $1 | BUF:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Noah Ostlund: 1+ goals YES | 19 | 0.228 | 0.217 | +0.028 | +0.017 | $1.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Ryan McLeod: 1+ goals YES | 15 | 0.188 | 0.173 | +0.029 | +0.015 | $1.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Alexandre Carrier: 1+ goals YES** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT17BUFMTL-BUFNOSTLUND86-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: MTL offense suppressed (<= 2 goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFNOSTLUND86-1|yes; why: higher confidence-adjusted growth (8.15 vs 3.81 bp); relationships: KXNHLGOAL-26OCT17BUFMTL-MTLACARRIER45-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT17BUFMTL-BUFNOSTLUND86-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: BUF offense suppressed (<= 2 goals)
- **Noah Ostlund: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes has the higher standalone adjusted growth (8.15 vs 3.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT17BUFMTL-MTLACARRIER45-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: BUF offense suppressed (<= 2 goals)
- **Ryan McLeod: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes has the higher standalone adjusted growth (8.15 vs 3.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT17BUFMTL-MTLACARRIER45-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17BUFMTL-BUFNOSTLUND86-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.3845): highest fidelity KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3662): highest fidelity KXNHLAST-26OCT17BUFMTL-MTLCKREIDER22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3882): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17BUFMTL-MTLACARRIER45-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3662, phi -0.1)
- KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3882, phi -0.24)
- KXNHLGOAL-26OCT17BUFMTL-BUFNOSTLUND86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3882, phi -0.199)
- KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3882, phi -0.192)

portfolios: A EV +1.66 (adj +0.65) on $12.71, P(profit) 0.5478, adj growth 6.0 bp · B EV +1.58 (adj +0.96) on $7.46, P(profit) 0.583, adj growth 9.1 bp · C EV +1.86 (adj +1.05) on $11.42, P(profit) 0.3294, adj growth 9.7 bp · R EV +0.18 (adj +0.11) on $1.00, P(profit) 0.2849, adj growth 4.1 bp

## SJS @ DET  ·  10000 joint draws  ·  424 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_SJS_win | p_overtime | goals | shots DET/SJS | DET/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.55 | 0.45 | 0.00 | 6.05 | 27.8/27.5 | 24.1/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.48 | 5.93 | 27.7/27.3 | 24.1/24.5 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.104 | 0.60 | 0.40 | 0.00 | 6.01 | 32.8/21.8 | 18.8/28.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.46 | 0.45 | 5.88 | 33.1/21.9 | 18.7/29.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.52 | 0.48 | 0.00 | 9.28 | 29.3/29.0 | 23.2/23.3 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.064 | 0.59 | 0.41 | 0.00 | 9.17 | 34.8/23.0 | 18.1/27.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Collin Graf: 1+ goals YES | 13 | 0.166 | 0.155 | +0.028 | +0.018 | $1.78 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Luca Cagnoni: 1+ goals NO | 91 | 0.939 | 0.929 | +0.024 | +0.014 | $7.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Kiefer Sherwood: 1+ goals YES | 17 | 0.204 | 0.193 | +0.024 | +0.013 | $1.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 71 | 0.810 | 0.735 | +0.086 | +0.011 | $5.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes; why: higher confidence-adjusted growth (5.63 vs 2.48 bp); relationships: KXNHLGOAL-26OCT17SJDET-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.048); failure: SJS offense suppressed (<= 2 goals)
- **Luca Cagnoni: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.061); failure: SJS offense succeeds (4+ goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17SJDET-DET3|no; why: higher confidence-adjusted growth (2.48 vs 1.06 bp); despite a smaller raw edge (+0.024 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT17SJDET-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.15); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17SJDET-SJMMARCHMENT27-1|no; why: KXNHLAST-26OCT17SJDET-SJMMARCHMENT27-1|no has the higher standalone adjusted growth (1.36 vs 1.31 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.010); relationships: KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLGOAL-26OCT17SJDET-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi 0.061); KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.15); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.3587): highest fidelity KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.419): highest fidelity KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17SJDET-SJMMARCHMENT27-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.419, phi -0.196)
- KXNHLGOAL-26OCT17SJDET-SJLCAGNONI42-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3587, phi -0.107)
- KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.419, phi -0.227)
- KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.5 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3587, phi -0.194)

portfolios: A EV +1.20 (adj +0.36) on $12.71, P(profit) 0.5868, adj growth 3.5 bp · B EV +1.41 (adj +0.53) on $16.20, P(profit) 0.3256, adj growth 5.1 bp · C EV +0.91 (adj +0.41) on $19.04, P(profit) 0.7923, adj growth 3.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ PHI  ·  10000 joint draws  ·  442 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.421 / away 0.579

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_OTT_win | p_overtime | goals | shots PHI/OTT | PHI/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.49 | 0.51 | 0.00 | 5.99 | 25.6/26.1 | 22.5/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.47 | 5.93 | 25.6/26.2 | 22.9/22.3 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.099 | 0.40 | 0.60 | 0.00 | 5.95 | 20.5/31.4 | 27.2/17.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.45 | 0.55 | 0.49 | 5.8 | 20.7/31.5 | 28.1/17.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.066 | 0.50 | 0.50 | 0.00 | 3.41 | 24.5/25.0 | 23.0/22.7 | even strength |
| OTT shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.49 | 0.51 | 0.49 | 2.76 | 19.0/29.7 | 28.2/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Porter Martone: 1+ goals NO | 78 | 0.822 | 0.809 | +0.030 | +0.017 | $7.33 | FUNDED_RESEARCH | $2 | PHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 18 | 0.217 | 0.206 | +0.026 | +0.016 | $1.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Tim Stutzle: 1+ assists NO | 50 | 0.626 | 0.534 | +0.108 | +0.017 | $3.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Ottawa over 3.5 goals scored NO | 59 | 0.651 | 0.618 | +0.044 | +0.011 | $1.74 | FUNDED_RESEARCH | $1 | OTT:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-PHIDJIRICEK55-1|no; why: higher confidence-adjusted growth (4.00 vs 0.00 bp); despite a smaller raw edge (+0.030 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0006 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17OTTPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no: MOSTLY_INDEPENDENT (phi 0.003); failure: PHI offense succeeds (4+ goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17OTTPHI-PHIOTIPPETT74-1|yes; why: higher confidence-adjusted growth (3.58 vs 0.66 bp); alternative not eligible: confidence-adjusted EV +0.0074 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no: MOSTLY_INDEPENDENT (phi -0.007); failure: PHI offense suppressed (<= 2 goals)
- **Tim Stutzle: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTCYAKEMCHUK26-1|no; why: KXNHLAST-26OCT17OTTPHI-OTTCYAKEMCHUK26-1|no has the higher standalone adjusted growth (2.71 vs 2.49 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.078); relationships: KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17OTTPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no: REINFORCING (phi 0.269); failure: OTT offense succeeds (4+ goals)
- **Ottawa over 3.5 goals scored NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTCYAKEMCHUK26-1|no; why: Broad expression KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTABURAKOVSKY95-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT17OTTPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: REINFORCING (phi 0.269); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:OFFENSE_4PLUS (p 0.3027): highest fidelity KXNHLGOAL-26OCT17OTTPHI-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17OTTPHI-PHICDVORAK22-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.4466): highest fidelity KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no — Broad expression KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTABURAKOVSKY95-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis PHI:SUPPRESSED (p 0.4749): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3027, phi -0.183)
- KXNHLGOAL-26OCT17OTTPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4749, phi -0.229)
- KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.1 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3398, phi -0.275)
- KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3398, phi -0.98)
- override: Broad expression KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTABURAKOVSKY95-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.55 (adj +0.30) on $12.71, P(profit) 0.6716, adj growth 2.8 bp · B EV +1.28 (adj +0.44) on $13.82, P(profit) 0.6049, adj growth 4.2 bp · C EV +0.99 (adj +0.39) on $10.83, P(profit) 0.827, adj growth 3.6 bp · R EV +0.15 (adj +0.06) on $3.00, P(profit) 0.5361, adj growth 2.4 bp

## NYR @ CBJ  ·  10000 joint draws  ·  416 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.551 / away 0.449

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_NYR_win | p_overtime | goals | shots CBJ/NYR | CBJ/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CBJ shot control · normal event (5-7) · decided (2+) | 0.115 | 0.63 | 0.37 | 0.00 | 6.02 | 32.2/20.9 | 18.1/27.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.60 | 0.40 | 0.00 | 6.02 | 26.7/26.2 | 22.9/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.44 | 5.87 | 26.8/26.5 | 23.3/23.5 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.52 | 0.48 | 0.51 | 5.92 | 32.3/21.2 | 18.0/29.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.62 | 0.38 | 0.00 | 9.2 | 28.2/27.7 | 22.3/21.4 | even strength |
| CBJ shot control · high event (8+) · decided (2+) | 0.068 | 0.68 | 0.32 | 0.00 | 9.17 | 33.7/22.2 | 17.6/26.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pavel Dorofeyev: 1+ assists NO | 72 | 0.797 | 0.751 | +0.063 | +0.017 | $6.63 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Charlie Coyle: 1+ goals YES | 24 | 0.275 | 0.265 | +0.022 | +0.012 | $1.38 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17NYRCBJ-NYR3|no; why: higher confidence-adjusted growth (3.29 vs 0.25 bp); alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17NYRCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: NYR offense succeeds (4+ goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (1.62 vs 1.23 bp); despite a smaller raw edge (+0.022 vs +0.022/contract); alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts CBJ shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYR:SUPPRESSED (p 0.4669): highest fidelity KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.4073): highest fidelity KXNHLGOAL-26OCT17NYRCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17NYRCBJ-CBJCCOYLE3-1|yes (same contract)
- KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.312, phi -0.216)
- KXNHLGOAL-26OCT17NYRCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3739, phi -0.222)

portfolios: A EV +0.60 (adj +0.21) on $6.93, P(profit) 0.2745, adj growth 2.0 bp · B EV +0.69 (adj +0.22) on $8.02, P(profit) 0.7974, adj growth 2.1 bp · C EV +1.00 (adj +0.32) on $11.63, P(profit) 0.7974, adj growth 3.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ CHI  ·  10000 joint draws  ·  396 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.344 / away 0.656

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_DAL_win | p_overtime | goals | shots CHI/DAL | CHI/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.45 | 0.55 | 0.00 | 5.99 | 25.8/26.4 | 22.6/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.53 | 0.47 | 0.47 | 5.95 | 25.7/26.0 | 22.7/22.3 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.106 | 0.41 | 0.59 | 0.00 | 5.98 | 20.2/31.2 | 27.2/17.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.46 | 0.54 | 0.47 | 5.86 | 20.2/30.8 | 27.4/17.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.47 | 0.53 | 0.00 | 9.27 | 27.0/27.6 | 21.3/21.3 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.067 | 0.41 | 0.59 | 0.00 | 9.18 | 21.8/32.8 | 25.6/16.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Chicago wins by over 1.5 goals YES | 17 | 0.250 | 0.208 | +0.070 | +0.028 | $2.36 | FUNDED_RESEARCH | $1 | CHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 25 | 0.304 | 0.288 | +0.041 | +0.025 | $2.68 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
| Anton Frondell: 1+ goals YES | 20 | 0.248 | 0.233 | +0.037 | +0.021 | $2.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ assists NO | 58 | 0.657 | 0.611 | +0.060 | +0.014 | $5.72 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
- **Chicago wins by over 1.5 goals YES** — thesis: CHI wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes; why: higher confidence-adjusted growth (11.28 vs 7.12 bp); relationships: KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: REINFORCING (phi 0.207); KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.15); KXNHLAST-26OCT17DALCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.193); failure: DAL wins (incl. OT/SO)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes has the higher standalone adjusted growth (11.28 vs 7.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.207); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes: REINFORCING (phi 0.207); KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26OCT17DALCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.138); failure: CHI offense suppressed (<= 2 goals)
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes has the higher standalone adjusted growth (11.28 vs 5.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.150); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes: MOSTLY_INDEPENDENT (phi 0.15); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26OCT17DALCHI-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.073); failure: CHI offense suppressed (<= 2 goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17DALCHI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (1.78 vs 1.74 bp); relationships: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes: INTENTIONAL_DIVERSIFIER (phi -0.193); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.138); KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.073); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:WINS_BY_2PLUS (p 0.2503): highest fidelity KXNHLSPREAD-26OCT17DALCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3499): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.384): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-DAL4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT17DALCHI-CHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.524, phi -0.606)
- KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4279, phi -0.275)
- KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4279, phi -0.24)
- KXNHLAST-26OCT17DALCHI-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3499, phi -0.261)

portfolios: A EV +2.48 (adj +0.55) on $12.71, P(profit) 0.5969, adj growth 5.0 bp · B EV +2.29 (adj +0.96) on $12.84, P(profit) 0.4647, adj growth 9.2 bp · C EV +2.39 (adj +0.83) on $11.40, P(profit) 0.7827, adj growth 7.7 bp · R EV +0.39 (adj +0.15) on $1.00, P(profit) 0.2503, adj growth 5.7 bp

## STL @ NSH  ·  10000 joint draws  ·  420 bet sides mapped, 1 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.491 / away 0.508

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_STL_win | p_overtime | goals | shots NSH/STL | NSH/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.51 | 0.49 | 0.00 | 6.03 | 27.3/27.5 | 23.9/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.48 | 5.89 | 27.4/27.6 | 24.4/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.51 | 0.49 | 0.00 | 9.37 | 29.0/29.0 | 23.0/22.8 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.069 | 0.56 | 0.44 | 0.00 | 5.96 | 32.4/22.0 | 19.0/28.2 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.066 | 0.43 | 0.57 | 0.00 | 5.99 | 21.6/31.9 | 27.6/18.6 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.53 | 0.47 | 0.48 | 5.97 | 32.6/22.2 | 18.9/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 25 | 0.291 | 0.278 | +0.028 | +0.015 | $1.84 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT17STLNSH-9|yes; why: higher confidence-adjusted growth (2.62 vs 0.09 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.905 vs 0.369); alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.3985): highest fidelity KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes (same contract)
- KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3789, phi -0.258)

portfolios: A EV +0.26 (adj +0.14) on $2.42, P(profit) 0.2912, adj growth 1.3 bp · B EV +0.20 (adj +0.11) on $1.84, P(profit) 0.2912, adj growth 1.0 bp · C EV +0.29 (adj +0.16) on $2.67, P(profit) 0.2912, adj growth 1.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ LAK  ·  10000 joint draws  ·  388 bet sides mapped, 3 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.553 / away 0.447

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BOS_win | p_overtime | goals | shots LAK/BOS | LAK/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.54 | 0.46 | 0.00 | 5.97 | 27.9/27.4 | 24.1/24.2 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.110 | 0.61 | 0.39 | 0.00 | 5.93 | 33.2/21.8 | 18.9/29.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.47 | 5.8 | 28.0/27.5 | 24.3/24.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.54 | 0.46 | 0.47 | 5.83 | 33.3/22.0 | 18.7/30.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.52 | 0.48 | 0.00 | 9.2 | 29.7/29.1 | 23.3/23.2 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.061 | 0.63 | 0.37 | 0.00 | 9.18 | 34.7/23.3 | 18.4/27.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Borgen: 1+ goals YES | 3 | 0.053 | 0.046 | +0.021 | +0.014 | $1.11 | FUNDED_RESEARCH | $1 | BOS:WINS_BY_2PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 71 | 0.788 | 0.741 | +0.063 | +0.017 | $7.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLPTS-26OCT17BOSLA-BOSFMINTEN93-1|yes; why: higher confidence-adjusted growth (13.11 vs 0.00 bp); despite a smaller raw edge (+0.021 vs +0.074/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); failure: BOS offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (3.18 vs 0.09 bp); alternative not eligible: confidence-adjusted EV +0.0032 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17BOSLA-BOSWBORGEN17-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BOS:SUPPRESSED (p 0.4548): highest fidelity KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no (same contract)
- thesis BOS:WINS_BY_2PLUS (p 0.2393): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis BOS:OFFENSE_4PLUS (p 0.3324): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17BOSLA-BOSWBORGEN17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4548, phi -0.123)
- KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3324, phi -0.223)

portfolios: A EV +1.63 (adj +0.86) on $7.93, P(profit) 0.1709, adj growth 8.0 bp · B EV +1.35 (adj +0.65) on $8.21, P(profit) 0.8045, adj growth 6.2 bp · C EV +0.81 (adj +0.22) on $9.25, P(profit) 0.7878, adj growth 2.0 bp · R EV +0.65 (adj +0.44) on $1.00, P(profit) 0.053, adj growth 13.8 bp

## EDM @ UTA  ·  10000 joint draws  ·  408 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.555 / away 0.445

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_EDM_win | p_overtime | goals | shots UTA/EDM | UTA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.54 | 0.46 | 0.00 | 6.1 | 27.5/27.6 | 24.3/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.121 | 0.53 | 0.47 | 0.00 | 9.53 | 29.2/29.1 | 23.0/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.49 | 0.51 | 0.47 | 6.02 | 27.7/27.7 | 24.3/24.2 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.070 | 0.60 | 0.40 | 0.00 | 6.0 | 32.5/21.8 | 18.8/28.2 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.45 | 6.05 | 32.7/22.0 | 18.8/29.3 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.067 | 0.62 | 0.38 | 0.00 | 9.5 | 34.4/23.4 | 18.3/27.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 15 | 0.209 | 0.192 | +0.050 | +0.033 | $3.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Mathieu Joseph: 1+ goals YES | 7 | 0.103 | 0.093 | +0.029 | +0.018 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 29 | 0.355 | 0.334 | +0.051 | +0.030 | $3.69 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| Evan Bouchard: 1+ goals YES | 18 | 0.228 | 0.215 | +0.038 | +0.024 | $2.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-2|yes; why: higher confidence-adjusted growth (17.29 vs 16.43 bp); despite a smaller raw edge (+0.050 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.858 vs 0.732); relationships: KXNHLGOAL-26OCT17EDMUTA-EDMMJOSEPH21-1|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT17EDMUTA-EDMEBOUCHARD2-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: EDM offense suppressed (<= 2 goals)
- **Mathieu Joseph: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (17.29 vs 10.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.025); they share one thesis budget; relationships: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT17EDMUTA-EDMEBOUCHARD2-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (17.29 vs 9.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT17EDMUTA-EDMMJOSEPH21-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT17EDMUTA-EDMEBOUCHARD2-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: EDM offense suppressed (<= 2 goals)
- **Evan Bouchard: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes; why: Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMEBOUCHARD2-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-2|yes because adjusted EV is 0.1 pts higher while thesis capture is 0.33 vs 0.23 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT17EDMUTA-EDMMJOSEPH21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4307): highest fidelity KXNHLPTS-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes — Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMEBOUCHARD2-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-2|yes because adjusted EV is 0.1 pts higher while thesis capture is 0.33 vs 0.23 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis EDM:SUPPRESSED (p 0.3487): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-1|no (same contract)
- thesis UTA:SUPPRESSED (p 0.3202): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3487, phi -0.206)
- KXNHLGOAL-26OCT17EDMUTA-EDMMJOSEPH21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3487, phi -0.133)
- KXNHLGOAL-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3487, phi -0.272)
- KXNHLGOAL-26OCT17EDMUTA-EDMEBOUCHARD2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3487, phi -0.198)
- override: Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMEBOUCHARD2-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-2|yes because adjusted EV is 0.1 pts higher while thesis capture is 0.33 vs 0.23 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.96 (adj +0.89) on $12.71, P(profit) 0.5556, adj growth 7.8 bp · B EV +2.71 (adj +1.71) on $10.95, P(profit) 0.644, adj growth 16.2 bp · C EV +2.01 (adj +1.13) on $8.24, P(profit) 0.5688, adj growth 10.4 bp · R EV +0.17 (adj +0.10) on $1.00, P(profit) 0.3555, adj growth 3.7 bp

## PIT @ VGK  ·  10000 joint draws  ·  422 bet sides mapped, 8 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.639 / away 0.361

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_PIT_win | p_overtime | goals | shots VGK/PIT | VGK/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.70 | 0.30 | 0.00 | 6.09 | 27.6/27.4 | 24.6/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.47 | 5.99 | 27.6/27.5 | 24.2/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.71 | 0.29 | 0.00 | 9.5 | 28.8/28.7 | 23.7/21.1 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.093 | 0.75 | 0.25 | 0.00 | 6.02 | 32.2/21.4 | 19.1/27.3 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.071 | 0.77 | 0.23 | 0.00 | 9.36 | 34.0/23.0 | 18.9/25.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.57 | 0.43 | 0.49 | 5.95 | 32.7/21.8 | 18.7/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Bryan Rust: 1+ goals YES | 23 | 0.284 | 0.269 | +0.041 | +0.027 | $3.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 10 | 0.128 | 0.119 | +0.021 | +0.013 | $1.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 69 | 0.734 | 0.718 | +0.029 | +0.013 | $4.21 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17PITVGK-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (8.42 vs 3.89 bp); relationships: KXNHLGOAL-26OCT17PITVGK-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes has the higher standalone adjusted growth (8.42 vs 3.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.021); they share one thesis budget; relationships: KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: PIT offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17PITVGK-VGKJEICHEL9-1|no; why: Player prop expression KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no selected over player prop KXNHLAST-26OCT17PITVGK-VGKTCONNELLY24-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.88 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17PITVGK-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.3095): highest fidelity KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.2848): highest fidelity KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.5106): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4763, phi -0.276)
- KXNHLGOAL-26OCT17PITVGK-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4763, phi -0.189)
- KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5106, phi -0.217)
- override: Player prop expression KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no selected over player prop KXNHLAST-26OCT17PITVGK-VGKTCONNELLY24-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.88 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.00 (adj +0.48) on $12.71, P(profit) 0.6101, adj growth 4.6 bp · B EV +0.94 (adj +0.56) on $8.48, P(profit) 0.372, adj growth 5.4 bp · C EV +1.03 (adj +0.61) on $10.68, P(profit) 0.2838, adj growth 5.7 bp · R EV +0.08 (adj +0.04) on $2.00, P(profit) 0.7341, adj growth 1.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
