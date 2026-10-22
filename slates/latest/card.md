# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-22T04:29:26Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +20.89 | +5.64 | +20.87 | 0.662 | -41.94 | -58.36 | 44.34 |
| B thesis-diversified (joint) ← optimiser card | 118.96 | +16.39 | +5.34 | +15.76 | 0.680 | -30.35 | -42.85 | 46.82 |
| C best expression per thesis | 88.83 | +11.69 | +4.09 | +11.97 | 0.679 | -24.27 | -41.16 | 35.93 |
| R FUNDED research stakes | 37.00 | +5.33 | +1.74 | +5.19 | 0.660 | -9.91 | -13.94 | 0.00 |

## NSH @ BOS  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_NSH_win | p_overtime | goals | shots BOS/NSH | BOS/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.61 | 0.39 | 0.00 | 6.06 | 28.2/28.1 | 25.0/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.50 | 6.03 | 28.4/28.2 | 24.8/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.62 | 0.38 | 0.00 | 9.36 | 29.6/29.3 | 23.9/22.8 | even strength |
| BOS shot control · normal event (5-7) · decided (2+) | 0.081 | 0.68 | 0.32 | 0.00 | 6.07 | 33.1/22.3 | 19.7/28.3 | even strength |
| BOS shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.56 | 0.44 | 0.47 | 5.9 | 33.2/22.4 | 19.1/29.7 | even strength |
| BOS shot control · high event (8+) · decided (2+) | 0.062 | 0.69 | 0.31 | 0.00 | 9.33 | 34.3/23.5 | 18.8/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 6.5 goals scored YES | 43 | 0.508 | 0.467 | +0.061 | +0.019 | $8.65 | FUNDED_RESEARCH | $3 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT22NSHBOS-6|yes; why: higher confidence-adjusted growth (3.31 vs 1.33 bp); relationships: only recommended bet in this game; failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis GAME:HIGH_EVENT (p 0.2968): highest fidelity KXNHLTOTAL-26OCT22NSHBOS-7|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT22NSHBOS-7|yes (same contract)
- KXNHLTOTAL-26OCT22NSHBOS-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.204, phi -0.514)

portfolios: A EV +2.10 (adj +0.62) on $19.24, P(profit) 0.508, adj growth 4.6 bp · B EV +1.18 (adj +0.37) on $8.65, P(profit) 0.508, adj growth 3.3 bp · C EV +1.18 (adj +0.37) on $8.65, P(profit) 0.508, adj growth 3.3 bp · R EV +0.41 (adj +0.13) on $3.00, P(profit) 0.508, adj growth 4.3 bp

## NYR @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYR_win | p_overtime | goals | shots TOR/NYR | TOR/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.53 | 0.47 | 0.00 | 6.01 | 27.4/27.5 | 24.2/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.50 | 0.50 | 0.46 | 5.93 | 27.2/27.2 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.56 | 0.44 | 0.00 | 9.36 | 28.9/29.0 | 23.1/22.5 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.078 | 0.44 | 0.56 | 0.00 | 5.98 | 21.6/32.3 | 28.2/18.4 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.50 | 0.50 | 0.44 | 5.9 | 22.1/32.7 | 29.3/19.0 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.059 | 0.60 | 0.40 | 0.00 | 6.01 | 32.4/22.1 | 19.0/28.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_SJS_win | p_overtime | goals | shots OTT/SJS | OTT/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.65 | 0.35 | 0.00 | 6.0 | 27.1/26.5 | 23.4/23.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.110 | 0.68 | 0.32 | 0.00 | 6.01 | 32.4/21.2 | 18.6/28.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.54 | 0.46 | 0.47 | 5.92 | 26.8/26.5 | 23.1/23.5 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.57 | 0.43 | 0.50 | 5.89 | 32.2/21.2 | 18.1/28.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.66 | 0.34 | 0.00 | 9.2 | 28.5/28.1 | 23.1/21.7 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.070 | 0.73 | 0.27 | 0.00 | 9.27 | 33.6/22.0 | 17.8/25.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## ANA @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_ANA_win | p_overtime | goals | shots NJD/ANA | NJD/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.56 | 0.44 | 0.00 | 6.03 | 28.9/28.7 | 25.2/25.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.46 | 5.97 | 28.6/28.5 | 25.2/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.58 | 0.42 | 0.00 | 9.23 | 30.2/29.9 | 24.3/23.6 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.087 | 0.59 | 0.41 | 0.00 | 5.99 | 34.0/22.8 | 19.9/29.9 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.52 | 0.48 | 0.47 | 5.99 | 34.0/22.9 | 19.7/30.6 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.061 | 0.64 | 0.36 | 0.00 | 9.33 | 35.5/24.3 | 19.3/27.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 2.5 goals NO | 71 | 0.790 | 0.747 | +0.065 | +0.023 | $20.00 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 1.5 goals YES | 19 | 0.248 | 0.217 | +0.048 | +0.016 | $2.81 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22ANANJ-NJ2|no; why: higher confidence-adjusted growth (5.80 vs 3.98 bp); despite a smaller raw edge (+0.065 vs +0.069/contract); relationships: KXNHLSPREAD-26OCT22ANANJ-ANA2|yes: REINFORCING (phi 0.297); failure: NJD wins by 2+
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26OCT22ANANJ-NJ3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22ANANJ-NJ3|no has the higher standalone adjusted growth (5.80 vs 3.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.297); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22ANANJ-NJ3|no: REINFORCING (phi 0.297); failure: NJD wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis ANA:WINS (p 0.4554): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22ANANJ-NJ3|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.2485): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22ANANJ-NJ3|no (same contract)
- thesis NJD:SUPPRESSED (p 0.3555): highest fidelity KXNHLSPREAD-26OCT22ANANJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22ANANJ-NJ3|no (same contract)
- KXNHLSPREAD-26OCT22ANANJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3245, phi -0.745)
- KXNHLSPREAD-26OCT22ANANJ-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.5446, phi -0.629)

