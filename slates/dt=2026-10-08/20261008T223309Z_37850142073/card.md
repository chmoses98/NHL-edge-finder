# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-08T22:33:09Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +30.53 | +7.75 | +30.83 | 0.816 | -12.62 | -24.92 | 71.88 |
| B thesis-diversified (joint) ← optimiser card | 150.02 | +30.65 | +15.61 | +28.47 | 0.751 | -22.96 | -36.56 | 146.70 |
| C best expression per thesis | 150.01 | +27.95 | +10.41 | +26.98 | 0.772 | -18.89 | -31.59 | 97.30 |
| R FUNDED research stakes | 14.00 | +2.20 | +1.17 | +1.34 | 0.562 | -5.10 | -7.01 | 0.00 |

## UTA @ BOS  ·  10000 joint draws  ·  174 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.452 / away 0.548

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
| Boston over 3.5 goals scored YES | 36 | 0.425 | 0.390 | +0.049 | +0.014 | $1.59 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Full Game: Over 6.5 goals scored YES | 43 | 0.493 | 0.459 | +0.046 | +0.012 | $1.32 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Boston over 2.5 goals scored YES | 58 | 0.643 | 0.609 | +0.046 | +0.012 | $1.06 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Boston over 3.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08UTABOS-7|yes; why: higher confidence-adjusted growth (1.79 vs 1.29 bp); relationships: KXNHLTOTAL-26OCT08UTABOS-7|yes: REINFORCING (phi 0.463); KXNHLTEAMTOTAL-26OCT08UTABOS-BOS3|yes: DUPLICATIVE (phi 0.641); failure: BOS offense suppressed (<= 2 goals)
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes has the higher standalone adjusted growth (1.79 vs 1.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.463); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes: REINFORCING (phi 0.463); KXNHLTEAMTOTAL-26OCT08UTABOS-BOS3|yes: REINFORCING (phi 0.474); failure: low-event game (<= 4 goals)
- **Boston over 2.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes has the higher standalone adjusted growth (1.79 vs 1.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.641); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes: DUPLICATIVE (phi 0.641); KXNHLTOTAL-26OCT08UTABOS-7|yes: REINFORCING (phi 0.474); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.4143): highest fidelity KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.2919): highest fidelity KXNHLTOTAL-26OCT08UTABOS-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.3673, phi -0.655)
- KXNHLTOTAL-26OCT08UTABOS-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.2096, phi -0.508)
- KXNHLTEAMTOTAL-26OCT08UTABOS-BOS3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.3673, phi -0.978)

portfolios: A EV +1.55 (adj +0.42) on $15.00, P(profit) 0.5315, adj growth 3.3 bp · B EV +0.42 (adj +0.12) on $3.97, P(profit) 0.5315, adj growth 1.1 bp · C EV +0.36 (adj +0.10) on $2.81, P(profit) 0.425, adj growth 1.0 bp · R EV +0.31 (adj +0.08) on $3.00, P(profit) 0.5315, adj growth 2.8 bp

## DAL @ BUF  ·  10000 joint draws  ·  336 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.479 / away 0.521

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
| Justin Danforth: 1+ goals YES | 8 | 0.122 | 0.110 | +0.037 | +0.025 | $2.76 | FUNDED_RESEARCH | $1 | BUF:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Peyton Krebs: 1+ goals YES | 11 | 0.160 | 0.145 | +0.043 | +0.028 | $3.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jiri Kulich: 1+ goals YES | 16 | 0.216 | 0.199 | +0.046 | +0.030 | $3.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ryan McLeod: 1+ goals YES | 13 | 0.171 | 0.160 | +0.033 | +0.022 | $2.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Justin Danforth: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes; why: higher confidence-adjusted growth (17.15 vs 16.74 bp); despite a smaller raw edge (+0.037 vs +0.043/contract); relationships: KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT08DALBUF-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: BUF offense suppressed (<= 2 goals)
- **Peyton Krebs: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes; why: higher confidence-adjusted growth (16.74 vs 13.64 bp); despite a smaller raw edge (+0.043 vs +0.046/contract); relationships: KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT08DALBUF-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: BUF offense suppressed (<= 2 goals)
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes has the higher standalone adjusted growth (16.74 vs 13.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT08DALBUF-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: BUF offense suppressed (<= 2 goals)
- **Ryan McLeod: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes has the higher standalone adjusted growth (16.74 vs 8.50 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.018); they share one thesis budget; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis BUF:OFFENSE_4PLUS (p 0.4096): highest fidelity KXNHLSPREAD-26OCT08DALBUF-DAL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.4276): highest fidelity KXNHLSPREAD-26OCT08DALBUF-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08DALBUF-DAL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:WINS (p 0.5427): highest fidelity KXNHLSPREAD-26OCT08DALBUF-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08DALBUF-DAL2|no (same contract)
- KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3683, phi -0.15)
- KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3683, phi -0.199)
- KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3683, phi -0.208)
- KXNHLGOAL-26OCT08DALBUF-BUFRMCLEOD71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3683, phi -0.176)

