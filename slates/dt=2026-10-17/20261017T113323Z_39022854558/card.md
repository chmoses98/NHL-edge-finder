# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T11:33:23Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +26.31 | +7.58 | +24.13 | 0.720 | -27.72 | -42.12 | 66.04 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +25.10 | +9.58 | +23.81 | 0.710 | -29.43 | -42.83 | 86.33 |
| C best expression per thesis | 115.47 | +20.17 | +7.16 | +18.42 | 0.690 | -29.78 | -43.26 | 62.80 |
| R FUNDED research stakes | 29.00 | +4.60 | +1.70 | +4.43 | 0.651 | -8.96 | -12.43 | 0.00 |

## NJD @ WSH  ·  10000 joint draws  ·  424 bet sides mapped, 4 +EV candidates, 4 on card


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
| Aliaksei Protas: 1+ goals YES | 19 | 0.243 | 0.227 | +0.042 | +0.026 | $5.71 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 29 | 0.375 | 0.325 | +0.070 | +0.020 | $4.80 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ assists NO | 54 | 0.651 | 0.573 | +0.094 | +0.015 | $6.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Nico Hischier: 1+ assists NO | 64 | 0.716 | 0.670 | +0.060 | +0.014 | $7.75 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17NJWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (9.39 vs 4.28 bp); despite a smaller raw edge (+0.042 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT17NJWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.04); KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: WSH offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (9.39 vs 4.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.040); they share one thesis budget; relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.04); KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: WSH offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no; why: higher confidence-adjusted growth (2.03 vs 1.99 bp); relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT17NJWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no: MOSTLY_INDEPENDENT (phi 0.073); failure: NJD offense succeeds (4+ goals)
- **Nico Hischier: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no; why: second expression of the same thesis: KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no has the higher standalone adjusted growth (2.03 vs 1.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.073); they share one thesis budget; relationships: KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT17NJWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.073); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4113): highest fidelity KXNHLAST-26OCT17NJWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4492): highest fidelity KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17NJWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3698, phi -0.226)
- KXNHLAST-26OCT17NJWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3698, phi -0.271)
- KXNHLAST-26OCT17NJWSH-NJJHUGHES86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.329, phi -0.269)
- KXNHLAST-26OCT17NJWSH-NJNHISCHIER13-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.329, phi -0.254)

portfolios: A EV +4.03 (adj +1.30) on $23.43, P(profit) 0.4707, adj growth 11.7 bp · B EV +4.06 (adj +1.41) on $24.50, P(profit) 0.4874, adj growth 12.7 bp · C EV +3.13 (adj +1.26) on $16.63, P(profit) 0.2429, adj growth 11.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ WPG  ·  10000 joint draws  ·  396 bet sides mapped, 9 +EV candidates, 4 on card


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
| Mike Reilly: 1+ goals YES | 4 | 0.057 | 0.055 | +0.014 | +0.012 | $2.49 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CAR:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 73 | 0.809 | 0.767 | +0.066 | +0.024 | $14.40 | FUNDED_RESEARCH | $4 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 1.5 goals NO | 61 | 0.698 | 0.651 | +0.071 | +0.025 | $5.39 | FUNDED_RESEARCH | $2 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Cole Koepke: 1+ goals YES | 9 | 0.116 | 0.109 | +0.020 | +0.013 | $2.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Mike Reilly: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT17CARWPG-9|yes; why: higher confidence-adjusted growth (7.99 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.858 vs 0.365); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLSPREAD-26OCT17CARWPG-CAR3|no: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLSPREAD-26OCT17CARWPG-CAR2|no: INTENTIONAL_DIVERSIFIER (phi -0.062); KXNHLGOAL-26OCT17CARWPG-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: CAR offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17CARWPG-CAR2|no; why: higher confidence-adjusted growth (6.36 vs 5.75 bp); despite a smaller raw edge (+0.066 vs +0.071/contract); relationships: KXNHLGOAL-26OCT17CARWPG-CARMREILLY6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLSPREAD-26OCT17CARWPG-CAR2|no: DUPLICATIVE (phi 0.737); KXNHLGOAL-26OCT17CARWPG-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.08); failure: CAR wins by 2+
- **Carolina wins by over 1.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17CARWPG-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17CARWPG-CAR3|no has the higher standalone adjusted growth (6.36 vs 5.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.737); they share one thesis budget; relationships: KXNHLGOAL-26OCT17CARWPG-CARMREILLY6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.062); KXNHLSPREAD-26OCT17CARWPG-CAR3|no: DUPLICATIVE (phi 0.737); KXNHLGOAL-26OCT17CARWPG-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.088); failure: CAR wins by 2+
- **Cole Koepke: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17CARWPG-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17CARWPG-CAR3|no has the higher standalone adjusted growth (6.36 vs 4.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.080); they share one thesis budget; relationships: KXNHLGOAL-26OCT17CARWPG-CARMREILLY6-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26OCT17CARWPG-CAR3|no: MOSTLY_INDEPENDENT (phi 0.08); KXNHLSPREAD-26OCT17CARWPG-CAR2|no: MOSTLY_INDEPENDENT (phi 0.088); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:WINS (p 0.4733): highest fidelity KXNHLSPREAD-26OCT17CARWPG-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR2|no (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3734): highest fidelity KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS_BY_2PLUS (p 0.2602): highest fidelity KXNHLSPREAD-26OCT17CARWPG-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17CARWPG-CAR2|no (same contract)
- KXNHLGOAL-26OCT17CARWPG-CARMREILLY6-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:SUPPRESSED (p 0.3699, phi -0.099)
- KXNHLSPREAD-26OCT17CARWPG-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3022, phi -0.737)
- KXNHLSPREAD-26OCT17CARWPG-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3022, phi -1.0)
- KXNHLGOAL-26OCT17CARWPG-WPGCKOEPKE45-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4046, phi -0.152)

