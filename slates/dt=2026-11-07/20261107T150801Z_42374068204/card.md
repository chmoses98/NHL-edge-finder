# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-07T15:08:01Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.07 | +8.82 | +25.36 | 0.763 | -20.36 | -31.86 | 81.71 |
| B thesis-diversified (joint) ← optimiser card | 148.39 | +27.00 | +12.87 | +25.56 | 0.751 | -20.52 | -32.63 | 121.45 |
| C best expression per thesis | 150.01 | +26.14 | +11.73 | +24.07 | 0.714 | -27.93 | -39.59 | 108.26 |
| R FUNDED research stakes | 23.00 | +3.24 | +1.53 | +2.68 | 0.641 | -5.87 | -8.23 | 0.00 |

## FLA @ WSH  ·  10000 joint draws  ·  448 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_FLA_win | p_overtime | goals | shots WSH/FLA | WSH/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.61 | 0.39 | 0.00 | 6.0 | 26.9/27.1 | 24.0/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.49 | 0.51 | 0.49 | 5.96 | 26.8/27.0 | 23.7/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.58 | 0.42 | 0.00 | 9.4 | 28.5/28.7 | 23.0/21.6 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.072 | 0.57 | 0.43 | 0.00 | 5.98 | 21.4/31.8 | 28.5/17.8 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.54 | 0.46 | 0.42 | 6.02 | 21.5/31.7 | 28.2/18.3 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.065 | 0.70 | 0.30 | 0.00 | 6.07 | 31.5/21.4 | 18.9/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 17 | 0.251 | 0.229 | +0.071 | +0.050 | $5.44 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 6 | 0.101 | 0.087 | +0.037 | +0.023 | $2.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Ryan Leonard: 1+ assists YES | 22 | 0.313 | 0.264 | +0.081 | +0.032 | $3.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_MIXED | D |
| Alex Ovechkin: 1+ assists YES | 22 | 0.311 | 0.263 | +0.079 | +0.031 | $3.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07FLAWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (35.41 vs 12.50 bp); despite a smaller raw edge (+0.071 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07FLAWSH-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV07FLAWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.057); KXNHLAST-26NOV07FLAWSH-WSHAOVECHKIN8-1|yes: MOSTLY_INDEPENDENT (phi 0.053); failure: WSH offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07FLAWSH-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (18.21 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV07FLAWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26NOV07FLAWSH-WSHAOVECHKIN8-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: FLA offense suppressed (<= 2 goals)
- **Ryan Leonard: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (35.41 vs 12.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.057); they share one thesis budget; relationships: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.057); KXNHLGOAL-26NOV07FLAWSH-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26NOV07FLAWSH-WSHAOVECHKIN8-1|yes: MOSTLY_INDEPENDENT (phi 0.03); failure: WSH offense suppressed (<= 2 goals)
- **Alex Ovechkin: 1+ assists YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (35.41 vs 11.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.053); they share one thesis budget; relationships: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.053); KXNHLGOAL-26NOV07FLAWSH-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26NOV07FLAWSH-WSHRLEONARD9-1|yes: MOSTLY_INDEPENDENT (phi 0.03); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4629): highest fidelity KXNHLAST-26NOV07FLAWSH-WSHAOVECHKIN8-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:WINS_BY_2PLUS (p 0.3469): highest fidelity KXNHLGOAL-26NOV07FLAWSH-FLASREINHART13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.424): highest fidelity KXNHLGOAL-26NOV07FLAWSH-FLASREINHART13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07FLAWSH-FLASREINHART13-1|no (same contract)
- KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3209, phi -0.227)
- KXNHLGOAL-26NOV07FLAWSH-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.424, phi -0.153)
- KXNHLAST-26NOV07FLAWSH-WSHRLEONARD9-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3209, phi -0.246)
- KXNHLAST-26NOV07FLAWSH-WSHAOVECHKIN8-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3209, phi -0.232)

