# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-16T21:40:08Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +29.33 | +5.65 | +32.63 | 0.639 | -48.02 | -49.97 | 40.18 |
| B thesis-diversified (joint) ← optimiser card | 92.42 | +15.79 | +5.25 | +9.59 | 0.708 | -19.55 | -45.11 | 46.68 |
| C best expression per thesis | 75.49 | +14.19 | +4.53 | +8.19 | 0.751 | -26.11 | -34.56 | 39.93 |
| R FUNDED research stakes | 9.00 | +0.70 | +0.44 | -1.14 | 0.381 | -9.00 | -9.00 | 0.00 |

## PIT @ COL  ·  10000 joint draws  ·  446 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.648 / away 0.352

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
| Cale Makar: 3+ assists NO | 92 | 0.979 | 0.944 | +0.053 | +0.019 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DIFFUSE | NONE | EVIDENCE_MIXED | D |
| Cale Makar: 1+ assists NO | 33 | 0.555 | 0.379 | +0.210 | +0.033 | $9.59 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.77) | CALIBRATION_WARNING | D |
| Nathan MacKinnon: 1+ goals NO | 50 | 0.568 | 0.550 | +0.051 | +0.032 | $13.94 | FUNDED_RESEARCH | $4 | COL:SUPPRESSED | DIRECT (0.79) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 11 | 0.143 | 0.133 | +0.026 | +0.016 | $4.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Cale Makar: 3+ assists NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: REINFORCING (phi 0.165); KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.077); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: COL offense succeeds (4+ goals)
- **Cale Makar: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (10.73 vs 9.12 bp); evidence CALIBRATION_WARNING vs EVIDENCE_STRONGER; relationships: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-3|no: REINFORCING (phi 0.165); KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: REINFORCING (phi 0.16); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: COL offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no; why: second expression of the same thesis: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no has the higher standalone adjusted growth (10.73 vs 9.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.160); they share one thesis budget; relationships: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-3|no: MOSTLY_INDEPENDENT (phi 0.077); KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: REINFORCING (phi 0.16); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: COL offense succeeds (4+ goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes; why: higher confidence-adjusted growth (5.15 vs 1.17 bp); relationships: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-3|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · high event (8+) · decided (2+) 0.10.
- thesis COL:SUPPRESSED (p 0.27): highest fidelity KXNHLPTS-26OCT16PITCOL-COLCMAKAR8-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.3739): highest fidelity KXNHLPTS-26OCT16PITCOL-COLCMAKAR8-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.3429): highest fidelity KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT16PITCOL-COLCMAKAR8-3|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; no single thesis (diffuse); fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5217, phi -0.128)
- KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 23% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 23.5 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5217, phi -0.259)
- KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5217, phi -0.286)
- KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4473, phi -0.205)

portfolios: A EV +17.50 (adj +2.63) on $50.00, P(profit) 0.5548, adj growth 17.8 bp · B EV +9.26 (adj +2.75) on $47.54, P(profit) 0.7933, adj growth 24.4 bp · C EV +9.26 (adj +2.75) on $47.54, P(profit) 0.7933, adj growth 24.4 bp · R EV +0.39 (adj +0.25) on $4.00, P(profit) 0.568, adj growth 8.8 bp

## BOS @ ANA  ·  10000 joint draws  ·  438 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.497 / away 0.503

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BOS_win | p_overtime | goals | shots ANA/BOS | ANA/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.122 | 0.59 | 0.41 | 0.00 | 6.11 | 34.6/22.3 | 19.3/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.55 | 0.45 | 0.00 | 6.07 | 28.8/28.2 | 24.8/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.53 | 0.47 | 0.00 | 9.54 | 30.2/29.5 | 23.4/23.7 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.103 | 0.64 | 0.36 | 0.00 | 9.39 | 35.8/23.5 | 18.5/28.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.54 | 0.46 | 0.47 | 6.0 | 34.0/22.1 | 18.9/30.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.54 | 0.46 | 0.47 | 5.99 | 28.8/28.1 | 24.7/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nikita Klepov: 1+ assists NO | 77 | 0.852 | 0.808 | +0.069 | +0.026 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | ANA:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| A.J. Greer: 1+ goals YES | 14 | 0.235 | 0.170 | +0.087 | +0.022 | $4.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 62 | 0.676 | 0.661 | +0.040 | +0.024 | $16.36 | FUNDED_RESEARCH | $5 | BOS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 10 | 0.133 | 0.121 | +0.027 | +0.015 | $3.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Nikita Klepov: 1+ assists NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT16BOSANA-ANANKLEPOV40-1|no; why: higher confidence-adjusted growth (8.71 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.043); KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT16BOSANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: ANA offense succeeds (4+ goals)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT16BOSANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (7.97 vs 4.62 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT16BOSANA-ANANKLEPOV40-1|no: MOSTLY_INDEPENDENT (phi -0.043); KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT16BOSANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: ANA offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT16BOSANA-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (5.58 vs 2.18 bp); despite a smaller raw edge (+0.040 vs +0.086/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT16BOSANA-ANANKLEPOV40-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT16BOSANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: BOS offense succeeds (4+ goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (7.97 vs 5.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLAST-26OCT16BOSANA-ANANKLEPOV40-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4805): highest fidelity KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.3771): highest fidelity KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no (same contract)
- thesis GAME:HIGH_EVENT (p 0.3416): highest fidelity KXNHLTEAMTOTAL-26OCT16BOSANA-ANA3|yes [DIRECT], best adjusted EV KXNHLAST-26OCT16BOSANA-ANAJLACOMBE2-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT16BOSANA-ANANKLEPOV40-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.4805, phi -0.153)
- KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.0 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3137, phi -0.214)
- KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4104, phi -0.252)
- KXNHLGOAL-26OCT16BOSANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3137, phi -0.16)

portfolios: A EV +11.83 (adj +3.02) on $50.00, P(profit) 0.4719, adj growth 22.4 bp · B EV +6.53 (adj +2.50) on $44.88, P(profit) 0.7033, adj growth 22.3 bp · C EV +4.94 (adj +1.78) on $27.95, P(profit) 0.7395, adj growth 15.5 bp · R EV +0.31 (adj +0.19) on $5.00, P(profit) 0.676, adj growth 6.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
