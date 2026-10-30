# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T01:36:52Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.80 | +6.56 | +22.86 | 0.694 | -42.56 | -60.59 | 50.65 |
| B thesis-diversified (joint) ← optimiser card | 139.52 | +19.54 | +10.65 | +12.50 | 0.636 | -40.33 | -52.49 | 93.81 |
| C best expression per thesis | 116.64 | +12.22 | +3.95 | +11.53 | 0.752 | -22.09 | -40.76 | 35.59 |
| R FUNDED research stakes | 13.00 | +1.03 | +0.68 | +1.67 | 0.554 | -6.19 | -8.74 | 0.00 |

## BUF @ ANA  ·  10000 joint draws  ·  446 bet sides mapped, 23 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.436 / away 0.564

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BUF_win | p_overtime | goals | shots ANA/BUF | ANA/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.58 | 0.42 | 0.00 | 6.06 | 28.1/27.9 | 24.6/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.110 | 0.61 | 0.39 | 0.00 | 9.41 | 29.6/29.4 | 23.8/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.50 | 0.50 | 0.49 | 5.96 | 28.1/28.0 | 24.6/24.8 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.080 | 0.63 | 0.37 | 0.00 | 6.05 | 33.3/22.3 | 19.3/28.9 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.55 | 0.45 | 0.48 | 5.99 | 33.4/22.4 | 19.2/29.8 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.061 | 0.67 | 0.33 | 0.00 | 9.5 | 34.9/23.7 | 18.8/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Washe: 1+ goals YES | 10 | 0.166 | 0.144 | +0.060 | +0.038 | $8.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 62 | 0.689 | 0.670 | +0.052 | +0.034 | $20.00 | FUNDED_RESEARCH | $5 | BUF:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 17 | 0.222 | 0.206 | +0.042 | +0.027 | $7.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 30 | 0.350 | 0.337 | +0.036 | +0.022 | $7.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: higher confidence-adjusted growth (32.40 vs 11.48 bp); despite a smaller raw edge (+0.060 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT29BUFANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: ANA offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: KXNHLSPREAD-26OCT29BUFANA-BUF3|no has the higher standalone adjusted growth (11.48 vs 10.84 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.130); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29BUFANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: BUF offense succeeds (4+ goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: KXNHLSPREAD-26OCT29BUFANA-BUF3|no has the higher standalone adjusted growth (11.48 vs 10.37 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.098); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT29BUFANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: ANA offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29BUFANA-BUF3|no; why: KXNHLSPREAD-26OCT29BUFANA-BUF3|no has the higher standalone adjusted growth (11.48 vs 4.85 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.137); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4673): highest fidelity KXNHLTEAMTOTAL-26OCT29BUFANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-BUF3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.5568): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29BUFANA-BUF3|no (same contract)
- thesis BUF:SUPPRESSED (p 0.3933): highest fidelity KXNHLSPREAD-26OCT29BUFANA-BUF3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3168, phi -0.166)
- KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3897, phi -0.24)
- KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3168, phi -0.195)
- KXNHLGOAL-26OCT29BUFANA-ANABSENNECKE45-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3168, phi -0.244)

portfolios: A EV +14.15 (adj +3.18) on $50.00, P(profit) 0.6346, adj growth 21.7 bp · B EV +9.29 (adj +5.92) on $44.06, P(profit) 0.4675, adj growth 51.1 bp · C EV +2.02 (adj +0.78) on $20.00, P(profit) 0.8509, adj growth 7.4 bp · R EV +0.41 (adj +0.27) on $5.00, P(profit) 0.6887, adj growth 9.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT29BUFANA-ANA|yes == KXNHLGAME-26OCT29BUFANA-BUF|no

