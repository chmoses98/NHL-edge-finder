# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-31T18:26:10Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +26.28 | +8.52 | +23.73 | 0.663 | -43.70 | -62.01 | 69.71 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +33.55 | +21.24 | +27.68 | 0.660 | -52.01 | -69.93 | 188.48 |
| C best expression per thesis | 150.01 | +26.60 | +14.34 | +22.70 | 0.641 | -47.02 | -64.12 | 125.39 |
| R FUNDED research stakes | 18.00 | +2.66 | +1.65 | +2.01 | 0.604 | -4.89 | -11.36 | 0.00 |

## BUF @ LAK  ·  10000 joint draws  ·  518 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.457 / away 0.543

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BUF_win | p_overtime | goals | shots LAK/BUF | LAK/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 6.02 | 27.9/27.9 | 24.7/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.48 | 5.9 | 28.1/28.2 | 24.8/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.57 | 0.43 | 0.00 | 9.19 | 29.2/29.3 | 23.8/22.7 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.072 | 0.65 | 0.35 | 0.00 | 6.03 | 32.7/22.2 | 19.5/28.1 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.066 | 0.51 | 0.49 | 0.00 | 5.99 | 22.4/32.9 | 29.4/19.1 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.51 | 0.49 | 0.42 | 5.95 | 32.9/22.4 | 19.1/29.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Andre Lee: 1+ goals YES | 9 | 0.125 | 0.115 | +0.029 | +0.019 | $3.92 | FUNDED_RESEARCH | $1 | LAK:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.080 | 0.067 | +0.027 | +0.014 | $2.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:WINS_BY_2PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Scott Laughton: 1+ goals YES | 12 | 0.159 | 0.148 | +0.032 | +0.021 | $4.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Alex Laferriere: 1+ goals YES | 25 | 0.297 | 0.284 | +0.034 | +0.021 | $5.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Andre Lee: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes; why: higher confidence-adjusted growth (8.97 vs 8.16 bp); despite a smaller raw edge (+0.029 vs +0.032/contract); relationships: KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: LAK offense suppressed (<= 2 goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK wins by 2+; alternative: KXNHLSPREAD-26OCT31BUFLA-BUF2|no; why: higher confidence-adjusted growth (8.37 vs 6.27 bp); despite a smaller raw edge (+0.027 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: LAK offense suppressed (<= 2 goals)
- **Scott Laughton: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT31BUFLA-BUF2|no; why: higher confidence-adjusted growth (8.16 vs 6.27 bp); despite a smaller raw edge (+0.032 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: LAK offense suppressed (<= 2 goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes has the higher standalone adjusted growth (8.16 vs 4.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis LAK:OFFENSE_4PLUS (p 0.4171): highest fidelity KXNHLTEAMTOTAL-26OCT31BUFLA-LA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:WINS_BY_2PLUS (p 0.3205): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no (same contract)
- thesis LAK:WINS (p 0.5446): highest fidelity KXNHLSPREAD-26OCT31BUFLA-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31BUFLA-BUF2|no (same contract)
- KXNHLGOAL-26OCT31BUFLA-LAALEE47-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3693, phi -0.15)
- KXNHLGOAL-26OCT31BUFLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3693, phi -0.122)
- KXNHLGOAL-26OCT31BUFLA-LASLAUGHTON21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3693, phi -0.193)
- KXNHLGOAL-26OCT31BUFLA-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3693, phi -0.241)

portfolios: A EV +2.93 (adj +0.87) on $26.05, P(profit) 0.4744, adj growth 6.8 bp · B EV +4.22 (adj +2.58) on $16.34, P(profit) 0.5223, adj growth 22.8 bp · C EV +3.03 (adj +1.42) on $23.38, P(profit) 0.782, adj growth 12.4 bp · R EV +0.30 (adj +0.20) on $1.00, P(profit) 0.1247, adj growth 7.0 bp

## OTT @ SJS  ·  10000 joint draws  ·  440 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.423 / away 0.577

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_OTT_win | p_overtime | goals | shots SJS/OTT | SJS/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.52 | 0.48 | 0.00 | 6.03 | 26.9/27.3 | 23.8/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.48 | 0.52 | 0.45 | 5.98 | 27.1/27.4 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.104 | 0.53 | 0.47 | 0.00 | 9.34 | 28.3/28.8 | 22.7/22.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.089 | 0.46 | 0.54 | 0.00 | 6.04 | 21.7/32.5 | 28.7/18.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.49 | 0.51 | 0.44 | 5.92 | 21.4/32.2 | 28.9/18.2 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.063 | 0.42 | 0.58 | 0.00 | 9.25 | 23.1/34.3 | 27.3/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Kleven: 1+ goals YES | 4 | 0.061 | 0.055 | +0.019 | +0.012 | $2.41 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Claude Giroux: 1+ goals YES | 18 | 0.222 | 0.210 | +0.032 | +0.020 | $5.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 23 | 0.273 | 0.260 | +0.031 | +0.017 | $4.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Ottawa wins by over 2.5 goals NO | 76 | 0.822 | 0.788 | +0.049 | +0.016 | $16.43 | FUNDED_RESEARCH | $5 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tyler Kleven: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (7.52 vs 5.58 bp); despite a smaller raw edge (+0.019 vs +0.032/contract); relationships: KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31OTTSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT31OTTSJ-OTT3|no: INTENTIONAL_DIVERSIFIER (phi -0.092); failure: OTT offense suppressed (<= 2 goals)
- **Claude Giroux: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31OTTSJ-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (5.58 vs 1.28 bp); alternative not eligible: confidence-adjusted EV +0.0091 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31OTTSJ-OTTTKLEVEN43-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31OTTSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT31OTTSJ-OTT3|no: INTENTIONAL_DIVERSIFIER (phi -0.153); failure: OTT offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes; why: Player prop expression KXNHLGOAL-26OCT31OTTSJ-SJMMARCHMENT27-1|yes selected over player prop KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.38 vs 0.44 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT31OTTSJ-OTTTKLEVEN43-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26OCT31OTTSJ-OTT3|no: MOSTLY_INDEPENDENT (phi 0.12); failure: SJS offense suppressed (<= 2 goals)
- **Ottawa wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT31OTTSJ-OTT2|no; why: higher confidence-adjusted growth (3.08 vs 2.44 bp); despite a smaller raw edge (+0.049 vs +0.052/contract); relationships: KXNHLGOAL-26OCT31OTTSJ-OTTTKLEVEN43-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.092); KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.153); KXNHLGOAL-26OCT31OTTSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.12); failure: OTT wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4197): highest fidelity KXNHLSPREAD-26OCT31OTTSJ-OTT3|no [DIRECT], best adjusted EV KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes — Player prop expression KXNHLGOAL-26OCT31OTTSJ-SJMMARCHMENT27-1|yes selected over player prop KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.38 vs 0.44 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis OTT:OFFENSE_4PLUS (p 0.4145): highest fidelity KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes (same contract)
- thesis SJS:WINS (p 0.5092): highest fidelity KXNHLSPREAD-26OCT31OTTSJ-OTT2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT31OTTSJ-OTT2|no (same contract)
- KXNHLGOAL-26OCT31OTTSJ-OTTTKLEVEN43-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3748, phi -0.115)
- KXNHLGOAL-26OCT31OTTSJ-OTTCGIROUX28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3748, phi -0.213)
- KXNHLGOAL-26OCT31OTTSJ-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3634, phi -0.205)
- KXNHLSPREAD-26OCT31OTTSJ-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2817, phi -0.743)
- override: Player prop expression KXNHLGOAL-26OCT31OTTSJ-SJMMARCHMENT27-1|yes selected over player prop KXNHLAST-26OCT31OTTSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.38 vs 0.44 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.55 (adj +1.17) on $26.05, P(profit) 0.4798, adj growth 9.6 bp · B EV +3.51 (adj +1.87) on $28.34, P(profit) 0.4562, adj growth 16.7 bp · C EV +3.90 (adj +1.65) on $31.83, P(profit) 0.4484, adj growth 14.4 bp · R EV +0.32 (adj +0.10) on $5.00, P(profit) 0.8219, adj growth 3.6 bp

