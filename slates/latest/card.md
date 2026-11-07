# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-07T16:08:15Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +30.27 | +10.53 | +28.74 | 0.780 | -16.99 | -29.51 | 98.03 |
| B thesis-diversified (joint) ← optimiser card | 149.02 | +31.49 | +19.55 | +25.00 | 0.731 | -23.88 | -35.91 | 174.24 |
| C best expression per thesis | 150.01 | +24.29 | +11.70 | +22.44 | 0.723 | -24.57 | -36.43 | 109.57 |
| R FUNDED research stakes | 23.00 | +4.57 | +3.55 | +1.24 | 0.573 | -6.32 | -8.34 | 0.00 |

## FLA @ WSH  ·  10000 joint draws  ·  452 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_FLA_win | p_overtime | goals | shots WSH/FLA | WSH/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.63 | 0.37 | 0.00 | 6.04 | 26.9/27.3 | 24.2/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.46 | 5.89 | 26.7/26.9 | 23.7/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.63 | 0.37 | 0.00 | 9.39 | 28.5/28.6 | 23.2/21.4 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.076 | 0.56 | 0.44 | 0.00 | 6.01 | 21.6/31.7 | 28.2/18.0 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.49 | 0.51 | 0.46 | 5.9 | 21.3/31.7 | 28.3/18.1 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.065 | 0.66 | 0.34 | 0.00 | 6.01 | 31.4/21.5 | 18.8/27.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anton Lundell: First Goalscorer YES | 1 | 0.032 | 0.036 | +0.021 | +0.025 | $2.16 | FUNDED_RESEARCH | $1 | FLA:SCORES_FIRST | FRAGILE (0.07) | EVIDENCE_MIXED | D |
| Aliaksei Protas: 1+ goals YES | 18 | 0.245 | 0.228 | +0.055 | +0.037 | $4.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 17 | 0.225 | 0.210 | +0.045 | +0.030 | $3.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Sandis Vilmanis: 1+ goals YES | 13 | 0.167 | 0.157 | +0.029 | +0.019 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Anton Lundell: First Goalscorer YES** — thesis: FLA scores first; alternative: KXNHL1PSPREAD-26NOV07FLAWSH-FLA2|yes; why: higher confidence-adjusted growth (106.23 vs 0.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.963 vs 0.849); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV07FLAWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV07FLAWSH-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: WSH scores first
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07FLAWSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (19.66 vs 13.38 bp); relationships: KXNHLFIRSTGOAL-26NOV07FLAWSH-FLAALUNDELL15|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV07FLAWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV07FLAWSH-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: WSH offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (19.66 vs 13.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLFIRSTGOAL-26NOV07FLAWSH-FLAALUNDELL15|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV07FLAWSH-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.037); failure: WSH offense suppressed (<= 2 goals)
- **Sandis Vilmanis: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07FLAWSH-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (6.27 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLFIRSTGOAL-26NOV07FLAWSH-FLAALUNDELL15|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV07FLAWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.037); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4512): highest fidelity KXNHLAST-26NOV07FLAWSH-WSHAOVECHKIN8-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.4344): highest fidelity KXNHLGOAL-26NOV07FLAWSH-FLASREINHART13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07FLAWSH-FLASREINHART13-1|no (same contract)
- thesis FLA:SCORES_FIRST (p 0.458): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLFIRSTGOAL-26NOV07FLAWSH-FLAALUNDELL15|yes: FUNDED_RESEARCH; family MIXED; loses 93% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SCORES_FIRST (p 0.5409, phi -0.198)
- KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3347, phi -0.248)
- KXNHLGOAL-26NOV07FLAWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3347, phi -0.207)
- KXNHLGOAL-26NOV07FLAWSH-FLASVILMANIS95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4344, phi -0.2)

portfolios: A EV +3.78 (adj +1.19) on $13.82, P(profit) 0.6208, adj growth 11.0 bp · B EV +6.94 (adj +6.87) on $12.15, P(profit) 0.5359, adj growth 54.2 bp · C EV +1.92 (adj +1.27) on $12.99, P(profit) 0.2455, adj growth 11.9 bp · R EV +2.01 (adj +2.38) on $1.00, P(profit) 0.0322, adj growth 62.6 bp

