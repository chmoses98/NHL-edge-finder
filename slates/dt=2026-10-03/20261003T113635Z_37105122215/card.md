# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-03T11:36:35Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +21.23 | +6.56 | +20.77 | 0.640 | -47.64 | -65.22 | 51.67 |
| B thesis-diversified (joint) ← optimiser card | 100.12 | +12.12 | +4.40 | +11.21 | 0.650 | -27.14 | -38.22 | 39.15 |
| C best expression per thesis | 82.39 | +11.48 | +3.89 | +10.25 | 0.613 | -29.96 | -38.75 | 34.07 |
| R FUNDED research stakes | 30.00 | +3.50 | +1.30 | +3.38 | 0.638 | -8.40 | -11.77 | 0.00 |

## CHI @ BUF  ·  10000 joint draws  ·  314 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_CHI_win | p_overtime | goals | shots BUF/CHI | BUF/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.139 | 0.74 | 0.26 | 0.00 | 6.02 | 33.2/21.3 | 19.0/28.4 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.55 | 0.45 | 0.48 | 5.92 | 33.4/21.5 | 18.4/30.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.68 | 0.32 | 0.00 | 6.0 | 27.8/27.1 | 24.2/23.4 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.094 | 0.75 | 0.25 | 0.00 | 9.24 | 35.1/22.7 | 18.6/26.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.53 | 0.47 | 0.46 | 5.89 | 28.1/27.4 | 24.2/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.66 | 0.34 | 0.00 | 9.28 | 29.5/28.5 | 23.5/22.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.14, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## OTT @ TOR  ·  10000 joint draws  ·  344 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_OTT_win | p_overtime | goals | shots TOR/OTT | TOR/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.137 | 0.41 | 0.59 | 0.00 | 5.97 | 21.8/34.3 | 30.1/18.8 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.45 | 0.55 | 0.47 | 5.92 | 21.8/34.2 | 30.7/18.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.46 | 5.91 | 27.5/28.4 | 25.1/24.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.099 | 0.47 | 0.53 | 0.00 | 5.99 | 27.6/28.5 | 24.8/24.2 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.076 | 0.44 | 0.56 | 0.00 | 9.02 | 23.3/35.9 | 28.8/18.1 | even strength |
| OTT shot control · low event (<=4) · tight (1-goal/OT) | 0.072 | 0.48 | 0.52 | 0.49 | 2.78 | 20.5/32.4 | 30.9/19.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Stephen Halliday: 1+ goals YES | 10 | 0.139 | 0.119 | +0.032 | +0.013 | $3.05 | FUNDED_RESEARCH | $1 | OTT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03OTTTOR-TOR3|no; why: higher confidence-adjusted growth (3.64 vs 1.36 bp); despite a smaller raw edge (+0.032 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.14, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis OTT:OFFENSE_4PLUS (p 0.3883): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT03OTTTOR-OTTSHALLIDAY34-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.386, phi -0.159)

portfolios: A EV +1.38 (adj +0.54) on $4.53, P(profit) 0.1386, adj growth 4.3 bp · B EV +0.93 (adj +0.36) on $3.05, P(profit) 0.1386, adj growth 3.1 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.30 (adj +0.12) on $1.00, P(profit) 0.1386, adj growth 3.9 bp

