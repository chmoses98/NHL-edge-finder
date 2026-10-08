# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-08T18:23:39Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +31.23 | +9.16 | +30.39 | 0.822 | -11.63 | -23.06 | 85.75 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +27.37 | +13.39 | +25.67 | 0.763 | -19.17 | -30.10 | 127.20 |
| C best expression per thesis | 149.99 | +28.68 | +12.05 | +27.06 | 0.746 | -23.02 | -36.20 | 111.88 |
| R FUNDED research stakes | 15.00 | +2.49 | +1.40 | +0.92 | 0.553 | -5.58 | -7.82 | 0.00 |

## UTA @ BOS  ·  10000 joint draws  ·  174 bet sides mapped, 1 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.467 / away 0.533

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_UTA_win | p_overtime | goals | shots BOS/UTA | BOS/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.50 | 0.50 | 0.00 | 6.02 | 27.3/27.5 | 24.0/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.52 | 0.48 | 0.48 | 5.94 | 27.2/27.5 | 24.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.54 | 0.46 | 0.00 | 9.4 | 28.9/29.3 | 23.3/22.5 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.090 | 0.48 | 0.52 | 0.00 | 5.99 | 21.5/32.8 | 29.2/18.3 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.47 | 0.53 | 0.44 | 5.93 | 21.7/32.8 | 29.4/18.5 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.062 | 0.43 | 0.57 | 0.00 | 9.29 | 23.3/34.3 | 27.4/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 6.5 goals scored YES | 43 | 0.493 | 0.459 | +0.046 | +0.012 | $2.26 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT08UTABOS-9|yes; why: higher confidence-adjusted growth (1.29 vs 1.23 bp); wins across more scripts (relative breadth 0.67 vs 0.362); alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis GAME:HIGH_EVENT (p 0.2919): highest fidelity KXNHLTOTAL-26OCT08UTABOS-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT08UTABOS-7|yes (same contract)
- KXNHLTOTAL-26OCT08UTABOS-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.2096, phi -0.508)

portfolios: A EV +0.66 (adj +0.17) on $6.38, P(profit) 0.4935, adj growth 1.5 bp · B EV +0.23 (adj +0.06) on $2.26, P(profit) 0.4935, adj growth 0.6 bp · C EV +0.32 (adj +0.08) on $3.08, P(profit) 0.4935, adj growth 0.8 bp · R EV +0.10 (adj +0.03) on $1.00, P(profit) 0.4935, adj growth 1.0 bp

## DAL @ BUF  ·  10000 joint draws  ·  336 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.478 / away 0.522

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_DAL_win | p_overtime | goals | shots BUF/DAL | BUF/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.56 | 0.44 | 0.00 | 6.0 | 26.4/26.4 | 23.1/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.45 | 5.91 | 26.5/26.3 | 23.1/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.54 | 0.46 | 0.00 | 9.29 | 27.9/27.8 | 22.2/21.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.086 | 0.62 | 0.38 | 0.00 | 5.96 | 31.5/20.9 | 18.1/27.4 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.54 | 0.46 | 0.48 | 5.9 | 31.6/21.2 | 18.1/28.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.57 | 0.43 | 0.00 | 3.49 | 25.5/25.4 | 23.7/23.4 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jiri Kulich: 1+ goals YES | 15 | 0.216 | 0.198 | +0.057 | +0.039 | $4.43 | FUNDED_RESEARCH | $2 | BUF:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Justin Danforth: 1+ goals YES | 8 | 0.122 | 0.110 | +0.037 | +0.025 | $2.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Peyton Krebs: 1+ goals YES | 12 | 0.160 | 0.148 | +0.033 | +0.020 | $2.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 22 | 0.266 | 0.253 | +0.034 | +0.021 | $2.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes; why: higher confidence-adjusted growth (24.45 vs 8.07 bp); relationships: KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT08DALBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: BUF offense suppressed (<= 2 goals)
- **Justin Danforth: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes has the higher standalone adjusted growth (24.45 vs 17.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT08DALBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: BUF offense suppressed (<= 2 goals)
- **Peyton Krebs: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes has the higher standalone adjusted growth (24.45 vs 8.07 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT08DALBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: BUF offense suppressed (<= 2 goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes has the higher standalone adjusted growth (24.45 vs 5.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.019); they share one thesis budget; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis BUF:OFFENSE_4PLUS (p 0.4096): highest fidelity KXNHLSPREAD-26OCT08DALBUF-DAL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.4276): highest fidelity KXNHLSPREAD-26OCT08DALBUF-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08DALBUF-DAL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:WINS (p 0.5427): highest fidelity KXNHLSPREAD-26OCT08DALBUF-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08DALBUF-DAL2|no (same contract)
- KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3683, phi -0.208)
- KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3683, phi -0.15)
- KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3683, phi -0.199)
- KXNHLGOAL-26OCT08DALBUF-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3683, phi -0.24)