portfolios: A EV +2.45 (adj +0.98) on $15.00, P(profit) 0.6034, adj growth 9.1 bp · B EV +4.09 (adj +2.70) on $12.50, P(profit) 0.5158, adj growth 25.2 bp · C EV +1.63 (adj +0.97) on $7.80, P(profit) 0.1604, adj growth 9.0 bp · R EV +0.43 (adj +0.29) on $1.00, P(profit) 0.122, adj growth 10.6 bp

## NSH @ MTL  ·  10000 joint draws  ·  324 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.595 / away 0.406

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
| Jake Evans: 1+ goals YES | 12 | 0.158 | 0.147 | +0.031 | +0.020 | $2.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 14 | 0.180 | 0.169 | +0.032 | +0.020 | $2.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Nils Hoglander: 1+ goals NO | 80 | 0.842 | 0.830 | +0.031 | +0.019 | $9.39 | FUNDED_RESEARCH | $3 | NSH:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 25 | 0.295 | 0.283 | +0.032 | +0.020 | $3.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLPTS-26OCT08NSHMTL-NSHRJOSI59-1|no; why: higher confidence-adjusted growth (7.70 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT08NSHMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT08NSHMTL-NSHNHOGLANDER21-1|no: MOSTLY_INDEPENDENT (phi 0.031); KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: MTL offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes has the higher standalone adjusted growth (7.70 vs 7.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT08NSHMTL-NSHNHOGLANDER21-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: MTL offense suppressed (<= 2 goals)
- **Nils Hoglander: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT08NSHMTL-NSHRJOSI59-1|no; why: higher confidence-adjusted growth (5.23 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.031); KXNHLGOAL-26OCT08NSHMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: NSH offense succeeds (4+ goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes; why: higher confidence-adjusted growth (4.38 vs 2.98 bp); despite a smaller raw edge (+0.032 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT08NSHMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT08NSHMTL-NSHNHOGLANDER21-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis MTL:WINS_BY_2PLUS (p 0.3424): highest fidelity KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4642): highest fidelity KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.3715): highest fidelity KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3251, phi -0.184)
- KXNHLGOAL-26OCT08NSHMTL-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3251, phi -0.174)
- KXNHLGOAL-26OCT08NSHMTL-NSHNHOGLANDER21-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3715, phi -0.193)
- KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4098, phi -0.242)

portfolios: A EV +2.44 (adj +0.91) on $15.00, P(profit) 0.5805, adj growth 8.5 bp · B EV +1.89 (adj +1.20) on $17.59, P(profit) 0.4839, adj growth 11.3 bp · C EV +1.09 (adj +0.69) on $6.19, P(profit) 0.4078, adj growth 6.4 bp · R EV +0.11 (adj +0.07) on $3.00, P(profit) 0.842, adj growth 2.7 bp

