# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-30T00:40:56Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +29.24 | +6.11 | +26.65 | 0.700 | -42.66 | -61.17 | 45.27 |
| B thesis-diversified (joint) ← optimiser card | 141.64 | +16.86 | +9.40 | +9.95 | 0.653 | -40.80 | -49.54 | 83.59 |
| C best expression per thesis | 123.78 | +16.40 | +5.67 | +17.74 | 0.689 | -28.19 | -43.99 | 50.37 |
| R FUNDED research stakes | 19.00 | +1.50 | +0.90 | +1.42 | 0.618 | -6.03 | -7.08 | 0.00 |

## BUF @ ANA  ·  10000 joint draws  ·  446 bet sides mapped, 23 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.436 / away 0.564

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_BUF_win | p_overtime | goals | shots ANA/BUF | ANA/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.58 | 0.42 | 0.00 | 6.05 | 28.2/28.1 | 24.9/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.51 | 0.49 | 0.48 | 5.99 | 28.1/28.0 | 24.6/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.58 | 0.42 | 0.00 | 9.42 | 29.7/29.5 | 23.5/22.9 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.080 | 0.68 | 0.32 | 0.00 | 6.02 | 33.2/22.3 | 19.7/28.4 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.066 | 0.68 | 0.32 | 0.00 | 9.3 | 34.5/23.5 | 18.9/26.5 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.55 | 0.45 | 0.48 | 6.03 | 33.9/22.8 | 19.5/30.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Washe: 1+ goals YES | 10 | 0.155 | 0.135 | +0.049 | +0.029 | $6.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 62 | 0.698 | 0.677 | +0.062 | +0.041 | $20.00 | FUNDED_RESEARCH | $5 | BUF:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 17 | 0.223 | 0.207 | +0.043 | +0.027 | $7.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 30 | 0.348 | 0.335 | +0.033 | +0.020 | $7.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BUFANA-ANAAGREER18-1|yes; why: higher confidence-adjusted growth (18.45 vs 12.04 bp); despite a smaller raw edge (+0.049 vs +0.104/contract); relationships: KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29BUFANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: ANA offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT29BUFANA-ANA3|yes; why: higher confidence-adjusted growth (15.92 vs 8.04 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.006 vs 0.46); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29BUFANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: BUF offense succeeds (4+ goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BUFANA-ANAAGREER18-1|yes; why: KXNHLGOAL-26OCT29BUFANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (12.04 vs 10.66 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.000); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT29BUFANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29BUFANA-ANAAGREER18-1|yes; why: KXNHLGOAL-26OCT29BUFANA-ANAAGREER18-1|yes has the higher standalone adjusted growth (12.04 vs 4.03 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.016); relationships: KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis BUF:SUPPRESSED (p 0.4009): highest fidelity KXNHLTEAMTOTAL-26OCT29BUFANA-BUF5|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:OFFENSE_4PLUS (p 0.469): highest fidelity KXNHLTEAMTOTAL-26OCT29BUFANA-ANA3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT29BUFANA-ANAAGREER18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.3402): highest fidelity KXNHLGAME-26OCT29BUFANA-BUF|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT29BUFANA-BUF3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29BUFANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3158, phi -0.158)
- KXNHLGOAL-26OCT29BUFANA-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3736, phi -0.233)
- KXNHLGOAL-26OCT29BUFANA-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3158, phi -0.201)
- KXNHLGOAL-26OCT29BUFANA-ANABSENNECKE45-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3158, phi -0.24)

