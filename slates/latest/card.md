# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T17:38:32Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +25.55 | +7.12 | +24.33 | 0.715 | -29.10 | -43.27 | 61.83 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +27.37 | +14.88 | +24.48 | 0.698 | -31.84 | -44.98 | 137.35 |
| C best expression per thesis | 148.42 | +27.99 | +12.48 | +24.83 | 0.673 | -43.12 | -58.74 | 108.81 |
| R FUNDED research stakes | 26.00 | +3.36 | +1.87 | +1.29 | 0.556 | -6.69 | -8.92 | 0.00 |

## TBL @ NSH  ·  10000 joint draws  ·  418 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.392 / away 0.609

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_TBL_win | p_overtime | goals | shots NSH/TBL | NSH/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.47 | 0.53 | 0.00 | 6.02 | 27.3/27.7 | 24.0/24.0 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.109 | 0.40 | 0.60 | 0.00 | 5.98 | 21.9/33.4 | 29.1/18.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.53 | 0.47 | 0.46 | 5.92 | 27.6/28.1 | 24.9/24.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.45 | 0.55 | 0.45 | 5.95 | 21.9/33.3 | 29.9/18.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.51 | 0.49 | 0.00 | 9.27 | 28.9/29.5 | 23.4/22.7 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.068 | 0.37 | 0.63 | 0.00 | 9.25 | 23.1/34.9 | 27.5/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay over 3.5 goals scored NO | 50 | 0.590 | 0.543 | +0.073 | +0.025 | $7.01 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ryan O'Reilly: 1+ goals YES | 26 | 0.308 | 0.295 | +0.034 | +0.021 | $3.87 | FUNDED_RESEARCH | $1 | NSH:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 74 | 0.803 | 0.769 | +0.050 | +0.016 | $1.15 | FUNDED_RESEARCH | $1 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nils Hoglander: 1+ goals YES | 11 | 0.140 | 0.128 | +0.023 | +0.011 | $1.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Tampa Bay over 3.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TBNSH-TB2|no; why: higher confidence-adjusted growth (5.54 vs 4.66 bp); relationships: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26OCT31TBNSH-TB3|no: REINFORCING (phi 0.501); KXNHLGOAL-26OCT31TBNSH-NSHNHOGLANDER21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: TBL offense succeeds (4+ goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31TBNSH-TB2|no; why: higher confidence-adjusted growth (4.92 vs 4.66 bp); despite a smaller raw edge (+0.034 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLTEAMTOTAL-26OCT31TBNSH-TB4|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.148); KXNHLGOAL-26OCT31TBNSH-NSHNHOGLANDER21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: NSH offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT31TBNSH-TB4|no; why: Broad expression KXNHLSPREAD-26OCT31TBNSH-TB3|no selected over player prop KXNHLAST-26OCT31TBNSH-TBNKUCHEROV86-1|no because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLTEAMTOTAL-26OCT31TBNSH-TB4|no: REINFORCING (phi 0.501); KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.148); KXNHLGOAL-26OCT31TBNSH-NSHNHOGLANDER21-1|yes: MOSTLY_INDEPENDENT (phi 0.085); failure: TBL wins by 2+
- **Nils Hoglander: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes has the higher standalone adjusted growth (4.92 vs 2.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT31TBNSH-TB4|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT31TBNSH-TB3|no: MOSTLY_INDEPENDENT (phi 0.085); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TBL:SUPPRESSED (p 0.379): highest fidelity KXNHLTEAMTOTAL-26OCT31TBNSH-TB4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31TBNSH-TB4|no (same contract)
- thesis NSH:WINS (p 0.4672): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31TBNSH-TB4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS_BY_2PLUS (p 0.2502): highest fidelity KXNHLSPREAD-26OCT31TBNSH-TB2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31TBNSH-TB4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT31TBNSH-TB4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3998, phi -0.98)
- KXNHLGOAL-26OCT31TBNSH-NSHROREILLY90-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.428, phi -0.26)
- KXNHLSPREAD-26OCT31TBNSH-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3071, phi -0.744)
- KXNHLGOAL-26OCT31TBNSH-NSHNHOGLANDER21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.428, phi -0.185)
- override: Broad expression KXNHLSPREAD-26OCT31TBNSH-TB3|no selected over player prop KXNHLAST-26OCT31TBNSH-TBNKUCHEROV86-1|no because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +3.64 (adj +0.69) on $19.38, P(profit) 0.6436, adj growth 6.1 bp · B EV +1.87 (adj +0.81) on $13.62, P(profit) 0.7244, adj growth 7.5 bp · C EV +2.72 (adj +1.18) on $20.03, P(profit) 0.7135, adj growth 10.3 bp · R EV +0.47 (adj +0.20) on $4.00, P(profit) 0.6618, adj growth 7.2 bp

