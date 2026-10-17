# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T15:39:23Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.96 | +26.26 | +7.66 | +25.88 | 0.787 | -15.39 | -25.80 | 71.38 |
| B thesis-diversified (joint) ← optimiser card | 146.22 | +23.30 | +11.95 | +21.81 | 0.742 | -20.51 | -31.79 | 113.69 |
| C best expression per thesis | 149.99 | +23.46 | +9.86 | +22.43 | 0.724 | -23.94 | -35.65 | 91.81 |
| R FUNDED research stakes | 24.00 | +3.46 | +1.53 | +2.91 | 0.650 | -6.14 | -8.41 | 0.00 |

## NJD @ WSH  ·  10000 joint draws  ·  432 bet sides mapped, 8 +EV candidates, 4 on card


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
| Aliaksei Protas: 1+ goals YES | 18 | 0.244 | 0.225 | +0.053 | +0.035 | $3.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Ethen Frank: 1+ goals YES | 11 | 0.144 | 0.133 | +0.027 | +0.016 | $1.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 17 | 0.206 | 0.195 | +0.027 | +0.015 | $1.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 76 | 0.798 | 0.786 | +0.026 | +0.014 | $5.79 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes; why: higher confidence-adjusted growth (17.12 vs 3.31 bp); relationships: KXNHLGOAL-26OCT17NJWSH-WSHEFRANK53-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.022); failure: WSH offense suppressed (<= 2 goals)
- **Ethen Frank: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (17.12 vs 5.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (17.12 vs 3.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17NJWSH-WSHEFRANK53-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.021); failure: WSH offense suppressed (<= 2 goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (2.32 vs 1.59 bp); despite a smaller raw edge (+0.026 vs +0.099/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT17NJWSH-WSHEFRANK53-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.021); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4117): highest fidelity KXNHLSPREAD-26OCT17NJWSH-NJ2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4673): highest fidelity KXNHLSPREAD-26OCT17NJWSH-NJ2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:NET_LOW_VOLUME (p 0.4631): highest fidelity KXNHLSAVE-26OCT17NJWSH-NJJALLEN34-26|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT17NJWSH-NJJALLEN34-26|no (same contract)
- KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3653, phi -0.23)
- KXNHLGOAL-26OCT17NJWSH-WSHEFRANK53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3653, phi -0.171)
- KXNHLGOAL-26OCT17NJWSH-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3653, phi -0.201)
- KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3188, phi -0.235)

portfolios: A EV +2.43 (adj +0.73) on $12.88, P(profit) 0.523, adj growth 7.0 bp · B EV +1.88 (adj +1.16) on $12.83, P(profit) 0.4539, adj growth 11.0 bp · C EV +2.88 (adj +1.24) on $18.96, P(profit) 0.575, adj growth 11.5 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.7985, adj growth 1.3 bp

