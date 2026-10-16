# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-16T14:07:25Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +12.58 | +4.12 | +8.90 | 0.561 | -53.66 | -72.87 | 26.45 |
| B thesis-diversified (joint) ← optimiser card | 54.01 | +8.01 | +3.74 | +9.07 | 0.662 | -27.79 | -35.30 | 32.93 |
| C best expression per thesis | 36.57 | +5.54 | +3.14 | -0.72 | 0.388 | -36.58 | -36.58 | 27.44 |
| R FUNDED research stakes | 7.00 | +0.92 | +0.46 | +2.66 | 0.718 | -7.00 | -7.00 | 0.00 |

## PIT @ COL  ·  10000 joint draws  ·  430 bet sides mapped, 8 +EV candidates, 4 on card


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
| Nathan MacKinnon: 1+ goals NO | 50 | 0.575 | 0.554 | +0.058 | +0.037 | $19.07 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 25 | 0.307 | 0.291 | +0.043 | +0.028 | $10.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ assists NO | 40 | 0.483 | 0.436 | +0.066 | +0.020 | $10.93 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.73) | EVIDENCE_MIXED | D |
| Artturi Lehkonen: 1+ assists YES | 28 | 0.346 | 0.311 | +0.052 | +0.017 | $8.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT16PITCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (11.71 vs 3.43 bp); despite a smaller raw edge (+0.058 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT16PITCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.195); failure: COL offense succeeds (4+ goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (8.82 vs 2.85 bp); despite a smaller raw edge (+0.043 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT16PITCOL-COLNMACKINNON29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.205); KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: COL offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no has the higher standalone adjusted growth (11.71 vs 3.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.205); KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: COL offense succeeds (4+ goals)
- **Artturi Lehkonen: 1+ assists YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (8.82 vs 2.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.195); KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT16PITCOL-COLNMACKINNON29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · high event (8+) · decided (2+) 0.10.
- thesis COL:SUPPRESSED (p 0.2806): highest fidelity KXNHLAST-26OCT16PITCOL-COLNKADRI91-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:OFFENSE_4PLUS (p 0.5227): highest fidelity KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.3368): highest fidelity KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT16PITCOL-PITBRUST17-1|yes (same contract)
- KXNHLGOAL-26OCT16PITCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5227, phi -0.297)
- KXNHLGOAL-26OCT16PITCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2806, phi -0.214)
- KXNHLAST-26OCT16PITCOL-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 27% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5227, phi -0.309)
- KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2806, phi -0.244)

portfolios: A EV +6.55 (adj +2.38) on $50.00, P(profit) 0.5826, adj growth 19.9 bp · B EV +7.05 (adj +3.44) on $48.70, P(profit) 0.6033, adj growth 30.3 bp · C EV +4.33 (adj +2.71) on $33.51, P(profit) 0.7025, adj growth 23.7 bp · R EV +0.56 (adj +0.35) on $5.00, P(profit) 0.5754, adj growth 12.3 bp

## BOS @ ANA  ·  10000 joint draws  ·  394 bet sides mapped, 6 +EV candidates, 1 on card


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
| Full Game: Over 7.5 goals scored YES | 27 | 0.335 | 0.300 | +0.051 | +0.016 | $5.31 | FUNDED_RESEARCH | $2 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Full Game: Over 7.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6|yes; why: Broad expression KXNHLTOTAL-26OCT16BOSANA-8|yes selected over broad KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.37 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: only recommended bet in this game; failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis GAME:HIGH_EVENT (p 0.3351): highest fidelity KXNHLTOTAL-26OCT16BOSANA-8|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT16BOSANA-8|yes (same contract)
- thesis ANA:OFFENSE_4PLUS (p 0.4649): highest fidelity KXNHLTEAMTOTAL-26OCT16BOSANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT16BOSANA-8|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTOTAL-26OCT16BOSANA-8|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.3728, phi -0.419)
- override: Broad expression KXNHLTOTAL-26OCT16BOSANA-8|yes selected over broad KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.37 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +6.03 (adj +1.74) on $50.00, P(profit) 0.5053, adj growth 6.5 bp · B EV +0.96 (adj +0.30) on $5.31, P(profit) 0.3351, adj growth 2.7 bp · C EV +1.21 (adj +0.43) on $3.06, P(profit) 0.1335, adj growth 3.7 bp · R EV +0.36 (adj +0.11) on $2.00, P(profit) 0.3351, adj growth 3.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
