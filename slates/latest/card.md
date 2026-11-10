# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-10T23:28:21Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +25.66 | +11.23 | +22.69 | 0.685 | -33.35 | -45.57 | 101.50 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +31.21 | +20.69 | +22.54 | 0.664 | -40.53 | -54.30 | 186.40 |
| C best expression per thesis | 149.99 | +26.55 | +15.07 | +21.90 | 0.649 | -41.09 | -55.01 | 136.01 |
| R FUNDED research stakes | 13.00 | +3.94 | +3.05 | +0.99 | 0.539 | -7.98 | -8.68 | 0.00 |

## COL @ TOR  ·  10000 joint draws  ·  436 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.391 / away 0.609

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_COL_win | p_overtime | goals | shots TOR/COL | TOR/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.131 | 0.34 | 0.66 | 0.00 | 6.06 | 22.8/35.9 | 31.1/19.9 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.106 | 0.35 | 0.65 | 0.00 | 9.39 | 24.7/37.8 | 29.7/19.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.42 | 0.58 | 0.00 | 6.08 | 29.2/29.9 | 25.9/25.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.45 | 0.55 | 0.47 | 5.96 | 23.1/36.3 | 32.9/19.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.39 | 0.61 | 0.00 | 9.51 | 30.7/31.7 | 24.5/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.49 | 0.51 | 0.45 | 6.0 | 29.3/30.2 | 26.7/25.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 10 | 0.167 | 0.149 | +0.061 | +0.043 | $6.25 | FUNDED_RESEARCH | $2 | TOR:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Dakota Joshua: 1+ goals YES | 11 | 0.151 | 0.140 | +0.034 | +0.023 | $3.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ assists NO | 40 | 0.490 | 0.443 | +0.073 | +0.026 | $6.53 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.72) | EVIDENCE_MIXED | D |
| Brandon Duhaime: 1+ goals YES | 8 | 0.108 | 0.100 | +0.023 | +0.015 | $2.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10COLTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (40.32 vs 5.29 bp); relationships: KXNHLGOAL-26NOV10COLTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV10COLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense suppressed (<= 2 goals)
- **Dakota Joshua: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (40.32 vs 10.87 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.022); they share one thesis budget; relationships: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV10COLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: TOR offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-2|no; why: higher confidence-adjusted growth (5.98 vs 3.54 bp); relationships: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV10COLTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV10COLTOR-TORBDUHAIME24-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: COL offense succeeds (4+ goals)
- **Brandon Duhaime: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (40.32 vs 5.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV10COLTOR-TORDJOSHUA81-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: TOR offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.13, COL shot control · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3729): highest fidelity KXNHLGOAL-26NOV10COLTOR-TORECOWAN53-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis COL:SUPPRESSED (p 0.3011): highest fidelity KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.4088): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV10COLTOR-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4088, phi -0.201)
- KXNHLGOAL-26NOV10COLTOR-TORDJOSHUA81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4088, phi -0.171)
- KXNHLAST-26NOV10COLTOR-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 28% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4898, phi -0.308)
- KXNHLGOAL-26NOV10COLTOR-TORBDUHAIME24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.4088, phi -0.149)

portfolios: A EV +4.30 (adj +2.43) on $21.43, P(profit) 0.5556, adj growth 22.5 bp · B EV +6.34 (adj +3.98) on $18.48, P(profit) 0.3662, adj growth 36.1 bp · C EV +5.56 (adj +3.44) on $14.94, P(profit) 0.5745, adj growth 30.7 bp · R EV +1.14 (adj +0.80) on $2.00, P(profit) 0.167, adj growth 28.3 bp

