# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-08T22:57:09Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +24.14 | +7.42 | +14.57 | 0.600 | -51.10 | -65.38 | 54.56 |
| B thesis-diversified (joint) ← optimiser card | 125.67 | +17.46 | +9.04 | +12.45 | 0.613 | -38.35 | -52.36 | 78.83 |
| C best expression per thesis | 94.63 | +14.58 | +6.95 | +9.37 | 0.623 | -36.99 | -43.76 | 60.68 |
| R FUNDED research stakes | 23.00 | +2.49 | +1.09 | +2.25 | 0.556 | -8.49 | -10.99 | 0.00 |

## TBL @ WPG  ·  10000 joint draws  ·  404 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.420 / away 0.580

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_TBL_win | p_overtime | goals | shots WPG/TBL | WPG/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.50 | 0.50 | 0.00 | 5.98 | 26.9/27.3 | 23.8/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.53 | 0.47 | 0.48 | 5.88 | 27.1/27.4 | 24.2/23.8 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.095 | 0.41 | 0.59 | 0.00 | 5.96 | 21.6/32.6 | 28.4/18.6 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.45 | 0.55 | 0.44 | 5.86 | 21.6/32.4 | 29.0/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.48 | 0.52 | 0.00 | 9.26 | 28.4/28.9 | 22.8/22.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.50 | 0.50 | 0.00 | 3.49 | 25.7/26.1 | 24.1/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cole Perfetti: 1+ assists YES | 32 | 0.382 | 0.348 | +0.047 | +0.013 | $4.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 1.5 goals NO | 64 | 0.704 | 0.669 | +0.048 | +0.013 | $2.16 | FUNDED_RESEARCH | $1 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 76 | 0.813 | 0.784 | +0.041 | +0.011 | $5.19 | FUNDED_RESEARCH | $2 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 3.5 goals scored NO | 54 | 0.607 | 0.571 | +0.049 | +0.013 | $5.36 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Cole Perfetti: 1+ assists YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV08TBWPG-TB2|no; why: higher confidence-adjusted growth (1.70 vs 1.69 bp); despite a smaller raw edge (+0.047 vs +0.048/contract); relationships: KXNHLSPREAD-26NOV08TBWPG-TB2|no: REINFORCING (phi 0.172); KXNHLSPREAD-26NOV08TBWPG-TB3|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLTEAMTOTAL-26NOV08TBWPG-TB4|no: MOSTLY_INDEPENDENT (phi -0.008); failure: WPG offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes; why: Broad expression KXNHLSPREAD-26NOV08TBWPG-TB2|no selected over player prop KXNHLAST-26NOV08TBWPG-TBNKUCHEROV86-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.97 vs 0.72 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: REINFORCING (phi 0.172); KXNHLSPREAD-26NOV08TBWPG-TB3|no: DUPLICATIVE (phi 0.738); KXNHLTEAMTOTAL-26NOV08TBWPG-TB4|no: REINFORCING (phi 0.534); failure: TBL wins by 2+
- **Tampa Bay wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes has the higher standalone adjusted growth (1.70 vs 1.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.146); they share one thesis budget; relationships: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi 0.146); KXNHLSPREAD-26NOV08TBWPG-TB2|no: DUPLICATIVE (phi 0.738); KXNHLTEAMTOTAL-26NOV08TBWPG-TB4|no: DUPLICATIVE (phi 0.508); failure: TBL wins by 2+
- **Tampa Bay over 3.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV08TBWPG-TB2|no; why: Broad expression KXNHLTEAMTOTAL-26NOV08TBWPG-TB4|no selected over player prop KXNHLAST-26NOV08TBWPG-TBJCARLSON74-1|no because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.84 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26NOV08TBWPG-TB2|no: REINFORCING (phi 0.534); KXNHLSPREAD-26NOV08TBWPG-TB3|no: DUPLICATIVE (phi 0.508); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WPG:OFFENSE_4PLUS (p 0.3565): highest fidelity KXNHLSPREAD-26NOV08TBWPG-TB3|no [DIRECT], best adjusted EV KXNHLGAME-26NOV08TBWPG-TB|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.4853): highest fidelity KXNHLGAME-26NOV08TBWPG-TB|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV08TBWPG-TB4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.4046): highest fidelity KXNHLTEAMTOTAL-26NOV08TBWPG-TB4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV08TBWPG-TB4|no (same contract)
- KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 43% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4206, phi -0.296)
- KXNHLSPREAD-26NOV08TBWPG-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2964, phi -1.0)
- KXNHLSPREAD-26NOV08TBWPG-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2964, phi -0.738)
- KXNHLTEAMTOTAL-26NOV08TBWPG-TB4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3813, phi -0.975)
- override: Broad expression KXNHLTEAMTOTAL-26NOV08TBWPG-TB4|no selected over player prop KXNHLAST-26NOV08TBWPG-TBJCARLSON74-1|no because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.84 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26NOV08TBWPG-TB2|no selected over player prop KXNHLAST-26NOV08TBWPG-TBNKUCHEROV86-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.97 vs 0.72 (DIRECT vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +6.00 (adj +0.97) on $37.50, P(profit) 0.6305, adj growth 6.4 bp · B EV +1.50 (adj +0.42) on $17.01, P(profit) 0.6599, adj growth 3.7 bp · C EV +1.19 (adj +0.33) on $12.70, P(profit) 0.7036, adj growth 2.9 bp · R EV +0.35 (adj +0.10) on $5.00, P(profit) 0.5902, adj growth 3.2 bp

## NJD @ TOR  ·  10000 joint draws  ·  434 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.409 / away 0.591

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NJD_win | p_overtime | goals | shots TOR/NJD | TOR/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.132 | 0.45 | 0.55 | 0.00 | 6.04 | 22.9/35.6 | 31.7/19.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.50 | 0.50 | 0.48 | 5.91 | 23.3/35.9 | 32.6/20.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.54 | 0.46 | 0.00 | 5.99 | 29.0/29.7 | 26.4/25.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.52 | 0.48 | 0.47 | 5.95 | 29.2/30.1 | 26.8/25.8 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.084 | 0.44 | 0.56 | 0.00 | 9.27 | 24.7/37.8 | 31.0/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.53 | 0.47 | 0.00 | 9.27 | 30.5/31.3 | 25.3/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 10 | 0.149 | 0.136 | +0.043 | +0.029 | $7.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ goals YES | 17 | 0.215 | 0.202 | +0.035 | +0.022 | $6.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 72 | 0.772 | 0.758 | +0.038 | +0.024 | $20.00 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 12 | 0.151 | 0.142 | +0.024 | +0.015 | $4.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (19.19 vs 7.45 bp); relationships: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV08NJTOR-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV08NJTOR-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: TOR offense suppressed (<= 2 goals)
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (19.19 vs 7.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV08NJTOR-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV08NJTOR-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: TOR offense suppressed (<= 2 goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV08NJTOR-TOR2|yes; why: Player prop expression KXNHLGOAL-26NOV08NJTOR-NJTMEIER28-1|no selected over player prop KXNHLAST-26NOV08NJTOR-NJERODRIGUES17-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.90 vs 0.93 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV08NJTOR-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: NJD offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-NJLEVANGELISTA77-1|yes; why: higher confidence-adjusted growth (4.11 vs 0.30 bp); alternative not eligible: confidence-adjusted EV +0.0048 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV08NJTOR-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3902): highest fidelity KXNHLTEAMTOTAL-26NOV08NJTOR-TOR3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.3972): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-NJTMEIER28-1|no — Player prop expression KXNHLGOAL-26NOV08NJTOR-NJTMEIER28-1|no selected over player prop KXNHLAST-26NOV08NJTOR-NJERODRIGUES17-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.90 vs 0.93 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis TOR:WINS_BY_2PLUS (p 0.2854): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08NJTOR-NJ2|no (same contract)
- KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3946, phi -0.201)
- KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3946, phi -0.225)
- KXNHLGOAL-26NOV08NJTOR-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3788, phi -0.226)
- KXNHLGOAL-26NOV08NJTOR-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3972, phi -0.169)
- override: Player prop expression KXNHLGOAL-26NOV08NJTOR-NJTMEIER28-1|no selected over player prop KXNHLAST-26NOV08NJTOR-NJERODRIGUES17-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.90 vs 0.93 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.02 (adj +1.18) on $37.50, P(profit) 0.6842, adj growth 10.5 bp · B EV +6.04 (adj +3.97) on $38.02, P(profit) 0.3744, adj growth 34.3 bp · C EV +4.41 (adj +2.77) on $29.37, P(profit) 0.3348, adj growth 23.9 bp · R EV +0.26 (adj +0.16) on $5.00, P(profit) 0.7723, adj growth 5.8 bp

