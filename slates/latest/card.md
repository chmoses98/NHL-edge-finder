# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-07T17:46:23Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.51 | +9.40 | +26.07 | 0.742 | -23.06 | -35.73 | 86.22 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +26.07 | +13.96 | +24.33 | 0.735 | -23.27 | -35.41 | 131.74 |
| C best expression per thesis | 150.00 | +22.98 | +10.72 | +21.65 | 0.710 | -26.07 | -38.52 | 99.61 |
| R FUNDED research stakes | 19.00 | +2.73 | +1.40 | +1.89 | 0.617 | -6.04 | -8.29 | 0.00 |

## STL @ NSH  ·  10000 joint draws  ·  414 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_STL_win | p_overtime | goals | shots NSH/STL | NSH/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.48 | 0.52 | 0.00 | 6.03 | 27.8/27.8 | 24.1/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.48 | 5.89 | 27.8/27.9 | 24.6/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.48 | 0.52 | 0.00 | 9.29 | 29.0/29.2 | 22.9/22.8 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.067 | 0.54 | 0.46 | 0.00 | 6.02 | 32.7/22.0 | 18.8/28.9 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.067 | 0.44 | 0.56 | 0.00 | 6.06 | 22.1/32.5 | 28.4/18.7 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.53 | 0.47 | 0.47 | 5.98 | 33.0/22.4 | 19.1/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Edstrom: 1+ goals YES | 15 | 0.200 | 0.186 | +0.041 | +0.027 | $3.14 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Justin Barron: 1+ goals YES | 5 | 0.073 | 0.067 | +0.020 | +0.014 | $1.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 25 | 0.304 | 0.289 | +0.041 | +0.026 | $4.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ assists NO | 70 | 0.777 | 0.731 | +0.062 | +0.016 | $8.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (11.89 vs 7.82 bp); despite a smaller raw edge (+0.041 vs +0.041/contract); relationships: KXNHLGOAL-26NOV07STLNSH-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26NOV07STLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.033); failure: NSH offense suppressed (<= 2 goals)
- **Justin Barron: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV07STLNSH-10|yes; why: higher confidence-adjusted growth (8.08 vs 4.58 bp); despite a smaller raw edge (+0.020 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.911 vs 0.325); relationships: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV07STLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: STL offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (11.89 vs 7.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07STLNSH-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV07STLNSH-NSHMBOURQUE22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.174); failure: NSH offense suppressed (<= 2 goals)
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV07STLNSH-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (2.90 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26NOV07STLNSH-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.174); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NSH:OFFENSE_4PLUS (p 0.3862): highest fidelity KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.3996): highest fidelity KXNHLGOAL-26NOV07STLNSH-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07STLNSH-STLRTHOMAS18-1|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.2757): highest fidelity KXNHLTOTAL-26NOV07STLNSH-10|yes [FRAGILE], best adjusted EV KXNHLTOTAL-26NOV07STLNSH-10|yes (same contract)
- KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3979, phi -0.231)
- KXNHLGOAL-26NOV07STLNSH-STLJBARRON72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3821, phi -0.108)
- KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3979, phi -0.233)
- KXNHLAST-26NOV07STLNSH-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3862, phi -0.204)

