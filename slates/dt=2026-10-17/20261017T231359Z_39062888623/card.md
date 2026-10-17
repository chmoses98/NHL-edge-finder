# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T23:13:59Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +25.31 | +9.63 | +19.08 | 0.610 | -52.38 | -69.79 | 75.08 |
| B thesis-diversified (joint) ← optimiser card | 125.37 | +17.72 | +9.41 | +11.78 | 0.569 | -34.60 | -51.31 | 81.74 |
| C best expression per thesis | 70.14 | +9.19 | +3.65 | +7.57 | 0.632 | -26.44 | -42.53 | 32.19 |
| R FUNDED research stakes | 12.00 | +0.65 | +0.38 | -0.22 | 0.344 | -5.98 | -6.25 | 0.00 |

## STL @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.497 / away 0.503

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_STL_win | p_overtime | goals | shots NSH/STL | NSH/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.48 | 0.52 | 0.00 | 6.04 | 27.3/27.5 | 23.7/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.49 | 5.97 | 27.5/27.5 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.50 | 0.50 | 0.00 | 9.39 | 29.1/29.0 | 22.9/22.8 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.068 | 0.47 | 0.53 | 0.00 | 6.0 | 21.6/31.9 | 27.9/18.4 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.068 | 0.59 | 0.41 | 0.00 | 5.98 | 32.2/21.8 | 18.7/28.2 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.57 | 0.43 | 0.46 | 5.92 | 32.3/22.0 | 18.7/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Wilsby: 1+ goals YES | 4 | 0.071 | 0.063 | +0.028 | +0.020 | $4.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Robert Thomas: 2+ goals YES | 3 | 0.047 | 0.043 | +0.015 | +0.011 | $2.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 27 | 0.313 | 0.301 | +0.029 | +0.017 | $6.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Dalibor Dvorsky: 1+ goals NO | 82 | 0.849 | 0.841 | +0.019 | +0.011 | $16.86 | FUNDED_RESEARCH | $5 | STL:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (20.87 vs 3.12 bp); despite a smaller raw edge (+0.028 vs +0.029/contract); relationships: KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-2|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17STLNSH-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: NSH offense suppressed (<= 2 goals)
- **Robert Thomas: 2+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (7.91 vs 4.02 bp); despite a smaller raw edge (+0.015 vs +0.031/contract); relationships: KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17STLNSH-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: STL offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT17STLNSH-9|yes; why: higher confidence-adjusted growth (3.12 vs 0.94 bp); despite a smaller raw edge (+0.029 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.931 vs 0.376); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-2|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17STLNSH-STLDDVORSKY15-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NSH offense suppressed (<= 2 goals)
- **Dalibor Dvorsky: 1+ goals NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17STLNSH-STLDHOLLOWAY81-1|no; why: higher confidence-adjusted growth (1.71 vs 0.01 bp); despite a smaller raw edge (+0.019 vs +0.025/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-2|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: STL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4049): highest fidelity KXNHLAST-26OCT17STLNSH-STLJNEIGHBOURS63-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.4176): highest fidelity KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes (same contract)
- thesis STL:SUPPRESSED (p 0.3808): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3659, phi -0.106)
- KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3808, phi -0.153)
- KXNHLGOAL-26OCT17STLNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3659, phi -0.249)
- KXNHLGOAL-26OCT17STLNSH-STLDDVORSKY15-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4049, phi -0.177)

portfolios: A EV +8.99 (adj +4.57) on $37.36, P(profit) 0.4089, adj growth 33.8 bp · B EV +5.14 (adj +3.57) on $29.92, P(profit) 0.3534, adj growth 30.2 bp · C EV +1.33 (adj +0.80) on $11.86, P(profit) 0.5078, adj growth 6.9 bp · R EV +0.11 (adj +0.06) on $5.00, P(profit) 0.8494, adj growth 2.1 bp

## BOS @ LAK  ·  10000 joint draws  ·  416 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.555 / away 0.445

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
| Charlie McAvoy: 1+ assists NO | 59 | 0.675 | 0.630 | +0.068 | +0.023 | $15.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Hampus Lindholm: 1+ assists YES | 25 | 0.321 | 0.275 | +0.058 | +0.012 | $4.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17BOSLA-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (4.81 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.063); failure: BOS offense succeeds (4+ goals)
- **Hampus Lindholm: 1+ assists YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (1.71 vs 1.29 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.063); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BOS:SUPPRESSED (p 0.4519): highest fidelity KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.3292): highest fidelity KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes (same contract)
- KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3292, phi -0.254)
- KXNHLAST-26OCT17BOSLA-BOSHLINDHOLM27-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4519, phi -0.271)

