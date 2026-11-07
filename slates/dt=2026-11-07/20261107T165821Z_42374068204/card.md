# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-07T16:58:21Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +31.27 | +10.48 | +29.83 | 0.766 | -21.56 | -35.36 | 95.98 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +32.13 | +20.65 | +24.05 | 0.722 | -26.81 | -40.77 | 181.54 |
| C best expression per thesis | 150.00 | +24.26 | +11.22 | +22.87 | 0.711 | -28.57 | -42.25 | 103.28 |
| R FUNDED research stakes | 18.00 | +3.97 | +3.35 | +0.90 | 0.562 | -5.72 | -7.93 | 0.00 |

## FLA @ WSH  ·  10000 joint draws  ·  452 bet sides mapped, 13 +EV candidates, 4 on card


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
| Anton Lundell: First Goalscorer YES | 1 | 0.032 | 0.036 | +0.021 | +0.025 | $2.43 | FUNDED_RESEARCH | $1 | FLA:SCORES_FIRST | FRAGILE (0.07) | EVIDENCE_MIXED | D |
| Aliaksei Protas: 1+ goals YES | 18 | 0.245 | 0.228 | +0.055 | +0.037 | $4.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 17 | 0.225 | 0.210 | +0.045 | +0.030 | $3.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Sandis Vilmanis: 1+ goals YES | 13 | 0.167 | 0.157 | +0.029 | +0.019 | $2.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Anton Lundell: First Goalscorer YES** — thesis: FLA scores first; alternative: KXNHLFIRSTGOAL-26NOV07FLAWSH-FLASBENNETT9|yes; why: higher confidence-adjusted growth (106.23 vs 0.00 bp); alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV07FLAWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV07FLAWSH-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: WSH scores first
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07FLAWSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (19.66 vs 13.38 bp); relationships: KXNHLFIRSTGOAL-26NOV07FLAWSH-FLAALUNDELL15|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV07FLAWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV07FLAWSH-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: WSH offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (19.66 vs 13.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLFIRSTGOAL-26NOV07FLAWSH-FLAALUNDELL15|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV07FLAWSH-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.037); failure: WSH offense suppressed (<= 2 goals)
- **Sandis Vilmanis: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07FLAWSH-FLACVERHAEGHE23-2|yes; why: higher confidence-adjusted growth (6.27 vs 2.98 bp); wins across more scripts (relative breadth 0.888 vs 0.768); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLFIRSTGOAL-26NOV07FLAWSH-FLAALUNDELL15|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV07FLAWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.037); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4512): highest fidelity KXNHLAST-26NOV07FLAWSH-WSHAOVECHKIN8-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:WINS_BY_2PLUS (p 0.3472): highest fidelity KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes (same contract)
- thesis FLA:SUPPRESSED (p 0.4344): highest fidelity KXNHLGOAL-26NOV07FLAWSH-FLASREINHART13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07FLAWSH-FLASREINHART13-1|no (same contract)
- KXNHLFIRSTGOAL-26NOV07FLAWSH-FLAALUNDELL15|yes: FUNDED_RESEARCH; family MIXED; loses 93% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SCORES_FIRST (p 0.5409, phi -0.198)
- KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3347, phi -0.248)
- KXNHLGOAL-26NOV07FLAWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3347, phi -0.207)
- KXNHLGOAL-26NOV07FLAWSH-FLASVILMANIS95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4344, phi -0.2)

portfolios: A EV +4.07 (adj +1.34) on $14.90, P(profit) 0.6208, adj growth 12.3 bp · B EV +7.79 (adj +7.72) on $13.65, P(profit) 0.5359, adj growth 60.1 bp · C EV +2.47 (adj +1.64) on $16.77, P(profit) 0.2455, adj growth 15.0 bp · R EV +2.01 (adj +2.38) on $1.00, P(profit) 0.0322, adj growth 62.6 bp

