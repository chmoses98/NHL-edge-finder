# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T13:12:23Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +25.20 | +6.65 | +23.17 | 0.745 | -21.88 | -33.33 | 59.75 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +21.57 | +8.84 | +20.47 | 0.739 | -19.46 | -30.34 | 83.11 |
| C best expression per thesis | 150.00 | +25.74 | +10.01 | +23.83 | 0.703 | -30.21 | -44.41 | 90.26 |
| R FUNDED research stakes | 24.00 | +2.96 | +1.20 | +2.95 | 0.670 | -5.66 | -8.33 | 0.00 |

## NJD @ WSH  ·  10000 joint draws  ·  424 bet sides mapped, 8 +EV candidates, 4 on card


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
| Aliaksei Protas: 1+ goals YES | 18 | 0.243 | 0.227 | +0.053 | +0.037 | $5.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 66 | 0.706 | 0.692 | +0.030 | +0.016 | $5.21 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 75 | 0.788 | 0.777 | +0.025 | +0.014 | $5.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ assists NO | 53 | 0.651 | 0.563 | +0.104 | +0.015 | $3.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17NJWSH-WSHDSTROME17-2|yes; why: higher confidence-adjusted growth (18.94 vs 2.83 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.929 vs 0.814); relationships: KXNHLGOAL-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: WSH offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no; why: KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no has the higher standalone adjusted growth (2.75 vs 2.54 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.120); relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: NJD offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no; why: Player prop expression KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.89 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.077); failure: NJD offense succeeds (4+ goals)
- **Jack Hughes: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no; why: KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no has the higher standalone adjusted growth (2.75 vs 2.08 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.073); relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.077); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4113): highest fidelity KXNHLAST-26OCT17NJWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4492): highest fidelity KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no — Player prop expression KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.89 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3698, phi -0.226)
- KXNHLGOAL-26OCT17NJWSH-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.329, phi -0.227)
- KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.329, phi -0.246)
- KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.6 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.329, phi -0.269)
- override: Player prop expression KXNHLGOAL-26OCT17NJWSH-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.89 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.39 (adj +0.52) on $16.71, P(profit) 0.5667, adj growth 4.8 bp · B EV +2.47 (adj +1.32) on $19.52, P(profit) 0.5247, adj growth 12.3 bp · C EV +3.28 (adj +1.91) on $18.72, P(profit) 0.2429, adj growth 17.0 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.7055, adj growth 1.7 bp

## CAR @ WPG  ·  10000 joint draws  ·  396 bet sides mapped, 10 +EV candidates, 4 on card


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
| Mike Reilly: 1+ goals YES | 4 | 0.057 | 0.055 | +0.014 | +0.012 | $1.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 73 | 0.809 | 0.767 | +0.066 | +0.024 | $9.60 | FUNDED_RESEARCH | $3 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Cole Koepke: 1+ goals YES | 9 | 0.116 | 0.109 | +0.020 | +0.013 | $1.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 31 | 0.352 | 0.341 | +0.027 | +0.016 | $2.26 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
- **Mike Reilly: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17CARWPG-CARMJANKOWSKI77-1|yes; why: higher confidence-adjusted growth (7.99 vs 0.00 bp); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLSPREAD-26OCT17CARWPG-CAR3|no: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26OCT17CARWPG-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: CAR offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes; why: higher confidence-adjusted growth (6.36 vs 3.91 bp); wins across more scripts (relative breadth 1.027 vs 0.554); relationships: KXNHLGOAL-26OCT17CARWPG-CARMREILLY6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26OCT17CARWPG-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.08); KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: REINFORCING (phi 0.154); failure: CAR wins by 2+
- **Cole Koepke: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17CARWPG-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17CARWPG-CAR3|no has the higher standalone adjusted growth (6.36 vs 4.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.080); they share one thesis budget; relationships: KXNHLGOAL-26OCT17CARWPG-CARMREILLY6-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26OCT17CARWPG-CAR3|no: MOSTLY_INDEPENDENT (phi 0.08); KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17CARWPG-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17CARWPG-CAR3|no has the higher standalone adjusted growth (6.36 vs 2.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.154); they share one thesis budget; relationships: KXNHLGOAL-26OCT17CARWPG-CARMREILLY6-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLSPREAD-26OCT17CARWPG-CAR3|no: REINFORCING (phi 0.154); KXNHLGOAL-26OCT17CARWPG-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:WINS (p 0.4733): highest fidelity KXNHLSPREAD-26OCT17CARWPG-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR3|no (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3734): highest fidelity KXNHLTEAMTOTAL-26OCT17CARWPG-WPG4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS_BY_2PLUS (p 0.2602): highest fidelity KXNHLSPREAD-26OCT17CARWPG-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR3|no (same contract)
- KXNHLGOAL-26OCT17CARWPG-CARMREILLY6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:SUPPRESSED (p 0.3699, phi -0.099)
- KXNHLSPREAD-26OCT17CARWPG-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3022, phi -0.737)
- KXNHLGOAL-26OCT17CARWPG-WPGCKOEPKE45-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4046, phi -0.152)
- KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4046, phi -0.282)

