# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-12T23:16:13Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +28.69 | +10.69 | +26.97 | 0.752 | -22.30 | -34.62 | 98.78 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +32.12 | +18.09 | +28.62 | 0.729 | -26.35 | -38.65 | 169.35 |
| C best expression per thesis | 150.01 | +30.45 | +15.06 | +24.13 | 0.693 | -29.23 | -41.16 | 137.54 |
| R FUNDED research stakes | 14.00 | +1.90 | +1.19 | +0.40 | 0.523 | -5.30 | -6.61 | 0.00 |

## MTL @ BOS  ·  10000 joint draws  ·  422 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.530 / away 0.470

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_MTL_win | p_overtime | goals | shots BOS/MTL | BOS/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.65 | 0.35 | 0.00 | 6.06 | 27.5/27.4 | 24.3/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.64 | 0.36 | 0.00 | 9.45 | 29.4/29.3 | 23.9/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.51 | 0.49 | 0.49 | 5.95 | 27.7/27.7 | 24.5/24.5 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.080 | 0.67 | 0.33 | 0.00 | 6.03 | 32.6/22.0 | 19.3/27.8 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.067 | 0.72 | 0.28 | 0.00 | 9.37 | 34.5/23.5 | 19.1/26.4 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.59 | 0.41 | 0.46 | 5.99 | 32.8/21.9 | 18.9/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Borgen: 1+ goals YES | 5 | 0.088 | 0.078 | +0.035 | +0.024 | $2.45 | FUNDED_RESEARCH | $1 | BOS:WINS_BY_2PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Tanner Jeannot: 1+ goals YES | 8 | 0.114 | 0.104 | +0.029 | +0.019 | $2.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Nick Suzuki: 1+ assists NO | 51 | 0.648 | 0.552 | +0.121 | +0.024 | $6.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Fraser Minten: 1+ goals YES | 19 | 0.225 | 0.215 | +0.025 | +0.015 | $1.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS6|yes; why: higher confidence-adjusted growth (24.22 vs 7.09 bp); despite a smaller raw edge (+0.035 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.699 vs 0.316); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: MTL wins (incl. OT/SO)
- **Tanner Jeannot: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS6|yes; why: higher confidence-adjusted growth (10.08 vs 7.09 bp); despite a smaller raw edge (+0.029 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.819 vs 0.316); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: BOS offense suppressed (<= 2 goals)
- **Nick Suzuki: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV12MTLBOS-MTLCCAUFIELD13-1|no; why: higher confidence-adjusted growth (5.20 vs 1.37 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV12MTLBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: MTL offense succeeds (4+ goals)
- **Fraser Minten: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS6|yes; why: Player prop expression KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes selected over player prop KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.31 vs 0.42 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV12MTLBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis BOS:WINS_BY_2PLUS (p 0.3718): highest fidelity KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS3|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4929): highest fidelity KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes — Player prop expression KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes selected over player prop KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.31 vs 0.42 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis GAME:HIGH_EVENT (p 0.3206): highest fidelity KXNHLTOTAL-26NOV12MTLBOS-8|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS6|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:WINS (p 0.4068, phi -0.151)
- KXNHLGOAL-26NOV12MTLBOS-BOSTJEANNOT84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3042, phi -0.146)
- KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.8 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3579, phi -0.277)
- KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3042, phi -0.206)
- override: Player prop expression KXNHLGOAL-26NOV12MTLBOS-BOSFMINTEN93-1|yes selected over player prop KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.31 vs 0.42 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.06 (adj +0.89) on $15.78, P(profit) 0.4626, adj growth 8.2 bp · B EV +3.99 (adj +2.02) on $12.68, P(profit) 0.3061, adj growth 18.8 bp · C EV +4.78 (adj +2.11) on $13.32, P(profit) 0.7255, adj growth 19.1 bp · R EV +0.66 (adj +0.45) on $1.00, P(profit) 0.0884, adj growth 16.0 bp