portfolios: A EV +3.09 (adj +1.49) on $15.00, P(profit) 0.4111, adj growth 13.6 bp · B EV +2.66 (adj +1.48) on $16.85, P(profit) 0.4096, adj growth 14.0 bp · C EV +2.58 (adj +1.16) on $15.80, P(profit) 0.2627, adj growth 10.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYR @ SEA  ·  10000 joint draws  ·  442 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.451 / away 0.549

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
| Ben Meyers: 1+ goals YES | 10 | 0.150 | 0.136 | +0.044 | +0.030 | $3.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| New York R wins by over 1.5 goals NO | 66 | 0.753 | 0.704 | +0.077 | +0.028 | $7.25 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ goals NO | 66 | 0.712 | 0.696 | +0.036 | +0.020 | $5.44 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Jani Nyman: 1+ goals YES | 12 | 0.153 | 0.141 | +0.026 | +0.014 | $1.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: higher confidence-adjusted growth (20.17 vs 7.95 bp); despite a smaller raw edge (+0.044 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: MOSTLY_INDEPENDENT (phi 0.086); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV07NYRSEA-SEAJNYMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: SEA offense suppressed (<= 2 goals)
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

portfolios: A EV +2.13 (adj +0.69) on $15.00, P(profit) 0.4692, adj growth 6.3 bp · B EV +2.63 (adj +1.46) on $17.04, P(profit) 0.6561, adj growth 13.8 bp · C EV +1.29 (adj +0.47) on $11.28, P(profit) 0.7527, adj growth 4.4 bp · R EV +0.33 (adj +0.14) on $4.00, P(profit) 0.5642, adj growth 5.4 bp

## MTL @ TOR  ·  10000 joint draws  ·  420 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.474 / away 0.526

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_MTL_win | p_overtime | goals | shots TOR/MTL | TOR/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.57 | 0.43 | 0.00 | 6.11 | 28.9/29.0 | 25.7/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.117 | 0.53 | 0.47 | 0.00 | 9.52 | 30.6/30.5 | 24.3/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.47 | 6.06 | 28.8/29.0 | 25.6/25.4 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.070 | 0.46 | 0.54 | 0.00 | 6.06 | 23.1/34.3 | 30.3/19.9 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.065 | 0.58 | 0.42 | 0.00 | 6.1 | 33.9/23.1 | 20.0/29.6 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.058 | 0.49 | 0.51 | 0.48 | 5.93 | 23.3/34.1 | 30.5/20.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.162 | 0.143 | +0.045 | +0.026 | $2.65 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Nick Suzuki: 1+ assists NO | 48 | 0.617 | 0.522 | +0.120 | +0.024 | $3.93 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
| Nick Suzuki: 2+ assists NO | 85 | 0.917 | 0.873 | +0.058 | +0.015 | $8.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07MTLTOR-MTL2|no; why: higher confidence-adjusted growth (13.98 vs 0.77 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-2|no: MOSTLY_INDEPENDENT (phi 0.009); failure: TOR offense suppressed (<= 2 goals)
- **Nick Suzuki: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07MTLTOR-MTL2|no; why: higher confidence-adjusted growth (5.09 vs 0.77 bp); alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-2|no: DUPLICATIVE (phi 0.383); failure: MTL offense succeeds (4+ goals)
- **Nick Suzuki: 2+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no; why: second expression of the same thesis: KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no has the higher standalone adjusted growth (5.09 vs 3.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.383); they share one thesis budget; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: DUPLICATIVE (phi 0.383); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.4639): highest fidelity KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.3656): highest fidelity KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no (same contract)
- KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3258, phi -0.186)
- KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.7 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4178, phi -0.266)
- KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4178, phi -0.236)