## STL @ NSH  ·  10000 joint draws  ·  412 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_STL_win | p_overtime | goals | shots NSH/STL | NSH/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.48 | 0.52 | 0.00 | 6.07 | 27.8/27.9 | 24.3/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.47 | 5.97 | 28.0/27.9 | 24.4/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.49 | 0.51 | 0.00 | 9.3 | 29.0/29.1 | 22.9/22.9 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.073 | 0.54 | 0.46 | 0.00 | 6.04 | 32.6/22.3 | 19.1/28.8 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.064 | 0.45 | 0.55 | 0.00 | 6.02 | 22.2/32.8 | 28.7/18.8 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.51 | 0.49 | 0.46 | 5.94 | 32.8/22.4 | 19.2/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Edstrom: 1+ goals YES | 15 | 0.201 | 0.187 | +0.042 | +0.028 | $3.37 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 25 | 0.306 | 0.290 | +0.043 | +0.027 | $3.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Justin Barron: 1+ goals YES | 5 | 0.071 | 0.066 | +0.018 | +0.013 | $1.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Ross Colton: 1+ goals YES | 15 | 0.178 | 0.170 | +0.019 | +0.011 | $1.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (12.42 vs 8.36 bp); despite a smaller raw edge (+0.042 vs +0.043/contract); relationships: KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV07STLNSH-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07STLNSH-NSHRCOLTON79-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: NSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (12.42 vs 8.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV07STLNSH-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV07STLNSH-NSHRCOLTON79-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: NSH offense suppressed (<= 2 goals)
- **Justin Barron: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07STLNSH-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (6.76 vs 1.47 bp); despite a smaller raw edge (+0.018 vs +0.021/contract); relationships: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV07STLNSH-NSHRCOLTON79-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: STL offense suppressed (<= 2 goals)
- **Ross Colton: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (12.42 vs 1.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.014); they share one thesis budget; relationships: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07STLNSH-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NSH:OFFENSE_4PLUS (p 0.3885): highest fidelity KXNHLTOTAL-26NOV07STLNSH-7|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.4008): highest fidelity KXNHLTOTAL-26NOV07STLNSH-7|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV07STLNSH-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2735): highest fidelity KXNHLTOTAL-26NOV07STLNSH-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26NOV07STLNSH-7|yes (same contract)
- KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3902, phi -0.216)
- KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3902, phi -0.256)
- KXNHLGOAL-26NOV07STLNSH-STLJBARRON72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.385, phi -0.122)
- KXNHLGOAL-26NOV07STLNSH-NSHRCOLTON79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3902, phi -0.197)

portfolios: A EV +2.26 (adj +1.24) on $14.90, P(profit) 0.5281, adj growth 11.4 bp · B EV +2.13 (adj +1.41) on $9.98, P(profit) 0.4841, adj growth 13.2 bp · C EV +1.57 (adj +0.98) on $8.22, P(profit) 0.4284, adj growth 8.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Ben Meyers: 1+ goals YES | 10 | 0.150 | 0.135 | +0.044 | +0.029 | $3.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| New York R wins by over 1.5 goals NO | 66 | 0.753 | 0.704 | +0.077 | +0.028 | $7.81 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ goals NO | 66 | 0.712 | 0.696 | +0.036 | +0.020 | $5.82 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Jani Nyman: 1+ goals YES | 12 | 0.153 | 0.141 | +0.026 | +0.014 | $1.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: higher confidence-adjusted growth (18.55 vs 7.95 bp); despite a smaller raw edge (+0.044 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: MOSTLY_INDEPENDENT (phi 0.086); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV07NYRSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: SEA offense suppressed (<= 2 goals)
- **New York R wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV07NYRSEA-SEA2|yes; why: higher confidence-adjusted growth (7.95 vs 4.96 bp); wins across more scripts (relative breadth 0.973 vs 0.517); relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.086); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26NOV07NYRSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.109); failure: NYR wins by 2+
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no has the higher standalone adjusted growth (7.95 vs 4.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.147); they share one thesis budget; relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26NOV07NYRSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: NYR offense succeeds (4+ goals)
- **Jani Nyman: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no has the higher standalone adjusted growth (7.95 vs 3.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.109); they share one thesis budget; relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: MOSTLY_INDEPENDENT (phi 0.109); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4274): highest fidelity KXNHLSPREAD-26NOV07NYRSEA-NYR3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.5415): highest fidelity KXNHLSPREAD-26NOV07NYRSEA-NYR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.3233): highest fidelity KXNHLSPREAD-26NOV07NYRSEA-NYR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no (same contract)
- KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3566, phi -0.17)
- KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYR:WINS_BY_2PLUS (p 0.2473, phi -1.0)
- KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3681, phi -0.246)
- KXNHLGOAL-26NOV07NYRSEA-SEAJNYMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3566, phi -0.176)

