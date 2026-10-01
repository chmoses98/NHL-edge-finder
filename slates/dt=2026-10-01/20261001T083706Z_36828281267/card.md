# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-01T08:37:06Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +21.78 | +5.61 | +21.68 | 0.616 | -67.09 | -93.68 | 32.91 |
| B thesis-diversified (joint) ← card | 48.31 | +6.57 | +1.85 | +8.95 | 0.612 | -26.17 | -29.09 | 16.22 |
| C best expression per thesis | 35.45 | +5.40 | +1.62 | +5.26 | 0.693 | -16.52 | -35.45 | 14.16 |

## PHI @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_PHI_win | p_overtime | goals | shots NJD/PHI | NJD/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.54 | 0.46 | 0.00 | 5.97 | 27.1/26.7 | 23.4/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.48 | 5.85 | 26.9/26.5 | 23.2/23.7 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.106 | 0.57 | 0.43 | 0.00 | 5.96 | 32.1/21.0 | 18.0/27.8 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.54 | 0.46 | 0.47 | 5.82 | 31.9/20.8 | 17.7/28.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.068 | 0.53 | 0.47 | 0.00 | 9.1 | 28.5/27.9 | 22.5/22.4 | even strength |
| NJD shot control · low event (<=4) · tight (1-goal/OT) | 0.063 | 0.52 | 0.48 | 0.50 | 2.79 | 30.8/20.2 | 18.8/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| New Jersey wins by over 1.5 goals NO | 63 | 0.705 | 0.662 | +0.059 | +0.016 | $8.06 | PHI:WINS | 0.2956 | EVIDENCE_MIXED | D |
| Philadelphia wins YES | 40 | 0.477 | 0.433 | +0.060 | +0.017 | $4.03 | PHI:WINS | 0.2291 | EVIDENCE_MIXED | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLGAME-26OCT01PHINJ-PHI|yes; why: higher confidence-adjusted growth (2.53 vs 2.52 bp); despite a smaller raw edge (+0.059 vs +0.060/contract); relationships: KXNHLGAME-26OCT01PHINJ-PHI|yes: DUPLICATIVE (phi 0.618); failure: NJD wins by 2+
- **Philadelphia wins YES** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01PHINJ-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT01PHINJ-NJ2|no has the higher standalone adjusted growth (2.53 vs 2.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.618); they share one thesis budget; relationships: KXNHLSPREAD-26OCT01PHINJ-NJ2|no: DUPLICATIVE (phi 0.618); failure: NJD wins (incl. OT/SO)

portfolios: A EV +4.16 (adj +1.15) on $35.29, P(profit) 0.4771, adj growth 6.9 bp · B EV +1.32 (adj +0.36) on $12.09, P(profit) 0.7051, adj growth 3.2 bp · C EV +1.11 (adj +0.31) on $12.24, P(profit) 0.7051, adj growth 2.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01PHINJ-NJ|no == KXNHLGAME-26OCT01PHINJ-PHI|yes

## TBL @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_TBL_win | p_overtime | goals | shots NYR/TBL | NYR/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.56 | 0.44 | 0.00 | 6.02 | 26.0/26.5 | 23.2/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.53 | 0.47 | 0.46 | 5.96 | 26.4/26.8 | 23.5/23.1 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.103 | 0.41 | 0.59 | 0.00 | 5.95 | 20.8/32.0 | 27.7/17.8 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.50 | 0.50 | 0.48 | 5.89 | 20.9/31.7 | 28.2/17.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.54 | 0.46 | 0.00 | 9.12 | 27.5/28.1 | 22.7/21.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.53 | 0.47 | 0.00 | 3.41 | 25.1/25.5 | 23.7/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| New York R wins YES | 44 | 0.518 | 0.476 | +0.061 | +0.019 | $8.79 | NYR:WINS | 0.2363 | EVIDENCE_MIXED | D |
- **New York R wins YES** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLGAME-26OCT01TBNYR-TB|no; why: higher confidence-adjusted growth (3.26 vs 2.47 bp); relationships: only recommended bet in this game; failure: TBL wins (incl. OT/SO)

