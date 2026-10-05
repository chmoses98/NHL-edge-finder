# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-05T18:34:13Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.78 | +7.90 | +24.61 | 0.714 | -29.01 | -41.27 | 69.12 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +35.58 | +18.47 | +28.50 | 0.655 | -47.82 | -64.25 | 160.97 |
| C best expression per thesis | 150.00 | +27.42 | +12.04 | +20.12 | 0.674 | -40.90 | -52.43 | 105.94 |
| R FUNDED research stakes | 18.00 | +3.57 | +2.29 | +0.08 | 0.607 | -7.21 | -12.33 | 0.00 |

## PHI @ TBL  ·  10000 joint draws  ·  342 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.660 / away 0.340

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_PHI_win | p_overtime | goals | shots TBL/PHI | TBL/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.126 | 0.68 | 0.32 | 0.00 | 5.98 | 31.3/20.3 | 17.7/26.9 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.54 | 0.46 | 0.49 | 5.84 | 32.1/20.7 | 17.6/28.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.59 | 0.41 | 0.00 | 5.96 | 26.5/26.1 | 22.9/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.45 | 5.86 | 26.5/26.0 | 22.8/23.2 | even strength |
| TBL shot control · low event (<=4) · decided (2+) | 0.073 | 0.62 | 0.38 | 0.00 | 3.41 | 30.2/19.3 | 17.9/28.0 | even strength |
| TBL shot control · low event (<=4) · tight (1-goal/OT) | 0.068 | 0.54 | 0.46 | 0.45 | 2.75 | 30.2/19.0 | 17.6/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sean Couturier: 1+ goals YES | 10 | 0.158 | 0.141 | +0.051 | +0.035 | $7.63 | FUNDED_RESEARCH | $2 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| John Carlson: 1+ assists NO | 52 | 0.722 | 0.584 | +0.184 | +0.047 | $18.82 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 69 | 0.783 | 0.734 | +0.078 | +0.029 | $14.73 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ assists NO | 35 | 0.475 | 0.391 | +0.109 | +0.025 | $5.88 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.69) | EVIDENCE_MIXED | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT05PHITB-TB3|no; why: higher confidence-adjusted growth (26.48 vs 8.80 bp); despite a smaller raw edge (+0.051 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT05PHITB-TB3|no: MOSTLY_INDEPENDENT (phi 0.106); KXNHLAST-26OCT05PHITB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: PHI offense suppressed (<= 2 goals)
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT05PHITB-TB3|no; why: higher confidence-adjusted growth (19.25 vs 8.80 bp); relationships: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT05PHITB-TB3|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLAST-26OCT05PHITB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.094); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT05PHITB-TB2|no; why: higher confidence-adjusted growth (8.80 vs 5.97 bp); wins across more scripts (relative breadth 0.989 vs 0.869); relationships: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.106); KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLAST-26OCT05PHITB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.214); failure: TBL wins by 2+
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no; why: second expression of the same thesis: KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no has the higher standalone adjusted growth (19.25 vs 5.72 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.094); they share one thesis budget; relationships: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.094); KXNHLSPREAD-26OCT05PHITB-TB3|no: REINFORCING (phi 0.214); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.13, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:OFFENSE_4PLUS (p 0.2807): highest fidelity KXNHLTEAMTOTAL-26OCT05PHITB-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.3945): highest fidelity KXNHLSPREAD-26OCT05PHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no — override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT05PHITB-TB4|no less than the minimum stake; KXNHLAST-26OCT05PHITB-TBNKUCHEROV86-1|no kept
- thesis GAME:TIGHT (p 0.4494): highest fidelity KXNHLSPREAD-26OCT05PHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT05PHITB-TB3|no (same contract)
- KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.501, phi -0.221)
- KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 21.2 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3853, phi -0.227)
- KXNHLSPREAD-26OCT05PHITB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3393, phi -0.735)
- KXNHLAST-26OCT05PHITB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 31% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.0 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3853, phi -0.313)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26OCT05PHITB-TB4|no less than the minimum stake; KXNHLAST-26OCT05PHITB-TBNKUCHEROV86-1|no kept

portfolios: A EV +10.69 (adj +2.06) on $37.50, P(profit) 0.6644, adj growth 17.8 bp · B EV +13.53 (adj +5.11) on $47.05, P(profit) 0.6792, adj growth 45.1 bp · C EV +12.61 (adj +5.03) on $46.00, P(profit) 0.6453, adj growth 44.2 bp · R EV +1.41 (adj +0.81) on $6.00, P(profit) 0.1577, adj growth 28.1 bp

