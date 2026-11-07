# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-07T15:37:58Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +31.92 | +10.83 | +29.31 | 0.778 | -19.89 | -32.87 | 99.76 |
| B thesis-diversified (joint) ← optimiser card | 149.03 | +26.05 | +13.15 | +24.49 | 0.747 | -20.99 | -33.26 | 124.32 |
| C best expression per thesis | 149.98 | +24.43 | +11.54 | +22.60 | 0.708 | -26.81 | -39.87 | 106.83 |
| R FUNDED research stakes | 23.00 | +3.28 | +1.68 | +2.23 | 0.603 | -6.98 | -9.50 | 0.00 |

## FLA @ WSH  ·  10000 joint draws  ·  450 bet sides mapped, 12 +EV candidates, 4 on card


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
| Aliaksei Protas: 1+ goals YES | 17 | 0.245 | 0.225 | +0.066 | +0.045 | $5.15 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 6 | 0.097 | 0.085 | +0.033 | +0.021 | $1.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Alex Ovechkin: 1+ goals YES | 21 | 0.258 | 0.245 | +0.037 | +0.023 | $2.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 18 | 0.225 | 0.210 | +0.035 | +0.020 | $2.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07FLAWSH-WSHAOVECHKIN8-1|yes; why: higher confidence-adjusted growth (30.00 vs 6.90 bp); relationships: KXNHLGOAL-26NOV07FLAWSH-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV07FLAWSH-WSHAOVECHKIN8-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV07FLAWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: WSH offense suppressed (<= 2 goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07FLAWSH-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (16.00 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV07FLAWSH-WSHAOVECHKIN8-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07FLAWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: FLA offense suppressed (<= 2 goals)
- **Alex Ovechkin: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (30.00 vs 6.90 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26NOV07FLAWSH-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07FLAWSH-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: WSH offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (30.00 vs 5.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV07FLAWSH-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV07FLAWSH-WSHAOVECHKIN8-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.4512): highest fidelity KXNHLAST-26NOV07FLAWSH-WSHAOVECHKIN8-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.4344): highest fidelity KXNHLGOAL-26NOV07FLAWSH-FLASREINHART13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07FLAWSH-FLASREINHART13-1|no (same contract)
- thesis FLA:OFFENSE_4PLUS (p 0.3428): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV07FLAWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3347, phi -0.248)
- KXNHLGOAL-26NOV07FLAWSH-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4344, phi -0.162)
- KXNHLGOAL-26NOV07FLAWSH-WSHAOVECHKIN8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3347, phi -0.221)
- KXNHLGOAL-26NOV07FLAWSH-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3347, phi -0.207)

portfolios: A EV +4.35 (adj +1.60) on $14.85, P(profit) 0.6208, adj growth 14.9 bp · B EV +3.79 (adj +2.50) on $12.24, P(profit) 0.4938, adj growth 23.5 bp · C EV +3.00 (adj +2.02) on $14.80, P(profit) 0.2455, adj growth 18.6 bp · R EV +0.73 (adj +0.51) on $2.00, P(profit) 0.2455, adj growth 18.4 bp

## STL @ NSH  ·  10000 joint draws  ·  412 bet sides mapped, 2 +EV candidates, 2 on card


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
| Adam Edstrom: 1+ goals YES | 16 | 0.203 | 0.188 | +0.033 | +0.019 | $2.11 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 26 | 0.304 | 0.290 | +0.030 | +0.017 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (5.39 vs 3.07 bp); relationships: KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.027); failure: NSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes has the higher standalone adjusted growth (5.39 vs 3.07 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.027); they share one thesis budget; relationships: KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.027); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis NSH:OFFENSE_4PLUS (p 0.4005): highest fidelity KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07STLNSH-NSHAEDSTROM84-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3824, phi -0.22)
- KXNHLGOAL-26NOV07STLNSH-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3824, phi -0.243)

