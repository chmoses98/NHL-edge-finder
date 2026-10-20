# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-20T12:05:55Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +39.63 | +14.17 | +27.29 | 0.688 | -38.47 | -54.09 | 117.45 |
| B thesis-diversified (joint) ← optimiser card | 149.01 | +35.75 | +15.76 | +29.03 | 0.685 | -38.27 | -52.18 | 139.13 |
| C best expression per thesis | 115.55 | +34.03 | +15.57 | +23.89 | 0.627 | -44.89 | -58.68 | 133.32 |
| R FUNDED research stakes | 37.00 | +10.43 | +4.36 | +6.94 | 0.638 | -12.05 | -15.86 | 0.00 |

## SJS @ MTL  ·  10000 joint draws  ·  394 bet sides mapped, 5 +EV candidates, 3 on card


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
| Mason Marchment: 1+ goals YES | 17 | 0.234 | 0.216 | +0.054 | +0.036 | $8.13 | FUNDED_RESEARCH | $3 | SJS:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Montreal wins by over 1.5 goals NO | 56 | 0.635 | 0.595 | +0.058 | +0.018 | $5.59 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Montreal wins by over 2.5 goals NO | 69 | 0.752 | 0.719 | +0.047 | +0.013 | $1.01 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20SJMTL-MTL2|no; why: higher confidence-adjusted growth (18.71 vs 2.86 bp); despite a smaller raw edge (+0.054 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT20SJMTL-MTL2|no: MOSTLY_INDEPENDENT (phi 0.143); KXNHLSPREAD-26OCT20SJMTL-MTL3|no: MOSTLY_INDEPENDENT (phi 0.13); failure: SJS offense suppressed (<= 2 goals)
- **Montreal wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT20SJMTL-MTL3|no; why: higher confidence-adjusted growth (2.86 vs 1.93 bp); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.143); KXNHLSPREAD-26OCT20SJMTL-MTL3|no: DUPLICATIVE (phi 0.758); failure: MTL wins by 2+
- **Montreal wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT20SJMTL-MTL2|no; why: Broad expression KXNHLSPREAD-26OCT20SJMTL-MTL3|no selected over broad KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.13); KXNHLSPREAD-26OCT20SJMTL-MTL2|no: DUPLICATIVE (phi 0.758); failure: MTL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:OFFENSE_4PLUS (p 0.3286): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4256): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20SJMTL-MTL2|no (same contract)
- thesis SJS:WINS (p 0.4087): highest fidelity KXNHLSPREAD-26OCT20SJMTL-MTL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20SJMTL-MTL2|no (same contract)
- KXNHLGOAL-26OCT20SJMTL-SJMMARCHMENT27-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.459, phi -0.244)
- KXNHLSPREAD-26OCT20SJMTL-MTL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.3648, phi -1.0)
- KXNHLSPREAD-26OCT20SJMTL-MTL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.3648, phi -0.758)
- override: Broad expression KXNHLSPREAD-26OCT20SJMTL-MTL3|no selected over broad KXNHLTEAMTOTAL-26OCT20SJMTL-MTL5|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.86 (adj +1.44) on $18.95, P(profit) 0.6533, adj growth 13.1 bp · B EV +3.09 (adj +1.81) on $14.73, P(profit) 0.2343, adj growth 16.0 bp · C EV +3.69 (adj +2.17) on $17.13, P(profit) 0.2343, adj growth 18.7 bp · R EV +1.18 (adj +0.68) on $6.00, P(profit) 0.2343, adj growth 22.5 bp

