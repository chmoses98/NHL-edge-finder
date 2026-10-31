# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T17:10:32Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +27.44 | +7.68 | +26.43 | 0.715 | -31.99 | -47.84 | 65.96 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +29.97 | +15.81 | +26.25 | 0.701 | -33.68 | -47.71 | 144.63 |
| C best expression per thesis | 125.07 | +25.45 | +10.97 | +22.56 | 0.653 | -41.88 | -55.22 | 95.12 |
| R FUNDED research stakes | 24.00 | +3.77 | +2.04 | -0.54 | 0.468 | -6.93 | -9.97 | 0.00 |

## TBL @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.392 / away 0.609

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_TBL_win | p_overtime | goals | shots NSH/TBL | NSH/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.48 | 0.52 | 0.00 | 6.0 | 27.3/27.8 | 24.2/23.6 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.111 | 0.40 | 0.60 | 0.00 | 5.97 | 21.6/33.3 | 29.0/18.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.51 | 0.49 | 0.48 | 5.96 | 27.5/28.0 | 24.7/24.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.44 | 0.56 | 0.48 | 5.88 | 22.0/33.6 | 30.2/18.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.46 | 0.54 | 0.00 | 9.29 | 29.1/29.5 | 23.5/23.2 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.068 | 0.39 | 0.61 | 0.00 | 9.22 | 22.9/35.0 | 27.6/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Charle-Edouard D'Astous: 1+ goals NO | 89 | 0.929 | 0.917 | +0.032 | +0.020 | $12.36 | FUNDED_RESEARCH | $4 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_STRONGER | D |
| Nils Hoglander: 1+ goals YES | 11 | 0.143 | 0.133 | +0.026 | +0.017 | $2.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 26 | 0.313 | 0.296 | +0.040 | +0.023 | $4.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 74 | 0.809 | 0.772 | +0.056 | +0.019 | $9.18 | FUNDED_RESEARCH | $3 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Charle-Edouard D'Astous: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TBNSH-TB3|no; why: higher confidence-adjusted growth (9.41 vs 4.09 bp); despite a smaller raw edge (+0.032 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31TBNSH-NSHNHOGLANDER21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.096); failure: TBL offense succeeds (4+ goals)
- **Nils Hoglander: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (5.74 vs 5.67 bp); despite a smaller raw edge (+0.026 vs +0.040/contract); relationships: KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.094); failure: NSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31TBNSH-TB3|no; why: higher confidence-adjusted growth (5.67 vs 4.09 bp); despite a smaller raw edge (+0.040 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31TBNSH-NSHNHOGLANDER21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.147); failure: NSH offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31TBNSH-TB2|no; why: Broad expression KXNHLSPREAD-26OCT31TBNSH-TB3|no selected over player prop KXNHLAST-26OCT31TBNSH-TBNKUCHEROV86-1|no because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: MOSTLY_INDEPENDENT (phi 0.096); KXNHLGOAL-26OCT31TBNSH-NSHNHOGLANDER21-1|yes: MOSTLY_INDEPENDENT (phi 0.094); KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.147); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NSH:OFFENSE_4PLUS (p 0.3613): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.3734): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB2|no — Broad expression KXNHLSPREAD-26OCT31TBNSH-TB3|no selected over player prop KXNHLAST-26OCT31TBNSH-TBNKUCHEROV86-1|no because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)
- thesis NSH:WINS (p 0.4644): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TBNSH-TB2|no (same contract)
- KXNHLGOAL-26OCT31TBNSH-TBCDASTOUS51-1|no: FUNDED_RESEARCH; family TRUSTED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4098, phi -0.122)
- KXNHLGOAL-26OCT31TBNSH-NSHNHOGLANDER21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4167, phi -0.186)
- KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4167, phi -0.281)
- KXNHLSPREAD-26OCT31TBNSH-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3117, phi -0.722)
- override: Broad expression KXNHLSPREAD-26OCT31TBNSH-TB3|no selected over player prop KXNHLAST-26OCT31TBNSH-TBNKUCHEROV86-1|no because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +3.83 (adj +0.66) on $21.92, P(profit) 0.6718, adj growth 5.7 bp · B EV +2.29 (adj +1.20) on $28.24, P(profit) 0.3928, adj growth 11.2 bp · C EV +2.31 (adj +1.00) on $24.75, P(profit) 0.2802, adj growth 8.8 bp · R EV +0.36 (adj +0.16) on $7.00, P(profit) 0.7612, adj growth 6.1 bp