## OTT @ BOS  ·  10000 joint draws  ·  366 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.487 / away 0.513

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_OTT_win | p_overtime | goals | shots BOS/OTT | BOS/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.54 | 0.46 | 0.00 | 5.97 | 27.4/28.0 | 24.6/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.48 | 5.89 | 27.4/27.8 | 24.4/24.1 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.104 | 0.45 | 0.55 | 0.00 | 5.99 | 21.5/33.1 | 29.2/18.3 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.46 | 0.54 | 0.46 | 5.87 | 21.8/33.5 | 30.0/18.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.52 | 0.48 | 0.00 | 9.12 | 28.5/29.1 | 23.2/22.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.54 | 0.46 | 0.00 | 3.42 | 26.1/26.6 | 24.8/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Marat Khusnutdinov: 1+ goals YES | 9 | 0.151 | 0.135 | +0.056 | +0.039 | $8.89 | FUNDED_RESEARCH | $3 | BOS:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Hayden Hodgson: 1+ goals YES | 6 | 0.100 | 0.088 | +0.036 | +0.024 | $5.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 7 | 0.110 | 0.099 | +0.035 | +0.024 | $5.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Casey Mittelstadt: 1+ goals YES | 14 | 0.190 | 0.176 | +0.042 | +0.028 | $7.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05OTTBOS-BOSCMITTELSTADT11-1|yes; why: higher confidence-adjusted growth (37.00 vs 13.23 bp); relationships: KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT05OTTBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: BOS offense suppressed (<= 2 goals)
- **Hayden Hodgson: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (19.86 vs 4.81 bp); relationships: KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT05OTTBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: OTT offense suppressed (<= 2 goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (17.71 vs 4.81 bp); relationships: KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT05OTTBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: OTT offense suppressed (<= 2 goals)
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT05OTTBOS-BOSMGEEKIE39-1|yes; why: higher confidence-adjusted growth (13.23 vs 2.48 bp); despite a smaller raw edge (+0.042 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.3561): highest fidelity KXNHLAST-26OCT05OTTBOS-BOSMGEEKIE39-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT05OTTBOS-BOSCMITTELSTADT11-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.4243): highest fidelity KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.3555): highest fidelity KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes (same contract)
- KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4243, phi -0.183)
- KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4252, phi -0.158)
- KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4252, phi -0.145)
- KXNHLGOAL-26OCT05OTTBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4243, phi -0.199)

portfolios: A EV +5.09 (adj +1.50) on $37.50, P(profit) 0.7558, adj growth 14.2 bp · B EV +12.67 (adj +8.64) on $26.68, P(profit) 0.4555, adj growth 74.2 bp · C EV +7.02 (adj +3.43) on $45.89, P(profit) 0.6523, adj growth 30.2 bp · R EV +1.74 (adj +1.22) on $3.00, P(profit) 0.1514, adj growth 39.4 bp

## WPG @ PIT  ·  10000 joint draws  ·  348 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.612 / away 0.388

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_WPG_win | p_overtime | goals | shots PIT/WPG | PIT/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.68 | 0.32 | 0.00 | 5.98 | 27.2/26.8 | 24.0/22.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.108 | 0.74 | 0.26 | 0.00 | 5.99 | 32.4/21.3 | 18.9/27.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.54 | 0.46 | 0.45 | 5.9 | 27.0/26.9 | 23.6/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.68 | 0.32 | 0.00 | 9.42 | 29.0/28.6 | 23.4/21.7 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.57 | 0.43 | 0.47 | 5.92 | 32.5/21.6 | 18.5/29.0 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.079 | 0.76 | 0.24 | 0.00 | 9.35 | 34.2/22.9 | 18.6/25.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 14 | 0.198 | 0.182 | +0.049 | +0.034 | $8.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Morgan Barron: 1+ goals YES | 10 | 0.133 | 0.123 | +0.027 | +0.017 | $4.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ goals NO | 77 | 0.803 | 0.794 | +0.021 | +0.011 | $12.86 | FUNDED_RESEARCH | $4 | PIT:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Egor Chinakhov: 1+ assists YES | 32 | 0.382 | 0.346 | +0.047 | +0.011 | $3.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes; why: higher confidence-adjusted growth (19.12 vs 1.17 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT05WPGPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes: MOSTLY_INDEPENDENT (phi 0.034); failure: PIT offense suppressed (<= 2 goals)
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05WPGPIT-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (6.70 vs 0.82 bp); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT05WPGPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: WPG offense suppressed (<= 2 goals)
- **Ben Kindel: 1+ goals NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05WPGPIT-PITEMALKIN71-1|no; why: higher confidence-adjusted growth (1.63 vs 0.11 bp); alternative not eligible: confidence-adjusted EV +0.0032 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes: MOSTLY_INDEPENDENT (phi -0.049); failure: PIT offense succeeds (4+ goals)
- **Egor Chinakhov: 1+ assists YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (19.12 vs 1.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.034); they share one thesis budget; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.034); KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT05WPGPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.049); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4982): highest fidelity KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3161): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis PIT:SUPPRESSED (p 0.2956): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.2956, phi -0.19)
- KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4715, phi -0.192)
- KXNHLGOAL-26OCT05WPGPIT-PITBKINDEL81-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4982, phi -0.181)
- KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.2956, phi -0.276)

