# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-08T14:41:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +29.33 | +7.62 | +28.34 | 0.794 | -15.57 | -27.61 | 69.84 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +22.25 | +8.99 | +21.19 | 0.774 | -14.47 | -24.23 | 85.47 |
| C best expression per thesis | 149.99 | +24.77 | +10.30 | +22.46 | 0.721 | -24.60 | -37.27 | 95.04 |
| R FUNDED research stakes | 21.00 | +2.47 | +1.09 | +1.91 | 0.595 | -6.78 | -9.02 | 0.00 |

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
| Boston over 4.5 goals scored YES | 18 | 0.234 | 0.204 | +0.043 | +0.014 | $1.29 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
| Full Game: Over 6.5 goals scored YES | 43 | 0.497 | 0.461 | +0.050 | +0.014 | $1.45 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Boston over 4.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08UTABOS-7|yes; why: higher confidence-adjusted growth (2.77 vs 1.68 bp); despite a smaller raw edge (+0.043 vs +0.050/contract); relationships: KXNHLTOTAL-26OCT08UTABOS-7|yes: REINFORCING (phi 0.452); failure: UTA wins (incl. OT/SO)
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26OCT08UTABOS-BOS5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT08UTABOS-BOS5|yes has the higher standalone adjusted growth (2.77 vs 1.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.452); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT08UTABOS-BOS5|yes: REINFORCING (phi 0.452); failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis BOS:OFFENSE_4PLUS (p 0.4093): highest fidelity KXNHLTOTAL-26OCT08UTABOS-7|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT08UTABOS-BOS5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2872): highest fidelity KXNHLTOTAL-26OCT08UTABOS-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT08UTABOS-BOS5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT08UTABOS-BOS5|yes: FUNDED_RESEARCH; family MIXED; loses 43% of the draws where the thesis happens; opposing: failure thesis UTA:WINS (p 0.4997, phi -0.452)
- KXNHLTOTAL-26OCT08UTABOS-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.2121, phi -0.516)

portfolios: A EV +1.64 (adj +0.50) on $10.36, P(profit) 0.5189, adj growth 4.0 bp · B EV +0.46 (adj +0.14) on $2.74, P(profit) 0.5189, adj growth 1.3 bp · C EV +0.53 (adj +0.17) on $2.33, P(profit) 0.2337, adj growth 1.6 bp · R EV +0.34 (adj +0.10) on $2.00, P(profit) 0.5189, adj growth 3.5 bp

## DAL @ BUF  ·  10000 joint draws  ·  328 bet sides mapped, 4 +EV candidates, 4 on card


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
| Jiri Kulich: 1+ goals YES | 16 | 0.214 | 0.196 | +0.045 | +0.026 | $2.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Justin Danforth: 1+ goals YES | 8 | 0.117 | 0.103 | +0.032 | +0.018 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Owen Power: 1+ assists YES | 31 | 0.396 | 0.348 | +0.071 | +0.023 | $2.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
| Mikko Rantanen: 1+ goals NO | 71 | 0.751 | 0.738 | +0.026 | +0.014 | $5.05 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08DALBUF-BUFOPOWER25-1|yes; why: higher confidence-adjusted growth (10.61 vs 5.20 bp); despite a smaller raw edge (+0.045 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT08DALBUF-BUFOPOWER25-1|yes: MOSTLY_INDEPENDENT (phi 0.108); KXNHLGOAL-26OCT08DALBUF-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: BUF offense suppressed (<= 2 goals)
- **Justin Danforth: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes has the higher standalone adjusted growth (10.61 vs 8.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT08DALBUF-BUFOPOWER25-1|yes: MOSTLY_INDEPENDENT (phi 0.05); KXNHLGOAL-26OCT08DALBUF-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: BUF offense suppressed (<= 2 goals)
- **Owen Power: 1+ assists YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes has the higher standalone adjusted growth (10.61 vs 5.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.108); they share one thesis budget; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.108); KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi 0.05); KXNHLGOAL-26OCT08DALBUF-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: BUF offense suppressed (<= 2 goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT08DALBUF-DAL3|no; why: higher confidence-adjusted growth (2.08 vs 0.70 bp); despite a smaller raw edge (+0.026 vs +0.029/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT08DALBUF-BUFOPOWER25-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.09.
- thesis BUF:OFFENSE_4PLUS (p 0.4032): highest fidelity KXNHLAST-26OCT08DALBUF-BUFOPOWER25-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.4337): highest fidelity KXNHLGOAL-26OCT08DALBUF-DALMRANTANEN96-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08DALBUF-DALMRANTANEN96-1|no (same contract)
- KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.38, phi -0.22)
- KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.38, phi -0.134)
- KXNHLAST-26OCT08DALBUF-BUFOPOWER25-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.38, phi -0.286)
- KXNHLGOAL-26OCT08DALBUF-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3456, phi -0.241)

