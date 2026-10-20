# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-20T14:44:09Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.98 | +45.63 | +16.73 | +33.18 | 0.750 | -23.95 | -37.76 | 147.67 |
| B thesis-diversified (joint) ← optimiser card | 148.97 | +26.78 | +14.25 | +21.50 | 0.722 | -20.87 | -30.72 | 134.18 |
| C best expression per thesis | 149.99 | +37.32 | +15.21 | +32.31 | 0.745 | -27.43 | -41.78 | 138.00 |
| R FUNDED research stakes | 29.00 | +4.02 | +2.13 | +1.82 | 0.601 | -6.44 | -8.75 | 0.00 |

## SJS @ MTL  ·  10000 joint draws  ·  394 bet sides mapped, 8 +EV candidates, 4 on card


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
| Mason Marchment: 1+ goals YES | 18 | 0.234 | 0.218 | +0.044 | +0.028 | $3.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Kiefer Sherwood: 1+ goals YES | 16 | 0.198 | 0.187 | +0.028 | +0.018 | $1.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ goals NO | 55 | 0.602 | 0.588 | +0.035 | +0.020 | $4.78 | FUNDED_RESEARCH | $2 | MTL:SUPPRESSED | DIRECT (0.79) | EVIDENCE_STRONGER | D |
| Zachary Bolduc: 1+ goals NO | 76 | 0.802 | 0.788 | +0.029 | +0.015 | $6.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20SJMTL-SJKSHERWOOD44-1|yes; why: higher confidence-adjusted growth (10.90 vs 4.82 bp); relationships: KXNHLGOAL-26OCT20SJMTL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT20SJMTL-MTLZBOLDUC76-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: SJS offense suppressed (<= 2 goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes has the higher standalone adjusted growth (10.90 vs 4.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT20SJMTL-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT20SJMTL-MTLZBOLDUC76-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: SJS offense suppressed (<= 2 goals)
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

portfolios: A EV +1.27 (adj +0.34) on $14.62, P(profit) 0.6106, adj growth 2.9 bp · B EV +1.61 (adj +0.97) on $16.81, P(profit) 0.6589, adj growth 9.2 bp · C EV +2.06 (adj +1.15) on $16.63, P(profit) 0.542, adj growth 10.5 bp · R EV +0.12 (adj +0.07) on $2.00, P(profit) 0.602, adj growth 2.6 bp

## COL @ NJD  ·  10000 joint draws  ·  462 bet sides mapped, 9 +EV candidates, 4 on card


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
| Fedor Svechkov: 1+ goals YES | 8 | 0.119 | 0.108 | +0.034 | +0.023 | $2.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ assists NO | 44 | 0.606 | 0.495 | +0.149 | +0.038 | $7.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 64 | 0.696 | 0.679 | +0.040 | +0.023 | $6.73 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Parker Kelly: 1+ goals YES | 10 | 0.128 | 0.120 | +0.022 | +0.013 | $1.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Fedor Svechkov: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes; why: KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes has the higher standalone adjusted growth (19.59 vs 14.62 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.088); relationships: KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT20COLNJ-COLPKELLY17-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: COL offense suppressed (<= 2 goals)
- **Cale Makar: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20COLNJ-COLCMAKAR8-2|no; why: higher confidence-adjusted growth (12.52 vs 0.50 bp); alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT20COLNJ-COLPKELLY17-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.062); failure: COL offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.84 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT20COLNJ-COLPKELLY17-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: NJD offense succeeds (4+ goals)
- **Parker Kelly: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes; why: KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes has the higher standalone adjusted growth (19.59 vs 4.11 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.050); relationships: KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: INTENTIONAL_DIVERSIFIER (phi -0.062); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: COL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis COL:SCORES_FIRST (p 0.5089): highest fidelity KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes [FRAGILE], best adjusted EV KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes (same contract)
- thesis COL:OFFENSE_4PLUS (p 0.3914): highest fidelity KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes [FRAGILE], best adjusted EV KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes (same contract)
- thesis COL:SUPPRESSED (p 0.3869): highest fidelity KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no (same contract)
- KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3869, phi -0.148)
- KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.1 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3914, phi -0.27)
- KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3638, phi -0.249)
- KXNHLGOAL-26OCT20COLNJ-COLPKELLY17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3869, phi -0.156)
- override: Player prop expression KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no selected over player prop KXNHLAST-26OCT20COLNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.84 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +8.57 (adj +2.21) on $14.62, P(profit) 0.4518, adj growth 18.8 bp · B EV +3.96 (adj +1.63) on $17.67, P(profit) 0.5479, adj growth 15.5 bp · C EV +9.43 (adj +2.37) on $23.33, P(profit) 0.6671, adj growth 21.6 bp · R EV +0.12 (adj +0.07) on $2.00, P(profit) 0.696, adj growth 2.7 bp

