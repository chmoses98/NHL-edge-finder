# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-11T12:22:49Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +23.08 | +9.72 | +20.06 | 0.616 | -63.26 | -85.47 | 73.32 |
| B thesis-diversified (joint) ← optimiser card | 100.58 | +20.65 | +12.64 | +17.88 | 0.609 | -45.32 | -72.21 | 109.19 |
| C best expression per thesis | 101.59 | +13.95 | +7.59 | +7.00 | 0.586 | -40.16 | -48.49 | 66.05 |
| R FUNDED research stakes | 15.00 | +2.62 | +1.60 | -1.19 | 0.329 | -8.28 | -8.28 | 0.00 |

## SEA @ WSH  ·  10000 joint draws  ·  444 bet sides mapped, 9 +EV candidates, 4 on card


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
| Shane Wright: 1+ goals YES | 13 | 0.192 | 0.175 | +0.054 | +0.037 | $9.64 | FUNDED_RESEARCH | $3 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 9 | 0.136 | 0.122 | +0.040 | +0.026 | $6.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 20 | 0.247 | 0.233 | +0.036 | +0.022 | $6.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 9 | 0.117 | 0.110 | +0.021 | +0.014 | $3.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT11SEAWSH-WSH2|no; why: higher confidence-adjusted growth (24.68 vs 5.65 bp); despite a smaller raw edge (+0.054 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT11SEAWSH-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (24.68 vs 16.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT11SEAWSH-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT11SEAWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (6.26 vs 0.98 bp); despite a smaller raw edge (+0.036 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT11SEAWSH-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: WSH offense suppressed (<= 2 goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (24.68 vs 4.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.3404): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.4352): highest fidelity KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes (same contract)
- thesis GAME:TIGHT (p 0.4379): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11SEAWSH-WSH2|no (same contract)
- KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4455, phi -0.233)
- KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4455, phi -0.178)
- KXNHLGOAL-26OCT11SEAWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3473, phi -0.24)
- KXNHLGOAL-26OCT11SEAWSH-SEAFGAUDREAU89-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4455, phi -0.179)

portfolios: A EV +11.11 (adj +6.46) on $50.00, P(profit) 0.3, adj growth 51.4 bp · B EV +8.31 (adj +5.53) on $26.25, P(profit) 0.5367, adj growth 47.4 bp · C EV +7.00 (adj +4.01) on $33.81, P(profit) 0.3935, adj growth 34.6 bp · R EV +1.17 (adj +0.81) on $3.00, P(profit) 0.1917, adj growth 26.6 bp

## VAN @ NYR  ·  10000 joint draws  ·  384 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_VAN_win | p_overtime | goals | shots NYR/VAN | NYR/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.65 | 0.35 | 0.00 | 6.04 | 26.4/26.3 | 23.5/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.54 | 0.46 | 0.50 | 5.96 | 26.5/26.4 | 23.1/23.1 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.096 | 0.72 | 0.28 | 0.00 | 5.98 | 31.8/21.1 | 18.7/27.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.68 | 0.32 | 0.00 | 9.32 | 28.3/28.2 | 23.0/21.1 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.59 | 0.41 | 0.48 | 5.87 | 31.5/21.0 | 17.9/28.1 | even strength |
| NYR shot control · high event (8+) · decided (2+) | 0.059 | 0.76 | 0.24 | 0.00 | 9.22 | 33.3/22.1 | 17.9/25.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 13 | 0.183 | 0.167 | +0.045 | +0.029 | $7.75 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 18 | 0.238 | 0.221 | +0.048 | +0.031 | $8.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 17 | 0.213 | 0.201 | +0.033 | +0.021 | $6.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 9 | 0.121 | 0.108 | +0.026 | +0.013 | $3.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (15.19 vs 13.42 bp); despite a smaller raw edge (+0.045 vs +0.048/contract); relationships: KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (15.19 vs 13.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (15.19 vs 6.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: VAN offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (15.19 vs 4.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYR shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3026): highest fidelity KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.3888): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3247): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11VANNYR-NYRPDOROFEYEV16-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4824, phi -0.217)
- KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4824, phi -0.238)
- KXNHLGOAL-26OCT11VANNYR-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4824, phi -0.236)
- KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4824, phi -0.195)

portfolios: A EV +6.05 (adj +1.34) on $50.00, P(profit) 0.6217, adj growth 9.1 bp · B EV +6.75 (adj +4.23) on $26.00, P(profit) 0.5712, adj growth 36.6 bp · C EV +3.76 (adj +2.09) on $27.78, P(profit) 0.4478, adj growth 18.0 bp · R EV +0.65 (adj +0.42) on $2.00, P(profit) 0.1826, adj growth 14.4 bp

## CAR @ PHI  ·  10000 joint draws  ·  412 bet sides mapped, 12 +EV candidates, 4 on card


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
| Noel Acciari: 1+ goals YES | 9 | 0.128 | 0.115 | +0.032 | +0.019 | $4.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 69 | 0.751 | 0.733 | +0.046 | +0.028 | $20.00 | FUNDED_RESEARCH | $5 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 73 | 0.814 | 0.770 | +0.071 | +0.026 | $20.00 | FUNDED_RESEARCH | $5 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Noah Cates: 1+ goals YES | 12 | 0.157 | 0.144 | +0.029 | +0.016 | $3.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT11CARPHI-CAR3|no; why: higher confidence-adjusted growth (9.02 vs 7.76 bp); despite a smaller raw edge (+0.032 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26OCT11CARPHI-CAR3|no: MOSTLY_INDEPENDENT (phi 0.085); KXNHLGOAL-26OCT11CARPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PHI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT11CARPHI-CAR3|no; why: higher confidence-adjusted growth (8.33 vs 7.76 bp); despite a smaller raw edge (+0.046 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26OCT11CARPHI-CAR3|no: MOSTLY_INDEPENDENT (phi 0.138); KXNHLGOAL-26OCT11CARPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: CAR offense succeeds (4+ goals)
- **Carolina wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT11CARPHI-CAR2|no; why: higher confidence-adjusted growth (7.76 vs 6.32 bp); despite a smaller raw edge (+0.071 vs +0.073/contract); relationships: KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.085); KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.138); KXNHLGOAL-26OCT11CARPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.097); failure: CAR wins by 2+
- **Noah Cates: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT11CARPHI-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT11CARPHI-CAR3|no has the higher standalone adjusted growth (7.76 vs 5.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.097); they share one thesis budget; relationships: KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26OCT11CARPHI-CAR3|no: MOSTLY_INDEPENDENT (phi 0.097); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.09.
- thesis CAR:SUPPRESSED (p 0.4207): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3236): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.475): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR2|no (same contract)
- KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4572, phi -0.167)
- KXNHLGOAL-26OCT11CARPHI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3578, phi -0.216)
- KXNHLSPREAD-26OCT11CARPHI-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2998, phi -0.73)
- KXNHLGOAL-26OCT11CARPHI-PHINCATES27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4572, phi -0.206)

portfolios: A EV +5.92 (adj +1.92) on $50.00, P(profit) 0.5726, adj growth 12.8 bp · B EV +5.59 (adj +2.88) on $48.33, P(profit) 0.7057, adj growth 25.2 bp · C EV +3.20 (adj +1.49) on $40.00, P(profit) 0.6346, adj growth 13.4 bp · R EV +0.80 (adj +0.37) on $10.00, P(profit) 0.6346, adj growth 13.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
