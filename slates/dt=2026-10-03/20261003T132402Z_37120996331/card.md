# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T13:24:02Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +31.86 | +10.91 | +29.44 | 0.788 | -16.30 | -28.24 | 101.32 |
| B thesis-diversified (joint) ← optimiser card | 149.46 | +32.05 | +14.29 | +27.61 | 0.751 | -19.90 | -31.41 | 133.47 |
| C best expression per thesis | 150.01 | +34.01 | +13.15 | +29.10 | 0.743 | -22.81 | -34.35 | 120.17 |
| R FUNDED research stakes | 18.00 | +3.09 | +1.67 | +0.70 | 0.531 | -6.52 | -8.29 | 0.00 |

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
| Ryan Greene: 1+ goals YES | 12 | 0.163 | 0.145 | +0.035 | +0.017 | $2.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 64 | 0.747 | 0.674 | +0.091 | +0.018 | $7.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ goals NO | 60 | 0.644 | 0.628 | +0.027 | +0.011 | $3.43 | FUNDED_RESEARCH | $1 | BUF:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03CHIBUF-BUF|no; why: higher confidence-adjusted growth (5.75 vs 0.07 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0027 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03CHIBUF-CHIPKANE88-1|no; why: higher confidence-adjusted growth (3.18 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.021); failure: CHI offense succeeds (4+ goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (1.10 vs 0.18 bp); despite a smaller raw edge (+0.027 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.021); failure: BUF offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.14, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.2982): highest fidelity KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4892): highest fidelity KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no (same contract)
- thesis BUF:SUPPRESSED (p 0.3006): highest fidelity KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no (same contract)
- KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4892, phi -0.222)
- KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.2 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2982, phi -0.247)
- KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4918, phi -0.239)

portfolios: A EV +1.80 (adj +0.63) on $13.52, P(profit) 0.5611, adj growth 5.8 bp · B EV +1.76 (adj +0.55) on $12.95, P(profit) 0.5611, adj growth 5.2 bp · C EV +2.35 (adj +0.73) on $17.30, P(profit) 0.5611, adj growth 6.7 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6436, adj growth 0.7 bp

## OTT @ TOR  ·  10000 joint draws  ·  344 bet sides mapped, 5 +EV candidates, 4 on card


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
| Stephen Halliday: 1+ goals YES | 9 | 0.141 | 0.120 | +0.046 | +0.024 | $2.59 | FUNDED_RESEARCH | $1 | OTT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 11 | 0.143 | 0.130 | +0.026 | +0.013 | $1.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Darren Raddysh: 1+ assists NO | 58 | 0.710 | 0.616 | +0.113 | +0.019 | $6.38 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Claude Giroux: 1+ assists YES | 27 | 0.371 | 0.295 | +0.087 | +0.012 | $1.04 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:OFFENSE_4PLUS | DIRECT (0.54) | EVIDENCE_MIXED | D |
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (14.17 vs 1.46 bp); despite a smaller raw edge (+0.046 vs +0.087/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi 0.129); failure: OTT offense suppressed (<= 2 goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (3.37 vs 1.46 bp); despite a smaller raw edge (+0.026 vs +0.087/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi 0.048); failure: OTT offense suppressed (<= 2 goals)
- **Darren Raddysh: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03OTTTOR-TOR|no; why: higher confidence-adjusted growth (3.21 vs 1.01 bp); relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT03OTTTOR-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: TOR offense succeeds (4+ goals)
- **Claude Giroux: 1+ assists YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03OTTTOR-TOR|no; why: higher confidence-adjusted growth (1.46 vs 1.01 bp); relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.129); KXNHLGOAL-26OCT03OTTTOR-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.048); KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no: MOSTLY_INDEPENDENT (phi -0.026); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.14, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis TOR:SUPPRESSED (p 0.4341): highest fidelity KXNHLGAME-26OCT03OTTTOR-TOR|no [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.397): highest fidelity KXNHLGAME-26OCT03OTTTOR-TOR|no [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:WINS (p 0.5414): highest fidelity KXNHLGAME-26OCT03OTTTOR-TOR|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.385, phi -0.169)
- KXNHLGOAL-26OCT03OTTTOR-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.385, phi -0.169)
- KXNHLAST-26OCT03OTTTOR-TORDRADDYSH43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.5 pts; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3378, phi -0.223)
- KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 46% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.6 pts; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.385, phi -0.299)