## COL @ NJD  ·  10000 joint draws  ·  436 bet sides mapped, 4 +EV candidates, 4 on card


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
| Fedor Svechkov: 1+ goals YES | 8 | 0.118 | 0.106 | +0.033 | +0.021 | $4.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Gabriel Landeskog: 1+ goals YES | 18 | 0.221 | 0.210 | +0.031 | +0.019 | $5.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ assists NO | 46 | 0.602 | 0.497 | +0.125 | +0.019 | $9.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 65 | 0.696 | 0.681 | +0.030 | +0.015 | $9.53 | FUNDED_RESEARCH | $3 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Fedor Svechkov: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20COLNJ-COLGLANDESKOG92-1|yes; why: higher confidence-adjusted growth (12.06 vs 5.25 bp); relationships: KXNHLGOAL-26OCT20COLNJ-COLGLANDESKOG92-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: INTENTIONAL_DIVERSIFIER (phi -0.063); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: COL offense suppressed (<= 2 goals)
- **Gabriel Landeskog: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT20COLNJ-COL2|yes; why: higher confidence-adjusted growth (5.25 vs 0.28 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.896 vs 0.789); alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: COL offense suppressed (<= 2 goals)
- **Cale Makar: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT20COLNJ-COLNMACKINNON29-2|no; why: higher confidence-adjusted growth (3.29 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0007 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.063); KXNHLGOAL-26OCT20COLNJ-COLGLANDESKOG92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: COL offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20COLNJ-NJERODRIGUES17-1|no; why: higher confidence-adjusted growth (2.17 vs 0.76 bp); despite a smaller raw edge (+0.030 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT20COLNJ-COLGLANDESKOG92-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis COL:OFFENSE_4PLUS (p 0.3914): highest fidelity KXNHLGOAL-26OCT20COLNJ-COLGLANDESKOG92-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20COLNJ-COLGLANDESKOG92-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.3869): highest fidelity KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no (same contract)
- thesis NJD:SUPPRESSED (p 0.4135): highest fidelity KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no (same contract)
- KXNHLGOAL-26OCT20COLNJ-COLFSVECHKOV9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3869, phi -0.141)
- KXNHLGOAL-26OCT20COLNJ-COLGLANDESKOG92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3869, phi -0.223)
- KXNHLAST-26OCT20COLNJ-COLCMAKAR8-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.2 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3914, phi -0.273)
- KXNHLGOAL-26OCT20COLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3638, phi -0.249)

portfolios: A EV +3.62 (adj +1.44) on $18.95, P(profit) 0.5862, adj growth 13.3 bp · B EV +5.45 (adj +2.20) on $28.52, P(profit) 0.5862, adj growth 19.5 bp · C EV +4.23 (adj +1.30) on $27.98, P(profit) 0.5572, adj growth 11.3 bp · R EV +0.14 (adj +0.07) on $3.00, P(profit) 0.696, adj growth 2.3 bp

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
| A.J. Greer: 1+ goals YES | 12 | 0.207 | 0.183 | +0.080 | +0.055 | $11.45 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20ANANYI-ANA6|yes; why: higher confidence-adjusted growth (57.97 vs 0.04 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.903 vs 0.325); alternative not eligible: confidence-adjusted EV +0.0011 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3427): highest fidelity KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes (same contract)
- KXNHLGOAL-26OCT20ANANYI-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4325, phi -0.236)

portfolios: A EV +4.74 (adj +3.30) on $7.58, P(profit) 0.2071, adj growth 30.1 bp · B EV +7.17 (adj +4.98) on $11.45, P(profit) 0.2071, adj growth 43.4 bp · C EV +8.59 (adj +5.97) on $13.72, P(profit) 0.2071, adj growth 50.5 bp · R EV +1.88 (adj +1.31) on $3.00, P(profit) 0.2071, adj growth 45.1 bp

## LAK @ WSH  ·  10000 joint draws  ·  414 bet sides mapped, 1 +EV candidates, 1 on card


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
| Joel Edmundson: 1+ goals YES | 4 | 0.065 | 0.056 | +0.022 | +0.014 | $2.50 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT20LAWSH-LAALAFERRIERE14-2|yes; why: higher confidence-adjusted growth (9.71 vs 0.09 bp); despite a smaller raw edge (+0.023 vs +0.033/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0023 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.07.
- thesis LAK:OFFENSE_4PLUS (p 0.3007): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT20LAWSH-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4854, phi -0.116)