## OTT @ LAK  ·  10000 joint draws  ·  434 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.474 / away 0.526

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_OTT_win | p_overtime | goals | shots LAK/OTT | LAK/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.57 | 0.43 | 0.00 | 5.99 | 27.0/27.3 | 24.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.46 | 5.91 | 26.8/27.1 | 23.8/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.57 | 0.43 | 0.00 | 9.25 | 28.6/28.6 | 22.9/22.4 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.074 | 0.50 | 0.50 | 0.00 | 5.96 | 21.2/31.9 | 28.4/17.9 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.48 | 0.52 | 0.45 | 5.79 | 21.6/32.1 | 28.8/18.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.50 | 0.50 | 0.52 | 2.82 | 25.5/25.6 | 24.1/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Thomas Chabot: 1+ assists NO | 70 | 0.790 | 0.743 | +0.076 | +0.028 | $18.95 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Joel Edmundson: 1+ goals YES | 5 | 0.075 | 0.067 | +0.022 | +0.013 | $3.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Drake Batherson: 1+ goals NO | 69 | 0.733 | 0.721 | +0.028 | +0.016 | $11.05 | FUNDED_RESEARCH | $3 | OTT:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Erik Gustafsson: 1+ assists NO | 64 | 0.708 | 0.672 | +0.052 | +0.016 | $12.42 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
- **Thomas Chabot: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (8.44 vs 4.52 bp); despite a smaller raw edge (+0.076 vs +0.105/contract); relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.108); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: OTT offense succeeds (4+ goals)
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT3|no; why: higher confidence-adjusted growth (7.38 vs 3.97 bp); despite a smaller raw edge (+0.022 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT29OTTLA-OTTTCHABOT72-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi -0.032); failure: LAK offense suppressed (<= 2 goals)
- **Drake Batherson: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29OTTLA-OTTTCHABOT72-1|no; why: Player prop expression KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no selected over player prop KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.85 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT29OTTLA-OTTTCHABOT72-1|no: MOSTLY_INDEPENDENT (phi 0.108); KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense succeeds (4+ goals)
- **Erik Gustafsson: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT29OTTLA-LAEGUSTAFSSON64-1|no; why: higher confidence-adjusted growth (2.36 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26OCT29OTTLA-OTTTCHABOT72-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis OTT:SUPPRESSED (p 0.4553): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT29OTTLA-OTTTCHABOT72-1|no — Player prop expression KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no selected over player prop KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.85 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis LAK:OFFENSE_4PLUS (p 0.3832): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT29OTTLA-OTT3|no (same contract)
- thesis LAK:WINS (p 0.5321): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29OTTLA-OTT3|no (same contract)
- KXNHLAST-26OCT29OTTLA-OTTTCHABOT72-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3242, phi -0.228)
- KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4032, phi -0.134)
- KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3242, phi -0.249)
- KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3832, phi -0.241)
- override: Player prop expression KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no selected over player prop KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.85 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.32 (adj +1.52) on $50.00, P(profit) 0.7493, adj growth 13.8 bp · B EV +4.70 (adj +2.04) on $45.46, P(profit) 0.4702, adj growth 18.1 bp · C EV +4.12 (adj +1.42) on $50.00, P(profit) 0.4818, adj growth 12.8 bp · R EV +0.12 (adj +0.07) on $3.00, P(profit) 0.7331, adj growth 2.5 bp

## VAN @ SJS  ·  10000 joint draws  ·  420 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.602 / away 0.398

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_VAN_win | p_overtime | goals | shots SJS/VAN | SJS/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.58 | 0.42 | 0.00 | 6.06 | 27.9/27.3 | 24.2/24.0 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.109 | 0.63 | 0.37 | 0.00 | 6.04 | 33.0/21.7 | 18.9/28.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.57 | 0.43 | 0.00 | 9.42 | 29.6/29.1 | 23.3/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.51 | 0.49 | 0.47 | 6.0 | 27.7/27.4 | 24.2/24.4 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.56 | 0.44 | 0.47 | 5.96 | 33.1/21.7 | 18.5/29.7 | even strength |
| SJS shot control · high event (8+) · decided (2+) | 0.086 | 0.69 | 0.31 | 0.00 | 9.37 | 34.5/22.9 | 18.1/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 1+ goals NO | 72 | 0.807 | 0.784 | +0.073 | +0.050 | $19.32 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Tyler Toffoli: 1+ assists YES | 27 | 0.342 | 0.304 | +0.059 | +0.020 | $6.45 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
| Marco Rossi: 1+ goals YES | 18 | 0.218 | 0.207 | +0.028 | +0.017 | $5.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Filip Chytil: 1+ assists NO | 72 | 0.794 | 0.752 | +0.060 | +0.018 | $19.16 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VAN:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (28.30 vs 3.88 bp); despite a smaller raw edge (+0.073 vs +0.099/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi -0.048); KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT29VANSJ-VANFCHYTIL77-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: SJS offense succeeds (4+ goals)
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29VANSJ-SJAGAUDETTE81-1|yes; why: higher confidence-adjusted growth (4.24 vs 0.53 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.048); KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT29VANSJ-VANFCHYTIL77-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: SJS offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (4.10 vs 2.24 bp); relationships: KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT29VANSJ-VANFCHYTIL77-1|no: INTENTIONAL_DIVERSIFIER (phi -0.063); failure: VAN offense suppressed (<= 2 goals)
- **Filip Chytil: 1+ assists NO** — thesis: VAN offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT29VANSJ-5|no; why: higher confidence-adjusted growth (3.62 vs 0.26 bp); wins across more scripts (relative breadth 1.002 vs 0.381); alternative not eligible: confidence-adjusted EV +0.0040 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.063); failure: VAN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4738): highest fidelity KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3162): highest fidelity KXNHLAST-26OCT29VANSJ-SJMCELEBRINI71-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:SUPPRESSED (p 0.3976): highest fidelity KXNHLAST-26OCT29VANSJ-VANFCHYTIL77-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29VANSJ-VANFCHYTIL77-1|no (same contract)
- KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4738, phi -0.181)
- KXNHLAST-26OCT29VANSJ-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3162, phi -0.263)
- KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3976, phi -0.201)
- KXNHLAST-26OCT29VANSJ-VANFCHYTIL77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:OFFENSE_4PLUS (p 0.3799, phi -0.206)

portfolios: A EV +8.33 (adj +1.86) on $50.00, P(profit) 0.5749, adj growth 15.1 bp · B EV +5.56 (adj +2.69) on $50.00, P(profit) 0.718, adj growth 24.7 bp · C EV +6.08 (adj +1.75) on $46.64, P(profit) 0.7605, adj growth 15.4 bp · R EV +0.50 (adj +0.34) on $5.00, P(profit) 0.807, adj growth 13.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