portfolios: A EV +3.01 (adj +0.90) on $24.05, P(profit) 0.6848, adj growth 7.2 bp · B EV +2.47 (adj +0.86) on $22.81, P(profit) 0.7897, adj growth 7.5 bp · C EV +1.80 (adj +0.63) on $20.00, P(profit) 0.7897, adj growth 5.7 bp · R EV +0.69 (adj +0.24) on $6.00, P(profit) 0.7897, adj growth 8.2 bp

## FLA @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_FLA_win | p_overtime | goals | shots PIT/FLA | PIT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.58 | 0.42 | 0.00 | 6.04 | 26.9/26.9 | 23.7/23.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.58 | 0.42 | 0.00 | 9.46 | 28.6/28.6 | 22.9/21.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.45 | 6.0 | 27.0/27.0 | 23.6/23.7 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.078 | 0.68 | 0.32 | 0.00 | 6.03 | 31.9/21.5 | 18.8/27.2 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.57 | 0.43 | 0.47 | 6.0 | 32.2/21.5 | 18.3/28.7 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.061 | 0.67 | 0.33 | 0.00 | 9.4 | 33.2/22.7 | 17.8/25.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## LAK @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_LAK_win | p_overtime | goals | shots NYI/LAK | NYI/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.57 | 0.43 | 0.00 | 5.98 | 27.3/27.2 | 23.9/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.50 | 0.50 | 0.48 | 5.91 | 27.4/27.4 | 24.1/24.1 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.082 | 0.65 | 0.35 | 0.00 | 5.99 | 32.3/21.6 | 18.9/27.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.55 | 0.45 | 0.00 | 9.02 | 28.7/28.7 | 23.2/22.8 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.56 | 0.44 | 0.52 | 5.82 | 32.4/21.8 | 18.7/29.0 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.54 | 0.46 | 0.46 | 2.78 | 25.9/25.8 | 24.3/24.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYI shot control · normal event (5-7) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_VGK_win | p_overtime | goals | shots STL/VGK | STL/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.48 | 0.52 | 0.00 | 6.05 | 26.7/26.9 | 23.2/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.47 | 5.92 | 26.7/26.7 | 23.5/23.2 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.093 | 0.40 | 0.60 | 0.00 | 6.04 | 20.9/31.8 | 27.7/17.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.50 | 0.50 | 0.00 | 9.3 | 28.1/28.5 | 22.4/22.0 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.48 | 0.52 | 0.46 | 5.89 | 21.1/31.7 | 28.4/18.0 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.059 | 0.41 | 0.59 | 0.00 | 9.32 | 22.6/33.7 | 27.0/17.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_WPG_win | p_overtime | goals | shots DAL/WPG | DAL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.62 | 0.38 | 0.00 | 6.01 | 25.9/25.8 | 22.6/21.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.47 | 5.87 | 26.1/25.8 | 22.5/22.8 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.099 | 0.68 | 0.32 | 0.00 | 5.96 | 30.8/20.4 | 17.8/26.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.58 | 0.42 | 0.51 | 5.86 | 31.1/20.5 | 17.4/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.61 | 0.39 | 0.00 | 9.18 | 27.6/27.2 | 21.9/20.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.55 | 0.46 | 0.00 | 3.45 | 24.8/24.5 | 22.7/22.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dallas wins by over 2.5 goals NO | 71 | 0.773 | 0.739 | +0.048 | +0.014 | $11.59 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Winnipeg wins by over 1.5 goals YES | 17 | 0.219 | 0.192 | +0.039 | +0.012 | $2.43 | FUNDED_RESEARCH | $1 | WPG:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL2|no; why: higher confidence-adjusted growth (2.29 vs 0.48 bp); wins across more scripts (relative breadth 1.006 vs 0.888); alternative not eligible: confidence-adjusted EV +0.0072 below the 0.010/contract floor; relationships: KXNHLSPREAD-26OCT22WPGDAL-WPG2|yes: REINFORCING (phi 0.287); failure: DAL wins by 2+
- **Winnipeg wins by over 1.5 goals YES** — thesis: WPG wins by 2+; alternative: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no has the higher standalone adjusted growth (2.29 vs 2.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.287); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: REINFORCING (phi 0.287); failure: DAL wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4294): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22WPGDAL-DAL3|no (same contract)
- thesis WPG:WINS_BY_2PLUS (p 0.2189): highest fidelity KXNHLSPREAD-26OCT22WPGDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22WPGDAL-DAL3|no (same contract)
- KXNHLSPREAD-26OCT22WPGDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3517, phi -0.736)
- KXNHLSPREAD-26OCT22WPGDAL-WPG2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.5823, phi -0.625)

