# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-01T07:53:13Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +19.38 | +5.80 | +18.51 | 0.583 | -72.30 | -94.83 | 33.65 |
| B thesis-diversified (joint) ← optimiser card | 82.05 | +9.50 | +4.10 | +6.60 | 0.613 | -30.79 | -41.47 | 35.76 |
| C best expression per thesis | 53.00 | +5.96 | +2.25 | +6.72 | 0.726 | -24.62 | -26.90 | 19.89 |
| R FUNDED research stakes | 22.00 | +2.35 | +0.86 | +2.94 | 0.601 | -8.04 | -11.40 | 0.00 |

## WPG @ CAR  ·  10000 joint draws  ·  358 bet sides mapped, 8 +EV candidates, 4 on card


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
| Alex Iafallo: 1+ goals YES | 10 | 0.146 | 0.131 | +0.040 | +0.025 | $5.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Nikolaj Ehlers: 1+ goals NO | 71 | 0.761 | 0.746 | +0.037 | +0.021 | $19.01 | FUNDED_RESEARCH | $5 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 51 | 0.587 | 0.546 | +0.059 | +0.018 | $5.04 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mark Scheifele: 1+ goals YES | 27 | 0.308 | 0.295 | +0.025 | +0.011 | $3.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG5|yes; why: higher confidence-adjusted growth (13.61 vs 3.06 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.948 vs 0.62); relationships: KXNHLGOAL-26NOV01WPGCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26NOV01WPGCAR-CAR2|no: MOSTLY_INDEPENDENT (phi 0.11); KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: WPG offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV01WPGCAR-CAR2|no; why: higher confidence-adjusted growth (5.09 vs 2.99 bp); despite a smaller raw edge (+0.037 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.017 vs 0.857); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26NOV01WPGCAR-CAR2|no: MOSTLY_INDEPENDENT (phi 0.142); KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CAR offense succeeds (4+ goals)
- **Carolina wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV01WPGCAR-CAR3|no; why: higher confidence-adjusted growth (2.99 vs 2.08 bp); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.11); KXNHLGOAL-26NOV01WPGCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.142); KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes: REINFORCING (phi 0.188); failure: CAR wins by 2+
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG5|yes; why: KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG5|yes has the higher standalone adjusted growth (3.06 vs 1.36 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.220); relationships: KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV01WPGCAR-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26NOV01WPGCAR-CAR2|no: REINFORCING (phi 0.188); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.12.
- thesis CAR:SUPPRESSED (p 0.2975): highest fidelity KXNHLSPREAD-26NOV01WPGCAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV01WPGCAR-CARNEHLERS27-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.2935): highest fidelity KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01WPGCAR-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4137): highest fidelity KXNHLSPREAD-26NOV01WPGCAR-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01WPGCAR-CAR2|no (same contract)
- KXNHLGOAL-26NOV01WPGCAR-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4925, phi -0.182)
- KXNHLGOAL-26NOV01WPGCAR-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4943, phi -0.19)
- KXNHLSPREAD-26NOV01WPGCAR-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.4131, phi -1.0)
- KXNHLGOAL-26NOV01WPGCAR-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4925, phi -0.284)

portfolios: A EV +5.86 (adj +1.58) on $50.00, P(profit) 0.4504, adj growth 6.4 bp · B EV +4.03 (adj +2.24) on $33.13, P(profit) 0.5907, adj growth 19.4 bp · C EV +2.42 (adj +1.00) on $26.94, P(profit) 0.5134, adj growth 8.8 bp · R EV +0.48 (adj +0.22) on $7.00, P(profit) 0.4765, adj growth 7.6 bp

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

