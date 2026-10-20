# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-20T13:53:48Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +44.25 | +15.71 | +32.43 | 0.731 | -30.12 | -44.74 | 135.44 |
| B thesis-diversified (joint) ← optimiser card | 147.06 | +28.37 | +13.14 | +25.38 | 0.729 | -25.25 | -37.35 | 121.79 |
| C best expression per thesis | 150.00 | +36.15 | +14.92 | +32.37 | 0.725 | -32.13 | -46.75 | 133.92 |
| R FUNDED research stakes | 27.00 | +5.85 | +2.40 | +3.33 | 0.634 | -7.55 | -10.23 | 0.00 |

## SJS @ MTL  ·  10000 joint draws  ·  394 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_SJS_win | p_overtime | goals | shots MTL/SJS | MTL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.64 | 0.36 | 0.00 | 6.02 | 27.1/27.2 | 24.2/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.54 | 0.46 | 0.49 | 5.94 | 27.3/27.2 | 23.9/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.61 | 0.39 | 0.00 | 9.32 | 28.7/28.6 | 23.3/22.2 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.076 | 0.72 | 0.28 | 0.00 | 6.03 | 32.2/21.5 | 19.0/27.4 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.067 | 0.57 | 0.43 | 0.00 | 5.98 | 21.5/32.0 | 28.6/17.9 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.56 | 0.44 | 0.41 | 5.86 | 32.1/21.7 | 18.7/28.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mason Marchment: 1+ goals YES | 17 | 0.234 | 0.217 | +0.054 | +0.037 | $5.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Kiefer Sherwood: 1+ goals YES | 16 | 0.198 | 0.187 | +0.028 | +0.018 | $2.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ goals NO | 55 | 0.602 | 0.588 | +0.035 | +0.020 | $6.41 | FUNDED_RESEARCH | $2 | MTL:SUPPRESSED | DIRECT (0.79) | EVIDENCE_STRONGER | D |
| Zachary Bolduc: 1+ goals NO | 76 | 0.802 | 0.788 | +0.029 | +0.015 | $9.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20SJMTL-SJKSHERWOOD44-1|yes; why: higher confidence-adjusted growth (20.03 vs 4.82 bp); relationships: KXNHLGOAL-26OCT20SJMTL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT20SJMTL-MTLZBOLDUC76-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: SJS offense suppressed (<= 2 goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes has the higher standalone adjusted growth (20.03 vs 4.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT20SJMTL-MTLZBOLDUC76-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: SJS offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20SJMTL-MTL2|no; why: higher confidence-adjusted growth (3.72 vs 2.86 bp); despite a smaller raw edge (+0.035 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.016 vs 0.883); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT20SJMTL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT20SJMTL-MTLZBOLDUC76-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: MTL offense succeeds (4+ goals)
- **Zachary Bolduc: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no has the higher standalone adjusted growth (3.72 vs 2.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20SJMTL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:OFFENSE_4PLUS (p 0.3286): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3265): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4256): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20SJMTL-MTL2|no (same contract)
- KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.459, phi -0.244)
- KXNHLGOAL-26OCT20SJMTL-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.459, phi -0.214)
- KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4635, phi -0.254)
- KXNHLGOAL-26OCT20SJMTL-MTLZBOLDUC76-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4635, phi -0.195)

portfolios: A EV +1.97 (adj +0.96) on $15.28, P(profit) 0.6533, adj growth 8.9 bp · B EV +2.84 (adj +1.82) on $23.80, P(profit) 0.371, adj growth 16.9 bp · C EV +3.21 (adj +2.00) on $19.90, P(profit) 0.542, adj growth 17.9 bp · R EV +0.12 (adj +0.07) on $2.00, P(profit) 0.602, adj growth 2.6 bp

