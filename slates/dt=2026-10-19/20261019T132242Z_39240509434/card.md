# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-19T13:22:42Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +31.05 | +9.23 | +28.77 | 0.680 | -46.93 | -65.79 | 74.14 |
| B thesis-diversified (joint) ← optimiser card | 118.93 | +20.87 | +11.77 | +10.93 | 0.573 | -46.42 | -59.24 | 101.61 |
| C best expression per thesis | 78.87 | +20.60 | +9.73 | +6.11 | 0.577 | -38.67 | -46.50 | 83.42 |
| R FUNDED research stakes | 18.00 | +3.24 | +2.05 | +0.14 | 0.572 | -9.01 | -12.95 | 0.00 |

## ANA @ NYR  ·  10000 joint draws  ·  414 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_ANA_win | p_overtime | goals | shots NYR/ANA | NYR/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.56 | 0.44 | 0.00 | 5.98 | 26.7/27.1 | 23.9/22.8 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.109 | 0.48 | 0.52 | 0.00 | 6.04 | 21.2/32.3 | 28.6/17.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.54 | 0.46 | 0.47 | 5.98 | 26.7/27.5 | 24.3/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.57 | 0.43 | 0.00 | 9.42 | 28.3/29.0 | 23.3/21.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.50 | 0.50 | 0.48 | 5.95 | 21.4/32.6 | 29.0/18.2 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.079 | 0.51 | 0.49 | 0.00 | 9.27 | 23.1/34.6 | 28.2/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 14 | 0.229 | 0.204 | +0.081 | +0.056 | $14.29 | FUNDED_RESEARCH | $4 | ANA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 9 | 0.122 | 0.111 | +0.026 | +0.015 | $3.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Tim Washe: 1+ goals YES | 10 | 0.131 | 0.122 | +0.025 | +0.015 | $3.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ assists NO | 69 | 0.761 | 0.723 | +0.056 | +0.018 | $16.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes; why: higher confidence-adjusted growth (52.05 vs 4.25 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.036); KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes has the higher standalone adjusted growth (52.05 vs 6.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: ANA offense suppressed (<= 2 goals)
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes has the higher standalone adjusted growth (52.05 vs 5.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.036); they share one thesis budget; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.036); KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: ANA offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT19ANANYR-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (3.41 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3865): highest fidelity KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.4327): highest fidelity KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.3515): highest fidelity KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT19ANANYR-ANAAGREER18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4, phi -0.244)
- KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4, phi -0.155)
- KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4, phi -0.15)
- KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.4327, phi -0.213)

portfolios: A EV +10.73 (adj +5.62) on $44.12, P(profit) 0.446, adj growth 47.8 bp · B EV +10.95 (adj +6.96) on $38.07, P(profit) 0.3876, adj growth 59.4 bp · C EV +10.16 (adj +6.27) on $33.81, P(profit) 0.3082, adj growth 53.5 bp · R EV +2.17 (adj +1.50) on $4.00, P(profit) 0.229, adj growth 50.2 bp