portfolios: A EV +1.88 (adj +0.58) on $15.34, P(profit) 0.2189, adj growth 4.5 bp · B EV +1.30 (adj +0.39) on $14.02, P(profit) 0.7727, adj growth 3.5 bp · C EV +0.95 (adj +0.28) on $14.26, P(profit) 0.7727, adj growth 2.5 bp · R EV +0.42 (adj +0.13) on $4.00, P(profit) 0.7727, adj growth 4.2 bp

## MIN @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_MIN_win | p_overtime | goals | shots CGY/MIN | CGY/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.43 | 0.57 | 0.00 | 6.0 | 29.1/29.4 | 25.4/25.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.46 | 0.54 | 0.46 | 5.94 | 29.3/29.6 | 26.1/26.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.44 | 0.56 | 0.00 | 9.18 | 31.0/31.2 | 24.9/25.1 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.083 | 0.35 | 0.65 | 0.00 | 5.98 | 23.6/34.8 | 30.4/20.7 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.50 | 0.50 | 0.47 | 5.94 | 23.6/35.0 | 31.6/20.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.059 | 0.46 | 0.54 | 0.48 | 2.79 | 27.5/27.7 | 26.1/26.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Minnesota wins by over 1.5 goals NO | 59 | 0.680 | 0.632 | +0.073 | +0.026 | $8.25 | FUNDED_RESEARCH | $3 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 72 | 0.796 | 0.755 | +0.061 | +0.021 | $10.35 | FUNDED_RESEARCH | $3 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Calgary wins by over 1.5 goals YES | 18 | 0.240 | 0.207 | +0.049 | +0.017 | $2.09 | FUNDED_RESEARCH | $1 | CGY:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Calgary over 4.5 goals scored YES | 13 | 0.176 | 0.150 | +0.038 | +0.012 | $1.07 | FUNDED_RESEARCH | $1 | CGY:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
- **Minnesota wins by over 1.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN3|no; why: higher confidence-adjusted growth (6.03 vs 5.06 bp); relationships: KXNHLSPREAD-26OCT22MINCGY-MIN3|no: DUPLICATIVE (phi 0.739); KXNHLSPREAD-26OCT22MINCGY-CGY2|yes: DUPLICATIVE (phi 0.385); KXNHLTEAMTOTAL-26OCT22MINCGY-CGY5|yes: REINFORCING (phi 0.292); failure: MIN wins by 2+
- **Minnesota wins by over 2.5 goals NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22MINCGY-MIN2|no has the higher standalone adjusted growth (6.03 vs 5.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.739); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22MINCGY-MIN2|no: DUPLICATIVE (phi 0.739); KXNHLSPREAD-26OCT22MINCGY-CGY2|yes: REINFORCING (phi 0.285); KXNHLTEAMTOTAL-26OCT22MINCGY-CGY5|yes: REINFORCING (phi 0.225); failure: MIN wins by 2+
- **Calgary wins by over 1.5 goals YES** — thesis: CGY wins by 2+; alternative: KXNHLSPREAD-26OCT22MINCGY-MIN2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22MINCGY-MIN2|no has the higher standalone adjusted growth (6.03 vs 4.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.385); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22MINCGY-MIN2|no: DUPLICATIVE (phi 0.385); KXNHLSPREAD-26OCT22MINCGY-MIN3|no: REINFORCING (phi 0.285); KXNHLTEAMTOTAL-26OCT22MINCGY-CGY5|yes: REINFORCING (phi 0.492); failure: MIN wins (incl. OT/SO)
- **Calgary over 4.5 goals scored YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT22MINCGY-MIN2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22MINCGY-MIN2|no has the higher standalone adjusted growth (6.03 vs 2.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.292); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22MINCGY-MIN2|no: REINFORCING (phi 0.292); KXNHLSPREAD-26OCT22MINCGY-MIN3|no: REINFORCING (phi 0.225); KXNHLSPREAD-26OCT22MINCGY-CGY2|yes: REINFORCING (phi 0.492); failure: MIN wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CGY:WINS (p 0.4531): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN2|no (same contract)
- thesis CGY:WINS_BY_2PLUS (p 0.2396): highest fidelity KXNHLSPREAD-26OCT22MINCGY-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN2|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3343): highest fidelity KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22MINCGY-MIN2|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT22MINCGY-CGY5|yes kept
- KXNHLSPREAD-26OCT22MINCGY-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3199, phi -1.0)
- KXNHLSPREAD-26OCT22MINCGY-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.3199, phi -0.739)
- KXNHLSPREAD-26OCT22MINCGY-CGY2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.5469, phi -0.617)
- KXNHLTEAMTOTAL-26OCT22MINCGY-CGY5|yes: FUNDED_RESEARCH; family MIXED; loses 47% of the draws where the thesis happens; opposing: failure thesis MIN:WINS (p 0.5469, phi -0.429)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT22MINCGY-CGY4|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT22MINCGY-CGY5|yes kept