## PHI @ OTT  ·  10000 joint draws  ·  418 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.613 / away 0.387

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
| William Eklund: 1+ assists NO | 62 | 0.785 | 0.668 | +0.149 | +0.032 | $9.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Sean Couturier: 1+ goals YES | 13 | 0.168 | 0.157 | +0.030 | +0.019 | $2.53 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 8 | 0.109 | 0.101 | +0.024 | +0.015 | $1.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 14 | 0.176 | 0.166 | +0.028 | +0.018 | $2.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (9.51 vs 8.09 bp); relationships: KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: OTT offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08PHIOTT-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (6.78 vs 2.87 bp); relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: PHI offense suppressed (<= 2 goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (6.55 vs 3.46 bp); despite a smaller raw edge (+0.024 vs +0.083/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (5.22 vs 3.46 bp); despite a smaller raw edge (+0.028 vs +0.083/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.14, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:SUPPRESSED (p 0.3694): highest fidelity KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.2792): highest fidelity KXNHLGOAL-26OCT08PHIOTT-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.4066): highest fidelity KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes (same contract)
- KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.0 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4066, phi -0.195)
- KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.5145, phi -0.22)
- KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3694, phi -0.14)
- KXNHLGOAL-26OCT08PHIOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3694, phi -0.19)

portfolios: A EV +3.81 (adj +0.70) on $15.00, P(profit) 0.6624, adj growth 6.6 bp · B EV +3.70 (adj +1.43) on $16.07, P(profit) 0.3629, adj growth 13.5 bp · C EV +3.65 (adj +1.15) on $26.05, P(profit) 0.7736, adj growth 10.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ TBL  ·  10000 joint draws  ·  400 bet sides mapped, 12 +EV candidates, 4 on card

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
| Erik Cernak: 1+ goals YES | 3 | 0.052 | 0.045 | +0.020 | +0.013 | $1.32 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.08) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 9 | 0.130 | 0.117 | +0.034 | +0.022 | $2.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 18 | 0.230 | 0.216 | +0.040 | +0.026 | $3.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Ilya Mikheyev: 1+ goals YES | 15 | 0.199 | 0.183 | +0.040 | +0.024 | $3.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Erik Cernak: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes; why: higher confidence-adjusted growth (11.64 vs 9.41 bp); despite a smaller raw edge (+0.020 vs +0.040/contract); relationships: KXNHLGOAL-26OCT08MINTB-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: TBL offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (11.53 vs 9.64 bp); despite a smaller raw edge (+0.034 vs +0.040/contract); relationships: KXNHLGOAL-26OCT08MINTB-TBECERNAK81-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08MINTB-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (9.64 vs 1.99 bp); relationships: KXNHLGOAL-26OCT08MINTB-TBECERNAK81-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT08MINTB-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: MIN offense suppressed (<= 2 goals)
- **Ilya Mikheyev: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08MINTB-TBACIRELLI71-1|yes; why: higher confidence-adjusted growth (9.41 vs 0.02 bp); alternative not eligible: confidence-adjusted EV +0.0012 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08MINTB-TBECERNAK81-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT08MINTB-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: TBL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.3752): highest fidelity KXNHLGOAL-26OCT08MINTB-MINBCOLEMAN20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:OFFENSE_4PLUS (p 0.4069): highest fidelity KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.3786): highest fidelity KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no (same contract)
- KXNHLGOAL-26OCT08MINTB-TBECERNAK81-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 92% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3786, phi -0.094)
- KXNHLGOAL-26OCT08MINTB-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4041, phi -0.182)
- KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4041, phi -0.225)
- KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3786, phi -0.206)

