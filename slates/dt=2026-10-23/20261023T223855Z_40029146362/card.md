# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-23T22:38:55Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 86.44 | +12.57 | +2.89 | +12.37 | 0.668 | -26.86 | -44.80 | 23.57 |
| B thesis-diversified (joint) ← optimiser card | 63.90 | +7.66 | +2.45 | +4.78 | 0.638 | -25.41 | -33.71 | 21.46 |
| C best expression per thesis | 67.91 | +9.92 | +2.55 | +10.54 | 0.645 | -24.05 | -27.29 | 22.55 |
| R FUNDED research stakes | 9.00 | +0.73 | +0.34 | -1.95 | 0.439 | -9.00 | -9.00 | 0.00 |

## MTL @ CHI  ·  10000 joint draws  ·  440 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.406 / away 0.595

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_MTL_win | p_overtime | goals | shots CHI/MTL | CHI/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.50 | 0.50 | 0.00 | 6.0 | 26.6/26.8 | 23.3/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.48 | 0.52 | 0.47 | 5.93 | 26.9/27.1 | 23.9/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.47 | 0.53 | 0.00 | 9.31 | 28.2/28.7 | 22.4/22.4 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.087 | 0.41 | 0.59 | 0.00 | 5.99 | 21.2/31.9 | 27.6/18.1 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.48 | 0.52 | 0.48 | 5.9 | 21.6/32.2 | 29.0/18.4 | even strength |
| MTL shot control · high event (8+) · decided (2+) | 0.058 | 0.36 | 0.64 | 0.00 | 9.28 | 22.5/33.5 | 26.3/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 25 | 0.296 | 0.283 | +0.033 | +0.020 | $7.17 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 57 | 0.686 | 0.607 | +0.099 | +0.020 | $17.72 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Frank Nazar: 1+ goals YES | 21 | 0.248 | 0.237 | +0.027 | +0.016 | $4.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Montreal wins by over 2.5 goals NO | 75 | 0.810 | 0.778 | +0.047 | +0.015 | $16.34 | FUNDED_RESEARCH | $5 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (4.61 vs 3.17 bp); relationships: KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.142); KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26OCT23MTLCHI-MTL3|no: MOSTLY_INDEPENDENT (phi 0.133); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT23MTLCHI-CHIAFRONDELL16-1|no; why: higher confidence-adjusted growth (3.70 vs 1.46 bp); relationships: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.142); KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLSPREAD-26OCT23MTLCHI-MTL3|no: INTENTIONAL_DIVERSIFIER (phi -0.154); failure: CHI offense succeeds (4+ goals)
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (4.61 vs 3.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.048); KXNHLSPREAD-26OCT23MTLCHI-MTL3|no: MOSTLY_INDEPENDENT (phi 0.115); failure: CHI offense suppressed (<= 2 goals)
- **Montreal wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT23MTLCHI-MTL2|no; why: Broad expression KXNHLSPREAD-26OCT23MTLCHI-MTL3|no selected over player prop KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.89 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.133); KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.154); KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.115); failure: MTL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CHI:OFFENSE_4PLUS (p 0.3786): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3821): highest fidelity KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no — Broad expression KXNHLSPREAD-26OCT23MTLCHI-MTL3|no selected over player prop KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.89 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CHI:SUPPRESSED (p 0.405): highest fidelity KXNHLAST-26OCT23MTLCHI-CHIAFRONDELL16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.405, phi -0.255)
- KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3786, phi -0.256)
- KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.405, phi -0.23)
- KXNHLSPREAD-26OCT23MTLCHI-MTL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.3006, phi -0.738)
- override: Broad expression KXNHLSPREAD-26OCT23MTLCHI-MTL3|no selected over player prop KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.89 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +8.06 (adj +1.60) on $50.00, P(profit) 0.616, adj growth 13.9 bp · B EV +5.47 (adj +1.81) on $45.99, P(profit) 0.6859, adj growth 15.9 bp · C EV +7.73 (adj +1.91) on $50.00, P(profit) 0.6641, adj growth 17.0 bp · R EV +0.56 (adj +0.25) on $7.00, P(profit) 0.2962, adj growth 8.3 bp

## TBL @ COL  ·  10000 joint draws  ·  430 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.527 / away 0.473

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
| Andrei Vasilevskiy: 28+ saves NO | 54 | 0.645 | 0.574 | +0.088 | +0.016 | $9.52 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Artturi Lehkonen: 1+ goals YES | 27 | 0.307 | 0.297 | +0.023 | +0.013 | $4.20 | FUNDED_RESEARCH | $2 | COL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Brayden Point: 1+ goals YES | 27 | 0.307 | 0.296 | +0.024 | +0.012 | $4.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
- **Andrei Vasilevskiy: 28+ saves NO** — thesis: TBL net faces light volume (<= 25 shots; COL suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLGOAL-26OCT23TBCOL-TBBPOINT21-1|yes: MOSTLY_INDEPENDENT (phi -0.028); failure: TBL net faces heavy volume (33+ shots; COL pressure)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT23TBCOL-TB3|no; why: higher confidence-adjusted growth (1.77 vs 1.15 bp); despite a smaller raw edge (+0.023 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no: MOSTLY_INDEPENDENT (phi 0.039); KXNHLGOAL-26OCT23TBCOL-TBBPOINT21-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: COL offense suppressed (<= 2 goals)
- **Brayden Point: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23TBCOL-TBJGUENTZEL59-2|yes; why: higher confidence-adjusted growth (1.50 vs 0.23 bp); wins across more scripts (relative breadth 0.945 vs 0.828); alternative not eligible: confidence-adjusted EV +0.0025 below the 0.010/contract floor; relationships: KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: TBL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TBL:NET_LOW_VOLUME (p 0.2922): highest fidelity KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no (same contract)
- thesis COL:OFFENSE_4PLUS (p 0.4376): highest fidelity KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes (same contract)
- thesis TBL:OFFENSE_4PLUS (p 0.329): highest fidelity KXNHLGOAL-26OCT23TBCOL-TBBPOINT21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT23TBCOL-TBBPOINT21-1|yes (same contract)
- KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.0 pts; fragile player expression; opposing: failure thesis TBL:NET_HIGH_VOLUME (p 0.2738, phi -0.712)
- KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3388, phi -0.234)
- KXNHLGOAL-26OCT23TBCOL-TBBPOINT21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.4558, phi -0.249)

portfolios: A EV +4.51 (adj +1.29) on $36.44, P(profit) 0.3681, adj growth 9.7 bp · B EV +2.19 (adj +0.64) on $17.91, P(profit) 0.3681, adj growth 5.6 bp · C EV +2.19 (adj +0.64) on $17.91, P(profit) 0.3681, adj growth 5.6 bp · R EV +0.16 (adj +0.09) on $2.00, P(profit) 0.3072, adj growth 2.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
