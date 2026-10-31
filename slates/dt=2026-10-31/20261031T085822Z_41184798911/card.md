# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T08:58:22Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.97 | +19.19 | +5.61 | +18.77 | 0.695 | -27.69 | -39.83 | 49.17 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +16.49 | +6.16 | +15.27 | 0.675 | -28.32 | -38.79 | 55.21 |
| C best expression per thesis | 109.88 | +14.96 | +4.30 | +14.21 | 0.673 | -27.84 | -38.13 | 37.48 |
| R FUNDED research stakes | 31.00 | +2.75 | +1.11 | +1.98 | 0.631 | -7.96 | -11.48 | 0.00 |

## CHI @ BOS  ·  10000 joint draws  ·  434 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_CHI_win | p_overtime | goals | shots BOS/CHI | BOS/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BOS shot control · normal event (5-7) · decided (2+) | 0.124 | 0.79 | 0.21 | 0.00 | 6.01 | 32.3/21.1 | 18.9/27.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.73 | 0.27 | 0.00 | 6.04 | 27.2/26.7 | 24.1/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.57 | 0.43 | 0.48 | 5.94 | 27.2/26.9 | 23.6/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.70 | 0.30 | 0.00 | 9.34 | 28.9/28.4 | 23.6/21.5 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.61 | 0.39 | 0.46 | 5.95 | 32.4/21.4 | 18.3/28.9 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.083 | 0.81 | 0.19 | 0.00 | 9.28 | 33.6/22.3 | 18.4/25.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Casey Mittelstadt: 1+ goals YES | 17 | 0.222 | 0.205 | +0.042 | +0.025 | $6.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 59 | 0.634 | 0.622 | +0.027 | +0.015 | $6.23 | FUNDED_RESEARCH | $2 | BOS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ assists NO | 56 | 0.638 | 0.592 | +0.061 | +0.015 | $7.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
| Pavel Zacha: 1+ assists NO | 54 | 0.610 | 0.570 | +0.053 | +0.013 | $6.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes; why: higher confidence-adjusted growth (9.37 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT31CHIBOS-BOSPZACHA18-1|no: INTENTIONAL_DIVERSIFIER (phi -0.105); failure: BOS offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31CHIBOS-BOSPZACHA18-1|no; why: higher confidence-adjusted growth (1.94 vs 1.42 bp); despite a smaller raw edge (+0.027 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT31CHIBOS-BOSPZACHA18-1|no: REINFORCING (phi 0.207); failure: BOS offense succeeds (4+ goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31CHIBOS-CHIPKANE88-1|no; why: higher confidence-adjusted growth (1.89 vs 0.70 bp); despite a smaller raw edge (+0.061 vs +0.074/contract); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT31CHIBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT31CHIBOS-BOSPZACHA18-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense succeeds (4+ goals)
- **Pavel Zacha: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT31CHIBOS-BOSDPASTRNAK88-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT31CHIBOS-BOSDPASTRNAK88-1|no has the higher standalone adjusted growth (1.94 vs 1.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.207); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.105); KXNHLGOAL-26OCT31CHIBOS-BOSDPASTRNAK88-1|no: REINFORCING (phi 0.207); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: BOS offense succeeds (4+ goals)

**Review**: scripts BOS shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis BOS:SUPPRESSED (p 0.2711): highest fidelity KXNHLGOAL-26OCT31CHIBOS-BOSDPASTRNAK88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT31CHIBOS-BOSDPASTRNAK88-1|no (same contract)
- thesis CHI:SUPPRESSED (p 0.5086): highest fidelity KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.5248): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.2711, phi -0.178)
- KXNHLGOAL-26OCT31CHIBOS-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.5248, phi -0.242)
- KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2796, phi -0.259)
- KXNHLAST-26OCT31CHIBOS-BOSPZACHA18-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.5248, phi -0.252)

portfolios: A EV +2.03 (adj +0.83) on $18.30, P(profit) 0.5369, adj growth 7.7 bp · B EV +3.24 (adj +1.41) on $27.16, P(profit) 0.4421, adj growth 12.5 bp · C EV +1.37 (adj +0.45) on $18.43, P(profit) 0.4022, adj growth 4.0 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.6336, adj growth 1.7 bp

