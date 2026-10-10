# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-10T17:22:44Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.95 | +30.41 | +8.88 | +29.80 | 0.854 | -6.40 | -15.63 | 84.34 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +33.04 | +17.70 | +31.21 | 0.807 | -14.77 | -25.79 | 169.86 |
| C best expression per thesis | 150.02 | +27.86 | +13.18 | +26.40 | 0.771 | -18.37 | -30.57 | 125.33 |
| R FUNDED research stakes | 17.00 | +2.44 | +1.39 | +1.47 | 0.602 | -4.35 | -5.93 | 0.00 |

## VAN @ NJD  ·  10000 joint draws  ·  416 bet sides mapped, 36 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.709 / away 0.291

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_VAN_win | p_overtime | goals | shots NJD/VAN | NJD/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.139 | 0.64 | 0.36 | 0.00 | 6.02 | 34.0/21.8 | 19.0/29.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.53 | 0.47 | 0.46 | 5.91 | 34.3/22.1 | 18.9/30.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.49 | 0.51 | 0.47 | 5.99 | 28.5/27.6 | 24.4/25.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.57 | 0.43 | 0.00 | 6.02 | 28.2/27.4 | 24.2/24.5 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.089 | 0.63 | 0.37 | 0.00 | 9.17 | 36.1/23.3 | 18.4/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.56 | 0.44 | 0.00 | 9.29 | 30.0/29.0 | 23.0/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Luke Evangelista: 1+ assists NO | 57 | 0.765 | 0.632 | +0.177 | +0.044 | $4.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Nico Hischier: 1+ goals NO | 66 | 0.737 | 0.715 | +0.061 | +0.039 | $4.48 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| New Jersey wins by over 1.5 goals NO | 51 | 0.666 | 0.561 | +0.138 | +0.034 | $2.02 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins by over 2.5 goals NO | 64 | 0.785 | 0.687 | +0.129 | +0.031 | $3.36 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Luke Evangelista: 1+ assists NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (19.19 vs 17.93 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.107); relationships: KXNHLGOAL-26OCT10VANNJ-NJNHISCHIER13-1|no: REINFORCING (phi 0.228); KXNHLSPREAD-26OCT10VANNJ-NJ2|no: REINFORCING (phi 0.161); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: REINFORCING (phi 0.153); failure: NJD offense succeeds (4+ goals)
- **Nico Hischier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (19.19 vs 15.61 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.107); relationships: KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: REINFORCING (phi 0.228); KXNHLSPREAD-26OCT10VANNJ-NJ2|no: REINFORCING (phi 0.166); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: REINFORCING (phi 0.16); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (19.19 vs 10.03 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.279); relationships: KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: REINFORCING (phi 0.161); KXNHLGOAL-26OCT10VANNJ-NJNHISCHIER13-1|no: REINFORCING (phi 0.166); KXNHLSPREAD-26OCT10VANNJ-NJ3|no: DUPLICATIVE (phi 0.739); failure: NJD wins by 2+
- **New Jersey wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes; why: KXNHLSPREAD-26OCT10VANNJ-VAN3|yes has the higher standalone adjusted growth (19.19 vs 9.53 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.206); relationships: KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: REINFORCING (phi 0.153); KXNHLGOAL-26OCT10VANNJ-NJNHISCHIER13-1|no: REINFORCING (phi 0.16); KXNHLSPREAD-26OCT10VANNJ-NJ2|no: DUPLICATIVE (phi 0.739); failure: NJD wins by 2+

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.14, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.2281): highest fidelity KXNHLGAME-26OCT10VANNJ-VAN|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10VANNJ-VAN|yes (same contract)
- thesis NJD:SUPPRESSED (p 0.3532): highest fidelity KXNHLSPREAD-26OCT10VANNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.3408): highest fidelity KXNHLTEAMTOTAL-26OCT10VANNJ-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26OCT10VANNJ-VAN|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT10VANNJ-NJLEVANGELISTA77-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.5 pts; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4263, phi -0.211)
- KXNHLGOAL-26OCT10VANNJ-NJNHISCHIER13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4263, phi -0.24)
- KXNHLSPREAD-26OCT10VANNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 16.1 pts; opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3342, phi -1.0)
- KXNHLSPREAD-26OCT10VANNJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.0 pts; opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3342, phi -0.739)

portfolios: A EV +4.45 (adj +0.87) on $11.76, P(profit) 0.7003, adj growth 8.3 bp · B EV +2.95 (adj +0.89) on $14.34, P(profit) 0.6794, adj growth 8.7 bp · C EV +1.49 (adj +0.63) on $1.87, P(profit) 0.1342, adj growth 5.9 bp · R EV +0.64 (adj +0.23) on $4.00, P(profit) 0.6071, adj growth 8.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10VANNJ-NJ|no == KXNHLGAME-26OCT10VANNJ-VAN|yes