portfolios: A EV +2.83 (adj +1.26) on $15.96, P(profit) 0.6034, adj growth 11.6 bp · B EV +3.62 (adj +2.42) on $11.88, P(profit) 0.5744, adj growth 22.8 bp · C EV +2.38 (adj +1.54) on $9.89, P(profit) 0.2157, adj growth 14.1 bp · R EV +0.71 (adj +0.49) on $2.00, P(profit) 0.2157, adj growth 17.6 bp

## NSH @ MTL  ·  10000 joint draws  ·  324 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.593 / away 0.407

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_NSH_win | p_overtime | goals | shots MTL/NSH | MTL/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.59 | 0.41 | 0.00 | 6.05 | 27.9/28.0 | 24.7/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.46 | 5.94 | 28.1/28.0 | 24.6/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.59 | 0.41 | 0.00 | 9.27 | 29.3/29.2 | 23.9/22.6 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.066 | 0.68 | 0.32 | 0.00 | 6.11 | 32.4/22.1 | 19.4/27.8 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.065 | 0.53 | 0.47 | 0.00 | 6.04 | 22.3/33.0 | 29.4/18.8 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.51 | 0.49 | 0.44 | 5.95 | 22.4/33.0 | 29.3/19.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan O'Reilly: 1+ goals YES | 24 | 0.295 | 0.280 | +0.043 | +0.028 | $3.84 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Jake Evans: 1+ goals YES | 12 | 0.158 | 0.147 | +0.031 | +0.020 | $2.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 14 | 0.180 | 0.168 | +0.032 | +0.019 | $2.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ assists NO | 69 | 0.795 | 0.723 | +0.090 | +0.018 | $8.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes; why: higher confidence-adjusted growth (8.75 vs 5.25 bp); despite a smaller raw edge (+0.043 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT08NSHMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLAST-26OCT08NSHMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.029); failure: NSH offense suppressed (<= 2 goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLPTS-26OCT08NSHMTL-MTLCCAUFIELD13-3|yes; why: higher confidence-adjusted growth (7.70 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; wins across more scripts (relative breadth 0.859 vs 0.641); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT08NSHMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT08NSHMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.029); failure: MTL offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes has the higher standalone adjusted growth (7.70 vs 6.22 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT08NSHMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.022); failure: MTL offense suppressed (<= 2 goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08NSHMTL-MTLNSUZUKI14-1|no; why: higher confidence-adjusted growth (3.58 vs 1.18 bp); relationships: KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26OCT08NSHMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis NSH:OFFENSE_4PLUS (p 0.3715): highest fidelity KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:WINS_BY_2PLUS (p 0.3424): highest fidelity KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4642): highest fidelity KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes (same contract)
- KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4098, phi -0.242)
- KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3251, phi -0.184)
- KXNHLGOAL-26OCT08NSHMTL-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3251, phi -0.174)
- KXNHLAST-26OCT08NSHMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.0 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4642, phi -0.195)

