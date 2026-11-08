# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-08T22:03:55Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +25.59 | +8.07 | +15.06 | 0.602 | -48.33 | -61.15 | 61.41 |
| B thesis-diversified (joint) ← optimiser card | 136.97 | +22.13 | +12.62 | +12.75 | 0.614 | -45.32 | -61.56 | 109.28 |
| C best expression per thesis | 82.20 | +14.58 | +6.42 | +11.11 | 0.584 | -35.43 | -36.51 | 55.94 |
| R FUNDED research stakes | 21.00 | +2.32 | +1.31 | +0.42 | 0.652 | -6.48 | -10.31 | 0.00 |

## TBL @ WPG  ·  10000 joint draws  ·  414 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.420 / away 0.580

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_TBL_win | p_overtime | goals | shots WPG/TBL | WPG/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.51 | 0.49 | 0.00 | 6.01 | 27.1/27.5 | 24.0/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.49 | 0.51 | 0.47 | 5.91 | 27.0/27.4 | 24.2/23.7 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.096 | 0.39 | 0.61 | 0.00 | 5.98 | 21.4/32.7 | 28.6/18.5 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.47 | 0.53 | 0.46 | 5.9 | 21.6/32.7 | 29.3/18.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.48 | 0.52 | 0.00 | 9.27 | 28.5/28.8 | 22.8/22.7 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.058 | 0.41 | 0.59 | 0.00 | 9.28 | 23.0/34.4 | 26.9/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charle-Edouard D'Astous: 1+ goals NO | 89 | 0.921 | 0.912 | +0.024 | +0.015 | $20.00 | FUNDED_RESEARCH | $5 | TBL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Cole Perfetti: 1+ assists YES | 32 | 0.396 | 0.355 | +0.061 | +0.020 | $6.58 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.58) | EVIDENCE_MIXED | D |
| Cole Koepke: 1+ goals YES | 9 | 0.113 | 0.106 | +0.017 | +0.010 | $2.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 77 | 0.821 | 0.793 | +0.039 | +0.011 | $8.39 | FUNDED_RESEARCH | $3 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV08TBWPG-TBVHEDMAN77-1|no; why: higher confidence-adjusted growth (5.29 vs 1.85 bp); despite a smaller raw edge (+0.024 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV08TBWPG-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLSPREAD-26NOV08TBWPG-TB3|no: MOSTLY_INDEPENDENT (phi 0.058); failure: TBL offense succeeds (4+ goals)
- **Cole Perfetti: 1+ assists YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV08TBWPG-TB3|no; why: higher confidence-adjusted growth (4.02 vs 1.46 bp); relationships: KXNHLGOAL-26NOV08TBWPG-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV08TBWPG-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.03); KXNHLSPREAD-26NOV08TBWPG-TB3|no: REINFORCING (phi 0.162); failure: WPG offense suppressed (<= 2 goals)
- **Cole Koepke: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes has the higher standalone adjusted growth (4.02 vs 2.67 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.030); they share one thesis budget; relationships: KXNHLGOAL-26NOV08TBWPG-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: MOSTLY_INDEPENDENT (phi 0.03); KXNHLSPREAD-26NOV08TBWPG-TB3|no: MOSTLY_INDEPENDENT (phi 0.084); failure: WPG offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes; why: Broad expression KXNHLSPREAD-26NOV08TBWPG-TB3|no selected over player prop KXNHLAST-26NOV08TBWPG-TBVHEDMAN77-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.89 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV08TBWPG-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.058); KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: REINFORCING (phi 0.162); KXNHLGOAL-26NOV08TBWPG-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.084); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.3592): highest fidelity KXNHLSPREAD-26NOV08TBWPG-TB3|no [DIRECT], best adjusted EV KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.4829): highest fidelity KXNHLSPREAD-26NOV08TBWPG-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.4017): highest fidelity KXNHLSPREAD-26NOV08TBWPG-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV08TBWPG-TBVHEDMAN77-1|no — Broad expression KXNHLSPREAD-26NOV08TBWPG-TB3|no selected over player prop KXNHLAST-26NOV08TBWPG-TBVHEDMAN77-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.89 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26NOV08TBWPG-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3836, phi -0.11)
- KXNHLAST-26NOV08TBWPG-WPGCPERFETTI91-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 42% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4151, phi -0.314)
- KXNHLGOAL-26NOV08TBWPG-WPGCKOEPKE45-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4151, phi -0.166)
- KXNHLSPREAD-26NOV08TBWPG-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.2932, phi -0.725)
- override: Broad expression KXNHLSPREAD-26NOV08TBWPG-TB3|no selected over player prop KXNHLAST-26NOV08TBWPG-TBVHEDMAN77-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.89 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.95 (adj +1.17) on $37.50, P(profit) 0.5741, adj growth 9.7 bp · B EV +2.59 (adj +1.11) on $37.45, P(profit) 0.4278, adj growth 9.9 bp · C EV +2.21 (adj +0.67) on $20.49, P(profit) 0.396, adj growth 5.9 bp · R EV +0.28 (adj +0.12) on $8.00, P(profit) 0.7619, adj growth 4.6 bp