## EDM @ SJS  ·  10000 joint draws  ·  426 bet sides mapped, 23 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.418 / away 0.582

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_EDM_win | p_overtime | goals | shots SJS/EDM | SJS/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.118 | 0.48 | 0.52 | 0.00 | 9.57 | 29.3/29.7 | 23.2/22.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.48 | 0.52 | 0.00 | 6.06 | 27.3/27.7 | 23.9/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.49 | 0.51 | 0.47 | 6.05 | 27.7/27.9 | 24.5/24.4 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.088 | 0.42 | 0.58 | 0.00 | 6.07 | 22.0/33.1 | 28.8/19.0 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.082 | 0.40 | 0.60 | 0.00 | 9.41 | 23.2/34.9 | 27.5/17.9 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.46 | 0.54 | 0.47 | 5.93 | 22.2/33.2 | 29.9/19.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 13 | 0.207 | 0.186 | +0.069 | +0.048 | $3.81 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Collin Graf: 1+ goals YES | 18 | 0.237 | 0.220 | +0.046 | +0.030 | $2.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 33 | 0.473 | 0.374 | +0.128 | +0.028 | $3.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ assists YES | 33 | 0.418 | 0.372 | +0.073 | +0.026 | $3.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10EDMSJ-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (41.73 vs 11.01 bp); despite a smaller raw edge (+0.069 vs +0.081/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.071); KXNHLAST-26OCT10EDMSJ-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: EDM offense suppressed (<= 2 goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10EDMSJ-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (12.28 vs 6.77 bp); relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT10EDMSJ-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: SJS offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (7.63 vs 3.44 bp); relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.071); KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT10EDMSJ-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.128); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes; why: Player prop expression KXNHLAST-26OCT10EDMSJ-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT10EDMSJ-EDMMEKHOLM14-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.56 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.128); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4672): highest fidelity KXNHLAST-26OCT10EDMSJ-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes — Player prop expression KXNHLAST-26OCT10EDMSJ-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT10EDMSJ-EDMMEKHOLM14-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.56 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis SJS:OFFENSE_4PLUS (p 0.4308): highest fidelity KXNHLSPREAD-26OCT10EDMSJ-EDM2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.3236): highest fidelity KXNHLSPREAD-26OCT10EDMSJ-EDM2|no [DIRECT], best adjusted EV KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10EDMSJ-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3236, phi -0.199)
- KXNHLGOAL-26OCT10EDMSJ-SJCGRAF51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.348, phi -0.217)
- KXNHLAST-26OCT10EDMSJ-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.3 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4672, phi -0.305)
- KXNHLAST-26OCT10EDMSJ-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 44% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3236, phi -0.287)
- override: Player prop expression KXNHLAST-26OCT10EDMSJ-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT10EDMSJ-EDMMEKHOLM14-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 0.56 vs 0.47 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.46 (adj +0.59) on $11.76, P(profit) 0.6333, adj growth 5.5 bp · B EV +4.53 (adj +2.26) on $13.12, P(profit) 0.4977, adj growth 21.7 bp · C EV +5.36 (adj +2.73) on $19.43, P(profit) 0.6, adj growth 25.8 bp · R EV +0.50 (adj +0.35) on $1.00, P(profit) 0.2068, adj growth 13.4 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10EDMSJ-SJ|yes == KXNHLGAME-26OCT10EDMSJ-EDM|no

## MIN @ FLA  ·  10000 joint draws  ·  402 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.551 / away 0.449

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_MIN_win | p_overtime | goals | shots FLA/MIN | FLA/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.45 | 0.55 | 0.00 | 6.02 | 28.0/28.0 | 24.0/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.48 | 0.52 | 0.46 | 5.93 | 28.1/28.0 | 24.6/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.46 | 0.54 | 0.00 | 9.35 | 29.8/29.7 | 23.3/23.8 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.077 | 0.50 | 0.50 | 0.00 | 6.0 | 33.5/22.7 | 19.2/29.6 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.54 | 0.46 | 0.50 | 5.96 | 33.3/22.5 | 19.4/29.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.057 | 0.37 | 0.63 | 0.00 | 6.02 | 22.3/32.8 | 28.6/19.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 8 | 0.137 | 0.121 | +0.052 | +0.036 | $2.52 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Nico Sturm: 1+ goals YES | 6 | 0.104 | 0.092 | +0.040 | +0.028 | $1.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Michael McCarron: 1+ goals YES | 8 | 0.127 | 0.114 | +0.042 | +0.029 | $2.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Sandis Vilmanis: 1+ goals YES | 10 | 0.150 | 0.136 | +0.044 | +0.030 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (35.50 vs 16.81 bp); relationships: KXNHLGOAL-26OCT10MINFLA-MINNSTURM78-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT10MINFLA-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: MIN offense suppressed (<= 2 goals)
- **Nico Sturm: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (27.26 vs 16.81 bp); despite a smaller raw edge (+0.040 vs +0.051/contract); relationships: KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT10MINFLA-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: MIN offense suppressed (<= 2 goals)
- **Michael McCarron: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (22.79 vs 16.81 bp); despite a smaller raw edge (+0.042 vs +0.051/contract); relationships: KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT10MINFLA-MINNSTURM78-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: MIN offense suppressed (<= 2 goals)
- **Sandis Vilmanis: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT10MINFLA-7|yes; why: higher confidence-adjusted growth (19.97 vs 2.13 bp); despite a smaller raw edge (+0.044 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.916 vs 0.676); relationships: KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10MINFLA-MINNSTURM78-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT10MINFLA-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: FLA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4253): highest fidelity KXNHLTEAMTOTAL-26OCT10MINFLA-MIN2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10MINFLA-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis FLA:SUPPRESSED (p 0.4036): highest fidelity KXNHLSPREAD-26OCT10MINFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10MINFLA-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:WINS_BY_2PLUS (p 0.314): highest fidelity KXNHLSPREAD-26OCT10MINFLA-MIN2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10MINFLA-MIN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10MINFLA-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3525, phi -0.156)
- KXNHLGOAL-26OCT10MINFLA-MINNSTURM78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3525, phi -0.141)
- KXNHLGOAL-26OCT10MINFLA-MINMMCCARRON47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3525, phi -0.169)
- KXNHLGOAL-26OCT10MINFLA-FLASVILMANIS95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4036, phi -0.182)