portfolios: A EV +1.83 (adj +0.46) on $16.71, P(profit) 0.6739, adj growth 4.2 bp · B EV +1.87 (adj +1.09) on $14.96, P(profit) 0.4254, adj growth 10.2 bp · C EV +1.40 (adj +0.50) on $15.89, P(profit) 0.8095, adj growth 4.7 bp · R EV +0.35 (adj +0.14) on $4.00, P(profit) 0.8095, adj growth 5.3 bp

## VAN @ TBL  ·  10000 joint draws  ·  382 bet sides mapped, 26 +EV candidates, 4 on card


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
| Filip Chytil: 1+ goals YES | 15 | 0.209 | 0.194 | +0.050 | +0.035 | $4.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 54 | 0.729 | 0.603 | +0.171 | +0.045 | $9.60 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Linus Karlsson: 1+ goals YES | 15 | 0.193 | 0.182 | +0.034 | +0.023 | $2.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Jake Guentzel: 1+ goals NO | 60 | 0.663 | 0.644 | +0.046 | +0.028 | $6.92 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17VANTB-VAN2|yes; why: higher confidence-adjusted growth (20.00 vs 18.77 bp); despite a smaller raw edge (+0.050 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.965 vs 0.56); relationships: KXNHLSPREAD-26OCT17VANTB-TB3|no: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26OCT17VANTB-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: VAN offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB2|no; why: higher confidence-adjusted growth (18.27 vs 15.44 bp); wins across more scripts (relative breadth 1.013 vs 0.855); relationships: KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26OCT17VANTB-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.112); KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no: REINFORCING (phi 0.158); failure: TBL wins by 2+
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (20.00 vs 8.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT17VANTB-TB3|no: MOSTLY_INDEPENDENT (phi 0.112); KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: VAN offense suppressed (<= 2 goals)
- **Jake Guentzel: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17VANTB-VAN2|yes; why: Player prop expression KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no selected over player prop KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLSPREAD-26OCT17VANTB-TB3|no: REINFORCING (phi 0.158); KXNHLGOAL-26OCT17VANTB-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.15, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, TBL shot control · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.2886): highest fidelity KXNHLTEAMTOTAL-26OCT17VANTB-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.3706): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB3|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.1755): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB3|no (same contract)
- KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4984, phi -0.261)
- KXNHLSPREAD-26OCT17VANTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 19.4 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4028, phi -0.743)
- KXNHLGOAL-26OCT17VANTB-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4984, phi -0.23)
- KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.475, phi -0.241)
- override: Player prop expression KXNHLGOAL-26OCT17VANTB-TBJGUENTZEL59-1|no selected over player prop KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.59 (adj +1.12) on $16.71, P(profit) 0.7897, adj growth 10.5 bp · B EV +5.36 (adj +2.42) on $23.41, P(profit) 0.6521, adj growth 22.7 bp · C EV +8.83 (adj +3.51) on $25.20, P(profit) 0.7594, adj growth 31.5 bp · R EV +1.07 (adj +0.33) on $5.00, P(profit) 0.7285, adj growth 12.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17VANTB-TB|no == KXNHLGAME-26OCT17VANTB-VAN|yes