## STL @ NSH  ·  10000 joint draws  ·  412 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_STL_win | p_overtime | goals | shots NSH/STL | NSH/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.48 | 0.52 | 0.00 | 6.04 | 27.8/27.8 | 24.0/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.51 | 0.49 | 0.45 | 5.95 | 27.7/27.9 | 24.6/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.50 | 0.50 | 0.00 | 9.39 | 29.3/29.4 | 23.3/23.0 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.072 | 0.56 | 0.44 | 0.00 | 6.0 | 32.9/22.4 | 19.3/28.8 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.064 | 0.46 | 0.54 | 0.00 | 6.01 | 22.0/32.7 | 28.8/18.8 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.53 | 0.47 | 0.46 | 5.92 | 32.8/22.0 | 18.8/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Edstrom: 1+ goals YES | 15 | 0.203 | 0.188 | +0.044 | +0.029 | $3.10 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 25 | 0.304 | 0.289 | +0.041 | +0.026 | $3.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Full Game: Over 6.5 goals scored YES | 42 | 0.485 | 0.450 | +0.048 | +0.013 | $1.18 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mavrik Bourque: 1+ assists NO | 70 | 0.767 | 0.726 | +0.052 | +0.011 | $6.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (13.71 vs 7.47 bp); relationships: KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLTOTAL-26NOV07STLNSH-7|yes: MOSTLY_INDEPENDENT (phi 0.138); KXNHLAST-26NOV07STLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.03); failure: NSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (13.71 vs 7.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.027); they share one thesis budget; relationships: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLTOTAL-26NOV07STLNSH-7|yes: REINFORCING (phi 0.163); KXNHLAST-26NOV07STLNSH-NSHMBOURQUE22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.173); failure: NSH offense suppressed (<= 2 goals)
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26NOV07STLNSH-9|yes; why: Broad expression KXNHLTOTAL-26NOV07STLNSH-7|yes selected over broad KXNHLTOTAL-26NOV07STLNSH-9|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.138); KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: REINFORCING (phi 0.163); KXNHLAST-26NOV07STLNSH-NSHMBOURQUE22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.171); failure: low-event game (<= 4 goals)
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV07STLNSH-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (1.39 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.173); KXNHLTOTAL-26NOV07STLNSH-7|yes: INTENTIONAL_DIVERSIFIER (phi -0.171); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:OFFENSE_4PLUS (p 0.4005): highest fidelity KXNHLTOTAL-26NOV07STLNSH-7|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2797): highest fidelity KXNHLTOTAL-26NOV07STLNSH-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26NOV07STLNSH-7|yes (same contract)
- thesis NSH:SUPPRESSED (p 0.3824): highest fidelity KXNHLAST-26NOV07STLNSH-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07STLNSH-NSHMBOURQUE22-1|no (same contract)
- KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3824, phi -0.22)
- KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3824, phi -0.243)
- KXNHLTOTAL-26NOV07STLNSH-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.2202, phi -0.516)
- KXNHLAST-26NOV07STLNSH-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.4005, phi -0.23)
- override: Broad expression KXNHLTOTAL-26NOV07STLNSH-7|yes selected over broad KXNHLTOTAL-26NOV07STLNSH-9|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.74 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.93 (adj +0.96) on $13.82, P(profit) 0.5772, adj growth 9.1 bp · B EV +2.01 (adj +1.06) on $14.54, P(profit) 0.4124, adj growth 10.0 bp · C EV +1.85 (adj +0.91) on $11.91, P(profit) 0.2923, adj growth 8.5 bp · R EV +0.11 (adj +0.03) on $1.00, P(profit) 0.4849, adj growth 1.1 bp

