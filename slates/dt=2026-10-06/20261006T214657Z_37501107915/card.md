# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-06T21:46:57Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +29.54 | +8.36 | +27.78 | 0.821 | -10.02 | -19.60 | 78.74 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +30.42 | +13.40 | +28.21 | 0.789 | -15.51 | -26.00 | 127.18 |
| C best expression per thesis | 150.00 | +19.03 | +7.66 | +17.61 | 0.752 | -15.30 | -25.42 | 72.62 |
| R FUNDED research stakes | 14.00 | +2.21 | +1.43 | -0.62 | 0.408 | -4.96 | -7.20 | 0.00 |

## NSH @ TOR  ·  10000 joint draws  ·  392 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NSH_win | p_overtime | goals | shots TOR/NSH | TOR/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.53 | 0.47 | 0.00 | 5.97 | 28.6/28.9 | 25.3/25.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.47 | 5.89 | 29.1/29.2 | 25.9/25.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.55 | 0.45 | 0.00 | 9.24 | 30.4/30.8 | 25.0/23.8 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.082 | 0.48 | 0.52 | 0.00 | 5.99 | 22.8/34.1 | 30.2/19.4 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.45 | 0.55 | 0.49 | 5.88 | 23.0/34.3 | 31.0/19.9 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.057 | 0.48 | 0.52 | 0.46 | 2.89 | 27.4/27.7 | 26.1/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Gavin McKenna: 1+ goals NO | 79 | 0.846 | 0.831 | +0.044 | +0.029 | $8.65 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Adam Wilsby: 1+ goals YES | 4 | 0.062 | 0.056 | +0.020 | +0.013 | $1.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Alexander Kerfoot: 1+ goals YES | 12 | 0.156 | 0.145 | +0.028 | +0.018 | $2.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 25 | 0.299 | 0.286 | +0.036 | +0.022 | $3.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (11.65 vs 6.63 bp); relationships: KXNHLGOAL-26OCT06NSHTOR-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06NSHTOR-NSHAKERFOOT14-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: TOR offense succeeds (4+ goals)
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (8.57 vs 5.65 bp); despite a smaller raw edge (+0.020 vs +0.036/contract); relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06NSHTOR-NSHAKERFOOT14-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: NSH offense suppressed (<= 2 goals)
- **Alexander Kerfoot: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (6.33 vs 5.65 bp); despite a smaller raw edge (+0.028 vs +0.036/contract); relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT06NSHTOR-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06NSHTOR-NSHROREILLY90-2|yes; why: higher confidence-adjusted growth (5.65 vs 4.26 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.897 vs 0.784); relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT06NSHTOR-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT06NSHTOR-NSHAKERFOOT14-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis TOR:SUPPRESSED (p 0.392): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS (p 0.4822): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.3613): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3838, phi -0.171)
- KXNHLGOAL-26OCT06NSHTOR-NSHAWILSBY2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4239, phi -0.107)
- KXNHLGOAL-26OCT06NSHTOR-NSHAKERFOOT14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4239, phi -0.188)
- KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4239, phi -0.25)

portfolios: A EV +1.63 (adj +0.49) on $16.67, P(profit) 0.7307, adj growth 4.7 bp · B EV +1.95 (adj +1.25) on $15.15, P(profit) 0.408, adj growth 11.9 bp · C EV +1.06 (adj +0.66) on $11.90, P(profit) 0.7615, adj growth 6.2 bp · R EV +0.16 (adj +0.11) on $3.00, P(profit) 0.8457, adj growth 4.2 bp

