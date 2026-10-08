# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-08T13:41:30Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.97 | +31.99 | +8.93 | +30.55 | 0.756 | -25.03 | -39.01 | 79.48 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +27.14 | +11.66 | +25.11 | 0.727 | -25.79 | -38.42 | 107.72 |
| C best expression per thesis | 149.99 | +29.76 | +11.42 | +27.53 | 0.710 | -33.55 | -49.05 | 101.64 |
| R FUNDED research stakes | 18.00 | +2.36 | +1.08 | +1.63 | 0.595 | -7.20 | -9.47 | 0.00 |

## UTA @ BOS  ·  10000 joint draws  ·  170 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_UTA_win | p_overtime | goals | shots BOS/UTA | BOS/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.52 | 0.48 | 0.00 | 6.06 | 27.2/27.5 | 24.0/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.49 | 0.51 | 0.46 | 5.93 | 27.1/27.3 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.52 | 0.48 | 0.00 | 9.41 | 28.7/29.1 | 23.0/22.3 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.092 | 0.46 | 0.54 | 0.00 | 6.07 | 21.7/32.8 | 28.7/18.5 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.46 | 0.54 | 0.50 | 5.96 | 22.0/32.7 | 29.2/18.8 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.065 | 0.43 | 0.57 | 0.00 | 9.32 | 23.1/34.3 | 27.2/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 6.5 goals scored YES | 43 | 0.497 | 0.461 | +0.050 | +0.014 | $3.83 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT08UTABOS-9|yes; why: higher confidence-adjusted growth (1.68 vs 0.82 bp); wins across more scripts (relative breadth 0.689 vs 0.378); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis GAME:HIGH_EVENT (p 0.2872): highest fidelity KXNHLTOTAL-26OCT08UTABOS-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT08UTABOS-7|yes (same contract)
- KXNHLTOTAL-26OCT08UTABOS-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.2121, phi -0.516)

portfolios: A EV +0.91 (adj +0.25) on $8.19, P(profit) 0.4969, adj growth 2.1 bp · B EV +0.43 (adj +0.12) on $3.83, P(profit) 0.4969, adj growth 1.1 bp · C EV +0.59 (adj +0.16) on $5.33, P(profit) 0.4969, adj growth 1.5 bp · R EV +0.11 (adj +0.03) on $1.00, P(profit) 0.4969, adj growth 1.1 bp

## DAL @ BUF  ·  10000 joint draws  ·  328 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_DAL_win | p_overtime | goals | shots BUF/DAL | BUF/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.55 | 0.45 | 0.00 | 6.02 | 26.5/26.4 | 23.2/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.50 | 0.50 | 0.47 | 5.91 | 26.5/26.3 | 23.0/23.2 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.088 | 0.62 | 0.38 | 0.00 | 6.03 | 31.3/20.9 | 17.8/26.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.58 | 0.42 | 0.00 | 9.29 | 28.1/27.8 | 22.4/21.5 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.56 | 0.44 | 0.50 | 5.91 | 31.4/21.1 | 17.9/28.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.53 | 0.47 | 0.00 | 3.46 | 25.2/25.3 | 23.3/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jiri Kulich: 1+ goals YES | 16 | 0.214 | 0.196 | +0.045 | +0.026 | $4.55 | FUNDED_RESEARCH | $2 | BUF:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Justin Danforth: 1+ goals YES | 8 | 0.117 | 0.103 | +0.032 | +0.018 | $2.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Peyton Krebs: 1+ goals YES | 12 | 0.158 | 0.142 | +0.030 | +0.015 | $2.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes; why: higher confidence-adjusted growth (10.61 vs 4.25 bp); relationships: KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: BUF offense suppressed (<= 2 goals)
- **Justin Danforth: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes has the higher standalone adjusted growth (10.61 vs 8.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: BUF offense suppressed (<= 2 goals)
- **Peyton Krebs: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes has the higher standalone adjusted growth (10.61 vs 4.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.09.
- thesis BUF:OFFENSE_4PLUS (p 0.4032): highest fidelity KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes (same contract)
- KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.38, phi -0.22)
- KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.38, phi -0.134)
- KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.38, phi -0.193)