portfolios: A EV +15.40 (adj +3.42) on $50.00, P(profit) 0.5886, adj growth 23.0 bp · B EV +7.63 (adj +4.73) on $41.64, P(profit) 0.4997, adj growth 41.4 bp · C EV +6.85 (adj +2.74) on $29.29, P(profit) 0.7763, adj growth 24.3 bp · R EV +0.48 (adj +0.32) on $5.00, P(profit) 0.6982, adj growth 11.8 bp
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
| Joel Edmundson: 1+ goals YES | 5 | 0.075 | 0.068 | +0.022 | +0.015 | $2.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Drake Batherson: 1+ goals NO | 68 | 0.733 | 0.719 | +0.038 | +0.023 | $15.77 | FUNDED_RESEARCH | $4 | OTT:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Ottawa wins by over 2.5 goals NO | 80 | 0.861 | 0.828 | +0.049 | +0.017 | $18.58 | FUNDED_RESEARCH | $5 | LAK:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Erik Gustafsson: 1+ assists NO | 64 | 0.708 | 0.672 | +0.052 | +0.016 | $12.69 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT3|no; why: higher confidence-adjusted growth (8.81 vs 3.97 bp); despite a smaller raw edge (+0.022 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT29OTTLA-OTT3|no: MOSTLY_INDEPENDENT (phi 0.071); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi -0.032); failure: LAK offense suppressed (<= 2 goals)
- **Drake Batherson: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29OTTLA-OTTTCHABOT72-1|no; why: Player prop expression KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no selected over player prop KXNHLAST-26OCT29OTTLA-OTTTCHABOT72-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLSPREAD-26OCT29OTTLA-OTT3|no: REINFORCING (phi 0.16); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense succeeds (4+ goals)
- **Ottawa wins by over 2.5 goals NO** — thesis: LAK wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT29OTTLA-OTT2|no; why: Broad expression KXNHLSPREAD-26OCT29OTTLA-OTT3|no selected over player prop KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.071); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: REINFORCING (phi 0.16); KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: INTENTIONAL_DIVERSIFIER (phi -0.116); failure: OTT wins by 2+
- **Erik Gustafsson: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT29OTTLA-LAEGUSTAFSSON64-1|no; why: higher confidence-adjusted growth (2.36 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.032); KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26OCT29OTTLA-OTT3|no: INTENTIONAL_DIVERSIFIER (phi -0.116); failure: LAK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis OTT:SUPPRESSED (p 0.4553): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT29OTTLA-OTTTCHABOT72-1|no — Player prop expression KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no selected over player prop KXNHLAST-26OCT29OTTLA-OTTTCHABOT72-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis LAK:OFFENSE_4PLUS (p 0.3832): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT29OTTLA-OTT3|no (same contract)
- thesis LAK:WINS (p 0.5321): highest fidelity KXNHLSPREAD-26OCT29OTTLA-OTT3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT29OTTLA-OTT3|no (same contract)
- KXNHLGOAL-26OCT29OTTLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.4032, phi -0.134)
- KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3242, phi -0.249)
- KXNHLSPREAD-26OCT29OTTLA-OTT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:WINS_BY_2PLUS (p 0.2432, phi -0.71)
- KXNHLAST-26OCT29OTTLA-LAEGUSTAFSSON64-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3832, phi -0.241)
- override: Player prop expression KXNHLGOAL-26OCT29OTTLA-OTTDBATHERSON19-1|no selected over player prop KXNHLAST-26OCT29OTTLA-OTTTCHABOT72-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.85 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLSPREAD-26OCT29OTTLA-OTT3|no selected over player prop KXNHLAST-26OCT29OTTLA-OTTJSANDERSON85-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +5.32 (adj +1.52) on $50.00, P(profit) 0.7493, adj growth 13.8 bp · B EV +4.23 (adj +2.01) on $50.00, P(profit) 0.492, adj growth 17.8 bp · C EV +4.12 (adj +1.42) on $50.00, P(profit) 0.4818, adj growth 12.8 bp · R EV +0.52 (adj +0.24) on $9.00, P(profit) 0.6554, adj growth 8.4 bp

## VAN @ SJS  ·  10000 joint draws  ·  420 bet sides mapped, 10 +EV candidates, 4 on card

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
| Ivar Stenberg: 1+ goals NO | 72 | 0.807 | 0.784 | +0.073 | +0.050 | $19.95 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 18 | 0.218 | 0.207 | +0.028 | +0.017 | $5.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Filip Chytil: 1+ assists NO | 72 | 0.794 | 0.752 | +0.060 | +0.018 | $19.95 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VAN:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Linus Karlsson: 1+ goals YES | 19 | 0.227 | 0.215 | +0.026 | +0.014 | $4.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (28.30 vs 3.88 bp); despite a smaller raw edge (+0.073 vs +0.099/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT29VANSJ-VANFCHYTIL77-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SJS offense succeeds (4+ goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (4.10 vs 2.69 bp); relationships: KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT29VANSJ-VANFCHYTIL77-1|no: INTENTIONAL_DIVERSIFIER (phi -0.063); KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: VAN offense suppressed (<= 2 goals)
- **Filip Chytil: 1+ assists NO** — thesis: VAN offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT29VANSJ-5|no; why: higher confidence-adjusted growth (3.62 vs 0.00 bp); wins across more scripts (relative breadth 1.002 vs 0.381); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.063); KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.077); failure: VAN offense succeeds (4+ goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT29VANSJ-VANFCHYTIL77-1|yes; why: higher confidence-adjusted growth (2.69 vs 1.88 bp); relationships: KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT29VANSJ-VANFCHYTIL77-1|no: INTENTIONAL_DIVERSIFIER (phi -0.077); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, SJS shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.3162): highest fidelity KXNHLPTS-26OCT29VANSJ-SJISTENBERG41-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT29VANSJ-SJISTENBERG41-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:SUPPRESSED (p 0.3976): highest fidelity KXNHLAST-26OCT29VANSJ-VANFCHYTIL77-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT29VANSJ-VANFCHYTIL77-1|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3799): highest fidelity KXNHLGOAL-26OCT29VANSJ-VANFCHYTIL77-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT29VANSJ-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4738, phi -0.181)
- KXNHLGOAL-26OCT29VANSJ-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3976, phi -0.201)
- KXNHLAST-26OCT29VANSJ-VANFCHYTIL77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:OFFENSE_4PLUS (p 0.3799, phi -0.206)
- KXNHLGOAL-26OCT29VANSJ-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.3976, phi -0.202)

portfolios: A EV +8.52 (adj +1.17) on $50.00, P(profit) 0.6738, adj growth 8.5 bp · B EV +5.00 (adj +2.66) on $50.00, P(profit) 0.7821, adj growth 24.4 bp · C EV +5.43 (adj +1.51) on $44.49, P(profit) 0.6586, adj growth 13.3 bp · R EV +0.50 (adj +0.34) on $5.00, P(profit) 0.807, adj growth 13.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