portfolios: A EV +2.89 (adj +0.53) on $11.76, P(profit) 0.5758, adj growth 4.8 bp · B EV +4.64 (adj +3.22) on $8.67, P(profit) 0.4287, adj growth 30.7 bp · C EV +2.07 (adj +1.17) on $13.86, P(profit) 0.4719, adj growth 11.1 bp · R EV +0.61 (adj +0.43) on $1.00, P(profit) 0.137, adj growth 15.8 bp

## UTA @ BUF  ·  10000 joint draws  ·  420 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.496 / away 0.504

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_UTA_win | p_overtime | goals | shots BUF/UTA | BUF/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.52 | 0.48 | 0.00 | 6.04 | 27.3/27.2 | 23.8/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.48 | 0.52 | 0.45 | 5.97 | 27.6/27.4 | 24.1/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.52 | 0.48 | 0.00 | 9.35 | 29.0/28.7 | 22.6/23.1 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.076 | 0.57 | 0.43 | 0.00 | 6.01 | 32.4/21.4 | 18.4/28.2 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.54 | 0.46 | 0.45 | 5.94 | 32.7/22.0 | 18.8/29.2 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.058 | 0.59 | 0.41 | 0.00 | 9.38 | 34.2/23.1 | 17.8/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vincent Trocheck: 1+ assists NO | 68 | 0.816 | 0.725 | +0.121 | +0.029 | $5.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | UTA:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Justin Danforth: 1+ goals YES | 10 | 0.131 | 0.122 | +0.024 | +0.015 | $1.18 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 12 | 0.152 | 0.140 | +0.024 | +0.013 | $1.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Peyton Krebs: 1+ goals YES | 14 | 0.170 | 0.162 | +0.022 | +0.013 | $1.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Vincent Trocheck: 1+ assists NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10UTABUF-UTADGUENTHER11-1|no; why: higher confidence-adjusted growth (8.90 vs 0.43 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10UTABUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT10UTABUF-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT10UTABUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: UTA offense succeeds (4+ goals)
- **Justin Danforth: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10UTABUF-BUFPKREBS19-1|yes; why: higher confidence-adjusted growth (5.33 vs 2.92 bp); relationships: KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT10UTABUF-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT10UTABUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: BUF offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10UTABUF-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (3.15 vs 1.42 bp); relationships: KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT10UTABUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT10UTABUF-BUFPKREBS19-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: UTA offense suppressed (<= 2 goals)
- **Peyton Krebs: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10UTABUF-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (2.92 vs 1.16 bp); alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT10UTABUF-BUFJDANFORTH15-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT10UTABUF-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.4173): highest fidelity KXNHLGOAL-26OCT10UTABUF-BUFPKREBS19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10UTABUF-BUFPKREBS19-1|yes (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.3915): highest fidelity KXNHLGOAL-26OCT10UTABUF-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10UTABUF-UTALCROUSE67-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3807): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT10UTABUF-UTAVTROCHECK16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.1 pts; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3915, phi -0.206)
- KXNHLGOAL-26OCT10UTABUF-BUFJDANFORTH15-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3655, phi -0.149)
- KXNHLGOAL-26OCT10UTABUF-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3807, phi -0.176)
- KXNHLGOAL-26OCT10UTABUF-BUFPKREBS19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3655, phi -0.202)

portfolios: A EV +1.68 (adj +0.68) on $9.58, P(profit) 0.3926, adj growth 6.4 bp · B EV +1.67 (adj +0.62) on $9.26, P(profit) 0.3426, adj growth 6.0 bp · C EV +0.35 (adj +0.19) on $2.64, P(profit) 0.3575, adj growth 1.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DET @ MTL  ·  10000 joint draws  ·  390 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.639 / away 0.361

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_DET_win | p_overtime | goals | shots MTL/DET | MTL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.67 | 0.33 | 0.00 | 6.06 | 27.3/27.7 | 25.0/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.55 | 0.45 | 0.46 | 5.89 | 27.2/27.7 | 24.5/23.9 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.096 | 0.61 | 0.39 | 0.00 | 5.97 | 22.0/32.7 | 29.5/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.68 | 0.32 | 0.00 | 9.34 | 28.8/29.1 | 24.1/21.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.52 | 0.48 | 0.45 | 5.88 | 21.8/32.5 | 29.1/18.5 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.063 | 0.63 | 0.37 | 0.00 | 9.28 | 23.3/34.6 | 28.8/16.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nate Danielson: 1+ goals YES | 7 | 0.107 | 0.095 | +0.032 | +0.021 | $1.45 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 17 | 0.208 | 0.197 | +0.028 | +0.017 | $1.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Emmitt Finnie: 1+ goals YES | 16 | 0.201 | 0.186 | +0.031 | +0.016 | $1.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ assists NO | 69 | 0.764 | 0.720 | +0.059 | +0.015 | $4.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Nate Danielson: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes; why: higher confidence-adjusted growth (12.90 vs 4.04 bp); relationships: KXNHLGOAL-26OCT10DETMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT10DETMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: DET offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10DETMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (4.36 vs 0.00 bp); alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT10DETMTL-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT10DETMTL-MTLCKREIDER22-1|no: INTENTIONAL_DIVERSIFIER (phi -0.096); failure: MTL offense suppressed (<= 2 goals)
- **Emmitt Finnie: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGAME-26OCT10DETMTL-DET|yes; why: higher confidence-adjusted growth (4.04 vs 0.12 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0035 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10DETMTL-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT10DETMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT10DETMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.015); failure: DET offense suppressed (<= 2 goals)
- **Chris Kreider: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10DETMTL-MTLNSUZUKI14-2|no; why: higher confidence-adjusted growth (2.26 vs 1.85 bp); relationships: KXNHLGOAL-26OCT10DETMTL-DETNDANIELSON29-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT10DETMTL-MTLJANDERSON17-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.096); KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis MTL:OFFENSE_4PLUS (p 0.4837): highest fidelity KXNHLGOAL-26OCT10DETMTL-MTLJANDERSON17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10DETMTL-MTLJANDERSON17-1|yes (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3182): highest fidelity KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.312): highest fidelity KXNHLAST-26OCT10DETMTL-MTLNSUZUKI14-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT10DETMTL-MTLCKREIDER22-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT10DETMTL-DETNDANIELSON29-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4676, phi -0.147)
- KXNHLGOAL-26OCT10DETMTL-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.312, phi -0.191)
- KXNHLGOAL-26OCT10DETMTL-DETEFINNIE58-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4676, phi -0.231)
- KXNHLAST-26OCT10DETMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4837, phi -0.204)

