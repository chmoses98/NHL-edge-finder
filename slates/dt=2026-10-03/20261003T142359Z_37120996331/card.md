# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T14:23:59Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +33.05 | +11.13 | +31.55 | 0.835 | -9.28 | -20.73 | 105.32 |
| B thesis-diversified (joint) ← optimiser card | 148.51 | +33.63 | +15.74 | +31.42 | 0.803 | -13.39 | -24.16 | 150.19 |
| C best expression per thesis | 149.99 | +34.13 | +15.10 | +28.93 | 0.726 | -26.86 | -40.31 | 138.05 |
| R FUNDED research stakes | 17.00 | +2.07 | +1.02 | +1.57 | 0.611 | -4.75 | -6.24 | 0.00 |

## CHI @ BUF  ·  10000 joint draws  ·  314 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_CHI_win | p_overtime | goals | shots BUF/CHI | BUF/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.139 | 0.74 | 0.26 | 0.00 | 6.02 | 33.2/21.3 | 19.0/28.4 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.55 | 0.45 | 0.48 | 5.92 | 33.4/21.5 | 18.4/30.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.68 | 0.32 | 0.00 | 6.0 | 27.8/27.1 | 24.2/23.4 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.094 | 0.75 | 0.25 | 0.00 | 9.24 | 35.1/22.7 | 18.6/26.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.53 | 0.47 | 0.46 | 5.89 | 28.1/27.4 | 24.2/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.66 | 0.34 | 0.00 | 9.28 | 29.5/28.5 | 23.5/22.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 12 | 0.163 | 0.150 | +0.035 | +0.022 | $2.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 64 | 0.747 | 0.674 | +0.091 | +0.018 | $5.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ goals NO | 60 | 0.644 | 0.628 | +0.027 | +0.011 | $2.49 | FUNDED_RESEARCH | $1 | BUF:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03CHIBUF-BUF|no; why: higher confidence-adjusted growth (9.54 vs 0.07 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0027 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03CHIBUF-CHIPKANE88-1|no; why: higher confidence-adjusted growth (3.18 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.021); failure: CHI offense succeeds (4+ goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (1.10 vs 0.18 bp); despite a smaller raw edge (+0.027 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.021); failure: BUF offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.14, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.2982): highest fidelity KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4892): highest fidelity KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no (same contract)
- thesis BUF:SUPPRESSED (p 0.3006): highest fidelity KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no (same contract)
- KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4892, phi -0.222)
- KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.2 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2982, phi -0.247)
- KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4918, phi -0.239)

portfolios: A EV +1.52 (adj +0.63) on $11.40, P(profit) 0.5611, adj growth 5.9 bp · B EV +1.43 (adj +0.55) on $10.00, P(profit) 0.5611, adj growth 5.3 bp · C EV +2.63 (adj +1.01) on $18.33, P(profit) 0.5611, adj growth 9.3 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6436, adj growth 0.7 bp

## OTT @ TOR  ·  10000 joint draws  ·  344 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_OTT_win | p_overtime | goals | shots TOR/OTT | TOR/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.140 | 0.40 | 0.60 | 0.00 | 5.98 | 21.8/34.1 | 30.0/18.9 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.122 | 0.46 | 0.54 | 0.47 | 5.89 | 21.9/34.4 | 31.0/18.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.48 | 0.52 | 0.00 | 5.97 | 27.4/28.4 | 24.8/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.50 | 0.50 | 0.48 | 5.93 | 27.7/28.6 | 25.4/24.5 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.084 | 0.39 | 0.61 | 0.00 | 9.17 | 23.1/35.9 | 28.8/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.45 | 0.55 | 0.00 | 9.27 | 29.0/29.8 | 23.2/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Stephen Halliday: 1+ goals YES | 9 | 0.141 | 0.127 | +0.046 | +0.032 | $2.70 | FUNDED_RESEARCH | $1 | OTT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Hayden Hodgson: 1+ goals YES | 8 | 0.110 | 0.102 | +0.025 | +0.017 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 11 | 0.143 | 0.131 | +0.026 | +0.014 | $1.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ assists YES | 27 | 0.337 | 0.296 | +0.053 | +0.012 | $1.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03OTTTOR-TOR|no; why: higher confidence-adjusted growth (24.23 vs 1.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT03OTTTOR-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.021); failure: OTT offense suppressed (<= 2 goals)
- **Hayden Hodgson: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03OTTTOR-TOR|no; why: higher confidence-adjusted growth (8.06 vs 1.01 bp); despite a smaller raw edge (+0.025 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT03OTTTOR-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: OTT offense suppressed (<= 2 goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03OTTTOR-TOR|no; why: higher confidence-adjusted growth (4.06 vs 1.01 bp); despite a smaller raw edge (+0.026 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT03OTTTOR-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: OTT offense suppressed (<= 2 goals)
- **Easton Cowan: 1+ assists YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT03OTTTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (1.61 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT03OTTTOR-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT03OTTTOR-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.14, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis TOR:OFFENSE_4PLUS (p 0.3378): highest fidelity KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.4341): highest fidelity KXNHLGAME-26OCT03OTTTOR-TOR|no [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.397): highest fidelity KXNHLGAME-26OCT03OTTTOR-TOR|no [DIRECT], best adjusted EV KXNHLGAME-26OCT03OTTTOR-TOR|no (same contract)
- KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.385, phi -0.169)
- KXNHLGOAL-26OCT03OTTTOR-OTTHHODGSON42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.385, phi -0.151)
- KXNHLGOAL-26OCT03OTTTOR-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.385, phi -0.169)
- KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4341, phi -0.286)

