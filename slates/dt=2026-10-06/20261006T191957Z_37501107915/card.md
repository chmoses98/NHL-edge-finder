# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-06T19:19:57Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +30.84 | +6.94 | +29.54 | 0.842 | -8.08 | -17.76 | 64.52 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +25.62 | +11.69 | +23.43 | 0.782 | -14.22 | -23.89 | 111.61 |
| C best expression per thesis | 149.99 | +19.49 | +8.49 | +17.99 | 0.749 | -15.93 | -25.06 | 80.80 |
| R FUNDED research stakes | 18.00 | +1.99 | +1.21 | +1.58 | 0.555 | -4.62 | -6.13 | 0.00 |

## NSH @ TOR  ·  10000 joint draws  ·  392 bet sides mapped, 11 +EV candidates, 4 on card

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
| Gavin McKenna: 1+ goals NO | 79 | 0.846 | 0.831 | +0.044 | +0.029 | $6.34 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ goals NO | 60 | 0.660 | 0.643 | +0.043 | +0.027 | $5.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 25 | 0.299 | 0.286 | +0.036 | +0.022 | $2.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ goals YES | 17 | 0.206 | 0.196 | +0.026 | +0.016 | $1.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (11.65 vs 6.63 bp); relationships: KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: TOR offense succeeds (4+ goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT06NSHTOR-TOR2|no; why: higher confidence-adjusted growth (6.63 vs 1.64 bp); despite a smaller raw edge (+0.043 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: TOR offense succeeds (4+ goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes; why: higher confidence-adjusted growth (5.65 vs 3.57 bp); relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NSH offense suppressed (<= 2 goals)
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes has the higher standalone adjusted growth (5.65 vs 3.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis TOR:SUPPRESSED (p 0.392): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:WINS (p 0.4822): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.3613): highest fidelity KXNHLSPREAD-26OCT06NSHTOR-TOR3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT06NSHTOR-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3838, phi -0.171)
- KXNHLGOAL-26OCT06NSHTOR-TORAMATTHEWS34-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.3838, phi -0.291)
- KXNHLGOAL-26OCT06NSHTOR-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4239, phi -0.25)
- KXNHLGOAL-26OCT06NSHTOR-NSHMBOURQUE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4239, phi -0.214)

portfolios: A EV +3.01 (adj +0.54) on $16.67, P(profit) 0.6314, adj growth 4.9 bp · B EV +1.33 (adj +0.84) on $15.99, P(profit) 0.7275, adj growth 8.1 bp · C EV +0.96 (adj +0.60) on $10.74, P(profit) 0.7615, adj growth 5.7 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.8457, adj growth 2.8 bp

## CAR @ MTL  ·  10000 joint draws  ·  396 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.459 / away 0.541

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
| Chris Kreider: 1+ assists NO | 71 | 0.855 | 0.751 | +0.131 | +0.027 | $7.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Jake Evans: 1+ goals YES | 11 | 0.143 | 0.132 | +0.026 | +0.015 | $1.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 74 | 0.785 | 0.773 | +0.032 | +0.019 | $7.49 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Alexandre Texier: 1+ goals YES | 12 | 0.150 | 0.141 | +0.022 | +0.014 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06CARMTL-MTLCKREIDER22-1|no; why: higher confidence-adjusted growth (7.78 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.058); failure: MTL offense succeeds (4+ goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLSPREAD-26OCT06CARMTL-CAR3|no; why: higher confidence-adjusted growth (4.86 vs 0.85 bp); despite a smaller raw edge (+0.026 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0077 below the 0.010/contract floor; relationships: KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: MTL offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06CARMTL-CARSGOSTISBEHERE4-1|no; why: higher confidence-adjusted growth (4.36 vs 3.41 bp); despite a smaller raw edge (+0.032 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CAR offense succeeds (4+ goals)
- **Alexandre Texier: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes has the higher standalone adjusted growth (4.86 vs 3.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.058); KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.15, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis MTL:WINS_BY_2PLUS (p 0.2989): highest fidelity KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.3905): highest fidelity KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes (same contract)
- thesis CAR:SUPPRESSED (p 0.4242): highest fidelity KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no (same contract)
- KXNHLAST-26OCT06CARMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.0 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.3905, phi -0.167)
- KXNHLGOAL-26OCT06CARMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3891, phi -0.203)
- KXNHLGOAL-26OCT06CARMTL-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.3575, phi -0.21)
- KXNHLGOAL-26OCT06CARMTL-MTLATEXIER85-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3891, phi -0.167)

