# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T06:55:56Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +18.75 | +6.22 | +17.72 | 0.661 | -35.38 | -49.67 | 53.12 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +16.93 | +6.82 | +15.61 | 0.660 | -31.44 | -44.42 | 60.54 |
| C best expression per thesis | 113.11 | +12.28 | +3.89 | +12.74 | 0.641 | -27.19 | -39.03 | 34.00 |
| R FUNDED research stakes | 36.00 | +3.69 | +1.37 | +3.35 | 0.638 | -8.69 | -11.80 | 0.00 |

## CHI @ BOS  ·  10000 joint draws  ·  434 bet sides mapped, 5 +EV candidates, 4 on card


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
| Casey Mittelstadt: 1+ goals YES | 17 | 0.222 | 0.205 | +0.042 | +0.025 | $6.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 22 | 0.260 | 0.247 | +0.028 | +0.015 | $5.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 59 | 0.634 | 0.622 | +0.027 | +0.015 | $8.41 | FUNDED_RESEARCH | $3 | BOS:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ assists NO | 56 | 0.638 | 0.592 | +0.061 | +0.015 | $9.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes; why: higher confidence-adjusted growth (9.37 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT31CHIBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: BOS offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT31CHIBOS-3|yes; why: higher confidence-adjusted growth (2.87 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.925 vs 0.754); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT31CHIBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: INTENTIONAL_DIVERSIFIER (phi -0.139); failure: CHI offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31CHIBOS-BOSPZACHA18-1|no; why: higher confidence-adjusted growth (1.94 vs 0.92 bp); despite a smaller raw edge (+0.027 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: BOS offense succeeds (4+ goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31CHIBOS-CHIPKANE88-1|no; why: higher confidence-adjusted growth (1.89 vs 0.27 bp); despite a smaller raw edge (+0.061 vs +0.074/contract); alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.139); KXNHLGOAL-26OCT31CHIBOS-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: CHI offense succeeds (4+ goals)

**Review**: scripts BOS shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.2796): highest fidelity KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.2711): highest fidelity KXNHLGOAL-26OCT31CHIBOS-BOSDPASTRNAK88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT31CHIBOS-BOSDPASTRNAK88-1|no (same contract)
- thesis CHI:SUPPRESSED (p 0.5086): highest fidelity KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no (same contract)
- KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.2711, phi -0.178)
- KXNHLGOAL-26OCT31CHIBOS-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5086, phi -0.257)
- KXNHLGOAL-26OCT31CHIBOS-BOSDPASTRNAK88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.5248, phi -0.242)
- KXNHLAST-26OCT31CHIBOS-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2796, phi -0.259)

portfolios: A EV +2.72 (adj +1.10) on $20.81, P(profit) 0.6369, adj growth 10.1 bp · B EV +3.62 (adj +1.74) on $30.26, P(profit) 0.6333, adj growth 15.3 bp · C EV +2.19 (adj +0.85) on $25.43, P(profit) 0.5334, adj growth 7.4 bp · R EV +0.13 (adj +0.07) on $3.00, P(profit) 0.6336, adj growth 2.4 bp

## STL @ DET  ·  10000 joint draws  ·  344 bet sides mapped, 2 +EV candidates, 2 on card


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
| Sheldon Dries: 1+ goals YES | 8 | 0.113 | 0.099 | +0.028 | +0.014 | $3.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 36 | 0.408 | 0.392 | +0.032 | +0.016 | $5.88 | FUNDED_RESEARCH | $2 | DET:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_STRONGER | D |
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (5.14 vs 2.35 bp); despite a smaller raw edge (+0.028 vs +0.032/contract); relationships: KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: DET offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT31STLDET-2|yes; why: higher confidence-adjusted growth (2.35 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DET:OFFENSE_4PLUS (p 0.3623): highest fidelity KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes (same contract)
- KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4186, phi -0.169)
- KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4186, phi -0.303)

portfolios: A EV +1.51 (adj +0.74) on $8.48, P(profit) 0.4744, adj growth 6.4 bp · B EV +1.50 (adj +0.74) on $8.93, P(profit) 0.4744, adj growth 6.4 bp · C EV +0.53 (adj +0.27) on $6.27, P(profit) 0.4077, adj growth 2.3 bp · R EV +0.17 (adj +0.08) on $2.00, P(profit) 0.4077, adj growth 2.8 bp

