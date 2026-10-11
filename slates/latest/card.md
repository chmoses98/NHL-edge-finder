# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-11T14:11:46Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +19.82 | +5.05 | +21.15 | 0.662 | -53.75 | -72.27 | 37.32 |
| B thesis-diversified (joint) ← optimiser card | 115.30 | +22.79 | +14.33 | +17.81 | 0.618 | -55.52 | -61.51 | 123.61 |
| C best expression per thesis | 123.54 | +16.65 | +8.68 | +12.18 | 0.613 | -38.27 | -49.15 | 75.68 |
| R FUNDED research stakes | 16.00 | +2.04 | +1.15 | -1.05 | 0.416 | -8.91 | -9.19 | 0.00 |

## SEA @ WSH  ·  10000 joint draws  ·  444 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_SEA_win | p_overtime | goals | shots WSH/SEA | WSH/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.58 | 0.42 | 0.00 | 6.0 | 27.8/27.4 | 24.3/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.53 | 0.47 | 0.49 | 5.93 | 27.5/27.2 | 24.0/24.3 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.097 | 0.66 | 0.34 | 0.00 | 6.0 | 32.7/21.5 | 18.8/28.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.61 | 0.39 | 0.00 | 9.19 | 29.3/28.7 | 23.5/22.4 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.55 | 0.45 | 0.46 | 5.95 | 32.6/21.9 | 18.8/28.8 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.059 | 0.66 | 0.34 | 0.00 | 9.4 | 34.4/23.2 | 18.2/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 9 | 0.136 | 0.122 | +0.040 | +0.026 | $5.92 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Shane Wright: 1+ goals YES | 14 | 0.192 | 0.177 | +0.043 | +0.029 | $7.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 20 | 0.247 | 0.234 | +0.036 | +0.023 | $8.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Washington wins by over 1.5 goals NO | 57 | 0.659 | 0.612 | +0.072 | +0.025 | $14.93 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes; why: higher confidence-adjusted growth (16.66 vs 14.38 bp); despite a smaller raw edge (+0.040 vs +0.043/contract); relationships: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLSPREAD-26OCT11SEAWSH-WSH2|no: MOSTLY_INDEPENDENT (phi 0.115); failure: SEA offense suppressed (<= 2 goals)
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no; why: higher confidence-adjusted growth (14.38 vs 5.65 bp); despite a smaller raw edge (+0.043 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26OCT11SEAWSH-WSH2|no: MOSTLY_INDEPENDENT (phi 0.137); failure: SEA offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT11SEAWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (6.99 vs 0.98 bp); despite a smaller raw edge (+0.036 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26OCT11SEAWSH-WSH2|no: INTENTIONAL_DIVERSIFIER (phi -0.237); failure: WSH offense suppressed (<= 2 goals)
- **Washington wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH3|no; why: higher confidence-adjusted growth (5.65 vs 4.25 bp); relationships: KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.115); KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.137); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.237); failure: WSH wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.3404): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.4352): highest fidelity KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes (same contract)
- thesis GAME:TIGHT (p 0.4379): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11SEAWSH-WSH2|no (same contract)
- KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4455, phi -0.178)
- KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4455, phi -0.233)
- KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3473, phi -0.24)
- KXNHLSPREAD-26OCT11SEAWSH-WSH2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.3407, phi -1.0)

portfolios: A EV +5.45 (adj +1.27) on $50.00, P(profit) 0.7064, adj growth 10.5 bp · B EV +7.87 (adj +4.59) on $36.56, P(profit) 0.4753, adj growth 39.6 bp · C EV +5.76 (adj +3.12) on $33.54, P(profit) 0.3935, adj growth 27.0 bp · R EV +1.33 (adj +0.71) on $6.00, P(profit) 0.6869, adj growth 23.4 bp

## VAN @ NYR  ·  10000 joint draws  ·  384 bet sides mapped, 16 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_VAN_win | p_overtime | goals | shots NYR/VAN | NYR/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.67 | 0.33 | 0.00 | 6.01 | 26.6/26.4 | 23.6/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.54 | 0.46 | 0.46 | 5.87 | 26.6/26.5 | 23.4/23.3 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.092 | 0.72 | 0.28 | 0.00 | 6.02 | 31.5/20.7 | 18.1/26.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.67 | 0.33 | 0.00 | 9.19 | 28.3/28.0 | 23.2/21.1 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.58 | 0.42 | 0.47 | 5.93 | 31.5/21.2 | 18.2/27.9 | even strength |
| NYR shot control · high event (8+) · decided (2+) | 0.064 | 0.75 | 0.25 | 0.00 | 9.23 | 32.9/22.0 | 17.6/25.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Max Sasson: 1+ goals YES | 8 | 0.127 | 0.114 | +0.041 | +0.029 | $6.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 19 | 0.242 | 0.228 | +0.041 | +0.027 | $7.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 62 | 0.686 | 0.667 | +0.049 | +0.030 | $20.00 | FUNDED_RESEARCH | $5 | NYR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 17 | 0.217 | 0.204 | +0.037 | +0.024 | $6.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (21.99 vs 9.64 bp); relationships: KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes has the higher standalone adjusted growth (21.99 vs 9.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT11VANNYR-NYR3|no; why: higher confidence-adjusted growth (8.75 vs 8.33 bp); despite a smaller raw edge (+0.049 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense succeeds (4+ goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes has the higher standalone adjusted growth (21.99 vs 8.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYR shot control · normal event (5-7) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.2992): highest fidelity KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11VANNYR-NYR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3178): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4211): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11VANNYR-NYR3|no (same contract)
- KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4803, phi -0.215)
- KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4803, phi -0.237)
- KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.4662, phi -0.222)
- KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4803, phi -0.226)