portfolios: A EV +1.66 (adj +0.81) on $11.76, P(profit) 0.2759, adj growth 7.7 bp · B EV +1.51 (adj +0.77) on $9.03, P(profit) 0.4054, adj growth 7.4 bp · C EV +1.14 (adj +0.49) on $9.74, P(profit) 0.3659, adj growth 4.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ OTT  ·  10000 joint draws  ·  410 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.593 / away 0.407

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NSH_win | p_overtime | goals | shots OTT/NSH | OTT/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| OTT shot control · normal event (5-7) · decided (2+) | 0.133 | 0.69 | 0.31 | 0.00 | 6.01 | 33.6/21.9 | 19.4/29.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.63 | 0.37 | 0.00 | 6.04 | 28.4/27.6 | 24.6/24.3 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.55 | 0.45 | 0.50 | 5.94 | 33.8/22.0 | 18.8/30.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.48 | 0.52 | 0.46 | 5.93 | 28.2/27.6 | 24.3/25.0 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.088 | 0.71 | 0.29 | 0.00 | 9.35 | 35.7/23.4 | 18.8/27.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.61 | 0.39 | 0.00 | 9.38 | 29.7/28.9 | 23.2/23.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Michael Amadio: 1+ goals YES | 15 | 0.212 | 0.194 | +0.053 | +0.035 | $2.88 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Ryan O'Reilly: 1+ goals YES | 22 | 0.279 | 0.263 | +0.047 | +0.031 | $2.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Stephen Halliday: 1+ goals YES | 11 | 0.150 | 0.139 | +0.033 | +0.022 | $1.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Warren Foegele: 1+ goals YES | 15 | 0.186 | 0.176 | +0.028 | +0.017 | $1.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10NSHOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (19.72 vs 1.76 bp); despite a smaller raw edge (+0.053 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT10NSHOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT10NSHOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: OTT offense suppressed (<= 2 goals)
- **Ryan O'Reilly: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT10NSHOTT-7|yes; why: higher confidence-adjusted growth (11.83 vs 0.24 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.929 vs 0.703); alternative not eligible: confidence-adjusted EV +0.0052 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT10NSHOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT10NSHOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: NSH offense suppressed (<= 2 goals)
- **Stephen Halliday: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (19.72 vs 9.84 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT10NSHOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: OTT offense suppressed (<= 2 goals)
- **Warren Foegele: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (19.72 vs 4.79 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT10NSHOTT-OTTSHALLIDAY34-1|yes: MOSTLY_INDEPENDENT (phi -0.022); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts OTT shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis OTT:OFFENSE_4PLUS (p 0.4604): highest fidelity KXNHLAST-26OCT10NSHOTT-OTTJSPENCE10-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:OFFENSE_4PLUS (p 0.3268): highest fidelity KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3217): highest fidelity KXNHLGOAL-26OCT10NSHOTT-OTTDCOZENS24-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10NSHOTT-OTTDCOZENS24-1|no (same contract)
- KXNHLGOAL-26OCT10NSHOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3217, phi -0.213)
- KXNHLGOAL-26OCT10NSHOTT-NSHROREILLY90-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4537, phi -0.253)
- KXNHLGOAL-26OCT10NSHOTT-OTTSHALLIDAY34-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3217, phi -0.152)
- KXNHLGOAL-26OCT10NSHOTT-OTTWFOEGELE37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3217, phi -0.165)

