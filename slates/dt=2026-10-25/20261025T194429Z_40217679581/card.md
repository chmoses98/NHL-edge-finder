# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-25T19:44:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +29.64 | +11.14 | +21.93 | 0.634 | -58.16 | -76.92 | 85.92 |
| B thesis-diversified (joint) ← optimiser card | 124.38 | +20.85 | +11.81 | +15.22 | 0.622 | -43.28 | -59.84 | 103.75 |
| C best expression per thesis | 80.01 | +14.11 | +7.15 | +6.39 | 0.555 | -36.89 | -42.67 | 62.31 |
| R FUNDED research stakes | 12.00 | +2.22 | +1.34 | -0.78 | 0.279 | -7.39 | -7.39 | 0.00 |

## NYI @ DAL  ·  10000 joint draws  ·  442 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.632 / away 0.368

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_NYI_win | p_overtime | goals | shots DAL/NYI | DAL/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.58 | 0.42 | 0.00 | 6.02 | 26.1/26.0 | 23.0/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.49 | 5.9 | 26.0/26.0 | 22.8/22.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.077 | 0.66 | 0.34 | 0.00 | 5.95 | 30.7/20.6 | 17.9/26.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.57 | 0.43 | 0.00 | 9.34 | 27.7/27.4 | 21.9/21.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.53 | 0.47 | 0.48 | 5.83 | 30.8/20.8 | 17.5/27.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.55 | 0.45 | 0.00 | 3.42 | 24.8/25.0 | 23.2/22.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden Schenn: 1+ goals YES | 16 | 0.228 | 0.208 | +0.058 | +0.039 | $10.72 | FUNDED_RESEARCH | $3 | NYI:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.160 | 0.147 | +0.033 | +0.020 | $5.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Victor Eklund: 1+ goals YES | 16 | 0.202 | 0.188 | +0.032 | +0.018 | $5.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| David Perron: 1+ goals YES | 13 | 0.163 | 0.154 | +0.025 | +0.016 | $4.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes; why: higher confidence-adjusted growth (22.91 vs 7.83 bp); relationships: KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT25NYIDAL-DALDPERRON57-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: NYI offense suppressed (<= 2 goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (22.91 vs 7.83 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT25NYIDAL-DALDPERRON57-1|yes: MOSTLY_INDEPENDENT (phi -0.021); failure: NYI offense suppressed (<= 2 goals)
- **Victor Eklund: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (22.91 vs 5.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT25NYIDAL-DALDPERRON57-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: NYI offense suppressed (<= 2 goals)
- **David Perron: 1+ goals YES** — thesis: DAL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT25NYIDAL-7|yes; why: higher confidence-adjusted growth (4.55 vs 1.43 bp); despite a smaller raw edge (+0.025 vs +0.046/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.919 vs 0.682); relationships: KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: DAL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3175): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.4477): highest fidelity KXNHLSPREAD-26OCT25NYIDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS_BY_2PLUS (p 0.2276): highest fidelity KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT25NYIDAL-NYI3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT25NYIDAL-NYIBSCHENN10-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4667, phi -0.239)
- KXNHLGOAL-26OCT25NYIDAL-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4667, phi -0.204)
- KXNHLGOAL-26OCT25NYIDAL-NYIVEKLUND73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4667, phi -0.219)
- KXNHLGOAL-26OCT25NYIDAL-DALDPERRON57-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:SUPPRESSED (p 0.3863, phi -0.196)

portfolios: A EV +8.41 (adj +3.87) on $42.42, P(profit) 0.4348, adj growth 28.9 bp · B EV +6.85 (adj +4.36) on $25.71, P(profit) 0.5709, adj growth 37.6 bp · C EV +4.78 (adj +2.71) on $23.93, P(profit) 0.3748, adj growth 23.3 bp · R EV +1.03 (adj +0.69) on $3.00, P(profit) 0.2276, adj growth 23.2 bp