portfolios: A EV +3.69 (adj +2.03) on $12.71, P(profit) 0.4175, adj growth 18.0 bp · B EV +2.79 (adj +1.54) on $9.59, P(profit) 0.4175, adj growth 14.1 bp · C EV +1.67 (adj +0.98) on $6.30, P(profit) 0.2143, adj growth 8.6 bp · R EV +0.53 (adj +0.31) on $2.00, P(profit) 0.2143, adj growth 10.6 bp

## NSH @ MTL  ·  10000 joint draws  ·  326 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_NSH_win | p_overtime | goals | shots MTL/NSH | MTL/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.62 | 0.38 | 0.00 | 6.04 | 27.7/27.8 | 24.7/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.45 | 5.94 | 27.7/27.9 | 24.7/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.62 | 0.38 | 0.00 | 9.39 | 29.2/29.3 | 23.9/22.3 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 6.06 | 32.8/22.2 | 19.6/28.2 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.065 | 0.58 | 0.42 | 0.00 | 6.04 | 22.3/32.8 | 29.3/18.6 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.50 | 0.50 | 0.45 | 6.0 | 22.4/33.2 | 30.0/19.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jake Evans: 1+ goals YES | 13 | 0.159 | 0.149 | +0.021 | +0.012 | $2.01 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 25 | 0.290 | 0.276 | +0.027 | +0.013 | $2.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Jake Evans: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08NSHMTL-9|yes; why: higher confidence-adjusted growth (2.47 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.82 vs 0.375); alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: MTL offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08NSHMTL-NSHMBOURQUE22-1|yes; why: higher confidence-adjusted growth (1.98 vs 0.92 bp); alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MTL:OFFENSE_4PLUS (p 0.4712): highest fidelity KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.3535): highest fidelity KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes (same contract)
- KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3168, phi -0.184)
- KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.434, phi -0.266)

portfolios: A EV +0.78 (adj +0.40) on $6.31, P(profit) 0.407, adj growth 3.6 bp · B EV +0.60 (adj +0.31) on $4.78, P(profit) 0.407, adj growth 2.8 bp · C EV +0.83 (adj +0.43) on $6.65, P(profit) 0.407, adj growth 3.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PHI @ OTT  ·  10000 joint draws  ·  420 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_PHI_win | p_overtime | goals | shots OTT/PHI | OTT/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.130 | 0.63 | 0.37 | 0.00 | 5.96 | 32.1/20.6 | 17.8/27.9 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.53 | 0.47 | 0.46 | 5.88 | 32.4/20.7 | 17.5/28.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.57 | 0.43 | 0.00 | 5.99 | 26.7/26.0 | 22.8/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.51 | 0.49 | 0.48 | 5.89 | 26.4/25.9 | 22.7/23.0 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.082 | 0.68 | 0.32 | 0.00 | 9.13 | 33.6/22.1 | 17.4/26.3 | even strength |
| OTT shot control · low event (<=4) · decided (2+) | 0.070 | 0.58 | 0.42 | 0.00 | 3.48 | 30.5/19.4 | 17.8/28.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Eklund: 1+ assists NO | 63 | 0.786 | 0.678 | +0.140 | +0.032 | $11.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Carter Yakemchuk: 1+ assists NO | 65 | 0.759 | 0.682 | +0.093 | +0.016 | $6.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Michael Amadio: 1+ goals YES | 14 | 0.174 | 0.160 | +0.025 | +0.012 | $2.12 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 13 | 0.162 | 0.149 | +0.024 | +0.011 | $1.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (9.82 vs 2.47 bp); relationships: KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.089); KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: OTT offense succeeds (4+ goals)
- **Carter Yakemchuk: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no; why: second expression of the same thesis: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no has the higher standalone adjusted growth (9.82 vs 2.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.089); they share one thesis budget; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.089); KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: OTT offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (2.44 vs 0.58 bp); despite a smaller raw edge (+0.025 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0074 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: OTT offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT08PHIOTT-PHI3|yes; why: higher confidence-adjusted growth (2.30 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.029); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.3734): highest fidelity KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4055): highest fidelity KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3195): highest fidelity KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes (same contract)
- KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.6 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4055, phi -0.215)
- KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.9 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4055, phi -0.218)
- KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3734, phi -0.19)
- KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.458, phi -0.225)