portfolios: A EV +2.49 (adj +0.96) on $11.97, P(profit) 0.4023, adj growth 9.1 bp · B EV +2.28 (adj +1.41) on $6.96, P(profit) 0.3463, adj growth 13.4 bp · C EV +1.34 (adj +0.30) on $11.35, P(profit) 0.5669, adj growth 2.7 bp · R EV +0.48 (adj +0.33) on $1.00, P(profit) 0.1413, adj growth 12.1 bp

## WSH @ TBL  ·  10000 joint draws  ·  352 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WSH_win | p_overtime | goals | shots TBL/WSH | TBL/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.67 | 0.33 | 0.00 | 6.03 | 27.1/26.6 | 23.8/22.8 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.116 | 0.71 | 0.29 | 0.00 | 5.98 | 32.5/21.1 | 18.5/27.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.54 | 0.46 | 0.47 | 5.92 | 27.1/26.9 | 23.7/24.0 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.56 | 0.44 | 0.45 | 5.93 | 32.5/21.4 | 18.2/29.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.64 | 0.36 | 0.00 | 9.29 | 28.9/28.4 | 23.0/21.9 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.076 | 0.73 | 0.27 | 0.00 | 9.19 | 34.0/22.4 | 18.1/26.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| John Carlson: 1+ assists NO | 50 | 0.740 | 0.571 | +0.223 | +0.054 | $6.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.214 | 0.202 | +0.034 | +0.022 | $2.25 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 11 | 0.144 | 0.131 | +0.027 | +0.014 | $1.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (25.23 vs 3.06 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT03WSHTB-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: TBL offense succeeds (4+ goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT03WSHTB-2|yes; why: higher confidence-adjusted growth (7.16 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT03WSHTB-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (7.16 vs 3.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.014); they share one thesis budget; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:SUPPRESSED (p 0.3142): highest fidelity KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no (same contract)
- thesis WSH:OFFENSE_4PLUS (p 0.3092): highest fidelity KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes (same contract)
- KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 26.0 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4662, phi -0.223)
- KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4775, phi -0.236)
- KXNHLGOAL-26OCT03WSHTB-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4775, phi -0.178)