## ANA @ NYI  ·  10000 joint draws  ·  388 bet sides mapped, 2 +EV candidates, 2 on card


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
| A.J. Greer: 1+ goals YES | 12 | 0.207 | 0.183 | +0.080 | +0.055 | $5.34 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Jackson LaCombe: 1+ goals YES | 11 | 0.136 | 0.128 | +0.019 | +0.011 | $1.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20ANANYI-ANA6|yes; why: higher confidence-adjusted growth (57.97 vs 0.04 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.903 vs 0.325); alternative not eligible: confidence-adjusted EV +0.0011 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20ANANYI-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: ANA offense suppressed (<= 2 goals)
- **Jackson LaCombe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes has the higher standalone adjusted growth (57.97 vs 2.76 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3427): highest fidelity KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes (same contract)
- KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4325, phi -0.236)
- KXNHLGOAL-26OCT20ANANYI-ANAJLACOMBE2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4325, phi -0.175)

portfolios: A EV +3.92 (adj +2.70) on $7.44, P(profit) 0.3129, adj growth 25.2 bp · B EV +3.53 (adj +2.43) on $6.46, P(profit) 0.3129, adj growth 22.8 bp · C EV +5.68 (adj +3.95) on $9.08, P(profit) 0.2071, adj growth 35.4 bp · R EV +1.25 (adj +0.87) on $2.00, P(profit) 0.2071, adj growth 31.6 bp

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
| Joel Edmundson: 1+ goals YES | 4 | 0.065 | 0.058 | +0.022 | +0.015 | $1.34 | FUNDED_RESEARCH | $1 | LAK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 19 | 0.238 | 0.222 | +0.037 | +0.021 | $2.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 53 | 0.639 | 0.558 | +0.092 | +0.011 | $3.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20LAWSH-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (11.53 vs 0.47 bp); despite a smaller raw edge (+0.023 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.086); failure: LAK offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20LAWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (6.19 vs 0.18 bp); despite a smaller raw edge (+0.037 vs +0.039/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20LAWSH-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: WSH offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20LAWSH-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (1.06 vs 0.23 bp); alternative not eligible: confidence-adjusted EV +0.0033 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20LAWSH-LAJEDMUNDSON6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.086); KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.07.
- thesis WSH:OFFENSE_4PLUS (p 0.4029): highest fidelity KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes (same contract)
- thesis LAK:SUPPRESSED (p 0.4854): highest fidelity KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.3007): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT20LAWSH-LAJEDMUNDSON6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4854, phi -0.116)
- KXNHLGOAL-26OCT20LAWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3754, phi -0.234)
- KXNHLAST-26OCT20LAWSH-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3007, phi -0.284)

portfolios: A EV +2.51 (adj +1.08) on $10.96, P(profit) 0.2869, adj growth 10.0 bp · B EV +1.68 (adj +0.79) on $6.88, P(profit) 0.2869, adj growth 7.5 bp · C EV +1.48 (adj +0.53) on $8.43, P(profit) 0.2379, adj growth 4.9 bp · R EV +0.53 (adj +0.35) on $1.00, P(profit) 0.0652, adj growth 11.5 bp