portfolios: A EV +1.17 (adj +0.72) on $2.23, P(profit) 0.0652, adj growth 6.3 bp · B EV +1.32 (adj +0.80) on $2.50, P(profit) 0.0652, adj growth 7.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ CBJ  ·  10000 joint draws  ·  388 bet sides mapped, 6 +EV candidates, 4 on card


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
| Toronto wins 1st Period by over 1.5 goals YES | 2 | 0.082 | 0.038 | +0.061 | +0.017 | $1.46 | FUNDED_RESEARCH | $1 | TOR:SCORES_FIRST | FRAGILE (0.18) | EVIDENCE_THIN | D |
| Toronto over 2.5 goals scored NO | 43 | 0.505 | 0.465 | +0.058 | +0.018 | $7.10 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Full Game: Over 5.5 goals scored NO | 40 | 0.472 | 0.434 | +0.056 | +0.017 | $3.87 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Darren Raddysh: 1+ assists NO | 60 | 0.669 | 0.627 | +0.052 | +0.010 | $3.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Toronto wins 1st Period by over 1.5 goals YES** — thesis: TOR scores first; alternative: KXNHLTEAMTOTAL-26OCT20TORCBJ-CBJ3|no; why: higher confidence-adjusted growth (28.10 vs 0.00 bp); evidence EVIDENCE_THIN vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.936 vs 0.771); alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no: INTENTIONAL_DIVERSIFIER (phi -0.238); KXNHLTOTAL-26OCT20TORCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.107); KXNHLAST-26OCT20TORCBJ-TORDRADDYSH43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.117); failure: CBJ scores first
- **Toronto over 2.5 goals scored NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT20TORCBJ-6|no; why: higher confidence-adjusted growth (2.77 vs 2.58 bp); relationships: KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes: INTENTIONAL_DIVERSIFIER (phi -0.238); KXNHLTOTAL-26OCT20TORCBJ-6|no: REINFORCING (phi 0.412); KXNHLAST-26OCT20TORCBJ-TORDRADDYSH43-1|no: REINFORCING (phi 0.294); failure: TOR offense succeeds (4+ goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no has the higher standalone adjusted growth (2.77 vs 2.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.412); they share one thesis budget; relationships: KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes: INTENTIONAL_DIVERSIFIER (phi -0.107); KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no: REINFORCING (phi 0.412); KXNHLAST-26OCT20TORCBJ-TORDRADDYSH43-1|no: REINFORCING (phi 0.189); failure: CBJ offense succeeds (4+ goals)
- **Darren Raddysh: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no has the higher standalone adjusted growth (2.77 vs 0.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.294); they share one thesis budget; relationships: KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes: INTENTIONAL_DIVERSIFIER (phi -0.117); KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no: REINFORCING (phi 0.294); KXNHLTOTAL-26OCT20TORCBJ-6|no: REINFORCING (phi 0.189); failure: TOR offense succeeds (4+ goals)

**Review**: scripts CBJ shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TOR:SCORES_FIRST (p 0.4412): highest fidelity KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes [FRAGILE], best adjusted EV KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.5171): highest fidelity KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no (same contract)
- thesis GAME:LOW_EVENT (p 0.2618): highest fidelity KXNHLTOTAL-26OCT20TORCBJ-6|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHL1PSPREAD-26OCT20TORCBJ-TOR2|yes: FUNDED_RESEARCH; family MIXED; loses 82% of the draws where the thesis happens; opposing: failure thesis CBJ:SCORES_FIRST (p 0.5575, phi -0.306)
- KXNHLTEAMTOTAL-26OCT20TORCBJ-TOR3|no: FUNDED_RESEARCH; family MIXED; loses 2% of the draws where the thesis happens; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2745, phi -0.621)
- KXNHLTOTAL-26OCT20TORCBJ-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4466, phi -0.539)
- KXNHLAST-26OCT20TORCBJ-TORDRADDYSH43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2745, phi -0.266)

portfolios: A EV +12.80 (adj +3.60) on $18.95, P(profit) 0.6081, adj growth 25.1 bp · B EV +5.91 (adj +1.67) on $16.28, P(profit) 0.5394, adj growth 14.8 bp · C EV +6.42 (adj +1.85) on $13.30, P(profit) 0.578, adj growth 15.9 bp · R EV +3.23 (adj +0.92) on $4.00, P(profit) 0.578, adj growth 25.3 bp