portfolios: A EV +1.49 (adj +0.48) on $16.67, P(profit) 0.7552, adj growth 4.6 bp · B EV +2.30 (adj +0.83) on $18.18, P(profit) 0.7548, adj growth 8.0 bp · C EV +0.72 (adj +0.43) on $10.07, P(profit) 0.812, adj growth 4.1 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.7852, adj growth 1.9 bp

## OTT @ DET  ·  10000 joint draws  ·  376 bet sides mapped, 16 +EV candidates, 4 on card

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
| William Eklund: 1+ assists NO | 67 | 0.849 | 0.729 | +0.163 | +0.044 | $7.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Nate Danielson: 1+ goals YES | 9 | 0.129 | 0.118 | +0.033 | +0.022 | $2.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Andrew Copp: 1+ goals YES | 18 | 0.228 | 0.215 | +0.038 | +0.025 | $2.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 40 | 0.443 | 0.430 | +0.026 | +0.013 | $2.06 | FUNDED_RESEARCH | $1 | DET:OFFENSE_4PLUS | DIRECT (0.63) | EVIDENCE_STRONGER | D |
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (19.63 vs 5.01 bp); relationships: KXNHLGOAL-26OCT06OTTDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: OTT offense succeeds (4+ goals)
- **Nate Danielson: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-2|yes; why: higher confidence-adjusted growth (12.07 vs 11.31 bp); wins across more scripts (relative breadth 0.921 vs 0.757); relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: DET offense suppressed (<= 2 goals)
- **Andrew Copp: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-2|yes; why: KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-2|yes has the higher standalone adjusted growth (11.31 vs 8.57 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.014); relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT06OTTDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: DET offense suppressed (<= 2 goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-2|yes; why: Player prop expression KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-2|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.63 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT06OTTDET-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis DET:OFFENSE_4PLUS (p 0.3797): highest fidelity KXNHLPTS-26OCT06OTTDET-DETACOPP18-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT06OTTDET-DETEFINNIE58-1|yes — override declined: the joint re-optimisation gives KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes less than the minimum stake; KXNHLGOAL-26OCT06OTTDET-DETNDANIELSON29-1|yes kept
- thesis DET:SUPPRESSED (p 0.4024): highest fidelity KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-DETVARVIDSSON33-1|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4377): highest fidelity KXNHLAST-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06OTTDET-OTTCYAKEMCHUK26-1|no (same contract)
- KXNHLAST-26OCT06OTTDET-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.4 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3428, phi -0.175)
- KXNHLGOAL-26OCT06OTTDET-DETNDANIELSON29-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4024, phi -0.157)
- KXNHLGOAL-26OCT06OTTDET-DETACOPP18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4024, phi -0.217)
- KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 37% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4024, phi -0.305)
- override: override declined: the joint re-optimisation gives KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes less than the minimum stake; KXNHLGOAL-26OCT06OTTDET-DETNDANIELSON29-1|yes kept
- override: Player prop expression KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-1|yes selected over player prop KXNHLGOAL-26OCT06OTTDET-DETADEBRINCAT93-2|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.63 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +3.98 (adj +0.66) on $16.67, P(profit) 0.6737, adj growth 6.3 bp · B EV +3.26 (adj +1.42) on $14.70, P(profit) 0.5826, adj growth 13.6 bp · C EV +3.71 (adj +1.25) on $21.43, P(profit) 0.6571, adj growth 11.9 bp · R EV +0.06 (adj +0.03) on $1.00, P(profit) 0.4432, adj growth 1.1 bp