portfolios: A EV +4.00 (adj +0.67) on $11.97, P(profit) 0.7404, adj growth 6.4 bp · B EV +3.73 (adj +1.14) on $10.47, P(profit) 0.8259, adj growth 11.1 bp · C EV +6.30 (adj +1.83) on $16.89, P(profit) 0.796, adj growth 17.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ PHI  ·  10000 joint draws  ·  372 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CAR_win | p_overtime | goals | shots PHI/CAR | PHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.125 | 0.52 | 0.48 | 0.00 | 5.99 | 20.5/32.2 | 28.6/17.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.50 | 0.50 | 0.48 | 5.89 | 20.5/32.2 | 29.0/17.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.62 | 0.38 | 0.00 | 6.01 | 25.9/26.7 | 23.7/21.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.56 | 0.44 | 0.49 | 5.87 | 25.9/26.5 | 23.3/22.5 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.074 | 0.50 | 0.50 | 0.49 | 2.77 | 19.1/30.6 | 29.1/17.7 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.074 | 0.52 | 0.48 | 0.00 | 3.44 | 19.5/30.9 | 29.1/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sean Couturier: 1+ goals YES | 10 | 0.180 | 0.158 | +0.074 | +0.051 | $4.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Carl Grundstrom: 1+ goals YES | 9 | 0.137 | 0.123 | +0.042 | +0.027 | $2.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Mark Jankowski: 1+ goals NO | 83 | 0.885 | 0.870 | +0.045 | +0.030 | $6.98 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Noel Acciari: 1+ goals YES | 9 | 0.133 | 0.119 | +0.037 | +0.023 | $1.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03CARPHI-PHI|yes; why: higher confidence-adjusted growth (57.70 vs 6.46 bp); despite a smaller raw edge (+0.074 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: PHI offense suppressed (<= 2 goals)
- **Carl Grundstrom: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (57.70 vs 18.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PHI offense suppressed (<= 2 goals)
- **Mark Jankowski: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03CARPHI-PHI|yes; why: higher confidence-adjusted growth (15.11 vs 6.46 bp); despite a smaller raw edge (+0.045 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: CAR offense succeeds (4+ goals)
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (57.70 vs 12.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.375): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.4669): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03CARPHI-PHI|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.5439): highest fidelity KXNHLGAME-26OCT03CARPHI-PHI|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03CARPHI-PHI|yes (same contract)
- KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3999, phi -0.224)
- KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3999, phi -0.177)
- KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3124, phi -0.164)
- KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3999, phi -0.167)

portfolios: A EV +3.14 (adj +1.81) on $11.97, P(profit) 0.5553, adj growth 17.2 bp · B EV +5.00 (adj +3.36) on $15.32, P(profit) 0.3865, adj growth 31.8 bp · C EV +5.97 (adj +3.89) on $12.10, P(profit) 0.1801, adj growth 35.0 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.8851, adj growth 2.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03CARPHI-CAR|no == KXNHLGAME-26OCT03CARPHI-PHI|yes

## MTL @ PIT  ·  10000 joint draws  ·  322 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_MTL_win | p_overtime | goals | shots PIT/MTL | PIT/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| PIT shot control · normal event (5-7) · decided (2+) | 0.124 | 0.66 | 0.34 | 0.00 | 6.04 | 32.7/20.9 | 18.2/28.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.56 | 0.44 | 0.00 | 6.09 | 27.2/26.6 | 23.3/23.3 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.100 | 0.64 | 0.36 | 0.00 | 9.35 | 34.7/22.5 | 17.5/26.9 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.54 | 0.46 | 0.46 | 5.98 | 32.9/21.5 | 18.3/29.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.52 | 0.48 | 0.47 | 5.95 | 27.3/26.8 | 23.5/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.59 | 0.41 | 0.00 | 9.46 | 28.9/28.3 | 22.7/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 13 | 0.210 | 0.187 | +0.072 | +0.049 | $4.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Filip Hallander: 1+ goals YES | 14 | 0.218 | 0.195 | +0.070 | +0.046 | $4.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Trevor van Riemsdyk: 1+ goals YES | 4 | 0.072 | 0.064 | +0.029 | +0.021 | $1.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ goals YES | 31 | 0.362 | 0.345 | +0.037 | +0.020 | $2.42 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes; why: higher confidence-adjusted growth (43.18 vs 8.50 bp); despite a smaller raw edge (+0.072 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.834 vs 0.498); relationships: KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT03MTLPIT-PITTVANRIEMSDYK57-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: PIT offense suppressed (<= 2 goals)
- **Filip Hallander: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (43.18 vs 36.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT03MTLPIT-PITTVANRIEMSDYK57-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: PIT offense suppressed (<= 2 goals)
- **Trevor van Riemsdyk: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (43.18 vs 22.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (43.18 vs 4.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT03MTLPIT-PITTVANRIEMSDYK57-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts PIT shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, PIT shot control · high event (8+) · decided (2+) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.3477): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.4718): highest fidelity KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.568): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-MTL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.222)
- KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.183)
- KXNHLGOAL-26OCT03MTLPIT-PITTVANRIEMSDYK57-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.096)
- KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.27)

portfolios: A EV +4.27 (adj +2.39) on $11.97, P(profit) 0.5393, adj growth 22.7 bp · B EV +5.64 (adj +3.84) on $12.65, P(profit) 0.4299, adj growth 36.4 bp · C EV +4.20 (adj +2.89) on $8.08, P(profit) 0.2096, adj growth 26.1 bp · R EV +0.11 (adj +0.06) on $1.00, P(profit) 0.3619, adj growth 2.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03MTLPIT-PIT|yes == KXNHLGAME-26OCT03MTLPIT-MTL|no

