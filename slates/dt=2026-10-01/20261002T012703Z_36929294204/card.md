# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-02T01:27:03Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +35.19 | +6.00 | +35.54 | 0.743 | -40.13 | -62.96 | 44.45 |
| B thesis-diversified (joint) ← card | 137.56 | +25.38 | +11.04 | +19.47 | 0.645 | -35.91 | -55.68 | 96.62 |
| C best expression per thesis | 129.77 | +20.86 | +9.03 | +17.49 | 0.649 | -35.40 | -47.39 | 80.39 |

## CHI @ UTA  ·  10000 joint draws  ·  320 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.658 / away 0.342

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_CHI_win | p_overtime | goals | shots UTA/CHI | UTA/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| UTA shot control · normal event (5-7) · decided (2+) | 0.129 | 0.79 | 0.21 | 0.00 | 6.05 | 33.0/21.1 | 19.0/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.73 | 0.27 | 0.00 | 6.02 | 27.5/26.9 | 24.4/23.0 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.107 | 0.80 | 0.20 | 0.00 | 9.36 | 34.5/22.6 | 18.6/25.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.71 | 0.29 | 0.00 | 9.44 | 29.1/28.6 | 23.7/21.7 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.57 | 0.43 | 0.45 | 5.95 | 32.7/21.4 | 18.3/29.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.53 | 0.47 | 0.49 | 6.0 | 27.5/27.0 | 23.6/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Ryan Greene: 1+ goals YES | 12 | 0.167 | 0.154 | +0.040 | +0.027 | $7.01 | CHI:OFFENSE_4PLUS | 0.2478 | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 22 | 0.265 | 0.251 | +0.033 | +0.019 | $6.56 | UTA:OFFENSE_4PLUS | 0.2894 | EVIDENCE_STRONGER | D |
| Vincent Trocheck: 1+ assists NO | 66 | 0.774 | 0.694 | +0.099 | +0.018 | $18.55 | UTA:SUPPRESSED | 0.2402 | EVIDENCE_MIXED | D |
| Anders Lee: 1+ goals YES | 24 | 0.278 | 0.267 | +0.025 | +0.014 | $5.44 | UTA:OFFENSE_4PLUS | 0.2958 | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT01CHIUTA-9|yes; why: higher confidence-adjusted growth (13.72 vs 2.07 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.959 vs 0.369); relationships: KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: CHI offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes; why: higher confidence-adjusted growth (4.51 vs 2.39 bp); relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.056); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: UTA offense suppressed (<= 2 goals)
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT01CHIUTA-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (3.19 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.056); KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.105); failure: UTA offense succeeds (4+ goals)
- **Anders Lee: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes has the higher standalone adjusted growth (4.51 vs 2.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.105); failure: UTA offense suppressed (<= 2 goals)

portfolios: A EV +6.62 (adj +1.31) on $50.00, P(profit) 0.6595, adj growth 11.2 bp · B EV +6.37 (adj +2.81) on $37.56, P(profit) 0.4731, adj growth 24.4 bp · C EV +5.85 (adj +2.45) on $29.77, P(profit) 0.4226, adj growth 21.2 bp

## EDM @ VAN  ·  10000 joint draws  ·  328 bet sides mapped, 29 +EV candidates, 4 on card

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
| Connor McDavid: 1+ assists NO | 31 | 0.476 | 0.365 | +0.151 | +0.040 | $8.55 | EDM:SUPPRESSED | 0.2285 | EVIDENCE_MIXED | D |
| Drew O'Connor: 1+ goals YES | 16 | 0.215 | 0.200 | +0.046 | +0.031 | $8.07 | VAN:OFFENSE_4PLUS | 0.2401 | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 67 | 0.831 | 0.717 | +0.146 | +0.031 | $19.64 | EDM:SUPPRESSED | 0.2301 | EVIDENCE_MIXED | D |
| Edmonton wins by over 2.5 goals NO | 68 | 0.773 | 0.724 | +0.077 | +0.029 | $13.74 | VAN:WINS | 0.2534 | EVIDENCE_MIXED | D |
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (15.80 vs 9.94 bp); relationships: KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: DUPLICATIVE (phi 0.43); KXNHLSPREAD-26OCT01EDMVAN-EDM3|no: REINFORCING (phi 0.191); failure: EDM offense succeeds (4+ goals)
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01EDMVAN-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (14.52 vs 8.62 bp); relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLSPREAD-26OCT01EDMVAN-EDM3|no: MOSTLY_INDEPENDENT (phi 0.12); failure: VAN offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no; why: second expression of the same thesis: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no has the higher standalone adjusted growth (15.80 vs 9.94 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.430); they share one thesis budget; relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: DUPLICATIVE (phi 0.43); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLSPREAD-26OCT01EDMVAN-EDM3|no: REINFORCING (phi 0.217); failure: EDM offense succeeds (4+ goals)
- **Edmonton wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no; why: second expression of the same thesis: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no has the higher standalone adjusted growth (15.80 vs 8.48 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.191); they share one thesis budget; relationships: KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no: REINFORCING (phi 0.191); KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.12); KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no: REINFORCING (phi 0.217); failure: EDM wins by 2+

portfolios: A EV +15.18 (adj +2.69) on $50.00, P(profit) 0.6178, adj growth 20.0 bp · B EV +11.87 (adj +3.98) on $50.00, P(profit) 0.5793, adj growth 34.9 bp · C EV +9.19 (adj +3.49) on $50.00, P(profit) 0.5862, adj growth 31.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01EDMVAN-VAN|yes == KXNHLGAME-26OCT01EDMVAN-EDM|no

## FLA @ SJS  ·  10000 joint draws  ·  368 bet sides mapped, 27 +EV candidates, 3 on card

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
| Kiefer Sherwood: 1+ goals YES | 15 | 0.215 | 0.198 | +0.057 | +0.039 | $10.14 | SJS:OFFENSE_4PLUS | 0.2595 | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 76 | 0.852 | 0.803 | +0.079 | +0.031 | $19.93 | SJS:WINS | 0.2411 | EVIDENCE_MIXED | D |
| Sam Reinhart: 1+ goals NO | 67 | 0.737 | 0.719 | +0.051 | +0.033 | $19.93 | FLA:SUPPRESSED | 0.2497 | EVIDENCE_STRONGER | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT01FLASJ-SJCGRAF51-1|yes; why: higher confidence-adjusted growth (24.17 vs 17.50 bp); relationships: KXNHLSPREAD-26OCT01FLASJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.112); KXNHLGOAL-26OCT01FLASJ-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: SJS offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT01FLASJ-SJ2|yes; why: higher confidence-adjusted growth (11.90 vs 8.24 bp); wins across more scripts (relative breadth 1.017 vs 0.525); relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.112); KXNHLGOAL-26OCT01FLASJ-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.138); failure: FLA wins by 2+
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT01FLASJ-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT01FLASJ-FLA3|no has the higher standalone adjusted growth (11.90 vs 11.43 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.138); they share one thesis budget; relationships: KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26OCT01FLASJ-FLA3|no: MOSTLY_INDEPENDENT (phi 0.138); failure: FLA offense succeeds (4+ goals)

portfolios: A EV +13.39 (adj +2.00) on $50.00, P(profit) 0.6212, adj growth 13.2 bp · B EV +7.14 (adj +4.25) on $50.00, P(profit) 0.7154, adj growth 37.4 bp · C EV +5.82 (adj +3.09) on $50.00, P(profit) 0.5969, adj growth 27.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT01FLASJ-SJ|yes == KXNHLGAME-26OCT01FLASJ-FLA|no

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