## PHI @ CGY  ·  10000 joint draws  ·  452 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.483 / away 0.517

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_PHI_win | p_overtime | goals | shots CGY/PHI | CGY/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.48 | 0.52 | 0.00 | 6.0 | 27.3/27.2 | 23.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.50 | 0.50 | 0.45 | 5.88 | 27.2/27.0 | 23.8/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.48 | 0.52 | 0.00 | 9.25 | 29.0/28.9 | 22.7/23.0 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.074 | 0.57 | 0.43 | 0.00 | 5.99 | 31.8/21.7 | 18.6/27.8 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.50 | 0.50 | 0.50 | 5.91 | 32.3/21.7 | 18.4/29.1 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.063 | 0.42 | 0.58 | 0.00 | 5.97 | 21.7/31.9 | 27.8/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Konecny: 1+ assists NO | 65 | 0.736 | 0.691 | +0.070 | +0.025 | $14.99 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Porter Martone: 1+ goals NO | 77 | 0.813 | 0.800 | +0.031 | +0.018 | $15.01 | FUNDED_RESEARCH | $4 | PHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 9 | 0.114 | 0.107 | +0.018 | +0.011 | $2.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Martin Pospisil: 1+ goals YES | 11 | 0.136 | 0.128 | +0.019 | +0.011 | $3.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no; why: higher confidence-adjusted growth (6.01 vs 3.96 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV08PHICGY-CGYMPOSPISIL76-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: PHI offense succeeds (4+ goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no; why: second expression of the same thesis: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no has the higher standalone adjusted growth (6.01 vs 3.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.056); they share one thesis budget; relationships: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV08PHICGY-CGYMPOSPISIL76-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PHI offense succeeds (4+ goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PHICGY-CGYMBACKLUND11-1|yes; why: higher confidence-adjusted growth (2.95 vs 0.08 bp); alternative not eligible: confidence-adjusted EV +0.0024 below the 0.010/contract floor; relationships: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV08PHICGY-CGYMPOSPISIL76-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CGY offense suppressed (<= 2 goals)
- **Martin Pospisil: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PHICGY-CGYMBACKLUND11-1|yes; why: higher confidence-adjusted growth (2.69 vs 0.08 bp); alternative not eligible: confidence-adjusted EV +0.0024 below the 0.010/contract floor; relationships: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis PHI:SUPPRESSED (p 0.4269): highest fidelity KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.3493): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3556, phi -0.238)
- KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3556, phi -0.187)
- KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4282, phi -0.143)
- KXNHLGOAL-26NOV08PHICGY-CGYMPOSPISIL76-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4282, phi -0.188)