## EDM @ NYI  ·  10000 joint draws  ·  424 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.499 / away 0.501

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
| Mattias Ekholm: 1+ goals YES | 6 | 0.114 | 0.098 | +0.050 | +0.034 | $4.24 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 12 | 0.178 | 0.163 | +0.051 | +0.035 | $5.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 34 | 0.460 | 0.379 | +0.104 | +0.023 | $7.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.68) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 26 | 0.302 | 0.290 | +0.028 | +0.017 | $4.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: higher confidence-adjusted growth (39.22 vs 5.14 bp); despite a smaller raw edge (+0.050 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.863 vs 0.371); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.102); KXNHLGOAL-26OCT31EDMNYI-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: EDM offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: higher confidence-adjusted growth (23.77 vs 5.14 bp); despite a smaller raw edge (+0.051 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.864 vs 0.371); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT31EDMNYI-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT31EDMNYI-EDMRNUGENTHOPKINS93-1|no; why: higher confidence-adjusted growth (5.07 vs 3.62 bp); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.102); KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT31EDMNYI-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.229); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT31EDMNYI-9|yes; why: KXNHLTOTAL-26OCT31EDMNYI-9|yes has the higher standalone adjusted growth (5.14 vs 3.00 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.132); relationships: KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.229); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4461): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-7|yes (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.42): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-7|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.3287): highest fidelity KXNHLTOTAL-26OCT31EDMNYI-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT31EDMNYI-7|yes (same contract)
- KXNHLGOAL-26OCT31EDMNYI-EDMMEKHOLM14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3438, phi -0.149)
- KXNHLGOAL-26OCT31EDMNYI-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3438, phi -0.171)
- KXNHLAST-26OCT31EDMNYI-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 32% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.5 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4461, phi -0.309)
- KXNHLGOAL-26OCT31EDMNYI-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3438, phi -0.253)

portfolios: A EV +3.77 (adj +0.96) on $19.38, P(profit) 0.635, adj growth 9.0 bp · B EV +7.88 (adj +4.38) on $20.97, P(profit) 0.3353, adj growth 40.0 bp · C EV +4.76 (adj +1.30) on $16.50, P(profit) 0.6324, adj growth 11.3 bp · R EV +1.55 (adj +1.05) on $2.00, P(profit) 0.1135, adj growth 34.7 bp

## BUF @ LAK  ·  10000 joint draws  ·  518 bet sides mapped, 11 +EV candidates, 4 on card

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
| Andre Lee: 1+ goals YES | 9 | 0.125 | 0.115 | +0.029 | +0.019 | $2.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.080 | 0.067 | +0.027 | +0.014 | $1.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 1.5 goals NO | 68 | 0.765 | 0.720 | +0.069 | +0.025 | $9.82 | FUNDED_RESEARCH | $3 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Rasmus Dahlin: 1+ goals NO | 81 | 0.844 | 0.833 | +0.024 | +0.013 | $7.57 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
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

portfolios: A EV +2.18 (adj +0.65) on $19.38, P(profit) 0.4744, adj growth 5.4 bp · B EV +2.76 (adj +1.39) on $21.51, P(profit) 0.7128, adj growth 12.8 bp · C EV +2.00 (adj +0.71) on $20.00, P(profit) 0.7646, adj growth 6.3 bp · R EV +0.36 (adj +0.14) on $5.00, P(profit) 0.6662, adj growth 5.1 bp

## OTT @ SJS  ·  10000 joint draws  ·  444 bet sides mapped, 3 +EV candidates, 3 on card

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
| Tyler Toffoli: 1+ assists YES | 24 | 0.325 | 0.280 | +0.072 | +0.027 | $4.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Adam Gaudette: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $2.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ goals NO | 79 | 0.824 | 0.814 | +0.022 | +0.013 | $9.98 | FUNDED_RESEARCH | $3 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes; why: higher confidence-adjusted growth (8.49 vs 7.48 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.063); KXNHLGOAL-26OCT31OTTSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.045); failure: SJS offense suppressed (<= 2 goals)
- **Adam Gaudette: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes has the higher standalone adjusted growth (8.49 vs 7.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.063); they share one thesis budget; relationships: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.063); KXNHLGOAL-26OCT31OTTSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT31OTTSJ-SJMCELEBRINI71-2|no; why: higher confidence-adjusted growth (2.24 vs 0.14 bp); despite a smaller raw edge (+0.022 vs +0.080/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4099): highest fidelity KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3765): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.254)
- KXNHLGOAL-26OCT31OTTSJ-SJAGAUDETTE81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3765, phi -0.201)
- KXNHLGOAL-26OCT31OTTSJ-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4099, phi -0.193)

