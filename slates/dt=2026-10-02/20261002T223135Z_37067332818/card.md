# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-02T22:31:35Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +29.90 | +10.71 | +24.27 | 0.677 | -37.29 | -52.86 | 92.34 |
| B thesis-diversified (joint) ← optimiser card | 146.23 | +33.03 | +17.96 | +26.25 | 0.642 | -56.23 | -69.44 | 155.94 |
| C best expression per thesis | 141.22 | +24.09 | +11.29 | +18.18 | 0.626 | -42.94 | -56.80 | 97.88 |
| R FUNDED research stakes | 11.00 | +2.42 | +1.63 | -3.81 | 0.437 | -11.00 | -11.00 | 0.00 |

## WSH @ CAR  ·  10000 joint draws  ·  364 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.571 / away 0.429

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WSH_win | p_overtime | goals | shots CAR/WSH | CAR/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.139 | 0.64 | 0.36 | 0.00 | 6.01 | 33.0/20.7 | 17.9/28.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.125 | 0.53 | 0.47 | 0.46 | 5.87 | 33.4/21.0 | 17.8/29.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.59 | 0.41 | 0.00 | 6.04 | 27.4/26.6 | 23.4/23.5 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.096 | 0.66 | 0.34 | 0.00 | 9.21 | 35.2/22.3 | 17.5/27.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.50 | 0.50 | 0.48 | 5.91 | 27.2/26.5 | 23.2/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.57 | 0.43 | 0.00 | 9.22 | 28.9/27.9 | 22.4/22.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Justin Sourdif: 1+ goals YES | 10 | 0.150 | 0.136 | +0.044 | +0.030 | $7.49 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 18 | 0.234 | 0.220 | +0.044 | +0.029 | $8.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Alex Tuch: 1+ assists NO | 75 | 0.877 | 0.791 | +0.114 | +0.028 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WSH:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| William Carrier: 1+ goals YES | 9 | 0.126 | 0.114 | +0.030 | +0.019 | $4.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
- **Justin Sourdif: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes; why: higher confidence-adjusted growth (20.07 vs 11.89 bp); despite a smaller raw edge (+0.044 vs +0.044/contract); relationships: KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: WSH offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-WSHTWILSON43-1|yes; why: higher confidence-adjusted growth (11.89 vs 0.04 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0019 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: WSH offense suppressed (<= 2 goals)
- **Alex Tuch: 1+ assists NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT02WSHCAR-WSHRLEONARD9-1|no; why: higher confidence-adjusted growth (9.59 vs 1.85 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: WSH offense succeeds (4+ goals)
- **William Carrier: 1+ goals YES** — thesis: CAR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02WSHCAR-CARKMILLER19-1|yes; why: higher confidence-adjusted growth (8.58 vs 1.37 bp); despite a smaller raw edge (+0.030 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: CAR offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3285): highest fidelity KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes (same contract)
- thesis CAR:SUPPRESSED (p 0.3589): highest fidelity KXNHLAST-26OCT02WSHCAR-CARSAHO20-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT02WSHCAR-CARSAHO20-1|no (same contract)
- thesis WSH:SUPPRESSED (p 0.4491): highest fidelity KXNHLGOAL-26OCT02WSHCAR-WSHRLEONARD9-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT02WSHCAR-WSHRLEONARD9-1|no (same contract)
- KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4491, phi -0.19)
- KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4491, phi -0.262)
- KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.2 pts; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.3285, phi -0.157)
- KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:SUPPRESSED (p 0.3589, phi -0.15)

portfolios: A EV +6.30 (adj +2.14) on $37.50, P(profit) 0.4945, adj growth 18.8 bp · B EV +9.46 (adj +5.03) on $40.56, P(profit) 0.4299, adj growth 43.9 bp · C EV +4.72 (adj +2.00) on $38.46, P(profit) 0.3716, adj growth 17.4 bp · R EV +0.82 (adj +0.56) on $2.00, P(profit) 0.15, adj growth 19.0 bp

