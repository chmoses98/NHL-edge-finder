# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T15:23:58Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.05 | +34.21 | +10.93 | +33.28 | 0.856 | -6.25 | -16.81 | 104.09 |
| B thesis-diversified (joint) ← optimiser card | 145.65 | +32.43 | +15.55 | +30.42 | 0.817 | -11.14 | -20.05 | 149.39 |
| C best expression per thesis | 150.00 | +31.14 | +12.93 | +27.85 | 0.780 | -16.39 | -27.19 | 121.70 |
| R FUNDED research stakes | 19.00 | +2.07 | +1.19 | +0.39 | 0.518 | -4.79 | -6.19 | 0.00 |

## CHI @ BUF  ·  10000 joint draws  ·  314 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_CHI_win | p_overtime | goals | shots BUF/CHI | BUF/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.140 | 0.73 | 0.27 | 0.00 | 5.99 | 33.3/21.4 | 19.0/28.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.67 | 0.33 | 0.00 | 6.02 | 27.7/27.1 | 24.2/23.5 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.56 | 0.44 | 0.45 | 5.87 | 33.5/21.7 | 18.5/29.8 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.094 | 0.75 | 0.25 | 0.00 | 9.37 | 35.1/22.8 | 18.7/26.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.52 | 0.48 | 0.48 | 5.93 | 28.0/27.3 | 24.0/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.64 | 0.36 | 0.00 | 9.25 | 29.2/28.4 | 23.2/22.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 12 | 0.166 | 0.153 | +0.038 | +0.026 | $1.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Rasmus Dahlin: 1+ goals NO | 78 | 0.822 | 0.810 | +0.030 | +0.018 | $5.54 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 59 | 0.646 | 0.628 | +0.039 | +0.021 | $3.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 64 | 0.751 | 0.676 | +0.095 | +0.020 | $4.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03CHIBUF-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (12.82 vs 0.62 bp); despite a smaller raw edge (+0.038 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CHIBUF-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.029); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.04); failure: CHI offense suppressed (<= 2 goals)
- **Rasmus Dahlin: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (4.53 vs 4.09 bp); despite a smaller raw edge (+0.030 vs +0.039/contract); relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: BUF offense succeeds (4+ goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03CHIBUF-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (4.09 vs 1.41 bp); despite a smaller raw edge (+0.039 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.029); KXNHLGOAL-26OCT03CHIBUF-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: BUF offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03CHIBUF-CHIPKANE88-1|no; why: higher confidence-adjusted growth (3.74 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.04); KXNHLGOAL-26OCT03CHIBUF-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: CHI offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3013): highest fidelity KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes (same contract)
- thesis BUF:SUPPRESSED (p 0.2993): highest fidelity KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no (same contract)
- thesis CHI:SUPPRESSED (p 0.4903): highest fidelity KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26OCT03CHIBUF-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4903, phi -0.231)
- KXNHLGOAL-26OCT03CHIBUF-BUFRDAHLIN26-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4843, phi -0.172)
- KXNHLGOAL-26OCT03CHIBUF-BUFTTHOMPSON72-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4843, phi -0.238)
- KXNHLAST-26OCT03CHIBUF-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.6 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3013, phi -0.247)

portfolios: A EV +1.49 (adj +0.65) on $11.62, P(profit) 0.4163, adj growth 6.2 bp · B EV +1.64 (adj +0.75) on $15.36, P(profit) 0.4961, adj growth 7.2 bp · C EV +2.44 (adj +1.06) on $16.73, P(profit) 0.5717, adj growth 10.0 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.8222, adj growth 1.8 bp