## CAR @ MTL  ·  10000 joint draws  ·  396 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.456 / away 0.544

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_CAR_win | p_overtime | goals | shots MTL/CAR | MTL/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.149 | 0.49 | 0.51 | 0.00 | 6.0 | 20.7/33.3 | 29.6/17.4 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.137 | 0.48 | 0.52 | 0.46 | 5.87 | 20.9/33.7 | 30.3/17.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.097 | 0.58 | 0.42 | 0.00 | 6.02 | 26.5/27.4 | 24.2/22.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.089 | 0.50 | 0.50 | 0.00 | 9.21 | 22.1/35.1 | 28.9/16.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.54 | 0.46 | 0.47 | 5.94 | 26.3/27.3 | 24.1/22.9 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.072 | 0.52 | 0.48 | 0.00 | 3.44 | 19.5/31.8 | 30.0/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Chris Kreider: 1+ assists NO | 72 | 0.855 | 0.761 | +0.121 | +0.027 | $8.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Jake Evans: 1+ goals YES | 11 | 0.143 | 0.132 | +0.026 | +0.015 | $1.74 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Phillip Danault: 1+ goals YES | 10 | 0.128 | 0.119 | +0.021 | +0.013 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Alexandre Texier: 1+ goals YES | 12 | 0.150 | 0.141 | +0.022 | +0.014 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06CARMTL-MTLCKREIDER22-1|no; why: higher confidence-adjusted growth (7.99 vs 0.08 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0029 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT06CARMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.058); failure: MTL offense succeeds (4+ goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLSPREAD-26OCT06CARMTL-CAR3|no; why: higher confidence-adjusted growth (4.86 vs 2.09 bp); despite a smaller raw edge (+0.026 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT06CARMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: MTL offense suppressed (<= 2 goals)
- **Phillip Danault: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes has the higher standalone adjusted growth (4.86 vs 3.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: MTL offense suppressed (<= 2 goals)
- **Alexandre Texier: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes has the higher standalone adjusted growth (4.86 vs 3.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.058); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06CARMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis MTL:WINS_BY_2PLUS (p 0.2989): highest fidelity KXNHLSPREAD-26OCT06CARMTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:OFFENSE_4PLUS (p 0.3905): highest fidelity KXNHLSPREAD-26OCT06CARMTL-CAR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.4242): highest fidelity KXNHLSPREAD-26OCT06CARMTL-CAR3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT06CARMTL-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.5 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3905, phi -0.167)
- KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3891, phi -0.203)
- KXNHLGOAL-26OCT06CARMTL-MTLPDANAULT24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3891, phi -0.175)
- KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3891, phi -0.167)