portfolios: A EV +0.92 (adj +0.52) on $6.04, P(profit) 0.4397, adj growth 4.8 bp · B EV +0.65 (adj +0.37) on $4.31, P(profit) 0.4397, adj growth 3.5 bp · C EV +0.59 (adj +0.33) on $3.00, P(profit) 0.2025, adj growth 3.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYR @ SEA  ·  10000 joint draws  ·  442 bet sides mapped, 8 +EV candidates, 4 on card


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
| Ben Meyers: 1+ goals YES | 10 | 0.150 | 0.131 | +0.044 | +0.025 | $2.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| New York R wins by over 1.5 goals NO | 67 | 0.753 | 0.709 | +0.067 | +0.023 | $5.82 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ryan Winterton: 1+ goals YES | 11 | 0.142 | 0.132 | +0.025 | +0.015 | $1.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 66 | 0.712 | 0.696 | +0.036 | +0.020 | $5.60 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: higher confidence-adjusted growth (14.08 vs 5.57 bp); despite a smaller raw edge (+0.044 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: MOSTLY_INDEPENDENT (phi 0.086); KXNHLGOAL-26NOV07NYRSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)
- **New York R wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV07NYRSEA-SEA2|yes; why: higher confidence-adjusted growth (5.57 vs 2.70 bp); wins across more scripts (relative breadth 0.973 vs 0.517); relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.086); KXNHLGOAL-26NOV07NYRSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.093); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.147); failure: NYR wins by 2+
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no has the higher standalone adjusted growth (5.57 vs 4.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.093); they share one thesis budget; relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: MOSTLY_INDEPENDENT (phi 0.093); KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: SEA offense suppressed (<= 2 goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NYRSEA-NYR2|no has the higher standalone adjusted growth (5.57 vs 4.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.147); they share one thesis budget; relationships: KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26NOV07NYRSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4274): highest fidelity KXNHLSPREAD-26NOV07NYRSEA-NYR2|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no (same contract)
- thesis SEA:WINS (p 0.5415): highest fidelity KXNHLSPREAD-26NOV07NYRSEA-NYR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no (same contract)
- thesis NYR:SUPPRESSED (p 0.4182): highest fidelity KXNHLSPREAD-26NOV07NYRSEA-NYR2|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV07NYRSEA-NYR2|no (same contract)
- KXNHLGOAL-26NOV07NYRSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3566, phi -0.17)
- KXNHLSPREAD-26NOV07NYRSEA-NYR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYR:WINS_BY_2PLUS (p 0.2473, phi -1.0)
- KXNHLGOAL-26NOV07NYRSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3566, phi -0.166)
- KXNHLGOAL-26NOV07NYRSEA-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3681, phi -0.246)

portfolios: A EV +2.92 (adj +1.22) on $14.85, P(profit) 0.5079, adj growth 11.0 bp · B EV +2.15 (adj +1.10) on $15.20, P(profit) 0.6575, adj growth 10.4 bp · C EV +1.11 (adj +0.39) on $11.36, P(profit) 0.7527, adj growth 3.6 bp · R EV +0.30 (adj +0.13) on $4.00, P(profit) 0.5642, adj growth 4.8 bp