## WSH @ TBL  ·  10000 joint draws  ·  352 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_WSH_win | p_overtime | goals | shots TBL/WSH | TBL/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.67 | 0.33 | 0.00 | 6.03 | 27.1/26.6 | 23.8/22.8 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.116 | 0.71 | 0.29 | 0.00 | 5.98 | 32.5/21.1 | 18.5/27.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.54 | 0.46 | 0.47 | 5.92 | 27.1/26.9 | 23.7/24.0 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.56 | 0.44 | 0.45 | 5.93 | 32.5/21.4 | 18.2/29.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.64 | 0.36 | 0.00 | 9.29 | 28.9/28.4 | 23.0/21.9 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.076 | 0.73 | 0.27 | 0.00 | 9.19 | 34.0/22.4 | 18.1/26.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CAR @ PHI  ·  10000 joint draws  ·  372 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_CAR_win | p_overtime | goals | shots PHI/CAR | PHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.132 | 0.53 | 0.47 | 0.00 | 5.98 | 20.5/32.0 | 28.6/17.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.49 | 0.51 | 0.49 | 5.84 | 20.7/32.5 | 29.1/17.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.58 | 0.42 | 0.00 | 5.98 | 26.1/26.7 | 23.7/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.54 | 0.46 | 0.49 | 5.89 | 25.8/26.7 | 23.4/22.6 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.073 | 0.53 | 0.47 | 0.48 | 2.72 | 19.1/30.3 | 28.9/17.7 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.068 | 0.51 | 0.49 | 0.00 | 3.43 | 19.3/30.9 | 28.9/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Noel Acciari: 1+ goals YES | 9 | 0.131 | 0.113 | +0.035 | +0.018 | $3.81 | FUNDED_RESEARCH | $1 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Carolina wins by over 2.5 goals NO | 79 | 0.858 | 0.821 | +0.056 | +0.020 | $17.97 | FUNDED_RESEARCH | $5 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 1.5 goals NO | 68 | 0.760 | 0.717 | +0.065 | +0.022 | $7.17 | FUNDED_RESEARCH | $2 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carl Grundstrom: 1+ goals YES | 10 | 0.137 | 0.118 | +0.030 | +0.011 | $2.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Noel Acciari: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03CARPHI-PHI|yes; why: higher confidence-adjusted growth (7.74 vs 5.59 bp); despite a smaller raw edge (+0.035 vs +0.073/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT03CARPHI-CAR3|no: MOSTLY_INDEPENDENT (phi 0.088); KXNHLSPREAD-26OCT03CARPHI-CAR2|no: MOSTLY_INDEPENDENT (phi 0.101); KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: PHI offense suppressed (<= 2 goals)
- **Carolina wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03CARPHI-PHI|yes; why: KXNHLGAME-26OCT03CARPHI-PHI|yes has the higher standalone adjusted growth (5.59 vs 5.38 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.442); relationships: KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.088); KXNHLSPREAD-26OCT03CARPHI-CAR2|no: DUPLICATIVE (phi 0.725); KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: MOSTLY_INDEPENDENT (phi 0.086); failure: CAR wins by 2+
- **Carolina wins by over 1.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03CARPHI-PHI|yes; why: KXNHLGAME-26OCT03CARPHI-PHI|yes has the higher standalone adjusted growth (5.59 vs 5.10 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.609); relationships: KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.101); KXNHLSPREAD-26OCT03CARPHI-CAR3|no: DUPLICATIVE (phi 0.725); KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: MOSTLY_INDEPENDENT (phi 0.097); failure: CAR wins by 2+
- **Carl Grundstrom: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT03CARPHI-PHI|yes; why: KXNHLGAME-26OCT03CARPHI-PHI|yes has the higher standalone adjusted growth (5.59 vs 2.91 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.117); relationships: KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLSPREAD-26OCT03CARPHI-CAR3|no: MOSTLY_INDEPENDENT (phi 0.086); KXNHLSPREAD-26OCT03CARPHI-CAR2|no: MOSTLY_INDEPENDENT (phi 0.097); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3725): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [DIRECT], best adjusted EV KXNHLGAME-26OCT03CARPHI-PHI|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.5401): highest fidelity KXNHLGAME-26OCT03CARPHI-PHI|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03CARPHI-PHI|yes (same contract)
- thesis CAR:SUPPRESSED (p 0.4632): highest fidelity KXNHLSPREAD-26OCT03CARPHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03CARPHI-PHI|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT03CARPHI-PHINACCIARI52-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4075, phi -0.176)
- KXNHLSPREAD-26OCT03CARPHI-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2402, phi -0.725)
- KXNHLSPREAD-26OCT03CARPHI-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.2402, phi -1.0)
- KXNHLGOAL-26OCT03CARPHI-PHICGRUNDSTROM91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4075, phi -0.165)