## COL @ NJD  ·  10000 joint draws  ·  440 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_COL_win | p_overtime | goals | shots NJD/COL | NJD/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.48 | 0.52 | 0.00 | 5.97 | 28.6/28.7 | 25.2/25.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.47 | 0.53 | 0.47 | 5.88 | 28.8/29.0 | 25.9/25.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.46 | 0.54 | 0.00 | 9.23 | 30.3/30.4 | 23.9/24.4 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.073 | 0.41 | 0.59 | 0.00 | 6.0 | 23.0/34.0 | 29.8/20.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.45 | 0.55 | 0.48 | 5.92 | 23.2/34.3 | 31.0/20.2 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.061 | 0.53 | 0.47 | 0.00 | 6.0 | 33.9/23.1 | 19.7/29.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins 1st Period by over 1.5 goals YES | 4 | 0.113 | 0.062 | +0.070 | +0.020 | $1.36 | FUNDED_RESEARCH | $1 | COL:SCORES_FIRST | FRAGILE (0.21) | EVIDENCE_THIN | D |
| Fedor Svechkov: 1+ goals YES | 8 | 0.118 | 0.107 | +0.033 | +0.022 | $2.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ assists NO | 44 | 0.602 | 0.493 | +0.145 | +0.036 | $10.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 65 | 0.696 | 0.682 | +0.030 | +0.016 | $5.77 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Colorado wins 1st Period by over 1.5 goals YES** — thesis: COL scores first; alternative: KXNHLSPREAD-26OCT20COLNJ-NJ2|no; why: higher confidence-adjusted growth (19.59 vs 0.00 bp); evidence EVIDENCE_THIN vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi 0.048); KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: INTENTIONAL_DIVERSIFIER (phi -0.113); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.049); failure: NJD scores first
- **Fedor Svechkov: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes; why: second expression of the same thesis: KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes has the higher standalone adjusted growth (19.59 vs 13.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.048); they share one thesis budget; relationships: KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes: MOSTLY_INDEPENDENT (phi 0.048); KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: INTENTIONAL_DIVERSIFIER (phi -0.063); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: COL offense suppressed (<= 2 goals)
- **Cale Makar: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20COLNJ-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (11.58 vs 1.87 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes: INTENTIONAL_DIVERSIFIER (phi -0.113); KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.063); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: COL offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20COLNJ-NJTMEIER28-1|no; why: higher confidence-adjusted growth (2.55 vs 0.70 bp); alternative not eligible: confidence-adjusted EV +0.0076 below the 0.010/contract floor; relationships: KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis COL:SCORES_FIRST (p 0.5089): highest fidelity KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes [FRAGILE], best adjusted EV KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes (same contract)
- thesis COL:OFFENSE_4PLUS (p 0.3914): highest fidelity KXNHLGOAL-26OCT20COLNJ-COLGLANDESKOG92-1|yes [FRAGILE], best adjusted EV KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.3869): highest fidelity KXNHLGOAL-26OCT20COLNJ-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes: FUNDED_RESEARCH; family MIXED; loses 79% of the draws where the thesis happens; opposing: failure thesis NJD:SCORES_FIRST (p 0.4897, phi -0.315)
- KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3869, phi -0.141)
- KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.7 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3914, phi -0.273)
- KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3638, phi -0.249)

portfolios: A EV +9.29 (adj +2.92) on $15.28, P(profit) 0.5553, adj growth 24.2 bp · B EV +6.86 (adj +2.33) on $20.22, P(profit) 0.7106, adj growth 21.6 bp · C EV +8.04 (adj +2.21) on $23.94, P(profit) 0.6647, adj growth 20.0 bp · R EV +1.74 (adj +0.51) on $3.00, P(profit) 0.7232, adj growth 15.9 bp

