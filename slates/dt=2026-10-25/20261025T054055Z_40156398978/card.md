# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T05:40:55Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +23.04 | +6.40 | +20.52 | 0.640 | -56.10 | -78.97 | 44.14 |
| B thesis-diversified (joint) ← optimiser card | 79.37 | +10.39 | +3.53 | +10.51 | 0.641 | -27.53 | -36.78 | 31.14 |
| C best expression per thesis | 56.63 | +7.66 | +2.80 | +12.47 | 0.563 | -27.45 | -29.74 | 24.71 |
| R FUNDED research stakes | 25.00 | +3.54 | +1.19 | +3.25 | 0.623 | -9.39 | -12.46 | 0.00 |

## FLA @ CHI  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_FLA_win | p_overtime | goals | shots CHI/FLA | CHI/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.113 | 0.41 | 0.59 | 0.00 | 5.96 | 20.7/31.8 | 27.7/17.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.48 | 5.92 | 26.4/26.9 | 23.7/23.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.48 | 0.52 | 0.00 | 6.05 | 26.3/26.8 | 23.1/22.9 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.46 | 0.54 | 0.46 | 5.97 | 21.1/32.1 | 28.7/17.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.50 | 0.50 | 0.00 | 9.41 | 27.8/28.4 | 22.1/21.8 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.069 | 0.38 | 0.62 | 0.00 | 9.29 | 22.2/34.3 | 27.1/17.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 2.5 goals NO | 73 | 0.810 | 0.767 | +0.066 | +0.024 | $20.00 | FUNDED_RESEARCH | $5 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Chicago wins by over 1.5 goals YES | 19 | 0.258 | 0.221 | +0.057 | +0.021 | $4.21 | FUNDED_RESEARCH | $2 | CHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25FLACHI-CHI2|yes; why: higher confidence-adjusted growth (6.39 vs 5.72 bp); wins across more scripts (relative breadth 1.013 vs 0.541); relationships: KXNHLSPREAD-26OCT25FLACHI-CHI2|yes: REINFORCING (phi 0.286); failure: FLA wins by 2+
- **Chicago wins by over 1.5 goals YES** — thesis: CHI wins by 2+; alternative: KXNHLSPREAD-26OCT25FLACHI-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25FLACHI-FLA3|no has the higher standalone adjusted growth (6.39 vs 5.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.286); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25FLACHI-FLA3|no: REINFORCING (phi 0.286); failure: FLA wins (incl. OT/SO)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis CHI:WINS (p 0.4731): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- thesis CHI:WINS_BY_2PLUS (p 0.2577): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- thesis FLA:SUPPRESSED (p 0.3798): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- KXNHLSPREAD-26OCT25FLACHI-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3033, phi -0.735)
- KXNHLSPREAD-26OCT25FLACHI-CHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS (p 0.5269, phi -0.622)

portfolios: A EV +6.18 (adj +2.15) on $39.47, P(profit) 0.6967, adj growth 15.2 bp · B EV +2.96 (adj +1.06) on $24.21, P(profit) 0.8096, adj growth 9.4 bp · C EV +1.77 (adj +0.63) on $20.00, P(profit) 0.8096, adj growth 5.8 bp · R EV +1.01 (adj +0.36) on $7.00, P(profit) 0.2577, adj growth 11.9 bp

## NYI @ DAL  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_NYI_win | p_overtime | goals | shots DAL/NYI | DAL/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.57 | 0.43 | 0.00 | 5.99 | 26.0/25.8 | 22.7/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.48 | 5.89 | 26.1/26.1 | 22.9/23.0 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.082 | 0.66 | 0.34 | 0.00 | 5.92 | 30.8/20.4 | 17.8/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.59 | 0.41 | 0.00 | 9.18 | 27.6/27.6 | 22.1/21.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.58 | 0.42 | 0.48 | 5.81 | 30.7/20.4 | 17.4/27.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.52 | 0.48 | 0.45 | 2.8 | 24.5/24.6 | 23.2/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dallas wins by over 1.5 goals NO | 61 | 0.672 | 0.638 | +0.045 | +0.012 | $5.75 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I over 2.5 goals scored YES | 47 | 0.539 | 0.499 | +0.051 | +0.012 | $3.82 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dallas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25NYIDAL-DAL3|no; why: higher confidence-adjusted growth (1.28 vs 0.84 bp); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes: REINFORCING (phi 0.465); failure: DAL wins by 2+
- **New York I over 2.5 goals scored YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25NYIDAL-DAL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25NYIDAL-DAL2|no has the higher standalone adjusted growth (1.28 vs 1.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.465); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25NYIDAL-DAL2|no: REINFORCING (phi 0.465); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis GAME:TIGHT (p 0.4414): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25NYIDAL-DAL2|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3209): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes (same contract)
- KXNHLSPREAD-26OCT25NYIDAL-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3283, phi -1.0)
- KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:SUPPRESSED (p 0.4727, phi -0.978)