## NJD @ TOR  ·  10000 joint draws  ·  428 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.416 / away 0.584

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NJD_win | p_overtime | goals | shots TOR/NJD | TOR/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.129 | 0.49 | 0.51 | 0.00 | 5.99 | 23.3/36.2 | 32.4/19.9 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.49 | 5.9 | 23.0/35.8 | 32.4/19.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.53 | 0.47 | 0.00 | 6.02 | 28.8/29.6 | 26.1/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.45 | 5.9 | 29.0/29.7 | 26.4/25.7 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.086 | 0.47 | 0.53 | 0.00 | 9.31 | 24.5/37.5 | 30.6/18.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.56 | 0.44 | 0.00 | 9.33 | 30.4/31.3 | 25.1/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brandon Duhaime: 1+ goals YES | 6 | 0.101 | 0.089 | +0.037 | +0.025 | $5.81 | FUNDED_RESEARCH | $2 | TOR:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 10 | 0.148 | 0.134 | +0.042 | +0.028 | $6.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ goals YES | 17 | 0.224 | 0.209 | +0.044 | +0.029 | $8.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Colton Sissons: 1+ goals YES | 9 | 0.129 | 0.118 | +0.033 | +0.022 | $5.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Brandon Duhaime: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes; why: higher confidence-adjusted growth (22.21 vs 17.05 bp); despite a smaller raw edge (+0.037 vs +0.042/contract); relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: TOR offense suppressed (<= 2 goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR wins by 2+; alternative: KXNHLSPREAD-26NOV08NJTOR-TOR2|yes; why: higher confidence-adjusted growth (17.05 vs 4.47 bp); despite a smaller raw edge (+0.042 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.864 vs 0.529); relationships: KXNHLGOAL-26NOV08NJTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: TOR offense suppressed (<= 2 goals)
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (17.05 vs 12.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV08NJTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: TOR offense suppressed (<= 2 goals)
- **Colton Sissons: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (17.05 vs 11.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26NOV08NJTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3942): highest fidelity KXNHLTEAMTOTAL-26NOV08NJTOR-TOR3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS_BY_2PLUS (p 0.2873): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4003): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08NJTOR-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV08NJTOR-TORBDUHAIME24-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.388, phi -0.13)
- KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.388, phi -0.202)
- KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.388, phi -0.195)
- KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.388, phi -0.17)

portfolios: A EV +5.31 (adj +1.66) on $37.50, P(profit) 0.5791, adj growth 14.5 bp · B EV +9.87 (adj +6.62) on $26.24, P(profit) 0.4816, adj growth 56.5 bp · C EV +3.41 (adj +1.97) on $10.04, P(profit) 0.3587, adj growth 16.9 bp · R EV +1.14 (adj +0.79) on $2.00, P(profit) 0.1005, adj growth 24.8 bp

