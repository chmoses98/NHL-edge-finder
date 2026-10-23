# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-23T18:49:30Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 58.17 | +6.10 | +1.70 | +2.26 | 0.642 | -21.34 | -36.51 | 14.52 |
| B thesis-diversified (joint) ← optimiser card | 49.27 | +6.06 | +2.17 | +0.91 | 0.673 | -27.98 | -27.98 | 18.93 |
| C best expression per thesis | 54.39 | +6.23 | +2.01 | +10.03 | 0.602 | -15.85 | -28.51 | 17.72 |
| R FUNDED research stakes | 9.00 | +0.84 | +0.40 | -2.45 | 0.430 | -9.00 | -9.00 | 0.00 |

## MTL @ CHI  ·  10000 joint draws  ·  440 bet sides mapped, 11 +EV candidates, 4 on card

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
| Anton Frondell: 1+ goals YES | 20 | 0.250 | 0.234 | +0.039 | +0.023 | $6.86 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 57 | 0.686 | 0.607 | +0.099 | +0.020 | $16.97 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Frank Nazar: 1+ goals YES | 21 | 0.248 | 0.237 | +0.027 | +0.016 | $4.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Montreal wins by over 2.5 goals NO | 75 | 0.810 | 0.778 | +0.047 | +0.015 | $16.25 | FUNDED_RESEARCH | $5 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (6.62 vs 3.17 bp); relationships: KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.081); KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLSPREAD-26OCT23MTLCHI-MTL3|no: MOSTLY_INDEPENDENT (phi 0.116); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (3.70 vs 1.66 bp); relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.081); KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLSPREAD-26OCT23MTLCHI-MTL3|no: INTENTIONAL_DIVERSIFIER (phi -0.154); failure: CHI offense succeeds (4+ goals)
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes has the higher standalone adjusted growth (6.62 vs 3.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.048); KXNHLSPREAD-26OCT23MTLCHI-MTL3|no: MOSTLY_INDEPENDENT (phi 0.115); failure: CHI offense suppressed (<= 2 goals)
- **Montreal wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT23MTLCHI-MTL2|no; why: Broad expression KXNHLSPREAD-26OCT23MTLCHI-MTL3|no selected over player prop KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.89 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.116); KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.154); KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.115); failure: MTL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CHI:OFFENSE_4PLUS (p 0.3786): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.405): highest fidelity KXNHLAST-26OCT23MTLCHI-CHIAFRONDELL16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3821): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no — Broad expression KXNHLSPREAD-26OCT23MTLCHI-MTL3|no selected over player prop KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.89 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.405, phi -0.214)
- KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3786, phi -0.256)
- KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.405, phi -0.23)
- KXNHLSPREAD-26OCT23MTLCHI-MTL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.3006, phi -0.738)
- override: Broad expression KXNHLSPREAD-26OCT23MTLCHI-MTL3|no selected over player prop KXNHLAST-26OCT23MTLCHI-MTLOKAPANEN91-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.89 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.43 (adj +1.33) on $50.00, P(profit) 0.6512, adj growth 11.7 bp · B EV +5.70 (adj +1.97) on $44.88, P(profit) 0.6577, adj growth 17.2 bp · C EV +5.87 (adj +1.81) on $50.00, P(profit) 0.5454, adj growth 16.0 bp · R EV +0.68 (adj +0.31) on $7.00, P(profit) 0.25, adj growth 10.3 bp

## TBL @ COL  ·  10000 joint draws  ·  430 bet sides mapped, 1 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.532 / away 0.468

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
| Artturi Lehkonen: 1+ goals YES | 27 | 0.307 | 0.297 | +0.023 | +0.013 | $4.39 | FUNDED_RESEARCH | $2 | COL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT23TBCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (1.77 vs 0.78 bp); despite a smaller raw edge (+0.023 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0085 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: COL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4376): highest fidelity KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes (same contract)
- KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3388, phi -0.234)

portfolios: A EV +0.67 (adj +0.37) on $8.17, P(profit) 0.3072, adj growth 2.8 bp · B EV +0.36 (adj +0.20) on $4.39, P(profit) 0.3072, adj growth 1.7 bp · C EV +0.36 (adj +0.20) on $4.39, P(profit) 0.3072, adj growth 1.7 bp · R EV +0.16 (adj +0.09) on $2.00, P(profit) 0.3072, adj growth 2.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
