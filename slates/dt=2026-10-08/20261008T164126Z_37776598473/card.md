# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-08T16:41:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +31.51 | +10.00 | +29.71 | 0.796 | -15.65 | -27.63 | 92.75 |
| B thesis-diversified (joint) ← optimiser card | 149.06 | +25.04 | +11.38 | +22.95 | 0.765 | -16.81 | -27.43 | 108.15 |
| C best expression per thesis | 150.00 | +25.85 | +11.83 | +23.41 | 0.739 | -22.32 | -33.53 | 110.97 |
| R FUNDED research stakes | 19.00 | +2.53 | +1.26 | +1.81 | 0.622 | -5.47 | -7.44 | 0.00 |

## UTA @ BOS  ·  10000 joint draws  ·  170 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.466 / away 0.534

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
| Boston over 3.5 goals scored YES | 36 | 0.425 | 0.390 | +0.049 | +0.014 | $1.70 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Full Game: Over 6.5 goals scored YES | 43 | 0.493 | 0.459 | +0.046 | +0.012 | $1.31 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Boston over 3.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08UTABOS-7|yes; why: higher confidence-adjusted growth (1.79 vs 1.29 bp); relationships: KXNHLTOTAL-26OCT08UTABOS-7|yes: REINFORCING (phi 0.463); failure: BOS offense suppressed (<= 2 goals)
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes has the higher standalone adjusted growth (1.79 vs 1.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.463); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes: REINFORCING (phi 0.463); failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.4143): highest fidelity KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.2919): highest fidelity KXNHLTOTAL-26OCT08UTABOS-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT08UTABOS-BOS4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.3673, phi -0.655)
- KXNHLTOTAL-26OCT08UTABOS-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.2096, phi -0.508)

portfolios: A EV +1.41 (adj +0.39) on $12.13, P(profit) 0.5943, adj growth 3.1 bp · B EV +0.36 (adj +0.10) on $3.00, P(profit) 0.425, adj growth 0.9 bp · C EV +0.35 (adj +0.10) on $2.69, P(profit) 0.425, adj growth 0.9 bp · R EV +0.23 (adj +0.06) on $2.00, P(profit) 0.5943, adj growth 2.2 bp

## DAL @ BUF  ·  10000 joint draws  ·  328 bet sides mapped, 7 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.479 / away 0.521

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_DAL_win | p_overtime | goals | shots BUF/DAL | BUF/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.55 | 0.45 | 0.00 | 6.03 | 26.5/26.3 | 23.0/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.51 | 0.49 | 0.47 | 5.95 | 26.8/26.3 | 23.0/23.5 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.089 | 0.62 | 0.38 | 0.00 | 6.01 | 31.4/21.2 | 18.3/27.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.55 | 0.45 | 0.00 | 9.3 | 28.0/27.9 | 22.3/22.0 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.56 | 0.44 | 0.48 | 5.87 | 31.5/20.9 | 17.8/28.2 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.056 | 0.60 | 0.40 | 0.00 | 9.13 | 33.3/22.4 | 17.7/26.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Justin Danforth: 1+ goals YES | 7 | 0.119 | 0.102 | +0.044 | +0.027 | $2.39 | FUNDED_RESEARCH | $1 | BUF:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Jiri Kulich: 1+ goals YES | 15 | 0.211 | 0.193 | +0.052 | +0.034 | $3.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Peyton Krebs: 1+ goals YES | 12 | 0.157 | 0.143 | +0.030 | +0.015 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Justin Danforth: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes; why: higher confidence-adjusted growth (22.32 vs 18.57 bp); despite a smaller raw edge (+0.044 vs +0.052/contract); relationships: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: BUF offense suppressed (<= 2 goals)
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes; why: higher confidence-adjusted growth (18.57 vs 4.59 bp); relationships: KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: BUF offense suppressed (<= 2 goals)
- **Peyton Krebs: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes has the higher standalone adjusted growth (18.57 vs 4.59 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.09.
- thesis BUF:OFFENSE_4PLUS (p 0.4055): highest fidelity KXNHLGOAL-26OCT08DALBUF-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.4346): highest fidelity KXNHLGOAL-26OCT08DALBUF-DALMRANTANEN96-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08DALBUF-DALMRANTANEN96-1|no (same contract)
- KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3795, phi -0.169)
- KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3795, phi -0.218)
- KXNHLGOAL-26OCT08DALBUF-BUFPKREBS19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3795, phi -0.192)