portfolios: A EV +2.04 (adj +0.49) on $16.67, P(profit) 0.7116, adj growth 4.7 bp · B EV +2.41 (adj +0.91) on $13.59, P(profit) 0.3422, adj growth 8.7 bp · C EV +1.58 (adj +0.50) on $12.92, P(profit) 0.6494, adj growth 4.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ DET  ·  10000 joint draws  ·  378 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.517 / away 0.483

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_OTT_win | p_overtime | goals | shots DET/OTT | DET/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.55 | 0.45 | 0.00 | 5.97 | 27.3/27.3 | 23.9/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.46 | 5.91 | 27.2/27.3 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.55 | 0.45 | 0.00 | 9.28 | 28.5/28.6 | 23.0/21.9 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.079 | 0.49 | 0.51 | 0.00 | 6.0 | 21.5/31.9 | 28.1/18.0 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.46 | 0.54 | 0.49 | 5.86 | 21.8/32.4 | 29.2/18.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.54 | 0.46 | 0.00 | 3.45 | 25.6/26.0 | 24.3/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Eklund: 1+ assists NO | 66 | 0.849 | 0.723 | +0.173 | +0.047 | $8.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Andrew Copp: 1+ goals YES | 18 | 0.228 | 0.215 | +0.038 | +0.025 | $3.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Jordan Spence: 1+ assists YES | 27 | 0.353 | 0.307 | +0.070 | +0.023 | $3.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Alex DeBrincat: 1+ goals YES | 39 | 0.443 | 0.429 | +0.036 | +0.022 | $3.95 | FUNDED_RESEARCH | $1 | DET:OFFENSE_4PLUS | DIRECT (0.63) | EVIDENCE_STRONGER | D |
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (22.31 vs 6.68 bp); relationships: KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: OTT offense succeeds (4+ goals)
- **Andrew Copp: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06OTTDET-DETACOPP18-1|yes; why: higher confidence-adjusted growth (8.57 vs 7.97 bp); despite a smaller raw edge (+0.038 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: DET offense suppressed (<= 2 goals)
- **Jordan Spence: 1+ assists YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06OTTDET-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (5.59 vs 0.52 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0055 below the 0.010/contract floor; relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: OTT offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06OTTDET-DETACOPP18-1|yes; why: Player prop expression KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLAST-26OCT06OTTDET-DETACOPP18-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.63 vs 0.61 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis DET:OFFENSE_4PLUS (p 0.3797): highest fidelity KXNHLPTS-26OCT06OTTDET-DETACOPP18-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-DETACOPP18-1|yes — Player prop expression KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLAST-26OCT06OTTDET-DETACOPP18-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.63 vs 0.61 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis OTT:SUPPRESSED (p 0.4377): highest fidelity KXNHLAST-26OCT06OTTDET-OTTTSTUTZLE18-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4024): highest fidelity KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no (same contract)
- KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.4 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3428, phi -0.175)
- KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4024, phi -0.217)
- KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4377, phi -0.283)
- KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 37% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4024, phi -0.305)
- override: Player prop expression KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLAST-26OCT06OTTDET-DETACOPP18-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.63 vs 0.61 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.43 (adj +0.70) on $16.67, P(profit) 0.6733, adj growth 6.7 bp · B EV +3.99 (adj +1.49) on $18.99, P(profit) 0.656, adj growth 14.2 bp · C EV +3.89 (adj +1.21) on $23.76, P(profit) 0.7524, adj growth 11.5 bp · R EV +0.09 (adj +0.05) on $1.00, P(profit) 0.4432, adj growth 2.0 bp

## UTA @ NJD  ·  10000 joint draws  ·  416 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_UTA_win | p_overtime | goals | shots NJD/UTA | NJD/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.45 | 0.55 | 0.00 | 6.0 | 27.8/27.6 | 23.8/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.49 | 0.51 | 0.48 | 5.91 | 28.0/27.7 | 24.3/24.6 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.088 | 0.52 | 0.48 | 0.00 | 5.99 | 33.1/22.1 | 18.8/29.3 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.53 | 0.47 | 0.48 | 5.93 | 33.2/22.3 | 19.1/29.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.44 | 0.56 | 0.00 | 9.24 | 29.4/29.2 | 22.8/23.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.059 | 0.46 | 0.54 | 0.50 | 2.8 | 26.3/26.2 | 24.6/25.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vincent Trocheck: 1+ assists NO | 67 | 0.842 | 0.724 | +0.156 | +0.038 | $8.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Lawson Crouse: 1+ goals YES | 16 | 0.213 | 0.198 | +0.043 | +0.029 | $3.35 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 64 | 0.808 | 0.689 | +0.152 | +0.033 | $8.23 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Cody Glass: 1+ goals YES | 11 | 0.143 | 0.133 | +0.026 | +0.016 | $1.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06UTANJ-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (14.86 vs 0.37 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: UTA offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06UTANJ-UTAALEE72-1|yes; why: higher confidence-adjusted growth (12.88 vs 1.52 bp); relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: UTA offense suppressed (<= 2 goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06UTANJ-NJJHUGHES86-2|no; why: higher confidence-adjusted growth (10.66 vs 2.77 bp); relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.021); failure: NJD offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26OCT06UTANJ-3|yes; why: higher confidence-adjusted growth (5.64 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.914 vs 0.794); alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.021); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis UTA:OFFENSE_4PLUS (p 0.3787): highest fidelity KXNHLGOAL-26OCT06UTANJ-UTAALEE72-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4288): highest fidelity KXNHLAST-26OCT06UTANJ-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06UTANJ-NJTMEIER28-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.4005): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.2 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3787, phi -0.17)
- KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4005, phi -0.214)
- KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.3 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3519, phi -0.199)
- KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4288, phi -0.175)