## NYR @ SEA  ·  10000 joint draws  ·  442 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_NYR_win | p_overtime | goals | shots SEA/NYR | SEA/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 6.04 | 27.5/27.4 | 24.2/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.48 | 5.94 | 27.5/27.5 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.57 | 0.43 | 0.00 | 9.45 | 29.0/28.9 | 23.1/22.3 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.071 | 0.62 | 0.38 | 0.00 | 6.02 | 32.0/21.7 | 18.9/27.4 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.068 | 0.50 | 0.50 | 0.00 | 5.99 | 21.8/32.1 | 28.4/18.5 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.55 | 0.45 | 0.49 | 5.91 | 32.1/21.9 | 18.7/28.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 9 | 0.150 | 0.131 | +0.054 | +0.036 | $3.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| New York R wins by over 1.5 goals NO | 67 | 0.753 | 0.709 | +0.067 | +0.023 | $5.19 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ goals NO | 66 | 0.712 | 0.696 | +0.036 | +0.020 | $5.42 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Jani Nyman: 1+ goals YES | 12 | 0.153 | 0.141 | +0.026 | +0.014 | $1.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: higher confidence-adjusted growth (30.82 vs 5.57 bp); despite a smaller raw edge (+0.054 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: MOSTLY_INDEPENDENT (phi 0.086); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV07NYRSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: SEA offense suppressed (<= 2 goals)
- **New York R wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV07NYRSEA-SEA2|yes; why: higher confidence-adjusted growth (5.57 vs 4.96 bp); wins across more scripts (relative breadth 0.973 vs 0.517); relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.086); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26NOV07NYRSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.109); failure: NYR wins by 2+
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no has the higher standalone adjusted growth (5.57 vs 4.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.147); they share one thesis budget; relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26NOV07NYRSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: NYR offense succeeds (4+ goals)
- **Jani Nyman: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no has the higher standalone adjusted growth (5.57 vs 3.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.109); they share one thesis budget; relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: MOSTLY_INDEPENDENT (phi 0.109); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4274): highest fidelity KXNHLSPREAD-26NOV07NYRSEA-NYR3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.5415): highest fidelity KXNHLSPREAD-26NOV07NYRSEA-NYR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.3233): highest fidelity KXNHLSPREAD-26NOV07NYRSEA-NYR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no (same contract)
- KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3566, phi -0.17)
- KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYR:WINS_BY_2PLUS (p 0.2473, phi -1.0)
- KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3681, phi -0.246)
- KXNHLGOAL-26NOV07NYRSEA-SEAJNYMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3566, phi -0.176)

portfolios: A EV +3.01 (adj +1.53) on $13.82, P(profit) 0.3997, adj growth 14.2 bp · B EV +2.91 (adj +1.69) on $15.19, P(profit) 0.6561, adj growth 15.9 bp · C EV +0.97 (adj +0.34) on $9.92, P(profit) 0.7527, adj growth 3.2 bp · R EV +0.30 (adj +0.13) on $4.00, P(profit) 0.5642, adj growth 4.8 bp

## MTL @ TOR  ·  10000 joint draws  ·  424 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_MTL_win | p_overtime | goals | shots TOR/MTL | TOR/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.54 | 0.46 | 0.00 | 6.11 | 28.9/28.9 | 25.6/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.117 | 0.54 | 0.46 | 0.00 | 9.36 | 30.3/30.4 | 24.4/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.47 | 5.98 | 28.8/28.9 | 25.6/25.5 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.073 | 0.58 | 0.42 | 0.00 | 6.01 | 33.8/23.1 | 19.9/29.6 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.067 | 0.49 | 0.51 | 0.00 | 6.03 | 23.4/34.1 | 30.4/19.8 | even strength |
| MTL shot control · high event (8+) · decided (2+) | 0.058 | 0.49 | 0.51 | 0.00 | 9.35 | 24.6/35.6 | 28.9/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 12 | 0.180 | 0.158 | +0.053 | +0.030 | $2.91 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Nick Suzuki: 1+ assists NO | 48 | 0.642 | 0.530 | +0.144 | +0.033 | $6.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Brandon Duhaime: 1+ goals YES | 8 | 0.110 | 0.102 | +0.025 | +0.016 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Dakota Joshua: 1+ goals YES | 13 | 0.166 | 0.155 | +0.029 | +0.017 | $1.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07MTLTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (17.68 vs 1.91 bp); relationships: KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV07MTLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV07MTLTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: TOR offense suppressed (<= 2 goals)
- **Nick Suzuki: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07MTLTOR-MTL2|no; why: higher confidence-adjusted growth (9.29 vs 0.90 bp); alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV07MTLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV07MTLTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: MTL offense succeeds (4+ goals)
- **Brandon Duhaime: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (17.68 vs 7.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.018); they share one thesis budget; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV07MTLTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: TOR offense suppressed (<= 2 goals)
- **Dakota Joshua: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (17.68 vs 5.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV07MTLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.4578): highest fidelity KXNHLAST-26NOV07MTLTOR-TORMRIELLY44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3713): highest fidelity KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no (same contract)
- KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3331, phi -0.197)
- KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.2 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4173, phi -0.249)
- KXNHLGOAL-26NOV07MTLTOR-TORBDUHAIME24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3331, phi -0.133)
- KXNHLGOAL-26NOV07MTLTOR-TORDJOSHUA81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3331, phi -0.178)