## STL @ DET  ·  10000 joint draws  ·  344 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_STL_win | p_overtime | goals | shots DET/STL | DET/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.46 | 0.54 | 0.00 | 5.97 | 27.2/26.8 | 23.1/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.47 | 0.53 | 0.48 | 5.88 | 27.5/27.1 | 23.9/24.4 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.099 | 0.53 | 0.47 | 0.00 | 5.96 | 32.5/21.4 | 18.1/28.5 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.53 | 0.47 | 0.49 | 5.83 | 32.5/21.4 | 18.2/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.46 | 0.54 | 0.00 | 9.21 | 28.9/28.7 | 22.5/23.1 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.059 | 0.54 | 0.46 | 0.00 | 9.15 | 34.6/23.0 | 17.6/27.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sheldon Dries: 1+ goals YES | 8 | 0.113 | 0.098 | +0.028 | +0.012 | $2.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 36 | 0.408 | 0.392 | +0.032 | +0.016 | $5.41 | FUNDED_RESEARCH | $2 | DET:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_STRONGER | D |
| Dylan Holloway: 1+ assists YES | 31 | 0.377 | 0.336 | +0.052 | +0.011 | $3.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (4.25 vs 2.35 bp); despite a smaller raw edge (+0.028 vs +0.032/contract); relationships: KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: DET offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT31STLDET-2|yes; why: higher confidence-adjusted growth (2.35 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: DET offense suppressed (<= 2 goals)
- **Dylan Holloway: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT31STLDET-2|yes; why: higher confidence-adjusted growth (1.24 vs 0.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DET:OFFENSE_4PLUS (p 0.3623): highest fidelity KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3756): highest fidelity KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes (same contract)
- KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4186, phi -0.169)
- KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4186, phi -0.303)
- KXNHLAST-26OCT31STLDET-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 45% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4014, phi -0.286)

portfolios: A EV +2.47 (adj +0.85) on $14.55, P(profit) 0.4487, adj growth 7.2 bp · B EV +1.84 (adj +0.71) on $11.34, P(profit) 0.4744, adj growth 6.3 bp · C EV +1.15 (adj +0.40) on $10.11, P(profit) 0.6296, adj growth 3.5 bp · R EV +0.17 (adj +0.08) on $2.00, P(profit) 0.4077, adj growth 2.8 bp

## TBL @ NSH  ·  10000 joint draws  ·  404 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_TBL_win | p_overtime | goals | shots NSH/TBL | NSH/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.47 | 0.53 | 0.00 | 6.0 | 27.5/28.0 | 24.3/24.0 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.108 | 0.42 | 0.58 | 0.00 | 5.99 | 21.7/33.2 | 28.9/18.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.51 | 0.49 | 0.46 | 5.95 | 27.3/27.9 | 24.6/24.0 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.46 | 0.54 | 0.49 | 5.94 | 22.0/33.4 | 30.0/18.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.47 | 0.53 | 0.00 | 9.27 | 28.7/29.3 | 23.3/22.9 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.074 | 0.41 | 0.59 | 0.00 | 9.28 | 23.1/34.9 | 27.9/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charle-Edouard D'Astous: 1+ goals NO | 88 | 0.936 | 0.918 | +0.048 | +0.031 | $17.42 | FUNDED_RESEARCH | $5 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 1.5 goals NO | 62 | 0.694 | 0.654 | +0.058 | +0.018 | $9.31 | FUNDED_RESEARCH | $3 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ goals NO | 63 | 0.675 | 0.660 | +0.029 | +0.014 | $6.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TBNSH-TB2|no; why: higher confidence-adjusted growth (21.05 vs 3.07 bp); despite a smaller raw edge (+0.048 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT31TBNSH-TB2|no: MOSTLY_INDEPENDENT (phi 0.084); KXNHLGOAL-26OCT31TBNSH-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT31TBNSH-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (3.07 vs 1.85 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.084); KXNHLGOAL-26OCT31TBNSH-TBNKUCHEROV86-1|no: REINFORCING (phi 0.224); failure: TBL wins by 2+
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TBNSH-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31TBNSH-TB2|no has the higher standalone adjusted growth (3.07 vs 1.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.224); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLSPREAD-26OCT31TBNSH-TB2|no: REINFORCING (phi 0.224); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TBL:SUPPRESSED (p 0.3705): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB2|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB2|no (same contract)
- thesis NSH:WINS (p 0.4744): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB2|no (same contract)
- KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4065, phi -0.109)
- KXNHLSPREAD-26OCT31TBNSH-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.306, phi -1.0)
- KXNHLGOAL-26OCT31TBNSH-TBNKUCHEROV86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4065, phi -0.268)

