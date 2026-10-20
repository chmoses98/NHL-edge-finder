# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-20T23:37:37Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +33.06 | +11.01 | +30.79 | 0.716 | -35.84 | -52.34 | 95.85 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +26.59 | +15.00 | +22.63 | 0.680 | -34.99 | -49.91 | 137.33 |
| C best expression per thesis | 149.07 | +26.12 | +12.92 | +23.18 | 0.679 | -35.98 | -52.86 | 116.85 |
| R FUNDED research stakes | 24.00 | +2.87 | +1.49 | +1.46 | 0.626 | -8.42 | -10.37 | 0.00 |

## WPG @ STL  ·  10000 joint draws  ·  506 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.551 / away 0.449

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_WPG_win | p_overtime | goals | shots STL/WPG | STL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.66 | 0.34 | 0.00 | 6.02 | 26.6/26.5 | 23.7/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.55 | 0.45 | 0.48 | 5.96 | 26.7/26.6 | 23.4/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.68 | 0.32 | 0.00 | 9.19 | 28.3/28.3 | 23.5/21.3 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.076 | 0.73 | 0.27 | 0.00 | 6.02 | 31.4/21.0 | 18.6/26.6 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.062 | 0.58 | 0.42 | 0.00 | 5.96 | 21.2/31.2 | 27.9/17.6 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.57 | 0.43 | 0.48 | 5.88 | 31.2/21.1 | 18.0/27.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 22 | 0.298 | 0.277 | +0.066 | +0.045 | $8.08 | FUNDED_RESEARCH | $3 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Haydn Fleury: 1+ goals NO | 94 | 0.962 | 0.955 | +0.018 | +0.011 | $12.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Philip Broberg: 1+ assists YES | 33 | 0.411 | 0.368 | +0.066 | +0.023 | $3.35 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
| Pius Suter: 1+ goals YES | 15 | 0.179 | 0.169 | +0.020 | +0.011 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes; why: higher confidence-adjusted growth (24.81 vs 5.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20WPGSTL-WPGHFLEURY24-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.141); KXNHLGOAL-26OCT20WPGSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: STL offense suppressed (<= 2 goals)
- **Haydn Fleury: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT20WPGSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: WPG offense succeeds (4+ goals)
- **Philip Broberg: 1+ assists YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (24.81 vs 5.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.141); they share one thesis budget; relationships: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.141); KXNHLGOAL-26OCT20WPGSTL-WPGHFLEURY24-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT20WPGSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.078); failure: STL offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (24.81 vs 1.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT20WPGSTL-WPGHFLEURY24-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.078); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis STL:OFFENSE_4PLUS (p 0.458): highest fidelity KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20WPGSTL-STLRTHOMAS18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3361, phi -0.242)
- KXNHLGOAL-26OCT20WPGSTL-WPGHFLEURY24-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3045, phi -0.089)
- KXNHLAST-26OCT20WPGSTL-STLPBROBERG6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3361, phi -0.279)
- KXNHLGOAL-26OCT20WPGSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3361, phi -0.212)

portfolios: A EV +5.01 (adj +2.73) on $25.00, P(profit) 0.5768, adj growth 23.9 bp · B EV +3.37 (adj +2.04) on $25.10, P(profit) 0.3518, adj growth 18.8 bp · C EV +3.18 (adj +2.16) on $24.81, P(profit) 0.2981, adj growth 19.6 bp · R EV +0.85 (adj +0.59) on $3.00, P(profit) 0.2981, adj growth 20.7 bp