portfolios: A EV +3.16 (adj +1.18) on $15.00, P(profit) 0.6778, adj growth 10.9 bp · B EV +2.53 (adj +0.92) on $14.88, P(profit) 0.6778, adj growth 8.7 bp · C EV +3.06 (adj +1.14) on $10.50, P(profit) 0.6778, adj growth 10.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ OTT  ·  10000 joint draws  ·  434 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.478 / away 0.522

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
| Lawson Crouse: 1+ goals YES | 16 | 0.212 | 0.197 | +0.043 | +0.027 | $3.17 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 16 | 0.201 | 0.187 | +0.032 | +0.018 | $2.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Dylan Cozens: 1+ goals YES | 25 | 0.298 | 0.283 | +0.035 | +0.020 | $2.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Fabian Zetterlund: 1+ goals YES | 20 | 0.240 | 0.227 | +0.029 | +0.016 | $2.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-UTAALEE72-1|yes; why: higher confidence-adjusted growth (11.43 vs 0.17 bp); alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07UTAOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: UTA offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes; why: higher confidence-adjusted growth (4.89 vs 4.62 bp); despite a smaller raw edge (+0.032 vs +0.035/contract); relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07UTAOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: OTT offense suppressed (<= 2 goals)
- **Dylan Cozens: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (4.89 vs 4.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07UTAOTT-OTTFZETTERLUND20-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense suppressed (<= 2 goals)
- **Fabian Zetterlund: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (4.89 vs 3.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.3923): highest fidelity KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4332): highest fidelity KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3856): highest fidelity KXNHLGOAL-26NOV07UTAOTT-UTALCOOLEY92-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-UTALCOOLEY92-1|no (same contract)
- KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3856, phi -0.214)
- KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.351, phi -0.199)
- KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.351, phi -0.223)
- KXNHLGOAL-26NOV07UTAOTT-OTTFZETTERLUND20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.351, phi -0.211)

portfolios: A EV +2.07 (adj +1.24) on $15.00, P(profit) 0.5091, adj growth 11.6 bp · B EV +1.84 (adj +1.10) on $10.05, P(profit) 0.5605, adj growth 10.4 bp · C EV +1.97 (adj +1.19) on $15.03, P(profit) 0.3718, adj growth 11.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ NYI  ·  10000 joint draws  ·  430 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.428 / away 0.572

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_NJD_win | p_overtime | goals | shots NYI/NJD | NYI/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.55 | 0.45 | 0.00 | 6.0 | 27.6/28.0 | 24.5/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.51 | 0.49 | 0.48 | 5.94 | 27.6/28.0 | 24.6/24.3 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.086 | 0.49 | 0.51 | 0.00 | 6.0 | 22.0/33.0 | 29.1/18.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.55 | 0.45 | 0.00 | 9.17 | 29.0/29.2 | 23.6/22.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.46 | 0.54 | 0.47 | 5.92 | 21.9/33.0 | 29.5/18.6 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.055 | 0.60 | 0.40 | 0.00 | 6.03 | 32.2/22.3 | 19.2/28.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York I wins by over 1.5 goals YES | 22 | 0.298 | 0.257 | +0.066 | +0.025 | $2.05 | FUNDED_RESEARCH | $1 | NYI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins by over 1.5 goals NO | 65 | 0.739 | 0.692 | +0.073 | +0.026 | $7.04 | FUNDED_RESEARCH | $2 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Cody Glass: 1+ goals YES | 11 | 0.140 | 0.132 | +0.023 | +0.015 | $2.00 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.253 | 0.239 | +0.031 | +0.018 | $1.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **New York I wins by over 1.5 goals YES** — thesis: NYI wins by 2+; alternative: KXNHLSPREAD-26NOV07NJNYI-NJ2|no; why: higher confidence-adjusted growth (7.33 vs 6.72 bp); despite a smaller raw edge (+0.066 vs +0.073/contract); relationships: KXNHLSPREAD-26NOV07NJNYI-NJ2|no: DUPLICATIVE (phi 0.387); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: REINFORCING (phi 0.177); failure: NJD wins (incl. OT/SO)
- **New Jersey wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV07NJNYI-NYI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NJNYI-NYI2|yes has the higher standalone adjusted growth (7.33 vs 6.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.387); they share one thesis budget; relationships: KXNHLSPREAD-26NOV07NJNYI-NYI2|yes: DUPLICATIVE (phi 0.387); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.148); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.148); failure: NJD wins by 2+
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07NJNYI-NJCBROWN16-1|yes; why: higher confidence-adjusted growth (4.47 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLSPREAD-26NOV07NJNYI-NYI2|yes: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLSPREAD-26NOV07NJNYI-NJ2|no: INTENTIONAL_DIVERSIFIER (phi -0.148); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: NJD offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NJNYI-NYI2|yes; why: Player prop expression KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes selected over player prop KXNHLAST-26NOV07NJNYI-NYIEHEINEMAN51-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.38 vs 0.44 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26NOV07NJNYI-NYI2|yes: REINFORCING (phi 0.177); KXNHLSPREAD-26NOV07NJNYI-NJ2|no: MOSTLY_INDEPENDENT (phi 0.148); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:WINS_BY_2PLUS (p 0.2981): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no (same contract)
- thesis NYI:WINS (p 0.5198): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3918): highest fidelity KXNHLTEAMTOTAL-26NOV07NJNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no — Player prop expression KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes selected over player prop KXNHLAST-26NOV07NJNYI-NYIEHEINEMAN51-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.38 vs 0.44 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLSPREAD-26NOV07NJNYI-NYI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.4802, phi -0.626)
- KXNHLSPREAD-26NOV07NJNYI-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.261, phi -1.0)
- KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4138, phi -0.177)
- KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.384, phi -0.241)
- override: Player prop expression KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes selected over player prop KXNHLAST-26NOV07NJNYI-NYIEHEINEMAN51-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.38 vs 0.44 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.15 (adj +0.70) on $15.00, P(profit) 0.5679, adj growth 6.5 bp · B EV +1.98 (adj +0.87) on $12.65, P(profit) 0.5033, adj growth 8.2 bp · C EV +1.15 (adj +0.43) on $4.04, P(profit) 0.2981, adj growth 4.0 bp · R EV +0.50 (adj +0.18) on $3.00, P(profit) 0.739, adj growth 6.8 bp

