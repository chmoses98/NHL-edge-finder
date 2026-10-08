# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-08T15:41:27Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +33.36 | +8.76 | +32.73 | 0.817 | -13.24 | -24.55 | 81.04 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +24.64 | +11.42 | +22.45 | 0.763 | -16.68 | -26.40 | 108.37 |
| C best expression per thesis | 150.02 | +28.05 | +12.69 | +25.59 | 0.737 | -23.89 | -36.89 | 118.03 |
| R FUNDED research stakes | 18.00 | +1.91 | +0.94 | +1.54 | 0.597 | -4.72 | -7.03 | 0.00 |

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
| Full Game: Over 6.5 goals scored YES | 43 | 0.497 | 0.461 | +0.050 | +0.014 | $2.46 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT08UTABOS-9|yes; why: higher confidence-adjusted growth (1.68 vs 1.47 bp); wins across more scripts (relative breadth 0.689 vs 0.378); alternative not eligible: confidence-adjusted EV +0.0100 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis GAME:HIGH_EVENT (p 0.2872): highest fidelity KXNHLTOTAL-26OCT08UTABOS-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT08UTABOS-7|yes (same contract)
- KXNHLTOTAL-26OCT08UTABOS-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.2121, phi -0.516)

portfolios: A EV +0.71 (adj +0.20) on $6.38, P(profit) 0.4969, adj growth 1.7 bp · B EV +0.27 (adj +0.08) on $2.46, P(profit) 0.4969, adj growth 0.7 bp · C EV +0.38 (adj +0.10) on $3.38, P(profit) 0.4969, adj growth 1.0 bp · R EV +0.11 (adj +0.03) on $1.00, P(profit) 0.4969, adj growth 1.1 bp

## DAL @ BUF  ·  10000 joint draws  ·  328 bet sides mapped, 6 +EV candidates, 4 on card


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
| Justin Danforth: 1+ goals YES | 7 | 0.119 | 0.102 | +0.044 | +0.027 | $2.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Jiri Kulich: 1+ goals YES | 15 | 0.211 | 0.194 | +0.052 | +0.035 | $3.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Miro Heiskanen: 1+ goals NO | 87 | 0.900 | 0.891 | +0.022 | +0.013 | $7.95 | FUNDED_RESEARCH | $2 | DAL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 22 | 0.256 | 0.245 | +0.024 | +0.013 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Justin Danforth: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes; why: higher confidence-adjusted growth (22.32 vs 19.94 bp); despite a smaller raw edge (+0.044 vs +0.052/contract); relationships: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT08DALBUF-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT08DALBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: BUF offense suppressed (<= 2 goals)
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (19.94 vs 2.21 bp); relationships: KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26OCT08DALBUF-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT08DALBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: BUF offense suppressed (<= 2 goals)
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08DALBUF-DALMRANTANEN96-1|no; why: higher confidence-adjusted growth (3.75 vs 1.70 bp); despite a smaller raw edge (+0.022 vs +0.026/contract); relationships: KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT08DALBUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: DAL offense succeeds (4+ goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes has the higher standalone adjusted growth (19.94 vs 2.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT08DALBUF-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.09.
- thesis BUF:OFFENSE_4PLUS (p 0.4055): highest fidelity KXNHLAST-26OCT08DALBUF-BUFOPOWER25-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.4346): highest fidelity KXNHLGOAL-26OCT08DALBUF-DALMRANTANEN96-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08DALBUF-DALMRANTANEN96-1|no (same contract)
- KXNHLGOAL-26OCT08DALBUF-BUFJDANFORTH15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3795, phi -0.169)
- KXNHLGOAL-26OCT08DALBUF-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3795, phi -0.218)
- KXNHLGOAL-26OCT08DALBUF-DALMHEISKANEN4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.3444, phi -0.146)
- KXNHLGOAL-26OCT08DALBUF-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3795, phi -0.214)

