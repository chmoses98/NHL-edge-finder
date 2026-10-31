# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T20:14:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +29.43 | +9.20 | +27.14 | 0.650 | -58.85 | -81.99 | 68.22 |
| B thesis-diversified (joint) ← optimiser card | 134.24 | +30.74 | +18.05 | +23.96 | 0.638 | -52.19 | -70.59 | 156.44 |
| C best expression per thesis | 120.92 | +22.22 | +12.24 | +18.76 | 0.621 | -46.07 | -61.92 | 106.58 |
| R FUNDED research stakes | 18.00 | +3.63 | +1.93 | +1.23 | 0.523 | -8.07 | -11.10 | 0.00 |

## PIT @ MTL  ·  10000 joint draws  ·  504 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.532 / away 0.468

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_PIT_win | p_overtime | goals | shots MTL/PIT | MTL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.55 | 0.45 | 0.00 | 6.06 | 27.2/27.5 | 24.2/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.55 | 0.45 | 0.00 | 9.4 | 28.8/29.0 | 23.0/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.53 | 0.47 | 0.45 | 5.91 | 27.1/27.4 | 24.0/23.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.084 | 0.50 | 0.50 | 0.00 | 6.1 | 21.8/32.6 | 28.8/18.3 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.50 | 0.50 | 0.47 | 5.93 | 21.6/32.3 | 29.0/18.4 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.066 | 0.47 | 0.53 | 0.00 | 9.24 | 23.1/34.3 | 27.4/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Blake Lizotte: 1+ goals YES | 9 | 0.121 | 0.111 | +0.025 | +0.015 | $3.77 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 13 | 0.159 | 0.149 | +0.021 | +0.011 | $3.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 30 | 0.337 | 0.326 | +0.022 | +0.012 | $4.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Zachary Bolduc: 1+ assists YES | 25 | 0.303 | 0.274 | +0.040 | +0.011 | $3.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_MIXED | D |
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (5.50 vs 2.41 bp); relationships: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi -0.041); failure: MTL wins (incl. OT/SO)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (2.41 vs 1.39 bp); despite a smaller raw edge (+0.021 vs +0.022/contract); relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes has the higher standalone adjusted growth (2.41 vs 1.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: PIT offense suppressed (<= 2 goals)
- **Zachary Bolduc: 1+ assists YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes; why: higher confidence-adjusted growth (1.31 vs 0.80 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.041); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4051): highest fidelity KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4375): highest fidelity KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes (same contract)
- KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:WINS (p 0.5282, phi -0.172)
- KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3817, phi -0.201)
- KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3817, phi -0.243)
- KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3469, phi -0.243)

portfolios: A EV +4.36 (adj +1.98) on $28.16, P(profit) 0.4871, adj growth 14.9 bp · B EV +2.29 (adj +1.14) on $14.56, P(profit) 0.3357, adj growth 9.9 bp · C EV +1.00 (adj +0.40) on $6.55, P(profit) 0.4133, adj growth 3.5 bp · R EV +0.26 (adj +0.16) on $1.00, P(profit) 0.1208, adj growth 5.3 bp

