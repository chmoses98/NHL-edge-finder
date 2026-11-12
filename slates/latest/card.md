# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-12T21:31:57Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +26.19 | +8.66 | +24.88 | 0.745 | -22.48 | -35.37 | 78.97 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +30.13 | +17.28 | +25.92 | 0.724 | -26.40 | -39.03 | 161.56 |
| C best expression per thesis | 149.99 | +31.60 | +16.59 | +23.02 | 0.669 | -36.91 | -51.12 | 148.71 |
| R FUNDED research stakes | 14.00 | +1.75 | +1.08 | +1.20 | 0.558 | -5.78 | -7.44 | 0.00 |

## MTL @ BOS  ·  10000 joint draws  ·  422 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.531 / away 0.469

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
| William Borgen: 1+ goals YES | 5 | 0.088 | 0.078 | +0.035 | +0.024 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:WINS_BY_2PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Nikita Zadorov: 1+ goals YES | 4 | 0.067 | 0.059 | +0.024 | +0.016 | $1.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Tanner Jeannot: 1+ goals YES | 8 | 0.114 | 0.104 | +0.029 | +0.019 | $2.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ goals NO | 61 | 0.650 | 0.639 | +0.023 | +0.012 | $3.69 | FUNDED_RESEARCH | $1 | MTL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS6|yes; why: higher confidence-adjusted growth (24.22 vs 7.09 bp); despite a smaller raw edge (+0.035 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.699 vs 0.316); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSNZADOROV91-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV12MTLBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV12MTLBOS-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: MTL wins (incl. OT/SO)
- **Nikita Zadorov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS6|yes; why: higher confidence-adjusted growth (13.05 vs 7.09 bp); despite a smaller raw edge (+0.024 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.753 vs 0.316); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV12MTLBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV12MTLBOS-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: BOS offense suppressed (<= 2 goals)
- **Tanner Jeannot: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS6|yes; why: higher confidence-adjusted growth (10.08 vs 7.09 bp); despite a smaller raw edge (+0.029 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.819 vs 0.316); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV12MTLBOS-BOSNZADOROV91-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV12MTLBOS-MTLCCAUFIELD13-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: BOS offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-1|no; why: Player prop expression KXNHLGOAL-26NOV12MTLBOS-MTLCCAUFIELD13-1|no selected over player prop KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-2|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.80 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV12MTLBOS-BOSNZADOROV91-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV12MTLBOS-BOSTJEANNOT84-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis BOS:WINS_BY_2PLUS (p 0.3718): highest fidelity KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS3|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.4929): highest fidelity KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLAST-26NOV12MTLBOS-BOSFMINTEN93-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3206): highest fidelity KXNHLTOTAL-26NOV12MTLBOS-8|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV12MTLBOS-BOS6|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12MTLBOS-BOSWBORGEN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:WINS (p 0.4068, phi -0.151)
- KXNHLGOAL-26NOV12MTLBOS-BOSNZADOROV91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3042, phi -0.106)
- KXNHLGOAL-26NOV12MTLBOS-BOSTJEANNOT84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3042, phi -0.146)
- KXNHLGOAL-26NOV12MTLBOS-MTLCCAUFIELD13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3579, phi -0.253)
- override: Player prop expression KXNHLGOAL-26NOV12MTLBOS-MTLCCAUFIELD13-1|no selected over player prop KXNHLAST-26NOV12MTLBOS-MTLNSUZUKI14-2|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.80 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.99 (adj +0.84) on $15.87, P(profit) 0.4626, adj growth 7.7 bp · B EV +3.46 (adj +2.32) on $10.05, P(profit) 0.2467, adj growth 21.5 bp · C EV +4.92 (adj +2.28) on $13.26, P(profit) 0.7255, adj growth 20.3 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.65, adj growth 0.7 bp