portfolios: A EV +2.12 (adj +0.69) on $14.90, P(profit) 0.4692, adj growth 6.2 bp · B EV +2.75 (adj +1.48) on $18.11, P(profit) 0.6561, adj growth 13.9 bp · C EV +1.46 (adj +0.53) on $12.81, P(profit) 0.7527, adj growth 5.0 bp · R EV +0.33 (adj +0.14) on $4.00, P(profit) 0.5642, adj growth 5.4 bp

## MTL @ TOR  ·  10000 joint draws  ·  426 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_MTL_win | p_overtime | goals | shots TOR/MTL | TOR/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.54 | 0.46 | 0.00 | 6.07 | 29.1/29.0 | 25.6/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.115 | 0.54 | 0.46 | 0.00 | 9.46 | 30.5/30.7 | 24.7/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.53 | 0.47 | 0.47 | 6.08 | 29.0/29.0 | 25.7/25.4 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.065 | 0.51 | 0.49 | 0.00 | 6.01 | 22.9/34.1 | 30.2/19.7 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.065 | 0.58 | 0.42 | 0.00 | 6.04 | 33.9/23.2 | 20.2/29.9 | even strength |
| TOR shot control · high event (8+) · decided (2+) | 0.061 | 0.62 | 0.38 | 0.00 | 9.46 | 35.3/24.4 | 19.3/27.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 12 | 0.166 | 0.147 | +0.038 | +0.019 | $2.19 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Nick Suzuki: 1+ assists NO | 48 | 0.625 | 0.524 | +0.127 | +0.027 | $6.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Brandon Duhaime: 1+ goals YES | 8 | 0.108 | 0.097 | +0.023 | +0.012 | $1.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07MTLTOR-MTL2|no; why: higher confidence-adjusted growth (7.39 vs 0.72 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV07MTLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: TOR offense suppressed (<= 2 goals)
- **Nick Suzuki: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07MTLTOR-MTL2|no; why: higher confidence-adjusted growth (6.26 vs 0.72 bp); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV07MTLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: MTL offense succeeds (4+ goals)
- **Brandon Duhaime: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (7.39 vs 4.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.4614): highest fidelity KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.3663): highest fidelity KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no (same contract)
- KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3303, phi -0.192)
- KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.5 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4185, phi -0.258)
- KXNHLGOAL-26NOV07MTLTOR-TORBDUHAIME24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3303, phi -0.129)

portfolios: A EV +3.02 (adj +1.09) on $11.11, P(profit) 0.7194, adj growth 10.0 bp · B EV +2.57 (adj +0.85) on $9.58, P(profit) 0.7194, adj growth 8.0 bp · C EV +3.19 (adj +0.95) on $11.88, P(profit) 0.685, adj growth 8.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ OTT  ·  10000 joint draws  ·  432 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_UTA_win | p_overtime | goals | shots OTT/UTA | OTT/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.53 | 0.47 | 0.00 | 6.02 | 27.0/27.0 | 23.5/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.54 | 0.46 | 0.51 | 5.96 | 27.3/27.2 | 23.9/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.52 | 0.48 | 0.00 | 9.5 | 29.0/28.7 | 22.6/22.6 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.083 | 0.61 | 0.39 | 0.00 | 6.08 | 32.1/21.6 | 18.6/27.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.55 | 0.45 | 0.47 | 5.97 | 32.0/21.6 | 18.4/28.6 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.057 | 0.45 | 0.55 | 0.00 | 6.0 | 21.5/31.8 | 27.9/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 16 | 0.212 | 0.198 | +0.043 | +0.029 | $3.57 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 16 | 0.201 | 0.187 | +0.032 | +0.018 | $2.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Dylan Cozens: 1+ goals YES | 25 | 0.298 | 0.283 | +0.035 | +0.020 | $2.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Fabian Zetterlund: 1+ goals YES | 20 | 0.240 | 0.226 | +0.029 | +0.015 | $1.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-UTAALEE72-1|yes; why: higher confidence-adjusted growth (12.49 vs 0.02 bp); alternative not eligible: confidence-adjusted EV +0.0012 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07UTAOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: UTA offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes; why: higher confidence-adjusted growth (4.89 vs 4.62 bp); despite a smaller raw edge (+0.032 vs +0.035/contract); relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07UTAOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: OTT offense suppressed (<= 2 goals)
- **Dylan Cozens: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (4.89 vs 4.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07UTAOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense suppressed (<= 2 goals)
- **Fabian Zetterlund: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (4.89 vs 2.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.3923): highest fidelity KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4332): highest fidelity KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes (same contract)
- KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3856, phi -0.214)
- KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.351, phi -0.199)
- KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.351, phi -0.223)
- KXNHLGOAL-26NOV07UTAOTT-OTTFZETTERLUND20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.351, phi -0.211)