## MTL @ WPG  ·  10000 joint draws  ·  446 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.482 / away 0.518

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_MTL_win | p_overtime | goals | shots WPG/MTL | WPG/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.43 | 0.57 | 0.00 | 6.01 | 27.2/27.1 | 23.3/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.50 | 0.50 | 0.48 | 5.91 | 27.1/27.2 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.48 | 0.52 | 0.00 | 9.26 | 28.8/28.6 | 22.5/22.7 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.077 | 0.53 | 0.47 | 0.00 | 5.99 | 32.1/21.5 | 18.3/28.1 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.50 | 0.50 | 0.47 | 5.88 | 32.4/21.7 | 18.6/29.0 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.061 | 0.41 | 0.59 | 0.00 | 5.99 | 21.8/31.9 | 27.7/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alexandre Carrier: 1+ goals YES | 4 | 0.068 | 0.059 | +0.025 | +0.017 | $3.68 | FUNDED_RESEARCH | $1 | MTL:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Alex Iafallo: 1+ goals YES | 13 | 0.170 | 0.152 | +0.032 | +0.014 | $3.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 29 | 0.335 | 0.323 | +0.031 | +0.018 | $6.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
- **Alexandre Carrier: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-MTLJANDERSON17-1|yes; why: higher confidence-adjusted growth (14.53 vs 0.26 bp); alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: MTL offense suppressed (<= 2 goals)
- **Alex Iafallo: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (3.79 vs 3.39 bp); relationships: KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26OCT25MTLWPG-WPGDSAMBERG54-1|yes; why: higher confidence-adjusted growth (3.39 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis WPG:OFFENSE_4PLUS (p 0.3703): highest fidelity KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.3953): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT25MTLWPG-MTLACARRIER45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3782, phi -0.108)
- KXNHLGOAL-26OCT25MTLWPG-WPGAIAFALLO9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4181, phi -0.204)
- KXNHLGOAL-26OCT25MTLWPG-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4181, phi -0.28)

portfolios: A EV +6.00 (adj +3.56) on $22.74, P(profit) 0.4819, adj growth 27.3 bp · B EV +3.63 (adj +2.21) on $13.56, P(profit) 0.4819, adj growth 18.8 bp · C EV +0.64 (adj +0.38) on $6.38, P(profit) 0.3351, adj growth 3.3 bp · R EV +0.59 (adj +0.39) on $1.00, P(profit) 0.0677, adj growth 13.1 bp

## COL @ NSH  ·  10000 joint draws  ·  464 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.325 / away 0.675

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
| Mavrik Bourque: 1+ assists NO | 79 | 0.866 | 0.821 | +0.065 | +0.019 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Nathan MacKinnon: 1+ assists NO | 41 | 0.496 | 0.448 | +0.069 | +0.021 | $7.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.74) | EVIDENCE_MIXED | D |
| Colorado wins by over 1.5 goals NO | 53 | 0.609 | 0.567 | +0.062 | +0.020 | $6.08 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado wins by over 2.5 goals NO | 66 | 0.732 | 0.694 | +0.057 | +0.018 | $7.46 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT25COLNSH-4|no; why: higher confidence-adjusted growth (5.00 vs 0.04 bp); wins across more scripts (relative breadth 0.998 vs 0.365); alternative not eligible: confidence-adjusted EV +0.0013 below the 0.010/contract floor; relationships: KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT25COLNSH-COL2|no: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLSPREAD-26OCT25COLNSH-COL3|no: INTENTIONAL_DIVERSIFIER (phi -0.092); failure: NSH offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: higher confidence-adjusted growth (3.92 vs 3.38 bp); wins across more scripts (relative breadth 1.018 vs 0.879); relationships: KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT25COLNSH-COL2|no: REINFORCING (phi 0.212); KXNHLSPREAD-26OCT25COLNSH-COL3|no: REINFORCING (phi 0.2); failure: COL offense succeeds (4+ goals)
- **Colorado wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL3|no; why: higher confidence-adjusted growth (3.38 vs 3.24 bp); relationships: KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.119); KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: REINFORCING (phi 0.212); KXNHLSPREAD-26OCT25COLNSH-COL3|no: DUPLICATIVE (phi 0.754); failure: COL wins by 2+
- **Colorado wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT25COLNSH-COL2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT25COLNSH-COL2|no has the higher standalone adjusted growth (3.38 vs 3.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.754); they share one thesis budget; relationships: KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.092); KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: REINFORCING (phi 0.2); KXNHLSPREAD-26OCT25COLNSH-COL2|no: DUPLICATIVE (phi 0.754); failure: COL wins by 2+

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:SUPPRESSED (p 0.3001): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no less than the minimum stake; KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no kept
- thesis GAME:TIGHT (p 0.4215): highest fidelity KXNHLSPREAD-26OCT25COLNSH-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25COLNSH-COL2|no (same contract)
- thesis NSH:SUPPRESSED (p 0.4609): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT25COLNSH-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3199, phi -0.162)
- KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 26% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4914, phi -0.316)
- KXNHLSPREAD-26OCT25COLNSH-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.391, phi -1.0)
- KXNHLSPREAD-26OCT25COLNSH-COL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.391, phi -0.754)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT25COLNSH-COL4|no less than the minimum stake; KXNHLAST-26OCT25COLNSH-COLNMACKINNON29-1|no kept