## MIN @ TOR  ·  10000 joint draws  ·  406 bet sides mapped, 29 +EV candidates, 3 on card

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
| Teddy Blueger: 1+ goals YES | 9 | 0.176 | 0.153 | +0.081 | +0.058 | $6.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ goals NO | 54 | 0.628 | 0.604 | +0.071 | +0.046 | $9.36 | FUNDED_RESEARCH | $3 | MIN:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ goals YES | 18 | 0.243 | 0.226 | +0.052 | +0.035 | $4.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (79.53 vs 17.61 bp); relationships: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.021); failure: TOR offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-2|no; why: higher confidence-adjusted growth (19.15 vs 9.41 bp); relationships: KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense succeeds (4+ goals)
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (79.53 vs 17.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.021); they share one thesis budget; relationships: KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis TOR:OFFENSE_4PLUS (p 0.411): highest fidelity KXNHLTEAMTOTAL-26NOV12MINTOR-TOR3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS (p 0.5074): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS_BY_2PLUS (p 0.2874): highest fidelity KXNHLSPREAD-26NOV12MINTOR-MIN3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV12MINTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3739, phi -0.231)
- KXNHLGOAL-26NOV12MINTOR-MINKKAPRIZOV97-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3978, phi -0.285)
- KXNHLGOAL-26NOV12MINTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3739, phi -0.213)

portfolios: A EV +4.75 (adj +0.83) on $15.87, P(profit) 0.4834, adj growth 6.8 bp · B EV +7.56 (adj +5.30) on $19.97, P(profit) 0.373, adj growth 49.1 bp · C EV +10.51 (adj +7.32) on $25.48, P(profit) 0.7093, adj growth 65.0 bp · R EV +0.38 (adj +0.25) on $3.00, P(profit) 0.6284, adj growth 9.4 bp
equivalent contracts collapsed: KXNHLGAME-26NOV12MINTOR-TOR|yes == KXNHLGAME-26NOV12MINTOR-MIN|no

## COL @ OTT  ·  10000 joint draws  ·  450 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.501 / away 0.499

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
| Jordan Spence: 1+ goals YES | 6 | 0.088 | 0.080 | +0.025 | +0.016 | $1.81 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Ridly Greig: 1+ goals YES | 16 | 0.204 | 0.190 | +0.034 | +0.021 | $2.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Hayden Hodgson: 1+ goals YES | 7 | 0.096 | 0.087 | +0.021 | +0.012 | $1.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
- **Jordan Spence: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (9.31 vs 6.64 bp); despite a smaller raw edge (+0.025 vs +0.034/contract); relationships: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV12COLOTT-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: OTT offense suppressed (<= 2 goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12COLOTT-OTTFZETTERLUND20-1|yes; why: higher confidence-adjusted growth (6.64 vs 0.27 bp); alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12COLOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV12COLOTT-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: OTT offense suppressed (<= 2 goals)
- **Hayden Hodgson: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes has the higher standalone adjusted growth (6.64 vs 4.76 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV12COLOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis OTT:OFFENSE_4PLUS (p 0.406): highest fidelity KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes (same contract)
- KXNHLGOAL-26NOV12COLOTT-OTTJSPENCE10-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3815, phi -0.114)
- KXNHLGOAL-26NOV12COLOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3815, phi -0.202)
- KXNHLGOAL-26NOV12COLOTT-OTTHHODGSON42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3815, phi -0.139)