portfolios: A EV +2.26 (adj +1.12) on $11.76, P(profit) 0.5431, adj growth 10.6 bp · B EV +2.29 (adj +1.51) on $8.99, P(profit) 0.6117, adj growth 14.4 bp · C EV +2.16 (adj +1.41) on $11.49, P(profit) 0.4369, adj growth 13.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ PIT  ·  10000 joint draws  ·  414 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.384 / away 0.616

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_DAL_win | p_overtime | goals | shots PIT/DAL | PIT/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.53 | 0.47 | 0.00 | 5.99 | 26.3/26.1 | 22.7/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.53 | 0.47 | 0.46 | 5.96 | 26.4/26.5 | 23.3/23.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.51 | 0.49 | 0.00 | 9.43 | 28.3/28.1 | 21.9/22.1 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.083 | 0.59 | 0.41 | 0.00 | 6.03 | 31.4/20.9 | 17.9/27.2 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.52 | 0.48 | 0.47 | 5.93 | 31.4/21.2 | 18.0/28.0 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.057 | 0.58 | 0.42 | 0.00 | 9.32 | 33.5/22.3 | 17.1/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 10 | 0.153 | 0.137 | +0.047 | +0.031 | $2.19 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Bryan Rust: 1+ goals YES | 26 | 0.330 | 0.311 | +0.057 | +0.038 | $3.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 8 | 0.115 | 0.106 | +0.030 | +0.021 | $1.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Dallas wins by over 2.5 goals NO | 75 | 0.830 | 0.787 | +0.067 | +0.024 | $4.98 | FUNDED_RESEARCH | $2 | PIT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes; why: higher confidence-adjusted growth (21.62 vs 15.81 bp); despite a smaller raw edge (+0.047 vs +0.057/contract); relationships: KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10DALPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT10DALPIT-DAL3|no: MOSTLY_INDEPENDENT (phi 0.105); failure: PIT offense suppressed (<= 2 goals)
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (21.62 vs 15.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10DALPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT10DALPIT-DAL3|no: MOSTLY_INDEPENDENT (phi 0.132); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (21.62 vs 12.44 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLSPREAD-26OCT10DALPIT-DAL3|no: MOSTLY_INDEPENDENT (phi 0.094); failure: PIT offense suppressed (<= 2 goals)
- **Dallas wins by over 2.5 goals NO** — thesis: PIT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT10DALPIT-PIT2|yes; why: Broad expression KXNHLSPREAD-26OCT10DALPIT-DAL3|no selected over player prop KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 1.00 vs 0.84 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.105); KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.132); KXNHLGOAL-26OCT10DALPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.094); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4158): highest fidelity KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS_BY_2PLUS (p 0.2945): highest fidelity KXNHLGAME-26OCT10DALPIT-PIT|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.3917): highest fidelity KXNHLSPREAD-26OCT10DALPIT-DAL3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no — Broad expression KXNHLSPREAD-26OCT10DALPIT-DAL3|no selected over player prop KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 1.00 vs 0.84 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT10DALPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3675, phi -0.193)
- KXNHLGOAL-26OCT10DALPIT-PITBRUST17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3675, phi -0.258)
- KXNHLGOAL-26OCT10DALPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3675, phi -0.163)
- KXNHLSPREAD-26OCT10DALPIT-DAL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.277, phi -0.732)
- override: Broad expression KXNHLSPREAD-26OCT10DALPIT-DAL3|no selected over player prop KXNHLAST-26OCT10DALPIT-DALRHINTZ24-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 1.00 vs 0.84 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.44 (adj +0.53) on $11.76, P(profit) 0.6359, adj growth 5.0 bp · B EV +2.68 (adj +1.67) on $12.23, P(profit) 0.4996, adj growth 16.0 bp · C EV +3.66 (adj +1.48) on $12.14, P(profit) 0.7471, adj growth 14.0 bp · R EV +0.17 (adj +0.06) on $2.00, P(profit) 0.8297, adj growth 2.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10DALPIT-DAL|no == KXNHLGAME-26OCT10DALPIT-PIT|yes

## CAR @ CHI  ·  10000 joint draws  ·  408 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.315 / away 0.685

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_CAR_win | p_overtime | goals | shots CHI/CAR | CHI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.171 | 0.34 | 0.66 | 0.00 | 6.01 | 20.4/33.5 | 28.9/17.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.139 | 0.45 | 0.55 | 0.46 | 5.9 | 20.5/33.4 | 30.1/17.4 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.120 | 0.34 | 0.66 | 0.00 | 9.36 | 22.2/35.2 | 27.5/17.4 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.079 | 0.38 | 0.62 | 0.00 | 3.46 | 19.0/32.1 | 29.8/17.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.079 | 0.39 | 0.61 | 0.00 | 6.04 | 26.1/27.1 | 23.1/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.075 | 0.47 | 0.53 | 0.47 | 5.91 | 26.3/27.4 | 24.0/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teuvo Teravainen: 1+ goals YES | 9 | 0.137 | 0.124 | +0.041 | +0.028 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 26 | 0.326 | 0.308 | +0.052 | +0.035 | $3.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_STRONGER | D |
| Ryan Donato: 1+ goals YES | 13 | 0.177 | 0.164 | +0.039 | +0.026 | $2.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 66 | 0.721 | 0.703 | +0.045 | +0.028 | $5.98 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Teuvo Teravainen: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (19.08 vs 13.20 bp); despite a smaller raw edge (+0.041 vs +0.052/contract); relationships: KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT10CARCHI-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10CARCHI-CHIRDONATO8-1|yes; why: higher confidence-adjusted growth (13.20 vs 12.29 bp); relationships: KXNHLGOAL-26OCT10CARCHI-CHITTERAVAINEN86-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT10CARCHI-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: CHI offense suppressed (<= 2 goals)
- **Ryan Donato: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (13.20 vs 12.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT10CARCHI-CHITTERAVAINEN86-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: CHI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10CARCHI-CARSAHO20-1|no; why: higher confidence-adjusted growth (7.66 vs 6.91 bp); despite a smaller raw edge (+0.045 vs +0.122/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10CARCHI-CHITTERAVAINEN86-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10CARCHI-CHIRDONATO8-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.12.
- thesis CHI:OFFENSE_4PLUS (p 0.3328): highest fidelity KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.4121): highest fidelity KXNHLSPREAD-26OCT10CARCHI-CAR3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS_BY_2PLUS (p 0.2128): highest fidelity KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2|yes (same contract)
- KXNHLGOAL-26OCT10CARCHI-CHITTERAVAINEN86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4482, phi -0.187)
- KXNHLGOAL-26OCT10CARCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4482, phi -0.268)
- KXNHLGOAL-26OCT10CARCHI-CHIRDONATO8-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4482, phi -0.207)
- KXNHLGOAL-26OCT10CARCHI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4595, phi -0.215)