## WPG @ STL  ·  10000 joint draws  ·  434 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_WPG_win | p_overtime | goals | shots STL/WPG | STL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.134 | 0.65 | 0.35 | 0.00 | 6.04 | 26.5/26.5 | 23.5/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.46 | 5.91 | 26.4/26.4 | 23.2/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.64 | 0.36 | 0.00 | 9.24 | 28.0/28.0 | 22.9/21.0 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.077 | 0.68 | 0.32 | 0.00 | 6.03 | 30.8/20.9 | 18.3/26.2 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.58 | 0.42 | 0.47 | 5.89 | 31.3/21.2 | 18.1/28.0 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.059 | 0.57 | 0.43 | 0.00 | 6.01 | 21.1/31.1 | 27.8/17.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ DAL  ·  10000 joint draws  ·  420 bet sides mapped, 6 +EV candidates, 3 on card


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
| Boston over 4.5 goals scored YES | 13 | 0.188 | 0.157 | +0.050 | +0.019 | $2.12 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Boston over 2.5 goals scored YES | 51 | 0.595 | 0.548 | +0.068 | +0.020 | $4.04 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 75 | 0.810 | 0.777 | +0.046 | +0.014 | $7.60 | FUNDED_RESEARCH | $2 | BOS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Boston over 4.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS6|yes; why: higher confidence-adjusted growth (6.34 vs 4.97 bp); wins across more scripts (relative breadth 0.562 vs 0.358); relationships: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: DUPLICATIVE (phi 0.397); KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: REINFORCING (phi 0.224); failure: DAL wins (incl. OT/SO)
- **Boston over 2.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes has the higher standalone adjusted growth (6.34 vs 3.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.397); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes: DUPLICATIVE (phi 0.397); KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: REINFORCING (phi 0.402); failure: BOS offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: BOS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes has the higher standalone adjusted growth (6.34 vs 2.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.224); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes: REINFORCING (phi 0.224); KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: REINFORCING (phi 0.402); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.3577): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.2541): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:WINS (p 0.4741): highest fidelity KXNHLSPREAD-26OCT20BOSDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes: FUNDED_RESEARCH; family MIXED; loses 47% of the draws where the thesis happens; opposing: failure thesis DAL:WINS (p 0.5259, phi -0.424)
- KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.4174, phi -0.974)
- KXNHLSPREAD-26OCT20BOSDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3031, phi -0.735)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS4|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes kept

portfolios: A EV +3.94 (adj +1.28) on $18.95, P(profit) 0.3691, adj growth 9.3 bp · B EV +1.76 (adj +0.58) on $13.77, P(profit) 0.561, adj growth 5.3 bp · C EV +1.67 (adj +0.62) on $4.58, P(profit) 0.1882, adj growth 5.4 bp · R EV +0.74 (adj +0.25) on $5.00, P(profit) 0.561, adj growth 8.4 bp

## MIN @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


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
| Edmonton over 3.5 goals scored YES | 44 | 0.512 | 0.471 | +0.055 | +0.014 | $5.25 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Edmonton over 3.5 goals scored YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20MINEDM-EDM3|yes; why: higher confidence-adjusted growth (1.67 vs 0.73 bp); wins across more scripts (relative breadth 0.712 vs 0.466); alternative not eligible: confidence-adjusted EV +0.0077 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.5018): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4|yes (same contract)
- KXNHLTEAMTOTAL-26OCT20MINEDM-EDM4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis EDM:SUPPRESSED (p 0.2953, phi -0.663)

portfolios: A EV +0.91 (adj +0.23) on $7.58, P(profit) 0.512, adj growth 1.9 bp · B EV +0.63 (adj +0.16) on $5.25, P(profit) 0.512, adj growth 1.4 bp · C EV +0.75 (adj +0.19) on $6.29, P(profit) 0.512, adj growth 1.7 bp · R EV +0.24 (adj +0.06) on $2.00, P(profit) 0.512, adj growth 2.0 bp