## ANA @ NYI  ·  10000 joint draws  ·  388 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_ANA_win | p_overtime | goals | shots NYI/ANA | NYI/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.60 | 0.40 | 0.00 | 6.02 | 27.7/27.8 | 24.7/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.53 | 0.47 | 0.48 | 5.94 | 27.9/28.1 | 24.8/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.62 | 0.38 | 0.00 | 9.4 | 29.5/29.5 | 24.0/22.4 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.071 | 0.59 | 0.41 | 0.00 | 6.02 | 22.2/32.7 | 29.4/18.4 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.48 | 0.52 | 0.48 | 5.93 | 22.4/33.0 | 29.4/19.2 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.061 | 0.65 | 0.35 | 0.00 | 6.08 | 32.4/22.1 | 19.3/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 13 | 0.207 | 0.184 | +0.069 | +0.046 | $6.18 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT20ANANYI-9|yes; why: higher confidence-adjusted growth (37.96 vs 0.48 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.903 vs 0.367); alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3427): highest fidelity KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes (same contract)
- KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4325, phi -0.236)

portfolios: A EV +3.07 (adj +2.05) on $6.11, P(profit) 0.2071, adj growth 18.9 bp · B EV +3.10 (adj +2.07) on $6.18, P(profit) 0.2071, adj growth 19.1 bp · C EV +4.38 (adj +2.92) on $8.74, P(profit) 0.2071, adj growth 26.0 bp · R EV +1.00 (adj +0.67) on $2.00, P(profit) 0.2071, adj growth 24.1 bp

## LAK @ WSH  ·  10000 joint draws  ·  414 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_LAK_win | p_overtime | goals | shots WSH/LAK | WSH/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.61 | 0.39 | 0.00 | 5.98 | 27.3/27.6 | 24.5/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.55 | 0.45 | 0.45 | 5.88 | 27.4/27.6 | 24.4/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.64 | 0.36 | 0.00 | 9.13 | 28.9/28.8 | 23.8/22.1 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.49 | 0.51 | 0.47 | 5.9 | 21.8/32.6 | 29.2/18.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.074 | 0.56 | 0.44 | 0.00 | 5.95 | 21.9/32.4 | 29.2/18.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.62 | 0.38 | 0.00 | 3.5 | 26.1/26.2 | 24.5/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 4 | 0.065 | 0.058 | +0.022 | +0.015 | $1.80 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 19 | 0.238 | 0.218 | +0.037 | +0.018 | $2.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 53 | 0.639 | 0.558 | +0.092 | +0.011 | $4.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20LAWSH-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (11.53 vs 0.86 bp); alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.086); failure: LAK offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-2|yes; why: higher confidence-adjusted growth (4.21 vs 0.16 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.902 vs 0.761); alternative not eligible: confidence-adjusted EV +0.0022 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20LAWSH-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: WSH offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHL3PTOTAL-26OCT20LAWSH-3|no; why: higher confidence-adjusted growth (1.06 vs 0.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT20LAWSH-LAJEDMUNDSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.086); KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.07.
- thesis WSH:OFFENSE_4PLUS (p 0.4029): highest fidelity KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes (same contract)
- thesis LAK:SUPPRESSED (p 0.4854): highest fidelity KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.3007): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT20LAWSH-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4854, phi -0.116)
- KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3754, phi -0.234)
- KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3007, phi -0.284)

