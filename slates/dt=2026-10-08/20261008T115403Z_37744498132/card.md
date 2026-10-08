# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-08T11:54:03Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.20 | +6.74 | +25.87 | 0.700 | -36.09 | -51.79 | 54.99 |
| B thesis-diversified (joint) ← optimiser card | 126.86 | +22.62 | +6.36 | +20.83 | 0.698 | -27.43 | -40.87 | 55.49 |
| C best expression per thesis | 106.09 | +22.41 | +6.45 | +20.15 | 0.683 | -28.42 | -40.03 | 55.98 |
| R FUNDED research stakes | 17.00 | +3.35 | +1.14 | +1.37 | 0.561 | -8.86 | -12.14 | 0.00 |

## UTA @ BOS  ·  10000 joint draws  ·  170 bet sides mapped, 2 +EV candidates, 2 on card


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
| Full Game: Over 6.5 goals scored YES | 43 | 0.497 | 0.461 | +0.050 | +0.014 | $4.96 | FUNDED_RESEARCH | $2 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Boston over 3.5 goals scored YES | 36 | 0.419 | 0.387 | +0.043 | +0.011 | $2.28 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes; why: higher confidence-adjusted growth (1.68 vs 1.09 bp); relationships: KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes: REINFORCING (phi 0.455); failure: low-event game (<= 4 goals)
- **Boston over 3.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08UTABOS-7|yes; why: second expression of the same thesis: KXNHLTOTAL-26OCT08UTABOS-7|yes has the higher standalone adjusted growth (1.68 vs 1.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.455); they share one thesis budget; relationships: KXNHLTOTAL-26OCT08UTABOS-7|yes: REINFORCING (phi 0.455); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis GAME:HIGH_EVENT (p 0.2872): highest fidelity KXNHLTOTAL-26OCT08UTABOS-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT08UTABOS-7|yes (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.4093): highest fidelity KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT08UTABOS-7|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTOTAL-26OCT08UTABOS-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.2121, phi -0.516)
- KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.3759, phi -0.659)

portfolios: A EV +1.77 (adj +0.47) on $15.72, P(profit) 0.5953, adj growth 3.4 bp · B EV +0.81 (adj +0.22) on $7.24, P(profit) 0.4969, adj growth 1.9 bp · C EV +0.69 (adj +0.19) on $6.17, P(profit) 0.4969, adj growth 1.7 bp · R EV +0.34 (adj +0.09) on $3.00, P(profit) 0.4969, adj growth 2.9 bp

## DAL @ BUF  ·  10000 joint draws  ·  328 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_DAL_win | p_overtime | goals | shots BUF/DAL | BUF/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.56 | 0.44 | 0.00 | 5.96 | 26.3/26.3 | 23.1/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.49 | 0.51 | 0.49 | 5.9 | 26.7/26.4 | 23.2/23.5 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.090 | 0.64 | 0.36 | 0.00 | 5.98 | 31.5/20.8 | 18.1/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.56 | 0.44 | 0.00 | 9.15 | 27.9/27.7 | 22.1/21.9 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.54 | 0.46 | 0.44 | 5.9 | 31.6/21.1 | 17.8/28.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.53 | 0.47 | 0.00 | 3.52 | 25.1/24.8 | 23.1/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jiri Kulich: 1+ goals YES | 16 | 0.209 | 0.184 | +0.039 | +0.015 | $3.79 | FUNDED_RESEARCH | $1 | BUF:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Peyton Krebs: 1+ goals YES | 12 | 0.160 | 0.138 | +0.033 | +0.010 | $2.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Owen Power: 1+ assists YES | 31 | 0.376 | 0.335 | +0.051 | +0.010 | $2.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes; why: higher confidence-adjusted growth (3.26 vs 2.11 bp); relationships: KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT08DALBUF-BUFOPOWER25-1|yes: MOSTLY_INDEPENDENT (phi 0.093); failure: BUF offense suppressed (<= 2 goals)
- **Peyton Krebs: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes has the higher standalone adjusted growth (3.26 vs 2.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT08DALBUF-BUFOPOWER25-1|yes: MOSTLY_INDEPENDENT (phi 0.09); failure: BUF offense suppressed (<= 2 goals)
- **Owen Power: 1+ assists YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes has the higher standalone adjusted growth (3.26 vs 1.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.093); they share one thesis budget; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.093); KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.09); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.09.
- thesis BUF:OFFENSE_4PLUS (p 0.4059): highest fidelity KXNHLAST-26OCT08DALBUF-BUFOPOWER25-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3786, phi -0.214)
- KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3786, phi -0.202)
- KXNHLAST-26OCT08DALBUF-BUFOPOWER25-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3786, phi -0.268)

