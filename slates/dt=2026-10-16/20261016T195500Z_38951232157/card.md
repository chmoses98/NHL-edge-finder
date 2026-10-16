# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-16T19:55:00Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +27.91 | +5.59 | +29.03 | 0.646 | -43.39 | -62.73 | 38.93 |
| B thesis-diversified (joint) ← optimiser card | 70.00 | +16.95 | +5.43 | +12.45 | 0.680 | -23.72 | -44.44 | 47.63 |
| C best expression per thesis | 67.30 | +15.53 | +4.82 | +16.86 | 0.647 | -29.17 | -40.03 | 41.98 |
| R FUNDED research stakes | 4.00 | +1.62 | +0.56 | -4.00 | 0.344 | -4.00 | -4.00 | 0.00 |

## PIT @ COL  ·  10000 joint draws  ·  446 bet sides mapped, 16 +EV candidates, 4 on card

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
| Cale Makar: 1+ assists NO | 34 | 0.555 | 0.390 | +0.200 | +0.034 | $12.86 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.77) | CALIBRATION_WARNING | D |
| Connor Dewar: 1+ goals YES | 11 | 0.143 | 0.133 | +0.026 | +0.016 | $4.12 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 26 | 0.307 | 0.294 | +0.033 | +0.020 | $7.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Evgeni Malkin: 1+ assists NO | 62 | 0.694 | 0.654 | +0.057 | +0.018 | $13.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Cale Makar: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (11.25 vs 4.85 bp); evidence CALIBRATION_WARNING vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: COL offense succeeds (4+ goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes; why: higher confidence-adjusted growth (5.15 vs 1.47 bp); relationships: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.035); failure: PIT offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (4.55 vs 2.71 bp); despite a smaller raw edge (+0.033 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: COL offense suppressed (<= 2 goals)
- **Evgeni Malkin: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT16PITCOL-PITBRUST17-1|no; why: higher confidence-adjusted growth (3.01 vs 0.34 bp); alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PIT offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · high event (8+) · decided (2+) 0.10.
- thesis COL:SUPPRESSED (p 0.27): highest fidelity KXNHLPTS-26OCT16PITCOL-COLCMAKAR8-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.3429): highest fidelity KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:OFFENSE_4PLUS (p 0.5217): highest fidelity KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 23% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 22.1 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5217, phi -0.259)
- KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4473, phi -0.205)
- KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.27, phi -0.207)
- KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3429, phi -0.264)

portfolios: A EV +16.08 (adj +2.57) on $50.00, P(profit) 0.5477, adj growth 16.5 bp · B EV +10.27 (adj +2.73) on $37.72, P(profit) 0.5949, adj growth 23.8 bp · C EV +10.27 (adj +2.73) on $37.72, P(profit) 0.5949, adj growth 23.8 bp · R EV +0.45 (adj +0.27) on $2.00, P(profit) 0.1434, adj growth 8.0 bp

## BOS @ ANA  ·  10000 joint draws  ·  428 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.501 / away 0.499

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
| A.J. Greer: 1+ goals YES | 14 | 0.235 | 0.170 | +0.087 | +0.022 | $4.96 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 10 | 0.134 | 0.123 | +0.028 | +0.017 | $4.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Beckett Sennecke: First Goalscorer YES | 5 | 0.069 | 0.065 | +0.016 | +0.011 | $2.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:SCORES_FIRST | FRAGILE (0.13) | EVIDENCE_MIXED | D |
- **Nikita Klepov: 1+ assists NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT16BOSANA-ANANKLEPOV40-1|no; why: higher confidence-adjusted growth (8.71 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.043); KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLFIRSTGOAL-26OCT16BOSANA-ANABSENNECKE45|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: ANA offense succeeds (4+ goals)
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT16BOSANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (7.97 vs 4.62 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT16BOSANA-ANANKLEPOV40-1|no: MOSTLY_INDEPENDENT (phi -0.043); KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLFIRSTGOAL-26OCT16BOSANA-ANABSENNECKE45|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: ANA offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (7.97 vs 6.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLAST-26OCT16BOSANA-ANANKLEPOV40-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLFIRSTGOAL-26OCT16BOSANA-ANABSENNECKE45|yes: MOSTLY_INDEPENDENT (phi -0.024); failure: ANA offense suppressed (<= 2 goals)
- **Beckett Sennecke: First Goalscorer YES** — thesis: ANA scores first; alternative: KXNHLTEAMTOTAL-26OCT16BOSANA-ANA2|yes; why: higher confidence-adjusted growth (5.38 vs 1.29 bp); despite a smaller raw edge (+0.016 vs +0.033/contract); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLAST-26OCT16BOSANA-ANANKLEPOV40-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.024); failure: BOS scores first

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4805): highest fidelity KXNHLAST-26OCT16BOSANA-ANAJLACOMBE2-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:SCORES_FIRST (p 0.5279): highest fidelity KXNHLFIRSTGOAL-26OCT16BOSANA-ANABSENNECKE45|yes [FRAGILE], best adjusted EV KXNHLFIRSTGOAL-26OCT16BOSANA-ANABSENNECKE45|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.3771): highest fidelity KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no (same contract)
- KXNHLAST-26OCT16BOSANA-ANANKLEPOV40-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.4805, phi -0.153)
- KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 67% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.0 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3137, phi -0.214)
- KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3137, phi -0.143)
- KXNHLFIRSTGOAL-26OCT16BOSANA-ANABSENNECKE45|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family MIXED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SCORES_FIRST (p 0.4711, phi -0.257)

portfolios: A EV +11.83 (adj +3.02) on $50.00, P(profit) 0.4719, adj growth 22.4 bp · B EV +6.69 (adj +2.70) on $32.28, P(profit) 0.3862, adj growth 23.8 bp · C EV +5.26 (adj +2.09) on $29.58, P(profit) 0.384, adj growth 18.2 bp · R EV +1.17 (adj +0.29) on $2.00, P(profit) 0.2351, adj growth 9.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