portfolios: A EV +4.65 (adj +1.43) on $42.42, P(profit) 0.6142, adj growth 11.9 bp · B EV +4.07 (adj +1.24) on $40.68, P(profit) 0.6393, adj growth 11.1 bp · C EV +2.22 (adj +0.69) on $16.48, P(profit) 0.4958, adj growth 6.0 bp · R EV +0.39 (adj +0.12) on $4.00, P(profit) 0.609, adj growth 4.3 bp

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
| Kirill Kaprizov: 2+ goals NO | 86 | 0.915 | 0.899 | +0.046 | +0.030 | $15.00 | FUNDED_RESEARCH | $4 | MIN:SUPPRESSED | DIRECT (0.99) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 16 | 0.224 | 0.203 | +0.054 | +0.033 | $7.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Matt Boldy: 1+ goals NO | 58 | 0.659 | 0.637 | +0.062 | +0.040 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 18 | 0.232 | 0.217 | +0.041 | +0.027 | $6.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Kirill Kaprizov: 2+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no; why: Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no selected over broad KXNHLSPREAD-26OCT25MINVAN-MIN2|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.97 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.027); failure: MIN offense succeeds (4+ goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT25MINVAN-VAN3|yes; why: higher confidence-adjusted growth (16.92 vs 14.00 bp); despite a smaller raw edge (+0.054 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.889 vs 0.466); relationships: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: VAN offense suppressed (<= 2 goals)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no; why: second expression of the same thesis: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no has the higher standalone adjusted growth (17.85 vs 14.55 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: MIN offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (16.92 vs 10.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts MIN shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, MIN shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis MIN:SUPPRESSED (p 0.3975): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.5197): highest fidelity KXNHLSPREAD-26OCT25MINVAN-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT25MINVAN-MIN2|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.4186): highest fidelity KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no: FUNDED_RESEARCH; family TRUSTED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.263)
- KXNHLGOAL-26OCT25MINVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3594, phi -0.202)
- KXNHLGOAL-26OCT25MINVAN-MINMBOLDY12-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.3883, phi -0.264)
- KXNHLGOAL-26OCT25MINVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3594, phi -0.199)
- override: Player prop expression KXNHLGOAL-26OCT25MINVAN-MINKKAPRIZOV97-2|no selected over broad KXNHLSPREAD-26OCT25MINVAN-MIN2|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.97 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +10.58 (adj +2.28) on $42.42, P(profit) 0.6263, adj growth 17.8 bp · B EV +6.29 (adj +4.00) on $44.43, P(profit) 0.4008, adj growth 36.2 bp · C EV +6.47 (adj +3.37) on $33.22, P(profit) 0.3543, adj growth 29.7 bp · R EV +0.21 (adj +0.14) on $4.00, P(profit) 0.9148, adj growth 5.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT25MINVAN-VAN|yes == KXNHLGAME-26OCT25MINVAN-MIN|no

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
