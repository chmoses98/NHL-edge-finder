# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-03T10:50:36Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +23.81 | +6.30 | +19.92 | 0.627 | -62.88 | -80.23 | 41.18 |
| B thesis-diversified (joint) ← optimiser card | 60.82 | +9.56 | +3.12 | +9.57 | 0.629 | -24.01 | -33.15 | 27.83 |
| C best expression per thesis | 27.28 | +8.55 | +3.19 | +3.87 | 0.511 | -27.29 | -27.29 | 27.62 |
| R FUNDED research stakes | 21.00 | +3.43 | +1.15 | +2.63 | 0.630 | -8.63 | -11.39 | 0.00 |

## UTA @ TOR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_UTA_win | p_overtime | goals | shots TOR/UTA | TOR/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.51 | 0.49 | 0.00 | 6.09 | 28.4/28.8 | 25.2/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.110 | 0.51 | 0.49 | 0.00 | 9.45 | 30.3/30.9 | 24.9/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.48 | 5.98 | 28.6/29.0 | 25.5/25.2 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.094 | 0.46 | 0.54 | 0.00 | 6.02 | 22.6/34.5 | 30.6/19.3 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.092 | 0.43 | 0.57 | 0.00 | 9.42 | 24.3/36.3 | 29.1/18.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.47 | 0.53 | 0.48 | 5.98 | 22.9/34.8 | 31.3/19.6 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ MTL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_WPG_win | p_overtime | goals | shots MTL/WPG | MTL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.63 | 0.37 | 0.00 | 6.05 | 27.1/27.0 | 24.0/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.50 | 5.95 | 27.3/27.4 | 24.1/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.65 | 0.35 | 0.00 | 9.22 | 28.5/28.4 | 23.4/21.7 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 6.04 | 31.6/21.4 | 18.8/27.0 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.067 | 0.56 | 0.44 | 0.00 | 6.01 | 21.4/31.7 | 28.2/17.8 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.46 | 5.92 | 32.1/21.9 | 18.8/28.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ TBL  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_DET_win | p_overtime | goals | shots TBL/DET | TBL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.66 | 0.34 | 0.00 | 6.01 | 27.3/27.1 | 24.3/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.55 | 0.45 | 0.46 | 5.97 | 27.3/27.0 | 23.9/23.8 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.101 | 0.76 | 0.24 | 0.00 | 6.0 | 32.6/21.5 | 19.3/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.66 | 0.34 | 0.00 | 9.32 | 29.1/28.8 | 23.7/22.1 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.56 | 0.44 | 0.49 | 5.9 | 32.3/21.7 | 18.6/28.9 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.064 | 0.72 | 0.28 | 0.00 | 9.32 | 34.1/22.9 | 18.6/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 1.5 goals NO | 53 | 0.606 | 0.565 | +0.058 | +0.018 | $8.81 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 66 | 0.729 | 0.689 | +0.053 | +0.013 | $2.29 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV03DETTB-TB3|no; why: higher confidence-adjusted growth (2.82 vs 1.83 bp); relationships: KXNHLSPREAD-26NOV03DETTB-TB3|no: DUPLICATIVE (phi 0.756); failure: TBL wins by 2+
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV03DETTB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV03DETTB-TB2|no has the higher standalone adjusted growth (2.82 vs 1.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.756); they share one thesis budget; relationships: KXNHLSPREAD-26NOV03DETTB-TB2|no: DUPLICATIVE (phi 0.756); failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.415): highest fidelity KXNHLSPREAD-26NOV03DETTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03DETTB-TB2|no (same contract)
- KXNHLSPREAD-26NOV03DETTB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3944, phi -1.0)
- KXNHLSPREAD-26NOV03DETTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3944, phi -0.756)

portfolios: A EV +2.91 (adj +0.83) on $31.58, P(profit) 0.6056, adj growth 5.6 bp · B EV +1.11 (adj +0.33) on $11.10, P(profit) 0.6056, adj growth 2.9 bp · C EV +1.07 (adj +0.33) on $10.09, P(profit) 0.6056, adj growth 2.9 bp · R EV +0.40 (adj +0.12) on $4.00, P(profit) 0.6056, adj growth 3.9 bp