## OTT @ TOR  ·  10000 joint draws  ·  344 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_OTT_win | p_overtime | goals | shots TOR/OTT | TOR/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.140 | 0.40 | 0.60 | 0.00 | 5.96 | 21.7/34.1 | 29.9/18.8 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.46 | 0.54 | 0.48 | 5.92 | 22.1/34.4 | 31.0/19.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.48 | 0.52 | 0.00 | 6.03 | 27.6/28.5 | 24.8/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.49 | 0.51 | 0.47 | 5.9 | 27.5/28.4 | 25.1/24.2 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.082 | 0.37 | 0.63 | 0.00 | 9.12 | 23.1/36.1 | 28.8/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.49 | 0.51 | 0.00 | 9.35 | 28.6/29.7 | 23.6/22.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Stephen Halliday: 1+ goals YES | 9 | 0.138 | 0.124 | +0.042 | +0.029 | $2.21 | FUNDED_RESEARCH | $1 | OTT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Hayden Hodgson: 1+ goals YES | 8 | 0.115 | 0.102 | +0.030 | +0.017 | $1.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ assists YES | 26 | 0.340 | 0.295 | +0.066 | +0.021 | $2.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
| Tim Stutzle: 1+ assists NO | 52 | 0.606 | 0.558 | +0.069 | +0.021 | $3.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (20.20 vs 2.05 bp); despite a smaller raw edge (+0.042 vs +0.084/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.046); failure: OTT offense suppressed (<= 2 goals)
- **Hayden Hodgson: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03OTTTOR-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (8.13 vs 2.05 bp); despite a smaller raw edge (+0.030 vs +0.084/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: OTT offense suppressed (<= 2 goals)
- **Easton Cowan: 1+ assists YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT03OTTTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (5.00 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT03OTTTOR-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: TOR offense suppressed (<= 2 goals)
- **Tim Stutzle: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-2|no; why: higher confidence-adjusted growth (3.75 vs 0.67 bp); alternative not eligible: confidence-adjusted EV +0.0059 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.046); KXNHLGOAL-26OCT03OTTTOR-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: OTT offense succeeds (4+ goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.14, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3485): highest fidelity KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3848): highest fidelity KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-1|no (same contract)
- thesis TOR:SUPPRESSED (p 0.4388): highest fidelity KXNHLSPREAD-26OCT03OTTTOR-TOR3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT03OTTTOR-TORKMARCHENKO86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3848, phi -0.158)
- KXNHLGOAL-26OCT03OTTTOR-OTTHHODGSON42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3848, phi -0.167)
- KXNHLAST-26OCT03OTTTOR-TORECOWAN53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4388, phi -0.286)
- KXNHLAST-26OCT03OTTTOR-OTTTSTUTZLE18-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3987, phi -0.276)

portfolios: A EV +2.12 (adj +0.37) on $11.62, P(profit) 0.5655, adj growth 3.5 bp · B EV +2.40 (adj +1.23) on $9.36, P(profit) 0.3975, adj growth 11.8 bp · C EV +2.93 (adj +0.70) on $16.38, P(profit) 0.7293, adj growth 6.6 bp · R EV +0.44 (adj +0.30) on $1.00, P(profit) 0.1376, adj growth 11.0 bp

## WSH @ TBL  ·  10000 joint draws  ·  352 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WSH_win | p_overtime | goals | shots TBL/WSH | TBL/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.67 | 0.33 | 0.00 | 6.01 | 27.1/26.6 | 23.7/22.9 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.112 | 0.71 | 0.29 | 0.00 | 6.0 | 32.4/20.9 | 18.5/27.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.52 | 0.48 | 0.46 | 6.01 | 27.2/26.9 | 23.6/23.9 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.55 | 0.45 | 0.48 | 5.9 | 32.5/21.4 | 18.3/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.64 | 0.36 | 0.00 | 9.38 | 28.7/28.3 | 22.9/21.7 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.075 | 0.74 | 0.26 | 0.00 | 9.18 | 34.2/22.5 | 18.3/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| John Carlson: 1+ assists NO | 48 | 0.746 | 0.567 | +0.249 | +0.069 | $6.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.211 | 0.200 | +0.031 | +0.020 | $1.72 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Boone Jenner: 1+ goals YES | 11 | 0.144 | 0.133 | +0.027 | +0.016 | $1.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jeffrey Viel: 1+ goals YES | 10 | 0.129 | 0.118 | +0.023 | +0.012 | $1.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03WSHTB-TBJCARLSON74-1|no; why: higher confidence-adjusted growth (41.91 vs 8.53 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT03WSHTB-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT03WSHTB-TBJVIEL25-1|yes: MOSTLY_INDEPENDENT (phi -0.036); failure: TBL offense succeeds (4+ goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03WSHTB-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (5.74 vs 0.00 bp); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT03WSHTB-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03WSHTB-TBJVIEL25-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: WSH offense suppressed (<= 2 goals)
- **Boone Jenner: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (5.74 vs 5.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT03WSHTB-TBJVIEL25-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: WSH offense suppressed (<= 2 goals)
- **Jeffrey Viel: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03WSHTB-TBCDASTOUS51-1|yes; why: higher confidence-adjusted growth (3.16 vs 1.55 bp); despite a smaller raw edge (+0.023 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT03WSHTB-WSHBJENNER38-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: TBL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:SUPPRESSED (p 0.3217): highest fidelity KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no (same contract)
- thesis WSH:OFFENSE_4PLUS (p 0.3068): highest fidelity KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes (same contract)
- thesis TBL:OFFENSE_4PLUS (p 0.4659): highest fidelity KXNHLAST-26OCT03WSHTB-TBCDASTOUS51-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT03WSHTB-TBCDASTOUS51-1|yes (same contract)
- KXNHLAST-26OCT03WSHTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 27.6 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4659, phi -0.21)
- KXNHLGOAL-26OCT03WSHTB-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4782, phi -0.238)
- KXNHLGOAL-26OCT03WSHTB-WSHBJENNER38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4782, phi -0.185)
- KXNHLGOAL-26OCT03WSHTB-TBJVIEL25-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3217, phi -0.138)