portfolios: A EV +1.98 (adj +1.23) on $7.18, P(profit) 0.3447, adj growth 11.3 bp · B EV +1.65 (adj +1.03) on $5.98, P(profit) 0.3447, adj growth 9.6 bp · C EV +0.85 (adj +0.52) on $4.23, P(profit) 0.2036, adj growth 4.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ NJD  ·  10000 joint draws  ·  414 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

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
| Cody Glass: 1+ goals YES | 12 | 0.169 | 0.155 | +0.042 | +0.028 | $3.52 | FUNDED_RESEARCH | $1 | NJD:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 17 | 0.224 | 0.208 | +0.044 | +0.028 | $3.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Pierre-Luc Dubois: 1+ goals YES | 17 | 0.211 | 0.200 | +0.031 | +0.020 | $2.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Anthony Beauvillier: 1+ goals YES | 10 | 0.129 | 0.121 | +0.023 | +0.014 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12WSHNJ-NJAGRITSYUK81-1|yes; why: higher confidence-adjusted growth (15.21 vs 1.45 bp); despite a smaller raw edge (+0.042 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV12WSHNJ-WSHABEAUVILLIER72-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: NJD offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (11.75 vs 5.74 bp); relationships: KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV12WSHNJ-WSHABEAUVILLIER72-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: WSH offense suppressed (<= 2 goals)
- **Pierre-Luc Dubois: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (11.75 vs 5.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV12WSHNJ-WSHABEAUVILLIER72-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: WSH offense suppressed (<= 2 goals)
- **Anthony Beauvillier: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes has the higher standalone adjusted growth (11.75 vs 4.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis WSH:OFFENSE_4PLUS (p 0.3457): highest fidelity KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.4391): highest fidelity KXNHLAST-26NOV12WSHNJ-NJAGRITSYUK81-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV12WSHNJ-NJAGRITSYUK81-1|yes (same contract)
- thesis WSH:SUPPRESSED (p 0.4344): highest fidelity KXNHLAST-26NOV12WSHNJ-WSHJKYROU25-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV12WSHNJ-WSHJKYROU25-1|no (same contract)
- KXNHLGOAL-26NOV12WSHNJ-NJCGLASS12-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3539, phi -0.176)
- KXNHLGOAL-26NOV12WSHNJ-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4344, phi -0.238)
- KXNHLGOAL-26NOV12WSHNJ-WSHPDUBOIS80-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4344, phi -0.226)
- KXNHLGOAL-26NOV12WSHNJ-WSHABEAUVILLIER72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.4344, phi -0.177)

portfolios: A EV +2.85 (adj +1.51) on $15.87, P(profit) 0.4968, adj growth 14.1 bp · B EV +2.94 (adj +1.91) on $11.79, P(profit) 0.562, adj growth 17.9 bp · C EV +2.32 (adj +1.16) on $15.39, P(profit) 0.398, adj growth 10.5 bp · R EV +0.33 (adj +0.22) on $1.00, P(profit) 0.169, adj growth 8.1 bp

## TBL @ CBJ  ·  10000 joint draws  ·  426 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.490 / away 0.510

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
| Yanni Gourde: 1+ goals NO | 86 | 0.900 | 0.889 | +0.032 | +0.021 | $9.36 | FUNDED_RESEARCH | $3 | TBL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 18 | 0.213 | 0.204 | +0.023 | +0.013 | $2.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Cole Sillinger: 1+ goals YES | 15 | 0.180 | 0.171 | +0.021 | +0.012 | $1.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Full Game: Over 5.5 goals scored NO | 40 | 0.463 | 0.429 | +0.046 | +0.012 | $3.07 | FUNDED_RESEARCH | $1 | GAME:LOW_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Yanni Gourde: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26NOV12TBCBJ-6|no; why: higher confidence-adjusted growth (8.15 vs 1.33 bp); despite a smaller raw edge (+0.032 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.995 vs 0.775); relationships: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV12TBCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLTOTAL-26NOV12TBCBJ-6|no: MOSTLY_INDEPENDENT (phi 0.088); failure: TBL offense succeeds (4+ goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV12TBCBJ-TB4|no; why: higher confidence-adjusted growth (2.53 vs 0.71 bp); despite a smaller raw edge (+0.023 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0088 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV12TBCBJ-CBJCSILLINGER4-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLTOTAL-26NOV12TBCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.152); failure: CBJ offense suppressed (<= 2 goals)
- **Cole Sillinger: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (2.53 vs 2.41 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLTOTAL-26NOV12TBCBJ-6|no: INTENTIONAL_DIVERSIFIER (phi -0.119); failure: CBJ offense suppressed (<= 2 goals)
- **Full Game: Over 5.5 goals scored NO** — thesis: low-event game (<= 4 goals); alternative: KXNHLAST-26NOV12TBCBJ-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (1.33 vs 1.32 bp); despite a smaller raw edge (+0.046 vs +0.130/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: MOSTLY_INDEPENDENT (phi 0.088); KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.152); KXNHLGOAL-26NOV12TBCBJ-CBJCSILLINGER4-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.119); failure: high-event game (8+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:WINS_BY_2PLUS (p 0.3041): highest fidelity KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.3795): highest fidelity KXNHLAST-26NOV12TBCBJ-CBJDSEVERSON78-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV12TBCBJ-CBJDSEVERSON78-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.4307): highest fidelity KXNHLAST-26NOV12TBCBJ-TBNKUCHEROV86-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV12TBCBJ-TBNKUCHEROV86-1|no (same contract)
- KXNHLGOAL-26NOV12TBCBJ-TBYGOURDE37-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3421, phi -0.129)
- KXNHLGOAL-26NOV12TBCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3983, phi -0.236)
- KXNHLGOAL-26NOV12TBCBJ-CBJCSILLINGER4-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3983, phi -0.194)
- KXNHLTOTAL-26NOV12TBCBJ-6|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:HIGH_EVENT (p 0.2349, phi -0.514)