portfolios: A EV +3.46 (adj +0.99) on $14.20, P(profit) 0.5955, adj growth 8.9 bp · B EV +3.10 (adj +1.06) on $11.54, P(profit) 0.4365, adj growth 9.9 bp · C EV +2.34 (adj +0.36) on $10.87, P(profit) 0.7102, adj growth 3.4 bp · R EV +0.48 (adj +0.25) on $1.00, P(profit) 0.1413, adj growth 9.0 bp

## WSH @ TBL  ·  10000 joint draws  ·  352 bet sides mapped, 4 +EV candidates, 3 on card


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
| John Carlson: 1+ assists NO | 51 | 0.740 | 0.571 | +0.213 | +0.044 | $6.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
| John Carlson: 2+ assists NO | 86 | 0.966 | 0.887 | +0.097 | +0.019 | $6.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (1.00) | EVIDENCE_MIXED | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.214 | 0.200 | +0.034 | +0.020 | $2.67 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (16.74 vs 5.53 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-2|no: DUPLICATIVE (phi 0.319); KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: TBL offense succeeds (4+ goals)
- **John Carlson: 2+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no; why: second expression of the same thesis: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no has the higher standalone adjusted growth (16.74 vs 6.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.319); they share one thesis budget; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: DUPLICATIVE (phi 0.319); KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: TBL offense succeeds (4+ goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT03WSHTB-2|yes; why: higher confidence-adjusted growth (5.64 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT03WSHTB-TBJCARLSON74-2|no: MOSTLY_INDEPENDENT (phi 0.001); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:SUPPRESSED (p 0.3142): highest fidelity KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no (same contract)
- thesis WSH:OFFENSE_4PLUS (p 0.3092): highest fidelity KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes (same contract)
- KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 26.0 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4662, phi -0.223)
- KXNHLAST-26OCT03WSHTB-TBJCARLSON74-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 0% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4662, phi -0.144)
- KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4775, phi -0.236)

portfolios: A EV +4.42 (adj +0.88) on $14.20, P(profit) 0.7171, adj growth 8.4 bp · B EV +4.05 (adj +1.01) on $16.41, P(profit) 0.7887, adj growth 9.7 bp · C EV +5.82 (adj +1.44) on $16.28, P(profit) 0.796, adj growth 13.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ PHI  ·  10000 joint draws  ·  372 bet sides mapped, 15 +EV candidates, 4 on card


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
| Sean Couturier: 1+ goals YES | 10 | 0.180 | 0.156 | +0.074 | +0.050 | $5.42 | FUNDED_RESEARCH | $2 | PHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Carl Grundstrom: 1+ goals YES | 8 | 0.137 | 0.119 | +0.052 | +0.034 | $3.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Noel Acciari: 1+ goals YES | 9 | 0.133 | 0.119 | +0.037 | +0.023 | $2.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 18 | 0.227 | 0.210 | +0.037 | +0.020 | $2.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03CARPHI-PHI|yes; why: higher confidence-adjusted growth (54.98 vs 6.46 bp); despite a smaller raw edge (+0.074 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: PHI offense suppressed (<= 2 goals)
- **Carl Grundstrom: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (54.98 vs 31.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: PHI offense suppressed (<= 2 goals)
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (54.98 vs 12.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (54.98 vs 5.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.375): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.5439): highest fidelity KXNHLGAME-26OCT03CARPHI-PHI|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03CARPHI-PHI|yes (same contract)
- thesis CAR:SUPPRESSED (p 0.4669): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03CARPHI-PHI|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3999, phi -0.224)
- KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3999, phi -0.177)
- KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3999, phi -0.167)
- KXNHLGOAL-26OCT03CARPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.3999, phi -0.209)

