# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-27T04:17:19Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 129.84 | +14.29 | +3.65 | +18.91 | 0.602 | -76.82 | -78.75 | 13.00 |
| B thesis-diversified (joint) ← optimiser card | 41.65 | +3.28 | +0.92 | +4.31 | 0.561 | -18.52 | -25.43 | 8.11 |
| C best expression per thesis | 31.82 | +2.71 | +0.79 | +7.19 | 0.652 | -15.16 | -15.16 | 6.92 |
| R FUNDED research stakes | 14.00 | +1.11 | +0.32 | +1.77 | 0.561 | -6.23 | -8.52 | 0.00 |

## CBJ @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CBJ_win | p_overtime | goals | shots PHI/CBJ | PHI/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.56 | 0.44 | 0.00 | 5.94 | 26.3/26.6 | 23.3/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.51 | 0.49 | 0.48 | 5.89 | 26.6/26.9 | 23.6/23.4 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.46 | 0.54 | 0.46 | 5.86 | 21.2/31.9 | 28.7/18.0 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.084 | 0.47 | 0.53 | 0.00 | 5.95 | 21.2/31.6 | 27.6/18.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.067 | 0.57 | 0.43 | 0.00 | 9.06 | 27.9/28.1 | 22.7/21.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.067 | 0.49 | 0.51 | 0.53 | 2.77 | 25.3/25.5 | 24.0/23.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ CAR  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_BOS_win | p_overtime | goals | shots CAR/BOS | CAR/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.165 | 0.64 | 0.36 | 0.00 | 6.04 | 34.6/21.4 | 18.6/30.2 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.139 | 0.53 | 0.47 | 0.47 | 6.02 | 34.6/21.3 | 18.0/31.1 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.137 | 0.66 | 0.34 | 0.00 | 9.4 | 36.2/22.7 | 17.7/28.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.082 | 0.57 | 0.43 | 0.00 | 6.03 | 28.1/27.0 | 23.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.51 | 0.49 | 0.47 | 6.03 | 28.0/27.2 | 23.8/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.60 | 0.40 | 0.00 | 9.38 | 29.8/28.6 | 22.9/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Boston over 2.5 goals scored YES | 53 | 0.607 | 0.564 | +0.060 | +0.016 | $8.49 | FUNDED_RESEARCH | $3 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Boston over 2.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes; why: higher confidence-adjusted growth (2.29 vs 1.24 bp); relationships: only recommended bet in this game; failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.14.
- thesis BOS:OFFENSE_4PLUS (p 0.3778): highest fidelity KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes (same contract)
- KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.4007, phi -0.984)

portfolios: A EV +5.30 (adj +1.26) on $39.84, P(profit) 0.388, adj growth 3.6 bp · B EV +0.92 (adj +0.25) on $8.49, P(profit) 0.6071, adj growth 2.2 bp · C EV +0.99 (adj +0.27) on $9.12, P(profit) 0.6071, adj growth 2.4 bp · R EV +0.33 (adj +0.09) on $3.00, P(profit) 0.6071, adj growth 3.0 bp