## UTA @ NJD  ·  10000 joint draws  ·  416 bet sides mapped, 8 +EV candidates, 4 on card

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
| Vincent Trocheck: 1+ assists NO | 67 | 0.842 | 0.727 | +0.156 | +0.041 | $6.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Luke Evangelista: 1+ assists NO | 65 | 0.808 | 0.696 | +0.142 | +0.030 | $6.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Lawson Crouse: 1+ goals YES | 17 | 0.213 | 0.200 | +0.033 | +0.020 | $1.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 73 | 0.768 | 0.757 | +0.024 | +0.013 | $3.40 | FUNDED_RESEARCH | $1 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT06UTANJ-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (17.51 vs 0.70 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT06UTANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: UTA offense succeeds (4+ goals)
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06UTANJ-NJAMANTHA39-1|no; why: higher confidence-adjusted growth (8.76 vs 5.30 bp); relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06UTANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.135); failure: NJD offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06UTANJ-UTAALEE72-1|yes; why: higher confidence-adjusted growth (5.75 vs 1.19 bp); alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.033); KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06UTANJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: UTA offense suppressed (<= 2 goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06UTANJ-NJAMANTHA39-1|no; why: Player prop expression KXNHLGOAL-26OCT06UTANJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT06UTANJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.88 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis UTA:OFFENSE_4PLUS (p 0.3787): highest fidelity KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes (same contract)
- thesis NJD:SUPPRESSED (p 0.4288): highest fidelity KXNHLAST-26OCT06UTANJ-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT06UTANJ-NJAMANTHA39-1|no — Player prop expression KXNHLGOAL-26OCT06UTANJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT06UTANJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.88 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis UTA:SUPPRESSED (p 0.4005): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT06UTANJ-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.7 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3787, phi -0.17)
- KXNHLAST-26OCT06UTANJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.3 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3519, phi -0.199)
- KXNHLGOAL-26OCT06UTANJ-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4005, phi -0.214)
- KXNHLGOAL-26OCT06UTANJ-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3519, phi -0.225)
- override: Player prop expression KXNHLGOAL-26OCT06UTANJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT06UTANJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.88 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.72 (adj +0.71) on $16.67, P(profit) 0.6924, adj growth 6.8 bp · B EV +3.51 (adj +1.00) on $19.14, P(profit) 0.7449, adj growth 9.7 bp · C EV +1.20 (adj +0.51) on $11.01, P(profit) 0.8569, adj growth 4.8 bp · R EV +0.03 (adj +0.02) on $1.00, P(profit) 0.7676, adj growth 0.7 bp

## MIN @ BUF  ·  10000 joint draws  ·  396 bet sides mapped, 11 +EV candidates, 4 on card

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
| Yakov Trenin: 1+ goals YES | 9 | 0.147 | 0.132 | +0.052 | +0.036 | $3.05 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 20 | 0.349 | 0.249 | +0.138 | +0.038 | $2.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
| Jiri Kulich: 1+ goals YES | 13 | 0.184 | 0.170 | +0.047 | +0.032 | $3.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Olli Maatta: 1+ goals YES | 4 | 0.066 | 0.059 | +0.023 | +0.017 | $1.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (31.50 vs 18.55 bp); despite a smaller raw edge (+0.052 vs +0.138/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.133); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT06MINBUF-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06MINBUF-MINJERIKSSONEK14-1|yes; why: higher confidence-adjusted growth (18.55 vs 3.12 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.133); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06MINBUF-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.036); failure: MIN offense suppressed (<= 2 goals)
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT06MINBUF-BUF2|yes; why: higher confidence-adjusted growth (18.09 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06MINBUF-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: BUF offense suppressed (<= 2 goals)
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (18.55 vs 14.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.036); they share one thesis budget; relationships: KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.036); KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4011): highest fidelity KXNHLPTS-26OCT06MINBUF-MINRHARTMAN38-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:OFFENSE_4PLUS (p 0.4008): highest fidelity KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes (same contract)
- thesis BUF:SUPPRESSED (p 0.384): highest fidelity KXNHLAST-26OCT06MINBUF-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06MINBUF-BUFTTHOMPSON72-1|no (same contract)
- KXNHLGOAL-26OCT06MINBUF-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3801, phi -0.165)
- KXNHLAST-26OCT06MINBUF-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.4 pts; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3801, phi -0.289)
- KXNHLGOAL-26OCT06MINBUF-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.384, phi -0.202)
- KXNHLGOAL-26OCT06MINBUF-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3801, phi -0.115)

