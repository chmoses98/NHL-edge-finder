# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-06T22:37:02Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +30.94 | +8.55 | +28.35 | 0.810 | -12.05 | -21.66 | 79.71 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +28.42 | +12.71 | +26.71 | 0.785 | -14.85 | -25.34 | 121.10 |
| C best expression per thesis | 150.00 | +19.00 | +8.10 | +18.37 | 0.745 | -17.25 | -26.49 | 76.91 |
| R FUNDED research stakes | 16.00 | +1.92 | +1.30 | +0.95 | 0.618 | -5.41 | -6.77 | 0.00 |

## NSH @ TOR  ·  10000 joint draws  ·  392 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.593 / away 0.407

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
| Gavin McKenna: 1+ goals NO | 79 | 0.846 | 0.831 | +0.044 | +0.029 | $8.10 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 10 | 0.136 | 0.126 | +0.030 | +0.020 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Adam Wilsby: 1+ goals YES | 4 | 0.062 | 0.056 | +0.020 | +0.013 | $1.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Alexander Kerfoot: 1+ goals YES | 12 | 0.156 | 0.145 | +0.028 | +0.018 | $1.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (11.65 vs 6.63 bp); relationships: KXNHLGOAL-26OCT06NSHTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT06NSHTOR-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06NSHTOR-NSHAKERFOOT14-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: TOR offense succeeds (4+ goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT06NSHTOR-TOR2|yes; why: higher confidence-adjusted growth (8.81 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.893 vs 0.792); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT06NSHTOR-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06NSHTOR-NSHAKERFOOT14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: TOR offense suppressed (<= 2 goals)
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (8.57 vs 5.65 bp); despite a smaller raw edge (+0.020 vs +0.036/contract); relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06NSHTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06NSHTOR-NSHAKERFOOT14-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NSH offense suppressed (<= 2 goals)
- **Alexander Kerfoot: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (6.33 vs 5.65 bp); despite a smaller raw edge (+0.028 vs +0.036/contract); relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT06NSHTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT06NSHTOR-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis TOR:SUPPRESSED (p 0.392): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS (p 0.4822): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.3613): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3838, phi -0.171)
- KXNHLGOAL-26OCT06NSHTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.392, phi -0.168)
- KXNHLGOAL-26OCT06NSHTOR-NSHAWILSBY2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4239, phi -0.107)
- KXNHLGOAL-26OCT06NSHTOR-NSHAKERFOOT14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4239, phi -0.188)

portfolios: A EV +2.61 (adj +0.62) on $16.67, P(profit) 0.6697, adj growth 5.8 bp · B EV +1.99 (adj +1.30) on $13.23, P(profit) 0.3147, adj growth 12.3 bp · C EV +1.03 (adj +0.64) on $11.53, P(profit) 0.7615, adj growth 6.0 bp · R EV +0.16 (adj +0.11) on $3.00, P(profit) 0.8457, adj growth 4.2 bp

## CAR @ MTL  ·  10000 joint draws  ·  396 bet sides mapped, 12 +EV candidates, 4 on card

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
| Jake Evans: 1+ goals YES | 11 | 0.143 | 0.132 | +0.026 | +0.015 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 74 | 0.785 | 0.773 | +0.032 | +0.019 | $7.91 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Alexandre Texier: 1+ goals YES | 12 | 0.150 | 0.141 | +0.022 | +0.014 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ assists NO | 73 | 0.855 | 0.761 | +0.111 | +0.017 | $8.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLSPREAD-26OCT06CARMTL-CAR3|no; why: higher confidence-adjusted growth (4.86 vs 2.09 bp); despite a smaller raw edge (+0.026 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.021); failure: MTL offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06CARMTL-CARSAHO20-1|no; why: higher confidence-adjusted growth (4.36 vs 3.41 bp); despite a smaller raw edge (+0.032 vs +0.097/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CAR offense succeeds (4+ goals)
- **Alexandre Texier: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes has the higher standalone adjusted growth (4.86 vs 3.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.058); failure: MTL offense suppressed (<= 2 goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06CARMTL-MTLCKREIDER22-1|no; why: higher confidence-adjusted growth (3.30 vs 0.26 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.058); failure: MTL offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis MTL:WINS_BY_2PLUS (p 0.2989): highest fidelity KXNHLSPREAD-26OCT06CARMTL-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:OFFENSE_4PLUS (p 0.3905): highest fidelity KXNHLSPREAD-26OCT06CARMTL-CAR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.4242): highest fidelity KXNHLSPREAD-26OCT06CARMTL-CAR3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT06CARMTL-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3891, phi -0.203)
- KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3575, phi -0.21)
- KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3891, phi -0.167)
- KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.5 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3905, phi -0.167)