portfolios: A EV +3.86 (adj +0.81) on $11.62, P(profit) 0.7611, adj growth 7.9 bp · B EV +3.89 (adj +1.33) on $10.16, P(profit) 0.7902, adj growth 13.0 bp · C EV +5.27 (adj +1.61) on $13.34, P(profit) 0.7965, adj growth 15.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ PHI  ·  10000 joint draws  ·  368 bet sides mapped, 15 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CAR_win | p_overtime | goals | shots PHI/CAR | PHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.133 | 0.53 | 0.47 | 0.00 | 6.0 | 20.6/32.3 | 28.8/17.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.53 | 0.47 | 0.46 | 5.86 | 20.5/32.0 | 28.6/17.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.59 | 0.41 | 0.00 | 5.96 | 25.7/26.5 | 23.4/21.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.53 | 0.47 | 0.46 | 5.91 | 25.8/26.5 | 23.0/22.5 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.075 | 0.52 | 0.48 | 0.48 | 2.75 | 19.0/30.2 | 28.8/17.6 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.070 | 0.51 | 0.49 | 0.00 | 3.44 | 19.6/30.9 | 29.0/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sean Couturier: 1+ goals YES | 10 | 0.184 | 0.161 | +0.078 | +0.054 | $3.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Noel Acciari: 1+ goals YES | 8 | 0.136 | 0.120 | +0.050 | +0.035 | $2.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Mark Jankowski: 1+ goals NO | 84 | 0.886 | 0.873 | +0.036 | +0.024 | $6.14 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03CARPHI-CAR3|no; why: higher confidence-adjusted growth (64.83 vs 6.03 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: PHI offense suppressed (<= 2 goals)
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (64.83 vs 33.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: MOSTLY_INDEPENDENT (phi 0.03); failure: PHI offense suppressed (<= 2 goals)
- **Mark Jankowski: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT03CARPHI-CAR3|no; why: higher confidence-adjusted growth (9.75 vs 6.03 bp); despite a smaller raw edge (+0.036 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.03); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3787): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS_BY_2PLUS (p 0.3144): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.4675): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03CARPHI-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03CARPHI-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4033, phi -0.233)
- KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4033, phi -0.176)
- KXNHLGOAL-26OCT03CARPHI-CARMJANKOWSKI77-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3152, phi -0.169)