portfolios: A EV +6.64 (adj +2.25) on $16.67, P(profit) 0.517, adj growth 20.4 bp · B EV +5.36 (adj +2.95) on $10.50, P(profit) 0.5574, adj growth 27.8 bp · C EV +4.62 (adj +1.78) on $19.91, P(profit) 0.4632, adj growth 16.9 bp · R EV +0.54 (adj +0.38) on $1.00, P(profit) 0.1473, adj growth 14.0 bp

## NYI @ NYR  ·  10000 joint draws  ·  410 bet sides mapped, 7 +EV candidates, 4 on card

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
| Matthew Schaefer: 1+ goals NO | 81 | 0.854 | 0.842 | +0.033 | +0.021 | $6.17 | FUNDED_RESEARCH | $2 | NYI:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Vladislav Gavrikov: 1+ assists YES | 26 | 0.337 | 0.293 | +0.063 | +0.020 | $1.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Bo Horvat: 1+ goals NO | 69 | 0.738 | 0.725 | +0.033 | +0.020 | $4.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Oliver Bjorkstrand: 1+ goals NO | 83 | 0.864 | 0.854 | +0.024 | +0.014 | $6.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
- **Matthew Schaefer: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no; why: higher confidence-adjusted growth (6.52 vs 4.23 bp); despite a smaller raw edge (+0.033 vs +0.033/contract); relationships: KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT06NYINYR-NYROBJORKSTRAND28-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: NYI offense succeeds (4+ goals)
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06NYINYR-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (4.37 vs 0.41 bp); alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06NYINYR-NYIMSCHAEFER48-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT06NYINYR-NYROBJORKSTRAND28-1|no: INTENTIONAL_DIVERSIFIER (phi -0.052); failure: NYR offense suppressed (<= 2 goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no; why: higher confidence-adjusted growth (4.23 vs 2.34 bp); despite a smaller raw edge (+0.033 vs +0.085/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06NYINYR-NYIMSCHAEFER48-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT06NYINYR-NYROBJORKSTRAND28-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: NYI offense succeeds (4+ goals)
- **Oliver Bjorkstrand: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06NYINYR-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (3.35 vs 1.02 bp); relationships: KXNHLGOAL-26OCT06NYINYR-NYIMSCHAEFER48-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYI shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYR:OFFENSE_4PLUS (p 0.4177): highest fidelity KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes (same contract)
- thesis NYI:SUPPRESSED (p 0.4901): highest fidelity KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.3608): highest fidelity KXNHLGOAL-26OCT06NYINYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NYINYR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT06NYINYR-NYIMSCHAEFER48-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.2881, phi -0.172)
- KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3608, phi -0.251)
- KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.2881, phi -0.241)
- KXNHLGOAL-26OCT06NYINYR-NYROBJORKSTRAND28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.4177, phi -0.148)

