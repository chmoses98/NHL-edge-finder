# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-01T05:40:16Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 147.29 | +22.31 | +6.56 | +10.37 | 0.517 | -80.76 | -102.76 | 27.83 |
| B thesis-diversified (joint) ← optimiser card | 56.65 | +6.10 | +2.00 | +8.24 | 0.572 | -23.02 | -34.88 | 17.61 |
| C best expression per thesis | 33.36 | +4.83 | +1.62 | +4.47 | 0.590 | -23.89 | -33.35 | 14.33 |
| R FUNDED research stakes | 18.00 | +2.13 | +0.69 | +1.56 | 0.594 | -7.83 | -11.53 | 0.00 |

## WPG @ CAR  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WPG_win | p_overtime | goals | shots CAR/WPG | CAR/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.167 | 0.74 | 0.26 | 0.00 | 6.01 | 33.6/20.7 | 18.4/28.6 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.140 | 0.57 | 0.43 | 0.45 | 5.91 | 33.7/21.0 | 17.9/30.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.120 | 0.76 | 0.24 | 0.00 | 9.33 | 35.4/22.3 | 18.0/26.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.092 | 0.67 | 0.33 | 0.00 | 6.0 | 27.6/26.6 | 23.9/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.52 | 0.48 | 0.45 | 6.0 | 27.7/26.7 | 23.3/24.3 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.075 | 0.71 | 0.29 | 0.00 | 3.44 | 32.3/19.7 | 18.5/29.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Winnipeg over 3.5 goals scored YES | 24 | 0.301 | 0.266 | +0.049 | +0.013 | $2.90 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 1.5 goals NO | 52 | 0.587 | 0.551 | +0.049 | +0.013 | $5.10 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Winnipeg over 3.5 goals scored YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG5|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes selected over broad KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV01WPGCAR-CAR2|no: REINFORCING (phi 0.41); failure: WPG offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV01WPGCAR-CAR3|no; why: higher confidence-adjusted growth (1.60 vs 0.52 bp); alternative not eligible: confidence-adjusted EV +0.0072 below the 0.010/contract floor; relationships: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes: REINFORCING (phi 0.41); failure: CAR wins by 2+

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.12.
- thesis WPG:OFFENSE_4PLUS (p 0.2935): highest fidelity KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01WPGCAR-CAR2|no — Broad expression KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes selected over broad KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:TIGHT (p 0.4137): highest fidelity KXNHLSPREAD-26NOV01WPGCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01WPGCAR-CAR2|no (same contract)
- KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:SUPPRESSED (p 0.4925, phi -0.647)
- KXNHLSPREAD-26NOV01WPGCAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.4131, phi -1.0)
- override: Broad expression KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes selected over broad KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.06 (adj +2.53) on $47.29, P(profit) 0.3013, adj growth 2.8 bp · B EV +1.02 (adj +0.28) on $7.99, P(profit) 0.6187, adj growth 2.4 bp · C EV +1.29 (adj +0.37) on $7.30, P(profit) 0.5938, adj growth 3.2 bp · R EV +0.38 (adj +0.10) on $3.00, P(profit) 0.6187, adj growth 3.3 bp

## MIN @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_MIN_win | p_overtime | goals | shots WSH/MIN | WSH/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.57 | 0.43 | 0.00 | 6.03 | 28.2/28.3 | 25.1/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.46 | 5.93 | 28.3/28.5 | 25.2/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 9.27 | 29.7/29.9 | 24.4/23.0 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.076 | 0.52 | 0.48 | 0.00 | 6.04 | 22.7/33.6 | 30.1/19.2 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.47 | 0.53 | 0.46 | 5.86 | 22.3/33.4 | 30.0/19.1 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.059 | 0.63 | 0.37 | 0.00 | 6.03 | 33.3/22.8 | 19.9/29.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_UTA_win | p_overtime | goals | shots PHI/UTA | PHI/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.52 | 0.48 | 0.00 | 6.0 | 26.6/27.0 | 23.5/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.49 | 0.51 | 0.48 | 5.92 | 26.4/26.9 | 23.7/23.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.092 | 0.44 | 0.56 | 0.00 | 5.96 | 21.1/31.9 | 27.9/18.0 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.46 | 0.54 | 0.44 | 5.9 | 21.2/31.9 | 28.4/18.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.52 | 0.48 | 0.00 | 9.2 | 27.9/28.3 | 22.4/21.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.52 | 0.48 | 0.00 | 3.46 | 25.2/25.5 | 23.7/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Philadelphia wins by over 1.5 goals YES | 21 | 0.280 | 0.243 | +0.059 | +0.021 | $4.50 | FUNDED_RESEARCH | $2 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Utah wins by over 2.5 goals NO | 76 | 0.831 | 0.790 | +0.058 | +0.018 | $16.82 | FUNDED_RESEARCH | $5 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLSPREAD-26NOV01UTAPHI-UTA3|no; why: higher confidence-adjusted growth (5.54 vs 3.92 bp); relationships: KXNHLSPREAD-26NOV01UTAPHI-UTA3|no: REINFORCING (phi 0.281); failure: UTA wins (incl. OT/SO)
- **Utah wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes has the higher standalone adjusted growth (5.54 vs 3.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.281); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes: REINFORCING (phi 0.281); failure: UTA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:WINS_BY_2PLUS (p 0.2802): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes (same contract)
- thesis PHI:WINS (p 0.5009): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.4141): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS (p 0.4991, phi -0.623)
- KXNHLSPREAD-26NOV01UTAPHI-UTA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2741, phi -0.734)

