# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-24T00:48:09Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +5.08 | +0.97 | +6.31 | 0.685 | -28.35 | -34.22 | 7.06 |
| B thesis-diversified (joint) ← optimiser card | 38.14 | +3.52 | +1.77 | +2.44 | 0.686 | -15.60 | -20.10 | 15.54 |
| C best expression per thesis | 28.93 | +2.66 | +0.94 | +5.67 | 0.628 | -11.95 | -11.95 | 8.24 |
| R FUNDED research stakes | 5.00 | +0.13 | +0.08 | +0.63 | 0.911 | +0.63 | -5.00 | 0.00 |

## TBL @ COL  ·  10000 joint draws  ·  440 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.526 / away 0.474

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_TBL_win | p_overtime | goals | shots COL/TBL | COL/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.64 | 0.36 | 0.00 | 6.03 | 28.2/27.7 | 24.8/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.48 | 5.88 | 28.1/27.7 | 24.5/24.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.100 | 0.63 | 0.37 | 0.00 | 5.96 | 33.5/22.1 | 19.3/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.61 | 0.39 | 0.00 | 9.29 | 29.7/29.3 | 23.7/22.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.56 | 0.44 | 0.48 | 5.9 | 33.4/22.2 | 19.1/30.1 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.067 | 0.69 | 0.31 | 0.00 | 9.16 | 34.4/23.4 | 18.8/27.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Josh Manson: 1+ goals YES | 4 | 0.059 | 0.054 | +0.016 | +0.011 | $2.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 2+ goals NO | 88 | 0.911 | 0.902 | +0.023 | +0.015 | $20.00 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Gabriel Landeskog: 1+ goals YES | 20 | 0.244 | 0.229 | +0.033 | +0.018 | $5.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Andrei Vasilevskiy: 28+ saves NO | 56 | 0.645 | 0.595 | +0.068 | +0.018 | $10.41 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Josh Manson: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23TBCOL-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (6.59 vs 4.28 bp); despite a smaller raw edge (+0.016 vs +0.033/contract); relationships: KXNHLGOAL-26OCT23TBCOL-COLNMACKINNON29-2|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT23TBCOL-COLGLANDESKOG92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no: MOSTLY_INDEPENDENT (phi 0.028); failure: COL offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 2+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT23TBCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (4.64 vs 0.39 bp); despite a smaller raw edge (+0.023 vs +0.075/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT23TBCOL-COLGLANDESKOG92-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no: INTENTIONAL_DIVERSIFIER (phi -0.053); failure: COL offense succeeds (4+ goals)
- **Gabriel Landeskog: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (4.28 vs 1.12 bp); relationships: KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT23TBCOL-COLNMACKINNON29-2|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no: MOSTLY_INDEPENDENT (phi 0.045); failure: COL offense suppressed (<= 2 goals)
- **Andrei Vasilevskiy: 28+ saves NO** — thesis: TBL net faces light volume (<= 25 shots; COL suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26OCT23TBCOL-COLNMACKINNON29-2|no: INTENTIONAL_DIVERSIFIER (phi -0.053); KXNHLGOAL-26OCT23TBCOL-COLGLANDESKOG92-1|yes: MOSTLY_INDEPENDENT (phi 0.045); failure: TBL net faces heavy volume (33+ shots; COL pressure)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4376): highest fidelity KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT23TBCOL-COLGLANDESKOG92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:NET_LOW_VOLUME (p 0.2922): highest fidelity KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no (same contract)
- thesis COL:WINS (p 0.5786): highest fidelity KXNHLTEAMTOTAL-26OCT23TBCOL-TB5|no [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT23TBCOL-TB4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3388, phi -0.099)
- KXNHLGOAL-26OCT23TBCOL-COLNMACKINNON29-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4376, phi -0.24)
- KXNHLGOAL-26OCT23TBCOL-COLGLANDESKOG92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3388, phi -0.197)
- KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.0 pts; fragile player expression; opposing: failure thesis TBL:NET_HIGH_VOLUME (p 0.2738, phi -0.712)

portfolios: A EV +5.08 (adj +0.97) on $50.00, P(profit) 0.6853, adj growth 7.1 bp · B EV +3.52 (adj +1.77) on $38.14, P(profit) 0.686, adj growth 15.5 bp · C EV +2.66 (adj +0.94) on $28.93, P(profit) 0.6282, adj growth 8.2 bp · R EV +0.13 (adj +0.08) on $5.00, P(profit) 0.9108, adj growth 3.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