portfolios: A EV +4.00 (adj +1.95) on $13.73, P(profit) 0.6253, adj growth 18.6 bp · B EV +5.68 (adj +3.17) on $14.28, P(profit) 0.5293, adj growth 29.7 bp · C EV +3.48 (adj +2.37) on $14.62, P(profit) 0.2508, adj growth 21.7 bp · R EV +0.79 (adj +0.55) on $2.00, P(profit) 0.2508, adj growth 20.2 bp

## STL @ NSH  ·  10000 joint draws  ·  406 bet sides mapped, 2 +EV candidates, 2 on card


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
| Adam Edstrom: 1+ goals YES | 16 | 0.203 | 0.188 | +0.033 | +0.019 | $2.16 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 26 | 0.304 | 0.290 | +0.030 | +0.017 | $2.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (5.39 vs 3.07 bp); relationships: KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.027); failure: NSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (5.39 vs 3.07 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.027); they share one thesis budget; relationships: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.027); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:OFFENSE_4PLUS (p 0.4005): highest fidelity KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3824, phi -0.22)
- KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3824, phi -0.243)

portfolios: A EV +0.85 (adj +0.48) on $5.58, P(profit) 0.4397, adj growth 4.4 bp · B EV +0.67 (adj +0.38) on $4.42, P(profit) 0.4397, adj growth 3.6 bp · C EV +0.61 (adj +0.34) on $3.12, P(profit) 0.2025, adj growth 3.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYR @ SEA  ·  10000 joint draws  ·  434 bet sides mapped, 8 +EV candidates, 4 on card


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
| Ben Meyers: 1+ goals YES | 10 | 0.150 | 0.131 | +0.044 | +0.025 | $2.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| New York R wins by over 1.5 goals NO | 67 | 0.753 | 0.709 | +0.067 | +0.023 | $5.97 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ryan Winterton: 1+ goals YES | 11 | 0.142 | 0.132 | +0.025 | +0.015 | $1.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 66 | 0.712 | 0.696 | +0.036 | +0.020 | $5.75 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: higher confidence-adjusted growth (14.08 vs 5.57 bp); despite a smaller raw edge (+0.044 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: MOSTLY_INDEPENDENT (phi 0.086); KXNHLGOAL-26NOV07NYRSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)
- **New York R wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV07NYRSEA-SEA2|yes; why: higher confidence-adjusted growth (5.57 vs 2.70 bp); wins across more scripts (relative breadth 0.973 vs 0.517); relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.086); KXNHLGOAL-26NOV07NYRSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.093); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.147); failure: NYR wins by 2+
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no has the higher standalone adjusted growth (5.57 vs 4.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.093); they share one thesis budget; relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: MOSTLY_INDEPENDENT (phi 0.093); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: SEA offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no has the higher standalone adjusted growth (5.57 vs 4.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.147); they share one thesis budget; relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26NOV07NYRSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4274): highest fidelity KXNHLTEAMTOTAL-26NOV07NYRSEA-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.5415): highest fidelity KXNHLSPREAD-26NOV07NYRSEA-NYR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no (same contract)
- thesis NYR:SUPPRESSED (p 0.4182): highest fidelity KXNHLSPREAD-26NOV07NYRSEA-NYR2|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no (same contract)
- KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3566, phi -0.17)
- KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYR:WINS_BY_2PLUS (p 0.2473, phi -1.0)
- KXNHLGOAL-26NOV07NYRSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3566, phi -0.166)
- KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3681, phi -0.246)

portfolios: A EV +1.76 (adj +0.53) on $13.73, P(profit) 0.4666, adj growth 4.7 bp · B EV +2.20 (adj +1.13) on $15.60, P(profit) 0.6575, adj growth 10.7 bp · C EV +1.16 (adj +0.40) on $11.80, P(profit) 0.7527, adj growth 3.7 bp · R EV +0.30 (adj +0.13) on $4.00, P(profit) 0.5642, adj growth 4.8 bp