portfolios: A EV +2.47 (adj +0.53) on $15.87, P(profit) 0.5392, adj growth 4.8 bp · B EV +1.17 (adj +0.59) on $16.31, P(profit) 0.6479, adj growth 5.7 bp · C EV +0.89 (adj +0.36) on $7.73, P(profit) 0.6085, adj growth 3.3 bp · R EV +0.22 (adj +0.10) on $4.00, P(profit) 0.4299, adj growth 3.8 bp

## DET @ FLA  ·  10000 joint draws  ·  420 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.604 / away 0.396

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
| Cole Schwindt: 1+ goals YES | 8 | 0.107 | 0.099 | +0.021 | +0.013 | $1.66 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| J.T. Compher: 1+ goals YES | 13 | 0.161 | 0.152 | +0.023 | +0.014 | $1.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Sam Bennett: 1+ goals YES | 27 | 0.308 | 0.297 | +0.024 | +0.014 | $2.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Anton Lundell: 1+ assists NO | 74 | 0.802 | 0.766 | +0.048 | +0.012 | $7.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | FLA:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes; why: higher confidence-adjusted growth (5.07 vs 1.99 bp); despite a smaller raw edge (+0.021 vs +0.024/contract); relationships: KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLAST-26NOV12DETFLA-FLAALUNDELL15-1|no: MOSTLY_INDEPENDENT (phi -0.034); failure: FLA offense suppressed (<= 2 goals)
- **J.T. Compher: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12DETFLA-DETADEBRINCAT93-2|yes; why: higher confidence-adjusted growth (3.42 vs 1.14 bp); alternative not eligible: confidence-adjusted EV +0.0056 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV12DETFLA-FLAALUNDELL15-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: DET offense suppressed (<= 2 goals)
- **Sam Bennett: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12DETFLA-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (1.99 vs 0.84 bp); despite a smaller raw edge (+0.024 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV12DETFLA-FLAALUNDELL15-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: FLA offense suppressed (<= 2 goals)
- **Anton Lundell: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV12DETFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (1.83 vs 0.44 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:OFFENSE_4PLUS (p 0.4446): highest fidelity KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4488): highest fidelity KXNHLAST-26NOV12DETFLA-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV12DETFLA-DETLRAYMOND23-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3345): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12DETFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3447, phi -0.146)
- KXNHLGOAL-26NOV12DETFLA-DETJCOMPHER37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4488, phi -0.193)
- KXNHLGOAL-26NOV12DETFLA-FLASBENNETT9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3447, phi -0.235)
- KXNHLAST-26NOV12DETFLA-FLAALUNDELL15-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4446, phi -0.198)