portfolios: A EV +2.80 (adj +0.85) on $24.05, P(profit) 0.6303, adj growth 7.1 bp · B EV +2.70 (adj +0.93) on $21.76, P(profit) 0.6831, adj growth 8.2 bp · C EV +2.07 (adj +0.73) on $17.19, P(profit) 0.6801, adj growth 6.4 bp · R EV +1.15 (adj +0.39) on $8.00, P(profit) 0.6831, adj growth 12.2 bp

## CAR @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_CAR_win | p_overtime | goals | shots EDM/CAR | EDM/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.62 | 0.38 | 0.00 | 6.08 | 27.5/28.0 | 25.0/23.4 | even strength |
| CAR shot control · normal event (5-7) · decided (2+) | 0.109 | 0.54 | 0.46 | 0.00 | 6.07 | 21.8/33.2 | 29.7/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.63 | 0.37 | 0.00 | 9.53 | 28.8/29.5 | 24.1/21.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.54 | 0.46 | 0.44 | 5.94 | 27.2/28.0 | 24.7/23.8 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.48 | 0.52 | 0.49 | 5.98 | 21.8/33.4 | 29.8/18.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.093 | 0.55 | 0.45 | 0.00 | 9.42 | 23.5/35.2 | 28.6/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Edmonton wins by over 1.5 goals YES | 28 | 0.353 | 0.314 | +0.059 | +0.020 | $6.03 | FUNDED_RESEARCH | $2 | EDM:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 1.5 goals NO | 70 | 0.760 | 0.725 | +0.045 | +0.010 | $3.34 | FUNDED_RESEARCH | $1 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Edmonton wins by over 1.5 goals YES** — thesis: EDM wins by 2+; alternative: KXNHLSPREAD-26OCT22CAREDM-CAR2|no; why: higher confidence-adjusted growth (4.11 vs 1.15 bp); relationships: KXNHLSPREAD-26OCT22CAREDM-CAR2|no: DUPLICATIVE (phi 0.415); failure: CAR wins (incl. OT/SO)
- **Carolina wins by over 1.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22CAREDM-EDM2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT22CAREDM-EDM2|yes has the higher standalone adjusted growth (4.11 vs 1.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.415); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22CAREDM-EDM2|yes: DUPLICATIVE (phi 0.415); failure: CAR wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CAR shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:WINS_BY_2PLUS (p 0.3528): highest fidelity KXNHLSPREAD-26OCT22CAREDM-EDM2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-EDM2|yes (same contract)
- thesis EDM:WINS (p 0.5621): highest fidelity KXNHLSPREAD-26OCT22CAREDM-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22CAREDM-EDM2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT22CAREDM-EDM2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.4379, phi -0.652)
- KXNHLSPREAD-26OCT22CAREDM-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2399, phi -1.0)