portfolios: A EV +2.99 (adj +1.43) on $15.52, P(profit) 0.4923, adj growth 13.2 bp · B EV +2.17 (adj +1.09) on $12.28, P(profit) 0.4923, adj growth 10.3 bp · C EV +1.42 (adj +0.81) on $11.76, P(profit) 0.2143, adj growth 7.5 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.7509, adj growth 1.4 bp

## NSH @ MTL  ·  10000 joint draws  ·  326 bet sides mapped, 5 +EV candidates, 4 on card


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
| Jonathan Marchessault: 1+ assists YES | 26 | 0.346 | 0.298 | +0.073 | +0.025 | $3.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_MIXED | D |
| Jake Evans: 1+ goals YES | 13 | 0.159 | 0.149 | +0.021 | +0.012 | $1.40 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 25 | 0.290 | 0.278 | +0.027 | +0.015 | $1.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ assists NO | 69 | 0.791 | 0.716 | +0.086 | +0.011 | $4.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Jonathan Marchessault: 1+ assists YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (6.64 vs 2.37 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.073); KXNHLAST-26OCT08NSHMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: NSH offense suppressed (<= 2 goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08NSHMTL-9|yes; why: higher confidence-adjusted growth (2.47 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.82 vs 0.375); alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT08NSHMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.023); failure: MTL offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes has the higher standalone adjusted growth (6.64 vs 2.37 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.073); they share one thesis budget; relationships: KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes: MOSTLY_INDEPENDENT (phi 0.073); KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT08NSHMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NSH offense suppressed (<= 2 goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08NSHMTL-MTLNSUZUKI14-1|no; why: higher confidence-adjusted growth (1.19 vs 0.91 bp); relationships: KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NSH:OFFENSE_4PLUS (p 0.3535): highest fidelity KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4712): highest fidelity KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.3168): highest fidelity KXNHLAST-26OCT08NSHMTL-MTLNSUZUKI14-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08NSHMTL-MTLNSUZUKI14-1|no (same contract)
- KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.434, phi -0.295)
- KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3168, phi -0.184)
- KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.434, phi -0.266)
- KXNHLAST-26OCT08NSHMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.6 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4712, phi -0.19)

