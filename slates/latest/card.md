# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-01T01:38:04Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +11.86 | +3.04 | +5.27 | 0.610 | -50.00 | -50.00 | 19.16 |
| B thesis-diversified (joint) ← optimiser card | 41.92 | +6.38 | +3.17 | +2.36 | 0.668 | -24.53 | -24.53 | 28.27 |
| C best expression per thesis | 23.91 | +5.19 | +2.15 | -0.45 | 0.380 | -23.91 | -23.91 | 18.58 |
| R FUNDED research stakes | 7.00 | +1.08 | +0.53 | -0.28 | 0.283 | -7.00 | -7.00 | 0.00 |

## CGY @ COL  ·  10000 joint draws  ·  466 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.769 / away 0.231

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_CGY_win | p_overtime | goals | shots COL/CGY | COL/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.156 | 0.81 | 0.19 | 0.00 | 6.02 | 35.6/22.7 | 20.6/30.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.119 | 0.83 | 0.17 | 0.00 | 9.37 | 37.8/24.3 | 20.4/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.78 | 0.22 | 0.00 | 6.04 | 29.7/28.9 | 26.5/24.7 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.60 | 0.40 | 0.47 | 5.95 | 36.6/23.2 | 20.2/33.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.74 | 0.26 | 0.00 | 9.38 | 31.3/30.4 | 25.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.56 | 0.44 | 0.51 | 5.99 | 30.0/29.1 | 25.8/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cale Makar: 1+ goals NO | 73 | 0.803 | 0.783 | +0.059 | +0.040 | $20.00 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 14 | 0.187 | 0.174 | +0.038 | +0.025 | $5.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Calgary over 3.5 goals scored YES | 20 | 0.283 | 0.239 | +0.072 | +0.028 | $6.57 | FUNDED_RESEARCH | $2 | CGY:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mackenzie Blackwood: 22+ saves YES | 53 | 0.608 | 0.561 | +0.060 | +0.014 | $9.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:NET_HIGH_VOLUME | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL2|no; why: higher confidence-adjusted growth (18.32 vs 3.41 bp); despite a smaller raw edge (+0.059 vs +0.097/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.022 vs 0.86); relationships: KXNHLGOAL-26OCT31CGYCOL-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLSAVE-26OCT31CGYCOL-COLMBLACKWOOD39-22|yes: MOSTLY_INDEPENDENT (phi -0.027); failure: COL offense succeeds (4+ goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes; why: higher confidence-adjusted growth (11.00 vs 10.00 bp); despite a smaller raw edge (+0.038 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.988 vs 0.803); relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: REINFORCING (phi 0.208); KXNHLSAVE-26OCT31CGYCOL-COLMBLACKWOOD39-22|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: CGY offense suppressed (<= 2 goals)
- **Calgary over 3.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CGYCOL-CGYASUNIEV61-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CGYCOL-CGYASUNIEV61-1|yes has the higher standalone adjusted growth (11.00 vs 10.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.208); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT31CGYCOL-CGYASUNIEV61-1|yes: REINFORCING (phi 0.208); KXNHLSAVE-26OCT31CGYCOL-COLMBLACKWOOD39-22|yes: INTENTIONAL_DIVERSIFIER (phi -0.097); failure: CGY offense suppressed (<= 2 goals)
- **Mackenzie Blackwood: 22+ saves YES** — thesis: COL net faces heavy volume (33+ shots; CGY pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT31CGYCOL-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: INTENTIONAL_DIVERSIFIER (phi -0.097); failure: COL net faces light volume (<= 25 shots; CGY suppressed)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.16, COL shot control · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CGY:OFFENSE_4PLUS (p 0.2746): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes (same contract)
- thesis CGY:WINS (p 0.3041): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.3862): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5689, phi -0.172)
- KXNHLGOAL-26OCT31CGYCOL-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5111, phi -0.202)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:SUPPRESSED (p 0.5111, phi -0.642)
- KXNHLSAVE-26OCT31CGYCOL-COLMBLACKWOOD39-22|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family MIXED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:NET_LOW_VOLUME (p 0.4633, phi -0.726)

portfolios: A EV +11.86 (adj +3.04) on $50.00, P(profit) 0.6101, adj growth 19.2 bp · B EV +6.38 (adj +3.17) on $41.92, P(profit) 0.6684, adj growth 28.3 bp · C EV +5.19 (adj +2.15) on $23.91, P(profit) 0.3804, adj growth 18.6 bp · R EV +1.08 (adj +0.53) on $7.00, P(profit) 0.2829, adj growth 19.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