portfolios: A EV +7.60 (adj +2.27) on $50.00, P(profit) 0.2802, adj growth 13.6 bp · B EV +2.45 (adj +0.81) on $21.32, P(profit) 0.8309, adj growth 7.1 bp · C EV +1.60 (adj +0.57) on $6.06, P(profit) 0.2802, adj growth 5.0 bp · R EV +0.90 (adj +0.30) on $7.00, P(profit) 0.2802, adj growth 9.9 bp

## EDM @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_EDM_win | p_overtime | goals | shots NYR/EDM | NYR/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.47 | 0.53 | 0.00 | 6.07 | 26.9/27.1 | 23.4/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.45 | 5.98 | 27.1/27.6 | 24.3/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.46 | 0.54 | 0.00 | 9.51 | 28.7/29.0 | 22.6/22.7 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.098 | 0.42 | 0.58 | 0.00 | 6.03 | 21.6/32.8 | 28.5/18.6 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.46 | 0.54 | 0.47 | 5.96 | 21.8/32.9 | 29.5/18.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.077 | 0.41 | 0.59 | 0.00 | 9.5 | 23.2/34.7 | 27.5/17.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_OTT_win | p_overtime | goals | shots ANA/OTT | ANA/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.61 | 0.39 | 0.00 | 6.05 | 27.4/27.4 | 24.4/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.54 | 0.46 | 0.49 | 6.01 | 27.7/27.6 | 24.3/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.61 | 0.39 | 0.00 | 9.45 | 29.0/29.0 | 23.4/22.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.081 | 0.67 | 0.33 | 0.00 | 6.01 | 32.0/21.9 | 19.1/27.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.53 | 0.47 | 0.47 | 5.96 | 32.7/22.2 | 19.0/29.3 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.062 | 0.69 | 0.31 | 0.00 | 9.39 | 34.1/23.1 | 18.2/26.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ottawa wins by over 1.5 goals NO | 69 | 0.773 | 0.729 | +0.068 | +0.024 | $13.60 | FUNDED_RESEARCH | $4 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ottawa wins by over 2.5 goals NO | 80 | 0.864 | 0.830 | +0.053 | +0.018 | $11.64 | FUNDED_RESEARCH | $3 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ottawa over 1.5 goals scored NO | 15 | 0.201 | 0.173 | +0.042 | +0.014 | $2.11 | FUNDED_RESEARCH | $1 | OTT:SUPPRESSED | FRAGILE (0.49) | EVIDENCE_MIXED | D |
- **Ottawa wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT3|no; why: higher confidence-adjusted growth (6.16 vs 4.80 bp); relationships: KXNHLSPREAD-26NOV01OTTANA-OTT3|no: DUPLICATIVE (phi 0.733); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no: REINFORCING (phi 0.271); failure: OTT wins by 2+
- **Ottawa wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV01OTTANA-OTT2|no has the higher standalone adjusted growth (6.16 vs 4.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.733); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT2|no: DUPLICATIVE (phi 0.733); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no: REINFORCING (phi 0.199); failure: OTT wins by 2+
- **Ottawa over 1.5 goals scored NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV01OTTANA-OTT2|no has the higher standalone adjusted growth (6.16 vs 3.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.271); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT2|no: REINFORCING (phi 0.271); KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.199); failure: OTT wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis ANA:WINS (p 0.5761): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT2|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4107): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT2|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no kept
- thesis ANA:WINS_BY_2PLUS (p 0.3588): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT2|no (same contract)
- KXNHLSPREAD-26NOV01OTTANA-OTT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2268, phi -1.0)
- KXNHLSPREAD-26NOV01OTTANA-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2268, phi -0.733)
- KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no: FUNDED_RESEARCH; family MIXED; loses 51% of the draws where the thesis happens; opposing: failure thesis OTT:WINS (p 0.4239, phi -0.406)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no kept

portfolios: A EV +5.65 (adj +1.76) on $50.00, P(profit) 0.3588, adj growth 11.4 bp · B EV +2.63 (adj +0.91) on $27.34, P(profit) 0.7732, adj growth 8.1 bp · C EV +1.94 (adj +0.68) on $20.00, P(profit) 0.7732, adj growth 6.1 bp · R EV +0.84 (adj +0.29) on $8.00, P(profit) 0.7732, adj growth 9.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
