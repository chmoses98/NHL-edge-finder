# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T13:59:35Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +24.95 | +6.03 | +24.73 | 0.756 | -19.98 | -32.68 | 54.39 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +24.07 | +9.59 | +22.84 | 0.741 | -22.13 | -33.09 | 89.33 |
| C best expression per thesis | 150.00 | +28.64 | +10.79 | +27.09 | 0.707 | -33.37 | -48.62 | 95.93 |
| R FUNDED research stakes | 24.00 | +3.38 | +1.34 | +2.88 | 0.663 | -6.10 | -8.59 | 0.00 |

## NJD @ WSH  ·  10000 joint draws  ·  424 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_NJD_win | p_overtime | goals | shots WSH/NJD | WSH/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.60 | 0.40 | 0.00 | 6.0 | 27.7/28.2 | 25.2/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.48 | 5.89 | 27.8/28.0 | 24.7/24.6 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.097 | 0.53 | 0.47 | 0.00 | 5.99 | 22.1/33.5 | 30.0/18.5 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.45 | 0.55 | 0.50 | 5.84 | 22.2/33.7 | 30.4/19.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.60 | 0.40 | 0.00 | 9.33 | 29.2/29.6 | 23.9/22.7 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.060 | 0.55 | 0.45 | 0.00 | 9.09 | 23.4/35.3 | 29.5/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 18 | 0.243 | 0.225 | +0.053 | +0.034 | $5.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 17 | 0.203 | 0.194 | +0.024 | +0.014 | $2.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 75 | 0.788 | 0.777 | +0.025 | +0.014 | $7.61 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ assists NO | 53 | 0.651 | 0.563 | +0.104 | +0.015 | $4.20 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes; why: higher confidence-adjusted growth (16.48 vs 2.85 bp); relationships: KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (16.48 vs 2.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.022); they share one thesis budget; relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: WSH offense suppressed (<= 2 goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no; why: Player prop expression KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.89 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.077); failure: NJD offense succeeds (4+ goals)
- **Jack Hughes: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no; why: KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no has the higher standalone adjusted growth (2.75 vs 2.08 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.073); relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.077); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4113): highest fidelity KXNHLAST-26OCT17NJWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4492): highest fidelity KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no — Player prop expression KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.89 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3698, phi -0.226)
- KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3698, phi -0.2)
- KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.329, phi -0.246)
- KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.6 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.329, phi -0.269)
- override: Player prop expression KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.89 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.34 (adj +0.48) on $16.41, P(profit) 0.5667, adj growth 4.4 bp · B EV +2.73 (adj +1.35) on $18.99, P(profit) 0.3779, adj growth 12.5 bp · C EV +3.47 (adj +1.88) on $20.27, P(profit) 0.2429, adj growth 16.5 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.7884, adj growth 1.4 bp