portfolios: A EV +3.77 (adj +2.12) on $15.96, P(profit) 0.4873, adj growth 19.6 bp · B EV +3.00 (adj +1.91) on $15.84, P(profit) 0.4637, adj growth 18.0 bp · C EV +1.94 (adj +1.28) on $11.44, P(profit) 0.2106, adj growth 11.8 bp · R EV +0.05 (adj +0.03) on $2.00, P(profit) 0.9002, adj growth 1.2 bp

## NSH @ MTL  ·  10000 joint draws  ·  326 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_NSH_win | p_overtime | goals | shots MTL/NSH | MTL/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.61 | 0.39 | 0.00 | 6.07 | 27.8/27.8 | 24.6/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.56 | 0.44 | 0.47 | 5.97 | 28.1/28.2 | 24.8/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.59 | 0.41 | 0.00 | 9.41 | 29.4/29.5 | 24.1/22.6 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.068 | 0.64 | 0.36 | 0.00 | 6.07 | 32.4/21.9 | 19.0/27.9 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.067 | 0.52 | 0.48 | 0.00 | 6.04 | 22.1/32.7 | 29.0/18.8 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.52 | 0.48 | 0.44 | 6.01 | 22.4/32.9 | 29.7/19.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan O'Reilly: 1+ goals YES | 24 | 0.296 | 0.281 | +0.044 | +0.028 | $3.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Jake Evans: 1+ goals YES | 12 | 0.156 | 0.146 | +0.029 | +0.019 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Nils Hoglander: 1+ goals NO | 81 | 0.844 | 0.834 | +0.023 | +0.013 | $7.01 | FUNDED_RESEARCH | $2 | NSH:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ assists NO | 69 | 0.796 | 0.718 | +0.091 | +0.013 | $5.32 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes; why: higher confidence-adjusted growth (9.18 vs 1.85 bp); despite a smaller raw edge (+0.044 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT08NSHMTL-NSHNHOGLANDER21-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT08NSHMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: NSH offense suppressed (<= 2 goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLAST-26OCT08NSHMTL-NSHRJOSI59-1|no; why: higher confidence-adjusted growth (6.70 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT08NSHMTL-NSHNHOGLANDER21-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLAST-26OCT08NSHMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.025); failure: MTL offense suppressed (<= 2 goals)
- **Nils Hoglander: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08NSHMTL-NSHRJOSI59-1|no; why: higher confidence-adjusted growth (2.69 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLAST-26OCT08NSHMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: NSH offense succeeds (4+ goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08NSHMTL-MTLNSUZUKI14-1|no; why: higher confidence-adjusted growth (1.65 vs 0.91 bp); relationships: KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT08NSHMTL-NSHNHOGLANDER21-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis NSH:OFFENSE_4PLUS (p 0.3678): highest fidelity KXNHLAST-26OCT08NSHMTL-NSHJMARCHESSAULT81-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.327): highest fidelity KXNHLAST-26OCT08NSHMTL-MTLNSUZUKI14-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08NSHMTL-MTLNSUZUKI14-1|no (same contract)
- thesis MTL:WINS_BY_2PLUS (p 0.3401): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT08NSHMTL-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4153, phi -0.244)
- KXNHLGOAL-26OCT08NSHMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.327, phi -0.186)
- KXNHLGOAL-26OCT08NSHMTL-NSHNHOGLANDER21-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3678, phi -0.171)
- KXNHLAST-26OCT08NSHMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4669, phi -0.186)

portfolios: A EV +2.87 (adj +0.73) on $15.96, P(profit) 0.4823, adj growth 6.6 bp · B EV +1.98 (adj +0.91) on $18.00, P(profit) 0.3987, adj growth 8.6 bp · C EV +1.16 (adj +0.62) on $7.47, P(profit) 0.2964, adj growth 5.7 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.8439, adj growth 1.2 bp

