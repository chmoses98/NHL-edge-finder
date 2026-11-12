# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-12T00:39:12Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +31.28 | +11.39 | +28.31 | 0.681 | -46.34 | -65.80 | 95.17 |
| B thesis-diversified (joint) ← optimiser card | 148.17 | +40.60 | +24.51 | +31.17 | 0.651 | -57.74 | -79.49 | 210.56 |
| C best expression per thesis | 103.52 | +22.00 | +11.11 | +18.04 | 0.628 | -44.62 | -59.88 | 96.53 |
| R FUNDED research stakes | 17.00 | +4.01 | +2.62 | +0.60 | 0.509 | -10.98 | -10.98 | 0.00 |

## PHI @ EDM  ·  10000 joint draws  ·  442 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.627 / away 0.372

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_PHI_win | p_overtime | goals | shots EDM/PHI | EDM/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.67 | 0.33 | 0.00 | 6.05 | 26.6/26.4 | 23.6/22.0 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.110 | 0.70 | 0.30 | 0.00 | 6.03 | 31.4/20.6 | 18.0/26.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.51 | 0.49 | 0.47 | 5.95 | 26.6/26.4 | 23.1/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.65 | 0.35 | 0.00 | 9.37 | 28.0/27.6 | 22.5/20.9 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.55 | 0.45 | 0.46 | 5.99 | 31.7/21.0 | 17.7/28.2 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.077 | 0.75 | 0.25 | 0.00 | 9.4 | 33.4/22.1 | 17.8/25.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sean Couturier: 1+ goals YES | 10 | 0.150 | 0.136 | +0.043 | +0.030 | $7.31 | FUNDED_RESEARCH | $2 | PHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 16 | 0.217 | 0.202 | +0.048 | +0.032 | $8.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 27 | 0.411 | 0.316 | +0.127 | +0.032 | $10.28 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.67) | EVIDENCE_MIXED | D |
| Vasily Podkolzin: 1+ assists YES | 27 | 0.349 | 0.307 | +0.065 | +0.023 | $8.63 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11PHIEDM-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (19.77 vs 15.73 bp); despite a smaller raw edge (+0.043 vs +0.048/contract); relationships: KXNHLGOAL-26NOV11PHIEDM-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26NOV11PHIEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26NOV11PHIEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11PHIEDM-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV11PHIEDM-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (19.77 vs 15.73 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26NOV11PHIEDM-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLAST-26NOV11PHIEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26NOV11PHIEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: PHI offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV11PHIEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (11.09 vs 2.74 bp); relationships: KXNHLGOAL-26NOV11PHIEDM-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV11PHIEDM-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26NOV11PHIEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.099); failure: EDM offense succeeds (4+ goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV11PHIEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (5.79 vs 4.50 bp); relationships: KXNHLGOAL-26NOV11PHIEDM-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV11PHIEDM-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26NOV11PHIEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.099); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, EDM shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PHI:OFFENSE_4PLUS (p 0.3254): highest fidelity KXNHLGOAL-26NOV11PHIEDM-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV11PHIEDM-PHICDVORAK22-1|yes (same contract)
- thesis EDM:SUPPRESSED (p 0.2936): highest fidelity KXNHLAST-26NOV11PHIEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV11PHIEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.502): highest fidelity KXNHLAST-26NOV11PHIEDM-EDMVPODKOLZIN92-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV11PHIEDM-EDMVPODKOLZIN92-1|yes (same contract)
- KXNHLGOAL-26NOV11PHIEDM-PHISCOUTURIER14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4548, phi -0.202)
- KXNHLGOAL-26NOV11PHIEDM-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4548, phi -0.224)
- KXNHLAST-26NOV11PHIEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 33% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.6 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.502, phi -0.329)
- KXNHLAST-26NOV11PHIEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2936, phi -0.263)

portfolios: A EV +10.08 (adj +2.78) on $37.50, P(profit) 0.6537, adj growth 23.7 bp · B EV +12.06 (adj +5.59) on $35.07, P(profit) 0.6057, adj growth 48.3 bp · C EV +9.63 (adj +3.95) on $26.26, P(profit) 0.6927, adj growth 34.1 bp · R EV +0.82 (adj +0.56) on $2.00, P(profit) 0.1497, adj growth 18.9 bp