portfolios: A EV +2.54 (adj +0.90) on $15.96, P(profit) 0.4757, adj growth 8.3 bp · B EV +2.74 (adj +1.28) on $16.71, P(profit) 0.4513, adj growth 12.1 bp · C EV +1.91 (adj +1.11) on $11.15, P(profit) 0.4078, adj growth 10.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PHI @ OTT  ·  10000 joint draws  ·  418 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.612 / away 0.388

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_PHI_win | p_overtime | goals | shots OTT/PHI | OTT/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.137 | 0.68 | 0.32 | 0.00 | 5.98 | 32.0/20.4 | 17.8/27.5 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.54 | 0.46 | 0.46 | 5.85 | 32.1/20.6 | 17.4/28.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.64 | 0.36 | 0.00 | 5.98 | 26.7/25.9 | 22.9/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.53 | 0.47 | 0.45 | 5.87 | 26.6/26.1 | 23.1/23.2 | even strength |
| OTT shot control · low event (<=4) · decided (2+) | 0.076 | 0.63 | 0.37 | 0.00 | 3.47 | 31.2/19.4 | 17.9/28.9 | even strength |
| OTT shot control · low event (<=4) · tight (1-goal/OT) | 0.071 | 0.57 | 0.43 | 0.50 | 2.79 | 30.7/19.5 | 18.1/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Eklund: 1+ assists NO | 61 | 0.785 | 0.668 | +0.159 | +0.042 | $8.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Sean Couturier: 1+ goals YES | 13 | 0.168 | 0.157 | +0.030 | +0.019 | $2.25 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 8 | 0.109 | 0.101 | +0.024 | +0.015 | $1.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 14 | 0.176 | 0.165 | +0.028 | +0.016 | $1.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (16.18 vs 8.09 bp); relationships: KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: OTT offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08PHIOTT-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (6.78 vs 2.87 bp); relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: PHI offense suppressed (<= 2 goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (6.55 vs 0.84 bp); despite a smaller raw edge (+0.024 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (4.51 vs 0.84 bp); despite a smaller raw edge (+0.028 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.14, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:SUPPRESSED (p 0.3694): highest fidelity KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.2792): highest fidelity KXNHLGOAL-26OCT08PHIOTT-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.4066): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.0 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4066, phi -0.195)
- KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.5145, phi -0.22)
- KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3694, phi -0.14)
- KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3694, phi -0.19)

portfolios: A EV +2.71 (adj +0.87) on $15.96, P(profit) 0.6809, adj growth 8.4 bp · B EV +3.42 (adj +1.37) on $14.15, P(profit) 0.3629, adj growth 13.1 bp · C EV +3.18 (adj +1.17) on $25.76, P(profit) 0.7562, adj growth 11.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ TBL  ·  10000 joint draws  ·  400 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.567 / away 0.433

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_MIN_win | p_overtime | goals | shots TBL/MIN | TBL/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.54 | 0.46 | 0.00 | 6.0 | 28.1/27.8 | 24.3/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.47 | 5.95 | 27.9/27.6 | 24.3/24.7 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.105 | 0.57 | 0.43 | 0.00 | 5.99 | 33.2/22.0 | 18.9/29.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.52 | 0.48 | 0.48 | 5.92 | 33.5/22.2 | 19.0/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.52 | 0.48 | 0.00 | 9.36 | 29.9/29.2 | 23.2/23.5 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.070 | 0.58 | 0.42 | 0.00 | 9.31 | 35.2/23.3 | 18.1/28.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jeffrey Viel: 1+ goals YES | 7 | 0.111 | 0.098 | +0.036 | +0.024 | $2.40 | FUNDED_RESEARCH | $1 | TBL:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Ilya Mikheyev: 1+ goals YES | 15 | 0.199 | 0.186 | +0.040 | +0.027 | $3.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| John Carlson: 1+ assists NO | 58 | 0.724 | 0.627 | +0.127 | +0.030 | $8.25 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ assists NO | 40 | 0.491 | 0.443 | +0.075 | +0.026 | $4.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
- **Jeffrey Viel: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes; why: higher confidence-adjusted growth (17.21 vs 11.44 bp); despite a smaller raw edge (+0.036 vs +0.040/contract); relationships: KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.049); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.026); failure: TBL offense suppressed (<= 2 goals)
- **Ilya Mikheyev: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08MINTB-TBACIRELLI71-1|yes; why: higher confidence-adjusted growth (11.44 vs 0.02 bp); alternative not eligible: confidence-adjusted EV +0.0012 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08MINTB-TBJVIEL25-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: INTENTIONAL_DIVERSIFIER (phi -0.055); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.047); failure: TBL offense suppressed (<= 2 goals)
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (8.20 vs 6.28 bp); relationships: KXNHLGOAL-26OCT08MINTB-TBJVIEL25-1|yes: MOSTLY_INDEPENDENT (phi -0.049); KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.055); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.12); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no; why: second expression of the same thesis: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no has the higher standalone adjusted growth (8.20 vs 6.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.120); they share one thesis budget; relationships: KXNHLGOAL-26OCT08MINTB-TBJVIEL25-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.047); KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.12); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TBL:OFFENSE_4PLUS (p 0.4069): highest fidelity KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.3786): highest fidelity KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.3752): highest fidelity KXNHLGOAL-26OCT08MINTB-MINBCOLEMAN20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08MINTB-TBJVIEL25-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3786, phi -0.144)
- KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3786, phi -0.206)
- KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.9 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4069, phi -0.244)
- KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4069, phi -0.319)