## BOS @ WPG  ·  10000 joint draws  ·  346 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_BOS_win | p_overtime | goals | shots WPG/BOS | WPG/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.51 | 0.49 | 0.00 | 5.99 | 27.3/27.0 | 23.3/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.52 | 0.48 | 0.47 | 5.9 | 27.2/27.0 | 23.8/24.0 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.088 | 0.56 | 0.44 | 0.00 | 6.01 | 32.4/21.4 | 18.3/28.6 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.53 | 0.47 | 0.49 | 5.92 | 32.4/21.9 | 18.7/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.52 | 0.48 | 0.00 | 9.22 | 29.0/28.7 | 22.8/23.0 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.50 | 0.50 | 0.50 | 2.81 | 26.1/25.8 | 24.3/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Marat Khusnutdinov: 1+ goals YES | 9 | 0.145 | 0.130 | +0.049 | +0.034 | $8.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Elias Lindholm: 1+ goals YES | 18 | 0.231 | 0.217 | +0.040 | +0.026 | $7.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 29 | 0.339 | 0.325 | +0.034 | +0.021 | $7.68 | FUNDED_RESEARCH | $2 | WPG:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| David Pastrnak: 1+ goals NO | 63 | 0.669 | 0.658 | +0.023 | +0.012 | $7.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (28.11 vs 9.75 bp); relationships: KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: BOS offense suppressed (<= 2 goals)
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes has the higher standalone adjusted growth (28.11 vs 9.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: BOS offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02BOSWPG-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (4.48 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: WPG offense suppressed (<= 2 goals)
- **David Pastrnak: 1+ goals NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT02BOSWPG-BOSJPETERKA10-1|no; why: Player prop expression KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.82 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, WPG shot control · normal event (5-7) · decided (2+) 0.09.
- thesis BOS:OFFENSE_4PLUS (p 0.3523): highest fidelity KXNHLAST-26OCT02BOSWPG-BOSELINDHOLM28-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3661): highest fidelity KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.4201): highest fidelity KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no (same contract)
- KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4201, phi -0.189)
- KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4201, phi -0.222)
- KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4128, phi -0.279)
- KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3523, phi -0.26)
- override: Player prop expression KXNHLGOAL-26OCT02BOSWPG-BOSDPASTRNAK88-1|no selected over player prop KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.82 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +9.02 (adj +4.69) on $37.50, P(profit) 0.5254, adj growth 39.7 bp · B EV +6.95 (adj +4.64) on $31.47, P(profit) 0.4942, adj growth 39.7 bp · C EV +5.35 (adj +3.60) on $23.85, P(profit) 0.4367, adj growth 30.7 bp · R EV +0.23 (adj +0.14) on $2.00, P(profit) 0.3387, adj growth 4.7 bp

## STL @ DAL  ·  10000 joint draws  ·  334 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.623 / away 0.378

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_STL_win | p_overtime | goals | shots DAL/STL | DAL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.55 | 0.45 | 0.00 | 5.98 | 25.9/25.6 | 22.4/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.47 | 5.95 | 26.0/25.8 | 22.6/22.6 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.093 | 0.61 | 0.39 | 0.00 | 6.0 | 30.9/20.4 | 17.5/26.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.57 | 0.43 | 0.00 | 9.21 | 27.7/27.6 | 22.1/21.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.56 | 0.44 | 0.50 | 5.92 | 31.0/20.5 | 17.4/27.6 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.057 | 0.63 | 0.37 | 0.00 | 9.21 | 32.3/21.7 | 16.9/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pius Suter: 1+ goals YES | 11 | 0.158 | 0.145 | +0.041 | +0.028 | $6.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 1+ goals NO | 68 | 0.738 | 0.723 | +0.043 | +0.027 | $18.26 | FUNDED_RESEARCH | $5 | DAL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Mason McTavish: 1+ assists NO | 74 | 0.874 | 0.777 | +0.121 | +0.024 | $18.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Dylan Holloway: 1+ goals YES | 26 | 0.312 | 0.298 | +0.039 | +0.025 | $7.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT02STLDAL-STL|yes; why: higher confidence-adjusted growth (16.36 vs 8.37 bp); despite a smaller raw edge (+0.041 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: INTENTIONAL_DIVERSIFIER (phi -0.054); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: STL offense suppressed (<= 2 goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT02STLDAL-DALMRANTANEN96-2|no; why: KXNHLAST-26OCT02STLDAL-DALMRANTANEN96-2|no has the higher standalone adjusted growth (10.51 vs 7.71 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.006); relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: DAL offense succeeds (4+ goals)
- **Mason McTavish: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT02STLDAL-STLMMCTAVISH83-1|no; why: higher confidence-adjusted growth (6.72 vs 0.26 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.054); KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi -0.044); failure: STL offense succeeds (4+ goals)
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes has the higher standalone adjusted growth (16.36 vs 6.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.023); they share one thesis budget; relationships: KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.044); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.3441): highest fidelity KXNHLTEAMTOTAL-26OCT02STLDAL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-STL|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.3803): highest fidelity KXNHLSPREAD-26OCT02STLDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-STL|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4586): highest fidelity KXNHLGAME-26OCT02STLDAL-STL|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT02STLDAL-STL|yes (same contract)
- KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.432, phi -0.208)
- KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4013, phi -0.231)
- KXNHLAST-26OCT02STLDAL-STLMMCTAVISH83-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.9 pts; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.3441, phi -0.177)
- KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.432, phi -0.266)

