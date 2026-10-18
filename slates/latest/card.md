# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-18T00:03:12Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +25.90 | +6.79 | +25.75 | 0.705 | -34.66 | -52.64 | 56.61 |
| B thesis-diversified (joint) ← optimiser card | 137.16 | +18.91 | +7.22 | +17.54 | 0.649 | -32.83 | -42.87 | 63.81 |
| C best expression per thesis | 135.42 | +17.37 | +5.78 | +16.53 | 0.676 | -29.53 | -43.07 | 51.33 |
| R FUNDED research stakes | 9.00 | +0.69 | +0.40 | -1.81 | 0.439 | -9.00 | -9.00 | 0.00 |

## BOS @ LAK  ·  10000 joint draws  ·  416 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.551 / away 0.449

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BOS_win | p_overtime | goals | shots LAK/BOS | LAK/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.55 | 0.45 | 0.00 | 5.96 | 28.1/27.5 | 24.1/24.4 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.111 | 0.63 | 0.37 | 0.00 | 5.93 | 33.3/21.8 | 19.0/29.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.47 | 5.92 | 28.1/27.7 | 24.5/24.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.53 | 0.47 | 0.42 | 5.84 | 33.5/22.0 | 18.7/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.55 | 0.45 | 0.00 | 9.18 | 29.3/29.0 | 23.3/22.9 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.062 | 0.64 | 0.36 | 0.00 | 9.19 | 34.9/23.4 | 18.5/27.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Artemi Panarin: 2+ assists NO | 84 | 0.908 | 0.866 | +0.058 | +0.017 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Charlie McAvoy: 1+ assists NO | 59 | 0.675 | 0.630 | +0.068 | +0.023 | $17.63 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Hampus Lindholm: 1+ assists YES | 25 | 0.321 | 0.278 | +0.058 | +0.015 | $4.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
| Elias Lindholm: 1+ goals YES | 20 | 0.233 | 0.222 | +0.022 | +0.011 | $4.23 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Artemi Panarin: 2+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no; why: higher confidence-adjusted growth (4.99 vs 2.32 bp); despite a smaller raw edge (+0.058 vs +0.098/contract); relationships: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: LAK offense succeeds (4+ goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (4.81 vs 0.51 bp); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.063); KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.173); failure: BOS offense succeeds (4+ goals)
- **Hampus Lindholm: 1+ assists YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (2.47 vs 1.64 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.063); KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.082); failure: BOS offense suppressed (<= 2 goals)
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes has the higher standalone adjusted growth (2.47 vs 1.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.082); they share one thesis budget; relationships: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.173); KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes: MOSTLY_INDEPENDENT (phi 0.082); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis LAK:SUPPRESSED (p 0.3978): highest fidelity KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no (same contract)
- thesis BOS:SUPPRESSED (p 0.4519): highest fidelity KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.3292): highest fidelity KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes (same contract)
- KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3926, phi -0.25)
- KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3292, phi -0.254)
- KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4519, phi -0.271)
- KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4519, phi -0.24)

portfolios: A EV +7.38 (adj +1.82) on $50.00, P(profit) 0.5959, adj growth 14.5 bp · B EV +4.80 (adj +1.55) on $46.50, P(profit) 0.6758, adj growth 13.8 bp · C EV +4.83 (adj +1.40) on $44.22, P(profit) 0.6666, adj growth 12.6 bp · R EV +0.21 (adj +0.11) on $2.00, P(profit) 0.2332, adj growth 3.0 bp

## EDM @ UTA  ·  10000 joint draws  ·  436 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.558 / away 0.442

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_EDM_win | p_overtime | goals | shots UTA/EDM | UTA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.53 | 0.47 | 0.00 | 6.05 | 27.4/27.3 | 23.9/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.118 | 0.54 | 0.46 | 0.00 | 9.51 | 29.2/29.1 | 23.2/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.47 | 6.04 | 27.8/27.7 | 24.3/24.3 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.075 | 0.59 | 0.41 | 0.00 | 6.09 | 32.6/21.8 | 18.7/28.0 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.064 | 0.62 | 0.38 | 0.00 | 9.52 | 34.0/23.2 | 18.0/26.3 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.53 | 0.47 | 0.49 | 6.05 | 32.7/22.0 | 18.7/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nate Schmidt: 1+ goals YES | 4 | 0.067 | 0.058 | +0.024 | +0.015 | $3.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ assists YES | 27 | 0.363 | 0.314 | +0.079 | +0.030 | $9.71 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_MIXED | D |
| Connor McDavid: 2+ assists NO | 71 | 0.798 | 0.751 | +0.073 | +0.027 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Zach Hyman: 1+ goals YES | 31 | 0.358 | 0.345 | +0.033 | +0.020 | $7.72 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Nate Schmidt: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (11.23 vs 1.95 bp); relationships: KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: UTA offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes; why: higher confidence-adjusted growth (9.71 vs 3.89 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.108); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi 0.11); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (8.04 vs 3.33 bp); despite a smaller raw edge (+0.073 vs +0.091/contract); relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.108); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.218); failure: EDM offense succeeds (4+ goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes; why: Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes because adjusted EV is 0.4 pts higher while thesis capture is 0.51 vs 0.17 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.11); KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.218); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4295): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes — Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes because adjusted EV is 0.4 pts higher while thesis capture is 0.51 vs 0.17 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis EDM:SUPPRESSED (p 0.3535): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.4702): highest fidelity KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes (same contract)
- KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3208, phi -0.107)
- KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3535, phi -0.269)
- KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4295, phi -0.328)
- KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3535, phi -0.271)
- override: Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes because adjusted EV is 0.4 pts higher while thesis capture is 0.51 vs 0.17 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +11.93 (adj +2.98) on $50.00, P(profit) 0.6946, adj growth 24.1 bp · B EV +7.33 (adj +3.36) on $40.66, P(profit) 0.5006, adj growth 29.6 bp · C EV +5.71 (adj +2.26) on $43.74, P(profit) 0.4737, adj growth 20.2 bp · R EV +0.20 (adj +0.12) on $2.00, P(profit) 0.358, adj growth 4.2 bp