## PHI @ OTT  ·  10000 joint draws  ·  420 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_PHI_win | p_overtime | goals | shots OTT/PHI | OTT/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.134 | 0.66 | 0.34 | 0.00 | 5.96 | 31.8/20.4 | 17.6/27.5 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.56 | 0.44 | 0.44 | 5.81 | 32.0/20.7 | 17.7/28.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.62 | 0.38 | 0.00 | 5.98 | 26.6/26.0 | 23.0/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.51 | 0.49 | 0.46 | 5.87 | 26.7/26.0 | 22.8/23.4 | even strength |
| OTT shot control · low event (<=4) · decided (2+) | 0.078 | 0.69 | 0.31 | 0.00 | 3.42 | 31.0/19.5 | 18.2/28.4 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.074 | 0.70 | 0.30 | 0.00 | 9.11 | 33.8/21.9 | 17.5/26.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Eklund: 1+ assists NO | 62 | 0.785 | 0.671 | +0.148 | +0.035 | $5.97 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Sean Couturier: 1+ goals YES | 11 | 0.148 | 0.136 | +0.031 | +0.019 | $1.95 | FUNDED_RESEARCH | $1 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 8 | 0.114 | 0.101 | +0.028 | +0.016 | $1.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Carter Yakemchuk: 1+ assists NO | 64 | 0.770 | 0.682 | +0.114 | +0.026 | $5.97 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (11.46 vs 6.70 bp); relationships: KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.062); failure: OTT offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08PHIOTT-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (7.58 vs 2.51 bp); relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: PHI offense suppressed (<= 2 goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (7.24 vs 1.51 bp); despite a smaller raw edge (+0.028 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.039); failure: OTT offense suppressed (<= 2 goals)
- **Carter Yakemchuk: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT08PHIOTT-OTTWEKLUND27-1|no; why: higher confidence-adjusted growth (6.70 vs 1.08 bp); despite a smaller raw edge (+0.114 vs +0.127/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.062); KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.039); failure: OTT offense succeeds (4+ goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.2864): highest fidelity KXNHLGOAL-26OCT08PHIOTT-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:SUPPRESSED (p 0.373): highest fidelity KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4048): highest fidelity KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT08PHIOTT-OTTJSPENCE10-1|yes (same contract)
- KXNHLAST-26OCT08PHIOTT-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.5 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4048, phi -0.191)
- KXNHLGOAL-26OCT08PHIOTT-PHISCOUTURIER14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.5074, phi -0.213)
- KXNHLGOAL-26OCT08PHIOTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.373, phi -0.153)
- KXNHLAST-26OCT08PHIOTT-OTTCYAKEMCHUK26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.5 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4048, phi -0.213)

portfolios: A EV +3.64 (adj +0.54) on $15.96, P(profit) 0.608, adj growth 5.0 bp · B EV +3.48 (adj +1.19) on $15.49, P(profit) 0.7115, adj growth 11.4 bp · C EV +3.03 (adj +0.98) on $15.85, P(profit) 0.8049, adj growth 9.1 bp · R EV +0.27 (adj +0.16) on $1.00, P(profit) 0.1479, adj growth 5.8 bp