portfolios: A EV +4.04 (adj +1.91) on $15.96, P(profit) 0.5777, adj growth 18.0 bp · B EV +4.52 (adj +2.00) on $18.22, P(profit) 0.5777, adj growth 18.9 bp · C EV +3.94 (adj +1.54) on $18.58, P(profit) 0.7886, adj growth 14.3 bp · R EV +0.49 (adj +0.32) on $1.00, P(profit) 0.111, adj growth 11.3 bp

## VAN @ CAR  ·  10000 joint draws  ·  426 bet sides mapped, 34 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.742 / away 0.259

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_VAN_win | p_overtime | goals | shots CAR/VAN | CAR/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.172 | 0.70 | 0.30 | 0.00 | 6.06 | 33.9/20.7 | 18.1/29.1 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.144 | 0.71 | 0.29 | 0.00 | 9.3 | 35.7/22.0 | 17.5/27.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.142 | 0.54 | 0.46 | 0.45 | 5.95 | 34.0/20.8 | 17.7/30.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.079 | 0.58 | 0.42 | 0.00 | 6.02 | 27.7/26.4 | 23.1/23.9 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.069 | 0.70 | 0.30 | 0.00 | 3.43 | 32.1/19.2 | 17.9/29.7 | late empty net |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.61 | 0.39 | 0.00 | 9.43 | 29.1/27.9 | 22.3/22.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sebastian Aho: 1+ goals NO | 63 | 0.705 | 0.685 | +0.059 | +0.039 | $6.41 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Andrei Svechnikov: 1+ goals NO | 63 | 0.698 | 0.680 | +0.052 | +0.033 | $6.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 45 | 0.607 | 0.502 | +0.140 | +0.034 | $3.72 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 59 | 0.728 | 0.635 | +0.121 | +0.028 | $2.19 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes has the higher standalone adjusted growth (19.25 vs 14.57 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.129); relationships: KXNHLGOAL-26OCT08VANCAR-CARASVECHNIKOV37-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT08VANCAR-CAR2|no: REINFORCING (phi 0.164); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: REINFORCING (phi 0.171); failure: CAR offense succeeds (4+ goals)
- **Andrei Svechnikov: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: Player prop expression KXNHLGOAL-26OCT08VANCAR-CARASVECHNIKOV37-1|no selected over player prop KXNHLAST-26OCT08VANCAR-CARSAHO20-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT08VANCAR-CAR2|no: REINFORCING (phi 0.169); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: REINFORCING (phi 0.162); failure: CAR offense succeeds (4+ goals)
- **Carolina wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08VANCAR-CAR3|no; why: Broad expression KXNHLSPREAD-26OCT08VANCAR-CAR2|no selected over broad KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes because adjusted EV is 1.4 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: REINFORCING (phi 0.164); KXNHLGOAL-26OCT08VANCAR-CARASVECHNIKOV37-1|no: REINFORCING (phi 0.169); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: DUPLICATIVE (phi 0.76); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08VANCAR-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT08VANCAR-CAR2|no has the higher standalone adjusted growth (10.42 vs 7.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.760); they share one thesis budget; relationships: KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: REINFORCING (phi 0.171); KXNHLGOAL-26OCT08VANCAR-CARASVECHNIKOV37-1|no: REINFORCING (phi 0.162); KXNHLSPREAD-26OCT08VANCAR-CAR2|no: DUPLICATIVE (phi 0.76); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · high event (8+) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14.
- thesis VAN:OFFENSE_4PLUS (p 0.3393): highest fidelity KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08VANCAR-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.1989): highest fidelity KXNHLGAME-26OCT08VANCAR-VAN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT08VANCAR-VAN|yes (same contract)
- thesis VAN:WINS (p 0.392): highest fidelity KXNHLGAME-26OCT08VANCAR-VAN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT08VANCAR-VAN|yes (same contract)
- KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4945, phi -0.254)
- KXNHLGOAL-26OCT08VANCAR-CARASVECHNIKOV37-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4945, phi -0.221)
- KXNHLSPREAD-26OCT08VANCAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.2 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3928, phi -1.0)
- KXNHLSPREAD-26OCT08VANCAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.3 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3928, phi -0.76)
- override: Player prop expression KXNHLGOAL-26OCT08VANCAR-CARASVECHNIKOV37-1|no selected over player prop KXNHLAST-26OCT08VANCAR-CARSAHO20-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLSPREAD-26OCT08VANCAR-CAR2|no selected over broad KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes because adjusted EV is 1.4 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.43 (adj +1.36) on $15.96, P(profit) 0.53, adj growth 12.6 bp · B EV +2.63 (adj +1.08) on $18.45, P(profit) 0.7176, adj growth 10.4 bp · C EV +5.48 (adj +2.50) on $12.86, P(profit) 0.3547, adj growth 23.0 bp · R EV +0.68 (adj +0.24) on $4.00, P(profit) 0.5483, adj growth 9.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08VANCAR-CAR|no == KXNHLGAME-26OCT08VANCAR-VAN|yes

