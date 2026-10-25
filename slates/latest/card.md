# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T11:34:52Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +24.24 | +5.50 | +22.71 | 0.645 | -52.77 | -72.22 | 37.67 |
| B thesis-diversified (joint) ← optimiser card | 113.23 | +18.08 | +6.92 | +19.07 | 0.664 | -34.38 | -51.92 | 60.55 |
| C best expression per thesis | 82.68 | +13.07 | +5.30 | +15.83 | 0.587 | -34.06 | -40.98 | 46.33 |
| R FUNDED research stakes | 28.00 | +4.00 | +1.37 | +4.26 | 0.677 | -8.84 | -12.98 | 0.00 |

## FLA @ CHI  ·  10000 joint draws  ·  436 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_FLA_win | p_overtime | goals | shots CHI/FLA | CHI/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.46 | 0.54 | 0.00 | 6.05 | 26.4/27.0 | 23.2/23.0 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.109 | 0.42 | 0.58 | 0.00 | 5.96 | 20.8/32.0 | 27.9/17.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.48 | 5.92 | 26.4/26.8 | 23.5/23.1 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.49 | 0.51 | 0.43 | 5.85 | 20.9/32.1 | 28.8/17.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.50 | 0.50 | 0.00 | 9.34 | 27.9/28.4 | 22.2/21.7 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.073 | 0.38 | 0.62 | 0.00 | 9.22 | 22.3/33.9 | 26.4/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Cole Schwindt: 1+ goals YES | 10 | 0.151 | 0.128 | +0.045 | +0.022 | $5.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 63 | 0.695 | 0.676 | +0.049 | +0.030 | $19.29 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 73 | 0.809 | 0.767 | +0.065 | +0.023 | $20.00 | FUNDED_RESEARCH | $5 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ryan Greene: 1+ goals YES | 12 | 0.158 | 0.145 | +0.031 | +0.018 | $4.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT25FLACHI-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (10.94 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSPREAD-26OCT25FLACHI-FLA3|no: INTENTIONAL_DIVERSIFIER (phi -0.181); KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: FLA offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25FLACHI-FLA3|no; why: higher confidence-adjusted growth (8.74 vs 6.22 bp); despite a smaller raw edge (+0.049 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSPREAD-26OCT25FLACHI-FLA3|no: REINFORCING (phi 0.156); KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25FLACHI-CHI2|yes; why: higher confidence-adjusted growth (6.22 vs 2.09 bp); wins across more scripts (relative breadth 1.01 vs 0.54); relationships: KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.181); KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: REINFORCING (phi 0.156); KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.096); failure: FLA wins by 2+
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25FLACHI-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25FLACHI-FLA3|no has the higher standalone adjusted growth (6.22 vs 6.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.096); they share one thesis budget; relationships: KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT25FLACHI-FLA3|no: MOSTLY_INDEPENDENT (phi 0.096); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis FLA:OFFENSE_4PLUS (p 0.4002): highest fidelity KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes (same contract)
- thesis FLA:SUPPRESSED (p 0.3764): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.4714): highest fidelity KXNHLSPREAD-26OCT25FLACHI-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25FLACHI-FLA3|no (same contract)
- KXNHLGOAL-26OCT25FLACHI-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3764, phi -0.193)
- KXNHLGOAL-26OCT25FLACHI-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4002, phi -0.235)
- KXNHLSPREAD-26OCT25FLACHI-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3045, phi -0.734)
- KXNHLGOAL-26OCT25FLACHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4176, phi -0.181)

portfolios: A EV +4.54 (adj +0.96) on $39.47, P(profit) 0.6551, adj growth 7.2 bp · B EV +6.74 (adj +3.34) on $49.51, P(profit) 0.7128, adj growth 29.3 bp · C EV +5.66 (adj +2.72) on $45.12, P(profit) 0.6707, adj growth 24.0 bp · R EV +0.82 (adj +0.39) on $10.00, P(profit) 0.5907, adj growth 13.7 bp