portfolios: A EV +2.35 (adj +1.41) on $12.94, P(profit) 0.5605, adj growth 13.1 bp · B EV +1.99 (adj +1.21) on $10.75, P(profit) 0.5605, adj growth 11.3 bp · C EV +1.92 (adj +1.21) on $8.41, P(profit) 0.3718, adj growth 11.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ NYI  ·  10000 joint draws  ·  428 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_NJD_win | p_overtime | goals | shots NYI/NJD | NYI/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.56 | 0.44 | 0.00 | 6.02 | 27.7/27.9 | 24.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.46 | 5.87 | 27.6/28.0 | 24.6/24.4 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.46 | 0.54 | 0.45 | 5.88 | 21.8/32.5 | 29.3/18.7 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.082 | 0.48 | 0.52 | 0.00 | 6.02 | 22.1/33.1 | 29.3/18.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.53 | 0.47 | 0.00 | 9.24 | 29.0/29.3 | 23.4/22.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.48 | 0.52 | 0.00 | 3.46 | 26.1/26.4 | 24.4/24.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 1.5 goals NO | 65 | 0.739 | 0.692 | +0.073 | +0.026 | $8.83 | FUNDED_RESEARCH | $3 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.167 | 0.154 | +0.029 | +0.016 | $1.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 11 | 0.139 | 0.129 | +0.022 | +0.012 | $1.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 64 | 0.683 | 0.671 | +0.027 | +0.015 | $3.24 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV07NJNYI-NJ3|no; why: higher confidence-adjusted growth (6.64 vs 5.80 bp); relationships: KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.119); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLGOAL-26NOV07NJNYI-NJJHUGHES86-1|no: REINFORCING (phi 0.16); failure: NJD wins by 2+
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NJNYI-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NJNYI-NJ2|no has the higher standalone adjusted growth (6.64 vs 4.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.119); they share one thesis budget; relationships: KXNHLSPREAD-26NOV07NJNYI-NJ2|no: MOSTLY_INDEPENDENT (phi 0.119); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV07NJNYI-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: NYI offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07NJNYI-NJCBROWN16-1|yes; why: higher confidence-adjusted growth (3.03 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLSPREAD-26NOV07NJNYI-NJ2|no: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV07NJNYI-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: NJD offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07NJNYI-NJ2|no; why: Player prop expression KXNHLGOAL-26NOV07NJNYI-NJJHUGHES86-1|no selected over player prop KXNHLAST-26NOV07NJNYI-NJLEVANGELISTA77-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.82 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26NOV07NJNYI-NJ2|no: REINFORCING (phi 0.16); KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.08.
- thesis NYI:WINS (p 0.5148): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no (same contract)
- thesis NJD:SUPPRESSED (p 0.4194): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no — Player prop expression KXNHLGOAL-26NOV07NJNYI-NJJHUGHES86-1|no selected over player prop KXNHLAST-26NOV07NJNYI-NJLEVANGELISTA77-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.82 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NYI:OFFENSE_4PLUS (p 0.3833): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV07NJNYI-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2613, phi -1.0)
- KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.395, phi -0.186)
- KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4194, phi -0.169)
- KXNHLGOAL-26NOV07NJNYI-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3587, phi -0.247)
- override: Player prop expression KXNHLGOAL-26NOV07NJNYI-NJJHUGHES86-1|no selected over player prop KXNHLAST-26NOV07NJNYI-NJLEVANGELISTA77-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.82 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.04 (adj +0.74) on $14.90, P(profit) 0.5683, adj growth 6.9 bp · B EV +1.73 (adj +0.77) on $15.32, P(profit) 0.6379, adj growth 7.3 bp · C EV +1.40 (adj +0.50) on $12.81, P(profit) 0.7387, adj growth 4.6 bp · R EV +0.37 (adj +0.14) on $4.00, P(profit) 0.7387, adj growth 5.2 bp