portfolios: A EV +1.93 (adj +0.57) on $16.67, P(profit) 0.6929, adj growth 5.4 bp · B EV +1.09 (adj +0.54) on $19.14, P(profit) 0.6762, adj growth 5.2 bp · C EV +1.14 (adj +0.48) on $14.45, P(profit) 0.6569, adj growth 4.6 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.8538, adj growth 2.0 bp

## STL @ CHI  ·  10000 joint draws  ·  394 bet sides mapped, 12 +EV candidates, 4 on card

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
| Ryan Greene: 1+ goals YES | 11 | 0.169 | 0.153 | +0.052 | +0.036 | $3.54 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Philip Broberg: 1+ goals YES | 7 | 0.100 | 0.091 | +0.026 | +0.017 | $1.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 59 | 0.738 | 0.635 | +0.131 | +0.029 | $7.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Oliver Moore: 1+ goals YES | 11 | 0.146 | 0.136 | +0.029 | +0.019 | $1.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06STLCHI-CHITBERTUZZI59-2|yes; why: higher confidence-adjusted growth (26.53 vs 0.61 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.944 vs 0.772); alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT06STLCHI-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: CHI offense suppressed (<= 2 goals)
- **Philip Broberg: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06STLCHI-STLPBUCHNEVICH89-1|yes; why: higher confidence-adjusted growth (8.86 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT06STLCHI-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: STL offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06STLCHI-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (7.46 vs 2.77 bp); relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT06STLCHI-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.034); failure: CHI offense succeeds (4+ goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes has the higher standalone adjusted growth (26.53 vs 7.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.034); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CHI:OFFENSE_4PLUS (p 0.3242): highest fidelity KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4578): highest fidelity KXNHLAST-26OCT06STLCHI-CHIBBYRAM24-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:SUPPRESSED (p 0.3661): highest fidelity KXNHLGOAL-26OCT06STLCHI-STLMMCTAVISH83-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06STLCHI-STLMMCTAVISH83-1|no (same contract)
- KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4578, phi -0.22)
- KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3661, phi -0.113)
- KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3242, phi -0.242)
- KXNHLGOAL-26OCT06STLCHI-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4578, phi -0.183)

portfolios: A EV +2.67 (adj +0.44) on $16.67, P(profit) 0.6895, adj growth 4.2 bp · B EV +4.25 (adj +2.11) on $14.70, P(profit) 0.3622, adj growth 20.0 bp · C EV +3.40 (adj +1.59) on $21.43, P(profit) 0.6193, adj growth 15.2 bp · R EV +0.44 (adj +0.31) on $1.00, P(profit) 0.1687, adj growth 11.5 bp

## VGK @ SEA  ·  10000 joint draws  ·  382 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.396 / away 0.604

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
| Ryan Winterton: 1+ goals YES | 10 | 0.141 | 0.129 | +0.034 | +0.023 | $2.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 70 | 0.760 | 0.744 | +0.045 | +0.029 | $7.66 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Vegas wins by over 2.5 goals NO | 74 | 0.819 | 0.777 | +0.065 | +0.024 | $7.47 | FUNDED_RESEARCH | $2 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Shane Wright: 1+ goals YES | 16 | 0.196 | 0.183 | +0.027 | +0.014 | $1.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK3|no; why: higher confidence-adjusted growth (11.89 vs 6.54 bp); despite a smaller raw edge (+0.034 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: MOSTLY_INDEPENDENT (phi 0.095); KXNHLGOAL-26OCT06VGKSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: SEA offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06VGKSEA-VGKJEICHEL9-2|no; why: higher confidence-adjusted growth (9.07 vs 7.14 bp); despite a smaller raw edge (+0.045 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: MOSTLY_INDEPENDENT (phi 0.13); KXNHLGOAL-26OCT06VGKSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: VGK offense succeeds (4+ goals)
- **Vegas wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no; why: higher confidence-adjusted growth (6.54 vs 6.10 bp); despite a smaller raw edge (+0.065 vs +0.072/contract); relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.095); KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.13); KXNHLGOAL-26OCT06VGKSEA-SEASWRIGHT51-1|yes: MOSTLY_INDEPENDENT (phi 0.107); failure: VGK wins by 2+
- **Shane Wright: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes has the higher standalone adjusted growth (11.89 vs 3.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: MOSTLY_INDEPENDENT (phi 0.107); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.3591): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.402): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4912): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no (same contract)
- KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4263, phi -0.186)
- KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3788, phi -0.223)
- KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.2913, phi -0.734)
- KXNHLGOAL-26OCT06VGKSEA-SEASWRIGHT51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4263, phi -0.221)