## CHI @ CAR  ·  10000 joint draws  ·  462 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.783 / away 0.217

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
| Sebastian Aho: 1+ goals NO | 61 | 0.703 | 0.679 | +0.077 | +0.052 | $8.30 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Dillon Boucher: 1+ goals YES | 5 | 0.089 | 0.077 | +0.036 | +0.024 | $2.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 18 | 0.243 | 0.225 | +0.053 | +0.034 | $4.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 12 | 0.153 | 0.143 | +0.026 | +0.015 | $1.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07CHICAR-CHI2|yes; why: higher confidence-adjusted growth (25.60 vs 8.09 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.032 vs 0.626); relationships: KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: CAR offense succeeds (4+ goals)
- **Dillon Boucher: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (23.40 vs 16.55 bp); despite a smaller raw edge (+0.036 vs +0.053/contract); relationships: KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07CHICAR-CHI2|yes; why: higher confidence-adjusted growth (16.55 vs 8.09 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.935 vs 0.626); relationships: KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CHI offense suppressed (<= 2 goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (16.55 vs 4.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.20, CAR shot control · high event (8+) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15.
- thesis CAR:SUPPRESSED (p 0.2461): highest fidelity KXNHLSPREAD-26NOV07CHICAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.2753): highest fidelity KXNHLTEAMTOTAL-26NOV07CHICAR-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS_BY_2PLUS (p 0.1426): highest fidelity KXNHLSPREAD-26NOV07CHICAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07CHICAR-CAR2|no (same contract)
- KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.5519, phi -0.228)
- KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.159)
- KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.253)
- KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.178)

portfolios: A EV +3.81 (adj +0.74) on $15.00, P(profit) 0.5271, adj growth 6.3 bp · B EV +3.97 (adj +2.60) on $16.30, P(profit) 0.3833, adj growth 24.6 bp · C EV +3.94 (adj +2.22) on $19.71, P(profit) 0.5266, adj growth 20.8 bp · R EV +0.37 (adj +0.25) on $3.00, P(profit) 0.7034, adj growth 9.6 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07CHICAR-CAR|no == KXNHLGAME-26NOV07CHICAR-CHI|yes