portfolios: A EV +3.63 (adj +0.99) on $20.46, P(profit) 0.7189, adj growth 9.2 bp · B EV +4.20 (adj +1.06) on $22.61, P(profit) 0.7189, adj growth 10.0 bp · C EV +4.70 (adj +1.30) on $22.76, P(profit) 0.7917, adj growth 11.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ TBL  ·  10000 joint draws  ·  404 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_MIN_win | p_overtime | goals | shots TBL/MIN | TBL/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.55 | 0.45 | 0.00 | 6.0 | 28.0/27.5 | 24.2/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.47 | 0.53 | 0.47 | 5.89 | 28.0/27.6 | 24.1/24.9 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.103 | 0.58 | 0.42 | 0.00 | 6.03 | 33.4/22.1 | 19.0/29.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.55 | 0.45 | 0.49 | 5.88 | 33.6/22.2 | 19.1/30.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.54 | 0.46 | 0.00 | 9.28 | 29.4/29.0 | 23.1/23.2 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.072 | 0.62 | 0.38 | 0.00 | 9.19 | 34.8/23.6 | 18.7/27.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| John Carlson: 1+ assists NO | 58 | 0.725 | 0.624 | +0.128 | +0.027 | $11.45 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Ilya Mikheyev: 1+ goals YES | 16 | 0.204 | 0.189 | +0.035 | +0.020 | $3.80 | FUNDED_RESEARCH | $1 | TBL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ assists NO | 40 | 0.489 | 0.442 | +0.073 | +0.025 | $6.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (6.71 vs 5.82 bp); relationships: KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.05); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.097); failure: TBL offense succeeds (4+ goals)
- **Ilya Mikheyev: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08MINTB-8|yes; why: higher confidence-adjusted growth (6.14 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.878 vs 0.332); alternative not eligible: confidence-adjusted EV +0.0008 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: INTENTIONAL_DIVERSIFIER (phi -0.05); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.046); failure: TBL offense suppressed (<= 2 goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no; why: second expression of the same thesis: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no has the higher standalone adjusted growth (6.71 vs 5.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.097); they share one thesis budget; relationships: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.097); KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.046); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TBL:SUPPRESSED (p 0.3719): highest fidelity KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no (same contract)
- thesis TBL:OFFENSE_4PLUS (p 0.4133): highest fidelity KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes (same contract)
- KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.5 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4133, phi -0.226)
- KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3719, phi -0.209)
- KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4133, phi -0.3)

portfolios: A EV +4.02 (adj +1.36) on $20.46, P(profit) 0.5148, adj growth 12.5 bp · B EV +4.31 (adj +1.35) on $21.43, P(profit) 0.5148, adj growth 12.4 bp · C EV +4.75 (adj +1.39) on $22.40, P(profit) 0.79, adj growth 12.4 bp · R EV +0.21 (adj +0.12) on $1.00, P(profit) 0.2042, adj growth 4.3 bp

