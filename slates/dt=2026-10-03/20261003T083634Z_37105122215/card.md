# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T08:36:34Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +30.18 | +8.97 | +23.24 | 0.577 | -92.01 | -124.21 | 42.27 |
| B thesis-diversified (joint) ← optimiser card | 33.95 | +4.30 | +1.45 | +3.11 | 0.589 | -16.27 | -22.58 | 13.15 |
| C best expression per thesis | 43.88 | +7.41 | +2.69 | +2.62 | 0.710 | -22.09 | -22.09 | 23.42 |
| R FUNDED research stakes | 12.00 | +1.75 | +0.60 | +2.47 | 0.605 | -6.66 | -7.65 | 0.00 |

## CHI @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_CHI_win | p_overtime | goals | shots BUF/CHI | BUF/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.135 | 0.74 | 0.26 | 0.00 | 6.02 | 33.4/21.3 | 18.9/28.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.66 | 0.34 | 0.00 | 6.02 | 28.0/27.4 | 24.6/23.7 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.57 | 0.43 | 0.46 | 5.88 | 33.5/21.7 | 18.6/30.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.58 | 0.42 | 0.45 | 5.94 | 27.9/27.3 | 24.0/24.5 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.093 | 0.73 | 0.27 | 0.00 | 9.31 | 35.0/22.7 | 18.3/26.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.67 | 0.33 | 0.00 | 9.25 | 29.5/28.8 | 23.6/22.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_OTT_win | p_overtime | goals | shots TOR/OTT | TOR/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.135 | 0.40 | 0.60 | 0.00 | 5.99 | 21.7/34.3 | 30.1/18.8 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.47 | 0.53 | 0.46 | 5.82 | 21.9/34.4 | 31.1/18.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.102 | 0.52 | 0.48 | 0.00 | 6.02 | 27.5/28.2 | 24.8/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.50 | 0.50 | 0.46 | 5.86 | 27.5/28.3 | 25.0/24.2 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.084 | 0.39 | 0.61 | 0.00 | 9.13 | 23.1/35.5 | 28.2/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.46 | 0.54 | 0.00 | 9.21 | 29.2/30.0 | 23.6/23.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.14, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WSH_win | p_overtime | goals | shots TBL/WSH | TBL/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.63 | 0.37 | 0.00 | 6.02 | 26.9/26.5 | 23.4/22.9 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.113 | 0.67 | 0.33 | 0.00 | 6.01 | 32.5/21.1 | 18.5/28.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.54 | 0.46 | 0.45 | 5.94 | 27.0/26.6 | 23.3/23.7 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.55 | 0.45 | 0.48 | 5.9 | 32.4/21.4 | 18.2/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.63 | 0.37 | 0.00 | 9.22 | 28.7/28.1 | 23.0/21.7 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.070 | 0.68 | 0.32 | 0.00 | 9.32 | 34.3/22.8 | 18.1/26.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CAR_win | p_overtime | goals | shots PHI/CAR | PHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.124 | 0.45 | 0.55 | 0.00 | 5.97 | 20.5/32.0 | 28.1/17.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.48 | 0.52 | 0.49 | 5.91 | 20.5/32.0 | 28.7/17.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.54 | 0.46 | 0.00 | 5.97 | 25.6/26.3 | 22.9/21.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.50 | 0.50 | 0.48 | 5.89 | 25.9/26.7 | 23.3/22.7 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.076 | 0.47 | 0.53 | 0.00 | 3.47 | 19.5/31.0 | 29.0/17.8 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.072 | 0.42 | 0.58 | 0.00 | 9.08 | 21.9/33.9 | 27.3/16.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MTL @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_MTL_win | p_overtime | goals | shots PIT/MTL | PIT/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| PIT shot control · normal event (5-7) · decided (2+) | 0.130 | 0.63 | 0.37 | 0.00 | 6.04 | 32.6/21.1 | 18.3/28.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.60 | 0.40 | 0.00 | 6.05 | 27.4/26.7 | 23.6/23.3 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.55 | 0.45 | 0.51 | 5.93 | 33.1/21.5 | 18.4/29.8 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.100 | 0.68 | 0.32 | 0.00 | 9.38 | 34.5/22.5 | 17.9/26.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.56 | 0.44 | 0.00 | 9.35 | 28.9/28.3 | 22.4/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.52 | 0.48 | 0.47 | 5.93 | 27.2/26.6 | 23.4/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Montreal wins NO | 47 | 0.564 | 0.514 | +0.076 | +0.027 | $8.01 | FUNDED_RESEARCH | $3 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pittsburgh wins by over 1.5 goals YES | 27 | 0.348 | 0.307 | +0.064 | +0.023 | $3.56 | FUNDED_RESEARCH | $1 | PIT:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Montreal wins by over 2.5 goals NO | 80 | 0.854 | 0.824 | +0.042 | +0.013 | $7.36 | FUNDED_RESEARCH | $2 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Montreal wins NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes; why: KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes has the higher standalone adjusted growth (9.46 vs 6.39 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.485); relationships: KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes: DUPLICATIVE (phi 0.643); KXNHLSPREAD-26OCT03MTLPIT-MTL3|no: DUPLICATIVE (phi 0.471); failure: MTL wins (incl. OT/SO)
- **Pittsburgh wins by over 1.5 goals YES** — thesis: PIT wins by 2+; alternative: KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes; why: Broad expression KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes selected over broad KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.67 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGAME-26OCT03MTLPIT-MTL|no: DUPLICATIVE (phi 0.643); KXNHLSPREAD-26OCT03MTLPIT-MTL3|no: DUPLICATIVE (phi 0.303); failure: MTL wins (incl. OT/SO)
- **Montreal wins by over 2.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes; why: KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes has the higher standalone adjusted growth (9.46 vs 2.47 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.229); relationships: KXNHLGAME-26OCT03MTLPIT-MTL|no: DUPLICATIVE (phi 0.471); KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes: DUPLICATIVE (phi 0.303); failure: MTL wins by 2+

