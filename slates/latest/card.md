# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-15T17:13:22Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +27.20 | +7.28 | +26.42 | 0.804 | -12.89 | -23.48 | 67.76 |
| B thesis-diversified (joint) ← optimiser card | 149.02 | +18.98 | +9.30 | +17.68 | 0.739 | -16.67 | -26.54 | 88.80 |
| C best expression per thesis | 149.99 | +24.75 | +9.37 | +21.83 | 0.738 | -19.61 | -29.53 | 87.39 |
| R FUNDED research stakes | 20.00 | +2.04 | +1.18 | +1.56 | 0.572 | -4.43 | -6.49 | 0.00 |

## BUF @ TOR  ·  10000 joint draws  ·  444 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.519 / away 0.480

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_BUF_win | p_overtime | goals | shots TOR/BUF | TOR/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.50 | 0.50 | 0.00 | 6.06 | 28.1/28.8 | 25.2/24.6 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.110 | 0.48 | 0.52 | 0.00 | 6.0 | 22.2/34.0 | 30.2/18.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.49 | 5.95 | 28.2/28.9 | 25.4/24.9 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.48 | 0.52 | 0.48 | 5.92 | 22.4/34.5 | 31.2/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.53 | 0.47 | 0.00 | 9.36 | 29.3/30.2 | 23.9/22.8 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.086 | 0.45 | 0.55 | 0.00 | 9.39 | 23.7/36.0 | 29.0/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Owen Power: 1+ goals NO | 88 | 0.915 | 0.905 | +0.028 | +0.018 | $7.53 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ assists NO | 70 | 0.763 | 0.729 | +0.049 | +0.014 | $5.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Sergei Bobrovsky: 26+ saves YES | 50 | 0.566 | 0.530 | +0.048 | +0.013 | $2.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:NET_HIGH_VOLUME | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ assists NO | 58 | 0.645 | 0.608 | +0.048 | +0.011 | $2.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BUF:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (6.90 vs 1.04 bp); despite a smaller raw edge (+0.028 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.063); failure: BUF offense succeeds (4+ goals)
- **Gavin McKenna: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15BUFTOR-TORDRADDYSH43-1|no; why: higher confidence-adjusted growth (2.23 vs 0.32 bp); alternative not eligible: confidence-adjusted EV +0.0059 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: TOR offense succeeds (4+ goals)
- **Sergei Bobrovsky: 26+ saves YES** — thesis: TOR net faces heavy volume (33+ shots; BUF pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.039); KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.042); failure: TOR net faces light volume (<= 25 shots; BUF suppressed)
- **Tage Thompson: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15BUFTOR-BUFJQUINN22-1|no; why: higher confidence-adjusted growth (1.04 vs 0.77 bp); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.063); KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes: MOSTLY_INDEPENDENT (phi 0.042); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:SUPPRESSED (p 0.3639): highest fidelity KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no (same contract)
- thesis TOR:NET_HIGH_VOLUME (p 0.3635): highest fidelity KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes (same contract)
- thesis BUF:SUPPRESSED (p 0.3752): highest fidelity KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no (same contract)
- KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4055, phi -0.117)
- KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4115, phi -0.217)
- KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family MIXED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:NET_LOW_VOLUME (p 0.2268, phi -0.618)
- KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4055, phi -0.257)

portfolios: A EV +0.94 (adj +0.29) on $13.81, P(profit) 0.6952, adj growth 2.7 bp · B EV +1.00 (adj +0.36) on $17.42, P(profit) 0.5899, adj growth 3.4 bp · C EV +1.12 (adj +0.30) on $14.52, P(profit) 0.6373, adj growth 2.8 bp · R EV +0.06 (adj +0.04) on $2.00, P(profit) 0.915, adj growth 1.6 bp

