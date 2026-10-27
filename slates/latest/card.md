# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-27T10:58:24Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +19.38 | +5.31 | +1.03 | 0.515 | -80.39 | -98.18 | 16.46 |
| B thesis-diversified (joint) ← optimiser card | 51.73 | +4.64 | +1.43 | +6.92 | 0.710 | -22.06 | -29.38 | 12.55 |
| C best expression per thesis | 44.44 | +5.06 | +1.72 | +5.08 | 0.668 | -22.09 | -22.09 | 14.97 |
| R FUNDED research stakes | 17.00 | +1.65 | +0.50 | +2.52 | 0.594 | -7.45 | -10.84 | 0.00 |

## CBJ @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CBJ_win | p_overtime | goals | shots PHI/CBJ | PHI/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.56 | 0.44 | 0.00 | 5.95 | 26.4/26.6 | 23.2/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.46 | 5.89 | 26.7/26.9 | 23.7/23.5 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.084 | 0.46 | 0.54 | 0.00 | 5.94 | 21.2/31.8 | 28.0/18.0 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.46 | 0.54 | 0.47 | 5.86 | 21.3/32.0 | 28.6/18.0 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.067 | 0.49 | 0.51 | 0.53 | 2.79 | 25.3/25.5 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.066 | 0.58 | 0.42 | 0.00 | 9.04 | 27.7/28.2 | 22.8/21.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, CBJ shot control · normal event (5-7) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ CAR  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_BOS_win | p_overtime | goals | shots CAR/BOS | CAR/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.164 | 0.63 | 0.37 | 0.00 | 6.03 | 34.7/21.4 | 18.5/30.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.144 | 0.53 | 0.47 | 0.47 | 6.02 | 34.4/21.5 | 18.3/30.9 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.135 | 0.65 | 0.35 | 0.00 | 9.39 | 36.2/22.7 | 17.4/28.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.083 | 0.59 | 0.41 | 0.00 | 6.05 | 27.9/26.9 | 23.6/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.59 | 0.41 | 0.00 | 9.4 | 29.9/28.6 | 22.9/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.51 | 0.49 | 0.47 | 6.04 | 28.5/27.4 | 23.9/25.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 8.5 goals scored YES | 19 | 0.241 | 0.213 | +0.040 | +0.012 | $2.76 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | DIRECT (0.74) | EVIDENCE_MIXED | D |
| Boston over 3.5 goals scored YES | 32 | 0.388 | 0.346 | +0.053 | +0.011 | $2.22 | FUNDED_RESEARCH | $1 | BOS:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Full Game: Over 8.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT27BOSCAR-10|yes; why: Broad expression KXNHLTOTAL-26OCT27BOSCAR-9|yes selected over broad KXNHLTOTAL-26OCT27BOSCAR-10|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.74 vs 0.35 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes: REINFORCING (phi 0.456); failure: BOS offense suppressed (<= 2 goals)
- **Boston over 3.5 goals scored YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT27BOSCAR-10|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes selected over broad KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS5|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.54 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLTOTAL-26OCT27BOSCAR-9|yes: REINFORCING (phi 0.456); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis GAME:HIGH_EVENT (p 0.3232): highest fidelity KXNHLTOTAL-26OCT27BOSCAR-9|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT27BOSCAR-10|yes — Broad expression KXNHLTOTAL-26OCT27BOSCAR-9|yes selected over broad KXNHLTOTAL-26OCT27BOSCAR-10|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.74 vs 0.35 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis BOS:OFFENSE_4PLUS (p 0.3778): highest fidelity KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes [STRUCTURAL], best adjusted EV KXNHLTOTAL-26OCT27BOSCAR-10|yes — Broad expression KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes selected over broad KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS5|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.54 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLTOTAL-26OCT27BOSCAR-9|yes: FUNDED_RESEARCH; family MIXED; loses 26% of the draws where the thesis happens; opposing: failure thesis BOS:SUPPRESSED (p 0.4007, phi -0.398)
- KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BOS:SUPPRESSED (p 0.4007, phi -0.651)
- override: Broad expression KXNHLTOTAL-26OCT27BOSCAR-9|yes selected over broad KXNHLTOTAL-26OCT27BOSCAR-10|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.74 vs 0.35 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS4|yes selected over broad KXNHLTEAMTOTAL-26OCT27BOSCAR-BOS5|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.54 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.46 (adj +2.57) on $45.16, P(profit) 0.4404, adj growth 0.1 bp · B EV +0.90 (adj +0.24) on $4.98, P(profit) 0.4404, adj growth 2.1 bp · C EV +1.68 (adj +0.64) on $3.15, P(profit) 0.1143, adj growth 5.5 bp · R EV +0.36 (adj +0.09) on $2.00, P(profit) 0.4404, adj growth 3.0 bp