## COL @ PHI  ·  10000 joint draws  ·  376 bet sides mapped, 24 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_COL_win | p_overtime | goals | shots PHI/COL | PHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.139 | 0.39 | 0.61 | 0.00 | 5.97 | 21.2/33.6 | 29.2/18.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.44 | 0.56 | 0.46 | 5.9 | 21.3/33.4 | 29.9/18.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.100 | 0.44 | 0.56 | 0.00 | 5.96 | 27.0/27.6 | 23.8/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.49 | 0.51 | 0.48 | 5.87 | 27.3/27.9 | 24.7/24.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.078 | 0.33 | 0.67 | 0.00 | 9.17 | 22.9/35.5 | 28.1/18.1 | even strength |
| COL shot control · low event (<=4) · tight (1-goal/OT) | 0.076 | 0.47 | 0.53 | 0.48 | 2.81 | 20.0/31.9 | 30.3/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Sanheim: 1+ goals YES | 9 | 0.137 | 0.117 | +0.041 | +0.022 | $5.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 55 | 0.624 | 0.601 | +0.057 | +0.033 | $19.61 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Noah Cates: 1+ goals YES | 14 | 0.193 | 0.171 | +0.045 | +0.023 | $5.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Trevor Zegras: 1+ goals YES | 25 | 0.295 | 0.280 | +0.032 | +0.017 | $5.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes; why: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes has the higher standalone adjusted growth (37.43 vs 11.72 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.051); relationships: KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT19COLPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT19COLPHI-PHITZEGRAS46-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: PHI offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT19COLPHI-PHI2|yes; why: higher confidence-adjusted growth (9.96 vs 8.87 bp); despite a smaller raw edge (+0.057 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.987 vs 0.558); relationships: KXNHLGOAL-26OCT19COLPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT19COLPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT19COLPHI-PHITZEGRAS46-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: COL offense succeeds (4+ goals)
- **Noah Cates: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes; why: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes has the higher standalone adjusted growth (37.43 vs 8.75 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.090); relationships: KXNHLGOAL-26OCT19COLPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT19COLPHI-PHITZEGRAS46-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: PHI offense suppressed (<= 2 goals)
- **Trevor Zegras: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes; why: KXNHL1PSPREAD-26OCT19COLPHI-PHI2|yes has the higher standalone adjusted growth (37.43 vs 3.11 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.099); relationships: KXNHLGOAL-26OCT19COLPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT19COLPHI-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:SCORES_FIRST (p 0.4661): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3131): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.2319): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no (same contract)
- KXNHLGOAL-26OCT19COLPHI-PHITSANHEIM6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4713, phi -0.18)
- KXNHLGOAL-26OCT19COLPHI-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3906, phi -0.302)
- KXNHLGOAL-26OCT19COLPHI-PHINCATES27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4713, phi -0.228)
- KXNHLGOAL-26OCT19COLPHI-PHITZEGRAS46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4713, phi -0.273)

portfolios: A EV +14.51 (adj +1.99) on $44.12, P(profit) 0.6917, adj growth 13.4 bp · B EV +6.59 (adj +3.57) on $36.04, P(profit) 0.433, adj growth 31.0 bp · C EV +8.24 (adj +2.76) on $26.71, P(profit) 0.6517, adj growth 23.8 bp · R EV +0.50 (adj +0.29) on $5.00, P(profit) 0.6243, adj growth 10.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT19COLPHI-COL|no == KXNHLGAME-26OCT19COLPHI-PHI|yes