## MIN @ TOR  ·  10000 joint draws  ·  406 bet sides mapped, 30 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.395 / away 0.605

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_MIN_win | p_overtime | goals | shots TOR/MIN | TOR/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.52 | 0.48 | 0.00 | 6.05 | 29.0/29.5 | 26.1/25.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.45 | 5.97 | 29.2/29.5 | 26.1/25.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.51 | 0.49 | 0.00 | 9.4 | 30.4/31.2 | 25.2/23.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.095 | 0.48 | 0.52 | 0.00 | 6.05 | 23.3/35.0 | 31.1/19.9 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.49 | 0.51 | 0.47 | 5.88 | 23.4/35.2 | 31.9/20.1 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.069 | 0.45 | 0.55 | 0.00 | 9.31 | 25.0/37.1 | 30.0/19.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 9 | 0.176 | 0.153 | +0.081 | +0.058 | $6.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Max Shabanov: 1+ goals NO | 75 | 0.804 | 0.788 | +0.041 | +0.025 | $9.24 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 52 | 0.628 | 0.555 | +0.091 | +0.017 | $4.09 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (79.53 vs 10.24 bp); relationships: KXNHLGOAL-26NOV12MINTOR-MINMSHABANOV49-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: TOR offense suppressed (<= 2 goals)
- **Max Shabanov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-2|no; why: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-2|no has the higher standalone adjusted growth (9.41 vs 7.46 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.002); relationships: KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: MIN offense succeeds (4+ goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-2|no; why: Player prop expression KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no selected over broad KXNHLSPREAD-26NOV12MINTOR-MIN3|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.73 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12MINTOR-MINMSHABANOV49-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis TOR:OFFENSE_4PLUS (p 0.411): highest fidelity KXNHLTEAMTOTAL-26NOV12MINTOR-TOR4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS (p 0.5074): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes — Player prop expression KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no selected over broad KXNHLSPREAD-26NOV12MINTOR-MIN3|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.73 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis TOR:WINS_BY_2PLUS (p 0.2874): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3739, phi -0.231)
- KXNHLGOAL-26NOV12MINTOR-MINMSHABANOV49-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3978, phi -0.196)
- KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family TRUSTED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.3 pts; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3978, phi -0.285)
- override: Player prop expression KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no selected over broad KXNHLSPREAD-26NOV12MINTOR-MIN3|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.73 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.07 (adj +0.82) on $15.78, P(profit) 0.6519, adj growth 7.2 bp · B EV +6.31 (adj +4.10) on $19.42, P(profit) 0.5891, adj growth 37.9 bp · C EV +8.17 (adj +5.57) on $23.61, P(profit) 0.228, adj growth 50.2 bp · R EV +0.16 (adj +0.10) on $3.00, P(profit) 0.8038, adj growth 3.7 bp
equivalent contracts collapsed: KXNHLGAME-26NOV12MINTOR-TOR|yes == KXNHLGAME-26NOV12MINTOR-MIN|no

## COL @ OTT  ·  10000 joint draws  ·  450 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.505 / away 0.495

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_COL_win | p_overtime | goals | shots OTT/COL | OTT/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.51 | 0.49 | 0.00 | 6.05 | 27.5/27.9 | 24.3/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.47 | 5.92 | 27.9/28.1 | 24.7/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.53 | 0.47 | 0.00 | 9.36 | 29.2/29.6 | 23.6/22.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.079 | 0.46 | 0.54 | 0.00 | 5.99 | 22.3/33.1 | 29.1/19.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.48 | 0.52 | 0.46 | 5.92 | 22.3/32.9 | 29.5/19.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.054 | 0.55 | 0.45 | 0.00 | 6.04 | 32.0/22.1 | 18.9/28.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Hayden Hodgson: 1+ goals YES | 6 | 0.096 | 0.084 | +0.032 | +0.021 | $2.17 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Jordan Spence: 1+ goals YES | 6 | 0.088 | 0.079 | +0.025 | +0.015 | $1.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Ridly Greig: 1+ goals YES | 16 | 0.204 | 0.189 | +0.034 | +0.019 | $2.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Hayden Hodgson: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (14.81 vs 5.87 bp); despite a smaller raw edge (+0.032 vs +0.034/contract); relationships: KXNHLGOAL-26NOV12COLOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: OTT offense suppressed (<= 2 goals)
- **Jordan Spence: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (7.94 vs 5.87 bp); despite a smaller raw edge (+0.025 vs +0.034/contract); relationships: KXNHLGOAL-26NOV12COLOTT-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: OTT offense suppressed (<= 2 goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes; why: higher confidence-adjusted growth (5.87 vs 0.27 bp); alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12COLOTT-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV12COLOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis OTT:OFFENSE_4PLUS (p 0.406): highest fidelity KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes (same contract)
- KXNHLGOAL-26NOV12COLOTT-OTTHHODGSON42-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3815, phi -0.139)
- KXNHLGOAL-26NOV12COLOTT-OTTJSPENCE10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3815, phi -0.114)
- KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3815, phi -0.202)