## NYI @ DAL  ·  10000 joint draws  ·  408 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_NYI_win | p_overtime | goals | shots DAL/NYI | DAL/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.58 | 0.42 | 0.00 | 6.0 | 26.1/25.9 | 22.7/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.53 | 0.47 | 0.45 | 5.88 | 26.0/26.0 | 22.8/22.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.58 | 0.42 | 0.00 | 9.24 | 27.7/27.6 | 22.1/21.4 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.079 | 0.64 | 0.36 | 0.00 | 5.98 | 30.5/20.6 | 17.8/26.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.53 | 0.47 | 0.45 | 5.9 | 30.9/20.8 | 17.5/27.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.57 | 0.43 | 0.00 | 3.42 | 24.6/24.6 | 22.9/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.166 | 0.152 | +0.028 | +0.014 | $3.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 73 | 0.796 | 0.760 | +0.052 | +0.017 | $13.05 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New York I over 3.5 goals scored YES | 26 | 0.330 | 0.290 | +0.057 | +0.017 | $2.26 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Bo Horvat: 1+ goals YES | 28 | 0.321 | 0.306 | +0.027 | +0.012 | $2.58 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5|yes; why: KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5|yes has the higher standalone adjusted growth (3.99 vs 3.69 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.180); relationships: KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.103); KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: REINFORCING (phi 0.211); KXNHLGOAL-26OCT25NYIDAL-NYIBHORVAT14-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: NYI offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25NYIDAL-DAL2|no; why: higher confidence-adjusted growth (3.14 vs 1.80 bp); wins across more scripts (relative breadth 0.99 vs 0.875); relationships: KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.103); KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: DUPLICATIVE (phi 0.312); KXNHLGOAL-26OCT25NYIDAL-NYIBHORVAT14-1|yes: MOSTLY_INDEPENDENT (phi 0.147); failure: DAL wins by 2+
- **New York I over 3.5 goals scored YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5|yes; why: Broad expression KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes selected over broad KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: REINFORCING (phi 0.211); KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: DUPLICATIVE (phi 0.312); KXNHLGOAL-26OCT25NYIDAL-NYIBHORVAT14-1|yes: REINFORCING (phi 0.266); failure: NYI offense suppressed (<= 2 goals)
- **Bo Horvat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5|yes; why: KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5|yes has the higher standalone adjusted growth (3.99 vs 1.42 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.231); relationships: KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: MOSTLY_INDEPENDENT (phi 0.147); KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: REINFORCING (phi 0.266); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3212): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes (same contract)
- thesis NYI:WINS (p 0.4417): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4484): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25NYIDAL-DAL3|no (same contract)
- KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4642, phi -0.208)
- KXNHLSPREAD-26OCT25NYIDAL-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.324, phi -0.732)
- KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NYI:SUPPRESSED (p 0.4642, phi -0.653)
- KXNHLGOAL-26OCT25NYIDAL-NYIBHORVAT14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4642, phi -0.289)
- override: Broad expression KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes selected over broad KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5|yes because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.50 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.67 (adj +1.34) on $39.47, P(profit) 0.5003, adj growth 8.4 bp · B EV +2.27 (adj +0.86) on $21.07, P(profit) 0.5096, adj growth 7.5 bp · C EV +2.04 (adj +0.64) on $17.49, P(profit) 0.7977, adj growth 5.6 bp · R EV +0.58 (adj +0.19) on $6.00, P(profit) 0.4466, adj growth 6.3 bp

## MTL @ WPG  ·  10000 joint draws  ·  388 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_MTL_win | p_overtime | goals | shots WPG/MTL | WPG/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.43 | 0.57 | 0.00 | 6.01 | 27.2/27.1 | 23.3/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.50 | 0.50 | 0.48 | 5.91 | 27.1/27.2 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.48 | 0.52 | 0.00 | 9.26 | 28.8/28.6 | 22.5/22.7 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.077 | 0.53 | 0.47 | 0.00 | 5.99 | 32.1/21.5 | 18.3/28.1 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.50 | 0.50 | 0.47 | 5.88 | 32.4/21.7 | 18.6/29.0 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.061 | 0.41 | 0.59 | 0.00 | 5.99 | 21.8/31.9 | 27.7/18.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## COL @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_COL_win | p_overtime | goals | shots NSH/COL | NSH/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.126 | 0.30 | 0.70 | 0.00 | 6.01 | 22.8/35.4 | 30.5/20.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.33 | 0.67 | 0.00 | 6.06 | 28.5/29.4 | 24.9/25.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.100 | 0.30 | 0.70 | 0.00 | 9.32 | 24.1/37.0 | 28.7/19.5 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.45 | 0.55 | 0.48 | 5.91 | 22.8/35.3 | 31.8/19.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.47 | 0.53 | 0.47 | 6.06 | 28.5/29.3 | 25.9/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.34 | 0.66 | 0.00 | 9.44 | 30.4/31.2 | 23.8/24.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Colorado wins by over 1.5 goals NO | 53 | 0.612 | 0.569 | +0.065 | +0.021 | $7.59 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 66 | 0.734 | 0.694 | +0.058 | +0.018 | $7.62 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL3|no; why: higher confidence-adjusted growth (3.90 vs 3.44 bp); relationships: KXNHLSPREAD-26OCT25COLNSH-COL3|no: DUPLICATIVE (phi 0.757); failure: COL wins by 2+
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25COLNSH-COL2|no has the higher standalone adjusted growth (3.90 vs 3.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.757); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25COLNSH-COL2|no: DUPLICATIVE (phi 0.757); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · high event (8+) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.4179): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL2|no (same contract)
- KXNHLSPREAD-26OCT25COLNSH-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3881, phi -1.0)
- KXNHLSPREAD-26OCT25COLNSH-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3881, phi -0.757)

portfolios: A EV +3.21 (adj +1.04) on $31.58, P(profit) 0.6119, adj growth 7.7 bp · B EV +1.55 (adj +0.50) on $15.22, P(profit) 0.6119, adj growth 4.4 bp · C EV +1.40 (adj +0.46) on $11.90, P(profit) 0.6119, adj growth 4.0 bp · R EV +0.41 (adj +0.13) on $4.00, P(profit) 0.6119, adj growth 4.6 bp