## LAK @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_LAK_win | p_overtime | goals | shots CHI/LAK | CHI/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.47 | 0.53 | 0.00 | 5.97 | 26.9/27.3 | 23.6/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.49 | 0.51 | 0.47 | 5.9 | 26.6/27.1 | 23.8/23.3 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.105 | 0.38 | 0.62 | 0.00 | 6.04 | 21.1/32.3 | 27.9/18.2 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.44 | 0.56 | 0.47 | 5.82 | 21.5/32.6 | 29.1/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.45 | 0.55 | 0.00 | 9.1 | 28.2/28.8 | 22.6/22.2 | even strength |
| LAK shot control · low event (<=4) · tight (1-goal/OT) | 0.059 | 0.43 | 0.57 | 0.49 | 2.79 | 19.8/31.1 | 29.5/18.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MTL @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_MTL_win | p_overtime | goals | shots STL/MTL | STL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.63 | 0.37 | 0.00 | 6.05 | 26.9/26.8 | 23.9/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.47 | 5.94 | 26.9/27.0 | 23.8/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.61 | 0.39 | 0.00 | 9.38 | 28.5/28.3 | 22.8/21.7 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.086 | 0.66 | 0.34 | 0.00 | 6.08 | 31.7/21.3 | 18.5/27.1 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.55 | 0.45 | 0.49 | 5.9 | 31.4/21.3 | 18.1/28.0 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.060 | 0.73 | 0.27 | 0.00 | 9.41 | 33.3/22.7 | 18.1/25.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_NYI_win | p_overtime | goals | shots NSH/NYI | NSH/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.52 | 0.48 | 0.00 | 6.01 | 27.8/27.9 | 24.5/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.52 | 0.48 | 0.46 | 5.96 | 27.9/28.0 | 24.7/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.53 | 0.47 | 0.00 | 9.34 | 29.3/29.5 | 23.5/22.9 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.081 | 0.51 | 0.49 | 0.00 | 5.99 | 22.5/33.4 | 29.5/19.1 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.49 | 0.51 | 0.47 | 5.92 | 22.7/33.1 | 29.7/19.5 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.059 | 0.47 | 0.53 | 0.00 | 9.22 | 23.6/35.0 | 28.2/18.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_NJD_win | p_overtime | goals | shots DAL/NJD | DAL/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.134 | 0.59 | 0.41 | 0.00 | 5.98 | 26.6/26.6 | 23.4/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.47 | 5.87 | 26.9/27.0 | 23.8/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.60 | 0.40 | 0.00 | 9.19 | 28.3/28.4 | 22.9/21.6 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.074 | 0.53 | 0.47 | 0.00 | 6.01 | 21.3/31.6 | 28.0/17.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.47 | 0.53 | 0.46 | 5.84 | 21.2/31.5 | 28.1/18.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.57 | 0.43 | 0.00 | 3.47 | 25.3/25.4 | 23.7/23.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## FLA @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_FLA_win | p_overtime | goals | shots WPG/FLA | WPG/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.53 | 0.47 | 0.00 | 6.0 | 26.8/26.9 | 23.5/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.50 | 5.9 | 26.7/27.0 | 23.7/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.55 | 0.45 | 0.00 | 9.12 | 28.2/28.5 | 23.0/22.0 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.46 | 0.54 | 0.48 | 5.89 | 21.4/31.8 | 28.4/18.3 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.071 | 0.51 | 0.49 | 0.00 | 5.97 | 21.4/31.7 | 27.9/18.1 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.56 | 0.44 | 0.44 | 5.79 | 31.6/21.7 | 18.6/28.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 2.5 goals NO | 80 | 0.852 | 0.823 | +0.040 | +0.012 | $13.57 | FUNDED_RESEARCH | $4 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 1.5 goals NO | 69 | 0.751 | 0.718 | +0.046 | +0.013 | $4.51 | FUNDED_RESEARCH | $2 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT27FLAWPG-FLA2|no; why: higher confidence-adjusted growth (2.09 vs 1.75 bp); despite a smaller raw edge (+0.040 vs +0.046/contract); relationships: KXNHLSPREAD-26OCT27FLAWPG-FLA2|no: DUPLICATIVE (phi 0.725); failure: FLA wins by 2+
- **Florida wins by over 1.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT27FLAWPG-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT27FLAWPG-FLA3|no has the higher standalone adjusted growth (2.09 vs 1.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.725); they share one thesis budget; relationships: KXNHLSPREAD-26OCT27FLAWPG-FLA3|no: DUPLICATIVE (phi 0.725); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis WPG:WINS (p 0.5264): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27FLAWPG-FLA2|no (same contract)
- KXNHLSPREAD-26OCT27FLAWPG-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2493, phi -0.725)
- KXNHLSPREAD-26OCT27FLAWPG-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2493, phi -1.0)

portfolios: A EV +2.29 (adj +0.66) on $40.00, P(profit) 0.7507, adj growth 4.7 bp · B EV +0.97 (adj +0.28) on $18.08, P(profit) 0.7507, adj growth 2.5 bp · C EV +0.90 (adj +0.27) on $18.13, P(profit) 0.8515, adj growth 2.4 bp · R EV +0.33 (adj +0.10) on $6.00, P(profit) 0.7507, adj growth 3.2 bp