portfolios: A EV +2.80 (adj +1.72) on $8.01, P(profit) 0.3447, adj growth 15.7 bp · B EV +2.22 (adj +1.37) on $6.34, P(profit) 0.3447, adj growth 12.7 bp · C EV +0.67 (adj +0.39) on $3.34, P(profit) 0.2036, adj growth 3.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ NJD  ·  10000 joint draws  ·  414 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.583 / away 0.417

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_WSH_win | p_overtime | goals | shots NJD/WSH | NJD/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.126 | 0.63 | 0.37 | 0.00 | 6.05 | 33.6/21.6 | 18.7/29.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.57 | 0.43 | 0.00 | 6.07 | 28.1/27.5 | 24.2/24.2 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.55 | 0.45 | 0.47 | 5.9 | 33.9/22.0 | 18.9/30.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.51 | 0.49 | 0.49 | 5.97 | 28.2/27.5 | 24.2/24.8 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.083 | 0.64 | 0.36 | 0.00 | 9.29 | 35.3/23.1 | 18.2/27.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.58 | 0.41 | 0.00 | 9.34 | 29.9/29.0 | 23.3/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 16 | 0.224 | 0.207 | +0.055 | +0.038 | $4.89 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 12 | 0.169 | 0.154 | +0.042 | +0.027 | $3.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 17 | 0.211 | 0.200 | +0.031 | +0.020 | $2.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Anthony Beauvillier: 1+ goals YES | 10 | 0.129 | 0.119 | +0.023 | +0.013 | $1.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (21.50 vs 5.74 bp); relationships: KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV12WSHNJ-WSHABEAUVILLIER72-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: WSH offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-NJCBROWN16-1|yes; why: higher confidence-adjusted growth (13.90 vs 0.62 bp); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV12WSHNJ-WSHABEAUVILLIER72-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: NJD offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (21.50 vs 5.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV12WSHNJ-WSHABEAUVILLIER72-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: WSH offense suppressed (<= 2 goals)
- **Anthony Beauvillier: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (21.50 vs 3.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3457): highest fidelity KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes (same contract)
- thesis NJD:SUPPRESSED (p 0.3539): highest fidelity KXNHLGOAL-26NOV12WSHNJ-NJJHUGHES86-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV12WSHNJ-NJJHUGHES86-1|no (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.4391): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4344, phi -0.238)
- KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3539, phi -0.176)
- KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4344, phi -0.226)
- KXNHLGOAL-26NOV12WSHNJ-WSHABEAUVILLIER72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4344, phi -0.177)

