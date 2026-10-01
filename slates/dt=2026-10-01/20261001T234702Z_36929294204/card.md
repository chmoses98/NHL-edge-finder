# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-01T23:47:02Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +30.00 | +7.71 | +29.13 | 0.746 | -27.00 | -41.05 | 67.29 |
| B thesis-diversified (joint) ← card | 150.00 | +23.01 | +9.53 | +21.03 | 0.719 | -24.51 | -38.70 | 87.88 |
| C best expression per thesis | 150.00 | +22.80 | +9.39 | +21.04 | 0.694 | -27.53 | -43.02 | 85.80 |

## MIN @ NSH  ·  10000 joint draws  ·  344 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.427 / away 0.573

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_MIN_win | p_overtime | goals | shots NSH/MIN | NSH/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.44 | 0.56 | 0.00 | 6.03 | 29.3/29.5 | 25.6/25.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.50 | 0.50 | 0.46 | 5.98 | 29.5/29.6 | 26.2/26.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.44 | 0.56 | 0.00 | 9.36 | 30.9/31.0 | 24.3/25.0 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.071 | 0.38 | 0.62 | 0.00 | 6.04 | 23.3/34.4 | 30.1/20.2 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.44 | 0.56 | 0.50 | 5.91 | 23.8/34.6 | 31.2/20.6 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.49 | 0.51 | 0.43 | 5.94 | 34.1/23.5 | 20.2/30.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Ryan Hartman: 1+ goals YES | 23 | 0.274 | 0.262 | +0.032 | +0.020 | $4.30 | MIN:OFFENSE_4PLUS | 0.2629 | EVIDENCE_STRONGER | D |
| Jared Spurgeon: 1+ goals NO | 91 | 0.935 | 0.927 | +0.019 | +0.012 | $13.84 | MIN:SUPPRESSED | 0.2414 | EVIDENCE_STRONGER | D |
| Mavrik Bourque: 1+ goals YES | 18 | 0.212 | 0.203 | +0.022 | +0.013 | $2.58 | NSH:OFFENSE_4PLUS | 0.2634 | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 26 | 0.299 | 0.288 | +0.025 | +0.014 | $3.29 | NSH:OFFENSE_4PLUS | 0.2649 | EVIDENCE_STRONGER | D |
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT01MINNSH-9|yes; why: higher confidence-adjusted growth (4.54 vs 0.51 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.896 vs 0.369); alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: MIN offense suppressed (<= 2 goals)
- **Jared Spurgeon: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01MINNSH-MINKKAPRIZOV97-1|no; why: higher confidence-adjusted growth (3.99 vs 0.03 bp); alternative not eligible: confidence-adjusted EV +0.0018 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: MIN offense succeeds (4+ goals)
- **Mavrik Bourque: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes; why: higher confidence-adjusted growth (2.23 vs 2.22 bp); despite a smaller raw edge (+0.022 vs +0.025/contract); relationships: KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: NSH offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes has the higher standalone adjusted growth (2.23 vs 2.22 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: NSH offense suppressed (<= 2 goals)

portfolios: A EV +2.06 (adj +1.22) on $28.01, P(profit) 0.5723, adj growth 10.7 bp · B EV +1.46 (adj +0.87) on $24.02, P(profit) 0.5723, adj growth 8.0 bp · C EV +1.00 (adj +0.60) on $7.98, P(profit) 0.4286, adj growth 5.4 bp

## SEA @ CGY  ·  10000 joint draws  ·  398 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.502 / away 0.498

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_SEA_win | p_overtime | goals | shots CGY/SEA | CGY/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.51 | 0.49 | 0.00 | 5.97 | 28.3/28.2 | 24.8/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.49 | 0.51 | 0.45 | 5.9 | 28.3/28.3 | 25.1/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.50 | 0.50 | 0.00 | 9.2 | 29.8/29.5 | 23.3/23.5 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.082 | 0.58 | 0.42 | 0.00 | 6.01 | 33.5/22.5 | 19.5/29.2 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.56 | 0.44 | 0.49 | 5.89 | 33.6/23.0 | 19.9/30.1 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.059 | 0.42 | 0.58 | 0.00 | 5.89 | 22.7/33.1 | 29.2/19.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Brandon Montour: 1+ goals NO | 83 | 0.892 | 0.875 | +0.052 | +0.036 | $10.46 | SEA:SUPPRESSED | 0.2497 | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 10 | 0.136 | 0.126 | +0.030 | +0.019 | $3.66 | SEA:OFFENSE_4PLUS | 0.2605 | EVIDENCE_STRONGER | D |
| Jared McCann: 1+ assists NO | 64 | 0.731 | 0.683 | +0.074 | +0.027 | $10.30 | SEA:SUPPRESSED | 0.2523 | EVIDENCE_MIXED | D |
| Adam Klapka: 1+ goals YES | 10 | 0.131 | 0.122 | +0.025 | +0.015 | $2.86 | CGY:OFFENSE_4PLUS | 0.2332 | EVIDENCE_STRONGER | D |
- **Brandon Montour: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (21.16 vs 6.93 bp); despite a smaller raw edge (+0.053 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: SEA offense succeeds (4+ goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01SEACGY-SEAMBENIERS10-1|yes; why: higher confidence-adjusted growth (8.48 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no: INTENTIONAL_DIVERSIFIER (phi -0.066); KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi -0.023); failure: SEA offense suppressed (<= 2 goals)
- **Jared McCann: 1+ assists NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (6.93 vs 1.62 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.083); KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.066); KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: SEA offense succeeds (4+ goals)
- **Adam Klapka: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01SEACGY-CGYMFROST16-1|yes; why: higher confidence-adjusted growth (5.48 vs 2.08 bp); relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: CGY offense suppressed (<= 2 goals)

portfolios: A EV +4.10 (adj +2.31) on $30.50, P(profit) 0.2516, adj growth 21.0 bp · B EV +3.50 (adj +1.95) on $27.28, P(profit) 0.7514, adj growth 18.1 bp · C EV +3.31 (adj +1.60) on $23.61, P(profit) 0.7772, adj growth 14.4 bp

## CHI @ UTA  ·  10000 joint draws  ·  320 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.657 / away 0.343

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_CHI_win | p_overtime | goals | shots UTA/CHI | UTA/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| UTA shot control · normal event (5-7) · decided (2+) | 0.128 | 0.77 | 0.23 | 0.00 | 6.01 | 33.0/21.4 | 19.0/27.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.69 | 0.31 | 0.00 | 6.06 | 27.3/26.8 | 24.0/22.8 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.57 | 0.43 | 0.46 | 5.94 | 32.9/21.5 | 18.4/29.6 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.097 | 0.75 | 0.25 | 0.00 | 9.3 | 34.5/22.5 | 18.3/26.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.69 | 0.31 | 0.00 | 9.32 | 29.1/28.4 | 23.5/21.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.55 | 0.46 | 0.44 | 5.95 | 27.7/27.0 | 23.8/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Ryan Greene: 1+ goals YES | 12 | 0.166 | 0.153 | +0.039 | +0.026 | $4.92 | CHI:OFFENSE_4PLUS | 0.2446 | EVIDENCE_STRONGER | D |
| MacKenzie Weegar: 1+ goals NO | 89 | 0.925 | 0.915 | +0.029 | +0.018 | $13.84 | DIFFUSE | 0.2474 | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 62 | 0.745 | 0.657 | +0.109 | +0.021 | $12.11 | CHI:SUPPRESSED | 0.2609 | EVIDENCE_MIXED | D |
| Lawson Crouse: 1+ goals YES | 22 | 0.259 | 0.247 | +0.027 | +0.015 | $3.40 | UTA:OFFENSE_4PLUS | 0.258 | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01CHIUTA-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (13.19 vs 2.36 bp); despite a smaller raw edge (+0.039 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01CHIUTA-UTAMWEEGAR52-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: CHI offense suppressed (<= 2 goals)
- **MacKenzie Weegar: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: UTA offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01CHIUTA-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (4.14 vs 1.13 bp); relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT01CHIUTA-UTAMWEEGAR52-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: CHI offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes; why: higher confidence-adjusted growth (2.73 vs 1.44 bp); relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT01CHIUTA-UTAMWEEGAR52-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: UTA offense suppressed (<= 2 goals)

portfolios: A EV +5.86 (adj +1.02) on $30.50, P(profit) 0.6436, adj growth 8.8 bp · B EV +4.42 (adj +1.91) on $34.27, P(profit) 0.7468, adj growth 17.5 bp · C EV +4.87 (adj +2.08) on $38.57, P(profit) 0.7468, adj growth 18.8 bp

## EDM @ VAN  ·  10000 joint draws  ·  328 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.348 / away 0.652

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_EDM_win | p_overtime | goals | shots VAN/EDM | VAN/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.43 | 0.57 | 0.00 | 6.04 | 27.7/28.3 | 24.4/24.4 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.113 | 0.35 | 0.65 | 0.00 | 6.02 | 22.1/33.9 | 29.7/19.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.48 | 0.52 | 0.47 | 5.98 | 27.9/28.7 | 25.3/24.7 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.45 | 0.55 | 0.46 | 5.91 | 22.5/34.3 | 30.9/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.43 | 0.57 | 0.00 | 9.47 | 29.4/30.1 | 23.5/23.4 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.086 | 0.34 | 0.66 | 0.00 | 9.36 | 23.4/35.5 | 27.8/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Connor McDavid: 1+ assists NO | 31 | 0.476 | 0.365 | +0.151 | +0.040 | $6.82 | EDM:SUPPRESSED | 0.2285 | EVIDENCE_MIXED | D |
| Drew O'Connor: 1+ goals YES | 16 | 0.215 | 0.200 | +0.046 | +0.031 | $6.03 | VAN:OFFENSE_4PLUS | 0.2401 | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 67 | 0.831 | 0.717 | +0.146 | +0.031 | $13.84 | EDM:SUPPRESSED | 0.2301 | EVIDENCE_MIXED | D |
| Marco Rossi: 1+ goals YES | 21 | 0.257 | 0.244 | +0.035 | +0.022 | $4.75 | VAN:OFFENSE_4PLUS | 0.2486 | EVIDENCE_STRONGER | D |
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (15.80 vs 9.94 bp); relationships: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: DUPLICATIVE (phi 0.43); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: EDM offense succeeds (4+ goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01EDMVAN-EDM3|no; why: higher confidence-adjusted growth (14.52 vs 8.48 bp); despite a smaller raw edge (+0.046 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: VAN offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no; why: second expression of the same thesis: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no has the higher standalone adjusted growth (15.80 vs 9.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.430); they share one thesis budget; relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: DUPLICATIVE (phi 0.43); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT01EDMVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: EDM offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (14.52 vs 6.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.011); failure: VAN offense suppressed (<= 2 goals)

portfolios: A EV +9.33 (adj +1.63) on $30.50, P(profit) 0.7061, adj growth 14.1 bp · B EV +8.51 (adj +3.04) on $31.44, P(profit) 0.6604, adj growth 27.8 bp · C EV +7.19 (adj +2.68) on $39.92, P(profit) 0.5862, adj growth 24.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01EDMVAN-VAN|yes == KXNHLGAME-26OCT01EDMVAN-EDM|no

## FLA @ SJS  ·  10000 joint draws  ·  368 bet sides mapped, 24 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.427 / away 0.573

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_FLA_win | p_overtime | goals | shots SJS/FLA | SJS/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.57 | 0.43 | 0.00 | 6.0 | 26.8/26.9 | 23.7/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.46 | 5.91 | 27.0/27.1 | 23.8/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.58 | 0.42 | 0.00 | 9.35 | 28.5/28.5 | 22.9/21.7 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.072 | 0.52 | 0.48 | 0.00 | 5.99 | 21.3/31.6 | 27.8/17.8 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.49 | 0.51 | 0.48 | 5.99 | 21.5/32.0 | 28.4/18.3 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.062 | 0.65 | 0.35 | 0.00 | 6.02 | 31.1/21.3 | 18.6/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Aleksander Barkov: 1+ assists NO | 51 | 0.692 | 0.567 | +0.164 | +0.040 | $9.79 | FLA:SUPPRESSED | 0.2467 | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 76 | 0.852 | 0.803 | +0.079 | +0.031 | $12.23 | SJS:WINS | 0.2411 | EVIDENCE_MIXED | D |
| Sam Reinhart: 1+ goals NO | 67 | 0.737 | 0.719 | +0.051 | +0.033 | $10.97 | FLA:SUPPRESSED | 0.2497 | EVIDENCE_STRONGER | D |
- **Aleksander Barkov: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: higher confidence-adjusted growth (13.76 vs 11.90 bp); relationships: KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.153); KXNHLGOAL-26OCT01FLASJ-FLASREINHART13-1|no: REINFORCING (phi 0.242); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: higher confidence-adjusted growth (11.90 vs 8.24 bp); wins across more scripts (relative breadth 1.017 vs 0.525); relationships: KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: REINFORCING (phi 0.153); KXNHLGOAL-26OCT01FLASJ-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.138); failure: FLA wins by 2+
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no; why: second expression of the same thesis: KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no has the higher standalone adjusted growth (13.76 vs 11.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.242); they share one thesis budget; relationships: KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: REINFORCING (phi 0.242); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.138); failure: FLA offense succeeds (4+ goals)

portfolios: A EV +8.66 (adj +1.53) on $30.50, P(profit) 0.6212, adj growth 12.7 bp · B EV +5.12 (adj +1.76) on $32.99, P(profit) 0.6672, adj growth 16.5 bp · C EV +6.42 (adj +2.43) on $39.92, P(profit) 0.6716, adj growth 22.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01FLASJ-FLA|no == KXNHLGAME-26OCT01FLASJ-SJ|yes

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