## CHI @ CAR  ·  10000 joint draws  ·  458 bet sides mapped, 12 +EV candidates, 4 on card


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
| Dillon Boucher: 1+ goals YES | 5 | 0.089 | 0.077 | +0.036 | +0.024 | $2.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 62 | 0.703 | 0.681 | +0.067 | +0.045 | $8.87 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 19 | 0.243 | 0.224 | +0.042 | +0.023 | $2.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Frank Nazar: 1+ goals YES | 19 | 0.225 | 0.215 | +0.025 | +0.015 | $1.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Dillon Boucher: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV07CHICAR-CHI5|yes; why: higher confidence-adjusted growth (23.40 vs 7.40 bp); despite a smaller raw edge (+0.036 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.899 vs 0.585); relationships: KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV07CHICAR-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: CHI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07CHICAR-CAR3|no; why: higher confidence-adjusted growth (19.11 vs 4.66 bp); despite a smaller raw edge (+0.067 vs +0.107/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07CHICAR-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: CAR offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV07CHICAR-CHI5|yes; why: KXNHLTEAMTOTAL-26NOV07CHICAR-CHI5|yes has the higher standalone adjusted growth (7.40 vs 6.97 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.197); relationships: KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07CHICAR-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI offense suppressed (<= 2 goals)
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV07CHICAR-CHI5|yes; why: KXNHLTEAMTOTAL-26NOV07CHICAR-CHI5|yes has the higher standalone adjusted growth (7.40 vs 2.83 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.175); relationships: KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.20, CAR shot control · high event (8+) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15.
- thesis CAR:SUPPRESSED (p 0.2461): highest fidelity KXNHLSPREAD-26NOV07CHICAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.2753): highest fidelity KXNHLTEAMTOTAL-26NOV07CHICAR-CHI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07CHICAR-CAR3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.313): highest fidelity KXNHLSPREAD-26NOV07CHICAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07CHICAR-CAR3|no (same contract)
- KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.159)
- KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.5519, phi -0.228)
- KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.253)
- KXNHLGOAL-26NOV07CHICAR-CHIFNAZAR91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.253)

portfolios: A EV +4.47 (adj +0.72) on $14.90, P(profit) 0.5763, adj growth 5.8 bp · B EV +3.34 (adj +2.12) on $15.97, P(profit) 0.3704, adj growth 19.9 bp · C EV +3.40 (adj +1.48) on $19.86, P(profit) 0.7442, adj growth 13.8 bp · R EV +0.32 (adj +0.21) on $3.00, P(profit) 0.7034, adj growth 8.1 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07CHICAR-CHI|yes == KXNHLGAME-26NOV07CHICAR-CAR|no