## MTL @ TOR  ·  10000 joint draws  ·  418 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_MTL_win | p_overtime | goals | shots TOR/MTL | TOR/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.55 | 0.45 | 0.00 | 6.09 | 28.7/28.9 | 25.3/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.113 | 0.56 | 0.44 | 0.00 | 9.46 | 30.4/30.5 | 24.6/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.48 | 6.0 | 29.0/29.1 | 25.8/25.7 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.064 | 0.59 | 0.41 | 0.00 | 6.08 | 34.0/23.2 | 20.1/29.5 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.063 | 0.51 | 0.49 | 0.00 | 6.06 | 23.1/33.8 | 30.0/19.6 | even strength |
| balanced shots · high event (8+) · tight (1-goal/OT) | 0.057 | 0.54 | 0.46 | 0.62 | 9.85 | 30.9/31.0 | 24.5/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 12 | 0.177 | 0.159 | +0.050 | +0.032 | $3.30 | FUNDED_RESEARCH | $1 | TOR:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Nick Suzuki: 1+ assists NO | 48 | 0.635 | 0.531 | +0.138 | +0.034 | $7.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Easton Cowan: 1+ assists YES | 31 | 0.393 | 0.349 | +0.068 | +0.024 | $3.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:OFFENSE_4PLUS | DIRECT (0.54) | EVIDENCE_MIXED | D |
| Easton Cowan: 1+ goals YES | 22 | 0.258 | 0.246 | +0.026 | +0.014 | $1.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07MTLTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (19.36 vs 5.61 bp); despite a smaller raw edge (+0.050 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26NOV07MTLTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.045); KXNHLGOAL-26NOV07MTLTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: TOR offense suppressed (<= 2 goals)
- **Nick Suzuki: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07MTLTOR-MTL2|no; why: higher confidence-adjusted growth (9.84 vs 0.69 bp); alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26NOV07MTLTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV07MTLTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: MTL offense succeeds (4+ goals)
- **Easton Cowan: 1+ assists YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (19.36 vs 5.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.045); they share one thesis budget; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.045); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV07MTLTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: TOR offense suppressed (<= 2 goals)
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (19.36 vs 2.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26NOV07MTLTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.4623): highest fidelity KXNHLAST-26NOV07MTLTOR-TORECOWAN53-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3723): highest fidelity KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no (same contract)
- KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3303, phi -0.195)
- KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.0 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4142, phi -0.27)
- KXNHLAST-26NOV07MTLTOR-TORECOWAN53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 46% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3303, phi -0.25)
- KXNHLGOAL-26NOV07MTLTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3303, phi -0.2)

portfolios: A EV +2.66 (adj +0.74) on $13.73, P(profit) 0.5673, adj growth 7.0 bp · B EV +4.10 (adj +1.64) on $15.31, P(profit) 0.4918, adj growth 15.4 bp · C EV +4.68 (adj +1.87) on $14.94, P(profit) 0.6993, adj growth 17.2 bp · R EV +0.39 (adj +0.25) on $1.00, P(profit) 0.1772, adj growth 9.3 bp