portfolios: A EV +3.34 (adj +2.19) on $15.78, P(profit) 0.4443, adj growth 20.5 bp · B EV +3.46 (adj +2.26) on $12.41, P(profit) 0.562, adj growth 21.2 bp · C EV +2.31 (adj +1.54) on $11.86, P(profit) 0.2243, adj growth 14.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TBL @ CBJ  ·  10000 joint draws  ·  426 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.501 / away 0.499

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_TBL_win | p_overtime | goals | shots CBJ/TBL | CBJ/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.56 | 0.44 | 0.00 | 6.0 | 27.0/27.2 | 24.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.52 | 0.48 | 0.47 | 5.88 | 27.3/27.5 | 24.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.55 | 0.45 | 0.00 | 9.24 | 28.7/29.0 | 23.3/22.2 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.079 | 0.47 | 0.53 | 0.00 | 5.94 | 21.6/32.3 | 28.5/18.4 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.47 | 0.53 | 0.45 | 5.85 | 21.5/32.3 | 28.8/18.4 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.059 | 0.60 | 0.40 | 0.00 | 6.0 | 31.5/21.5 | 18.6/27.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yanni Gourde: 1+ goals NO | 86 | 0.900 | 0.889 | +0.032 | +0.021 | $9.24 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Steven Lorentz: 1+ goals YES | 8 | 0.106 | 0.099 | +0.021 | +0.013 | $1.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 18 | 0.213 | 0.204 | +0.023 | +0.013 | $2.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Full Game: Over 5.5 goals scored NO | 40 | 0.463 | 0.429 | +0.046 | +0.012 | $3.12 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Yanni Gourde: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12TBCBJ-TBNKUCHEROV86-2|no; why: higher confidence-adjusted growth (8.15 vs 2.16 bp); despite a smaller raw edge (+0.032 vs +0.127/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV12TBCBJ-CBJSLORENTZ18-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLTOTAL-26NOV12TBCBJ-6|no: MOSTLY_INDEPENDENT (phi 0.088); failure: TBL offense succeeds (4+ goals)
- **Steven Lorentz: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (4.90 vs 2.53 bp); despite a smaller raw edge (+0.021 vs +0.023/contract); relationships: KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLTOTAL-26NOV12TBCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.109); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLPTS-26NOV12TBCBJ-TBNKUCHEROV86-2|no; why: higher confidence-adjusted growth (2.53 vs 2.16 bp); despite a smaller raw edge (+0.023 vs +0.127/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV12TBCBJ-CBJSLORENTZ18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLTOTAL-26NOV12TBCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.152); failure: CBJ offense suppressed (<= 2 goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLPTS-26NOV12TBCBJ-TBNKUCHEROV86-2|no; why: KXNHLPTS-26NOV12TBCBJ-TBNKUCHEROV86-2|no has the higher standalone adjusted growth (2.16 vs 1.33 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.276); relationships: KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi 0.088); KXNHLGOAL-26NOV12TBCBJ-CBJSLORENTZ18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.109); KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.152); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3795): highest fidelity KXNHLAST-26NOV12TBCBJ-CBJDSEVERSON78-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV12TBCBJ-CBJDSEVERSON78-1|yes (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.3041): highest fidelity KXNHLPTS-26NOV12TBCBJ-TBNKUCHEROV86-2|no [DIRECT], best adjusted EV KXNHLPTS-26NOV12TBCBJ-TBNKUCHEROV86-2|no (same contract)
- thesis TBL:SUPPRESSED (p 0.4307): highest fidelity KXNHLPTS-26NOV12TBCBJ-TBNKUCHEROV86-2|no [DIRECT], best adjusted EV KXNHLPTS-26NOV12TBCBJ-TBNKUCHEROV86-2|no (same contract)
- KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3421, phi -0.129)
- KXNHLGOAL-26NOV12TBCBJ-CBJSLORENTZ18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3983, phi -0.137)
- KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3983, phi -0.236)
- KXNHLTOTAL-26NOV12TBCBJ-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2349, phi -0.514)

portfolios: A EV +3.15 (adj +0.53) on $15.78, P(profit) 0.6989, adj growth 4.7 bp · B EV +1.34 (adj +0.71) on $16.08, P(profit) 0.6208, adj growth 6.8 bp · C EV +1.70 (adj +0.33) on $9.25, P(profit) 0.7908, adj growth 3.1 bp · R EV +0.22 (adj +0.10) on $4.00, P(profit) 0.4299, adj growth 3.8 bp