## CAR @ WPG  ·  10000 joint draws  ·  396 bet sides mapped, 13 +EV candidates, 3 on card


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
| Winnipeg wins by over 1.5 goals YES | 18 | 0.260 | 0.218 | +0.070 | +0.027 | $2.30 | FUNDED_RESEARCH | $1 | WPG:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikolaj Ehlers: 1+ goals NO | 73 | 0.777 | 0.764 | +0.033 | +0.020 | $6.57 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Kyle Connor: 1+ goals YES | 37 | 0.412 | 0.400 | +0.025 | +0.014 | $1.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_STRONGER | D |
- **Winnipeg wins by over 1.5 goals YES** — thesis: WPG wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes; why: higher confidence-adjusted growth (10.42 vs 7.54 bp); relationships: KXNHLGOAL-26OCT17CARWPG-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.13); KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: REINFORCING (phi 0.205); failure: CAR wins (incl. OT/SO)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes has the higher standalone adjusted growth (10.42 vs 4.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.130); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: MOSTLY_INDEPENDENT (phi 0.13); KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CAR offense succeeds (4+ goals)
- **Kyle Connor: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes; why: Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.54 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: REINFORCING (phi 0.205); KXNHLGOAL-26OCT17CARWPG-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:WINS_BY_2PLUS (p 0.2602): highest fidelity KXNHLSPREAD-26OCT17CARWPG-WPG2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-WPG2|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3734): highest fidelity KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-WPG2|yes — Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.53 vs 0.55 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis WPG:WINS (p 0.4733): highest fidelity KXNHLSPREAD-26OCT17CARWPG-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-WPG2|yes — Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.54 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLSPREAD-26OCT17CARWPG-WPG2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5267, phi -0.626)
- KXNHLGOAL-26OCT17CARWPG-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4113, phi -0.211)
- KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4046, phi -0.315)
- override: Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.54 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.53 vs 0.55 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.99 (adj +0.73) on $12.88, P(profit) 0.4733, adj growth 6.4 bp · B EV +1.22 (adj +0.55) on $10.17, P(profit) 0.451, adj growth 5.3 bp · C EV +1.45 (adj +0.56) on $3.94, P(profit) 0.2602, adj growth 5.2 bp · R EV +0.46 (adj +0.20) on $3.00, P(profit) 0.2602, adj growth 7.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17CARWPG-WPG|yes == KXNHLGAME-26OCT17CARWPG-CAR|no

## VAN @ TBL  ·  10000 joint draws  ·  382 bet sides mapped, 22 +EV candidates, 4 on card


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
| Tampa Bay wins by over 1.5 goals NO | 42 | 0.607 | 0.482 | +0.170 | +0.045 | $2.96 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 54 | 0.726 | 0.602 | +0.168 | +0.044 | $6.49 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| John Carlson: 1+ goals NO | 82 | 0.878 | 0.860 | +0.048 | +0.030 | $7.59 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Filip Chytil: 1+ goals YES | 16 | 0.210 | 0.195 | +0.041 | +0.026 | $2.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB3|no; why: higher confidence-adjusted growth (18.13 vs 17.46 bp); relationships: KXNHLSPREAD-26OCT17VANTB-TB3|no: DUPLICATIVE (phi 0.765); KXNHLGOAL-26OCT17VANTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.09); KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: REINFORCING (phi 0.169); failure: TBL wins by 2+
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17VANTB-TB2|no has the higher standalone adjusted growth (18.13 vs 17.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.765); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: DUPLICATIVE (phi 0.765); KXNHLGOAL-26OCT17VANTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.09); KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.143); failure: TBL wins by 2+
- **John Carlson: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17VANTB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17VANTB-TB2|no has the higher standalone adjusted growth (18.13 vs 13.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.090); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: MOSTLY_INDEPENDENT (phi 0.09); KXNHLSPREAD-26OCT17VANTB-TB3|no: MOSTLY_INDEPENDENT (phi 0.09); KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: TBL offense succeeds (4+ goals)
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17VANTB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17VANTB-TB2|no has the higher standalone adjusted growth (18.13 vs 10.10 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.169); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: REINFORCING (phi 0.169); KXNHLSPREAD-26OCT17VANTB-TB3|no: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26OCT17VANTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.16, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, TBL shot control · high event (8+) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4201): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.1871): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no (same contract)
- thesis TBL:SUPPRESSED (p 0.3164): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT17VANTB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 19.2 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3928, phi -1.0)
- KXNHLSPREAD-26OCT17VANTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 19.1 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3928, phi -0.765)
- KXNHLGOAL-26OCT17VANTB-TBJCARLSON74-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.477, phi -0.13)
- KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4839, phi -0.255)

portfolios: A EV +4.90 (adj +0.98) on $12.88, P(profit) 0.6072, adj growth 9.1 bp · B EV +4.06 (adj +1.42) on $19.18, P(profit) 0.6939, adj growth 13.6 bp · C EV +4.39 (adj +1.15) on $11.38, P(profit) 0.6072, adj growth 10.7 bp · R EV +1.11 (adj +0.33) on $5.00, P(profit) 0.71, adj growth 12.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17VANTB-VAN|yes == KXNHLGAME-26OCT17VANTB-TB|no

