# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T21:09:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +26.93 | +9.83 | +23.06 | 0.641 | -51.96 | -71.60 | 77.92 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +25.01 | +15.01 | +20.92 | 0.639 | -49.00 | -63.94 | 132.88 |
| C best expression per thesis | 100.53 | +16.78 | +8.50 | +12.77 | 0.549 | -36.55 | -45.19 | 74.65 |
| R FUNDED research stakes | 17.00 | +2.07 | +1.25 | +2.43 | 0.555 | -11.42 | -11.42 | 0.00 |

## NYI @ DAL  ·  10000 joint draws  ·  438 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.621 / away 0.379

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_NYI_win | p_overtime | goals | shots DAL/NYI | DAL/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 5.95 | 26.0/25.9 | 22.9/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.48 | 5.9 | 26.1/26.0 | 22.7/22.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.079 | 0.63 | 0.37 | 0.00 | 5.99 | 30.5/20.4 | 17.5/26.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.59 | 0.41 | 0.00 | 9.29 | 27.6/27.4 | 21.7/21.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.51 | 0.49 | 0.50 | 5.85 | 30.9/20.8 | 17.7/27.6 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.063 | 0.53 | 0.47 | 0.00 | 5.87 | 20.7/30.7 | 27.2/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden Schenn: 1+ goals YES | 17 | 0.235 | 0.218 | +0.055 | +0.038 | $10.49 | FUNDED_RESEARCH | $3 | NYI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Victor Eklund: 1+ goals YES | 15 | 0.201 | 0.187 | +0.042 | +0.028 | $6.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 9 | 0.128 | 0.117 | +0.032 | +0.021 | $4.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Victor Eklund: 1+ assists NO | 75 | 0.816 | 0.781 | +0.053 | +0.017 | $17.94 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI5|yes; why: higher confidence-adjusted growth (20.84 vs 10.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.925 vs 0.539); relationships: KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT25NYIDAL-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT25NYIDAL-NYIVEKLUND73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.217); failure: NYI offense suppressed (<= 2 goals)
- **Victor Eklund: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (20.84 vs 12.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT25NYIDAL-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT25NYIDAL-NYIVEKLUND73-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: NYI offense suppressed (<= 2 goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (20.84 vs 11.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT25NYIDAL-NYIVEKLUND73-1|no: MOSTLY_INDEPENDENT (phi -0.045); failure: NYI offense suppressed (<= 2 goals)
- **Victor Eklund: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT25NYIDAL-NYIMSCHAEFER48-1|no; why: higher confidence-adjusted growth (3.70 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.217); KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT25NYIDAL-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.045); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3194): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.4516): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS_BY_2PLUS (p 0.2378): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4568, phi -0.25)
- KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4568, phi -0.207)
- KXNHLGOAL-26OCT25NYIDAL-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4568, phi -0.183)
- KXNHLAST-26OCT25NYIDAL-NYIVEKLUND73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.3194, phi -0.21)

portfolios: A EV +7.82 (adj +3.22) on $38.60, P(profit) 0.4406, adj growth 24.3 bp · B EV +7.92 (adj +4.91) on $40.23, P(profit) 0.4682, adj growth 43.3 bp · C EV +7.14 (adj +3.60) on $44.82, P(profit) 0.3272, adj growth 31.5 bp · R EV +0.92 (adj +0.63) on $3.00, P(profit) 0.2353, adj growth 21.3 bp

