# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-16T15:07:14Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +27.62 | +8.14 | +15.56 | 0.615 | -41.06 | -57.06 | 62.63 |
| B thesis-diversified (joint) ← optimiser card | 72.63 | +16.22 | +7.41 | +13.42 | 0.590 | -33.88 | -55.62 | 64.64 |
| C best expression per thesis | 65.92 | +13.56 | +5.05 | +6.33 | 0.640 | -28.56 | -42.57 | 43.83 |
| R FUNDED research stakes | 8.00 | +1.07 | +0.69 | -0.42 | 0.395 | -8.00 | -8.00 | 0.00 |

## PIT @ COL  ·  10000 joint draws  ·  436 bet sides mapped, 12 +EV candidates, 4 on card


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
| Nathan MacKinnon: 1+ goals NO | 51 | 0.575 | 0.556 | +0.048 | +0.029 | $15.06 | FUNDED_RESEARCH | $4 | COL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Fedor Svechkov: 1+ goals YES | 10 | 0.133 | 0.122 | +0.027 | +0.016 | $4.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Bryan Rust: 1+ goals YES | 24 | 0.285 | 0.273 | +0.033 | +0.020 | $6.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 26 | 0.307 | 0.292 | +0.033 | +0.019 | $6.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT16PITCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (7.42 vs 1.27 bp); despite a smaller raw edge (+0.048 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT16PITCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: COL offense succeeds (4+ goals)
- **Fedor Svechkov: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (5.82 vs 3.95 bp); despite a smaller raw edge (+0.027 vs +0.033/contract); relationships: KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: COL offense suppressed (<= 2 goals)
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16PITCOL-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (4.62 vs 3.83 bp); relationships: KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT16PITCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PIT offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (3.95 vs 1.29 bp); despite a smaller raw edge (+0.033 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT16PITCOL-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · high event (8+) · decided (2+) 0.10.
- thesis COL:SUPPRESSED (p 0.2806): highest fidelity KXNHLAST-26OCT16PITCOL-COLNKADRI91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.3368): highest fidelity KXNHLGOAL-26OCT16PITCOL-PITRRAKELL67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:OFFENSE_4PLUS (p 0.5227): highest fidelity KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5227, phi -0.297)
- KXNHLGOAL-26OCT16PITCOL-COLFSVECHKOV9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2806, phi -0.129)
- KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4484, phi -0.26)
- KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2806, phi -0.214)

portfolios: A EV +4.94 (adj +1.57) on $50.00, P(profit) 0.5348, adj growth 12.7 bp · B EV +3.99 (adj +2.39) on $31.80, P(profit) 0.4187, adj growth 20.8 bp · C EV +4.17 (adj +2.12) on $40.71, P(profit) 0.6498, adj growth 18.5 bp · R EV +0.36 (adj +0.22) on $4.00, P(profit) 0.5754, adj growth 7.7 bp

## BOS @ ANA  ·  10000 joint draws  ·  400 bet sides mapped, 21 +EV candidates, 4 on card


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
| Beckett Sennecke: 1+ goals YES | 32 | 0.395 | 0.375 | +0.060 | +0.040 | $14.22 | FUNDED_RESEARCH | $4 | ANA:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Leo Carlsson: 1+ goals YES | 32 | 0.376 | 0.360 | +0.040 | +0.025 | $8.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 62 | 0.665 | 0.653 | +0.029 | +0.016 | $10.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes; why: higher confidence-adjusted growth (34.18 vs 15.30 bp); relationships: KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: ANA offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (34.18 vs 15.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.031); they share one thesis budget; relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: ANA offense suppressed (<= 2 goals)
- **Leo Carlsson: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes; why: Player prop expression KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes selected over player prop KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.51 vs 0.21 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: ANA offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT16BOSANA-BOSCMCAVOY73-1|no; why: Player prop expression KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT16BOSANA-BOSCMCAVOY73-2|no because adjusted EV is 0.5 pts higher while thesis capture is 0.82 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: BOS offense succeeds (4+ goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4649): highest fidelity KXNHLTEAMTOTAL-26OCT16BOSANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes — Player prop expression KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes selected over player prop KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.51 vs 0.21 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis GAME:HIGH_EVENT (p 0.3351): highest fidelity KXNHLTOTAL-26OCT16BOSANA-8|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT16BOSANA-ANA3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4146): highest fidelity KXNHLTOTAL-26OCT16BOSANA-6|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT16BOSANA-8|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT16BOSANA-ANAAGREER18-1|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 63% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.1 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3256, phi -0.232)
- KXNHLGOAL-26OCT16BOSANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3256, phi -0.267)
- KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3256, phi -0.266)
- KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4146, phi -0.244)
- override: Player prop expression KXNHLGOAL-26OCT16BOSANA-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT16BOSANA-BOSCMCAVOY73-2|no because adjusted EV is 0.5 pts higher while thesis capture is 0.82 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT16BOSANA-ANALCARLSSON91-1|yes selected over player prop KXNHLGOAL-26OCT16BOSANA-ANATWASHE42-1|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.51 vs 0.21 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +22.67 (adj +6.57) on $50.00, P(profit) 0.5915, adj growth 49.9 bp · B EV +12.23 (adj +5.02) on $40.83, P(profit) 0.667, adj growth 43.8 bp · C EV +9.39 (adj +2.93) on $25.21, P(profit) 0.3742, adj growth 25.3 bp · R EV +0.71 (adj +0.47) on $4.00, P(profit) 0.3948, adj growth 16.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