portfolios: A EV +2.53 (adj +0.57) on $15.00, P(profit) 0.673, adj growth 5.4 bp · B EV +3.20 (adj +2.04) on $10.32, P(profit) 0.4887, adj growth 19.0 bp · C EV +3.94 (adj +1.55) on $17.93, P(profit) 0.381, adj growth 14.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ CAR  ·  10000 joint draws  ·  426 bet sides mapped, 35 +EV candidates, 3 on card

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
| Sebastian Aho: 1+ goals NO | 62 | 0.705 | 0.683 | +0.069 | +0.046 | $7.83 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ assists NO | 48 | 0.653 | 0.534 | +0.155 | +0.036 | $6.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CAR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 59 | 0.728 | 0.635 | +0.121 | +0.028 | $6.75 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN2|yes; why: KXNHLSPREAD-26OCT08VANCAR-VAN2|yes has the higher standalone adjusted growth (25.34 vs 20.34 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.157); relationships: KXNHLAST-26OCT08VANCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: REINFORCING (phi 0.171); failure: CAR offense succeeds (4+ goals)
- **Sebastian Aho: 1+ assists NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN2|yes; why: KXNHLSPREAD-26OCT08VANCAR-VAN2|yes has the higher standalone adjusted growth (25.34 vs 11.62 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.142); relationships: KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: REINFORCING (phi 0.163); failure: CAR offense succeeds (4+ goals)
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08VANCAR-CAR2|no; why: KXNHLSPREAD-26OCT08VANCAR-CAR2|no has the higher standalone adjusted growth (10.42 vs 7.31 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.760); relationships: KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: REINFORCING (phi 0.171); KXNHLAST-26OCT08VANCAR-CARSAHO20-1|no: REINFORCING (phi 0.163); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · high event (8+) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14.
- thesis VAN:WINS_BY_2PLUS (p 0.1989): highest fidelity KXNHLGAME-26OCT08VANCAR-VAN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT08VANCAR-VAN|yes (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3393): highest fidelity KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08VANCAR-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CAR:SUPPRESSED (p 0.2975): highest fidelity KXNHLSPREAD-26OCT08VANCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4945, phi -0.254)
- KXNHLAST-26OCT08VANCAR-CARSAHO20-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.3 pts; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4945, phi -0.247)
- KXNHLSPREAD-26OCT08VANCAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.3 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3928, phi -0.76)

portfolios: A EV +5.81 (adj +1.47) on $15.00, P(profit) 0.53, adj growth 13.5 bp · B EV +4.15 (adj +1.34) on $20.84, P(profit) 0.7551, adj growth 12.8 bp · C EV +3.75 (adj +1.34) on $8.10, P(profit) 0.6072, adj growth 12.4 bp · R EV +0.62 (adj +0.24) on $4.00, P(profit) 0.5483, adj growth 9.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08VANCAR-CAR|no == KXNHLGAME-26OCT08VANCAR-VAN|yes

## CHI @ NYI  ·  10000 joint draws  ·  398 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.621 / away 0.379

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
| Ryan Greene: 1+ goals YES | 10 | 0.154 | 0.140 | +0.048 | +0.033 | $3.95 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Calum Ritchie: 1+ assists YES | 26 | 0.350 | 0.302 | +0.076 | +0.029 | $4.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Patrick Kane: 1+ assists NO | 59 | 0.727 | 0.631 | +0.120 | +0.024 | $8.79 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Casey Cizikas: 1+ goals YES | 11 | 0.140 | 0.131 | +0.023 | +0.014 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08CHINYI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (24.77 vs 0.53 bp); alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26OCT08CHINYI-NYICCIZIKAS53-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: CHI offense suppressed (<= 2 goals)
- **Calum Ritchie: 1+ assists YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08CHINYI-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (9.18 vs 0.23 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT08CHINYI-NYICCIZIKAS53-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NYI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08CHINYI-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (5.46 vs 1.05 bp); relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT08CHINYI-NYICCIZIKAS53-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: CHI offense succeeds (4+ goals)
- **Casey Cizikas: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes has the higher standalone adjusted growth (9.18 vs 4.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.4651): highest fidelity KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4838): highest fidelity KXNHLAST-26OCT08CHINYI-CHIBBYRAM24-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:SUPPRESSED (p 0.3263): highest fidelity KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no (same contract)
- KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4838, phi -0.215)
- KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3263, phi -0.257)
- KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.7 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2974, phi -0.251)
- KXNHLGOAL-26OCT08CHINYI-NYICCIZIKAS53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3263, phi -0.169)