## CAR @ WPG  ·  10000 joint draws  ·  396 bet sides mapped, 14 +EV candidates, 4 on card


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
| Winnipeg wins by over 1.5 goals YES | 18 | 0.260 | 0.218 | +0.070 | +0.027 | $2.94 | FUNDED_RESEARCH | $1 | WPG:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mark Scheifele: 1+ goals YES | 30 | 0.352 | 0.334 | +0.037 | +0.019 | $2.35 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 71 | 0.809 | 0.742 | +0.085 | +0.017 | $5.09 | FUNDED_RESEARCH | $2 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Alex Iafallo: 1+ goals YES | 14 | 0.175 | 0.161 | +0.027 | +0.013 | $1.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Winnipeg wins by over 1.5 goals YES** — thesis: WPG wins by 2+; alternative: KXNHLSPREAD-26OCT17CARWPG-WPG3|yes; why: higher confidence-adjusted growth (10.42 vs 6.00 bp); relationships: KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: REINFORCING (phi 0.207); KXNHLSPREAD-26OCT17CARWPG-CAR3|no: REINFORCING (phi 0.288); KXNHLGOAL-26OCT17CARWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.142); failure: CAR wins (incl. OT/SO)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes has the higher standalone adjusted growth (10.42 vs 3.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.207); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: REINFORCING (phi 0.207); KXNHLSPREAD-26OCT17CARWPG-CAR3|no: REINFORCING (phi 0.154); KXNHLGOAL-26OCT17CARWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: WPG offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes; why: Broad expression KXNHLSPREAD-26OCT17CARWPG-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: REINFORCING (phi 0.288); KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: REINFORCING (phi 0.154); KXNHLGOAL-26OCT17CARWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.102); failure: CAR wins by 2+
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes has the higher standalone adjusted growth (10.42 vs 2.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.142); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: MOSTLY_INDEPENDENT (phi 0.142); KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT17CARWPG-CAR3|no: MOSTLY_INDEPENDENT (phi 0.102); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:WINS_BY_2PLUS (p 0.2602): highest fidelity KXNHLSPREAD-26OCT17CARWPG-WPG2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-WPG2|yes (same contract)
- thesis WPG:WINS (p 0.4733): highest fidelity KXNHLSPREAD-26OCT17CARWPG-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-WPG2|yes — Broad expression KXNHLSPREAD-26OCT17CARWPG-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis WPG:OFFENSE_4PLUS (p 0.3734): highest fidelity KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-WPG2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5267, phi -0.626)
- KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4046, phi -0.282)
- KXNHLSPREAD-26OCT17CARWPG-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.4 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3022, phi -0.737)
- KXNHLGOAL-26OCT17CARWPG-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4046, phi -0.187)
- override: Broad expression KXNHLSPREAD-26OCT17CARWPG-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.80 (adj +0.93) on $16.41, P(profit) 0.4733, adj growth 7.9 bp · B EV +2.19 (adj +0.80) on $11.74, P(profit) 0.5043, adj growth 7.5 bp · C EV +2.37 (adj +0.93) on $6.46, P(profit) 0.2602, adj growth 8.2 bp · R EV +0.72 (adj +0.25) on $4.00, P(profit) 0.4388, adj growth 9.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17CARWPG-WPG|yes == KXNHLGAME-26OCT17CARWPG-CAR|no