portfolios: A EV +2.18 (adj +0.43) on $11.76, P(profit) 0.554, adj growth 4.1 bp · B EV +2.50 (adj +1.66) on $13.48, P(profit) 0.455, adj growth 15.9 bp · C EV +2.10 (adj +1.11) on $19.29, P(profit) 0.6656, adj growth 10.6 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.7211, adj growth 3.1 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10CARCHI-CHI|yes == KXNHLGAME-26OCT10CARCHI-CAR|no

## CBJ @ STL  ·  10000 joint draws  ·  428 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.532 / away 0.468

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_STL_win | p_CBJ_win | p_overtime | goals | shots STL/CBJ | STL/CBJ starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.57 | 0.43 | 0.00 | 5.99 | 26.8/27.1 | 23.7/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.121 | 0.51 | 0.49 | 0.49 | 5.9 | 27.0/27.2 | 23.9/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.57 | 0.43 | 0.00 | 9.21 | 28.5/28.7 | 23.0/22.0 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.079 | 0.48 | 0.52 | 0.47 | 5.89 | 21.7/32.3 | 28.8/18.5 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.079 | 0.50 | 0.50 | 0.00 | 5.97 | 21.4/32.0 | 28.3/18.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.063 | 0.58 | 0.42 | 0.00 | 3.48 | 25.6/25.8 | 24.2/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Conor Garland: 1+ goals NO | 84 | 0.887 | 0.874 | +0.038 | +0.025 | $4.72 | FUNDED_RESEARCH | $2 | CBJ:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Matthew Knies: 1+ assists NO | 65 | 0.734 | 0.689 | +0.068 | +0.023 | $4.25 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CBJ:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Charlie Coyle: 1+ goals YES | 21 | 0.243 | 0.232 | +0.021 | +0.010 | $1.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Conor Garland: 1+ goals NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no; why: higher confidence-adjusted growth (10.84 vs 5.39 bp); despite a smaller raw edge (+0.038 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT10CBJSTL-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CBJ offense succeeds (4+ goals)
- **Matthew Knies: 1+ assists NO** — thesis: CBJ offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10CBJSTL-CBJVNICHUSHKIN43-1|no; why: higher confidence-adjusted growth (5.39 vs 0.26 bp); alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10CBJSTL-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT10CBJSTL-CBJCCOYLE3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: CBJ offense succeeds (4+ goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10CBJSTL-CBJSMONAHAN23-1|yes; why: higher confidence-adjusted growth (1.37 vs 0.92 bp); alternative not eligible: confidence-adjusted EV +0.0080 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10CBJSTL-CBJCGARLAND83-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no: INTENTIONAL_DIVERSIFIER (phi -0.088); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:SUPPRESSED (p 0.447): highest fidelity KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.3309): highest fidelity KXNHLGOAL-26OCT10CBJSTL-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10CBJSTL-CBJCCOYLE3-1|yes (same contract)
- KXNHLGOAL-26OCT10CBJSTL-CBJCGARLAND83-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3309, phi -0.167)
- KXNHLAST-26OCT10CBJSTL-CBJMKNIES23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:OFFENSE_4PLUS (p 0.3309, phi -0.225)
- KXNHLGOAL-26OCT10CBJSTL-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.447, phi -0.234)

portfolios: A EV +0.84 (adj +0.38) on $11.01, P(profit) 0.7411, adj growth 3.7 bp · B EV +0.75 (adj +0.34) on $10.06, P(profit) 0.7411, adj growth 3.3 bp · C EV +0.93 (adj +0.34) on $9.21, P(profit) 0.7336, adj growth 3.2 bp · R EV +0.09 (adj +0.06) on $2.00, P(profit) 0.8875, adj growth 2.3 bp