portfolios: A EV +5.27 (adj +1.35) on $31.95, P(profit) 0.3209, adj growth 9.0 bp · B EV +2.70 (adj +0.80) on $20.10, P(profit) 0.6746, adj growth 7.0 bp · C EV +2.70 (adj +0.80) on $20.10, P(profit) 0.6746, adj growth 7.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ UTA  ·  10000 joint draws  ·  436 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.561 / away 0.439

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
| Nate Schmidt: 1+ goals YES | 4 | 0.067 | 0.058 | +0.024 | +0.015 | $3.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 71 | 0.798 | 0.751 | +0.073 | +0.027 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ goals YES | 8 | 0.110 | 0.100 | +0.025 | +0.015 | $4.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Zach Hyman: 1+ goals YES | 31 | 0.358 | 0.345 | +0.033 | +0.020 | $9.02 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Nate Schmidt: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (11.23 vs 1.95 bp); relationships: KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: UTA offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (8.04 vs 5.81 bp); relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.218); failure: EDM offense succeeds (4+ goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (5.96 vs 5.23 bp); despite a smaller raw edge (+0.025 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: EDM offense suppressed (<= 2 goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes; why: Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.51 vs 0.50 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.218); KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:SUPPRESSED (p 0.3535): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.4295): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes — Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.51 vs 0.50 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis UTA:OFFENSE_4PLUS (p 0.4702): highest fidelity KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes (same contract)
- KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3208, phi -0.107)
- KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4295, phi -0.328)
- KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3535, phi -0.149)
- KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3535, phi -0.271)
- override: Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.51 vs 0.50 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +8.06 (adj +2.26) on $40.34, P(profit) 0.7047, adj growth 19.0 bp · B EV +5.90 (adj +3.09) on $36.23, P(profit) 0.3772, adj growth 27.2 bp · C EV +4.34 (adj +1.58) on $31.97, P(profit) 0.4259, adj growth 14.2 bp · R EV +0.30 (adj +0.18) on $3.00, P(profit) 0.358, adj growth 5.7 bp

## PIT @ VGK  ·  10000 joint draws  ·  424 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.643 / away 0.357

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
| Mitch Marner: 1+ goals NO | 68 | 0.734 | 0.720 | +0.039 | +0.024 | $15.08 | FUNDED_RESEARCH | $4 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Trevor Connelly: 1+ assists NO | 69 | 0.773 | 0.727 | +0.068 | +0.022 | $14.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.084 | 0.075 | +0.020 | +0.011 | $2.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:WINS_BY_2PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Bryan Rust: 1+ goals YES | 24 | 0.286 | 0.272 | +0.033 | +0.019 | $6.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17PITVGK-VGKJEICHEL9-2|no; why: higher confidence-adjusted growth (6.14 vs 0.73 bp); despite a smaller raw edge (+0.039 vs +0.116/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17PITVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.042); KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: VGK offense succeeds (4+ goals)
- **Trevor Connelly: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17PITVGK-VGKJEICHEL9-2|no; why: higher confidence-adjusted growth (4.94 vs 0.73 bp); despite a smaller raw edge (+0.068 vs +0.116/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.042); KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VGK offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK wins by 2+; alternative: KXNHLPTS-26OCT17PITVGK-PITEMALKIN71-1|no; why: higher confidence-adjusted growth (4.54 vs 0.00 bp); despite a smaller raw edge (+0.020 vs +0.054/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT17PITVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: VGK offense suppressed (<= 2 goals)
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17PITVGK-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (4.26 vs 0.86 bp); alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT17PITVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.3109): highest fidelity KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.2823): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis VGK:WINS_BY_2PLUS (p 0.4186): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5155, phi -0.202)
- KXNHLAST-26OCT17PITVGK-VGKTCONNELLY24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5155, phi -0.185)
- KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2823, phi -0.1)
- KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4708, phi -0.264)

portfolios: A EV +2.99 (adj +1.45) on $40.34, P(profit) 0.5901, adj growth 13.2 bp · B EV +3.98 (adj +1.95) on $39.12, P(profit) 0.707, adj growth 17.4 bp · C EV +0.82 (adj +0.47) on $6.21, P(profit) 0.286, adj growth 4.1 bp · R EV +0.23 (adj +0.14) on $4.00, P(profit) 0.7344, adj growth 5.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