## STL @ NYR  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_STL_win | p_overtime | goals | shots NYR/STL | NYR/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.55 | 0.45 | 0.00 | 6.04 | 26.7/26.7 | 23.4/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.50 | 0.50 | 0.49 | 5.94 | 26.7/26.7 | 23.4/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.55 | 0.45 | 0.00 | 9.31 | 28.5/28.4 | 22.9/22.1 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.072 | 0.63 | 0.37 | 0.00 | 6.04 | 31.4/21.3 | 18.5/27.3 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.070 | 0.48 | 0.52 | 0.00 | 6.0 | 21.4/31.7 | 27.9/18.1 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.53 | 0.47 | 0.48 | 5.88 | 31.6/21.4 | 18.3/28.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ PHI  ·  10000 joint draws  ·  98 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_MIN_win | p_overtime | goals | shots PHI/MIN | PHI/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.54 | 0.46 | 0.00 | 5.99 | 27.0/27.3 | 24.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.48 | 5.87 | 27.1/27.4 | 24.2/23.8 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.091 | 0.50 | 0.50 | 0.00 | 5.94 | 21.5/32.8 | 29.1/18.2 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.50 | 0.50 | 0.47 | 5.85 | 21.7/32.8 | 29.3/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.55 | 0.45 | 0.00 | 9.21 | 28.8/29.1 | 23.2/22.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.56 | 0.44 | 0.00 | 3.48 | 25.8/26.2 | 24.4/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Philadelphia wins by over 1.5 goals YES | 20 | 0.289 | 0.242 | +0.078 | +0.031 | $1.81 | FUNDED_RESEARCH | $1 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Philadelphia over 3.5 goals scored YES | 29 | 0.380 | 0.332 | +0.075 | +0.028 | $4.03 | FUNDED_RESEARCH | $2 | PHI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota over 1.5 goals scored NO | 15 | 0.214 | 0.180 | +0.055 | +0.021 | $2.44 | FUNDED_RESEARCH | $1 | MIN:SUPPRESSED | FRAGILE (0.49) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 74 | 0.847 | 0.774 | +0.093 | +0.021 | $7.66 | FUNDED_RESEARCH | $2 | PHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes; why: higher confidence-adjusted growth (12.46 vs 8.01 bp); relationships: KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes: REINFORCING (phi 0.532); KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2|no: REINFORCING (phi 0.452); KXNHLSPREAD-26NOV03MINPHI-MIN3|no: REINFORCING (phi 0.271); failure: MIN wins (incl. OT/SO)
- **Philadelphia over 3.5 goals scored YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes has the higher standalone adjusted growth (12.46 vs 8.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.532); they share one thesis budget; relationships: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: REINFORCING (phi 0.532); KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2|no: INTENTIONAL_DIVERSIFIER (phi 0.011); KXNHLSPREAD-26NOV03MINPHI-MIN3|no: REINFORCING (phi 0.297); failure: PHI offense suppressed (<= 2 goals)
- **Minnesota over 1.5 goals scored NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes has the higher standalone adjusted growth (12.46 vs 6.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.452); they share one thesis budget; relationships: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: REINFORCING (phi 0.452); KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes: INTENTIONAL_DIVERSIFIER (phi 0.011); KXNHLSPREAD-26NOV03MINPHI-MIN3|no: REINFORCING (phi 0.222); failure: MIN wins (incl. OT/SO)
- **Minnesota wins by over 2.5 goals NO** — thesis: PHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes has the higher standalone adjusted growth (12.46 vs 5.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.271); they share one thesis budget; relationships: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: REINFORCING (phi 0.271); KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes: REINFORCING (phi 0.297); KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2|no: REINFORCING (phi 0.222); failure: MIN wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:WINS_BY_2PLUS (p 0.2894): highest fidelity KXNHLSPREAD-26NOV03MINPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3682): highest fidelity KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.4411): highest fidelity KXNHLSPREAD-26NOV03MINPHI-MIN3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV03MINPHI-MIN4|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2|no kept
- KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.4734, phi -0.605)
- KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PHI:SUPPRESSED (p 0.4034, phi -0.643)
- KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2|no: FUNDED_RESEARCH; family MIXED; loses 51% of the draws where the thesis happens; opposing: failure thesis MIN:WINS (p 0.4734, phi -0.447)
- KXNHLSPREAD-26NOV03MINPHI-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.2 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2523, phi -0.732)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV03MINPHI-MIN4|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2|no kept

