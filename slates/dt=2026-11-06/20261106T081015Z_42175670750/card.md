# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-06T08:10:15Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 125.84 | +16.47 | +4.60 | +15.44 | 0.518 | -69.03 | -96.24 | 20.30 |
| B thesis-diversified (joint) ← optimiser card | 35.05 | +3.40 | +1.10 | +12.67 | 0.508 | -12.08 | -31.31 | 9.75 |
| C best expression per thesis | 35.18 | +4.26 | +1.39 | +14.25 | 0.568 | -12.22 | -35.18 | 12.13 |
| R FUNDED research stakes | 11.00 | +1.10 | +0.35 | +2.78 | 0.614 | -4.62 | -9.58 | 0.00 |

## CBJ @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_CBJ_win | p_overtime | goals | shots BUF/CBJ | BUF/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.57 | 0.43 | 0.00 | 6.04 | 27.6/27.4 | 24.1/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.50 | 0.50 | 0.48 | 5.94 | 27.7/27.4 | 24.1/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.55 | 0.45 | 0.00 | 9.24 | 29.2/29.1 | 23.5/22.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.079 | 0.63 | 0.37 | 0.00 | 6.03 | 32.6/21.8 | 19.0/28.0 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.53 | 0.47 | 0.51 | 5.91 | 32.9/22.1 | 18.9/29.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.055 | 0.54 | 0.46 | 0.00 | 3.48 | 26.4/26.2 | 24.4/24.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Buffalo wins by over 1.5 goals NO | 61 | 0.689 | 0.647 | +0.062 | +0.020 | $14.39 | FUNDED_RESEARCH | $4 | CBJ:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Buffalo wins by over 1.5 goals NO** — thesis: CBJ wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV06CBJBUF-BUF3|no; why: higher confidence-adjusted growth (3.88 vs 1.98 bp); relationships: only recommended bet in this game; failure: BUF wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:WINS (p 0.4663): highest fidelity KXNHLSPREAD-26NOV06CBJBUF-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06CBJBUF-BUF2|no (same contract)
- KXNHLSPREAD-26NOV06CBJBUF-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.311, phi -1.0)

portfolios: A EV +3.17 (adj +0.99) on $40.00, P(profit) 0.689, adj growth 7.0 bp · B EV +1.43 (adj +0.47) on $14.39, P(profit) 0.689, adj growth 4.1 bp · C EV +1.43 (adj +0.47) on $14.39, P(profit) 0.689, adj growth 4.1 bp · R EV +0.40 (adj +0.13) on $4.00, P(profit) 0.689, adj growth 4.5 bp

## SJS @ MIN  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_SJS_win | p_overtime | goals | shots MIN/SJS | MIN/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.66 | 0.34 | 0.00 | 6.04 | 28.6/28.2 | 25.4/24.2 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.114 | 0.70 | 0.30 | 0.00 | 6.01 | 33.8/22.2 | 19.7/29.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.53 | 0.47 | 0.47 | 5.99 | 28.7/28.2 | 24.9/25.2 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.57 | 0.43 | 0.49 | 5.89 | 34.1/22.5 | 19.4/30.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.67 | 0.33 | 0.00 | 9.39 | 30.5/29.9 | 24.8/23.2 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.079 | 0.71 | 0.29 | 0.00 | 9.26 | 35.4/23.6 | 18.9/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Minnesota wins by over 2.5 goals NO | 66 | 0.739 | 0.697 | +0.064 | +0.021 | $16.73 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| San Jose over 3.5 goals scored YES | 26 | 0.320 | 0.285 | +0.046 | +0.011 | $1.30 | FUNDED_RESEARCH | $1 | SJS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Minnesota wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV06SJMIN-MIN2|no; why: higher confidence-adjusted growth (4.61 vs 0.72 bp); despite a smaller raw edge (+0.064 vs +0.077/contract); wins across more scripts (relative breadth 1.011 vs 0.876); alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLTEAMTOTAL-26NOV06SJMIN-SJ4|yes: REINFORCING (phi 0.342); failure: MIN wins by 2+
- **San Jose over 3.5 goals scored YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV06SJMIN-MIN3|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV06SJMIN-MIN3|no has the higher standalone adjusted growth (4.61 vs 1.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.342); they share one thesis budget; relationships: KXNHLSPREAD-26NOV06SJMIN-MIN3|no: REINFORCING (phi 0.342); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:TIGHT (p 0.4229): highest fidelity KXNHLSPREAD-26NOV06SJMIN-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06SJMIN-MIN3|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3101): highest fidelity KXNHLTEAMTOTAL-26NOV06SJMIN-SJ4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV06SJMIN-MIN3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV06SJMIN-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3856, phi -0.75)
- KXNHLTEAMTOTAL-26NOV06SJMIN-SJ4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis SJS:SUPPRESSED (p 0.4686, phi -0.643)

portfolios: A EV +4.55 (adj +1.29) on $35.84, P(profit) 0.3195, adj growth 7.2 bp · B EV +1.79 (adj +0.58) on $18.03, P(profit) 0.7393, adj growth 5.1 bp · C EV +1.68 (adj +0.57) on $17.88, P(profit) 0.7393, adj growth 5.0 bp · R EV +0.64 (adj +0.20) on $6.00, P(profit) 0.7393, adj growth 6.6 bp

## ANA @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_ANA_win | p_overtime | goals | shots CGY/ANA | CGY/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.44 | 0.56 | 0.00 | 6.03 | 28.5/28.8 | 25.0/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.114 | 0.41 | 0.59 | 0.00 | 9.51 | 30.3/30.5 | 23.5/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.49 | 0.51 | 0.46 | 6.01 | 28.6/28.9 | 25.6/25.3 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.091 | 0.39 | 0.61 | 0.00 | 5.99 | 22.6/34.0 | 29.8/19.6 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.084 | 0.34 | 0.66 | 0.00 | 9.4 | 24.3/35.8 | 27.9/19.3 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.44 | 0.56 | 0.48 | 5.97 | 23.0/34.5 | 31.2/19.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Calgary wins by over 1.5 goals NO | 69 | 0.753 | 0.719 | +0.048 | +0.014 | $2.63 | FUNDED_RESEARCH | $1 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Calgary wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV06ANACGY-ANA6|yes; why: KXNHLTEAMTOTAL-26NOV06ANACGY-ANA6|yes has the higher standalone adjusted growth (3.73 vs 2.03 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.229); relationships: only recommended bet in this game; failure: CGY wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:HIGH_EVENT (p 0.3378): highest fidelity KXNHLTOTAL-26NOV06ANACGY-8|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV06ANACGY-ANA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3381): highest fidelity KXNHLSPREAD-26NOV06ANACGY-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV06ANACGY-ANA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:OFFENSE_4PLUS (p 0.476): highest fidelity KXNHLTEAMTOTAL-26NOV06ANACGY-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV06ANACGY-ANA5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV06ANACGY-CGY2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:WINS_BY_2PLUS (p 0.2473, phi -1.0)

portfolios: A EV +8.76 (adj +2.32) on $50.00, P(profit) 0.4125, adj growth 6.0 bp · B EV +0.18 (adj +0.05) on $2.63, P(profit) 0.7527, adj growth 0.5 bp · C EV +1.15 (adj +0.35) on $2.91, P(profit) 0.1482, adj growth 3.0 bp · R EV +0.07 (adj +0.02) on $1.00, P(profit) 0.7527, adj growth 0.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
