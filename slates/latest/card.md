# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-01T06:41:16Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +19.06 | +5.51 | +15.99 | 0.598 | -71.77 | -99.87 | 28.28 |
| B thesis-diversified (joint) ← optimiser card | 59.40 | +7.05 | +2.33 | +8.24 | 0.589 | -25.77 | -35.17 | 20.47 |
| C best expression per thesis | 36.05 | +5.59 | +1.90 | +7.29 | 0.601 | -21.08 | -36.05 | 16.71 |
| R FUNDED research stakes | 20.00 | +2.80 | +0.93 | +1.53 | 0.603 | -9.83 | -10.63 | 0.00 |

## WPG @ CAR  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_WPG_win | p_overtime | goals | shots CAR/WPG | CAR/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.168 | 0.74 | 0.26 | 0.00 | 6.01 | 33.8/20.8 | 18.4/29.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.138 | 0.57 | 0.43 | 0.45 | 5.92 | 33.8/21.0 | 17.8/30.4 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.118 | 0.76 | 0.24 | 0.00 | 9.33 | 35.5/22.3 | 18.0/26.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.092 | 0.66 | 0.34 | 0.00 | 6.02 | 27.6/26.5 | 23.6/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.52 | 0.48 | 0.47 | 5.97 | 27.6/26.5 | 23.2/24.2 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.074 | 0.71 | 0.29 | 0.00 | 3.45 | 32.2/19.7 | 18.5/29.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 1.5 goals NO | 51 | 0.587 | 0.546 | +0.059 | +0.018 | $8.19 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Winnipeg over 3.5 goals scored YES | 24 | 0.301 | 0.266 | +0.049 | +0.013 | $2.20 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV01WPGCAR-CAR3|no; why: higher confidence-adjusted growth (2.99 vs 0.52 bp); alternative not eligible: confidence-adjusted EV +0.0072 below the 0.010/contract floor; relationships: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes: REINFORCING (phi 0.41); failure: CAR wins by 2+
- **Winnipeg over 3.5 goals scored YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG5|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes selected over broad KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV01WPGCAR-CAR2|no: REINFORCING (phi 0.41); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.12.
- thesis WPG:OFFENSE_4PLUS (p 0.2935): highest fidelity KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01WPGCAR-CAR2|no — Broad expression KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes selected over broad KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:TIGHT (p 0.4137): highest fidelity KXNHLSPREAD-26NOV01WPGCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01WPGCAR-CAR2|no (same contract)
- KXNHLSPREAD-26NOV01WPGCAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.4131, phi -1.0)
- KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:SUPPRESSED (p 0.4925, phi -0.647)
- override: Broad expression KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes selected over broad KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG5|yes because adjusted EV is 0.1 pts higher while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +6.60 (adj +1.75) on $50.00, P(profit) 0.4504, adj growth 4.6 bp · B EV +1.35 (adj +0.40) on $10.39, P(profit) 0.5869, adj growth 3.5 bp · C EV +1.61 (adj +0.49) on $9.85, P(profit) 0.5938, adj growth 4.3 bp · R EV +0.53 (adj +0.16) on $4.00, P(profit) 0.5869, adj growth 5.0 bp