## UTA @ CBJ  ·  10000 joint draws  ·  342 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_UTA_win | p_overtime | goals | shots CBJ/UTA | CBJ/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.57 | 0.43 | 0.00 | 6.03 | 27.4/27.4 | 24.1/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.47 | 5.94 | 27.7/27.4 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 9.31 | 29.2/29.0 | 23.3/22.8 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.079 | 0.64 | 0.36 | 0.00 | 6.0 | 32.3/21.7 | 18.9/27.9 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.57 | 0.43 | 0.46 | 5.91 | 32.4/21.9 | 18.8/28.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.058 | 0.50 | 0.50 | 0.00 | 5.97 | 21.9/32.1 | 28.3/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vincent Trocheck: 1+ assists NO | 67 | 0.862 | 0.727 | +0.176 | +0.042 | $6.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Charlie Coyle: 1+ goals YES | 21 | 0.271 | 0.252 | +0.049 | +0.030 | $3.17 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 2+ assists NO | 94 | 0.991 | 0.958 | +0.047 | +0.014 | $6.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DIFFUSE | NONE | EVIDENCE_MIXED | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03UTACBJ-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (18.00 vs 2.72 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-2|no: REINFORCING (phi 0.238); failure: UTA offense succeeds (4+ goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03UTACBJ-CBJ|yes; why: higher confidence-adjusted growth (11.35 vs 0.75 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-2|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CBJ offense suppressed (<= 2 goals)
- **Vincent Trocheck: 2+ assists NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: REINFORCING (phi 0.238); KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.4162): highest fidelity KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.419): highest fidelity KXNHLPTS-26OCT03UTACBJ-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLPTS-26OCT03UTACBJ-UTAVTROCHECK16-1|no (same contract)
- thesis CBJ:SUPPRESSED (p 0.3649): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.7 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3582, phi -0.189)
- KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.235)
- KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; no single thesis (diffuse); fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3582, phi -0.09)

portfolios: A EV +2.93 (adj +0.86) on $11.97, P(profit) 0.7664, adj growth 8.2 bp · B EV +2.85 (adj +0.96) on $17.13, P(profit) 0.8955, adj growth 9.3 bp · C EV +3.53 (adj +1.18) on $25.02, P(profit) 0.7664, adj growth 11.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ EDM  ·  10000 joint draws  ·  356 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_SEA_win | p_overtime | goals | shots EDM/SEA | EDM/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.126 | 0.73 | 0.27 | 0.00 | 6.05 | 33.9/21.9 | 19.4/28.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.65 | 0.35 | 0.00 | 6.04 | 28.4/27.9 | 24.9/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.54 | 0.46 | 0.49 | 6.0 | 28.4/27.8 | 24.6/25.1 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.58 | 0.42 | 0.46 | 6.01 | 34.2/22.2 | 19.0/30.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.099 | 0.71 | 0.29 | 0.00 | 9.44 | 35.8/23.5 | 19.1/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.68 | 0.32 | 0.00 | 9.37 | 29.8/29.3 | 24.1/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 18 | 0.244 | 0.221 | +0.054 | +0.030 | $3.29 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 69 | 0.817 | 0.728 | +0.112 | +0.023 | $6.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Ryan Winterton: 1+ goals YES | 11 | 0.142 | 0.131 | +0.025 | +0.015 | $1.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 34 | 0.462 | 0.373 | +0.106 | +0.017 | $1.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (12.99 vs 1.64 bp); despite a smaller raw edge (+0.054 vs +0.089/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.097); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (5.53 vs 2.79 bp); relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: DUPLICATIVE (phi 0.439); failure: EDM offense succeeds (4+ goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT03SEAEDM-SEA5|yes; why: higher confidence-adjusted growth (4.40 vs 0.03 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.893 vs 0.563); alternative not eligible: confidence-adjusted EV +0.0014 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: SEA offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no; why: second expression of the same thesis: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no has the higher standalone adjusted growth (5.53 vs 2.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.439); they share one thesis budget; relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.097); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: DUPLICATIVE (phi 0.439); KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.5105): highest fidelity KXNHLAST-26OCT03SEAEDM-EDMMEKHOLM14-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2853): highest fidelity KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.3297): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2853, phi -0.224)
- KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5105, phi -0.305)
- KXNHLGOAL-26OCT03SEAEDM-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4474, phi -0.186)
- KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5105, phi -0.308)

