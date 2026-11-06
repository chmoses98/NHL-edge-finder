# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-06T00:05:14Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +16.05 | +3.49 | +15.83 | 0.615 | -40.26 | -56.70 | 24.05 |
| B thesis-diversified (joint) ← optimiser card | 48.74 | +8.18 | +4.68 | +5.29 | 0.541 | -21.50 | -48.75 | 40.62 |
| C best expression per thesis | 58.45 | +7.41 | +2.57 | +6.47 | 0.654 | -23.04 | -31.21 | 22.53 |
| R FUNDED research stakes | 3.00 | +0.90 | +0.58 | -3.00 | 0.210 | -3.00 | -3.00 | 0.00 |

## ANA @ EDM  ·  10000 joint draws  ·  466 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.629 / away 0.371

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_ANA_win | p_overtime | goals | shots EDM/ANA | EDM/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.134 | 0.62 | 0.38 | 0.00 | 9.65 | 29.5/29.5 | 23.7/22.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.60 | 0.40 | 0.00 | 6.12 | 28.0/28.0 | 24.8/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.53 | 0.47 | 0.47 | 6.05 | 28.0/27.9 | 24.6/24.4 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.071 | 0.64 | 0.36 | 0.00 | 9.52 | 34.7/23.9 | 18.9/27.1 | even strength |
| balanced shots · high event (8+) · tight (1-goal/OT) | 0.065 | 0.50 | 0.50 | 0.60 | 9.78 | 30.0/30.0 | 23.4/23.6 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.064 | 0.66 | 0.34 | 0.00 | 6.08 | 32.9/22.1 | 19.5/28.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Washe: 1+ goals YES | 11 | 0.151 | 0.140 | +0.035 | +0.023 | $5.93 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Jeff Malott: 1+ goals YES | 9 | 0.122 | 0.113 | +0.027 | +0.017 | $4.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Sam Colangelo: 1+ goals YES | 13 | 0.166 | 0.156 | +0.029 | +0.018 | $4.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 16 | 0.199 | 0.187 | +0.029 | +0.017 | $4.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (10.94 vs 4.55 bp); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: ANA offense suppressed (<= 2 goals)
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (7.37 vs 4.55 bp); despite a smaller raw edge (+0.027 vs +0.029/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: ANA offense suppressed (<= 2 goals)
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (5.97 vs 4.55 bp); despite a smaller raw edge (+0.028 vs +0.029/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes; why: higher confidence-adjusted growth (4.55 vs 4.50 bp); despite a smaller raw edge (+0.029 vs +0.035/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.433): highest fidelity KXNHLSPREAD-26NOV05ANAEDM-EDM3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2668): highest fidelity KXNHLPTS-26NOV05ANAEDM-EDMLDRAISAITL29-3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-EDMLDRAISAITL29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.5288): highest fidelity KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05ANAEDM-ANATWASHE42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.181)
- KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.148)
- KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.175)
- KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.206)

portfolios: A EV +10.19 (adj +1.32) on $50.00, P(profit) 0.6296, adj growth 7.8 bp · B EV +4.84 (adj +3.10) on $20.17, P(profit) 0.5033, adj growth 26.7 bp · C EV +4.53 (adj +1.55) on $29.44, P(profit) 0.5405, adj growth 13.5 bp · R EV +0.59 (adj +0.39) on $2.00, P(profit) 0.1514, adj growth 12.8 bp

## NSH @ COL  ·  10000 joint draws  ·  440 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.657 / away 0.343

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_NSH_win | p_overtime | goals | shots COL/NSH | COL/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.148 | 0.75 | 0.25 | 0.00 | 6.04 | 34.7/22.2 | 19.9/29.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.120 | 0.76 | 0.24 | 0.00 | 9.41 | 37.0/23.8 | 19.4/28.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.58 | 0.42 | 0.50 | 5.98 | 35.4/22.8 | 19.6/31.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.69 | 0.31 | 0.00 | 6.07 | 29.1/28.2 | 25.6/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.73 | 0.27 | 0.00 | 9.44 | 30.9/29.8 | 24.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.46 | 0.48 | 6.03 | 29.4/28.6 | 25.2/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mavrik Bourque: 1+ assists NO | 72 | 0.796 | 0.755 | +0.062 | +0.021 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Adam Wilsby: 1+ goals YES | 5 | 0.070 | 0.064 | +0.016 | +0.010 | $2.52 | FUNDED_RESEARCH | $1 | NSH:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Nils Hoglander: 1+ goals YES | 11 | 0.136 | 0.128 | +0.019 | +0.011 | $3.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 13 | 0.156 | 0.148 | +0.018 | +0.010 | $2.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05NSHCOL-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (5.13 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05NSHCOL-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV05NSHCOL-NSHNHOGLANDER21-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: NSH offense succeeds (4+ goals)
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes; why: higher confidence-adjusted growth (4.41 vs 1.98 bp); despite a smaller raw edge (+0.016 vs +0.018/contract); relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV05NSHCOL-NSHNHOGLANDER21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NSH offense suppressed (<= 2 goals)
- **Nils Hoglander: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes; why: higher confidence-adjusted growth (2.62 vs 1.98 bp); relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26NOV05NSHCOL-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: NSH offense suppressed (<= 2 goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV05NSHCOL-3|yes; why: higher confidence-adjusted growth (1.98 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.907 vs 0.738); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV05NSHCOL-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV05NSHCOL-NSHNHOGLANDER21-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NSH:SUPPRESSED (p 0.4705): highest fidelity KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.3136): highest fidelity KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.256): highest fidelity KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no (same contract)
- KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3136, phi -0.2)
- KXNHLGOAL-26NOV05NSHCOL-NSHAWILSBY2-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4705, phi -0.122)
- KXNHLGOAL-26NOV05NSHCOL-NSHNHOGLANDER21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4705, phi -0.172)
- KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4705, phi -0.216)

portfolios: A EV +5.86 (adj +2.17) on $50.00, P(profit) 0.516, adj growth 16.2 bp · B EV +3.35 (adj +1.58) on $28.57, P(profit) 0.2704, adj growth 13.9 bp · C EV +2.89 (adj +1.02) on $29.01, P(profit) 0.4574, adj growth 9.0 bp · R EV +0.31 (adj +0.19) on $1.00, P(profit) 0.0697, adj growth 5.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