portfolios: A EV +1.16 (adj +0.51) on $18.30, P(profit) 0.5169, adj growth 4.9 bp · B EV +2.08 (adj +1.01) on $33.36, P(profit) 0.6588, adj growth 9.5 bp · C EV +1.18 (adj +0.37) on $13.08, P(profit) 0.694, adj growth 3.2 bp · R EV +0.54 (adj +0.26) on $8.00, P(profit) 0.6588, adj growth 9.7 bp

## EDM @ NYI  ·  10000 joint draws  ·  408 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_EDM_win | p_overtime | goals | shots NYI/EDM | NYI/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.43 | 0.57 | 0.00 | 6.04 | 27.4/27.3 | 23.6/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.49 | 0.51 | 0.49 | 5.95 | 27.6/27.4 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.115 | 0.46 | 0.54 | 0.00 | 9.44 | 29.2/29.1 | 22.6/23.1 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.072 | 0.50 | 0.50 | 0.00 | 6.07 | 32.5/22.0 | 18.5/28.5 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.54 | 0.46 | 0.47 | 5.91 | 32.6/22.4 | 19.2/29.3 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.063 | 0.41 | 0.59 | 0.00 | 6.06 | 21.9/32.2 | 28.0/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden Schenn: 1+ goals YES | 22 | 0.263 | 0.250 | +0.031 | +0.018 | $4.45 | FUNDED_RESEARCH | $2 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 8 | 0.109 | 0.096 | +0.024 | +0.011 | $2.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 33 | 0.444 | 0.363 | +0.098 | +0.018 | $6.93 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.67) | EVIDENCE_MIXED | D |
| Full Game: Over 6.5 goals scored YES | 47 | 0.532 | 0.499 | +0.045 | +0.011 | $4.87 | FUNDED_RESEARCH | $2 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: KXNHLTOTAL-26OCT31EDMNYI-9|yes has the higher standalone adjusted growth (4.35 vs 3.87 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.136); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLTOTAL-26OCT31EDMNYI-7|yes: REINFORCING (phi 0.16); failure: NYI offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: KXNHLTOTAL-26OCT31EDMNYI-9|yes has the higher standalone adjusted growth (4.35 vs 3.05 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.095); relationships: KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.124); KXNHLTOTAL-26OCT31EDMNYI-7|yes: MOSTLY_INDEPENDENT (phi 0.101); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (3.05 vs 1.42 bp); relationships: KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.124); KXNHLTOTAL-26OCT31EDMNYI-7|yes: INTENTIONAL_DIVERSIFIER (phi -0.226); failure: EDM offense succeeds (4+ goals)
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: Broad expression KXNHLTOTAL-26OCT31EDMNYI-7|yes selected over broad KXNHLTOTAL-26OCT31EDMNYI-9|yes because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.76 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: REINFORCING (phi 0.16); KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.101); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.226); failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis GAME:HIGH_EVENT (p 0.3308): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-9|yes — Broad expression KXNHLTOTAL-26OCT31EDMNYI-7|yes selected over broad KXNHLTOTAL-26OCT31EDMNYI-9|yes because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.76 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYI:OFFENSE_4PLUS (p 0.4158): highest fidelity KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.4499): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3666, phi -0.224)
- KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3384, phi -0.148)
- KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 33% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.4 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4499, phi -0.325)
- KXNHLTOTAL-26OCT31EDMNYI-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.1859, phi -0.51)
- override: Broad expression KXNHLTOTAL-26OCT31EDMNYI-7|yes selected over broad KXNHLTOTAL-26OCT31EDMNYI-9|yes because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.76 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.67 (adj +0.86) on $18.30, P(profit) 0.7195, adj growth 7.8 bp · B EV +3.68 (adj +1.10) on $18.62, P(profit) 0.649, adj growth 9.8 bp · C EV +3.78 (adj +0.94) on $13.87, P(profit) 0.6253, adj growth 8.2 bp · R EV +0.45 (adj +0.20) on $4.00, P(profit) 0.6201, adj growth 6.3 bp