portfolios: A EV +3.25 (adj +0.48) on $11.97, P(profit) 0.72, adj growth 4.4 bp · B EV +2.71 (adj +0.98) on $12.92, P(profit) 0.6506, adj growth 9.4 bp · C EV +3.69 (adj +1.35) on $18.66, P(profit) 0.2444, adj growth 12.5 bp · R EV +0.28 (adj +0.16) on $1.00, P(profit) 0.2444, adj growth 6.0 bp

## NJD @ NYI  ·  10000 joint draws  ·  338 bet sides mapped, 7 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_NJD_win | p_overtime | goals | shots NYI/NJD | NYI/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.57 | 0.43 | 0.00 | 5.96 | 27.8/28.0 | 24.8/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.50 | 0.50 | 0.48 | 5.86 | 27.9/27.9 | 24.7/24.6 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.073 | 0.50 | 0.50 | 0.00 | 5.98 | 22.3/32.9 | 29.1/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.59 | 0.41 | 0.00 | 9.09 | 29.4/29.4 | 23.9/23.0 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.47 | 0.53 | 0.47 | 5.88 | 22.6/33.3 | 30.0/19.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.49 | 0.51 | 0.52 | 2.79 | 26.6/26.8 | 25.3/25.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York I wins YES | 44 | 0.529 | 0.482 | +0.072 | +0.025 | $2.24 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins by over 2.5 goals NO | 79 | 0.856 | 0.821 | +0.054 | +0.019 | $5.59 | FUNDED_RESEARCH | $2 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey over 3.5 goals scored NO | 59 | 0.675 | 0.628 | +0.068 | +0.021 | $1.35 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New York I wins YES** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03NJNYI-NJ3|no; why: higher confidence-adjusted growth (5.48 vs 4.92 bp); relationships: KXNHLSPREAD-26OCT03NJNYI-NJ3|no: DUPLICATIVE (phi 0.435); KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no: REINFORCING (phi 0.51); failure: NJD wins (incl. OT/SO)
- **New Jersey wins by over 2.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03NJNYI-NYI|yes; why: second expression of the same thesis: KXNHLGAME-26OCT03NJNYI-NYI|yes has the higher standalone adjusted growth (5.48 vs 4.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.435); they share one thesis budget; relationships: KXNHLGAME-26OCT03NJNYI-NYI|yes: DUPLICATIVE (phi 0.435); KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no: DUPLICATIVE (phi 0.482); failure: NJD wins by 2+
- **New Jersey over 3.5 goals scored NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03NJNYI-NYI|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no selected over player prop KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGAME-26OCT03NJNYI-NYI|yes: REINFORCING (phi 0.51); KXNHLSPREAD-26OCT03NJNYI-NJ3|no: DUPLICATIVE (phi 0.482); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.07.
- thesis NJD:SUPPRESSED (p 0.4595): highest fidelity KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NYI|yes — Broad expression KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no selected over player prop KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYI:WINS (p 0.5294): highest fidelity KXNHLGAME-26OCT03NJNYI-NYI|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NYI|yes (same contract)
- KXNHLGAME-26OCT03NJNYI-NYI|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.4706, phi -1.0)
- KXNHLSPREAD-26OCT03NJNYI-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2413, phi -0.728)
- KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3139, phi -0.975)
- override: Broad expression KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no selected over player prop KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.73 (adj +0.47) on $11.97, P(profit) 0.6384, adj growth 4.5 bp · B EV +0.88 (adj +0.30) on $9.18, P(profit) 0.7099, adj growth 2.9 bp · C EV +1.15 (adj +0.40) on $7.30, P(profit) 0.5294, adj growth 3.7 bp · R EV +0.41 (adj +0.14) on $4.00, P(profit) 0.7099, adj growth 5.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03NJNYI-NJ|no == KXNHLGAME-26OCT03NJNYI-NYI|yes

