# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-24T00:25:54Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +3.67 | +0.98 | +13.59 | 0.529 | -28.65 | -31.51 | 7.54 |
| B thesis-diversified (joint) ← optimiser card | 30.32 | +3.10 | +1.72 | -8.81 | 0.473 | -10.60 | -30.32 | 14.81 |
| C best expression per thesis | 33.06 | +2.24 | +0.78 | -1.02 | 0.436 | -11.59 | -22.49 | 6.83 |
| R FUNDED research stakes | 6.00 | +0.69 | +0.39 | +0.31 | 0.839 | -6.00 | -6.00 | 0.00 |

## TBL @ COL  ·  10000 joint draws  ·  430 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.526 / away 0.474

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_TBL_win | p_overtime | goals | shots COL/TBL | COL/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.64 | 0.36 | 0.00 | 6.03 | 28.2/27.8 | 24.8/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.48 | 5.9 | 28.2/27.8 | 24.6/25.0 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.100 | 0.63 | 0.37 | 0.00 | 5.96 | 33.5/22.0 | 19.3/29.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.60 | 0.40 | 0.00 | 9.3 | 29.8/29.4 | 23.7/23.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.55 | 0.45 | 0.47 | 5.88 | 33.4/22.3 | 19.2/30.1 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.068 | 0.70 | 0.30 | 0.00 | 9.17 | 34.3/23.4 | 18.8/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Josh Manson: 1+ goals YES | 4 | 0.062 | 0.057 | +0.019 | +0.014 | $3.22 | FUNDED_RESEARCH | $1 | COL:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Brayden Point: 1+ goals YES | 27 | 0.307 | 0.297 | +0.024 | +0.013 | $5.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 27 | 0.307 | 0.297 | +0.023 | +0.013 | $4.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Tampa Bay over 4.5 goals scored NO | 78 | 0.830 | 0.802 | +0.038 | +0.010 | $17.03 | FUNDED_RESEARCH | $5 | COL:WINS | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Josh Manson: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (9.85 vs 1.77 bp); despite a smaller raw edge (+0.019 vs +0.023/contract); relationships: KXNHLGOAL-26OCT23TBCOL-TBBPOINT21-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLTEAMTOTAL-26OCT23TBCOL-TB5|no: MOSTLY_INDEPENDENT (phi 0.01); failure: COL offense suppressed (<= 2 goals)
- **Brayden Point: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23TBCOL-TBBHAGEL38-2|yes; why: higher confidence-adjusted growth (1.83 vs 1.12 bp); wins across more scripts (relative breadth 0.945 vs 0.797); alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLTEAMTOTAL-26OCT23TBCOL-TB5|no: INTENTIONAL_DIVERSIFIER (phi -0.192); failure: TBL offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23TBCOL-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (1.77 vs 1.54 bp); despite a smaller raw edge (+0.023 vs +0.024/contract); relationships: KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT23TBCOL-TBBPOINT21-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLTEAMTOTAL-26OCT23TBCOL-TB5|no: MOSTLY_INDEPENDENT (phi -0.001); failure: COL offense suppressed (<= 2 goals)
- **Tampa Bay over 4.5 goals scored NO** — thesis: COL wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT23TBCOL-TB4|no; why: higher confidence-adjusted growth (1.41 vs 1.04 bp); despite a smaller raw edge (+0.038 vs +0.043/contract); relationships: KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT23TBCOL-TBBPOINT21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.192); KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TBL:OFFENSE_4PLUS (p 0.329): highest fidelity KXNHLGOAL-26OCT23TBCOL-TBBPOINT21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT23TBCOL-TBBPOINT21-1|yes (same contract)
- thesis COL:OFFENSE_4PLUS (p 0.4376): highest fidelity KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes (same contract)
- thesis COL:WINS (p 0.5786): highest fidelity KXNHLTEAMTOTAL-26OCT23TBCOL-TB5|no [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT23TBCOL-TB4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3388, phi -0.091)
- KXNHLGOAL-26OCT23TBCOL-TBBPOINT21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.4558, phi -0.249)
- KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3388, phi -0.234)
- KXNHLTEAMTOTAL-26OCT23TBCOL-TB5|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.329, phi -0.647)

portfolios: A EV +3.67 (adj +0.98) on $50.00, P(profit) 0.529, adj growth 7.5 bp · B EV +3.10 (adj +1.72) on $30.32, P(profit) 0.4726, adj growth 14.8 bp · C EV +2.24 (adj +0.78) on $33.06, P(profit) 0.4365, adj growth 6.8 bp · R EV +0.69 (adj +0.39) on $6.00, P(profit) 0.8393, adj growth 12.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