## MIN @ MTL  ·  10000 joint draws  ·  444 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.464 / away 0.536

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_MIN_win | p_overtime | goals | shots MTL/MIN | MTL/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.53 | 0.47 | 0.00 | 6.03 | 28.1/28.4 | 25.1/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.52 | 0.48 | 0.46 | 6.0 | 28.2/28.4 | 25.1/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.54 | 0.46 | 0.00 | 9.33 | 29.5/29.9 | 24.0/23.0 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.087 | 0.46 | 0.54 | 0.00 | 6.04 | 22.5/33.6 | 29.8/19.2 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.48 | 0.52 | 0.46 | 5.96 | 22.4/33.7 | 30.4/19.1 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.061 | 0.45 | 0.55 | 0.00 | 9.35 | 23.9/35.3 | 28.5/18.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 9 | 0.135 | 0.123 | +0.039 | +0.027 | $4.17 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Phillip Danault: 1+ goals YES | 11 | 0.159 | 0.145 | +0.042 | +0.028 | $4.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 16 | 0.213 | 0.198 | +0.043 | +0.029 | $4.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Nick Suzuki: 1+ assists NO | 53 | 0.606 | 0.563 | +0.058 | +0.015 | $6.20 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10MINMTL-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (17.69 vs 2.05 bp); relationships: KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26NOV10MINMTL-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: MIN offense suppressed (<= 2 goals)
- **Phillip Danault: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes; why: higher confidence-adjusted growth (16.62 vs 12.88 bp); despite a smaller raw edge (+0.042 vs +0.043/contract); relationships: KXNHLGOAL-26NOV10MINMTL-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLAST-26NOV10MINMTL-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi -0.038); failure: MTL offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes has the higher standalone adjusted growth (16.62 vs 12.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.028); they share one thesis budget; relationships: KXNHLGOAL-26NOV10MINMTL-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLAST-26NOV10MINMTL-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi -0.048); failure: MTL offense suppressed (<= 2 goals)
- **Nick Suzuki: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV10MINMTL-MTLNSUZUKI14-2|no; why: higher confidence-adjusted growth (2.11 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV10MINMTL-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.048); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis MTL:OFFENSE_4PLUS (p 0.4298): highest fidelity KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.3778): highest fidelity KXNHLAST-26NOV10MINMTL-MINQHUGHES43-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV10MINMTL-MINQHUGHES43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:SUPPRESSED (p 0.359): highest fidelity KXNHLAST-26NOV10MINMTL-MTLNSUZUKI14-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV10MINMTL-MTLNSUZUKI14-1|no (same contract)
- KXNHLGOAL-26NOV10MINMTL-MINYTRENIN13-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3778, phi -0.149)
- KXNHLGOAL-26NOV10MINMTL-MTLPDANAULT24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.359, phi -0.201)
- KXNHLGOAL-26NOV10MINMTL-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.359, phi -0.213)
- KXNHLAST-26NOV10MINMTL-MTLNSUZUKI14-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4298, phi -0.269)

portfolios: A EV +2.97 (adj +0.61) on $21.43, P(profit) 0.5704, adj growth 5.4 bp · B EV +5.27 (adj +3.29) on $19.85, P(profit) 0.4275, adj growth 30.0 bp · C EV +4.05 (adj +1.88) on $19.63, P(profit) 0.4927, adj growth 16.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WSH @ OTT  ·  10000 joint draws  ·  438 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.491 / away 0.509

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_WSH_win | p_overtime | goals | shots OTT/WSH | OTT/WSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.53 | 0.47 | 0.00 | 6.03 | 27.1/26.9 | 23.5/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.48 | 0.52 | 0.47 | 5.96 | 27.3/27.0 | 23.8/24.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.093 | 0.58 | 0.42 | 0.00 | 6.0 | 32.4/21.5 | 18.4/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.53 | 0.47 | 0.00 | 9.3 | 28.9/28.5 | 22.6/22.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.58 | 0.42 | 0.47 | 5.9 | 32.4/21.5 | 18.4/28.7 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.069 | 0.58 | 0.42 | 0.00 | 9.34 | 34.2/22.8 | 17.7/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 16 | 0.238 | 0.217 | +0.069 | +0.048 | $8.03 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Ridly Greig: 1+ goals YES | 16 | 0.203 | 0.190 | +0.034 | +0.021 | $3.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 54 | 0.610 | 0.573 | +0.052 | +0.015 | $5.99 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26NOV10WSHOTT-WSHAOVECHKIN8-1|yes; why: higher confidence-adjusted growth (35.00 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV10WSHOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: WSH offense suppressed (<= 2 goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10WSHOTT-OTTDCOZENS24-1|yes; why: higher confidence-adjusted growth (6.50 vs 0.38 bp); alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV10WSHOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.105); failure: OTT offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10WSHOTT-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (2.01 vs 0.02 bp); despite a smaller raw edge (+0.052 vs +0.073/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0015 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.105); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis WSH:OFFENSE_4PLUS (p 0.3849): highest fidelity KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4214): highest fidelity KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3614): highest fidelity KXNHLAST-26NOV10WSHOTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV10WSHOTT-OTTJSANDERSON85-1|no (same contract)
- KXNHLGOAL-26NOV10WSHOTT-WSHAPROTAS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.393, phi -0.251)
- KXNHLGOAL-26NOV10WSHOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3614, phi -0.209)
- KXNHLAST-26NOV10WSHOTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4214, phi -0.262)