portfolios: A EV +3.55 (adj +1.02) on $35.29, P(profit) 0.518, adj growth 6.3 bp · B EV +1.17 (adj +0.37) on $8.79, P(profit) 0.518, adj growth 3.2 bp · C EV +1.17 (adj +0.37) on $8.80, P(profit) 0.518, adj growth 3.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01TBNYR-TB|no == KXNHLGAME-26OCT01TBNYR-NYR|yes

## BUF @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_BUF_win | p_overtime | goals | shots CBJ/BUF | CBJ/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.58 | 0.42 | 0.00 | 6.0 | 28.2/28.1 | 25.0/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.46 | 5.94 | 28.3/28.1 | 24.7/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.58 | 0.42 | 0.00 | 9.32 | 30.1/29.9 | 24.5/23.3 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.080 | 0.65 | 0.35 | 0.00 | 5.99 | 33.4/22.5 | 19.7/29.1 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.57 | 0.43 | 0.46 | 5.91 | 33.1/22.6 | 19.5/29.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.58 | 0.42 | 0.00 | 3.44 | 26.9/26.7 | 25.1/24.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_MIN_win | p_overtime | goals | shots NSH/MIN | NSH/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.136 | 0.49 | 0.51 | 0.00 | 6.03 | 29.3/29.3 | 25.6/25.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.48 | 0.52 | 0.45 | 5.93 | 29.2/29.6 | 26.3/26.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.45 | 0.55 | 0.00 | 9.38 | 30.7/30.8 | 24.3/24.5 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.078 | 0.41 | 0.59 | 0.00 | 6.03 | 23.9/35.0 | 30.7/20.7 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.063 | 0.51 | 0.49 | 0.00 | 6.05 | 34.1/23.6 | 20.0/30.4 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.057 | 0.43 | 0.57 | 0.48 | 5.99 | 23.6/34.5 | 30.9/20.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_SEA_win | p_overtime | goals | shots CGY/SEA | CGY/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.50 | 0.50 | 0.00 | 6.0 | 28.3/28.2 | 24.8/24.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.48 | 5.98 | 28.2/28.1 | 24.8/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.53 | 0.47 | 0.00 | 9.23 | 29.8/29.6 | 23.7/23.4 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.078 | 0.59 | 0.41 | 0.00 | 5.99 | 33.8/23.0 | 20.0/29.8 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.52 | 0.48 | 0.48 | 5.84 | 33.3/22.5 | 19.3/30.1 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.060 | 0.44 | 0.56 | 0.00 | 5.98 | 22.6/32.9 | 28.9/19.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_CHI_win | p_overtime | goals | shots UTA/CHI | UTA/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| UTA shot control · normal event (5-7) · decided (2+) | 0.125 | 0.75 | 0.25 | 0.00 | 6.02 | 32.8/21.2 | 18.9/27.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.68 | 0.32 | 0.00 | 5.99 | 27.3/26.7 | 23.9/23.0 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.098 | 0.76 | 0.24 | 0.00 | 9.34 | 34.7/22.6 | 18.3/26.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.51 | 0.49 | 0.46 | 5.94 | 27.6/27.1 | 23.9/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.68 | 0.32 | 0.00 | 9.39 | 28.9/28.2 | 23.3/21.8 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.60 | 0.40 | 0.47 | 5.94 | 32.9/21.6 | 18.4/29.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_EDM_win | p_overtime | goals | shots VAN/EDM | VAN/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.43 | 0.57 | 0.00 | 6.02 | 27.8/28.6 | 24.5/24.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.107 | 0.39 | 0.61 | 0.00 | 6.04 | 22.2/33.9 | 29.6/19.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.49 | 0.51 | 0.43 | 5.95 | 27.7/28.3 | 25.0/24.4 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.46 | 0.54 | 0.48 | 5.96 | 22.0/34.1 | 30.7/18.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.44 | 0.56 | 0.00 | 9.5 | 29.5/30.4 | 23.8/23.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.085 | 0.35 | 0.65 | 0.00 | 9.3 | 23.8/35.7 | 27.8/19.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Vancouver wins YES | 36 | 0.445 | 0.397 | +0.069 | +0.021 | $8.19 | VAN:WINS | 0.2264 | EVIDENCE_MIXED | D |
- **Vancouver wins YES** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLGAME-26OCT01EDMVAN-EDM|no; why: higher confidence-adjusted growth (4.21 vs 3.28 bp); relationships: only recommended bet in this game; failure: EDM wins (incl. OT/SO)

