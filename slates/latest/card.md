# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T21:41:25Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +27.46 | +8.92 | +26.09 | 0.664 | -53.15 | -77.40 | 69.81 |
| B thesis-diversified (joint) ← optimiser card | 146.92 | +29.75 | +18.13 | +23.06 | 0.639 | -55.84 | -71.84 | 157.12 |
| C best expression per thesis | 126.47 | +23.14 | +11.71 | +18.96 | 0.621 | -44.09 | -57.06 | 101.95 |
| R FUNDED research stakes | 20.00 | +3.54 | +1.94 | -0.28 | 0.492 | -10.66 | -13.28 | 0.00 |

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
| Blake Lizotte: 1+ goals YES | 9 | 0.121 | 0.112 | +0.025 | +0.016 | $4.13 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 13 | 0.159 | 0.149 | +0.021 | +0.011 | $3.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 30 | 0.337 | 0.326 | +0.022 | +0.012 | $4.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Zachary Bolduc: 1+ assists YES | 25 | 0.303 | 0.274 | +0.040 | +0.011 | $3.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_MIXED | D |
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (6.45 vs 2.41 bp); relationships: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi -0.041); failure: MTL wins (incl. OT/SO)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (2.41 vs 1.39 bp); despite a smaller raw edge (+0.021 vs +0.022/contract); relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes has the higher standalone adjusted growth (2.41 vs 1.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: PIT offense suppressed (<= 2 goals)
- **Zachary Bolduc: 1+ assists YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes; why: higher confidence-adjusted growth (1.31 vs 1.12 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.041); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4051): highest fidelity KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4375): highest fidelity KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes (same contract)
- KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:WINS (p 0.5282, phi -0.172)
- KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3817, phi -0.201)
- KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3817, phi -0.243)
- KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3469, phi -0.243)

portfolios: A EV +4.36 (adj +2.06) on $28.16, P(profit) 0.4871, adj growth 15.7 bp · B EV +2.39 (adj +1.25) on $14.93, P(profit) 0.3357, adj growth 10.8 bp · C EV +1.00 (adj +0.40) on $6.55, P(profit) 0.4133, adj growth 3.5 bp · R EV +0.52 (adj +0.34) on $2.00, P(profit) 0.1208, adj growth 9.9 bp

## TOR @ VAN  ·  10000 joint draws  ·  424 bet sides mapped, 23 +EV candidates, 4 on card

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
| Linus Karlsson: 1+ goals YES | 19 | 0.269 | 0.248 | +0.069 | +0.048 | $13.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 18 | 0.247 | 0.229 | +0.056 | +0.038 | $10.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 73 | 0.784 | 0.769 | +0.040 | +0.025 | $20.00 | FUNDED_RESEARCH | $5 | TOR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 13 | 0.165 | 0.153 | +0.027 | +0.015 | $4.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (30.17 vs 20.61 bp); relationships: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31TORVAN-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (30.17 vs 20.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT31TORVAN-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: VAN offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31TORVAN-TORWNYLANDER88-2|no; why: KXNHLAST-26OCT31TORVAN-TORWNYLANDER88-2|no has the higher standalone adjusted growth (8.86 vs 7.36 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.103); relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT31TORVAN-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: TOR offense succeeds (4+ goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT31TORVAN-TORTSTECHER28-1|yes; why: higher confidence-adjusted growth (4.39 vs 0.00 bp); despite a smaller raw edge (+0.027 vs +0.051/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4305): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLSPREAD-26OCT31TORVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3557): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.239)
- KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.223)
- KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4235, phi -0.203)
- KXNHLGOAL-26OCT31TORVAN-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3557, phi -0.188)

portfolios: A EV +8.65 (adj +1.66) on $40.61, P(profit) 0.6025, adj growth 11.9 bp · B EV +9.76 (adj +6.57) on $48.67, P(profit) 0.5218, adj growth 56.9 bp · C EV +7.20 (adj +4.07) on $36.90, P(profit) 0.4319, adj growth 35.5 bp · R EV +0.27 (adj +0.17) on $5.00, P(profit) 0.7837, adj growth 6.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT31TORVAN-TOR|no == KXNHLGAME-26OCT31TORVAN-VAN|yes