portfolios: A EV +3.76 (adj +2.10) on $14.20, P(profit) 0.5045, adj growth 19.8 bp · B EV +7.50 (adj +4.89) on $14.28, P(profit) 0.3865, adj growth 45.3 bp · C EV +5.77 (adj +3.67) on $11.86, P(profit) 0.1801, adj growth 33.0 bp · R EV +1.39 (adj +0.94) on $2.00, P(profit) 0.1801, adj growth 33.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03CARPHI-CAR|no == KXNHLGAME-26OCT03CARPHI-PHI|yes

## MTL @ PIT  ·  10000 joint draws  ·  322 bet sides mapped, 11 +EV candidates, 4 on card


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
| Connor Dewar: 1+ goals YES | 13 | 0.210 | 0.187 | +0.072 | +0.049 | $5.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Trevor van Riemsdyk: 1+ goals YES | 4 | 0.072 | 0.061 | +0.029 | +0.019 | $1.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Pittsburgh wins by over 1.5 goals YES | 26 | 0.348 | 0.301 | +0.074 | +0.028 | $1.13 | FUNDED_RESEARCH | $1 | PIT:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sidney Crosby: 1+ goals YES | 31 | 0.362 | 0.346 | +0.037 | +0.021 | $3.23 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes; why: higher confidence-adjusted growth (43.18 vs 8.50 bp); despite a smaller raw edge (+0.072 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.834 vs 0.498); relationships: KXNHLGOAL-26OCT03MTLPIT-PITTVANRIEMSDYK57-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes: REINFORCING (phi 0.244); KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: PIT offense suppressed (<= 2 goals)
- **Trevor van Riemsdyk: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (43.18 vs 17.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes: MOSTLY_INDEPENDENT (phi 0.069); KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PIT offense suppressed (<= 2 goals)
- **Pittsburgh wins by over 1.5 goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: Broad expression KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes selected over broad KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes because adjusted EV is 0.5 pts higher while thesis capture is 1.00 vs 0.66 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: REINFORCING (phi 0.244); KXNHLGOAL-26OCT03MTLPIT-PITTVANRIEMSDYK57-1|yes: MOSTLY_INDEPENDENT (phi 0.069); KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: REINFORCING (phi 0.221); failure: MTL wins (incl. OT/SO)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (43.18 vs 4.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT03MTLPIT-PITTVANRIEMSDYK57-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes: REINFORCING (phi 0.221); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts PIT shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, PIT shot control · high event (8+) · decided (2+) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.3477): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — Broad expression KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes selected over broad KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes because adjusted EV is 0.5 pts higher while thesis capture is 1.00 vs 0.66 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis PIT:OFFENSE_4PLUS (p 0.4718): highest fidelity KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.568): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-MTL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.222)
- KXNHLGOAL-26OCT03MTLPIT-PITTVANRIEMSDYK57-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.096)
- KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS (p 0.432, phi -0.637)
- KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.27)
- override: Broad expression KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes selected over broad KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes because adjusted EV is 0.5 pts higher while thesis capture is 1.00 vs 0.66 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.97 (adj +1.92) on $14.20, P(profit) 0.5282, adj growth 17.6 bp · B EV +4.92 (adj +3.19) on $11.95, P(profit) 0.3781, adj growth 29.6 bp · C EV +4.17 (adj +2.87) on $8.03, P(profit) 0.2096, adj growth 25.9 bp · R EV +0.39 (adj +0.17) on $2.00, P(profit) 0.5331, adj growth 6.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03MTLPIT-PIT|yes == KXNHLGAME-26OCT03MTLPIT-MTL|no

## UTA @ CBJ  ·  10000 joint draws  ·  342 bet sides mapped, 5 +EV candidates, 4 on card


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
| Charlie Coyle: 1+ goals YES | 21 | 0.271 | 0.248 | +0.049 | +0.026 | $3.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 2+ assists NO | 94 | 0.991 | 0.958 | +0.047 | +0.014 | $9.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DIFFUSE | NONE | EVIDENCE_MIXED | D |
| Danton Heinen: 1+ goals YES | 10 | 0.132 | 0.120 | +0.025 | +0.014 | $1.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Conor Garland: 1+ goals NO | 83 | 0.863 | 0.851 | +0.024 | +0.011 | $8.70 | FUNDED_RESEARCH | $3 | CBJ:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (8.71 vs 0.20 bp); alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-2|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: CBJ offense suppressed (<= 2 goals)
- **Vincent Trocheck: 2+ assists NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: UTA offense succeeds (4+ goals)
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (8.71 vs 4.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-2|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: CBJ offense suppressed (<= 2 goals)
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03UTACBJ-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (2.14 vs 0.60 bp); despite a smaller raw edge (+0.024 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0077 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-2|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.4162): highest fidelity KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.419): highest fidelity KXNHLPTS-26OCT03UTACBJ-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLPTS-26OCT03UTACBJ-UTAVTROCHECK16-1|no (same contract)
- thesis CBJ:SUPPRESSED (p 0.3649): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.235)
- KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; no single thesis (diffuse); fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3582, phi -0.09)
- KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.15)
- KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4162, phi -0.154)