portfolios: A EV +3.12 (adj +1.06) on $16.67, P(profit) 0.705, adj growth 10.3 bp · B EV +5.05 (adj +1.70) on $21.62, P(profit) 0.7811, adj growth 16.3 bp · C EV +1.53 (adj +0.80) on $13.38, P(profit) 0.2129, adj growth 7.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ BUF  ·  10000 joint draws  ·  396 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.493 / away 0.507

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_MIN_win | p_overtime | goals | shots BUF/MIN | BUF/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.49 | 0.51 | 0.00 | 6.03 | 28.8/28.5 | 24.8/25.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.48 | 5.99 | 28.9/28.7 | 25.4/25.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.48 | 0.52 | 0.00 | 9.29 | 30.5/30.2 | 23.9/24.4 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.085 | 0.54 | 0.46 | 0.00 | 6.06 | 34.0/22.8 | 19.5/30.1 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.54 | 0.46 | 0.47 | 5.94 | 34.1/23.0 | 19.8/30.8 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.068 | 0.56 | 0.44 | 0.00 | 9.22 | 35.9/24.2 | 19.0/28.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 9 | 0.147 | 0.132 | +0.052 | +0.036 | $3.54 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Zach Metsa: 1+ goals NO | 93 | 0.962 | 0.953 | +0.028 | +0.018 | $8.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 21 | 0.349 | 0.252 | +0.128 | +0.031 | $2.71 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Peyton Krebs: 1+ goals YES | 11 | 0.142 | 0.133 | +0.025 | +0.016 | $1.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (31.50 vs 11.82 bp); despite a smaller raw edge (+0.052 vs +0.128/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06MINBUF-BUFZMETSA73-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.133); KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense suppressed (<= 2 goals)
- **Zach Metsa: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: BUF offense succeeds (4+ goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (11.82 vs 3.27 bp); despite a smaller raw edge (+0.128 vs +0.138/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.133); KXNHLGOAL-26OCT06MINBUF-BUFZMETSA73-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: MIN offense suppressed (<= 2 goals)
- **Peyton Krebs: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes; why: higher confidence-adjusted growth (5.18 vs 0.92 bp); alternative not eligible: confidence-adjusted EV +0.0077 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT06MINBUF-BUFZMETSA73-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4011): highest fidelity KXNHLPTS-26OCT06MINBUF-MINRHARTMAN38-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:OFFENSE_4PLUS (p 0.4008): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis BUF:SUPPRESSED (p 0.384): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3801, phi -0.165)
- KXNHLGOAL-26OCT06MINBUF-BUFZMETSA73-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4008, phi -0.072)
- KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.9 pts; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3801, phi -0.289)
- KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.384, phi -0.178)

portfolios: A EV +6.10 (adj +2.14) on $16.67, P(profit) 0.5628, adj growth 19.4 bp · B EV +4.11 (adj +2.12) on $16.69, P(profit) 0.4931, adj growth 19.9 bp · C EV +2.43 (adj +0.70) on $13.23, P(profit) 0.3495, adj growth 6.7 bp · R EV +0.54 (adj +0.38) on $1.00, P(profit) 0.1473, adj growth 14.0 bp

