# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-16T04:27:01Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +7.94 | +2.26 | -19.06 | 0.407 | -50.00 | -50.00 | 1.35 |
| B thesis-diversified (joint) ← optimiser card | 6.26 | +1.07 | +0.30 | -3.61 | 0.407 | -6.26 | -6.26 | 2.63 |
| C best expression per thesis | 4.67 | +0.78 | +0.23 | -4.67 | 0.331 | -4.67 | -4.67 | 2.05 |
| R FUNDED research stakes | 4.00 | +0.66 | +0.19 | -1.99 | 0.407 | -4.00 | -4.00 | 0.00 |

## PIT @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_PIT_win | p_overtime | goals | shots COL/PIT | COL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.121 | 0.71 | 0.29 | 0.00 | 6.08 | 33.9/22.2 | 19.6/28.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.66 | 0.34 | 0.00 | 6.04 | 28.4/27.8 | 24.9/24.1 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.104 | 0.73 | 0.27 | 0.00 | 9.44 | 36.0/23.7 | 19.2/27.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.68 | 0.32 | 0.00 | 9.41 | 30.1/29.4 | 24.3/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.53 | 0.47 | 0.48 | 5.99 | 28.9/28.2 | 24.9/25.5 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.57 | 0.43 | 0.46 | 5.98 | 34.0/22.3 | 19.2/30.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BOS_win | p_overtime | goals | shots ANA/BOS | ANA/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.122 | 0.58 | 0.42 | 0.00 | 6.05 | 33.9/22.1 | 18.9/29.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.53 | 0.47 | 0.00 | 6.09 | 28.6/28.0 | 24.7/24.7 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.55 | 0.45 | 0.48 | 5.98 | 34.5/22.4 | 19.2/31.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.54 | 0.46 | 0.00 | 9.46 | 30.4/29.6 | 23.6/23.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.098 | 0.60 | 0.40 | 0.00 | 9.43 | 36.0/23.7 | 18.4/28.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.50 | 0.50 | 0.50 | 5.97 | 28.5/27.9 | 24.6/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 7.5 goals scored YES | 27 | 0.331 | 0.298 | +0.047 | +0.014 | $1.42 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Full Game: Over 8.5 goals scored YES | 20 | 0.253 | 0.224 | +0.041 | +0.013 | $1.46 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | DIRECT (0.76) | EVIDENCE_MIXED | D |
| Anaheim over 4.5 goals scored YES | 22 | 0.279 | 0.245 | +0.047 | +0.013 | $2.06 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | DIRECT (0.60) | EVIDENCE_MIXED | D |
| Full Game: Over 6.5 goals scored YES | 48 | 0.544 | 0.510 | +0.047 | +0.012 | $1.32 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Full Game: Over 7.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT16BOSANA-9|yes; why: higher confidence-adjusted growth (2.18 vs 2.07 bp); relationships: KXNHLTOTAL-26OCT16BOSANA-9|yes: DUPLICATIVE (phi 0.826); KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5|yes: REINFORCING (phi 0.525); KXNHLTOTAL-26OCT16BOSANA-7|yes: DUPLICATIVE (phi 0.644); failure: BOS offense suppressed (<= 2 goals)
- **Full Game: Over 8.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT16BOSANA-8|yes; why: second expression of the same thesis: KXNHLTOTAL-26OCT16BOSANA-8|yes has the higher standalone adjusted growth (2.18 vs 2.07 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.826); they share one thesis budget; relationships: KXNHLTOTAL-26OCT16BOSANA-8|yes: DUPLICATIVE (phi 0.826); KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5|yes: REINFORCING (phi 0.462); KXNHLTOTAL-26OCT16BOSANA-7|yes: DUPLICATIVE (phi 0.532); failure: BOS offense suppressed (<= 2 goals)
- **Anaheim over 4.5 goals scored YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT16BOSANA-8|yes; why: second expression of the same thesis: KXNHLTOTAL-26OCT16BOSANA-8|yes has the higher standalone adjusted growth (2.18 vs 1.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.525); they share one thesis budget; relationships: KXNHLTOTAL-26OCT16BOSANA-8|yes: REINFORCING (phi 0.525); KXNHLTOTAL-26OCT16BOSANA-9|yes: REINFORCING (phi 0.462); KXNHLTOTAL-26OCT16BOSANA-7|yes: REINFORCING (phi 0.453); failure: BOS wins (incl. OT/SO)
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT16BOSANA-8|yes; why: second expression of the same thesis: KXNHLTOTAL-26OCT16BOSANA-8|yes has the higher standalone adjusted growth (2.18 vs 1.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.644); they share one thesis budget; relationships: KXNHLTOTAL-26OCT16BOSANA-8|yes: DUPLICATIVE (phi 0.644); KXNHLTOTAL-26OCT16BOSANA-9|yes: DUPLICATIVE (phi 0.532); KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5|yes: REINFORCING (phi 0.453); failure: low-event game (<= 4 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:HIGH_EVENT (p 0.3311): highest fidelity KXNHLTOTAL-26OCT16BOSANA-8|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT16BOSANA-8|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4615): highest fidelity KXNHLTOTAL-26OCT16BOSANA-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT16BOSANA-8|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTOTAL-26OCT16BOSANA-8|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.371, phi -0.408)
- KXNHLTOTAL-26OCT16BOSANA-9|yes: FUNDED_RESEARCH; family MIXED; loses 24% of the draws where the thesis happens; opposing: failure thesis BOS:SUPPRESSED (p 0.371, phi -0.389)
- KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5|yes: FUNDED_RESEARCH; family MIXED; loses 40% of the draws where the thesis happens; opposing: failure thesis BOS:WINS (p 0.465, phi -0.469)
- KXNHLTOTAL-26OCT16BOSANA-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.1821, phi -0.516)

portfolios: A EV +7.94 (adj +2.26) on $50.00, P(profit) 0.4069, adj growth 1.4 bp · B EV +1.07 (adj +0.30) on $6.26, P(profit) 0.4069, adj growth 2.6 bp · C EV +0.78 (adj +0.23) on $4.67, P(profit) 0.3311, adj growth 2.0 bp · R EV +0.66 (adj +0.19) on $4.00, P(profit) 0.4069, adj growth 5.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