## SEA @ FLA  ·  10000 joint draws  ·  418 bet sides mapped, 18 +EV candidates, 4 on card


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
| Berkly Catton: 1+ goals YES | 13 | 0.193 | 0.173 | +0.055 | +0.035 | $3.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 10 | 0.148 | 0.133 | +0.042 | +0.027 | $2.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 64 | 0.709 | 0.690 | +0.052 | +0.034 | $7.67 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 11 | 0.155 | 0.139 | +0.038 | +0.022 | $2.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes; why: higher confidence-adjusted growth (22.34 vs 10.24 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes; why: higher confidence-adjusted growth (16.42 vs 10.24 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: SEA offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17SEAFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (11.32 vs 8.77 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: FLA offense succeeds (4+ goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes; why: higher confidence-adjusted growth (10.24 vs 7.37 bp); despite a smaller raw edge (+0.038 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.906 vs 0.535); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis FLA:SUPPRESSED (p 0.3867): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.3753): highest fidelity KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA2|yes (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2633): highest fidelity KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA2|yes (same contract)
- KXNHLGOAL-26OCT17SEAFLA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.198)
- KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.183)
- KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4008, phi -0.247)
- KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.205)

portfolios: A EV +2.02 (adj +0.45) on $12.88, P(profit) 0.6479, adj growth 4.2 bp · B EV +3.64 (adj +2.31) on $15.70, P(profit) 0.4163, adj growth 21.9 bp · C EV +2.46 (adj +1.34) on $15.80, P(profit) 0.7518, adj growth 12.5 bp · R EV +0.16 (adj +0.10) on $2.00, P(profit) 0.7086, adj growth 4.0 bp

## NYI @ TOR  ·  10000 joint draws  ·  428 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYI_win | p_overtime | goals | shots TOR/NYI | TOR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.53 | 0.47 | 0.00 | 6.02 | 27.7/28.4 | 25.0/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.50 | 6.03 | 27.8/28.6 | 25.2/24.4 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.106 | 0.49 | 0.51 | 0.00 | 5.99 | 22.1/34.0 | 30.4/18.8 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.47 | 0.53 | 0.49 | 5.97 | 22.3/34.4 | 30.9/19.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.55 | 0.45 | 0.00 | 9.38 | 29.4/30.1 | 24.3/22.7 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.079 | 0.47 | 0.53 | 0.00 | 9.25 | 23.8/36.2 | 29.4/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ondrej Palat: 1+ goals YES | 11 | 0.143 | 0.132 | +0.026 | +0.015 | $1.53 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.244 | 0.234 | +0.022 | +0.012 | $1.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (4.82 vs 1.92 bp); relationships: KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NYI offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NYITOR-NYIMMACCELLI63-1|yes; why: higher confidence-adjusted growth (1.92 vs 0.52 bp); despite a smaller raw edge (+0.022 vs +0.023/contract); alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17NYITOR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYI shot control · normal event (5-7) · decided (2+) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.3875): highest fidelity KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes (same contract)
- KXNHLGOAL-26OCT17NYITOR-NYIOPALAT81-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.396, phi -0.182)
- KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.396, phi -0.218)