portfolios: A EV +2.89 (adj +0.93) on $25.08, P(profit) 0.5969, adj growth 7.8 bp · B EV +3.99 (adj +1.62) on $31.25, P(profit) 0.7857, adj growth 14.1 bp · C EV +1.84 (adj +0.64) on $11.80, P(profit) 0.5401, adj growth 5.6 bp · R EV +0.91 (adj +0.37) on $8.00, P(profit) 0.7768, adj growth 12.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03CARPHI-CAR|no == KXNHLGAME-26OCT03CARPHI-PHI|yes

## MTL @ PIT  ·  10000 joint draws  ·  322 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_MTL_win | p_overtime | goals | shots PIT/MTL | PIT/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| PIT shot control · normal event (5-7) · decided (2+) | 0.124 | 0.66 | 0.34 | 0.00 | 6.04 | 32.7/20.9 | 18.2/28.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.56 | 0.44 | 0.00 | 6.09 | 27.2/26.6 | 23.3/23.3 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.100 | 0.64 | 0.36 | 0.00 | 9.35 | 34.7/22.5 | 17.5/26.9 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.54 | 0.46 | 0.46 | 5.98 | 32.9/21.5 | 18.3/29.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.52 | 0.48 | 0.47 | 5.95 | 27.3/26.8 | 23.5/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.59 | 0.41 | 0.00 | 9.46 | 28.9/28.3 | 22.7/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pittsburgh over 3.5 goals scored YES | 39 | 0.484 | 0.434 | +0.077 | +0.028 | $5.50 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sidney Crosby: 1+ goals YES | 31 | 0.362 | 0.345 | +0.037 | +0.020 | $4.13 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| Montreal wins by over 1.5 goals NO | 69 | 0.762 | 0.724 | +0.058 | +0.019 | $3.89 | FUNDED_RESEARCH | $1 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Montreal wins by over 2.5 goals NO | 80 | 0.853 | 0.824 | +0.042 | +0.013 | $1.05 | FUNDED_RESEARCH | $1 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Pittsburgh over 3.5 goals scored YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes; why: higher confidence-adjusted growth (7.01 vs 4.31 bp); wins across more scripts (relative breadth 0.711 vs 0.498); relationships: KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: REINFORCING (phi 0.275); KXNHLSPREAD-26OCT03MTLPIT-MTL2|no: REINFORCING (phi 0.435); KXNHLSPREAD-26OCT03MTLPIT-MTL3|no: DUPLICATIVE (phi 0.335); failure: PIT offense suppressed (<= 2 goals)
- **Sidney Crosby: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes has the higher standalone adjusted growth (7.01 vs 4.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.275); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes: REINFORCING (phi 0.275); KXNHLSPREAD-26OCT03MTLPIT-MTL2|no: REINFORCING (phi 0.172); KXNHLSPREAD-26OCT03MTLPIT-MTL3|no: MOSTLY_INDEPENDENT (phi 0.146); failure: PIT offense suppressed (<= 2 goals)
- **Montreal wins by over 1.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes has the higher standalone adjusted growth (7.01 vs 3.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.435); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes: REINFORCING (phi 0.435); KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: REINFORCING (phi 0.172); KXNHLSPREAD-26OCT03MTLPIT-MTL3|no: DUPLICATIVE (phi 0.743); failure: MTL wins by 2+
- **Montreal wins by over 2.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes has the higher standalone adjusted growth (7.01 vs 2.41 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.335); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes: DUPLICATIVE (phi 0.335); KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: MOSTLY_INDEPENDENT (phi 0.146); KXNHLSPREAD-26OCT03MTLPIT-MTL2|no: DUPLICATIVE (phi 0.743); failure: MTL wins by 2+