portfolios: A EV +2.79 (adj +0.68) on $31.58, P(profit) 0.5386, adj growth 3.9 bp · B EV +0.81 (adj +0.20) on $9.57, P(profit) 0.4707, adj growth 1.8 bp · C EV +0.59 (adj +0.15) on $8.17, P(profit) 0.6717, adj growth 1.3 bp · R EV +0.25 (adj +0.06) on $3.00, P(profit) 0.6717, adj growth 2.1 bp

## MTL @ WPG  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_MTL_win | p_overtime | goals | shots WPG/MTL | WPG/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.46 | 0.54 | 0.00 | 6.01 | 27.3/27.1 | 23.5/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.50 | 0.50 | 0.48 | 5.9 | 27.3/27.3 | 23.9/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.46 | 0.54 | 0.00 | 9.31 | 28.7/28.7 | 22.5/22.8 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.081 | 0.53 | 0.47 | 0.00 | 5.99 | 32.1/21.8 | 18.4/28.5 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.48 | 5.83 | 32.3/21.7 | 18.6/29.0 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.058 | 0.38 | 0.62 | 0.00 | 5.94 | 21.5/31.6 | 27.4/18.8 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 6 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_COL_win | p_overtime | goals | shots NSH/COL | NSH/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.120 | 0.35 | 0.65 | 0.00 | 5.98 | 22.7/35.5 | 31.1/19.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.39 | 0.61 | 0.00 | 6.06 | 28.6/29.4 | 25.1/25.5 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.46 | 0.54 | 0.49 | 5.95 | 22.8/35.2 | 31.8/19.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.48 | 0.52 | 0.45 | 5.93 | 28.7/29.4 | 26.1/25.5 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.093 | 0.32 | 0.68 | 0.00 | 9.35 | 24.5/37.5 | 29.0/19.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.38 | 0.62 | 0.00 | 9.53 | 30.4/31.1 | 23.8/24.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins by over 2.5 goals NO | 67 | 0.754 | 0.709 | +0.068 | +0.024 | $15.56 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado over 4.5 goals scored NO | 64 | 0.720 | 0.675 | +0.064 | +0.019 | $4.93 | FUNDED_RESEARCH | $2 | NSH:WINS | DIRECT (0.95) | EVIDENCE_MIXED | D |
| Colorado over 2.5 goals scored NO | 24 | 0.308 | 0.269 | +0.055 | +0.016 | $1.73 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT25COLNSH-COL5|no; why: higher confidence-adjusted growth (5.79 vs 3.52 bp); wins across more scripts (relative breadth 1.011 vs 0.894); relationships: KXNHLTEAMTOTAL-26OCT25COLNSH-COL5|no: REINFORCING (phi 0.526); KXNHLTEAMTOTAL-26OCT25COLNSH-COL3|no: DUPLICATIVE (phi 0.381); failure: COL wins by 2+
- **Colorado over 4.5 goals scored NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25COLNSH-COL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25COLNSH-COL3|no has the higher standalone adjusted growth (5.79 vs 3.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.526); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25COLNSH-COL3|no: REINFORCING (phi 0.526); KXNHLTEAMTOTAL-26OCT25COLNSH-COL3|no: DUPLICATIVE (phi 0.416); failure: COL offense succeeds (4+ goals)
- **Colorado over 2.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25COLNSH-COL3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25COLNSH-COL3|no has the higher standalone adjusted growth (5.79 vs 3.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.381); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25COLNSH-COL3|no: DUPLICATIVE (phi 0.381); KXNHLTEAMTOTAL-26OCT25COLNSH-COL5|no: DUPLICATIVE (phi 0.416); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:TIGHT (p 0.4254): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- thesis NSH:WINS (p 0.4152): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- thesis COL:SUPPRESSED (p 0.3188): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL3|no (same contract)
- KXNHLSPREAD-26OCT25COLNSH-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3586, phi -0.765)
- KXNHLTEAMTOTAL-26OCT25COLNSH-COL5|no: FUNDED_RESEARCH; family MIXED; loses 5% of the draws where the thesis happens; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4698, phi -0.662)
- KXNHLTEAMTOTAL-26OCT25COLNSH-COL3|no: FUNDED_RESEARCH; family MIXED; loses 3% of the draws where the thesis happens; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4698, phi -0.628)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT25COLNSH-COL2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT25COLNSH-COL5|no kept
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT25COLNSH-COL3|no kept