portfolios: A EV +0.60 (adj +0.35) on $3.70, P(profit) 0.352, adj growth 3.2 bp · B EV +0.49 (adj +0.28) on $3.01, P(profit) 0.352, adj growth 2.7 bp · C EV +0.21 (adj +0.12) on $2.08, P(profit) 0.2436, adj growth 1.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ MTL  ·  10000 joint draws  ·  408 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_BUF_win | p_overtime | goals | shots MTL/BUF | MTL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.55 | 0.45 | 0.00 | 6.04 | 27.3/27.6 | 24.3/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.49 | 0.51 | 0.48 | 5.95 | 27.3/27.8 | 24.4/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.53 | 0.47 | 0.00 | 9.26 | 28.7/28.9 | 23.1/22.4 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.092 | 0.47 | 0.53 | 0.00 | 6.0 | 21.7/32.6 | 28.7/18.4 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.47 | 0.53 | 0.46 | 6.0 | 21.9/32.6 | 29.1/18.6 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.065 | 0.45 | 0.55 | 0.00 | 9.36 | 23.4/34.5 | 27.8/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan McLeod: 1+ goals YES | 13 | 0.182 | 0.168 | +0.044 | +0.029 | $2.96 | FUNDED_RESEARCH | $1 | BUF:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 23 | 0.284 | 0.268 | +0.042 | +0.026 | $3.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Noah Ostlund: 1+ goals YES | 19 | 0.234 | 0.221 | +0.034 | +0.020 | $2.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Ryan McLeod: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (15.72 vs 7.92 bp); relationships: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT17BUFMTL-BUFNOSTLUND86-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: BUF offense suppressed (<= 2 goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFNOSTLUND86-1|yes; why: higher confidence-adjusted growth (7.92 vs 5.42 bp); relationships: KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT17BUFMTL-BUFNOSTLUND86-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: BUF offense suppressed (<= 2 goals)
- **Noah Ostlund: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes has the higher standalone adjusted growth (7.92 vs 5.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.3925): highest fidelity KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:OFFENSE_4PLUS (p 0.4189): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3869, phi -0.188)
- KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3869, phi -0.24)
- KXNHLGOAL-26OCT17BUFMTL-BUFNOSTLUND86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3869, phi -0.22)

portfolios: A EV +2.53 (adj +1.36) on $12.88, P(profit) 0.4965, adj growth 12.7 bp · B EV +1.86 (adj +1.19) on $8.33, P(profit) 0.5517, adj growth 11.3 bp · C EV +0.77 (adj +0.47) on $4.44, P(profit) 0.2844, adj growth 4.4 bp · R EV +0.32 (adj +0.21) on $1.00, P(profit) 0.1816, adj growth 7.9 bp

## SJS @ DET  ·  10000 joint draws  ·  424 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_SJS_win | p_overtime | goals | shots DET/SJS | DET/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.53 | 0.47 | 0.00 | 6.0 | 27.6/27.3 | 24.0/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.47 | 5.94 | 27.8/27.4 | 24.1/24.5 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.101 | 0.61 | 0.39 | 0.00 | 5.99 | 32.8/21.6 | 18.7/28.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.55 | 0.45 | 0.48 | 5.89 | 33.1/21.8 | 18.7/29.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.51 | 0.49 | 0.00 | 9.23 | 29.2/28.8 | 22.8/23.0 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.065 | 0.58 | 0.42 | 0.00 | 9.24 | 35.0/23.2 | 18.0/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Collin Graf: 1+ goals YES | 13 | 0.167 | 0.156 | +0.029 | +0.018 | $1.97 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Kiefer Sherwood: 1+ goals YES | 17 | 0.204 | 0.195 | +0.025 | +0.015 | $1.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Luca Cagnoni: 1+ assists NO | 70 | 0.768 | 0.729 | +0.053 | +0.014 | $5.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Mason Marchment: 1+ assists NO | 72 | 0.777 | 0.746 | +0.043 | +0.012 | $5.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes; why: higher confidence-adjusted growth (6.12 vs 3.20 bp); relationships: KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.03); KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi -0.04); KXNHLAST-26OCT17SJDET-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.038); failure: SJS offense suppressed (<= 2 goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes has the higher standalone adjusted growth (6.12 vs 3.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.030); they share one thesis budget; relationships: KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.03); KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi -0.029); KXNHLAST-26OCT17SJDET-SJMMARCHMENT27-1|no: INTENTIONAL_DIVERSIFIER (phi -0.099); failure: SJS offense suppressed (<= 2 goals)
- **Luca Cagnoni: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17SJDET-SJMMARCHMENT27-1|no; why: higher confidence-adjusted growth (2.16 vs 1.62 bp); relationships: KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.04); KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.029); KXNHLAST-26OCT17SJDET-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.058); failure: SJS offense succeeds (4+ goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no; why: second expression of the same thesis: KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no has the higher standalone adjusted growth (2.16 vs 1.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.058); they share one thesis budget; relationships: KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.099); KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi 0.058); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.3656): highest fidelity KXNHLSPREAD-26OCT17SJDET-DET2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.4201): highest fidelity KXNHLAST-26OCT17SJDET-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS (p 0.4781): highest fidelity KXNHLSPREAD-26OCT17SJDET-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17SJDET-DET2|no (same contract)
- KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4201, phi -0.199)
- KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4201, phi -0.217)
- KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3656, phi -0.218)
- KXNHLAST-26OCT17SJDET-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3656, phi -0.232)