## BUF @ LAK  ·  10000 joint draws  ·  426 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BUF_win | p_overtime | goals | shots LAK/BUF | LAK/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.58 | 0.41 | 0.00 | 6.02 | 27.9/28.0 | 24.8/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.49 | 0.51 | 0.47 | 5.92 | 27.8/27.8 | 24.4/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.56 | 0.44 | 0.00 | 9.25 | 29.3/29.3 | 23.7/23.0 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.074 | 0.63 | 0.37 | 0.00 | 6.0 | 32.7/22.1 | 19.2/28.1 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.53 | 0.47 | 0.45 | 5.91 | 32.7/22.3 | 19.2/29.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.55 | 0.45 | 0.00 | 3.45 | 26.3/26.2 | 24.5/24.3 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Andre Lee: 1+ goals YES | 10 | 0.128 | 0.120 | +0.022 | +0.014 | $2.85 | FUNDED_RESEARCH | $1 | LAK:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Scott Laughton: 1+ goals YES | 13 | 0.160 | 0.150 | +0.022 | +0.012 | $2.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 2.5 goals NO | 80 | 0.854 | 0.824 | +0.042 | +0.013 | $12.62 | FUNDED_RESEARCH | $4 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Los Angeles wins by over 1.5 goals YES | 26 | 0.319 | 0.287 | +0.045 | +0.013 | $1.56 | FUNDED_RESEARCH | $1 | LAK:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes; why: higher confidence-adjusted growth (4.30 vs 2.56 bp); relationships: KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLSPREAD-26OCT31BUFLA-BUF3|no: MOSTLY_INDEPENDENT (phi 0.077); KXNHLSPREAD-26OCT31BUFLA-LA2|yes: MOSTLY_INDEPENDENT (phi 0.116); failure: LAK offense suppressed (<= 2 goals)
- **Scott Laughton: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: higher confidence-adjusted growth (2.56 vs 2.45 bp); despite a smaller raw edge (+0.022 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLSPREAD-26OCT31BUFLA-BUF3|no: MOSTLY_INDEPENDENT (phi 0.11); KXNHLSPREAD-26OCT31BUFLA-LA2|yes: REINFORCING (phi 0.194); failure: LAK offense suppressed (<= 2 goals)
- **Buffalo wins by over 2.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31BUFLA-LA2|yes; why: higher confidence-adjusted growth (2.45 vs 1.99 bp); despite a smaller raw edge (+0.042 vs +0.045/contract); wins across more scripts (relative breadth 1.011 vs 0.518); relationships: KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.077); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.11); KXNHLSPREAD-26OCT31BUFLA-LA2|yes: REINFORCING (phi 0.283); failure: BUF wins by 2+
- **Los Angeles wins by over 1.5 goals YES** — thesis: LAK wins by 2+; alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31BUFLA-BUF3|no has the higher standalone adjusted growth (2.45 vs 1.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.283); they share one thesis budget; relationships: KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.116); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: REINFORCING (phi 0.194); KXNHLSPREAD-26OCT31BUFLA-BUF3|no: REINFORCING (phi 0.283); failure: BUF wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis LAK:OFFENSE_4PLUS (p 0.4021): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-LA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS (p 0.5422): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-LA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS_BY_2PLUS (p 0.3189): highest fidelity KXNHLSPREAD-26OCT31BUFLA-LA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-LA2|yes (same contract)
- KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3772, phi -0.162)
- KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3772, phi -0.192)
- KXNHLSPREAD-26OCT31BUFLA-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2391, phi -0.739)
- KXNHLSPREAD-26OCT31BUFLA-LA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4578, phi -0.629)