## VAN @ TBL  ·  10000 joint draws  ·  382 bet sides mapped, 23 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_VAN_win | p_overtime | goals | shots TBL/VAN | TBL/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.154 | 0.72 | 0.28 | 0.00 | 5.99 | 33.3/20.8 | 18.2/28.6 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.126 | 0.56 | 0.44 | 0.48 | 5.91 | 33.4/21.2 | 18.1/29.8 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.106 | 0.72 | 0.28 | 0.00 | 9.32 | 34.8/22.1 | 17.8/26.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.69 | 0.31 | 0.00 | 6.03 | 27.3/26.4 | 23.4/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.51 | 0.49 | 0.45 | 5.91 | 27.5/26.8 | 23.5/24.1 | even strength |
| TBL shot control · low event (<=4) · decided (2+) | 0.070 | 0.74 | 0.26 | 0.00 | 3.44 | 32.1/19.8 | 18.6/29.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 2.5 goals NO | 54 | 0.729 | 0.603 | +0.171 | +0.045 | $10.55 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Filip Chytil: 1+ goals YES | 15 | 0.209 | 0.192 | +0.050 | +0.033 | $4.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 11 | 0.155 | 0.139 | +0.038 | +0.022 | $2.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Jake Guentzel: 1+ goals NO | 60 | 0.663 | 0.644 | +0.046 | +0.028 | $7.48 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB2|no; why: higher confidence-adjusted growth (18.27 vs 15.44 bp); wins across more scripts (relative breadth 1.013 vs 0.855); relationships: KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26OCT17VANTB-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.111); KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no: REINFORCING (phi 0.158); failure: TBL wins by 2+
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17VANTB-VAN2|yes; why: KXNHLSPREAD-26OCT17VANTB-VAN2|yes has the higher standalone adjusted growth (18.77 vs 17.29 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.174); relationships: KXNHLSPREAD-26OCT17VANTB-TB3|no: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26OCT17VANTB-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: VAN offense suppressed (<= 2 goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17VANTB-VAN2|yes; why: KXNHLSPREAD-26OCT17VANTB-VAN2|yes has the higher standalone adjusted growth (18.77 vs 9.91 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.122); relationships: KXNHLSPREAD-26OCT17VANTB-TB3|no: MOSTLY_INDEPENDENT (phi 0.111); KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense suppressed (<= 2 goals)
- **Jake Guentzel: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17VANTB-VAN2|yes; why: Player prop expression KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no selected over player prop KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26OCT17VANTB-TB3|no: REINFORCING (phi 0.158); KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT17VANTB-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.15, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, TBL shot control · high event (8+) · decided (2+) 0.11.
- thesis VAN:WINS_BY_2PLUS (p 0.1755): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB3|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.2886): highest fidelity KXNHLTEAMTOTAL-26OCT17VANTB-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.3108): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB3|no (same contract)
- KXNHLSPREAD-26OCT17VANTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 19.4 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4028, phi -0.743)
- KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4984, phi -0.261)
- KXNHLGOAL-26OCT17VANTB-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4984, phi -0.189)
- KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.475, phi -0.241)
- override: Player prop expression KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no selected over player prop KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.49 (adj +1.10) on $16.41, P(profit) 0.7897, adj growth 10.3 bp · B EV +5.92 (adj +2.52) on $24.68, P(profit) 0.6427, adj growth 23.5 bp · C EV +8.23 (adj +2.60) on $22.05, P(profit) 0.7285, adj growth 23.3 bp · R EV +1.07 (adj +0.33) on $5.00, P(profit) 0.7285, adj growth 12.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17VANTB-TB|no == KXNHLGAME-26OCT17VANTB-VAN|yes

## SEA @ FLA  ·  10000 joint draws  ·  416 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_SEA_win | p_overtime | goals | shots FLA/SEA | FLA/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.53 | 0.47 | 0.00 | 5.99 | 27.5/27.0 | 23.6/23.9 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.112 | 0.58 | 0.42 | 0.00 | 6.03 | 33.1/21.5 | 18.4/29.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.50 | 0.50 | 0.47 | 5.98 | 27.5/27.0 | 23.6/24.1 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.55 | 0.45 | 0.47 | 5.91 | 33.0/21.7 | 18.6/29.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.51 | 0.49 | 0.00 | 9.2 | 29.2/28.5 | 22.7/23.0 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.071 | 0.60 | 0.40 | 0.00 | 9.24 | 34.4/22.9 | 18.1/27.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 64 | 0.714 | 0.693 | +0.057 | +0.036 | $10.55 | FUNDED_RESEARCH | $3 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 10 | 0.141 | 0.129 | +0.035 | +0.022 | $2.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 11 | 0.154 | 0.140 | +0.037 | +0.023 | $2.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 72 | 0.802 | 0.758 | +0.068 | +0.024 | $8.27 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no; why: higher confidence-adjusted growth (12.99 vs 7.31 bp); despite a smaller raw edge (+0.057 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.02 vs 0.915); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: REINFORCING (phi 0.18); failure: FLA offense succeeds (4+ goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes; why: higher confidence-adjusted growth (11.08 vs 10.64 bp); despite a smaller raw edge (+0.035 vs +0.037/contract); relationships: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.091); failure: SEA offense suppressed (<= 2 goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no; why: higher confidence-adjusted growth (10.64 vs 7.31 bp); despite a smaller raw edge (+0.037 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.104); failure: SEA offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no has the higher standalone adjusted growth (12.99 vs 6.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.180); they share one thesis budget; relationships: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: REINFORCING (phi 0.18); KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.091); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.104); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis FLA:SUPPRESSED (p 0.3722): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.469): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.3612): highest fidelity KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4053, phi -0.249)
- KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4173, phi -0.167)
- KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4173, phi -0.189)
- KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3053, phi -0.75)