## DAL @ NSH  ·  10000 joint draws  ·  324 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_DAL_win | p_overtime | goals | shots NSH/DAL | NSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.55 | 0.45 | 0.00 | 6.03 | 26.8/27.1 | 23.8/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.51 | 0.49 | 0.46 | 5.89 | 27.0/27.3 | 24.0/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.58 | 0.42 | 0.00 | 9.19 | 28.3/28.6 | 23.0/21.7 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.074 | 0.47 | 0.53 | 0.00 | 5.91 | 21.5/32.1 | 28.4/18.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.50 | 0.50 | 0.42 | 5.87 | 21.6/31.8 | 28.4/18.4 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.060 | 0.60 | 0.40 | 0.00 | 6.01 | 31.8/21.6 | 18.7/27.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nashville wins YES | 45 | 0.536 | 0.491 | +0.069 | +0.023 | $2.64 | FUNDED_RESEARCH | $1 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 79 | 0.848 | 0.817 | +0.047 | +0.015 | $4.08 | FUNDED_RESEARCH | $2 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Roope Hintz: 1+ assists NO | 66 | 0.762 | 0.686 | +0.087 | +0.010 | $2.05 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Nashville wins YES** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL2|no; why: higher confidence-adjusted growth (4.80 vs 3.59 bp); relationships: KXNHLSPREAD-26OCT03DALNSH-DAL3|no: DUPLICATIVE (phi 0.455); KXNHLAST-26OCT03DALNSH-DALRHINTZ24-1|no: REINFORCING (phi 0.162); failure: DAL wins (incl. OT/SO)
- **Dallas wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03DALNSH-NSH|yes; why: second expression of the same thesis: KXNHLGAME-26OCT03DALNSH-NSH|yes has the higher standalone adjusted growth (4.80 vs 3.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.455); they share one thesis budget; relationships: KXNHLGAME-26OCT03DALNSH-NSH|yes: DUPLICATIVE (phi 0.455); KXNHLAST-26OCT03DALNSH-DALRHINTZ24-1|no: MOSTLY_INDEPENDENT (phi 0.141); failure: DAL wins by 2+
- **Roope Hintz: 1+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03DALNSH-NSH|yes; why: second expression of the same thesis: KXNHLGAME-26OCT03DALNSH-NSH|yes has the higher standalone adjusted growth (4.80 vs 1.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.162); they share one thesis budget; relationships: KXNHLGAME-26OCT03DALNSH-NSH|yes: REINFORCING (phi 0.162); KXNHLSPREAD-26OCT03DALNSH-DAL3|no: MOSTLY_INDEPENDENT (phi 0.141); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:WINS (p 0.5364): highest fidelity KXNHLGAME-26OCT03DALNSH-NSH|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes (same contract)
- thesis NSH:WINS_BY_2PLUS (p 0.3038): highest fidelity KXNHLGAME-26OCT03DALNSH-NSH|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes (same contract)
- thesis DAL:SUPPRESSED (p 0.4367): highest fidelity KXNHLSPREAD-26OCT03DALNSH-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGAME-26OCT03DALNSH-NSH|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.4636, phi -1.0)
- KXNHLSPREAD-26OCT03DALNSH-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.2473, phi -0.737)
- KXNHLAST-26OCT03DALNSH-DALRHINTZ24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.7 pts; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3374, phi -0.228)

portfolios: A EV +1.62 (adj +0.33) on $11.97, P(profit) 0.6028, adj growth 3.1 bp · B EV +0.89 (adj +0.24) on $8.76, P(profit) 0.5364, adj growth 2.3 bp · C EV +1.03 (adj +0.35) on $7.00, P(profit) 0.5364, adj growth 3.2 bp · R EV +0.26 (adj +0.09) on $3.00, P(profit) 0.5364, adj growth 3.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03DALNSH-DAL|no == KXNHLGAME-26OCT03DALNSH-NSH|yes

## BOS @ MIN  ·  10000 joint draws  ·  332 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_BOS_win | p_overtime | goals | shots MIN/BOS | MIN/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.70 | 0.30 | 0.00 | 6.02 | 29.2/28.9 | 26.2/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.55 | 0.45 | 0.49 | 5.91 | 28.7/28.3 | 25.0/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.67 | 0.33 | 0.00 | 9.38 | 30.4/30.1 | 25.0/23.0 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.101 | 0.71 | 0.29 | 0.00 | 6.05 | 34.2/22.7 | 20.3/29.4 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.56 | 0.44 | 0.47 | 5.92 | 34.4/23.0 | 19.8/30.9 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.075 | 0.73 | 0.27 | 0.00 | 9.21 | 36.0/24.0 | 19.5/27.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Elias Lindholm: 1+ goals YES | 17 | 0.227 | 0.208 | +0.048 | +0.028 | $2.76 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Olli Maatta: 1+ goals YES | 5 | 0.081 | 0.069 | +0.028 | +0.016 | $1.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 12 | 0.152 | 0.140 | +0.025 | +0.013 | $1.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 24 | 0.279 | 0.266 | +0.026 | +0.013 | $1.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03BOSMIN-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (11.60 vs 1.68 bp); despite a smaller raw edge (+0.048 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: BOS offense suppressed (<= 2 goals)
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (10.87 vs 1.91 bp); relationships: KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: MIN offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (3.30 vs 1.91 bp); despite a smaller raw edge (+0.025 vs +0.026/contract); relationships: KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT03BOSMIN-7|yes; why: higher confidence-adjusted growth (1.91 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.877 vs 0.655); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis BOS:OFFENSE_4PLUS (p 0.317): highest fidelity KXNHLAST-26OCT03BOSMIN-BOSELINDHOLM28-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.4949): highest fidelity KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes (same contract)
- KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4652, phi -0.244)
- KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2885, phi -0.112)
- KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2885, phi -0.148)
- KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2885, phi -0.213)