## MIN @ TBL  ·  10000 joint draws  ·  404 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_MIN_win | p_overtime | goals | shots TBL/MIN | TBL/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.51 | 0.49 | 0.00 | 6.09 | 28.0/27.6 | 24.0/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.52 | 0.48 | 0.48 | 5.92 | 28.0/27.7 | 24.3/24.7 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.106 | 0.59 | 0.41 | 0.00 | 6.0 | 33.5/22.2 | 19.3/29.5 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.57 | 0.43 | 0.43 | 5.89 | 33.5/22.1 | 18.9/30.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.54 | 0.46 | 0.00 | 9.27 | 29.5/29.2 | 23.4/23.3 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.071 | 0.60 | 0.40 | 0.00 | 9.23 | 34.9/23.3 | 18.1/27.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ilya Mikheyev: 1+ goals YES | 15 | 0.200 | 0.186 | +0.042 | +0.028 | $3.33 | FUNDED_RESEARCH | $1 | TBL:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| John Carlson: 1+ assists NO | 58 | 0.725 | 0.627 | +0.128 | +0.030 | $7.87 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Michael McCarron: 1+ goals YES | 9 | 0.124 | 0.112 | +0.029 | +0.016 | $1.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ assists NO | 40 | 0.491 | 0.443 | +0.074 | +0.026 | $4.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
- **Ilya Mikheyev: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08MINTB-9|yes; why: higher confidence-adjusted growth (12.29 vs 0.30 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.858 vs 0.375); alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26OCT08MINTB-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.048); failure: TBL offense suppressed (<= 2 goals)
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (8.38 vs 6.19 bp); relationships: KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLGOAL-26OCT08MINTB-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.099); failure: TBL offense succeeds (4+ goals)
- **Michael McCarron: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08MINTB-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (6.49 vs 1.17 bp); alternative not eligible: confidence-adjusted EV +0.0098 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: MIN offense suppressed (<= 2 goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no; why: second expression of the same thesis: KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no has the higher standalone adjusted growth (8.38 vs 6.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.099); they share one thesis budget; relationships: KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.099); KXNHLGOAL-26OCT08MINTB-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.11.
- thesis TBL:OFFENSE_4PLUS (p 0.4153): highest fidelity KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes (same contract)
- thesis TBL:SUPPRESSED (p 0.377): highest fidelity KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.3717): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT08MINTB-TBIMIKHEYEV95-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.377, phi -0.212)
- KXNHLAST-26OCT08MINTB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.0 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4153, phi -0.227)
- KXNHLGOAL-26OCT08MINTB-MINMMCCARRON47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.4055, phi -0.166)
- KXNHLAST-26OCT08MINTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4153, phi -0.314)

portfolios: A EV +2.75 (adj +1.05) on $15.96, P(profit) 0.6027, adj growth 10.0 bp · B EV +3.75 (adj +1.51) on $16.87, P(profit) 0.5611, adj growth 14.3 bp · C EV +3.50 (adj +1.33) on $15.38, P(profit) 0.7932, adj growth 12.4 bp · R EV +0.26 (adj +0.17) on $1.00, P(profit) 0.2004, adj growth 6.4 bp

## VAN @ CAR  ·  10000 joint draws  ·  428 bet sides mapped, 34 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_VAN_win | p_overtime | goals | shots CAR/VAN | CAR/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.183 | 0.69 | 0.31 | 0.00 | 6.06 | 33.9/20.5 | 17.8/29.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.144 | 0.55 | 0.45 | 0.45 | 5.96 | 33.9/20.7 | 17.5/30.4 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.134 | 0.73 | 0.27 | 0.00 | 9.43 | 35.7/22.2 | 17.6/27.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.078 | 0.63 | 0.37 | 0.00 | 6.07 | 27.8/26.6 | 23.4/23.8 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.071 | 0.67 | 0.33 | 0.00 | 3.45 | 32.4/19.5 | 18.2/29.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.54 | 0.46 | 0.48 | 5.98 | 27.7/26.7 | 23.3/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 2.5 goals NO | 59 | 0.736 | 0.638 | +0.129 | +0.031 | $6.45 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikolaj Ehlers: 1+ goals NO | 70 | 0.760 | 0.742 | +0.045 | +0.028 | $6.45 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 64 | 0.701 | 0.685 | +0.045 | +0.029 | $5.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08VANCAR-CAR2|no; why: KXNHLSPREAD-26OCT08VANCAR-CAR2|no has the higher standalone adjusted growth (9.21 vs 8.83 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.751); relationships: KXNHLGOAL-26OCT08VANCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: REINFORCING (phi 0.156); failure: CAR wins by 2+
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes has the higher standalone adjusted growth (20.31 vs 8.30 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.111); relationships: KXNHLSPREAD-26OCT08VANCAR-CAR3|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: CAR offense succeeds (4+ goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: Player prop expression KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no selected over player prop KXNHLAST-26OCT08VANCAR-CARSAHO20-1|no because adjusted EV is 0.4 pts higher while thesis capture is 0.85 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26OCT08VANCAR-CAR3|no: REINFORCING (phi 0.156); KXNHLGOAL-26OCT08VANCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.18, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:OFFENSE_4PLUS (p 0.3383): highest fidelity KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08VANCAR-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.195): highest fidelity KXNHLSPREAD-26OCT08VANCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08VANCAR-CAR2|no (same contract)
- thesis VAN:WINS (p 0.3852): highest fidelity KXNHLSPREAD-26OCT08VANCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08VANCAR-CAR2|no (same contract)
- KXNHLSPREAD-26OCT08VANCAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.1 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3884, phi -0.751)
- KXNHLGOAL-26OCT08VANCAR-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.5027, phi -0.206)
- KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.5027, phi -0.231)
- override: Player prop expression KXNHLGOAL-26OCT08VANCAR-CARSAHO20-1|no selected over player prop KXNHLAST-26OCT08VANCAR-CARSAHO20-1|no because adjusted EV is 0.4 pts higher while thesis capture is 0.85 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.61 (adj +1.03) on $15.96, P(profit) 0.5315, adj growth 9.0 bp · B EV +2.16 (adj +0.82) on $18.38, P(profit) 0.6993, adj growth 7.9 bp · C EV +5.62 (adj +2.80) on $11.72, P(profit) 0.3305, adj growth 25.7 bp · R EV +0.55 (adj +0.18) on $4.00, P(profit) 0.5872, adj growth 6.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08VANCAR-CAR|no == KXNHLGAME-26OCT08VANCAR-VAN|yes