## DET @ FLA  ·  10000 joint draws  ·  420 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.618 / away 0.382

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_DET_win | p_overtime | goals | shots FLA/DET | FLA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.60 | 0.40 | 0.00 | 6.02 | 27.5/27.4 | 24.3/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.50 | 5.93 | 27.7/27.6 | 24.3/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.63 | 0.37 | 0.00 | 9.38 | 29.3/29.0 | 23.7/22.0 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.084 | 0.68 | 0.32 | 0.00 | 5.98 | 32.1/21.4 | 18.9/27.5 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.57 | 0.43 | 0.48 | 5.89 | 32.5/22.2 | 19.1/29.3 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.059 | 0.54 | 0.46 | 0.00 | 5.98 | 22.1/32.3 | 28.8/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cole Schwindt: 1+ goals YES | 8 | 0.107 | 0.099 | +0.021 | +0.013 | $1.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 63 | 0.683 | 0.669 | +0.037 | +0.023 | $7.25 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| J.T. Compher: 1+ goals YES | 13 | 0.161 | 0.152 | +0.023 | +0.014 | $1.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Sam Bennett: 1+ goals YES | 27 | 0.308 | 0.297 | +0.024 | +0.014 | $2.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes; why: higher confidence-adjusted growth (5.07 vs 4.22 bp); despite a smaller raw edge (+0.021 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.021); failure: FLA offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV12DETFLA-FLA2|no; why: higher confidence-adjusted growth (4.89 vs 0.79 bp); despite a smaller raw edge (+0.037 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: FLA offense succeeds (4+ goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12DETFLA-DETADEBRINCAT93-2|yes; why: higher confidence-adjusted growth (3.42 vs 1.14 bp); alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV12DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: DET offense suppressed (<= 2 goals)
- **Sam Bennett: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes; why: Player prop expression KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes selected over player prop KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.43 vs 0.47 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV12DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV12DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.3447): highest fidelity KXNHLGOAL-26NOV12DETFLA-FLABTKACHUK8-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV12DETFLA-FLABTKACHUK8-1|no (same contract)
- thesis FLA:OFFENSE_4PLUS (p 0.4446): highest fidelity KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4488): highest fidelity KXNHLAST-26NOV12DETFLA-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV12DETFLA-DETLRAYMOND23-1|no (same contract)
- KXNHLGOAL-26NOV12DETFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3447, phi -0.146)
- KXNHLGOAL-26NOV12DETFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4446, phi -0.238)
- KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4488, phi -0.193)
- KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3447, phi -0.235)
- override: Player prop expression KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes selected over player prop KXNHLAST-26NOV12DETFLA-FLAAEKBLAD5-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.43 vs 0.47 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.65 (adj +0.58) on $15.78, P(profit) 0.5753, adj growth 5.5 bp · B EV +1.29 (adj +0.78) on $12.75, P(profit) 0.382, adj growth 7.3 bp · C EV +1.87 (adj +0.75) on $19.18, P(profit) 0.596, adj growth 7.0 bp · R EV +0.12 (adj +0.07) on $2.00, P(profit) 0.6835, adj growth 2.6 bp

## BUF @ CHI  ·  10000 joint draws  ·  420 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.417 / away 0.583

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_BUF_win | p_overtime | goals | shots CHI/BUF | CHI/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.51 | 0.49 | 0.00 | 6.02 | 27.2/27.7 | 24.1/23.6 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.115 | 0.45 | 0.55 | 0.00 | 6.01 | 21.6/33.2 | 29.2/18.3 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.49 | 5.94 | 21.7/33.4 | 30.0/18.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.47 | 5.91 | 27.1/27.8 | 24.6/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.47 | 0.53 | 0.00 | 9.24 | 28.3/29.3 | 23.0/22.5 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.076 | 0.43 | 0.57 | 0.00 | 9.26 | 23.0/34.5 | 27.4/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 24 | 0.287 | 0.274 | +0.034 | +0.021 | $2.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 60 | 0.653 | 0.638 | +0.036 | +0.021 | $5.73 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Rasmus Dahlin: 1+ goals NO | 80 | 0.836 | 0.826 | +0.025 | +0.015 | $8.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 1.5 goals NO | 64 | 0.708 | 0.671 | +0.052 | +0.015 | $2.30 | FUNDED_RESEARCH | $1 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no; why: higher confidence-adjusted growth (5.11 vs 2.31 bp); despite a smaller raw edge (+0.034 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV12BUFCHI-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: REINFORCING (phi 0.158); failure: CHI offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no; why: higher confidence-adjusted growth (4.28 vs 3.50 bp); despite a smaller raw edge (+0.036 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.999 vs 0.892); relationships: KXNHLGOAL-26NOV12BUFCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV12BUFCHI-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: REINFORCING (phi 0.177); failure: BUF offense succeeds (4+ goals)
- **Rasmus Dahlin: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-1|no has the higher standalone adjusted growth (4.28 vs 3.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV12BUFCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: REINFORCING (phi 0.155); failure: BUF offense succeeds (4+ goals)
- **Buffalo wins by over 1.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no; why: Broad expression KXNHLSPREAD-26NOV12BUFCHI-BUF2|no selected over broad KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF5|no because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV12BUFCHI-CHITBERTUZZI59-1|yes: REINFORCING (phi 0.158); KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.177); KXNHLGOAL-26NOV12BUFCHI-BUFRDAHLIN26-1|no: REINFORCING (phi 0.155); failure: BUF wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3754): highest fidelity KXNHLSPREAD-26NOV12BUFCHI-BUF3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV12BUFCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3878): highest fidelity KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.4913): highest fidelity KXNHLSPREAD-26NOV12BUFCHI-BUF2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no — Broad expression KXNHLSPREAD-26NOV12BUFCHI-BUF2|no selected over broad KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF5|no because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26NOV12BUFCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4045, phi -0.253)
- KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3889, phi -0.251)
- KXNHLGOAL-26NOV12BUFCHI-BUFRDAHLIN26-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3889, phi -0.181)
- KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2919, phi -1.0)
- override: Broad expression KXNHLSPREAD-26NOV12BUFCHI-BUF2|no selected over broad KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF5|no because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.97 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.23 (adj +0.36) on $15.78, P(profit) 0.6892, adj growth 3.3 bp · B EV +1.17 (adj +0.65) on $19.16, P(profit) 0.6599, adj growth 6.1 bp · C EV +1.55 (adj +0.78) on $16.25, P(profit) 0.5484, adj growth 7.2 bp · R EV +0.20 (adj +0.09) on $3.00, P(profit) 0.6527, adj growth 3.5 bp