## TBL @ NSH  ·  10000 joint draws  ·  404 bet sides mapped, 2 +EV candidates, 2 on card


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
| Charle-Edouard D'Astous: 1+ goals NO | 88 | 0.936 | 0.918 | +0.048 | +0.031 | $18.87 | FUNDED_RESEARCH | $5 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 1.5 goals NO | 62 | 0.694 | 0.654 | +0.058 | +0.018 | $11.71 | FUNDED_RESEARCH | $3 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TBNSH-TB2|no; why: higher confidence-adjusted growth (21.05 vs 3.07 bp); despite a smaller raw edge (+0.048 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT31TBNSH-TB2|no: MOSTLY_INDEPENDENT (phi 0.084); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (3.07 vs 0.98 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.084); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TBL:SUPPRESSED (p 0.3705): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB2|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB2|no (same contract)
- thesis NSH:WINS (p 0.4744): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB2|no (same contract)
- KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4065, phi -0.109)
- KXNHLSPREAD-26OCT31TBNSH-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.306, phi -1.0)

portfolios: A EV +1.20 (adj +0.52) on $16.65, P(profit) 0.6588, adj growth 5.0 bp · B EV +2.08 (adj +0.98) on $30.57, P(profit) 0.6588, adj growth 9.3 bp · C EV +1.18 (adj +0.37) on $13.08, P(profit) 0.694, adj growth 3.2 bp · R EV +0.54 (adj +0.26) on $8.00, P(profit) 0.6588, adj growth 9.7 bp

## EDM @ NYI  ·  10000 joint draws  ·  220 bet sides mapped, 6 +EV candidates, 4 on card


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
| Alex Formenton: 1+ goals YES | 13 | 0.171 | 0.159 | +0.033 | +0.021 | $5.32 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 14 | 0.178 | 0.162 | +0.029 | +0.014 | $3.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Anthony Duclair: 1+ goals YES | 15 | 0.185 | 0.170 | +0.026 | +0.011 | $2.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Full Game: Over 6.5 goals scored YES | 47 | 0.532 | 0.499 | +0.045 | +0.011 | $1.85 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: higher confidence-adjusted growth (8.32 vs 4.35 bp); despite a smaller raw edge (+0.033 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.884 vs 0.375); relationships: KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT31EDMNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLTOTAL-26OCT31EDMNYI-7|yes: MOSTLY_INDEPENDENT (phi 0.117); failure: EDM offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: KXNHLTOTAL-26OCT31EDMNYI-9|yes has the higher standalone adjusted growth (4.35 vs 3.21 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.126); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT31EDMNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLTOTAL-26OCT31EDMNYI-7|yes: MOSTLY_INDEPENDENT (phi 0.119); failure: NYI offense suppressed (<= 2 goals)
- **Anthony Duclair: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: KXNHLTOTAL-26OCT31EDMNYI-9|yes has the higher standalone adjusted growth (4.35 vs 1.91 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.137); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLTOTAL-26OCT31EDMNYI-7|yes: MOSTLY_INDEPENDENT (phi 0.141); failure: NYI offense suppressed (<= 2 goals)
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: Broad expression KXNHLTOTAL-26OCT31EDMNYI-7|yes selected over broad KXNHLTOTAL-26OCT31EDMNYI-9|yes because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.76 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.117); KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.119); KXNHLGOAL-26OCT31EDMNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi 0.141); failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4499): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3308): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-9|yes — Broad expression KXNHLTOTAL-26OCT31EDMNYI-7|yes selected over broad KXNHLTOTAL-26OCT31EDMNYI-9|yes because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.76 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYI:OFFENSE_4PLUS (p 0.4158): highest fidelity KXNHLTEAMTOTAL-26OCT31EDMNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3384, phi -0.181)
- KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3666, phi -0.186)
- KXNHLGOAL-26OCT31EDMNYI-NYIADUCLAIR11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3666, phi -0.185)
- KXNHLTOTAL-26OCT31EDMNYI-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.1859, phi -0.51)
- override: Broad expression KXNHLTOTAL-26OCT31EDMNYI-7|yes selected over broad KXNHLTOTAL-26OCT31EDMNYI-9|yes because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.76 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.09 (adj +1.19) on $20.81, P(profit) 0.5384, adj growth 9.7 bp · B EV +2.53 (adj +1.36) on $13.19, P(profit) 0.4414, adj growth 11.9 bp · C EV +1.29 (adj +0.45) on $5.01, P(profit) 0.2524, adj growth 3.9 bp · R EV +0.57 (adj +0.33) on $3.00, P(profit) 0.1708, adj growth 10.8 bp