## UTA @ VGK  ·  10000 joint draws  ·  466 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.538 / away 0.462

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_UTA_win | p_overtime | goals | shots VGK/UTA | VGK/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.58 | 0.42 | 0.00 | 6.03 | 27.2/27.1 | 24.0/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.53 | 0.47 | 0.45 | 5.93 | 27.2/27.0 | 23.7/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.61 | 0.39 | 0.00 | 9.39 | 28.6/28.6 | 23.1/21.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.081 | 0.64 | 0.36 | 0.00 | 6.04 | 32.0/21.5 | 18.7/27.8 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.53 | 0.47 | 0.46 | 5.87 | 31.9/21.6 | 18.5/28.7 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.062 | 0.56 | 0.44 | 0.00 | 6.01 | 22.1/32.3 | 28.9/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 4 | 0.084 | 0.071 | +0.041 | +0.029 | $5.81 | FUNDED_RESEARCH | $2 | VGK:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Jack McBain: 1+ goals YES | 9 | 0.151 | 0.135 | +0.055 | +0.039 | $9.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 16 | 0.220 | 0.204 | +0.050 | +0.034 | $9.32 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ goals YES | 17 | 0.223 | 0.207 | +0.043 | +0.028 | $7.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (41.22 vs 11.14 bp); despite a smaller raw edge (+0.041 vs +0.043/contract); relationships: KXNHLGOAL-26NOV11UTAVGK-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: VGK offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (36.58 vs 17.84 bp); relationships: KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: UTA offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV11UTAVGK-UTAMWEEGAR52-1|yes; why: higher confidence-adjusted growth (17.84 vs 3.74 bp); despite a smaller raw edge (+0.050 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV11UTAVGK-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: UTA offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11UTAVGK-VGKBHOWDEN21-1|yes; why: higher confidence-adjusted growth (11.14 vs 6.45 bp); relationships: KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV11UTAVGK-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis UTA:OFFENSE_4PLUS (p 0.3475): highest fidelity KXNHLAST-26NOV11UTAVGK-UTAMWEEGAR52-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:OFFENSE_4PLUS (p 0.4491): highest fidelity KXNHLAST-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3419, phi -0.135)
- KXNHLGOAL-26NOV11UTAVGK-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4274, phi -0.182)
- KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4274, phi -0.246)
- KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3419, phi -0.194)

portfolios: A EV +10.07 (adj +4.90) on $37.50, P(profit) 0.4084, adj growth 40.7 bp · B EV +15.60 (adj +10.76) on $32.29, P(profit) 0.5294, adj growth 90.9 bp · C EV +4.75 (adj +3.14) on $17.47, P(profit) 0.395, adj growth 27.1 bp · R EV +1.92 (adj +1.35) on $2.00, P(profit) 0.0836, adj growth 41.7 bp

## NSH @ ANA  ·  10000 joint draws  ·  474 bet sides mapped, 23 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.562 / away 0.438

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_NSH_win | p_overtime | goals | shots ANA/NSH | ANA/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.117 | 0.74 | 0.26 | 0.00 | 9.46 | 30.0/29.4 | 24.6/22.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.71 | 0.29 | 0.00 | 6.13 | 28.3/28.0 | 25.4/23.6 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.111 | 0.79 | 0.21 | 0.00 | 6.06 | 33.9/22.0 | 19.8/28.5 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.109 | 0.81 | 0.19 | 0.00 | 9.4 | 35.6/23.5 | 19.5/26.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.090 | 0.58 | 0.42 | 0.47 | 5.98 | 34.3/22.2 | 19.0/30.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.51 | 0.49 | 0.46 | 6.04 | 28.3/27.8 | 24.5/25.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tim Washe: 1+ goals YES | 10 | 0.160 | 0.144 | +0.053 | +0.037 | $8.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Beckett Sennecke: 1+ goals YES | 33 | 0.413 | 0.391 | +0.067 | +0.045 | $14.93 | FUNDED_RESEARCH | $4 | ANA:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Jackson LaCombe: 1+ goals YES | 12 | 0.171 | 0.157 | +0.043 | +0.029 | $6.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Steven Stamkos: 1+ goals NO | 62 | 0.689 | 0.671 | +0.053 | +0.034 | $19.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Tim Washe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes; why: higher confidence-adjusted growth (30.92 vs 19.84 bp); despite a smaller raw edge (+0.053 vs +0.067/contract); relationships: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV11NSHANA-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: ANA offense suppressed (<= 2 goals)
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11NSHANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (19.84 vs 18.28 bp); relationships: KXNHLGOAL-26NOV11NSHANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV11NSHANA-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.031); failure: ANA offense suppressed (<= 2 goals)
- **Jackson LaCombe: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes has the higher standalone adjusted growth (19.84 vs 16.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV11NSHANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: ANA offense suppressed (<= 2 goals)
- **Steven Stamkos: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV11NSHANA-ANA2|yes; why: higher confidence-adjusted growth (11.04 vs 7.22 bp); despite a smaller raw edge (+0.053 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.01 vs 0.511); relationships: KXNHLGOAL-26NOV11NSHANA-ANATWASHE42-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.031); KXNHLGOAL-26NOV11NSHANA-ANAJLACOMBE2-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.5711): highest fidelity KXNHLSPREAD-26NOV11NSHANA-NSH3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:SUPPRESSED (p 0.4555): highest fidelity KXNHLSPREAD-26NOV11NSHANA-NSH3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS_BY_2PLUS (p 0.453): highest fidelity KXNHLSPREAD-26NOV11NSHANA-ANA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV11NSHANA-ANA2|yes (same contract)
- KXNHLGOAL-26NOV11NSHANA-ANATWASHE42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2432, phi -0.159)
- KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2432, phi -0.24)
- KXNHLGOAL-26NOV11NSHANA-ANAJLACOMBE2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2432, phi -0.155)
- KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3175, phi -0.253)