## PIT @ MTL  ·  10000 joint draws  ·  504 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.535 / away 0.465

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_PIT_win | p_overtime | goals | shots MTL/PIT | MTL/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.55 | 0.45 | 0.00 | 6.06 | 27.2/27.5 | 24.2/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.55 | 0.45 | 0.00 | 9.4 | 28.8/29.0 | 23.0/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.53 | 0.47 | 0.45 | 5.91 | 27.1/27.4 | 24.0/23.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.084 | 0.50 | 0.50 | 0.00 | 6.1 | 21.8/32.6 | 28.8/18.3 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.50 | 0.50 | 0.47 | 5.93 | 21.6/32.3 | 29.0/18.4 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.066 | 0.47 | 0.53 | 0.00 | 9.24 | 23.1/34.3 | 27.4/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Blake Lizotte: 1+ goals YES | 9 | 0.121 | 0.112 | +0.025 | +0.016 | $3.41 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 13 | 0.159 | 0.149 | +0.021 | +0.011 | $2.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Zachary Bolduc: 1+ assists YES | 24 | 0.303 | 0.266 | +0.050 | +0.014 | $3.62 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_MIXED | D |
| Rickard Rakell: 1+ goals YES | 30 | 0.337 | 0.326 | +0.022 | +0.012 | $3.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (6.45 vs 2.41 bp); relationships: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi -0.041); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: MTL wins (incl. OT/SO)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (2.41 vs 1.39 bp); despite a smaller raw edge (+0.021 vs +0.022/contract); relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: PIT offense suppressed (<= 2 goals)
- **Zachary Bolduc: 1+ assists YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-MTLPDANAULT24-1|yes; why: higher confidence-adjusted growth (2.14 vs 1.12 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.041); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: MTL offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes has the higher standalone adjusted growth (2.41 vs 1.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4051): highest fidelity KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4375): highest fidelity KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes (same contract)
- KXNHLGOAL-26OCT31PITMTL-PITBLIZOTTE46-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:WINS (p 0.5282, phi -0.172)
- KXNHLGOAL-26OCT31PITMTL-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3817, phi -0.201)
- KXNHLAST-26OCT31PITMTL-MTLZBOLDUC76-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3469, phi -0.243)
- KXNHLGOAL-26OCT31PITMTL-PITRRAKELL67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3817, phi -0.243)

