# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-16T19:00:00Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +27.75 | +5.78 | +25.86 | 0.694 | -37.61 | -53.58 | 44.07 |
| B thesis-diversified (joint) ← optimiser card | 73.22 | +16.48 | +5.09 | +15.56 | 0.649 | -22.45 | -37.52 | 44.97 |
| C best expression per thesis | 60.88 | +15.42 | +4.40 | +19.97 | 0.616 | -25.73 | -40.15 | 38.36 |
| R FUNDED research stakes | 7.00 | +0.43 | +0.25 | +0.86 | 0.677 | -7.00 | -7.00 | 0.00 |

## PIT @ COL  ·  10000 joint draws  ·  446 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.650 / away 0.350

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_PIT_win | p_overtime | goals | shots COL/PIT | COL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.123 | 0.73 | 0.27 | 0.00 | 6.03 | 33.8/21.9 | 19.5/28.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.67 | 0.33 | 0.00 | 6.06 | 28.4/27.9 | 25.1/24.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.102 | 0.72 | 0.28 | 0.00 | 9.42 | 35.8/23.6 | 19.1/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.67 | 0.33 | 0.00 | 9.4 | 30.1/29.4 | 24.2/22.6 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.56 | 0.44 | 0.50 | 5.99 | 34.4/22.6 | 19.4/30.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.52 | 0.48 | 0.45 | 5.94 | 28.5/28.0 | 24.7/25.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cale Makar: 1+ assists NO | 33 | 0.555 | 0.379 | +0.210 | +0.033 | $11.62 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.77) | CALIBRATION_WARNING | D |
| Connor Dewar: 1+ goals YES | 11 | 0.143 | 0.133 | +0.026 | +0.016 | $3.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 26 | 0.307 | 0.294 | +0.033 | +0.020 | $7.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 52 | 0.568 | 0.553 | +0.030 | +0.016 | $5.64 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.79) | EVIDENCE_STRONGER | D |
- **Cale Makar: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT16PITCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (10.73 vs 4.29 bp); evidence CALIBRATION_WARNING vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: REINFORCING (phi 0.16); failure: COL offense succeeds (4+ goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT16PITCOL-PIT6|yes; why: higher confidence-adjusted growth (5.15 vs 0.25 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.894 vs 0.376); alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: PIT offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16PITCOL-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (4.55 vs 0.49 bp); alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: COL offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no; why: Player prop expression KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT16PITCOL-COLNMACKINNON29-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.79 vs 0.72 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: REINFORCING (phi 0.16); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · high event (8+) · decided (2+) 0.10.
- thesis COL:SUPPRESSED (p 0.27): highest fidelity KXNHLPTS-26OCT16PITCOL-COLCMAKAR8-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no — Player prop expression KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT16PITCOL-COLNMACKINNON29-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.79 vs 0.72 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PIT:OFFENSE_4PLUS (p 0.3429): highest fidelity KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes (same contract)
- thesis COL:OFFENSE_4PLUS (p 0.5217): highest fidelity KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes (same contract)
- KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 23% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 23.5 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5217, phi -0.259)
- KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4473, phi -0.205)
- KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.27, phi -0.207)
- KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5217, phi -0.286)
- override: Player prop expression KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no selected over player prop KXNHLAST-26OCT16PITCOL-COLNMACKINNON29-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.79 vs 0.72 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +14.43 (adj +2.32) on $50.00, P(profit) 0.6847, adj growth 18.3 bp · B EV +9.20 (adj +2.39) on $28.76, P(profit) 0.6827, adj growth 20.8 bp · C EV +10.42 (adj +2.66) on $36.99, P(profit) 0.5949, adj growth 23.2 bp · R EV +0.11 (adj +0.06) on $2.00, P(profit) 0.568, adj growth 2.1 bp

## BOS @ ANA  ·  10000 joint draws  ·  428 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.487 / away 0.513

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BOS_win | p_overtime | goals | shots ANA/BOS | ANA/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.117 | 0.59 | 0.41 | 0.00 | 6.06 | 34.2/22.1 | 19.1/29.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.53 | 0.47 | 0.00 | 6.09 | 28.6/28.0 | 24.6/24.8 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.104 | 0.62 | 0.38 | 0.00 | 9.43 | 35.8/23.7 | 18.5/28.4 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.52 | 0.48 | 0.44 | 6.01 | 34.7/22.3 | 19.1/31.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.51 | 0.49 | 0.48 | 6.04 | 28.2/27.7 | 24.3/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.55 | 0.45 | 0.00 | 9.42 | 30.2/29.6 | 23.5/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nikita Klepov: 1+ assists NO | 77 | 0.862 | 0.814 | +0.080 | +0.031 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | ANA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| A.J. Greer: 1+ goals YES | 13 | 0.233 | 0.163 | +0.095 | +0.025 | $5.16 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 62 | 0.677 | 0.660 | +0.040 | +0.024 | $16.04 | FUNDED_RESEARCH | $5 | BOS:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 10 | 0.128 | 0.119 | +0.022 | +0.012 | $3.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Nikita Klepov: 1+ assists NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT16BOSANA-ANANKLEPOV40-1|no; why: higher confidence-adjusted growth (12.75 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: ANA offense succeeds (4+ goals)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT16BOSANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (11.04 vs 2.54 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT16BOSANA-ANANKLEPOV40-1|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.03); KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: ANA offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT16BOSANA-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (5.29 vs 2.96 bp); despite a smaller raw edge (+0.040 vs +0.093/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT16BOSANA-ANANKLEPOV40-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.03); KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: BOS offense succeeds (4+ goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (11.04 vs 3.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLAST-26OCT16BOSANA-ANANKLEPOV40-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.464): highest fidelity KXNHLAST-26OCT16BOSANA-ANAJLACOMBE2-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.3744): highest fidelity KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.407): highest fidelity KXNHLGOAL-26OCT16BOSANA-BOSMKHUSNUTDINOV92-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT16BOSANA-BOSMKHUSNUTDINOV92-1|yes (same contract)
- KXNHLAST-26OCT16BOSANA-ANANKLEPOV40-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.464, phi -0.163)
- KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 66% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.8 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3312, phi -0.237)
- KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.407, phi -0.259)
- KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3312, phi -0.161)

portfolios: A EV +13.32 (adj +3.46) on $50.00, P(profit) 0.4704, adj growth 25.8 bp · B EV +7.27 (adj +2.70) on $44.46, P(profit) 0.7075, adj growth 24.2 bp · C EV +5.00 (adj +1.74) on $23.89, P(profit) 0.746, adj growth 15.2 bp · R EV +0.32 (adj +0.19) on $5.00, P(profit) 0.6768, adj growth 6.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