**Review**: scripts PIT shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, PIT shot control · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4718): highest fidelity KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes (same contract)
- thesis PIT:WINS_BY_2PLUS (p 0.3477): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-PIT2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS (p 0.568): highest fidelity KXNHLSPREAD-26OCT03MTLPIT-MTL2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.66)
- KXNHLGOAL-26OCT03MTLPIT-PITSCROSBY87-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3172, phi -0.27)
- KXNHLSPREAD-26OCT03MTLPIT-MTL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.2375, phi -1.0)
- KXNHLSPREAD-26OCT03MTLPIT-MTL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.2375, phi -0.743)

portfolios: A EV +4.28 (adj +1.21) on $25.08, P(profit) 0.5341, adj growth 9.1 bp · B EV +1.89 (adj +0.75) on $14.57, P(profit) 0.5585, adj growth 6.9 bp · C EV +2.17 (adj +0.78) on $11.41, P(profit) 0.484, adj growth 6.8 bp · R EV +0.74 (adj +0.30) on $6.00, P(profit) 0.5983, adj growth 10.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03MTLPIT-PIT|yes == KXNHLGAME-26OCT03MTLPIT-MTL|no

## UTA @ CBJ  ·  10000 joint draws  ·  342 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_UTA_win | p_overtime | goals | shots CBJ/UTA | CBJ/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.57 | 0.43 | 0.00 | 6.03 | 27.4/27.4 | 24.1/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.47 | 5.94 | 27.7/27.4 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 9.31 | 29.2/29.0 | 23.3/22.8 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.079 | 0.64 | 0.36 | 0.00 | 6.0 | 32.3/21.7 | 18.9/27.9 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.57 | 0.43 | 0.46 | 5.91 | 32.4/21.9 | 18.8/28.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.058 | 0.50 | 0.50 | 0.00 | 5.97 | 21.9/32.1 | 28.3/18.5 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ EDM  ·  10000 joint draws  ·  356 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_SEA_win | p_overtime | goals | shots EDM/SEA | EDM/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.134 | 0.71 | 0.29 | 0.00 | 6.02 | 34.0/21.8 | 19.2/29.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.67 | 0.33 | 0.00 | 6.04 | 28.5/28.0 | 25.1/24.0 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.53 | 0.47 | 0.46 | 5.98 | 33.9/22.1 | 18.9/30.4 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.101 | 0.72 | 0.28 | 0.00 | 9.33 | 35.6/23.4 | 19.0/27.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.54 | 0.46 | 0.50 | 6.0 | 28.5/28.0 | 24.7/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.63 | 0.37 | 0.00 | 9.39 | 30.0/29.2 | 23.8/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vasily Podkolzin: 1+ assists YES | 37 | 0.445 | 0.398 | +0.059 | +0.011 | $4.42 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_MIXED | D |
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT03SEAEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (1.16 vs 0.00 bp); despite a smaller raw edge (+0.059 vs +0.094/contract); alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, EDM shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.505): highest fidelity KXNHLAST-26OCT03SEAEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT03SEAEDM-EDMVPODKOLZIN92-1|yes (same contract)
- KXNHLAST-26OCT03SEAEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2841, phi -0.281)