portfolios: A EV +2.43 (adj +0.79) on $14.20, P(profit) 0.3679, adj growth 7.4 bp · B EV +1.95 (adj +0.92) on $23.64, P(profit) 0.3674, adj growth 8.7 bp · C EV +2.68 (adj +0.87) on $21.83, P(profit) 0.2706, adj growth 8.1 bp · R EV +0.08 (adj +0.04) on $3.00, P(profit) 0.8634, adj growth 1.5 bp

## SEA @ EDM  ·  10000 joint draws  ·  356 bet sides mapped, 3 +EV candidates, 3 on card


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
| Connor McDavid: 2+ assists NO | 69 | 0.817 | 0.728 | +0.112 | +0.023 | $8.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ assists YES | 26 | 0.388 | 0.295 | +0.114 | +0.021 | $3.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
| Kasperi Kapanen: 1+ goals NO | 77 | 0.805 | 0.794 | +0.023 | +0.011 | $5.64 | FUNDED_RESEARCH | $2 | EDM:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (5.53 vs 0.09 bp); alternative not eligible: confidence-adjusted EV +0.0032 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03SEAEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.074); KXNHLGOAL-26OCT03SEAEDM-EDMKKAPANEN42-1|no: MOSTLY_INDEPENDENT (phi 0.068); failure: EDM offense succeeds (4+ goals)
- **Mattias Ekholm: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (5.08 vs 0.89 bp); alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.074); KXNHLGOAL-26OCT03SEAEDM-EDMKKAPANEN42-1|no: INTENTIONAL_DIVERSIFIER (phi -0.054); failure: EDM offense suppressed (<= 2 goals)
- **Kasperi Kapanen: 1+ goals NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no; why: second expression of the same thesis: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no has the higher standalone adjusted growth (5.53 vs 1.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.068); they share one thesis budget; relationships: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi 0.068); KXNHLAST-26OCT03SEAEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.054); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:SUPPRESSED (p 0.2853): highest fidelity KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.5105): highest fidelity KXNHLAST-26OCT03SEAEDM-EDMMEKHOLM14-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT03SEAEDM-EDMMEKHOLM14-1|yes (same contract)
- KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5105, phi -0.305)
- KXNHLAST-26OCT03SEAEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2853, phi -0.253)
- KXNHLGOAL-26OCT03SEAEDM-EDMKKAPANEN42-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5105, phi -0.187)

portfolios: A EV +2.87 (adj +0.60) on $14.20, P(profit) 0.3879, adj growth 5.6 bp · B EV +2.92 (adj +0.62) on $17.60, P(profit) 0.7938, adj growth 5.9 bp · C EV +3.83 (adj +0.75) on $17.06, P(profit) 0.8167, adj growth 7.0 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.8052, adj growth 1.1 bp