portfolios: A EV +3.28 (adj +1.14) on $13.82, P(profit) 0.4403, adj growth 10.7 bp · B EV +3.93 (adj +1.65) on $12.79, P(profit) 0.779, adj growth 15.6 bp · C EV +3.90 (adj +1.41) on $11.87, P(profit) 0.7024, adj growth 13.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ OTT  ·  10000 joint draws  ·  432 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_UTA_win | p_overtime | goals | shots OTT/UTA | OTT/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.54 | 0.46 | 0.00 | 6.05 | 27.1/27.0 | 23.6/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.47 | 5.96 | 27.2/27.0 | 23.8/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.55 | 0.45 | 0.00 | 9.4 | 28.6/28.6 | 22.8/22.1 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.079 | 0.61 | 0.39 | 0.00 | 6.0 | 31.9/21.7 | 18.7/27.7 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.54 | 0.46 | 0.46 | 5.92 | 32.4/21.7 | 18.5/29.1 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.058 | 0.64 | 0.36 | 0.00 | 9.36 | 33.8/23.1 | 18.2/26.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 16 | 0.211 | 0.196 | +0.041 | +0.026 | $2.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Dylan Cozens: 1+ goals YES | 24 | 0.293 | 0.279 | +0.040 | +0.026 | $3.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 16 | 0.201 | 0.183 | +0.032 | +0.014 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Logan Cooley: 1+ goals NO | 68 | 0.722 | 0.710 | +0.026 | +0.015 | $4.79 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-UTAALEE72-1|yes; why: higher confidence-adjusted growth (10.45 vs 0.68 bp); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07UTAOTT-UTALCOOLEY92-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: UTA offense suppressed (<= 2 goals)
- **Dylan Cozens: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (7.61 vs 2.99 bp); relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV07UTAOTT-UTALCOOLEY92-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes has the higher standalone adjusted growth (7.61 vs 2.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.019); they share one thesis budget; relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV07UTAOTT-UTALCOOLEY92-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: OTT offense suppressed (<= 2 goals)
- **Logan Cooley: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV07UTAOTT-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (2.24 vs 1.87 bp); relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.3838): highest fidelity KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4341): highest fidelity KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3946): highest fidelity KXNHLGOAL-26NOV07UTAOTT-UTALCOOLEY92-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-UTALCOOLEY92-1|no (same contract)
- KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3946, phi -0.244)
- KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3514, phi -0.22)
- KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3514, phi -0.207)
- KXNHLGOAL-26NOV07UTAOTT-UTALCOOLEY92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3838, phi -0.246)

portfolios: A EV +1.92 (adj +1.12) on $13.82, P(profit) 0.5035, adj growth 10.5 bp · B EV +1.70 (adj +1.01) on $12.51, P(profit) 0.5239, adj growth 9.6 bp · C EV +1.79 (adj +1.12) on $13.90, P(profit) 0.4452, adj growth 10.5 bp · R EV +0.08 (adj +0.04) on $2.00, P(profit) 0.7216, adj growth 1.6 bp

## NJD @ NYI  ·  10000 joint draws  ·  426 bet sides mapped, 14 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_NJD_win | p_overtime | goals | shots NYI/NJD | NYI/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.53 | 0.47 | 0.00 | 6.05 | 27.5/27.8 | 24.4/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.50 | 0.50 | 0.46 | 5.93 | 27.6/27.7 | 24.5/24.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.086 | 0.44 | 0.56 | 0.00 | 5.93 | 22.0/32.9 | 28.9/18.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.56 | 0.44 | 0.00 | 9.17 | 29.2/29.5 | 24.0/22.8 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.49 | 0.51 | 0.43 | 5.87 | 22.0/32.6 | 29.4/18.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.52 | 0.48 | 0.00 | 3.45 | 26.4/26.6 | 24.7/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 1.5 goals NO | 64 | 0.732 | 0.684 | +0.076 | +0.028 | $7.90 | FUNDED_RESEARCH | $2 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.170 | 0.157 | +0.032 | +0.019 | $1.84 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 11 | 0.143 | 0.133 | +0.027 | +0.016 | $1.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.254 | 0.240 | +0.032 | +0.019 | $1.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV07NJNYI-NJ3|no; why: higher confidence-adjusted growth (7.35 vs 4.05 bp); relationships: KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.121); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.142); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.149); failure: NJD wins by 2+
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NJNYI-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NJNYI-NJ2|no has the higher standalone adjusted growth (7.35 vs 6.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.121); they share one thesis budget; relationships: KXNHLSPREAD-26NOV07NJNYI-NJ2|no: MOSTLY_INDEPENDENT (phi 0.121); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: NYI offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV07NJNYI-3|yes; why: higher confidence-adjusted growth (5.20 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.901 vs 0.782); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLSPREAD-26NOV07NJNYI-NJ2|no: INTENTIONAL_DIVERSIFIER (phi -0.142); KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NJD offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NJNYI-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NJNYI-NJ2|no has the higher standalone adjusted growth (7.35 vs 4.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.149); they share one thesis budget; relationships: KXNHLSPREAD-26NOV07NJNYI-NJ2|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:WINS (p 0.5147): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3843): highest fidelity KXNHLTEAMTOTAL-26NOV07NJNYI-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4163): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV07NJNYI-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2678, phi -1.0)
- KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3999, phi -0.194)
- KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4163, phi -0.174)
- KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3999, phi -0.228)