portfolios: A EV +1.83 (adj +0.63) on $16.41, P(profit) 0.6967, adj growth 6.1 bp · B EV +3.50 (adj +1.98) on $24.41, P(profit) 0.6875, adj growth 18.5 bp · C EV +4.53 (adj +2.43) on $34.08, P(profit) 0.5959, adj growth 21.7 bp · R EV +0.54 (adj +0.27) on $6.00, P(profit) 0.6046, adj growth 10.0 bp

## NYI @ TOR  ·  10000 joint draws  ·  426 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYI_win | p_overtime | goals | shots TOR/NYI | TOR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.53 | 0.47 | 0.00 | 6.0 | 27.7/28.4 | 25.0/24.0 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.112 | 0.49 | 0.51 | 0.00 | 6.0 | 22.1/34.1 | 30.3/18.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.52 | 0.48 | 0.48 | 5.91 | 28.1/28.6 | 25.3/24.6 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.47 | 0.53 | 0.46 | 5.9 | 22.4/34.5 | 31.2/19.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.55 | 0.45 | 0.00 | 9.25 | 29.6/30.2 | 24.4/23.0 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.073 | 0.46 | 0.54 | 0.00 | 9.15 | 23.4/35.3 | 28.9/18.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Easton Cowan: 1+ assists YES | 26 | 0.328 | 0.286 | +0.054 | +0.013 | $2.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
- **Easton Cowan: 1+ assists YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT17NYITOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (1.79 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, NYI shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3983): highest fidelity KXNHLAST-26OCT17NYITOR-TORECOWAN53-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT17NYITOR-TORECOWAN53-1|yes (same contract)
- KXNHLAST-26OCT17NYITOR-TORECOWAN53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3785, phi -0.25)

portfolios: A EV +1.21 (adj +0.29) on $6.10, P(profit) 0.3275, adj growth 2.3 bp · B EV +0.42 (adj +0.10) on $2.14, P(profit) 0.3275, adj growth 0.9 bp · C EV +0.71 (adj +0.17) on $3.61, P(profit) 0.3275, adj growth 1.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ MTL  ·  10000 joint draws  ·  406 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_BUF_win | p_overtime | goals | shots MTL/BUF | MTL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.54 | 0.46 | 0.00 | 6.02 | 27.4/27.7 | 24.4/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.50 | 0.50 | 0.45 | 5.99 | 27.2/27.5 | 24.1/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.57 | 0.43 | 0.00 | 9.38 | 29.0/29.2 | 23.5/22.4 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.090 | 0.47 | 0.53 | 0.00 | 6.01 | 21.6/32.7 | 28.9/18.4 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.46 | 0.54 | 0.48 | 5.91 | 21.6/32.7 | 29.3/18.5 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.059 | 0.47 | 0.53 | 0.00 | 9.21 | 23.3/34.6 | 27.7/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Zach Benson: 1+ goals YES | 23 | 0.285 | 0.269 | +0.043 | +0.026 | $4.41 | FUNDED_RESEARCH | $2 | BUF:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Noah Ostlund: 1+ goals YES | 19 | 0.228 | 0.215 | +0.027 | +0.014 | $1.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ assists YES | 34 | 0.412 | 0.369 | +0.057 | +0.013 | $1.42 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_MIXED | D |
| Jack Quinn: 1+ goals YES | 27 | 0.306 | 0.295 | +0.022 | +0.012 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFNOSTLUND86-1|yes; why: higher confidence-adjusted growth (8.29 vs 2.59 bp); relationships: KXNHLGOAL-26OCT17BUFMTL-BUFNOSTLUND86-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT17BUFMTL-BUFJQUINN22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: BUF offense suppressed (<= 2 goals)
- **Noah Ostlund: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes has the higher standalone adjusted growth (8.29 vs 2.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes: REINFORCING (phi 0.213); KXNHLGOAL-26OCT17BUFMTL-BUFJQUINN22-1|yes: MOSTLY_INDEPENDENT (phi 0.025); failure: BUF offense suppressed (<= 2 goals)
- **Zach Benson: 1+ assists YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes has the higher standalone adjusted growth (8.29 vs 1.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT17BUFMTL-BUFNOSTLUND86-1|yes: REINFORCING (phi 0.213); KXNHLGOAL-26OCT17BUFMTL-BUFJQUINN22-1|yes: REINFORCING (phi 0.244); failure: BUF offense suppressed (<= 2 goals)
- **Jack Quinn: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes has the higher standalone adjusted growth (8.29 vs 1.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT17BUFMTL-BUFNOSTLUND86-1|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes: REINFORCING (phi 0.244); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.3924): highest fidelity KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3902, phi -0.247)
- KXNHLGOAL-26OCT17BUFMTL-BUFNOSTLUND86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3902, phi -0.205)
- KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3902, phi -0.298)
- KXNHLGOAL-26OCT17BUFMTL-BUFJQUINN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3902, phi -0.247)