## BUF @ LAK  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 2 on card


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
| Buffalo wins by over 2.5 goals NO | 80 | 0.854 | 0.824 | +0.042 | +0.013 | $15.24 | FUNDED_RESEARCH | $4 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Los Angeles wins by over 1.5 goals YES | 26 | 0.319 | 0.287 | +0.045 | +0.013 | $2.88 | FUNDED_RESEARCH | $1 | LAK:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Buffalo wins by over 2.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31BUFLA-LA2|yes; why: higher confidence-adjusted growth (2.45 vs 1.99 bp); despite a smaller raw edge (+0.042 vs +0.045/contract); wins across more scripts (relative breadth 1.011 vs 0.518); relationships: KXNHLSPREAD-26OCT31BUFLA-LA2|yes: REINFORCING (phi 0.283); failure: BUF wins by 2+
- **Los Angeles wins by over 1.5 goals YES** — thesis: LAK wins by 2+; alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31BUFLA-BUF3|no has the higher standalone adjusted growth (2.45 vs 1.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.283); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31BUFLA-BUF3|no: REINFORCING (phi 0.283); failure: BUF wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis LAK:WINS (p 0.5422): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-LA2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS_BY_2PLUS (p 0.3189): highest fidelity KXNHLSPREAD-26OCT31BUFLA-LA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-LA2|yes (same contract)
- KXNHLSPREAD-26OCT31BUFLA-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2391, phi -0.739)
- KXNHLSPREAD-26OCT31BUFLA-LA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4578, phi -0.629)

portfolios: A EV +1.85 (adj +0.55) on $20.81, P(profit) 0.3189, adj growth 4.5 bp · B EV +1.27 (adj +0.39) on $18.12, P(profit) 0.8535, adj growth 3.4 bp · C EV +1.03 (adj +0.32) on $19.74, P(profit) 0.8535, adj growth 2.8 bp · R EV +0.37 (adj +0.11) on $5.00, P(profit) 0.3189, adj growth 3.9 bp

## OTT @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_OTT_win | p_overtime | goals | shots SJS/OTT | SJS/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.50 | 0.50 | 0.00 | 6.01 | 27.0/27.3 | 23.6/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.46 | 5.95 | 27.0/27.4 | 24.1/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.50 | 0.50 | 0.00 | 9.38 | 28.6/29.0 | 22.7/22.5 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.090 | 0.42 | 0.58 | 0.00 | 6.03 | 21.5/32.5 | 28.3/18.5 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.46 | 0.54 | 0.48 | 5.91 | 21.5/32.6 | 29.3/18.3 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.067 | 0.40 | 0.60 | 0.00 | 9.24 | 23.1/34.3 | 27.0/18.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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

## TOR @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 3 on card


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
| Toronto wins by over 1.5 goals NO | 62 | 0.710 | 0.660 | +0.073 | +0.023 | $6.73 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Toronto wins by over 2.5 goals NO | 74 | 0.813 | 0.774 | +0.059 | +0.020 | $12.58 | FUNDED_RESEARCH | $4 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver wins by over 1.5 goals YES | 22 | 0.286 | 0.248 | +0.054 | +0.016 | $2.20 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Toronto wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31TORVAN-TOR3|no; why: higher confidence-adjusted growth (5.18 vs 4.95 bp); relationships: KXNHLSPREAD-26OCT31TORVAN-TOR3|no: DUPLICATIVE (phi 0.75); KXNHLSPREAD-26OCT31TORVAN-VAN2|yes: DUPLICATIVE (phi 0.405); failure: TOR wins by 2+
- **Toronto wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31TORVAN-TOR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31TORVAN-TOR2|no has the higher standalone adjusted growth (5.18 vs 4.95 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.750); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31TORVAN-TOR2|no: DUPLICATIVE (phi 0.75); KXNHLSPREAD-26OCT31TORVAN-VAN2|yes: DUPLICATIVE (phi 0.304); failure: TOR wins by 2+
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT31TORVAN-TOR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31TORVAN-TOR2|no has the higher standalone adjusted growth (5.18 vs 3.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.405); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31TORVAN-TOR2|no: DUPLICATIVE (phi 0.405); KXNHLSPREAD-26OCT31TORVAN-TOR3|no: DUPLICATIVE (phi 0.304); failure: TOR wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:WINS (p 0.5048): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-TOR2|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.2864): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-TOR2|no (same contract)
- thesis TOR:SUPPRESSED (p 0.3579): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT31TORVAN-TOR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2903, phi -1.0)
- KXNHLSPREAD-26OCT31TORVAN-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2903, phi -0.75)
- KXNHLSPREAD-26OCT31TORVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS (p 0.4952, phi -0.627)