portfolios: A EV +3.18 (adj +1.75) on $11.62, P(profit) 0.5618, adj growth 16.7 bp · B EV +4.58 (adj +3.18) on $12.50, P(profit) 0.2943, adj growth 30.3 bp · C EV +5.02 (adj +3.24) on $21.44, P(profit) 0.1843, adj growth 30.0 bp · R EV +0.09 (adj +0.06) on $2.00, P(profit) 0.8858, adj growth 2.2 bp
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
| Filip Hallander: 1+ goals YES | 13 | 0.218 | 0.194 | +0.080 | +0.056 | $4.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 13 | 0.210 | 0.187 | +0.072 | +0.049 | $3.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Trevor van Riemsdyk: 1+ goals YES | 4 | 0.072 | 0.061 | +0.029 | +0.019 | $1.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ goals YES | 32 | 0.362 | 0.348 | +0.027 | +0.012 | $1.32 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
- **Filip Hallander: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (54.98 vs 43.18 bp); relationships: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT03MTLPIT-PITTVANRIEMSDYK57-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes; why: higher confidence-adjusted growth (43.18 vs 8.50 bp); despite a smaller raw edge (+0.072 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.834 vs 0.498); relationships: KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT03MTLPIT-PITTVANRIEMSDYK57-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: PIT offense suppressed (<= 2 goals)
- **Trevor van Riemsdyk: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (43.18 vs 17.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (43.18 vs 1.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT03MTLPIT-PITTVANRIEMSDYK57-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts PIT shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, PIT shot control · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4718): highest fidelity KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS_BY_2PLUS (p 0.3477): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.568): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-MTL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03MTLPIT-PITFHALLANDER11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.183)
- KXNHLGOAL-26OCT03MTLPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.222)
- KXNHLGOAL-26OCT03MTLPIT-PITTVANRIEMSDYK57-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.096)
- KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.27)

portfolios: A EV +4.47 (adj +2.59) on $11.62, P(profit) 0.5393, adj growth 24.6 bp · B EV +5.45 (adj +3.70) on $10.71, P(profit) 0.4299, adj growth 35.3 bp · C EV +2.97 (adj +2.04) on $5.71, P(profit) 0.2096, adj growth 19.0 bp · R EV +0.08 (adj +0.04) on $1.00, P(profit) 0.3619, adj growth 1.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03MTLPIT-PIT|yes == KXNHLGAME-26OCT03MTLPIT-MTL|no

## UTA @ CBJ  ·  10000 joint draws  ·  342 bet sides mapped, 6 +EV candidates, 4 on card


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
| Vincent Trocheck: 1+ assists NO | 67 | 0.862 | 0.727 | +0.176 | +0.042 | $5.97 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Charlie Coyle: 1+ goals YES | 21 | 0.271 | 0.253 | +0.049 | +0.031 | $2.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Danton Heinen: 1+ goals YES | 10 | 0.132 | 0.121 | +0.025 | +0.015 | $1.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Conor Garland: 1+ goals NO | 83 | 0.863 | 0.851 | +0.024 | +0.011 | $5.47 | FUNDED_RESEARCH | $2 | CBJ:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT03UTACBJ-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (18.00 vs 1.14 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: UTA offense succeeds (4+ goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03UTACBJ-CBJ|yes; why: higher confidence-adjusted growth (12.31 vs 0.75 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: CBJ offense suppressed (<= 2 goals)
- **Danton Heinen: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (12.31 vs 5.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: CBJ offense suppressed (<= 2 goals)
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03UTACBJ-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (2.14 vs 0.60 bp); despite a smaller raw edge (+0.024 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0077 below the 0.010/contract floor; relationships: KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.4162): highest fidelity KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.419): highest fidelity KXNHLPTS-26OCT03UTACBJ-UTAVTROCHECK16-1|no [DIRECT], best adjusted EV KXNHLPTS-26OCT03UTACBJ-UTAVTROCHECK16-1|no (same contract)
- thesis CBJ:SUPPRESSED (p 0.3649): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT03UTACBJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.7 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3582, phi -0.189)
- KXNHLGOAL-26OCT03UTACBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.235)
- KXNHLGOAL-26OCT03UTACBJ-CBJDHEINEN58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3649, phi -0.15)
- KXNHLGOAL-26OCT03UTACBJ-CBJCGARLAND83-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.4162, phi -0.154)

portfolios: A EV +2.18 (adj +0.64) on $11.62, P(profit) 0.7642, adj growth 6.2 bp · B EV +2.58 (adj +0.99) on $15.36, P(profit) 0.363, adj growth 9.6 bp · C EV +2.06 (adj +0.80) on $16.23, P(profit) 0.2706, adj growth 7.6 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.8634, adj growth 1.0 bp

