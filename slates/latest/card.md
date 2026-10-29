# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-29T00:44:20Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +15.11 | +3.76 | +20.44 | 0.614 | -37.45 | -43.48 | 30.10 |
| B thesis-diversified (joint) ← optimiser card | 78.66 | +16.93 | +8.49 | +10.14 | 0.565 | -40.98 | -41.16 | 73.45 |
| C best expression per thesis | 78.90 | +11.28 | +5.16 | +13.15 | 0.588 | -27.54 | -41.18 | 45.11 |
| R FUNDED research stakes | 4.00 | +1.55 | +1.05 | -4.00 | 0.257 | -4.00 | -4.00 | 0.00 |

## NJD @ COL  ·  10000 joint draws  ·  456 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.574 / away 0.426

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_NJD_win | p_overtime | goals | shots COL/NJD | COL/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.68 | 0.32 | 0.00 | 6.05 | 28.8/28.6 | 25.8/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.57 | 0.43 | 0.46 | 5.9 | 28.5/28.6 | 25.3/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.68 | 0.32 | 0.00 | 9.32 | 30.3/30.3 | 25.3/22.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.081 | 0.72 | 0.28 | 0.00 | 6.0 | 33.8/23.1 | 20.5/28.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.56 | 0.44 | 0.49 | 5.85 | 34.0/23.0 | 19.9/30.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.063 | 0.75 | 0.25 | 0.00 | 9.22 | 35.4/24.2 | 20.0/27.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nicolas Roy: 1+ assists NO | 79 | 0.900 | 0.825 | +0.098 | +0.024 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Luke Evangelista: 1+ assists NO | 66 | 0.776 | 0.694 | +0.101 | +0.019 | $16.73 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
| Amadeus Lombardi: 1+ goals YES | 10 | 0.123 | 0.116 | +0.017 | +0.010 | $2.80 | FUNDED_RESEARCH | $1 | NJD:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ assists NO | 54 | 0.643 | 0.570 | +0.086 | +0.012 | $7.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Nicolas Roy: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT28NJCOL-COLNROY10-1|no; why: higher confidence-adjusted growth (7.72 vs 0.02 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: COL offense succeeds (4+ goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (3.45 vs 1.31 bp); relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.044); failure: NJD offense succeeds (4+ goals)
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT28NJCOL-NJDHAMILTON7-2|yes; why: higher confidence-adjusted growth (2.31 vs 0.00 bp); despite a smaller raw edge (+0.017 vs +0.024/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; wins across more scripts (relative breadth 0.922 vs 0.815); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.036); failure: NJD offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no; why: second expression of the same thesis: KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no has the higher standalone adjusted growth (3.45 vs 1.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.044); they share one thesis budget; relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.044); KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.036); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NJD:SUPPRESSED (p 0.4797): highest fidelity KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no (same contract)
- thesis NJD:NET_LOW_VOLUME (p 0.3032): highest fidelity KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no (same contract)
- thesis COL:NET_LOW_VOLUME (p 0.3591): highest fidelity KXNHLSAVE-26OCT28NJCOL-COLMBLACKWOOD39-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT28NJCOL-COLMBLACKWOOD39-27|no (same contract)
- KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.5 pts; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4821, phi -0.134)
- KXNHLAST-26OCT28NJCOL-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.6 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3008, phi -0.213)
- KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4797, phi -0.175)
- KXNHLAST-26OCT28NJCOL-NJJHUGHES86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.3 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3008, phi -0.274)

portfolios: A EV +6.61 (adj +1.21) on $50.00, P(profit) 0.7152, adj growth 10.5 bp · B EV +6.49 (adj +1.47) on $46.63, P(profit) 0.7363, adj growth 13.3 bp · C EV +3.73 (adj +0.72) on $29.87, P(profit) 0.6634, adj growth 6.3 bp · R EV +0.16 (adj +0.09) on $1.00, P(profit) 0.1235, adj growth 3.0 bp

## TOR @ SEA  ·  10000 joint draws  ·  442 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.449 / away 0.551

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_TOR_win | p_overtime | goals | shots SEA/TOR | SEA/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.56 | 0.44 | 0.00 | 6.07 | 29.4/29.3 | 26.0/25.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.60 | 0.40 | 0.00 | 9.39 | 30.9/30.7 | 25.1/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.46 | 5.98 | 29.5/29.2 | 25.8/26.0 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.082 | 0.63 | 0.37 | 0.00 | 6.02 | 34.5/23.4 | 20.5/30.0 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.55 | 0.45 | 0.47 | 5.96 | 34.8/23.7 | 20.4/31.2 | even strength |
| SEA shot control · high event (8+) · decided (2+) | 0.065 | 0.67 | 0.33 | 0.00 | 9.44 | 36.3/24.4 | 19.6/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 10 | 0.155 | 0.140 | +0.049 | +0.034 | $8.38 | FUNDED_RESEARCH | $3 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 16 | 0.219 | 0.203 | +0.050 | +0.034 | $9.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ben Meyers: 1+ goals YES | 11 | 0.160 | 0.145 | +0.043 | +0.028 | $6.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Mackie Samoskevich: 1+ goals YES | 20 | 0.248 | 0.235 | +0.037 | +0.024 | $7.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT28TORSEA-3|yes; why: higher confidence-adjusted growth (25.77 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.881 vs 0.77); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT28TORSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: TOR offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (17.22 vs 8.42 bp); despite a smaller raw edge (+0.050 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT28TORSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: SEA offense suppressed (<= 2 goals)
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (16.22 vs 8.42 bp); despite a smaller raw edge (+0.043 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT28TORSEA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)
- **Mackie Samoskevich: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: KXNHLSPREAD-26OCT28TORSEA-TOR2|no has the higher standalone adjusted growth (8.42 vs 7.40 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.128); relationships: KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3912): highest fidelity KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.393): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.476): highest fidelity KXNHLTEAMTOTAL-26OCT28TORSEA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.393, phi -0.194)
- KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3185, phi -0.199)
- KXNHLGOAL-26OCT28TORSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3185, phi -0.16)
- KXNHLGOAL-26OCT28TORSEA-SEAMSAMOSKEVICH11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3185, phi -0.2)

portfolios: A EV +8.50 (adj +2.55) on $50.00, P(profit) 0.5004, adj growth 19.6 bp · B EV +10.44 (adj +7.02) on $32.03, P(profit) 0.587, adj growth 60.1 bp · C EV +7.55 (adj +4.44) on $49.03, P(profit) 0.716, adj growth 38.8 bp · R EV +1.39 (adj +0.96) on $3.00, P(profit) 0.1554, adj growth 30.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