portfolios: A EV +5.15 (adj +3.18) on $21.43, P(profit) 0.3929, adj growth 28.8 bp · B EV +4.58 (adj +2.89) on $17.77, P(profit) 0.3929, adj growth 26.4 bp · C EV +5.34 (adj +3.37) on $20.71, P(profit) 0.3929, adj growth 30.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NJD @ WPG  ·  10000 joint draws  ·  434 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.434 / away 0.566

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_NJD_win | p_overtime | goals | shots WPG/NJD | WPG/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.50 | 0.50 | 0.00 | 6.01 | 27.5/28.1 | 24.5/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.49 | 0.51 | 0.44 | 5.89 | 27.8/28.4 | 25.2/24.5 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.098 | 0.42 | 0.58 | 0.00 | 6.01 | 21.8/33.4 | 29.4/18.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.48 | 0.52 | 0.49 | 5.87 | 22.2/33.5 | 30.0/19.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.50 | 0.50 | 0.00 | 9.29 | 29.1/29.6 | 23.6/23.1 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.057 | 0.52 | 0.48 | 0.48 | 2.87 | 26.2/26.8 | 25.3/24.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack Hughes: 1+ goals NO | 58 | 0.659 | 0.637 | +0.062 | +0.040 | $9.67 | FUNDED_RESEARCH | $3 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Tyrel Bauer: 1+ goals NO | 94 | 0.971 | 0.962 | +0.027 | +0.018 | $9.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 71 | 0.759 | 0.745 | +0.035 | +0.021 | $8.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 13 | 0.162 | 0.153 | +0.024 | +0.015 | $1.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10NJWPG-NJLEVANGELISTA77-1|no; why: higher confidence-adjusted growth (14.39 vs 7.73 bp); despite a smaller raw edge (+0.062 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV10NJWPG-WPGTBAUER77-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV10NJWPG-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV10NJWPG-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: NJD offense succeeds (4+ goals)
- **Tyrel Bauer: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV10NJWPG-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26NOV10NJWPG-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: WPG offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26NOV10NJWPG-NJTMEIER28-1|no selected over player prop KXNHLAST-26NOV10NJWPG-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV10NJWPG-WPGTBAUER77-1|no: MOSTLY_INDEPENDENT (phi 0.026); KXNHLGOAL-26NOV10NJWPG-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: NJD offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26NOV10NJWPG-NJAGRITSYUK81-1|yes; why: higher confidence-adjusted growth (4.05 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV10NJWPG-WPGTBAUER77-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV10NJWPG-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.10.
- thesis NJD:SUPPRESSED (p 0.4007): highest fidelity KXNHLTEAMTOTAL-26NOV10NJWPG-NJ4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26NOV10NJWPG-NJTMEIER28-1|no selected over player prop KXNHLAST-26NOV10NJWPG-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis WPG:SUPPRESSED (p 0.4169): highest fidelity KXNHLAST-26NOV10NJWPG-WPGJMORRISSEY44-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV10NJWPG-WPGJMORRISSEY44-1|no (same contract)
- thesis WPG:WINS (p 0.4873): highest fidelity KXNHLSPREAD-26NOV10NJWPG-NJ2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV10NJWPG-NJ3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV10NJWPG-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3797, phi -0.266)
- KXNHLGOAL-26NOV10NJWPG-WPGTBAUER77-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.36, phi -0.086)
- KXNHLGOAL-26NOV10NJWPG-NJTMEIER28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3797, phi -0.24)
- KXNHLGOAL-26NOV10NJWPG-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4007, phi -0.191)
- override: Player prop expression KXNHLGOAL-26NOV10NJWPG-NJTMEIER28-1|no selected over player prop KXNHLAST-26NOV10NJWPG-NJLEVANGELISTA77-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.73 (adj +0.78) on $21.43, P(profit) 0.5729, adj growth 6.9 bp · B EV +2.03 (adj +1.29) on $30.14, P(profit) 0.5586, adj growth 12.3 bp · C EV +3.40 (adj +1.46) on $35.66, P(profit) 0.5483, adj growth 13.7 bp · R EV +0.31 (adj +0.20) on $3.00, P(profit) 0.659, adj growth 7.5 bp