## CHI @ NYI  ·  10000 joint draws  ·  398 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.622 / away 0.378

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CHI_win | p_overtime | goals | shots NYI/CHI | NYI/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NYI shot control · normal event (5-7) · decided (2+) | 0.133 | 0.71 | 0.29 | 0.00 | 6.0 | 33.1/21.1 | 18.6/28.4 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.56 | 0.44 | 0.47 | 5.89 | 33.3/21.4 | 18.2/29.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.65 | 0.35 | 0.00 | 6.03 | 27.4/26.9 | 24.0/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.51 | 0.49 | 0.47 | 5.96 | 27.3/26.6 | 23.3/24.0 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.086 | 0.73 | 0.27 | 0.00 | 9.18 | 34.7/22.4 | 18.0/26.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.67 | 0.33 | 0.00 | 9.28 | 29.0/28.1 | 23.0/21.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 11 | 0.154 | 0.142 | +0.038 | +0.025 | $2.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Calum Ritchie: 1+ assists YES | 26 | 0.350 | 0.302 | +0.076 | +0.029 | $3.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Patrick Kane: 1+ assists NO | 59 | 0.727 | 0.631 | +0.120 | +0.024 | $7.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Bo Horvat: 1+ goals NO | 62 | 0.672 | 0.658 | +0.036 | +0.021 | $6.56 | FUNDED_RESEARCH | $2 | NYI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08CHINYI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (13.25 vs 0.53 bp); alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: CHI offense suppressed (<= 2 goals)
- **Calum Ritchie: 1+ assists YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08CHINYI-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (9.18 vs 0.23 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: INTENTIONAL_DIVERSIFIER (phi -0.071); failure: NYI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08CHINYI-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (5.46 vs 0.30 bp); alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CHI offense succeeds (4+ goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08CHINYI-NYIVEKLUND73-1|no; why: higher confidence-adjusted growth (4.38 vs 0.15 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.071); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NYI offense succeeds (4+ goals)

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.4651): highest fidelity KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4838): highest fidelity KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no (same contract)
- thesis NYI:SUPPRESSED (p 0.3263): highest fidelity KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no (same contract)
- KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4838, phi -0.215)
- KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3263, phi -0.257)
- KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.7 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2974, phi -0.251)
- KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.4651, phi -0.23)

