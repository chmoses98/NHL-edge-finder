# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-23T17:50:48Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 69.96 | +8.01 | +2.49 | +14.89 | 0.521 | -30.02 | -49.36 | 18.45 |
| B thesis-diversified (joint) ← optimiser card | 47.37 | +6.20 | +2.66 | +2.36 | 0.566 | -26.21 | -32.61 | 23.15 |
| C best expression per thesis | 34.25 | +4.20 | +1.55 | +2.47 | 0.570 | -16.20 | -16.20 | 13.47 |
| R FUNDED research stakes | 6.00 | +0.77 | +0.40 | -1.36 | 0.388 | -6.00 | -6.00 | 0.00 |

## MTL @ CHI  ·  10000 joint draws  ·  428 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.403 / away 0.597

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_MTL_win | p_overtime | goals | shots CHI/MTL | CHI/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.49 | 0.51 | 0.00 | 6.04 | 26.7/27.0 | 23.3/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.48 | 0.52 | 0.46 | 5.93 | 26.9/27.2 | 23.8/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.45 | 0.55 | 0.00 | 9.28 | 28.3/28.8 | 22.4/22.7 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.089 | 0.41 | 0.59 | 0.00 | 6.03 | 21.2/31.9 | 27.9/18.2 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.51 | 0.49 | 0.46 | 5.92 | 21.3/32.0 | 28.7/18.1 | even strength |
| MTL shot control · high event (8+) · decided (2+) | 0.057 | 0.37 | 0.63 | 0.00 | 9.35 | 23.1/34.1 | 26.6/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anton Frondell: 1+ goals YES | 20 | 0.250 | 0.236 | +0.039 | +0.025 | $7.38 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 26 | 0.309 | 0.293 | +0.036 | +0.020 | $6.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
| Montreal wins by over 1.5 goals NO | 63 | 0.701 | 0.663 | +0.055 | +0.017 | $9.54 | FUNDED_RESEARCH | $3 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Patrick Kane: 1+ assists NO | 59 | 0.691 | 0.619 | +0.084 | +0.012 | $12.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (8.06 vs 4.31 bp); relationships: KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26OCT23MTLCHI-MTL2|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.072); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes has the higher standalone adjusted growth (8.06 vs 4.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26OCT23MTLCHI-MTL2|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.124); failure: CHI offense suppressed (<= 2 goals)
- **Montreal wins by over 1.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT23MTLCHI-MTL3|no; why: higher confidence-adjusted growth (2.73 vs 1.95 bp); relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.149); KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.157); failure: MTL wins by 2+
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (1.30 vs 0.84 bp); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.124); KXNHLSPREAD-26OCT23MTLCHI-MTL2|no: INTENTIONAL_DIVERSIFIER (phi -0.157); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CHI:OFFENSE_4PLUS (p 0.3735): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.4826): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT23MTLCHI-MTL2|no (same contract)
- thesis MTL:SUPPRESSED (p 0.3787): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT23MTLCHI-MTL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4011, phi -0.243)
- KXNHLGOAL-26OCT23MTLCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4011, phi -0.263)
- KXNHLSPREAD-26OCT23MTLCHI-MTL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.2986, phi -1.0)
- KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.1 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3735, phi -0.241)

portfolios: A EV +5.53 (adj +1.04) on $50.00, P(profit) 0.578, adj growth 7.4 bp · B EV +4.82 (adj +1.86) on $36.48, P(profit) 0.4592, adj growth 16.2 bp · C EV +3.88 (adj +1.38) on $30.22, P(profit) 0.5776, adj growth 12.0 bp · R EV +0.62 (adj +0.31) on $5.00, P(profit) 0.2498, adj growth 10.7 bp

## TBL @ COL  ·  10000 joint draws  ·  428 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.532 / away 0.468

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_TBL_win | p_overtime | goals | shots COL/TBL | COL/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.63 | 0.37 | 0.00 | 6.03 | 28.1/27.7 | 24.7/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.44 | 5.91 | 28.3/28.1 | 24.9/25.0 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.097 | 0.70 | 0.30 | 0.00 | 6.05 | 33.1/22.0 | 19.4/28.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.63 | 0.37 | 0.00 | 9.34 | 29.8/29.3 | 23.9/23.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.52 | 0.48 | 0.47 | 5.89 | 33.4/22.4 | 19.2/30.1 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.065 | 0.71 | 0.29 | 0.00 | 9.29 | 34.8/23.5 | 19.0/27.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ilya Mikheyev: 1+ goals YES | 15 | 0.182 | 0.173 | +0.023 | +0.014 | $3.90 | FUNDED_RESEARCH | $1 | TBL:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Parker Kelly: 1+ goals YES | 11 | 0.136 | 0.128 | +0.019 | +0.011 | $3.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 27 | 0.306 | 0.296 | +0.022 | +0.012 | $3.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Ilya Mikheyev: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23TBCOL-TBBPOINT21-1|yes; why: higher confidence-adjusted growth (3.07 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0023 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT23TBCOL-COLPKELLY17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: TBL offense suppressed (<= 2 goals)
- **Parker Kelly: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (2.76 vs 1.50 bp); despite a smaller raw edge (+0.019 vs +0.022/contract); relationships: KXNHLGOAL-26OCT23TBCOL-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: COL offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT23TBCOL-TB2|no; why: higher confidence-adjusted growth (1.50 vs 0.97 bp); despite a smaller raw edge (+0.022 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT23TBCOL-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT23TBCOL-COLPKELLY17-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4485): highest fidelity KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes (same contract)
- thesis TBL:OFFENSE_4PLUS (p 0.3249): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT23TBCOL-TBIMIKHEYEV95-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.4559, phi -0.213)
- KXNHLGOAL-26OCT23TBCOL-COLPKELLY17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3395, phi -0.158)
- KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3395, phi -0.243)

portfolios: A EV +2.48 (adj +1.45) on $19.96, P(profit) 0.5069, adj growth 11.1 bp · B EV +1.37 (adj +0.80) on $10.89, P(profit) 0.5069, adj growth 7.0 bp · C EV +0.31 (adj +0.17) on $4.03, P(profit) 0.3058, adj growth 1.5 bp · R EV +0.14 (adj +0.09) on $1.00, P(profit) 0.1819, adj growth 3.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