## FLA @ CBJ  ·  10000 joint draws  ·  426 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.470 / away 0.530

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_FLA_win | p_overtime | goals | shots CBJ/FLA | CBJ/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.61 | 0.39 | 0.00 | 6.02 | 27.2/27.2 | 24.1/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.51 | 0.49 | 0.49 | 5.92 | 27.2/27.4 | 24.1/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.60 | 0.40 | 0.00 | 9.33 | 28.5/28.8 | 23.5/21.9 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.070 | 0.70 | 0.30 | 0.00 | 6.04 | 31.7/21.3 | 18.7/27.1 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.070 | 0.52 | 0.48 | 0.00 | 6.04 | 21.9/31.9 | 28.3/18.5 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.56 | 0.44 | 0.47 | 5.97 | 32.4/22.2 | 19.0/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 2+ goals YES | 1 | 0.034 | 0.031 | +0.024 | +0.020 | $2.01 | FUNDED_RESEARCH | $1 | CBJ:WINS_BY_2PLUS | FRAGILE (0.08) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 15 | 0.229 | 0.208 | +0.070 | +0.049 | $5.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Dmitri Voronkov: 1+ goals YES | 14 | 0.185 | 0.173 | +0.037 | +0.024 | $4.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 24 | 0.297 | 0.282 | +0.045 | +0.029 | $5.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 2+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes; why: higher confidence-adjusted growth (68.83 vs 38.76 bp); despite a smaller raw edge (+0.024 vs +0.070/contract); relationships: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes: DUPLICATIVE (phi 0.345); KXNHLGOAL-26NOV10FLACBJ-CBJDVORONKOV10-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV10FLACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ5|yes; why: higher confidence-adjusted growth (38.76 vs 9.86 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.829 vs 0.517); relationships: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-2|yes: DUPLICATIVE (phi 0.345); KXNHLGOAL-26NOV10FLACBJ-CBJDVORONKOV10-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV10FLACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CBJ offense suppressed (<= 2 goals)
- **Dmitri Voronkov: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (38.76 vs 9.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-2|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV10FLACBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (38.76 vs 9.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-2|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV10FLACBJ-CBJDVORONKOV10-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis CBJ:WINS_BY_2PLUS (p 0.3474): highest fidelity KXNHLSPREAD-26NOV10FLACBJ-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:OFFENSE_4PLUS (p 0.4468): highest fidelity KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS (p 0.565): highest fidelity KXNHLSPREAD-26NOV10FLACBJ-FLA2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-2|yes: FUNDED_RESEARCH; family TRUSTED; loses 92% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3438, phi -0.129)
- KXNHLGOAL-26NOV10FLACBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3438, phi -0.242)
- KXNHLGOAL-26NOV10FLACBJ-CBJDVORONKOV10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3438, phi -0.164)
- KXNHLGOAL-26NOV10FLACBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3438, phi -0.25)

portfolios: A EV +5.57 (adj +2.79) on $21.43, P(profit) 0.3866, adj growth 24.5 bp · B EV +9.03 (adj +6.89) on $17.64, P(profit) 0.5613, adj growth 59.8 bp · C EV +5.99 (adj +3.76) on $25.96, P(profit) 0.343, adj growth 33.8 bp · R EV +2.21 (adj +1.87) on $1.00, P(profit) 0.0343, adj growth 56.0 bp

## DET @ STL  ·  10000 joint draws  ·  452 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.561 / away 0.439

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_DET_win | p_overtime | goals | shots STL/DET | STL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.65 | 0.35 | 0.00 | 6.02 | 27.2/27.5 | 24.7/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.53 | 0.47 | 0.48 | 5.89 | 27.0/27.3 | 24.1/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.66 | 0.34 | 0.00 | 9.3 | 28.6/28.8 | 23.3/21.5 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.073 | 0.62 | 0.38 | 0.00 | 5.97 | 21.8/32.5 | 29.5/18.0 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.49 | 0.51 | 0.50 | 5.88 | 21.8/32.4 | 29.1/18.5 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.064 | 0.71 | 0.29 | 0.00 | 6.01 | 31.4/21.6 | 19.1/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pius Suter: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $3.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Cam Fowler: 1+ goals NO | 92 | 0.947 | 0.939 | +0.022 | +0.014 | $12.23 | FUNDED_RESEARCH | $4 | STL:SUPPRESSED | DIRECT (0.98) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 26 | 0.301 | 0.290 | +0.028 | +0.016 | $3.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Lucas Raymond: 1+ assists NO | 58 | 0.640 | 0.608 | +0.043 | +0.011 | $4.07 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Pius Suter: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (7.42 vs 2.84 bp); relationships: KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26NOV10DETSTL-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: STL offense suppressed (<= 2 goals)
- **Cam Fowler: 1+ goals NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10DETSTL-STLRTHOMAS18-1|no; why: higher confidence-adjusted growth (6.05 vs 0.00 bp); despite a smaller raw edge (+0.022 vs +0.037/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV10DETSTL-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: STL offense succeeds (4+ goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV10DETSTL-STLJBARRON72-1|yes; why: higher confidence-adjusted growth (2.84 vs 0.52 bp); despite a smaller raw edge (+0.028 vs +0.082/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV10DETSTL-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.017); failure: STL offense suppressed (<= 2 goals)
- **Lucas Raymond: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10DETSTL-DETLRAYMOND23-2|no; why: higher confidence-adjusted growth (1.04 vs 0.22 bp); alternative not eligible: confidence-adjusted EV +0.0029 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis STL:OFFENSE_4PLUS (p 0.4371): highest fidelity KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4695): highest fidelity KXNHLAST-26NOV10DETSTL-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV10DETSTL-DETLRAYMOND23-1|no (same contract)
- thesis STL:SUPPRESSED (p 0.346): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV10DETSTL-STLPSUTER22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.346, phi -0.19)
- KXNHLGOAL-26NOV10DETSTL-STLCFOWLER17-1|no: FUNDED_RESEARCH; family TRUSTED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4371, phi -0.108)
- KXNHLGOAL-26NOV10DETSTL-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.346, phi -0.253)
- KXNHLAST-26NOV10DETSTL-DETLRAYMOND23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3028, phi -0.273)