portfolios: A EV +1.04 (adj +0.28) on $12.88, P(profit) 0.5635, adj growth 2.6 bp · B EV +1.36 (adj +0.60) on $14.44, P(profit) 0.7335, adj growth 5.7 bp · C EV +1.50 (adj +0.60) on $15.88, P(profit) 0.5789, adj growth 5.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ PHI  ·  10000 joint draws  ·  396 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_OTT_win | p_overtime | goals | shots PHI/OTT | PHI/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.50 | 0.50 | 0.00 | 5.98 | 25.8/26.2 | 22.7/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.47 | 5.88 | 26.0/26.3 | 23.0/22.8 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.100 | 0.43 | 0.56 | 0.00 | 5.92 | 20.6/31.1 | 27.2/17.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.47 | 0.53 | 0.47 | 5.81 | 20.4/31.5 | 28.1/17.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.49 | 0.51 | 0.48 | 2.78 | 24.3/24.4 | 22.9/22.9 | even strength |
| OTT shot control · low event (<=4) · decided (2+) | 0.065 | 0.45 | 0.56 | 0.00 | 3.36 | 19.2/29.9 | 27.8/17.6 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Porter Martone: 1+ goals NO | 78 | 0.820 | 0.808 | +0.028 | +0.016 | $7.67 | FUNDED_RESEARCH | $2 | PHI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 18 | 0.220 | 0.204 | +0.029 | +0.013 | $1.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Ottawa wins by over 2.5 goals NO | 78 | 0.835 | 0.805 | +0.043 | +0.013 | $5.53 | FUNDED_RESEARCH | $2 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ottawa over 3.5 goals scored NO | 59 | 0.657 | 0.621 | +0.050 | +0.014 | $1.79 | FUNDED_RESEARCH | $1 | OTT:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17OTTPHI-PHIPMARTONE94-1|no; why: higher confidence-adjusted growth (3.24 vs 0.00 bp); despite a smaller raw edge (+0.028 vs +0.030/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT17OTTPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSPREAD-26OCT17OTTPHI-OTT3|no: INTENTIONAL_DIVERSIFIER (phi -0.108); KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no: MOSTLY_INDEPENDENT (phi 0.007); failure: PHI offense succeeds (4+ goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17OTTPHI-OTT3|no; why: higher confidence-adjusted growth (2.48 vs 2.23 bp); despite a smaller raw edge (+0.029 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSPREAD-26OCT17OTTPHI-OTT3|no: MOSTLY_INDEPENDENT (phi 0.097); KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no: MOSTLY_INDEPENDENT (phi -0.011); failure: PHI offense suppressed (<= 2 goals)
- **Ottawa wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no; why: Broad expression KXNHLSPREAD-26OCT17OTTPHI-OTT3|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-2|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: INTENTIONAL_DIVERSIFIER (phi -0.108); KXNHLGOAL-26OCT17OTTPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.097); KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no: DUPLICATIVE (phi 0.51); failure: OTT wins by 2+
- **Ottawa over 3.5 goals scored NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-2|no; why: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-2|no has the higher standalone adjusted growth (4.32 vs 1.79 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.253); relationships: KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17OTTPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLSPREAD-26OCT17OTTPHI-OTT3|no: DUPLICATIVE (phi 0.51); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.45): highest fidelity KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-2|no — Broad expression KXNHLSPREAD-26OCT17OTTPHI-OTT3|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-2|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis PHI:SUPPRESSED (p 0.4548): highest fidelity KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3158): highest fidelity KXNHLSPREAD-26OCT17OTTPHI-OTT3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17OTTPHI-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3158, phi -0.198)
- KXNHLGOAL-26OCT17OTTPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4548, phi -0.214)
- KXNHLSPREAD-26OCT17OTTPHI-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2801, phi -0.713)
- KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3336, phi -0.979)
- override: Broad expression KXNHLSPREAD-26OCT17OTTPHI-OTT3|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-2|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +0.92 (adj +0.23) on $12.88, P(profit) 0.7117, adj growth 2.2 bp · B EV +0.93 (adj +0.38) on $16.35, P(profit) 0.715, adj growth 3.6 bp · C EV +1.59 (adj +0.57) on $27.11, P(profit) 0.6927, adj growth 5.4 bp · R EV +0.26 (adj +0.09) on $5.00, P(profit) 0.6693, adj growth 3.6 bp

