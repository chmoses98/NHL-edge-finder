# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-23T01:30:05Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +20.59 | +4.14 | +27.64 | 0.655 | -46.74 | -63.77 | 28.10 |
| B thesis-diversified (joint) ← optimiser card | 87.48 | +20.84 | +14.00 | +17.37 | 0.585 | -57.00 | -59.27 | 121.67 |
| C best expression per thesis | 66.40 | +12.52 | +7.49 | -17.97 | 0.487 | -45.21 | -45.21 | 64.81 |
| R FUNDED research stakes | 10.00 | +0.66 | +0.42 | +5.02 | 0.504 | -2.60 | -10.00 | 0.00 |

## UTA @ SEA  ·  10000 joint draws  ·  470 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.387 / away 0.613

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_UTA_win | p_overtime | goals | shots SEA/UTA | SEA/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.51 | 0.49 | 0.00 | 6.05 | 27.3/27.7 | 24.1/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.51 | 0.49 | 0.45 | 5.99 | 27.3/27.8 | 24.6/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.49 | 0.51 | 0.00 | 9.34 | 28.9/29.4 | 23.5/22.8 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.098 | 0.42 | 0.58 | 0.00 | 6.01 | 21.5/33.0 | 29.1/18.5 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.46 | 0.54 | 0.47 | 5.96 | 21.6/32.9 | 29.5/18.4 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.077 | 0.39 | 0.61 | 0.00 | 9.26 | 23.1/34.8 | 27.4/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Shane Wright: 1+ goals YES | 15 | 0.205 | 0.189 | +0.046 | +0.030 | $8.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 10 | 0.136 | 0.126 | +0.030 | +0.020 | $4.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 64 | 0.700 | 0.683 | +0.044 | +0.027 | $20.00 | FUNDED_RESEARCH | $5 | UTA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Kaapo Kakko: 1+ goals YES | 15 | 0.189 | 0.178 | +0.030 | +0.019 | $5.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: higher confidence-adjusted growth (14.52 vs 8.60 bp); despite a smaller raw edge (+0.046 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22UTASEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (14.52 vs 8.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT22UTASEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: SEA offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: KXNHLSPREAD-26OCT22UTASEA-UTA3|no has the higher standalone adjusted growth (8.60 vs 7.31 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.152); relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT22UTASEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: UTA offense succeeds (4+ goals)
- **Kaapo Kakko: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes has the higher standalone adjusted growth (14.52 vs 5.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4001): highest fidelity KXNHLTEAMTOTAL-26OCT22UTASEA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4891): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA3|no (same contract)
- thesis UTA:SUPPRESSED (p 0.3607): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA3|no (same contract)
- KXNHLGOAL-26OCT22UTASEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3757, phi -0.222)
- KXNHLGOAL-26OCT22UTASEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3757, phi -0.169)
- KXNHLGOAL-26OCT22UTASEA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4242, phi -0.25)
- KXNHLGOAL-26OCT22UTASEA-SEAKKAKKO84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3757, phi -0.183)

portfolios: A EV +10.23 (adj +2.13) on $50.00, P(profit) 0.5952, adj growth 13.8 bp · B EV +6.09 (adj +3.92) on $38.42, P(profit) 0.4022, adj growth 34.0 bp · C EV +4.66 (adj +2.45) on $47.70, P(profit) 0.8087, adj growth 21.6 bp · R EV +0.33 (adj +0.21) on $5.00, P(profit) 0.6997, adj growth 7.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22UTASEA-UTA|no == KXNHLGAME-26OCT22UTASEA-SEA|yes

## DET @ VAN  ·  10000 joint draws  ·  442 bet sides mapped, 27 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.399 / away 0.601

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_DET_win | p_overtime | goals | shots VAN/DET | VAN/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.117 | 0.52 | 0.48 | 0.00 | 6.05 | 21.8/33.5 | 29.9/18.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.60 | 0.40 | 0.00 | 6.05 | 27.2/27.8 | 24.7/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.46 | 5.94 | 27.5/28.1 | 24.8/24.1 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.50 | 5.91 | 21.8/33.5 | 30.2/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.56 | 0.44 | 0.00 | 9.34 | 29.0/29.5 | 23.7/22.5 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.074 | 0.51 | 0.49 | 0.00 | 9.2 | 23.2/35.2 | 28.7/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Filip Chytil: 1+ goals YES | 18 | 0.270 | 0.246 | +0.080 | +0.056 | $13.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Max Sasson: 1+ goals YES | 10 | 0.165 | 0.147 | +0.059 | +0.041 | $8.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 12 | 0.177 | 0.159 | +0.049 | +0.031 | $7.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Dylan Larkin: 1+ goals NO | 66 | 0.720 | 0.704 | +0.044 | +0.028 | $19.06 | FUNDED_RESEARCH | $5 | DET:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (43.37 vs 21.39 bp); relationships: KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Max Sasson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (43.37 vs 37.32 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: VAN offense suppressed (<= 2 goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (43.37 vs 18.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.023); failure: VAN offense suppressed (<= 2 goals)
- **Dylan Larkin: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes has the higher standalone adjusted growth (9.48 vs 7.81 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.125); relationships: KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: DET offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4129): highest fidelity KXNHLTEAMTOTAL-26OCT22DETVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5383): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.3099): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-DET2|no (same contract)
- KXNHLGOAL-26OCT22DETVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3705, phi -0.246)
- KXNHLGOAL-26OCT22DETVAN-VANMSASSON63-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3705, phi -0.177)
- KXNHLGOAL-26OCT22DETVAN-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3705, phi -0.186)
- KXNHLGOAL-26OCT22DETVAN-DETDLARKIN71-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.358, phi -0.234)

portfolios: A EV +10.37 (adj +2.01) on $50.00, P(profit) 0.6508, adj growth 14.3 bp · B EV +14.74 (adj +10.08) on $49.06, P(profit) 0.4993, adj growth 87.7 bp · C EV +7.86 (adj +5.04) on $18.70, P(profit) 0.3838, adj growth 43.2 bp · R EV +0.33 (adj +0.21) on $5.00, P(profit) 0.7198, adj growth 7.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