portfolios: A EV +2.46 (adj +0.74) on $23.43, P(profit) 0.6739, adj growth 6.7 bp · B EV +3.19 (adj +1.72) on $24.60, P(profit) 0.7314, adj growth 15.4 bp · C EV +1.77 (adj +0.63) on $20.00, P(profit) 0.8095, adj growth 5.7 bp · R EV +0.58 (adj +0.21) on $6.00, P(profit) 0.6978, adj growth 7.3 bp

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
| Tampa Bay wins by over 1.5 goals NO | 42 | 0.597 | 0.479 | +0.160 | +0.042 | $6.15 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 55 | 0.729 | 0.606 | +0.161 | +0.039 | $10.22 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Filip Chytil: 1+ goals YES | 16 | 0.209 | 0.197 | +0.040 | +0.027 | $4.82 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 16 | 0.193 | 0.185 | +0.024 | +0.015 | $2.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB3|no; why: higher confidence-adjusted growth (15.44 vs 13.35 bp); despite a smaller raw edge (+0.160 vs +0.161/contract); relationships: KXNHLSPREAD-26OCT17VANTB-TB3|no: DUPLICATIVE (phi 0.743); KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: REINFORCING (phi 0.169); KXNHLGOAL-26OCT17VANTB-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.138); failure: TBL wins by 2+
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB2|no; why: Broad expression KXNHLSPREAD-26OCT17VANTB-TB3|no selected over player prop KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no because adjusted EV is 1.0 pts higher while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: DUPLICATIVE (phi 0.743); KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26OCT17VANTB-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.112); failure: TBL wins by 2+
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT17VANTB-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT17VANTB-VAN5|yes has the higher standalone adjusted growth (15.57 vs 11.45 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.194); relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: REINFORCING (phi 0.169); KXNHLSPREAD-26OCT17VANTB-TB3|no: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26OCT17VANTB-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT17VANTB-VAN5|yes; why: Player prop expression KXNHLGOAL-26OCT17VANTB-VANLKARLSSON94-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17VANTB-VAN5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.33 vs 0.50 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: MOSTLY_INDEPENDENT (phi 0.138); KXNHLSPREAD-26OCT17VANTB-TB3|no: MOSTLY_INDEPENDENT (phi 0.112); KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.15, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, TBL shot control · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.2886): highest fidelity KXNHLTEAMTOTAL-26OCT17VANTB-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no — Player prop expression KXNHLGOAL-26OCT17VANTB-VANLKARLSSON94-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17VANTB-VAN5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.33 vs 0.50 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis VAN:WINS_BY_2PLUS (p 0.1755): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no (same contract)
- thesis VAN:WINS (p 0.3706): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no (same contract)
- KXNHLSPREAD-26OCT17VANTB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 18.2 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4028, phi -1.0)
- KXNHLSPREAD-26OCT17VANTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 18.9 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4028, phi -0.743)
- KXNHLGOAL-26OCT17VANTB-VANFCHYTIL77-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4984, phi -0.261)
- KXNHLGOAL-26OCT17VANTB-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4984, phi -0.23)
- override: Broad expression KXNHLSPREAD-26OCT17VANTB-TB3|no selected over player prop KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no because adjusted EV is 1.0 pts higher while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26OCT17VANTB-VANLKARLSSON94-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17VANTB-VAN5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.33 vs 0.50 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.69 (adj +1.28) on $23.43, P(profit) 0.7292, adj growth 11.5 bp · B EV +6.63 (adj +2.29) on $23.68, P(profit) 0.6646, adj growth 20.7 bp · C EV +7.88 (adj +2.42) on $18.49, P(profit) 0.6028, adj growth 21.0 bp · R EV +2.05 (adj +0.72) on $7.00, P(profit) 0.6476, adj growth 24.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17VANTB-TB|no == KXNHLGAME-26OCT17VANTB-VAN|yes