## UTA @ OTT  ·  10000 joint draws  ·  426 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_UTA_win | p_overtime | goals | shots OTT/UTA | OTT/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.55 | 0.45 | 0.00 | 6.02 | 27.1/27.1 | 23.8/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.49 | 0.51 | 0.49 | 5.92 | 26.9/26.9 | 23.6/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.60 | 0.40 | 0.00 | 9.27 | 28.7/28.6 | 23.1/22.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.079 | 0.65 | 0.35 | 0.00 | 6.02 | 31.9/21.5 | 18.8/27.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.56 | 0.44 | 0.50 | 5.9 | 32.4/21.8 | 18.6/29.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.058 | 0.57 | 0.43 | 0.00 | 6.0 | 21.7/31.6 | 28.2/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dylan Cozens: 1+ goals YES | 24 | 0.289 | 0.276 | +0.037 | +0.023 | $2.84 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 16 | 0.207 | 0.189 | +0.038 | +0.020 | $2.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 16 | 0.198 | 0.186 | +0.029 | +0.017 | $2.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Utah wins by over 1.5 goals NO | 70 | 0.767 | 0.731 | +0.052 | +0.016 | $5.73 | FUNDED_RESEARCH | $2 | OTT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dylan Cozens: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (6.14 vs 6.04 bp); despite a smaller raw edge (+0.037 vs +0.038/contract); relationships: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLSPREAD-26NOV07UTAOTT-UTA2|no: MOSTLY_INDEPENDENT (phi 0.141); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes has the higher standalone adjusted growth (6.14 vs 6.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.03); KXNHLSPREAD-26NOV07UTAOTT-UTA2|no: MOSTLY_INDEPENDENT (phi 0.132); failure: OTT offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV07UTAOTT-3|yes; why: higher confidence-adjusted growth (4.39 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.899 vs 0.771); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.03); KXNHLSPREAD-26NOV07UTAOTT-UTA2|no: INTENTIONAL_DIVERSIFIER (phi -0.168); failure: UTA offense suppressed (<= 2 goals)
- **Utah wins by over 1.5 goals NO** — thesis: OTT wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV07UTAOTT-UTA5|no; why: Broad expression KXNHLSPREAD-26NOV07UTAOTT-UTA2|no selected over broad KXNHLTEAMTOTAL-26NOV07UTAOTT-UTA5|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi 0.141); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.168); failure: UTA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis OTT:OFFENSE_4PLUS (p 0.4363): highest fidelity KXNHLSPREAD-26NOV07UTAOTT-UTA3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:WINS_BY_2PLUS (p 0.3314): highest fidelity KXNHLSPREAD-26NOV07UTAOTT-UTA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:OFFENSE_4PLUS (p 0.3568): highest fidelity KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes (same contract)
- KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3486, phi -0.224)
- KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3486, phi -0.211)
- KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4208, phi -0.22)
- KXNHLSPREAD-26NOV07UTAOTT-UTA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2328, phi -1.0)
- override: Broad expression KXNHLSPREAD-26NOV07UTAOTT-UTA2|no selected over broad KXNHLTEAMTOTAL-26NOV07UTAOTT-UTA5|no because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.34 (adj +0.41) on $13.73, P(profit) 0.6169, adj growth 3.7 bp · B EV +1.71 (adj +0.88) on $13.06, P(profit) 0.5144, adj growth 8.3 bp · C EV +2.72 (adj +1.37) on $22.88, P(profit) 0.4688, adj growth 12.6 bp · R EV +0.15 (adj +0.05) on $2.00, P(profit) 0.7672, adj growth 1.7 bp

## NJD @ NYI  ·  10000 joint draws  ·  426 bet sides mapped, 11 +EV candidates, 4 on card


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
| New Jersey wins by over 1.5 goals NO | 64 | 0.732 | 0.684 | +0.076 | +0.028 | $8.36 | FUNDED_RESEARCH | $3 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.170 | 0.156 | +0.032 | +0.018 | $1.79 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.254 | 0.240 | +0.032 | +0.019 | $1.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 11 | 0.143 | 0.130 | +0.027 | +0.013 | $1.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV07NJNYI-NJ3|no; why: higher confidence-adjusted growth (7.35 vs 2.99 bp); relationships: KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.121); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.142); failure: NJD wins by 2+
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NJNYI-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NJNYI-NJ2|no has the higher standalone adjusted growth (7.35 vs 6.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.121); they share one thesis budget; relationships: KXNHLSPREAD-26NOV07NJNYI-NJ2|no: MOSTLY_INDEPENDENT (phi 0.121); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: NYI offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NJNYI-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NJNYI-NJ2|no has the higher standalone adjusted growth (7.35 vs 4.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.149); they share one thesis budget; relationships: KXNHLSPREAD-26NOV07NJNYI-NJ2|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NYI offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV07NJNYI-3|yes; why: higher confidence-adjusted growth (3.69 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.901 vs 0.782); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLSPREAD-26NOV07NJNYI-NJ2|no: INTENTIONAL_DIVERSIFIER (phi -0.142); KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:WINS (p 0.5147): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3843): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4163): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV07NJNYI-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2678, phi -1.0)
- KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3999, phi -0.194)
- KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3999, phi -0.228)
- KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4163, phi -0.174)

