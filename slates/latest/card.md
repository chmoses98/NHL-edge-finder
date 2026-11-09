# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-09T00:39:06Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +13.86 | +4.41 | -31.98 | 0.462 | -50.00 | -50.00 | 23.69 |
| B thesis-diversified (joint) ← optimiser card | 36.87 | +6.19 | +3.08 | -2.37 | 0.402 | -26.46 | -36.87 | 26.69 |
| C best expression per thesis | 10.04 | +3.51 | +1.37 | -10.04 | 0.365 | -10.04 | -10.04 | 11.87 |
| R FUNDED research stakes | 8.00 | +1.11 | +0.44 | +0.75 | 0.522 | -5.27 | -8.00 | 0.00 |

## PIT @ ANA  ·  10000 joint draws  ·  442 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.523 / away 0.477

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_PIT_win | p_overtime | goals | shots ANA/PIT | ANA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.143 | 0.69 | 0.31 | 0.00 | 9.61 | 29.1/28.9 | 23.7/21.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.70 | 0.30 | 0.00 | 6.12 | 27.7/27.5 | 24.7/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.53 | 0.47 | 0.47 | 6.06 | 27.8/27.6 | 24.2/24.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.094 | 0.77 | 0.23 | 0.00 | 9.65 | 34.3/23.1 | 18.8/25.5 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.091 | 0.71 | 0.29 | 0.00 | 6.12 | 32.2/21.4 | 18.8/27.4 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.61 | 0.39 | 0.46 | 6.02 | 32.9/22.1 | 18.9/29.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jeff Malott: 1+ goals YES | 11 | 0.158 | 0.144 | +0.041 | +0.028 | $6.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Anaheim wins by over 2.5 goals YES | 22 | 0.313 | 0.264 | +0.081 | +0.032 | $6.69 | FUNDED_RESEARCH | $2 | ANA:WINS_BY_2PLUS | DIRECT (0.72) | EVIDENCE_MIXED | D |
| Pittsburgh wins by over 2.5 goals NO | 82 | 0.886 | 0.851 | +0.056 | +0.020 | $20.00 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Beckett Sennecke: 1+ goals YES | 35 | 0.395 | 0.382 | +0.029 | +0.016 | $3.81 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV08PITANA-ANA3|yes; why: higher confidence-adjusted growth (15.68 vs 12.38 bp); despite a smaller raw edge (+0.041 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.803 vs 0.477); relationships: KXNHLSPREAD-26NOV08PITANA-ANA3|yes: MOSTLY_INDEPENDENT (phi 0.111); KXNHLSPREAD-26NOV08PITANA-PIT3|no: MOSTLY_INDEPENDENT (phi 0.086); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: ANA offense suppressed (<= 2 goals)
- **Anaheim wins by over 2.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes; why: higher confidence-adjusted growth (12.38 vs 7.11 bp); wins across more scripts (relative breadth 0.477 vs 0.308); relationships: KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.111); KXNHLSPREAD-26NOV08PITANA-PIT3|no: REINFORCING (phi 0.242); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: REINFORCING (phi 0.166); failure: tight game (one-goal final or OT)
- **Pittsburgh wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV08PITANA-ANA3|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV08PITANA-ANA3|yes has the higher standalone adjusted growth (12.38 vs 6.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.242); they share one thesis budget; relationships: KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.086); KXNHLSPREAD-26NOV08PITANA-ANA3|yes: REINFORCING (phi 0.242); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.135); failure: PIT wins by 2+
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV08PITANA-ANA3|yes; why: Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.50 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26NOV08PITANA-ANA3|yes: REINFORCING (phi 0.166); KXNHLSPREAD-26NOV08PITANA-PIT3|no: MOSTLY_INDEPENDENT (phi 0.135); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.5812): highest fidelity KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA3|yes — Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.50 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis ANA:WINS_BY_2PLUS (p 0.4353): highest fidelity KXNHLSPREAD-26NOV08PITANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.6389): highest fidelity KXNHLSPREAD-26NOV08PITANA-PIT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-ANA3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2295, phi -0.147)
- KXNHLSPREAD-26NOV08PITANA-ANA3|yes: FUNDED_RESEARCH; family MIXED; loses 28% of the draws where the thesis happens; opposing: failure thesis GAME:TIGHT (p 0.3779, phi -0.526)
- KXNHLSPREAD-26NOV08PITANA-PIT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:WINS_BY_2PLUS (p 0.1868, phi -0.748)
- KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2295, phi -0.251)
- override: Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.50 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +13.86 (adj +4.41) on $50.00, P(profit) 0.4623, adj growth 23.7 bp · B EV +6.19 (adj +3.08) on $36.87, P(profit) 0.4023, adj growth 26.7 bp · C EV +3.51 (adj +1.37) on $10.04, P(profit) 0.365, adj growth 11.9 bp · R EV +1.11 (adj +0.44) on $8.00, P(profit) 0.5225, adj growth 15.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