## SEA @ FLA  ·  10000 joint draws  ·  416 bet sides mapped, 7 +EV candidates, 4 on card


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
| Ben Meyers: 1+ goals YES | 10 | 0.141 | 0.127 | +0.035 | +0.021 | $3.59 | FUNDED_RESEARCH | $1 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Florida wins by over 1.5 goals NO | 60 | 0.695 | 0.645 | +0.078 | +0.028 | $6.45 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 72 | 0.802 | 0.758 | +0.068 | +0.024 | $9.90 | FUNDED_RESEARCH | $3 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Kaapo Kakko: 1+ assists YES | 26 | 0.335 | 0.290 | +0.061 | +0.016 | $2.63 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SEA:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no; why: higher confidence-adjusted growth (9.88 vs 7.31 bp); despite a smaller raw edge (+0.035 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no: MOSTLY_INDEPENDENT (phi 0.114); KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: MOSTLY_INDEPENDENT (phi 0.091); KXNHLAST-26OCT17SEAFLA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: SEA offense suppressed (<= 2 goals)
- **Florida wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA3|no; why: higher confidence-adjusted growth (7.31 vs 6.66 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.114); KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: DUPLICATIVE (phi 0.75); KXNHLAST-26OCT17SEAFLA-SEAKKAKKO84-1|yes: REINFORCING (phi 0.185); failure: FLA wins by 2+
- **Florida wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no has the higher standalone adjusted growth (7.31 vs 6.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.750); they share one thesis budget; relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.091); KXNHLSPREAD-26OCT17SEAFLA-FLA2|no: DUPLICATIVE (phi 0.75); KXNHLAST-26OCT17SEAFLA-SEAKKAKKO84-1|yes: REINFORCING (phi 0.154); failure: FLA wins by 2+
- **Kaapo Kakko: 1+ assists YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17SEAFLA-FLA2|no has the higher standalone adjusted growth (7.31 vs 2.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.185); they share one thesis budget; relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLSPREAD-26OCT17SEAFLA-FLA2|no: REINFORCING (phi 0.185); KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: REINFORCING (phi 0.154); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:OFFENSE_4PLUS (p 0.3612): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.469): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-FLA2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2549): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-FLA2|no (same contract)
- KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4173, phi -0.167)
- KXNHLSPREAD-26OCT17SEAFLA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3053, phi -1.0)
- KXNHLSPREAD-26OCT17SEAFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3053, phi -0.75)
- KXNHLAST-26OCT17SEAFLA-SEAKKAKKO84-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4173, phi -0.287)

portfolios: A EV +3.21 (adj +1.00) on $23.43, P(profit) 0.6264, adj growth 8.7 bp · B EV +3.50 (adj +1.48) on $22.57, P(profit) 0.7419, adj growth 13.4 bp · C EV +2.46 (adj +0.89) on $19.46, P(profit) 0.6947, adj growth 7.8 bp · R EV +0.86 (adj +0.39) on $6.00, P(profit) 0.7196, adj growth 13.8 bp

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
| Brayden Schenn: 1+ goals YES | 21 | 0.241 | 0.232 | +0.019 | +0.010 | $2.38 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17NYITOR-TOR2|no; why: higher confidence-adjusted growth (1.28 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, NYI shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.3752): highest fidelity KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes (same contract)
- KXNHLGOAL-26OCT17NYITOR-NYIBSCHENN10-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.411, phi -0.259)