**Review**: scripts PIT shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, PIT shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:WINS_BY_2PLUS (p 0.3482): highest fidelity KXNHLGAME-26OCT03MTLPIT-PIT|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03MTLPIT-PIT|yes (same contract)
- thesis PIT:WINS (p 0.5639): highest fidelity KXNHLGAME-26OCT03MTLPIT-PIT|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03MTLPIT-PIT|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4736): highest fidelity KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT3|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03MTLPIT-PIT|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGAME-26OCT03MTLPIT-MTL|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS (p 0.4361, phi -1.0)
- KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS (p 0.4361, phi -0.643)
- KXNHLSPREAD-26OCT03MTLPIT-MTL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.2383, phi -0.74)
- override: Broad expression KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes selected over broad KXNHLSPREAD-26OCT03MTLPIT-PIT3|yes because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.67 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +12.63 (adj +4.68) on $50.00, P(profit) 0.3482, adj growth 19.1 bp · B EV +2.45 (adj +0.85) on $18.93, P(profit) 0.5639, adj growth 7.4 bp · C EV +2.41 (adj +0.93) on $6.37, P(profit) 0.2335, adj growth 8.1 bp · R EV +0.80 (adj +0.28) on $6.00, P(profit) 0.5639, adj growth 9.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03MTLPIT-PIT|yes == KXNHLGAME-26OCT03MTLPIT-MTL|no

## UTA @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_UTA_win | p_overtime | goals | shots CBJ/UTA | CBJ/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.55 | 0.45 | 0.00 | 6.01 | 27.4/27.3 | 24.0/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.49 | 5.9 | 27.4/27.3 | 24.0/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.54 | 0.46 | 0.00 | 9.38 | 29.1/29.0 | 22.8/22.4 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.082 | 0.59 | 0.41 | 0.00 | 5.97 | 32.5/22.0 | 18.9/28.4 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.56 | 0.44 | 0.47 | 5.89 | 32.5/22.1 | 18.9/28.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.056 | 0.56 | 0.44 | 0.00 | 3.44 | 26.2/26.2 | 24.3/24.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_SEA_win | p_overtime | goals | shots EDM/SEA | EDM/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.127 | 0.73 | 0.27 | 0.00 | 6.02 | 33.9/22.0 | 19.5/29.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.67 | 0.33 | 0.00 | 6.06 | 28.2/27.7 | 24.8/23.6 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.59 | 0.41 | 0.49 | 5.92 | 33.9/22.3 | 19.1/30.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.100 | 0.69 | 0.31 | 0.00 | 9.34 | 35.8/23.5 | 18.9/27.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.52 | 0.48 | 0.50 | 5.96 | 28.2/27.8 | 24.3/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.65 | 0.35 | 0.00 | 9.39 | 30.0/29.2 | 24.0/22.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, EDM shot control · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ NYI  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_NJD_win | p_overtime | goals | shots NYI/NJD | NYI/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.55 | 0.45 | 0.00 | 5.95 | 27.8/27.9 | 24.6/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.43 | 5.9 | 27.8/28.0 | 24.7/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.52 | 0.48 | 0.00 | 9.16 | 29.4/29.5 | 23.8/23.2 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.069 | 0.53 | 0.47 | 0.00 | 5.96 | 22.1/32.7 | 29.2/18.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.48 | 0.52 | 0.46 | 5.87 | 22.4/33.0 | 29.7/19.4 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.068 | 0.60 | 0.40 | 0.00 | 5.98 | 32.7/22.5 | 19.6/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 1.5 goals NO | 68 | 0.754 | 0.715 | +0.059 | +0.019 | $5.99 | FUNDED_RESEARCH | $2 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03NJNYI-NJ|no; why: higher confidence-adjusted growth (3.85 vs 2.58 bp); relationships: only recommended bet in this game; failure: NJD wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.07.
- thesis NYI:WINS (p 0.5341): highest fidelity KXNHLSPREAD-26OCT03NJNYI-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03NJNYI-NJ2|no (same contract)
- thesis NJD:SUPPRESSED (p 0.4655): highest fidelity KXNHLSPREAD-26OCT03NJNYI-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03NJNYI-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT03NJNYI-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.246, phi -1.0)