## MTL @ WPG  ·  10000 joint draws  ·  450 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.479 / away 0.521

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_MTL_win | p_overtime | goals | shots WPG/MTL | WPG/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.48 | 0.52 | 0.00 | 6.01 | 27.1/27.0 | 23.4/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.47 | 0.53 | 0.49 | 5.97 | 27.4/27.2 | 23.8/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.44 | 0.56 | 0.00 | 9.32 | 28.9/28.8 | 22.4/23.2 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.077 | 0.54 | 0.46 | 0.00 | 6.02 | 32.4/21.7 | 18.5/28.6 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.52 | 0.48 | 0.46 | 5.93 | 32.2/21.8 | 18.6/28.8 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.063 | 0.41 | 0.59 | 0.00 | 6.0 | 21.7/31.9 | 27.7/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alexandre Carrier: 1+ goals YES | 4 | 0.064 | 0.057 | +0.021 | +0.014 | $2.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 13 | 0.172 | 0.160 | +0.034 | +0.022 | $5.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Neal Pionk: 1+ goals NO | 89 | 0.921 | 0.911 | +0.024 | +0.014 | $17.94 | FUNDED_RESEARCH | $5 | WPG:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 30 | 0.340 | 0.329 | +0.025 | +0.014 | $4.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
- **Alexandre Carrier: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes; why: higher confidence-adjusted growth (9.78 vs 0.15 bp); alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT25MTLWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: MTL offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (8.79 vs 1.91 bp); relationships: KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT25MTLWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: WPG offense suppressed (<= 2 goals)
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT25MTLWPG-WPGMSCHEIFELE55-1|no; why: higher confidence-adjusted growth (4.53 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense succeeds (4+ goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (1.91 vs 0.01 bp); alternative not eligible: confidence-adjusted EV +0.0007 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT25MTLWPG-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WPG:OFFENSE_4PLUS (p 0.3773): highest fidelity KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.3983): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis WPG:SUPPRESSED (p 0.4089): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3825, phi -0.11)
- KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4089, phi -0.206)
- KXNHLGOAL-26OCT25MTLWPG-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3773, phi -0.119)
- KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4089, phi -0.282)

portfolios: A EV +4.87 (adj +3.11) on $34.21, P(profit) 0.4643, adj growth 25.5 bp · B EV +3.44 (adj +2.18) on $30.15, P(profit) 0.4643, adj growth 19.2 bp · C EV +0.39 (adj +0.22) on $4.92, P(profit) 0.3396, adj growth 1.9 bp · R EV +0.13 (adj +0.08) on $5.00, P(profit) 0.9208, adj growth 2.9 bp

## COL @ NSH  ·  10000 joint draws  ·  464 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.324 / away 0.676

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_COL_win | p_overtime | goals | shots NSH/COL | NSH/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.127 | 0.28 | 0.72 | 0.00 | 6.03 | 22.7/35.2 | 30.1/20.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.34 | 0.66 | 0.00 | 6.0 | 28.6/29.3 | 25.0/25.7 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.45 | 0.55 | 0.46 | 5.87 | 23.1/35.6 | 32.1/19.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.46 | 0.54 | 0.48 | 5.95 | 28.7/29.4 | 26.1/25.3 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.095 | 0.27 | 0.73 | 0.00 | 9.29 | 24.2/37.0 | 28.1/19.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.35 | 0.65 | 0.00 | 9.23 | 30.0/30.8 | 23.8/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mavrik Bourque: 1+ assists NO | 78 | 0.866 | 0.818 | +0.074 | +0.026 | $17.94 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Nathan MacKinnon: 1+ assists NO | 41 | 0.496 | 0.448 | +0.069 | +0.021 | $6.64 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.74) | EVIDENCE_MIXED | D |
| Colorado wins by over 1.5 goals NO | 53 | 0.609 | 0.567 | +0.062 | +0.020 | $8.27 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Adam Edstrom: 1+ goals YES | 11 | 0.135 | 0.127 | +0.018 | +0.010 | $2.23 | FUNDED_RESEARCH | $1 | NSH:WINS_BY_2PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT25COLNSH-4|no; why: higher confidence-adjusted growth (9.14 vs 0.04 bp); wins across more scripts (relative breadth 0.998 vs 0.365); alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT25COLNSH-COL2|no: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.045); failure: NSH offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: higher confidence-adjusted growth (3.92 vs 3.38 bp); wins across more scripts (relative breadth 1.018 vs 0.879); relationships: KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT25COLNSH-COL2|no: REINFORCING (phi 0.212); KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL3|no; why: higher confidence-adjusted growth (3.38 vs 1.78 bp); relationships: KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: REINFORCING (phi 0.212); KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.134); failure: COL wins by 2+
- **Adam Edstrom: 1+ goals YES** — thesis: NSH wins by 2+; alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25COLNSH-COL2|no has the higher standalone adjusted growth (3.38 vs 2.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.134); they share one thesis budget; relationships: KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.045); KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLSPREAD-26OCT25COLNSH-COL2|no: MOSTLY_INDEPENDENT (phi 0.134); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:SUPPRESSED (p 0.3001): highest fidelity KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no — override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT25COLNSH-COL3|no less than the minimum stake; KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no kept
- thesis GAME:TIGHT (p 0.4215): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL2|no (same contract)
- thesis NSH:WINS_BY_2PLUS (p 0.1875): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL2|no (same contract)
- KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3199, phi -0.162)
- KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 26% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4914, phi -0.316)
- KXNHLSPREAD-26OCT25COLNSH-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.391, phi -1.0)
- KXNHLGOAL-26OCT25COLNSH-NSHAEDSTROM84-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4609, phi -0.213)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT25COLNSH-COL3|no less than the minimum stake; KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no kept

