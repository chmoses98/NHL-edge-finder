# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-11T11:22:49Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +29.63 | +6.80 | +26.34 | 0.635 | -60.22 | -86.34 | 42.10 |
| B thesis-diversified (joint) ← optimiser card | 71.35 | +20.38 | +11.64 | +11.71 | 0.588 | -44.45 | -44.45 | 99.62 |
| C best expression per thesis | 72.89 | +12.61 | +6.06 | +0.49 | 0.601 | -26.40 | -46.00 | 52.91 |
| R FUNDED research stakes | 10.00 | +3.42 | +2.10 | -3.28 | 0.418 | -10.00 | -10.00 | 0.00 |

## SEA @ WSH  ·  10000 joint draws  ·  444 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_SEA_win | p_overtime | goals | shots WSH/SEA | WSH/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.60 | 0.40 | 0.00 | 6.04 | 27.5/27.1 | 24.0/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.48 | 5.93 | 27.4/27.3 | 24.0/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.60 | 0.40 | 0.00 | 9.29 | 29.3/28.9 | 23.5/22.7 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.092 | 0.65 | 0.35 | 0.00 | 6.02 | 32.5/21.7 | 19.0/28.2 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.56 | 0.44 | 0.49 | 5.93 | 32.8/21.7 | 18.5/29.4 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.072 | 0.66 | 0.34 | 0.00 | 9.32 | 34.6/23.0 | 18.3/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Shane Wright: 2+ goals YES | 1 | 0.025 | 0.021 | +0.015 | +0.011 | $1.70 | FUNDED_RESEARCH | $1 | SEA:OFFENSE_4PLUS | FRAGILE (0.06) | EVIDENCE_STRONGER | D |
| Shane Wright: 1+ goals YES | 14 | 0.193 | 0.175 | +0.045 | +0.026 | $5.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 9 | 0.136 | 0.116 | +0.041 | +0.020 | $4.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Matty Beniers: 1+ goals YES | 18 | 0.230 | 0.216 | +0.040 | +0.026 | $7.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Shane Wright: 2+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes; why: higher confidence-adjusted growth (21.30 vs 11.99 bp); despite a smaller raw edge (+0.015 vs +0.045/contract); relationships: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: DUPLICATIVE (phi 0.328); KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT11SEAWSH-SEAMBENIERS10-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: SEA offense suppressed (<= 2 goals)
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11SEAWSH-SEAMBENIERS10-1|yes; why: higher confidence-adjusted growth (11.99 vs 9.31 bp); relationships: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-2|yes: DUPLICATIVE (phi 0.328); KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT11SEAWSH-SEAMBENIERS10-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (11.99 vs 10.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-2|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT11SEAWSH-SEAMBENIERS10-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: SEA offense suppressed (<= 2 goals)
- **Matty Beniers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (11.99 vs 9.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-2|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.3515): highest fidelity KXNHLTEAMTOTAL-26OCT11SEAWSH-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4296): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11SEAWSH-WSH2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2288): highest fidelity KXNHLSPREAD-26OCT11SEAWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11SEAWSH-WSH2|no (same contract)
- KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 94% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4298, phi -0.127)
- KXNHLGOAL-26OCT11SEAWSH-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4298, phi -0.22)
- KXNHLGOAL-26OCT11SEAWSH-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4298, phi -0.177)
- KXNHLGOAL-26OCT11SEAWSH-SEAMBENIERS10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4298, phi -0.214)

portfolios: A EV +8.70 (adj +1.70) on $50.00, P(profit) 0.5781, adj growth 10.8 bp · B EV +7.36 (adj +4.60) on $18.90, P(profit) 0.4637, adj growth 38.6 bp · C EV +3.97 (adj +1.90) on $24.10, P(profit) 0.2886, adj growth 16.4 bp · R EV +1.36 (adj +1.00) on $1.00, P(profit) 0.0252, adj growth 26.1 bp

## VAN @ NYR  ·  10000 joint draws  ·  384 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_VAN_win | p_overtime | goals | shots NYR/VAN | NYR/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.61 | 0.39 | 0.00 | 5.99 | 26.7/26.5 | 23.4/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.48 | 5.96 | 26.8/26.6 | 23.3/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.60 | 0.40 | 0.00 | 9.27 | 28.1/27.8 | 22.6/21.5 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.092 | 0.71 | 0.29 | 0.00 | 6.0 | 31.3/20.8 | 18.3/26.7 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.55 | 0.45 | 0.50 | 5.97 | 31.7/21.1 | 17.9/28.3 | even strength |
| NYR shot control · high event (8+) · decided (2+) | 0.060 | 0.70 | 0.30 | 0.00 | 9.22 | 33.0/22.2 | 17.6/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 13 | 0.194 | 0.174 | +0.056 | +0.036 | $9.31 | FUNDED_RESEARCH | $3 | VAN:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 9 | 0.134 | 0.118 | +0.039 | +0.023 | $5.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 20 | 0.252 | 0.234 | +0.041 | +0.023 | $6.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Arshdeep Bains: 1+ goals YES | 7 | 0.095 | 0.085 | +0.021 | +0.011 | $2.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes; why: higher confidence-adjusted growth (23.29 vs 9.08 bp); despite a smaller raw edge (+0.056 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT11VANNYR-VANABAINS13-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: VAN offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (23.29 vs 12.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT11VANNYR-VANABAINS13-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (23.29 vs 6.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT11VANNYR-VANABAINS13-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: VAN offense suppressed (<= 2 goals)
- **Arshdeep Bains: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (23.29 vs 3.60 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VAN:OFFENSE_4PLUS (p 0.3451): highest fidelity KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.4269): highest fidelity KXNHLSPREAD-26OCT11VANNYR-NYR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2807): highest fidelity KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2|yes (same contract)
- KXNHLGOAL-26OCT11VANNYR-VANDOCONNOR18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4371, phi -0.22)
- KXNHLGOAL-26OCT11VANNYR-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4371, phi -0.182)
- KXNHLGOAL-26OCT11VANNYR-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4371, phi -0.231)
- KXNHLGOAL-26OCT11VANNYR-VANABAINS13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4371, phi -0.138)