portfolios: A EV +2.63 (adj +1.06) on $11.46, P(profit) 0.2869, adj growth 9.7 bp · B EV +2.14 (adj +0.95) on $8.63, P(profit) 0.2869, adj growth 8.8 bp · C EV +1.50 (adj +0.43) on $8.58, P(profit) 0.725, adj growth 3.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ CBJ  ·  10000 joint draws  ·  388 bet sides mapped, 10 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_TOR_win | p_overtime | goals | shots CBJ/TOR | CBJ/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CBJ shot control · normal event (5-7) · decided (2+) | 0.134 | 0.72 | 0.28 | 0.00 | 5.98 | 34.1/22.1 | 19.6/29.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.67 | 0.33 | 0.00 | 5.99 | 29.1/28.4 | 25.6/25.0 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.59 | 0.41 | 0.47 | 5.84 | 34.4/22.3 | 19.3/30.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.53 | 0.47 | 0.45 | 5.86 | 29.0/28.3 | 25.1/25.6 | even strength |
| CBJ shot control · high event (8+) · decided (2+) | 0.077 | 0.71 | 0.29 | 0.00 | 9.1 | 36.2/23.6 | 19.3/28.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.066 | 0.66 | 0.34 | 0.00 | 9.18 | 30.2/29.6 | 24.4/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Auston Matthews: 2+ assists NO | 88 | 0.935 | 0.900 | +0.047 | +0.013 | $10.49 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Mathieu Olivier: 1+ goals YES | 19 | 0.231 | 0.217 | +0.030 | +0.016 | $2.56 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Toronto over 2.5 goals scored NO | 43 | 0.505 | 0.462 | +0.058 | +0.015 | $4.60 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
- **Auston Matthews: 2+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT20TORCBJ-7|no; why: higher confidence-adjusted growth (3.46 vs 2.68 bp); despite a smaller raw edge (+0.047 vs +0.058/contract); wins across more scripts (relative breadth 0.99 vs 0.749); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no: REINFORCING (phi 0.217); failure: TOR offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no; why: higher confidence-adjusted growth (3.43 vs 2.04 bp); despite a smaller raw edge (+0.030 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.853 vs 0.748); relationships: KXNHLAST-26OCT20TORCBJ-TORAMATTHEWS34-2|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no: MOSTLY_INDEPENDENT (phi 0.069); failure: CBJ offense suppressed (<= 2 goals)
- **Toronto over 2.5 goals scored NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20TORCBJ-TORAMATTHEWS34-2|no; why: second expression of the same thesis: KXNHLAST-26OCT20TORCBJ-TORAMATTHEWS34-2|no has the higher standalone adjusted growth (3.46 vs 2.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.217); they share one thesis budget; relationships: KXNHLAST-26OCT20TORCBJ-TORAMATTHEWS34-2|no: REINFORCING (phi 0.217); KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.069); failure: TOR offense succeeds (4+ goals)

**Review**: scripts CBJ shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TOR:SCORES_FIRST (p 0.4412): highest fidelity KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes [FRAGILE], best adjusted EV KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.5171): highest fidelity KXNHLAST-26OCT20TORCBJ-TORAMATTHEWS34-2|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT20TORCBJ-7|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.3886): highest fidelity KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT20TORCBJ-TORAMATTHEWS34-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2745, phi -0.246)
- KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3359, phi -0.229)
- KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no: FUNDED_RESEARCH; family MIXED; loses 2% of the draws where the thesis happens; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2745, phi -0.621)

portfolios: A EV +10.43 (adj +2.95) on $15.28, P(profit) 0.5971, adj growth 22.1 bp · B EV +1.53 (adj +0.51) on $17.66, P(profit) 0.5848, adj growth 4.7 bp · C EV +5.89 (adj +1.83) on $28.81, P(profit) 0.713, adj growth 16.5 bp · R EV +0.26 (adj +0.07) on $2.00, P(profit) 0.5047, adj growth 2.3 bp