## DET @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


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
| Detroit wins by over 2.5 goals NO | 82 | 0.875 | 0.845 | +0.044 | +0.015 | $16.69 | FUNDED_RESEARCH | $5 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Detroit wins by over 1.5 goals NO | 72 | 0.783 | 0.749 | +0.049 | +0.015 | $2.92 | FUNDED_RESEARCH | $1 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Detroit over 3.5 goals scored NO | 60 | 0.668 | 0.629 | +0.051 | +0.012 | $1.51 | FUNDED_RESEARCH | $1 | DET:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Detroit wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT20DETSEA-DET2|no; why: higher confidence-adjusted growth (3.32 vs 2.53 bp); despite a smaller raw edge (+0.044 vs +0.049/contract); relationships: KXNHLSPREAD-26OCT20DETSEA-DET2|no: DUPLICATIVE (phi 0.719); KXNHLTEAMTOTAL-26OCT20DETSEA-DET4|no: DUPLICATIVE (phi 0.46); failure: DET wins by 2+
- **Detroit wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT20DETSEA-DET3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT20DETSEA-DET3|no has the higher standalone adjusted growth (3.32 vs 2.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.719); they share one thesis budget; relationships: KXNHLSPREAD-26OCT20DETSEA-DET3|no: DUPLICATIVE (phi 0.719); KXNHLTEAMTOTAL-26OCT20DETSEA-DET4|no: REINFORCING (phi 0.523); failure: DET wins by 2+
- **Detroit over 3.5 goals scored NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20DETSEA-DET3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT20DETSEA-DET3|no has the higher standalone adjusted growth (3.32 vs 1.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.460); they share one thesis budget; relationships: KXNHLSPREAD-26OCT20DETSEA-DET3|no: DUPLICATIVE (phi 0.46); KXNHLSPREAD-26OCT20DETSEA-DET2|no: REINFORCING (phi 0.523); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:WINS (p 0.5826): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no (same contract)
- thesis DET:SUPPRESSED (p 0.4646): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT20DETSEA-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2168, phi -0.719)
- KXNHLSPREAD-26OCT20DETSEA-DET2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2168, phi -1.0)
- KXNHLTEAMTOTAL-26OCT20DETSEA-DET4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3213, phi -0.976)

portfolios: A EV +1.29 (adj +0.37) on $18.95, P(profit) 0.6247, adj growth 3.2 bp · B EV +1.21 (adj +0.38) on $21.12, P(profit) 0.8147, adj growth 3.5 bp · C EV +1.07 (adj +0.35) on $20.00, P(profit) 0.8748, adj growth 3.2 bp · R EV +0.42 (adj +0.13) on $7.00, P(profit) 0.8147, adj growth 4.4 bp

## CAR @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 18 +EV candidates, 3 on card


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
| Vancouver over 4.5 goals scored YES | 11 | 0.200 | 0.152 | +0.083 | +0.035 | $3.85 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
| Vancouver wins by over 2.5 goals YES | 7 | 0.138 | 0.102 | +0.064 | +0.027 | $2.16 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | DIRECT (0.59) | EVIDENCE_MIXED | D |
| Carolina wins by over 1.5 goals NO | 48 | 0.656 | 0.538 | +0.159 | +0.041 | $11.08 | FUNDED_RESEARCH | $3 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver over 4.5 goals scored YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20CARVAN-VAN3|yes; why: higher confidence-adjusted growth (25.77 vs 22.40 bp); relationships: KXNHLSPREAD-26OCT20CARVAN-VAN3|yes: REINFORCING (phi 0.486); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.317); failure: CAR wins (incl. OT/SO)
- **Vancouver wins by over 2.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes has the higher standalone adjusted growth (25.77 vs 22.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.486); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes: REINFORCING (phi 0.486); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.29); failure: CAR wins (incl. OT/SO)
- **Carolina wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes has the higher standalone adjusted growth (25.77 vs 14.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.317); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes: REINFORCING (phi 0.317); KXNHLSPREAD-26OCT20CARVAN-VAN3|yes: REINFORCING (phi 0.29); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:OFFENSE_4PLUS (p 0.3646): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2337): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- thesis VAN:WINS (p 0.4398): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no (same contract)
- KXNHLTEAMTOTAL-26OCT20CARVAN-VAN5|yes: FUNDED_RESEARCH; family MIXED; loses 45% of the draws where the thesis happens; opposing: failure thesis CAR:WINS (p 0.5602, phi -0.453)
- KXNHLSPREAD-26OCT20CARVAN-VAN3|yes: FUNDED_RESEARCH; family MIXED; loses 41% of the draws where the thesis happens; opposing: failure thesis CAR:WINS (p 0.5602, phi -0.452)
- KXNHLSPREAD-26OCT20CARVAN-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 18.1 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3436, phi -1.0)
- override: Broad expression KXNHLSPREAD-26OCT20CARVAN-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT20CARVAN-CAR6|no because adjusted EV is 1.0 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT20CARVAN-VAN2|yes less than the minimum stake; KXNHLSPREAD-26OCT20CARVAN-VAN3|yes kept