portfolios: A EV +2.75 (adj +0.78) on $15.96, P(profit) 0.6376, adj growth 7.5 bp · B EV +3.86 (adj +1.54) on $20.89, P(profit) 0.7002, adj growth 14.5 bp · C EV +4.07 (adj +1.31) on $25.02, P(profit) 0.6425, adj growth 12.2 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.6723, adj growth 2.5 bp

## SJS @ STL  ·  10000 joint draws  ·  398 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.572 / away 0.428

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_SJS_win | p_overtime | goals | shots STL/SJS | STL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 6.03 | 26.5/26.3 | 23.3/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.46 | 5.94 | 26.5/26.3 | 22.9/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.58 | 0.42 | 0.00 | 9.34 | 28.1/27.9 | 22.5/21.4 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.088 | 0.68 | 0.33 | 0.00 | 6.07 | 31.3/21.0 | 18.4/26.7 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.57 | 0.43 | 0.47 | 5.93 | 31.8/21.4 | 18.3/28.3 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.061 | 0.68 | 0.32 | 0.00 | 9.3 | 33.4/22.6 | 18.3/25.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Philip Broberg: 1+ goals YES | 7 | 0.101 | 0.092 | +0.026 | +0.017 | $1.76 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 72 | 0.808 | 0.762 | +0.074 | +0.028 | $8.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Mason McTavish: 1+ assists NO | 70 | 0.783 | 0.739 | +0.069 | +0.024 | $8.36 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Pius Suter: 1+ goals YES | 14 | 0.176 | 0.166 | +0.028 | +0.018 | $2.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Philip Broberg: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08SJSTL-STLCMCMICHAEL77-1|yes; why: higher confidence-adjusted growth (9.01 vs 0.32 bp); alternative not eligible: confidence-adjusted EV +0.0050 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT08SJSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: STL offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no; why: higher confidence-adjusted growth (8.57 vs 2.85 bp); despite a smaller raw edge (+0.074 vs +0.084/contract); relationships: KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT08SJSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.025); failure: SJS offense succeeds (4+ goals)
- **Mason McTavish: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08SJSTL-STLAJIRICEK36-1|no; why: higher confidence-adjusted growth (6.45 vs 0.46 bp); alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT08SJSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.028); failure: STL offense succeeds (4+ goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08SJSTL-STLCMCMICHAEL77-1|yes; why: higher confidence-adjusted growth (5.22 vs 0.32 bp); alternative not eligible: confidence-adjusted EV +0.0050 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.025); KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.028); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:SUPPRESSED (p 0.4352): highest fidelity KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3496): highest fidelity KXNHLAST-26OCT08SJSTL-SJDORLOV9-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT08SJSTL-SJCGRAF51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.4425): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3389, phi -0.119)
- KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3496, phi -0.207)
- KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4425, phi -0.199)
- KXNHLGOAL-26OCT08SJSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3389, phi -0.182)