portfolios: A EV +2.49 (adj +0.69) on $15.52, P(profit) 0.6305, adj growth 6.3 bp · B EV +1.80 (adj +0.57) on $10.98, P(profit) 0.5535, adj growth 5.4 bp · C EV +1.90 (adj +0.66) on $9.53, P(profit) 0.4534, adj growth 6.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PHI @ OTT  ·  10000 joint draws  ·  420 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_PHI_win | p_overtime | goals | shots OTT/PHI | OTT/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.127 | 0.67 | 0.33 | 0.00 | 5.95 | 32.0/20.5 | 17.9/27.7 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.53 | 0.47 | 0.46 | 5.88 | 32.3/20.8 | 17.7/29.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.62 | 0.38 | 0.00 | 5.94 | 26.6/26.0 | 22.9/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.49 | 0.51 | 0.47 | 5.93 | 26.9/26.3 | 22.9/23.5 | even strength |
| OTT shot control · low event (<=4) · tight (1-goal/OT) | 0.073 | 0.55 | 0.45 | 0.47 | 2.81 | 30.6/19.2 | 17.7/29.1 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 9.1 | 33.6/21.7 | 17.1/26.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Eklund: 1+ assists NO | 62 | 0.790 | 0.673 | +0.153 | +0.036 | $6.85 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Carter Yakemchuk: 1+ assists NO | 64 | 0.759 | 0.678 | +0.103 | +0.022 | $5.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Sean Couturier: 1+ goals YES | 12 | 0.153 | 0.142 | +0.025 | +0.015 | $1.68 | FUNDED_RESEARCH | $1 | PHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 14 | 0.174 | 0.162 | +0.025 | +0.013 | $1.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (12.59 vs 4.81 bp); relationships: KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.091); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: OTT offense succeeds (4+ goals)
- **Carter Yakemchuk: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08PHIOTT-OTTWEKLUND27-1|no; why: higher confidence-adjusted growth (4.81 vs 0.80 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.091); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.048); failure: OTT offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT08PHIOTT-OTT|no; why: higher confidence-adjusted growth (4.25 vs 0.00 bp); despite a smaller raw edge (+0.025 vs +0.026/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.027); failure: PHI offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (2.98 vs 0.35 bp); despite a smaller raw edge (+0.025 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.048); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.027); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:SUPPRESSED (p 0.3701): highest fidelity KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.295): highest fidelity KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4057): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.0 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4057, phi -0.199)
- KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.4 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4057, phi -0.207)
- KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4904, phi -0.207)
- KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3701, phi -0.186)

portfolios: A EV +2.42 (adj +0.70) on $15.52, P(profit) 0.6717, adj growth 6.8 bp · B EV +3.15 (adj +0.92) on $15.82, P(profit) 0.7178, adj growth 8.9 bp · C EV +2.20 (adj +0.65) on $13.42, P(profit) 0.7936, adj growth 6.0 bp · R EV +0.20 (adj +0.12) on $1.00, P(profit) 0.1529, adj growth 4.0 bp

## MIN @ TBL  ·  10000 joint draws  ·  404 bet sides mapped, 7 +EV candidates, 4 on card


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
| Ilya Mikheyev: 1+ goals YES | 16 | 0.204 | 0.191 | +0.035 | +0.021 | $2.71 | FUNDED_RESEARCH | $1 | TBL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| John Carlson: 1+ assists NO | 58 | 0.725 | 0.624 | +0.128 | +0.027 | $7.75 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ assists NO | 40 | 0.489 | 0.442 | +0.073 | +0.025 | $4.13 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
| Ryan Hartman: 1+ goals YES | 19 | 0.226 | 0.216 | +0.026 | +0.015 | $1.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Ilya Mikheyev: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08MINTB-8|yes; why: higher confidence-adjusted growth (6.93 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.878 vs 0.332); alternative not eligible: confidence-adjusted EV +0.0008 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: INTENTIONAL_DIVERSIFIER (phi -0.05); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.046); KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: TBL offense suppressed (<= 2 goals)
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (6.71 vs 5.82 bp); relationships: KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.05); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.097); KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no; why: second expression of the same thesis: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no has the higher standalone adjusted growth (6.71 vs 5.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.097); they share one thesis budget; relationships: KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.046); KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.097); KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: TBL offense succeeds (4+ goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08MINTB-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (3.16 vs 2.00 bp); relationships: KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TBL:OFFENSE_4PLUS (p 0.4133): highest fidelity KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.3719): highest fidelity KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.3611): highest fidelity KXNHLGOAL-26OCT08MINTB-MINBCOLEMAN20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3719, phi -0.209)
- KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.5 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4133, phi -0.226)
- KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4133, phi -0.3)
- KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4174, phi -0.234)