portfolios: A EV +1.73 (adj +0.39) on $13.73, P(profit) 0.724, adj growth 3.8 bp · B EV +2.06 (adj +0.95) on $13.83, P(profit) 0.4263, adj growth 9.0 bp · C EV +1.37 (adj +0.49) on $11.80, P(profit) 0.7322, adj growth 4.6 bp · R EV +0.35 (adj +0.13) on $3.00, P(profit) 0.7322, adj growth 4.7 bp

## CHI @ CAR  ·  10000 joint draws  ·  428 bet sides mapped, 14 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CHI_win | p_overtime | goals | shots CAR/CHI | CAR/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.207 | 0.79 | 0.21 | 0.00 | 6.06 | 34.4/20.4 | 18.2/29.1 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.159 | 0.81 | 0.19 | 0.00 | 9.41 | 36.4/21.6 | 17.7/27.2 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.148 | 0.60 | 0.40 | 0.45 | 5.91 | 34.5/20.6 | 17.6/31.1 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.076 | 0.74 | 0.26 | 0.00 | 3.5 | 32.9/19.1 | 18.0/30.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.068 | 0.73 | 0.27 | 0.00 | 6.03 | 27.4/26.1 | 23.5/22.8 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.068 | 0.58 | 0.42 | 0.48 | 2.92 | 33.3/19.2 | 17.7/31.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 18 | 0.237 | 0.222 | +0.047 | +0.031 | $3.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 63 | 0.704 | 0.682 | +0.058 | +0.035 | $8.36 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Frank Nazar: 1+ goals YES | 18 | 0.222 | 0.209 | +0.032 | +0.018 | $2.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Chicago over 1.5 goals scored YES | 63 | 0.741 | 0.666 | +0.095 | +0.019 | $2.76 | FUNDED_RESEARCH | $1 | CHI:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV07CHICAR-CHI5|yes; why: KXNHLTEAMTOTAL-26NOV07CHICAR-CHI5|yes has the higher standalone adjusted growth (22.80 vs 13.79 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.170); relationships: KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV07CHICAR-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLTEAMTOTAL-26NOV07CHICAR-CHI2|yes: REINFORCING (phi 0.217); failure: CHI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07CHICAR-CHI2|yes; why: higher confidence-adjusted growth (12.03 vs 8.90 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.051 vs 0.625); relationships: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV07CHICAR-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLTEAMTOTAL-26NOV07CHICAR-CHI2|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: CAR offense succeeds (4+ goals)
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV07CHICAR-CHI5|yes; why: KXNHLTEAMTOTAL-26NOV07CHICAR-CHI5|yes has the higher standalone adjusted growth (22.80 vs 4.83 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.178); relationships: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLTEAMTOTAL-26NOV07CHICAR-CHI2|yes: REINFORCING (phi 0.225); failure: CHI offense suppressed (<= 2 goals)
- **Chicago over 1.5 goals scored YES** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV07CHICAR-CHI5|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV07CHICAR-CHI2|yes selected over broad KXNHLTEAMTOTAL-26NOV07CHICAR-CHI5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.51 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: REINFORCING (phi 0.217); KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV07CHICAR-CHIFNAZAR91-1|yes: REINFORCING (phi 0.225); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.21, CAR shot control · high event (8+) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15.
- thesis CHI:OFFENSE_4PLUS (p 0.2733): highest fidelity KXNHLTEAMTOTAL-26NOV07CHICAR-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes — Broad expression KXNHLTEAMTOTAL-26NOV07CHICAR-CHI2|yes selected over broad KXNHLTEAMTOTAL-26NOV07CHICAR-CHI5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.51 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CHI:WINS_BY_2PLUS (p 0.1444): highest fidelity KXNHLSPREAD-26NOV07CHICAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07CHICAR-CAR2|no (same contract)
- thesis CHI:WINS (p 0.3105): highest fidelity KXNHLSPREAD-26NOV07CHICAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07CHICAR-CAR2|no (same contract)
- KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5157, phi -0.243)
- KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.5585, phi -0.223)
- KXNHLGOAL-26NOV07CHICAR-CHIFNAZAR91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5157, phi -0.238)
- KXNHLTEAMTOTAL-26NOV07CHICAR-CHI2|yes: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.6 pts; opposing: failure thesis CHI:SUPPRESSED (p 0.5157, phi -0.573)
- override: Broad expression KXNHLTEAMTOTAL-26NOV07CHICAR-CHI2|yes selected over broad KXNHLTEAMTOTAL-26NOV07CHICAR-CHI5|yes because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.51 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.23 (adj +0.74) on $13.73, P(profit) 0.5746, adj growth 6.2 bp · B EV +2.39 (adj +1.34) on $16.84, P(profit) 0.619, adj growth 12.8 bp · C EV +4.44 (adj +1.89) on $17.90, P(profit) 0.7424, adj growth 17.4 bp · R EV +0.41 (adj +0.19) on $4.00, P(profit) 0.7039, adj growth 7.4 bp