portfolios: A EV +6.42 (adj +2.49) on $37.50, P(profit) 0.5812, adj growth 21.1 bp · B EV +10.96 (adj +7.45) on $49.16, P(profit) 0.5067, adj growth 65.1 bp · C EV +5.61 (adj +3.43) on $40.05, P(profit) 0.5836, adj growth 30.2 bp · R EV +0.78 (adj +0.53) on $4.00, P(profit) 0.4129, adj growth 18.4 bp

## PIT @ SJS  ·  10000 joint draws  ·  464 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.428 / away 0.572

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_PIT_win | p_overtime | goals | shots SJS/PIT | SJS/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.49 | 0.51 | 0.00 | 6.03 | 27.4/27.6 | 23.8/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.48 | 0.52 | 0.47 | 5.95 | 27.7/28.0 | 24.6/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.49 | 0.51 | 0.00 | 9.37 | 29.2/29.3 | 22.9/23.0 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.077 | 0.39 | 0.61 | 0.00 | 6.06 | 22.0/32.5 | 28.2/19.1 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.47 | 0.53 | 0.46 | 5.91 | 22.3/33.1 | 29.6/19.1 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.057 | 0.43 | 0.57 | 0.00 | 9.23 | 23.3/34.7 | 27.9/18.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Erik Karlsson: 1+ goals NO | 82 | 0.855 | 0.845 | +0.025 | +0.015 | $20.00 | FUNDED_RESEARCH | $5 | PIT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_STRONGER | D |
| Pittsburgh over 3.5 goals scored NO | 50 | 0.569 | 0.532 | +0.051 | +0.015 | $4.32 | FUNDED_RESEARCH | $2 | PIT:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pittsburgh wins by over 1.5 goals NO | 64 | 0.703 | 0.669 | +0.047 | +0.013 | $4.02 | FUNDED_RESEARCH | $2 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tyler Toffoli: 1+ assists YES | 24 | 0.304 | 0.264 | +0.051 | +0.012 | $3.30 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
- **Erik Karlsson: 1+ goals NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no; why: KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no has the higher standalone adjusted growth (3.85 vs 3.47 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.123); relationships: KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: REINFORCING (phi 0.176); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PIT offense succeeds (4+ goals)
- **Pittsburgh over 3.5 goals scored NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no; why: Broad expression KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no selected over player prop KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: REINFORCING (phi 0.176); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: REINFORCING (phi 0.531); KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PIT offense succeeds (4+ goals)
- **Pittsburgh wins by over 1.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no has the higher standalone adjusted growth (1.84 vs 1.60 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.531); they share one thesis budget; relationships: KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: REINFORCING (phi 0.531); KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes: MOSTLY_INDEPENDENT (phi 0.143); failure: PIT wins by 2+
- **Tyler Toffoli: 1+ assists YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV11PITSJ-PIT2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV11PITSJ-PIT2|no has the higher standalone adjusted growth (1.60 vs 1.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.143); they share one thesis budget; relationships: KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: MOSTLY_INDEPENDENT (phi 0.143); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:SUPPRESSED (p 0.3636): highest fidelity KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no — Broad expression KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no selected over player prop KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis SJS:WINS (p 0.4876): highest fidelity KXNHLSPREAD-26NOV11PITSJ-PIT2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:OFFENSE_4PLUS (p 0.4037): highest fidelity KXNHLSPREAD-26NOV11PITSJ-PIT2|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV11PITSJ-PIT2|no (same contract)
- KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4203, phi -0.175)
- KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4203, phi -0.978)
- KXNHLSPREAD-26NOV11PITSJ-PIT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:WINS_BY_2PLUS (p 0.2971, phi -1.0)
- KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3833, phi -0.236)
- override: Broad expression KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no selected over player prop KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.71 (adj +1.22) on $37.50, P(profit) 0.4865, adj growth 9.6 bp · B EV +1.99 (adj +0.71) on $31.65, P(profit) 0.6194, adj growth 6.3 bp · C EV +2.01 (adj +0.59) on $19.74, P(profit) 0.5325, adj growth 5.2 bp · R EV +0.49 (adj +0.18) on $9.00, P(profit) 0.6624, adj growth 6.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
