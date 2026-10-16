# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-16T17:55:59Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +35.37 | +8.39 | +21.03 | 0.673 | -39.25 | -58.85 | 63.51 |
| B thesis-diversified (joint) ← optimiser card | 84.45 | +24.89 | +9.05 | +25.88 | 0.709 | -32.82 | -55.15 | 78.84 |
| C best expression per thesis | 65.28 | +20.48 | +5.80 | +22.17 | 0.695 | -31.94 | -43.12 | 50.39 |
| R FUNDED research stakes | 6.00 | +1.43 | +0.93 | -6.00 | 0.484 | -6.00 | -6.00 | 0.00 |

## PIT @ COL  ·  10000 joint draws  ·  438 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.650 / away 0.350

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_PIT_win | p_overtime | goals | shots COL/PIT | COL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.124 | 0.71 | 0.29 | 0.00 | 6.07 | 34.0/22.0 | 19.5/29.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.68 | 0.32 | 0.00 | 6.05 | 28.5/27.9 | 25.1/24.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.098 | 0.73 | 0.27 | 0.00 | 9.38 | 35.4/23.4 | 19.0/27.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.64 | 0.36 | 0.00 | 9.45 | 30.3/29.5 | 24.3/23.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.59 | 0.41 | 0.48 | 5.94 | 34.4/22.5 | 19.3/30.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.53 | 0.47 | 0.45 | 5.95 | 28.2/28.0 | 24.7/24.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Fedor Svechkov: 1+ goals YES | 10 | 0.144 | 0.131 | +0.038 | +0.024 | $6.38 | FUNDED_RESEARCH | $2 | COL:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ assists NO | 35 | 0.557 | 0.398 | +0.191 | +0.032 | $12.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.77) | CALIBRATION_WARNING | D |
| Connor Dewar: 1+ goals YES | 11 | 0.143 | 0.132 | +0.026 | +0.015 | $4.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Evgeni Malkin: 1+ assists NO | 62 | 0.695 | 0.655 | +0.059 | +0.019 | $14.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
- **Fedor Svechkov: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (13.42 vs 1.21 bp); relationships: KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.04); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: COL offense suppressed (<= 2 goals)
- **Cale Makar: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT16PITCOL-COLCMAKAR8-2|no; why: higher confidence-adjusted growth (9.70 vs 3.46 bp); relationships: KXNHLGOAL-26OCT16PITCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.04); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: COL offense succeeds (4+ goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT16PITCOL-PITECHINAKHOV59-1|yes; why: higher confidence-adjusted growth (4.86 vs 1.19 bp); despite a smaller raw edge (+0.026 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT16PITCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.047); failure: PIT offense suppressed (<= 2 goals)
- **Evgeni Malkin: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT16PITCOL-PITBRUST17-1|no; why: higher confidence-adjusted growth (3.32 vs 0.02 bp); alternative not eligible: confidence-adjusted EV +0.0014 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT16PITCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.047); failure: PIT offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · high event (8+) · decided (2+) 0.10.
- thesis COL:SUPPRESSED (p 0.2769): highest fidelity KXNHLPTS-26OCT16PITCOL-COLCMAKAR8-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.3342): highest fidelity KXNHLAST-26OCT16PITCOL-PITECHINAKHOV59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:SUPPRESSED (p 0.4479): highest fidelity KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no (same contract)
- KXNHLGOAL-26OCT16PITCOL-COLFSVECHKOV9-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2769, phi -0.146)
- KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 23% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 21.2 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.518, phi -0.278)
- KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4479, phi -0.21)
- KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3342, phi -0.262)

portfolios: A EV +13.33 (adj +2.34) on $50.00, P(profit) 0.6658, adj growth 18.4 bp · B EV +10.89 (adj +3.50) on $36.95, P(profit) 0.5398, adj growth 30.4 bp · C EV +8.96 (adj +2.20) on $34.99, P(profit) 0.6129, adj growth 19.2 bp · R EV +0.71 (adj +0.46) on $2.00, P(profit) 0.1443, adj growth 15.0 bp

## BOS @ ANA  ·  10000 joint draws  ·  406 bet sides mapped, 25 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.487 / away 0.513

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BOS_win | p_overtime | goals | shots ANA/BOS | ANA/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.116 | 0.61 | 0.39 | 0.00 | 6.05 | 34.3/22.0 | 19.1/29.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.53 | 0.47 | 0.00 | 6.06 | 28.6/28.0 | 24.5/24.9 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.101 | 0.60 | 0.40 | 0.00 | 9.28 | 35.8/23.6 | 18.5/28.5 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.56 | 0.44 | 0.46 | 5.99 | 34.6/22.5 | 19.3/31.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.48 | 0.52 | 0.45 | 5.98 | 28.5/27.9 | 24.6/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.54 | 0.46 | 0.00 | 9.48 | 30.2/29.5 | 23.6/23.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 11 | 0.256 | 0.158 | +0.139 | +0.041 | $6.86 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 32 | 0.395 | 0.375 | +0.060 | +0.040 | $14.26 | FUNDED_RESEARCH | $4 | ANA:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Charlie McAvoy: 1+ assists NO | 58 | 0.674 | 0.624 | +0.077 | +0.027 | $17.50 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Leo Carlsson: 1+ goals YES | 32 | 0.376 | 0.360 | +0.040 | +0.025 | $8.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes; why: higher confidence-adjusted growth (34.18 vs 15.30 bp); relationships: KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLAST-26OCT16BOSANA-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: ANA offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (34.18 vs 15.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.031); they share one thesis budget; relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLAST-26OCT16BOSANA-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: ANA offense suppressed (<= 2 goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no; why: higher confidence-adjusted growth (6.79 vs 2.47 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: BOS offense succeeds (4+ goals)
- **Leo Carlsson: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes; why: Player prop expression KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes selected over player prop KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.51 vs 0.21 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT16BOSANA-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4649): highest fidelity KXNHLTEAMTOTAL-26OCT16BOSANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes — Player prop expression KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes selected over player prop KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.51 vs 0.21 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis BOS:SUPPRESSED (p 0.3728): highest fidelity KXNHLAST-26OCT16BOSANA-BOSCMCAVOY73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT16BOSANA-BOSCMCAVOY73-1|no (same contract)
- thesis GAME:HIGH_EVENT (p 0.3351): highest fidelity KXNHLTOTAL-26OCT16BOSANA-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT16BOSANA-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 63% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.1 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3256, phi -0.232)
- KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3256, phi -0.267)
- KXNHLAST-26OCT16BOSANA-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4146, phi -0.246)
- KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3256, phi -0.266)
- override: Player prop expression KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes selected over player prop KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.51 vs 0.21 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +22.04 (adj +6.05) on $50.00, P(profit) 0.4909, adj growth 45.1 bp · B EV +13.99 (adj +5.55) on $47.50, P(profit) 0.6061, adj growth 48.5 bp · C EV +11.53 (adj +3.60) on $30.29, P(profit) 0.7563, adj growth 31.2 bp · R EV +0.71 (adj +0.47) on $4.00, P(profit) 0.3948, adj growth 16.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
