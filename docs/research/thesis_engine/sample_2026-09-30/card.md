# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-09-30T23:20:00Z · nhl-thesis-1.0 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.24 | +8.07 | +25.02 | 0.717 | -31.11 | -46.19 | 70.18 |
| B thesis-diversified (joint) ← card | 142.48 | +23.93 | +11.75 | +19.29 | 0.669 | -41.99 | -58.75 | 103.61 |
| C best expression per thesis | 105.61 | +18.09 | +7.88 | +16.51 | 0.637 | -35.05 | -49.47 | 69.32 |

## PIT @ PHI  ·  10000 joint draws  ·  354 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.569 / away 0.431

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_PIT_win | p_overtime | goals | shots PHI/PIT | PHI/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.58 | 0.42 | 0.00 | 5.99 | 26.1/26.3 | 23.2/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.44 | 5.93 | 26.2/26.4 | 23.2/22.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.60 | 0.40 | 0.00 | 9.2 | 27.9/28.0 | 22.6/21.4 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.074 | 0.53 | 0.47 | 0.00 | 6.01 | 21.0/31.4 | 27.8/17.5 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.45 | 0.55 | 0.48 | 5.93 | 21.2/31.5 | 28.1/18.1 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.064 | 0.64 | 0.36 | 0.00 | 6.05 | 31.1/21.1 | 18.4/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Porter Martone: 1+ goals NO | 70 | 0.776 | 0.755 | +0.061 | +0.041 | $20.00 | PHI:SUPPRESSED | 0.2448 | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 11 | 0.157 | 0.144 | +0.040 | +0.027 | $7.06 | PIT:OFFENSE_4PLUS | 0.2565 | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 13 | 0.179 | 0.166 | +0.042 | +0.028 | $7.67 | PHI:OFFENSE_4PLUS | 0.2553 | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 27 | 0.327 | 0.311 | +0.043 | +0.028 | $9.51 | PIT:OFFENSE_4PLUS | 0.2388 | EVIDENCE_STRONGER | D |
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26SEP30PITPHI-PHIMMICHKOV39-1|no; why: higher confidence-adjusted growth (18.07 vs 0.14 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0037 below the 0.010/contract floor; relationships: KXNHLGOAL-26SEP30PITPHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26SEP30PITPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26SEP30PITPHI-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: PHI offense succeeds (4+ goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26SEP30PITPHI-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (15.34 vs 8.20 bp); despite a smaller raw edge (+0.040 vs +0.043/contract); relationships: KXNHLGOAL-26SEP30PITPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26SEP30PITPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26SEP30PITPHI-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: PIT offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLAST-26SEP30PITPHI-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (14.02 vs 0.08 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0028 below the 0.010/contract floor; relationships: KXNHLGOAL-26SEP30PITPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26SEP30PITPHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26SEP30PITPHI-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: PHI offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26SEP30PITPHI-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26SEP30PITPHI-PITCDEWAR19-1|yes has the higher standalone adjusted growth (15.34 vs 8.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26SEP30PITPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26SEP30PITPHI-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26SEP30PITPHI-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: PIT offense suppressed (<= 2 goals)

portfolios: A EV +7.43 (adj +4.20) on $50.00, P(profit) 0.4122, adj growth 36.7 bp · B EV +7.89 (adj +5.27) on $44.24, P(profit) 0.4832, adj growth 46.2 bp · C EV +5.91 (adj +3.50) on $24.55, P(profit) 0.3119, adj growth 30.1 bp

## NYI @ TOR  ·  10000 joint draws  ·  348 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (4 books): home 0.557 / away 0.443

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYI_win | p_overtime | goals | shots TOR/NYI | TOR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NYI shot control · normal event (5-7) · decided (2+) | 0.119 | 0.43 | 0.57 | 0.00 | 5.96 | 22.2/34.0 | 30.0/19.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.48 | 0.52 | 0.00 | 6.0 | 28.0/28.7 | 25.1/24.6 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.45 | 5.89 | 22.6/34.5 | 31.0/19.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.53 | 0.47 | 0.47 | 5.86 | 28.3/28.9 | 25.7/25.0 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.069 | 0.43 | 0.57 | 0.00 | 9.18 | 24.0/36.2 | 29.2/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.065 | 0.49 | 0.51 | 0.00 | 9.13 | 29.4/30.2 | 24.1/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Teddy Blueger: 1+ goals YES | 9 | 0.130 | 0.119 | +0.035 | +0.023 | $6.27 | TOR:OFFENSE_4PLUS | 0.2619 | EVIDENCE_STRONGER | D |
| Auston Matthews: 1+ assists NO | 60 | 0.694 | 0.645 | +0.077 | +0.028 | $17.26 | TOR:SUPPRESSED | 0.2333 | EVIDENCE_MIXED | D |
| Toronto wins NO | 44 | 0.520 | 0.481 | +0.062 | +0.024 | $12.48 | NYI:WINS | 0.2411 | EVIDENCE_MIXED | B |
| Ilya Sorokin: 25+ saves NO | 49 | 0.626 | 0.528 | +0.119 | +0.021 | $12.23 | NYI:NET_LOW_VOLUME | 0.3208 | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26SEP30NYITOR-TORJTAVARES91-1|yes; why: higher confidence-adjusted growth (13.23 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26SEP30NYITOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGAME-26SEP30NYITOR-TOR|no: INTENTIONAL_DIVERSIFIER (phi -0.135); KXNHLSAVE-26SEP30NYITOR-NYIISOROKIN30-25|no: MOSTLY_INDEPENDENT (phi 0.038); failure: TOR offense suppressed (<= 2 goals)
- **Auston Matthews: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGAME-26SEP30NYITOR-NYI|yes; why: higher confidence-adjusted growth (7.20 vs 5.19 bp); relationships: KXNHLGOAL-26SEP30NYITOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGAME-26SEP30NYITOR-TOR|no: REINFORCING (phi 0.172); KXNHLSAVE-26SEP30NYITOR-NYIISOROKIN30-25|no: MOSTLY_INDEPENDENT (phi -0.03); failure: TOR offense succeeds (4+ goals)
- **Toronto wins NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLGAME-26SEP30NYITOR-NYI|yes; why: best adjusted growth among the thesis's expressions; relationships: KXNHLGOAL-26SEP30NYITOR-TORTBLUEGER73-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.135); KXNHLAST-26SEP30NYITOR-TORAMATTHEWS34-1|no: REINFORCING (phi 0.172); KXNHLSAVE-26SEP30NYITOR-NYIISOROKIN30-25|no: INTENTIONAL_DIVERSIFIER (phi -0.125); failure: TOR wins (incl. OT/SO)
- **Ilya Sorokin: 25+ saves NO** — thesis: NYI net faces light volume (<= 25 shots; TOR suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26SEP30NYITOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.038); KXNHLAST-26SEP30NYITOR-TORAMATTHEWS34-1|no: MOSTLY_INDEPENDENT (phi -0.03); KXNHLGAME-26SEP30NYITOR-TOR|no: INTENTIONAL_DIVERSIFIER (phi -0.125); failure: NYI net faces heavy volume (33+ shots; TOR pressure)

portfolios: A EV +7.80 (adj +1.65) on $50.00, P(profit) 0.6659, adj growth 14.7 bp · B EV +8.99 (adj +3.45) on $48.24, P(profit) 0.7233, adj growth 30.0 bp · C EV +5.14 (adj +1.35) on $31.06, P(profit) 0.6943, adj growth 11.9 bp
equivalent contracts collapsed: KXNHLGAME-26SEP30NYITOR-NYI|yes == KXNHLGAME-26SEP30NYITOR-TOR|no

## LAK @ COL  ·  10000 joint draws  ·  350 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.638 / away 0.362

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_LAK_win | p_overtime | goals | shots COL/LAK | COL/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.127 | 0.66 | 0.34 | 0.00 | 5.96 | 34.6/22.4 | 19.7/30.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.54 | 0.46 | 0.49 | 5.81 | 34.4/22.3 | 19.2/31.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.62 | 0.38 | 0.00 | 5.97 | 28.7/28.1 | 25.2/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.50 | 0.50 | 0.50 | 5.89 | 28.9/28.1 | 24.9/25.6 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.071 | 0.73 | 0.27 | 0.00 | 9.19 | 35.8/23.7 | 19.4/27.7 | even strength |
| COL shot control · low event (<=4) · tight (1-goal/OT) | 0.069 | 0.53 | 0.47 | 0.42 | 2.75 | 32.7/21.1 | 19.6/31.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | stake | thesis | conc top2 | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| Nathan MacKinnon: 1+ goals NO | 55 | 0.644 | 0.619 | +0.076 | +0.052 | $19.49 | COL:SUPPRESSED | 0.2308 | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 1+ assists NO | 67 | 0.792 | 0.706 | +0.106 | +0.021 | $19.49 | LAK:SUPPRESSED | 0.2359 | EVIDENCE_MIXED | D |
| Alex Laferriere: 1+ goals YES | 21 | 0.251 | 0.239 | +0.029 | +0.018 | $5.75 | LAK:OFFENSE_4PLUS | 0.2457 | EVIDENCE_STRONGER | D |
| Colorado over 3.5 goals scored NO | 50 | 0.580 | 0.538 | +0.063 | +0.020 | $5.26 | COL:SUPPRESSED | 0.2759 | EVIDENCE_MIXED | D |
- **Nathan MacKinnon: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26SEP30LACOL-COL4|no; why: higher confidence-adjusted growth (23.98 vs 3.54 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.988 vs 0.841); relationships: KXNHLAST-26SEP30LACOL-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26SEP30LACOL-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLTEAMTOTAL-26SEP30LACOL-COL4|no: REINFORCING (phi 0.282); failure: COL offense succeeds (4+ goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26SEP30LACOL-6|no; why: higher confidence-adjusted growth (4.33 vs 1.68 bp); wins across more scripts (relative breadth 0.996 vs 0.747); relationships: KXNHLGOAL-26SEP30LACOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26SEP30LACOL-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.092); KXNHLTEAMTOTAL-26SEP30LACOL-COL4|no: MOSTLY_INDEPENDENT (phi 0.005); failure: LAK offense succeeds (4+ goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGAME-26SEP30LACOL-COL|no; why: higher confidence-adjusted growth (3.93 vs 1.87 bp); despite a smaller raw edge (+0.029 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26SEP30LACOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26SEP30LACOL-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.092); KXNHLTEAMTOTAL-26SEP30LACOL-COL4|no: MOSTLY_INDEPENDENT (phi -0.001); failure: LAK offense suppressed (<= 2 goals)
- **Colorado over 3.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26SEP30LACOL-COLNMACKINNON29-1|no; why: second expression of the same thesis: KXNHLGOAL-26SEP30LACOL-COLNMACKINNON29-1|no has the higher standalone adjusted growth (23.98 vs 3.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.282); they share one thesis budget; relationships: KXNHLGOAL-26SEP30LACOL-COLNMACKINNON29-1|no: REINFORCING (phi 0.282); KXNHLAST-26SEP30LACOL-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26SEP30LACOL-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: COL offense succeeds (4+ goals)

portfolios: A EV +11.01 (adj +2.22) on $50.00, P(profit) 0.6264, adj growth 18.8 bp · B EV +7.04 (adj +3.03) on $50.00, P(profit) 0.6196, adj growth 27.3 bp · C EV +7.04 (adj +3.03) on $50.00, P(profit) 0.6196, adj growth 27.3 bp
equivalent contracts collapsed: KXNHLGAME-26SEP30LACOL-LA|yes == KXNHLGAME-26SEP30LACOL-COL|no

_RESEARCH_ONLY thesis card: stakes are suggestions for a nominal bankroll; nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