portfolios: A EV +0.24 (adj +0.13) on $2.86, P(profit) 0.2406, adj growth 1.1 bp · B EV +0.20 (adj +0.11) on $2.38, P(profit) 0.2406, adj growth 1.0 bp · C EV +0.27 (adj +0.14) on $3.15, P(profit) 0.2406, adj growth 1.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ MTL  ·  10000 joint draws  ·  406 bet sides mapped, 2 +EV candidates, 2 on card


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
| Zach Benson: 2+ assists YES | 6 | 0.101 | 0.081 | +0.037 | +0.017 | $2.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_MIXED | D |
| Zach Benson: 1+ goals YES | 23 | 0.285 | 0.266 | +0.043 | +0.024 | $5.62 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Zach Benson: 2+ assists YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (9.74 vs 6.81 bp); despite a smaller raw edge (+0.037 vs +0.043/contract); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: BUF offense suppressed (<= 2 goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-2|yes; why: second expression of the same thesis: KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-2|yes has the higher standalone adjusted growth (9.74 vs 6.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-2|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.3924): highest fidelity KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes (same contract)
- KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-2|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3902, phi -0.214)
- KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3902, phi -0.247)

portfolios: A EV +3.86 (adj +1.86) on $11.26, P(profit) 0.3558, adj growth 15.5 bp · B EV +2.47 (adj +1.22) on $8.18, P(profit) 0.3558, adj growth 10.9 bp · C EV +1.98 (adj +0.89) on $3.42, P(profit) 0.101, adj growth 7.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Ivar Stenberg: 1+ assists NO | 69 | 0.814 | 0.720 | +0.109 | +0.015 | $12.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17SJDET-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (2.51 vs 0.02 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0014 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.4043): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT17SJDET-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.4 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3732, phi -0.203)

portfolios: A EV +1.45 (adj +0.21) on $9.37, P(profit) 0.814, adj growth 1.9 bp · B EV +1.98 (adj +0.28) on $12.79, P(profit) 0.814, adj growth 2.5 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ PHI  ·  10000 joint draws  ·  396 bet sides mapped, 1 +EV candidates, 1 on card


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
| Ottawa wins by over 2.5 goals NO | 78 | 0.830 | 0.803 | +0.038 | +0.011 | $10.83 | FUNDED_RESEARCH | $3 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ottawa wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4|no; why: higher confidence-adjusted growth (1.52 vs 0.66 bp); despite a smaller raw edge (+0.038 vs +0.039/contract); wins across more scripts (relative breadth 0.989 vs 0.871); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: OTT wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:WINS (p 0.4816): highest fidelity KXNHLSPREAD-26OCT17OTTPHI-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17OTTPHI-OTT3|no (same contract)
- KXNHLSPREAD-26OCT17OTTPHI-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2825, phi -0.72)

portfolios: A EV +0.45 (adj +0.13) on $9.37, P(profit) 0.8304, adj growth 1.2 bp · B EV +0.52 (adj +0.15) on $10.83, P(profit) 0.8304, adj growth 1.3 bp · C EV +0.69 (adj +0.19) on $14.32, P(profit) 0.8304, adj growth 1.7 bp · R EV +0.15 (adj +0.04) on $3.00, P(profit) 0.8304, adj growth 1.5 bp