## MTL @ TOR  ·  10000 joint draws  ·  418 bet sides mapped, 7 +EV candidates, 4 on card


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
| Teddy Blueger: 1+ goals YES | 12 | 0.180 | 0.159 | +0.053 | +0.032 | $3.12 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Nick Suzuki: 1+ assists NO | 48 | 0.642 | 0.530 | +0.144 | +0.033 | $6.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| William Nylander: 2+ goals YES | 6 | 0.085 | 0.076 | +0.021 | +0.012 | $1.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Colton Sissons: 1+ goals YES | 11 | 0.146 | 0.131 | +0.029 | +0.014 | $1.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07MTLTOR-TORWNYLANDER88-2|yes; why: higher confidence-adjusted growth (19.15 vs 5.35 bp); wins across more scripts (relative breadth 0.837 vs 0.688); relationships: KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV07MTLTOR-TORWNYLANDER88-2|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07MTLTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: TOR offense suppressed (<= 2 goals)
- **Nick Suzuki: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07MTLTOR-MTL2|no; why: higher confidence-adjusted growth (9.29 vs 0.90 bp); alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV07MTLTOR-TORWNYLANDER88-2|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV07MTLTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: MTL offense succeeds (4+ goals)
- **William Nylander: 2+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (19.15 vs 5.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV07MTLTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: TOR offense suppressed (<= 2 goals)
- **Colton Sissons: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (19.15 vs 4.18 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.026); they share one thesis budget; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV07MTLTOR-TORWNYLANDER88-2|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.4578): highest fidelity KXNHLAST-26NOV07MTLTOR-TORMRIELLY44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.3713): highest fidelity KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no (same contract)
- KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3331, phi -0.197)
- KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.2 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4173, phi -0.249)
- KXNHLGOAL-26NOV07MTLTOR-TORWNYLANDER88-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3331, phi -0.183)
- KXNHLGOAL-26NOV07MTLTOR-TORCSISSONS15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3331, phi -0.171)

portfolios: A EV +3.52 (adj +1.25) on $14.85, P(profit) 0.4403, adj growth 11.8 bp · B EV +3.96 (adj +1.60) on $12.33, P(profit) 0.7283, adj growth 15.1 bp · C EV +4.55 (adj +1.71) on $13.80, P(profit) 0.7024, adj growth 15.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ OTT  ·  10000 joint draws  ·  426 bet sides mapped, 5 +EV candidates, 4 on card


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
| Lawson Crouse: 1+ goals YES | 16 | 0.211 | 0.196 | +0.041 | +0.026 | $3.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Dylan Cozens: 1+ goals YES | 24 | 0.293 | 0.279 | +0.040 | +0.026 | $3.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 16 | 0.201 | 0.185 | +0.032 | +0.015 | $1.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Logan Cooley: 1+ goals NO | 68 | 0.722 | 0.710 | +0.026 | +0.015 | $4.94 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-UTAALEE72-1|yes; why: higher confidence-adjusted growth (10.45 vs 0.68 bp); alternative not eligible: confidence-adjusted EV +0.0073 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07UTAOTT-UTALCOOLEY92-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: UTA offense suppressed (<= 2 goals)
- **Dylan Cozens: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (7.61 vs 3.55 bp); relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV07UTAOTT-UTALCOOLEY92-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes has the higher standalone adjusted growth (7.61 vs 3.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.019); they share one thesis budget; relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV07UTAOTT-UTALCOOLEY92-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: OTT offense suppressed (<= 2 goals)
- **Logan Cooley: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV07UTAOTT-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (2.24 vs 1.87 bp); relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.3838): highest fidelity KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4341): highest fidelity KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3946): highest fidelity KXNHLGOAL-26NOV07UTAOTT-UTALCOOLEY92-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-UTALCOOLEY92-1|no (same contract)
- KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3946, phi -0.244)
- KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3514, phi -0.22)
- KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3514, phi -0.207)
- KXNHLGOAL-26NOV07UTAOTT-UTALCOOLEY92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3838, phi -0.246)

portfolios: A EV +2.07 (adj +1.22) on $14.85, P(profit) 0.5035, adj growth 11.5 bp · B EV +1.78 (adj +1.07) on $13.03, P(profit) 0.5239, adj growth 10.1 bp · C EV +2.05 (adj +1.28) on $15.92, P(profit) 0.4452, adj growth 11.9 bp · R EV +0.08 (adj +0.04) on $2.00, P(profit) 0.7216, adj growth 1.6 bp