## TOR @ COL  ·  10000 joint draws  ·  430 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.656 / away 0.344

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_TOR_win | p_overtime | goals | shots COL/TOR | COL/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.193 | 0.77 | 0.23 | 0.00 | 6.05 | 36.9/22.2 | 19.9/31.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.157 | 0.80 | 0.20 | 0.00 | 9.36 | 38.5/23.8 | 19.8/29.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.141 | 0.56 | 0.44 | 0.46 | 5.94 | 37.0/22.5 | 19.3/33.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.078 | 0.76 | 0.24 | 0.00 | 6.06 | 30.2/28.8 | 26.3/25.4 | even strength |
| COL shot control · low event (<=4) · decided (2+) | 0.070 | 0.71 | 0.29 | 0.00 | 3.52 | 35.6/21.4 | 20.2/32.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.54 | 0.46 | 0.48 | 6.06 | 30.1/28.7 | 25.1/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Zachary L'Heureux: 1+ goals YES | 12 | 0.169 | 0.153 | +0.042 | +0.026 | $1.91 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ goals NO | 76 | 0.806 | 0.792 | +0.033 | +0.019 | $5.61 | FUNDED_RESEARCH | $2 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Kirill Marchenko: 1+ assists NO | 62 | 0.700 | 0.655 | +0.063 | +0.018 | $3.81 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Martin Necas: 1+ goals NO | 62 | 0.667 | 0.654 | +0.031 | +0.018 | $3.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Zachary L'Heureux: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10TORCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (12.94 vs 0.28 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0051 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: COL offense suppressed (<= 2 goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no; why: higher confidence-adjusted growth (4.53 vs 3.01 bp); relationships: KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: COL offense succeeds (4+ goals)
- **Kirill Marchenko: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10TORCOL-TORECOWAN53-1|no; why: higher confidence-adjusted growth (3.18 vs 0.08 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0023 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: TOR offense succeeds (4+ goals)
- **Martin Necas: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10TORCOL-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (3.01 vs 1.03 bp); relationships: KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.19, COL shot control · high event (8+) · decided (2+) 0.16, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.14.
- thesis TOR:SUPPRESSED (p 0.4923): highest fidelity KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no (same contract)
- thesis COL:SUPPRESSED (p 0.2507): highest fidelity KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no (same contract)
- thesis COL:OFFENSE_4PLUS (p 0.5575): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT10TORCOL-COLZLHEUREUX68-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2507, phi -0.178)
- KXNHLGOAL-26OCT10TORCOL-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5575, phi -0.174)
- KXNHLAST-26OCT10TORCOL-TORKMARCHENKO86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.2851, phi -0.251)
- KXNHLGOAL-26OCT10TORCOL-COLMNECAS88-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5575, phi -0.225)

portfolios: A EV +1.27 (adj +0.67) on $11.76, P(profit) 0.4839, adj growth 6.4 bp · B EV +1.41 (adj +0.73) on $14.69, P(profit) 0.4839, adj growth 7.0 bp · C EV +0.74 (adj +0.28) on $9.95, P(profit) 0.4688, adj growth 2.7 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.8057, adj growth 1.9 bp

## TBL @ NYI  ·  10000 joint draws  ·  392 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.397 / away 0.603

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_TBL_win | p_overtime | goals | shots NYI/TBL | NYI/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.54 | 0.46 | 0.00 | 6.0 | 26.7/27.0 | 23.6/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.49 | 5.87 | 27.0/27.3 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.55 | 0.45 | 0.00 | 9.22 | 28.4/28.4 | 22.6/22.1 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.074 | 0.43 | 0.57 | 0.00 | 5.93 | 21.2/31.8 | 27.7/18.2 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.44 | 0.56 | 0.46 | 5.83 | 21.5/32.1 | 28.7/18.4 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.067 | 0.54 | 0.46 | 0.48 | 2.78 | 25.3/25.6 | 24.2/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden Schenn: 1+ goals YES | 19 | 0.268 | 0.247 | +0.067 | +0.046 | $3.98 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Ondrej Palat: 1+ goals YES | 9 | 0.137 | 0.125 | +0.041 | +0.029 | $2.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| John Carlson: 1+ assists NO | 54 | 0.727 | 0.599 | +0.170 | +0.042 | $5.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.176 | 0.165 | +0.038 | +0.027 | $2.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT10TBNYI-TB3|no; why: higher confidence-adjusted growth (28.50 vs 11.47 bp); despite a smaller raw edge (+0.067 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT10TBNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT10TBNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: NYI offense suppressed (<= 2 goals)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (28.50 vs 21.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10TBNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: NYI offense suppressed (<= 2 goals)
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT10TBNYI-TB3|no; why: higher confidence-adjusted growth (15.35 vs 11.47 bp); relationships: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT10TBNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT10TBNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: TBL offense succeeds (4+ goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes has the higher standalone adjusted growth (28.50 vs 12.97 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT10TBNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NYI:OFFENSE_4PLUS (p 0.3546): highest fidelity KXNHLTEAMTOTAL-26OCT10TBNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.4424): highest fidelity KXNHLSPREAD-26OCT10TBNYI-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.5144): highest fidelity KXNHLSPREAD-26OCT10TBNYI-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT10TBNYI-TB3|no (same contract)
- KXNHLGOAL-26OCT10TBNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4237, phi -0.259)
- KXNHLGOAL-26OCT10TBNYI-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4237, phi -0.173)
- KXNHLAST-26OCT10TBNYI-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 19.7 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3353, phi -0.231)
- KXNHLGOAL-26OCT10TBNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4237, phi -0.194)

portfolios: A EV +3.38 (adj +0.68) on $11.76, P(profit) 0.651, adj growth 6.4 bp · B EV +4.67 (adj +2.44) on $14.25, P(profit) 0.4796, adj growth 23.4 bp · C EV +4.56 (adj +1.91) on $19.43, P(profit) 0.7213, adj growth 18.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp
equivalent contracts collapsed: KXNHLGAME-26OCT10TBNYI-TB|no == KXNHLGAME-26OCT10TBNYI-NYI|yes