## LAK @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_LAK_win | p_overtime | goals | shots CHI/LAK | CHI/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.47 | 0.53 | 0.00 | 6.0 | 26.9/27.4 | 23.5/23.5 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.106 | 0.37 | 0.63 | 0.00 | 6.02 | 21.3/32.5 | 28.1/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.48 | 0.52 | 0.46 | 5.91 | 26.8/27.4 | 24.0/23.6 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.44 | 0.56 | 0.47 | 5.81 | 21.5/32.5 | 29.0/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.47 | 0.53 | 0.00 | 9.16 | 28.3/29.0 | 22.7/22.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.47 | 0.53 | 0.00 | 3.46 | 25.4/26.0 | 23.9/23.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MTL @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_MTL_win | p_overtime | goals | shots STL/MTL | STL/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.63 | 0.37 | 0.00 | 6.06 | 27.0/26.8 | 23.9/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.53 | 0.47 | 0.48 | 5.96 | 27.1/27.1 | 23.8/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.61 | 0.39 | 0.00 | 9.35 | 28.5/28.3 | 22.9/21.6 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.086 | 0.67 | 0.33 | 0.00 | 6.06 | 31.7/21.2 | 18.4/27.3 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.55 | 0.45 | 0.48 | 5.89 | 31.4/21.3 | 18.0/27.9 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.061 | 0.56 | 0.44 | 0.00 | 6.05 | 21.5/31.6 | 28.2/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| St. Louis wins by over 1.5 goals YES | 30 | 0.362 | 0.329 | +0.047 | +0.014 | $4.80 | FUNDED_RESEARCH | $2 | STL:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **St. Louis wins by over 1.5 goals YES** — thesis: STL wins by 2+; alternative: KXNHLSPREAD-26OCT27MTLSTL-MTL2|no; why: higher confidence-adjusted growth (1.94 vs 0.24 bp); alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: MTL wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis STL:WINS_BY_2PLUS (p 0.3621): highest fidelity KXNHLSPREAD-26OCT27MTLSTL-STL2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27MTLSTL-STL2|yes (same contract)
- KXNHLSPREAD-26OCT27MTLSTL-STL2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS (p 0.4201, phi -0.641)

portfolios: A EV +2.55 (adj +0.74) on $16.90, P(profit) 0.3621, adj growth 4.1 bp · B EV +0.72 (adj +0.21) on $4.80, P(profit) 0.3621, adj growth 1.8 bp · C EV +0.72 (adj +0.21) on $4.80, P(profit) 0.3621, adj growth 1.8 bp · R EV +0.30 (adj +0.09) on $2.00, P(profit) 0.3621, adj growth 2.8 bp