portfolios: A EV +5.27 (adj +1.08) on $37.50, P(profit) 0.7266, adj growth 9.9 bp · B EV +7.34 (adj +3.47) on $50.00, P(profit) 0.7901, adj growth 31.1 bp · C EV +5.70 (adj +2.90) on $35.54, P(profit) 0.5025, adj growth 25.5 bp · R EV +0.31 (adj +0.20) on $5.00, P(profit) 0.7383, adj growth 7.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02STLDAL-DAL|no == KXNHLGAME-26OCT02STLDAL-STL|yes

## ANA @ VGK  ·  10000 joint draws  ·  358 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.643 / away 0.357

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_ANA_win | p_overtime | goals | shots VGK/ANA | VGK/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.66 | 0.34 | 0.00 | 6.03 | 28.1/28.2 | 25.3/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.54 | 0.46 | 0.50 | 5.97 | 28.0/28.1 | 24.8/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.66 | 0.34 | 0.00 | 9.35 | 29.5/29.6 | 24.3/22.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.076 | 0.62 | 0.38 | 0.00 | 6.04 | 22.5/33.4 | 30.2/18.7 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.48 | 0.52 | 0.47 | 5.9 | 22.5/33.5 | 30.2/19.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.061 | 0.70 | 0.30 | 0.00 | 6.02 | 32.6/22.3 | 19.7/28.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Washe: 1+ goals YES | 7 | 0.114 | 0.102 | +0.040 | +0.027 | $6.11 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 18 | 0.233 | 0.218 | +0.043 | +0.028 | $8.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ assists YES | 23 | 0.363 | 0.270 | +0.121 | +0.028 | $6.47 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | ANA:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
| Judd Caulfield: 1+ goals YES | 8 | 0.109 | 0.101 | +0.024 | +0.016 | $3.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (22.68 vs 11.06 bp); despite a smaller raw edge (+0.040 vs +0.043/contract); relationships: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.029); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (11.06 vs 9.14 bp); despite a smaller raw edge (+0.043 vs +0.121/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ assists YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (11.06 vs 9.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.049); failure: ANA offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (11.06 vs 6.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.029); KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.049); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.3325): highest fidelity KXNHLGAME-26OCT02ANAVGK-VGK|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.4029): highest fidelity KXNHLGAME-26OCT02ANAVGK-VGK|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:SUPPRESSED (p 0.4449): highest fidelity KXNHLAST-26OCT02ANAVGK-ANALCARLSSON91-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT02ANAVGK-ANALCARLSSON91-1|no (same contract)
- KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.176)
- KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.241)
- KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 45% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.292)
- KXNHLGOAL-26OCT02ANAVGK-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.4449, phi -0.166)

portfolios: A EV +9.31 (adj +2.80) on $37.50, P(profit) 0.6689, adj growth 24.0 bp · B EV +9.28 (adj +4.82) on $24.20, P(profit) 0.6009, adj growth 41.2 bp · C EV +8.31 (adj +2.79) on $43.37, P(profit) 0.487, adj growth 24.3 bp · R EV +1.06 (adj +0.73) on $2.00, P(profit) 0.1141, adj growth 23.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT02ANAVGK-ANA|yes == KXNHLGAME-26OCT02ANAVGK-VGK|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