## NYI @ OTT  ·  10000 joint draws  ·  450 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.593 / away 0.407

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NYI_win | p_overtime | goals | shots OTT/NYI | OTT/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.66 | 0.34 | 0.00 | 5.98 | 26.8/26.8 | 23.9/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.44 | 5.9 | 26.9/26.6 | 23.5/23.6 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.097 | 0.69 | 0.31 | 0.00 | 6.02 | 31.9/21.0 | 18.3/27.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.64 | 0.36 | 0.00 | 9.23 | 28.5/28.3 | 23.1/21.5 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.57 | 0.43 | 0.46 | 5.82 | 31.8/21.5 | 18.4/28.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.60 | 0.40 | 0.00 | 3.42 | 25.5/25.5 | 24.0/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Andre Burakovsky: 1+ assists NO | 75 | 0.828 | 0.786 | +0.065 | +0.023 | $7.53 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Warren Foegele: 1+ goals YES | 14 | 0.176 | 0.166 | +0.028 | +0.018 | $1.92 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 10 | 0.131 | 0.121 | +0.025 | +0.014 | $1.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Matias Maccelli: 1+ assists NO | 66 | 0.731 | 0.691 | +0.056 | +0.015 | $5.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (6.58 vs 1.08 bp); relationships: KXNHLGOAL-26OCT15NYIOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26OCT15NYIOTT-NYIMMACCELLI63-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense succeeds (4+ goals)
- **Warren Foegele: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-8|yes; why: higher confidence-adjusted growth (5.27 vs 0.60 bp); despite a smaller raw edge (+0.028 vs +0.030/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.894 vs 0.334); alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15NYIOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT15NYIOTT-NYIMMACCELLI63-1|no: MOSTLY_INDEPENDENT (phi -0.017); failure: OTT offense suppressed (<= 2 goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-8|yes; why: higher confidence-adjusted growth (4.74 vs 0.60 bp); despite a smaller raw edge (+0.025 vs +0.030/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.968 vs 0.334); alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15NYIOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT15NYIOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT15NYIOTT-NYIMMACCELLI63-1|no: INTENTIONAL_DIVERSIFIER (phi -0.063); failure: NYI offense suppressed (<= 2 goals)
- **Matias Maccelli: 1+ assists NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15NYIOTT-NYIKPALMIERI21-1|no; why: higher confidence-adjusted growth (2.22 vs 1.28 bp); relationships: KXNHLAST-26OCT15NYIOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT15NYIOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.063); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis NYI:SUPPRESSED (p 0.4937): highest fidelity KXNHLAST-26OCT15NYIOTT-NYIKPALMIERI21-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYIOTT-NYIMMACCELLI63-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:SUPPRESSED (p 0.349): highest fidelity KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4381): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT15NYIOTT-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4381, phi -0.188)
- KXNHLGOAL-26OCT15NYIOTT-OTTWFOEGELE37-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.349, phi -0.178)
- KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4937, phi -0.167)
- KXNHLAST-26OCT15NYIOTT-NYIMMACCELLI63-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.2978, phi -0.232)

portfolios: A EV +0.97 (adj +0.28) on $13.81, P(profit) 0.7593, adj growth 2.7 bp · B EV +1.76 (adj +0.77) on $16.06, P(profit) 0.7154, adj growth 7.3 bp · C EV +0.82 (adj +0.21) on $11.32, P(profit) 0.5378, adj growth 2.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ TBL  ·  10000 joint draws  ·  406 bet sides mapped, 30 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.705 / away 0.295

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_SEA_win | p_overtime | goals | shots TBL/SEA | TBL/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.136 | 0.68 | 0.32 | 0.00 | 6.0 | 32.8/21.2 | 18.5/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.59 | 0.41 | 0.00 | 5.98 | 27.3/26.6 | 23.4/23.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.55 | 0.45 | 0.45 | 5.82 | 33.0/21.5 | 18.4/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.51 | 0.49 | 0.47 | 5.95 | 27.4/26.8 | 23.5/24.2 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.081 | 0.71 | 0.29 | 0.00 | 9.18 | 34.4/22.6 | 18.1/26.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.60 | 0.40 | 0.00 | 9.15 | 28.6/28.0 | 22.5/22.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| John Carlson: 1+ assists NO | 51 | 0.680 | 0.566 | +0.153 | +0.039 | $4.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Jake Guentzel: 1+ goals NO | 61 | 0.671 | 0.654 | +0.044 | +0.028 | $4.07 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ goals NO | 59 | 0.640 | 0.625 | +0.034 | +0.018 | $2.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (13.22 vs 10.14 bp); relationships: KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi 0.139); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.143); failure: TBL offense succeeds (4+ goals)
- **Jake Guentzel: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no; why: Player prop expression KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.83 vs 0.71 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.139); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no; why: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.76 vs 0.98 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TBL:SUPPRESSED (p 0.3553): highest fidelity KXNHLTEAMTOTAL-26OCT15SEATB-TB4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no — Player prop expression KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.83 vs 0.71 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis SEA:WINS_BY_2PLUS (p 0.2152): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4164): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no — Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.76 vs 0.98 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.5 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4272, phi -0.243)
- KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4272, phi -0.238)
- KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4272, phi -0.26)
- override: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.76 vs 0.98 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.83 vs 0.71 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.74 (adj +0.97) on $13.81, P(profit) 0.6253, adj growth 9.1 bp · B EV +1.82 (adj +0.61) on $11.29, P(profit) 0.6215, adj growth 5.9 bp · C EV +5.95 (adj +1.84) on $24.66, P(profit) 0.6675, adj growth 17.2 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.671, adj growth 3.4 bp