portfolios: A EV +1.97 (adj +0.53) on $15.52, P(profit) 0.7271, adj growth 5.1 bp · B EV +3.18 (adj +1.09) on $16.51, P(profit) 0.5662, adj growth 10.3 bp · C EV +3.69 (adj +1.23) on $18.52, P(profit) 0.79, adj growth 11.4 bp · R EV +0.21 (adj +0.13) on $1.00, P(profit) 0.2042, adj growth 4.6 bp

## VAN @ CAR  ·  10000 joint draws  ·  428 bet sides mapped, 28 +EV candidates, 4 on card


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
| Drew O'Connor: 1+ goals YES | 12 | 0.187 | 0.169 | +0.059 | +0.042 | $3.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 64 | 0.705 | 0.688 | +0.049 | +0.031 | $7.35 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ assists NO | 49 | 0.646 | 0.538 | +0.139 | +0.031 | $5.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CAR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 59 | 0.731 | 0.636 | +0.124 | +0.029 | $4.34 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: higher confidence-adjusted growth (32.88 vs 18.13 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.938 vs 0.509); relationships: KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT08VANCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.117); failure: VAN offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes has the higher standalone adjusted growth (18.13 vs 9.59 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.101); relationships: KXNHLGOAL-26OCT08VANCAR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT08VANCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: REINFORCING (phi 0.15); failure: CAR offense succeeds (4+ goals)
- **Sebastian Aho: 1+ assists NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes has the higher standalone adjusted growth (18.13 vs 8.29 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.128); relationships: KXNHLGOAL-26OCT08VANCAR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: REINFORCING (phi 0.165); failure: CAR offense succeeds (4+ goals)
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes; why: KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes has the higher standalone adjusted growth (8.95 vs 7.75 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.430); relationships: KXNHLGOAL-26OCT08VANCAR-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.117); KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: REINFORCING (phi 0.15); KXNHLAST-26OCT08VANCAR-CARSAHO20-1|no: REINFORCING (phi 0.165); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.19, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:OFFENSE_4PLUS (p 0.3395): highest fidelity KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08VANCAR-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2009): highest fidelity KXNHLSPREAD-26OCT08VANCAR-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08VANCAR-VAN2|yes (same contract)
- thesis CAR:SUPPRESSED (p 0.288): highest fidelity KXNHLSPREAD-26OCT08VANCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08VANCAR-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4529, phi -0.224)
- KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.5018, phi -0.201)
- KXNHLAST-26OCT08VANCAR-CARSAHO20-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.6 pts; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.5018, phi -0.257)
- KXNHLSPREAD-26OCT08VANCAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.6 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.396, phi -0.75)

portfolios: A EV +4.96 (adj +0.98) on $15.52, P(profit) 0.5265, adj growth 8.8 bp · B EV +4.56 (adj +2.07) on $20.52, P(profit) 0.5571, adj growth 19.7 bp · C EV +5.27 (adj +2.89) on $16.92, P(profit) 0.2672, adj growth 26.4 bp · R EV +0.56 (adj +0.19) on $4.00, P(profit) 0.5455, adj growth 7.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08VANCAR-CAR|no == KXNHLGAME-26OCT08VANCAR-VAN|yes