## EDM @ NYI  ·  10000 joint draws  ·  424 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.490 / away 0.510

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_EDM_win | p_overtime | goals | shots NYI/EDM | NYI/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.45 | 0.55 | 0.00 | 6.07 | 27.5/27.5 | 23.7/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.112 | 0.50 | 0.50 | 0.00 | 9.43 | 29.3/29.2 | 22.9/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.50 | 0.50 | 0.49 | 5.99 | 27.7/27.6 | 24.2/24.3 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.073 | 0.52 | 0.48 | 0.00 | 6.02 | 32.4/22.0 | 18.6/28.5 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.53 | 0.47 | 0.50 | 6.02 | 32.4/22.1 | 18.7/28.8 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.061 | 0.44 | 0.56 | 0.00 | 6.06 | 21.9/32.1 | 27.9/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mattias Ekholm: 1+ goals YES | 6 | 0.114 | 0.096 | +0.050 | +0.032 | $4.47 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 13 | 0.178 | 0.165 | +0.041 | +0.027 | $4.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 34 | 0.460 | 0.379 | +0.104 | +0.023 | $7.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.68) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 26 | 0.302 | 0.290 | +0.028 | +0.017 | $4.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: higher confidence-adjusted growth (36.43 vs 5.14 bp); despite a smaller raw edge (+0.050 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.863 vs 0.371); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.102); KXNHLGOAL-26OCT31EDMNYI-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: higher confidence-adjusted growth (13.36 vs 5.14 bp); despite a smaller raw edge (+0.041 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.864 vs 0.371); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT31EDMNYI-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (5.07 vs 3.39 bp); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.102); KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT31EDMNYI-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.229); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: KXNHLTOTAL-26OCT31EDMNYI-9|yes has the higher standalone adjusted growth (5.14 vs 3.00 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.132); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.229); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4461): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-7|yes (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.42): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-7|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.3287): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-7|yes (same contract)
- KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3438, phi -0.149)
- KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3438, phi -0.171)
- KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 32% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.5 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4461, phi -0.309)
- KXNHLGOAL-26OCT31EDMNYI-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3438, phi -0.253)

portfolios: A EV +4.09 (adj +1.01) on $21.92, P(profit) 0.661, adj growth 9.2 bp · B EV +7.58 (adj +3.96) on $21.71, P(profit) 0.6227, adj growth 35.9 bp · C EV +4.76 (adj +1.30) on $16.50, P(profit) 0.6324, adj growth 11.3 bp · R EV +1.55 (adj +1.01) on $2.00, P(profit) 0.1135, adj growth 33.1 bp

## BUF @ LAK  ·  10000 joint draws  ·  518 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.457 / away 0.543

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BUF_win | p_overtime | goals | shots LAK/BUF | LAK/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 6.02 | 27.9/27.9 | 24.7/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.48 | 5.9 | 28.1/28.2 | 24.8/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.57 | 0.43 | 0.00 | 9.19 | 29.2/29.3 | 23.8/22.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.072 | 0.65 | 0.35 | 0.00 | 6.03 | 32.7/22.2 | 19.5/28.1 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.066 | 0.51 | 0.49 | 0.00 | 5.99 | 22.4/32.9 | 29.4/19.1 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.51 | 0.49 | 0.42 | 5.95 | 32.9/22.4 | 19.1/29.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Andre Lee: 1+ goals YES | 9 | 0.125 | 0.115 | +0.029 | +0.019 | $2.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.080 | 0.067 | +0.027 | +0.014 | $1.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 1.5 goals NO | 68 | 0.765 | 0.720 | +0.069 | +0.025 | $10.84 | FUNDED_RESEARCH | $3 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Rasmus Dahlin: 1+ goals NO | 81 | 0.844 | 0.833 | +0.024 | +0.013 | $8.35 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF2|no; why: higher confidence-adjusted growth (8.97 vs 6.27 bp); despite a smaller raw edge (+0.029 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT31BUFLA-BUF2|no: MOSTLY_INDEPENDENT (phi 0.09); KXNHLGOAL-26OCT31BUFLA-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.032); failure: LAK offense suppressed (<= 2 goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLSPREAD-26OCT31BUFLA-BUF2|no; why: higher confidence-adjusted growth (8.37 vs 6.27 bp); despite a smaller raw edge (+0.027 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT31BUFLA-BUF2|no: MOSTLY_INDEPENDENT (phi 0.061); KXNHLGOAL-26OCT31BUFLA-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: LAK offense suppressed (<= 2 goals)
- **Buffalo wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF3|no; why: higher confidence-adjusted growth (6.27 vs 3.57 bp); relationships: KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.09); KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.061); KXNHLGOAL-26OCT31BUFLA-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.134); failure: BUF wins by 2+
- **Rasmus Dahlin: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31BUFLA-BUF2|no has the higher standalone adjusted growth (6.27 vs 2.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.134); they share one thesis budget; relationships: KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.032); KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26OCT31BUFLA-BUF2|no: MOSTLY_INDEPENDENT (phi 0.134); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.4171): highest fidelity KXNHLTEAMTOTAL-26OCT31BUFLA-LA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS_BY_2PLUS (p 0.3205): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no (same contract)
- thesis LAK:WINS (p 0.5446): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no (same contract)
- KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3693, phi -0.15)
- KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3693, phi -0.122)
- KXNHLSPREAD-26OCT31BUFLA-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2354, phi -1.0)
- KXNHLGOAL-26OCT31BUFLA-BUFRDAHLIN26-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3397, phi -0.195)