portfolios: A EV +5.87 (adj +1.38) on $35.29, P(profit) 0.4448, adj growth 7.9 bp · B EV +1.50 (adj +0.46) on $8.19, P(profit) 0.4448, adj growth 4.0 bp · C EV +1.50 (adj +0.46) on $8.19, P(profit) 0.4448, adj growth 4.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01EDMVAN-EDM|no == KXNHLGAME-26OCT01EDMVAN-VAN|yes

## FLA @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_FLA_win | p_overtime | goals | shots SJS/FLA | SJS/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.58 | 0.42 | 0.00 | 6.05 | 26.7/26.7 | 23.6/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.50 | 0.50 | 0.50 | 6.02 | 26.8/27.0 | 23.7/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.62 | 0.38 | 0.00 | 9.37 | 28.4/28.7 | 23.1/21.3 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.079 | 0.51 | 0.49 | 0.00 | 6.05 | 21.3/31.9 | 28.3/17.9 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.49 | 0.51 | 0.43 | 5.87 | 21.5/31.7 | 28.3/18.3 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.063 | 0.65 | 0.35 | 0.00 | 6.05 | 31.2/21.4 | 18.6/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| San Jose wins by over 1.5 goals YES | 25 | 0.332 | 0.283 | +0.069 | +0.020 | $4.27 | SJS:WINS_BY_2PLUS | 0.4051 | EVIDENCE_MIXED | D |
| Florida wins NO | 43 | 0.546 | 0.468 | +0.099 | +0.020 | $2.36 | SJS:WINS | 0.246 | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 78 | 0.852 | 0.806 | +0.059 | +0.014 | $12.60 | SJS:WINS | 0.2339 | EVIDENCE_MIXED | D |
- **San Jose wins by over 1.5 goals YES** — thesis: SJS wins by 2+; alternative: KXNHLGAME-26OCT01FLASJ-FLA|no; why: higher confidence-adjusted growth (4.61 vs 3.64 bp); despite a smaller raw edge (+0.069 vs +0.099/contract); relationships: KXNHLGAME-26OCT01FLASJ-FLA|no: DUPLICATIVE (phi 0.642); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.294); failure: FLA wins (incl. OT/SO)
- **Florida wins NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes has the higher standalone adjusted growth (4.61 vs 3.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.642); they share one thesis budget; relationships: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes: DUPLICATIVE (phi 0.642); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: DUPLICATIVE (phi 0.458); failure: FLA wins (incl. OT/SO)
- **Florida wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes has the higher standalone adjusted growth (4.61 vs 2.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.294); they share one thesis budget; relationships: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes: REINFORCING (phi 0.294); KXNHLGAME-26OCT01FLASJ-FLA|no: DUPLICATIVE (phi 0.458); failure: FLA wins by 2+

portfolios: A EV +8.20 (adj +2.06) on $44.12, P(profit) 0.5463, adj growth 11.8 bp · B EV +2.59 (adj +0.66) on $19.24, P(profit) 0.5463, adj growth 5.7 bp · C EV +1.62 (adj +0.48) on $6.22, P(profit) 0.3318, adj growth 4.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01FLASJ-SJ|yes == KXNHLGAME-26OCT01FLASJ-FLA|no

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