portfolios: A EV +3.05 (adj +1.39) on $11.97, P(profit) 0.5156, adj growth 12.8 bp · B EV +1.74 (adj +1.00) on $6.65, P(profit) 0.3956, adj growth 9.5 bp · C EV +1.64 (adj +0.94) on $7.88, P(profit) 0.4465, adj growth 8.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ COL  ·  10000 joint draws  ·  336 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_STL_win | p_overtime | goals | shots COL/STL | COL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.149 | 0.71 | 0.29 | 0.00 | 6.02 | 34.0/21.4 | 18.9/29.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.57 | 0.43 | 0.45 | 5.95 | 34.2/21.8 | 18.7/30.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.112 | 0.75 | 0.25 | 0.00 | 9.28 | 35.4/22.7 | 18.5/26.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.69 | 0.31 | 0.00 | 6.05 | 28.0/27.1 | 24.4/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.53 | 0.47 | 0.47 | 5.94 | 28.3/27.4 | 24.2/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.64 | 0.36 | 0.00 | 9.32 | 30.0/28.7 | 23.5/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins NO | 28 | 0.369 | 0.322 | +0.075 | +0.028 | $2.44 | FUNDED_RESEARCH | $1 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nathan MacKinnon: 3+ assists NO | 91 | 0.970 | 0.932 | +0.054 | +0.017 | $6.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pius Suter: 1+ goals YES | 11 | 0.145 | 0.133 | +0.028 | +0.016 | $1.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 55 | 0.606 | 0.587 | +0.038 | +0.019 | $2.93 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Colorado wins NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03STLCOL-COL2|no; why: higher confidence-adjusted growth (8.05 vs 6.27 bp); despite a smaller raw edge (+0.075 vs +0.076/contract); wins across more scripts (relative breadth 1.065 vs 0.881); relationships: KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-3|no: MOSTLY_INDEPENDENT (phi 0.103); KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: REINFORCING (phi 0.22); failure: COL wins (incl. OT/SO)
- **Nathan MacKinnon: 3+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: second expression of the same thesis: KXNHLGAME-26OCT03STLCOL-COL|no has the higher standalone adjusted growth (8.05 vs 8.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.103); they share one thesis budget; relationships: KXNHLGAME-26OCT03STLCOL-COL|no: MOSTLY_INDEPENDENT (phi 0.103); KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: COL offense succeeds (4+ goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: second expression of the same thesis: KXNHLGAME-26OCT03STLCOL-COL|no has the higher standalone adjusted growth (8.05 vs 5.27 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.135); they share one thesis budget; relationships: KXNHLGAME-26OCT03STLCOL-COL|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-3|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: STL offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: second expression of the same thesis: KXNHLGAME-26OCT03STLCOL-COL|no has the higher standalone adjusted growth (8.05 vs 3.32 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.220); they share one thesis budget; relationships: KXNHLGAME-26OCT03STLCOL-COL|no: REINFORCING (phi 0.22); KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-3|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis STL:WINS (p 0.3687): highest fidelity KXNHLGAME-26OCT03STLCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no (same contract)
- thesis COL:SUPPRESSED (p 0.2896): highest fidelity KXNHLSPREAD-26OCT03STLCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.3081): highest fidelity KXNHLTEAMTOTAL-26OCT03STLCOL-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGAME-26OCT03STLCOL-COL|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS (p 0.6313, phi -1.0)
- KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-3|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4997, phi -0.16)
- KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4763, phi -0.194)
- KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4997, phi -0.279)

portfolios: A EV +2.16 (adj +0.40) on $11.97, P(profit) 0.6207, adj growth 3.8 bp · B EV +1.53 (adj +0.63) on $13.61, P(profit) 0.4336, adj growth 6.0 bp · C EV +1.72 (adj +0.63) on $8.79, P(profit) 0.5935, adj growth 5.8 bp · R EV +0.32 (adj +0.13) on $2.00, P(profit) 0.3687, adj growth 4.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03STLCOL-STL|yes == KXNHLGAME-26OCT03STLCOL-COL|no