## NJD @ NYI  ·  10000 joint draws  ·  338 bet sides mapped, 8 +EV candidates, 4 on card


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
| New Jersey wins by over 1.5 goals NO | 68 | 0.759 | 0.717 | +0.064 | +0.022 | $6.78 | FUNDED_RESEARCH | $2 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins NO | 45 | 0.529 | 0.487 | +0.062 | +0.020 | $2.24 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins by over 2.5 goals NO | 80 | 0.856 | 0.826 | +0.045 | +0.014 | $2.15 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Kyle Palmieri: 1+ assists NO | 70 | 0.816 | 0.728 | +0.101 | +0.013 | $8.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03NJNYI-NJ|no; why: higher confidence-adjusted growth (4.85 vs 3.47 bp); relationships: KXNHLGAME-26OCT03NJNYI-NJ|no: DUPLICATIVE (phi 0.598); KXNHLSPREAD-26OCT03NJNYI-NJ3|no: DUPLICATIVE (phi 0.728); KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: INTENTIONAL_DIVERSIFIER (phi -0.118); failure: NJD wins by 2+
- **New Jersey wins NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03NJNYI-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT03NJNYI-NJ2|no has the higher standalone adjusted growth (4.85 vs 3.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.598); they share one thesis budget; relationships: KXNHLSPREAD-26OCT03NJNYI-NJ2|no: DUPLICATIVE (phi 0.598); KXNHLSPREAD-26OCT03NJNYI-NJ3|no: DUPLICATIVE (phi 0.435); KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: INTENTIONAL_DIVERSIFIER (phi -0.139); failure: NJD wins (incl. OT/SO)
- **New Jersey wins by over 2.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03NJNYI-NJ2|no; why: Broad expression KXNHLSPREAD-26OCT03NJNYI-NJ3|no selected over player prop KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT03NJNYI-NJ2|no: DUPLICATIVE (phi 0.728); KXNHLGAME-26OCT03NJNYI-NJ|no: DUPLICATIVE (phi 0.435); KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: INTENTIONAL_DIVERSIFIER (phi -0.096); failure: NJD wins by 2+
- **Kyle Palmieri: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT03NJNYI-6|no; why: higher confidence-adjusted growth (1.79 vs 0.38 bp); wins across more scripts (relative breadth 1.002 vs 0.763); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLSPREAD-26OCT03NJNYI-NJ2|no: INTENTIONAL_DIVERSIFIER (phi -0.118); KXNHLGAME-26OCT03NJNYI-NJ|no: INTENTIONAL_DIVERSIFIER (phi -0.139); KXNHLSPREAD-26OCT03NJNYI-NJ3|no: INTENTIONAL_DIVERSIFIER (phi -0.096); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.07.
- thesis NYI:WINS (p 0.5294): highest fidelity KXNHLSPREAD-26OCT03NJNYI-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03NJNYI-NJ2|no (same contract)
- thesis NJD:SUPPRESSED (p 0.4595): highest fidelity KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03NJNYI-NJ2|no — Broad expression KXNHLSPREAD-26OCT03NJNYI-NJ3|no selected over player prop KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYI:SUPPRESSED (p 0.4194): highest fidelity KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no (same contract)
- KXNHLSPREAD-26OCT03NJNYI-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2413, phi -1.0)
- KXNHLGAME-26OCT03NJNYI-NJ|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.4706, phi -1.0)
- KXNHLSPREAD-26OCT03NJNYI-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2413, phi -0.728)
- KXNHLAST-26OCT03NJNYI-NYIKPALMIERI21-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.6 pts; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.3653, phi -0.189)
- override: Broad expression KXNHLSPREAD-26OCT03NJNYI-NJ3|no selected over player prop KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.01 (adj +0.43) on $14.20, P(profit) 0.674, adj growth 4.1 bp · B EV +2.27 (adj +0.50) on $19.86, P(profit) 0.5995, adj growth 4.7 bp · C EV +2.73 (adj +0.60) on $23.80, P(profit) 0.5995, adj growth 5.5 bp · R EV +0.37 (adj +0.12) on $4.00, P(profit) 0.7587, adj growth 4.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03NJNYI-NYI|yes == KXNHLGAME-26OCT03NJNYI-NJ|no