portfolios: A EV +2.47 (adj +0.74) on $21.92, P(profit) 0.4744, adj growth 5.9 bp · B EV +3.05 (adj +1.53) on $23.73, P(profit) 0.7128, adj growth 14.0 bp · C EV +2.00 (adj +0.71) on $20.00, P(profit) 0.7646, adj growth 6.3 bp · R EV +0.39 (adj +0.15) on $6.00, P(profit) 0.6662, adj growth 5.6 bp

## OTT @ SJS  ·  10000 joint draws  ·  444 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.423 / away 0.577

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_OTT_win | p_overtime | goals | shots SJS/OTT | SJS/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.49 | 0.51 | 0.00 | 6.03 | 27.0/27.3 | 23.7/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.46 | 6.01 | 27.1/27.5 | 24.0/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.51 | 0.49 | 0.00 | 9.44 | 28.6/28.8 | 22.6/22.4 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.091 | 0.46 | 0.54 | 0.00 | 6.03 | 21.5/32.4 | 28.6/18.3 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.44 | 0.56 | 0.44 | 5.89 | 21.6/32.6 | 28.9/18.4 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.064 | 0.45 | 0.55 | 0.00 | 9.37 | 22.9/33.9 | 26.9/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Gaudette: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $3.23 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Tyler Toffoli: 1+ assists YES | 24 | 0.325 | 0.277 | +0.072 | +0.025 | $4.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Adam Gaudette: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (7.48 vs 7.00 bp); despite a smaller raw edge (+0.031 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.063); failure: SJS offense suppressed (<= 2 goals)
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes has the higher standalone adjusted growth (7.48 vs 7.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.063); they share one thesis budget; relationships: KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.063); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4099): highest fidelity KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes (same contract)
- KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.201)
- KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.254)

portfolios: A EV +3.41 (adj +1.44) on $12.76, P(profit) 0.4282, adj growth 12.4 bp · B EV +1.96 (adj +0.90) on $7.53, P(profit) 0.4282, adj growth 8.2 bp · C EV +1.26 (adj +0.81) on $5.52, P(profit) 0.1693, adj growth 7.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ MTL  ·  10000 joint draws  ·  504 bet sides mapped, 2 +EV candidates, 2 on card

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
| Blake Lizotte: 1+ goals YES | 9 | 0.121 | 0.111 | +0.025 | +0.015 | $2.29 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 13 | 0.159 | 0.149 | +0.021 | +0.011 | $1.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (5.50 vs 2.41 bp); relationships: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: MTL wins (incl. OT/SO)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (2.41 vs 0.86 bp); despite a smaller raw edge (+0.021 vs +0.022/contract); alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.023); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4051): highest fidelity KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes (same contract)
- KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:WINS (p 0.5282, phi -0.172)
- KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3817, phi -0.201)