## MIN @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_MIN_win | p_overtime | goals | shots VAN/MIN | VAN/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| MIN shot control · normal event (5-7) · decided (2+) | 0.120 | 0.50 | 0.50 | 0.00 | 6.01 | 22.4/34.5 | 30.8/19.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.55 | 0.45 | 0.00 | 6.01 | 27.8/28.4 | 25.1/24.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.47 | 0.53 | 0.45 | 5.98 | 22.1/34.3 | 30.6/18.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.54 | 0.46 | 0.47 | 5.92 | 28.2/28.9 | 25.6/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.56 | 0.44 | 0.00 | 9.49 | 29.5/30.3 | 24.5/23.1 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.083 | 0.49 | 0.51 | 0.00 | 9.31 | 23.9/36.1 | 29.6/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 2.5 goals YES | 12 | 0.199 | 0.154 | +0.071 | +0.027 | $3.71 | FUNDED_RESEARCH | $1 | VAN:WINS_BY_2PLUS | DIRECT (0.65) | EVIDENCE_MIXED | D |
| Minnesota wins by over 1.5 goals NO | 58 | 0.739 | 0.632 | +0.141 | +0.035 | $15.82 | FUNDED_RESEARCH | $4 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vancouver over 4.5 goals scored YES | 17 | 0.251 | 0.205 | +0.071 | +0.025 | $2.16 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | DIRECT (0.58) | EVIDENCE_MIXED | D |
| Minnesota wins by over 2.5 goals NO | 71 | 0.832 | 0.750 | +0.108 | +0.025 | $5.74 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Vancouver wins by over 2.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26OCT25MINVAN-MIN2|no; why: higher confidence-adjusted growth (13.95 vs 11.31 bp); despite a smaller raw edge (+0.071 vs +0.141/contract); relationships: KXNHLSPREAD-26OCT25MINVAN-MIN2|no: REINFORCING (phi 0.296); KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes: REINFORCING (phi 0.522); KXNHLSPREAD-26OCT25MINVAN-MIN3|no: REINFORCING (phi 0.224); failure: MIN wins (incl. OT/SO)
- **Minnesota wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes has the higher standalone adjusted growth (13.95 vs 11.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.296); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes: REINFORCING (phi 0.296); KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes: DUPLICATIVE (phi 0.308); KXNHLSPREAD-26OCT25MINVAN-MIN3|no: DUPLICATIVE (phi 0.755); failure: MIN wins by 2+
- **Vancouver over 4.5 goals scored YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: second expression of the same thesis: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes has the higher standalone adjusted growth (13.95 vs 9.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.522); they share one thesis budget; relationships: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes: REINFORCING (phi 0.522); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: DUPLICATIVE (phi 0.308); KXNHLSPREAD-26OCT25MINVAN-MIN3|no: REINFORCING (phi 0.241); failure: MIN wins (incl. OT/SO)
- **Minnesota wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: Broad expression KXNHLSPREAD-26OCT25MINVAN-MIN3|no selected over broad KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2|no because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.47 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes: REINFORCING (phi 0.224); KXNHLSPREAD-26OCT25MINVAN-MIN2|no: DUPLICATIVE (phi 0.755); KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes: REINFORCING (phi 0.241); failure: MIN wins by 2+

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.304): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- thesis VAN:WINS (p 0.5303): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.4295): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT25MINVAN-VAN3|yes: FUNDED_RESEARCH; family MIXED; loses 35% of the draws where the thesis happens; opposing: failure thesis MIN:WINS (p 0.4697, phi -0.469)
- KXNHLSPREAD-26OCT25MINVAN-MIN2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.4 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2614, phi -1.0)
- KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5|yes: FUNDED_RESEARCH; family MIXED; loses 42% of the draws where the thesis happens; opposing: failure thesis MIN:WINS (p 0.4697, phi -0.448)
- KXNHLSPREAD-26OCT25MINVAN-MIN3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 12.7 pts; opposing: failure thesis MIN:WINS_BY_2PLUS (p 0.2614, phi -0.755)
- override: Broad expression KXNHLSPREAD-26OCT25MINVAN-MIN3|no selected over broad KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2|no because adjusted EV is 0.3 pts higher while thesis capture is 1.00 vs 0.47 (STRUCTURAL vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +11.82 (adj +2.16) on $39.47, P(profit) 0.5303, adj growth 14.3 bp · B EV +7.53 (adj +2.22) on $27.43, P(profit) 0.7386, adj growth 19.4 bp · C EV +3.98 (adj +1.48) on $8.17, P(profit) 0.3092, adj growth 12.7 bp · R EV +2.20 (adj +0.66) on $8.00, P(profit) 0.7424, adj growth 22.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT25MINVAN-VAN|yes == KXNHLGAME-26OCT25MINVAN-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