## SEA @ EDM  ·  10000 joint draws  ·  356 bet sides mapped, 12 +EV candidates, 4 on card


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
| Alex Formenton: 1+ goals YES | 18 | 0.244 | 0.223 | +0.054 | +0.033 | $3.14 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 68 | 0.817 | 0.725 | +0.121 | +0.029 | $6.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Connor McDavid: 1+ assists NO | 33 | 0.462 | 0.370 | +0.116 | +0.024 | $2.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ assists YES | 36 | 0.450 | 0.400 | +0.073 | +0.024 | $3.22 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.58) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (15.19 vs 5.19 bp); despite a smaller raw edge (+0.054 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.097); KXNHLAST-26OCT03SEAEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.029); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (8.96 vs 5.59 bp); relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: DUPLICATIVE (phi 0.439); KXNHLAST-26OCT03SEAEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.1); failure: EDM offense succeeds (4+ goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no; why: second expression of the same thesis: KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no has the higher standalone adjusted growth (8.96 vs 5.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.439); they share one thesis budget; relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.097); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: DUPLICATIVE (phi 0.439); KXNHLAST-26OCT03SEAEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.123); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (15.19 vs 5.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.029); they share one thesis budget; relationships: KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.029); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.1); KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.123); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.5105): highest fidelity KXNHLPTS-26OCT03SEAEDM-EDMMEKHOLM14-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2853): highest fidelity KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no (same contract)
- thesis SEA:SUPPRESSED (p 0.4474): highest fidelity KXNHLAST-26OCT03SEAEDM-SEAJMCCANN19-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03SEAEDM-SEAJMCCANN19-1|no (same contract)
- KXNHLGOAL-26OCT03SEAEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2853, phi -0.224)
- KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.2 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5105, phi -0.305)
- KXNHLAST-26OCT03SEAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.2 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5105, phi -0.308)
- KXNHLAST-26OCT03SEAEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 42% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2853, phi -0.279)

portfolios: A EV +3.38 (adj +0.52) on $11.62, P(profit) 0.6826, adj growth 5.0 bp · B EV +3.36 (adj +1.16) on $14.77, P(profit) 0.742, adj growth 11.2 bp · C EV +3.62 (adj +1.42) on $21.66, P(profit) 0.7546, adj growth 13.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ NYI  ·  10000 joint draws  ·  338 bet sides mapped, 13 +EV candidates, 4 on card


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
| New Jersey wins NO | 44 | 0.529 | 0.482 | +0.072 | +0.025 | $1.42 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins by over 2.5 goals NO | 79 | 0.856 | 0.821 | +0.054 | +0.019 | $3.30 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey over 4.5 goals scored NO | 78 | 0.844 | 0.809 | +0.052 | +0.017 | $2.52 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Timo Meier: 1+ goals NO | 74 | 0.781 | 0.767 | +0.028 | +0.014 | $1.97 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **New Jersey wins NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03NJNYI-NYI|yes; why: best adjusted growth among the thesis's expressions; relationships: KXNHLSPREAD-26OCT03NJNYI-NJ3|no: DUPLICATIVE (phi 0.435); KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5|no: DUPLICATIVE (phi 0.383); KXNHLGOAL-26OCT03NJNYI-NJTMEIER28-1|no: REINFORCING (phi 0.162); failure: NJD wins (incl. OT/SO)
- **New Jersey wins by over 2.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03NJNYI-NJ|no; why: second expression of the same thesis: KXNHLGAME-26OCT03NJNYI-NJ|no has the higher standalone adjusted growth (5.48 vs 4.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.435); they share one thesis budget; relationships: KXNHLGAME-26OCT03NJNYI-NJ|no: DUPLICATIVE (phi 0.435); KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5|no: REINFORCING (phi 0.488); KXNHLGOAL-26OCT03NJNYI-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.147); failure: NJD wins by 2+
- **New Jersey over 4.5 goals scored NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03NJNYI-NJ|no; why: Broad expression KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5|no selected over player prop KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGAME-26OCT03NJNYI-NJ|no: DUPLICATIVE (phi 0.383); KXNHLSPREAD-26OCT03NJNYI-NJ3|no: REINFORCING (phi 0.488); KXNHLGOAL-26OCT03NJNYI-NJTMEIER28-1|no: REINFORCING (phi 0.178); failure: NJD offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT03NJNYI-NJ|no; why: second expression of the same thesis: KXNHLGAME-26OCT03NJNYI-NJ|no has the higher standalone adjusted growth (5.48 vs 2.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.162); they share one thesis budget; relationships: KXNHLGAME-26OCT03NJNYI-NJ|no: REINFORCING (phi 0.162); KXNHLSPREAD-26OCT03NJNYI-NJ3|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5|no: REINFORCING (phi 0.178); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.07.
- thesis NJD:SUPPRESSED (p 0.4595): highest fidelity KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no — Broad expression KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5|no selected over player prop KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYI:WINS (p 0.5294): highest fidelity KXNHLGAME-26OCT03NJNYI-NJ|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no (same contract)
- thesis NYI:WINS_BY_2PLUS (p 0.2963): highest fidelity KXNHLGAME-26OCT03NJNYI-NJ|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03NJNYI-NJ|no (same contract)
- KXNHLGAME-26OCT03NJNYI-NJ|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.4706, phi -1.0)
- KXNHLSPREAD-26OCT03NJNYI-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2413, phi -0.728)
- KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3139, phi -0.636)
- KXNHLGOAL-26OCT03NJNYI-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3139, phi -0.225)
- override: Broad expression KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5|no selected over player prop KXNHLAST-26OCT03NJNYI-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.28 (adj +0.30) on $11.62, P(profit) 0.7296, adj growth 2.9 bp · B EV +0.68 (adj +0.25) on $9.22, P(profit) 0.7292, adj growth 2.4 bp · C EV +0.81 (adj +0.28) on $5.16, P(profit) 0.5294, adj growth 2.7 bp · R EV +0.33 (adj +0.12) on $4.00, P(profit) 0.5238, adj growth 4.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03NJNYI-NYI|yes == KXNHLGAME-26OCT03NJNYI-NJ|no