portfolios: A EV +5.80 (adj +1.71) on $50.00, P(profit) 0.5903, adj growth 8.6 bp · B EV +0.51 (adj +0.17) on $5.99, P(profit) 0.754, adj growth 1.6 bp · C EV +1.45 (adj +0.48) on $17.18, P(profit) 0.754, adj growth 4.2 bp · R EV +0.17 (adj +0.06) on $2.00, P(profit) 0.754, adj growth 2.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03NJNYI-NYI|yes == KXNHLGAME-26OCT03NJNYI-NJ|no

## DAL @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_DAL_win | p_overtime | goals | shots NSH/DAL | NSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.50 | 0.50 | 0.00 | 6.01 | 26.9/27.2 | 23.7/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.47 | 5.96 | 26.8/27.0 | 23.6/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.47 | 0.53 | 0.00 | 9.33 | 28.5/28.8 | 22.6/22.4 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.079 | 0.42 | 0.58 | 0.00 | 5.93 | 21.5/32.2 | 28.1/18.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.48 | 0.52 | 0.46 | 5.88 | 21.6/32.4 | 29.2/18.5 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.062 | 0.58 | 0.42 | 0.00 | 6.01 | 31.8/21.7 | 18.5/27.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ MIN  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_BOS_win | p_overtime | goals | shots MIN/BOS | MIN/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.59 | 0.41 | 0.00 | 6.02 | 28.6/28.3 | 25.2/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.48 | 5.94 | 28.7/28.6 | 25.3/25.4 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.106 | 0.68 | 0.32 | 0.00 | 6.02 | 34.2/22.7 | 20.1/29.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.63 | 0.37 | 0.00 | 9.35 | 30.6/30.2 | 24.9/23.8 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.56 | 0.44 | 0.45 | 5.92 | 34.5/23.1 | 19.9/31.0 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.074 | 0.72 | 0.28 | 0.00 | 9.32 | 35.8/23.9 | 19.2/27.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, MIN shot control · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 10 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_STL_win | p_overtime | goals | shots COL/STL | COL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.140 | 0.68 | 0.32 | 0.00 | 6.02 | 33.9/21.4 | 18.8/29.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.56 | 0.44 | 0.47 | 5.95 | 34.0/21.7 | 18.5/30.6 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.111 | 0.72 | 0.28 | 0.00 | 9.32 | 36.0/23.0 | 18.5/28.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.100 | 0.62 | 0.38 | 0.00 | 5.97 | 28.0/27.1 | 24.2/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.50 | 0.50 | 0.43 | 5.92 | 28.1/27.2 | 23.9/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.64 | 0.36 | 0.00 | 9.39 | 29.6/28.8 | 23.3/22.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| St. Louis wins by over 1.5 goals YES | 13 | 0.198 | 0.161 | +0.060 | +0.024 | $1.10 | FUNDED_RESEARCH | $1 | STL:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| St. Louis over 1.5 goals scored YES | 70 | 0.783 | 0.736 | +0.068 | +0.022 | $6.03 | FUNDED_RESEARCH | $2 | STL:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 63 | 0.746 | 0.667 | +0.099 | +0.021 | $1.90 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **St. Louis wins by over 1.5 goals YES** — thesis: STL wins by 2+; alternative: KXNHLTEAMTOTAL-26OCT03STLCOL-STL5|yes; why: higher confidence-adjusted growth (9.98 vs 7.64 bp); relationships: KXNHLTEAMTOTAL-26OCT03STLCOL-STL2|yes: REINFORCING (phi 0.262); KXNHLSPREAD-26OCT03STLCOL-COL3|no: REINFORCING (phi 0.29); failure: COL wins (incl. OT/SO)
- **St. Louis over 1.5 goals scored YES** — thesis: STL wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03STLCOL-STL2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT03STLCOL-STL2|yes has the higher standalone adjusted growth (9.98 vs 5.03 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.262); they share one thesis budget; relationships: KXNHLSPREAD-26OCT03STLCOL-STL2|yes: REINFORCING (phi 0.262); KXNHLSPREAD-26OCT03STLCOL-COL3|no: REINFORCING (phi 0.409); failure: STL offense suppressed (<= 2 goals)
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT03STLCOL-STL2|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT03STLCOL-STL2|yes has the higher standalone adjusted growth (5.03 vs 4.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.409); they share one thesis budget; relationships: KXNHLSPREAD-26OCT03STLCOL-STL2|yes: REINFORCING (phi 0.29); KXNHLTEAMTOTAL-26OCT03STLCOL-STL2|yes: REINFORCING (phi 0.409); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.14, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis STL:WINS_BY_2PLUS (p 0.1978): highest fidelity KXNHLSPREAD-26OCT03STLCOL-STL2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03STLCOL-STL2|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3335): highest fidelity KXNHLTEAMTOTAL-26OCT03STLCOL-STL2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03STLCOL-STL2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.3959): highest fidelity KXNHLGAME-26OCT03STLCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03STLCOL-STL2|yes — override declined: the joint re-optimisation gives KXNHLGAME-26OCT03STLCOL-COL|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT03STLCOL-STL2|yes kept
- KXNHLSPREAD-26OCT03STLCOL-STL2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS (p 0.6041, phi -0.613)
- KXNHLTEAMTOTAL-26OCT03STLCOL-STL2|yes: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.59)
- KXNHLSPREAD-26OCT03STLCOL-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.1 pts; opposing: failure thesis COL:WINS_BY_2PLUS (p 0.376, phi -0.752)
- override: override declined: the joint re-optimisation gives KXNHLGAME-26OCT03STLCOL-COL|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT03STLCOL-STL2|yes kept