## VAN @ FLA  ·  10000 joint draws  ·  388 bet sides mapped, 31 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.715 / away 0.285

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_VAN_win | p_overtime | goals | shots FLA/VAN | FLA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.118 | 0.68 | 0.32 | 0.00 | 6.02 | 32.7/21.1 | 18.4/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.61 | 0.39 | 0.00 | 6.02 | 27.2/26.7 | 23.7/23.1 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.54 | 0.46 | 0.45 | 5.96 | 32.6/21.4 | 18.2/29.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.51 | 0.49 | 0.49 | 6.0 | 27.5/26.9 | 23.5/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.59 | 0.41 | 0.00 | 9.35 | 28.9/28.4 | 22.7/22.4 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.087 | 0.67 | 0.33 | 0.00 | 9.22 | 34.4/22.5 | 17.8/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 62 | 0.701 | 0.678 | +0.064 | +0.041 | $5.65 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 62 | 0.697 | 0.676 | +0.060 | +0.040 | $5.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 63 | 0.767 | 0.675 | +0.121 | +0.028 | $4.49 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jake DeBrusk: 1+ goals YES | 27 | 0.321 | 0.307 | +0.037 | +0.023 | $2.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes; why: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes has the higher standalone adjusted growth (24.00 vs 16.29 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.143); relationships: KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26OCT15VANFLA-FLA3|no: REINFORCING (phi 0.184); KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: FLA offense succeeds (4+ goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes; why: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes has the higher standalone adjusted growth (24.00 vs 14.94 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26OCT15VANFLA-FLA3|no: REINFORCING (phi 0.172); KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes has the higher standalone adjusted growth (28.92 vs 7.76 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.248); relationships: KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: REINFORCING (phi 0.184); KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: REINFORCING (phi 0.172); KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes: REINFORCING (phi 0.16); failure: FLA wins by 2+
- **Jake DeBrusk: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes; why: Player prop expression KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes selected over broad KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2|yes because adjusted EV is 0.2 pts higher while thesis capture is 0.43 vs 0.99 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT15VANFLA-FLA3|no: REINFORCING (phi 0.16); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3482): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.224): highest fidelity KXNHLSPREAD-26OCT15VANFLA-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15VANFLA-VAN2|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.2973): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4608, phi -0.244)
- KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4608, phi -0.234)
- KXNHLSPREAD-26OCT15VANFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.2 pts; opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3547, phi -0.743)
- KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4311, phi -0.274)
- override: Player prop expression KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes selected over broad KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2|yes because adjusted EV is 0.2 pts higher while thesis capture is 0.43 vs 0.99 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.75 (adj +1.09) on $13.81, P(profit) 0.5027, adj growth 9.8 bp · B EV +2.21 (adj +1.08) on $17.80, P(profit) 0.543, adj growth 10.5 bp · C EV +5.94 (adj +3.30) on $9.64, P(profit) 0.383, adj growth 30.3 bp · R EV +0.57 (adj +0.22) on $4.00, P(profit) 0.573, adj growth 8.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT15VANFLA-VAN|yes == KXNHLGAME-26OCT15VANFLA-FLA|no