## WPG @ STL  ·  10000 joint draws  ·  434 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_WPG_win | p_overtime | goals | shots STL/WPG | STL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.134 | 0.65 | 0.35 | 0.00 | 6.04 | 26.5/26.5 | 23.5/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.46 | 5.91 | 26.4/26.4 | 23.2/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.64 | 0.36 | 0.00 | 9.24 | 28.0/28.0 | 22.9/21.0 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.077 | 0.68 | 0.32 | 0.00 | 6.03 | 30.8/20.9 | 18.3/26.2 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.58 | 0.42 | 0.47 | 5.89 | 31.3/21.2 | 18.1/28.0 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.059 | 0.57 | 0.43 | 0.00 | 6.01 | 21.1/31.1 | 27.8/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Morgan Barron: 1+ goals YES | 7 | 0.124 | 0.108 | +0.050 | +0.034 | $4.00 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Philip Broberg: 1+ assists YES | 33 | 0.405 | 0.362 | +0.059 | +0.017 | $3.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (34.13 vs 0.01 bp); alternative not eligible: confidence-adjusted EV +0.0012 below the 0.010/contract floor; relationships: KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: WPG offense suppressed (<= 2 goals)
- **Philip Broberg: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (2.71 vs 0.49 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20WPGSTL-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis STL:OFFENSE_4PLUS (p 0.4452): highest fidelity KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3123): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT20WPGSTL-WPGMBARRON36-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4685, phi -0.177)
- KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 45% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3423, phi -0.271)

portfolios: A EV +3.77 (adj +2.14) on $10.21, P(profit) 0.4809, adj growth 19.5 bp · B EV +3.23 (adj +1.96) on $7.31, P(profit) 0.4809, adj growth 18.0 bp · C EV +0.77 (adj +0.22) on $4.53, P(profit) 0.4045, adj growth 2.0 bp · R EV +0.67 (adj +0.45) on $1.00, P(profit) 0.1242, adj growth 16.5 bp

## BOS @ DAL  ·  10000 joint draws  ·  420 bet sides mapped, 9 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_BOS_win | p_overtime | goals | shots DAL/BOS | DAL/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.53 | 0.47 | 0.00 | 6.0 | 26.4/25.9 | 22.5/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.48 | 5.98 | 26.7/26.2 | 22.9/23.3 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.102 | 0.60 | 0.40 | 0.00 | 6.02 | 31.6/20.8 | 17.8/27.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.52 | 0.48 | 0.48 | 5.88 | 31.7/20.8 | 17.7/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.54 | 0.46 | 0.00 | 9.26 | 28.3/27.9 | 22.1/22.2 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.066 | 0.60 | 0.40 | 0.00 | 9.13 | 33.2/22.0 | 17.0/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Morgan Geekie: 1+ goals YES | 24 | 0.299 | 0.283 | +0.046 | +0.030 | $4.28 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Boston over 2.5 goals scored YES | 51 | 0.595 | 0.550 | +0.068 | +0.023 | $2.65 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 75 | 0.810 | 0.777 | +0.046 | +0.014 | $4.08 | FUNDED_RESEARCH | $2 | BOS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Morgan Geekie: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes; why: higher confidence-adjusted growth (10.49 vs 4.97 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.913 vs 0.358); relationships: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: REINFORCING (phi 0.253); KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.131); failure: BOS offense suppressed (<= 2 goals)
- **Boston over 2.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes has the higher standalone adjusted growth (10.49 vs 4.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.253); they share one thesis budget; relationships: KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes: REINFORCING (phi 0.253); KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: REINFORCING (phi 0.402); failure: BOS offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: BOS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes; why: Broad expression KXNHLSPREAD-26OCT20BOSDAL-DAL3|no selected over player prop KXNHLAST-26OCT20BOSDAL-DALRHINTZ24-1|no because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.84 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes: MOSTLY_INDEPENDENT (phi 0.131); KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: REINFORCING (phi 0.402); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.3577): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2541): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes kept
- thesis BOS:WINS (p 0.4741): highest fidelity KXNHLSPREAD-26OCT20BOSDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4174, phi -0.26)
- KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.4174, phi -0.974)
- KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3031, phi -0.735)
- override: Broad expression KXNHLSPREAD-26OCT20BOSDAL-DAL3|no selected over player prop KXNHLAST-26OCT20BOSDAL-DALRHINTZ24-1|no because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.84 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes kept

portfolios: A EV +1.77 (adj +0.49) on $15.28, P(profit) 0.5016, adj growth 4.4 bp · B EV +1.37 (adj +0.70) on $11.01, P(profit) 0.299, adj growth 6.6 bp · C EV +2.28 (adj +1.14) on $15.64, P(profit) 0.3358, adj growth 10.3 bp · R EV +0.25 (adj +0.08) on $3.00, P(profit) 0.5595, adj growth 3.0 bp

