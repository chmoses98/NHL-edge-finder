# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-11T15:11:58Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +25.04 | +5.37 | +25.67 | 0.663 | -49.73 | -68.97 | 38.82 |
| B thesis-diversified (joint) ← optimiser card | 128.46 | +22.12 | +13.53 | +16.43 | 0.605 | -49.68 | -64.25 | 117.77 |
| C best expression per thesis | 100.04 | +14.48 | +7.65 | +15.26 | 0.573 | -43.11 | -44.77 | 66.60 |
| R FUNDED research stakes | 19.00 | +2.35 | +1.24 | -0.09 | 0.486 | -7.95 | -11.14 | 0.00 |

## SEA @ WSH  ·  10000 joint draws  ·  450 bet sides mapped, 10 +EV candidates, 4 on card


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
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT11SEAWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (6.99 vs 1.79 bp); despite a smaller raw edge (+0.036 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26OCT11SEAWSH-WSH2|no: INTENTIONAL_DIVERSIFIER (phi -0.237); failure: WSH offense suppressed (<= 2 goals)
- **Washington wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH3|no; why: higher confidence-adjusted growth (5.65 vs 4.25 bp); relationships: KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.115); KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.137); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.237); failure: WSH wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.3404): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.4352): highest fidelity KXNHLAST-26OCT11SEAWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4379): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11SEAWSH-WSH2|no (same contract)
- KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4455, phi -0.178)
- KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4455, phi -0.233)
- KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3473, phi -0.24)
- KXNHLSPREAD-26OCT11SEAWSH-WSH2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:WINS_BY_2PLUS (p 0.3407, phi -1.0)

portfolios: A EV +8.06 (adj +1.75) on $50.00, P(profit) 0.7254, adj growth 13.9 bp · B EV +7.87 (adj +4.59) on $36.56, P(profit) 0.4753, adj growth 39.6 bp · C EV +5.76 (adj +3.12) on $33.54, P(profit) 0.3935, adj growth 27.0 bp · R EV +1.33 (adj +0.71) on $6.00, P(profit) 0.6869, adj growth 23.4 bp

## VAN @ NYR  ·  10000 joint draws  ·  390 bet sides mapped, 14 +EV candidates, 4 on card


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
| Max Sasson: 1+ goals YES | 8 | 0.127 | 0.114 | +0.041 | +0.029 | $6.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Drew O'Connor: 1+ goals YES | 13 | 0.179 | 0.166 | +0.042 | +0.028 | $7.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 19 | 0.242 | 0.228 | +0.041 | +0.027 | $7.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 62 | 0.686 | 0.666 | +0.049 | +0.029 | $19.75 | FUNDED_RESEARCH | $5 | NYR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (21.99 vs 9.64 bp); relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: VAN offense suppressed (<= 2 goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes has the higher standalone adjusted growth (21.99 vs 14.10 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes has the higher standalone adjusted growth (21.99 vs 9.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT11VANNYR-NYR3|no; why: KXNHLSPREAD-26OCT11VANNYR-NYR3|no has the higher standalone adjusted growth (8.33 vs 8.04 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.144); relationships: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYR shot control · normal event (5-7) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.2992): highest fidelity KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11VANNYR-NYR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4211): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11VANNYR-NYR3|no (same contract)
- thesis NYR:SUPPRESSED (p 0.3178): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4803, phi -0.215)
- KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4803, phi -0.21)
- KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4803, phi -0.237)
- KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.4662, phi -0.222)

portfolios: A EV +6.48 (adj +1.73) on $50.00, P(profit) 0.591, adj growth 12.5 bp · B EV +8.68 (adj +5.73) on $41.90, P(profit) 0.4039, adj growth 49.3 bp · C EV +5.53 (adj +3.04) on $26.50, P(profit) 0.7631, adj growth 26.1 bp · R EV +0.39 (adj +0.23) on $5.00, P(profit) 0.6858, adj growth 8.1 bp

## CAR @ PHI  ·  10000 joint draws  ·  426 bet sides mapped, 19 +EV candidates, 4 on card


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
| Noel Acciari: 1+ goals YES | 8 | 0.128 | 0.115 | +0.043 | +0.030 | $4.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 69 | 0.751 | 0.733 | +0.046 | +0.028 | $15.73 | FUNDED_RESEARCH | $4 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 73 | 0.814 | 0.770 | +0.071 | +0.026 | $15.71 | FUNDED_RESEARCH | $4 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikolaj Ehlers: 1+ goals NO | 76 | 0.807 | 0.791 | +0.034 | +0.018 | $13.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT11CARPHI-CAR3|no; why: higher confidence-adjusted growth (23.84 vs 7.76 bp); despite a smaller raw edge (+0.043 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26OCT11CARPHI-CAR3|no: MOSTLY_INDEPENDENT (phi 0.085); KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT11CARPHI-CAR3|no; why: higher confidence-adjusted growth (8.33 vs 7.76 bp); despite a smaller raw edge (+0.046 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26OCT11CARPHI-CAR3|no: MOSTLY_INDEPENDENT (phi 0.138); KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: CAR offense succeeds (4+ goals)
- **Carolina wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT11CARPHI-CAR3|no; why: higher confidence-adjusted growth (7.76 vs 6.87 bp); despite a smaller raw edge (+0.071 vs +0.073/contract); wins across more scripts (relative breadth 1.002 vs 0.779); relationships: KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.085); KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.138); KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.136); failure: CAR wins by 2+
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no; why: Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over broad KXNHLTEAMTOTAL-26OCT11CARPHI-CAR4|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.90 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLSPREAD-26OCT11CARPHI-CAR3|no: MOSTLY_INDEPENDENT (phi 0.136); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.09.
- thesis CAR:SUPPRESSED (p 0.4207): highest fidelity KXNHLTEAMTOTAL-26OCT11CARPHI-CAR4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no — Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over broad KXNHLTEAMTOTAL-26OCT11CARPHI-CAR4|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.90 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PHI:OFFENSE_4PLUS (p 0.3236): highest fidelity KXNHLTEAMTOTAL-26OCT11CARPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.475): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT11CARPHI-CAR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4572, phi -0.167)
- KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3578, phi -0.216)
- KXNHLSPREAD-26OCT11CARPHI-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2998, phi -0.73)
- KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3578, phi -0.208)
- override: Player prop expression KXNHLGOAL-26OCT11CARPHI-CARNEHLERS27-1|no selected over broad KXNHLTEAMTOTAL-26OCT11CARPHI-CAR4|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.90 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +10.50 (adj +1.89) on $50.00, P(profit) 0.5731, adj growth 12.5 bp · B EV +5.58 (adj +3.21) on $50.00, P(profit) 0.5806, adj growth 28.9 bp · C EV +3.20 (adj +1.49) on $40.00, P(profit) 0.6346, adj growth 13.4 bp · R EV +0.64 (adj +0.30) on $8.00, P(profit) 0.6346, adj growth 11.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT11CARPHI-PHI|yes == KXNHLGAME-26OCT11CARPHI-CAR|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
