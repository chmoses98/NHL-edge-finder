# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T23:10:57Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 34.33 | +6.58 | +3.56 | -1.41 | 0.454 | -34.33 | -34.33 | 25.98 |
| B thesis-diversified (joint) ← optimiser card | 17.29 | +3.23 | +1.83 | -0.29 | 0.454 | -17.29 | -17.29 | 15.85 |
| C best expression per thesis | 3.47 | +0.85 | +0.34 | -3.47 | 0.172 | -3.47 | -3.47 | 2.94 |
| R FUNDED research stakes | 2.00 | +0.46 | +0.30 | -2.00 | 0.157 | -2.00 | -2.00 | 0.00 |

## SEA @ CGY  ·  10000 joint draws  ·  452 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.489 / away 0.511

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_SEA_win | p_overtime | goals | shots CGY/SEA | CGY/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.44 | 0.56 | 0.00 | 6.05 | 28.9/28.7 | 24.7/25.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.48 | 0.52 | 0.46 | 5.97 | 28.7/28.5 | 25.3/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.46 | 0.54 | 0.00 | 9.35 | 30.1/30.0 | 23.6/24.1 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.086 | 0.51 | 0.49 | 0.00 | 5.98 | 33.9/22.7 | 19.3/30.3 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.50 | 0.50 | 0.49 | 5.89 | 34.0/23.0 | 19.7/30.8 | even strength |
| CGY shot control · high event (8+) · decided (2+) | 0.056 | 0.53 | 0.47 | 0.00 | 9.27 | 35.4/23.8 | 18.2/28.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 12 | 0.157 | 0.146 | +0.029 | +0.019 | $5.01 | FUNDED_RESEARCH | $2 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 18 | 0.221 | 0.209 | +0.031 | +0.019 | $5.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 13 | 0.172 | 0.151 | +0.034 | +0.013 | $3.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:WINS_BY_2PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 19 | 0.222 | 0.213 | +0.021 | +0.012 | $3.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (6.97 vs 3.29 bp); despite a smaller raw edge (+0.029 vs +0.034/contract); relationships: KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes; why: higher confidence-adjusted growth (5.17 vs 3.29 bp); despite a smaller raw edge (+0.031 vs +0.034/contract); relationships: KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.028); failure: SEA offense suppressed (<= 2 goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA wins by 2+; alternative: KXNHLPTS-26OCT30SEACGY-CGYJFARABEE86-1|no; why: higher confidence-adjusted growth (3.29 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: SEA offense suppressed (<= 2 goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT30SEACGY-CGYMBACKLUND11-1|yes; why: higher confidence-adjusted growth (1.92 vs 0.01 bp); alternative not eligible: confidence-adjusted EV +0.0006 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.4144): highest fidelity KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.3033): highest fidelity KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3744): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT30SEACGY-SEABMEYERS59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3603, phi -0.183)
- KXNHLGOAL-26OCT30SEACGY-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3603, phi -0.204)
- KXNHLGOAL-26OCT30SEACGY-SEAFGAUDREAU89-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3603, phi -0.202)
- KXNHLGOAL-26OCT30SEACGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.407, phi -0.194)

portfolios: A EV +6.58 (adj +3.56) on $34.33, P(profit) 0.454, adj growth 26.0 bp · B EV +3.23 (adj +1.83) on $17.29, P(profit) 0.454, adj growth 15.9 bp · C EV +0.85 (adj +0.34) on $3.47, P(profit) 0.1718, adj growth 2.9 bp · R EV +0.46 (adj +0.30) on $2.00, P(profit) 0.1568, adj growth 9.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