## DAL @ NSH  ·  10000 joint draws  ·  324 bet sides mapped, 7 +EV candidates, 2 on card


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
| Nashville wins YES | 45 | 0.536 | 0.491 | +0.069 | +0.023 | $2.22 | FUNDED_RESEARCH | $1 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 79 | 0.848 | 0.817 | +0.047 | +0.015 | $3.61 | FUNDED_RESEARCH | $1 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Nashville wins YES** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL2|no; why: higher confidence-adjusted growth (4.80 vs 3.59 bp); relationships: KXNHLSPREAD-26OCT03DALNSH-DAL3|no: DUPLICATIVE (phi 0.455); failure: DAL wins (incl. OT/SO)
- **Dallas wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03DALNSH-NSH|yes; why: second expression of the same thesis: KXNHLGAME-26OCT03DALNSH-NSH|yes has the higher standalone adjusted growth (4.80 vs 3.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.455); they share one thesis budget; relationships: KXNHLGAME-26OCT03DALNSH-NSH|yes: DUPLICATIVE (phi 0.455); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:WINS (p 0.5364): highest fidelity KXNHLGAME-26OCT03DALNSH-NSH|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.3886): highest fidelity KXNHLSPREAD-26OCT03DALNSH-DAL3|no [DIRECT], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS_BY_2PLUS (p 0.3038): highest fidelity KXNHLGAME-26OCT03DALNSH-NSH|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes (same contract)
- KXNHLGAME-26OCT03DALNSH-NSH|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.4636, phi -1.0)
- KXNHLSPREAD-26OCT03DALNSH-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.2473, phi -0.737)

portfolios: A EV +1.37 (adj +0.33) on $11.62, P(profit) 0.6652, adj growth 3.1 bp · B EV +0.54 (adj +0.18) on $5.83, P(profit) 0.5364, adj growth 1.7 bp · C EV +0.73 (adj +0.25) on $4.94, P(profit) 0.5364, adj growth 2.3 bp · R EV +0.21 (adj +0.07) on $2.00, P(profit) 0.5364, adj growth 2.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03DALNSH-DAL|no == KXNHLGAME-26OCT03DALNSH-NSH|yes

