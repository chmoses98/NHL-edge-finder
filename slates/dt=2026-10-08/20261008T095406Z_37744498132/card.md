# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-08T09:54:06Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +19.86 | +4.37 | +20.16 | 0.658 | -73.25 | -79.73 | 23.96 |
| B thesis-diversified (joint) ← optimiser card | 34.96 | +7.50 | +2.36 | +7.51 | 0.613 | -15.81 | -34.97 | 20.55 |
| C best expression per thesis | 26.53 | +6.32 | +1.98 | -3.24 | 0.423 | -26.52 | -26.52 | 17.17 |
| R FUNDED research stakes | 12.00 | +2.89 | +0.96 | +0.83 | 0.565 | -7.14 | -12.00 | 0.00 |

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

## VAN @ CAR  ·  10000 joint draws  ·  98 bet sides mapped, 13 +EV candidates, 4 on card


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
| Vancouver wins by over 2.5 goals YES | 6 | 0.110 | 0.082 | +0.046 | +0.018 | $1.91 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | DIRECT (0.58) | EVIDENCE_MIXED | D |
| Vancouver wins by over 1.5 goals YES | 12 | 0.189 | 0.152 | +0.061 | +0.025 | $2.37 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 1.5 goals NO | 47 | 0.610 | 0.516 | +0.122 | +0.028 | $2.73 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 60 | 0.733 | 0.643 | +0.116 | +0.026 | $11.82 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 2.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT08VANCAR-VAN2|yes; why: higher confidence-adjusted growth (12.13 vs 11.64 bp); despite a smaller raw edge (+0.046 vs +0.061/contract); relationships: KXNHLSPREAD-26OCT08VANCAR-VAN2|yes: DUPLICATIVE (phi 0.728); KXNHLSPREAD-26OCT08VANCAR-CAR2|no: REINFORCING (phi 0.281); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: REINFORCING (phi 0.212); failure: CAR wins (incl. OT/SO)
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes has the higher standalone adjusted growth (12.13 vs 11.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.728); they share one thesis budget; relationships: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes: DUPLICATIVE (phi 0.728); KXNHLSPREAD-26OCT08VANCAR-CAR2|no: DUPLICATIVE (phi 0.386); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: REINFORCING (phi 0.291); failure: CAR wins (incl. OT/SO)
- **Carolina wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08VANCAR-CAR3|no; why: Broad expression KXNHLSPREAD-26OCT08VANCAR-CAR2|no selected over broad KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes because adjusted EV is 0.8 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes: REINFORCING (phi 0.281); KXNHLSPREAD-26OCT08VANCAR-VAN2|yes: DUPLICATIVE (phi 0.386); KXNHLSPREAD-26OCT08VANCAR-CAR3|no: DUPLICATIVE (phi 0.754); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08VANCAR-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT08VANCAR-CAR2|no has the higher standalone adjusted growth (6.96 vs 6.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.754); they share one thesis budget; relationships: KXNHLSPREAD-26OCT08VANCAR-VAN3|yes: REINFORCING (phi 0.212); KXNHLSPREAD-26OCT08VANCAR-VAN2|yes: REINFORCING (phi 0.291); KXNHLSPREAD-26OCT08VANCAR-CAR2|no: DUPLICATIVE (phi 0.754); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15, CAR shot control · high event (8+) · decided (2+) 0.14.
- thesis VAN:WINS_BY_2PLUS (p 0.1889): highest fidelity KXNHLSPREAD-26OCT08VANCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08VANCAR-CAR2|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3284): highest fidelity KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08VANCAR-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.389): highest fidelity KXNHLSPREAD-26OCT08VANCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08VANCAR-CAR2|no (same contract)
- KXNHLSPREAD-26OCT08VANCAR-VAN3|yes: FUNDED_RESEARCH; family MIXED; loses 42% of the draws where the thesis happens; opposing: failure thesis CAR:WINS (p 0.611, phi -0.44)
- KXNHLSPREAD-26OCT08VANCAR-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.611, phi -0.605)
- KXNHLSPREAD-26OCT08VANCAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.5 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3903, phi -1.0)
- KXNHLSPREAD-26OCT08VANCAR-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.8 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3903, phi -0.754)
- override: Broad expression KXNHLSPREAD-26OCT08VANCAR-CAR2|no selected over broad KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2|yes because adjusted EV is 0.8 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +13.91 (adj +2.49) on $50.00, P(profit) 0.5014, adj growth 13.5 bp · B EV +5.42 (adj +1.67) on $18.82, P(profit) 0.733, adj growth 14.5 bp · C EV +4.76 (adj +1.46) on $13.55, P(profit) 0.6097, adj growth 12.6 bp · R EV +2.02 (adj +0.67) on $6.00, P(profit) 0.6097, adj growth 20.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT08VANCAR-CAR|no == KXNHLGAME-26OCT08VANCAR-VAN|yes

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