portfolios: A EV +2.02 (adj +0.56) on $15.96, P(profit) 0.6763, adj growth 5.3 bp · B EV +2.64 (adj +1.24) on $20.52, P(profit) 0.7244, adj growth 11.8 bp · C EV +1.54 (adj +0.66) on $13.93, P(profit) 0.8549, adj growth 6.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ CGY  ·  10000 joint draws  ·  418 bet sides mapped, 37 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.324 / away 0.676

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_COL_win | p_overtime | goals | shots CGY/COL | CGY/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.131 | 0.36 | 0.64 | 0.00 | 6.0 | 22.9/35.5 | 30.9/20.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.48 | 0.52 | 0.50 | 5.91 | 23.1/35.5 | 32.0/19.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.42 | 0.58 | 0.00 | 5.97 | 28.6/29.5 | 25.5/25.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.50 | 0.50 | 0.46 | 5.94 | 28.9/29.7 | 26.5/25.6 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.084 | 0.36 | 0.64 | 0.00 | 9.28 | 24.2/37.2 | 29.7/19.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.41 | 0.59 | 0.00 | 9.24 | 30.1/31.2 | 24.5/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nathan MacKinnon: 1+ goals NO | 55 | 0.644 | 0.619 | +0.077 | +0.052 | $6.27 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Martin Necas: 1+ goals NO | 61 | 0.701 | 0.677 | +0.074 | +0.050 | $6.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no; why: higher confidence-adjusted growth (24.11 vs 23.58 bp); relationships: KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: COL offense succeeds (4+ goals)
- **Martin Necas: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no has the higher standalone adjusted growth (24.11 vs 23.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis COL:SUPPRESSED (p 0.3484): highest fidelity KXNHLTEAMTOTAL-26OCT08COLCGY-COL4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS_BY_2PLUS (p 0.221): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS (p 0.4375): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4289, phi -0.263)
- KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4289, phi -0.228)

portfolios: A EV +6.21 (adj +0.91) on $15.96, P(profit) 0.7613, adj growth 8.4 bp · B EV +1.59 (adj +1.07) on $12.54, P(profit) 0.4508, adj growth 10.5 bp · C EV +4.99 (adj +1.82) on $19.73, P(profit) 0.6698, adj growth 17.0 bp · R EV +0.27 (adj +0.18) on $2.00, P(profit) 0.644, adj growth 7.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08COLCGY-COL|no == KXNHLGAME-26OCT08COLCGY-CGY|yes

## TOR @ VGK  ·  10000 joint draws  ·  446 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.605 / away 0.395

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
| Brayden McNabb: 1+ goals YES | 6 | 0.094 | 0.083 | +0.030 | +0.019 | $1.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Braeden Bowman: 1+ goals YES | 17 | 0.218 | 0.205 | +0.038 | +0.025 | $2.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 81 | 0.854 | 0.841 | +0.033 | +0.020 | $8.36 | FUNDED_RESEARCH | $3 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 8 | 0.104 | 0.097 | +0.019 | +0.012 | $1.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (13.15 vs 2.84 bp); despite a smaller raw edge (+0.030 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT08TORVGK-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: VGK offense suppressed (<= 2 goals)
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (9.06 vs 2.84 bp); despite a smaller raw edge (+0.038 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT08TORVGK-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: VGK offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (5.85 vs 2.26 bp); relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT08TORVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: TOR offense succeeds (4+ goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (3.87 vs 0.00 bp); despite a smaller raw edge (+0.019 vs +0.026/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT08TORVGK-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT08TORVGK-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.15, VGK shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis VGK:OFFENSE_4PLUS (p 0.5116): highest fidelity KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.5003): highest fidelity KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:OFFENSE_4PLUS (p 0.2815): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2881, phi -0.118)
- KXNHLGOAL-26OCT08TORVGK-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2881, phi -0.178)
- KXNHLGOAL-26OCT08TORVGK-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2815, phi -0.179)
- KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.5003, phi -0.172)

portfolios: A EV +2.04 (adj +0.44) on $15.96, P(profit) 0.6295, adj growth 4.1 bp · B EV +2.11 (adj +1.33) on $14.38, P(profit) 0.365, adj growth 12.6 bp · C EV +0.89 (adj +0.32) on $9.99, P(profit) 0.3729, adj growth 3.0 bp · R EV +0.12 (adj +0.07) on $3.00, P(profit) 0.854, adj growth 2.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
