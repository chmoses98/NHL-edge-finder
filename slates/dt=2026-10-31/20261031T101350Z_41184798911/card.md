# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T10:13:50Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +20.96 | +7.66 | +18.20 | 0.658 | -36.47 | -49.99 | 65.91 |
| B thesis-diversified (joint) ← optimiser card | 148.18 | +22.94 | +9.69 | +19.12 | 0.649 | -38.32 | -52.53 | 84.10 |
| C best expression per thesis | 110.84 | +13.09 | +4.33 | +12.39 | 0.646 | -27.29 | -41.32 | 38.05 |
| R FUNDED research stakes | 34.00 | +4.58 | +1.61 | +4.12 | 0.614 | -10.45 | -13.14 | 0.00 |

## CHI @ BOS  ·  10000 joint draws  ·  434 bet sides mapped, 2 +EV candidates, 2 on card


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
| Casey Mittelstadt: 1+ goals YES | 16 | 0.222 | 0.205 | +0.052 | +0.036 | $9.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Roman Kantserov: 1+ goals NO | 76 | 0.794 | 0.785 | +0.022 | +0.012 | $13.36 | FUNDED_RESEARCH | $4 | CHI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes; why: higher confidence-adjusted growth (19.50 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: BOS offense suppressed (<= 2 goals)
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31CHIBOS-CHIPKANE88-1|no; why: higher confidence-adjusted growth (1.76 vs 0.27 bp); despite a smaller raw edge (+0.022 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: CHI offense succeeds (4+ goals)

**Review**: scripts BOS shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis CHI:SUPPRESSED (p 0.5086): highest fidelity KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.5248): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT31CHIBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.2711, phi -0.178)
- KXNHLGOAL-26OCT31CHIBOS-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2796, phi -0.206)

portfolios: A EV +2.44 (adj +1.63) on $15.99, P(profit) 0.2219, adj growth 14.7 bp · B EV +3.47 (adj +2.31) on $23.36, P(profit) 0.2219, adj growth 19.9 bp · C EV +0.38 (adj +0.21) on $13.47, P(profit) 0.7945, adj growth 1.8 bp · R EV +0.11 (adj +0.06) on $4.00, P(profit) 0.7945, adj growth 2.1 bp

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
| Sheldon Dries: 1+ goals YES | 7 | 0.113 | 0.095 | +0.039 | +0.021 | $4.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 36 | 0.408 | 0.390 | +0.032 | +0.013 | $5.22 | FUNDED_RESEARCH | $2 | DET:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_STRONGER | D |
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (12.93 vs 1.67 bp); relationships: KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: DET offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT31STLDET-2|yes; why: higher confidence-adjusted growth (1.67 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DET:OFFENSE_4PLUS (p 0.3623): highest fidelity KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes (same contract)
- KXNHLGOAL-26OCT31STLDET-DETSDRIES15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4186, phi -0.169)
- KXNHLGOAL-26OCT31STLDET-DETADEBRINCAT93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4186, phi -0.303)

portfolios: A EV +2.92 (adj +1.49) on $10.34, P(profit) 0.4744, adj growth 12.7 bp · B EV +2.80 (adj +1.43) on $9.74, P(profit) 0.4744, adj growth 12.3 bp · C EV +0.44 (adj +0.19) on $5.27, P(profit) 0.4077, adj growth 1.6 bp · R EV +0.17 (adj +0.07) on $2.00, P(profit) 0.4077, adj growth 2.3 bp

## TBL @ NSH  ·  10000 joint draws  ·  404 bet sides mapped, 1 +EV candidates, 1 on card


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
| Tampa Bay wins by over 1.5 goals NO | 62 | 0.694 | 0.654 | +0.058 | +0.018 | $13.08 | FUNDED_RESEARCH | $4 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (3.07 vs 0.74 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NSH:WINS (p 0.4744): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB2|no (same contract)
- KXNHLSPREAD-26OCT31TBNSH-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.306, phi -1.0)