portfolios: A EV +4.58 (adj +1.19) on $39.47, P(profit) 0.6414, adj growth 8.8 bp · B EV +2.41 (adj +0.79) on $22.22, P(profit) 0.7536, adj growth 7.0 bp · C EV +1.99 (adj +0.70) on $20.00, P(profit) 0.7536, adj growth 6.2 bp · R EV +0.81 (adj +0.26) on $7.00, P(profit) 0.6446, adj growth 8.8 bp

## MIN @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_MIN_win | p_overtime | goals | shots VAN/MIN | VAN/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| MIN shot control · normal event (5-7) · decided (2+) | 0.119 | 0.44 | 0.56 | 0.00 | 5.96 | 22.0/34.0 | 30.0/18.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.49 | 0.51 | 0.00 | 6.03 | 28.0/28.5 | 24.9/24.4 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.49 | 0.51 | 0.46 | 5.97 | 22.3/34.3 | 30.9/19.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.53 | 0.47 | 0.45 | 6.01 | 27.9/28.6 | 25.2/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.51 | 0.49 | 0.00 | 9.3 | 29.5/30.2 | 24.2/23.2 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.090 | 0.42 | 0.58 | 0.00 | 9.32 | 23.6/36.0 | 28.9/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 19 | 0.279 | 0.232 | +0.079 | +0.031 | $5.74 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota wins by over 1.5 goals NO | 58 | 0.705 | 0.621 | +0.108 | +0.024 | $2.03 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 2.5 goals scored YES | 55 | 0.636 | 0.591 | +0.069 | +0.023 | $6.89 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Minnesota over 4.5 goals scored NO | 69 | 0.766 | 0.723 | +0.061 | +0.018 | $8.71 | FUNDED_RESEARCH | $3 | VAN:WINS | DIRECT (0.96) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT25MINVAN-MIN2|no; why: higher confidence-adjusted growth (13.28 vs 5.06 bp); despite a smaller raw edge (+0.079 vs +0.108/contract); relationships: KXNHLSPREAD-26OCT25MINVAN-MIN2|no: DUPLICATIVE (phi 0.403); KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes: DUPLICATIVE (phi 0.435); KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5|no: DUPLICATIVE (phi 0.313); failure: MIN wins (incl. OT/SO)
- **Minnesota wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes has the higher standalone adjusted growth (13.28 vs 5.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.403); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes: DUPLICATIVE (phi 0.403); KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes: REINFORCING (phi 0.475); KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5|no: REINFORCING (phi 0.509); failure: MIN wins by 2+
- **Vancouver over 2.5 goals scored YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes has the higher standalone adjusted growth (13.28 vs 4.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.435); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes: DUPLICATIVE (phi 0.435); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: REINFORCING (phi 0.475); KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5|no: MOSTLY_INDEPENDENT (phi -0.006); failure: VAN offense suppressed (<= 2 goals)
- **Minnesota over 4.5 goals scored NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes has the higher standalone adjusted growth (13.28 vs 3.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.313); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25MINVAN-VAN2|yes: DUPLICATIVE (phi 0.313); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: REINFORCING (phi 0.509); KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: MIN offense succeeds (4+ goals)

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.2794): highest fidelity KXNHLSPREAD-26OCT25MINVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-VAN2|yes (same contract)
- thesis VAN:WINS (p 0.4933): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-VAN2|yes — override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT25MINVAN-MIN3|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5|no kept
- thesis VAN:OFFENSE_4PLUS (p 0.4043): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-VAN2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT25MINVAN-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.5067, phi -0.631)
- KXNHLSPREAD-26OCT25MINVAN-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.0 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2947, phi -1.0)
- KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VAN:SUPPRESSED (p 0.3742, phi -0.979)
- KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5|no: FUNDED_RESEARCH; family MIXED; loses 4% of the draws where the thesis happens; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4133, phi -0.658)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT25MINVAN-MIN3|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT25MINVAN-MIN5|no kept

portfolios: A EV +9.48 (adj +2.38) on $39.47, P(profit) 0.4933, adj growth 16.2 bp · B EV +4.20 (adj +1.48) on $23.37, P(profit) 0.4997, adj growth 13.0 bp · C EV +3.31 (adj +1.32) on $8.46, P(profit) 0.2794, adj growth 11.5 bp · R EV +1.47 (adj +0.51) on $8.00, P(profit) 0.4997, adj growth 17.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