portfolios: A EV +7.80 (adj +1.32) on $39.47, P(profit) 0.6537, adj growth 9.6 bp · B EV +3.47 (adj +1.16) on $15.94, P(profit) 0.5041, adj growth 10.7 bp · C EV +3.16 (adj +1.25) on $8.54, P(profit) 0.2894, adj growth 10.9 bp · R EV +1.46 (adj +0.52) on $6.00, P(profit) 0.5103, adj growth 17.5 bp
equivalent contracts collapsed: KXNHLGAME-26NOV03MINPHI-MIN|no == KXNHLGAME-26NOV03MINPHI-PHI|yes

## VGK @ PIT  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_VGK_win | p_overtime | goals | shots PIT/VGK | PIT/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.48 | 0.52 | 0.00 | 6.04 | 27.4/27.3 | 23.7/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.48 | 5.99 | 27.4/27.3 | 24.1/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.45 | 0.55 | 0.00 | 9.39 | 28.8/28.8 | 22.7/22.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.073 | 0.56 | 0.44 | 0.00 | 6.02 | 31.7/21.4 | 18.4/27.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.068 | 0.45 | 0.55 | 0.00 | 6.03 | 21.7/32.2 | 28.2/18.6 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.47 | 5.94 | 32.5/22.0 | 18.7/29.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ WSH  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_DAL_win | p_overtime | goals | shots WSH/DAL | WSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.56 | 0.44 | 0.00 | 5.98 | 25.9/26.0 | 22.8/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.47 | 5.96 | 26.1/26.2 | 23.0/22.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.60 | 0.40 | 0.00 | 9.35 | 27.6/27.7 | 22.2/20.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.076 | 0.50 | 0.50 | 0.00 | 5.95 | 20.7/30.8 | 27.1/17.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.47 | 0.53 | 0.46 | 5.86 | 20.6/30.8 | 27.5/17.5 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.062 | 0.65 | 0.35 | 0.00 | 6.02 | 30.4/20.8 | 18.1/26.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ CBJ  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_COL_win | p_overtime | goals | shots CBJ/COL | CBJ/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.46 | 0.54 | 0.00 | 6.01 | 28.0/28.4 | 24.6/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.48 | 0.52 | 0.45 | 5.94 | 28.1/28.5 | 25.3/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.47 | 0.53 | 0.00 | 9.34 | 29.5/29.9 | 23.8/23.4 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.091 | 0.38 | 0.62 | 0.00 | 6.0 | 22.2/33.9 | 29.8/19.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.43 | 0.57 | 0.46 | 5.87 | 22.6/34.1 | 30.5/19.6 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.059 | 0.39 | 0.61 | 0.00 | 9.22 | 23.5/35.2 | 28.2/18.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_EDM_win | p_overtime | goals | shots NJD/EDM | NJD/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.47 | 0.53 | 0.00 | 6.07 | 28.2/27.8 | 24.0/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.49 | 0.51 | 0.47 | 6.0 | 28.2/28.0 | 24.6/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.49 | 0.51 | 0.00 | 9.43 | 29.7/29.4 | 23.3/23.5 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.093 | 0.56 | 0.44 | 0.00 | 6.07 | 33.6/22.0 | 18.9/29.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.54 | 0.46 | 0.43 | 5.93 | 33.1/22.0 | 18.8/29.6 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.073 | 0.54 | 0.46 | 0.00 | 9.41 | 35.2/23.8 | 18.2/28.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Edmonton over 4.5 goals scored YES | 17 | 0.243 | 0.201 | +0.063 | +0.021 | $3.95 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
| New Jersey wins by over 1.5 goals NO | 64 | 0.717 | 0.676 | +0.061 | +0.020 | $8.59 | FUNDED_RESEARCH | $3 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins by over 2.5 goals NO | 76 | 0.818 | 0.787 | +0.045 | +0.014 | $3.28 | FUNDED_RESEARCH | $1 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Full Game: Over 6.5 goals scored YES | 46 | 0.521 | 0.488 | +0.044 | +0.011 | $1.65 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Edmonton over 4.5 goals scored YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV03EDMNJ-NJ2|no; why: higher confidence-adjusted growth (6.76 vs 3.80 bp); relationships: KXNHLSPREAD-26NOV03EDMNJ-NJ2|no: DUPLICATIVE (phi 0.325); KXNHLSPREAD-26NOV03EDMNJ-NJ3|no: REINFORCING (phi 0.252); KXNHLTOTAL-26NOV03EDMNJ-7|yes: REINFORCING (phi 0.443); failure: NJD wins (incl. OT/SO)
- **New Jersey wins by over 1.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes has the higher standalone adjusted growth (6.76 vs 3.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.325); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes: DUPLICATIVE (phi 0.325); KXNHLSPREAD-26NOV03EDMNJ-NJ3|no: DUPLICATIVE (phi 0.75); KXNHLTOTAL-26NOV03EDMNJ-7|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NJD wins by 2+
- **New Jersey wins by over 2.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes has the higher standalone adjusted growth (6.76 vs 2.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.252); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes: REINFORCING (phi 0.252); KXNHLSPREAD-26NOV03EDMNJ-NJ2|no: DUPLICATIVE (phi 0.75); KXNHLTOTAL-26NOV03EDMNJ-7|yes: INTENTIONAL_DIVERSIFIER (phi -0.083); failure: NJD wins by 2+
- **Full Game: Over 6.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes has the higher standalone adjusted growth (6.76 vs 1.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.443); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes: REINFORCING (phi 0.443); KXNHLSPREAD-26NOV03EDMNJ-NJ2|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26NOV03EDMNJ-NJ3|no: INTENTIONAL_DIVERSIFIER (phi -0.083); failure: low-event game (<= 4 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4235): highest fidelity KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3|yes less than the minimum stake; KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes kept
- thesis EDM:WINS (p 0.5035): highest fidelity KXNHLSPREAD-26NOV03EDMNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS_BY_2PLUS (p 0.2921): highest fidelity KXNHLSPREAD-26NOV03EDMNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes: FUNDED_RESEARCH; family MIXED; loses 43% of the draws where the thesis happens; opposing: failure thesis NJD:WINS (p 0.4965, phi -0.463)
- KXNHLSPREAD-26NOV03EDMNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2832, phi -1.0)
- KXNHLSPREAD-26NOV03EDMNJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2832, phi -0.75)
- KXNHLTOTAL-26NOV03EDMNJ-7|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis GAME:LOW_EVENT (p 0.2012, phi -0.524)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3|yes less than the minimum stake; KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes kept