## CGY @ VAN  ·  10000 joint draws  ·  310 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CGY_win | p_overtime | goals | shots VAN/CGY | VAN/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.59 | 0.41 | 0.00 | 5.96 | 28.3/28.3 | 25.2/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.52 | 0.48 | 0.46 | 5.94 | 28.4/28.4 | 25.1/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.62 | 0.38 | 0.00 | 9.33 | 29.6/29.7 | 24.1/22.8 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.069 | 0.68 | 0.32 | 0.00 | 6.05 | 33.1/22.7 | 20.0/28.3 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.069 | 0.55 | 0.45 | 0.00 | 6.01 | 22.7/33.3 | 29.9/19.1 | even strength |
| VAN shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.54 | 0.46 | 0.46 | 5.86 | 33.2/22.4 | 19.3/30.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 18 | 0.220 | 0.206 | +0.030 | +0.016 | $1.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Zeev Buium: 1+ goals NO | 89 | 0.923 | 0.907 | +0.026 | +0.010 | $6.98 | FUNDED_RESEARCH | $2 | VAN:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03CGYVAN-VAN2|yes; why: higher confidence-adjusted growth (3.54 vs 0.72 bp); despite a smaller raw edge (+0.030 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.903 vs 0.519); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: VAN offense suppressed (<= 2 goals)
- **Zeev Buium: 1+ goals NO** — thesis: VAN offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT03CGYVAN-10|no; why: higher confidence-adjusted growth (2.44 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: VAN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.4402): highest fidelity KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes (same contract)
- thesis VAN:SUPPRESSED (p 0.3458): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3458, phi -0.217)
- KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:OFFENSE_4PLUS (p 0.4402, phi -0.114)

portfolios: A EV +0.48 (adj +0.24) on $6.97, P(profit) 0.2199, adj growth 2.2 bp · B EV +0.45 (adj +0.21) on $8.61, P(profit) 0.202, adj growth 2.1 bp · C EV +0.46 (adj +0.25) on $2.97, P(profit) 0.2199, adj growth 2.3 bp · R EV +0.06 (adj +0.02) on $2.00, P(profit) 0.9226, adj growth 0.9 bp

## LAK @ SJS  ·  10000 joint draws  ·  312 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_LAK_win | p_overtime | goals | shots SJS/LAK | SJS/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.52 | 0.48 | 0.00 | 6.02 | 27.3/27.5 | 24.2/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.49 | 5.92 | 27.3/27.7 | 24.3/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.54 | 0.46 | 0.00 | 9.3 | 29.0/29.3 | 23.6/22.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.077 | 0.44 | 0.56 | 0.00 | 6.01 | 21.8/32.4 | 28.7/18.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.49 | 0.51 | 0.48 | 5.9 | 21.8/32.7 | 29.4/18.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.52 | 0.48 | 0.00 | 3.44 | 26.1/26.3 | 24.5/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mats Zuccarello: 1+ assists NO | 59 | 0.826 | 0.653 | +0.219 | +0.046 | $6.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Kiefer Sherwood: 1+ goals YES | 14 | 0.199 | 0.174 | +0.051 | +0.026 | $2.37 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 68 | 0.812 | 0.713 | +0.117 | +0.018 | $6.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (19.55 vs 0.24 bp); alternative not eligible: confidence-adjusted EV +0.0052 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: LAK offense succeeds (4+ goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03LASJ-LA3|no; why: higher confidence-adjusted growth (11.41 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.025); failure: SJS offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no; why: higher confidence-adjusted growth (3.36 vs 1.03 bp); relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis SJS:SUPPRESSED (p 0.3966): highest fidelity KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no (same contract)
- thesis LAK:SUPPRESSED (p 0.4231): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis SJS:OFFENSE_4PLUS (p 0.3833): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 26.6 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3574, phi -0.21)
- KXNHLGOAL-26OCT03LASJ-SJKSHERWOOD44-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3966, phi -0.198)
- KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.2 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3833, phi -0.202)

portfolios: A EV +2.40 (adj +0.50) on $11.97, P(profit) 0.6703, adj growth 4.9 bp · B EV +4.49 (adj +1.12) on $16.25, P(profit) 0.7329, adj growth 10.8 bp · C EV +0.46 (adj +0.08) on $5.62, P(profit) 0.7411, adj growth 0.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