## SJS @ TOR  ·  10000 joint draws  ·  438 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_SJS_win | p_overtime | goals | shots TOR/SJS | TOR/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.135 | 0.53 | 0.47 | 0.00 | 6.01 | 28.1/28.4 | 25.0/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.48 | 5.95 | 28.1/28.3 | 25.1/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.58 | 0.42 | 0.00 | 9.38 | 29.6/29.9 | 24.0/23.2 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.084 | 0.53 | 0.47 | 0.00 | 6.0 | 22.6/33.6 | 29.9/19.2 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.51 | 0.49 | 0.46 | 5.87 | 22.5/33.9 | 30.4/19.3 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.059 | 0.47 | 0.53 | 0.00 | 9.1 | 23.6/35.1 | 28.6/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 1+ goals NO | 78 | 0.829 | 0.816 | +0.037 | +0.024 | $15.67 | FUNDED_RESEARCH | $4 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 71 | 0.777 | 0.739 | +0.052 | +0.014 | $9.58 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Full Game: Over 6.5 goals scored NO | 45 | 0.520 | 0.483 | +0.053 | +0.015 | $4.75 | FUNDED_RESEARCH | $2 | SJS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Tyler Toffoli: 1+ assists YES | 25 | 0.314 | 0.274 | +0.050 | +0.011 | $4.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT19SJTOR-5|no; why: higher confidence-adjusted growth (7.54 vs 2.37 bp); despite a smaller raw edge (+0.037 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.001 vs 0.401); relationships: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLTOTAL-26OCT19SJTOR-7|no: MOSTLY_INDEPENDENT (phi 0.133); KXNHLAST-26OCT19SJTOR-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: SJS offense succeeds (4+ goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT19SJTOR-5|no; why: KXNHLTOTAL-26OCT19SJTOR-5|no has the higher standalone adjusted growth (2.37 vs 2.17 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.129); relationships: KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLTOTAL-26OCT19SJTOR-7|no: REINFORCING (phi 0.156); KXNHLAST-26OCT19SJTOR-SJTTOFFOLI73-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.067); failure: SJS offense succeeds (4+ goals)
- **Full Game: Over 6.5 goals scored NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT19SJTOR-5|no; why: Broad expression KXNHLTOTAL-26OCT19SJTOR-7|no selected over broad KXNHLTOTAL-26OCT19SJTOR-5|no because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.133); KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: REINFORCING (phi 0.156); KXNHLAST-26OCT19SJTOR-SJTTOFFOLI73-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.184); failure: high-event game (8+ goals)
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT19SJTOR-TOR3|no; why: higher confidence-adjusted growth (1.39 vs 0.24 bp); alternative not eligible: confidence-adjusted EV +0.0044 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: INTENTIONAL_DIVERSIFIER (phi -0.067); KXNHLTOTAL-26OCT19SJTOR-7|no: INTENTIONAL_DIVERSIFIER (phi -0.184); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.4108): highest fidelity KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT19SJTOR-7|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:LOW_EVENT (p 0.2183): highest fidelity KXNHLTOTAL-26OCT19SJTOR-7|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT19SJTOR-7|no (same contract)
- thesis TOR:SUPPRESSED (p 0.3555): highest fidelity KXNHLTOTAL-26OCT19SJTOR-7|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT19SJTOR-7|no (same contract)
- KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3779, phi -0.172)
- KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3779, phi -0.209)
- KXNHLTOTAL-26OCT19SJTOR-7|no: FUNDED_RESEARCH; family MIXED; loses 17% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2788, phi -0.648)
- KXNHLAST-26OCT19SJTOR-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4108, phi -0.267)
- override: Broad expression KXNHLTOTAL-26OCT19SJTOR-7|no selected over broad KXNHLTOTAL-26OCT19SJTOR-5|no because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.90 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.92 (adj +1.21) on $44.12, P(profit) 0.5897, adj growth 9.6 bp · B EV +2.80 (adj +0.99) on $34.31, P(profit) 0.5659, adj growth 9.1 bp · C EV +1.68 (adj +0.45) on $7.84, P(profit) 0.4772, adj growth 4.0 bp · R EV +0.42 (adj +0.19) on $6.00, P(profit) 0.4565, adj growth 6.7 bp

## PIT @ UTA  ·  10000 joint draws  ·  462 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_PIT_win | p_overtime | goals | shots UTA/PIT | UTA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.61 | 0.39 | 0.00 | 6.06 | 27.5/27.3 | 24.2/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.114 | 0.62 | 0.38 | 0.00 | 9.48 | 28.8/28.6 | 23.0/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.53 | 0.47 | 0.47 | 6.0 | 27.3/27.2 | 23.9/23.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.081 | 0.70 | 0.30 | 0.00 | 6.01 | 32.1/21.3 | 18.7/27.4 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.58 | 0.42 | 0.43 | 5.96 | 32.2/21.8 | 18.6/28.7 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.070 | 0.67 | 0.33 | 0.00 | 9.42 | 33.9/23.1 | 18.3/26.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dylan Guenther: 1+ goals NO | 62 | 0.669 | 0.651 | +0.032 | +0.015 | $10.51 | FUNDED_RESEARCH | $3 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT19PITUTA-UTACKELLER9-2|no; why: higher confidence-adjusted growth (2.12 vs 0.19 bp); despite a smaller raw edge (+0.032 vs +0.063/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis UTA:SUPPRESSED (p 0.3006): highest fidelity KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no (same contract)
- KXNHLGOAL-26OCT19PITUTA-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.493, phi -0.229)

portfolios: A EV +0.89 (adj +0.41) on $17.65, P(profit) 0.6686, adj growth 3.3 bp · B EV +0.53 (adj +0.25) on $10.51, P(profit) 0.6686, adj growth 2.2 bp · C EV +0.53 (adj +0.25) on $10.51, P(profit) 0.6686, adj growth 2.2 bp · R EV +0.15 (adj +0.07) on $3.00, P(profit) 0.6686, adj growth 2.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