portfolios: A EV +1.53 (adj +0.29) on $10.03, P(profit) 0.4451, adj growth 2.1 bp · B EV +0.67 (adj +0.13) on $4.42, P(profit) 0.4451, adj growth 1.1 bp · C EV +0.67 (adj +0.13) on $4.42, P(profit) 0.4451, adj growth 1.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ NYI  ·  10000 joint draws  ·  268 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_NJD_win | p_overtime | goals | shots NYI/NJD | NYI/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.57 | 0.43 | 0.00 | 5.96 | 27.8/28.0 | 24.8/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.50 | 0.50 | 0.48 | 5.86 | 27.9/27.9 | 24.7/24.6 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.073 | 0.50 | 0.50 | 0.00 | 5.98 | 22.3/32.9 | 29.1/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.59 | 0.41 | 0.00 | 9.09 | 29.4/29.4 | 23.9/23.0 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.47 | 0.53 | 0.47 | 5.88 | 22.6/33.3 | 30.0/19.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.49 | 0.51 | 0.52 | 2.79 | 26.6/26.8 | 25.3/25.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 1.5 goals NO | 68 | 0.759 | 0.717 | +0.064 | +0.022 | $9.44 | FUNDED_RESEARCH | $3 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I wins YES | 45 | 0.529 | 0.487 | +0.062 | +0.020 | $2.16 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins by over 2.5 goals NO | 80 | 0.856 | 0.826 | +0.045 | +0.014 | $2.10 | FUNDED_RESEARCH | $1 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03NJNYI-NYI|yes; why: higher confidence-adjusted growth (4.85 vs 3.47 bp); relationships: KXNHLGAME-26OCT03NJNYI-NYI|yes: DUPLICATIVE (phi 0.598); KXNHLSPREAD-26OCT03NJNYI-NJ3|no: DUPLICATIVE (phi 0.728); failure: NJD wins by 2+
- **New York I wins YES** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03NJNYI-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT03NJNYI-NJ2|no has the higher standalone adjusted growth (4.85 vs 3.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.598); they share one thesis budget; relationships: KXNHLSPREAD-26OCT03NJNYI-NJ2|no: DUPLICATIVE (phi 0.598); KXNHLSPREAD-26OCT03NJNYI-NJ3|no: DUPLICATIVE (phi 0.435); failure: NJD wins (incl. OT/SO)
- **New Jersey wins by over 2.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03NJNYI-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT03NJNYI-NJ2|no has the higher standalone adjusted growth (4.85 vs 2.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.728); they share one thesis budget; relationships: KXNHLSPREAD-26OCT03NJNYI-NJ2|no: DUPLICATIVE (phi 0.728); KXNHLGAME-26OCT03NJNYI-NYI|yes: DUPLICATIVE (phi 0.435); failure: NJD wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.07.
- thesis NYI:WINS (p 0.5294): highest fidelity KXNHLSPREAD-26OCT03NJNYI-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03NJNYI-NJ2|no (same contract)
- thesis NJD:SUPPRESSED (p 0.4595): highest fidelity KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03NJNYI-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT03NJNYI-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2413, phi -1.0)
- KXNHLGAME-26OCT03NJNYI-NYI|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS (p 0.4706, phi -1.0)
- KXNHLSPREAD-26OCT03NJNYI-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2413, phi -0.728)

portfolios: A EV +2.66 (adj +0.83) on $25.08, P(profit) 0.6675, adj growth 6.8 bp · B EV +1.26 (adj +0.42) on $13.70, P(profit) 0.7587, adj growth 3.9 bp · C EV +1.77 (adj +0.60) on $19.39, P(profit) 0.7587, adj growth 5.3 bp · R EV +0.46 (adj +0.15) on $5.00, P(profit) 0.7587, adj growth 5.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03NJNYI-NJ|no == KXNHLGAME-26OCT03NJNYI-NYI|yes