portfolios: A EV +1.21 (adj +0.70) on $5.74, P(profit) 0.258, adj growth 6.2 bp · B EV +0.89 (adj +0.51) on $4.17, P(profit) 0.258, adj growth 4.7 bp · C EV +0.49 (adj +0.26) on $3.14, P(profit) 0.1592, adj growth 2.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ VAN  ·  10000 joint draws  ·  418 bet sides mapped, 19 +EV candidates, 4 on card

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
| Linus Karlsson: 1+ goals YES | 19 | 0.269 | 0.247 | +0.069 | +0.046 | $8.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 18 | 0.247 | 0.226 | +0.056 | +0.036 | $6.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 72 | 0.784 | 0.764 | +0.050 | +0.030 | $12.36 | FUNDED_RESEARCH | $4 | TOR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 16 | 0.211 | 0.194 | +0.042 | +0.024 | $3.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (28.62 vs 18.03 bp); relationships: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (28.62 vs 18.03 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: VAN offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes; why: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes has the higher standalone adjusted growth (12.30 vs 10.12 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.119); relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: TOR offense succeeds (4+ goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (28.62 vs 8.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4305): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLSPREAD-26OCT31TORVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3557): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31TORVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.239)
- KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.223)
- KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4235, phi -0.203)
- KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.212)

portfolios: A EV +5.34 (adj +1.44) on $21.92, P(profit) 0.4991, adj growth 12.2 bp · B EV +6.42 (adj +4.11) on $30.62, P(profit) 0.5372, adj growth 37.7 bp · C EV +6.35 (adj +3.67) on $18.11, P(profit) 0.4368, adj growth 31.6 bp · R EV +0.27 (adj +0.16) on $4.00, P(profit) 0.7837, adj growth 6.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT31TORVAN-VAN|yes == KXNHLGAME-26OCT31TORVAN-TOR|no

## CBJ @ DAL  ·  10000 joint draws  ·  436 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.631 / away 0.369

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_CBJ_win | p_overtime | goals | shots DAL/CBJ | DAL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.55 | 0.45 | 0.00 | 6.03 | 26.1/25.8 | 22.6/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.53 | 0.47 | 0.45 | 5.88 | 26.3/26.0 | 22.8/23.1 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.089 | 0.63 | 0.37 | 0.00 | 5.98 | 31.0/20.6 | 17.8/26.8 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.55 | 0.46 | 0.47 | 5.9 | 31.2/20.8 | 17.6/28.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.57 | 0.43 | 0.00 | 9.25 | 27.7/27.4 | 21.6/21.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.066 | 0.52 | 0.48 | 0.00 | 3.48 | 24.9/24.7 | 22.9/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 13 | 0.187 | 0.169 | +0.049 | +0.031 | $4.87 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ryan Lomberg: 1+ goals YES | 5 | 0.077 | 0.069 | +0.024 | +0.016 | $2.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 20 | 0.253 | 0.235 | +0.042 | +0.024 | $4.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Dallas wins by over 1.5 goals NO | 61 | 0.689 | 0.647 | +0.062 | +0.020 | $3.96 | FUNDED_RESEARCH | $1 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (17.39 vs 7.40 bp); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26OCT31CBJDAL-DAL2|no: MOSTLY_INDEPENDENT (phi 0.145); failure: CBJ offense suppressed (<= 2 goals)
- **Ryan Lomberg: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (17.39 vs 10.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT31CBJDAL-DAL2|no: MOSTLY_INDEPENDENT (phi 0.083); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (17.39 vs 7.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT31CBJDAL-DAL2|no: MOSTLY_INDEPENDENT (phi 0.143); failure: CBJ offense suppressed (<= 2 goals)
- **Dallas wins by over 1.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ4|yes; why: higher confidence-adjusted growth (3.92 vs 2.73 bp); wins across more scripts (relative breadth 0.89 vs 0.749); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.145); KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.143); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3192): highest fidelity KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.2429): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS (p 0.4582): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL2|no (same contract)
- KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4629, phi -0.234)
- KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4629, phi -0.137)
- KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4629, phi -0.249)
- KXNHLSPREAD-26OCT31CBJDAL-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3108, phi -1.0)

portfolios: A EV +2.69 (adj +0.79) on $21.92, P(profit) 0.5047, adj growth 6.4 bp · B EV +3.93 (adj +2.34) on $15.19, P(profit) 0.441, adj growth 21.3 bp · C EV +3.82 (adj +2.09) on $18.43, P(profit) 0.187, adj growth 18.0 bp · R EV +0.81 (adj +0.48) on $3.00, P(profit) 0.187, adj growth 16.7 bp