portfolios: A EV +3.52 (adj +0.47) on $16.67, P(profit) 0.6078, adj growth 4.1 bp · B EV +2.02 (adj +1.10) on $18.50, P(profit) 0.6842, adj growth 10.5 bp · C EV +2.05 (adj +1.13) on $19.52, P(profit) 0.6842, adj growth 10.7 bp · R EV +0.30 (adj +0.14) on $4.00, P(profit) 0.6437, adj growth 5.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT06VGKSEA-VGK|no == KXNHLGAME-26OCT06VGKSEA-SEA|yes

## FLA @ LAK  ·  10000 joint draws  ·  414 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.478 / away 0.522

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
| Mats Zuccarello: 1+ assists NO | 63 | 0.789 | 0.682 | +0.142 | +0.036 | $5.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Brady Tkachuk: 1+ goals NO | 69 | 0.749 | 0.733 | +0.044 | +0.028 | $5.98 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Florida wins by over 1.5 goals NO | 70 | 0.790 | 0.743 | +0.075 | +0.028 | $5.98 | FUNDED_RESEARCH | $2 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Trevor Moore: 1+ goals YES | 19 | 0.230 | 0.217 | +0.029 | +0.016 | $1.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06FLALA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (12.43 vs 6.59 bp); relationships: KXNHLGOAL-26OCT06FLALA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT06FLALA-FLA2|no: INTENTIONAL_DIVERSIFIER (phi -0.11); KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: LAK offense succeeds (4+ goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT06FLALA-FLA2|no; why: higher confidence-adjusted growth (8.50 vs 8.41 bp); despite a smaller raw edge (+0.044 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSPREAD-26OCT06FLALA-FLA2|no: MOSTLY_INDEPENDENT (phi 0.148); KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 1.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: higher confidence-adjusted growth (8.41 vs 7.98 bp); relationships: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.11); KXNHLGOAL-26OCT06FLALA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.148); KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes: MOSTLY_INDEPENDENT (phi 0.14); failure: FLA wins by 2+
- **Trevor Moore: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06FLALA-FLA2|no; why: Player prop expression KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes selected over player prop KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.34 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT06FLALA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSPREAD-26OCT06FLALA-FLA2|no: MOSTLY_INDEPENDENT (phi 0.14); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis FLA:SUPPRESSED (p 0.4918): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06FLALA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS (p 0.5803): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no (same contract)
- thesis LAK:OFFENSE_4PLUS (p 0.4049): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT06FLALA-FLA2|no — Player prop expression KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes selected over player prop KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.34 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.4 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4049, phi -0.188)
- KXNHLGOAL-26OCT06FLALA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.2891, phi -0.23)
- KXNHLSPREAD-26OCT06FLALA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2098, phi -1.0)
- KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3764, phi -0.223)
- override: Player prop expression KXNHLGOAL-26OCT06FLALA-LATMOORE12-1|yes selected over player prop KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.34 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.89 (adj +0.82) on $16.67, P(profit) 0.6208, adj growth 7.8 bp · B EV +2.50 (adj +0.90) on $19.14, P(profit) 0.5608, adj growth 8.8 bp · C EV +1.68 (adj +0.72) on $21.43, P(profit) 0.5559, adj growth 7.0 bp · R EV +0.34 (adj +0.16) on $4.00, P(profit) 0.6183, adj growth 6.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