portfolios: A EV +2.42 (adj +1.03) on $16.41, P(profit) 0.5957, adj growth 9.1 bp · B EV +1.40 (adj +0.74) on $9.52, P(profit) 0.5392, adj growth 6.9 bp · C EV +1.32 (adj +0.82) on $7.46, P(profit) 0.2852, adj growth 7.2 bp · R EV +0.35 (adj +0.22) on $2.00, P(profit) 0.2852, adj growth 7.6 bp

## SJS @ DET  ·  10000 joint draws  ·  416 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_SJS_win | p_overtime | goals | shots DET/SJS | DET/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.51 | 0.49 | 0.00 | 5.99 | 27.8/27.5 | 23.9/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.49 | 5.94 | 27.6/27.4 | 24.0/24.2 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.104 | 0.54 | 0.46 | 0.00 | 5.98 | 32.8/21.8 | 18.5/28.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.51 | 0.49 | 0.00 | 9.26 | 29.3/29.0 | 23.0/23.3 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.54 | 0.46 | 0.45 | 5.9 | 33.4/21.7 | 18.5/29.9 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.063 | 0.60 | 0.40 | 0.00 | 9.27 | 34.7/23.4 | 18.3/27.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 1+ assists NO | 69 | 0.814 | 0.724 | +0.109 | +0.019 | $10.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17SJDET-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (3.69 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.4043): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.9 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3732, phi -0.203)