## WPG @ DAL  ·  10000 joint draws  ·  416 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.593 / away 0.407

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_WPG_win | p_overtime | goals | shots DAL/WPG | DAL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.60 | 0.40 | 0.00 | 5.99 | 26.1/25.8 | 22.8/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.47 | 5.9 | 26.1/26.0 | 22.7/22.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.102 | 0.68 | 0.32 | 0.00 | 5.98 | 30.7/20.4 | 17.8/26.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.61 | 0.39 | 0.00 | 9.15 | 27.6/27.2 | 22.0/21.2 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.60 | 0.40 | 0.48 | 5.96 | 31.2/20.9 | 17.9/27.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.61 | 0.39 | 0.00 | 3.47 | 24.8/24.7 | 23.1/22.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Josh Morrissey: 1+ assists NO | 59 | 0.743 | 0.640 | +0.136 | +0.033 | $9.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Cole Koepke: 1+ goals YES | 7 | 0.098 | 0.090 | +0.023 | +0.015 | $1.86 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Arttu Hyry: 1+ goals YES | 14 | 0.179 | 0.168 | +0.030 | +0.019 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Jamie Benn: 1+ goals YES | 16 | 0.200 | 0.187 | +0.030 | +0.018 | $2.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Josh Morrissey: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12WPGDAL-WPGJMORRISSEY44-2|no; why: higher confidence-adjusted growth (10.29 vs 1.05 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0074 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WPGDAL-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: WPG offense succeeds (4+ goals)
- **Cole Koepke: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes; why: higher confidence-adjusted growth (7.16 vs 1.30 bp); despite a smaller raw edge (+0.023 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi -0.04); KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: WPG offense suppressed (<= 2 goals)
- **Arttu Hyry: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes; why: higher confidence-adjusted growth (6.40 vs 4.87 bp); relationships: KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12WPGDAL-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.04); KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: DAL offense suppressed (<= 2 goals)
- **Jamie Benn: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes has the higher standalone adjusted growth (6.40 vs 4.87 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV12WPGDAL-WPGCKOEPKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:SUPPRESSED (p 0.4737): highest fidelity KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no (same contract)
- thesis DAL:OFFENSE_4PLUS (p 0.4274): highest fidelity KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3102): highest fidelity KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes (same contract)
- KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3102, phi -0.22)
- KXNHLGOAL-26NOV12WPGDAL-WPGCKOEPKE45-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4737, phi -0.163)
- KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3527, phi -0.199)
- KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3527, phi -0.185)