portfolios: A EV +0.81 (adj +0.25) on $8.93, P(profit) 0.694, adj growth 2.3 bp · B EV +1.18 (adj +0.37) on $13.08, P(profit) 0.694, adj growth 3.2 bp · C EV +1.18 (adj +0.37) on $13.08, P(profit) 0.694, adj growth 3.2 bp · R EV +0.36 (adj +0.11) on $4.00, P(profit) 0.694, adj growth 3.9 bp

## EDM @ NYI  ·  10000 joint draws  ·  424 bet sides mapped, 7 +EV candidates, 4 on card


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
| Mattias Ekholm: 1+ goals YES | 7 | 0.109 | 0.092 | +0.035 | +0.017 | $3.96 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.178 | 0.155 | +0.040 | +0.017 | $4.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.263 | 0.240 | +0.042 | +0.018 | $5.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Ryan Nugent-Hopkins: 1+ assists NO | 65 | 0.729 | 0.680 | +0.063 | +0.014 | $12.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: higher confidence-adjusted growth (9.30 vs 4.35 bp); despite a smaller raw edge (+0.035 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.818 vs 0.375); relationships: KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT31EDMNYI-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.045); failure: EDM offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: higher confidence-adjusted growth (5.06 vs 4.35 bp); despite a smaller raw edge (+0.040 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.877 vs 0.375); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT31EDMNYI-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: NYI offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: KXNHLTOTAL-26OCT31EDMNYI-9|yes has the higher standalone adjusted growth (4.35 vs 4.18 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.136); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT31EDMNYI-EDMRNUGENTHOPKINS93-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: NYI offense suppressed (<= 2 goals)
- **Ryan Nugent-Hopkins: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (1.86 vs 1.42 bp); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4499): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:OFFENSE_4PLUS (p 0.4158): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3308): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-9|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3384, phi -0.148)
- KXNHLGOAL-26OCT31EDMNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3666, phi -0.186)
- KXNHLGOAL-26OCT31EDMNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3666, phi -0.224)
- KXNHLAST-26OCT31EDMNYI-EDMRNUGENTHOPKINS93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4499, phi -0.219)

portfolios: A EV +2.93 (adj +0.83) on $22.34, P(profit) 0.4067, adj growth 7.3 bp · B EV +5.26 (adj +2.14) on $25.97, P(profit) 0.4073, adj growth 18.5 bp · C EV +2.72 (adj +0.78) on $19.12, P(profit) 0.8238, adj growth 6.8 bp · R EV +0.46 (adj +0.23) on $1.00, P(profit) 0.1092, adj growth 7.9 bp

## BUF @ LAK  ·  10000 joint draws  ·  426 bet sides mapped, 3 +EV candidates, 3 on card


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
| Scott Laughton: 1+ goals YES | 13 | 0.160 | 0.150 | +0.022 | +0.012 | $2.87 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 2.5 goals NO | 80 | 0.854 | 0.824 | +0.042 | +0.013 | $15.50 | FUNDED_RESEARCH | $4 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 1.5 goals NO | 70 | 0.761 | 0.728 | +0.046 | +0.013 | $2.40 | FUNDED_RESEARCH | $1 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Scott Laughton: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: higher confidence-adjusted growth (2.56 vs 2.45 bp); despite a smaller raw edge (+0.022 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT31BUFLA-BUF3|no: MOSTLY_INDEPENDENT (phi 0.11); KXNHLSPREAD-26OCT31BUFLA-BUF2|no: MOSTLY_INDEPENDENT (phi 0.124); failure: LAK offense suppressed (<= 2 goals)
- **Buffalo wins by over 2.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF2|no; why: higher confidence-adjusted growth (2.45 vs 1.89 bp); despite a smaller raw edge (+0.042 vs +0.046/contract); relationships: KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.11); KXNHLSPREAD-26OCT31BUFLA-BUF2|no: DUPLICATIVE (phi 0.739); failure: BUF wins by 2+
- **Buffalo wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31BUFLA-BUF3|no has the higher standalone adjusted growth (2.45 vs 1.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.739); they share one thesis budget; relationships: KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.124); KXNHLSPREAD-26OCT31BUFLA-BUF3|no: DUPLICATIVE (phi 0.739); failure: BUF wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis LAK:OFFENSE_4PLUS (p 0.4021): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS (p 0.5422): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no (same contract)
- KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3772, phi -0.192)
- KXNHLSPREAD-26OCT31BUFLA-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2391, phi -0.739)
- KXNHLSPREAD-26OCT31BUFLA-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2391, phi -1.0)