## CHI @ NYI  ·  10000 joint draws  ·  396 bet sides mapped, 6 +EV candidates, 4 on card


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
| Ryan Greene: 1+ goals YES | 12 | 0.164 | 0.150 | +0.036 | +0.023 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Patrick Kane: 2+ assists NO | 90 | 0.956 | 0.923 | +0.050 | +0.017 | $8.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Calum Ritchie: 1+ assists YES | 27 | 0.356 | 0.308 | +0.072 | +0.024 | $3.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
| Bo Horvat: 1+ goals NO | 63 | 0.679 | 0.664 | +0.033 | +0.018 | $5.59 | FUNDED_RESEARCH | $2 | NYI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08CHINYI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (10.12 vs 0.68 bp); alternative not eligible: confidence-adjusted EV +0.0079 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08CHINYI-CHIPKANE88-2|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 2+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no; why: higher confidence-adjusted growth (7.28 vs 2.18 bp); despite a smaller raw edge (+0.050 vs +0.103/contract); relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: CHI offense succeeds (4+ goals)
- **Calum Ritchie: 1+ assists YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08CHINYI-9|yes; why: higher confidence-adjusted growth (6.21 vs 0.14 bp); wins across more scripts (relative breadth 0.888 vs 0.375); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLAST-26OCT08CHINYI-CHIPKANE88-2|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: INTENTIONAL_DIVERSIFIER (phi -0.062); failure: NYI offense suppressed (<= 2 goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08CHINYI-NYIKPALMIERI21-1|no; why: higher confidence-adjusted growth (3.04 vs 1.61 bp); despite a smaller raw edge (+0.033 vs +0.083/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT08CHINYI-CHIPKANE88-2|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.062); failure: NYI offense succeeds (4+ goals)

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3014): highest fidelity KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.464): highest fidelity KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes (same contract)
- thesis NYI:SUPPRESSED (p 0.3184): highest fidelity KXNHLAST-26OCT08CHINYI-NYIKPALMIERI21-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4848, phi -0.211)
- KXNHLAST-26OCT08CHINYI-CHIPKANE88-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3014, phi -0.193)
- KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3184, phi -0.247)
- KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.464, phi -0.258)

portfolios: A EV +2.31 (adj +0.57) on $15.52, P(profit) 0.7151, adj growth 5.4 bp · B EV +2.32 (adj +1.05) on $19.86, P(profit) 0.4571, adj growth 10.0 bp · C EV +3.84 (adj +1.46) on $23.49, P(profit) 0.7027, adj growth 13.5 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.6788, adj growth 2.0 bp

## SJS @ STL  ·  10000 joint draws  ·  402 bet sides mapped, 4 +EV candidates, 4 on card


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
| Ivar Stenberg: 1+ assists NO | 72 | 0.799 | 0.757 | +0.065 | +0.023 | $7.08 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Mason Marchment: 1+ assists NO | 70 | 0.773 | 0.729 | +0.058 | +0.014 | $5.42 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Full Game: Over 8.5 goals scored YES | 16 | 0.206 | 0.181 | +0.037 | +0.011 | $1.02 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | DIRECT (0.73) | EVIDENCE_MIXED | D |
| Full Game: Over 7.5 goals scored YES | 23 | 0.284 | 0.255 | +0.042 | +0.012 | $1.03 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no; why: higher confidence-adjusted growth (5.83 vs 2.22 bp); relationships: KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLTOTAL-26OCT08SJSTL-9|yes: INTENTIONAL_DIVERSIFIER (phi -0.114); KXNHLTOTAL-26OCT08SJSTL-8|yes: INTENTIONAL_DIVERSIFIER (phi -0.123); failure: SJS offense succeeds (4+ goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no; why: second expression of the same thesis: KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no has the higher standalone adjusted growth (5.83 vs 2.22 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLTOTAL-26OCT08SJSTL-9|yes: INTENTIONAL_DIVERSIFIER (phi -0.153); KXNHLTOTAL-26OCT08SJSTL-8|yes: INTENTIONAL_DIVERSIFIER (phi -0.155); failure: SJS offense succeeds (4+ goals)
- **Full Game: Over 8.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-8|yes; why: higher confidence-adjusted growth (1.97 vs 1.72 bp); despite a smaller raw edge (+0.037 vs +0.042/contract); relationships: KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.114); KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: INTENTIONAL_DIVERSIFIER (phi -0.153); KXNHLTOTAL-26OCT08SJSTL-8|yes: DUPLICATIVE (phi 0.81); failure: SJS offense suppressed (<= 2 goals)
- **Full Game: Over 7.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-9|yes; why: second expression of the same thesis: KXNHLTOTAL-26OCT08SJSTL-9|yes has the higher standalone adjusted growth (1.97 vs 1.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.810); they share one thesis budget; relationships: KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.123); KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: INTENTIONAL_DIVERSIFIER (phi -0.155); KXNHLTOTAL-26OCT08SJSTL-9|yes: DUPLICATIVE (phi 0.81); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.422): highest fidelity KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no (same contract)
- thesis GAME:HIGH_EVENT (p 0.2839): highest fidelity KXNHLTOTAL-26OCT08SJSTL-8|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT08SJSTL-8|yes (same contract)
- KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3571, phi -0.204)
- KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3571, phi -0.247)
- KXNHLTOTAL-26OCT08SJSTL-9|yes: FUNDED_RESEARCH; family MIXED; loses 27% of the draws where the thesis happens; opposing: failure thesis SJS:SUPPRESSED (p 0.422, phi -0.37)
- KXNHLTOTAL-26OCT08SJSTL-8|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis SJS:SUPPRESSED (p 0.422, phi -0.4)

