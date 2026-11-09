# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-09T00:12:54Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +9.92 | +2.67 | -9.49 | 0.424 | -50.00 | -50.00 | 13.97 |
| B thesis-diversified (joint) ← optimiser card | 27.41 | +5.53 | +3.55 | -4.75 | 0.473 | -27.41 | -27.41 | 30.68 |
| C best expression per thesis | 30.00 | +3.29 | +1.57 | +1.02 | 0.643 | -7.38 | -30.00 | 13.98 |
| R FUNDED research stakes | 3.00 | +0.28 | +0.17 | -3.00 | 0.401 | -3.00 | -3.00 | 0.00 |

## PIT @ ANA  ·  10000 joint draws  ·  448 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.523 / away 0.477

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_PIT_win | p_overtime | goals | shots ANA/PIT | ANA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.135 | 0.69 | 0.31 | 0.00 | 9.73 | 29.4/29.2 | 23.9/21.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.70 | 0.30 | 0.00 | 6.09 | 27.4/27.2 | 24.4/22.9 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.096 | 0.77 | 0.23 | 0.00 | 9.58 | 34.3/23.0 | 18.7/25.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.56 | 0.44 | 0.47 | 6.08 | 27.6/27.4 | 24.0/24.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.087 | 0.73 | 0.27 | 0.00 | 6.05 | 32.4/21.5 | 19.0/27.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.58 | 0.42 | 0.47 | 6.01 | 32.6/22.1 | 18.8/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jeff Malott: 1+ goals YES | 11 | 0.156 | 0.143 | +0.039 | +0.027 | $6.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 19 | 0.244 | 0.228 | +0.043 | +0.027 | $8.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 35 | 0.401 | 0.387 | +0.035 | +0.021 | $8.29 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
| Sam Colangelo: 1+ goals YES | 14 | 0.173 | 0.163 | +0.025 | +0.015 | $4.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (14.68 vs 10.10 bp); despite a smaller raw edge (+0.039 vs +0.043/contract); relationships: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV08PITANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV08PITANA-PIT3|no; why: higher confidence-adjusted growth (10.10 vs 7.35 bp); despite a smaller raw edge (+0.043 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV08PITANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: ANA offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (10.10 vs 4.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV08PITANA-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: ANA offense suppressed (<= 2 goals)
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (10.10 vs 3.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.5882): highest fidelity KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:SUPPRESSED (p 0.3996): highest fidelity KXNHLSPREAD-26NOV08PITANA-PIT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.6384): highest fidelity KXNHLSPREAD-26NOV08PITANA-PIT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2252, phi -0.134)
- KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2252, phi -0.175)
- KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2252, phi -0.247)
- KXNHLGOAL-26NOV08PITANA-ANASCOLANGELO12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2252, phi -0.138)

portfolios: A EV +9.92 (adj +2.67) on $50.00, P(profit) 0.4244, adj growth 14.0 bp · B EV +5.53 (adj +3.55) on $27.41, P(profit) 0.4727, adj growth 30.7 bp · C EV +3.29 (adj +1.57) on $30.00, P(profit) 0.6433, adj growth 14.0 bp · R EV +0.28 (adj +0.17) on $3.00, P(profit) 0.4006, adj growth 5.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