portfolios: A EV +2.53 (adj +0.79) on $19.24, P(profit) 0.3528, adj growth 6.1 bp · B EV +1.42 (adj +0.45) on $9.38, P(profit) 0.3528, adj growth 4.0 bp · C EV +1.31 (adj +0.44) on $6.55, P(profit) 0.3528, adj growth 3.8 bp · R EV +0.46 (adj +0.15) on $3.00, P(profit) 0.3528, adj growth 5.0 bp

## UTA @ SEA  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_UTA_win | p_overtime | goals | shots SEA/UTA | SEA/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.51 | 0.49 | 0.00 | 6.08 | 27.3/27.7 | 24.2/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.51 | 0.49 | 0.46 | 5.96 | 27.3/27.9 | 24.4/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.48 | 0.52 | 0.00 | 9.41 | 28.8/29.0 | 22.7/22.6 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.097 | 0.44 | 0.56 | 0.00 | 6.01 | 21.9/33.1 | 29.0/18.8 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.50 | 0.50 | 0.46 | 5.98 | 21.7/33.1 | 29.7/18.5 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.074 | 0.41 | 0.59 | 0.00 | 9.36 | 23.4/34.9 | 27.8/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Utah wins by over 1.5 goals NO | 62 | 0.702 | 0.659 | +0.066 | +0.022 | $14.35 | FUNDED_RESEARCH | $4 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Utah wins by over 2.5 goals NO | 75 | 0.811 | 0.778 | +0.048 | +0.015 | $2.54 | FUNDED_RESEARCH | $1 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Utah wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA3|no; why: higher confidence-adjusted growth (4.68 vs 2.78 bp); relationships: KXNHLSPREAD-26OCT22UTASEA-UTA3|no: DUPLICATIVE (phi 0.74); failure: UTA wins by 2+
- **Utah wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22UTASEA-UTA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT22UTASEA-UTA2|no has the higher standalone adjusted growth (4.68 vs 2.78 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.740); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22UTASEA-UTA2|no: DUPLICATIVE (phi 0.74); failure: UTA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SEA:WINS (p 0.4896): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no (same contract)
- thesis SEA:WINS_BY_2PLUS (p 0.2741): highest fidelity KXNHLSPREAD-26OCT22UTASEA-UTA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22UTASEA-UTA2|no (same contract)
- KXNHLSPREAD-26OCT22UTASEA-UTA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2976, phi -1.0)
- KXNHLSPREAD-26OCT22UTASEA-UTA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2976, phi -0.74)

portfolios: A EV +2.61 (adj +0.76) on $24.05, P(profit) 0.7024, adj growth 5.9 bp · B EV +1.65 (adj +0.55) on $16.89, P(profit) 0.7024, adj growth 4.9 bp · C EV +1.68 (adj +0.57) on $16.25, P(profit) 0.7024, adj growth 5.0 bp · R EV +0.48 (adj +0.16) on $5.00, P(profit) 0.7024, adj growth 5.5 bp