portfolios: A EV +1.01 (adj +0.17) on $6.56, P(profit) 0.814, adj growth 1.7 bp · B EV +1.63 (adj +0.28) on $10.55, P(profit) 0.814, adj growth 2.6 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ PHI  ·  10000 joint draws  ·  396 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_OTT_win | p_overtime | goals | shots PHI/OTT | PHI/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.50 | 0.50 | 0.00 | 5.94 | 25.6/26.1 | 22.7/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.50 | 0.50 | 0.47 | 5.87 | 25.8/26.2 | 23.0/22.4 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.101 | 0.42 | 0.58 | 0.00 | 5.97 | 20.2/31.3 | 27.5/17.2 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.45 | 0.55 | 0.47 | 5.82 | 20.4/31.2 | 27.8/17.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.069 | 0.50 | 0.50 | 0.00 | 3.42 | 24.6/25.1 | 23.2/22.7 | late empty net |
| OTT shot control · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.50 | 0.50 | 0.49 | 2.73 | 19.1/29.6 | 28.1/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Stutzle: 1+ assists NO | 50 | 0.624 | 0.537 | +0.106 | +0.019 | $4.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Sean Couturier: 1+ goals YES | 14 | 0.180 | 0.160 | +0.032 | +0.012 | $1.52 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ottawa over 3.5 goals scored NO | 59 | 0.655 | 0.620 | +0.049 | +0.013 | $1.85 | FUNDED_RESEARCH | $1 | OTT:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ottawa wins by over 2.5 goals NO | 78 | 0.830 | 0.803 | +0.038 | +0.011 | $3.54 | FUNDED_RESEARCH | $1 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tim Stutzle: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (3.27 vs 2.88 bp); relationships: KXNHLGOAL-26OCT17OTTPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no: REINFORCING (phi 0.268); KXNHLSPREAD-26OCT17OTTPHI-OTT3|no: REINFORCING (phi 0.163); failure: OTT offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17OTTPHI-OTT3|no; why: higher confidence-adjusted growth (2.36 vs 1.52 bp); despite a smaller raw edge (+0.032 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no: MOSTLY_INDEPENDENT (phi 0.032); KXNHLSPREAD-26OCT17OTTPHI-OTT3|no: MOSTLY_INDEPENDENT (phi 0.122); failure: PHI offense suppressed (<= 2 goals)
- **Ottawa over 3.5 goals scored NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no; why: Broad expression KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTCYAKEMCHUK26-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.87 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: REINFORCING (phi 0.268); KXNHLGOAL-26OCT17OTTPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLSPREAD-26OCT17OTTPHI-OTT3|no: REINFORCING (phi 0.493); failure: OTT offense succeeds (4+ goals)
- **Ottawa wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no; why: second expression of the same thesis: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no has the higher standalone adjusted growth (3.27 vs 1.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.163); they share one thesis budget; relationships: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: REINFORCING (phi 0.163); KXNHLGOAL-26OCT17OTTPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.122); KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no: REINFORCING (phi 0.493); failure: OTT wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.4388): highest fidelity KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no — Broad expression KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTCYAKEMCHUK26-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.87 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis PHI:WINS (p 0.4816): highest fidelity KXNHLSPREAD-26OCT17OTTPHI-OTT3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3227): highest fidelity KXNHLSPREAD-26OCT17OTTPHI-OTT3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17OTTPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.4 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3348, phi -0.264)
- KXNHLGOAL-26OCT17OTTPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4664, phi -0.225)
- KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3348, phi -0.979)
- KXNHLSPREAD-26OCT17OTTPHI-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2825, phi -0.72)
- override: Broad expression KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTCYAKEMCHUK26-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.87 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.73 (adj +0.40) on $16.41, P(profit) 0.6292, adj growth 3.7 bp · B EV +1.63 (adj +0.39) on $11.68, P(profit) 0.6264, adj growth 3.6 bp · C EV +2.49 (adj +0.56) on $12.01, P(profit) 0.6907, adj growth 5.0 bp · R EV +0.13 (adj +0.04) on $2.00, P(profit) 0.6322, adj growth 1.3 bp

## NYR @ CBJ  ·  10000 joint draws  ·  404 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_NYR_win | p_overtime | goals | shots CBJ/NYR | CBJ/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.57 | 0.43 | 0.00 | 5.96 | 26.8/26.2 | 23.0/23.0 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.112 | 0.65 | 0.35 | 0.00 | 5.97 | 32.0/20.9 | 18.0/27.7 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.54 | 0.46 | 0.48 | 5.86 | 32.5/21.0 | 17.9/29.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.50 | 0.50 | 0.46 | 5.89 | 26.8/26.4 | 23.0/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.59 | 0.41 | 0.00 | 9.25 | 28.4/27.9 | 22.6/21.9 | even strength |
| CBJ shot control · high event (8+) · decided (2+) | 0.068 | 0.65 | 0.35 | 0.00 | 9.14 | 33.5/22.1 | 17.5/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pavel Dorofeyev: 1+ assists NO | 72 | 0.786 | 0.748 | +0.052 | +0.014 | $7.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17NYRCBJ-NYR3|no; why: higher confidence-adjusted growth (2.19 vs 0.06 bp); alternative not eligible: confidence-adjusted EV +0.0018 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · decided (2+) 0.11, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NYR:SUPPRESSED (p 0.4638): highest fidelity KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.321, phi -0.207)