## NYR @ NJD  ·  10000 joint draws  ·  432 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.549 / away 0.451

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_NYR_win | p_overtime | goals | shots NJD/NYR | NJD/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.129 | 0.54 | 0.46 | 0.00 | 5.99 | 33.0/21.1 | 17.9/29.2 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.52 | 0.48 | 0.47 | 5.87 | 33.0/21.3 | 18.2/29.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.48 | 0.52 | 0.00 | 6.02 | 27.3/26.7 | 23.1/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.49 | 0.51 | 0.50 | 5.94 | 27.4/26.7 | 23.4/24.1 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.073 | 0.57 | 0.43 | 0.00 | 9.17 | 34.8/22.8 | 17.4/28.1 | even strength |
| NJD shot control · low event (<=4) · decided (2+) | 0.070 | 0.55 | 0.45 | 0.00 | 3.46 | 31.5/20.0 | 18.4/29.5 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Matt Rempe: 1+ goals YES | 6 | 0.090 | 0.082 | +0.026 | +0.018 | $1.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 73 | 0.777 | 0.762 | +0.033 | +0.019 | $6.40 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 62 | 0.671 | 0.657 | +0.035 | +0.021 | $4.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Amadeus Lombardi: 1+ goals YES | 10 | 0.129 | 0.119 | +0.023 | +0.013 | $1.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
- **Matt Rempe: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (10.90 vs 3.31 bp); despite a smaller raw edge (+0.026 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT15NYRNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: NYR offense suppressed (<= 2 goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no; why: Player prop expression KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.88 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15NYRNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NJD offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no; why: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no has the higher standalone adjusted growth (7.28 vs 4.05 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.024); relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15NYRNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: NJD offense succeeds (4+ goals)
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15NYRNJ-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (3.81 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis NJD:SUPPRESSED (p 0.4147): highest fidelity KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.88 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NYR:OFFENSE_4PLUS (p 0.3577): highest fidelity KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes (same contract)
- thesis NYR:SUPPRESSED (p 0.4207): highest fidelity KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4207, phi -0.14)
- KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3686, phi -0.211)
- KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3686, phi -0.24)
- KXNHLGOAL-26OCT15NYRNJ-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4147, phi -0.184)
- override: Player prop expression KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.88 vs 0.78 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.08 (adj +0.59) on $13.81, P(profit) 0.6186, adj growth 5.6 bp · B EV +1.48 (adj +0.91) on $14.17, P(profit) 0.6148, adj growth 8.7 bp · C EV +1.95 (adj +0.61) on $21.88, P(profit) 0.8155, adj growth 5.8 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.7767, adj growth 1.9 bp

## PHI @ DET  ·  10000 joint draws  ·  406 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.559 / away 0.441

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_PHI_win | p_overtime | goals | shots DET/PHI | DET/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.112 | 0.54 | 0.46 | 0.00 | 5.93 | 32.3/21.1 | 18.0/28.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.50 | 0.50 | 0.00 | 5.96 | 27.2/26.8 | 23.3/23.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.55 | 0.45 | 0.47 | 5.84 | 32.9/21.3 | 18.2/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.49 | 5.89 | 27.3/26.8 | 23.5/24.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.067 | 0.49 | 0.51 | 0.00 | 3.44 | 26.3/25.6 | 23.8/24.5 | even strength |
| DET shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.49 | 0.51 | 0.49 | 2.77 | 31.2/20.3 | 18.8/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nate Danielson: 1+ goals NO | 84 | 0.887 | 0.873 | +0.038 | +0.023 | $7.53 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Sheldon Dries: 1+ goals YES | 9 | 0.121 | 0.113 | +0.025 | +0.017 | $1.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 19 | 0.233 | 0.221 | +0.032 | +0.020 | $2.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 15 | 0.183 | 0.172 | +0.024 | +0.013 | $1.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Nate Danielson: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (9.52 vs 3.46 bp); despite a smaller raw edge (+0.038 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15PHIDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: DET offense succeeds (4+ goals)
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15PHIDET-DETEFINNIE58-1|yes; why: higher confidence-adjusted growth (7.35 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.024); failure: DET offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (5.49 vs 2.82 bp); relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15PHIDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PHI offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes has the higher standalone adjusted growth (5.49 vs 2.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT15PHIDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3214): highest fidelity KXNHLSPREAD-26OCT15PHIDET-DET3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4363): highest fidelity KXNHLSPREAD-26OCT15PHIDET-DET3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.4828): highest fidelity KXNHLSPREAD-26OCT15PHIDET-DET3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15PHIDET-DET3|no (same contract)
- KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3447, phi -0.153)
- KXNHLGOAL-26OCT15PHIDET-DETSDRIES15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4363, phi -0.176)
- KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.224)
- KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.23)

portfolios: A EV +1.02 (adj +0.47) on $13.81, P(profit) 0.6705, adj growth 4.5 bp · B EV +1.34 (adj +0.85) on $12.85, P(profit) 0.4166, adj growth 8.1 bp · C EV +1.35 (adj +0.58) on $14.88, P(profit) 0.7112, adj growth 5.4 bp · R EV +0.09 (adj +0.06) on $2.00, P(profit) 0.8871, adj growth 2.2 bp