portfolios: A EV +3.23 (adj +1.48) on $19.03, P(profit) 0.4282, adj growth 13.1 bp · B EV +2.21 (adj +1.06) on $17.33, P(profit) 0.4282, adj growth 9.9 bp · C EV +2.34 (adj +0.88) on $8.22, P(profit) 0.3249, adj growth 7.7 bp · R EV +0.08 (adj +0.05) on $3.00, P(profit) 0.8241, adj growth 1.7 bp

## PIT @ MTL  ·  10000 joint draws  ·  504 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.533 / away 0.467

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
| Blake Lizotte: 1+ goals YES | 9 | 0.121 | 0.107 | +0.025 | +0.011 | $1.54 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 13 | 0.159 | 0.149 | +0.021 | +0.011 | $1.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Zachary Bolduc: 1+ assists YES | 24 | 0.303 | 0.266 | +0.050 | +0.014 | $2.42 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_MIXED | D |
| Rickard Rakell: 1+ goals YES | 30 | 0.337 | 0.326 | +0.022 | +0.012 | $2.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (3.09 vs 2.41 bp); relationships: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi -0.041); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: MTL wins (incl. OT/SO)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (2.41 vs 1.39 bp); despite a smaller raw edge (+0.021 vs +0.022/contract); relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: PIT offense suppressed (<= 2 goals)
- **Zachary Bolduc: 1+ assists YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes; why: higher confidence-adjusted growth (2.14 vs 1.12 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.041); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: MTL offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes has the higher standalone adjusted growth (2.41 vs 1.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4051): highest fidelity KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4375): highest fidelity KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes (same contract)
- KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:WINS (p 0.5282, phi -0.172)
- KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3817, phi -0.201)
- KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3469, phi -0.243)
- KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3817, phi -0.243)

portfolios: A EV +2.58 (adj +0.98) on $14.70, P(profit) 0.4871, adj growth 8.4 bp · B EV +1.31 (adj +0.54) on $7.98, P(profit) 0.4871, adj growth 5.0 bp · C EV +1.31 (adj +0.49) on $7.31, P(profit) 0.4133, adj growth 4.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ VAN  ·  10000 joint draws  ·  418 bet sides mapped, 20 +EV candidates, 4 on card

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
| Linus Karlsson: 1+ goals YES | 19 | 0.269 | 0.248 | +0.069 | +0.048 | $7.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 71 | 0.784 | 0.763 | +0.059 | +0.038 | $11.20 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 18 | 0.247 | 0.224 | +0.056 | +0.033 | $5.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 16 | 0.211 | 0.194 | +0.042 | +0.024 | $3.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (30.17 vs 15.63 bp); relationships: KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: VAN offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes; why: higher confidence-adjusted growth (16.30 vs 12.30 bp); despite a smaller raw edge (+0.059 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.015 vs 0.522); relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: TOR offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (30.17 vs 15.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: VAN offense suppressed (<= 2 goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (30.17 vs 8.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4305): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLSPREAD-26OCT31TORVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3557): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.239)
- KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4235, phi -0.203)
- KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.223)
- KXNHLGOAL-26OCT31TORVAN-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.212)

portfolios: A EV +3.49 (adj +0.60) on $19.38, P(profit) 0.6466, adj growth 5.3 bp · B EV +5.93 (adj +3.81) on $27.56, P(profit) 0.5372, adj growth 35.3 bp · C EV +7.87 (adj +4.81) on $37.82, P(profit) 0.4143, adj growth 42.1 bp · R EV +0.25 (adj +0.16) on $3.00, P(profit) 0.7837, adj growth 6.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT31TORVAN-VAN|yes == KXNHLGAME-26OCT31TORVAN-TOR|no