portfolios: A EV +4.06 (adj +2.48) on $15.32, P(profit) 0.4104, adj growth 22.9 bp · B EV +3.00 (adj +1.85) on $7.70, P(profit) 0.4104, adj growth 17.4 bp · C EV +1.73 (adj +1.11) on $10.81, P(profit) 0.2106, adj growth 10.3 bp · R EV +0.59 (adj +0.36) on $1.00, P(profit) 0.1188, adj growth 13.0 bp

## NSH @ MTL  ·  10000 joint draws  ·  324 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.597 / away 0.403

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
| Josh Anderson: 1+ goals YES | 13 | 0.180 | 0.164 | +0.042 | +0.026 | $2.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 24 | 0.295 | 0.280 | +0.043 | +0.028 | $3.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Jake Evans: 1+ goals YES | 12 | 0.158 | 0.147 | +0.031 | +0.020 | $2.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Nils Hoglander: 1+ goals NO | 80 | 0.842 | 0.830 | +0.031 | +0.019 | $8.21 | FUNDED_RESEARCH | $3 | NSH:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (12.06 vs 7.70 bp); relationships: KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT08NSHMTL-NSHNHOGLANDER21-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: MTL offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes; why: higher confidence-adjusted growth (8.75 vs 5.25 bp); despite a smaller raw edge (+0.043 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08NSHMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT08NSHMTL-NSHNHOGLANDER21-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: NSH offense suppressed (<= 2 goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLPTS-26OCT08NSHMTL-MTLCCAUFIELD13-3|yes; why: higher confidence-adjusted growth (7.70 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; wins across more scripts (relative breadth 0.859 vs 0.641); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT08NSHMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT08NSHMTL-NSHNHOGLANDER21-1|no: MOSTLY_INDEPENDENT (phi 0.031); failure: MTL offense suppressed (<= 2 goals)
- **Nils Hoglander: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08NSHMTL-NSHRJOSI59-1|no; why: higher confidence-adjusted growth (5.23 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT08NSHMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.031); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis NSH:OFFENSE_4PLUS (p 0.3715): highest fidelity KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:OFFENSE_4PLUS (p 0.4642): highest fidelity KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes (same contract)
- thesis MTL:WINS_BY_2PLUS (p 0.3424): highest fidelity KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes (same contract)
- KXNHLGOAL-26OCT08NSHMTL-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3251, phi -0.174)
- KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4098, phi -0.242)
- KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3251, phi -0.184)
- KXNHLGOAL-26OCT08NSHMTL-NSHNHOGLANDER21-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3715, phi -0.193)

portfolios: A EV +3.12 (adj +1.40) on $15.32, P(profit) 0.5373, adj growth 13.0 bp · B EV +2.31 (adj +1.46) on $16.86, P(profit) 0.472, adj growth 13.8 bp · C EV +1.81 (adj +1.01) on $10.28, P(profit) 0.4078, adj growth 9.4 bp · R EV +0.11 (adj +0.07) on $3.00, P(profit) 0.842, adj growth 2.7 bp