## SEA @ FLA  ·  10000 joint draws  ·  416 bet sides mapped, 13 +EV candidates, 4 on card


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
| Sam Reinhart: 1+ goals NO | 64 | 0.714 | 0.693 | +0.057 | +0.036 | $9.60 | FUNDED_RESEARCH | $3 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 10 | 0.141 | 0.129 | +0.035 | +0.022 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 72 | 0.802 | 0.758 | +0.068 | +0.024 | $7.85 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ryan Winterton: 1+ goals YES | 11 | 0.154 | 0.135 | +0.037 | +0.018 | $1.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no; why: higher confidence-adjusted growth (12.99 vs 7.31 bp); despite a smaller raw edge (+0.057 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.02 vs 0.915); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: REINFORCING (phi 0.18); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: FLA offense succeeds (4+ goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no; why: higher confidence-adjusted growth (11.08 vs 7.31 bp); despite a smaller raw edge (+0.035 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.091); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no has the higher standalone adjusted growth (12.99 vs 6.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.180); they share one thesis budget; relationships: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: REINFORCING (phi 0.18); KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.091); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.104); failure: FLA wins by 2+
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no; why: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no has the higher standalone adjusted growth (7.31 vs 6.48 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.125); relationships: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.104); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis FLA:SUPPRESSED (p 0.3722): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.469): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.3612): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4053, phi -0.249)
- KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4173, phi -0.167)
- KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3053, phi -0.75)
- KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4173, phi -0.189)

portfolios: A EV +2.43 (adj +0.66) on $16.71, P(profit) 0.6327, adj growth 6.1 bp · B EV +3.00 (adj +1.60) on $21.86, P(profit) 0.6875, adj growth 15.1 bp · C EV +2.93 (adj +1.44) on $28.12, P(profit) 0.5393, adj growth 13.2 bp · R EV +0.45 (adj +0.23) on $5.00, P(profit) 0.6046, adj growth 8.8 bp

## NYI @ TOR  ·  10000 joint draws  ·  426 bet sides mapped, 2 +EV candidates, 2 on card


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
| Easton Cowan: 1+ assists YES | 26 | 0.328 | 0.286 | +0.054 | +0.013 | $1.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.241 | 0.232 | +0.019 | +0.010 | $1.52 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Easton Cowan: 1+ assists YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NYITOR-TORWNYLANDER88-1|yes; why: higher confidence-adjusted growth (1.79 vs 0.11 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: TOR offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17NYITOR-NYICRITCHIE64-1|yes; why: higher confidence-adjusted growth (1.28 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT17NYITOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, NYI shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3983): highest fidelity KXNHLAST-26OCT17NYITOR-TORECOWAN53-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT17NYITOR-TORECOWAN53-1|yes (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3752): highest fidelity KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes (same contract)
- KXNHLAST-26OCT17NYITOR-TORECOWAN53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3785, phi -0.25)
- KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.411, phi -0.259)

portfolios: A EV +1.40 (adj +0.38) on $8.25, P(profit) 0.4907, adj growth 3.2 bp · B EV +0.52 (adj +0.16) on $3.48, P(profit) 0.4907, adj growth 1.5 bp · C EV +0.86 (adj +0.27) on $5.76, P(profit) 0.4907, adj growth 2.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ MTL  ·  10000 joint draws  ·  406 bet sides mapped, 4 +EV candidates, 3 on card


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
| Zach Benson: 1+ goals YES | 23 | 0.285 | 0.269 | +0.043 | +0.026 | $4.03 | FUNDED_RESEARCH | $2 | BUF:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ assists YES | 34 | 0.412 | 0.369 | +0.057 | +0.013 | $1.86 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_MIXED | D |
| Jack Quinn: 1+ goals YES | 27 | 0.306 | 0.295 | +0.022 | +0.012 | $1.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-2|yes; why: KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-2|yes has the higher standalone adjusted growth (9.74 vs 8.29 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.012); relationships: KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT17BUFMTL-BUFJQUINN22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: BUF offense suppressed (<= 2 goals)
- **Zach Benson: 1+ assists YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-2|yes; why: Player prop expression KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes selected over player prop KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-2|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.59 vs 0.20 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT17BUFMTL-BUFJQUINN22-1|yes: REINFORCING (phi 0.244); failure: BUF offense suppressed (<= 2 goals)
- **Jack Quinn: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-2|yes; why: KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-2|yes has the higher standalone adjusted growth (9.74 vs 1.48 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.185); relationships: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes: REINFORCING (phi 0.244); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.3924): highest fidelity KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes — Player prop expression KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes selected over player prop KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-2|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.59 vs 0.20 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3902, phi -0.247)
- KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3902, phi -0.298)
- KXNHLGOAL-26OCT17BUFMTL-BUFJQUINN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3902, phi -0.247)
- override: Player prop expression KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes selected over player prop KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-2|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.59 vs 0.20 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.81 (adj +1.61) on $14.71, P(profit) 0.5804, adj growth 13.6 bp · B EV +1.13 (adj +0.57) on $7.44, P(profit) 0.4158, adj growth 5.4 bp · C EV +1.58 (adj +0.70) on $2.72, P(profit) 0.101, adj growth 6.2 bp · R EV +0.35 (adj +0.22) on $2.00, P(profit) 0.2852, adj growth 7.6 bp