## NYR @ CBJ  ·  10000 joint draws  ·  404 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_NYR_win | p_overtime | goals | shots CBJ/NYR | CBJ/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.57 | 0.43 | 0.00 | 5.96 | 26.8/26.2 | 23.0/23.0 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.112 | 0.65 | 0.35 | 0.00 | 5.97 | 32.0/20.9 | 18.0/27.7 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.54 | 0.46 | 0.48 | 5.86 | 32.5/21.0 | 17.9/29.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.50 | 0.50 | 0.46 | 5.89 | 26.8/26.4 | 23.0/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.59 | 0.41 | 0.00 | 9.25 | 28.4/27.9 | 22.6/21.9 | even strength |
| CBJ shot control · high event (8+) · decided (2+) | 0.068 | 0.65 | 0.35 | 0.00 | 9.14 | 33.5/22.1 | 17.5/25.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · decided (2+) 0.11, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ CHI  ·  10000 joint draws  ·  394 bet sides mapped, 6 +EV candidates, 4 on card


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
| Dallas wins by over 2.5 goals NO | 72 | 0.807 | 0.761 | +0.073 | +0.027 | $15.13 | FUNDED_RESEARCH | $4 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 60 | 0.689 | 0.642 | +0.072 | +0.025 | $2.34 | FUNDED_RESEARCH | $1 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Chicago over 4.5 goals scored YES | 13 | 0.182 | 0.154 | +0.045 | +0.016 | $1.92 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Chicago over 2.5 goals scored YES | 50 | 0.579 | 0.537 | +0.061 | +0.019 | $1.10 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17DALCHI-DAL2|no; why: higher confidence-adjusted growth (8.29 vs 5.92 bp); wins across more scripts (relative breadth 1.011 vs 0.909); relationships: KXNHLSPREAD-26OCT17DALCHI-DAL2|no: DUPLICATIVE (phi 0.727); KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes: REINFORCING (phi 0.22); KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes: REINFORCING (phi 0.398); failure: DAL wins by 2+
- **Dallas wins by over 1.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT17DALCHI-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17DALCHI-DAL3|no has the higher standalone adjusted growth (8.29 vs 5.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.727); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17DALCHI-DAL3|no: DUPLICATIVE (phi 0.727); KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes: REINFORCING (phi 0.293); KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes: REINFORCING (phi 0.463); failure: DAL wins by 2+
- **Chicago over 4.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17DALCHI-DAL3|no has the higher standalone adjusted growth (8.29 vs 4.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.220); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17DALCHI-DAL3|no: REINFORCING (phi 0.22); KXNHLSPREAD-26OCT17DALCHI-DAL2|no: REINFORCING (phi 0.293); KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes: DUPLICATIVE (phi 0.403); failure: DAL wins (incl. OT/SO)
- **Chicago over 2.5 goals scored YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17DALCHI-DAL3|no has the higher standalone adjusted growth (8.29 vs 3.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.398); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17DALCHI-DAL3|no: REINFORCING (phi 0.398); KXNHLSPREAD-26OCT17DALCHI-DAL2|no: REINFORCING (phi 0.463); KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes: DUPLICATIVE (phi 0.403); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:WINS (p 0.4598): highest fidelity KXNHLSPREAD-26OCT17DALCHI-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-DAL3|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3451): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-DAL3|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes kept
- thesis CHI:WINS_BY_2PLUS (p 0.2424): highest fidelity KXNHLSPREAD-26OCT17DALCHI-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-DAL3|no (same contract)
- KXNHLSPREAD-26OCT17DALCHI-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3109, phi -0.727)
- KXNHLSPREAD-26OCT17DALCHI-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3109, phi -1.0)
- KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes: FUNDED_RESEARCH; family MIXED; loses 47% of the draws where the thesis happens; opposing: failure thesis DAL:WINS (p 0.5402, phi -0.426)
- KXNHLTEAMTOTAL-26OCT17DALCHI-CHI3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CHI:SUPPRESSED (p 0.4313, phi -0.979)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT17DALCHI-CHI5|yes kept

portfolios: A EV +2.92 (adj +0.93) on $23.43, P(profit) 0.527, adj growth 7.7 bp · B EV +2.54 (adj +0.92) on $20.48, P(profit) 0.8074, adj growth 8.4 bp · C EV +2.00 (adj +0.74) on $20.00, P(profit) 0.8074, adj growth 6.8 bp · R EV +0.96 (adj +0.34) on $7.00, P(profit) 0.7308, adj growth 11.7 bp

## STL @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_STL_win | p_overtime | goals | shots NSH/STL | NSH/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.51 | 0.49 | 0.00 | 6.04 | 27.5/27.5 | 23.8/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.48 | 5.96 | 27.6/27.6 | 24.2/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.52 | 0.48 | 0.00 | 9.34 | 28.8/28.9 | 23.0/22.2 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.072 | 0.43 | 0.57 | 0.00 | 6.04 | 21.9/32.3 | 28.2/18.8 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.065 | 0.58 | 0.42 | 0.00 | 5.97 | 32.1/21.8 | 18.8/28.0 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.43 | 0.57 | 0.47 | 5.9 | 22.0/32.3 | 28.8/19.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BOS_win | p_overtime | goals | shots LAK/BOS | LAK/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.55 | 0.45 | 0.00 | 5.98 | 27.7/27.4 | 23.9/24.0 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.109 | 0.62 | 0.38 | 0.00 | 6.0 | 33.3/21.7 | 18.8/29.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.52 | 0.48 | 0.47 | 5.88 | 27.9/27.3 | 24.0/24.5 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.50 | 0.50 | 0.47 | 5.89 | 33.6/22.2 | 19.1/30.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.55 | 0.45 | 0.00 | 9.21 | 29.4/29.0 | 23.1/22.8 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.066 | 0.62 | 0.38 | 0.00 | 9.15 | 34.8/23.4 | 18.5/27.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
