# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-04T01:39:39Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +7.42 | +3.19 | +0.22 | 0.686 | -30.83 | -50.00 | 25.83 |
| B thesis-diversified (joint) ← optimiser card | 33.01 | +5.86 | +3.78 | -9.73 | 0.455 | -33.01 | -33.01 | 32.69 |
| C best expression per thesis | 34.57 | +5.19 | +2.63 | +1.73 | 0.628 | -34.57 | -34.57 | 22.88 |
| R FUNDED research stakes | 4.00 | +0.27 | +0.16 | +2.81 | 0.627 | -4.00 | -4.00 | 0.00 |

## ANA @ VAN  ·  10000 joint draws  ·  422 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.372 / away 0.628

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_ANA_win | p_overtime | goals | shots VAN/ANA | VAN/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.122 | 0.38 | 0.62 | 0.00 | 6.06 | 21.8/33.7 | 29.2/19.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.42 | 0.58 | 0.00 | 6.09 | 27.3/28.0 | 24.1/24.1 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.48 | 0.52 | 0.47 | 5.96 | 22.1/34.1 | 30.7/18.9 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.102 | 0.35 | 0.65 | 0.00 | 9.47 | 22.9/35.4 | 27.8/18.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.44 | 0.56 | 0.00 | 9.57 | 29.0/29.6 | 22.9/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.50 | 0.50 | 0.47 | 6.03 | 27.3/27.9 | 24.6/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Linus Karlsson: 1+ goals YES | 18 | 0.237 | 0.222 | +0.047 | +0.032 | $8.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 19 | 0.241 | 0.227 | +0.040 | +0.026 | $7.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Tom Willander: 1+ goals YES | 4 | 0.061 | 0.055 | +0.018 | +0.012 | $2.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Cutter Gauthier: 1+ goals NO | 57 | 0.627 | 0.610 | +0.040 | +0.023 | $13.67 | FUNDED_RESEARCH | $4 | ANA:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (13.92 vs 9.38 bp); relationships: KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV03ANAVAN-VANTWILLANDER5-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV03ANAVAN-ANACGAUTHIER61-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (13.92 vs 9.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV03ANAVAN-VANTWILLANDER5-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV03ANAVAN-ANACGAUTHIER61-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: VAN offense suppressed (<= 2 goals)
- **Tom Willander: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (13.92 vs 7.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV03ANAVAN-ANACGAUTHIER61-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Cutter Gauthier: 1+ goals NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV03ANAVAN-ANA4|no; why: higher confidence-adjusted growth (4.79 vs 2.86 bp); despite a smaller raw edge (+0.040 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.028 vs 0.91); relationships: KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV03ANAVAN-VANTWILLANDER5-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: ANA offense succeeds (4+ goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.395): highest fidelity KXNHLSPREAD-26NOV03ANAVAN-ANA3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:SUPPRESSED (p 0.3118): highest fidelity KXNHLTEAMTOTAL-26NOV03ANAVAN-ANA4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV03ANAVAN-ANACGAUTHIER61-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.4443): highest fidelity KXNHLSPREAD-26NOV03ANAVAN-ANA3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03ANAVAN-ANA4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV03ANAVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3864, phi -0.221)
- KXNHLGOAL-26NOV03ANAVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3864, phi -0.229)
- KXNHLGOAL-26NOV03ANAVAN-VANTWILLANDER5-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3864, phi -0.108)
- KXNHLGOAL-26NOV03ANAVAN-ANACGAUTHIER61-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.4842, phi -0.272)

portfolios: A EV +7.42 (adj +3.19) on $50.00, P(profit) 0.6861, adj growth 25.8 bp · B EV +5.86 (adj +3.78) on $33.01, P(profit) 0.4545, adj growth 32.7 bp · C EV +5.19 (adj +2.63) on $34.57, P(profit) 0.6282, adj growth 22.9 bp · R EV +0.27 (adj +0.16) on $4.00, P(profit) 0.6269, adj growth 5.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