## MIN @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_MIN_win | p_overtime | goals | shots WSH/MIN | WSH/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 6.06 | 28.5/28.4 | 25.1/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.46 | 5.96 | 28.3/28.6 | 25.4/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.58 | 0.42 | 0.00 | 9.3 | 29.7/29.7 | 23.9/23.4 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.078 | 0.53 | 0.47 | 0.00 | 6.01 | 22.8/33.5 | 29.9/19.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.49 | 0.51 | 0.46 | 5.84 | 22.2/33.0 | 29.6/19.0 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.058 | 0.59 | 0.41 | 0.00 | 6.02 | 33.4/22.9 | 19.8/29.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## UTA @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_UTA_win | p_overtime | goals | shots PHI/UTA | PHI/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.51 | 0.49 | 0.00 | 6.0 | 26.6/26.9 | 23.4/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.47 | 5.93 | 26.4/26.9 | 23.7/23.2 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.093 | 0.44 | 0.56 | 0.00 | 5.98 | 21.1/31.7 | 27.7/18.0 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.44 | 0.56 | 0.45 | 5.88 | 21.1/31.8 | 28.4/18.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.50 | 0.50 | 0.00 | 9.15 | 27.9/28.2 | 22.2/21.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.53 | 0.47 | 0.00 | 3.47 | 25.0/25.1 | 23.2/23.0 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Philadelphia wins by over 1.5 goals YES | 21 | 0.280 | 0.243 | +0.059 | +0.021 | $2.78 | FUNDED_RESEARCH | $1 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Philadelphia over 5.5 goals scored YES | 5 | 0.083 | 0.064 | +0.029 | +0.011 | $1.48 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | FRAGILE (0.32) | EVIDENCE_MIXED | D |
| Utah wins by over 2.5 goals NO | 76 | 0.831 | 0.790 | +0.058 | +0.018 | $16.04 | FUNDED_RESEARCH | $5 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Utah over 1.5 goals scored NO | 15 | 0.196 | 0.171 | +0.037 | +0.012 | $1.36 | FUNDED_RESEARCH | $1 | UTA:SUPPRESSED | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI6|yes; why: higher confidence-adjusted growth (5.54 vs 4.70 bp); wins across more scripts (relative breadth 0.547 vs 0.331); relationships: KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI6|yes: REINFORCING (phi 0.375); KXNHLSPREAD-26NOV01UTAPHI-UTA3|no: REINFORCING (phi 0.281); KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA2|no: REINFORCING (phi 0.46); failure: UTA wins (incl. OT/SO)
- **Philadelphia over 5.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3|yes; why: higher confidence-adjusted growth (4.70 vs 1.55 bp); despite a smaller raw edge (+0.029 vs +0.049/contract); relationships: KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes: REINFORCING (phi 0.375); KXNHLSPREAD-26NOV01UTAPHI-UTA3|no: INTENTIONAL_DIVERSIFIER (phi 0.132); KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA2|no: INTENTIONAL_DIVERSIFIER (phi -0.038); failure: UTA wins (incl. OT/SO)
- **Utah wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes has the higher standalone adjusted growth (5.54 vs 3.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.281); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes: REINFORCING (phi 0.281); KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI6|yes: INTENTIONAL_DIVERSIFIER (phi 0.132); KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA2|no: REINFORCING (phi 0.223); failure: UTA wins by 2+
- **Utah over 1.5 goals scored NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes has the higher standalone adjusted growth (5.54 vs 2.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.460); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes: REINFORCING (phi 0.46); KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI6|yes: INTENTIONAL_DIVERSIFIER (phi -0.038); KXNHLSPREAD-26NOV01UTAPHI-UTA3|no: REINFORCING (phi 0.223); failure: UTA wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, UTA shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:WINS_BY_2PLUS (p 0.2802): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes (same contract)
- thesis PHI:WINS (p 0.5009): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.4141): highest fidelity KXNHLSPREAD-26NOV01UTAPHI-UTA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes — override declined: the joint re-optimisation gives KXNHLSPREAD-26NOV01UTAPHI-UTA2|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA2|no kept
- KXNHLSPREAD-26NOV01UTAPHI-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS (p 0.4991, phi -0.623)
- KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI6|yes: FUNDED_RESEARCH; family MIXED; loses 68% of the draws where the thesis happens; opposing: failure thesis UTA:WINS (p 0.4991, phi -0.279)
- KXNHLSPREAD-26NOV01UTAPHI-UTA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2741, phi -0.734)
- KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA2|no: FUNDED_RESEARCH; family MIXED; loses 53% of the draws where the thesis happens; opposing: failure thesis UTA:WINS (p 0.4991, phi -0.455)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3|yes less than the minimum stake; KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI6|yes kept
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26NOV01UTAPHI-UTA2|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA2|no kept

portfolios: A EV +6.81 (adj +2.00) on $50.00, P(profit) 0.5488, adj growth 12.3 bp · B EV +3.08 (adj +1.02) on $21.67, P(profit) 0.3524, adj growth 8.9 bp · C EV +2.04 (adj +0.73) on $6.20, P(profit) 0.2933, adj growth 6.3 bp · R EV +1.43 (adj +0.48) on $8.00, P(profit) 0.3524, adj growth 14.3 bp

## EDM @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_EDM_win | p_overtime | goals | shots NYR/EDM | NYR/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.48 | 0.52 | 0.00 | 6.07 | 27.2/27.4 | 23.6/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.52 | 0.48 | 0.45 | 5.99 | 27.1/27.5 | 24.2/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.47 | 0.53 | 0.00 | 9.53 | 28.7/29.1 | 22.8/22.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.096 | 0.41 | 0.59 | 0.00 | 6.05 | 21.4/32.6 | 28.4/18.4 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.46 | 0.54 | 0.47 | 5.96 | 21.8/33.0 | 29.6/18.7 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.079 | 0.40 | 0.60 | 0.00 | 9.47 | 23.2/34.6 | 27.3/17.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_OTT_win | p_overtime | goals | shots ANA/OTT | ANA/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.61 | 0.39 | 0.00 | 6.05 | 27.5/27.4 | 24.5/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.48 | 6.04 | 27.5/27.4 | 24.0/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.61 | 0.39 | 0.00 | 9.44 | 29.0/29.2 | 23.6/22.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.076 | 0.65 | 0.35 | 0.00 | 6.01 | 32.3/21.8 | 19.0/27.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.58 | 0.42 | 0.49 | 5.94 | 32.9/22.0 | 18.8/29.4 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.060 | 0.71 | 0.29 | 0.00 | 9.4 | 33.8/23.1 | 18.5/25.4 | even strength |

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