## PHI @ OTT  ·  10000 joint draws  ·  416 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.610 / away 0.390

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_PHI_win | p_overtime | goals | shots OTT/PHI | OTT/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.131 | 0.69 | 0.31 | 0.00 | 5.98 | 32.4/20.4 | 17.8/27.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.53 | 0.47 | 0.46 | 5.84 | 32.0/20.4 | 17.2/28.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.59 | 0.41 | 0.00 | 5.99 | 26.6/26.0 | 22.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.50 | 0.50 | 0.46 | 5.83 | 26.8/26.0 | 22.9/23.7 | even strength |
| OTT shot control · low event (<=4) · tight (1-goal/OT) | 0.074 | 0.56 | 0.44 | 0.51 | 2.81 | 30.6/19.2 | 17.7/29.2 | even strength |
| OTT shot control · low event (<=4) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 3.48 | 30.5/19.1 | 17.8/28.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Eklund: 1+ assists NO | 62 | 0.782 | 0.670 | +0.145 | +0.034 | $6.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Carter Yakemchuk: 1+ assists NO | 63 | 0.763 | 0.670 | +0.117 | +0.024 | $5.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Nick Cousins: 1+ goals YES | 8 | 0.110 | 0.097 | +0.025 | +0.012 | $1.27 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 13 | 0.162 | 0.153 | +0.024 | +0.015 | $1.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (10.71 vs 5.39 bp); relationships: KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: OTT offense succeeds (4+ goals)
- **Carter Yakemchuk: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08PHIOTT-OTTDBATHERSON19-1|no; why: higher confidence-adjusted growth (5.39 vs 1.51 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.043); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: OTT offense succeeds (4+ goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (4.17 vs 1.01 bp); despite a smaller raw edge (+0.025 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.043); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: OTT offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08PHIOTT-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (4.00 vs 1.47 bp); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis OTT:SUPPRESSED (p 0.3786): highest fidelity KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.2804): highest fidelity KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.3981): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.2 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3981, phi -0.187)
- KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3981, phi -0.221)
- KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3786, phi -0.146)
- KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.5085, phi -0.21)

portfolios: A EV +3.24 (adj +1.00) on $15.32, P(profit) 0.7038, adj growth 9.5 bp · B EV +3.19 (adj +0.92) on $15.23, P(profit) 0.6968, adj growth 8.8 bp · C EV +2.15 (adj +0.58) on $11.96, P(profit) 0.8019, adj growth 5.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ TBL  ·  10000 joint draws  ·  406 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.564 / away 0.436

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
| Ilya Mikheyev: 1+ goals YES | 15 | 0.199 | 0.186 | +0.040 | +0.027 | $3.20 | FUNDED_RESEARCH | $1 | TBL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 18 | 0.231 | 0.217 | +0.041 | +0.027 | $3.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| John Carlson: 1+ assists NO | 58 | 0.724 | 0.627 | +0.127 | +0.030 | $8.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ assists NO | 40 | 0.491 | 0.443 | +0.075 | +0.026 | $4.08 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
- **Ilya Mikheyev: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08MINTB-9|yes; why: higher confidence-adjusted growth (11.44 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.908 vs 0.371); alternative not eligible: confidence-adjusted EV +0.0009 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: INTENTIONAL_DIVERSIFIER (phi -0.055); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.047); failure: TBL offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT08MINTB-MIN2|yes; why: higher confidence-adjusted growth (9.97 vs 1.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.926 vs 0.549); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: MIN offense suppressed (<= 2 goals)
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (8.20 vs 6.28 bp); relationships: KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.055); KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.12); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no; why: second expression of the same thesis: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no has the higher standalone adjusted growth (8.20 vs 6.28 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.120); they share one thesis budget; relationships: KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.047); KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.12); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis TBL:OFFENSE_4PLUS (p 0.4069): highest fidelity KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.3752): highest fidelity KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.3786): highest fidelity KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3786, phi -0.206)
- KXNHLGOAL-26OCT08MINTB-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4041, phi -0.224)
- KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.9 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4069, phi -0.244)
- KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4069, phi -0.319)

portfolios: A EV +2.15 (adj +0.61) on $15.32, P(profit) 0.6076, adj growth 5.8 bp · B EV +3.95 (adj +1.64) on $18.60, P(profit) 0.5981, adj growth 15.6 bp · C EV +4.55 (adj +1.89) on $24.35, P(profit) 0.6494, adj growth 17.7 bp · R EV +0.25 (adj +0.17) on $1.00, P(profit) 0.1991, adj growth 6.2 bp

