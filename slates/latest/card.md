# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-16T15:54:47Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +32.31 | +9.08 | +8.57 | 0.587 | -43.10 | -62.35 | 64.76 |
| B thesis-diversified (joint) ← optimiser card | 75.82 | +15.39 | +7.07 | +9.64 | 0.625 | -27.54 | -49.94 | 62.81 |
| C best expression per thesis | 57.85 | +14.45 | +5.13 | +7.45 | 0.620 | -34.94 | -37.61 | 44.43 |
| R FUNDED research stakes | 8.00 | +0.76 | +0.49 | -1.53 | 0.395 | -8.00 | -8.00 | 0.00 |

## PIT @ COL  ·  10000 joint draws  ·  436 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_PIT_win | p_overtime | goals | shots COL/PIT | COL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.122 | 0.72 | 0.28 | 0.00 | 6.04 | 34.0/22.2 | 19.7/29.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.68 | 0.32 | 0.00 | 6.07 | 28.6/27.9 | 25.0/24.2 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.101 | 0.74 | 0.26 | 0.00 | 9.45 | 35.7/23.5 | 19.2/27.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.63 | 0.37 | 0.00 | 9.48 | 29.8/29.3 | 23.7/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.53 | 0.47 | 0.47 | 5.96 | 28.5/27.9 | 24.7/25.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.56 | 0.44 | 0.47 | 5.97 | 34.5/22.4 | 19.2/30.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cale Makar: 1+ goals NO | 76 | 0.808 | 0.795 | +0.035 | +0.022 | $20.00 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Bryan Rust: 1+ goals YES | 24 | 0.285 | 0.273 | +0.033 | +0.020 | $6.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 11 | 0.141 | 0.130 | +0.024 | +0.013 | $3.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Evgeni Malkin: 1+ assists NO | 62 | 0.696 | 0.655 | +0.059 | +0.019 | $15.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (6.03 vs 3.64 bp); despite a smaller raw edge (+0.035 vs +0.038/contract); relationships: KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: COL offense succeeds (4+ goals)
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (4.62 vs 3.83 bp); relationships: KXNHLGOAL-26OCT16PITCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.053); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes has the higher standalone adjusted growth (4.62 vs 3.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT16PITCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.046); failure: PIT offense suppressed (<= 2 goals)
- **Evgeni Malkin: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT16PITCOL-PITBRUST17-1|no; why: higher confidence-adjusted growth (3.37 vs 0.12 bp); alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT16PITCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.053); KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.046); failure: PIT offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.3368): highest fidelity KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.2806): highest fidelity KXNHLAST-26OCT16PITCOL-COLNMACKINNON29-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:SUPPRESSED (p 0.4484): highest fidelity KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no (same contract)
- KXNHLGOAL-26OCT16PITCOL-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5227, phi -0.201)
- KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4484, phi -0.26)
- KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4484, phi -0.204)
- KXNHLAST-26OCT16PITCOL-PITEMALKIN71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3368, phi -0.259)

portfolios: A EV +5.04 (adj +1.36) on $50.00, P(profit) 0.5892, adj growth 10.8 bp · B EV +3.96 (adj +1.99) on $45.82, P(profit) 0.7195, adj growth 17.5 bp · C EV +2.99 (adj +1.37) on $32.17, P(profit) 0.5347, adj growth 12.0 bp · R EV +0.23 (adj +0.14) on $5.00, P(profit) 0.8079, adj growth 5.1 bp

## BOS @ ANA  ·  10000 joint draws  ·  400 bet sides mapped, 24 +EV candidates, 4 on card


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
| A.J. Greer: 1+ goals YES | 11 | 0.256 | 0.158 | +0.139 | +0.041 | $5.68 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 32 | 0.395 | 0.375 | +0.060 | +0.040 | $11.94 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 10 | 0.143 | 0.131 | +0.036 | +0.024 | $4.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Leo Carlsson: 1+ goals YES | 32 | 0.376 | 0.360 | +0.040 | +0.025 | $7.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes; why: higher confidence-adjusted growth (34.18 vs 15.30 bp); relationships: KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT16BOSANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: ANA offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (34.18 vs 15.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.031); they share one thesis budget; relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT16BOSANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (34.18 vs 13.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.019); they share one thesis budget; relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: ANA offense suppressed (<= 2 goals)
- **Leo Carlsson: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes; why: Player prop expression KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes selected over player prop KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.51 vs 0.21 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT16BOSANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4649): highest fidelity KXNHLTEAMTOTAL-26OCT16BOSANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes — Player prop expression KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes selected over player prop KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.51 vs 0.21 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis GAME:HIGH_EVENT (p 0.3351): highest fidelity KXNHLTOTAL-26OCT16BOSANA-8|yes [STRUCTURAL], best adjusted EV KXNHLAST-26OCT16BOSANA-ANAJLACOMBE2-2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4146): highest fidelity KXNHLTOTAL-26OCT16BOSANA-6|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT16BOSANA-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 63% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.1 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3256, phi -0.232)
- KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3256, phi -0.267)
- KXNHLGOAL-26OCT16BOSANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3256, phi -0.158)
- KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3256, phi -0.266)
- override: Player prop expression KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes selected over player prop KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.51 vs 0.21 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +27.27 (adj +7.72) on $50.00, P(profit) 0.5269, adj growth 53.9 bp · B EV +11.43 (adj +5.08) on $30.00, P(profit) 0.6185, adj growth 45.3 bp · C EV +11.46 (adj +3.76) on $25.68, P(profit) 0.44, adj growth 32.4 bp · R EV +0.53 (adj +0.35) on $3.00, P(profit) 0.3948, adj growth 12.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