## ANA @ CGY  ·  10000 joint draws  ·  426 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.474 / away 0.526

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_ANA_win | p_overtime | goals | shots CGY/ANA | CGY/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.50 | 0.50 | 0.00 | 6.02 | 28.5/29.0 | 25.5/25.0 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.107 | 0.43 | 0.57 | 0.00 | 6.01 | 23.0/35.0 | 31.0/19.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.50 | 0.50 | 0.46 | 5.97 | 28.6/29.2 | 25.9/25.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.52 | 0.48 | 0.00 | 9.45 | 30.0/30.6 | 24.4/23.4 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.47 | 0.53 | 0.49 | 5.92 | 22.7/34.6 | 31.2/19.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.079 | 0.43 | 0.57 | 0.00 | 9.42 | 24.4/36.2 | 29.0/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| A.J. Greer: 1+ goals YES | 16 | 0.224 | 0.201 | +0.055 | +0.031 | $2.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 14 | 0.195 | 0.173 | +0.047 | +0.024 | $1.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Judd Caulfield: 1+ goals YES | 10 | 0.131 | 0.120 | +0.025 | +0.013 | $1.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Cutter Gauthier: 1+ goals NO | 59 | 0.634 | 0.622 | +0.027 | +0.015 | $2.86 | FUNDED_RESEARCH | $1 | ANA:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **A.J. Greer: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT10ANACGY-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (14.85 vs 0.47 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: ANA offense suppressed (<= 2 goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10ANACGY-CGYMFROST16-1|yes; why: higher confidence-adjusted growth (10.06 vs 0.52 bp); alternative not eligible: confidence-adjusted EV +0.0070 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: CGY offense suppressed (<= 2 goals)
- **Judd Caulfield: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes has the higher standalone adjusted growth (14.85 vs 4.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)
- **Cutter Gauthier: 1+ goals NO** — thesis: ANA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-1|no; why: Player prop expression KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no selected over player prop KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.82 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, ANA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.4242): highest fidelity KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes (same contract)
- thesis ANA:SUPPRESSED (p 0.3599): highest fidelity KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.4082): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT10ANACGY-ANAAGREER18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3599, phi -0.21)
- KXNHLGOAL-26OCT10ANACGY-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.3745, phi -0.184)
- KXNHLGOAL-26OCT10ANACGY-ANAJCAULFIELD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3599, phi -0.164)
- KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:OFFENSE_4PLUS (p 0.4242, phi -0.28)
- override: Player prop expression KXNHLGOAL-26OCT10ANACGY-ANACGAUTHIER61-1|no selected over player prop KXNHLAST-26OCT10ANACGY-ANALCARLSSON91-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.82 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.37 (adj +1.09) on $11.76, P(profit) 0.377, adj growth 10.4 bp · B EV +1.78 (adj +0.97) on $8.29, P(profit) 0.4573, adj growth 9.3 bp · C EV +1.24 (adj +0.70) on $7.17, P(profit) 0.2241, adj growth 6.7 bp · R EV +0.04 (adj +0.02) on $1.00, P(profit) 0.6342, adj growth 0.9 bp

## LAK @ VGK  ·  10000 joint draws  ·  412 bet sides mapped, 5 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.598 / away 0.402

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_LAK_win | p_overtime | goals | shots VGK/LAK | VGK/LAK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.62 | 0.38 | 0.00 | 5.95 | 27.3/27.1 | 24.1/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.53 | 0.47 | 0.46 | 5.94 | 27.7/27.5 | 24.2/24.4 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.096 | 0.70 | 0.30 | 0.00 | 5.99 | 32.4/21.4 | 18.9/27.9 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.58 | 0.42 | 0.45 | 5.88 | 32.7/22.0 | 19.0/29.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.64 | 0.36 | 0.00 | 9.2 | 28.9/28.7 | 23.7/22.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.63 | 0.37 | 0.00 | 3.44 | 26.1/25.9 | 24.5/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 68 | 0.751 | 0.732 | +0.056 | +0.036 | $5.79 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Artemi Panarin: 1+ assists NO | 50 | 0.642 | 0.546 | +0.124 | +0.029 | $4.62 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
| Tomas Hertl: 1+ goals NO | 70 | 0.738 | 0.727 | +0.023 | +0.013 | $3.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10LAVGK-VGKTHERTL48-1|no; why: higher confidence-adjusted growth (13.90 vs 1.72 bp); relationships: KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT10LAVGK-VGKTHERTL48-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: VGK offense succeeds (4+ goals)
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT10LAVGK-5|no; why: higher confidence-adjusted growth (7.28 vs 0.10 bp); wins across more scripts (relative breadth 0.978 vs 0.39); alternative not eligible: confidence-adjusted EV +0.0028 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT10LAVGK-VGKTHERTL48-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: LAK offense succeeds (4+ goals)
- **Tomas Hertl: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no; why: Player prop expression KXNHLGOAL-26OCT10LAVGK-VGKTHERTL48-1|no selected over player prop KXNHLAST-26OCT10LAVGK-VGKTHERTL48-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.86 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis VGK:SUPPRESSED (p 0.3662): highest fidelity KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no (same contract)
- thesis LAK:SUPPRESSED (p 0.4923): highest fidelity KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no (same contract)
- KXNHLGOAL-26OCT10LAVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4128, phi -0.235)
- KXNHLAST-26OCT10LAVGK-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.7 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.2867, phi -0.289)
- KXNHLGOAL-26OCT10LAVGK-VGKTHERTL48-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4128, phi -0.203)
- override: Player prop expression KXNHLGOAL-26OCT10LAVGK-VGKTHERTL48-1|no selected over player prop KXNHLAST-26OCT10LAVGK-VGKTHERTL48-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 0.86 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.53 (adj +0.50) on $11.76, P(profit) 0.5807, adj growth 4.9 bp · B EV +1.67 (adj +0.62) on $13.59, P(profit) 0.4841, adj growth 6.0 bp · C EV +2.07 (adj +0.74) on $13.80, P(profit) 0.4841, adj growth 7.2 bp · R EV +0.16 (adj +0.11) on $2.00, P(profit) 0.7507, adj growth 4.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