portfolios: A EV +1.91 (adj +0.40) on $16.67, P(profit) 0.7057, adj growth 3.9 bp · B EV +2.18 (adj +0.77) on $19.21, P(profit) 0.7548, adj growth 7.3 bp · C EV +1.01 (adj +0.52) on $15.53, P(profit) 0.7125, adj growth 4.9 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.7852, adj growth 1.9 bp

## OTT @ DET  ·  10000 joint draws  ·  374 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.526 / away 0.474

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_OTT_win | p_overtime | goals | shots DET/OTT | DET/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.55 | 0.45 | 0.00 | 5.97 | 27.0/27.2 | 24.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.48 | 5.92 | 27.0/27.1 | 24.0/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.59 | 0.41 | 0.00 | 9.21 | 28.2/28.6 | 23.0/21.9 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.079 | 0.49 | 0.51 | 0.00 | 6.0 | 21.6/32.3 | 28.6/18.2 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.46 | 0.54 | 0.48 | 5.89 | 21.6/32.6 | 29.2/18.5 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.061 | 0.64 | 0.36 | 0.00 | 5.99 | 31.2/21.2 | 18.5/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Eklund: 1+ assists NO | 66 | 0.854 | 0.721 | +0.178 | +0.046 | $8.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Andrew Copp: 1+ goals YES | 18 | 0.234 | 0.220 | +0.044 | +0.029 | $3.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 39 | 0.457 | 0.439 | +0.050 | +0.032 | $5.42 | FUNDED_RESEARCH | $2 | DET:OFFENSE_4PLUS | DIRECT (0.64) | EVIDENCE_STRONGER | D |
| Jordan Spence: 1+ assists YES | 26 | 0.340 | 0.297 | +0.067 | +0.024 | $3.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (21.00 vs 6.84 bp); relationships: KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.035); failure: OTT offense succeeds (4+ goals)
- **Andrew Copp: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes; why: higher confidence-adjusted growth (11.89 vs 9.24 bp); despite a smaller raw edge (+0.044 vs +0.050/contract); relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: DET offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes has the higher standalone adjusted growth (11.89 vs 9.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.021); they share one thesis budget; relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: DET offense suppressed (<= 2 goals)
- **Jordan Spence: 1+ assists YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06OTTDET-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (6.32 vs 0.49 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis DET:OFFENSE_4PLUS (p 0.3946): highest fidelity KXNHLPTS-26OCT06OTTDET-DETACOPP18-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:SUPPRESSED (p 0.4335): highest fidelity KXNHLAST-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no (same contract)
- thesis DET:SUPPRESSED (p 0.3844): highest fidelity KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no (same contract)
- KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.4 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3443, phi -0.17)
- KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3844, phi -0.221)
- KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 36% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.3844, phi -0.322)
- KXNHLAST-26OCT06OTTDET-OTTJSPENCE10-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4335, phi -0.274)

portfolios: A EV +4.64 (adj +0.73) on $16.67, P(profit) 0.6861, adj growth 7.0 bp · B EV +4.39 (adj +1.79) on $20.24, P(profit) 0.6647, adj growth 17.2 bp · C EV +3.78 (adj +1.43) on $23.02, P(profit) 0.781, adj growth 13.6 bp · R EV +0.25 (adj +0.16) on $2.00, P(profit) 0.4565, adj growth 5.8 bp