portfolios: A EV +3.51 (adj +1.70) on $37.50, P(profit) 0.6894, adj growth 14.7 bp · B EV +3.19 (adj +1.50) on $35.83, P(profit) 0.6841, adj growth 13.4 bp · C EV +2.11 (adj +0.74) on $20.00, P(profit) 0.7362, adj growth 6.5 bp · R EV +0.16 (adj +0.09) on $4.00, P(profit) 0.8132, adj growth 3.3 bp

## PIT @ ANA  ·  10000 joint draws  ·  454 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_PIT_win | p_overtime | goals | shots ANA/PIT | ANA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.141 | 0.68 | 0.32 | 0.00 | 9.61 | 29.1/28.9 | 23.7/21.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.68 | 0.32 | 0.00 | 6.1 | 27.7/27.4 | 24.5/23.2 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.097 | 0.76 | 0.24 | 0.00 | 9.7 | 34.3/23.2 | 18.7/25.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.55 | 0.45 | 0.45 | 6.03 | 27.7/27.5 | 24.2/24.3 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.086 | 0.72 | 0.28 | 0.00 | 6.07 | 32.6/21.5 | 19.1/27.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.59 | 0.41 | 0.49 | 6.03 | 32.9/22.0 | 18.7/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anaheim over 5.5 goals scored YES | 14 | 0.216 | 0.176 | +0.068 | +0.027 | $4.59 | FUNDED_RESEARCH | $2 | GAME:HIGH_EVENT | FRAGILE (0.49) | EVIDENCE_MIXED | D |
| Pittsburgh wins by over 1.5 goals NO | 71 | 0.805 | 0.755 | +0.080 | +0.030 | $20.00 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Kaedan Korczak: 1+ goals YES | 3 | 0.051 | 0.043 | +0.019 | +0.011 | $2.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 34 | 0.401 | 0.384 | +0.045 | +0.029 | $7.81 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
- **Anaheim over 5.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes; why: higher confidence-adjusted growth (12.60 vs 1.81 bp); relationships: KXNHLSPREAD-26NOV08PITANA-PIT2|no: REINFORCING (phi 0.245); KXNHLGOAL-26NOV08PITANA-PITKKORCZAK6-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: REINFORCING (phi 0.205); failure: PIT wins (incl. OT/SO)
- **Pittsburgh wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes has the higher standalone adjusted growth (12.60 vs 10.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.245); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes: REINFORCING (phi 0.245); KXNHLGOAL-26NOV08PITANA-PITKKORCZAK6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.143); failure: PIT wins by 2+
- **Kaedan Korczak: 1+ goals YES** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLSPREAD-26NOV08PITANA-PIT2|no: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: PIT offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes; why: Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes because adjusted EV is 0.2 pts higher while thesis capture is 0.50 vs 0.20 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes: REINFORCING (phi 0.205); KXNHLSPREAD-26NOV08PITANA-PIT2|no: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26NOV08PITANA-PITKKORCZAK6-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.13, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.5797): highest fidelity KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-PIT2|no — Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes because adjusted EV is 0.2 pts higher while thesis capture is 0.50 vs 0.20 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis GAME:HIGH_EVENT (p 0.3995): highest fidelity KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.6301): highest fidelity KXNHLSPREAD-26NOV08PITANA-PIT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-PIT2|no (same contract)
- KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes: FUNDED_RESEARCH; family MIXED; loses 51% of the draws where the thesis happens; opposing: failure thesis PIT:WINS (p 0.3699, phi -0.361)
- KXNHLSPREAD-26NOV08PITANA-PIT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:WINS_BY_2PLUS (p 0.1953, phi -1.0)
- KXNHLGOAL-26NOV08PITANA-PITKKORCZAK6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4004, phi -0.1)
- KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2362, phi -0.24)
- override: Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes because adjusted EV is 0.2 pts higher while thesis capture is 0.50 vs 0.20 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +10.61 (adj +3.57) on $37.50, P(profit) 0.456, adj growth 22.9 bp · B EV +6.73 (adj +3.15) on $34.81, P(profit) 0.4667, adj growth 27.5 bp · C EV +6.87 (adj +3.11) on $32.56, P(profit) 0.3759, adj growth 27.3 bp · R EV +1.72 (adj +0.74) on $9.00, P(profit) 0.4396, adj growth 24.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