## BOS @ MIN  ·  10000 joint draws  ·  332 bet sides mapped, 4 +EV candidates, 4 on card


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
| Olli Maatta: 1+ goals YES | 5 | 0.081 | 0.073 | +0.028 | +0.020 | $1.41 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 11 | 0.152 | 0.137 | +0.035 | +0.020 | $1.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Elias Lindholm: 1+ assists YES | 25 | 0.321 | 0.280 | +0.058 | +0.017 | $1.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
| Ryan Hartman: 1+ goals YES | 24 | 0.279 | 0.266 | +0.026 | +0.013 | $1.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (16.40 vs 1.91 bp); relationships: KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT03BOSMIN-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: MIN offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (8.17 vs 1.91 bp); relationships: KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT03BOSMIN-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: MIN offense suppressed (<= 2 goals)
- **Elias Lindholm: 1+ assists YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03BOSMIN-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (3.33 vs 0.25 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: BOS offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT03BOSMIN-7|yes; why: higher confidence-adjusted growth (1.91 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.877 vs 0.655); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT03BOSMIN-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis BOS:OFFENSE_4PLUS (p 0.317): highest fidelity KXNHLAST-26OCT03BOSMIN-BOSELINDHOLM28-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT03BOSMIN-BOSELINDHOLM28-1|yes (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.4949): highest fidelity KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes (same contract)
- KXNHLGOAL-26OCT03BOSMIN-MINOMAATTA3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2885, phi -0.112)
- KXNHLGOAL-26OCT03BOSMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2885, phi -0.148)
- KXNHLAST-26OCT03BOSMIN-BOSELINDHOLM28-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4652, phi -0.277)
- KXNHLGOAL-26OCT03BOSMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.2885, phi -0.213)

portfolios: A EV +2.79 (adj +1.43) on $10.61, P(profit) 0.4717, adj growth 13.2 bp · B EV +1.69 (adj +0.96) on $5.87, P(profit) 0.4717, adj growth 9.1 bp · C EV +0.72 (adj +0.25) on $4.29, P(profit) 0.5096, adj growth 2.4 bp · R EV +0.52 (adj +0.37) on $1.00, P(profit) 0.0809, adj growth 12.9 bp

## STL @ COL  ·  10000 joint draws  ·  336 bet sides mapped, 18 +EV candidates, 3 on card


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
| Pius Suter: 1+ goals YES | 11 | 0.145 | 0.134 | +0.028 | +0.017 | $1.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Colorado wins by over 2.5 goals NO | 64 | 0.717 | 0.676 | +0.061 | +0.020 | $2.70 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nathan MacKinnon: 1+ goals NO | 55 | 0.606 | 0.587 | +0.038 | +0.019 | $2.94 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03STLCOL-COL2|no; why: KXNHLSPREAD-26OCT03STLCOL-COL2|no has the higher standalone adjusted growth (6.27 vs 6.12 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.127); relationships: KXNHLSPREAD-26OCT03STLCOL-COL3|no: MOSTLY_INDEPENDENT (phi 0.102); KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: STL offense suppressed (<= 2 goals)
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT03STLCOL-COL2|no; why: Broad expression KXNHLSPREAD-26OCT03STLCOL-COL3|no selected over player prop KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.102); KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: REINFORCING (phi 0.198); failure: COL wins by 2+
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no; why: KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no has the higher standalone adjusted growth (7.16 vs 3.32 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.008); relationships: KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLSPREAD-26OCT03STLCOL-COL3|no: REINFORCING (phi 0.198); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis COL:SUPPRESSED (p 0.2896): highest fidelity KXNHLSPREAD-26OCT03STLCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no — Broad expression KXNHLSPREAD-26OCT03STLCOL-COL3|no selected over player prop KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis STL:WINS (p 0.3687): highest fidelity KXNHLSPREAD-26OCT03STLCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.412): highest fidelity KXNHLSPREAD-26OCT03STLCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03STLCOL-COL2|no (same contract)
- KXNHLGOAL-26OCT03STLCOL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4763, phi -0.194)
- KXNHLSPREAD-26OCT03STLCOL-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4065, phi -0.759)
- KXNHLGOAL-26OCT03STLCOL-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4997, phi -0.279)
- override: Broad expression KXNHLSPREAD-26OCT03STLCOL-COL3|no selected over player prop KXNHLAST-26OCT03STLCOL-COLNMACKINNON29-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.65 (adj +0.44) on $11.62, P(profit) 0.5288, adj growth 4.0 bp · B EV +0.74 (adj +0.36) on $6.84, P(profit) 0.5432, adj growth 3.4 bp · C EV +1.98 (adj +0.55) on $9.04, P(profit) 0.7393, adj growth 5.2 bp · R EV +0.16 (adj +0.06) on $2.00, P(profit) 0.4779, adj growth 2.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03STLCOL-STL|yes == KXNHLGAME-26OCT03STLCOL-COL|no

