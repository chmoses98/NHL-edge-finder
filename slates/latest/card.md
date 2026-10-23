# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-23T01:51:55Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +20.39 | +3.63 | +16.66 | 0.678 | -45.79 | -65.43 | 23.61 |
| B thesis-diversified (joint) ← optimiser card | 88.01 | +19.98 | +13.44 | +15.04 | 0.615 | -57.53 | -61.29 | 117.67 |
| C best expression per thesis | 69.97 | +11.77 | +6.77 | -6.90 | 0.453 | -30.92 | -47.51 | 59.13 |
| R FUNDED research stakes | 10.00 | +0.67 | +0.41 | +5.02 | 0.504 | -2.60 | -10.00 | 0.00 |

## UTA @ SEA  ·  10000 joint draws  ·  474 bet sides mapped, 25 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.385 / away 0.616

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_UTA_win | p_overtime | goals | shots SEA/UTA | SEA/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.50 | 0.50 | 0.00 | 6.01 | 27.4/27.9 | 24.4/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.46 | 5.97 | 27.6/27.9 | 24.6/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.52 | 0.48 | 0.00 | 9.43 | 28.9/29.4 | 23.4/22.8 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.102 | 0.45 | 0.55 | 0.00 | 6.03 | 21.8/32.8 | 28.8/18.7 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.46 | 0.54 | 0.46 | 5.9 | 21.7/33.2 | 30.1/18.6 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.078 | 0.39 | 0.61 | 0.00 | 9.38 | 23.1/34.3 | 27.1/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Shane Wright: 1+ goals YES | 15 | 0.200 | 0.186 | +0.041 | +0.027 | $7.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 10 | 0.140 | 0.129 | +0.034 | +0.023 | $5.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 15 | 0.194 | 0.182 | +0.035 | +0.023 | $6.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 64 | 0.702 | 0.685 | +0.046 | +0.029 | $20.00 | FUNDED_RESEARCH | $5 | UTA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22UTASEA-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (11.96 vs 8.79 bp); relationships: KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT22UTASEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22UTASEA-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (11.58 vs 8.79 bp); despite a smaller raw edge (+0.034 vs +0.040/contract); relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT22UTASEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22UTASEA-SEAFGAUDREAU89-1|yes; why: KXNHLGOAL-26OCT22UTASEA-SEAFGAUDREAU89-1|yes has the higher standalone adjusted growth (8.79 vs 8.52 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.026); relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: SEA offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: higher confidence-adjusted growth (8.43 vs 8.01 bp); despite a smaller raw edge (+0.046 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT22UTASEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4061): highest fidelity KXNHLTEAMTOTAL-26OCT22UTASEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.3601): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4833): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA3|no (same contract)
- KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3841, phi -0.182)
- KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3841, phi -0.166)
- KXNHLGOAL-26OCT22UTASEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3841, phi -0.211)
- KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4223, phi -0.256)

portfolios: A EV +10.94 (adj +1.87) on $50.00, P(profit) 0.608, adj growth 11.9 bp · B EV +6.68 (adj +4.38) on $39.96, P(profit) 0.4483, adj growth 38.1 bp · C EV +4.22 (adj +2.04) on $50.00, P(profit) 0.6218, adj growth 18.6 bp · R EV +0.35 (adj +0.22) on $5.00, P(profit) 0.7024, adj growth 8.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22UTASEA-UTA|no == KXNHLGAME-26OCT22UTASEA-SEA|yes

## DET @ VAN  ·  10000 joint draws  ·  442 bet sides mapped, 27 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.399 / away 0.601

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_DET_win | p_overtime | goals | shots VAN/DET | VAN/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.114 | 0.51 | 0.49 | 0.00 | 5.98 | 21.8/33.6 | 29.9/18.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.55 | 0.45 | 0.00 | 6.01 | 27.4/27.9 | 24.5/23.4 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.47 | 0.53 | 0.46 | 5.94 | 21.7/33.4 | 30.0/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.53 | 0.47 | 0.46 | 5.97 | 27.6/28.2 | 24.8/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.58 | 0.42 | 0.00 | 9.28 | 28.8/29.4 | 24.0/22.3 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.072 | 0.48 | 0.52 | 0.00 | 9.22 | 23.0/35.2 | 28.3/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Filip Chytil: 1+ goals YES | 18 | 0.267 | 0.244 | +0.077 | +0.054 | $12.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 10 | 0.166 | 0.147 | +0.060 | +0.041 | $8.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 19 | 0.255 | 0.238 | +0.054 | +0.037 | $9.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Dylan Larkin: 1+ goals NO | 66 | 0.719 | 0.701 | +0.043 | +0.026 | $18.05 | FUNDED_RESEARCH | $5 | DET:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (39.77 vs 18.25 bp); relationships: KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (39.77 vs 36.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (39.77 vs 18.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: VAN offense suppressed (<= 2 goals)
- **Dylan Larkin: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes; why: KXNHLSPREAD-26OCT22DETVAN-VAN2|yes has the higher standalone adjusted growth (9.59 vs 6.61 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.159); relationships: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: DET offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.4079): highest fidelity KXNHLTEAMTOTAL-26OCT22DETVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5261): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.3052): highest fidelity KXNHLSPREAD-26OCT22DETVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-VAN2|yes (same contract)
- KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3666, phi -0.236)
- KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3666, phi -0.179)
- KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3666, phi -0.219)
- KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3717, phi -0.261)

portfolios: A EV +9.45 (adj +1.76) on $50.00, P(profit) 0.6368, adj growth 11.7 bp · B EV +13.30 (adj +9.06) on $48.05, P(profit) 0.5019, adj growth 79.6 bp · C EV +7.55 (adj +4.73) on $19.97, P(profit) 0.4566, adj growth 40.6 bp · R EV +0.32 (adj +0.19) on $5.00, P(profit) 0.7185, adj growth 6.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