## CHI @ NYI  ·  10000 joint draws  ·  396 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CHI_win | p_overtime | goals | shots NYI/CHI | NYI/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NYI shot control · normal event (5-7) · decided (2+) | 0.134 | 0.72 | 0.28 | 0.00 | 6.03 | 33.3/21.2 | 18.7/28.5 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.58 | 0.42 | 0.47 | 5.92 | 33.4/21.3 | 18.1/29.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.67 | 0.33 | 0.00 | 6.02 | 27.6/26.9 | 24.2/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.51 | 0.49 | 0.46 | 5.91 | 27.6/26.9 | 23.6/24.3 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.089 | 0.71 | 0.29 | 0.00 | 9.22 | 34.6/22.4 | 18.1/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.67 | 0.33 | 0.00 | 9.31 | 29.2/28.3 | 23.1/21.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 11 | 0.157 | 0.144 | +0.040 | +0.027 | $2.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Calum Ritchie: 1+ assists YES | 27 | 0.351 | 0.306 | +0.068 | +0.022 | $3.03 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
| Patrick Kane: 1+ assists NO | 59 | 0.721 | 0.629 | +0.115 | +0.023 | $6.91 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Bo Horvat: 1+ goals NO | 62 | 0.673 | 0.658 | +0.036 | +0.022 | $6.30 | FUNDED_RESEARCH | $2 | NYI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08CHINYI-9|yes; why: higher confidence-adjusted growth (15.51 vs 0.14 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.953 vs 0.376); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: CHI offense suppressed (<= 2 goals)
- **Calum Ritchie: 1+ assists YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08CHINYI-9|yes; why: higher confidence-adjusted growth (5.16 vs 0.14 bp); wins across more scripts (relative breadth 0.884 vs 0.376); alternative not eligible: confidence-adjusted EV +0.0030 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.048); failure: NYI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08CHINYI-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (4.68 vs 0.18 bp); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.034); KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: CHI offense succeeds (4+ goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08CHINYI-NYIMMACCELLI63-1|no; why: higher confidence-adjusted growth (4.50 vs 0.07 bp); despite a smaller raw edge (+0.036 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0025 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: NYI offense succeeds (4+ goals)

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.13, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3014): highest fidelity KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.464): highest fidelity KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4848): highest fidelity KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26OCT08CHINYI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4848, phi -0.216)
- KXNHLAST-26OCT08CHINYI-NYICRITCHIE64-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3184, phi -0.242)
- KXNHLAST-26OCT08CHINYI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.1 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3014, phi -0.228)
- KXNHLGOAL-26OCT08CHINYI-NYIBHORVAT14-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.464, phi -0.236)