## NJD @ NYI  ·  10000 joint draws  ·  426 bet sides mapped, 13 +EV candidates, 4 on card


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
| New Jersey wins by over 1.5 goals NO | 64 | 0.732 | 0.684 | +0.076 | +0.028 | $8.15 | FUNDED_RESEARCH | $3 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.170 | 0.156 | +0.032 | +0.018 | $1.74 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 11 | 0.143 | 0.133 | +0.027 | +0.016 | $1.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.254 | 0.240 | +0.032 | +0.019 | $1.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV07NJNYI-NJ3|no; why: higher confidence-adjusted growth (7.35 vs 2.99 bp); relationships: KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.121); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.142); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.149); failure: NJD wins by 2+
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NJNYI-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NJNYI-NJ2|no has the higher standalone adjusted growth (7.35 vs 6.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.121); they share one thesis budget; relationships: KXNHLSPREAD-26NOV07NJNYI-NJ2|no: MOSTLY_INDEPENDENT (phi 0.121); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: NYI offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV07NJNYI-3|yes; why: higher confidence-adjusted growth (5.20 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.901 vs 0.782); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLSPREAD-26NOV07NJNYI-NJ2|no: INTENTIONAL_DIVERSIFIER (phi -0.142); KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NJD offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NJNYI-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NJNYI-NJ2|no has the higher standalone adjusted growth (7.35 vs 4.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.149); they share one thesis budget; relationships: KXNHLSPREAD-26NOV07NJNYI-NJ2|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:WINS (p 0.5147): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3843): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4163): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV07NJNYI-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2678, phi -1.0)
- KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3999, phi -0.194)
- KXNHLGOAL-26NOV07NJNYI-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4163, phi -0.174)
- KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3999, phi -0.228)

portfolios: A EV +3.37 (adj +0.58) on $14.85, P(profit) 0.5683, adj growth 5.2 bp · B EV +2.08 (adj +1.00) on $13.77, P(profit) 0.4263, adj growth 9.5 bp · C EV +1.32 (adj +0.48) on $11.36, P(profit) 0.7322, adj growth 4.5 bp · R EV +0.35 (adj +0.13) on $3.00, P(profit) 0.7322, adj growth 4.7 bp

## CHI @ CAR  ·  10000 joint draws  ·  452 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CHI_win | p_overtime | goals | shots CAR/CHI | CAR/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.211 | 0.80 | 0.20 | 0.00 | 6.04 | 34.4/20.3 | 18.1/29.0 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.164 | 0.79 | 0.21 | 0.00 | 9.37 | 36.2/21.7 | 17.7/27.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.142 | 0.59 | 0.41 | 0.49 | 5.93 | 34.8/20.6 | 17.6/31.3 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.074 | 0.73 | 0.27 | 0.00 | 3.5 | 33.2/19.3 | 18.2/30.5 | late empty net |
| balanced shots · normal event (5-7) · decided (2+) | 0.067 | 0.71 | 0.29 | 0.00 | 5.99 | 27.9/26.6 | 24.0/23.2 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.52 | 0.48 | 0.47 | 2.78 | 32.8/19.2 | 17.7/31.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sebastian Aho: 1+ goals NO | 62 | 0.701 | 0.677 | +0.064 | +0.040 | $8.15 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 18 | 0.235 | 0.220 | +0.044 | +0.029 | $3.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Frank Nazar: 1+ goals YES | 18 | 0.226 | 0.212 | +0.035 | +0.021 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Roman Kantserov: 1+ goals YES | 21 | 0.253 | 0.240 | +0.031 | +0.018 | $2.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07CHICAR-CHI2|yes; why: higher confidence-adjusted growth (15.32 vs 9.76 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.033 vs 0.613); relationships: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07CHICAR-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV07CHICAR-CHIRKANTSEROV80-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: CAR offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07CHICAR-CHI2|yes; why: higher confidence-adjusted growth (12.07 vs 9.76 bp); despite a smaller raw edge (+0.044 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.943 vs 0.613); relationships: KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07CHICAR-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07CHICAR-CHIRKANTSEROV80-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CHI offense suppressed (<= 2 goals)
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (12.07 vs 6.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07CHICAR-CHIRKANTSEROV80-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense suppressed (<= 2 goals)
- **Roman Kantserov: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (12.07 vs 4.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV07CHICAR-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.21, CAR shot control · high event (8+) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14.
- thesis CAR:SUPPRESSED (p 0.2451): highest fidelity KXNHLSPREAD-26NOV07CHICAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.2808): highest fidelity KXNHLTEAMTOTAL-26NOV07CHICAR-CHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS_BY_2PLUS (p 0.1462): highest fidelity KXNHLSPREAD-26NOV07CHICAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07CHICAR-CAR2|no (same contract)
- KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.5583, phi -0.221)
- KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5096, phi -0.261)
- KXNHLGOAL-26NOV07CHICAR-CHIFNAZAR91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5096, phi -0.235)
- KXNHLGOAL-26NOV07CHICAR-CHIRKANTSEROV80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5096, phi -0.251)