## SJS @ DET  ·  10000 joint draws  ·  416 bet sides mapped, 2 +EV candidates, 2 on card


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
| Ivar Stenberg: 1+ assists NO | 69 | 0.814 | 0.724 | +0.109 | +0.019 | $9.60 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Collin Graf: 1+ goals YES | 13 | 0.172 | 0.150 | +0.034 | +0.012 | $1.57 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17SJDET-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (3.69 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.042); failure: SJS offense succeeds (4+ goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17SJDET-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (2.64 vs 0.23 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.042); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.3732): highest fidelity KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.4043): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.9 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3732, phi -0.203)
- KXNHLGOAL-26OCT17SJDET-SJCGRAF51-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4043, phi -0.2)

portfolios: A EV +1.83 (adj +0.46) on $9.95, P(profit) 0.1716, adj growth 4.2 bp · B EV +1.87 (adj +0.39) on $11.17, P(profit) 0.8521, adj growth 3.7 bp · C EV +0.60 (adj +0.21) on $2.46, P(profit) 0.1716, adj growth 1.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ PHI  ·  10000 joint draws  ·  396 bet sides mapped, 5 +EV candidates, 4 on card


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
| Tim Stutzle: 1+ assists NO | 50 | 0.624 | 0.537 | +0.106 | +0.019 | $4.01 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Dylan Cozens: 1+ assists NO | 67 | 0.734 | 0.699 | +0.048 | +0.014 | $4.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Andre Burakovsky: 1+ assists NO | 75 | 0.849 | 0.775 | +0.086 | +0.012 | $6.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Ottawa wins by over 2.5 goals NO | 78 | 0.830 | 0.803 | +0.038 | +0.011 | $3.97 | FUNDED_RESEARCH | $1 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tim Stutzle: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTDCOZENS24-1|no; why: higher confidence-adjusted growth (3.27 vs 1.94 bp); relationships: KXNHLAST-26OCT17OTTPHI-OTTDCOZENS24-1|no: MOSTLY_INDEPENDENT (phi 0.074); KXNHLAST-26OCT17OTTPHI-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.033); KXNHLSPREAD-26OCT17OTTPHI-OTT3|no: REINFORCING (phi 0.163); failure: OTT offense succeeds (4+ goals)
- **Dylan Cozens: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no; why: second expression of the same thesis: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no has the higher standalone adjusted growth (3.27 vs 1.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.074); they share one thesis budget; relationships: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.074); KXNHLAST-26OCT17OTTPHI-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.059); KXNHLSPREAD-26OCT17OTTPHI-OTT3|no: MOSTLY_INDEPENDENT (phi 0.15); failure: OTT offense succeeds (4+ goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no; why: second expression of the same thesis: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no has the higher standalone adjusted growth (3.27 vs 1.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.033); they share one thesis budget; relationships: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.033); KXNHLAST-26OCT17OTTPHI-OTTDCOZENS24-1|no: MOSTLY_INDEPENDENT (phi 0.059); KXNHLSPREAD-26OCT17OTTPHI-OTT3|no: MOSTLY_INDEPENDENT (phi 0.117); failure: OTT offense succeeds (4+ goals)
- **Ottawa wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no; why: second expression of the same thesis: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no has the higher standalone adjusted growth (3.27 vs 1.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.163); they share one thesis budget; relationships: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: REINFORCING (phi 0.163); KXNHLAST-26OCT17OTTPHI-OTTDCOZENS24-1|no: MOSTLY_INDEPENDENT (phi 0.15); KXNHLAST-26OCT17OTTPHI-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.117); failure: OTT wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.4388): highest fidelity KXNHLSPREAD-26OCT17OTTPHI-OTT3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.4816): highest fidelity KXNHLSPREAD-26OCT17OTTPHI-OTT3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.4 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3348, phi -0.264)
- KXNHLAST-26OCT17OTTPHI-OTTDCOZENS24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3348, phi -0.243)
- KXNHLAST-26OCT17OTTPHI-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.4 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3348, phi -0.186)
- KXNHLSPREAD-26OCT17OTTPHI-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2825, phi -0.72)

