# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-19T12:17:31Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.74 | +6.06 | +23.95 | 0.661 | -45.74 | -65.94 | 42.99 |
| B thesis-diversified (joint) ← optimiser card | 88.11 | +10.54 | +4.76 | +7.59 | 0.567 | -29.31 | -39.69 | 41.60 |
| C best expression per thesis | 57.71 | +9.84 | +3.03 | +10.58 | 0.571 | -24.87 | -26.74 | 26.40 |
| R FUNDED research stakes | 14.00 | +0.98 | +0.48 | +0.45 | 0.549 | -7.69 | -7.76 | 0.00 |

## ANA @ NYR  ·  10000 joint draws  ·  414 bet sides mapped, 7 +EV candidates, 4 on card


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
| Tim Washe: 1+ goals YES | 10 | 0.131 | 0.122 | +0.025 | +0.015 | $3.86 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Alexis Lafreniere: 2+ assists YES | 7 | 0.102 | 0.086 | +0.028 | +0.012 | $2.60 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_MIXED | D |
| Jackson LaCombe: 1+ assists YES | 44 | 0.517 | 0.476 | +0.060 | +0.019 | $7.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | DIRECT (0.71) | EVIDENCE_MIXED | D |
| Jeff Malott: 1+ goals YES | 9 | 0.122 | 0.106 | +0.026 | +0.011 | $2.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes; why: KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes has the higher standalone adjusted growth (8.38 vs 5.48 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.052); relationships: KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.071); KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)
- **Alexis Lafreniere: 2+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-1|yes; why: higher confidence-adjusted growth (4.26 vs 0.02 bp); despite a smaller raw edge (+0.028 vs +0.034/contract); alternative not eligible: confidence-adjusted EV +0.0015 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: NYR offense suppressed (<= 2 goals)
- **Jackson LaCombe: 1+ assists YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes; why: Player prop expression KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes selected over player prop KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.71 vs 0.33 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.071); KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.061); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes; why: KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes has the higher standalone adjusted growth (8.38 vs 2.78 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.065); relationships: KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.061); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3865): highest fidelity KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes — Player prop expression KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes selected over player prop KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.71 vs 0.33 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYR:OFFENSE_4PLUS (p 0.4327): highest fidelity KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.3515): highest fidelity KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT19ANANYR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT19ANANYR-ANATWASHE42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4, phi -0.15)
- KXNHLAST-26OCT19ANANYR-NYRALAFRENIERE13-2|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3515, phi -0.209)
- KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4, phi -0.335)
- KXNHLGOAL-26OCT19ANANYR-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4, phi -0.155)
- override: Player prop expression KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-1|yes selected over player prop KXNHLAST-26OCT19ANANYR-ANAJLACOMBE2-2|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.71 vs 0.33 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.26 (adj +3.09) on $50.00, P(profit) 0.4038, adj growth 20.4 bp · B EV +3.48 (adj +1.54) on $16.17, P(profit) 0.3159, adj growth 13.3 bp · C EV +3.61 (adj +1.39) on $18.48, P(profit) 0.2591, adj growth 12.1 bp · R EV +0.23 (adj +0.15) on $1.00, P(profit) 0.1308, adj growth 5.1 bp