## VAN @ CAR  ·  10000 joint draws  ·  430 bet sides mapped, 33 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.741 / away 0.259

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
| Andrei Svechnikov: 1+ goals NO | 63 | 0.698 | 0.680 | +0.052 | +0.033 | $8.21 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 46 | 0.607 | 0.508 | +0.130 | +0.031 | $3.02 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 59 | 0.728 | 0.635 | +0.121 | +0.028 | $3.84 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Andrei Svechnikov: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: Player prop expression KXNHLGOAL-26OCT08VANCAR-CARASVECHNIKOV37-1|no selected over player prop KXNHLAST-26OCT08VANCAR-CARSAHO20-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26OCT08VANCAR-CAR2|no: REINFORCING (phi 0.169); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: REINFORCING (phi 0.162); failure: CAR offense succeeds (4+ goals)
- **Carolina wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes; why: Broad expression KXNHLSPREAD-26OCT08VANCAR-CAR2|no selected over broad KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT08VANCAR-CARASVECHNIKOV37-1|no: REINFORCING (phi 0.169); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: DUPLICATIVE (phi 0.76); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes; why: KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes has the higher standalone adjusted growth (8.89 vs 7.31 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.399); relationships: KXNHLGOAL-26OCT08VANCAR-CARASVECHNIKOV37-1|no: REINFORCING (phi 0.162); KXNHLSPREAD-26OCT08VANCAR-CAR2|no: DUPLICATIVE (phi 0.76); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · high event (8+) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14.
- thesis VAN:OFFENSE_4PLUS (p 0.3393): highest fidelity KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08VANCAR-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.1989): highest fidelity KXNHLGAME-26OCT08VANCAR-VAN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT08VANCAR-VAN|yes (same contract)
- thesis VAN:WINS (p 0.392): highest fidelity KXNHLGAME-26OCT08VANCAR-VAN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT08VANCAR-VAN|yes (same contract)
- KXNHLGOAL-26OCT08VANCAR-CARASVECHNIKOV37-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4945, phi -0.221)
- KXNHLSPREAD-26OCT08VANCAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.2 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3928, phi -1.0)
- KXNHLSPREAD-26OCT08VANCAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.3 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3928, phi -0.76)
- override: Broad expression KXNHLSPREAD-26OCT08VANCAR-CAR2|no selected over broad KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Player prop expression KXNHLGOAL-26OCT08VANCAR-CARASVECHNIKOV37-1|no selected over player prop KXNHLAST-26OCT08VANCAR-CARSAHO20-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.86 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.79 (adj +1.49) on $15.32, P(profit) 0.53, adj growth 13.7 bp · B EV +2.25 (adj +0.80) on $15.08, P(profit) 0.5413, adj growth 7.6 bp · C EV +5.03 (adj +2.70) on $13.84, P(profit) 0.337, adj growth 25.0 bp · R EV +0.71 (adj +0.27) on $5.00, P(profit) 0.5413, adj growth 10.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08VANCAR-CAR|no == KXNHLGAME-26OCT08VANCAR-VAN|yes

## CHI @ NYI  ·  10000 joint draws  ·  398 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.620 / away 0.380

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
| Ryan Greene: 1+ goals YES | 11 | 0.154 | 0.142 | +0.038 | +0.025 | $2.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 59 | 0.727 | 0.631 | +0.120 | +0.024 | $7.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Calum Ritchie: 1+ assists YES | 27 | 0.350 | 0.305 | +0.066 | +0.021 | $3.02 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Bo Horvat: 1+ goals NO | 62 | 0.672 | 0.658 | +0.036 | +0.021 | $6.39 | FUNDED_RESEARCH | $2 | NYI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08CHINYI-9|yes; why: higher confidence-adjusted growth (13.25 vs 0.01 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.938 vs 0.379); alternative not eligible: confidence-adjusted EV +0.0007 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08CHINYI-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (5.46 vs 0.30 bp); alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CHI offense succeeds (4+ goals)
- **Calum Ritchie: 1+ assists YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08CHINYI-NYIBSCHENN10-1|yes; why: higher confidence-adjusted growth (4.79 vs 0.23 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: INTENTIONAL_DIVERSIFIER (phi -0.071); failure: NYI offense suppressed (<= 2 goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08CHINYI-NYIVEKLUND73-1|no; why: higher confidence-adjusted growth (4.38 vs 0.15 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.071); failure: NYI offense succeeds (4+ goals)

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:SUPPRESSED (p 0.4838): highest fidelity KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.4651): highest fidelity KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes (same contract)
- thesis NYI:SUPPRESSED (p 0.3263): highest fidelity KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no (same contract)
- KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4838, phi -0.215)
- KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.7 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.2974, phi -0.251)
- KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3263, phi -0.257)
- KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.4651, phi -0.23)