portfolios: A EV +4.60 (adj +0.83) on $14.85, P(profit) 0.5764, adj growth 6.9 bp · B EV +2.43 (adj +1.53) on $16.51, P(profit) 0.4742, adj growth 14.6 bp · C EV +3.74 (adj +1.87) on $19.92, P(profit) 0.5366, adj growth 17.4 bp · R EV +0.30 (adj +0.19) on $3.00, P(profit) 0.7005, adj growth 7.2 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07CHICAR-CHI|yes == KXNHLGAME-26NOV07CHICAR-CAR|no

## SJS @ DAL  ·  10000 joint draws  ·  432 bet sides mapped, 7 +EV candidates, 4 on card


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
| San Jose over 4.5 goals scored YES | 9 | 0.136 | 0.111 | +0.041 | +0.015 | $1.34 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
| Dallas wins by over 2.5 goals NO | 63 | 0.717 | 0.668 | +0.070 | +0.022 | $6.41 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ivar Stenberg: 1+ assists NO | 72 | 0.800 | 0.753 | +0.066 | +0.019 | $7.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Macklin Celebrini: 1+ assists NO | 53 | 0.610 | 0.565 | +0.063 | +0.018 | $4.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.76) | EVIDENCE_MIXED | D |
- **San Jose over 4.5 goals scored YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07SJDAL-DAL3|no; why: higher confidence-adjusted growth (5.50 vs 4.68 bp); despite a smaller raw edge (+0.041 vs +0.070/contract); relationships: KXNHLSPREAD-26NOV07SJDAL-DAL3|no: REINFORCING (phi 0.233); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.155); KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.217); failure: DAL wins (incl. OT/SO)
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no; why: higher confidence-adjusted growth (4.68 vs 2.18 bp); wins across more scripts (relative breadth 1.013 vs 0.855); relationships: KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes: REINFORCING (phi 0.233); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.117); KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.177); failure: DAL wins by 2+
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (3.89 vs 2.76 bp); relationships: KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes: INTENTIONAL_DIVERSIFIER (phi -0.155); KXNHLSPREAD-26NOV07SJDAL-DAL3|no: INTENTIONAL_DIVERSIFIER (phi -0.117); KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.064); failure: SJS offense succeeds (4+ goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no; why: second expression of the same thesis: KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no has the higher standalone adjusted growth (3.89 vs 2.76 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.064); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes: INTENTIONAL_DIVERSIFIER (phi -0.217); KXNHLSPREAD-26NOV07SJDAL-DAL3|no: INTENTIONAL_DIVERSIFIER (phi -0.177); KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.064); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SJS:OFFENSE_4PLUS (p 0.2745): highest fidelity KXNHLSPREAD-26NOV07SJDAL-DAL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV07SJDAL-DAL3|no (same contract)
- thesis GAME:TIGHT (p 0.4211): highest fidelity KXNHLSPREAD-26NOV07SJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07SJDAL-DAL3|no (same contract)
- thesis DAL:SUPPRESSED (p 0.3039): highest fidelity KXNHLSPREAD-26NOV07SJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07SJDAL-DAL3|no (same contract)
- KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes: FUNDED_RESEARCH; family MIXED; loses 50% of the draws where the thesis happens; opposing: failure thesis DAL:WINS (p 0.6448, phi -0.428)
- KXNHLSPREAD-26NOV07SJDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.4094, phi -0.755)
- KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.2745, phi -0.186)
- KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 24% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.2745, phi -0.269)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26NOV07SJDAL-DAL2|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV07SJDAL-SJ5|yes kept