## NYR @ CBJ  ·  10000 joint draws  ·  404 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_NYR_win | p_overtime | goals | shots CBJ/NYR | CBJ/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.59 | 0.41 | 0.00 | 6.03 | 26.8/26.2 | 23.1/23.1 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.113 | 0.67 | 0.33 | 0.00 | 6.0 | 32.1/20.9 | 18.2/27.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.47 | 5.91 | 26.8/26.3 | 23.0/23.6 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.56 | 0.44 | 0.45 | 5.85 | 32.4/21.0 | 18.0/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.58 | 0.42 | 0.00 | 9.2 | 28.4/27.7 | 22.2/21.9 | even strength |
| CBJ shot control · high event (8+) · decided (2+) | 0.066 | 0.68 | 0.32 | 0.00 | 9.29 | 34.1/22.5 | 17.7/26.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 17 | 0.204 | 0.191 | +0.025 | +0.011 | $1.22 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NYRCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (1.78 vs 0.53 bp); alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CBJ:OFFENSE_4PLUS (p 0.4116): highest fidelity KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes (same contract)
- KXNHLGOAL-26OCT17NYRCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3757, phi -0.234)

portfolios: A EV +0.26 (adj +0.12) on $1.93, P(profit) 0.2045, adj growth 1.1 bp · B EV +0.17 (adj +0.07) on $1.22, P(profit) 0.2045, adj growth 0.7 bp · C EV +0.24 (adj +0.11) on $1.72, P(profit) 0.2045, adj growth 1.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ CHI  ·  10000 joint draws  ·  396 bet sides mapped, 21 +EV candidates, 4 on card


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
| Chicago wins by over 1.5 goals YES | 17 | 0.250 | 0.208 | +0.070 | +0.028 | $1.77 | FUNDED_RESEARCH | $1 | CHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ryan Greene: 1+ goals YES | 11 | 0.150 | 0.135 | +0.033 | +0.018 | $1.58 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 25 | 0.304 | 0.287 | +0.041 | +0.024 | $2.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
| Frank Nazar: 1+ goals YES | 19 | 0.236 | 0.222 | +0.035 | +0.021 | $2.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Chicago wins by over 1.5 goals YES** — thesis: CHI wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes; why: higher confidence-adjusted growth (11.28 vs 6.41 bp); despite a smaller raw edge (+0.070 vs +0.077/contract); relationships: KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: REINFORCING (phi 0.163); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: REINFORCING (phi 0.207); KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: REINFORCING (phi 0.169); failure: DAL wins (incl. OT/SO)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes has the higher standalone adjusted growth (11.28 vs 6.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.163); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes: REINFORCING (phi 0.163); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes has the higher standalone adjusted growth (11.28 vs 6.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.207); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes: REINFORCING (phi 0.207); KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: CHI offense suppressed (<= 2 goals)
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes has the higher standalone adjusted growth (11.28 vs 6.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.169); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes: REINFORCING (phi 0.169); KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:WINS_BY_2PLUS (p 0.2503): highest fidelity KXNHLSPREAD-26OCT17DALCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3499): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.384): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-DAL4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT17DALCHI-CHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.524, phi -0.606)
- KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4279, phi -0.19)
- KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4279, phi -0.275)
- KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4279, phi -0.228)