portfolios: A EV +2.46 (adj +0.60) on $15.32, P(profit) 0.6376, adj growth 5.7 bp · B EV +3.44 (adj +1.33) on $19.73, P(profit) 0.7002, adj growth 12.6 bp · C EV +3.07 (adj +0.90) on $20.60, P(profit) 0.6425, adj growth 8.5 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.6723, adj growth 2.5 bp

## SJS @ STL  ·  10000 joint draws  ·  402 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.580 / away 0.420

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_SJS_win | p_overtime | goals | shots STL/SJS | STL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.59 | 0.41 | 0.00 | 6.01 | 26.4/26.4 | 23.4/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.49 | 5.94 | 26.9/26.7 | 23.5/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.61 | 0.39 | 0.00 | 9.44 | 28.1/28.0 | 22.7/21.0 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.090 | 0.66 | 0.34 | 0.00 | 6.0 | 31.2/20.7 | 18.1/27.0 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.60 | 0.40 | 0.50 | 5.86 | 31.9/21.3 | 18.2/28.4 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.065 | 0.62 | 0.38 | 0.00 | 9.26 | 33.1/22.4 | 17.6/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 1+ assists NO | 72 | 0.800 | 0.758 | +0.066 | +0.024 | $8.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Collin Graf: 1+ goals YES | 15 | 0.190 | 0.178 | +0.031 | +0.019 | $2.43 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Philip Broberg: 1+ goals YES | 7 | 0.099 | 0.087 | +0.025 | +0.012 | $1.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Mason McTavish: 1+ assists NO | 70 | 0.776 | 0.735 | +0.061 | +0.021 | $8.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no; why: higher confidence-adjusted growth (6.22 vs 4.47 bp); relationships: KXNHLGOAL-26OCT08SJSTL-SJCGRAF51-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.1); KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: SJS offense succeeds (4+ goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-8|yes; why: higher confidence-adjusted growth (6.17 vs 2.18 bp); despite a smaller raw edge (+0.031 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.899 vs 0.333); relationships: KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.1); KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: SJS offense suppressed (<= 2 goals)
- **Philip Broberg: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08SJSTL-STLPSUTER22-1|yes; why: higher confidence-adjusted growth (4.74 vs 3.48 bp); relationships: KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT08SJSTL-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.031); failure: STL offense suppressed (<= 2 goals)
- **Mason McTavish: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08SJSTL-STLAJIRICEK36-1|no; why: higher confidence-adjusted growth (4.62 vs 0.32 bp); alternative not eligible: confidence-adjusted EV +0.0055 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT08SJSTL-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.031); failure: STL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SJS:OFFENSE_4PLUS (p 0.3523): highest fidelity KXNHLTOTAL-26OCT08SJSTL-8|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT08SJSTL-SJCGRAF51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:SUPPRESSED (p 0.3373): highest fidelity KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no (same contract)
- thesis SJS:SUPPRESSED (p 0.4305): highest fidelity KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no (same contract)
- KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3523, phi -0.197)
- KXNHLGOAL-26OCT08SJSTL-SJCGRAF51-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4305, phi -0.231)
- KXNHLGOAL-26OCT08SJSTL-STLPBROBERG6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3373, phi -0.124)
- KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.45, phi -0.216)

