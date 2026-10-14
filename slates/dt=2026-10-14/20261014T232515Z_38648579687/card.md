# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-14T23:25:15Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +16.86 | +5.99 | +12.68 | 0.600 | -43.02 | -63.11 | 47.26 |
| B thesis-diversified (joint) ← optimiser card | 81.55 | +14.55 | +7.57 | +11.01 | 0.532 | -35.63 | -38.39 | 64.99 |
| C best expression per thesis | 39.50 | +6.96 | +3.17 | +10.37 | 0.576 | -17.66 | -39.51 | 27.55 |
| R FUNDED research stakes | 8.00 | +2.71 | +1.77 | -0.23 | 0.296 | -8.00 | -8.00 | 0.00 |

## MTL @ WSH  ·  10000 joint draws  ·  500 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_MTL_win | p_overtime | goals | shots WSH/MTL | WSH/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.52 | 0.48 | 0.00 | 6.03 | 27.3/27.0 | 23.5/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.49 | 0.51 | 0.46 | 5.91 | 27.4/27.2 | 24.0/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.53 | 0.47 | 0.00 | 9.25 | 28.9/28.8 | 22.6/22.8 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.090 | 0.60 | 0.40 | 0.00 | 6.02 | 32.5/21.8 | 18.8/28.2 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.54 | 0.46 | 0.45 | 5.93 | 32.3/21.7 | 18.5/28.9 | even strength |
| WSH shot control · high event (8+) · decided (2+) | 0.059 | 0.62 | 0.38 | 0.00 | 9.2 | 34.4/23.2 | 18.2/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 18 | 0.239 | 0.223 | +0.048 | +0.032 | $9.97 | FUNDED_RESEARCH | $3 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 31 | 0.393 | 0.347 | +0.068 | +0.022 | $7.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
| Justin Sourdif: 1+ goals YES | 13 | 0.162 | 0.152 | +0.024 | +0.015 | $3.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Full Game: Over 5.5 goals scored NO | 37 | 0.430 | 0.398 | +0.044 | +0.011 | $9.68 | FUNDED_RESEARCH | $3 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (14.71 vs 4.67 bp); despite a smaller raw edge (+0.048 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLGOAL-26OCT14MTLWSH-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLTOTAL-26OCT14MTLWSH-6|no: INTENTIONAL_DIVERSIFIER (phi -0.149); failure: WSH offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (14.71 vs 4.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.039); they share one thesis budget; relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLGOAL-26OCT14MTLWSH-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi 0.118); KXNHLTOTAL-26OCT14MTLWSH-6|no: INTENTIONAL_DIVERSIFIER (phi -0.213); failure: WSH offense suppressed (<= 2 goals)
- **Justin Sourdif: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (14.71 vs 3.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.118); KXNHLTOTAL-26OCT14MTLWSH-6|no: INTENTIONAL_DIVERSIFIER (phi -0.132); failure: WSH offense suppressed (<= 2 goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTOTAL-26OCT14MTLWSH-5|no; why: Broad expression KXNHLTOTAL-26OCT14MTLWSH-6|no selected over broad KXNHLTOTAL-26OCT14MTLWSH-5|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.149); KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.213); KXNHLGOAL-26OCT14MTLWSH-WSHJSOURDIF34-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.132); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.4057): highest fidelity KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:SUPPRESSED (p 0.3754): highest fidelity KXNHLTOTAL-26OCT14MTLWSH-6|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT14MTLWSH-5|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:LOW_EVENT (p 0.2337): highest fidelity KXNHLTOTAL-26OCT14MTLWSH-6|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT14MTLWSH-5|no — Broad expression KXNHLTOTAL-26OCT14MTLWSH-6|no selected over broad KXNHLTOTAL-26OCT14MTLWSH-5|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT14MTLWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3754, phi -0.242)
- KXNHLAST-26OCT14MTLWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 43% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3754, phi -0.298)
- KXNHLGOAL-26OCT14MTLWSH-WSHJSOURDIF34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3754, phi -0.186)
- KXNHLTOTAL-26OCT14MTLWSH-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2693, phi -0.528)
- override: Broad expression KXNHLTOTAL-26OCT14MTLWSH-6|no selected over broad KXNHLTOTAL-26OCT14MTLWSH-5|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +10.04 (adj +4.14) on $50.00, P(profit) 0.4819, adj growth 32.1 bp · B EV +5.98 (adj +2.93) on $31.55, P(profit) 0.405, adj growth 25.4 bp · C EV +3.73 (adj +2.10) on $14.81, P(profit) 0.4231, adj growth 18.2 bp · R EV +1.10 (adj +0.60) on $6.00, P(profit) 0.5977, adj growth 19.8 bp