## UTA @ NJD  ·  10000 joint draws  ·  416 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.531 / away 0.469

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
| Vincent Trocheck: 1+ assists NO | 67 | 0.842 | 0.724 | +0.156 | +0.038 | $7.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Lawson Crouse: 1+ goals YES | 16 | 0.213 | 0.198 | +0.043 | +0.029 | $3.14 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Luke Evangelista: 1+ assists NO | 64 | 0.808 | 0.689 | +0.152 | +0.033 | $7.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Cody Glass: 1+ goals YES | 11 | 0.143 | 0.133 | +0.026 | +0.016 | $1.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06UTANJ-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (14.86 vs 0.18 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0042 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: UTA offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06UTANJ-UTAALEE72-1|yes; why: higher confidence-adjusted growth (12.88 vs 1.52 bp); relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: UTA offense suppressed (<= 2 goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06UTANJ-NJJHUGHES86-2|no; why: higher confidence-adjusted growth (10.66 vs 2.77 bp); relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.021); failure: NJD offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06UTANJ-NJAMANTHA39-1|yes; why: higher confidence-adjusted growth (5.64 vs 0.20 bp); alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi -0.021); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis UTA:OFFENSE_4PLUS (p 0.3787): highest fidelity KXNHLGOAL-26OCT06UTANJ-UTAALEE72-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4288): highest fidelity KXNHLAST-26OCT06UTANJ-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06UTANJ-NJTMEIER28-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.4005): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.2 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3787, phi -0.17)
- KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4005, phi -0.214)
- KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.3 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3519, phi -0.199)
- KXNHLGOAL-26OCT06UTANJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4288, phi -0.175)

portfolios: A EV +2.46 (adj +0.56) on $16.67, P(profit) 0.6673, adj growth 5.5 bp · B EV +4.72 (adj +1.59) on $20.24, P(profit) 0.7811, adj growth 15.3 bp · C EV +1.49 (adj +0.78) on $12.96, P(profit) 0.2129, adj growth 7.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ BUF  ·  10000 joint draws  ·  396 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.495 / away 0.505

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
| Yakov Trenin: 1+ goals YES | 9 | 0.147 | 0.132 | +0.052 | +0.036 | $3.31 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 21 | 0.349 | 0.252 | +0.128 | +0.031 | $2.47 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Peyton Krebs: 1+ goals YES | 11 | 0.142 | 0.133 | +0.025 | +0.016 | $1.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Michael McCarron: 1+ goals YES | 10 | 0.129 | 0.120 | +0.022 | +0.014 | $1.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (31.50 vs 11.82 bp); despite a smaller raw edge (+0.052 vs +0.128/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.133); KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT06MINBUF-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (11.82 vs 3.27 bp); despite a smaller raw edge (+0.128 vs +0.138/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.133); KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT06MINBUF-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi 0.033); failure: MIN offense suppressed (<= 2 goals)
- **Peyton Krebs: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes; why: higher confidence-adjusted growth (5.18 vs 0.92 bp); alternative not eligible: confidence-adjusted EV +0.0077 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT06MINBUF-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: BUF offense suppressed (<= 2 goals)
- **Michael McCarron: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (11.82 vs 4.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.033); they share one thesis budget; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.033); KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4011): highest fidelity KXNHLPTS-26OCT06MINBUF-MINRHARTMAN38-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:OFFENSE_4PLUS (p 0.4008): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis BUF:SUPPRESSED (p 0.384): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3801, phi -0.165)
- KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.9 pts; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3801, phi -0.289)
- KXNHLGOAL-26OCT06MINBUF-BUFPKREBS19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.384, phi -0.178)
- KXNHLGOAL-26OCT06MINBUF-MINMMCCARRON47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3801, phi -0.167)

portfolios: A EV +7.27 (adj +2.56) on $16.67, P(profit) 0.4581, adj growth 22.8 bp · B EV +3.87 (adj +2.00) on $8.88, P(profit) 0.5644, adj growth 18.8 bp · C EV +2.08 (adj +0.50) on $3.61, P(profit) 0.3495, adj growth 4.7 bp · R EV +0.54 (adj +0.38) on $1.00, P(profit) 0.1473, adj growth 14.0 bp