## MIN @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_MIN_win | p_overtime | goals | shots UTA/MIN | UTA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.61 | 0.39 | 0.00 | 6.05 | 28.4/28.1 | 25.0/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.55 | 0.45 | 0.47 | 5.99 | 28.3/28.2 | 24.9/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.59 | 0.41 | 0.00 | 9.33 | 29.6/29.5 | 23.9/22.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.079 | 0.67 | 0.33 | 0.00 | 6.01 | 33.6/22.4 | 19.7/29.0 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.59 | 0.41 | 0.46 | 5.91 | 33.6/22.6 | 19.4/30.4 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.059 | 0.64 | 0.36 | 0.00 | 9.35 | 34.8/23.7 | 18.8/27.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_OTT_win | p_overtime | goals | shots VGK/OTT | VGK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.60 | 0.40 | 0.00 | 5.98 | 26.8/26.7 | 23.6/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.48 | 5.91 | 26.5/26.5 | 23.2/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.61 | 0.39 | 0.00 | 9.33 | 28.3/28.3 | 22.9/21.6 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.079 | 0.69 | 0.31 | 0.00 | 6.03 | 31.4/21.0 | 18.4/26.9 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.47 | 5.88 | 31.5/21.1 | 18.1/28.2 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.063 | 0.57 | 0.43 | 0.00 | 5.99 | 21.4/31.7 | 28.5/17.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_VAN_win | p_overtime | goals | shots ANA/VAN | ANA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.148 | 0.69 | 0.31 | 0.00 | 6.07 | 34.1/21.4 | 18.7/29.3 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.138 | 0.68 | 0.32 | 0.00 | 9.46 | 36.0/22.7 | 18.0/27.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.122 | 0.55 | 0.45 | 0.48 | 5.96 | 34.6/21.4 | 18.3/31.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.095 | 0.62 | 0.38 | 0.00 | 6.09 | 27.9/26.9 | 23.8/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.62 | 0.38 | 0.00 | 9.53 | 29.7/28.5 | 23.0/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.50 | 0.50 | 0.44 | 6.01 | 28.0/27.1 | 23.8/24.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.15, ANA shot control · high event (8+) · decided (2+) 0.14, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.12.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_BUF_win | p_overtime | goals | shots SJS/BUF | SJS/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.56 | 0.44 | 0.00 | 6.03 | 27.7/27.8 | 24.5/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.46 | 5.96 | 27.7/28.0 | 24.8/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.55 | 0.45 | 0.00 | 9.45 | 29.2/29.3 | 23.3/22.6 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.076 | 0.49 | 0.51 | 0.00 | 6.06 | 22.3/33.3 | 29.6/19.0 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.48 | 0.52 | 0.44 | 5.9 | 22.3/33.3 | 30.0/19.0 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.059 | 0.42 | 0.58 | 0.00 | 9.27 | 23.5/34.4 | 27.4/18.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| San Jose wins by over 1.5 goals YES | 25 | 0.310 | 0.278 | +0.047 | +0.015 | $3.18 | FUNDED_RESEARCH | $1 | SJS:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 1.5 goals NO | 67 | 0.740 | 0.700 | +0.055 | +0.015 | $6.10 | FUNDED_RESEARCH | $2 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 2.5 goals NO | 78 | 0.837 | 0.803 | +0.044 | +0.011 | $5.81 | FUNDED_RESEARCH | $2 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **San Jose wins by over 1.5 goals YES** — thesis: SJS wins by 2+; alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF2|no; why: higher confidence-adjusted growth (2.35 vs 2.21 bp); despite a smaller raw edge (+0.047 vs +0.055/contract); relationships: KXNHLSPREAD-26OCT27BUFSJ-BUF2|no: DUPLICATIVE (phi 0.397); KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: REINFORCING (phi 0.296); failure: BUF wins (incl. OT/SO)
- **Buffalo wins by over 1.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes has the higher standalone adjusted growth (2.35 vs 2.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.397); they share one thesis budget; relationships: KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes: DUPLICATIVE (phi 0.397); KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: DUPLICATIVE (phi 0.747); failure: BUF wins by 2+
- **Buffalo wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes has the higher standalone adjusted growth (2.35 vs 1.69 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.296); they share one thesis budget; relationships: KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes: REINFORCING (phi 0.296); KXNHLSPREAD-26OCT27BUFSJ-BUF2|no: DUPLICATIVE (phi 0.747); failure: BUF wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis SJS:WINS_BY_2PLUS (p 0.3102): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no (same contract)
- thesis SJS:WINS (p 0.5341): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no (same contract)
- thesis BUF:SUPPRESSED (p 0.3965): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4659, phi -0.626)
- KXNHLSPREAD-26OCT27BUFSJ-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2596, phi -1.0)
- KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2596, phi -0.747)

portfolios: A EV +6.69 (adj +1.73) on $50.00, P(profit) 0.4677, adj growth 4.8 bp · B EV +1.38 (adj +0.39) on $15.08, P(profit) 0.7404, adj growth 3.4 bp · C EV +0.82 (adj +0.25) on $4.57, P(profit) 0.3102, adj growth 2.2 bp · R EV +0.45 (adj +0.13) on $5.00, P(profit) 0.7404, adj growth 4.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