## BOS @ DAL  ·  10000 joint draws  ·  422 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.598 / away 0.402

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_BOS_win | p_overtime | goals | shots DAL/BOS | DAL/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.51 | 0.49 | 0.00 | 6.06 | 26.6/26.4 | 22.7/23.0 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.109 | 0.59 | 0.41 | 0.00 | 6.02 | 31.5/20.6 | 17.5/27.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.47 | 0.53 | 0.46 | 5.9 | 26.6/26.4 | 23.1/23.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.54 | 0.46 | 0.46 | 5.92 | 31.7/20.7 | 17.5/28.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.48 | 0.52 | 0.00 | 9.22 | 27.9/27.7 | 21.8/22.0 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.065 | 0.60 | 0.40 | 0.00 | 9.31 | 33.6/22.1 | 17.1/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mikko Rantanen: 1+ goals NO | 68 | 0.735 | 0.720 | +0.040 | +0.025 | $12.17 | FUNDED_RESEARCH | $4 | DAL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Boston over 2.5 goals scored YES | 51 | 0.598 | 0.552 | +0.071 | +0.024 | $6.73 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pavel Zacha: 1+ goals YES | 23 | 0.270 | 0.259 | +0.028 | +0.017 | $2.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Thomas Harley: 1+ assists YES | 32 | 0.385 | 0.347 | +0.050 | +0.012 | $3.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DAL:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20BOSDAL-DAL3|no; why: higher confidence-adjusted growth (6.52 vs 1.66 bp); despite a smaller raw edge (+0.040 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT20BOSDAL-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT20BOSDAL-DALTHARLEY55-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.129); failure: DAL offense succeeds (4+ goals)
- **Boston over 2.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes selected over broad KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT20BOSDAL-BOSPZACHA18-1|yes: REINFORCING (phi 0.232); KXNHLAST-26OCT20BOSDAL-DALTHARLEY55-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: BOS offense suppressed (<= 2 goals)
- **Pavel Zacha: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes; why: KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes has the higher standalone adjusted growth (10.79 vs 3.26 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.194); relationships: KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: REINFORCING (phi 0.232); KXNHLAST-26OCT20BOSDAL-DALTHARLEY55-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: BOS offense suppressed (<= 2 goals)
- **Thomas Harley: 1+ assists YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT20BOSDAL-7|yes; why: KXNHLTOTAL-26OCT20BOSDAL-7|yes has the higher standalone adjusted growth (1.52 vs 1.46 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.201); relationships: KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: INTENTIONAL_DIVERSIFIER (phi -0.129); KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT20BOSDAL-BOSPZACHA18-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BOS:OFFENSE_4PLUS (p 0.3632): highest fidelity KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes — Broad expression KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes selected over broad KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis BOS:WINS (p 0.4864): highest fidelity KXNHLSPREAD-26OCT20BOSDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.25): highest fidelity KXNHLTOTAL-26OCT20BOSDAL-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20BOSDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3916, phi -0.225)
- KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.4135, phi -0.976)
- KXNHLGOAL-26OCT20BOSDAL-BOSPZACHA18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4135, phi -0.231)
- KXNHLAST-26OCT20BOSDAL-DALTHARLEY55-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3957, phi -0.298)
- override: Broad expression KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS3|yes selected over broad KXNHLTEAMTOTAL-26OCT20BOSDAL-BOS5|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.55 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.63 (adj +1.91) on $25.00, P(profit) 0.4574, adj growth 14.8 bp · B EV +2.38 (adj +1.03) on $24.63, P(profit) 0.6055, adj growth 9.6 bp · C EV +2.79 (adj +1.28) on $19.93, P(profit) 0.7874, adj growth 11.6 bp · R EV +0.50 (adj +0.24) on $6.00, P(profit) 0.4451, adj growth 8.6 bp

## MIN @ EDM  ·  10000 joint draws  ·  480 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.549 / away 0.451

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_MIN_win | p_overtime | goals | shots EDM/MIN | EDM/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.64 | 0.36 | 0.00 | 6.06 | 28.3/28.3 | 25.3/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.116 | 0.65 | 0.35 | 0.00 | 9.45 | 30.2/30.0 | 24.5/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.55 | 0.45 | 0.47 | 5.95 | 28.8/28.5 | 25.2/25.4 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.083 | 0.67 | 0.33 | 0.00 | 5.99 | 33.5/22.5 | 19.8/29.0 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.54 | 0.46 | 0.48 | 5.97 | 34.2/22.9 | 19.7/30.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.066 | 0.70 | 0.30 | 0.00 | 9.6 | 35.8/24.4 | 19.6/27.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 13 | 0.190 | 0.172 | +0.052 | +0.034 | $5.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Kasperi Kapanen: 1+ assists YES | 22 | 0.311 | 0.263 | +0.079 | +0.031 | $5.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_MIXED | D |
| Connor McDavid: 1+ assists NO | 32 | 0.410 | 0.362 | +0.074 | +0.027 | $7.42 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.67) | EVIDENCE_MIXED | D |
| Zach Hyman: 1+ goals YES | 33 | 0.375 | 0.361 | +0.029 | +0.016 | $4.25 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (21.29 vs 11.66 bp); despite a smaller raw edge (+0.052 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi 0.029); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.055); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: EDM offense suppressed (<= 2 goals)
- **Kasperi Kapanen: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20MINEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (11.66 vs 5.58 bp); relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.029); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.049); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi 0.125); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (7.18 vs 2.63 bp); despite a smaller raw edge (+0.074 vs +0.093/contract); relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.055); KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi -0.049); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.207); failure: EDM offense succeeds (4+ goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes; why: Player prop expression KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes selected over player prop KXNHLAST-26OCT20MINEDM-EDMVPODKOLZIN92-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.50 vs 0.55 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi 0.125); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.207); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4983): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes — Player prop expression KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes selected over player prop KXNHLAST-26OCT20MINEDM-EDMVPODKOLZIN92-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.50 vs 0.55 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis EDM:SUPPRESSED (p 0.2913): highest fidelity KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4276): highest fidelity KXNHLAST-26OCT20MINEDM-MINMSHABANOV49-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT20MINEDM-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2913, phi -0.178)
- KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2913, phi -0.211)
- KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 33% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4983, phi -0.328)
- KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2913, phi -0.265)
- override: Player prop expression KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes selected over player prop KXNHLAST-26OCT20MINEDM-EDMVPODKOLZIN92-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.50 vs 0.55 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.61 (adj +1.92) on $25.00, P(profit) 0.7112, adj growth 17.6 bp · B EV +5.83 (adj +2.86) on $22.30, P(profit) 0.4194, adj growth 26.2 bp · C EV +4.47 (adj +1.80) on $23.29, P(profit) 0.4975, adj growth 16.3 bp · R EV +0.17 (adj +0.09) on $2.00, P(profit) 0.3749, adj growth 3.0 bp