portfolios: A EV +1.49 (adj +0.55) on $20.69, P(profit) 0.7705, adj growth 4.8 bp · B EV +1.42 (adj +0.54) on $20.78, P(profit) 0.7797, adj growth 4.7 bp · C EV +1.39 (adj +0.54) on $20.81, P(profit) 0.8627, adj growth 4.7 bp · R EV +0.27 (adj +0.08) on $5.00, P(profit) 0.7609, adj growth 2.9 bp

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
| Adam Gaudette: 1+ goals YES | 12 | 0.164 | 0.146 | +0.037 | +0.018 | $4.65 | FUNDED_RESEARCH | $2 | SJS:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Adam Gaudette: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31OTTSJ-OTT3|no; why: higher confidence-adjusted growth (6.41 vs 0.38 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0055 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4049): highest fidelity KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes (same contract)
- KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3868, phi -0.208)

portfolios: A EV +1.35 (adj +0.67) on $4.70, P(profit) 0.1641, adj growth 5.8 bp · B EV +1.34 (adj +0.66) on $4.65, P(profit) 0.1641, adj growth 5.7 bp · C EV +1.34 (adj +0.66) on $4.65, P(profit) 0.1641, adj growth 5.7 bp · R EV +0.58 (adj +0.29) on $2.00, P(profit) 0.1641, adj growth 8.8 bp

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

## TOR @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 2 on card


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
| Toronto wins by over 2.5 goals NO | 73 | 0.813 | 0.769 | +0.069 | +0.025 | $20.00 | FUNDED_RESEARCH | $5 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver wins by over 1.5 goals YES | 22 | 0.286 | 0.251 | +0.054 | +0.019 | $3.75 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Toronto wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes; why: higher confidence-adjusted growth (7.29 vs 4.26 bp); wins across more scripts (relative breadth 1.029 vs 0.52); relationships: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes: DUPLICATIVE (phi 0.304); failure: TOR wins by 2+
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT31TORVAN-TOR3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31TORVAN-TOR3|no has the higher standalone adjusted growth (7.29 vs 4.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.304); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31TORVAN-TOR3|no: DUPLICATIVE (phi 0.304); failure: TOR wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:WINS (p 0.5048): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-TOR3|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.2864): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-TOR3|no (same contract)
- thesis TOR:SUPPRESSED (p 0.3579): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-TOR3|no (same contract)
- KXNHLSPREAD-26OCT31TORVAN-TOR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2903, phi -0.75)
- KXNHLSPREAD-26OCT31TORVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS (p 0.4952, phi -0.627)

portfolios: A EV +2.49 (adj +0.63) on $22.34, P(profit) 0.5505, adj growth 5.3 bp · B EV +2.74 (adj +0.98) on $23.75, P(profit) 0.8128, adj growth 8.7 bp · C EV +1.86 (adj +0.67) on $20.00, P(profit) 0.8128, adj growth 6.2 bp · R EV +0.70 (adj +0.25) on $6.00, P(profit) 0.8128, adj growth 8.9 bp

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
| Columbus wins by over 1.5 goals YES | 19 | 0.239 | 0.212 | +0.038 | +0.011 | $2.50 | FUNDED_RESEARCH | $1 | CBJ:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 74 | 0.799 | 0.764 | +0.045 | +0.011 | $9.67 | FUNDED_RESEARCH | $3 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Columbus wins by over 1.5 goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLSPREAD-26OCT31CBJDAL-DAL3|no; why: higher confidence-adjusted growth (1.71 vs 1.43 bp); despite a smaller raw edge (+0.038 vs +0.045/contract); relationships: KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: REINFORCING (phi 0.281); failure: DAL wins (incl. OT/SO)
- **Dallas wins by over 2.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes has the higher standalone adjusted growth (1.71 vs 1.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.281); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes: REINFORCING (phi 0.281); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:WINS_BY_2PLUS (p 0.239): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes (same contract)
- thesis CBJ:WINS (p 0.4515): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT31CBJDAL-CBJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.5485, phi -0.618)
- KXNHLSPREAD-26OCT31CBJDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3159, phi -0.738)