## CBJ @ DAL  ·  10000 joint draws  ·  452 bet sides mapped, 9 +EV candidates, 4 on card

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
| Mathieu Olivier: 1+ goals YES | 13 | 0.187 | 0.169 | +0.049 | +0.031 | $4.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 20 | 0.253 | 0.235 | +0.042 | +0.024 | $3.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Dallas wins by over 1.5 goals NO | 61 | 0.689 | 0.647 | +0.062 | +0.020 | $3.84 | FUNDED_RESEARCH | $1 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mikko Rantanen: 1+ goals NO | 69 | 0.732 | 0.718 | +0.027 | +0.013 | $5.24 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (17.39 vs 7.40 bp); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26OCT31CBJDAL-DAL2|no: MOSTLY_INDEPENDENT (phi 0.145); KXNHLGOAL-26OCT31CBJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.023); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (17.39 vs 7.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26OCT31CBJDAL-DAL2|no: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26OCT31CBJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: CBJ offense suppressed (<= 2 goals)
- **Dallas wins by over 1.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ4|yes; why: higher confidence-adjusted growth (3.92 vs 2.73 bp); wins across more scripts (relative breadth 0.89 vs 0.749); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.145); KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26OCT31CBJDAL-DALMRANTANEN96-1|no: REINFORCING (phi 0.155); failure: DAL wins by 2+
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31CBJDAL-DAL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT31CBJDAL-DAL2|no has the higher standalone adjusted growth (3.92 vs 1.76 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.155); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26OCT31CBJDAL-DAL2|no: REINFORCING (phi 0.155); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3192): highest fidelity KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.2429): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS (p 0.4582): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31CBJDAL-DAL2|no (same contract)
- KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4629, phi -0.234)
- KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4629, phi -0.249)
- KXNHLSPREAD-26OCT31CBJDAL-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3108, phi -1.0)
- KXNHLGOAL-26OCT31CBJDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3804, phi -0.236)

portfolios: A EV +2.38 (adj +0.68) on $19.38, P(profit) 0.5047, adj growth 5.5 bp · B EV +2.90 (adj +1.64) on $17.26, P(profit) 0.394, adj growth 15.1 bp · C EV +3.82 (adj +2.09) on $18.43, P(profit) 0.187, adj growth 18.0 bp · R EV +0.18 (adj +0.07) on $3.00, P(profit) 0.5363, adj growth 2.6 bp

## CGY @ COL  ·  10000 joint draws  ·  448 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.777 / away 0.223

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_CGY_win | p_overtime | goals | shots COL/CGY | COL/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.155 | 0.79 | 0.21 | 0.00 | 6.01 | 35.7/22.8 | 20.5/30.2 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.119 | 0.80 | 0.20 | 0.00 | 9.38 | 37.3/24.1 | 20.0/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.76 | 0.24 | 0.00 | 6.05 | 29.8/29.1 | 26.7/24.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.62 | 0.38 | 0.51 | 5.95 | 36.0/22.9 | 19.8/32.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.78 | 0.22 | 0.00 | 9.41 | 31.4/30.5 | 26.1/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.57 | 0.43 | 0.43 | 5.99 | 29.9/29.1 | 25.8/26.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Calgary over 1.5 goals scored YES | 64 | 0.729 | 0.682 | +0.073 | +0.026 | $8.25 | FUNDED_RESEARCH | $3 | CGY:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Aydar Suniev: 1+ goals YES | 15 | 0.193 | 0.178 | +0.034 | +0.019 | $2.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 8 | 0.110 | 0.100 | +0.025 | +0.015 | $1.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ goals NO | 75 | 0.799 | 0.784 | +0.036 | +0.021 | $11.20 | FUNDED_RESEARCH | $3 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
- **Calgary over 1.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes; why: higher confidence-adjusted growth (6.59 vs 6.25 bp); relationships: KXNHLGOAL-26OCT31CGYCOL-CGYASUNIEV61-1|yes: REINFORCING (phi 0.208); KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: REINFORCING (phi 0.158); KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: CGY offense suppressed (<= 2 goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes has the higher standalone adjusted growth (6.59 vs 6.10 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.208); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes: REINFORCING (phi 0.208); KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CGY offense suppressed (<= 2 goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes has the higher standalone adjusted growth (6.59 vs 6.02 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.158); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes: REINFORCING (phi 0.158); KXNHLGOAL-26OCT31CGYCOL-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: CGY offense suppressed (<= 2 goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT31CGYCOL-COL|no; why: KXNHLGAME-26OCT31CGYCOL-COL|no has the higher standalone adjusted growth (5.84 vs 5.36 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.135); relationships: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT31CGYCOL-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12.
- thesis CGY:OFFENSE_4PLUS (p 0.2792): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes (same contract)
- thesis CGY:WINS (p 0.3004): highest fidelity KXNHLGAME-26OCT31CGYCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS_BY_2PLUS (p 0.1445): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes (same contract)
- KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:SUPPRESSED (p 0.5138, phi -0.593)
- KXNHLGOAL-26OCT31CGYCOL-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5138, phi -0.224)
- KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5138, phi -0.174)
- KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5694, phi -0.164)

portfolios: A EV +4.28 (adj +1.08) on $19.38, P(profit) 0.5155, adj growth 8.9 bp · B EV +2.50 (adj +1.25) on $23.76, P(profit) 0.6525, adj growth 11.7 bp · C EV +3.18 (adj +1.02) on $20.11, P(profit) 0.7293, adj growth 8.9 bp · R EV +0.47 (adj +0.20) on $6.00, P(profit) 0.583, adj growth 7.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