## DET @ SEA  ·  10000 joint draws  ·  450 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.485 / away 0.515

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_DET_win | p_overtime | goals | shots SEA/DET | SEA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.63 | 0.37 | 0.00 | 6.02 | 27.8/28.1 | 25.1/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.48 | 5.92 | 27.9/28.3 | 25.0/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.64 | 0.36 | 0.00 | 9.26 | 29.6/29.9 | 24.5/22.6 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 6.04 | 22.4/33.7 | 30.3/18.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.50 | 0.50 | 0.47 | 5.87 | 22.2/33.6 | 30.3/19.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.56 | 0.44 | 0.00 | 3.45 | 26.8/27.1 | 25.3/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 11 | 0.153 | 0.141 | +0.036 | +0.024 | $3.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Dylan Larkin: 1+ goals NO | 68 | 0.741 | 0.725 | +0.046 | +0.030 | $12.17 | FUNDED_RESEARCH | $4 | DET:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $3.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 17 | 0.212 | 0.200 | +0.032 | +0.020 | $3.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes; why: higher confidence-adjusted growth (12.40 vs 11.45 bp); despite a smaller raw edge (+0.037 vs +0.113/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT20DETSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: SEA offense suppressed (<= 2 goals)
- **Dylan Larkin: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20DETSEA-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (9.09 vs 6.02 bp); despite a smaller raw edge (+0.046 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT20DETSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: DET offense succeeds (4+ goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes; why: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes has the higher standalone adjusted growth (11.45 vs 7.37 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.085); relationships: KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT20DETSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: SEA offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes; why: Player prop expression KXNHLGOAL-26OCT20DETSEA-SEABCATTON27-1|yes selected over player prop KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.30 vs 0.44 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4437): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [DIRECT], best adjusted EV KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes — Player prop expression KXNHLGOAL-26OCT20DETSEA-SEABCATTON27-1|yes selected over player prop KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.30 vs 0.44 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis DET:SUPPRESSED (p 0.4539): highest fidelity KXNHLTEAMTOTAL-26OCT20DETSEA-DET4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.58): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20DETSEA-DET2|no (same contract)
- KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.164)
- KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3287, phi -0.226)
- KXNHLGOAL-26OCT20DETSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.182)
- KXNHLGOAL-26OCT20DETSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.193)
- override: Player prop expression KXNHLGOAL-26OCT20DETSEA-SEABCATTON27-1|yes selected over player prop KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.30 vs 0.44 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.28 (adj +1.77) on $25.00, P(profit) 0.5286, adj growth 15.8 bp · B EV +3.37 (adj +2.19) on $22.79, P(profit) 0.4067, adj growth 20.2 bp · C EV +4.78 (adj +1.68) on $30.81, P(profit) 0.6959, adj growth 15.4 bp · R EV +0.27 (adj +0.17) on $4.00, P(profit) 0.7414, adj growth 6.3 bp