portfolios: A EV +11.76 (adj +2.58) on $50.00, P(profit) 0.624, adj growth 14.6 bp · B EV +1.34 (adj +0.43) on $9.03, P(profit) 0.6569, adj growth 4.1 bp · C EV +3.54 (adj +1.28) on $20.33, P(profit) 0.7826, adj growth 11.1 bp · R EV +0.78 (adj +0.26) on $4.00, P(profit) 0.6569, adj growth 9.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03STLCOL-STL|yes == KXNHLGAME-26OCT03STLCOL-COL|no

## CGY @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CGY_win | p_overtime | goals | shots VAN/CGY | VAN/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.60 | 0.40 | 0.00 | 6.05 | 28.2/28.0 | 24.8/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.50 | 0.50 | 0.48 | 5.93 | 28.3/28.2 | 25.0/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.63 | 0.37 | 0.00 | 9.34 | 30.0/30.1 | 24.7/23.0 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.068 | 0.56 | 0.44 | 0.00 | 6.06 | 22.5/33.1 | 29.6/18.9 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.065 | 0.65 | 0.35 | 0.00 | 6.04 | 33.2/22.5 | 19.8/28.7 | even strength |
| VAN shot control · normal event (5-7) · tight (1-goal/OT) | 0.056 | 0.56 | 0.44 | 0.48 | 5.91 | 33.2/22.2 | 19.0/29.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## LAK @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_LAK_win | p_overtime | goals | shots SJS/LAK | SJS/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.56 | 0.44 | 0.00 | 6.0 | 27.3/27.4 | 24.1/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.49 | 0.51 | 0.45 | 5.88 | 27.2/27.4 | 24.1/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.54 | 0.46 | 0.00 | 9.29 | 29.2/29.4 | 23.7/22.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.47 | 0.53 | 0.44 | 5.82 | 21.9/32.6 | 29.2/18.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.073 | 0.46 | 0.54 | 0.00 | 5.99 | 22.1/32.9 | 29.1/18.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.52 | 0.48 | 0.00 | 3.45 | 26.1/26.3 | 24.6/24.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
