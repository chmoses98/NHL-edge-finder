# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-08T08:54:07Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 70.00 | +16.45 | +2.78 | +26.67 | 0.530 | -43.40 | -70.00 | 13.50 |
| B thesis-diversified (joint) ← optimiser card | 25.40 | +4.98 | +1.33 | -2.11 | 0.454 | -25.39 | -25.39 | 11.67 |
| C best expression per thesis | 24.93 | +5.97 | +1.85 | -1.64 | 0.423 | -24.92 | -24.92 | 16.05 |
| R FUNDED research stakes | 8.00 | +1.60 | +0.43 | -0.82 | 0.454 | -8.00 | -8.00 | 0.00 |

## UTA @ BOS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_UTA_win | p_overtime | goals | shots BOS/UTA | BOS/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.55 | 0.45 | 0.00 | 6.07 | 27.4/27.7 | 24.4/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.49 | 5.93 | 27.4/27.6 | 24.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.51 | 0.49 | 0.00 | 9.28 | 28.7/29.1 | 23.1/22.4 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.091 | 0.44 | 0.56 | 0.00 | 6.06 | 21.6/32.7 | 28.6/18.5 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.43 | 0.57 | 0.45 | 5.92 | 21.9/33.0 | 29.5/18.7 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.063 | 0.43 | 0.57 | 0.00 | 9.16 | 23.2/34.5 | 27.6/18.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_DAL_win | p_overtime | goals | shots BUF/DAL | BUF/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.56 | 0.43 | 0.00 | 6.02 | 26.5/26.4 | 23.1/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.47 | 5.92 | 26.6/26.3 | 23.1/23.3 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.083 | 0.63 | 0.37 | 0.00 | 6.03 | 31.4/20.9 | 18.1/27.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.56 | 0.44 | 0.00 | 9.33 | 28.0/27.9 | 22.3/21.5 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.52 | 0.48 | 0.47 | 5.85 | 31.4/21.1 | 17.9/28.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.54 | 0.46 | 0.00 | 3.53 | 25.6/25.6 | 23.7/23.6 | late empty net |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_NSH_win | p_overtime | goals | shots MTL/NSH | MTL/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.61 | 0.39 | 0.00 | 6.04 | 27.9/27.8 | 24.8/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.54 | 0.46 | 0.46 | 5.93 | 27.9/27.9 | 24.7/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.60 | 0.40 | 0.00 | 9.34 | 29.4/29.4 | 24.0/22.6 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.072 | 0.55 | 0.45 | 0.00 | 6.0 | 22.2/32.8 | 29.3/18.8 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.068 | 0.70 | 0.30 | 0.00 | 6.02 | 32.5/22.1 | 19.7/27.8 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.58 | 0.42 | 0.46 | 5.96 | 32.8/22.3 | 19.2/29.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PHI @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_PHI_win | p_overtime | goals | shots OTT/PHI | OTT/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.134 | 0.64 | 0.36 | 0.00 | 5.99 | 32.0/20.6 | 17.7/27.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.53 | 0.47 | 0.49 | 5.88 | 32.0/20.6 | 17.4/28.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.57 | 0.43 | 0.00 | 6.02 | 26.7/26.0 | 22.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.51 | 0.49 | 0.47 | 5.93 | 26.7/26.1 | 22.8/23.4 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.081 | 0.69 | 0.31 | 0.00 | 9.16 | 33.8/21.8 | 17.1/26.4 | even strength |
| OTT shot control · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.46 | 2.79 | 30.4/19.2 | 17.9/28.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_MIN_win | p_overtime | goals | shots TBL/MIN | TBL/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.54 | 0.46 | 0.00 | 6.02 | 28.1/27.7 | 24.3/24.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.50 | 5.9 | 28.0/27.5 | 24.2/24.7 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.103 | 0.60 | 0.40 | 0.00 | 6.02 | 33.4/22.1 | 19.0/29.4 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.56 | 0.44 | 0.50 | 5.96 | 33.6/22.4 | 19.3/30.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.51 | 0.49 | 0.00 | 9.35 | 29.6/29.1 | 22.9/23.1 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.068 | 0.63 | 0.37 | 0.00 | 9.22 | 34.7/23.0 | 18.1/27.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ CAR  ·  10000 joint draws  ·  98 bet sides mapped, 5 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_VAN_win | p_overtime | goals | shots CAR/VAN | CAR/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.173 | 0.72 | 0.28 | 0.00 | 6.02 | 33.8/20.6 | 18.1/29.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.147 | 0.54 | 0.46 | 0.46 | 5.97 | 34.2/20.8 | 17.6/30.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.138 | 0.72 | 0.28 | 0.00 | 9.35 | 35.5/21.9 | 17.4/27.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.078 | 0.61 | 0.39 | 0.00 | 6.04 | 27.7/26.7 | 23.6/23.7 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.072 | 0.66 | 0.34 | 0.00 | 3.46 | 32.7/19.4 | 17.9/30.3 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.068 | 0.55 | 0.45 | 0.48 | 2.89 | 32.5/19.4 | 18.0/30.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 1.5 goals NO | 47 | 0.610 | 0.512 | +0.122 | +0.025 | $9.81 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver wins by over 1.5 goals YES | 13 | 0.189 | 0.154 | +0.051 | +0.017 | $2.60 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08VANCAR-CAR3|no; why: higher confidence-adjusted growth (5.45 vs 2.60 bp); relationships: KXNHLSPREAD-26OCT08VANCAR-VAN2|yes: DUPLICATIVE (phi 0.386); failure: CAR wins by 2+
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: Broad expression KXNHLSPREAD-26OCT08VANCAR-VAN2|yes selected over broad KXNHLSPREAD-26OCT08VANCAR-VAN3|yes because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.58 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT08VANCAR-CAR2|no: DUPLICATIVE (phi 0.386); failure: CAR wins (incl. OT/SO)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15, CAR shot control · high event (8+) · decided (2+) 0.14.
- thesis VAN:WINS_BY_2PLUS (p 0.1889): highest fidelity KXNHLSPREAD-26OCT08VANCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08VANCAR-CAR2|no (same contract)
- thesis VAN:WINS (p 0.389): highest fidelity KXNHLSPREAD-26OCT08VANCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08VANCAR-CAR2|no (same contract)
- thesis GAME:TIGHT (p 0.4208): highest fidelity KXNHLSPREAD-26OCT08VANCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08VANCAR-CAR2|no (same contract)
- KXNHLSPREAD-26OCT08VANCAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.0 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3903, phi -1.0)
- KXNHLSPREAD-26OCT08VANCAR-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.611, phi -0.605)
- override: Broad expression KXNHLSPREAD-26OCT08VANCAR-VAN2|yes selected over broad KXNHLSPREAD-26OCT08VANCAR-VAN3|yes because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.58 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +14.05 (adj +1.98) on $50.00, P(profit) 0.6097, adj growth 7.0 bp · B EV +3.42 (adj +0.81) on $12.42, P(profit) 0.6097, adj growth 7.1 bp · C EV +4.41 (adj +1.33) on $11.95, P(profit) 0.6097, adj growth 11.5 bp · R EV +1.12 (adj +0.27) on $4.00, P(profit) 0.6097, adj growth 9.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08VANCAR-VAN|yes == KXNHLGAME-26OCT08VANCAR-CAR|no