## MIN @ EDM  ·  10000 joint draws  ·  452 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_MIN_win | p_overtime | goals | shots EDM/MIN | EDM/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.62 | 0.38 | 0.00 | 6.05 | 28.6/28.4 | 25.3/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.113 | 0.64 | 0.36 | 0.00 | 9.45 | 30.3/30.2 | 24.6/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.55 | 0.45 | 0.47 | 5.98 | 28.4/28.4 | 25.0/25.2 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.082 | 0.70 | 0.30 | 0.00 | 6.07 | 33.7/22.7 | 20.0/29.0 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.069 | 0.72 | 0.28 | 0.00 | 9.46 | 35.1/24.2 | 19.6/26.7 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.58 | 0.42 | 0.50 | 5.94 | 33.9/22.9 | 19.7/30.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 14 | 0.192 | 0.175 | +0.043 | +0.026 | $3.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Zach Hyman: 1+ goals YES | 31 | 0.370 | 0.353 | +0.045 | +0.029 | $5.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ assists NO | 40 | 0.483 | 0.436 | +0.066 | +0.020 | $3.83 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.69) | EVIDENCE_MIXED | D |
| Kirill Kaprizov: 1+ goals NO | 58 | 0.627 | 0.614 | +0.030 | +0.017 | $4.19 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes; why: higher confidence-adjusted growth (11.90 vs 8.09 bp); despite a smaller raw edge (+0.043 vs +0.045/contract); relationships: KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: EDM offense suppressed (<= 2 goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (11.90 vs 8.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: EDM offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no; why: higher confidence-adjusted growth (3.50 vs 2.57 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no: REINFORCING (phi 0.251); failure: MIN offense succeeds (4+ goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no; why: second expression of the same thesis: KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no has the higher standalone adjusted growth (3.50 vs 2.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.251); they share one thesis budget; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: REINFORCING (phi 0.251); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.5018): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3227): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT20MINEDM-EDM6|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4289): highest fidelity KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2953, phi -0.184)
- KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2953, phi -0.252)
- KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 31% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3548, phi -0.318)
- KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3548, phi -0.306)

portfolios: A EV +2.54 (adj +1.16) on $15.28, P(profit) 0.5241, adj growth 10.8 bp · B EV +2.66 (adj +1.45) on $17.22, P(profit) 0.4163, adj growth 13.5 bp · C EV +3.15 (adj +1.43) on $13.43, P(profit) 0.6439, adj growth 12.9 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.6268, adj growth 2.0 bp

## DET @ SEA  ·  10000 joint draws  ·  388 bet sides mapped, 5 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_DET_win | p_overtime | goals | shots SEA/DET | SEA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.64 | 0.36 | 0.00 | 6.05 | 27.8/28.2 | 25.3/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.46 | 5.92 | 27.8/28.1 | 24.8/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.64 | 0.36 | 0.00 | 9.28 | 29.3/29.7 | 24.4/22.1 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.093 | 0.56 | 0.44 | 0.00 | 5.99 | 22.1/33.3 | 30.0/18.5 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.49 | 0.51 | 0.47 | 5.79 | 22.3/33.8 | 30.7/19.2 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.055 | 0.56 | 0.44 | 0.00 | 9.17 | 24.0/35.4 | 29.2/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Detroit wins by over 1.5 goals NO | 71 | 0.783 | 0.744 | +0.059 | +0.020 | $7.15 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Detroit wins by over 2.5 goals NO | 82 | 0.875 | 0.845 | +0.044 | +0.015 | $5.59 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Detroit wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT20DETSEA-DET3|no; why: higher confidence-adjusted growth (4.27 vs 3.32 bp); relationships: KXNHLSPREAD-26OCT20DETSEA-DET3|no: DUPLICATIVE (phi 0.719); failure: DET wins by 2+
- **Detroit wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT20DETSEA-DET2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT20DETSEA-DET2|no has the higher standalone adjusted growth (4.27 vs 3.32 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.719); they share one thesis budget; relationships: KXNHLSPREAD-26OCT20DETSEA-DET2|no: DUPLICATIVE (phi 0.719); failure: DET wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:WINS (p 0.5826): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no (same contract)
- thesis DET:SUPPRESSED (p 0.4646): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.3551): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no (same contract)
- KXNHLSPREAD-26OCT20DETSEA-DET2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2168, phi -1.0)
- KXNHLSPREAD-26OCT20DETSEA-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2168, phi -0.719)