## CBJ @ DAL  ·  10000 joint draws  ·  462 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.620 / away 0.380

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
| Damon Severson: 1+ goals YES | 6 | 0.107 | 0.094 | +0.043 | +0.030 | $6.88 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 18 | 0.254 | 0.234 | +0.063 | +0.043 | $12.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.187 | 0.170 | +0.049 | +0.032 | $8.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Valeri Nichushkin: 1+ assists NO | 71 | 0.787 | 0.746 | +0.062 | +0.021 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (30.80 vs 26.37 bp); despite a smaller raw edge (+0.043 vs +0.063/contract); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT31CBJDAL-CBJVNICHUSHKIN43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.09); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (26.37 vs 18.71 bp); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT31CBJDAL-CBJVNICHUSHKIN43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.05); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (26.37 vs 18.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT31CBJDAL-CBJVNICHUSHKIN43-1|no: MOSTLY_INDEPENDENT (phi -0.031); failure: CBJ offense suppressed (<= 2 goals)
- **Valeri Nichushkin: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT31CBJDAL-CBJVNICHUSHKIN43-1|no; why: higher confidence-adjusted growth (5.09 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.05); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.031); failure: CBJ offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3151): highest fidelity KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.249): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS (p 0.468): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL2|no (same contract)
- KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.155)
- KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.241)
- KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.225)
- KXNHLAST-26OCT31CBJDAL-CBJVNICHUSHKIN43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3151, phi -0.219)

portfolios: A EV +6.75 (adj +3.45) on $40.61, P(profit) 0.4766, adj growth 30.0 bp · B EV +13.53 (adj +8.68) on $48.05, P(profit) 0.4593, adj growth 74.5 bp · C EV +9.68 (adj +5.61) on $50.00, P(profit) 0.3933, adj growth 48.7 bp · R EV +1.33 (adj +0.93) on $2.00, P(profit) 0.1066, adj growth 30.2 bp

## CGY @ COL  ·  10000 joint draws  ·  454 bet sides mapped, 21 +EV candidates, 4 on card

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
| Cale Makar: 1+ goals NO | 73 | 0.803 | 0.783 | +0.059 | +0.040 | $20.00 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Colorado wins by over 1.5 goals NO | 40 | 0.523 | 0.440 | +0.107 | +0.023 | $4.34 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 53 | 0.653 | 0.570 | +0.105 | +0.022 | $5.29 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado over 5.5 goals scored NO | 75 | 0.810 | 0.778 | +0.047 | +0.015 | $5.64 | FUNDED_RESEARCH | $2 | CGY:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31CGYCOL-COL2|no; why: higher confidence-adjusted growth (18.32 vs 4.82 bp); despite a smaller raw edge (+0.059 vs +0.107/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.022 vs 0.86); relationships: KXNHLSPREAD-26OCT31CGYCOL-COL2|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLSPREAD-26OCT31CGYCOL-COL3|no: MOSTLY_INDEPENDENT (phi 0.128); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: MOSTLY_INDEPENDENT (phi 0.147); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes; why: Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLSPREAD-26OCT31CGYCOL-COL3|no: DUPLICATIVE (phi 0.765); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: REINFORCING (phi 0.418); failure: COL wins by 2+
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes; why: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes has the higher standalone adjusted growth (7.65 vs 4.38 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.413); relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.128); KXNHLSPREAD-26OCT31CGYCOL-COL2|no: DUPLICATIVE (phi 0.765); KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: REINFORCING (phi 0.469); failure: COL wins by 2+
- **Colorado over 5.5 goals scored NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no selected over player prop KXNHLAST-26OCT31CGYCOL-COLNMACKINNON29-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.72 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLSPREAD-26OCT31CGYCOL-COL2|no: REINFORCING (phi 0.418); KXNHLSPREAD-26OCT31CGYCOL-COL3|no: REINFORCING (phi 0.469); failure: high-event game (8+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.16, COL shot control · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CGY:OFFENSE_4PLUS (p 0.2746): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes (same contract)
- thesis CGY:WINS (p 0.3041): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes — Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:TIGHT (p 0.3862): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5689, phi -0.172)
- KXNHLSPREAD-26OCT31CGYCOL-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.8 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4765, phi -1.0)
- KXNHLSPREAD-26OCT31CGYCOL-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.8 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4765, phi -0.765)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.3114, phi -0.579)
- override: Broad expression KXNHLSPREAD-26OCT31CGYCOL-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLTEAMTOTAL-26OCT31CGYCOL-COL6|no selected over player prop KXNHLAST-26OCT31CGYCOL-COLNMACKINNON29-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.72 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +7.70 (adj +1.75) on $40.61, P(profit) 0.5695, adj growth 12.2 bp · B EV +4.07 (adj +1.63) on $35.27, P(profit) 0.5483, adj growth 15.0 bp · C EV +5.26 (adj +1.63) on $33.02, P(profit) 0.5647, adj growth 14.3 bp · R EV +1.42 (adj +0.50) on $11.00, P(profit) 0.6074, adj growth 17.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