## TOR @ CBJ  ·  10000 joint draws  ·  388 bet sides mapped, 13 +EV candidates, 4 on card


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
| Mathieu Olivier: 1+ goals YES | 19 | 0.231 | 0.218 | +0.030 | +0.017 | $2.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Jack Roslovic: 1+ goals NO | 76 | 0.802 | 0.790 | +0.029 | +0.017 | $6.50 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 25 | 0.295 | 0.281 | +0.032 | +0.018 | $2.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Full Game: Over 5.5 goals scored NO | 40 | 0.472 | 0.434 | +0.056 | +0.017 | $3.49 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no; why: higher confidence-adjusted growth (3.99 vs 2.04 bp); despite a smaller raw edge (+0.030 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.853 vs 0.748); relationships: KXNHLGOAL-26OCT20TORCBJ-TORJROSLOVIC96-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLTOTAL-26OCT20TORCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.135); failure: CBJ offense suppressed (<= 2 goals)
- **Jack Roslovic: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT20TORCBJ-6|no; why: higher confidence-adjusted growth (3.80 vs 2.58 bp); despite a smaller raw edge (+0.029 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.993 vs 0.767); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLTOTAL-26OCT20TORCBJ-6|no: REINFORCING (phi 0.162); failure: TOR offense succeeds (4+ goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (3.99 vs 3.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT20TORCBJ-TORJROSLOVIC96-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLTOTAL-26OCT20TORCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.18); failure: CBJ offense suppressed (<= 2 goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no; why: higher confidence-adjusted growth (2.58 vs 2.04 bp); despite a smaller raw edge (+0.056 vs +0.058/contract); relationships: KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.135); KXNHLGOAL-26OCT20TORCBJ-TORJROSLOVIC96-1|no: REINFORCING (phi 0.162); KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.18); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts CBJ shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TOR:SCORES_FIRST (p 0.4412): highest fidelity KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes [FRAGILE], best adjusted EV KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.3886): highest fidelity KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:OFFENSE_4PLUS (p 0.4466): highest fidelity KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes (same contract)
- KXNHLGOAL-26OCT20TORCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3359, phi -0.229)
- KXNHLGOAL-26OCT20TORCBJ-TORJROSLOVIC96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2745, phi -0.215)
- KXNHLGOAL-26OCT20TORCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3359, phi -0.239)
- KXNHLTOTAL-26OCT20TORCBJ-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4466, phi -0.539)

portfolios: A EV +9.89 (adj +2.76) on $14.62, P(profit) 0.6083, adj growth 21.0 bp · B EV +1.39 (adj +0.68) on $15.07, P(profit) 0.6635, adj growth 6.4 bp · C EV +5.02 (adj +1.76) on $23.37, P(profit) 0.5897, adj growth 16.0 bp · R EV +0.21 (adj +0.09) on $3.00, P(profit) 0.4112, adj growth 3.2 bp

## WPG @ STL  ·  10000 joint draws  ·  434 bet sides mapped, 4 +EV candidates, 4 on card


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
| Morgan Barron: 1+ goals YES | 5 | 0.124 | 0.104 | +0.071 | +0.051 | $3.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Dalibor Dvorsky: 1+ goals NO | 81 | 0.857 | 0.844 | +0.036 | +0.023 | $7.82 | FUNDED_RESEARCH | $2 | STL:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Philip Broberg: 1+ assists YES | 33 | 0.405 | 0.365 | +0.059 | +0.019 | $2.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
| Mark Scheifele: 1+ goals YES | 28 | 0.316 | 0.304 | +0.022 | +0.010 | $1.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (102.49 vs 1.10 bp); relationships: KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20WPGSTL-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: WPG offense suppressed (<= 2 goals)
- **Dalibor Dvorsky: 1+ goals NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20WPGSTL-STLMMCTAVISH83-1|no; why: higher confidence-adjusted growth (7.86 vs 0.57 bp); despite a smaller raw edge (+0.036 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20WPGSTL-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.057); KXNHLGOAL-26OCT20WPGSTL-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: STL offense succeeds (4+ goals)
- **Philip Broberg: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (3.58 vs 0.69 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20WPGSTL-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: INTENTIONAL_DIVERSIFIER (phi -0.057); KXNHLGOAL-26OCT20WPGSTL-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: STL offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20WPGSTL-WPGAIAFALLO9-1|yes; why: higher confidence-adjusted growth (1.10 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.031/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT20WPGSTL-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis STL:OFFENSE_4PLUS (p 0.4452): highest fidelity KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3123): highest fidelity KXNHLGOAL-26OCT20WPGSTL-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20WPGSTL-WPGMSCHEIFELE55-1|yes (same contract)
- thesis STL:SUPPRESSED (p 0.3423): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT20WPGSTL-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4685, phi -0.177)
- KXNHLGOAL-26OCT20WPGSTL-STLDDVORSKY15-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4452, phi -0.175)
- KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 45% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3423, phi -0.271)
- KXNHLGOAL-26OCT20WPGSTL-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4685, phi -0.286)

