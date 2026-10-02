# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-02T00:37:04Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +28.56 | +6.54 | +28.22 | 0.743 | -27.03 | -42.88 | 56.34 |
| B thesis-diversified (joint) ← card | 150.00 | +26.59 | +10.84 | +26.25 | 0.722 | -31.03 | -43.86 | 98.36 |
| C best expression per thesis | 150.00 | +23.35 | +10.61 | +18.27 | 0.635 | -38.92 | -52.03 | 93.56 |

## SEA @ CGY  ·  10000 joint draws  ·  398 bet sides mapped, 8 +EV candidates, 4 on card

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
| Brandon Montour: 1+ goals NO | 83 | 0.892 | 0.875 | +0.052 | +0.036 | $15.33 | SEA:SUPPRESSED | 0.2497 | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 10 | 0.136 | 0.126 | +0.030 | +0.019 | $3.90 | SEA:OFFENSE_4PLUS | 0.2605 | EVIDENCE_STRONGER | D |
| Adam Klapka: 1+ goals YES | 10 | 0.131 | 0.122 | +0.025 | +0.015 | $3.17 | CGY:OFFENSE_4PLUS | 0.2332 | EVIDENCE_STRONGER | D |
| Maxim Tsyplakov: 1+ goals NO | 86 | 0.895 | 0.885 | +0.027 | +0.017 | $15.33 | CGY:SUPPRESSED | 0.2492 | EVIDENCE_STRONGER | D |
- **Brandon Montour: 1+ goals NO** — thesis: SEA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01SEACGY-SEAJMCCANN19-1|no; why: higher confidence-adjusted growth (21.16 vs 3.70 bp); despite a smaller raw edge (+0.053 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT01SEACGY-CGYMTSYPLAKOV72-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: SEA offense succeeds (4+ goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01SEACGY-SEAMBENIERS10-1|yes; why: higher confidence-adjusted growth (8.48 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT01SEACGY-CGYMTSYPLAKOV72-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: SEA offense suppressed (<= 2 goals)
- **Adam Klapka: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01SEACGY-CGYMFROST16-1|yes; why: higher confidence-adjusted growth (5.48 vs 2.08 bp); relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT01SEACGY-CGYMTSYPLAKOV72-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: CGY offense suppressed (<= 2 goals)
- **Maxim Tsyplakov: 1+ goals NO** — thesis: CGY offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01SEACGY-CGYSNEMEC71-1|no; why: higher confidence-adjusted growth (5.42 vs 0.06 bp); despite a smaller raw edge (+0.027 vs +0.034/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0024 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: CGY offense succeeds (4+ goals)

portfolios: A EV +3.36 (adj +1.83) on $37.50, P(profit) 0.6553, adj growth 16.8 bp · B EV +3.25 (adj +2.12) on $37.73, P(profit) 0.2494, adj growth 19.6 bp · C EV +3.30 (adj +1.58) on $24.86, P(profit) 0.3187, adj growth 13.8 bp

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
| Ryan Greene: 1+ goals YES | 12 | 0.166 | 0.153 | +0.039 | +0.026 | $5.43 | CHI:OFFENSE_4PLUS | 0.2446 | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 21 | 0.259 | 0.246 | +0.038 | +0.024 | $6.09 | UTA:OFFENSE_4PLUS | 0.258 | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 66 | 0.776 | 0.694 | +0.100 | +0.018 | $13.66 | UTA:SUPPRESSED | 0.2441 | EVIDENCE_MIXED | D |
| Patrick Kane: 1+ assists NO | 62 | 0.745 | 0.654 | +0.109 | +0.018 | $11.44 | CHI:SUPPRESSED | 0.2609 | EVIDENCE_MIXED | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT01CHIUTA-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (13.19 vs 1.39 bp); despite a smaller raw edge (+0.039 vs +0.048/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.037); failure: CHI offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes; why: higher confidence-adjusted growth (7.31 vs 1.44 bp); relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.062); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: UTA offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT01CHIUTA-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (3.36 vs 0.12 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0035 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.062); KXNHLAST-26OCT01CHIUTA-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: UTA offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01CHIUTA-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (2.95 vs 1.13 bp); relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: CHI offense succeeds (4+ goals)

portfolios: A EV +5.10 (adj +0.99) on $37.50, P(profit) 0.658, adj growth 8.6 bp · B EV +6.68 (adj +2.46) on $36.61, P(profit) 0.7374, adj growth 22.1 bp · C EV +5.35 (adj +2.31) on $43.24, P(profit) 0.3315, adj growth 20.5 bp

## EDM @ VAN  ·  10000 joint draws  ·  328 bet sides mapped, 23 +EV candidates, 4 on card

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
| Connor McDavid: 1+ assists NO | 31 | 0.476 | 0.365 | +0.151 | +0.040 | $6.55 | EDM:SUPPRESSED | 0.2285 | EVIDENCE_MIXED | D |
| Drew O'Connor: 1+ goals YES | 16 | 0.215 | 0.200 | +0.046 | +0.031 | $6.19 | VAN:OFFENSE_4PLUS | 0.2401 | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 67 | 0.831 | 0.717 | +0.146 | +0.031 | $15.05 | EDM:SUPPRESSED | 0.2301 | EVIDENCE_MIXED | D |
| Edmonton wins by over 2.5 goals NO | 68 | 0.773 | 0.724 | +0.077 | +0.029 | $10.54 | VAN:WINS | 0.2534 | EVIDENCE_MIXED | D |
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (15.80 vs 9.94 bp); relationships: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: DUPLICATIVE (phi 0.43); KXNHLSPREAD-26OCT01EDMVAN-EDM3|no: REINFORCING (phi 0.191); failure: EDM offense succeeds (4+ goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01EDMVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (14.52 vs 8.62 bp); relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLSPREAD-26OCT01EDMVAN-EDM3|no: MOSTLY_INDEPENDENT (phi 0.12); failure: VAN offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no; why: second expression of the same thesis: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no has the higher standalone adjusted growth (15.80 vs 9.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.430); they share one thesis budget; relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: DUPLICATIVE (phi 0.43); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLSPREAD-26OCT01EDMVAN-EDM3|no: REINFORCING (phi 0.217); failure: EDM offense succeeds (4+ goals)
- **Edmonton wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no; why: second expression of the same thesis: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no has the higher standalone adjusted growth (15.80 vs 8.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.191); they share one thesis budget; relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: REINFORCING (phi 0.191); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.12); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: REINFORCING (phi 0.217); failure: EDM wins by 2+

portfolios: A EV +10.50 (adj +2.09) on $37.50, P(profit) 0.6568, adj growth 17.8 bp · B EV +9.10 (adj +3.05) on $38.33, P(profit) 0.5793, adj growth 27.6 bp · C EV +9.04 (adj +3.42) on $34.71, P(profit) 0.529, adj growth 30.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01EDMVAN-VAN|yes == KXNHLGAME-26OCT01EDMVAN-EDM|no

## FLA @ SJS  ·  10000 joint draws  ·  368 bet sides mapped, 23 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.426 / away 0.574

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
| Kiefer Sherwood: 1+ goals YES | 15 | 0.215 | 0.198 | +0.057 | +0.039 | $7.83 | SJS:OFFENSE_4PLUS | 0.2595 | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 76 | 0.852 | 0.803 | +0.079 | +0.031 | $15.33 | SJS:WINS | 0.2411 | EVIDENCE_MIXED | D |
| Aleksander Barkov: 1+ assists NO | 53 | 0.692 | 0.577 | +0.144 | +0.029 | $11.88 | FLA:SUPPRESSED | 0.2467 | EVIDENCE_MIXED | D |
| Brady Tkachuk: 1+ goals NO | 67 | 0.711 | 0.700 | +0.025 | +0.014 | $2.29 | FLA:SUPPRESSED | 0.245 | EVIDENCE_STRONGER | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: higher confidence-adjusted growth (24.17 vs 11.90 bp); despite a smaller raw edge (+0.057 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT01FLASJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.112); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT01FLASJ-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: SJS offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: higher confidence-adjusted growth (11.90 vs 8.24 bp); wins across more scripts (relative breadth 1.017 vs 0.525); relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.112); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: REINFORCING (phi 0.153); KXNHLGOAL-26OCT01FLASJ-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.133); failure: FLA wins by 2+
- **Aleksander Barkov: 1+ assists NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-FLA3|no has the higher standalone adjusted growth (11.90 vs 7.63 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.153); they share one thesis budget; relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: REINFORCING (phi 0.153); KXNHLGOAL-26OCT01FLASJ-FLABTKACHUK8-1|no: REINFORCING (phi 0.327); failure: FLA offense succeeds (4+ goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-FLA3|no has the higher standalone adjusted growth (11.90 vs 2.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.133); they share one thesis budget; relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.133); KXNHLAST-26OCT01FLASJ-FLAABARKOV16-1|no: REINFORCING (phi 0.327); failure: FLA offense succeeds (4+ goals)

portfolios: A EV +9.60 (adj +1.63) on $37.50, P(profit) 0.6105, adj growth 13.1 bp · B EV +7.57 (adj +3.21) on $37.33, P(profit) 0.6905, adj growth 29.0 bp · C EV +5.66 (adj +3.30) on $47.19, P(profit) 0.2154, adj growth 29.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01FLASJ-SJ|yes == KXNHLGAME-26OCT01FLASJ-FLA|no

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