portfolios: A EV +3.14 (adj +0.54) on $13.82, P(profit) 0.5683, adj growth 4.9 bp · B EV +2.05 (adj +1.01) on $13.51, P(profit) 0.4263, adj growth 9.5 bp · C EV +1.15 (adj +0.42) on $9.92, P(profit) 0.7322, adj growth 3.9 bp · R EV +0.23 (adj +0.08) on $2.00, P(profit) 0.7322, adj growth 3.2 bp

## CHI @ CAR  ·  10000 joint draws  ·  458 bet sides mapped, 14 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CHI_win | p_overtime | goals | shots CAR/CHI | CAR/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.205 | 0.79 | 0.21 | 0.00 | 6.04 | 34.4/20.2 | 18.0/29.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.160 | 0.81 | 0.19 | 0.00 | 9.39 | 36.3/21.7 | 17.7/27.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.152 | 0.57 | 0.43 | 0.49 | 5.97 | 34.5/20.7 | 17.5/30.9 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.081 | 0.74 | 0.26 | 0.00 | 3.48 | 32.9/19.1 | 18.0/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.070 | 0.74 | 0.26 | 0.00 | 6.03 | 28.0/26.6 | 24.0/23.2 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.57 | 0.43 | 0.52 | 2.9 | 33.0/19.1 | 17.6/31.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sebastian Aho: 1+ goals NO | 62 | 0.703 | 0.680 | +0.067 | +0.044 | $7.90 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 18 | 0.241 | 0.223 | +0.051 | +0.033 | $3.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 39 | 0.527 | 0.435 | +0.120 | +0.028 | $2.55 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dillon Boucher: 1+ goals YES | 6 | 0.089 | 0.078 | +0.025 | +0.014 | $1.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07CHICAR-CAR2|no; why: higher confidence-adjusted growth (18.05 vs 7.13 bp); despite a smaller raw edge (+0.067 vs +0.120/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.032 vs 0.847); relationships: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26NOV07CHICAR-CAR2|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CAR offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07CHICAR-CAR2|no; why: higher confidence-adjusted growth (15.28 vs 7.13 bp); despite a smaller raw edge (+0.051 vs +0.120/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLSPREAD-26NOV07CHICAR-CAR2|no: REINFORCING (phi 0.15); KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: CHI offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV07CHICAR-CAR3|no; why: higher confidence-adjusted growth (7.13 vs 6.14 bp); relationships: KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: REINFORCING (phi 0.15); KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi 0.086); failure: CAR wins by 2+
- **Dillon Boucher: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (15.28 vs 6.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26NOV07CHICAR-CAR2|no: MOSTLY_INDEPENDENT (phi 0.086); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.20, CAR shot control · high event (8+) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15.
- thesis CAR:SUPPRESSED (p 0.2461): highest fidelity KXNHLSPREAD-26NOV07CHICAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.2753): highest fidelity KXNHLSPREAD-26NOV07CHICAR-CAR3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.3845): highest fidelity KXNHLSPREAD-26NOV07CHICAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07CHICAR-CAR2|no (same contract)
- KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.5519, phi -0.228)
- KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.251)
- KXNHLSPREAD-26NOV07CHICAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.2 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.4729, phi -1.0)
- KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.16)

