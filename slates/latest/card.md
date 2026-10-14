# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-14T09:34:21Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 39.14 | +3.96 | +1.02 | +0.27 | 0.551 | -39.14 | -39.14 | 1.63 |
| B thesis-diversified (joint) ← optimiser card | 5.39 | +0.60 | +0.16 | -3.30 | 0.443 | -5.39 | -5.39 | 1.38 |
| C best expression per thesis | 5.00 | +0.58 | +0.16 | -5.00 | 0.443 | -5.00 | -5.00 | 1.36 |
| R FUNDED research stakes | 3.00 | +0.32 | +0.08 | -1.03 | 0.443 | -3.00 | -3.00 | 0.00 |

## MTL @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_MTL_win | p_overtime | goals | shots WSH/MTL | WSH/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.58 | 0.42 | 0.00 | 6.05 | 27.7/27.5 | 24.2/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.50 | 0.50 | 0.46 | 5.87 | 27.4/27.2 | 24.0/24.1 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.094 | 0.65 | 0.35 | 0.00 | 5.98 | 32.4/21.5 | 18.6/28.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.55 | 0.45 | 0.00 | 9.29 | 28.9/28.8 | 23.3/22.4 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.54 | 0.46 | 0.46 | 5.93 | 32.1/21.6 | 18.5/28.7 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.055 | 0.66 | 0.34 | 0.00 | 9.36 | 34.0/23.0 | 18.0/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 5.5 goals scored NO | 38 | 0.443 | 0.409 | +0.046 | +0.012 | $4.33 | FUNDED_RESEARCH | $2 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Full Game: Over 6.5 goals scored NO | 49 | 0.551 | 0.518 | +0.044 | +0.011 | $1.06 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-7|no; why: higher confidence-adjusted growth (1.39 vs 1.00 bp); relationships: KXNHLTOTAL-26OCT14MTLWSH-7|no: DUPLICATIVE (phi 0.804); failure: WSH offense succeeds (4+ goals)
- **Full Game: Over 6.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-6|no; why: second expression of the same thesis: KXNHLTOTAL-26OCT14MTLWSH-6|no has the higher standalone adjusted growth (1.39 vs 1.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.804); they share one thesis budget; relationships: KXNHLTOTAL-26OCT14MTLWSH-6|no: DUPLICATIVE (phi 0.804); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis GAME:LOW_EVENT (p 0.2398): highest fidelity KXNHLTOTAL-26OCT14MTLWSH-6|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT14MTLWSH-6|no (same contract)
- KXNHLTOTAL-26OCT14MTLWSH-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4165, phi -0.525)
- KXNHLTOTAL-26OCT14MTLWSH-7|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2487, phi -0.638)

portfolios: A EV +3.96 (adj +1.02) on $39.14, P(profit) 0.5514, adj growth 1.6 bp · B EV +0.60 (adj +0.16) on $5.39, P(profit) 0.4427, adj growth 1.4 bp · C EV +0.58 (adj +0.16) on $5.00, P(profit) 0.4427, adj growth 1.4 bp · R EV +0.32 (adj +0.08) on $3.00, P(profit) 0.4427, adj growth 2.4 bp

## DAL @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_DAL_win | p_overtime | goals | shots COL/DAL | COL/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.127 | 0.72 | 0.28 | 0.00 | 5.99 | 32.7/21.1 | 18.6/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.66 | 0.34 | 0.00 | 5.99 | 27.2/26.6 | 23.9/23.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.60 | 0.40 | 0.48 | 5.91 | 32.8/21.4 | 18.4/29.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.53 | 0.47 | 0.47 | 5.92 | 27.3/26.7 | 23.4/23.9 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.083 | 0.72 | 0.28 | 0.00 | 9.18 | 34.8/22.8 | 18.6/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.64 | 0.36 | 0.00 | 9.21 | 28.8/28.2 | 23.0/21.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