portfolios: A EV +1.84 (adj +0.67) on $18.30, P(profit) 0.3786, adj growth 5.8 bp · B EV +1.88 (adj +0.85) on $19.35, P(profit) 0.4463, adj growth 7.5 bp · C EV +1.39 (adj +0.54) on $20.81, P(profit) 0.8627, adj growth 4.7 bp · R EV +0.58 (adj +0.24) on $6.00, P(profit) 0.3883, adj growth 8.2 bp

## OTT @ SJS  ·  10000 joint draws  ·  432 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_OTT_win | p_overtime | goals | shots SJS/OTT | SJS/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.50 | 0.50 | 0.00 | 6.01 | 27.0/27.3 | 23.6/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.46 | 5.95 | 27.0/27.4 | 24.1/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.50 | 0.50 | 0.00 | 9.38 | 28.6/29.0 | 22.7/22.5 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.090 | 0.42 | 0.58 | 0.00 | 6.03 | 21.5/32.5 | 28.3/18.5 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.46 | 0.54 | 0.48 | 5.91 | 21.5/32.6 | 29.3/18.3 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.067 | 0.40 | 0.60 | 0.00 | 9.24 | 23.1/34.3 | 27.0/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Thomas Chabot: 1+ assists NO | 72 | 0.789 | 0.747 | +0.055 | +0.013 | $11.86 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Thomas Chabot: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31OTTSJ-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (1.87 vs 0.11 bp); despite a smaller raw edge (+0.055 vs +0.070/contract); alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.3615): highest fidelity KXNHLAST-26OCT31OTTSJ-OTTTCHABOT72-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31OTTSJ-OTTTCHABOT72-1|no (same contract)
- KXNHLAST-26OCT31OTTSJ-OTTTCHABOT72-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4147, phi -0.217)

portfolios: A EV +0.55 (adj +0.13) on $7.32, P(profit) 0.789, adj growth 1.2 bp · B EV +0.89 (adj +0.21) on $11.86, P(profit) 0.789, adj growth 1.9 bp · C EV +1.02 (adj +0.24) on $13.61, P(profit) 0.789, adj growth 2.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_PIT_win | p_overtime | goals | shots MTL/PIT | MTL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.55 | 0.45 | 0.00 | 6.04 | 27.4/27.5 | 24.1/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.47 | 5.93 | 27.3/27.5 | 24.2/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.60 | 0.40 | 0.00 | 9.43 | 28.7/29.0 | 23.4/21.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.086 | 0.50 | 0.50 | 0.00 | 6.01 | 21.9/33.0 | 29.2/18.6 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.48 | 0.52 | 0.46 | 5.87 | 21.8/32.6 | 29.2/18.7 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.067 | 0.55 | 0.45 | 0.00 | 9.4 | 23.2/34.1 | 28.2/17.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_TOR_win | p_overtime | goals | shots VAN/TOR | VAN/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.50 | 0.50 | 0.00 | 6.05 | 28.3/28.4 | 24.7/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.46 | 5.98 | 28.4/28.7 | 25.3/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.51 | 0.49 | 0.00 | 9.45 | 29.8/29.9 | 23.6/23.6 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.074 | 0.46 | 0.54 | 0.00 | 6.06 | 22.8/33.8 | 29.9/19.5 | even strength |
| TOR shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.49 | 0.51 | 0.46 | 6.01 | 22.7/33.4 | 30.0/19.4 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.062 | 0.54 | 0.46 | 0.00 | 6.0 | 33.7/23.0 | 19.8/29.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 22 | 0.286 | 0.251 | +0.054 | +0.019 | $3.60 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Toronto wins by over 2.5 goals NO | 74 | 0.813 | 0.771 | +0.059 | +0.018 | $14.11 | FUNDED_RESEARCH | $4 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT31TORVAN-TOR3|no; why: higher confidence-adjusted growth (4.26 vs 3.81 bp); despite a smaller raw edge (+0.054 vs +0.059/contract); relationships: KXNHLSPREAD-26OCT31TORVAN-TOR3|no: DUPLICATIVE (phi 0.304); failure: TOR wins (incl. OT/SO)
- **Toronto wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes has the higher standalone adjusted growth (4.26 vs 3.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.304); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes: DUPLICATIVE (phi 0.304); failure: TOR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:WINS_BY_2PLUS (p 0.2864): highest fidelity KXNHLSPREAD-26OCT31TORVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-VAN2|yes (same contract)
- thesis VAN:WINS (p 0.5048): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3579): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT31TORVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS (p 0.4952, phi -0.627)
- KXNHLSPREAD-26OCT31TORVAN-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2903, phi -0.75)