portfolios: A EV +6.10 (adj +2.06) on $50.00, P(profit) 0.6131, adj growth 16.3 bp · B EV +7.78 (adj +5.14) on $41.27, P(profit) 0.3815, adj growth 44.3 bp · C EV +7.70 (adj +4.07) on $50.00, P(profit) 0.5887, adj growth 35.2 bp · R EV +0.39 (adj +0.24) on $5.00, P(profit) 0.6858, adj growth 8.5 bp

## CAR @ PHI  ·  10000 joint draws  ·  412 bet sides mapped, 16 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CAR_win | p_overtime | goals | shots PHI/CAR | PHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.147 | 0.41 | 0.59 | 0.00 | 5.94 | 20.4/32.6 | 28.6/17.4 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.135 | 0.49 | 0.51 | 0.46 | 5.87 | 20.4/32.9 | 29.4/17.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.092 | 0.52 | 0.48 | 0.00 | 5.94 | 25.9/26.7 | 23.5/22.3 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.085 | 0.42 | 0.58 | 0.00 | 3.4 | 19.1/31.3 | 29.3/17.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.52 | 0.48 | 0.48 | 5.87 | 25.9/26.7 | 23.5/22.6 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.083 | 0.47 | 0.53 | 0.48 | 2.74 | 19.2/31.0 | 29.5/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Noel Acciari: 1+ goals YES | 8 | 0.128 | 0.115 | +0.043 | +0.030 | $7.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 69 | 0.751 | 0.733 | +0.046 | +0.028 | $20.00 | FUNDED_RESEARCH | $5 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 16 | 0.205 | 0.191 | +0.035 | +0.021 | $6.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Noah Cates: 1+ goals YES | 12 | 0.157 | 0.144 | +0.029 | +0.016 | $4.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT11CARPHI-CAR3|no; why: higher confidence-adjusted growth (23.84 vs 7.76 bp); despite a smaller raw edge (+0.043 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT11CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT11CARPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PHI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT11CARPHI-CAR3|no; why: higher confidence-adjusted growth (8.33 vs 7.76 bp); despite a smaller raw edge (+0.046 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT11CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT11CARPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: CAR offense succeeds (4+ goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT11CARPHI-CAR3|no; why: KXNHLSPREAD-26OCT11CARPHI-CAR3|no has the higher standalone adjusted growth (7.76 vs 7.13 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.105); relationships: KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT11CARPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: PHI offense suppressed (<= 2 goals)
- **Noah Cates: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT11CARPHI-CAR3|no; why: KXNHLSPREAD-26OCT11CARPHI-CAR3|no has the higher standalone adjusted growth (7.76 vs 5.21 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.097); relationships: KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT11CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.09.
- thesis CAR:SUPPRESSED (p 0.4207): highest fidelity KXNHLTEAMTOTAL-26OCT11CARPHI-CAR4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3236): highest fidelity KXNHLTEAMTOTAL-26OCT11CARPHI-PHI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.475): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT11CARPHI-CAR4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4572, phi -0.167)
- KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3578, phi -0.216)
- KXNHLGOAL-26OCT11CARPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4572, phi -0.217)
- KXNHLGOAL-26OCT11CARPHI-PHINCATES27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4572, phi -0.206)

portfolios: A EV +8.27 (adj +1.72) on $50.00, P(profit) 0.6074, adj growth 10.6 bp · B EV +7.14 (adj +4.60) on $37.47, P(profit) 0.3506, adj growth 39.7 bp · C EV +3.20 (adj +1.49) on $40.00, P(profit) 0.6346, adj growth 13.4 bp · R EV +0.32 (adj +0.20) on $5.00, P(profit) 0.7507, adj growth 7.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT11CARPHI-PHI|yes == KXNHLGAME-26OCT11CARPHI-CAR|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