## DET @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_DET_win | p_overtime | goals | shots VAN/DET | VAN/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.113 | 0.50 | 0.50 | 0.00 | 5.98 | 21.7/33.4 | 29.7/18.3 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.49 | 0.51 | 0.51 | 5.93 | 22.0/33.9 | 30.5/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.58 | 0.42 | 0.00 | 5.99 | 27.2/27.9 | 24.8/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.51 | 0.49 | 0.48 | 5.89 | 27.3/27.9 | 24.7/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.59 | 0.41 | 0.00 | 9.32 | 28.7/29.5 | 24.1/22.1 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.075 | 0.48 | 0.52 | 0.00 | 9.3 | 23.3/35.3 | 28.7/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 2.5 goals YES | 13 | 0.201 | 0.163 | +0.063 | +0.025 | $3.75 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | DIRECT (0.66) | EVIDENCE_MIXED | D |
| Detroit over 1.5 goals scored NO | 13 | 0.197 | 0.161 | +0.059 | +0.023 | $3.11 | FUNDED_RESEARCH | $1 | DET:SUPPRESSED | FRAGILE (0.48) | EVIDENCE_MIXED | D |
| Detroit wins by over 1.5 goals NO | 62 | 0.750 | 0.662 | +0.114 | +0.026 | $6.33 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Detroit wins by over 2.5 goals NO | 74 | 0.846 | 0.774 | +0.093 | +0.021 | $12.26 | FUNDED_RESEARCH | $4 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 2.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no; why: higher confidence-adjusted growth (11.24 vs 9.73 bp); relationships: KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no: REINFORCING (phi 0.413); KXNHLSPREAD-26OCT22DETVAN-DET2|no: REINFORCING (phi 0.289); KXNHLSPREAD-26OCT22DETVAN-DET3|no: REINFORCING (phi 0.214); failure: DET wins (incl. OT/SO)
- **Detroit over 1.5 goals scored NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes has the higher standalone adjusted growth (11.24 vs 9.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.413); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes: REINFORCING (phi 0.413); KXNHLSPREAD-26OCT22DETVAN-DET2|no: REINFORCING (phi 0.286); KXNHLSPREAD-26OCT22DETVAN-DET3|no: REINFORCING (phi 0.211); failure: DET wins (incl. OT/SO)
- **Detroit wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: Broad expression KXNHLSPREAD-26OCT22DETVAN-DET2|no selected over broad KXNHLTEAMTOTAL-26OCT22DETVAN-DET5|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes: REINFORCING (phi 0.289); KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no: REINFORCING (phi 0.286); KXNHLSPREAD-26OCT22DETVAN-DET3|no: DUPLICATIVE (phi 0.738); failure: DET wins by 2+
- **Detroit wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes has the higher standalone adjusted growth (11.24 vs 4.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.214); they share one thesis budget; relationships: KXNHLSPREAD-26OCT22DETVAN-VAN3|yes: REINFORCING (phi 0.214); KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no: REINFORCING (phi 0.211); KXNHLSPREAD-26OCT22DETVAN-DET2|no: DUPLICATIVE (phi 0.738); failure: DET wins by 2+

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.11, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis VAN:WINS_BY_2PLUS (p 0.3064): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-DET2|no (same contract)
- thesis DET:SUPPRESSED (p 0.4122): highest fidelity KXNHLTEAMTOTAL-26OCT22DETVAN-DET5|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-DET2|no — override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT22DETVAN-VAN2|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no kept
- thesis VAN:WINS (p 0.5315): highest fidelity KXNHLSPREAD-26OCT22DETVAN-DET2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT22DETVAN-DET2|no (same contract)
- KXNHLSPREAD-26OCT22DETVAN-VAN3|yes: FUNDED_RESEARCH; family MIXED; loses 34% of the draws where the thesis happens; opposing: failure thesis DET:WINS (p 0.4685, phi -0.47)
- KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no: FUNDED_RESEARCH; family MIXED; loses 52% of the draws where the thesis happens; opposing: failure thesis DET:WINS (p 0.4685, phi -0.426)
- KXNHLSPREAD-26OCT22DETVAN-DET2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.5 pts; opposing: failure thesis DET:WINS_BY_2PLUS (p 0.25, phi -1.0)
- KXNHLSPREAD-26OCT22DETVAN-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.1 pts; opposing: failure thesis DET:WINS_BY_2PLUS (p 0.25, phi -0.738)
- override: Broad expression KXNHLSPREAD-26OCT22DETVAN-DET2|no selected over broad KXNHLTEAMTOTAL-26OCT22DETVAN-DET5|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT22DETVAN-VAN2|yes less than the minimum stake; KXNHLSPREAD-26OCT22DETVAN-VAN3|yes kept
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT22DETVAN-VAN2|yes less than the minimum stake; KXNHLTEAMTOTAL-26OCT22DETVAN-DET2|no kept

portfolios: A EV +5.96 (adj +1.14) on $24.05, P(profit) 0.5315, adj growth 9.0 bp · B EV +5.68 (adj +1.79) on $25.45, P(profit) 0.75, adj growth 15.6 bp · C EV +2.70 (adj +1.07) on $5.93, P(profit) 0.2007, adj growth 9.3 bp · R EV +1.73 (adj +0.54) on $8.00, P(profit) 0.75, adj growth 18.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT22DETVAN-VAN|yes == KXNHLGAME-26OCT22DETVAN-DET|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