## DAL @ NSH  ·  10000 joint draws  ·  324 bet sides mapped, 6 +EV candidates, 4 on card


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
| Nashville wins YES | 45 | 0.536 | 0.491 | +0.069 | +0.023 | $3.40 | FUNDED_RESEARCH | $1 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 68 | 0.753 | 0.714 | +0.058 | +0.019 | $3.51 | FUNDED_RESEARCH | $1 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Roope Hintz: 1+ assists NO | 66 | 0.762 | 0.686 | +0.087 | +0.010 | $2.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Mikko Rantanen: 1+ assists NO | 52 | 0.636 | 0.548 | +0.099 | +0.010 | $1.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Nashville wins YES** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL2|no; why: higher confidence-adjusted growth (4.80 vs 3.59 bp); relationships: KXNHLSPREAD-26OCT03DALNSH-DAL2|no: DUPLICATIVE (phi 0.617); KXNHLAST-26OCT03DALNSH-DALRHINTZ24-1|no: REINFORCING (phi 0.162); KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-1|no: REINFORCING (phi 0.205); failure: DAL wins (incl. OT/SO)
- **Dallas wins by over 1.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03DALNSH-NSH|yes; why: second expression of the same thesis: KXNHLGAME-26OCT03DALNSH-NSH|yes has the higher standalone adjusted growth (4.80 vs 3.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.617); they share one thesis budget; relationships: KXNHLGAME-26OCT03DALNSH-NSH|yes: DUPLICATIVE (phi 0.617); KXNHLAST-26OCT03DALNSH-DALRHINTZ24-1|no: REINFORCING (phi 0.16); KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-1|no: REINFORCING (phi 0.194); failure: DAL wins by 2+
- **Roope Hintz: 1+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03DALNSH-NSH|yes; why: second expression of the same thesis: KXNHLGAME-26OCT03DALNSH-NSH|yes has the higher standalone adjusted growth (4.80 vs 1.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.162); they share one thesis budget; relationships: KXNHLGAME-26OCT03DALNSH-NSH|yes: REINFORCING (phi 0.162); KXNHLSPREAD-26OCT03DALNSH-DAL2|no: REINFORCING (phi 0.16); KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.052); failure: DAL offense succeeds (4+ goals)
- **Mikko Rantanen: 1+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03DALNSH-NSH|yes; why: second expression of the same thesis: KXNHLGAME-26OCT03DALNSH-NSH|yes has the higher standalone adjusted growth (4.80 vs 0.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.205); they share one thesis budget; relationships: KXNHLGAME-26OCT03DALNSH-NSH|yes: REINFORCING (phi 0.205); KXNHLSPREAD-26OCT03DALNSH-DAL2|no: REINFORCING (phi 0.194); KXNHLAST-26OCT03DALNSH-DALRHINTZ24-1|no: MOSTLY_INDEPENDENT (phi 0.052); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:WINS (p 0.5364): highest fidelity KXNHLGAME-26OCT03DALNSH-NSH|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes (same contract)
- thesis NSH:WINS_BY_2PLUS (p 0.3038): highest fidelity KXNHLGAME-26OCT03DALNSH-NSH|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes (same contract)
- thesis DAL:SUPPRESSED (p 0.4367): highest fidelity KXNHLSPREAD-26OCT03DALNSH-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes — override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT03DALNSH-DAL3|no less than the minimum stake; KXNHLAST-26OCT03DALNSH-DALRHINTZ24-1|no kept
- KXNHLGAME-26OCT03DALNSH-NSH|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.4636, phi -1.0)
- KXNHLSPREAD-26OCT03DALNSH-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.2473, phi -1.0)
- KXNHLAST-26OCT03DALNSH-DALRHINTZ24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.7 pts; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3374, phi -0.228)
- KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.6 pts; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3374, phi -0.271)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT03DALNSH-DAL3|no less than the minimum stake; KXNHLAST-26OCT03DALNSH-DALRHINTZ24-1|no kept
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT03DALNSH-DAL3|no less than the minimum stake; KXNHLAST-26OCT03DALNSH-DALMRANTANEN96-1|no kept

portfolios: A EV +1.92 (adj +0.39) on $14.20, P(profit) 0.6028, adj growth 3.7 bp · B EV +1.41 (adj +0.33) on $11.12, P(profit) 0.6313, adj growth 3.1 bp · C EV +1.03 (adj +0.35) on $6.95, P(profit) 0.5364, adj growth 3.2 bp · R EV +0.23 (adj +0.08) on $2.00, P(profit) 0.5364, adj growth 2.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03DALNSH-DAL|no == KXNHLGAME-26OCT03DALNSH-NSH|yes