## CAR @ VAN  ·  10000 joint draws  ·  452 bet sides mapped, 35 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.280 / away 0.720

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CAR_win | p_overtime | goals | shots VAN/CAR | VAN/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.171 | 0.37 | 0.63 | 0.00 | 6.02 | 20.8/34.0 | 29.5/18.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.144 | 0.48 | 0.52 | 0.48 | 5.95 | 21.1/34.6 | 31.1/17.8 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.128 | 0.37 | 0.63 | 0.00 | 9.39 | 22.5/36.1 | 28.6/17.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.082 | 0.42 | 0.58 | 0.00 | 6.04 | 27.0/28.3 | 24.3/23.8 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.073 | 0.41 | 0.59 | 0.00 | 3.47 | 19.8/32.7 | 30.3/18.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.48 | 0.52 | 0.49 | 5.98 | 26.7/28.0 | 24.7/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Filip Chytil: 1+ goals YES | 16 | 0.249 | 0.225 | +0.080 | +0.056 | $8.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 49 | 0.657 | 0.545 | +0.149 | +0.038 | $3.69 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 62 | 0.769 | 0.669 | +0.133 | +0.033 | $6.48 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 62 | 0.685 | 0.668 | +0.049 | +0.031 | $10.89 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT20CARVAN-VAN2|yes; why: higher confidence-adjusted growth (47.34 vs 25.62 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; relationships: KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.164); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: MOSTLY_INDEPENDENT (phi 0.134); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VAN offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (47.34 vs 12.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.164); they share one thesis budget; relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: REINFORCING (phi 0.164); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: DUPLICATIVE (phi 0.757); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: REINFORCING (phi 0.187); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (47.34 vs 10.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.134); they share one thesis budget; relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.134); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: DUPLICATIVE (phi 0.757); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: REINFORCING (phi 0.162); failure: CAR wins by 2+
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20CARVAN-VAN3|yes; why: KXNHLSPREAD-26OCT20CARVAN-VAN3|yes has the higher standalone adjusted growth (25.58 vs 9.26 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.135); relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.187); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: REINFORCING (phi 0.162); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:OFFENSE_4PLUS (p 0.3652): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.4391): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:SCORES_FIRST (p 0.4662): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes [DIRECT], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4186, phi -0.236)
- KXNHLSPREAD-26OCT20CARVAN-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 17.2 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3434, phi -1.0)
- KXNHLSPREAD-26OCT20CARVAN-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.4 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3434, phi -0.757)
- KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.458, phi -0.245)

portfolios: A EV +8.21 (adj +1.90) on $25.00, P(profit) 0.5489, adj growth 16.4 bp · B EV +7.36 (adj +4.02) on $29.77, P(profit) 0.5943, adj growth 36.8 bp · C EV +7.93 (adj +4.59) on $16.93, P(profit) 0.3316, adj growth 41.2 bp · R EV +0.94 (adj +0.32) on $6.00, P(profit) 0.5589, adj growth 12.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT20CARVAN-VAN|yes == KXNHLGAME-26OCT20CARVAN-CAR|no

## TBL @ VGK  ·  10000 joint draws  ·  490 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TBL_win | p_overtime | goals | shots VGK/TBL | VGK/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.63 | 0.37 | 0.00 | 6.03 | 26.8/26.8 | 23.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.49 | 5.94 | 26.8/27.1 | 23.8/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.65 | 0.35 | 0.00 | 9.21 | 28.5/28.5 | 23.4/21.5 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.072 | 0.58 | 0.42 | 0.00 | 5.95 | 21.4/31.7 | 28.4/17.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.067 | 0.70 | 0.30 | 0.00 | 5.99 | 31.4/21.2 | 18.5/26.7 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.54 | 0.46 | 0.53 | 2.82 | 25.4/25.4 | 23.9/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 4 | 0.080 | 0.069 | +0.037 | +0.026 | $3.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Brett Howden: 1+ goals YES | 19 | 0.233 | 0.221 | +0.032 | +0.020 | $3.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 72 | 0.767 | 0.754 | +0.033 | +0.020 | $11.64 | FUNDED_RESEARCH | $3 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ goals NO | 65 | 0.696 | 0.682 | +0.030 | +0.016 | $6.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes; why: higher confidence-adjusted growth (34.44 vs 5.57 bp); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VGK offense suppressed (<= 2 goals)
- **Brett Howden: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20TBVGK-TB2|no; why: higher confidence-adjusted growth (5.57 vs 5.30 bp); despite a smaller raw edge (+0.032 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT20TBVGK-4|no; why: higher confidence-adjusted growth (4.42 vs 0.17 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.007 vs 0.351); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: VGK offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no; why: Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis TBL:SUPPRESSED (p 0.4793): highest fidelity KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no — Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis VGK:OFFENSE_4PLUS (p 0.4283): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- thesis VGK:WINS (p 0.5848): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3602, phi -0.131)
- KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3602, phi -0.236)
- KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4283, phi -0.197)
- KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3048, phi -0.253)
- override: Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT20TBVGK-TBJCARLSON74-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.32 (adj +0.78) on $25.00, P(profit) 0.7059, adj growth 7.4 bp · B EV +4.29 (adj +2.86) on $25.40, P(profit) 0.6546, adj growth 25.8 bp · C EV +2.98 (adj +1.41) on $33.30, P(profit) 0.6472, adj growth 12.8 bp · R EV +0.13 (adj +0.08) on $3.00, P(profit) 0.7669, adj growth 3.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