portfolios: A EV +3.44 (adj +1.01) on $16.96, P(profit) 0.5565, adj growth 7.8 bp · B EV +1.94 (adj +0.61) on $8.96, P(profit) 0.336, adj growth 5.3 bp · C EV +0.91 (adj +0.34) on $3.94, P(profit) 0.2086, adj growth 2.9 bp · R EV +0.23 (adj +0.09) on $1.00, P(profit) 0.2086, adj growth 3.0 bp

## NSH @ MTL  ·  10000 joint draws  ·  326 bet sides mapped, 1 +EV candidates, 1 on card


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
| Ryan O'Reilly: 1+ goals YES | 25 | 0.290 | 0.276 | +0.027 | +0.013 | $4.36 | FUNDED_RESEARCH | $2 | NSH:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT08NSHMTL-NSH5|yes; why: higher confidence-adjusted growth (1.98 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.887 vs 0.534); alternative not eligible: confidence-adjusted EV +0.0008 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NSH:OFFENSE_4PLUS (p 0.3535): highest fidelity KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes (same contract)
- KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.434, phi -0.266)

portfolios: A EV +0.40 (adj +0.20) on $3.89, P(profit) 0.2902, adj growth 1.7 bp · B EV +0.45 (adj +0.22) on $4.36, P(profit) 0.2902, adj growth 1.9 bp · C EV +0.45 (adj +0.22) on $4.36, P(profit) 0.2902, adj growth 1.9 bp · R EV +0.21 (adj +0.10) on $2.00, P(profit) 0.2902, adj growth 3.1 bp

## PHI @ OTT  ·  10000 joint draws  ·  420 bet sides mapped, 2 +EV candidates, 2 on card


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
| William Eklund: 1+ assists NO | 65 | 0.786 | 0.681 | +0.121 | +0.016 | $15.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Jordan Spence: 1+ assists YES | 27 | 0.343 | 0.294 | +0.059 | +0.010 | $3.53 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (2.40 vs 0.36 bp); alternative not eligible: confidence-adjusted EV +0.0061 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.044); failure: OTT offense succeeds (4+ goals)
- **Jordan Spence: 1+ assists YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT08PHIOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (1.13 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.044); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.3734): highest fidelity KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4055): highest fidelity KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes (same contract)
- KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.1 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4055, phi -0.215)
- KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3734, phi -0.271)

portfolios: A EV +3.30 (adj +0.50) on $16.93, P(profit) 0.3431, adj growth 3.9 bp · B EV +3.47 (adj +0.48) on $18.64, P(profit) 0.7865, adj growth 4.2 bp · C EV +3.47 (adj +0.48) on $18.64, P(profit) 0.7865, adj growth 4.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| John Carlson: 1+ assists NO | 59 | 0.725 | 0.627 | +0.118 | +0.021 | $14.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ assists NO | 41 | 0.489 | 0.442 | +0.063 | +0.015 | $5.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
| Ilya Mikheyev: 1+ goals YES | 16 | 0.204 | 0.181 | +0.035 | +0.011 | $3.41 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (3.86 vs 2.10 bp); relationships: KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.097); KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.05); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no; why: second expression of the same thesis: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no has the higher standalone adjusted growth (3.86 vs 2.10 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.097); they share one thesis budget; relationships: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.097); KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.046); failure: TBL offense succeeds (4+ goals)
- **Ilya Mikheyev: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08MINTB-8|yes; why: higher confidence-adjusted growth (1.95 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.878 vs 0.332); alternative not eligible: confidence-adjusted EV +0.0008 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: INTENTIONAL_DIVERSIFIER (phi -0.05); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.046); failure: TBL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TBL:SUPPRESSED (p 0.3719): highest fidelity KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no (same contract)
- thesis TBL:OFFENSE_4PLUS (p 0.4133): highest fidelity KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes (same contract)
- KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.0 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4133, phi -0.226)
- KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4133, phi -0.3)
- KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3719, phi -0.209)