portfolios: A EV +2.10 (adj +0.60) on $20.81, P(profit) 0.5505, adj growth 5.1 bp · B EV +2.28 (adj +0.74) on $21.51, P(profit) 0.7097, adj growth 6.6 bp · C EV +1.99 (adj +0.63) on $17.27, P(profit) 0.7097, adj growth 5.6 bp · R EV +0.78 (adj +0.25) on $7.00, P(profit) 0.7097, adj growth 8.5 bp

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
| Dallas wins by over 2.5 goals NO | 74 | 0.799 | 0.767 | +0.045 | +0.013 | $11.88 | FUNDED_RESEARCH | $3 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Columbus wins by over 1.5 goals YES | 19 | 0.239 | 0.212 | +0.038 | +0.011 | $2.14 | FUNDED_RESEARCH | $1 | CBJ:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 2.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes; why: higher confidence-adjusted growth (2.15 vs 1.71 bp); wins across more scripts (relative breadth 1.002 vs 0.545); relationships: KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes: REINFORCING (phi 0.281); failure: DAL wins by 2+
- **Columbus wins by over 1.5 goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLSPREAD-26OCT31CBJDAL-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31CBJDAL-DAL3|no has the higher standalone adjusted growth (2.15 vs 1.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.281); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: REINFORCING (phi 0.281); failure: DAL wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:WINS (p 0.4515): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL3|no (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.239): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL3|no (same contract)
- KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3159, phi -0.738)
- KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.5485, phi -0.618)

portfolios: A EV +1.99 (adj +0.54) on $20.81, P(profit) 0.6841, adj growth 4.1 bp · B EV +1.12 (adj +0.33) on $14.03, P(profit) 0.7989, adj growth 2.9 bp · C EV +0.91 (adj +0.27) on $15.07, P(profit) 0.7989, adj growth 2.4 bp · R EV +0.37 (adj +0.11) on $4.00, P(profit) 0.239, adj growth 3.7 bp

## CGY @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 10 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_CGY_win | p_overtime | goals | shots COL/CGY | COL/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.151 | 0.79 | 0.21 | 0.00 | 6.06 | 35.7/22.7 | 20.4/30.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.115 | 0.82 | 0.18 | 0.00 | 9.4 | 37.4/24.2 | 20.2/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.75 | 0.25 | 0.00 | 6.0 | 29.8/28.9 | 26.3/25.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.60 | 0.40 | 0.47 | 5.92 | 36.2/23.1 | 20.0/32.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.56 | 0.44 | 0.47 | 5.99 | 29.9/29.1 | 25.7/26.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.77 | 0.23 | 0.00 | 9.4 | 31.1/30.5 | 25.6/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins by over 2.5 goals NO | 55 | 0.674 | 0.590 | +0.106 | +0.023 | $13.40 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL2|no; why: Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL3|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: only recommended bet in this game; failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis GAME:TIGHT (p 0.3913): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no (same contract)
- thesis COL:SUPPRESSED (p 0.2562): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no — Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL3|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CGY:WINS_BY_2PLUS (p 0.143): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no (same contract)
- KXNHLSPREAD-26OCT31CGYCOL-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.9 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4657, phi -0.745)
- override: Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL3|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-COL3|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.28 (adj +0.98) on $20.81, P(profit) 0.584, adj growth 8.2 bp · B EV +2.52 (adj +0.54) on $13.40, P(profit) 0.6738, adj growth 4.8 bp · C EV +3.17 (adj +0.73) on $11.24, P(profit) 0.5343, adj growth 6.4 bp · R EV +0.75 (adj +0.16) on $4.00, P(profit) 0.6738, adj growth 5.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