## DAL @ COL  ·  10000 joint draws  ·  480 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.588 / away 0.412

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_DAL_win | p_overtime | goals | shots COL/DAL | COL/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.129 | 0.70 | 0.30 | 0.00 | 5.99 | 32.7/21.1 | 18.6/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.64 | 0.36 | 0.00 | 6.0 | 27.1/26.7 | 23.9/23.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.55 | 0.45 | 0.49 | 5.9 | 32.9/21.2 | 18.1/29.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.53 | 0.47 | 0.48 | 5.9 | 27.5/26.9 | 23.5/24.2 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.077 | 0.70 | 0.30 | 0.00 | 9.25 | 34.6/22.6 | 18.1/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.63 | 0.37 | 0.00 | 9.26 | 28.9/28.3 | 23.0/22.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Josh Manson: 1+ goals YES | 4 | 0.077 | 0.068 | +0.034 | +0.025 | $5.43 | FUNDED_RESEARCH | $2 | COL:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 3+ assists NO | 92 | 0.970 | 0.942 | +0.044 | +0.017 | $19.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Devon Toews: 1+ assists YES | 30 | 0.386 | 0.341 | +0.072 | +0.026 | $8.97 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Tyler Seguin: 1+ assists NO | 71 | 0.780 | 0.740 | +0.056 | +0.016 | $15.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Josh Manson: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT14DALCOL-COLDTOEWS7-1|yes; why: higher confidence-adjusted growth (31.57 vs 6.79 bp); despite a smaller raw edge (+0.034 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT14DALCOL-COLNMACKINNON29-3|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT14DALCOL-COLDTOEWS7-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT14DALCOL-DALTSEGUIN91-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: COL offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 3+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT14DALCOL-COLNMACKINNON29-2|no; why: higher confidence-adjusted growth (9.48 vs 0.86 bp); despite a smaller raw edge (+0.044 vs +0.122/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT14DALCOL-COLJMANSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT14DALCOL-COLDTOEWS7-1|yes: MOSTLY_INDEPENDENT (phi -0.044); KXNHLAST-26OCT14DALCOL-DALTSEGUIN91-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: COL offense succeeds (4+ goals)
- **Devon Toews: 1+ assists YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT14DALCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (6.79 vs 1.20 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT14DALCOL-COLJMANSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT14DALCOL-COLNMACKINNON29-3|no: MOSTLY_INDEPENDENT (phi -0.044); KXNHLAST-26OCT14DALCOL-DALTSEGUIN91-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: COL offense suppressed (<= 2 goals)
- **Tyler Seguin: 1+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no; why: higher confidence-adjusted growth (2.71 vs 2.54 bp); relationships: KXNHLGOAL-26OCT14DALCOL-COLJMANSON42-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT14DALCOL-COLNMACKINNON29-3|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT14DALCOL-COLDTOEWS7-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: DAL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4441): highest fidelity KXNHLAST-26OCT14DALCOL-COLDTOEWS7-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT14DALCOL-COLDTOEWS7-1|yes (same contract)
- thesis DAL:SUPPRESSED (p 0.4873): highest fidelity KXNHLAST-26OCT14DALCOL-DALJROBERTSON21-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT14DALCOL-DALRHINTZ24-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.3357): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT14DALCOL-COLJMANSON42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.101)
- KXNHLAST-26OCT14DALCOL-COLNMACKINNON29-3|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4441, phi -0.166)
- KXNHLAST-26OCT14DALCOL-COLDTOEWS7-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3357, phi -0.269)
- KXNHLAST-26OCT14DALCOL-DALTSEGUIN91-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3011, phi -0.23)

portfolios: A EV +6.82 (adj +1.85) on $50.00, P(profit) 0.6022, adj growth 15.2 bp · B EV +8.57 (adj +4.64) on $50.00, P(profit) 0.432, adj growth 39.6 bp · C EV +3.24 (adj +1.07) on $24.69, P(profit) 0.3863, adj growth 9.4 bp · R EV +1.61 (adj +1.17) on $2.00, P(profit) 0.077, adj growth 35.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