## CGY @ VAN  ·  10000 joint draws  ·  310 bet sides mapped, 4 +EV candidates, 4 on card


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
| Zeev Buium: 1+ goals NO | 86 | 0.923 | 0.906 | +0.054 | +0.037 | $4.61 | FUNDED_RESEARCH | $2 | VAN:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Zayne Parekh: 1+ goals NO | 85 | 0.903 | 0.886 | +0.044 | +0.027 | $4.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Drew O'Connor: 1+ goals YES | 17 | 0.220 | 0.199 | +0.040 | +0.019 | $1.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Paul Cotter: 1+ goals NO | 84 | 0.874 | 0.864 | +0.024 | +0.015 | $4.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
- **Zeev Buium: 1+ goals NO** — thesis: VAN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANBBOESER6-1|no; why: higher confidence-adjusted growth (27.39 vs 0.00 bp); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: VAN offense succeeds (4+ goals)
- **Zayne Parekh: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT03CGYVAN-VAN2|yes; why: higher confidence-adjusted growth (13.49 vs 0.10 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.0 vs 0.519); alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CGY offense succeeds (4+ goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (5.19 vs 0.12 bp); alternative not eligible: confidence-adjusted EV +0.0031 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense suppressed (<= 2 goals)
- **Paul Cotter: 1+ goals NO** — thesis: VAN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT03CGYVAN-VANBBOESER6-1|no; why: higher confidence-adjusted growth (3.65 vs 0.00 bp); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.4402): highest fidelity KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes (same contract)
- thesis VAN:SUPPRESSED (p 0.3458): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis CGY:SUPPRESSED (p 0.4302): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03CGYVAN-VANZBUIUM8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:OFFENSE_4PLUS (p 0.4402, phi -0.114)
- KXNHLGOAL-26OCT03CGYVAN-CGYZPAREKH19-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:OFFENSE_4PLUS (p 0.35, phi -0.122)
- KXNHLGOAL-26OCT03CGYVAN-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3458, phi -0.217)
- KXNHLGOAL-26OCT03CGYVAN-VANPCOTTER47-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:OFFENSE_4PLUS (p 0.4402, phi -0.152)

portfolios: A EV +0.89 (adj +0.50) on $11.62, P(profit) 0.2195, adj growth 4.9 bp · B EV +0.92 (adj +0.55) on $15.10, P(profit) 0.7815, adj growth 5.4 bp · C EV +0.53 (adj +0.25) on $2.38, P(profit) 0.2199, adj growth 2.3 bp · R EV +0.12 (adj +0.09) on $2.00, P(profit) 0.9226, adj growth 3.4 bp

## LAK @ SJS  ·  10000 joint draws  ·  312 bet sides mapped, 7 +EV candidates, 3 on card


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
| Mats Zuccarello: 1+ assists NO | 58 | 0.826 | 0.653 | +0.229 | +0.056 | $5.58 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Mason Marchment: 1+ assists NO | 67 | 0.812 | 0.713 | +0.127 | +0.028 | $5.58 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Artemi Panarin: 1+ assists NO | 50 | 0.640 | 0.543 | +0.123 | +0.025 | $3.42 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (28.62 vs 5.55 bp); relationships: KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.061); failure: LAK offense succeeds (4+ goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no; why: higher confidence-adjusted growth (7.86 vs 1.61 bp); relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: SJS offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT03LASJ-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (5.55 vs 5.20 bp); relationships: KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.061); KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis LAK:SUPPRESSED (p 0.4231): highest fidelity KXNHLAST-26OCT03LASJ-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:OFFENSE_4PLUS (p 0.3833): highest fidelity KXNHLGOAL-26OCT03LASJ-SJCGRAF51-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT03LASJ-SJCGRAF51-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3966): highest fidelity KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT03LASJ-SJLCAGNONI42-1|no (same contract)
- KXNHLAST-26OCT03LASJ-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 26.6 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3574, phi -0.21)
- KXNHLAST-26OCT03LASJ-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.2 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3833, phi -0.202)
- KXNHLAST-26OCT03LASJ-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.0 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3574, phi -0.279)

portfolios: A EV +2.55 (adj +0.60) on $11.62, P(profit) 0.8447, adj growth 5.9 bp · B EV +3.98 (adj +0.91) on $14.57, P(profit) 0.8502, adj growth 9.0 bp · C EV +2.06 (adj +0.48) on $12.70, P(profit) 0.5539, adj growth 4.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