## PIT @ VGK  ·  10000 joint draws  ·  424 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.645 / away 0.355

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_PIT_win | p_overtime | goals | shots VGK/PIT | VGK/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.69 | 0.31 | 0.00 | 6.04 | 27.7/27.5 | 24.8/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.71 | 0.29 | 0.00 | 9.35 | 29.1/28.8 | 23.9/21.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.55 | 0.45 | 0.46 | 6.0 | 27.6/27.4 | 24.1/24.2 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.094 | 0.74 | 0.26 | 0.00 | 6.02 | 32.4/21.6 | 19.2/27.6 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.56 | 0.44 | 0.48 | 5.93 | 32.3/21.7 | 18.6/28.7 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.067 | 0.77 | 0.23 | 0.00 | 9.33 | 34.2/23.0 | 18.8/25.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adin Hill: 22+ saves YES | 47 | 0.617 | 0.515 | +0.130 | +0.028 | $12.43 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:NET_HIGH_VOLUME | DIRECT (0.95) | EVIDENCE_MIXED | D |
| Mitch Marner: 1+ goals NO | 68 | 0.734 | 0.720 | +0.039 | +0.024 | $19.23 | FUNDED_RESEARCH | $5 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Evgeni Malkin: 1+ assists NO | 63 | 0.716 | 0.670 | +0.069 | +0.024 | $16.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.084 | 0.074 | +0.020 | +0.010 | $2.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:WINS_BY_2PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
- **Adin Hill: 22+ saves YES** — thesis: VGK net faces heavy volume (33+ shots; PIT pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.04); KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.03); failure: VGK net faces light volume (<= 25 shots; PIT suppressed)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17PITVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (6.14 vs 1.33 bp); relationships: KXNHLSAVE-26OCT17PITVGK-VGKAHILL33-22|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: VGK offense succeeds (4+ goals)
- **Evgeni Malkin: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17PITVGK-PITSCROSBY87-1|no; why: higher confidence-adjusted growth (5.50 vs 0.45 bp); alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLSAVE-26OCT17PITVGK-VGKAHILL33-22|yes: MOSTLY_INDEPENDENT (phi 0.04); KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: PIT offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK wins by 2+; alternative: KXNHLPTS-26OCT17PITVGK-PITEMALKIN71-1|no; why: higher confidence-adjusted growth (3.59 vs 0.00 bp); despite a smaller raw edge (+0.020 vs +0.064/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLSAVE-26OCT17PITVGK-VGKAHILL33-22|yes: MOSTLY_INDEPENDENT (phi 0.03); KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VGK:NET_HIGH_VOLUME (p 0.1594): highest fidelity KXNHLSAVE-26OCT17PITVGK-VGKAHILL33-22|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT17PITVGK-VGKAHILL33-22|yes (same contract)
- thesis PIT:SUPPRESSED (p 0.4708): highest fidelity KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.3109): highest fidelity KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes (same contract)
- KXNHLSAVE-26OCT17PITVGK-VGKAHILL33-22|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 5% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.7 pts; fragile player expression; opposing: failure thesis VGK:NET_LOW_VOLUME (p 0.4451, phi -0.727)
- KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5155, phi -0.202)
- KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3109, phi -0.225)
- KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2823, phi -0.1)

portfolios: A EV +6.58 (adj +1.99) on $50.00, P(profit) 0.6715, adj growth 18.1 bp · B EV +6.79 (adj +2.31) on $50.00, P(profit) 0.7847, adj growth 20.4 bp · C EV +6.83 (adj +2.12) on $47.46, P(profit) 0.5793, adj growth 18.6 bp · R EV +0.28 (adj +0.17) on $5.00, P(profit) 0.7344, adj growth 6.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