## TOR @ VAN  ·  10000 joint draws  ·  418 bet sides mapped, 23 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.371 / away 0.629

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_TOR_win | p_overtime | goals | shots VAN/TOR | VAN/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.50 | 0.50 | 0.00 | 6.05 | 28.3/28.4 | 24.9/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.49 | 0.51 | 0.47 | 5.96 | 28.5/28.7 | 25.3/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.109 | 0.51 | 0.49 | 0.00 | 9.38 | 29.9/30.0 | 23.7/23.6 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.073 | 0.47 | 0.53 | 0.00 | 6.06 | 22.3/33.3 | 29.2/19.0 | even strength |
| TOR shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.46 | 0.54 | 0.47 | 6.0 | 22.9/33.4 | 30.1/19.7 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.061 | 0.55 | 0.45 | 0.00 | 6.05 | 33.0/22.8 | 19.6/29.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Linus Karlsson: 1+ goals YES | 19 | 0.269 | 0.247 | +0.069 | +0.046 | $12.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 18 | 0.247 | 0.226 | +0.056 | +0.036 | $9.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 71 | 0.784 | 0.764 | +0.059 | +0.040 | $20.00 | FUNDED_RESEARCH | $5 | TOR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Toronto wins by over 1.5 goals NO | 59 | 0.716 | 0.631 | +0.110 | +0.024 | $5.77 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (28.62 vs 18.03 bp); relationships: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLSPREAD-26OCT31TORVAN-TOR2|no: MOSTLY_INDEPENDENT (phi 0.144); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (28.62 vs 18.03 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT31TORVAN-TOR2|no: MOSTLY_INDEPENDENT (phi 0.141); failure: VAN offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes; why: higher confidence-adjusted growth (17.38 vs 8.10 bp); despite a smaller raw edge (+0.059 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.015 vs 0.522); relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT31TORVAN-TOR2|no: REINFORCING (phi 0.16); failure: TOR offense succeeds (4+ goals)
- **Toronto wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes; why: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes has the higher standalone adjusted growth (8.10 vs 5.32 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.401); relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.144); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.141); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: REINFORCING (phi 0.16); failure: TOR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4305): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLSPREAD-26OCT31TORVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3557): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.239)
- KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.223)
- KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4235, phi -0.203)
- KXNHLSPREAD-26OCT31TORVAN-TOR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.1 pts; opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2836, phi -1.0)

portfolios: A EV +8.04 (adj +1.48) on $40.61, P(profit) 0.6025, adj growth 10.2 bp · B EV +10.03 (adj +6.18) on $48.61, P(profit) 0.45, adj growth 54.0 bp · C EV +7.09 (adj +4.42) on $36.36, P(profit) 0.4143, adj growth 38.8 bp · R EV +0.77 (adj +0.35) on $7.00, P(profit) 0.5911, adj growth 13.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT31TORVAN-VAN|yes == KXNHLGAME-26OCT31TORVAN-TOR|no

## CBJ @ DAL  ·  10000 joint draws  ·  460 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.625 / away 0.375

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_CBJ_win | p_overtime | goals | shots DAL/CBJ | DAL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.56 | 0.44 | 0.00 | 5.97 | 26.1/25.9 | 22.7/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.47 | 5.89 | 26.2/25.9 | 22.7/23.1 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.085 | 0.57 | 0.43 | 0.00 | 5.98 | 31.3/20.7 | 17.6/27.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.58 | 0.42 | 0.46 | 5.86 | 30.9/20.5 | 17.3/27.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.57 | 0.43 | 0.00 | 9.23 | 27.9/27.8 | 21.9/21.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.54 | 0.46 | 0.00 | 3.44 | 25.0/24.8 | 23.0/22.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Damon Severson: 1+ goals YES | 6 | 0.107 | 0.092 | +0.043 | +0.029 | $6.17 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 18 | 0.254 | 0.234 | +0.063 | +0.043 | $12.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.187 | 0.170 | +0.049 | +0.032 | $8.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ryan Lomberg: 1+ goals YES | 5 | 0.077 | 0.069 | +0.024 | +0.016 | $3.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (28.32 vs 26.37 bp); despite a smaller raw edge (+0.043 vs +0.063/contract); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (26.37 vs 18.71 bp); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (26.37 vs 18.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Ryan Lomberg: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (26.37 vs 10.41 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3151): highest fidelity KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.249): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.4138): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-DALMRANTANEN96-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.155)
- KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.241)
- KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.225)
- KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.125)

portfolios: A EV +6.75 (adj +3.45) on $40.61, P(profit) 0.4766, adj growth 30.0 bp · B EV +12.60 (adj +8.47) on $30.00, P(profit) 0.4991, adj growth 72.4 bp · C EV +8.78 (adj +5.64) on $45.88, P(profit) 0.3933, adj growth 48.7 bp · R EV +1.33 (adj +0.89) on $2.00, P(profit) 0.1066, adj growth 28.6 bp