## VAN @ CAR  ·  10000 joint draws  ·  428 bet sides mapped, 25 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_VAN_win | p_overtime | goals | shots CAR/VAN | CAR/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.190 | 0.70 | 0.30 | 0.00 | 6.04 | 33.7/20.5 | 17.9/29.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.143 | 0.56 | 0.44 | 0.49 | 5.94 | 34.1/20.9 | 17.7/30.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.135 | 0.70 | 0.30 | 0.00 | 9.36 | 35.7/22.0 | 17.4/27.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.082 | 0.62 | 0.38 | 0.00 | 6.01 | 27.8/26.5 | 23.5/23.7 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.070 | 0.67 | 0.33 | 0.00 | 3.48 | 32.4/19.3 | 17.9/29.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.52 | 0.48 | 0.45 | 5.99 | 27.6/26.7 | 23.4/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 13 | 0.187 | 0.170 | +0.049 | +0.032 | $5.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 16 | 0.217 | 0.196 | +0.047 | +0.027 | $4.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 60 | 0.731 | 0.642 | +0.114 | +0.026 | $6.77 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 65 | 0.705 | 0.690 | +0.039 | +0.024 | $10.15 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: higher confidence-adjusted growth (18.71 vs 18.13 bp); despite a smaller raw edge (+0.049 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.938 vs 0.509); relationships: KXNHLGOAL-26OCT08VANCAR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.117); KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08VANCAR-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08VANCAR-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (18.71 vs 11.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT08VANCAR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.111); KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: VAN offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08VANCAR-CAR2|no; why: Broad expression KXNHLSPREAD-26OCT08VANCAR-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT08VANCAR-CAR5|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.95 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT08VANCAR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.117); KXNHLGOAL-26OCT08VANCAR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.111); KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: REINFORCING (phi 0.15); failure: CAR wins by 2+
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes has the higher standalone adjusted growth (18.13 vs 5.72 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.101); relationships: KXNHLGOAL-26OCT08VANCAR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT08VANCAR-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: REINFORCING (phi 0.15); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.19, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:OFFENSE_4PLUS (p 0.3395): highest fidelity KXNHLTEAMTOTAL-26OCT08VANCAR-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08VANCAR-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2009): highest fidelity KXNHLSPREAD-26OCT08VANCAR-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08VANCAR-VAN2|yes (same contract)
- thesis CAR:SUPPRESSED (p 0.288): highest fidelity KXNHLSPREAD-26OCT08VANCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08VANCAR-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08VANCAR-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4529, phi -0.224)
- KXNHLGOAL-26OCT08VANCAR-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4529, phi -0.212)
- KXNHLSPREAD-26OCT08VANCAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.6 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.396, phi -0.75)
- KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.5018, phi -0.201)
- override: Broad expression KXNHLSPREAD-26OCT08VANCAR-CAR3|no selected over broad KXNHLTEAMTOTAL-26OCT08VANCAR-CAR5|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.95 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.87 (adj +1.07) on $20.46, P(profit) 0.5265, adj growth 9.1 bp · B EV +4.85 (adj +2.52) on $26.33, P(profit) 0.3485, adj growth 23.1 bp · C EV +6.58 (adj +2.94) on $19.42, P(profit) 0.2672, adj growth 25.8 bp · R EV +0.55 (adj +0.19) on $5.00, P(profit) 0.5455, adj growth 7.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08VANCAR-VAN|yes == KXNHLGAME-26OCT08VANCAR-CAR|no

## CHI @ NYI  ·  10000 joint draws  ·  396 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CHI_win | p_overtime | goals | shots NYI/CHI | NYI/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NYI shot control · normal event (5-7) · decided (2+) | 0.134 | 0.71 | 0.29 | 0.00 | 6.03 | 33.2/21.2 | 18.6/28.5 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.58 | 0.42 | 0.47 | 5.92 | 33.4/21.3 | 18.1/29.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.67 | 0.33 | 0.00 | 6.02 | 27.6/26.9 | 24.2/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.51 | 0.49 | 0.47 | 5.91 | 27.5/26.8 | 23.5/24.3 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.089 | 0.70 | 0.30 | 0.00 | 9.23 | 34.6/22.4 | 18.1/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.67 | 0.33 | 0.00 | 9.31 | 29.3/28.3 | 23.2/21.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 12 | 0.164 | 0.150 | +0.036 | +0.023 | $3.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Calum Ritchie: 1+ assists YES | 27 | 0.356 | 0.308 | +0.072 | +0.024 | $5.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
| Patrick Kane: 1+ assists NO | 61 | 0.720 | 0.639 | +0.093 | +0.012 | $5.83 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Bo Horvat: 1+ goals NO | 64 | 0.679 | 0.667 | +0.023 | +0.011 | $5.17 | FUNDED_RESEARCH | $2 | NYI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08CHINYI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (10.12 vs 0.68 bp); alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: CHI offense suppressed (<= 2 goals)
- **Calum Ritchie: 1+ assists YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08CHINYI-9|yes; why: higher confidence-adjusted growth (6.21 vs 0.14 bp); wins across more scripts (relative breadth 0.888 vs 0.375); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: INTENTIONAL_DIVERSIFIER (phi -0.062); failure: NYI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08CHINYI-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (1.35 vs 0.07 bp); alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI offense succeeds (4+ goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08CHINYI-NYIKPALMIERI21-1|no; why: higher confidence-adjusted growth (1.06 vs 0.38 bp); despite a smaller raw edge (+0.023 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.062); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: NYI offense succeeds (4+ goals)

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3014): highest fidelity KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.464): highest fidelity KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4848): highest fidelity KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4848, phi -0.211)
- KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3184, phi -0.247)
- KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.5 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3014, phi -0.236)
- KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.464, phi -0.258)

