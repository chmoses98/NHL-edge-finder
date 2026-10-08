# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-08T05:06:53Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 111.68 | +23.44 | +6.36 | +18.46 | 0.642 | -84.65 | -111.68 | 37.80 |
| B thesis-diversified (joint) ← optimiser card | 41.78 | +6.41 | +1.73 | +12.47 | 0.614 | -21.03 | -37.02 | 15.11 |
| C best expression per thesis | 29.81 | +7.07 | +2.22 | +11.34 | 0.516 | -29.80 | -29.80 | 19.22 |
| R FUNDED research stakes | 13.00 | +1.92 | +0.52 | +2.39 | 0.612 | -5.04 | -11.62 | 0.00 |

## UTA @ BOS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_UTA_win | p_overtime | goals | shots BOS/UTA | BOS/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.54 | 0.46 | 0.00 | 6.08 | 27.2/27.5 | 24.0/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.49 | 5.92 | 27.3/27.4 | 24.0/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.51 | 0.49 | 0.00 | 9.3 | 28.7/29.1 | 23.2/22.4 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.092 | 0.44 | 0.56 | 0.00 | 6.04 | 21.7/33.0 | 28.8/18.5 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.45 | 0.55 | 0.46 | 5.93 | 21.9/32.9 | 29.4/18.7 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.063 | 0.44 | 0.56 | 0.00 | 9.18 | 23.3/34.5 | 27.6/18.2 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_DAL_win | p_overtime | goals | shots BUF/DAL | BUF/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.56 | 0.44 | 0.00 | 6.02 | 26.5/26.3 | 23.0/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.52 | 0.48 | 0.46 | 5.91 | 26.5/26.3 | 23.1/23.3 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.084 | 0.63 | 0.37 | 0.00 | 6.02 | 31.3/21.0 | 18.3/27.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.54 | 0.46 | 0.00 | 9.29 | 28.2/27.9 | 22.0/21.9 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.53 | 0.47 | 0.48 | 5.91 | 31.5/21.2 | 18.0/28.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.55 | 0.45 | 0.00 | 3.48 | 25.6/25.3 | 23.5/23.6 | late empty net |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_NSH_win | p_overtime | goals | shots MTL/NSH | MTL/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.61 | 0.39 | 0.00 | 6.04 | 27.8/27.8 | 24.8/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.53 | 0.47 | 0.46 | 5.96 | 27.8/27.9 | 24.7/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.62 | 0.38 | 0.00 | 9.34 | 29.3/29.5 | 24.0/22.5 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.070 | 0.57 | 0.43 | 0.00 | 5.99 | 22.3/32.9 | 29.7/18.8 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.067 | 0.69 | 0.31 | 0.00 | 6.04 | 32.6/22.1 | 19.5/27.7 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.60 | 0.40 | 0.46 | 5.96 | 32.9/22.5 | 19.4/29.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PHI @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_PHI_win | p_overtime | goals | shots OTT/PHI | OTT/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.133 | 0.64 | 0.36 | 0.00 | 6.01 | 32.0/20.6 | 17.8/27.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.53 | 0.47 | 0.47 | 5.88 | 32.1/20.5 | 17.3/28.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.56 | 0.44 | 0.00 | 6.01 | 26.6/25.9 | 22.7/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.50 | 0.50 | 0.48 | 5.93 | 26.8/26.2 | 23.0/23.5 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.082 | 0.68 | 0.32 | 0.00 | 9.16 | 33.8/22.0 | 17.4/26.2 | even strength |
| OTT shot control · low event (<=4) · tight (1-goal/OT) | 0.069 | 0.52 | 0.48 | 0.46 | 2.76 | 30.6/19.4 | 18.0/29.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_MIN_win | p_overtime | goals | shots TBL/MIN | TBL/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.54 | 0.46 | 0.00 | 6.03 | 28.1/27.7 | 24.3/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.53 | 0.47 | 0.50 | 5.9 | 28.0/27.6 | 24.4/24.7 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.101 | 0.60 | 0.40 | 0.00 | 6.01 | 33.5/22.1 | 19.0/29.4 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.55 | 0.45 | 0.50 | 5.95 | 33.6/22.3 | 19.1/30.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.51 | 0.49 | 0.00 | 9.35 | 29.5/29.1 | 22.9/23.1 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.068 | 0.64 | 0.36 | 0.00 | 9.26 | 34.8/23.0 | 18.1/27.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ CAR  ·  10000 joint draws  ·  98 bet sides mapped, 10 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_VAN_win | p_overtime | goals | shots CAR/VAN | CAR/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.174 | 0.71 | 0.29 | 0.00 | 6.01 | 33.9/20.6 | 18.0/29.1 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.146 | 0.54 | 0.46 | 0.46 | 5.96 | 34.0/20.7 | 17.5/30.6 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.134 | 0.71 | 0.29 | 0.00 | 9.36 | 35.4/21.9 | 17.4/27.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.078 | 0.63 | 0.37 | 0.00 | 6.06 | 27.9/26.7 | 23.6/23.7 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.071 | 0.65 | 0.35 | 0.00 | 3.45 | 33.0/19.4 | 17.9/30.6 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.067 | 0.55 | 0.45 | 0.48 | 2.89 | 32.3/19.4 | 17.9/30.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 2.5 goals NO | 60 | 0.733 | 0.643 | +0.116 | +0.026 | $18.59 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 1.5 goals scored YES | 71 | 0.780 | 0.737 | +0.055 | +0.013 | $3.45 | FUNDED_RESEARCH | $1 | VAN:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08VANCAR-CAR2|no; why: KXNHLSPREAD-26OCT08VANCAR-CAR2|no has the higher standalone adjusted growth (6.96 vs 6.52 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.754); relationships: KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes: REINFORCING (phi 0.401); failure: CAR wins by 2+
- **Vancouver over 1.5 goals scored YES** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes selected over broad KXNHLTEAMTOTAL-26OCT08VANCAR-VAN5|yes because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.52 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT08VANCAR-CAR3|no: REINFORCING (phi 0.401); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:WINS_BY_2PLUS (p 0.1889): highest fidelity KXNHLGAME-26OCT08VANCAR-CAR|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT08VANCAR-CAR|no (same contract)
- thesis VAN:WINS (p 0.389): highest fidelity KXNHLGAME-26OCT08VANCAR-CAR|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT08VANCAR-CAR|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3284): highest fidelity KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT08VANCAR-CAR|no — Broad expression KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes selected over broad KXNHLTEAMTOTAL-26OCT08VANCAR-VAN5|yes because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.52 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLSPREAD-26OCT08VANCAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.8 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3903, phi -0.754)
- KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis VAN:SUPPRESSED (p 0.4505, phi -0.587)
- override: Broad expression KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes selected over broad KXNHLTEAMTOTAL-26OCT08VANCAR-VAN5|yes because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.52 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +14.36 (adj +3.41) on $50.00, P(profit) 0.6097, adj growth 21.2 bp · B EV +3.77 (adj +0.86) on $22.04, P(profit) 0.733, adj growth 7.6 bp · C EV +4.76 (adj +1.46) on $13.55, P(profit) 0.6097, adj growth 12.6 bp · R EV +1.02 (adj +0.23) on $6.00, P(profit) 0.733, adj growth 8.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08VANCAR-VAN|yes == KXNHLGAME-26OCT08VANCAR-CAR|no