portfolios: A EV +7.29 (adj +2.33) on $39.47, P(profit) 0.3625, adj growth 14.0 bp · B EV +2.52 (adj +0.83) on $17.47, P(profit) 0.4002, adj growth 7.3 bp · C EV +1.96 (adj +0.67) on $5.60, P(profit) 0.2427, adj growth 5.8 bp · R EV +0.78 (adj +0.25) on $6.00, P(profit) 0.4002, adj growth 8.5 bp

## CAR @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_CAR_win | p_overtime | goals | shots NSH/CAR | NSH/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.143 | 0.38 | 0.62 | 0.00 | 6.02 | 21.6/34.5 | 30.1/18.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.126 | 0.47 | 0.53 | 0.46 | 6.0 | 21.9/34.8 | 31.2/18.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.113 | 0.38 | 0.62 | 0.00 | 9.35 | 23.0/35.8 | 28.1/17.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.45 | 0.55 | 0.00 | 6.03 | 27.3/28.3 | 24.5/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.45 | 0.55 | 0.00 | 9.38 | 29.1/30.1 | 23.3/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.50 | 0.50 | 0.47 | 5.97 | 27.6/28.6 | 25.3/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 1.5 goals NO | 58 | 0.665 | 0.620 | +0.068 | +0.023 | $10.06 | FUNDED_RESEARCH | $3 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nashville over 4.5 goals scored YES | 15 | 0.211 | 0.176 | +0.053 | +0.017 | $2.62 | FUNDED_RESEARCH | $1 | NSH:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
| Nashville over 2.5 goals scored YES | 52 | 0.605 | 0.557 | +0.067 | +0.020 | $3.62 | FUNDED_RESEARCH | $1 | NSH:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes has the higher standalone adjusted growth (11.37 vs 4.78 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.220); relationships: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes: DUPLICATIVE (phi 0.336); KXNHLTEAMTOTAL-26NOV03CARNSH-NSH3|yes: REINFORCING (phi 0.501); failure: CAR wins by 2+
- **Nashville over 4.5 goals scored YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes selected over broad KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.52 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV03CARNSH-CAR2|no: DUPLICATIVE (phi 0.336); KXNHLTEAMTOTAL-26NOV03CARNSH-NSH3|yes: DUPLICATIVE (phi 0.419); failure: CAR wins (incl. OT/SO)
- **Nashville over 2.5 goals scored YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes has the higher standalone adjusted growth (11.37 vs 3.48 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.261); relationships: KXNHLSPREAD-26NOV03CARNSH-CAR2|no: REINFORCING (phi 0.501); KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes: DUPLICATIVE (phi 0.419); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.11.
- thesis GAME:HIGH_EVENT (p 0.3104): highest fidelity KXNHLTEAMTOTAL-26NOV03CARNSH-NSH3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes — Broad expression KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes selected over broad KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.52 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NSH:WINS (p 0.45): highest fidelity KXNHLSPREAD-26NOV03CARNSH-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03CARNSH-CAR2|no (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.3814): highest fidelity KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03CARNSH-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV03CARNSH-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3351, phi -1.0)
- KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes: FUNDED_RESEARCH; family MIXED; loses 45% of the draws where the thesis happens; opposing: failure thesis CAR:WINS (p 0.55, phi -0.466)
- KXNHLTEAMTOTAL-26NOV03CARNSH-NSH3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NSH:SUPPRESSED (p 0.4046, phi -0.981)
- override: Broad expression KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes selected over broad KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.52 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.81 (adj +1.82) on $39.47, P(profit) 0.5492, adj growth 12.0 bp · B EV +2.46 (adj +0.80) on $16.31, P(profit) 0.671, adj growth 7.0 bp · C EV +2.36 (adj +0.94) on $3.05, P(profit) 0.0946, adj growth 8.1 bp · R EV +0.80 (adj +0.26) on $5.00, P(profit) 0.671, adj growth 8.6 bp

## ANA @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_ANA_win | p_overtime | goals | shots VAN/ANA | VAN/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.129 | 0.39 | 0.61 | 0.00 | 6.11 | 21.7/33.6 | 29.1/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.45 | 0.55 | 0.00 | 6.05 | 27.3/28.0 | 24.2/23.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.46 | 0.54 | 0.45 | 6.02 | 22.0/34.0 | 30.4/18.8 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.102 | 0.35 | 0.65 | 0.00 | 9.49 | 23.0/35.6 | 27.8/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.45 | 0.55 | 0.00 | 9.51 | 29.0/29.9 | 23.1/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.48 | 0.52 | 0.45 | 6.05 | 27.4/28.1 | 24.6/24.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