## WPG @ CHI  ·  10000 joint draws  ·  466 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.455 / away 0.545

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_WPG_win | p_overtime | goals | shots CHI/WPG | CHI/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.51 | 0.49 | 0.00 | 6.0 | 26.4/26.6 | 23.2/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.49 | 5.91 | 26.4/26.7 | 23.4/23.1 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.097 | 0.45 | 0.55 | 0.00 | 5.96 | 21.1/31.9 | 28.0/17.9 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.50 | 0.50 | 0.49 | 5.92 | 21.2/31.8 | 28.4/18.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.49 | 0.51 | 0.00 | 9.32 | 28.0/28.2 | 22.1/21.9 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.059 | 0.43 | 0.57 | 0.00 | 9.15 | 22.4/33.5 | 26.4/17.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Roman Kantserov: 1+ goals NO | 74 | 0.792 | 0.777 | +0.039 | +0.023 | $7.45 | FUNDED_RESEARCH | $2 | CHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Ryan Greene: 1+ goals YES | 13 | 0.162 | 0.152 | +0.024 | +0.015 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 27 | 0.314 | 0.301 | +0.030 | +0.018 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ goals NO | 66 | 0.702 | 0.689 | +0.026 | +0.013 | $3.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (6.38 vs 1.93 bp); despite a smaller raw edge (+0.039 vs +0.112/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CHI offense succeeds (4+ goals)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (3.89 vs 3.31 bp); despite a smaller raw edge (+0.024 vs +0.030/contract); relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-2|yes; why: higher confidence-adjusted growth (3.31 vs 0.04 bp); wins across more scripts (relative breadth 0.948 vs 0.804); alternative not eligible: confidence-adjusted EV +0.0010 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CHI offense suppressed (<= 2 goals)
- **Connor Bedard: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no; why: Player prop expression KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no selected over player prop KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.84 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:SUPPRESSED (p 0.4051): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.3726): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes (same contract)
- KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3726, phi -0.209)
- KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4051, phi -0.178)
- KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4051, phi -0.274)
- KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3726, phi -0.251)
- override: Player prop expression KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no selected over player prop KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.84 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.51 (adj +0.43) on $13.81, P(profit) 0.6621, adj growth 4.1 bp · B EV +1.02 (adj +0.60) on $15.01, P(profit) 0.6801, adj growth 5.7 bp · C EV +0.88 (adj +0.52) on $13.78, P(profit) 0.7922, adj growth 4.9 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7922, adj growth 2.4 bp

## SJS @ NSH  ·  10000 joint draws  ·  460 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.557 / away 0.443

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_SJS_win | p_overtime | goals | shots NSH/SJS | NSH/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.53 | 0.47 | 0.00 | 6.04 | 27.9/27.9 | 24.5/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.47 | 6.01 | 27.7/27.7 | 24.5/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.55 | 0.45 | 0.00 | 9.29 | 29.3/29.2 | 23.4/22.7 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.068 | 0.58 | 0.42 | 0.00 | 5.97 | 32.2/22.0 | 18.9/28.0 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.067 | 0.50 | 0.50 | 0.00 | 6.0 | 22.3/32.8 | 29.1/18.9 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.55 | 0.45 | 0.47 | 5.86 | 32.6/22.4 | 19.4/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Collin Graf: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $2.11 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 20 | 0.244 | 0.232 | +0.033 | +0.021 | $2.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Kiefer Sherwood: 1+ goals YES | 17 | 0.202 | 0.193 | +0.022 | +0.013 | $1.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Macklin Celebrini: 1+ assists NO | 43 | 0.575 | 0.459 | +0.128 | +0.012 | $2.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.76) | CALIBRATION_WARNING | D |
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (7.26 vs 5.58 bp); despite a smaller raw edge (+0.031 vs +0.033/contract); relationships: KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT15SJNSH-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: SJS offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes has the higher standalone adjusted growth (7.26 vs 5.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT15SJNSH-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); failure: SJS offense suppressed (<= 2 goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes has the higher standalone adjusted growth (7.26 vs 2.41 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi -0.03); failure: SJS offense suppressed (<= 2 goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (1.19 vs 0.95 bp); evidence CALIBRATION_WARNING vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLGOAL-26OCT15SJNSH-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.03); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.395): highest fidelity KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3851): highest fidelity KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no (same contract)
- KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3851, phi -0.208)
- KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3851, phi -0.234)
- KXNHLGOAL-26OCT15SJNSH-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3851, phi -0.196)
- KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 24% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.5 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.395, phi -0.281)