## SJS @ DAL  ·  10000 joint draws  ·  412 bet sides mapped, 7 +EV candidates, 4 on card


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
| Macklin Celebrini: 1+ assists NO | 53 | 0.610 | 0.568 | +0.063 | +0.020 | $5.73 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.76) | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 48 | 0.591 | 0.515 | +0.093 | +0.018 | $4.21 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 62 | 0.717 | 0.651 | +0.080 | +0.014 | $1.93 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ assists NO | 71 | 0.800 | 0.735 | +0.076 | +0.011 | $5.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (3.59 vs 1.26 bp); despite a smaller raw edge (+0.063 vs +0.076/contract); relationships: KXNHLSPREAD-26NOV07SJDAL-DAL2|no: INTENTIONAL_DIVERSIFIER (phi -0.195); KXNHLSPREAD-26NOV07SJDAL-DAL3|no: INTENTIONAL_DIVERSIFIER (phi -0.177); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.064); failure: SJS offense succeeds (4+ goals)
- **Dallas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no; why: higher confidence-adjusted growth (2.83 vs 2.18 bp); relationships: KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.195); KXNHLSPREAD-26NOV07SJDAL-DAL3|no: DUPLICATIVE (phi 0.755); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.129); failure: DAL wins by 2+
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV07SJDAL-DAL2|no; why: Broad expression KXNHLSPREAD-26NOV07SJDAL-DAL3|no selected over broad KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.95 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.177); KXNHLSPREAD-26NOV07SJDAL-DAL2|no: DUPLICATIVE (phi 0.755); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.117); failure: DAL wins by 2+
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no; why: second expression of the same thesis: KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no has the higher standalone adjusted growth (3.59 vs 1.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.064); they share one thesis budget; relationships: KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.064); KXNHLSPREAD-26NOV07SJDAL-DAL2|no: INTENTIONAL_DIVERSIFIER (phi -0.129); KXNHLSPREAD-26NOV07SJDAL-DAL3|no: INTENTIONAL_DIVERSIFIER (phi -0.117); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SJS:OFFENSE_4PLUS (p 0.2745): highest fidelity KXNHLSPREAD-26NOV07SJDAL-DAL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV07SJDAL-DAL2|no — Broad expression KXNHLSPREAD-26NOV07SJDAL-DAL3|no selected over broad KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.95 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis SJS:SUPPRESSED (p 0.5121): highest fidelity KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4211): highest fidelity KXNHLSPREAD-26NOV07SJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07SJDAL-DAL2|no (same contract)
- KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 24% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.2745, phi -0.269)
- KXNHLSPREAD-26NOV07SJDAL-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.6 pts; opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.4094, phi -1.0)
- KXNHLSPREAD-26NOV07SJDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.2 pts; opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.4094, phi -0.755)
- KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.0 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.2745, phi -0.186)
- override: Broad expression KXNHLSPREAD-26NOV07SJDAL-DAL3|no selected over broad KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.95 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.83 (adj +0.38) on $13.73, P(profit) 0.5894, adj growth 3.6 bp · B EV +2.27 (adj +0.49) on $17.43, P(profit) 0.7763, adj growth 4.6 bp · C EV +2.87 (adj +0.84) on $16.36, P(profit) 0.6996, adj growth 7.8 bp · R EV +0.50 (adj +0.09) on $3.00, P(profit) 0.5906, adj growth 3.3 bp