portfolios: A EV +3.79 (adj +0.86) on $13.82, P(profit) 0.5271, adj growth 7.7 bp · B EV +3.01 (adj +1.60) on $15.23, P(profit) 0.5614, adj growth 15.2 bp · C EV +3.31 (adj +1.70) on $18.00, P(profit) 0.5259, adj growth 16.1 bp · R EV +0.51 (adj +0.21) on $3.00, P(profit) 0.7034, adj growth 7.9 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07CHICAR-CHI|yes == KXNHLGAME-26NOV07CHICAR-CAR|no

## SJS @ DAL  ·  10000 joint draws  ·  432 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_SJS_win | p_overtime | goals | shots DAL/SJS | DAL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.70 | 0.30 | 0.00 | 6.01 | 26.5/26.1 | 23.5/22.0 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.115 | 0.78 | 0.22 | 0.00 | 6.0 | 31.4/20.5 | 18.4/26.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.56 | 0.44 | 0.47 | 5.94 | 26.7/26.3 | 23.0/23.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.60 | 0.40 | 0.47 | 5.9 | 31.5/20.6 | 17.6/28.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.72 | 0.28 | 0.00 | 9.25 | 28.3/27.7 | 22.9/21.0 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.071 | 0.77 | 0.23 | 0.00 | 9.19 | 33.4/21.9 | 17.9/25.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 1+ assists NO | 72 | 0.800 | 0.753 | +0.066 | +0.019 | $7.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Dallas over 3.5 goals scored NO | 43 | 0.501 | 0.463 | +0.053 | +0.016 | $2.25 | FUNDED_RESEARCH | $1 | DAL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| San Jose over 2.5 goals scored YES | 43 | 0.498 | 0.462 | +0.051 | +0.014 | $3.37 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Wyatt Johnston: 1+ goals NO | 60 | 0.641 | 0.628 | +0.025 | +0.012 | $2.34 | FUNDED_RESEARCH | $1 | DAL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (3.89 vs 0.07 bp); alternative not eligible: confidence-adjusted EV +0.0028 below the 0.010/contract floor; relationships: KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes: INTENTIONAL_DIVERSIFIER (phi -0.217); KXNHLGOAL-26NOV07SJDAL-DALWJOHNSTON53-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: SJS offense succeeds (4+ goals)
- **Dallas over 3.5 goals scored NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07SJDAL-DAL3|no; why: higher confidence-adjusted growth (2.18 vs 1.89 bp); despite a smaller raw edge (+0.053 vs +0.080/contract); relationships: KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26NOV07SJDAL-DALWJOHNSTON53-1|no: REINFORCING (phi 0.251); failure: DAL offense succeeds (4+ goals)
- **San Jose over 2.5 goals scored YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes selected over broad KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.217); KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26NOV07SJDAL-DALWJOHNSTON53-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: SJS offense suppressed (<= 2 goals)
- **Wyatt Johnston: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no has the higher standalone adjusted growth (2.18 vs 1.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.251); they share one thesis budget; relationships: KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no: REINFORCING (phi 0.251); KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SJS:OFFENSE_4PLUS (p 0.2745): highest fidelity KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes — Broad expression KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes selected over broad KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis SJS:SUPPRESSED (p 0.5121): highest fidelity KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no (same contract)
- thesis DAL:SUPPRESSED (p 0.3039): highest fidelity KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no (same contract)
- KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.2745, phi -0.186)
- KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4889, phi -0.979)
- KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis SJS:SUPPRESSED (p 0.5121, phi -0.98)
- KXNHLGOAL-26NOV07SJDAL-DALWJOHNSTON53-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4889, phi -0.249)
- override: Broad expression KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes selected over broad KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes because adjusted EV differs by only 0.0 pts while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.73 (adj +0.38) on $13.82, P(profit) 0.5848, adj growth 3.5 bp · B EV +1.46 (adj +0.43) on $15.86, P(profit) 0.5751, adj growth 4.1 bp · C EV +2.09 (adj +0.66) on $15.16, P(profit) 0.493, adj growth 6.2 bp · R EV +0.27 (adj +0.09) on $3.00, P(profit) 0.5628, adj growth 3.2 bp