## DAL @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_DAL_win | p_overtime | goals | shots NSH/DAL | NSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.56 | 0.44 | 0.00 | 5.96 | 27.0/27.1 | 23.7/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.53 | 0.47 | 0.49 | 5.93 | 27.3/27.5 | 24.3/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.56 | 0.44 | 0.00 | 9.22 | 28.4/28.5 | 22.8/22.1 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.077 | 0.50 | 0.50 | 0.00 | 5.96 | 21.3/32.0 | 28.3/18.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.44 | 0.56 | 0.50 | 5.88 | 21.6/32.2 | 28.8/18.4 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.059 | 0.60 | 0.40 | 0.00 | 5.93 | 31.7/21.8 | 18.9/27.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nashville wins YES | 45 | 0.537 | 0.491 | +0.070 | +0.024 | $7.82 | FUNDED_RESEARCH | $2 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 68 | 0.754 | 0.714 | +0.058 | +0.019 | $8.86 | FUNDED_RESEARCH | $3 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Nashville wins YES** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03DALNSH-DAL2|no; why: higher confidence-adjusted growth (4.92 vs 3.77 bp); relationships: KXNHLSPREAD-26OCT03DALNSH-DAL2|no: DUPLICATIVE (phi 0.616); failure: DAL wins (incl. OT/SO)
- **Dallas wins by over 1.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03DALNSH-NSH|yes; why: second expression of the same thesis: KXNHLGAME-26OCT03DALNSH-NSH|yes has the higher standalone adjusted growth (4.92 vs 3.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.616); they share one thesis budget; relationships: KXNHLGAME-26OCT03DALNSH-NSH|yes: DUPLICATIVE (phi 0.616); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NSH:WINS (p 0.537): highest fidelity KXNHLGAME-26OCT03DALNSH-NSH|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes (same contract)
- thesis NSH:WINS_BY_2PLUS (p 0.3085): highest fidelity KXNHLGAME-26OCT03DALNSH-NSH|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03DALNSH-NSH|yes (same contract)
- KXNHLGAME-26OCT03DALNSH-NSH|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS (p 0.463, phi -1.0)
- KXNHLSPREAD-26OCT03DALNSH-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.2464, phi -1.0)

portfolios: A EV +3.31 (adj +1.00) on $25.08, P(profit) 0.537, adj growth 7.3 bp · B EV +1.91 (adj +0.64) on $16.69, P(profit) 0.537, adj growth 5.6 bp · C EV +1.65 (adj +0.56) on $11.07, P(profit) 0.537, adj growth 4.9 bp · R EV +0.55 (adj +0.18) on $5.00, P(profit) 0.537, adj growth 6.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03DALNSH-DAL|no == KXNHLGAME-26OCT03DALNSH-NSH|yes

## BOS @ MIN  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_BOS_win | p_overtime | goals | shots MIN/BOS | MIN/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.65 | 0.35 | 0.00 | 6.02 | 29.1/28.8 | 25.9/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.53 | 0.47 | 0.47 | 5.96 | 28.6/28.5 | 25.3/25.3 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.103 | 0.72 | 0.28 | 0.00 | 6.03 | 34.3/22.6 | 20.0/29.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.68 | 0.32 | 0.00 | 9.46 | 30.4/30.0 | 25.0/23.1 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.57 | 0.43 | 0.47 | 5.94 | 34.8/23.3 | 20.0/31.4 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.074 | 0.75 | 0.25 | 0.00 | 9.27 | 35.7/24.2 | 19.8/27.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10, MIN shot control · normal event (5-7) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 8 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_STL_win | p_overtime | goals | shots COL/STL | COL/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.154 | 0.71 | 0.29 | 0.00 | 6.02 | 33.7/21.3 | 18.8/28.8 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.54 | 0.46 | 0.48 | 5.92 | 34.1/21.8 | 18.5/30.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.114 | 0.76 | 0.24 | 0.00 | 9.31 | 35.6/22.7 | 18.6/27.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.68 | 0.32 | 0.00 | 6.04 | 28.0/27.1 | 24.2/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.51 | 0.49 | 0.45 | 5.95 | 28.3/27.6 | 24.3/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.68 | 0.32 | 0.00 | 9.4 | 29.9/28.9 | 23.9/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins NO | 28 | 0.372 | 0.323 | +0.077 | +0.029 | $1.96 | FUNDED_RESEARCH | $1 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 64 | 0.723 | 0.679 | +0.067 | +0.023 | $2.92 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado wins NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLGAME-26OCT03STLCOL-STL|yes; why: higher confidence-adjusted growth (8.92 vs 5.86 bp); relationships: KXNHLSPREAD-26OCT03STLCOL-COL3|no: DUPLICATIVE (phi 0.476); failure: COL wins (incl. OT/SO)
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT03STLCOL-COL2|no; why: KXNHLSPREAD-26OCT03STLCOL-COL2|no has the higher standalone adjusted growth (5.54 vs 5.14 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.743); relationships: KXNHLGAME-26OCT03STLCOL-COL|no: DUPLICATIVE (phi 0.476); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis STL:WINS (p 0.3716): highest fidelity KXNHLGAME-26OCT03STLCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no (same contract)
- thesis STL:WINS_BY_2PLUS (p 0.1808): highest fidelity KXNHLGAME-26OCT03STLCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3093): highest fidelity KXNHLTEAMTOTAL-26OCT03STLCOL-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT03STLCOL-COL|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGAME-26OCT03STLCOL-COL|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS (p 0.6284, phi -1.0)
- KXNHLSPREAD-26OCT03STLCOL-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.4097, phi -0.743)