portfolios: A EV +3.37 (adj +1.20) on $15.96, P(profit) 0.433, adj growth 11.4 bp · B EV +3.37 (adj +1.38) on $19.09, P(profit) 0.6978, adj growth 13.0 bp · C EV +4.64 (adj +1.89) on $26.26, P(profit) 0.6978, adj growth 17.5 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.6727, adj growth 2.6 bp

## SJS @ STL  ·  10000 joint draws  ·  402 bet sides mapped, 7 +EV candidates, 4 on card


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
| Ivar Stenberg: 1+ assists NO | 72 | 0.799 | 0.757 | +0.065 | +0.023 | $7.95 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Collin Graf: 1+ goals YES | 15 | 0.192 | 0.177 | +0.033 | +0.018 | $2.01 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Mason McTavish: 1+ assists NO | 70 | 0.771 | 0.733 | +0.056 | +0.018 | $7.95 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Full Game: Over 7.5 goals scored YES | 23 | 0.284 | 0.255 | +0.042 | +0.012 | $1.91 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08SJSTL-SJMMARCHMENT27-1|no; why: higher confidence-adjusted growth (5.83 vs 2.22 bp); relationships: KXNHLGOAL-26OCT08SJSTL-SJCGRAF51-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.078); KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLTOTAL-26OCT08SJSTL-8|yes: INTENTIONAL_DIVERSIFIER (phi -0.123); failure: SJS offense succeeds (4+ goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-9|yes; why: higher confidence-adjusted growth (5.51 vs 1.97 bp); despite a smaller raw edge (+0.033 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.911 vs 0.374); relationships: KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.078); KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLTOTAL-26OCT08SJSTL-8|yes: INTENTIONAL_DIVERSIFIER (phi 0.133); failure: SJS offense suppressed (<= 2 goals)
- **Mason McTavish: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08SJSTL-STLAJIRICEK36-1|no; why: higher confidence-adjusted growth (3.61 vs 0.21 bp); alternative not eligible: confidence-adjusted EV +0.0044 below the 0.010/contract floor; relationships: KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT08SJSTL-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLTOTAL-26OCT08SJSTL-8|yes: INTENTIONAL_DIVERSIFIER (phi -0.181); failure: STL offense succeeds (4+ goals)
- **Full Game: Over 7.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-9|yes; why: Broad expression KXNHLTOTAL-26OCT08SJSTL-8|yes selected over broad KXNHLTOTAL-26OCT08SJSTL-9|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.73 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.123); KXNHLGOAL-26OCT08SJSTL-SJCGRAF51-1|yes: INTENTIONAL_DIVERSIFIER (phi 0.133); KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no: INTENTIONAL_DIVERSIFIER (phi -0.181); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.422): highest fidelity KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3571): highest fidelity KXNHLTOTAL-26OCT08SJSTL-7|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT08SJSTL-SJCGRAF51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:SUPPRESSED (p 0.3333): highest fidelity KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no (same contract)
- KXNHLAST-26OCT08SJSTL-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3571, phi -0.204)
- KXNHLGOAL-26OCT08SJSTL-SJCGRAF51-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.422, phi -0.204)
- KXNHLAST-26OCT08SJSTL-STLMMCTAVISH83-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4475, phi -0.212)
- KXNHLTOTAL-26OCT08SJSTL-8|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis SJS:SUPPRESSED (p 0.422, phi -0.4)
- override: Broad expression KXNHLTOTAL-26OCT08SJSTL-8|yes selected over broad KXNHLTOTAL-26OCT08SJSTL-9|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.73 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.42 (adj +0.42) on $15.96, P(profit) 0.7042, adj growth 4.1 bp · B EV +2.07 (adj +0.78) on $19.83, P(profit) 0.6978, adj growth 7.4 bp · C EV +2.83 (adj +1.07) on $26.52, P(profit) 0.7582, adj growth 10.1 bp · R EV +0.17 (adj +0.05) on $1.00, P(profit) 0.2839, adj growth 1.7 bp