portfolios: A EV +2.14 (adj +0.56) on $22.34, P(profit) 0.6841, adj growth 4.0 bp · B EV +1.06 (adj +0.28) on $12.17, P(profit) 0.7989, adj growth 2.5 bp · C EV +0.61 (adj +0.18) on $3.20, P(profit) 0.239, adj growth 1.6 bp · R EV +0.37 (adj +0.10) on $4.00, P(profit) 0.239, adj growth 3.3 bp

## CGY @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 9 +EV candidates, 4 on card


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
| Colorado wins by over 1.5 goals NO | 40 | 0.534 | 0.444 | +0.117 | +0.027 | $4.82 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado over 3.5 goals scored NO | 35 | 0.436 | 0.388 | +0.070 | +0.022 | $4.88 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 55 | 0.674 | 0.590 | +0.106 | +0.023 | $3.03 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Calgary over 4.5 goals scored YES | 9 | 0.136 | 0.108 | +0.040 | +0.012 | $1.95 | FUNDED_RESEARCH | $1 | CGY:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4|no; why: Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes because adjusted EV is 1.2 pts higher while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4|no: REINFORCING (phi 0.563); KXNHLSPREAD-26OCT31CGYCOL-COL3|no: DUPLICATIVE (phi 0.745); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY5|yes: REINFORCING (phi 0.31); failure: COL wins by 2+
- **Colorado over 3.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31CGYCOL-COL2|no has the higher standalone adjusted growth (6.53 vs 4.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.563); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31CGYCOL-COL2|no: REINFORCING (phi 0.563); KXNHLSPREAD-26OCT31CGYCOL-COL3|no: REINFORCING (phi 0.524); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY5|yes: INTENTIONAL_DIVERSIFIER (phi 0.006); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL2|no; why: Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL3|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no because adjusted EV is 1.0 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT31CGYCOL-COL2|no: DUPLICATIVE (phi 0.745); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4|no: REINFORCING (phi 0.524); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY5|yes: REINFORCING (phi 0.245); failure: COL wins by 2+
- **Calgary over 4.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31CGYCOL-COL2|no has the higher standalone adjusted growth (6.53 vs 3.66 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.310); they share one thesis budget; relationships: KXNHLSPREAD-26OCT31CGYCOL-COL2|no: REINFORCING (phi 0.31); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4|no: INTENTIONAL_DIVERSIFIER (phi 0.006); KXNHLSPREAD-26OCT31CGYCOL-COL3|no: REINFORCING (phi 0.245); failure: COL wins (incl. OT/SO)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis GAME:TIGHT (p 0.3913): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no (same contract)
- thesis COL:SUPPRESSED (p 0.2562): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS_BY_2PLUS (p 0.143): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL2|no (same contract)
- KXNHLSPREAD-26OCT31CGYCOL-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.9 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4657, phi -1.0)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-COL4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5534, phi -0.979)
- KXNHLSPREAD-26OCT31CGYCOL-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.9 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4657, phi -0.745)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY5|yes: FUNDED_RESEARCH; family MIXED; loses 51% of the draws where the thesis happens; opposing: failure thesis COL:WINS (p 0.6869, phi -0.434)
- override: Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes because adjusted EV is 1.2 pts higher while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL3|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no because adjusted EV is 1.0 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.39 (adj +1.05) on $22.34, P(profit) 0.5776, adj growth 8.9 bp · B EV +3.68 (adj +0.98) on $14.68, P(profit) 0.5879, adj growth 8.5 bp · C EV +3.17 (adj +0.73) on $11.24, P(profit) 0.5343, adj growth 6.4 bp · R EV +1.55 (adj +0.42) on $6.00, P(profit) 0.5879, adj growth 13.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