portfolios: A EV +4.61 (adj +1.61) on $25.08, P(profit) 0.4799, adj growth 12.8 bp · B EV +0.81 (adj +0.30) on $4.88, P(profit) 0.3716, adj growth 2.9 bp · C EV +2.73 (adj +1.00) on $12.74, P(profit) 0.3716, adj growth 8.8 bp · R EV +0.37 (adj +0.13) on $2.00, P(profit) 0.3716, adj growth 5.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT03STLCOL-STL|yes == KXNHLGAME-26OCT03STLCOL-COL|no

## CGY @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CGY_win | p_overtime | goals | shots VAN/CGY | VAN/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.60 | 0.40 | 0.00 | 6.02 | 28.1/28.2 | 25.0/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.53 | 0.47 | 0.46 | 5.92 | 28.4/28.5 | 25.2/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.64 | 0.36 | 0.00 | 9.39 | 29.7/29.9 | 24.5/22.7 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.067 | 0.65 | 0.35 | 0.00 | 6.01 | 32.9/22.2 | 19.5/28.2 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.066 | 0.56 | 0.44 | 0.00 | 5.98 | 22.8/33.5 | 30.2/19.1 | even strength |
| VAN shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.50 | 5.98 | 33.5/22.8 | 19.7/30.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Calgary wins by over 1.5 goals NO | 72 | 0.776 | 0.745 | +0.042 | +0.011 | $11.56 | FUNDED_RESEARCH | $3 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Calgary wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT03CGYVAN-CGY3|no; why: higher confidence-adjusted growth (1.45 vs 0.64 bp); alternative not eligible: confidence-adjusted EV +0.0063 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: CGY wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis VAN:WINS (p 0.569): highest fidelity KXNHLSPREAD-26OCT03CGYVAN-CGY2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT03CGYVAN-CGY2|no (same contract)
- KXNHLSPREAD-26OCT03CGYVAN-CGY2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CGY:WINS_BY_2PLUS (p 0.2241, phi -1.0)

portfolios: A EV +0.57 (adj +0.15) on $10.03, P(profit) 0.7759, adj growth 1.4 bp · B EV +0.66 (adj +0.18) on $11.56, P(profit) 0.7759, adj growth 1.6 bp · C EV +0.66 (adj +0.18) on $11.56, P(profit) 0.7759, adj growth 1.6 bp · R EV +0.17 (adj +0.05) on $3.00, P(profit) 0.7759, adj growth 1.6 bp

## LAK @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_LAK_win | p_overtime | goals | shots SJS/LAK | SJS/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.52 | 0.48 | 0.00 | 6.02 | 27.3/27.5 | 24.2/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.49 | 5.92 | 27.3/27.7 | 24.3/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.54 | 0.46 | 0.00 | 9.3 | 29.0/29.3 | 23.6/22.9 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.077 | 0.44 | 0.56 | 0.00 | 6.01 | 21.8/32.4 | 28.7/18.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.49 | 0.51 | 0.48 | 5.9 | 21.8/32.7 | 29.4/18.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.065 | 0.52 | 0.48 | 0.00 | 3.44 | 26.1/26.3 | 24.5/24.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