portfolios: A EV +3.47 (adj +1.50) on $19.76, P(profit) 0.4871, adj growth 12.5 bp · B EV +2.23 (adj +1.10) on $12.88, P(profit) 0.4871, adj growth 9.8 bp · C EV +1.25 (adj +0.47) on $7.00, P(profit) 0.4133, adj growth 4.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## TOR @ VAN  ·  10000 joint draws  ·  418 bet sides mapped, 24 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.371 / away 0.629

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_TOR_win | p_overtime | goals | shots VAN/TOR | VAN/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.50 | 0.50 | 0.00 | 6.05 | 28.3/28.4 | 24.9/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.49 | 0.51 | 0.47 | 5.96 | 28.5/28.7 | 25.3/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.109 | 0.51 | 0.49 | 0.00 | 9.38 | 29.9/30.0 | 23.7/23.6 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.073 | 0.47 | 0.53 | 0.00 | 6.06 | 22.3/33.3 | 29.2/19.0 | even strength |
| TOR shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.46 | 0.54 | 0.47 | 6.0 | 22.9/33.4 | 30.1/19.7 | even strength |
| VAN shot control · normal event (5-7) · decided (2+) | 0.061 | 0.55 | 0.45 | 0.00 | 6.05 | 33.0/22.8 | 19.6/29.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Linus Karlsson: 1+ goals YES | 19 | 0.269 | 0.248 | +0.069 | +0.048 | $11.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 18 | 0.247 | 0.229 | +0.056 | +0.038 | $9.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ goals NO | 71 | 0.784 | 0.764 | +0.059 | +0.040 | $16.43 | FUNDED_RESEARCH | $5 | TOR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Teddy Blueger: 1+ goals YES | 13 | 0.165 | 0.153 | +0.027 | +0.015 | $3.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (30.17 vs 20.61 bp); relationships: KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31TORVAN-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (30.17 vs 20.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT31TORVAN-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: VAN offense suppressed (<= 2 goals)
- **Gavin McKenna: 1+ goals NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT31TORVAN-VAN2|yes; why: higher confidence-adjusted growth (17.38 vs 12.30 bp); despite a smaller raw edge (+0.059 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.015 vs 0.522); relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT31TORVAN-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: TOR offense succeeds (4+ goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT31TORVAN-TORTSTECHER28-1|yes; why: higher confidence-adjusted growth (4.39 vs 0.00 bp); despite a smaller raw edge (+0.027 vs +0.041/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.4305): highest fidelity KXNHLTEAMTOTAL-26OCT31TORVAN-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLSPREAD-26OCT31TORVAN-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3557): highest fidelity KXNHLSPREAD-26OCT31TORVAN-TOR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31TORVAN-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.239)
- KXNHLGOAL-26OCT31TORVAN-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3565, phi -0.223)
- KXNHLGOAL-26OCT31TORVAN-TORGMCKENNA92-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4235, phi -0.203)
- KXNHLGOAL-26OCT31TORVAN-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3557, phi -0.188)