## NYI @ NYR  ·  10000 joint draws  ·  406 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.588 / away 0.412

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
| Ondrej Palat: 1+ goals YES | 8 | 0.111 | 0.101 | +0.026 | +0.016 | $1.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Vladislav Gavrikov: 1+ assists YES | 26 | 0.327 | 0.289 | +0.054 | +0.015 | $2.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_MIXED | D |
| Bo Horvat: 1+ goals NO | 70 | 0.738 | 0.728 | +0.024 | +0.013 | $4.77 | FUNDED_RESEARCH | $2 | NYI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ goals NO | 66 | 0.698 | 0.687 | +0.022 | +0.011 | $4.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT06NYINYR-NYI3|yes; why: higher confidence-adjusted growth (6.83 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT06NYINYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: NYI offense suppressed (<= 2 goals)
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06NYINYR-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (2.51 vs 0.87 bp); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06NYINYR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT06NYINYR-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.097); failure: NYR offense suppressed (<= 2 goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no; why: Player prop expression KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no selected over player prop KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT06NYINYR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT06NYINYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NYI offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06NYINYR-NYRSDURZI5-1|no; why: higher confidence-adjusted growth (1.25 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.033/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06NYINYR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.097); KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYI shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:SUPPRESSED (p 0.4901): highest fidelity KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no (same contract)
- thesis NYR:OFFENSE_4PLUS (p 0.4177): highest fidelity KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.3608): highest fidelity KXNHLGOAL-26OCT06NYINYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NYINYR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT06NYINYR-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4901, phi -0.181)
- KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3608, phi -0.245)
- KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.2881, phi -0.241)
- KXNHLGOAL-26OCT06NYINYR-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.4177, phi -0.231)
- override: Player prop expression KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no selected over player prop KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.49 (adj +0.78) on $16.67, P(profit) 0.4019, adj growth 7.2 bp · B EV +1.19 (adj +0.56) on $12.60, P(profit) 0.6957, adj growth 5.3 bp · C EV +1.81 (adj +0.43) on $16.35, P(profit) 0.675, adj growth 4.1 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.7383, adj growth 1.3 bp

## STL @ CHI  ·  10000 joint draws  ·  394 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.434 / away 0.566

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
| Ryan Greene: 1+ goals YES | 11 | 0.169 | 0.153 | +0.052 | +0.036 | $3.44 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Philip Broberg: 1+ goals YES | 7 | 0.100 | 0.091 | +0.026 | +0.017 | $1.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 59 | 0.738 | 0.635 | +0.131 | +0.029 | $7.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Mason McTavish: 1+ assists NO | 70 | 0.786 | 0.738 | +0.072 | +0.023 | $7.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06STLCHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (26.53 vs 0.22 bp); alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.031); KXNHLAST-26OCT06STLCHI-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: CHI offense suppressed (<= 2 goals)
- **Philip Broberg: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06STLCHI-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (8.86 vs 0.04 bp); alternative not eligible: confidence-adjusted EV +0.0019 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT06STLCHI-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.024); failure: STL offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06STLCHI-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (7.46 vs 2.77 bp); relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT06STLCHI-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: CHI offense succeeds (4+ goals)
- **Mason McTavish: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06STLCHI-STLMMCTAVISH83-1|no; why: higher confidence-adjusted growth (5.93 vs 1.66 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: STL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CHI:OFFENSE_4PLUS (p 0.3242): highest fidelity KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4578): highest fidelity KXNHLAST-26OCT06STLCHI-CHIBBYRAM24-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:SUPPRESSED (p 0.3661): highest fidelity KXNHLGOAL-26OCT06STLCHI-STLMMCTAVISH83-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06STLCHI-STLMMCTAVISH83-1|no (same contract)
- KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4578, phi -0.22)
- KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3661, phi -0.113)
- KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3242, phi -0.242)
- KXNHLAST-26OCT06STLCHI-STLMMCTAVISH83-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4172, phi -0.205)

portfolios: A EV +3.42 (adj +1.47) on $16.67, P(profit) 0.561, adj growth 14.0 bp · B EV +4.47 (adj +2.01) on $20.24, P(profit) 0.6894, adj growth 19.1 bp · C EV +3.56 (adj +1.64) on $23.02, P(profit) 0.6193, adj growth 15.7 bp · R EV +0.44 (adj +0.31) on $1.00, P(profit) 0.1687, adj growth 11.5 bp