## TBL @ MIN  ·  10000 joint draws  ·  406 bet sides mapped, 8 +EV candidates, 4 on card


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
| Yakov Trenin: 1+ goals YES | 9 | 0.138 | 0.124 | +0.043 | +0.028 | $2.93 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Bobby Brink: 1+ goals YES | 14 | 0.184 | 0.171 | +0.036 | +0.022 | $2.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ assists NO | 37 | 0.458 | 0.411 | +0.071 | +0.025 | $5.20 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.68) | EVIDENCE_MIXED | D |
| Blake Coleman: 1+ goals YES | 20 | 0.249 | 0.231 | +0.038 | +0.020 | $2.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (19.31 vs 8.31 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: MIN offense suppressed (<= 2 goals)
- **Bobby Brink: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (8.31 vs 5.00 bp); despite a smaller raw edge (+0.036 vs +0.038/contract); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.082); KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: MIN offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07TBMIN-MINMBOLDY12-1|no; why: higher confidence-adjusted growth (5.77 vs 4.13 bp); despite a smaller raw edge (+0.071 vs +0.104/contract); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.082); KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: MIN offense succeeds (4+ goals)
- **Blake Coleman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes has the higher standalone adjusted growth (8.31 vs 5.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.3695): highest fidelity KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4098): highest fidelity KXNHLAST-26NOV07TBMIN-MINMBOLDY12-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4098, phi -0.169)
- KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4098, phi -0.209)
- KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 32% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3695, phi -0.326)
- KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4098, phi -0.247)

portfolios: A EV +3.22 (adj +1.44) on $13.73, P(profit) 0.5298, adj growth 13.6 bp · B EV +3.38 (adj +1.83) on $13.41, P(profit) 0.64, adj growth 17.3 bp · C EV +2.08 (adj +0.98) on $10.15, P(profit) 0.5733, adj growth 9.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ COL  ·  10000 joint draws  ·  446 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_DET_win | p_overtime | goals | shots COL/DET | COL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.74 | 0.26 | 0.00 | 6.0 | 28.7/28.1 | 25.7/23.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.111 | 0.78 | 0.22 | 0.00 | 6.01 | 33.8/22.1 | 20.0/28.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.73 | 0.27 | 0.00 | 9.43 | 30.4/29.7 | 25.0/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.53 | 0.47 | 0.46 | 5.94 | 28.8/28.2 | 24.9/25.4 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.62 | 0.38 | 0.43 | 5.92 | 33.7/22.4 | 19.4/30.4 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.086 | 0.81 | 0.19 | 0.00 | 9.37 | 35.4/23.6 | 19.6/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sheldon Dries: 1+ goals YES | 8 | 0.107 | 0.096 | +0.022 | +0.011 | $1.17 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Lucas Raymond: 1+ assists NO | 61 | 0.682 | 0.639 | +0.056 | +0.012 | $3.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL1PTOTAL-26NOV07DETCOL-3|yes; why: higher confidence-adjusted growth (3.52 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.904 vs 0.709); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: DET offense suppressed (<= 2 goals)
- **Lucas Raymond: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV07DETCOL-DETLRAYMOND23-1|no; why: higher confidence-adjusted growth (1.37 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07DETCOL-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis DET:SUPPRESSED (p 0.4951): highest fidelity KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.2857): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV07DETCOL-DETSDRIES15-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4951, phi -0.156)
- KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.2857, phi -0.262)