portfolios: A EV +1.77 (adj +0.45) on $14.85, P(profit) 0.5894, adj growth 4.3 bp · B EV +2.49 (adj +0.77) on $19.97, P(profit) 0.4198, adj growth 7.4 bp · C EV +2.72 (adj +0.86) on $21.82, P(profit) 0.6013, adj growth 8.0 bp · R EV +0.64 (adj +0.22) on $3.00, P(profit) 0.7193, adj growth 7.6 bp

## TBL @ MIN  ·  10000 joint draws  ·  420 bet sides mapped, 8 +EV candidates, 4 on card


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
| Yakov Trenin: 1+ goals YES | 9 | 0.138 | 0.124 | +0.043 | +0.028 | $2.84 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Blake Coleman: 1+ goals YES | 19 | 0.249 | 0.231 | +0.049 | +0.030 | $3.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Bobby Brink: 1+ goals YES | 14 | 0.184 | 0.168 | +0.036 | +0.020 | $2.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ assists NO | 37 | 0.458 | 0.411 | +0.071 | +0.025 | $5.18 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.68) | EVIDENCE_MIXED | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (19.31 vs 12.13 bp); despite a smaller raw edge (+0.043 vs +0.049/contract); relationships: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); failure: MIN offense suppressed (<= 2 goals)
- **Blake Coleman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (12.13 vs 6.54 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: MIN offense suppressed (<= 2 goals)
- **Bobby Brink: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes has the higher standalone adjusted growth (12.13 vs 6.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.082); failure: MIN offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07TBMIN-MINMBOLDY12-1|no; why: higher confidence-adjusted growth (5.77 vs 4.13 bp); despite a smaller raw edge (+0.071 vs +0.104/contract); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.082); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.3695): highest fidelity KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.4098): highest fidelity KXNHLAST-26NOV07TBMIN-MINMBOLDY12-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4098, phi -0.169)
- KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4098, phi -0.247)
- KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4098, phi -0.209)
- KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 32% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3695, phi -0.326)

portfolios: A EV +3.65 (adj +1.74) on $14.85, P(profit) 0.5901, adj growth 16.5 bp · B EV +3.68 (adj +2.03) on $14.05, P(profit) 0.4689, adj growth 19.1 bp · C EV +2.45 (adj +1.20) on $11.58, P(profit) 0.6119, adj growth 11.1 bp · R EV +0.45 (adj +0.29) on $1.00, P(profit) 0.1384, adj growth 10.7 bp

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

## PIT @ LAK  ·  10000 joint draws  ·  426 bet sides mapped, 3 +EV candidates, 2 on card


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
| Connor Dewar: 1+ goals YES | 12 | 0.159 | 0.146 | +0.031 | +0.019 | $2.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ goals NO | 77 | 0.809 | 0.798 | +0.027 | +0.016 | $7.66 | FUNDED_RESEARCH | $2 | PIT:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (7.04 vs 0.68 bp); alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: PIT offense suppressed (<= 2 goals)
- **Ben Kindel: 1+ goals NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV07PITLA-PITBKINDEL81-1|no; why: higher confidence-adjusted growth (3.24 vs 0.00 bp); despite a smaller raw edge (+0.027 vs +0.037/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: PIT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.2396): highest fidelity KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes (same contract)
- thesis PIT:SUPPRESSED (p 0.4218): highest fidelity KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.431): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4218, phi -0.198)
- KXNHLGOAL-26NOV07PITLA-PITBKINDEL81-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3516, phi -0.212)

portfolios: A EV +1.58 (adj +0.87) on $10.34, P(profit) 0.2214, adj growth 8.0 bp · B EV +0.76 (adj +0.46) on $9.70, P(profit) 0.8396, adj growth 4.4 bp · C EV +1.07 (adj +0.65) on $13.58, P(profit) 0.8396, adj growth 6.0 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.8093, adj growth 1.5 bp