portfolios: A EV +6.10 (adj +3.36) on $37.50, P(profit) 0.5087, adj growth 28.1 bp · B EV +4.75 (adj +2.93) on $29.21, P(profit) 0.3067, adj growth 25.4 bp · C EV +2.97 (adj +2.02) on $8.94, P(profit) 0.1977, adj growth 17.4 bp · R EV +0.11 (adj +0.06) on $4.00, P(profit) 0.8032, adj growth 2.0 bp

## SJS @ DAL  ·  10000 joint draws  ·  362 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.642 / away 0.358

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_SJS_win | p_overtime | goals | shots DAL/SJS | DAL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.58 | 0.42 | 0.00 | 6.02 | 26.6/26.3 | 23.1/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.50 | 0.50 | 0.48 | 5.88 | 26.6/26.3 | 23.1/23.2 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.103 | 0.61 | 0.39 | 0.00 | 6.04 | 31.6/20.8 | 18.0/27.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.53 | 0.47 | 0.49 | 5.9 | 31.4/20.7 | 17.6/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.56 | 0.44 | 0.00 | 9.27 | 28.3/27.9 | 22.3/22.0 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.068 | 0.66 | 0.34 | 0.00 | 9.2 | 33.0/22.2 | 17.5/25.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mikko Rantanen: 1+ goals NO | 67 | 0.729 | 0.713 | +0.043 | +0.027 | $16.61 | FUNDED_RESEARCH | $5 | DAL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 69 | 0.812 | 0.726 | +0.107 | +0.021 | $16.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Jason Robertson: 1+ goals NO | 58 | 0.631 | 0.617 | +0.034 | +0.020 | $10.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Igor Chernyshov: 1+ goals YES | 18 | 0.215 | 0.205 | +0.025 | +0.015 | $3.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no; why: higher confidence-adjusted growth (7.65 vs 4.05 bp); despite a smaller raw edge (+0.043 vs +0.110/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26OCT05SJDAL-SJICHERNYSHOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: DAL offense succeeds (4+ goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05SJDAL-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (4.79 vs 0.05 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0023 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT05SJDAL-SJICHERNYSHOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.044); failure: SJS offense succeeds (4+ goals)
- **Jason Robertson: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no has the higher standalone adjusted growth (7.65 vs 3.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.034); they share one thesis budget; relationships: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT05SJDAL-SJICHERNYSHOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: DAL offense succeeds (4+ goals)
- **Igor Chernyshov: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT05SJDAL-DAL3|no; why: Player prop expression KXNHLGOAL-26OCT05SJDAL-SJICHERNYSHOV92-1|yes selected over player prop KXNHLAST-26OCT05SJDAL-SJDORLOV9-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.34 vs 0.50 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.044); KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DAL:SUPPRESSED (p 0.3644): highest fidelity KXNHLSPREAD-26OCT05SJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.4353): highest fidelity KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3447): highest fidelity KXNHLSPREAD-26OCT05SJDAL-DAL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT05SJDAL-DAL3|no (same contract)
- KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4208, phi -0.235)
- KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.2 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3447, phi -0.214)
- KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4208, phi -0.258)
- KXNHLGOAL-26OCT05SJDAL-SJICHERNYSHOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4353, phi -0.218)
- override: Player prop expression KXNHLGOAL-26OCT05SJDAL-SJICHERNYSHOV92-1|yes selected over player prop KXNHLAST-26OCT05SJDAL-SJDORLOV9-1|yes because adjusted EV differs by only 0.2 pts while thesis capture is 0.34 vs 0.50 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.91 (adj +0.98) on $37.50, P(profit) 0.7586, adj growth 9.0 bp · B EV +4.63 (adj +1.79) on $47.05, P(profit) 0.6438, adj growth 16.3 bp · C EV +4.82 (adj +1.56) on $49.17, P(profit) 0.5895, adj growth 14.1 bp · R EV +0.32 (adj +0.20) on $5.00, P(profit) 0.7288, adj growth 7.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