## NYI @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_NYI_win | p_overtime | goals | shots NSH/NYI | NSH/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.53 | 0.47 | 0.00 | 6.01 | 27.9/28.1 | 24.6/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.46 | 5.94 | 27.8/28.0 | 24.8/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.52 | 0.48 | 0.00 | 9.32 | 29.2/29.5 | 23.5/22.9 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.083 | 0.50 | 0.50 | 0.00 | 6.01 | 22.4/33.3 | 29.4/19.2 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.49 | 0.51 | 0.47 | 5.9 | 22.5/33.2 | 29.8/19.3 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.058 | 0.47 | 0.53 | 0.00 | 9.25 | 23.8/34.9 | 28.0/18.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_NJD_win | p_overtime | goals | shots DAL/NJD | DAL/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.59 | 0.41 | 0.00 | 6.01 | 26.7/26.8 | 23.5/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.49 | 0.51 | 0.48 | 5.85 | 26.9/26.9 | 23.8/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.60 | 0.40 | 0.00 | 9.17 | 28.2/28.4 | 22.9/21.9 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.075 | 0.52 | 0.48 | 0.00 | 5.96 | 21.2/31.4 | 27.9/17.8 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.47 | 0.53 | 0.48 | 5.84 | 21.1/31.4 | 28.0/18.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.57 | 0.43 | 0.00 | 3.46 | 25.5/25.7 | 24.1/23.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## FLA @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_FLA_win | p_overtime | goals | shots WPG/FLA | WPG/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.53 | 0.47 | 0.00 | 5.98 | 26.9/26.9 | 23.6/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.51 | 0.49 | 0.49 | 5.9 | 26.8/27.0 | 23.8/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.54 | 0.46 | 0.00 | 9.13 | 28.4/28.6 | 22.9/22.3 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.47 | 0.53 | 0.48 | 5.88 | 21.3/31.8 | 28.4/18.1 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.070 | 0.52 | 0.48 | 0.00 | 6.01 | 21.6/31.8 | 28.0/18.1 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.55 | 0.46 | 0.45 | 5.8 | 31.4/21.5 | 18.3/28.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 2.5 goals NO | 80 | 0.852 | 0.823 | +0.040 | +0.012 | $18.13 | FUNDED_RESEARCH | $5 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 2.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT27FLAWPG-FLA2|no; why: higher confidence-adjusted growth (2.09 vs 1.14 bp); despite a smaller raw edge (+0.040 vs +0.046/contract); relationships: only recommended bet in this game; failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis WPG:WINS (p 0.5264): highest fidelity KXNHLSPREAD-26OCT27FLAWPG-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27FLAWPG-FLA3|no (same contract)
- KXNHLSPREAD-26OCT27FLAWPG-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2493, phi -0.725)

portfolios: A EV +2.24 (adj +0.58) on $39.09, P(profit) 0.7507, adj growth 3.9 bp · B EV +0.90 (adj +0.27) on $18.13, P(profit) 0.8515, adj growth 2.4 bp · C EV +0.90 (adj +0.27) on $18.13, P(profit) 0.8515, adj growth 2.4 bp · R EV +0.25 (adj +0.07) on $5.00, P(profit) 0.8515, adj growth 2.6 bp