## UTA @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 2 on card


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
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.48 | 0.52 | 0.00 | 6.07 | 27.2/27.4 | 23.6/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.52 | 0.48 | 0.45 | 5.99 | 27.1/27.5 | 24.2/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.47 | 0.53 | 0.00 | 9.53 | 28.7/29.1 | 22.8/22.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.096 | 0.41 | 0.59 | 0.00 | 6.05 | 21.4/32.6 | 28.4/18.4 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.46 | 0.54 | 0.47 | 5.96 | 21.8/33.0 | 29.6/18.7 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.079 | 0.40 | 0.60 | 0.00 | 9.47 | 23.2/34.6 | 27.3/17.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 4 on card


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
| Ottawa wins by over 1.5 goals NO | 69 | 0.773 | 0.729 | +0.068 | +0.024 | $10.68 | FUNDED_RESEARCH | $3 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Anaheim wins by over 1.5 goals YES | 28 | 0.359 | 0.317 | +0.065 | +0.023 | $3.95 | FUNDED_RESEARCH | $1 | ANA:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ottawa wins by over 2.5 goals NO | 80 | 0.864 | 0.830 | +0.053 | +0.018 | $11.64 | FUNDED_RESEARCH | $3 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ottawa over 1.5 goals scored NO | 15 | 0.201 | 0.173 | +0.042 | +0.014 | $1.33 | FUNDED_RESEARCH | $1 | OTT:SUPPRESSED | FRAGILE (0.49) | EVIDENCE_MIXED | D |
- **Ottawa wins by over 1.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-ANA2|yes; why: higher confidence-adjusted growth (6.16 vs 5.44 bp); wins across more scripts (relative breadth 0.998 vs 0.518); relationships: KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: DUPLICATIVE (phi 0.405); KXNHLSPREAD-26NOV01OTTANA-OTT3|no: DUPLICATIVE (phi 0.733); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no: REINFORCING (phi 0.271); failure: OTT wins by 2+
- **Anaheim wins by over 1.5 goals YES** — thesis: ANA wins by 2+; alternative: KXNHLSPREAD-26NOV01OTTANA-OTT2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV01OTTANA-OTT2|no has the higher standalone adjusted growth (6.16 vs 5.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.405); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT2|no: DUPLICATIVE (phi 0.405); KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.297); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no: REINFORCING (phi 0.438); failure: OTT wins (incl. OT/SO)
- **Ottawa wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV01OTTANA-OTT2|no has the higher standalone adjusted growth (6.16 vs 4.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.733); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT2|no: DUPLICATIVE (phi 0.733); KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: REINFORCING (phi 0.297); KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no: REINFORCING (phi 0.199); failure: OTT wins by 2+
- **Ottawa over 1.5 goals scored NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV01OTTANA-OTT2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV01OTTANA-OTT2|no has the higher standalone adjusted growth (6.16 vs 3.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.271); they share one thesis budget; relationships: KXNHLSPREAD-26NOV01OTTANA-OTT2|no: REINFORCING (phi 0.271); KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: REINFORCING (phi 0.438); KXNHLSPREAD-26NOV01OTTANA-OTT3|no: REINFORCING (phi 0.199); failure: OTT wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis ANA:WINS (p 0.5761): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT2|no (same contract)
- thesis ANA:WINS_BY_2PLUS (p 0.3588): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT2|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4107): highest fidelity KXNHLSPREAD-26NOV01OTTANA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV01OTTANA-OTT2|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no kept
- KXNHLSPREAD-26NOV01OTTANA-OTT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2268, phi -1.0)
- KXNHLSPREAD-26NOV01OTTANA-ANA2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS (p 0.4239, phi -0.642)
- KXNHLSPREAD-26NOV01OTTANA-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2268, phi -0.733)
- KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no: FUNDED_RESEARCH; family MIXED; loses 51% of the draws where the thesis happens; opposing: failure thesis OTT:WINS (p 0.4239, phi -0.406)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2|no kept

portfolios: A EV +5.92 (adj +1.95) on $50.00, P(profit) 0.6172, adj growth 13.6 bp · B EV +3.01 (adj +1.05) on $27.60, P(profit) 0.7732, adj growth 9.2 bp · C EV +1.94 (adj +0.68) on $20.00, P(profit) 0.7732, adj growth 6.1 bp · R EV +0.97 (adj +0.34) on $8.00, P(profit) 0.4034, adj growth 11.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