## COL @ PHI  ·  10000 joint draws  ·  376 bet sides mapped, 16 +EV candidates, 4 on card


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
| Travis Sanheim: 1+ goals YES | 9 | 0.137 | 0.117 | +0.041 | +0.022 | $5.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ goals NO | 79 | 0.833 | 0.820 | +0.032 | +0.018 | $18.57 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Noel Acciari: 1+ goals YES | 11 | 0.152 | 0.132 | +0.035 | +0.015 | $3.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Brock Nelson: 1+ goals NO | 74 | 0.776 | 0.766 | +0.023 | +0.013 | $11.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT19COLPHI-COL2|no; why: higher confidence-adjusted growth (11.72 vs 5.04 bp); despite a smaller raw edge (+0.041 vs +0.109/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT19COLPHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT19COLPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT19COLPHI-COLBNELSON11-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: PHI offense suppressed (<= 2 goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT19COLPHI-COL2|no; why: KXNHLTEAMTOTAL-26OCT19COLPHI-COL2|no has the higher standalone adjusted growth (6.86 vs 4.68 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.157); relationships: KXNHLGOAL-26OCT19COLPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT19COLPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT19COLPHI-COLBNELSON11-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: COL offense succeeds (4+ goals)
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT19COLPHI-COL2|no; why: KXNHLSPREAD-26OCT19COLPHI-COL2|no has the higher standalone adjusted growth (5.04 vs 4.67 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.137); relationships: KXNHLGOAL-26OCT19COLPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT19COLPHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT19COLPHI-COLBNELSON11-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: PHI offense suppressed (<= 2 goals)
- **Brock Nelson: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT19COLPHI-COL2|no; why: Player prop expression KXNHLGOAL-26OCT19COLPHI-COLBNELSON11-1|no selected over broad KXNHLTEAMTOTAL-26OCT19COLPHI-COL2|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.88 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT19COLPHI-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT19COLPHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT19COLPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis COL:SUPPRESSED (p 0.3943): highest fidelity KXNHLTEAMTOTAL-26OCT19COLPHI-COL4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no — Player prop expression KXNHLGOAL-26OCT19COLPHI-COLBNELSON11-1|no selected over broad KXNHLTEAMTOTAL-26OCT19COLPHI-COL2|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.88 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PHI:WINS_BY_2PLUS (p 0.2319): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no (same contract)
- thesis PHI:WINS (p 0.4425): highest fidelity KXNHLSPREAD-26OCT19COLPHI-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT19COLPHI-COL2|no (same contract)
- KXNHLGOAL-26OCT19COLPHI-PHITSANHEIM6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4713, phi -0.18)
- KXNHLGOAL-26OCT19COLPHI-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3906, phi -0.18)
- KXNHLGOAL-26OCT19COLPHI-PHINACCIARI52-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4713, phi -0.206)
- KXNHLGOAL-26OCT19COLPHI-COLBNELSON11-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.3906, phi -0.212)
- override: Player prop expression KXNHLGOAL-26OCT19COLPHI-COLBNELSON11-1|no selected over broad KXNHLTEAMTOTAL-26OCT19COLPHI-COL2|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.88 vs 0.46 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +12.90 (adj +1.60) on $50.00, P(profit) 0.6459, adj growth 12.0 bp · B EV +4.37 (adj +2.24) on $38.75, P(profit) 0.2636, adj growth 19.5 bp · C EV +3.59 (adj +0.96) on $14.49, P(profit) 0.6767, adj growth 8.4 bp · R EV +0.20 (adj +0.11) on $5.00, P(profit) 0.8333, adj growth 4.1 bp

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
| Ivar Stenberg: 1+ goals NO | 78 | 0.829 | 0.813 | +0.037 | +0.021 | $20.00 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Full Game: Over 6.5 goals scored NO | 45 | 0.520 | 0.483 | +0.053 | +0.015 | $5.99 | FUNDED_RESEARCH | $2 | SJS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Tyler Toffoli: 1+ assists YES | 25 | 0.314 | 0.274 | +0.050 | +0.011 | $4.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_MIXED | D |
| Toronto over 3.5 goals scored NO | 51 | 0.573 | 0.539 | +0.046 | +0.012 | $2.93 | FUNDED_RESEARCH | $1 | TOR:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no; why: higher confidence-adjusted growth (6.03 vs 2.17 bp); despite a smaller raw edge (+0.037 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLTOTAL-26OCT19SJTOR-7|no: MOSTLY_INDEPENDENT (phi 0.133); KXNHLAST-26OCT19SJTOR-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLTEAMTOTAL-26OCT19SJTOR-TOR4|no: MOSTLY_INDEPENDENT (phi 0.019); failure: SJS offense succeeds (4+ goals)
- **Full Game: Over 6.5 goals scored NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no; why: KXNHLAST-26OCT19SJTOR-SJMMARCHMENT27-1|no has the higher standalone adjusted growth (2.17 vs 2.06 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.156); relationships: KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.133); KXNHLAST-26OCT19SJTOR-SJTTOFFOLI73-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.184); KXNHLTEAMTOTAL-26OCT19SJTOR-TOR4|no: REINFORCING (phi 0.45); failure: high-event game (8+ goals)
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT19SJTOR-TOR3|no; why: higher confidence-adjusted growth (1.39 vs 0.24 bp); alternative not eligible: confidence-adjusted EV +0.0044 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLTOTAL-26OCT19SJTOR-7|no: INTENTIONAL_DIVERSIFIER (phi -0.184); KXNHLTEAMTOTAL-26OCT19SJTOR-TOR4|no: MOSTLY_INDEPENDENT (phi -0.003); failure: SJS offense suppressed (<= 2 goals)
- **Toronto over 3.5 goals scored NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT19SJTOR-7|no; why: second expression of the same thesis: KXNHLTOTAL-26OCT19SJTOR-7|no has the higher standalone adjusted growth (2.06 vs 1.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.450); they share one thesis budget; relationships: KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLTOTAL-26OCT19SJTOR-7|no: REINFORCING (phi 0.45); KXNHLAST-26OCT19SJTOR-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.4108): highest fidelity KXNHLAST-26OCT19SJTOR-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT19SJTOR-7|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:LOW_EVENT (p 0.2183): highest fidelity KXNHLTOTAL-26OCT19SJTOR-7|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT19SJTOR-7|no (same contract)
- thesis TOR:SUPPRESSED (p 0.3555): highest fidelity KXNHLTEAMTOTAL-26OCT19SJTOR-TOR4|no [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT19SJTOR-7|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT19SJTOR-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3779, phi -0.172)
- KXNHLTOTAL-26OCT19SJTOR-7|no: FUNDED_RESEARCH; family MIXED; loses 17% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2788, phi -0.648)
- KXNHLAST-26OCT19SJTOR-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4108, phi -0.267)
- KXNHLTEAMTOTAL-26OCT19SJTOR-TOR4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4163, phi -0.978)

portfolios: A EV +5.58 (adj +1.37) on $50.00, P(profit) 0.5897, adj growth 10.6 bp · B EV +2.69 (adj +0.98) on $33.19, P(profit) 0.6203, adj growth 8.7 bp · C EV +2.64 (adj +0.68) on $24.74, P(profit) 0.5964, adj growth 6.0 bp · R EV +0.55 (adj +0.22) on $8.00, P(profit) 0.5805, adj growth 7.7 bp

## PIT @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_PIT_win | p_overtime | goals | shots UTA/PIT | UTA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.61 | 0.39 | 0.00 | 6.06 | 27.5/27.3 | 24.2/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.114 | 0.62 | 0.38 | 0.00 | 9.48 | 28.8/28.6 | 23.0/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.53 | 0.47 | 0.47 | 6.0 | 27.3/27.2 | 23.9/23.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.081 | 0.70 | 0.30 | 0.00 | 6.01 | 32.1/21.3 | 18.7/27.4 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.58 | 0.42 | 0.43 | 5.96 | 32.2/21.8 | 18.6/28.7 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.070 | 0.67 | 0.33 | 0.00 | 9.42 | 33.9/23.1 | 18.3/26.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