## CGY @ COL  ·  10000 joint draws  ·  454 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.777 / away 0.223

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_CGY_win | p_overtime | goals | shots COL/CGY | COL/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.156 | 0.81 | 0.19 | 0.00 | 6.02 | 35.6/22.7 | 20.6/30.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.119 | 0.83 | 0.17 | 0.00 | 9.37 | 37.8/24.3 | 20.4/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.78 | 0.22 | 0.00 | 6.04 | 29.7/28.9 | 26.5/24.7 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.60 | 0.40 | 0.47 | 5.95 | 36.6/23.2 | 20.2/33.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.74 | 0.26 | 0.00 | 9.38 | 31.3/30.4 | 25.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.56 | 0.44 | 0.51 | 5.99 | 30.0/29.1 | 25.8/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cale Makar: 1+ goals NO | 74 | 0.803 | 0.786 | +0.050 | +0.033 | $20.00 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Calgary over 3.5 goals scored YES | 20 | 0.283 | 0.239 | +0.072 | +0.028 | $7.02 | FUNDED_RESEARCH | $2 | CGY:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 1.5 goals NO | 40 | 0.523 | 0.440 | +0.107 | +0.023 | $3.89 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mackenzie Blackwood: 22+ saves YES | 53 | 0.608 | 0.561 | +0.060 | +0.014 | $10.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:NET_HIGH_VOLUME | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT31CGYCOL-COL|no; why: higher confidence-adjusted growth (12.60 vs 6.67 bp); despite a smaller raw edge (+0.050 vs +0.083/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLSPREAD-26OCT31CGYCOL-COL2|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLSAVE-26OCT31CGYCOL-COLMBLACKWOOD39-22|yes: MOSTLY_INDEPENDENT (phi -0.027); failure: COL offense succeeds (4+ goals)
- **Calgary over 3.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes; why: higher confidence-adjusted growth (10.00 vs 7.65 bp); despite a smaller raw edge (+0.072 vs +0.077/contract); relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.025); KXNHLSPREAD-26OCT31CGYCOL-COL2|no: REINFORCING (phi 0.436); KXNHLSAVE-26OCT31CGYCOL-COLMBLACKWOOD39-22|yes: INTENTIONAL_DIVERSIFIER (phi -0.097); failure: CGY offense suppressed (<= 2 goals)
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes; why: Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: REINFORCING (phi 0.436); KXNHLSAVE-26OCT31CGYCOL-COLMBLACKWOOD39-22|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: COL wins by 2+
- **Mackenzie Blackwood: 22+ saves YES** — thesis: COL net faces heavy volume (33+ shots; CGY pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: INTENTIONAL_DIVERSIFIER (phi -0.097); KXNHLSPREAD-26OCT31CGYCOL-COL2|no: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: COL net faces light volume (<= 25 shots; CGY suppressed)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.16, COL shot control · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CGY:OFFENSE_4PLUS (p 0.2746): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes (same contract)
- thesis CGY:WINS (p 0.3041): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes — Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:TIGHT (p 0.3862): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5689, phi -0.172)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:SUPPRESSED (p 0.5111, phi -0.642)
- KXNHLSPREAD-26OCT31CGYCOL-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.8 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4765, phi -1.0)
- KXNHLSAVE-26OCT31CGYCOL-COLMBLACKWOOD39-22|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family MIXED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:NET_LOW_VOLUME (p 0.4633, phi -0.726)
- override: Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +10.28 (adj +2.29) on $40.61, P(profit) 0.5695, adj growth 13.1 bp · B EV +5.81 (adj +2.26) on $41.07, P(profit) 0.6388, adj growth 20.2 bp · C EV +5.35 (adj +1.78) on $32.13, P(profit) 0.5647, adj growth 15.5 bp · R EV +1.26 (adj +0.53) on $8.00, P(profit) 0.5227, adj growth 18.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