## CGY @ COL  ·  10000 joint draws  ·  448 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.777 / away 0.223

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_CGY_win | p_overtime | goals | shots COL/CGY | COL/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.148 | 0.80 | 0.20 | 0.00 | 6.05 | 35.4/22.7 | 20.5/30.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.124 | 0.82 | 0.18 | 0.00 | 9.4 | 37.5/24.1 | 20.2/28.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.76 | 0.24 | 0.00 | 6.02 | 30.0/29.0 | 26.4/25.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.60 | 0.40 | 0.49 | 6.01 | 36.2/23.3 | 20.1/32.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.78 | 0.22 | 0.00 | 9.41 | 31.3/30.4 | 25.8/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.54 | 0.46 | 0.48 | 6.02 | 29.8/29.0 | 25.8/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jonathan Castagna: 1+ goals YES | 8 | 0.111 | 0.101 | +0.026 | +0.016 | $2.34 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Colorado wins by over 2.5 goals NO | 53 | 0.654 | 0.570 | +0.106 | +0.023 | $7.55 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Maxim Tsyplakov: 1+ goals YES | 7 | 0.094 | 0.086 | +0.019 | +0.011 | $1.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Mackenzie Blackwood: 22+ saves YES | 50 | 0.605 | 0.537 | +0.088 | +0.019 | $7.35 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | COL:NET_HIGH_VOLUME | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT31CGYCOL-COL|no; why: higher confidence-adjusted growth (6.89 vs 6.30 bp); despite a smaller raw edge (+0.026 vs +0.081/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLSPREAD-26OCT31CGYCOL-COL3|no: MOSTLY_INDEPENDENT (phi 0.078); KXNHLGOAL-26OCT31CGYCOL-CGYMTSYPLAKOV72-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSAVE-26OCT31CGYCOL-COLMBLACKWOOD39-22|yes: MOSTLY_INDEPENDENT (phi -0.038); failure: CGY offense suppressed (<= 2 goals)
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLGAME-26OCT31CGYCOL-COL|no; why: KXNHLGAME-26OCT31CGYCOL-COL|no has the higher standalone adjusted growth (6.30 vs 4.55 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.479); relationships: KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.078); KXNHLGOAL-26OCT31CGYCOL-CGYMTSYPLAKOV72-1|yes: MOSTLY_INDEPENDENT (phi 0.09); KXNHLSAVE-26OCT31CGYCOL-COLMBLACKWOOD39-22|yes: INTENTIONAL_DIVERSIFIER (phi -0.074); failure: COL wins by 2+
- **Maxim Tsyplakov: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT31CGYCOL-COL|no; why: KXNHLGAME-26OCT31CGYCOL-COL|no has the higher standalone adjusted growth (6.30 vs 3.79 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.101); relationships: KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26OCT31CGYCOL-COL3|no: MOSTLY_INDEPENDENT (phi 0.09); KXNHLSAVE-26OCT31CGYCOL-COLMBLACKWOOD39-22|yes: MOSTLY_INDEPENDENT (phi -0.03); failure: CGY offense suppressed (<= 2 goals)
- **Mackenzie Blackwood: 22+ saves YES** — thesis: COL net faces heavy volume (33+ shots; CGY pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLSPREAD-26OCT31CGYCOL-COL3|no: INTENTIONAL_DIVERSIFIER (phi -0.074); KXNHLGOAL-26OCT31CGYCOL-CGYMTSYPLAKOV72-1|yes: MOSTLY_INDEPENDENT (phi -0.03); failure: COL net faces light volume (<= 25 shots; CGY suppressed)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CGY:OFFENSE_4PLUS (p 0.2764): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS (p 0.3025): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL3|no (same contract)
- thesis GAME:TIGHT (p 0.3759): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CGYCOL-COL3|no (same contract)
- KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5083, phi -0.159)
- KXNHLSPREAD-26OCT31CGYCOL-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.9 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.484, phi -0.751)
- KXNHLGOAL-26OCT31CGYCOL-CGYMTSYPLAKOV72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5083, phi -0.143)
- KXNHLSAVE-26OCT31CGYCOL-COLMBLACKWOOD39-22|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.5 pts; fragile player expression; opposing: failure thesis COL:NET_LOW_VOLUME (p 0.4686, phi -0.734)

portfolios: A EV +4.41 (adj +0.90) on $21.92, P(profit) 0.6112, adj growth 7.9 bp · B EV +3.85 (adj +1.26) on $18.81, P(profit) 0.4926, adj growth 11.5 bp · C EV +4.48 (adj +1.13) on $18.62, P(profit) 0.7497, adj growth 9.8 bp · R EV +0.39 (adj +0.08) on $2.00, P(profit) 0.6539, adj growth 3.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