portfolios: A EV +5.03 (adj +0.95) on $26.05, P(profit) 0.6025, adj growth 7.7 bp · B EV +8.49 (adj +5.75) on $40.01, P(profit) 0.5218, adj growth 51.4 bp · C EV +7.54 (adj +4.64) on $36.24, P(profit) 0.4143, adj growth 40.9 bp · R EV +0.41 (adj +0.27) on $5.00, P(profit) 0.7837, adj growth 10.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT31TORVAN-VAN|yes == KXNHLGAME-26OCT31TORVAN-TOR|no

## CBJ @ DAL  ·  10000 joint draws  ·  458 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.626 / away 0.373

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_CBJ_win | p_overtime | goals | shots DAL/CBJ | DAL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.56 | 0.44 | 0.00 | 5.97 | 26.1/25.9 | 22.7/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.50 | 0.50 | 0.47 | 5.89 | 26.2/25.9 | 22.7/23.1 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.085 | 0.57 | 0.43 | 0.00 | 5.98 | 31.3/20.7 | 17.6/27.3 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.58 | 0.42 | 0.46 | 5.86 | 30.9/20.5 | 17.3/27.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.57 | 0.43 | 0.00 | 9.23 | 27.9/27.8 | 21.9/21.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.064 | 0.54 | 0.46 | 0.00 | 3.44 | 25.0/24.8 | 23.0/22.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Damon Severson: 1+ goals YES | 6 | 0.107 | 0.092 | +0.043 | +0.029 | $5.13 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 18 | 0.254 | 0.234 | +0.063 | +0.043 | $10.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 13 | 0.187 | 0.170 | +0.049 | +0.032 | $6.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Ryan Lomberg: 1+ goals YES | 5 | 0.077 | 0.068 | +0.024 | +0.015 | $2.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (28.32 vs 26.37 bp); despite a smaller raw edge (+0.043 vs +0.063/contract); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (26.37 vs 18.71 bp); relationships: KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (26.37 vs 18.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Ryan Lomberg: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (26.37 vs 8.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.3151): highest fidelity KXNHLTEAMTOTAL-26OCT31CBJDAL-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.249): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.4138): highest fidelity KXNHLSPREAD-26OCT31CBJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT31CBJDAL-DALMRANTANEN96-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31CBJDAL-CBJDSEVERSON78-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.155)
- KXNHLGOAL-26OCT31CBJDAL-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.241)
- KXNHLGOAL-26OCT31CBJDAL-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.225)
- KXNHLGOAL-26OCT31CBJDAL-CBJRLOMBERG94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4565, phi -0.125)