portfolios: A EV +0.46 (adj +0.12) on $6.56, P(profit) 0.7861, adj growth 1.2 bp · B EV +0.54 (adj +0.15) on $7.67, P(profit) 0.7861, adj growth 1.4 bp · C EV +0.92 (adj +0.25) on $12.94, P(profit) 0.7861, adj growth 2.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ CHI  ·  10000 joint draws  ·  394 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_DAL_win | p_overtime | goals | shots CHI/DAL | CHI/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.45 | 0.55 | 0.00 | 5.99 | 25.5/26.0 | 22.3/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.48 | 5.94 | 25.6/26.1 | 22.9/22.3 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.106 | 0.39 | 0.61 | 0.00 | 5.99 | 19.9/30.9 | 26.5/16.9 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.45 | 0.55 | 0.47 | 5.85 | 20.4/31.0 | 27.6/17.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.45 | 0.55 | 0.00 | 9.23 | 27.2/27.6 | 21.2/21.4 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.066 | 0.34 | 0.66 | 0.00 | 9.16 | 21.6/32.7 | 25.5/16.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 11 | 0.149 | 0.134 | +0.032 | +0.017 | $2.22 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 25 | 0.303 | 0.281 | +0.040 | +0.018 | $2.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
| Cole Smith: 1+ goals YES | 7 | 0.093 | 0.085 | +0.019 | +0.011 | $1.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 71 | 0.807 | 0.741 | +0.083 | +0.016 | $6.53 | FUNDED_RESEARCH | $2 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes; why: higher confidence-adjusted growth (6.21 vs 4.75 bp); despite a smaller raw edge (+0.032 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.917 vs 0.544); relationships: KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT17DALCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26OCT17DALCHI-DAL3|no: MOSTLY_INDEPENDENT (phi 0.099); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes; why: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes has the higher standalone adjusted growth (4.75 vs 3.71 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.175); relationships: KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT17DALCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT17DALCHI-DAL3|no: MOSTLY_INDEPENDENT (phi 0.127); failure: CHI offense suppressed (<= 2 goals)
- **Cole Smith: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes; why: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes has the higher standalone adjusted growth (4.75 vs 3.49 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.144); relationships: KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT17DALCHI-DAL3|no: MOSTLY_INDEPENDENT (phi 0.087); failure: CHI offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes; why: Broad expression KXNHLSPREAD-26OCT17DALCHI-DAL3|no selected over broad KXNHLTEAMTOTAL-26OCT17DALCHI-DAL2|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.45 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.099); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.127); KXNHLGOAL-26OCT17DALCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi 0.087); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3451): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS_BY_2PLUS (p 0.2424): highest fidelity KXNHLSPREAD-26OCT17DALCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes (same contract)
- thesis DAL:SUPPRESSED (p 0.3767): highest fidelity KXNHLSPREAD-26OCT17DALCHI-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes — Broad expression KXNHLSPREAD-26OCT17DALCHI-DAL3|no selected over broad KXNHLTEAMTOTAL-26OCT17DALCHI-DAL2|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.45 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4313, phi -0.183)
- KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4313, phi -0.259)
- KXNHLGOAL-26OCT17DALCHI-CHICSMITH22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4313, phi -0.151)
- KXNHLSPREAD-26OCT17DALCHI-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.2 pts; opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3109, phi -0.727)
- override: Broad expression KXNHLSPREAD-26OCT17DALCHI-DAL3|no selected over broad KXNHLTEAMTOTAL-26OCT17DALCHI-DAL2|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.45 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.79 (adj +0.47) on $16.41, P(profit) 0.5631, adj growth 4.0 bp · B EV +2.11 (adj +0.85) on $12.85, P(profit) 0.4309, adj growth 7.9 bp · C EV +1.22 (adj +0.43) on $4.48, P(profit) 0.2424, adj growth 3.8 bp · R EV +0.50 (adj +0.19) on $3.00, P(profit) 0.1488, adj growth 6.8 bp