## NYI @ NYR  ·  10000 joint draws  ·  410 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.589 / away 0.411

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_NYI_win | p_overtime | goals | shots NYR/NYI | NYR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.66 | 0.34 | 0.00 | 5.97 | 26.6/27.0 | 24.3/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.54 | 0.46 | 0.47 | 5.87 | 26.9/27.2 | 24.0/23.6 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.088 | 0.57 | 0.43 | 0.00 | 5.97 | 21.5/32.4 | 29.0/17.9 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.51 | 0.49 | 0.50 | 5.85 | 21.3/32.3 | 29.2/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.65 | 0.35 | 0.00 | 9.07 | 28.2/28.6 | 23.5/21.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.63 | 0.37 | 0.00 | 3.5 | 25.7/26.1 | 24.6/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ondrej Palat: 1+ goals YES | 8 | 0.111 | 0.101 | +0.026 | +0.016 | $1.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Matthew Schaefer: 1+ goals NO | 81 | 0.854 | 0.842 | +0.033 | +0.021 | $8.65 | FUNDED_RESEARCH | $3 | NYI:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Vladislav Gavrikov: 1+ assists YES | 26 | 0.337 | 0.293 | +0.063 | +0.020 | $2.57 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Matt Rempe: 1+ goals YES | 8 | 0.103 | 0.096 | +0.018 | +0.011 | $1.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT06NYINYR-NYI3|yes; why: higher confidence-adjusted growth (6.83 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06NYINYR-NYIMSCHAEFER48-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT06NYINYR-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: NYI offense suppressed (<= 2 goals)
- **Matthew Schaefer: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06NYINYR-NYIMMACCELLI63-1|no; why: higher confidence-adjusted growth (6.52 vs 1.98 bp); despite a smaller raw edge (+0.033 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06NYINYR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT06NYINYR-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: NYI offense succeeds (4+ goals)
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06NYINYR-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (4.37 vs 0.41 bp); alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06NYINYR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT06NYINYR-NYIMSCHAEFER48-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT06NYINYR-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi 0.068); failure: NYR offense suppressed (<= 2 goals)
- **Matt Rempe: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes has the higher standalone adjusted growth (4.37 vs 3.13 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.068); they share one thesis budget; relationships: KXNHLGOAL-26OCT06NYINYR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT06NYINYR-NYIMSCHAEFER48-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.068); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYI shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYR:OFFENSE_4PLUS (p 0.4177): highest fidelity KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes (same contract)
- thesis NYI:SUPPRESSED (p 0.4901): highest fidelity KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3608): highest fidelity KXNHLGOAL-26OCT06NYINYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NYINYR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT06NYINYR-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4901, phi -0.181)
- KXNHLGOAL-26OCT06NYINYR-NYIMSCHAEFER48-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.2881, phi -0.172)
- KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3608, phi -0.251)
- KXNHLGOAL-26OCT06NYINYR-NYRMREMPE73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3608, phi -0.149)

portfolios: A EV +1.90 (adj +0.54) on $16.67, P(profit) 0.3338, adj growth 5.1 bp · B EV +1.68 (adj +0.85) on $13.97, P(profit) 0.4139, adj growth 8.1 bp · C EV +1.40 (adj +0.43) on $15.15, P(profit) 0.7093, adj growth 4.0 bp · R EV +0.12 (adj +0.08) on $3.00, P(profit) 0.8538, adj growth 2.9 bp