## SJS @ DAL  ·  10000 joint draws  ·  444 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.722 / away 0.278

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_SJS_win | p_overtime | goals | shots DAL/SJS | DAL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.68 | 0.32 | 0.00 | 6.01 | 26.6/26.2 | 23.5/22.2 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.114 | 0.75 | 0.25 | 0.00 | 6.01 | 31.5/20.6 | 18.3/26.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.54 | 0.46 | 0.44 | 5.93 | 26.4/26.0 | 22.9/23.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.57 | 0.43 | 0.45 | 5.87 | 31.5/21.0 | 17.8/28.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.69 | 0.31 | 0.00 | 9.23 | 28.2/27.6 | 22.7/21.2 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.073 | 0.78 | 0.22 | 0.00 | 9.22 | 33.6/21.9 | 17.9/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Adam Gaudette: 1+ goals YES | 9 | 0.125 | 0.112 | +0.029 | +0.017 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 1+ goals NO | 63 | 0.688 | 0.672 | +0.041 | +0.026 | $6.83 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 72 | 0.797 | 0.751 | +0.063 | +0.017 | $8.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 48 | 0.592 | 0.516 | +0.095 | +0.018 | $3.25 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Adam Gaudette: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07SJDAL-SJ2|yes; why: higher confidence-adjusted growth (6.85 vs 3.85 bp); despite a smaller raw edge (+0.029 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.963 vs 0.56); relationships: KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26NOV07SJDAL-DAL2|no: MOSTLY_INDEPENDENT (phi 0.105); failure: SJS offense suppressed (<= 2 goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07SJDAL-SJ2|yes; why: higher confidence-adjusted growth (6.28 vs 3.85 bp); despite a smaller raw edge (+0.041 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.01 vs 0.56); relationships: KXNHLGOAL-26NOV07SJDAL-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLSPREAD-26NOV07SJDAL-DAL2|no: MOSTLY_INDEPENDENT (phi 0.149); failure: DAL offense succeeds (4+ goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV07SJDAL-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (3.23 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07SJDAL-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLSPREAD-26NOV07SJDAL-DAL2|no: INTENTIONAL_DIVERSIFIER (phi -0.131); failure: SJS offense succeeds (4+ goals)
- **Dallas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV07SJDAL-DAL3|no; why: higher confidence-adjusted growth (3.00 vs 1.21 bp); relationships: KXNHLGOAL-26NOV07SJDAL-SJAGAUDETTE81-1|yes: MOSTLY_INDEPENDENT (phi 0.105); KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.131); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis DAL:SUPPRESSED (p 0.3123): highest fidelity KXNHLSPREAD-26NOV07SJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:OFFENSE_4PLUS (p 0.2843): highest fidelity KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07SJDAL-DAL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:WINS_BY_2PLUS (p 0.1799): highest fidelity KXNHLSPREAD-26NOV07SJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07SJDAL-DAL2|no (same contract)
- KXNHLGOAL-26NOV07SJDAL-SJAGAUDETTE81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4988, phi -0.171)
- KXNHLGOAL-26NOV07SJDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4779, phi -0.223)
- KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.2843, phi -0.212)
- KXNHLSPREAD-26NOV07SJDAL-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.7 pts; opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.4079, phi -1.0)

portfolios: A EV +2.60 (adj +0.44) on $15.00, P(profit) 0.5454, adj growth 3.8 bp · B EV +2.24 (adj +0.86) on $19.86, P(profit) 0.6023, adj growth 8.1 bp · C EV +2.68 (adj +0.90) on $25.20, P(profit) 0.6164, adj growth 8.4 bp · R EV +0.32 (adj +0.12) on $3.00, P(profit) 0.6875, adj growth 4.4 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07SJDAL-SJ|yes == KXNHLGAME-26NOV07SJDAL-DAL|no