portfolios: A EV +1.96 (adj +0.58) on $15.52, P(profit) 0.2776, adj growth 5.2 bp · B EV +1.46 (adj +0.45) on $14.54, P(profit) 0.7151, adj growth 4.3 bp · C EV +1.52 (adj +0.51) on $14.11, P(profit) 0.7987, adj growth 4.8 bp · R EV +0.39 (adj +0.12) on $2.00, P(profit) 0.2839, adj growth 3.4 bp

## COL @ CGY  ·  10000 joint draws  ·  414 bet sides mapped, 31 +EV candidates, 3 on card


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
| Nathan MacKinnon: 1+ goals NO | 56 | 0.643 | 0.620 | +0.066 | +0.043 | $8.22 | FUNDED_RESEARCH | $3 | COL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Cale Makar: 3+ assists NO | 94 | 0.984 | 0.957 | +0.040 | +0.013 | $8.22 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DIFFUSE | NONE | EVIDENCE_MIXED | D |
| Colorado over 4.5 goals scored NO | 68 | 0.756 | 0.715 | +0.061 | +0.020 | $4.38 | FUNDED_RESEARCH | $2 | CGY:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT08COLCGY-CGY3|yes; why: higher confidence-adjusted growth (16.54 vs 9.34 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.996 vs 0.471); relationships: KXNHLAST-26OCT08COLCGY-COLCMAKAR8-3|no: MOSTLY_INDEPENDENT (phi 0.074); KXNHLTEAMTOTAL-26OCT08COLCGY-COL5|no: REINFORCING (phi 0.242); failure: COL offense succeeds (4+ goals)
- **Cale Makar: 3+ assists NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.074); KXNHLTEAMTOTAL-26OCT08COLCGY-COL5|no: REINFORCING (phi 0.162); failure: high-event game (8+ goals)
- **Colorado over 4.5 goals scored NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no; why: Broad expression KXNHLTEAMTOTAL-26OCT08COLCGY-COL5|no selected over player prop KXNHLAST-26OCT08COLCGY-COLNMACKINNON29-2|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: REINFORCING (phi 0.242); KXNHLAST-26OCT08COLCGY-COLCMAKAR8-3|no: REINFORCING (phi 0.162); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis COL:SUPPRESSED (p 0.3455): highest fidelity KXNHLTEAMTOTAL-26OCT08COLCGY-COL4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no — Broad expression KXNHLTEAMTOTAL-26OCT08COLCGY-COL5|no selected over player prop KXNHLAST-26OCT08COLCGY-COLNMACKINNON29-2|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)
- thesis CGY:WINS (p 0.4308): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS_BY_2PLUS (p 0.225): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4359, phi -0.276)
- KXNHLAST-26OCT08COLCGY-COLCMAKAR8-3|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; no single thesis (diffuse); fragile player expression; opposing: failure thesis GAME:HIGH_EVENT (p 0.2644, phi -0.125)
- KXNHLTEAMTOTAL-26OCT08COLCGY-COL5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4359, phi -0.647)
- override: Broad expression KXNHLTEAMTOTAL-26OCT08COLCGY-COL5|no selected over player prop KXNHLAST-26OCT08COLCGY-COLNMACKINNON29-2|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +6.16 (adj +0.75) on $15.52, P(profit) 0.6542, adj growth 6.8 bp · B EV +1.68 (adj +0.85) on $20.82, P(profit) 0.6378, adj growth 8.2 bp · C EV +3.43 (adj +1.55) on $28.83, P(profit) 0.6607, adj growth 14.5 bp · R EV +0.52 (adj +0.28) on $5.00, P(profit) 0.6435, adj growth 10.5 bp