## SJS @ DAL  ·  10000 joint draws  ·  436 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_SJS_win | p_overtime | goals | shots DAL/SJS | DAL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.71 | 0.29 | 0.00 | 5.97 | 26.7/26.2 | 23.6/22.3 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.112 | 0.75 | 0.25 | 0.00 | 6.01 | 31.4/20.5 | 18.2/26.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.52 | 0.48 | 0.47 | 6.02 | 26.6/26.3 | 23.0/23.2 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.59 | 0.41 | 0.48 | 5.9 | 31.7/21.0 | 17.9/27.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.69 | 0.31 | 0.00 | 9.21 | 28.1/27.6 | 22.8/21.2 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.074 | 0.78 | 0.22 | 0.00 | 9.28 | 33.4/22.0 | 17.8/25.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Gaudette: 1+ goals YES | 9 | 0.125 | 0.111 | +0.029 | +0.016 | $1.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 1+ goals NO | 63 | 0.684 | 0.669 | +0.038 | +0.023 | $7.33 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 72 | 0.794 | 0.749 | +0.060 | +0.015 | $8.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| San Jose over 2.5 goals scored YES | 43 | 0.508 | 0.464 | +0.061 | +0.017 | $3.64 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Adam Gaudette: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes; why: higher confidence-adjusted growth (6.04 vs 5.94 bp); despite a smaller raw edge (+0.029 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.96 vs 0.553); relationships: KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes: REINFORCING (phi 0.195); failure: SJS offense suppressed (<= 2 goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no; why: higher confidence-adjusted growth (5.05 vs 2.58 bp); despite a smaller raw edge (+0.038 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.01 vs 0.846); relationships: KXNHLGOAL-26NOV07SJDAL-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: DAL offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (2.65 vs 0.06 bp); alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07SJDAL-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes: INTENTIONAL_DIVERSIFIER (phi -0.216); failure: SJS offense succeeds (4+ goals)
- **San Jose over 2.5 goals scored YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes selected over broad KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.49 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV07SJDAL-SJAGAUDETTE81-1|yes: REINFORCING (phi 0.195); KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.216); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.2809): highest fidelity KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes (same contract)
- thesis SJS:WINS_BY_2PLUS (p 0.1721): highest fidelity KXNHLSPREAD-26NOV07SJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS (p 0.3632): highest fidelity KXNHLSPREAD-26NOV07SJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07SJDAL-SJAGAUDETTE81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.5008, phi -0.194)
- KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4881, phi -0.233)
- KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.2809, phi -0.212)
- KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis SJS:SUPPRESSED (p 0.5008, phi -0.982)
- override: Broad expression KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes selected over broad KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.49 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.91 (adj +0.41) on $14.90, P(profit) 0.5939, adj growth 3.8 bp · B EV +2.10 (adj +0.82) on $21.32, P(profit) 0.6002, adj growth 7.8 bp · C EV +3.15 (adj +1.15) on $28.32, P(profit) 0.6122, adj growth 10.6 bp · R EV +0.25 (adj +0.11) on $3.00, P(profit) 0.684, adj growth 4.1 bp

## TBL @ MIN  ·  10000 joint draws  ·  420 bet sides mapped, 9 +EV candidates, 4 on card


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
| Yakov Trenin: 1+ goals YES | 9 | 0.138 | 0.124 | +0.043 | +0.028 | $3.10 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Blake Coleman: 1+ goals YES | 19 | 0.249 | 0.232 | +0.049 | +0.031 | $4.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Bobby Brink: 1+ goals YES | 14 | 0.184 | 0.171 | +0.036 | +0.022 | $2.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ assists NO | 37 | 0.458 | 0.411 | +0.071 | +0.025 | $5.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.68) | EVIDENCE_MIXED | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (19.31 vs 13.16 bp); despite a smaller raw edge (+0.043 vs +0.049/contract); relationships: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); failure: MIN offense suppressed (<= 2 goals)
- **Blake Coleman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (13.16 vs 8.31 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: MIN offense suppressed (<= 2 goals)
- **Bobby Brink: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes has the higher standalone adjusted growth (13.16 vs 8.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.082); failure: MIN offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07TBMIN-MINMBOLDY12-1|no; why: higher confidence-adjusted growth (5.77 vs 4.13 bp); despite a smaller raw edge (+0.071 vs +0.104/contract); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.082); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.3695): highest fidelity KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.4098): highest fidelity KXNHLAST-26NOV07TBMIN-MINMBOLDY12-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4098, phi -0.169)
- KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4098, phi -0.247)
- KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4098, phi -0.209)
- KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 32% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3695, phi -0.326)

portfolios: A EV +2.73 (adj +1.04) on $14.90, P(profit) 0.5749, adj growth 9.9 bp · B EV +4.14 (adj +2.36) on $15.86, P(profit) 0.4689, adj growth 22.1 bp · C EV +2.82 (adj +1.43) on $13.34, P(profit) 0.6119, adj growth 13.1 bp · R EV +0.45 (adj +0.29) on $1.00, P(profit) 0.1384, adj growth 10.7 bp

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