portfolios: A EV +11.77 (adj +2.10) on $50.00, P(profit) 0.5377, adj growth 11.9 bp · B EV +7.97 (adj +4.81) on $24.09, P(profit) 0.5285, adj growth 41.3 bp · C EV +6.48 (adj +3.33) on $28.79, P(profit) 0.3442, adj growth 28.7 bp · R EV +1.21 (adj +0.78) on $3.00, P(profit) 0.1936, adj growth 25.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT11VANNYR-VAN|yes == KXNHLGAME-26OCT11VANNYR-NYR|no

## CAR @ PHI  ·  10000 joint draws  ·  412 bet sides mapped, 7 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CAR_win | p_overtime | goals | shots PHI/CAR | PHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.151 | 0.43 | 0.57 | 0.00 | 5.97 | 20.4/32.6 | 28.7/17.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.137 | 0.47 | 0.53 | 0.50 | 5.89 | 20.4/32.7 | 29.3/17.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.53 | 0.47 | 0.00 | 5.99 | 25.8/26.5 | 23.3/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.48 | 0.52 | 0.47 | 5.94 | 26.2/27.0 | 23.7/23.1 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.086 | 0.43 | 0.57 | 0.00 | 9.16 | 21.8/34.5 | 27.5/16.7 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.079 | 0.45 | 0.55 | 0.47 | 2.81 | 19.4/31.3 | 29.7/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 2.5 goals NO | 73 | 0.824 | 0.775 | +0.080 | +0.031 | $20.00 | FUNDED_RESEARCH | $5 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Noel Acciari: 1+ goals YES | 9 | 0.132 | 0.117 | +0.036 | +0.021 | $4.38 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Philadelphia wins by over 1.5 goals YES | 19 | 0.263 | 0.224 | +0.062 | +0.023 | $3.98 | FUNDED_RESEARCH | $1 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT11CARPHI-PHI2|yes; why: higher confidence-adjusted growth (11.00 vs 7.16 bp); wins across more scripts (relative breadth 1.019 vs 0.55); relationships: KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.089); KXNHLSPREAD-26OCT11CARPHI-PHI2|yes: REINFORCING (phi 0.276); failure: CAR wins by 2+
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT11CARPHI-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT11CARPHI-CAR3|no has the higher standalone adjusted growth (11.00 vs 10.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.089); they share one thesis budget; relationships: KXNHLSPREAD-26OCT11CARPHI-CAR3|no: MOSTLY_INDEPENDENT (phi 0.089); KXNHLSPREAD-26OCT11CARPHI-PHI2|yes: MOSTLY_INDEPENDENT (phi 0.149); failure: PHI offense suppressed (<= 2 goals)
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLSPREAD-26OCT11CARPHI-CAR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT11CARPHI-CAR3|no has the higher standalone adjusted growth (11.00 vs 7.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.276); they share one thesis budget; relationships: KXNHLSPREAD-26OCT11CARPHI-CAR3|no: REINFORCING (phi 0.276); KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.149); failure: CAR wins (incl. OT/SO)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:WINS (p 0.478): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR3|no (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3491): highest fidelity KXNHLTEAMTOTAL-26OCT11CARPHI-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2626): highest fidelity KXNHLSPREAD-26OCT11CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT11CARPHI-CAR3|no (same contract)
- KXNHLSPREAD-26OCT11CARPHI-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2868, phi -0.728)
- KXNHLGOAL-26OCT11CARPHI-PHINACCIARI52-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4303, phi -0.183)
- KXNHLSPREAD-26OCT11CARPHI-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.522, phi -0.624)

portfolios: A EV +9.17 (adj +3.00) on $50.00, P(profit) 0.2626, adj growth 19.5 bp · B EV +5.05 (adj +2.23) on $28.36, P(profit) 0.3377, adj growth 19.7 bp · C EV +2.16 (adj +0.83) on $20.00, P(profit) 0.8242, adj growth 7.8 bp · R EV +0.85 (adj +0.32) on $6.00, P(profit) 0.8242, adj growth 11.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