portfolios: A EV +1.39 (adj +0.52) on $15.87, P(profit) 0.7015, adj growth 4.9 bp · B EV +1.36 (adj +0.67) on $12.76, P(profit) 0.4373, adj growth 6.3 bp · C EV +0.79 (adj +0.28) on $9.17, P(profit) 0.76, adj growth 2.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ CHI  ·  10000 joint draws  ·  420 bet sides mapped, 7 +EV candidates, 4 on card

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
| Tyler Bertuzzi: 1+ goals YES | 24 | 0.287 | 0.274 | +0.034 | +0.021 | $3.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 60 | 0.653 | 0.638 | +0.036 | +0.021 | $5.80 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
| Rasmus Dahlin: 1+ goals NO | 80 | 0.836 | 0.826 | +0.025 | +0.015 | $8.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 1.5 goals NO | 64 | 0.708 | 0.671 | +0.052 | +0.015 | $2.32 | FUNDED_RESEARCH | $1 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV12BUFCHI-BUF2|no; why: higher confidence-adjusted growth (5.11 vs 2.31 bp); despite a smaller raw edge (+0.034 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV12BUFCHI-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV12BUFCHI-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: REINFORCING (phi 0.158); failure: CHI offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4|no; why: higher confidence-adjusted growth (4.28 vs 2.67 bp); despite a smaller raw edge (+0.036 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.999 vs 0.892); relationships: KXNHLGOAL-26NOV12BUFCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV12BUFCHI-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26NOV12BUFCHI-BUF2|no: REINFORCING (phi 0.177); failure: BUF offense succeeds (4+ goals)
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

portfolios: A EV +1.24 (adj +0.35) on $15.87, P(profit) 0.6892, adj growth 3.1 bp · B EV +1.18 (adj +0.66) on $19.39, P(profit) 0.6599, adj growth 6.2 bp · C EV +1.73 (adj +0.87) on $18.52, P(profit) 0.6051, adj growth 7.9 bp · R EV +0.20 (adj +0.09) on $3.00, P(profit) 0.6527, adj growth 3.5 bp

## WPG @ DAL  ·  10000 joint draws  ·  416 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.605 / away 0.395

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
| Josh Morrissey: 1+ assists NO | 60 | 0.743 | 0.644 | +0.126 | +0.027 | $9.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Arttu Hyry: 1+ goals YES | 14 | 0.179 | 0.168 | +0.030 | +0.019 | $2.43 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Jamie Benn: 1+ goals YES | 16 | 0.200 | 0.189 | +0.030 | +0.019 | $2.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Roope Hintz: 1+ goals YES | 27 | 0.318 | 0.305 | +0.034 | +0.021 | $3.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
- **Josh Morrissey: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12WPGDAL-WPGJMORRISSEY44-2|no; why: higher confidence-adjusted growth (6.68 vs 1.05 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0074 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: WPG offense succeeds (4+ goals)
- **Arttu Hyry: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes; why: higher confidence-adjusted growth (6.40 vs 5.58 bp); relationships: KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: DAL offense suppressed (<= 2 goals)
- **Jamie Benn: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes has the higher standalone adjusted growth (6.40 vs 5.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: DAL offense suppressed (<= 2 goals)
- **Roope Hintz: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes has the higher standalone adjusted growth (6.40 vs 4.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:SUPPRESSED (p 0.4737): highest fidelity KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no (same contract)
- thesis DAL:OFFENSE_4PLUS (p 0.4274): highest fidelity KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3102): highest fidelity KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes [DIRECT], best adjusted EV KXNHLAST-26NOV12WPGDAL-WPGCPERFETTI91-1|yes (same contract)
- KXNHLAST-26NOV12WPGDAL-WPGJMORRISSEY44-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.3 pts; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3102, phi -0.22)
- KXNHLGOAL-26NOV12WPGDAL-DALAHYRY25-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3527, phi -0.199)
- KXNHLGOAL-26NOV12WPGDAL-DALJBENN14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3527, phi -0.185)
- KXNHLGOAL-26NOV12WPGDAL-DALRHINTZ24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3527, phi -0.241)