## PIT @ LAK  ·  10000 joint draws  ·  432 bet sides mapped, 3 +EV candidates, 3 on card


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
| Connor Dewar: 1+ goals YES | 12 | 0.159 | 0.148 | +0.031 | +0.020 | $2.36 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 9 | 0.124 | 0.112 | +0.028 | +0.016 | $1.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.076 | 0.064 | +0.022 | +0.011 | $1.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (7.99 vs 6.37 bp); relationships: KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes has the higher standalone adjusted growth (7.99 vs 6.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.036); failure: LAK wins (incl. OT/SO)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07PITLA-LATMOORE12-1|yes; why: higher confidence-adjusted growth (5.01 vs 1.08 bp); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.036); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.2396): highest fidelity KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.431): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4218, phi -0.198)
- KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:WINS (p 0.5534, phi -0.191)
- KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3524, phi -0.128)

portfolios: A EV +2.07 (adj +1.17) on $6.75, P(profit) 0.319, adj growth 10.7 bp · B EV +1.56 (adj +0.90) on $5.22, P(profit) 0.319, adj growth 8.4 bp · C EV +0.85 (adj +0.55) on $3.48, P(profit) 0.1586, adj growth 5.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ EDM  ·  10000 joint draws  ·  434 bet sides mapped, 12 +EV candidates, 4 on card


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
| Marco Rossi: 1+ goals YES | 17 | 0.215 | 0.201 | +0.035 | +0.021 | $2.38 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Drew O'Connor: 1+ goals YES | 13 | 0.167 | 0.157 | +0.029 | +0.019 | $2.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Edmonton wins by over 2.5 goals NO | 58 | 0.669 | 0.622 | +0.072 | +0.025 | $6.85 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 27 | 0.315 | 0.300 | +0.031 | +0.016 | $3.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07VANEDM-EDM2|no; why: higher confidence-adjusted growth (6.51 vs 6.13 bp); despite a smaller raw edge (+0.035 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07VANEDM-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26NOV07VANEDM-EDM3|no: MOSTLY_INDEPENDENT (phi 0.13); KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: VAN offense suppressed (<= 2 goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07VANEDM-EDM2|no; why: higher confidence-adjusted growth (6.37 vs 6.13 bp); despite a smaller raw edge (+0.029 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07VANEDM-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26NOV07VANEDM-EDM3|no: MOSTLY_INDEPENDENT (phi 0.107); KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: VAN offense suppressed (<= 2 goals)
- **Edmonton wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV07VANEDM-EDM2|no; why: Broad expression KXNHLSPREAD-26NOV07VANEDM-EDM3|no selected over player prop KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV07VANEDM-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.13); KXNHLGOAL-26NOV07VANEDM-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.107); KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.183); failure: EDM wins by 2+
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (2.76 vs 0.05 bp); despite a smaller raw edge (+0.031 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0023 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07VANEDM-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV07VANEDM-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLSPREAD-26NOV07VANEDM-EDM3|no: INTENTIONAL_DIVERSIFIER (phi -0.183); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.15, EDM shot control · high event (8+) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.338): highest fidelity KXNHLTEAMTOTAL-26NOV07VANEDM-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07VANEDM-EDM2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.3772): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07VANEDM-EDM2|no (same contract)
- thesis EDM:SUPPRESSED (p 0.2262): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07VANEDM-EDM2|no — Broad expression KXNHLSPREAD-26NOV07VANEDM-EDM3|no selected over player prop KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26NOV07VANEDM-VANMROSSI23-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4419, phi -0.225)
- KXNHLGOAL-26NOV07VANEDM-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4419, phi -0.194)
- KXNHLSPREAD-26NOV07VANEDM-EDM3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis EDM:WINS_BY_2PLUS (p 0.4575, phi -0.765)
- KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2262, phi -0.206)
- override: Broad expression KXNHLSPREAD-26NOV07VANEDM-EDM3|no selected over player prop KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.24 (adj +0.63) on $14.90, P(profit) 0.626, adj growth 5.7 bp · B EV +2.04 (adj +1.01) on $14.24, P(profit) 0.4201, adj growth 9.5 bp · C EV +2.02 (adj +0.80) on $14.10, P(profit) 0.735, adj growth 7.3 bp · R EV +0.24 (adj +0.08) on $2.00, P(profit) 0.6695, adj growth 3.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