## TBL @ MIN  ·  10000 joint draws  ·  420 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.448 / away 0.552

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_TBL_win | p_overtime | goals | shots MIN/TBL | MIN/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.124 | 0.50 | 0.50 | 0.50 | 6.0 | 27.8/27.9 | 24.6/24.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.48 | 0.52 | 0.00 | 6.0 | 27.6/27.9 | 24.3/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.47 | 0.53 | 0.00 | 9.45 | 29.5/29.6 | 23.1/23.4 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.073 | 0.40 | 0.60 | 0.00 | 5.99 | 22.0/32.8 | 28.7/19.1 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.48 | 0.52 | 0.47 | 5.96 | 22.5/33.0 | 29.8/19.2 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.059 | 0.48 | 0.52 | 0.00 | 6.04 | 32.2/22.0 | 18.4/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 9 | 0.138 | 0.125 | +0.043 | +0.029 | $2.97 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Bobby Brink: 1+ goals YES | 14 | 0.187 | 0.170 | +0.038 | +0.022 | $2.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ assists NO | 53 | 0.615 | 0.568 | +0.068 | +0.020 | $5.68 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Ryan Hartman: 1+ goals YES | 15 | 0.183 | 0.172 | +0.024 | +0.013 | $1.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (20.94 vs 7.96 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26NOV07TBMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26NOV07TBMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: MIN offense suppressed (<= 2 goals)
- **Bobby Brink: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINDYUROV22-1|yes; why: higher confidence-adjusted growth (7.96 vs 2.25 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26NOV07TBMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26NOV07TBMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: MIN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no; why: higher confidence-adjusted growth (3.54 vs 3.04 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26NOV07TBMIN-MINRHARTMAN38-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.103); failure: MIN offense succeeds (4+ goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes has the higher standalone adjusted growth (7.96 vs 2.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26NOV07TBMIN-MINKKAPRIZOV97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.103); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:OFFENSE_4PLUS (p 0.384): highest fidelity KXNHLGOAL-26NOV07TBMIN-MINDYUROV22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.388): highest fidelity KXNHLAST-26NOV07TBMIN-MINMBOLDY12-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07TBMIN-MINKKAPRIZOV97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.388, phi -0.169)
- KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.388, phi -0.203)
- KXNHLAST-26NOV07TBMIN-MINKKAPRIZOV97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.384, phi -0.287)
- KXNHLGOAL-26NOV07TBMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.388, phi -0.179)

portfolios: A EV +2.93 (adj +1.23) on $15.00, P(profit) 0.6302, adj growth 11.6 bp · B EV +2.91 (adj +1.61) on $12.80, P(profit) 0.3629, adj growth 15.2 bp · C EV +1.71 (adj +0.74) on $10.18, P(profit) 0.6954, adj growth 6.8 bp · R EV +0.44 (adj +0.31) on $1.00, P(profit) 0.1383, adj growth 11.2 bp

## DET @ COL  ·  10000 joint draws  ·  452 bet sides mapped, 0 +EV candidates, 0 on card

sportsbook moneyline consensus (5 books): home 0.664 / away 0.336

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

## PIT @ LAK  ·  10000 joint draws  ·  432 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.529 / away 0.471

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
| Joel Edmundson: 1+ goals YES | 5 | 0.076 | 0.069 | +0.022 | +0.016 | $1.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 12 | 0.159 | 0.148 | +0.031 | +0.020 | $2.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 9 | 0.124 | 0.112 | +0.028 | +0.016 | $1.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ goals NO | 77 | 0.809 | 0.798 | +0.027 | +0.016 | $7.94 | FUNDED_RESEARCH | $2 | PIT:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07PITLA-LATMOORE12-1|yes; why: higher confidence-adjusted growth (10.57 vs 1.08 bp); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: LAK offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (7.99 vs 6.37 bp); relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes has the higher standalone adjusted growth (7.99 vs 6.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: LAK wins (incl. OT/SO)
- **Ben Kindel: 1+ goals NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07PITLA-PIT2|no; why: higher confidence-adjusted growth (3.24 vs 0.14 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: PIT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.2396): highest fidelity KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes (same contract)
- thesis PIT:SUPPRESSED (p 0.4218): highest fidelity KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no (same contract)
- thesis LAK:SUPPRESSED (p 0.3524): highest fidelity KXNHLGOAL-26NOV07PITLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07PITLA-LAAPANARIN10-1|no (same contract)
- KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3524, phi -0.128)
- KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4218, phi -0.198)
- KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:WINS (p 0.5534, phi -0.191)
- KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3516, phi -0.212)