portfolios: A EV +2.55 (adj +0.50) on $12.88, P(profit) 0.5755, adj growth 4.5 bp · B EV +1.91 (adj +0.97) on $8.00, P(profit) 0.6069, adj growth 9.2 bp · C EV +1.53 (adj +0.60) on $3.91, P(profit) 0.2503, adj growth 5.6 bp · R EV +0.68 (adj +0.31) on $2.00, P(profit) 0.3377, adj growth 11.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17DALCHI-CHI|yes == KXNHLGAME-26OCT17DALCHI-DAL|no

## STL @ NSH  ·  10000 joint draws  ·  420 bet sides mapped, 3 +EV candidates, 2 on card


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
| Ryan O'Reilly: 1+ goals YES | 27 | 0.308 | 0.296 | +0.025 | +0.012 | $1.64 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 25 | 0.286 | 0.275 | +0.023 | +0.011 | $1.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT17STLNSH-8|yes; why: higher confidence-adjusted growth (1.66 vs 0.12 bp); despite a smaller raw edge (+0.025 vs +0.025/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.907 vs 0.332); alternative not eligible: confidence-adjusted EV +0.0032 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: NSH offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT17STLNSH-8|yes; why: higher confidence-adjusted growth (1.47 vs 0.12 bp); despite a smaller raw edge (+0.023 vs +0.025/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.906 vs 0.332); alternative not eligible: confidence-adjusted EV +0.0032 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NSH:OFFENSE_4PLUS (p 0.407): highest fidelity KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3967): highest fidelity KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes (same contract)
- KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3768, phi -0.259)
- KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3875, phi -0.248)

portfolios: A EV +0.64 (adj +0.38) on $5.22, P(profit) 0.5387, adj growth 3.5 bp · B EV +0.27 (adj +0.13) on $3.07, P(profit) 0.5052, adj growth 1.3 bp · C EV +0.38 (adj +0.19) on $4.32, P(profit) 0.5052, adj growth 1.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| JJ Peterka: 1+ assists NO | 71 | 0.826 | 0.744 | +0.102 | +0.020 | $7.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Charlie McAvoy: 1+ assists NO | 62 | 0.694 | 0.647 | +0.057 | +0.010 | $2.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (4.29 vs 1.03 bp); relationships: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.027); failure: BOS offense succeeds (4+ goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no; why: second expression of the same thesis: KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no has the higher standalone adjusted growth (4.29 vs 1.03 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.027); they share one thesis budget; relationships: KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.027); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BOS:SUPPRESSED (p 0.4548): highest fidelity KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no (same contract)
- KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.6 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3324, phi -0.209)
- KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3324, phi -0.271)