## COL @ CGY  ·  10000 joint draws  ·  414 bet sides mapped, 33 +EV candidates, 2 on card


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
| Martin Necas: 1+ goals NO | 61 | 0.704 | 0.679 | +0.077 | +0.052 | $5.97 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ goals NO | 56 | 0.643 | 0.619 | +0.066 | +0.042 | $5.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Martin Necas: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (25.75 vs 15.58 bp); relationships: KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: COL offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no has the higher standalone adjusted growth (25.75 vs 15.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis COL:SUPPRESSED (p 0.3455): highest fidelity KXNHLPTS-26OCT08COLCGY-COLNMACKINNON29-3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:WINS (p 0.4308): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.3371): highest fidelity KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08COLCGY-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08COLCGY-COLMNECAS88-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4359, phi -0.241)
- KXNHLGOAL-26OCT08COLCGY-COLNMACKINNON29-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4359, phi -0.276)

portfolios: A EV +6.79 (adj +0.91) on $15.96, P(profit) 0.6542, adj growth 8.3 bp · B EV +1.42 (adj +0.93) on $11.93, P(profit) 0.4526, adj growth 9.1 bp · C EV +3.65 (adj +2.09) on $20.53, P(profit) 0.5611, adj growth 19.8 bp · R EV +0.25 (adj +0.17) on $2.00, P(profit) 0.7036, adj growth 6.5 bp

## TOR @ VGK  ·  10000 joint draws  ·  446 bet sides mapped, 11 +EV candidates, 4 on card


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
| Brayden McNabb: 1+ goals YES | 5 | 0.094 | 0.082 | +0.041 | +0.029 | $2.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Marc Gatcomb: 1+ goals YES | 11 | 0.146 | 0.135 | +0.029 | +0.018 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ assists YES | 29 | 0.373 | 0.329 | +0.069 | +0.025 | $2.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
| Auston Matthews: 1+ goals NO | 66 | 0.704 | 0.692 | +0.029 | +0.016 | $5.16 | FUNDED_RESEARCH | $2 | TOR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (33.59 vs 6.19 bp); despite a smaller raw edge (+0.041 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08TORVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.067); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: VGK offense suppressed (<= 2 goals)
- **Marc Gatcomb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (6.61 vs 6.19 bp); despite a smaller raw edge (+0.029 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: VGK offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ assists YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT08TORVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (6.19 vs 2.00 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.067); KXNHLGOAL-26OCT08TORVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: VGK offense suppressed (<= 2 goals)
- **Auston Matthews: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no; why: higher confidence-adjusted growth (2.65 vs 2.14 bp); despite a smaller raw edge (+0.029 vs +0.084/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT08TORVGK-VGKMGATCOMB17-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: TOR offense succeeds (4+ goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.15, VGK shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis VGK:OFFENSE_4PLUS (p 0.5116): highest fidelity KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.5003): highest fidelity KXNHLAST-26OCT08TORVGK-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT08TORVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2881, phi -0.118)
- KXNHLGOAL-26OCT08TORVGK-VGKMGATCOMB17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2881, phi -0.14)
- KXNHLAST-26OCT08TORVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2881, phi -0.246)
- KXNHLGOAL-26OCT08TORVGK-TORAMATTHEWS34-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2815, phi -0.274)

portfolios: A EV +2.44 (adj +0.56) on $15.96, P(profit) 0.6543, adj growth 5.3 bp · B EV +3.14 (adj +1.91) on $12.10, P(profit) 0.4245, adj growth 17.9 bp · C EV +1.31 (adj +0.53) on $11.47, P(profit) 0.3729, adj growth 4.9 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.7043, adj growth 1.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