portfolios: A EV +1.59 (adj +0.95) on $15.00, P(profit) 0.261, adj growth 8.9 bp · B EV +1.97 (adj +1.27) on $13.41, P(profit) 0.319, adj growth 11.9 bp · C EV +1.37 (adj +0.84) on $19.75, P(profit) 0.6241, adj growth 7.8 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.8093, adj growth 1.5 bp

## VAN @ EDM  ·  10000 joint draws  ·  418 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.748 / away 0.252

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_VAN_win | p_overtime | goals | shots EDM/VAN | EDM/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.146 | 0.79 | 0.21 | 0.00 | 6.1 | 33.1/21.0 | 18.8/27.7 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.137 | 0.78 | 0.22 | 0.00 | 9.37 | 34.7/22.3 | 18.3/26.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.71 | 0.29 | 0.00 | 9.58 | 29.3/28.3 | 23.3/21.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.099 | 0.70 | 0.30 | 0.00 | 6.07 | 27.3/26.7 | 24.2/22.6 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.57 | 0.43 | 0.49 | 6.06 | 33.7/21.5 | 18.2/30.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.50 | 0.50 | 0.48 | 6.08 | 27.5/26.7 | 23.3/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brendan Gallagher: 1+ goals YES | 10 | 0.146 | 0.132 | +0.040 | +0.026 | $2.44 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 27 | 0.337 | 0.316 | +0.053 | +0.033 | $5.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Edmonton wins by over 1.5 goals NO | 45 | 0.542 | 0.494 | +0.075 | +0.026 | $6.44 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ goals YES | 12 | 0.154 | 0.141 | +0.026 | +0.014 | $1.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (15.10 vs 6.20 bp); relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26NOV07VANEDM-EDM2|no: MOSTLY_INDEPENDENT (phi 0.139); KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: VAN offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07VANEDM-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (11.31 vs 3.01 bp); despite a smaller raw edge (+0.053 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26NOV07VANEDM-EDM2|no: INTENTIONAL_DIVERSIFIER (phi -0.212); KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: EDM offense suppressed (<= 2 goals)
- **Edmonton wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV07VANEDM-EDM3|no; why: higher confidence-adjusted growth (6.13 vs 5.79 bp); relationships: KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.139); KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.212); KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.133); failure: EDM wins by 2+
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (11.31 vs 3.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26NOV07VANEDM-EDM2|no: INTENTIONAL_DIVERSIFIER (phi -0.133); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.15, EDM shot control · high event (8+) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.5893): highest fidelity KXNHLAST-26NOV07VANEDM-EDMMEKHOLM14-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.338): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV07VANEDM-EDM2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.3772): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07VANEDM-EDM2|no (same contract)
- KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4419, phi -0.185)
- KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2262, phi -0.228)
- KXNHLSPREAD-26NOV07VANEDM-EDM2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis EDM:WINS_BY_2PLUS (p 0.4575, phi -1.0)
- KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2262, phi -0.141)

portfolios: A EV +2.98 (adj +0.74) on $15.00, P(profit) 0.4791, adj growth 6.6 bp · B EV +3.35 (adj +1.79) on $16.16, P(profit) 0.4725, adj growth 16.9 bp · C EV +3.25 (adj +1.63) on $18.51, P(profit) 0.4418, adj growth 15.1 bp · R EV +0.70 (adj +0.36) on $3.00, P(profit) 0.585, adj growth 12.9 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07VANEDM-VAN|yes == KXNHLGAME-26NOV07VANEDM-EDM|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
