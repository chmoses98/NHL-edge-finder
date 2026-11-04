# NHL THESIS CARD — RESEARCH_ONLY — status **NO_BETS**

generated 2026-11-04T01:17:59Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |
| B thesis-diversified (joint) ← optimiser card | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |
| C best expression per thesis | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |
| R FUNDED research stakes | 0.00 | +0.00 | +0.00 | +0.00 | 0.000 | +0.00 | +0.00 | 0.00 |

## ANA @ VAN  ·  10000 joint draws  ·  416 bet sides mapped, 0 +EV candidates, 0 on card

sportsbook moneyline consensus (5 books): home 0.375 / away 0.625

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_ANA_win | p_overtime | goals | shots VAN/ANA | VAN/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.118 | 0.41 | 0.59 | 0.00 | 6.05 | 21.7/34.0 | 29.7/18.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.118 | 0.39 | 0.61 | 0.00 | 9.51 | 23.2/35.5 | 27.9/17.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.50 | 0.50 | 0.00 | 6.05 | 27.2/27.8 | 24.2/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.45 | 0.55 | 0.00 | 9.49 | 29.0/29.8 | 23.1/22.9 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.45 | 0.55 | 0.46 | 6.06 | 21.9/33.9 | 30.3/18.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.52 | 0.48 | 0.46 | 6.01 | 27.3/28.1 | 24.8/23.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, ANA shot control · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