portfolios: A EV +1.95 (adj +0.43) on $18.30, P(profit) 0.5505, adj growth 3.6 bp · B EV +1.96 (adj +0.63) on $17.71, P(profit) 0.8128, adj growth 5.6 bp · C EV +1.30 (adj +0.45) on $5.53, P(profit) 0.2864, adj growth 3.9 bp · R EV +0.55 (adj +0.18) on $5.00, P(profit) 0.8128, adj growth 6.2 bp

## CBJ @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_CBJ_win | p_overtime | goals | shots DAL/CBJ | DAL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 6.0 | 26.1/25.9 | 22.7/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.45 | 5.87 | 26.4/26.2 | 22.9/23.1 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.091 | 0.63 | 0.37 | 0.00 | 5.97 | 30.9/20.6 | 17.9/26.7 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.56 | 0.44 | 0.52 | 5.83 | 31.0/20.6 | 17.6/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.56 | 0.44 | 0.00 | 9.11 | 27.7/27.6 | 22.1/21.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.55 | 0.45 | 0.00 | 3.53 | 25.1/24.8 | 23.0/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Columbus wins by over 1.5 goals YES | 19 | 0.239 | 0.212 | +0.038 | +0.011 | $2.17 | FUNDED_RESEARCH | $1 | CBJ:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 74 | 0.799 | 0.764 | +0.045 | +0.011 | $8.43 | FUNDED_RESEARCH | $3 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Columbus wins by over 1.5 goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLSPREAD-26OCT31CBJDAL-DAL3|no; why: higher confidence-adjusted growth (1.71 vs 1.43 bp); despite a smaller raw edge (+0.038 vs +0.045/contract); relationships: KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: REINFORCING (phi 0.281); failure: DAL wins (incl. OT/SO)
- **Dallas wins by over 2.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes has the higher standalone adjusted growth (1.71 vs 1.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.281); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes: REINFORCING (phi 0.281); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:WINS_BY_2PLUS (p 0.239): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes (same contract)
- thesis CBJ:WINS (p 0.4515): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.5485, phi -0.618)
- KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3159, phi -0.738)

portfolios: A EV +1.75 (adj +0.46) on $18.30, P(profit) 0.6841, adj growth 3.5 bp · B EV +0.92 (adj +0.24) on $10.60, P(profit) 0.7989, adj growth 2.2 bp · C EV +0.61 (adj +0.18) on $3.20, P(profit) 0.239, adj growth 1.6 bp · R EV +0.37 (adj +0.10) on $4.00, P(profit) 0.239, adj growth 3.3 bp

## CGY @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 10 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_CGY_win | p_overtime | goals | shots COL/CGY | COL/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.151 | 0.79 | 0.21 | 0.00 | 6.06 | 35.7/22.7 | 20.4/30.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.115 | 0.82 | 0.18 | 0.00 | 9.4 | 37.4/24.2 | 20.2/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.75 | 0.25 | 0.00 | 6.0 | 29.8/28.9 | 26.3/25.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.60 | 0.40 | 0.47 | 5.92 | 36.2/23.1 | 20.0/32.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.56 | 0.44 | 0.47 | 5.99 | 29.9/29.1 | 25.7/26.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.77 | 0.23 | 0.00 | 9.4 | 31.1/30.5 | 25.6/23.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis GAME:TIGHT (p 0.3913): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no (same contract)
- thesis CGY:WINS_BY_2PLUS (p 0.143): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.2745): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order

portfolios: A EV +3.76 (adj +0.87) on $18.30, P(profit) 0.584, adj growth 7.3 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +3.17 (adj +0.73) on $11.24, P(profit) 0.5343, adj growth 6.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