portfolios: A EV +5.90 (adj +1.13) on $18.95, P(profit) 0.5501, adj growth 9.8 bp · B EV +8.11 (adj +2.86) on $17.09, P(profit) 0.6648, adj growth 25.4 bp · C EV +6.66 (adj +2.84) on $8.75, P(profit) 0.2432, adj growth 24.3 bp · R EV +2.52 (adj +0.91) on $5.00, P(profit) 0.6648, adj growth 31.0 bp
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
| Tampa Bay wins by over 1.5 goals NO | 73 | 0.793 | 0.759 | +0.049 | +0.015 | $6.95 | SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS | $0 | VGK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 83 | 0.879 | 0.852 | +0.039 | +0.012 | $8.49 | FUNDED_RESEARCH | $2 | VGK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 3.5 goals scored NO | 61 | 0.685 | 0.640 | +0.058 | +0.013 | $2.86 | SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS | $0 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: VGK wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no; why: KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no has the higher standalone adjusted growth (2.73 vs 2.61 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.286); relationships: KXNHLSPREAD-26OCT20TBVGK-TB3|no: DUPLICATIVE (phi 0.727); KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no: REINFORCING (phi 0.525); failure: TBL wins by 2+
- **Tampa Bay wins by over 2.5 goals NO** — thesis: VGK wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no; why: KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no has the higher standalone adjusted growth (2.73 vs 2.33 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.208); relationships: KXNHLSPREAD-26OCT20TBVGK-TB2|no: DUPLICATIVE (phi 0.727); KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no: DUPLICATIVE (phi 0.471); failure: TBL wins by 2+
- **Tampa Bay over 3.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no; why: Broad expression KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no selected over broad KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT20TBVGK-TB2|no: REINFORCING (phi 0.525); KXNHLSPREAD-26OCT20TBVGK-TB3|no: DUPLICATIVE (phi 0.471); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis TBL:SUPPRESSED (p 0.4798): highest fidelity KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no — Broad expression KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no selected over broad KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis VGK:WINS (p 0.5885): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- KXNHLSPREAD-26OCT20TBVGK-TB2|no: SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2073, phi -1.0)
- KXNHLSPREAD-26OCT20TBVGK-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2073, phi -0.727)
- KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no: SHADOW_ONLY — RESEARCH_STAKE_ZERO_UNDER_CAPS; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3059, phi -0.979)
- override: Broad expression KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no selected over broad KXNHLTEAMTOTAL-26OCT20TBVGK-TB2|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.39 (adj +0.66) on $18.95, P(profit) 0.6418, adj growth 5.3 bp · B EV +1.11 (adj +0.32) on $18.30, P(profit) 0.7927, adj growth 2.9 bp · C EV +0.96 (adj +0.28) on $3.80, P(profit) 0.2385, adj growth 2.4 bp · R EV +0.09 (adj +0.03) on $2.00, P(profit) 0.8786, adj growth 1.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