portfolios: A EV +2.52 (adj +0.68) on $15.00, P(profit) 0.6376, adj growth 6.5 bp · B EV +5.07 (adj +2.26) on $18.80, P(profit) 0.4386, adj growth 21.1 bp · C EV +3.73 (adj +1.20) on $22.90, P(profit) 0.6425, adj growth 11.2 bp · R EV +0.45 (adj +0.31) on $1.00, P(profit) 0.1545, adj growth 11.6 bp

## SJS @ STL  ·  10000 joint draws  ·  402 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.583 / away 0.417

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
| Philip Broberg: 1+ goals YES | 7 | 0.101 | 0.092 | +0.026 | +0.017 | $1.97 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Ross Johnston: 1+ goals YES | 6 | 0.087 | 0.079 | +0.023 | +0.015 | $1.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 70 | 0.789 | 0.740 | +0.074 | +0.025 | $9.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Pius Suter: 1+ goals YES | 14 | 0.176 | 0.166 | +0.028 | +0.018 | $2.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Philip Broberg: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-7|yes; why: higher confidence-adjusted growth (9.01 vs 0.39 bp); despite a smaller raw edge (+0.026 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.893 vs 0.69); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08SJSTL-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT08SJSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: STL offense suppressed (<= 2 goals)
- **Ross Johnston: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-7|yes; why: higher confidence-adjusted growth (7.76 vs 0.39 bp); despite a smaller raw edge (+0.023 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.91 vs 0.69); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT08SJSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: STL offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (6.64 vs 2.22 bp); relationships: KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT08SJSTL-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT08SJSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: SJS offense succeeds (4+ goals)
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-7|yes; why: higher confidence-adjusted growth (5.22 vs 0.39 bp); despite a smaller raw edge (+0.028 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.883 vs 0.69); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT08SJSTL-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:SUPPRESSED (p 0.4352): highest fidelity KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:OFFENSE_4PLUS (p 0.3496): highest fidelity KXNHLAST-26OCT08SJSTL-SJDORLOV9-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT08SJSTL-SJDORLOV9-1|yes (same contract)
- thesis STL:SUPPRESSED (p 0.3389): highest fidelity KXNHLAST-26OCT08SJSTL-STLAJIRICEK36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08SJSTL-STLAJIRICEK36-1|no (same contract)
- KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3389, phi -0.119)
- KXNHLGOAL-26OCT08SJSTL-STLRJOHNSTON49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3389, phi -0.115)
- KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3496, phi -0.192)
- KXNHLGOAL-26OCT08SJSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3389, phi -0.182)

portfolios: A EV +1.81 (adj +0.57) on $15.00, P(profit) 0.6763, adj growth 5.5 bp · B EV +2.68 (adj +1.43) on $15.33, P(profit) 0.3259, adj growth 13.4 bp · C EV +2.29 (adj +0.73) on $19.96, P(profit) 0.7248, adj growth 6.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ CGY  ·  10000 joint draws  ·  418 bet sides mapped, 34 +EV candidates, 3 on card

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
| Nathan MacKinnon: 1+ goals NO | 55 | 0.644 | 0.619 | +0.077 | +0.052 | $7.04 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Martin Necas: 1+ goals NO | 62 | 0.701 | 0.679 | +0.064 | +0.043 | $7.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Scott Wedgewood: 22+ saves YES | 51 | 0.588 | 0.544 | +0.060 | +0.016 | $4.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:NET_HIGH_VOLUME | DIRECT (0.95) | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no; why: higher confidence-adjusted growth (24.11 vs 17.35 bp); relationships: KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSAVE-26OCT08COLCGY-COLSWEDGEWOOD41-22|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: COL offense succeeds (4+ goals)
- **Martin Necas: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no; why: Player prop expression KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no selected over player prop KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no because adjusted EV is 0.7 pts higher while thesis capture is 0.85 vs 0.94 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability); relationships: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSAVE-26OCT08COLCGY-COLSWEDGEWOOD41-22|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: COL offense succeeds (4+ goals)
- **Scott Wedgewood: 22+ saves YES** — thesis: COL net faces heavy volume (33+ shots; CGY pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: COL net faces light volume (<= 25 shots; CGY suppressed)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis COL:SUPPRESSED (p 0.3484): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no — Player prop expression KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no selected over player prop KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no because adjusted EV is 0.7 pts higher while thesis capture is 0.85 vs 0.94 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)
- thesis CGY:WINS_BY_2PLUS (p 0.221): highest fidelity KXNHLSPREAD-26OCT08COLCGY-CGY2|yes [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS (p 0.4375): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4289, phi -0.263)
- KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4289, phi -0.228)
- KXNHLSAVE-26OCT08COLCGY-COLSWEDGEWOOD41-22|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family MIXED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:NET_LOW_VOLUME (p 0.4694, phi -0.728)
- override: Player prop expression KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no selected over player prop KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no because adjusted EV is 0.7 pts higher while thesis capture is 0.85 vs 0.94 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs CALIBRATION_WARNING; decided on family reliability)