## TOR @ VGK  ·  10000 joint draws  ·  446 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TOR_win | p_overtime | goals | shots VGK/TOR | VGK/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.148 | 0.77 | 0.23 | 0.00 | 5.99 | 34.3/21.6 | 19.3/29.2 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.58 | 0.42 | 0.48 | 5.92 | 34.3/21.9 | 18.7/30.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.70 | 0.29 | 0.00 | 6.03 | 28.3/27.5 | 24.7/23.7 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.106 | 0.80 | 0.20 | 0.00 | 9.34 | 35.8/23.2 | 19.2/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.56 | 0.44 | 0.48 | 6.0 | 28.4/27.8 | 24.5/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.69 | 0.31 | 0.00 | 9.21 | 29.7/29.1 | 24.4/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 6 | 0.094 | 0.082 | +0.030 | +0.018 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Kirill Marchenko: 2+ assists NO | 92 | 0.964 | 0.937 | +0.039 | +0.012 | $7.88 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Auston Matthews: 1+ goals NO | 66 | 0.704 | 0.692 | +0.029 | +0.016 | $4.61 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Mark Stone: 1+ goals YES | 32 | 0.358 | 0.346 | +0.023 | +0.011 | $1.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (11.52 vs 2.84 bp); despite a smaller raw edge (+0.030 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT08TORVGK-TORKMARCHENKO86-2|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT08TORVGK-VGKMSTONE61-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: VGK offense suppressed (<= 2 goals)
- **Kirill Marchenko: 2+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (4.67 vs 2.65 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: REINFORCING (phi 0.171); KXNHLGOAL-26OCT08TORVGK-VGKMSTONE61-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: TOR offense succeeds (4+ goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no; why: higher confidence-adjusted growth (2.65 vs 1.25 bp); despite a smaller raw edge (+0.029 vs +0.084/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT08TORVGK-TORKMARCHENKO86-2|no: REINFORCING (phi 0.171); KXNHLGOAL-26OCT08TORVGK-VGKMSTONE61-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense succeeds (4+ goals)
- **Mark Stone: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes; why: Player prop expression KXNHLGOAL-26OCT08TORVGK-VGKMSTONE61-1|yes selected over player prop KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.48 vs 0.49 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT08TORVGK-TORKMARCHENKO86-2|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.15, VGK shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis VGK:OFFENSE_4PLUS (p 0.5116): highest fidelity KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.5003): highest fidelity KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2881, phi -0.118)
- KXNHLAST-26OCT08TORVGK-TORKMARCHENKO86-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2815, phi -0.186)
- KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2815, phi -0.274)
- KXNHLGOAL-26OCT08TORVGK-VGKMSTONE61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2881, phi -0.254)
- override: Player prop expression KXNHLGOAL-26OCT08TORVGK-VGKMSTONE61-1|yes selected over player prop KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.48 vs 0.49 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.43 (adj +0.89) on $15.52, P(profit) 0.4203, adj growth 8.2 bp · B EV +1.47 (adj +0.76) on $15.94, P(profit) 0.322, adj growth 7.2 bp · C EV +0.96 (adj +0.37) on $11.08, P(profit) 0.7043, adj growth 3.4 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.7043, adj growth 1.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