## MIN @ UTA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_MIN_win | p_overtime | goals | shots UTA/MIN | UTA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.61 | 0.39 | 0.00 | 6.03 | 28.4/28.1 | 25.0/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.55 | 0.45 | 0.47 | 5.99 | 28.3/28.3 | 25.0/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.58 | 0.42 | 0.00 | 9.34 | 29.5/29.5 | 23.9/22.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.081 | 0.67 | 0.33 | 0.00 | 6.03 | 33.4/22.2 | 19.5/28.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.58 | 0.42 | 0.47 | 5.92 | 33.7/22.7 | 19.4/30.3 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.061 | 0.66 | 0.34 | 0.00 | 9.32 | 34.7/23.6 | 18.8/27.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_OTT_win | p_overtime | goals | shots VGK/OTT | VGK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.61 | 0.39 | 0.00 | 6.0 | 26.7/26.7 | 23.7/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.46 | 5.88 | 26.6/26.6 | 23.4/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.62 | 0.38 | 0.00 | 9.37 | 28.3/28.4 | 23.1/21.3 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.081 | 0.70 | 0.30 | 0.00 | 6.0 | 31.6/21.0 | 18.5/27.0 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.51 | 0.49 | 0.49 | 5.93 | 31.7/21.3 | 18.1/28.4 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.063 | 0.56 | 0.44 | 0.00 | 5.99 | 21.4/31.6 | 28.2/17.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_VAN_win | p_overtime | goals | shots ANA/VAN | ANA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.150 | 0.69 | 0.31 | 0.00 | 6.07 | 34.0/21.4 | 18.7/29.4 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.138 | 0.69 | 0.31 | 0.00 | 9.45 | 35.9/22.7 | 18.0/27.9 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.56 | 0.44 | 0.47 | 5.98 | 34.5/21.5 | 18.4/31.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.091 | 0.62 | 0.38 | 0.00 | 6.1 | 28.0/26.9 | 23.9/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.60 | 0.40 | 0.00 | 9.53 | 29.6/28.6 | 23.0/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.48 | 0.52 | 0.46 | 5.99 | 28.0/27.0 | 23.7/24.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.15, ANA shot control · high event (8+) · decided (2+) 0.14, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.12.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_BUF_win | p_overtime | goals | shots SJS/BUF | SJS/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.56 | 0.44 | 0.00 | 6.01 | 27.7/27.8 | 24.4/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.47 | 5.96 | 27.7/28.0 | 24.6/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.55 | 0.45 | 0.00 | 9.42 | 29.2/29.4 | 23.5/22.7 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.076 | 0.49 | 0.51 | 0.00 | 6.08 | 22.3/33.1 | 29.5/18.9 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.47 | 0.53 | 0.43 | 5.9 | 22.2/33.1 | 29.8/19.0 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.059 | 0.41 | 0.59 | 0.00 | 9.31 | 23.5/34.7 | 27.7/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Buffalo wins by over 1.5 goals NO | 66 | 0.740 | 0.698 | +0.065 | +0.022 | $9.17 | FUNDED_RESEARCH | $3 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 2.5 goals NO | 77 | 0.837 | 0.801 | +0.054 | +0.018 | $12.60 | FUNDED_RESEARCH | $4 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| San Jose wins by over 1.5 goals YES | 25 | 0.310 | 0.278 | +0.047 | +0.015 | $2.05 | FUNDED_RESEARCH | $1 | SJS:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Buffalo wins by over 1.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no; why: higher confidence-adjusted growth (4.85 vs 4.36 bp); relationships: KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: DUPLICATIVE (phi 0.747); KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes: DUPLICATIVE (phi 0.397); failure: BUF wins by 2+
- **Buffalo wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT27BUFSJ-BUF2|no has the higher standalone adjusted growth (4.85 vs 4.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.747); they share one thesis budget; relationships: KXNHLSPREAD-26OCT27BUFSJ-BUF2|no: DUPLICATIVE (phi 0.747); KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes: REINFORCING (phi 0.296); failure: BUF wins by 2+
- **San Jose wins by over 1.5 goals YES** — thesis: SJS wins by 2+; alternative: KXNHLSPREAD-26OCT27BUFSJ-BUF2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT27BUFSJ-BUF2|no has the higher standalone adjusted growth (4.85 vs 2.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.397); they share one thesis budget; relationships: KXNHLSPREAD-26OCT27BUFSJ-BUF2|no: DUPLICATIVE (phi 0.397); KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: REINFORCING (phi 0.296); failure: BUF wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis SJS:WINS (p 0.5341): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no (same contract)
- thesis SJS:WINS_BY_2PLUS (p 0.3102): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no (same contract)
- thesis BUF:SUPPRESSED (p 0.3965): highest fidelity KXNHLSPREAD-26OCT27BUFSJ-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT27BUFSJ-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT27BUFSJ-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2596, phi -1.0)
- KXNHLSPREAD-26OCT27BUFSJ-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.2596, phi -0.747)
- KXNHLSPREAD-26OCT27BUFSJ-SJ2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS (p 0.4659, phi -0.626)

portfolios: A EV +5.14 (adj +1.42) on $48.86, P(profit) 0.3863, adj growth 8.3 bp · B EV +2.12 (adj +0.71) on $23.82, P(profit) 0.7404, adj growth 6.2 bp · C EV +1.76 (adj +0.60) on $18.36, P(profit) 0.7404, adj growth 5.3 bp · R EV +0.74 (adj +0.25) on $8.00, P(profit) 0.7404, adj growth 8.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