## STL @ NSH  ·  10000 joint draws  ·  420 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_STL_win | p_overtime | goals | shots NSH/STL | NSH/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.51 | 0.49 | 0.00 | 6.04 | 27.5/27.5 | 23.8/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.48 | 5.96 | 27.6/27.6 | 24.2/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.52 | 0.48 | 0.00 | 9.34 | 28.8/28.9 | 23.0/22.2 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.072 | 0.43 | 0.57 | 0.00 | 6.04 | 21.9/32.3 | 28.2/18.8 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.065 | 0.58 | 0.42 | 0.00 | 5.97 | 32.1/21.8 | 18.8/28.0 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.43 | 0.57 | 0.47 | 5.9 | 22.0/32.3 | 28.8/19.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan O'Reilly: 1+ goals YES | 27 | 0.308 | 0.295 | +0.025 | +0.011 | $2.00 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT17STLNSH-NSH6|yes; why: higher confidence-adjusted growth (1.34 vs 0.28 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.907 vs 0.328); alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NSH:OFFENSE_4PLUS (p 0.407): highest fidelity KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes (same contract)
- KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3768, phi -0.259)

portfolios: A EV +0.24 (adj +0.11) on $2.81, P(profit) 0.3083, adj growth 1.0 bp · B EV +0.17 (adj +0.08) on $2.00, P(profit) 0.3083, adj growth 0.7 bp · C EV +0.29 (adj +0.13) on $3.38, P(profit) 0.3083, adj growth 1.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ LAK  ·  10000 joint draws  ·  402 bet sides mapped, 2 +EV candidates, 2 on card


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
| JJ Peterka: 1+ assists NO | 71 | 0.826 | 0.744 | +0.102 | +0.020 | $10.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 54 | 0.616 | 0.568 | +0.059 | +0.011 | $3.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (4.29 vs 0.63 bp); alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: BOS offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17BOSLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (1.01 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BOS:SUPPRESSED (p 0.4548): highest fidelity KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no (same contract)
- thesis LAK:SUPPRESSED (p 0.3886): highest fidelity KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no (same contract)
- KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.6 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3324, phi -0.209)
- KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3823, phi -0.279)

portfolios: A EV +1.61 (adj +0.30) on $13.12, P(profit) 0.5101, adj growth 2.8 bp · B EV +1.82 (adj +0.35) on $13.78, P(profit) 0.8261, adj growth 3.3 bp · C EV +3.07 (adj +0.59) on $23.26, P(profit) 0.8261, adj growth 5.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_EDM_win | p_overtime | goals | shots UTA/EDM | UTA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.54 | 0.46 | 0.00 | 6.1 | 27.5/27.6 | 24.3/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.121 | 0.53 | 0.47 | 0.00 | 9.53 | 29.2/29.1 | 23.0/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.49 | 0.51 | 0.47 | 6.02 | 27.7/27.7 | 24.3/24.2 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.070 | 0.60 | 0.40 | 0.00 | 6.0 | 32.5/21.8 | 18.8/28.2 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.45 | 6.05 | 32.7/22.0 | 18.8/29.3 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.067 | 0.62 | 0.38 | 0.00 | 9.5 | 34.4/23.4 | 18.3/27.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_PIT_win | p_overtime | goals | shots VGK/PIT | VGK/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.70 | 0.30 | 0.00 | 6.09 | 27.6/27.4 | 24.6/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.47 | 5.99 | 27.6/27.5 | 24.2/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.71 | 0.29 | 0.00 | 9.5 | 28.8/28.7 | 23.7/21.1 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.093 | 0.75 | 0.25 | 0.00 | 6.02 | 32.2/21.4 | 19.1/27.3 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.071 | 0.77 | 0.23 | 0.00 | 9.36 | 34.0/23.0 | 18.9/25.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.57 | 0.43 | 0.49 | 5.95 | 32.7/21.8 | 18.7/29.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