## PHI @ CGY  ·  10000 joint draws  ·  452 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.483 / away 0.517

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_PHI_win | p_overtime | goals | shots CGY/PHI | CGY/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.48 | 0.52 | 0.00 | 6.01 | 27.0/27.0 | 23.5/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.49 | 0.51 | 0.48 | 5.88 | 27.1/27.2 | 23.8/23.7 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.075 | 0.57 | 0.43 | 0.00 | 5.98 | 31.9/21.5 | 18.4/27.8 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.53 | 0.47 | 0.47 | 5.89 | 32.2/22.0 | 18.9/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.50 | 0.50 | 0.00 | 9.22 | 28.7/28.6 | 22.7/22.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.44 | 0.56 | 0.00 | 3.44 | 25.9/26.0 | 24.1/24.2 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Konecny: 1+ assists NO | 65 | 0.739 | 0.689 | +0.073 | +0.023 | $15.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Porter Martone: 1+ goals NO | 77 | 0.813 | 0.798 | +0.031 | +0.016 | $14.85 | FUNDED_RESEARCH | $4 | PHI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 9 | 0.116 | 0.107 | +0.020 | +0.011 | $2.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Martin Pospisil: 1+ goals YES | 11 | 0.137 | 0.128 | +0.020 | +0.011 | $2.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV08PHICGY-PHIPMARTONE94-1|no; why: higher confidence-adjusted growth (5.39 vs 0.02 bp); alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV08PHICGY-CGYMPOSPISIL76-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PHI offense succeeds (4+ goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no; why: second expression of the same thesis: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no has the higher standalone adjusted growth (5.39 vs 3.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.056); they share one thesis budget; relationships: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi 0.056); KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV08PHICGY-CGYMPOSPISIL76-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense succeeds (4+ goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PHICGY-CGYASUNIEV61-1|yes; why: higher confidence-adjusted growth (2.96 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0018 below the 0.010/contract floor; relationships: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV08PHICGY-CGYMPOSPISIL76-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CGY offense suppressed (<= 2 goals)
- **Martin Pospisil: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PHICGY-CGYASUNIEV61-1|yes; why: higher confidence-adjusted growth (2.53 vs 0.05 bp); alternative not eligible: confidence-adjusted EV +0.0018 below the 0.010/contract floor; relationships: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, CGY shot control · normal event (5-7) · decided (2+) 0.07.
- thesis PHI:SUPPRESSED (p 0.4273): highest fidelity KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3547): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3453, phi -0.216)
- KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3453, phi -0.182)
- KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4301, phi -0.168)
- KXNHLGOAL-26NOV08PHICGY-CGYMPOSPISIL76-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4301, phi -0.178)

portfolios: A EV +3.73 (adj +1.67) on $37.50, P(profit) 0.6945, adj growth 14.2 bp · B EV +3.30 (adj +1.42) on $35.60, P(profit) 0.6894, adj growth 12.6 bp · C EV +2.09 (adj +0.67) on $19.11, P(profit) 0.7386, adj growth 5.9 bp · R EV +0.16 (adj +0.08) on $4.00, P(profit) 0.813, adj growth 3.0 bp

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
| Alex Killorn: 1+ goals YES | 18 | 0.237 | 0.222 | +0.047 | +0.031 | $8.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Pittsburgh wins by over 1.5 goals NO | 71 | 0.805 | 0.755 | +0.080 | +0.030 | $20.00 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Kaedan Korczak: 1+ goals YES | 3 | 0.051 | 0.043 | +0.019 | +0.011 | $2.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 35 | 0.401 | 0.387 | +0.035 | +0.021 | $6.83 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes; why: higher confidence-adjusted growth (13.79 vs 12.60 bp); despite a smaller raw edge (+0.047 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.821 vs 0.329); relationships: KXNHLSPREAD-26NOV08PITANA-PIT2|no: MOSTLY_INDEPENDENT (phi 0.126); KXNHLGOAL-26NOV08PITANA-PITKKORCZAK6-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: ANA offense suppressed (<= 2 goals)
- **Pittsburgh wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes; why: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes has the higher standalone adjusted growth (12.60 vs 10.24 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.245); relationships: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.126); KXNHLGOAL-26NOV08PITANA-PITKKORCZAK6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.143); failure: PIT wins by 2+
- **Kaedan Korczak: 1+ goals YES** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26NOV08PITANA-PIT2|no: INTENTIONAL_DIVERSIFIER (phi -0.068); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: PIT offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes; why: Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.50 vs 0.20 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26NOV08PITANA-PIT2|no: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26NOV08PITANA-PITKKORCZAK6-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.13, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.5797): highest fidelity KXNHLSPREAD-26NOV08PITANA-PIT3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV08PITANA-PIT2|no — Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.50 vs 0.20 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis GAME:HIGH_EVENT (p 0.3995): highest fidelity KXNHLTEAMTOTAL-26NOV08PITANA-ANA5|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.6301): highest fidelity KXNHLSPREAD-26NOV08PITANA-PIT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV08PITANA-PIT2|no (same contract)
- KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2362, phi -0.175)
- KXNHLSPREAD-26NOV08PITANA-PIT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:WINS_BY_2PLUS (p 0.1953, phi -1.0)
- KXNHLGOAL-26NOV08PITANA-PITKKORCZAK6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4004, phi -0.1)
- KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2362, phi -0.24)
- override: Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.50 vs 0.20 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +10.61 (adj +3.57) on $37.50, P(profit) 0.456, adj growth 22.9 bp · B EV +6.38 (adj +3.47) on $37.68, P(profit) 0.526, adj growth 30.3 bp · C EV +6.87 (adj +3.11) on $32.56, P(profit) 0.3759, adj growth 27.3 bp · R EV +0.74 (adj +0.32) on $7.00, P(profit) 0.3503, adj growth 11.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