portfolios: A EV +2.11 (adj +0.65) on $15.87, P(profit) 0.5071, adj growth 6.1 bp · B EV +3.27 (adj +1.26) on $17.67, P(profit) 0.4455, adj growth 11.8 bp · C EV +4.35 (adj +1.31) on $22.35, P(profit) 0.7865, adj growth 11.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ UTA  ·  10000 joint draws  ·  436 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.462 / away 0.538

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
| Lawson Crouse: 1+ goals YES | 18 | 0.246 | 0.228 | +0.056 | +0.038 | $4.95 | FUNDED_RESEARCH | $2 | UTA:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| MacKenzie Weegar: 1+ assists YES | 28 | 0.367 | 0.321 | +0.073 | +0.027 | $3.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | UTA:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Jack McBain: 1+ goals YES | 14 | 0.182 | 0.169 | +0.034 | +0.021 | $2.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Pius Suter: 1+ goals YES | 13 | 0.162 | 0.153 | +0.024 | +0.015 | $1.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-1|yes; why: higher confidence-adjusted growth (20.21 vs 7.54 bp); despite a smaller raw edge (+0.056 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-1|yes: MOSTLY_INDEPENDENT (phi 0.092); KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: UTA offense suppressed (<= 2 goals)
- **MacKenzie Weegar: 1+ assists YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (20.21 vs 7.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.092); they share one thesis budget; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.092); KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.06); KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: UTA offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (20.21 vs 7.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-1|yes: MOSTLY_INDEPENDENT (phi 0.06); KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: UTA offense suppressed (<= 2 goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV12STLUTA-7|yes; why: higher confidence-adjusted growth (4.00 vs 0.69 bp); despite a smaller raw edge (+0.024 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.885 vs 0.683); alternative not eligible: confidence-adjusted EV +0.0088 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.4237): highest fidelity KXNHLTEAMTOTAL-26NOV12STLUTA-UTA5|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.3803): highest fidelity KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3627): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV12STLUTA-UTALCROUSE67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.231)
- KXNHLAST-26NOV12STLUTA-UTAMWEEGAR52-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.259)
- KXNHLGOAL-26NOV12STLUTA-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3627, phi -0.187)
- KXNHLGOAL-26NOV12STLUTA-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4013, phi -0.208)

portfolios: A EV +3.72 (adj +1.63) on $15.87, P(profit) 0.4154, adj growth 14.7 bp · B EV +3.19 (adj +1.85) on $12.70, P(profit) 0.4844, adj growth 17.3 bp · C EV +2.83 (adj +1.89) on $10.82, P(profit) 0.3691, adj growth 17.1 bp · R EV +0.59 (adj +0.40) on $2.00, P(profit) 0.2462, adj growth 14.4 bp

## NYI @ LAK  ·  10000 joint draws  ·  370 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.529 / away 0.471

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
| Mats Zuccarello: 1+ assists NO | 65 | 0.851 | 0.717 | +0.185 | +0.051 | $9.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Andre Lee: 1+ goals YES | 9 | 0.132 | 0.119 | +0.036 | +0.023 | $2.76 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 2+ assists NO | 94 | 0.989 | 0.957 | +0.045 | +0.013 | $9.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DIFFUSE | NONE | EVIDENCE_MIXED | D |
| Trevor Moore: 1+ goals YES | 17 | 0.206 | 0.196 | +0.026 | +0.016 | $2.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no; why: higher confidence-adjusted growth (25.96 vs 1.25 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-2|no: REINFORCING (phi 0.255); KXNHLGOAL-26NOV12NYILA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: LAK offense succeeds (4+ goals)
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV12NYILA-LATMOORE12-1|yes; why: higher confidence-adjusted growth (13.17 vs 3.57 bp); relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.072); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-2|no: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26NOV12NYILA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: LAK offense suppressed (<= 2 goals)
- **Mats Zuccarello: 2+ assists NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: REINFORCING (phi 0.255); KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26NOV12NYILA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: LAK offense succeeds (4+ goals)
- **Trevor Moore: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (3.57 vs 1.29 bp); despite a smaller raw edge (+0.026 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-2|no: MOSTLY_INDEPENDENT (phi -0.016); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.386): highest fidelity KXNHLAST-26NOV12NYILA-LAALAFERRIERE14-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV12NYILA-LATMOORE12-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:SUPPRESSED (p 0.395): highest fidelity KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no [DIRECT], best adjusted EV KXNHLPTS-26NOV12NYILA-LAMZUCCARELLO36-1|no (same contract)
- KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.6 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.386, phi -0.181)
- KXNHLGOAL-26NOV12NYILA-LAALEE47-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.16)
- KXNHLAST-26NOV12NYILA-LAMZUCCARELLO36-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; no single thesis (diffuse); fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.386, phi -0.108)
- KXNHLGOAL-26NOV12NYILA-LATMOORE12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.395, phi -0.209)

portfolios: A EV +2.69 (adj +0.57) on $15.87, P(profit) 0.7617, adj growth 5.4 bp · B EV +4.35 (adj +1.69) on $23.39, P(profit) 0.8792, adj growth 16.2 bp · C EV +2.40 (adj +0.60) on $23.04, P(profit) 0.7543, adj growth 5.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
