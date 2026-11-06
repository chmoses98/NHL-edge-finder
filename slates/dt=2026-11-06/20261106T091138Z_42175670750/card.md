# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-06T09:11:38Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 140.00 | +18.95 | +5.00 | +6.13 | 0.585 | -81.54 | -86.28 | 20.87 |
| B thesis-diversified (joint) ← optimiser card | 35.98 | +3.47 | +1.12 | +11.74 | 0.508 | -13.01 | -30.93 | 9.92 |
| C best expression per thesis | 37.83 | +4.50 | +1.46 | +11.59 | 0.630 | -14.87 | -37.83 | 12.73 |
| R FUNDED research stakes | 11.00 | +1.10 | +0.35 | +2.78 | 0.614 | -4.62 | -9.58 | 0.00 |

## CBJ @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_CBJ_win | p_overtime | goals | shots BUF/CBJ | BUF/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.56 | 0.44 | 0.00 | 6.01 | 27.5/27.5 | 24.2/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.51 | 0.49 | 0.50 | 5.95 | 27.8/27.7 | 24.3/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.53 | 0.47 | 0.00 | 9.21 | 29.0/29.1 | 23.4/22.6 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.081 | 0.62 | 0.38 | 0.00 | 6.06 | 32.5/22.0 | 19.1/28.0 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.53 | 0.47 | 0.47 | 5.88 | 32.9/22.0 | 18.9/29.6 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.056 | 0.49 | 0.51 | 0.00 | 6.07 | 22.0/32.4 | 28.7/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Buffalo wins by over 1.5 goals NO | 61 | 0.689 | 0.647 | +0.062 | +0.020 | $14.39 | FUNDED_RESEARCH | $4 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Buffalo wins by over 1.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV06CBJBUF-BUF3|no; why: higher confidence-adjusted growth (3.88 vs 1.98 bp); relationships: only recommended bet in this game; failure: BUF wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:WINS (p 0.4663): highest fidelity KXNHLSPREAD-26NOV06CBJBUF-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06CBJBUF-BUF2|no (same contract)
- KXNHLSPREAD-26NOV06CBJBUF-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.311, phi -1.0)

portfolios: A EV +3.17 (adj +0.99) on $40.00, P(profit) 0.689, adj growth 7.0 bp · B EV +1.43 (adj +0.47) on $14.39, P(profit) 0.689, adj growth 4.1 bp · C EV +1.43 (adj +0.47) on $14.39, P(profit) 0.689, adj growth 4.1 bp · R EV +0.40 (adj +0.13) on $4.00, P(profit) 0.689, adj growth 4.5 bp

## SJS @ MIN  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_SJS_win | p_overtime | goals | shots MIN/SJS | MIN/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.68 | 0.32 | 0.00 | 6.07 | 28.6/28.2 | 25.3/24.1 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.109 | 0.70 | 0.30 | 0.00 | 5.99 | 33.6/22.1 | 19.5/28.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.53 | 0.47 | 0.49 | 5.96 | 28.5/28.2 | 24.9/25.1 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.57 | 0.43 | 0.47 | 5.93 | 34.0/22.3 | 19.1/30.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.66 | 0.34 | 0.00 | 9.34 | 30.4/29.8 | 24.7/23.2 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.080 | 0.72 | 0.28 | 0.00 | 9.31 | 35.8/23.7 | 19.2/27.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Minnesota wins by over 2.5 goals NO | 66 | 0.739 | 0.697 | +0.064 | +0.021 | $16.73 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| San Jose over 3.5 goals scored YES | 26 | 0.320 | 0.285 | +0.046 | +0.011 | $1.30 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Minnesota wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV06SJMIN-MIN2|no; why: higher confidence-adjusted growth (4.61 vs 2.19 bp); despite a smaller raw edge (+0.064 vs +0.087/contract); wins across more scripts (relative breadth 1.012 vs 0.874); relationships: KXNHLTEAMTOTAL-26NOV06SJMIN-SJ4|yes: REINFORCING (phi 0.342); failure: MIN wins by 2+
- **San Jose over 3.5 goals scored YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV06SJMIN-MIN3|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV06SJMIN-MIN3|no has the higher standalone adjusted growth (4.61 vs 1.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.342); they share one thesis budget; relationships: KXNHLSPREAD-26NOV06SJMIN-MIN3|no: REINFORCING (phi 0.342); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:TIGHT (p 0.4229): highest fidelity KXNHLSPREAD-26NOV06SJMIN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06SJMIN-MIN3|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3101): highest fidelity KXNHLTEAMTOTAL-26NOV06SJMIN-SJ4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06SJMIN-MIN3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV06SJMIN-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3856, phi -0.75)
- KXNHLTEAMTOTAL-26NOV06SJMIN-SJ4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis SJS:SUPPRESSED (p 0.4686, phi -0.643)

portfolios: A EV +7.02 (adj +1.69) on $50.00, P(profit) 0.6399, adj growth 7.8 bp · B EV +1.79 (adj +0.58) on $18.03, P(profit) 0.7393, adj growth 5.1 bp · C EV +1.68 (adj +0.57) on $17.88, P(profit) 0.7393, adj growth 5.0 bp · R EV +0.64 (adj +0.20) on $6.00, P(profit) 0.7393, adj growth 6.6 bp

## ANA @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_ANA_win | p_overtime | goals | shots CGY/ANA | CGY/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.45 | 0.55 | 0.00 | 6.05 | 28.4/28.5 | 24.6/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.115 | 0.41 | 0.58 | 0.00 | 9.41 | 30.1/30.4 | 23.7/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.47 | 6.01 | 28.6/28.8 | 25.5/25.2 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.090 | 0.40 | 0.60 | 0.00 | 5.99 | 22.6/34.0 | 29.7/19.6 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.081 | 0.34 | 0.66 | 0.00 | 9.47 | 24.1/35.8 | 28.1/19.0 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.44 | 0.56 | 0.49 | 6.02 | 22.9/34.5 | 30.9/19.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Calgary wins by over 1.5 goals NO | 69 | 0.753 | 0.719 | +0.048 | +0.014 | $3.56 | FUNDED_RESEARCH | $1 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Calgary wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV06ANACGY-ANA3|yes; why: KXNHLSPREAD-26NOV06ANACGY-ANA3|yes has the higher standalone adjusted growth (3.32 vs 2.03 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.309); relationships: only recommended bet in this game; failure: CGY wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis ANA:WINS_BY_2PLUS (p 0.3381): highest fidelity KXNHLSPREAD-26NOV06ANACGY-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV06ANACGY-ANA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:OFFENSE_4PLUS (p 0.476): highest fidelity KXNHLTEAMTOTAL-26NOV06ANACGY-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV06ANACGY-ANA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5534): highest fidelity KXNHLSPREAD-26NOV06ANACGY-CGY2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV06ANACGY-ANA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV06ANACGY-CGY2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:WINS_BY_2PLUS (p 0.2473, phi -1.0)

portfolios: A EV +8.76 (adj +2.32) on $50.00, P(profit) 0.4125, adj growth 6.0 bp · B EV +0.24 (adj +0.07) on $3.56, P(profit) 0.7527, adj growth 0.7 bp · C EV +1.39 (adj +0.42) on $5.56, P(profit) 0.3484, adj growth 3.6 bp · R EV +0.07 (adj +0.02) on $1.00, P(profit) 0.7527, adj growth 0.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