portfolios: A EV +2.82 (adj +0.92) on $12.75, P(profit) 0.4456, adj growth 8.6 bp · B EV +1.86 (adj +0.73) on $8.93, P(profit) 0.4456, adj growth 6.9 bp · C EV +1.64 (adj +0.52) on $6.39, P(profit) 0.6632, adj growth 4.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ MIN  ·  10000 joint draws  ·  432 bet sides mapped, 5 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.563 / away 0.437

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_STL_win | p_overtime | goals | shots MIN/STL | MIN/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.58 | 0.42 | 0.00 | 6.04 | 27.7/27.4 | 23.9/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.55 | 0.45 | 0.46 | 5.99 | 27.7/27.6 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.58 | 0.42 | 0.00 | 9.3 | 29.3/29.1 | 23.3/22.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.081 | 0.66 | 0.34 | 0.00 | 6.01 | 32.7/21.9 | 19.2/28.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.53 | 0.47 | 0.48 | 5.93 | 32.7/22.1 | 18.9/29.3 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.061 | 0.62 | 0.38 | 0.00 | 9.21 | 34.7/23.4 | 18.4/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ross Johnston: 1+ goals YES | 5 | 0.075 | 0.072 | +0.022 | +0.018 | $1.69 | FUNDED_RESEARCH | $1 | STL:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 24 | 0.318 | 0.274 | +0.066 | +0.021 | $2.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Ryan Hartman: 1+ goals YES | 19 | 0.232 | 0.219 | +0.032 | +0.018 | $2.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Ross Johnston: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (13.87 vs 1.68 bp); despite a smaller raw edge (+0.022 vs +0.025/contract); relationships: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: STL offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (5.29 vs 4.60 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT15STLMIN-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (5.29 vs 4.60 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT15STLMIN-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4345): highest fidelity KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3552): highest fidelity KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes (same contract)
- KXNHLGOAL-26OCT15STLMIN-STLRJOHNSTON49-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4256, phi -0.141)
- KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3426, phi -0.24)
- KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3426, phi -0.209)

portfolios: A EV +2.84 (adj +1.12) on $13.00, P(profit) 0.5361, adj growth 10.0 bp · B EV +1.61 (adj +0.96) on $6.01, P(profit) 0.5177, adj growth 9.1 bp · C EV +1.10 (adj +0.39) on $5.44, P(profit) 0.5003, adj growth 3.6 bp · R EV +0.41 (adj +0.34) on $1.00, P(profit) 0.0754, adj growth 11.8 bp

## UTA @ EDM  ·  10000 joint draws  ·  452 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.517 / away 0.483

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_UTA_win | p_overtime | goals | shots EDM/UTA | EDM/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.63 | 0.37 | 0.00 | 6.07 | 27.5/27.5 | 24.5/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.60 | 0.40 | 0.00 | 9.46 | 29.4/29.3 | 23.8/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.45 | 6.07 | 28.1/28.0 | 24.7/24.7 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.077 | 0.67 | 0.33 | 0.00 | 6.07 | 32.8/22.1 | 19.4/28.1 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.071 | 0.69 | 0.31 | 0.00 | 9.48 | 34.3/23.4 | 18.9/26.2 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.56 | 0.44 | 0.45 | 5.94 | 32.9/22.3 | 19.2/29.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 16 | 0.217 | 0.200 | +0.047 | +0.031 | $3.32 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 9 | 0.129 | 0.119 | +0.033 | +0.024 | $2.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 32 | 0.452 | 0.363 | +0.117 | +0.028 | $4.37 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
| Filip Hallander: 1+ goals YES | 14 | 0.179 | 0.169 | +0.031 | +0.021 | $2.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (14.40 vs 4.25 bp); despite a smaller raw edge (+0.047 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26OCT15UTAEDM-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (13.71 vs 4.25 bp); despite a smaller raw edge (+0.033 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.111); KXNHLGOAL-26OCT15UTAEDM-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (7.49 vs 4.65 bp); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.111); KXNHLGOAL-26OCT15UTAEDM-EDMFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: EDM offense succeeds (4+ goals)
- **Filip Hallander: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (7.40 vs 4.25 bp); despite a smaller raw edge (+0.031 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:SUPPRESSED (p 0.2932): highest fidelity KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.4964): highest fidelity KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT15UTAEDM-EDMKKAPANEN42-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.3988): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2932, phi -0.19)
- KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2932, phi -0.154)
- KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4964, phi -0.318)
- KXNHLGOAL-26OCT15UTAEDM-EDMFHALLANDER11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2932, phi -0.163)