portfolios: A EV +3.54 (adj +1.29) on $20.46, P(profit) 0.4648, adj growth 11.8 bp · B EV +3.40 (adj +1.30) on $19.80, P(profit) 0.4341, adj growth 11.9 bp · C EV +4.72 (adj +1.81) on $27.55, P(profit) 0.4341, adj growth 16.0 bp · R EV +0.07 (adj +0.03) on $2.00, P(profit) 0.6788, adj growth 1.1 bp

## SJS @ STL  ·  10000 joint draws  ·  402 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_SJS_win | p_overtime | goals | shots STL/SJS | STL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.62 | 0.38 | 0.00 | 6.03 | 26.6/26.5 | 23.4/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.52 | 0.48 | 0.44 | 5.97 | 26.6/26.4 | 23.1/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.58 | 0.41 | 0.00 | 9.32 | 28.0/27.8 | 22.2/21.3 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.086 | 0.65 | 0.35 | 0.00 | 6.07 | 31.5/21.1 | 18.3/26.9 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.57 | 0.43 | 0.48 | 5.96 | 31.8/21.3 | 18.2/28.4 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.063 | 0.69 | 0.31 | 0.00 | 9.26 | 33.2/22.3 | 17.9/25.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 7.5 goals scored YES | 23 | 0.284 | 0.255 | +0.042 | +0.012 | $1.77 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mason Marchment: 1+ assists NO | 70 | 0.773 | 0.727 | +0.058 | +0.012 | $8.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Full Game: Over 6.5 goals scored YES | 43 | 0.495 | 0.460 | +0.048 | +0.013 | $2.53 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Full Game: Over 7.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-9|yes; why: Broad expression KXNHLTOTAL-26OCT08SJSTL-8|yes selected over broad KXNHLTOTAL-26OCT08SJSTL-9|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.73 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: INTENTIONAL_DIVERSIFIER (phi -0.155); KXNHLTOTAL-26OCT08SJSTL-7|yes: DUPLICATIVE (phi 0.636); failure: SJS offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT08SJSTL-SJLCAGNONI42-1|no; why: higher confidence-adjusted growth (1.51 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLTOTAL-26OCT08SJSTL-8|yes: INTENTIONAL_DIVERSIFIER (phi -0.155); KXNHLTOTAL-26OCT08SJSTL-7|yes: INTENTIONAL_DIVERSIFIER (phi -0.171); failure: SJS offense succeeds (4+ goals)
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-9|yes; why: KXNHLTOTAL-26OCT08SJSTL-9|yes has the higher standalone adjusted growth (1.97 vs 1.44 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.515); relationships: KXNHLTOTAL-26OCT08SJSTL-8|yes: DUPLICATIVE (phi 0.636); KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: INTENTIONAL_DIVERSIFIER (phi -0.171); failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis GAME:HIGH_EVENT (p 0.2839): highest fidelity KXNHLTOTAL-26OCT08SJSTL-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT08SJSTL-7|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.422): highest fidelity KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no (same contract)
- KXNHLTOTAL-26OCT08SJSTL-8|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis SJS:SUPPRESSED (p 0.422, phi -0.4)
- KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3571, phi -0.247)
- KXNHLTOTAL-26OCT08SJSTL-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.2128, phi -0.515)
- override: Broad expression KXNHLTOTAL-26OCT08SJSTL-8|yes selected over broad KXNHLTOTAL-26OCT08SJSTL-9|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.73 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.33 (adj +0.60) on $20.46, P(profit) 0.4404, adj growth 4.7 bp · B EV +1.30 (adj +0.31) on $13.19, P(profit) 0.3467, adj growth 2.8 bp · C EV +1.64 (adj +0.40) on $14.97, P(profit) 0.8458, adj growth 3.6 bp · R EV +0.28 (adj +0.08) on $2.00, P(profit) 0.4948, adj growth 2.5 bp