portfolios: A EV +2.19 (adj +0.66) on $15.78, P(profit) 0.5071, adj growth 6.3 bp · B EV +3.59 (adj +1.46) on $15.97, P(profit) 0.3716, adj growth 13.8 bp · C EV +3.83 (adj +1.20) on $18.35, P(profit) 0.7865, adj growth 11.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ UTA  ·  10000 joint draws  ·  436 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.460 / away 0.540

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_STL_win | p_overtime | goals | shots UTA/STL | UTA/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.52 | 0.48 | 0.00 | 6.0 | 27.1/27.0 | 23.4/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.49 | 5.94 | 27.3/27.0 | 23.7/24.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.102 | 0.61 | 0.39 | 0.00 | 6.05 | 32.4/21.4 | 18.5/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.52 | 0.48 | 0.00 | 9.34 | 29.1/28.7 | 22.8/23.0 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.56 | 0.44 | 0.45 | 5.92 | 32.6/21.5 | 18.4/29.1 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.071 | 0.64 | 0.36 | 0.00 | 9.2 | 33.9/22.8 | 17.9/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 18 | 0.246 | 0.228 | +0.056 | +0.038 | $5.13 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 13 | 0.182 | 0.168 | +0.044 | +0.030 | $3.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 13 | 0.162 | 0.153 | +0.024 | +0.015 | $1.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Kevin Stenlund: 1+ goals YES | 8 | 0.104 | 0.097 | +0.019 | +0.012 | $1.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-1|yes; why: higher confidence-adjusted growth (20.21 vs 3.73 bp); despite a smaller raw edge (+0.056 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV12STLUTA-UTAKSTENLUND82-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: UTA offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (20.21 vs 16.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12STLUTA-UTAKSTENLUND82-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: UTA offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV12STLUTA-7|yes; why: higher confidence-adjusted growth (4.00 vs 0.69 bp); despite a smaller raw edge (+0.024 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.885 vs 0.683); alternative not eligible: confidence-adjusted EV +0.0088 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12STLUTA-UTAKSTENLUND82-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: STL offense suppressed (<= 2 goals)
- **Kevin Stenlund: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (20.21 vs 3.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.4237): highest fidelity KXNHLTEAMTOTAL-26NOV12STLUTA-UTA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.3803): highest fidelity KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3627): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.231)
- KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.187)
- KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4013, phi -0.208)
- KXNHLGOAL-26NOV12STLUTA-UTAKSTENLUND82-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.156)

portfolios: A EV +3.12 (adj +1.32) on $15.78, P(profit) 0.4831, adj growth 11.9 bp · B EV +3.34 (adj +2.23) on $12.08, P(profit) 0.5396, adj growth 20.8 bp · C EV +2.39 (adj +1.60) on $9.14, P(profit) 0.3691, adj growth 14.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ LAK  ·  10000 joint draws  ·  364 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.526 / away 0.474

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_NYI_win | p_overtime | goals | shots LAK/NYI | LAK/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 5.98 | 27.8/27.6 | 24.4/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.86 | 27.8/27.5 | 24.4/24.6 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.086 | 0.60 | 0.40 | 0.00 | 5.98 | 32.9/22.3 | 19.3/28.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.56 | 0.44 | 0.50 | 5.87 | 33.1/22.2 | 19.0/29.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.59 | 0.41 | 0.00 | 9.25 | 29.4/29.2 | 23.9/22.7 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.46 | 2.83 | 26.4/26.2 | 24.7/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Andre Lee: 1+ goals YES | 8 | 0.132 | 0.118 | +0.047 | +0.032 | $3.59 | FUNDED_RESEARCH | $1 | LAK:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 1+ assists NO | 65 | 0.851 | 0.717 | +0.185 | +0.051 | $9.08 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Mats Zuccarello: 2+ assists NO | 93 | 0.989 | 0.954 | +0.054 | +0.020 | $9.08 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DIFFUSE | NONE | EVIDENCE_MIXED | D |
| Joel Edmundson: 1+ goals YES | 6 | 0.083 | 0.076 | +0.019 | +0.012 | $1.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (28.42 vs 3.04 bp); relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-2|no: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: LAK offense suppressed (<= 2 goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no; why: higher confidence-adjusted growth (25.96 vs 2.89 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-2|no: REINFORCING (phi 0.255); KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.043); failure: LAK offense succeeds (4+ goals)
- **Mats Zuccarello: 2+ assists NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: REINFORCING (phi 0.255); KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: LAK offense succeeds (4+ goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (5.20 vs 1.29 bp); despite a smaller raw edge (+0.019 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.043); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-2|no: MOSTLY_INDEPENDENT (phi -0.016); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.386): highest fidelity KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12NYILA-LAALAFERRIERE14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.395): highest fidelity KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no (same contract)
- thesis LAK:WINS_BY_2PLUS (p 0.3124): highest fidelity KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes (same contract)
- KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.16)
- KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.6 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.386, phi -0.181)
- KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; no single thesis (diffuse); fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.386, phi -0.108)
- KXNHLGOAL-26NOV12NYILA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.136)

portfolios: A EV +4.08 (adj +1.62) on $15.78, P(profit) 0.7339, adj growth 15.5 bp · B EV +5.42 (adj +2.51) on $23.11, P(profit) 0.8915, adj growth 23.9 bp · C EV +3.19 (adj +0.79) on $25.71, P(profit) 0.4518, adj growth 7.5 bp · R EV +0.55 (adj +0.38) on $1.00, P(profit) 0.1318, adj growth 14.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