## COL @ CGY  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


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
| Colorado wins by over 1.5 goals NO | 54 | 0.624 | 0.580 | +0.067 | +0.022 | $6.35 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 67 | 0.745 | 0.705 | +0.059 | +0.019 | $8.18 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Calgary wins by over 2.5 goals YES | 8 | 0.117 | 0.096 | +0.032 | +0.011 | $1.61 | FUNDED_RESEARCH | $1 | CGY:WINS_BY_2PLUS | DIRECT (0.59) | EVIDENCE_MIXED | D |
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08COLCGY-COL3|no; why: higher confidence-adjusted growth (4.42 vs 3.86 bp); relationships: KXNHLSPREAD-26OCT08COLCGY-COL3|no: DUPLICATIVE (phi 0.755); KXNHLSPREAD-26OCT08COLCGY-CGY3|yes: REINFORCING (phi 0.282); failure: COL wins by 2+
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT08COLCGY-COL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT08COLCGY-COL2|no has the higher standalone adjusted growth (4.42 vs 3.86 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.755); they share one thesis budget; relationships: KXNHLSPREAD-26OCT08COLCGY-COL2|no: DUPLICATIVE (phi 0.755); KXNHLSPREAD-26OCT08COLCGY-CGY3|yes: REINFORCING (phi 0.213); failure: COL wins by 2+
- **Calgary wins by over 2.5 goals YES** — thesis: CGY wins by 2+; alternative: KXNHLSPREAD-26OCT08COLCGY-COL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT08COLCGY-COL2|no has the higher standalone adjusted growth (4.42 vs 3.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.282); they share one thesis budget; relationships: KXNHLSPREAD-26OCT08COLCGY-COL2|no: REINFORCING (phi 0.282); KXNHLSPREAD-26OCT08COLCGY-COL3|no: REINFORCING (phi 0.213); failure: COL wins (incl. OT/SO)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis GAME:TIGHT (p 0.4252): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08COLCGY-COL2|no (same contract)
- thesis CGY:WINS_BY_2PLUS (p 0.1992): highest fidelity KXNHLSPREAD-26OCT08COLCGY-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08COLCGY-COL2|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.3192): highest fidelity KXNHLTEAMTOTAL-26OCT08COLCGY-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT08COLCGY-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT08COLCGY-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3756, phi -1.0)
- KXNHLSPREAD-26OCT08COLCGY-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3756, phi -0.755)
- KXNHLSPREAD-26OCT08COLCGY-CGY3|yes: FUNDED_RESEARCH; family MIXED; loses 41% of the draws where the thesis happens; opposing: failure thesis COL:WINS (p 0.6054, phi -0.45)

portfolios: A EV +5.96 (adj +1.88) on $50.00, P(profit) 0.6371, adj growth 10.5 bp · B EV +2.07 (adj +0.69) on $16.14, P(profit) 0.6244, adj growth 6.0 bp · C EV +1.56 (adj +0.52) on $12.98, P(profit) 0.6244, adj growth 4.6 bp · R EV +0.87 (adj +0.29) on $6.00, P(profit) 0.6244, adj growth 9.1 bp

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