portfolios: A EV +0.91 (adj +0.32) on $7.12, P(profit) 0.7182, adj growth 3.0 bp · B EV +0.62 (adj +0.22) on $4.81, P(profit) 0.7182, adj growth 2.1 bp · C EV +0.45 (adj +0.10) on $5.06, P(profit) 0.6825, adj growth 0.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ LAK  ·  10000 joint draws  ·  426 bet sides mapped, 4 +EV candidates, 3 on card


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
| Connor Dewar: 1+ goals YES | 12 | 0.159 | 0.146 | +0.031 | +0.019 | $2.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ goals NO | 77 | 0.809 | 0.798 | +0.027 | +0.016 | $7.58 | FUNDED_RESEARCH | $2 | PIT:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Sidney Crosby: 1+ assists NO | 58 | 0.646 | 0.611 | +0.049 | +0.014 | $3.59 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (7.04 vs 0.41 bp); alternative not eligible: confidence-adjusted EV +0.0042 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26NOV07PITLA-PITSCROSBY87-1|no: MOSTLY_INDEPENDENT (phi -0.021); failure: PIT offense suppressed (<= 2 goals)
- **Ben Kindel: 1+ goals NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07PITLA-PITSCROSBY87-1|no; why: higher confidence-adjusted growth (3.24 vs 1.71 bp); despite a smaller raw edge (+0.027 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26NOV07PITLA-PITSCROSBY87-1|no: MOSTLY_INDEPENDENT (phi 0.048); failure: PIT offense succeeds (4+ goals)
- **Sidney Crosby: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no has the higher standalone adjusted growth (3.24 vs 1.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.048); they share one thesis budget; relationships: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi 0.048); failure: PIT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.2396): highest fidelity KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes (same contract)
- thesis PIT:SUPPRESSED (p 0.4218): highest fidelity KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.431): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4218, phi -0.198)
- KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3516, phi -0.212)
- KXNHLAST-26NOV07PITLA-PITSCROSBY87-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3516, phi -0.251)

portfolios: A EV +1.75 (adj +0.85) on $13.73, P(profit) 0.6388, adj growth 7.9 bp · B EV +1.08 (adj +0.55) on $13.28, P(profit) 0.6097, adj growth 5.2 bp · C EV +1.11 (adj +0.67) on $14.09, P(profit) 0.8396, adj growth 6.2 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.8093, adj growth 1.5 bp

## VAN @ EDM  ·  10000 joint draws  ·  414 bet sides mapped, 5 +EV candidates, 2 on card


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
| Edmonton wins by over 1.5 goals NO | 45 | 0.542 | 0.494 | +0.075 | +0.026 | $2.30 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Edmonton wins by over 2.5 goals NO | 58 | 0.669 | 0.622 | +0.072 | +0.025 | $3.82 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Edmonton wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV07VANEDM-EDM3|no; why: higher confidence-adjusted growth (6.13 vs 5.79 bp); relationships: KXNHLSPREAD-26NOV07VANEDM-EDM3|no: DUPLICATIVE (phi 0.765); failure: EDM wins by 2+
- **Edmonton wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV07VANEDM-EDM2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07VANEDM-EDM2|no has the higher standalone adjusted growth (6.13 vs 5.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.765); they share one thesis budget; relationships: KXNHLSPREAD-26NOV07VANEDM-EDM2|no: DUPLICATIVE (phi 0.765); failure: EDM wins by 2+

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.15, EDM shot control · high event (8+) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.3772): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07VANEDM-EDM2|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.1653): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07VANEDM-EDM2|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.338): highest fidelity KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07VANEDM-EDM2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV07VANEDM-EDM2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis EDM:WINS_BY_2PLUS (p 0.4575, phi -1.0)
- KXNHLSPREAD-26NOV07VANEDM-EDM3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis EDM:WINS_BY_2PLUS (p 0.4575, phi -0.765)

portfolios: A EV +1.81 (adj +0.59) on $13.73, P(profit) 0.5962, adj growth 5.3 bp · B EV +0.83 (adj +0.29) on $6.12, P(profit) 0.6695, adj growth 2.8 bp · C EV +1.17 (adj +0.41) on $7.29, P(profit) 0.5425, adj growth 3.8 bp · R EV +0.28 (adj +0.10) on $2.00, P(profit) 0.5425, adj growth 3.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