portfolios: A EV +6.55 (adj +4.37) on $14.62, P(profit) 0.4401, adj growth 40.3 bp · B EV +6.16 (adj +4.19) on $15.98, P(profit) 0.4212, adj growth 38.8 bp · C EV +0.97 (adj +0.34) on $6.99, P(profit) 0.5924, adj growth 3.1 bp · R EV +0.09 (adj +0.06) on $2.00, P(profit) 0.8565, adj growth 2.2 bp

## BOS @ DAL  ·  10000 joint draws  ·  420 bet sides mapped, 7 +EV candidates, 3 on card


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
| Morgan Geekie: 1+ goals YES | 24 | 0.299 | 0.283 | +0.046 | +0.030 | $3.19 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Boston over 2.5 goals scored YES | 51 | 0.595 | 0.550 | +0.068 | +0.023 | $1.97 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 75 | 0.810 | 0.777 | +0.046 | +0.014 | $3.04 | FUNDED_RESEARCH | $1 | BOS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Morgan Geekie: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes; why: higher confidence-adjusted growth (10.49 vs 4.97 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.913 vs 0.358); relationships: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: REINFORCING (phi 0.253); KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.131); failure: BOS offense suppressed (<= 2 goals)
- **Boston over 2.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes has the higher standalone adjusted growth (10.49 vs 4.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.253); they share one thesis budget; relationships: KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes: REINFORCING (phi 0.253); KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: REINFORCING (phi 0.402); failure: BOS offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: BOS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes; why: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes has the higher standalone adjusted growth (4.97 vs 2.44 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.146); relationships: KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes: MOSTLY_INDEPENDENT (phi 0.131); KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: REINFORCING (phi 0.402); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.3577): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2541): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes kept
- thesis BOS:WINS (p 0.4741): highest fidelity KXNHLSPREAD-26OCT20BOSDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20BOSDAL-BOSMGEEKIE39-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4174, phi -0.26)
- KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.4174, phi -0.974)
- KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3031, phi -0.735)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes kept

portfolios: A EV +1.95 (adj +0.78) on $14.62, P(profit) 0.4849, adj growth 7.1 bp · B EV +1.02 (adj +0.52) on $8.20, P(profit) 0.299, adj growth 5.0 bp · C EV +1.69 (adj +0.93) on $7.02, P(profit) 0.3358, adj growth 8.5 bp · R EV +0.19 (adj +0.06) on $2.00, P(profit) 0.5595, adj growth 2.3 bp

## MIN @ EDM  ·  10000 joint draws  ·  452 bet sides mapped, 8 +EV candidates, 4 on card


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
| Alex Formenton: 1+ goals YES | 14 | 0.192 | 0.175 | +0.043 | +0.026 | $2.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Zach Hyman: 1+ goals YES | 31 | 0.370 | 0.353 | +0.045 | +0.029 | $4.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 58 | 0.627 | 0.614 | +0.030 | +0.017 | $4.17 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 68 | 0.781 | 0.706 | +0.086 | +0.010 | $6.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes; why: higher confidence-adjusted growth (11.90 vs 8.09 bp); despite a smaller raw edge (+0.043 vs +0.045/contract); relationships: KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.045); failure: EDM offense suppressed (<= 2 goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (11.90 vs 8.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.178); failure: EDM offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no; why: Player prop expression KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.80 vs 0.69 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.004); failure: MIN offense succeeds (4+ goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20MINEDM-EDMLDRAISAITL29-1|no; why: higher confidence-adjusted growth (1.12 vs 0.02 bp); despite a smaller raw edge (+0.086 vs +0.086/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.178); KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.5018): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3227): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.4289): highest fidelity KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no — Player prop expression KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.80 vs 0.69 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2953, phi -0.184)
- KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2953, phi -0.252)
- KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3548, phi -0.306)
- KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.6 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5018, phi -0.336)
- override: Player prop expression KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no selected over player prop KXNHLAST-26OCT20MINEDM-MINQHUGHES43-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.80 vs 0.69 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.21 (adj +0.62) on $14.62, P(profit) 0.4532, adj growth 5.6 bp · B EV +2.45 (adj +1.12) on $17.96, P(profit) 0.4545, adj growth 10.6 bp · C EV +4.30 (adj +1.50) on $23.06, P(profit) 0.5611, adj growth 13.7 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.6268, adj growth 2.0 bp