portfolios: A EV +3.19 (adj +0.66) on $13.81, P(profit) 0.6694, adj growth 6.3 bp · B EV +3.74 (adj +1.86) on $12.26, P(profit) 0.7141, adj growth 17.6 bp · C EV +2.69 (adj +0.70) on $9.26, P(profit) 0.6709, adj growth 6.5 bp · R EV +0.28 (adj +0.18) on $1.00, P(profit) 0.2168, adj growth 6.8 bp

## CGY @ VGK  ·  10000 joint draws  ·  412 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.726 / away 0.274

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_CGY_win | p_overtime | goals | shots VGK/CGY | VGK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.127 | 0.79 | 0.21 | 0.00 | 5.97 | 33.9/22.1 | 19.9/28.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.73 | 0.27 | 0.00 | 6.01 | 28.3/27.8 | 25.3/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.56 | 0.44 | 0.47 | 5.92 | 28.5/28.3 | 24.9/25.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.58 | 0.42 | 0.46 | 5.83 | 33.7/22.2 | 18.9/30.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.75 | 0.25 | 0.00 | 9.18 | 29.7/29.2 | 24.6/21.8 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.078 | 0.78 | 0.22 | 0.00 | 9.16 | 35.4/23.4 | 19.3/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 68 | 0.742 | 0.725 | +0.046 | +0.030 | $7.45 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Vegas wins by over 2.5 goals NO | 61 | 0.690 | 0.648 | +0.064 | +0.021 | $3.32 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Vegas over 5.5 goals scored NO | 80 | 0.855 | 0.825 | +0.044 | +0.014 | $2.61 | FUNDED_RESEARCH | $1 | CGY:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Jack Eichel: 1+ goals NO | 63 | 0.675 | 0.663 | +0.029 | +0.017 | $3.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no; why: higher confidence-adjusted growth (9.18 vs 4.11 bp); despite a smaller raw edge (+0.046 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK6|no: REINFORCING (phi 0.151); KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.028); failure: VGK offense succeeds (4+ goals)
- **Vegas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no; why: higher confidence-adjusted growth (4.11 vs 3.27 bp); wins across more scripts (relative breadth 1.025 vs 0.85); relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK6|no: REINFORCING (phi 0.455); KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.142); failure: VGK wins by 2+
- **Vegas over 5.5 goals scored NO** — thesis: CGY wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no has the higher standalone adjusted growth (4.11 vs 2.74 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.455); they share one thesis budget; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: REINFORCING (phi 0.151); KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: REINFORCING (phi 0.455); KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: REINFORCING (phi 0.159); failure: high-event game (8+ goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no; why: Player prop expression KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.84 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: MOSTLY_INDEPENDENT (phi 0.142); KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK6|no: REINFORCING (phi 0.159); failure: VGK offense succeeds (4+ goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.09.
- thesis VGK:SUPPRESSED (p 0.2919): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK3|no (same contract)
- thesis GAME:TIGHT (p 0.401): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK3|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.2574): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK3|no (same contract)
- KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5032, phi -0.194)
- KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4414, phi -0.754)
- KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2569, phi -0.552)
- KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5032, phi -0.235)
- override: Player prop expression KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.84 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26OCT15CGYVGK-VGK2|no less than the minimum stake; KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK6|no kept

portfolios: A EV +2.35 (adj +0.46) on $13.81, P(profit) 0.5678, adj growth 4.3 bp · B EV +1.15 (adj +0.57) on $17.22, P(profit) 0.6122, adj growth 5.5 bp · C EV +1.30 (adj +0.40) on $18.22, P(profit) 0.6779, adj growth 3.8 bp · R EV +0.29 (adj +0.14) on $4.00, P(profit) 0.6739, adj growth 5.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT15CGYVGK-VGK|no == KXNHLGAME-26OCT15CGYVGK-CGY|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