## COL @ CGY  ·  10000 joint draws  ·  414 bet sides mapped, 18 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_COL_win | p_overtime | goals | shots CGY/COL | CGY/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.129 | 0.37 | 0.63 | 0.00 | 5.98 | 22.7/35.3 | 30.8/19.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.44 | 0.56 | 0.49 | 5.96 | 23.0/35.5 | 31.9/19.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.41 | 0.59 | 0.00 | 5.98 | 28.8/29.6 | 25.6/25.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.48 | 0.52 | 0.47 | 5.94 | 28.7/29.7 | 26.3/25.4 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.089 | 0.38 | 0.62 | 0.00 | 9.2 | 24.1/37.5 | 29.6/19.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.39 | 0.61 | 0.00 | 9.28 | 30.2/31.2 | 24.5/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Zachary L'Heureux: 1+ goals YES | 8 | 0.139 | 0.121 | +0.054 | +0.036 | $4.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 56 | 0.643 | 0.620 | +0.066 | +0.043 | $9.31 | FUNDED_RESEARCH | $3 | COL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Martin Necas: 1+ goals NO | 63 | 0.704 | 0.680 | +0.057 | +0.034 | $9.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Calgary over 2.5 goals scored YES | 48 | 0.567 | 0.521 | +0.070 | +0.024 | $5.76 | FUNDED_RESEARCH | $2 | CGY:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Zachary L'Heureux: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT08COLCGY-COLSMALINSKI70-1|yes; why: higher confidence-adjusted growth (34.17 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: COL offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no; why: higher confidence-adjusted growth (16.54 vs 11.04 bp); relationships: KXNHLGOAL-26OCT08COLCGY-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3|yes: MOSTLY_INDEPENDENT (phi 0.042); failure: COL offense succeeds (4+ goals)
- **Martin Necas: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no; why: Player prop expression KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no selected over player prop KXNHLAST-26OCT08COLCGY-COLNMACKINNON29-1|no because adjusted EV is 0.8 pts higher while thesis capture is 0.85 vs 0.76 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT08COLCGY-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: COL offense succeeds (4+ goals)
- **Calgary over 2.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT08COLCGY-CGY3|yes; why: KXNHLSPREAD-26OCT08COLCGY-CGY3|yes has the higher standalone adjusted growth (9.34 vs 4.88 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.341); relationships: KXNHLGOAL-26OCT08COLCGY-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.042); KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis COL:SUPPRESSED (p 0.3455): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no — Player prop expression KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no selected over player prop KXNHLAST-26OCT08COLCGY-COLNMACKINNON29-1|no because adjusted EV is 0.8 pts higher while thesis capture is 0.85 vs 0.76 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)
- thesis CGY:WINS (p 0.4308): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS_BY_2PLUS (p 0.225): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08COLCGY-COLZLHEUREUX68-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3455, phi -0.169)
- KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4359, phi -0.276)
- KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4359, phi -0.241)
- KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:SUPPRESSED (p 0.4436, phi -0.978)
- override: Player prop expression KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no selected over player prop KXNHLAST-26OCT08COLCGY-COLNMACKINNON29-1|no because adjusted EV is 0.8 pts higher while thesis capture is 0.85 vs 0.76 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +7.22 (adj +0.94) on $20.46, P(profit) 0.7199, adj growth 8.4 bp · B EV +5.29 (adj +3.15) on $28.44, P(profit) 0.5311, adj growth 29.5 bp · C EV +4.27 (adj +2.01) on $24.61, P(profit) 0.6665, adj growth 18.1 bp · R EV +0.62 (adj +0.32) on $5.00, P(profit) 0.6435, adj growth 11.9 bp

## TOR @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TOR_win | p_overtime | goals | shots VGK/TOR | VGK/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.148 | 0.77 | 0.23 | 0.00 | 5.99 | 34.3/21.6 | 19.3/29.2 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.58 | 0.42 | 0.48 | 5.92 | 34.3/21.9 | 18.7/30.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.70 | 0.29 | 0.00 | 6.03 | 28.3/27.5 | 24.7/23.7 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.106 | 0.80 | 0.20 | 0.00 | 9.34 | 35.8/23.2 | 19.2/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.56 | 0.44 | 0.48 | 6.0 | 28.4/27.8 | 24.5/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.69 | 0.31 | 0.00 | 9.21 | 29.7/29.1 | 24.4/22.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.15, VGK shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