## CHI @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CHI_win | p_overtime | goals | shots NYI/CHI | NYI/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NYI shot control · normal event (5-7) · decided (2+) | 0.136 | 0.70 | 0.30 | 0.00 | 6.01 | 33.4/21.3 | 18.7/28.8 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.56 | 0.44 | 0.47 | 5.9 | 33.0/21.1 | 17.9/29.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.65 | 0.35 | 0.00 | 6.02 | 27.5/27.1 | 24.2/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.53 | 0.47 | 0.47 | 5.94 | 27.4/26.6 | 23.3/24.1 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.087 | 0.75 | 0.25 | 0.00 | 9.23 | 34.7/22.5 | 18.2/26.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.66 | 0.34 | 0.00 | 9.23 | 29.1/28.2 | 23.0/22.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.14, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_SJS_win | p_overtime | goals | shots STL/SJS | STL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.59 | 0.41 | 0.00 | 6.04 | 26.6/26.3 | 23.2/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.53 | 0.47 | 0.48 | 6.0 | 26.5/26.6 | 23.2/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.61 | 0.39 | 0.00 | 9.34 | 28.2/28.0 | 22.5/21.3 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.089 | 0.65 | 0.35 | 0.00 | 6.03 | 31.6/21.2 | 18.5/27.0 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.52 | 0.48 | 0.43 | 5.93 | 31.4/21.0 | 17.7/27.9 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.063 | 0.69 | 0.31 | 0.00 | 9.2 | 33.2/22.3 | 17.9/25.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_COL_win | p_overtime | goals | shots CGY/COL | CGY/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.133 | 0.33 | 0.67 | 0.00 | 6.04 | 22.7/35.5 | 30.6/19.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.45 | 0.55 | 0.47 | 5.91 | 23.1/35.8 | 32.4/20.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.36 | 0.64 | 0.00 | 6.05 | 28.6/29.6 | 25.3/25.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.49 | 0.51 | 0.47 | 5.9 | 28.9/29.7 | 26.4/25.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.093 | 0.27 | 0.73 | 0.00 | 9.32 | 24.1/37.7 | 28.9/19.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.36 | 0.64 | 0.00 | 9.27 | 30.2/31.0 | 24.0/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins by over 1.5 goals NO | 54 | 0.624 | 0.580 | +0.067 | +0.022 | $12.98 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08COLCGY-COL3|no; why: higher confidence-adjusted growth (4.42 vs 0.98 bp); alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis GAME:TIGHT (p 0.4252): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08COLCGY-COL2|no (same contract)
- KXNHLSPREAD-26OCT08COLCGY-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3756, phi -1.0)

portfolios: A EV +2.40 (adj +0.80) on $20.00, P(profit) 0.6244, adj growth 6.5 bp · B EV +1.56 (adj +0.52) on $12.98, P(profit) 0.6244, adj growth 4.6 bp · C EV +1.56 (adj +0.52) on $12.98, P(profit) 0.6244, adj growth 4.6 bp · R EV +0.48 (adj +0.16) on $4.00, P(profit) 0.6244, adj growth 5.4 bp

## TOR @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TOR_win | p_overtime | goals | shots VGK/TOR | VGK/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.146 | 0.74 | 0.26 | 0.00 | 6.03 | 34.1/21.7 | 19.3/29.2 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.58 | 0.42 | 0.47 | 5.87 | 34.4/21.9 | 18.9/30.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.69 | 0.31 | 0.00 | 6.03 | 28.3/27.6 | 24.7/23.9 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.100 | 0.76 | 0.24 | 0.00 | 9.21 | 35.5/23.1 | 18.9/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.56 | 0.44 | 0.46 | 5.92 | 28.3/27.5 | 24.2/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.71 | 0.29 | 0.00 | 9.31 | 29.9/28.9 | 24.0/22.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.15, VGK shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