## BOS @ MIN  ·  10000 joint draws  ·  332 bet sides mapped, 3 +EV candidates, 3 on card


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
| Elias Lindholm: 1+ goals YES | 17 | 0.227 | 0.208 | +0.048 | +0.028 | $3.77 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Olli Maatta: 1+ goals YES | 5 | 0.081 | 0.069 | +0.028 | +0.016 | $1.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 24 | 0.279 | 0.263 | +0.026 | +0.010 | $1.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03BOSMIN-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (11.60 vs 0.07 bp); despite a smaller raw edge (+0.048 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0025 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: BOS offense suppressed (<= 2 goals)
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (10.87 vs 1.24 bp); relationships: KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT03BOSMIN-7|yes; why: higher confidence-adjusted growth (1.24 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.877 vs 0.655); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis BOS:OFFENSE_4PLUS (p 0.317): highest fidelity KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.4949): highest fidelity KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes (same contract)
- KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4652, phi -0.244)
- KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2885, phi -0.112)
- KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2885, phi -0.213)

portfolios: A EV +2.42 (adj +1.37) on $8.69, P(profit) 0.4905, adj growth 12.6 bp · B EV +2.03 (adj +1.16) on $7.08, P(profit) 0.2893, adj growth 10.8 bp · C EV +1.57 (adj +0.89) on $7.30, P(profit) 0.4465, adj growth 8.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ COL  ·  10000 joint draws  ·  336 bet sides mapped, 8 +EV candidates, 1 on card


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
| Nathan MacKinnon: 1+ goals NO | 56 | 0.606 | 0.588 | +0.028 | +0.011 | $3.03 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03STLCOL-COL|no; why: Player prop expression KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no selected over player prop KXNHLPTS-26OCT03STLCOL-COLCMAKAR8-2|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.81 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability); relationships: only recommended bet in this game; failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis STL:WINS (p 0.3687): highest fidelity KXNHLGAME-26OCT03STLCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no (same contract)
- thesis STL:WINS_BY_2PLUS (p 0.1815): highest fidelity KXNHLGAME-26OCT03STLCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3081): highest fidelity KXNHLTEAMTOTAL-26OCT03STLCOL-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4997, phi -0.279)
- override: Player prop expression KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no selected over player prop KXNHLPTS-26OCT03STLCOL-COLCMAKAR8-2|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.81 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +2.80 (adj +0.81) on $14.20, P(profit) 0.5557, adj growth 7.4 bp · B EV +0.15 (adj +0.06) on $3.03, P(profit) 0.6055, adj growth 0.5 bp · C EV +1.71 (adj +0.62) on $8.73, P(profit) 0.5935, adj growth 5.7 bp · R EV +0.05 (adj +0.02) on $1.00, P(profit) 0.6055, adj growth 0.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03STLCOL-STL|yes == KXNHLGAME-26OCT03STLCOL-COL|no

## CGY @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CGY_win | p_overtime | goals | shots VAN/CGY | VAN/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.59 | 0.41 | 0.00 | 5.96 | 28.3/28.3 | 25.2/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.52 | 0.48 | 0.46 | 5.94 | 28.4/28.4 | 25.1/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.62 | 0.38 | 0.00 | 9.33 | 29.6/29.7 | 24.1/22.8 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.069 | 0.68 | 0.32 | 0.00 | 6.05 | 33.1/22.7 | 20.0/28.3 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.069 | 0.55 | 0.45 | 0.00 | 6.01 | 22.7/33.3 | 29.9/19.1 | even strength |
| VAN shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.54 | 0.46 | 0.46 | 5.86 | 33.2/22.4 | 19.3/30.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## LAK @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_LAK_win | p_overtime | goals | shots SJS/LAK | SJS/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.52 | 0.48 | 0.00 | 6.02 | 27.3/27.5 | 24.2/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.49 | 5.92 | 27.3/27.7 | 24.3/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.54 | 0.46 | 0.00 | 9.3 | 29.0/29.3 | 23.6/22.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.077 | 0.44 | 0.56 | 0.00 | 6.01 | 21.8/32.4 | 28.7/18.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.49 | 0.51 | 0.48 | 5.9 | 21.8/32.7 | 29.4/18.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.52 | 0.48 | 0.00 | 3.44 | 26.1/26.3 | 24.5/24.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