## DET @ SEA  ·  10000 joint draws  ·  394 bet sides mapped, 8 +EV candidates, 4 on card


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
| Ryan Winterton: 1+ goals YES | 13 | 0.165 | 0.155 | +0.027 | +0.017 | $1.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 12 | 0.153 | 0.143 | +0.025 | +0.016 | $1.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Detroit wins by over 1.5 goals NO | 71 | 0.783 | 0.744 | +0.059 | +0.020 | $5.66 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Michael Rasmussen: 1+ goals NO | 85 | 0.882 | 0.873 | +0.023 | +0.014 | $7.82 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20DETSEA-DET2|no; why: higher confidence-adjusted growth (5.21 vs 4.27 bp); despite a smaller raw edge (+0.027 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT20DETSEA-DET2|no: MOSTLY_INDEPENDENT (phi 0.1); KXNHLGOAL-26OCT20DETSEA-DETMRASMUSSEN27-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20DETSEA-DET2|no; why: higher confidence-adjusted growth (4.86 vs 4.27 bp); despite a smaller raw edge (+0.025 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT20DETSEA-DET2|no: MOSTLY_INDEPENDENT (phi 0.087); KXNHLGOAL-26OCT20DETSEA-DETMRASMUSSEN27-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: SEA offense suppressed (<= 2 goals)
- **Detroit wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT20DETSEA-DET3|no; why: higher confidence-adjusted growth (4.27 vs 3.32 bp); relationships: KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.1); KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.087); KXNHLGOAL-26OCT20DETSEA-DETMRASMUSSEN27-1|no: MOSTLY_INDEPENDENT (phi 0.13); failure: DET wins by 2+
- **Michael Rasmussen: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20DETSEA-DET2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT20DETSEA-DET2|no has the higher standalone adjusted growth (4.27 vs 3.60 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.130); they share one thesis budget; relationships: KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLSPREAD-26OCT20DETSEA-DET2|no: MOSTLY_INDEPENDENT (phi 0.13); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4353): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.5826): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no (same contract)
- thesis DET:SUPPRESSED (p 0.4646): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3412, phi -0.181)
- KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3412, phi -0.172)
- KXNHLSPREAD-26OCT20DETSEA-DET2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2168, phi -1.0)
- KXNHLGOAL-26OCT20DETSEA-DETMRASMUSSEN27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3213, phi -0.166)

portfolios: A EV +1.22 (adj +0.33) on $14.62, P(profit) 0.6325, adj growth 2.9 bp · B EV +1.30 (adj +0.68) on $16.67, P(profit) 0.763, adj growth 6.4 bp · C EV +1.06 (adj +0.36) on $13.06, P(profit) 0.7832, adj growth 3.3 bp · R EV +0.22 (adj +0.09) on $4.00, P(profit) 0.7083, adj growth 3.3 bp