portfolios: A EV +5.72 (adj +0.83) on $15.00, P(profit) 0.7613, adj growth 7.7 bp · B EV +2.16 (adj +1.25) on $18.44, P(profit) 0.715, adj growth 12.1 bp · C EV +5.21 (adj +1.85) on $22.61, P(profit) 0.6389, adj growth 17.4 bp · R EV +0.27 (adj +0.18) on $2.00, P(profit) 0.644, adj growth 7.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08COLCGY-COL|no == KXNHLGAME-26OCT08COLCGY-CGY|yes

## TOR @ VGK  ·  10000 joint draws  ·  448 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.601 / away 0.400

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TOR_win | p_overtime | goals | shots VGK/TOR | VGK/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.153 | 0.76 | 0.24 | 0.00 | 5.99 | 34.0/21.4 | 19.1/29.0 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.59 | 0.41 | 0.48 | 5.92 | 34.3/21.7 | 18.7/30.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.68 | 0.32 | 0.00 | 6.04 | 28.4/27.7 | 25.0/24.0 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.105 | 0.77 | 0.23 | 0.00 | 9.28 | 36.0/23.0 | 18.9/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.47 | 0.49 | 5.96 | 28.4/27.7 | 24.5/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.73 | 0.27 | 0.00 | 9.35 | 30.1/29.2 | 24.6/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Marc Gatcomb: 1+ goals YES | 11 | 0.152 | 0.140 | +0.035 | +0.024 | $2.87 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.088 | 0.080 | +0.024 | +0.016 | $1.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 8 | 0.112 | 0.103 | +0.027 | +0.017 | $2.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Darren Raddysh: 1+ assists NO | 63 | 0.721 | 0.673 | +0.075 | +0.027 | $9.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
- **Marc Gatcomb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (11.44 vs 6.95 bp); despite a smaller raw edge (+0.035 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: VGK offense suppressed (<= 2 goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (8.88 vs 6.95 bp); despite a smaller raw edge (+0.024 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08TORVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: VGK offense suppressed (<= 2 goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (8.37 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT08TORVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.069); failure: TOR offense suppressed (<= 2 goals)
- **Darren Raddysh: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no; why: higher confidence-adjusted growth (6.89 vs 4.81 bp); relationships: KXNHLGOAL-26OCT08TORVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.069); failure: TOR offense succeeds (4+ goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.15, VGK shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis VGK:OFFENSE_4PLUS (p 0.5093): highest fidelity KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT08TORVGK-VGKSTHEODORE27-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.5076): highest fidelity KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:OFFENSE_4PLUS (p 0.2861): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT08TORVGK-VGKMGATCOMB17-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2885, phi -0.167)
- KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2885, phi -0.115)
- KXNHLGOAL-26OCT08TORVGK-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.5076, phi -0.177)
- KXNHLAST-26OCT08TORVGK-TORDRADDYSH43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2861, phi -0.26)

portfolios: A EV +1.88 (adj +0.62) on $15.00, P(profit) 0.6686, adj growth 5.9 bp · B EV +3.28 (adj +1.84) on $16.16, P(profit) 0.314, adj growth 17.2 bp · C EV +2.31 (adj +0.83) on $15.66, P(profit) 0.7212, adj growth 7.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