portfolios: A EV +1.43 (adj +0.37) on $15.28, P(profit) 0.6325, adj growth 3.1 bp · B EV +0.88 (adj +0.29) on $12.74, P(profit) 0.7832, adj growth 2.7 bp · C EV +1.19 (adj +0.40) on $14.64, P(profit) 0.7832, adj growth 3.6 bp · R EV +0.27 (adj +0.09) on $4.00, P(profit) 0.7832, adj growth 3.3 bp

## CAR @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 17 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CAR_win | p_overtime | goals | shots VAN/CAR | VAN/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.171 | 0.37 | 0.63 | 0.00 | 6.02 | 20.9/34.4 | 30.0/18.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.145 | 0.47 | 0.53 | 0.45 | 5.94 | 21.3/34.7 | 31.2/18.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.132 | 0.37 | 0.63 | 0.00 | 9.36 | 22.2/35.6 | 27.9/17.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.083 | 0.46 | 0.54 | 0.00 | 6.02 | 26.6/27.8 | 24.1/23.0 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.074 | 0.39 | 0.61 | 0.00 | 3.5 | 19.9/32.6 | 30.3/18.3 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.068 | 0.46 | 0.54 | 0.47 | 2.86 | 19.7/32.8 | 31.3/18.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 1.5 goals NO | 49 | 0.656 | 0.545 | +0.149 | +0.037 | $6.58 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 1.5 goals scored YES | 71 | 0.799 | 0.752 | +0.075 | +0.028 | $7.65 | FUNDED_RESEARCH | $2 | VAN:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 64 | 0.775 | 0.684 | +0.119 | +0.028 | $1.40 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: Broad expression KXNHLSPREAD-26OCT20CARVAN-CAR2|no selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no because adjusted EV is 1.9 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes: REINFORCING (phi 0.431); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: DUPLICATIVE (phi 0.745); failure: CAR wins by 2+
- **Vancouver over 1.5 goals scored YES** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.431); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: REINFORCING (phi 0.403); failure: VAN offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: Broad expression KXNHLSPREAD-26OCT20CARVAN-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-CAR2|no because adjusted EV is 0.6 pts higher while thesis capture is 1.00 vs 0.43 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT20CARVAN-CAR2|no: DUPLICATIVE (phi 0.745); KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes: REINFORCING (phi 0.403); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:OFFENSE_4PLUS (p 0.3646): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no — Broad expression KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis VAN:WINS_BY_2PLUS (p 0.2337): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- thesis VAN:WINS (p 0.4398): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- KXNHLSPREAD-26OCT20CARVAN-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 17.1 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3436, phi -1.0)
- KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis VAN:SUPPRESSED (p 0.4241, phi -0.584)
- KXNHLSPREAD-26OCT20CARVAN-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.0 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3436, phi -0.745)
- override: Broad expression KXNHLSPREAD-26OCT20CARVAN-CAR2|no selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no because adjusted EV is 1.9 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26OCT20CARVAN-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-CAR2|no because adjusted EV is 0.6 pts higher while thesis capture is 1.00 vs 0.43 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT20CARVAN-VAN3|yes less than the minimum stake; KXNHL1PSPREAD-26OCT20CARVAN-VAN2|yes kept