portfolios: A EV +3.76 (adj +0.88) on $21.16, P(profit) 0.5148, adj growth 7.6 bp · B EV +4.39 (adj +0.93) on $23.86, P(profit) 0.7497, adj growth 8.1 bp · C EV +3.67 (adj +0.74) on $18.73, P(profit) 0.79, adj growth 6.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ CAR  ·  10000 joint draws  ·  428 bet sides mapped, 15 +EV candidates, 4 on card


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
| Vancouver wins by over 1.5 goals YES | 12 | 0.201 | 0.158 | +0.073 | +0.031 | $5.42 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 3.5 goals scored YES | 23 | 0.349 | 0.268 | +0.106 | +0.026 | $1.68 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 60 | 0.731 | 0.642 | +0.114 | +0.026 | $9.98 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sebastian Aho: 2+ assists NO | 86 | 0.927 | 0.881 | +0.059 | +0.013 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CAR:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes has the higher standalone adjusted growth (18.13 vs 17.94 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.731); relationships: KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4|yes: REINFORCING (phi 0.514); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: DUPLICATIVE (phi 0.304); KXNHLAST-26OCT08VANCAR-CARSAHO20-2|no: MOSTLY_INDEPENDENT (phi 0.089); failure: CAR wins (incl. OT/SO)
- **Vancouver over 3.5 goals scored YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4|yes selected over broad KXNHLTEAMTOTAL-26OCT08VANCAR-VAN5|yes because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.51 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT08VANCAR-VAN2|yes: REINFORCING (phi 0.514); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: REINFORCING (phi 0.371); KXNHLAST-26OCT08VANCAR-CARSAHO20-2|no: MOSTLY_INDEPENDENT (phi -0.001); failure: VAN offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08VANCAR-CAR2|no; why: higher confidence-adjusted growth (6.11 vs 6.01 bp); despite a smaller raw edge (+0.114 vs +0.117/contract); wins across more scripts (relative breadth 1.069 vs 0.936); relationships: KXNHLSPREAD-26OCT08VANCAR-VAN2|yes: DUPLICATIVE (phi 0.304); KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4|yes: REINFORCING (phi 0.371); KXNHLAST-26OCT08VANCAR-CARSAHO20-2|no: MOSTLY_INDEPENDENT (phi 0.122); failure: CAR wins by 2+
- **Sebastian Aho: 2+ assists NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes has the higher standalone adjusted growth (18.13 vs 3.15 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.071); relationships: KXNHLSPREAD-26OCT08VANCAR-VAN2|yes: MOSTLY_INDEPENDENT (phi 0.089); KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.122); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.19, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:WINS_BY_2PLUS (p 0.2009): highest fidelity KXNHLSPREAD-26OCT08VANCAR-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08VANCAR-VAN2|yes (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3395): highest fidelity KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08VANCAR-VAN2|yes — Broad expression KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4|yes selected over broad KXNHLTEAMTOTAL-26OCT08VANCAR-VAN5|yes because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.51 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis VAN:WINS (p 0.3879): highest fidelity KXNHLSPREAD-26OCT08VANCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08VANCAR-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT08VANCAR-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.6121, phi -0.63)
- KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.4 pts; opposing: failure thesis VAN:SUPPRESSED (p 0.4529, phi -0.666)
- KXNHLSPREAD-26OCT08VANCAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.6 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.396, phi -0.75)
- KXNHLAST-26OCT08VANCAR-CARSAHO20-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.5018, phi -0.182)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT08VANCAR-CAR4|no less than the minimum stake; KXNHLAST-26OCT08VANCAR-CARSAHO20-2|no kept
- override: Broad expression KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4|yes selected over broad KXNHLTEAMTOTAL-26OCT08VANCAR-VAN5|yes because adjusted EV is 0.0 pts higher while thesis capture is 1.00 vs 0.51 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.94 (adj +1.03) on $21.16, P(profit) 0.5265, adj growth 8.7 bp · B EV +7.06 (adj +2.19) on $37.08, P(profit) 0.6969, adj growth 19.1 bp · C EV +5.77 (adj +1.91) on $17.88, P(profit) 0.7306, adj growth 16.4 bp · R EV +2.15 (adj +0.71) on $6.00, P(profit) 0.3658, adj growth 22.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08VANCAR-CAR|no == KXNHLGAME-26OCT08VANCAR-VAN|yes

## CHI @ NYI  ·  10000 joint draws  ·  396 bet sides mapped, 3 +EV candidates, 3 on card


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
| Calum Ritchie: 1+ assists YES | 27 | 0.356 | 0.308 | +0.072 | +0.024 | $8.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
| Ryan Greene: 1+ goals YES | 12 | 0.164 | 0.145 | +0.036 | +0.018 | $4.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Bo Horvat: 1+ goals NO | 64 | 0.679 | 0.667 | +0.023 | +0.011 | $8.50 | FUNDED_RESEARCH | $3 | NYI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Calum Ritchie: 1+ assists YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08CHINYI-10|yes; why: higher confidence-adjusted growth (6.21 vs 0.07 bp); wins across more scripts (relative breadth 0.888 vs 0.313); alternative not eligible: confidence-adjusted EV +0.0015 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: INTENTIONAL_DIVERSIFIER (phi -0.062); failure: NYI offense suppressed (<= 2 goals)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08CHINYI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (6.21 vs 0.48 bp); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: CHI offense suppressed (<= 2 goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08CHINYI-NYIKPALMIERI21-1|no; why: higher confidence-adjusted growth (1.06 vs 0.00 bp); despite a smaller raw edge (+0.023 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.062); KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: NYI offense succeeds (4+ goals)

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.464): highest fidelity KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3014): highest fidelity KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes (same contract)
- thesis NYI:SUPPRESSED (p 0.3184): highest fidelity KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no (same contract)
- KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3184, phi -0.247)
- KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4848, phi -0.211)
- KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.464, phi -0.258)