portfolios: A EV +4.33 (adj +2.19) on $26.05, P(profit) 0.4766, adj growth 20.1 bp · B EV +10.35 (adj +6.90) on $24.65, P(profit) 0.4991, adj growth 60.6 bp · C EV +8.41 (adj +5.41) on $43.95, P(profit) 0.3933, adj growth 47.0 bp · R EV +1.33 (adj +0.89) on $2.00, P(profit) 0.1066, adj growth 28.6 bp

## CGY @ COL  ·  10000 joint draws  ·  448 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.777 / away 0.223

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_CGY_win | p_overtime | goals | shots COL/CGY | COL/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.155 | 0.79 | 0.21 | 0.00 | 6.01 | 35.7/22.8 | 20.5/30.2 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.119 | 0.80 | 0.20 | 0.00 | 9.38 | 37.3/24.1 | 20.0/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.76 | 0.24 | 0.00 | 6.05 | 29.8/29.1 | 26.7/24.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.62 | 0.38 | 0.51 | 5.95 | 36.0/22.9 | 19.8/32.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.78 | 0.22 | 0.00 | 9.41 | 31.4/30.5 | 26.1/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.57 | 0.43 | 0.43 | 5.99 | 29.9/29.1 | 25.8/26.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jonathan Castagna: 1+ goals YES | 7 | 0.110 | 0.099 | +0.035 | +0.024 | $4.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ goals NO | 74 | 0.799 | 0.783 | +0.045 | +0.029 | $16.43 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 15 | 0.193 | 0.178 | +0.034 | +0.019 | $4.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Maxim Tsyplakov: 1+ goals YES | 7 | 0.095 | 0.086 | +0.020 | +0.011 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes; why: higher confidence-adjusted growth (17.82 vs 6.25 bp); despite a smaller raw edge (+0.035 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.925 vs 0.801); relationships: KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31CGYCOL-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT31CGYCOL-CGYMTSYPLAKOV72-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: CGY offense suppressed (<= 2 goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGAME-26OCT31CGYCOL-COL|no; why: higher confidence-adjusted growth (10.27 vs 5.84 bp); despite a smaller raw edge (+0.045 vs +0.079/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT31CGYCOL-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31CGYCOL-CGYMTSYPLAKOV72-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: COL offense succeeds (4+ goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes; why: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes has the higher standalone adjusted growth (6.25 vs 6.10 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.187); relationships: KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT31CGYCOL-CGYMTSYPLAKOV72-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CGY offense suppressed (<= 2 goals)
- **Maxim Tsyplakov: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes; why: KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes has the higher standalone adjusted growth (6.25 vs 4.00 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.152); relationships: KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT31CGYCOL-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12.
- thesis CGY:OFFENSE_4PLUS (p 0.2792): highest fidelity KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes (same contract)
- thesis CGY:WINS (p 0.3004): highest fidelity KXNHLGAME-26OCT31CGYCOL-COL|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT31CGYCOL-CGY4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.2361): highest fidelity KXNHLSPREAD-26OCT31CGYCOL-COL3|no [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT31CGYCOL-COL|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT31CGYCOL-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5138, phi -0.174)
- KXNHLGOAL-26OCT31CGYCOL-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5694, phi -0.164)
- KXNHLGOAL-26OCT31CGYCOL-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5138, phi -0.224)
- KXNHLGOAL-26OCT31CGYCOL-CGYMTSYPLAKOV72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5138, phi -0.152)

portfolios: A EV +6.98 (adj +1.84) on $26.05, P(profit) 0.5555, adj growth 13.1 bp · B EV +4.75 (adj +3.04) on $27.78, P(profit) 0.3499, adj growth 27.1 bp · C EV +2.47 (adj +0.75) on $7.61, P(profit) 0.3874, adj growth 6.6 bp · R EV +0.30 (adj +0.19) on $5.00, P(profit) 0.7988, adj growth 7.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