portfolios: A EV +5.32 (adj +1.06) on $15.28, P(profit) 0.5027, adj growth 9.3 bp · B EV +2.97 (adj +0.84) on $15.63, P(profit) 0.6064, adj growth 7.9 bp · C EV +4.94 (adj +2.11) on $6.49, P(profit) 0.2432, adj growth 18.8 bp · R EV +0.97 (adj +0.27) on $5.00, P(profit) 0.6564, adj growth 9.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT20CARVAN-VAN|yes == KXNHLGAME-26OCT20CARVAN-CAR|no

## TBL @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TBL_win | p_overtime | goals | shots VGK/TBL | VGK/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.62 | 0.38 | 0.00 | 6.02 | 26.7/26.8 | 23.7/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.54 | 0.46 | 0.45 | 5.9 | 26.7/26.7 | 23.4/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.65 | 0.35 | 0.00 | 9.3 | 28.3/28.3 | 23.0/21.2 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.072 | 0.56 | 0.44 | 0.00 | 6.01 | 21.7/31.9 | 28.6/18.0 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.069 | 0.72 | 0.28 | 0.00 | 5.99 | 31.5/21.3 | 18.8/26.7 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.53 | 0.47 | 0.49 | 5.85 | 21.6/31.9 | 28.6/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay over 2.5 goals scored NO | 39 | 0.468 | 0.424 | +0.061 | +0.017 | $1.53 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Tampa Bay over 1.5 goals scored NO | 18 | 0.238 | 0.204 | +0.048 | +0.014 | $1.13 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | FRAGILE (0.50) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 1.5 goals NO | 73 | 0.793 | 0.756 | +0.049 | +0.013 | $4.00 | FUNDED_RESEARCH | $1 | VGK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay over 2.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no; why: higher confidence-adjusted growth (2.74 vs 2.73 bp); wins across more scripts (relative breadth 0.78 vs 0.608); relationships: KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no: DUPLICATIVE (phi 0.597); KXNHLSPREAD-26OCT20TBVGK-TB2|no: DUPLICATIVE (phi 0.441); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay over 1.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT20TBVGK-TB3|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT20TBVGK-TB3|no has the higher standalone adjusted growth (2.74 vs 2.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.597); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT20TBVGK-TB3|no: DUPLICATIVE (phi 0.597); KXNHLSPREAD-26OCT20TBVGK-TB2|no: REINFORCING (phi 0.286); failure: TBL wins (incl. OT/SO)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: VGK wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20TBVGK-TB3|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT20TBVGK-TB3|no has the higher standalone adjusted growth (2.74 vs 1.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.441); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT20TBVGK-TB3|no: DUPLICATIVE (phi 0.441); KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no: REINFORCING (phi 0.286); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis TBL:SUPPRESSED (p 0.4798): highest fidelity KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20TBVGK-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:WINS (p 0.5885): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20TBVGK-TB3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT20TBVGK-TB3|no: FUNDED_RESEARCH; family MIXED; loses 2% of the draws where the thesis happens; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3059, phi -0.623)
- KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no: FUNDED_RESEARCH; family MIXED; loses 50% of the draws where the thesis happens; opposing: failure thesis TBL:WINS (p 0.4115, phi -0.435)
- KXNHLSPREAD-26OCT20TBVGK-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2073, phi -1.0)

portfolios: A EV +2.03 (adj +0.55) on $15.28, P(profit) 0.4681, adj growth 4.6 bp · B EV +0.78 (adj +0.22) on $6.66, P(profit) 0.4603, adj growth 2.0 bp · C EV +0.80 (adj +0.23) on $5.30, P(profit) 0.4681, adj growth 2.1 bp · R EV +0.47 (adj +0.13) on $3.00, P(profit) 0.4603, adj growth 4.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