portfolios: A EV +1.65 (adj +0.54) on $15.32, P(profit) 0.6751, adj growth 5.2 bp · B EV +2.33 (adj +1.01) on $20.13, P(profit) 0.7232, adj growth 9.6 bp · C EV +2.61 (adj +1.11) on $24.58, P(profit) 0.7223, adj growth 10.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ CGY  ·  10000 joint draws  ·  414 bet sides mapped, 35 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.325 / away 0.675

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
| Martin Necas: 1+ goals NO | 61 | 0.704 | 0.679 | +0.077 | +0.052 | $6.16 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 55 | 0.643 | 0.619 | +0.076 | +0.051 | $6.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Colorado wins by over 1.5 goals NO | 54 | 0.662 | 0.580 | +0.105 | +0.022 | $3.28 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Martin Necas: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (25.75 vs 23.77 bp); relationships: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26OCT08COLCGY-COL2|no: REINFORCING (phi 0.158); failure: COL offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no has the higher standalone adjusted growth (25.75 vs 23.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26OCT08COLCGY-COL2|no: REINFORCING (phi 0.223); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08COLCGY-COL3|no; why: Broad expression KXNHLSPREAD-26OCT08COLCGY-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT08COLCGY-CGY2|yes because adjusted EV is 0.5 pts higher while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: REINFORCING (phi 0.158); KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: REINFORCING (phi 0.223); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis COL:SUPPRESSED (p 0.3455): highest fidelity KXNHLTEAMTOTAL-26OCT08COLCGY-COL4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS (p 0.4308): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no — Broad expression KXNHLSPREAD-26OCT08COLCGY-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT08COLCGY-CGY2|yes because adjusted EV is 0.5 pts higher while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CGY:WINS_BY_2PLUS (p 0.225): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4359, phi -0.241)
- KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4359, phi -0.276)
- KXNHLSPREAD-26OCT08COLCGY-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.7 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3376, phi -1.0)
- override: Broad expression KXNHLSPREAD-26OCT08COLCGY-COL2|no selected over broad KXNHLTEAMTOTAL-26OCT08COLCGY-CGY2|yes because adjusted EV is 0.5 pts higher while thesis capture is 1.00 vs 0.98 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.86 (adj +0.94) on $15.32, P(profit) 0.756, adj growth 8.8 bp · B EV +2.20 (adj +1.20) on $15.59, P(profit) 0.7152, adj growth 11.7 bp · C EV +3.37 (adj +1.95) on $20.43, P(profit) 0.5363, adj growth 18.7 bp · R EV +0.43 (adj +0.21) on $3.00, P(profit) 0.7036, adj growth 8.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08COLCGY-COL|no == KXNHLGAME-26OCT08COLCGY-CGY|yes

## TOR @ VGK  ·  10000 joint draws  ·  446 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.602 / away 0.398

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
| Brayden McNabb: 1+ goals YES | 6 | 0.094 | 0.083 | +0.030 | +0.019 | $1.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ assists YES | 29 | 0.373 | 0.329 | +0.069 | +0.025 | $3.08 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
| Gavin McKenna: 1+ goals NO | 81 | 0.854 | 0.841 | +0.033 | +0.020 | $7.55 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ goals NO | 66 | 0.704 | 0.692 | +0.029 | +0.016 | $4.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (13.15 vs 6.19 bp); despite a smaller raw edge (+0.030 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.067); KXNHLGOAL-26OCT08TORVGK-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: VGK offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ assists YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08TORVGK-VGKMSTONE61-1|yes; why: higher confidence-adjusted growth (6.19 vs 1.18 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.067); KXNHLGOAL-26OCT08TORVGK-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: VGK offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (5.85 vs 2.65 bp); relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: TOR offense succeeds (4+ goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no; why: higher confidence-adjusted growth (2.65 vs 2.14 bp); despite a smaller raw edge (+0.029 vs +0.084/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT08TORVGK-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: TOR offense succeeds (4+ goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.15, VGK shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis VGK:OFFENSE_4PLUS (p 0.5116): highest fidelity KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.5003): highest fidelity KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2881, phi -0.118)
- KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2881, phi -0.246)
- KXNHLGOAL-26OCT08TORVGK-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2815, phi -0.179)
- KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2815, phi -0.274)

portfolios: A EV +1.77 (adj +0.55) on $15.32, P(profit) 0.6703, adj growth 5.2 bp · B EV +2.03 (adj +1.07) on $17.14, P(profit) 0.4084, adj growth 10.1 bp · C EV +1.19 (adj +0.48) on $10.46, P(profit) 0.3729, adj growth 4.5 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.854, adj growth 1.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