## STL @ CHI  ·  10000 joint draws  ·  394 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.437 / away 0.563

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_STL_win | p_overtime | goals | shots CHI/STL | CHI/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.41 | 0.59 | 0.00 | 5.99 | 26.4/26.7 | 22.8/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.48 | 0.52 | 0.45 | 5.91 | 26.5/26.7 | 23.4/23.1 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.081 | 0.34 | 0.66 | 0.00 | 5.94 | 20.9/31.3 | 26.9/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.41 | 0.59 | 0.00 | 9.24 | 27.7/28.1 | 21.7/22.4 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.45 | 0.55 | 0.47 | 5.89 | 21.3/31.8 | 28.5/18.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.42 | 0.58 | 0.00 | 3.45 | 25.0/25.2 | 23.1/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 11 | 0.169 | 0.153 | +0.052 | +0.036 | $4.00 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Philip Broberg: 1+ goals YES | 7 | 0.100 | 0.091 | +0.026 | +0.017 | $1.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 59 | 0.738 | 0.635 | +0.131 | +0.029 | $8.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Dillon Dube: 1+ goals YES | 8 | 0.106 | 0.098 | +0.021 | +0.013 | $1.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06STLCHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (26.53 vs 0.22 bp); alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT06STLCHI-STLDDUBE65-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: CHI offense suppressed (<= 2 goals)
- **Philip Broberg: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06STLCHI-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (8.86 vs 0.23 bp); alternative not eligible: confidence-adjusted EV +0.0048 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT06STLCHI-STLDDUBE65-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: STL offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06STLCHI-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (7.46 vs 0.92 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT06STLCHI-STLDDUBE65-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: CHI offense succeeds (4+ goals)
- **Dillon Dube: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06STLCHI-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (4.79 vs 0.23 bp); alternative not eligible: confidence-adjusted EV +0.0048 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CHI:OFFENSE_4PLUS (p 0.3242): highest fidelity KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4578): highest fidelity KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no (same contract)
- thesis STL:SUPPRESSED (p 0.3661): highest fidelity KXNHLGOAL-26OCT06STLCHI-STLMMCTAVISH83-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06STLCHI-STLMMCTAVISH83-1|no (same contract)
- KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4578, phi -0.22)
- KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3661, phi -0.113)
- KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3242, phi -0.242)
- KXNHLGOAL-26OCT06STLCHI-STLDDUBE65-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3661, phi -0.137)

portfolios: A EV +3.70 (adj +1.44) on $16.67, P(profit) 0.5286, adj growth 13.7 bp · B EV +4.61 (adj +2.26) on $15.84, P(profit) 0.3329, adj growth 21.2 bp · C EV +3.59 (adj +1.62) on $23.76, P(profit) 0.6193, adj growth 15.4 bp · R EV +0.89 (adj +0.61) on $2.00, P(profit) 0.1687, adj growth 21.4 bp

## VGK @ SEA  ·  10000 joint draws  ·  384 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.398 / away 0.602

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_VGK_win | p_overtime | goals | shots SEA/VGK | SEA/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.49 | 0.51 | 0.00 | 5.98 | 26.8/27.3 | 23.7/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.47 | 5.88 | 27.0/27.3 | 24.1/23.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.104 | 0.41 | 0.59 | 0.00 | 5.96 | 21.4/32.3 | 28.3/18.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.46 | 0.54 | 0.48 | 5.85 | 21.4/32.4 | 29.0/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.52 | 0.48 | 0.00 | 9.16 | 28.2/28.6 | 23.0/22.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.057 | 0.50 | 0.50 | 0.00 | 3.44 | 25.5/26.0 | 24.1/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Winterton: 1+ goals YES | 10 | 0.141 | 0.129 | +0.034 | +0.023 | $2.36 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Brayden McNabb: 1+ goals YES | 5 | 0.076 | 0.067 | +0.022 | +0.013 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 8 | 0.114 | 0.101 | +0.029 | +0.016 | $1.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Vegas wins by over 1.5 goals NO | 62 | 0.709 | 0.662 | +0.072 | +0.025 | $7.23 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK3|no; why: higher confidence-adjusted growth (11.89 vs 6.54 bp); despite a smaller raw edge (+0.034 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06VGKSEA-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: MOSTLY_INDEPENDENT (phi 0.116); failure: SEA offense suppressed (<= 2 goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06VGKSEA-VGKBBOWMAN42-1|yes; why: higher confidence-adjusted growth (7.63 vs 0.55 bp); alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: INTENTIONAL_DIVERSIFIER (phi -0.129); failure: VGK offense suppressed (<= 2 goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes has the higher standalone adjusted growth (11.89 vs 6.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT06VGKSEA-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: MOSTLY_INDEPENDENT (phi 0.116); failure: SEA offense suppressed (<= 2 goals)
- **Vegas wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK3|no; why: KXNHLSPREAD-26OCT06VGKSEA-VGK3|no has the higher standalone adjusted growth (6.54 vs 6.10 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.734); relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.116); KXNHLGOAL-26OCT06VGKSEA-VGKBMCNABB3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.129); KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.116); failure: VGK wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.3591): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4912): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no (same contract)
- thesis VGK:SUPPRESSED (p 0.402): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4263, phi -0.186)
- KXNHLGOAL-26OCT06VGKSEA-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.402, phi -0.133)
- KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4263, phi -0.17)
- KXNHLSPREAD-26OCT06VGKSEA-VGK2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.2913, phi -1.0)