portfolios: A EV +1.81 (adj +0.93) on $21.43, P(profit) 0.3326, adj growth 8.5 bp · B EV +1.67 (adj +0.94) on $22.91, P(profit) 0.4052, adj growth 8.7 bp · C EV +0.73 (adj +0.31) on $8.56, P(profit) 0.3011, adj growth 2.8 bp · R EV +0.09 (adj +0.06) on $4.00, P(profit) 0.9468, adj growth 2.3 bp

## NSH @ LAK  ·  10000 joint draws  ·  436 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.541 / away 0.459

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_NSH_win | p_overtime | goals | shots LAK/NSH | LAK/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.59 | 0.41 | 0.00 | 5.93 | 28.4/27.9 | 24.8/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.52 | 0.48 | 0.47 | 5.94 | 28.5/28.2 | 24.9/25.3 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.105 | 0.69 | 0.31 | 0.00 | 5.98 | 33.5/22.1 | 19.6/28.9 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.53 | 0.47 | 0.46 | 5.85 | 33.4/22.3 | 19.2/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.61 | 0.39 | 0.00 | 9.18 | 29.5/29.2 | 23.9/22.9 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.065 | 0.67 | 0.33 | 0.00 | 9.21 | 35.4/23.7 | 18.8/27.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.077 | 0.069 | +0.024 | +0.016 | $2.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ goals NO | 63 | 0.687 | 0.671 | +0.041 | +0.025 | $11.45 | FUNDED_RESEARCH | $3 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Steven Stamkos: 1+ goals NO | 65 | 0.696 | 0.681 | +0.030 | +0.015 | $6.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Alex Laferriere: 1+ goals YES | 27 | 0.309 | 0.298 | +0.025 | +0.014 | $2.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes; why: higher confidence-adjusted growth (10.60 vs 2.07 bp); despite a smaller raw edge (+0.024 vs +0.025/contract); relationships: KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: LAK offense suppressed (<= 2 goals)
- **Artemi Panarin: 1+ goals NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV10NSHLA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (6.09 vs 0.28 bp); despite a smaller raw edge (+0.041 vs +0.084/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.036); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: LAK offense succeeds (4+ goals)
- **Steven Stamkos: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (2.26 vs 1.62 bp); despite a smaller raw edge (+0.030 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.028); KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: NSH offense succeeds (4+ goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV10NSHLA-NSH2|no; why: higher confidence-adjusted growth (2.07 vs 0.08 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11.
- thesis LAK:SUPPRESSED (p 0.3567): highest fidelity KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no (same contract)
- thesis NSH:SUPPRESSED (p 0.4707): highest fidelity KXNHLAST-26NOV10NSHLA-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.4241): highest fidelity KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes (same contract)
- KXNHLGOAL-26NOV10NSHLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3567, phi -0.129)
- KXNHLGOAL-26NOV10NSHLA-LAAPANARIN10-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4241, phi -0.258)
- KXNHLGOAL-26NOV10NSHLA-NSHSSTAMKOS91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3177, phi -0.256)
- KXNHLGOAL-26NOV10NSHLA-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3567, phi -0.238)

portfolios: A EV +1.14 (adj +0.51) on $21.43, P(profit) 0.7552, adj growth 4.9 bp · B EV +2.29 (adj +1.41) on $23.20, P(profit) 0.5816, adj growth 12.9 bp · C EV +1.48 (adj +0.85) on $24.53, P(profit) 0.5446, adj growth 7.8 bp · R EV +0.19 (adj +0.12) on $3.00, P(profit) 0.687, adj growth 4.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