## TBL @ MIN  ·  10000 joint draws  ·  420 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_TBL_win | p_overtime | goals | shots MIN/TBL | MIN/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.45 | 0.55 | 0.00 | 6.02 | 27.6/27.7 | 23.9/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.49 | 0.51 | 0.49 | 5.9 | 27.7/27.8 | 24.5/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.44 | 0.56 | 0.00 | 9.29 | 29.3/29.5 | 22.9/23.8 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.071 | 0.39 | 0.61 | 0.00 | 6.04 | 22.3/33.0 | 28.8/19.5 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.47 | 0.53 | 0.46 | 5.91 | 22.2/32.6 | 29.2/19.0 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.061 | 0.52 | 0.48 | 0.00 | 6.03 | 32.4/22.3 | 18.9/28.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Blake Coleman: 1+ goals YES | 18 | 0.249 | 0.230 | +0.059 | +0.039 | $4.59 | FUNDED_RESEARCH | $2 | MIN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 9 | 0.138 | 0.124 | +0.043 | +0.028 | $2.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Bobby Brink: 1+ goals YES | 14 | 0.184 | 0.168 | +0.036 | +0.020 | $2.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ assists NO | 37 | 0.458 | 0.411 | +0.071 | +0.025 | $5.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.68) | EVIDENCE_MIXED | D |
- **Blake Coleman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (21.44 vs 6.54 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: MIN offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes has the higher standalone adjusted growth (21.44 vs 19.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); failure: MIN offense suppressed (<= 2 goals)
- **Bobby Brink: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes has the higher standalone adjusted growth (21.44 vs 6.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.082); failure: MIN offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07TBMIN-MINMBOLDY12-1|no; why: higher confidence-adjusted growth (5.77 vs 4.13 bp); despite a smaller raw edge (+0.071 vs +0.104/contract); relationships: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.082); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.3695): highest fidelity KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.3654): highest fidelity KXNHLAST-26NOV07TBMIN-TBNKUCHEROV86-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV07TBMIN-TBNKUCHEROV86-2|no (same contract)
- thesis MIN:SUPPRESSED (p 0.4098): highest fidelity KXNHLAST-26NOV07TBMIN-MINMBOLDY12-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4098, phi -0.247)
- KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4098, phi -0.169)
- KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4098, phi -0.209)
- KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 32% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3695, phi -0.326)

portfolios: A EV +2.63 (adj +1.13) on $13.82, P(profit) 0.5149, adj growth 10.9 bp · B EV +4.13 (adj +2.37) on $14.68, P(profit) 0.4689, adj growth 22.4 bp · C EV +3.67 (adj +1.84) on $21.34, P(profit) 0.5579, adj growth 17.2 bp · R EV +0.62 (adj +0.41) on $2.00, P(profit) 0.2494, adj growth 14.8 bp

## DET @ COL  ·  10000 joint draws  ·  452 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_DET_win | p_overtime | goals | shots COL/DET | COL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.74 | 0.26 | 0.00 | 6.0 | 28.7/28.1 | 25.7/23.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.111 | 0.78 | 0.22 | 0.00 | 6.01 | 33.8/22.1 | 20.0/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.73 | 0.27 | 0.00 | 9.43 | 30.4/29.7 | 25.0/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.53 | 0.47 | 0.46 | 5.94 | 28.8/28.2 | 24.9/25.4 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.62 | 0.38 | 0.43 | 5.92 | 33.7/22.4 | 19.4/30.4 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.086 | 0.81 | 0.19 | 0.00 | 9.37 | 35.4/23.6 | 19.6/25.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ LAK  ·  10000 joint draws  ·  432 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_PIT_win | p_overtime | goals | shots LAK/PIT | LAK/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.59 | 0.41 | 0.00 | 6.02 | 27.5/27.5 | 24.4/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.51 | 0.49 | 0.47 | 5.91 | 27.4/27.3 | 24.1/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.58 | 0.42 | 0.00 | 9.25 | 28.9/28.7 | 23.1/22.2 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.071 | 0.66 | 0.34 | 0.00 | 6.01 | 32.2/21.5 | 18.7/27.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.56 | 0.44 | 0.44 | 5.83 | 32.4/22.0 | 19.0/29.0 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.062 | 0.50 | 0.50 | 0.00 | 6.0 | 22.0/32.4 | 28.7/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 12 | 0.159 | 0.146 | +0.031 | +0.019 | $1.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 9 | 0.124 | 0.111 | +0.028 | +0.015 | $1.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ goals NO | 77 | 0.809 | 0.798 | +0.027 | +0.016 | $7.57 | FUNDED_RESEARCH | $2 | PIT:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (7.04 vs 5.42 bp); relationships: KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes has the higher standalone adjusted growth (7.04 vs 5.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: LAK wins (incl. OT/SO)
- **Ben Kindel: 1+ goals NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV07PITLA-PITEMALKIN71-1|no; why: higher confidence-adjusted growth (3.24 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0006 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: PIT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.2396): highest fidelity KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes (same contract)
- thesis PIT:SUPPRESSED (p 0.4218): highest fidelity KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.431): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4218, phi -0.198)
- KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:WINS (p 0.5534, phi -0.191)
- KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3516, phi -0.212)