## VGK @ SEA  ·  10000 joint draws  ·  384 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.395 / away 0.605

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
| Ryan Winterton: 1+ goals YES | 10 | 0.141 | 0.129 | +0.034 | +0.023 | $2.33 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 70 | 0.760 | 0.744 | +0.045 | +0.029 | $8.10 | FUNDED_RESEARCH | $3 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 8 | 0.114 | 0.103 | +0.029 | +0.018 | $1.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Matty Beniers: 1+ goals YES | 18 | 0.228 | 0.215 | +0.038 | +0.025 | $2.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06VGKSEA-SEAMBENIERS10-1|yes; why: higher confidence-adjusted growth (11.89 vs 8.47 bp); despite a smaller raw edge (+0.034 vs +0.038/contract); relationships: KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT06VGKSEA-SEAMBENIERS10-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: SEA offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK3|no; why: higher confidence-adjusted growth (9.07 vs 6.54 bp); despite a smaller raw edge (+0.045 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT06VGKSEA-SEAMBENIERS10-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: VGK offense succeeds (4+ goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes has the higher standalone adjusted growth (11.89 vs 9.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT06VGKSEA-SEAMBENIERS10-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)
- **Matty Beniers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes has the higher standalone adjusted growth (11.89 vs 8.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.3591): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.402): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4912): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no (same contract)
- KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4263, phi -0.186)
- KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3788, phi -0.223)
- KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4263, phi -0.17)
- KXNHLGOAL-26OCT06VGKSEA-SEAMBENIERS10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4263, phi -0.228)

portfolios: A EV +2.16 (adj +0.53) on $16.67, P(profit) 0.6885, adj growth 4.8 bp · B EV +2.45 (adj +1.58) on $15.11, P(profit) 0.4115, adj growth 15.0 bp · C EV +2.21 (adj +1.21) on $20.96, P(profit) 0.6842, adj growth 11.4 bp · R EV +0.19 (adj +0.12) on $3.00, P(profit) 0.7599, adj growth 4.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT06VGKSEA-VGK|no == KXNHLGAME-26OCT06VGKSEA-SEA|yes

## FLA @ LAK  ·  10000 joint draws  ·  416 bet sides mapped, 21 +EV candidates, 4 on card

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
| Sam Reinhart: 1+ goals NO | 69 | 0.771 | 0.749 | +0.066 | +0.044 | $7.04 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 1+ assists NO | 64 | 0.789 | 0.685 | +0.133 | +0.029 | $7.04 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Alex Laferriere: 1+ goals YES | 23 | 0.275 | 0.262 | +0.032 | +0.020 | $2.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 49 | 0.610 | 0.529 | +0.103 | +0.021 | $3.73 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06FLALA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (20.79 vs 8.50 bp); relationships: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT06FLALA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: FLA offense succeeds (4+ goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06FLALA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (8.41 vs 6.59 bp); relationships: KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.113); KXNHLAST-26OCT06FLALA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.054); failure: LAK offense succeeds (4+ goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06FLALA-FLA2|no; why: Player prop expression KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes selected over player prop KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.40 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.113); KXNHLAST-26OCT06FLALA-LAAPANARIN10-1|no: INTENTIONAL_DIVERSIFIER (phi -0.064); failure: LAK offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06FLALA-LAAPANARIN10-2|no; why: KXNHLAST-26OCT06FLALA-LAAPANARIN10-2|no has the higher standalone adjusted growth (6.59 vs 3.98 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.379); relationships: KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.054); KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.064); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis FLA:SUPPRESSED (p 0.4918): highest fidelity KXNHLTEAMTOTAL-26OCT06FLALA-FLA4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.4049): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no — Player prop expression KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes selected over player prop KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.40 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis LAK:WINS (p 0.5803): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no (same contract)
- KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.2891, phi -0.237)
- KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.9 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4049, phi -0.188)
- KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3764, phi -0.239)
- KXNHLAST-26OCT06FLALA-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.5 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4049, phi -0.279)
- override: Player prop expression KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes selected over player prop KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.40 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.98 (adj +0.90) on $16.67, P(profit) 0.6208, adj growth 8.6 bp · B EV +3.15 (adj +1.11) on $20.24, P(profit) 0.6865, adj growth 10.8 bp · C EV +2.03 (adj +0.95) on $23.02, P(profit) 0.5718, adj growth 9.2 bp · R EV +0.19 (adj +0.13) on $2.00, P(profit) 0.7706, adj growth 4.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