portfolios: A EV +1.88 (adj +0.37) on $16.71, P(profit) 0.687, adj growth 3.5 bp · B EV +2.01 (adj +0.38) on $18.37, P(profit) 0.7375, adj growth 3.6 bp · C EV +1.71 (adj +0.31) on $8.31, P(profit) 0.6238, adj growth 2.8 bp · R EV +0.05 (adj +0.01) on $1.00, P(profit) 0.8304, adj growth 0.5 bp

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
| Pavel Dorofeyev: 1+ assists NO | 72 | 0.786 | 0.748 | +0.052 | +0.014 | $6.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT17NYRCBJ-NYR2|no; why: higher confidence-adjusted growth (2.19 vs 0.11 bp); wins across more scripts (relative breadth 0.991 vs 0.578); alternative not eligible: confidence-adjusted EV +0.0028 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · decided (2+) 0.11, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NYR:SUPPRESSED (p 0.4638): highest fidelity KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.321, phi -0.207)

portfolios: A EV +0.47 (adj +0.13) on $6.68, P(profit) 0.7861, adj growth 1.2 bp · B EV +0.49 (adj +0.13) on $6.98, P(profit) 0.7861, adj growth 1.2 bp · C EV +0.82 (adj +0.22) on $11.55, P(profit) 0.7861, adj growth 2.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ CHI  ·  10000 joint draws  ·  394 bet sides mapped, 6 +EV candidates, 2 on card


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
| Dallas wins by over 2.5 goals NO | 72 | 0.807 | 0.761 | +0.073 | +0.027 | $9.60 | FUNDED_RESEARCH | $3 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Chicago over 2.5 goals scored YES | 50 | 0.579 | 0.534 | +0.061 | +0.017 | $2.00 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes; why: higher confidence-adjusted growth (8.29 vs 4.56 bp); wins across more scripts (relative breadth 1.011 vs 0.566); relationships: KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes: REINFORCING (phi 0.398); failure: DAL wins by 2+
- **Chicago over 2.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-DAL3|no; why: Broad expression KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes selected over broad KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.53 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT17DALCHI-DAL3|no: REINFORCING (phi 0.398); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:WINS (p 0.4598): highest fidelity KXNHLSPREAD-26OCT17DALCHI-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-DAL3|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3451): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-DAL3|no — Broad expression KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes selected over broad KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.53 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CHI:WINS_BY_2PLUS (p 0.2424): highest fidelity KXNHLSPREAD-26OCT17DALCHI-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-DAL3|no (same contract)
- KXNHLSPREAD-26OCT17DALCHI-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3109, phi -0.727)
- KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CHI:SUPPRESSED (p 0.4313, phi -0.979)
- override: Broad expression KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes selected over broad KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.53 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.97 (adj +0.52) on $16.71, P(profit) 0.7291, adj growth 4.7 bp · B EV +1.20 (adj +0.42) on $11.60, P(profit) 0.8074, adj growth 4.0 bp · C EV +1.59 (adj +0.59) on $15.89, P(profit) 0.8074, adj growth 5.5 bp · R EV +0.42 (adj +0.14) on $4.00, P(profit) 0.8074, adj growth 5.4 bp

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
| Matthew Wood: 1+ goals YES | 17 | 0.214 | 0.194 | +0.034 | +0.014 | $1.91 | FUNDED_RESEARCH | $1 | NSH:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Matthew Wood: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT17STLNSH-NSH6|yes; why: higher confidence-adjusted growth (2.95 vs 0.89 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.893 vs 0.328); alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NSH:OFFENSE_4PLUS (p 0.407): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17STLNSH-NSHMWOOD71-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3768, phi -0.196)

portfolios: A EV +0.65 (adj +0.27) on $3.45, P(profit) 0.2137, adj growth 2.4 bp · B EV +0.36 (adj +0.15) on $1.91, P(profit) 0.2137, adj growth 1.4 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.19 (adj +0.08) on $1.00, P(profit) 0.2137, adj growth 2.7 bp

## BOS @ LAK  ·  10000 joint draws  ·  402 bet sides mapped, 1 +EV candidates, 1 on card


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
| JJ Peterka: 1+ assists NO | 71 | 0.826 | 0.741 | +0.102 | +0.017 | $9.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17BOSLA-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (2.99 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BOS:SUPPRESSED (p 0.4548): highest fidelity KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no (same contract)
- KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.1 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3324, phi -0.209)

portfolios: A EV +0.94 (adj +0.15) on $6.68, P(profit) 0.8261, adj growth 1.5 bp · B EV +1.30 (adj +0.21) on $9.29, P(profit) 0.8261, adj growth 2.0 bp · C EV +2.16 (adj +0.35) on $15.38, P(profit) 0.8261, adj growth 3.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