## CHI @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CHI_win | p_overtime | goals | shots NYI/CHI | NYI/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NYI shot control · normal event (5-7) · decided (2+) | 0.136 | 0.70 | 0.30 | 0.00 | 6.01 | 33.3/21.2 | 18.7/28.4 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.57 | 0.43 | 0.46 | 5.91 | 33.1/21.1 | 17.9/29.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.65 | 0.35 | 0.00 | 6.03 | 27.4/26.9 | 24.0/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.52 | 0.48 | 0.47 | 5.94 | 27.6/26.6 | 23.3/24.2 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.087 | 0.76 | 0.24 | 0.00 | 9.24 | 34.7/22.5 | 18.2/26.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.66 | 0.34 | 0.00 | 9.22 | 28.9/28.1 | 22.9/21.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts NYI shot control · normal event (5-7) · decided (2+) 0.14, NYI shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SJS @ STL  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_SJS_win | p_overtime | goals | shots STL/SJS | STL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.58 | 0.42 | 0.00 | 6.05 | 26.7/26.5 | 23.3/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.53 | 0.47 | 0.47 | 6.01 | 26.5/26.5 | 23.1/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.59 | 0.41 | 0.00 | 9.25 | 28.0/27.8 | 22.3/21.4 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.087 | 0.65 | 0.35 | 0.00 | 6.04 | 31.4/21.1 | 18.3/26.9 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.51 | 0.49 | 0.44 | 5.94 | 31.4/20.8 | 17.7/28.1 | even strength |
| STL shot control · high event (8+) · decided (2+) | 0.062 | 0.71 | 0.29 | 0.00 | 9.26 | 33.3/22.3 | 18.0/25.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Full Game: Over 8.5 goals scored YES | 16 | 0.208 | 0.182 | +0.039 | +0.012 | $3.28 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | DIRECT (0.73) | EVIDENCE_MIXED | D |
- **Full Game: Over 8.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTOTAL-26OCT08SJSTL-6|yes; why: higher confidence-adjusted growth (2.29 vs 0.56 bp); alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis GAME:HIGH_EVENT (p 0.2865): highest fidelity KXNHLTOTAL-26OCT08SJSTL-9|yes [DIRECT], best adjusted EV KXNHLTOTAL-26OCT08SJSTL-9|yes (same contract)
- KXNHLTOTAL-26OCT08SJSTL-9|yes: FUNDED_RESEARCH; family MIXED; loses 27% of the draws where the thesis happens; opposing: failure thesis SJS:SUPPRESSED (p 0.427, phi -0.382)