portfolios: A EV +2.11 (adj +1.15) on $11.79, P(profit) 0.319, adj growth 10.6 bp · B EV +1.17 (adj +0.67) on $10.99, P(profit) 0.261, adj growth 6.4 bp · C EV +0.93 (adj +0.56) on $11.85, P(profit) 0.8396, adj growth 5.3 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.8093, adj growth 1.5 bp

## VAN @ EDM  ·  10000 joint draws  ·  428 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_VAN_win | p_overtime | goals | shots EDM/VAN | EDM/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.146 | 0.79 | 0.21 | 0.00 | 6.1 | 33.1/21.0 | 18.9/27.7 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.137 | 0.78 | 0.22 | 0.00 | 9.38 | 34.7/22.3 | 18.3/26.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.72 | 0.28 | 0.00 | 9.58 | 29.3/28.3 | 23.3/21.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.099 | 0.70 | 0.30 | 0.00 | 6.08 | 27.3/26.7 | 24.1/22.7 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.57 | 0.43 | 0.49 | 6.06 | 33.7/21.4 | 18.2/30.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.51 | 0.49 | 0.48 | 6.08 | 27.5/26.7 | 23.3/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brendan Gallagher: 1+ goals YES | 10 | 0.148 | 0.135 | +0.042 | +0.029 | $2.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Edmonton wins by over 1.5 goals NO | 45 | 0.542 | 0.494 | +0.075 | +0.026 | $4.57 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 27 | 0.315 | 0.301 | +0.031 | +0.017 | $2.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Leon Draisaitl: 1+ goals NO | 49 | 0.532 | 0.519 | +0.025 | +0.012 | $1.37 | FUNDED_RESEARCH | $1 | EDM:SUPPRESSED | DIRECT (0.76) | EVIDENCE_STRONGER | D |
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07VANEDM-EDM2|no; why: higher confidence-adjusted growth (18.52 vs 6.13 bp); despite a smaller raw edge (+0.042 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV07VANEDM-EDM2|no: MOSTLY_INDEPENDENT (phi 0.138); KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Edmonton wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV07VANEDM-EDM3|no; why: higher confidence-adjusted growth (6.13 vs 5.79 bp); relationships: KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.138); KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.21); KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no: REINFORCING (phi 0.174); failure: EDM wins by 2+
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (3.21 vs 0.00 bp); despite a smaller raw edge (+0.031 vs +0.053/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26NOV07VANEDM-EDM2|no: INTENTIONAL_DIVERSIFIER (phi -0.21); KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: EDM offense suppressed (<= 2 goals)
- **Leon Draisaitl: 1+ goals NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07VANEDM-EDM2|no; why: Player prop expression KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no selected over player prop KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.76 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26NOV07VANEDM-EDM2|no: REINFORCING (phi 0.174); KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.15, EDM shot control · high event (8+) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.338): highest fidelity KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.3772): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07VANEDM-EDM2|no (same contract)
- thesis EDM:SUPPRESSED (p 0.2262): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07VANEDM-EDM2|no — Player prop expression KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no selected over player prop KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.76 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4419, phi -0.207)
- KXNHLSPREAD-26NOV07VANEDM-EDM2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis EDM:WINS_BY_2PLUS (p 0.4575, phi -1.0)
- KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2262, phi -0.206)
- KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 24% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5893, phi -0.269)
- override: Player prop expression KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no selected over player prop KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.76 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.95 (adj +0.53) on $13.82, P(profit) 0.6053, adj growth 4.9 bp · B EV +2.18 (adj +1.19) on $11.57, P(profit) 0.5331, adj growth 11.3 bp · C EV +2.70 (adj +1.47) on $13.15, P(profit) 0.4184, adj growth 13.7 bp · R EV +0.37 (adj +0.14) on $3.00, P(profit) 0.5425, adj growth 5.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