portfolios: A EV +2.56 (adj +0.56) on $16.67, P(profit) 0.6593, adj growth 5.1 bp · B EV +2.71 (adj +1.44) on $12.54, P(profit) 0.2985, adj growth 13.6 bp · C EV +1.68 (adj +0.87) on $12.14, P(profit) 0.8317, adj growth 8.1 bp · R EV +0.23 (adj +0.08) on $2.00, P(profit) 0.7087, adj growth 3.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT06VGKSEA-VGK|no == KXNHLGAME-26OCT06VGKSEA-SEA|yes

## FLA @ LAK  ·  10000 joint draws  ·  416 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.483 / away 0.517

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_FLA_win | p_overtime | goals | shots LAK/FLA | LAK/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.63 | 0.37 | 0.00 | 5.95 | 27.0/26.9 | 23.9/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.53 | 0.47 | 0.46 | 5.91 | 27.1/27.0 | 23.8/23.8 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.083 | 0.69 | 0.31 | 0.00 | 6.0 | 32.4/21.6 | 18.9/27.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.62 | 0.38 | 0.00 | 9.15 | 29.0/28.7 | 23.5/22.3 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.56 | 0.44 | 0.45 | 5.85 | 31.9/21.8 | 18.7/28.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.067 | 0.52 | 0.48 | 0.46 | 2.81 | 25.6/25.4 | 24.0/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 69 | 0.771 | 0.747 | +0.066 | +0.042 | $7.97 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 1+ assists NO | 63 | 0.789 | 0.682 | +0.142 | +0.036 | $7.97 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Alex Laferriere: 1+ assists YES | 27 | 0.387 | 0.308 | +0.103 | +0.024 | $2.95 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:OFFENSE_4PLUS | DIRECT (0.54) | EVIDENCE_MIXED | D |
| Alex Laferriere: 1+ goals YES | 23 | 0.275 | 0.262 | +0.032 | +0.020 | $2.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06FLALA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (18.50 vs 8.50 bp); relationships: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: FLA offense succeeds (4+ goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06FLALA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (12.43 vs 6.59 bp); relationships: KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.113); failure: LAK offense succeeds (4+ goals)
- **Alex Laferriere: 1+ assists YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: KXNHLSPREAD-26OCT06FLALA-FLA3|no has the higher standalone adjusted growth (7.98 vs 6.04 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.142); relationships: KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: LAK offense suppressed (<= 2 goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: KXNHLSPREAD-26OCT06FLALA-FLA3|no has the higher standalone adjusted growth (7.98 vs 4.61 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.109); relationships: KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.113); KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis FLA:SUPPRESSED (p 0.4918): highest fidelity KXNHLTEAMTOTAL-26OCT06FLALA-FLA4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS (p 0.5803): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT06FLALA-FLA4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.4049): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [DIRECT], best adjusted EV KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.2891, phi -0.237)
- KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4049, phi -0.188)
- KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 46% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.2 pts; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3764, phi -0.27)
- KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3764, phi -0.239)

portfolios: A EV +4.06 (adj +0.94) on $16.67, P(profit) 0.6208, adj growth 9.0 bp · B EV +3.93 (adj +1.38) on $21.62, P(profit) 0.8075, adj growth 13.4 bp · C EV +1.86 (adj +0.87) on $23.76, P(profit) 0.6343, adj growth 8.4 bp · R EV +0.19 (adj +0.12) on $2.00, P(profit) 0.7706, adj growth 4.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