## CAR @ VAN  ·  10000 joint draws  ·  404 bet sides mapped, 24 +EV candidates, 4 on card


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
| Carolina wins by over 1.5 goals NO | 48 | 0.656 | 0.538 | +0.159 | +0.041 | $3.17 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 62 | 0.775 | 0.671 | +0.138 | +0.034 | $3.60 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 1.5 goals scored YES | 71 | 0.799 | 0.752 | +0.075 | +0.028 | $4.95 | FUNDED_RESEARCH | $2 | VAN:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 62 | 0.685 | 0.666 | +0.048 | +0.030 | $5.99 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Carolina wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes has the higher standalone adjusted growth (25.77 vs 14.72 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.317); relationships: KXNHLSPREAD-26OCT20CARVAN-CAR3|no: DUPLICATIVE (phi 0.745); KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes: REINFORCING (phi 0.431); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: REINFORCING (phi 0.166); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: Broad expression KXNHLSPREAD-26OCT20CARVAN-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no because adjusted EV is 0.9 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT20CARVAN-CAR2|no: DUPLICATIVE (phi 0.745); KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes: REINFORCING (phi 0.403); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.146); failure: CAR wins by 2+
- **Vancouver over 1.5 goals scored YES** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.431); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: REINFORCING (phi 0.403); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: VAN offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20CARVAN-VAN3|yes; why: KXNHLSPREAD-26OCT20CARVAN-VAN3|yes has the higher standalone adjusted growth (22.40 vs 8.32 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.122); relationships: KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.166); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:OFFENSE_4PLUS (p 0.3646): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no — Broad expression KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis VAN:WINS_BY_2PLUS (p 0.2337): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- thesis VAN:WINS (p 0.4398): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- KXNHLSPREAD-26OCT20CARVAN-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 18.1 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3436, phi -1.0)
- KXNHLSPREAD-26OCT20CARVAN-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.0 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3436, phi -0.745)
- KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis VAN:SUPPRESSED (p 0.4241, phi -0.584)
- KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4561, phi -0.236)
- override: Broad expression KXNHLSPREAD-26OCT20CARVAN-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no because adjusted EV is 0.9 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.80 (adj +1.00) on $14.62, P(profit) 0.5461, adj growth 9.1 bp · B EV +2.76 (adj +0.92) on $17.71, P(profit) 0.6952, adj growth 8.9 bp · C EV +4.41 (adj +1.88) on $5.79, P(profit) 0.2432, adj growth 17.0 bp · R EV +0.89 (adj +0.31) on $6.00, P(profit) 0.6952, adj growth 11.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT20CARVAN-VAN|yes == KXNHLGAME-26OCT20CARVAN-CAR|no

## TBL @ VGK  ·  10000 joint draws  ·  414 bet sides mapped, 4 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TBL_win | p_overtime | goals | shots VGK/TBL | VGK/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.63 | 0.37 | 0.00 | 6.04 | 26.8/26.8 | 23.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.54 | 0.46 | 0.49 | 5.9 | 26.8/27.1 | 23.9/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.64 | 0.36 | 0.00 | 9.21 | 28.2/28.2 | 23.2/21.3 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.069 | 0.59 | 0.41 | 0.00 | 6.02 | 21.4/31.9 | 28.6/17.6 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.066 | 0.70 | 0.30 | 0.00 | 6.0 | 31.0/21.2 | 18.5/26.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.59 | 0.41 | 0.00 | 3.44 | 25.5/25.6 | 24.1/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 1.5 goals NO | 71 | 0.792 | 0.748 | +0.067 | +0.024 | $7.55 | FUNDED_RESEARCH | $2 | VGK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 3.5 goals scored NO | 60 | 0.685 | 0.637 | +0.068 | +0.021 | $2.00 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: VGK wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no; why: higher confidence-adjusted growth (6.32 vs 3.96 bp); despite a smaller raw edge (+0.067 vs +0.068/contract); relationships: KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no: REINFORCING (phi 0.513); failure: TBL wins by 2+
- **Tampa Bay over 3.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20TBVGK-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT20TBVGK-TB2|no has the higher standalone adjusted growth (6.32 vs 3.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.513); they share one thesis budget; relationships: KXNHLSPREAD-26OCT20TBVGK-TB2|no: REINFORCING (phi 0.513); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis VGK:WINS (p 0.5876): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- thesis TBL:SUPPRESSED (p 0.4817): highest fidelity KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT20TBVGK-TB3|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no kept
- KXNHLSPREAD-26OCT20TBVGK-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2083, phi -1.0)
- KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3045, phi -0.976)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT20TBVGK-TB3|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no kept

portfolios: A EV +1.73 (adj +0.54) on $14.62, P(profit) 0.6465, adj growth 4.8 bp · B EV +0.92 (adj +0.32) on $9.56, P(profit) 0.7917, adj growth 3.0 bp · C EV +1.23 (adj +0.44) on $13.23, P(profit) 0.7917, adj growth 4.1 bp · R EV +0.30 (adj +0.10) on $3.00, P(profit) 0.6391, adj growth 3.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