portfolios: A EV +1.19 (adj +0.22) on $10.31, P(profit) 0.5778, adj growth 2.1 bp · B EV +1.33 (adj +0.25) on $10.44, P(profit) 0.8261, adj growth 2.4 bp · C EV +1.52 (adj +0.30) on $10.85, P(profit) 0.8261, adj growth 2.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ UTA  ·  10000 joint draws  ·  408 bet sides mapped, 11 +EV candidates, 4 on card


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
| Alex Formenton: 1+ goals YES | 15 | 0.209 | 0.192 | +0.050 | +0.033 | $3.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 18 | 0.241 | 0.222 | +0.051 | +0.032 | $3.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 29 | 0.355 | 0.337 | +0.051 | +0.032 | $4.31 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| Evan Bouchard: 1+ goals YES | 18 | 0.228 | 0.215 | +0.038 | +0.024 | $2.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-2|yes; why: higher confidence-adjusted growth (17.29 vs 16.43 bp); despite a smaller raw edge (+0.050 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.858 vs 0.732); relationships: KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT17EDMUTA-EDMEBOUCHARD2-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: EDM offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT17EDMUTA-10|yes; why: higher confidence-adjusted growth (14.03 vs 0.66 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.833 vs 0.326); alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT17EDMUTA-EDMEBOUCHARD2-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: UTA offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (17.29 vs 10.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT17EDMUTA-EDMEBOUCHARD2-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: EDM offense suppressed (<= 2 goals)
- **Evan Bouchard: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes; why: Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMEBOUCHARD2-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-2|yes because adjusted EV is 0.1 pts higher while thesis capture is 0.33 vs 0.23 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4307): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes — Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMEBOUCHARD2-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-2|yes because adjusted EV is 0.1 pts higher while thesis capture is 0.33 vs 0.23 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis UTA:OFFENSE_4PLUS (p 0.4726): highest fidelity KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.3487): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no (same contract)
- KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3487, phi -0.206)
- KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3202, phi -0.209)
- KXNHLGOAL-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3487, phi -0.272)
- KXNHLGOAL-26OCT17EDMUTA-EDMEBOUCHARD2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3487, phi -0.198)
- override: Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMEBOUCHARD2-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-2|yes because adjusted EV is 0.1 pts higher while thesis capture is 0.33 vs 0.23 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.00 (adj +0.76) on $12.88, P(profit) 0.689, adj growth 7.2 bp · B EV +3.26 (adj +2.08) on $13.90, P(profit) 0.7022, adj growth 19.7 bp · C EV +3.49 (adj +1.99) on $18.70, P(profit) 0.4004, adj growth 18.4 bp · R EV +0.34 (adj +0.21) on $2.00, P(profit) 0.3555, adj growth 7.7 bp

## PIT @ VGK  ·  10000 joint draws  ·  422 bet sides mapped, 5 +EV candidates, 3 on card


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
| Bryan Rust: 1+ goals YES | 23 | 0.284 | 0.269 | +0.041 | +0.027 | $3.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 24 | 0.280 | 0.269 | +0.027 | +0.016 | $1.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 69 | 0.734 | 0.718 | +0.029 | +0.013 | $4.40 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17PITVGK-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (8.42 vs 2.94 bp); relationships: KXNHLGOAL-26OCT17PITVGK-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes has the higher standalone adjusted growth (8.42 vs 2.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: PIT offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17PITVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (1.81 vs 0.12 bp); alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17PITVGK-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.3095): highest fidelity KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.2848): highest fidelity KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no (same contract)
- KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4763, phi -0.276)
- KXNHLGOAL-26OCT17PITVGK-PITRRAKELL67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4763, phi -0.271)
- KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5106, phi -0.217)

portfolios: A EV +1.19 (adj +0.57) on $12.88, P(profit) 0.4574, adj growth 5.5 bp · B EV +0.94 (adj +0.56) on $9.58, P(profit) 0.4327, adj growth 5.3 bp · C EV +1.05 (adj +0.62) on $10.90, P(profit) 0.2838, adj growth 5.8 bp · R EV +0.08 (adj +0.04) on $2.00, P(profit) 0.7341, adj growth 1.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