## VAN @ EDM  ·  10000 joint draws  ·  428 bet sides mapped, 10 +EV candidates, 4 on card


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
| Edmonton wins by over 1.5 goals NO | 45 | 0.542 | 0.494 | +0.075 | +0.026 | $5.11 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Leon Draisaitl: 2+ assists NO | 73 | 0.837 | 0.761 | +0.093 | +0.017 | $8.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ goals YES | 27 | 0.315 | 0.301 | +0.031 | +0.017 | $3.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Leon Draisaitl: 1+ goals NO | 49 | 0.532 | 0.518 | +0.025 | +0.011 | $1.14 | FUNDED_RESEARCH | $1 | EDM:SUPPRESSED | DIRECT (0.76) | EVIDENCE_STRONGER | D |
- **Edmonton wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV07VANEDM-EDM3|no; why: higher confidence-adjusted growth (6.13 vs 5.79 bp); relationships: KXNHLAST-26NOV07VANEDM-EDMLDRAISAITL29-2|no: REINFORCING (phi 0.202); KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.21); KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no: REINFORCING (phi 0.174); failure: EDM wins by 2+
- **Leon Draisaitl: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07VANEDM-EDM2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07VANEDM-EDM2|no has the higher standalone adjusted growth (6.13 vs 3.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.202); they share one thesis budget; relationships: KXNHLSPREAD-26NOV07VANEDM-EDM2|no: REINFORCING (phi 0.202); KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.171); KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (3.21 vs 0.26 bp); despite a smaller raw edge (+0.031 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0051 below the 0.010/contract floor; relationships: KXNHLSPREAD-26NOV07VANEDM-EDM2|no: INTENTIONAL_DIVERSIFIER (phi -0.21); KXNHLAST-26NOV07VANEDM-EDMLDRAISAITL29-2|no: INTENTIONAL_DIVERSIFIER (phi -0.171); KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: EDM offense suppressed (<= 2 goals)
- **Leon Draisaitl: 1+ goals NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07VANEDM-EDM2|no; why: Player prop expression KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no selected over player prop KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.76 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26NOV07VANEDM-EDM2|no: REINFORCING (phi 0.174); KXNHLAST-26NOV07VANEDM-EDMLDRAISAITL29-2|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: EDM offense succeeds (4+ goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.15, EDM shot control · high event (8+) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.3772): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07VANEDM-EDM2|no (same contract)
- thesis EDM:SUPPRESSED (p 0.2262): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07VANEDM-EDM2|no — override declined: the joint re-optimisation gives KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no less than the minimum stake; KXNHLAST-26NOV07VANEDM-EDMLDRAISAITL29-2|no kept
- thesis VAN:OFFENSE_4PLUS (p 0.338): highest fidelity KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07VANEDM-EDM2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV07VANEDM-EDM2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis EDM:WINS_BY_2PLUS (p 0.4575, phi -1.0)
- KXNHLAST-26NOV07VANEDM-EDMLDRAISAITL29-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.7 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5893, phi -0.262)
- KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2262, phi -0.206)
- KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 24% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5893, phi -0.269)
- override: override declined: the joint re-optimisation gives KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no less than the minimum stake; KXNHLAST-26NOV07VANEDM-EDMLDRAISAITL29-2|no kept
- override: Player prop expression KXNHLGOAL-26NOV07VANEDM-EDMLDRAISAITL29-1|no selected over player prop KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.76 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.17 (adj +0.55) on $14.85, P(profit) 0.6053, adj growth 5.0 bp · B EV +2.28 (adj +0.72) on $17.92, P(profit) 0.6421, adj growth 6.8 bp · C EV +1.84 (adj +0.75) on $12.84, P(profit) 0.735, adj growth 6.9 bp · R EV +0.37 (adj +0.13) on $3.00, P(profit) 0.5425, adj growth 4.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