portfolios: A EV +4.61 (adj +1.43) on $38.60, P(profit) 0.5352, adj growth 11.6 bp · B EV +4.02 (adj +1.41) on $35.08, P(profit) 0.6685, adj growth 12.9 bp · C EV +2.22 (adj +0.69) on $16.48, P(profit) 0.4958, adj growth 6.0 bp · R EV +0.49 (adj +0.20) on $4.00, P(profit) 0.6393, adj growth 6.4 bp

## MIN @ VAN  ·  10000 joint draws  ·  432 bet sides mapped, 26 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.368 / away 0.632

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_MIN_win | p_overtime | goals | shots VAN/MIN | VAN/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| MIN shot control · normal event (5-7) · decided (2+) | 0.117 | 0.50 | 0.50 | 0.00 | 6.01 | 22.0/34.4 | 30.5/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.56 | 0.44 | 0.00 | 6.08 | 27.8/28.5 | 25.1/24.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.47 | 0.53 | 0.45 | 5.9 | 22.4/34.4 | 30.9/19.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.54 | 0.46 | 0.47 | 5.98 | 27.9/28.7 | 25.5/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.57 | 0.43 | 0.00 | 9.41 | 29.4/30.3 | 24.4/23.0 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.084 | 0.48 | 0.52 | 0.00 | 9.26 | 23.9/35.8 | 29.3/18.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Linus Karlsson: 1+ goals YES | 16 | 0.224 | 0.206 | +0.054 | +0.037 | $9.14 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 17 | 0.232 | 0.215 | +0.052 | +0.035 | $8.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Filip Chytil: 1+ goals YES | 18 | 0.241 | 0.225 | +0.051 | +0.034 | $8.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Matt Boldy: 1+ goals NO | 58 | 0.659 | 0.638 | +0.062 | +0.041 | $17.94 | FUNDED_RESEARCH | $5 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MINVAN-VANFCHYTIL77-1|yes; why: higher confidence-adjusted growth (20.91 vs 16.38 bp); relationships: KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT25MINVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (20.91 vs 17.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT25MINVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: VAN offense suppressed (<= 2 goals)
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (20.91 vs 16.38 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: VAN offense suppressed (<= 2 goals)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no; why: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no has the higher standalone adjusted growth (27.41 vs 15.48 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.001); relationships: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT25MINVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: MIN offense succeeds (4+ goals)

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis MIN:SUPPRESSED (p 0.3975): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5197): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.4186): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3594, phi -0.202)
- KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3594, phi -0.199)
- KXNHLGOAL-26OCT25MINVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3594, phi -0.23)
- KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.264)

portfolios: A EV +9.63 (adj +2.07) on $38.60, P(profit) 0.6263, adj growth 16.6 bp · B EV +9.63 (adj +6.51) on $44.54, P(profit) 0.5482, adj growth 57.4 bp · C EV +7.03 (adj +3.99) on $34.31, P(profit) 0.3543, adj growth 35.3 bp · R EV +0.52 (adj +0.34) on $5.00, P(profit) 0.6593, adj growth 12.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT25MINVAN-VAN|yes == KXNHLGAME-26OCT25MINVAN-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