portfolios: A EV +3.64 (adj +1.45) on $19.84, P(profit) 0.4648, adj growth 12.6 bp · B EV +3.65 (adj +1.47) on $21.17, P(profit) 0.4648, adj growth 12.7 bp · C EV +3.65 (adj +1.47) on $21.17, P(profit) 0.4648, adj growth 12.7 bp · R EV +0.10 (adj +0.05) on $3.00, P(profit) 0.6788, adj growth 1.5 bp

## SJS @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


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
| Full Game: Over 8.5 goals scored YES | 16 | 0.206 | 0.181 | +0.037 | +0.011 | $2.24 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | DIRECT (0.73) | EVIDENCE_MIXED | D |
| Full Game: Over 6.5 goals scored YES | 43 | 0.495 | 0.460 | +0.048 | +0.013 | $3.32 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Full Game: Over 8.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-7|yes; why: higher confidence-adjusted growth (1.97 vs 1.44 bp); despite a smaller raw edge (+0.037 vs +0.048/contract); relationships: KXNHLTOTAL-26OCT08SJSTL-7|yes: DUPLICATIVE (phi 0.515); failure: SJS offense suppressed (<= 2 goals)
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-9|yes; why: second expression of the same thesis: KXNHLTOTAL-26OCT08SJSTL-9|yes has the higher standalone adjusted growth (1.97 vs 1.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.515); they share one thesis budget; relationships: KXNHLTOTAL-26OCT08SJSTL-9|yes: DUPLICATIVE (phi 0.515); failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis GAME:HIGH_EVENT (p 0.2839): highest fidelity KXNHLTOTAL-26OCT08SJSTL-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT08SJSTL-7|yes (same contract)
- KXNHLTOTAL-26OCT08SJSTL-9|yes: FUNDED_RESEARCH; family MIXED; loses 27% of the draws where the thesis happens; opposing: failure thesis SJS:SUPPRESSED (p 0.422, phi -0.37)
- KXNHLTOTAL-26OCT08SJSTL-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.2128, phi -0.515)

portfolios: A EV +1.93 (adj +0.56) on $13.18, P(profit) 0.4948, adj growth 3.9 bp · B EV +0.84 (adj +0.24) on $5.55, P(profit) 0.4948, adj growth 2.1 bp · C EV +0.66 (adj +0.20) on $3.05, P(profit) 0.2064, adj growth 1.8 bp · R EV +0.32 (adj +0.10) on $2.00, P(profit) 0.4948, adj growth 3.0 bp

## COL @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_COL_win | p_overtime | goals | shots CGY/COL | CGY/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.130 | 0.34 | 0.66 | 0.00 | 5.98 | 22.9/35.7 | 31.1/20.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.45 | 0.55 | 0.46 | 5.93 | 23.0/35.7 | 32.3/19.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.42 | 0.58 | 0.00 | 6.03 | 28.6/29.4 | 25.4/25.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.49 | 0.51 | 0.44 | 5.96 | 28.6/29.7 | 26.3/25.3 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.086 | 0.34 | 0.66 | 0.00 | 9.27 | 24.1/37.1 | 29.4/19.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.42 | 0.58 | 0.00 | 9.36 | 30.5/31.3 | 24.4/24.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CGY:WINS_BY_2PLUS (p 0.2234): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08COLCGY-COL2|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3376): highest fidelity KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08COLCGY-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.3423): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08COLCGY-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order

portfolios: A EV +3.02 (adj +0.64) on $21.16, P(profit) 0.6948, adj growth 5.3 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +3.13 (adj +0.90) on $12.15, P(profit) 0.6585, adj growth 7.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TOR_win | p_overtime | goals | shots VGK/TOR | VGK/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.151 | 0.74 | 0.26 | 0.00 | 6.0 | 34.0/21.6 | 19.2/29.1 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.56 | 0.44 | 0.48 | 5.92 | 34.3/21.9 | 18.7/30.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.69 | 0.31 | 0.00 | 5.99 | 28.3/27.4 | 24.8/23.9 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.102 | 0.77 | 0.23 | 0.00 | 9.25 | 35.8/23.2 | 19.0/26.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.53 | 0.47 | 0.46 | 5.94 | 28.5/27.7 | 24.5/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.71 | 0.29 | 0.00 | 9.38 | 30.0/29.1 | 24.4/22.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.15, VGK shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