portfolios: A EV +2.67 (adj +0.84) on $11.68, P(profit) 0.2082, adj growth 4.6 bp · B EV +0.75 (adj +0.24) on $3.28, P(profit) 0.2082, adj growth 2.1 bp · C EV +0.75 (adj +0.24) on $3.28, P(profit) 0.2082, adj growth 2.1 bp · R EV +0.23 (adj +0.07) on $1.00, P(profit) 0.2082, adj growth 2.4 bp

## COL @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_COL_win | p_overtime | goals | shots CGY/COL | CGY/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.135 | 0.34 | 0.66 | 0.00 | 6.04 | 22.8/35.7 | 30.9/20.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.45 | 0.55 | 0.47 | 5.9 | 23.0/35.7 | 32.4/19.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.35 | 0.65 | 0.00 | 6.05 | 28.7/29.7 | 25.3/25.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.49 | 0.51 | 0.48 | 5.92 | 28.9/29.8 | 26.5/25.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.094 | 0.28 | 0.72 | 0.00 | 9.31 | 23.8/37.5 | 28.8/19.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.34 | 0.66 | 0.00 | 9.31 | 30.2/31.0 | 23.8/25.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins by over 1.5 goals NO | 54 | 0.624 | 0.580 | +0.067 | +0.022 | $4.89 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 67 | 0.745 | 0.705 | +0.059 | +0.019 | $8.21 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins NO | 32 | 0.395 | 0.355 | +0.059 | +0.020 | $3.36 | FUNDED_RESEARCH | $1 | CGY:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08COLCGY-COL3|no; why: higher confidence-adjusted growth (4.42 vs 3.86 bp); relationships: KXNHLSPREAD-26OCT08COLCGY-COL3|no: DUPLICATIVE (phi 0.755); KXNHLGAME-26OCT08COLCGY-COL|no: DUPLICATIVE (phi 0.626); failure: COL wins by 2+
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08COLCGY-COL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT08COLCGY-COL2|no has the higher standalone adjusted growth (4.42 vs 3.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.755); they share one thesis budget; relationships: KXNHLSPREAD-26OCT08COLCGY-COL2|no: DUPLICATIVE (phi 0.755); KXNHLGAME-26OCT08COLCGY-COL|no: DUPLICATIVE (phi 0.472); failure: COL wins by 2+
- **Colorado wins NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT08COLCGY-COL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT08COLCGY-COL2|no has the higher standalone adjusted growth (4.42 vs 3.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.626); they share one thesis budget; relationships: KXNHLSPREAD-26OCT08COLCGY-COL2|no: DUPLICATIVE (phi 0.626); KXNHLSPREAD-26OCT08COLCGY-COL3|no: DUPLICATIVE (phi 0.472); failure: COL wins (incl. OT/SO)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis GAME:TIGHT (p 0.4252): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08COLCGY-COL2|no (same contract)
- thesis CGY:WINS (p 0.3946): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08COLCGY-COL2|no (same contract)
- KXNHLSPREAD-26OCT08COLCGY-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3756, phi -1.0)
- KXNHLSPREAD-26OCT08COLCGY-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3756, phi -0.755)
- KXNHLGAME-26OCT08COLCGY-COL|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS (p 0.6054, phi -1.0)

portfolios: A EV +6.40 (adj +2.11) on $50.00, P(profit) 0.6244, adj growth 12.0 bp · B EV +1.89 (adj +0.63) on $16.46, P(profit) 0.6244, adj growth 5.5 bp · C EV +1.56 (adj +0.52) on $12.98, P(profit) 0.6244, adj growth 4.6 bp · R EV +0.68 (adj +0.22) on $6.00, P(profit) 0.6244, adj growth 7.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08COLCGY-CGY|yes == KXNHLGAME-26OCT08COLCGY-COL|no

## TOR @ VGK  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TOR_win | p_overtime | goals | shots VGK/TOR | VGK/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.146 | 0.75 | 0.25 | 0.00 | 6.03 | 34.3/21.6 | 19.3/29.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.58 | 0.42 | 0.47 | 5.91 | 34.5/22.0 | 18.8/31.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.68 | 0.32 | 0.00 | 6.0 | 28.2/27.5 | 24.6/24.0 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.100 | 0.76 | 0.24 | 0.00 | 9.27 | 35.7/22.9 | 18.6/27.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.55 | 0.45 | 0.46 | 5.9 | 28.5/27.5 | 24.2/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.72 | 0.28 | 0.00 | 9.27 | 29.8/29.0 | 24.3/22.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.15, VGK shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
