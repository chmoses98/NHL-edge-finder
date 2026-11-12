# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-12T02:00:34Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +30.45 | +13.52 | +23.60 | 0.623 | -62.00 | -86.50 | 106.45 |
| B thesis-diversified (joint) ← optimiser card | 123.61 | +22.72 | +14.21 | +9.97 | 0.557 | -44.72 | -55.49 | 122.15 |
| C best expression per thesis | 102.68 | +15.93 | +8.17 | +14.13 | 0.610 | -38.91 | -56.17 | 71.40 |
| R FUNDED research stakes | 17.00 | +3.10 | +1.97 | -1.39 | 0.417 | -7.41 | -10.46 | 0.00 |

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
| Lawson Crouse: 1+ goals YES | 16 | 0.220 | 0.204 | +0.050 | +0.034 | $9.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ goals YES | 17 | 0.223 | 0.209 | +0.043 | +0.029 | $8.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (41.22 vs 12.16 bp); despite a smaller raw edge (+0.041 vs +0.043/contract); relationships: KXNHLGOAL-26NOV11UTAVGK-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: VGK offense suppressed (<= 2 goals)
- **Jack McBain: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (36.58 vs 17.84 bp); relationships: KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: UTA offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLAST-26NOV11UTAVGK-UTAMWEEGAR52-1|yes; why: higher confidence-adjusted growth (17.84 vs 3.74 bp); despite a smaller raw edge (+0.050 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV11UTAVGK-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: UTA offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11UTAVGK-VGKBHOWDEN21-1|yes; why: higher confidence-adjusted growth (12.16 vs 6.45 bp); relationships: KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV11UTAVGK-UTAJMCBAIN22-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis UTA:OFFENSE_4PLUS (p 0.3475): highest fidelity KXNHLAST-26NOV11UTAVGK-UTAMWEEGAR52-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:OFFENSE_4PLUS (p 0.4491): highest fidelity KXNHLAST-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV11UTAVGK-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3419, phi -0.135)
- KXNHLGOAL-26NOV11UTAVGK-UTAJMCBAIN22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4274, phi -0.182)
- KXNHLGOAL-26NOV11UTAVGK-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.4274, phi -0.246)
- KXNHLGOAL-26NOV11UTAVGK-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3419, phi -0.194)

portfolios: A EV +14.92 (adj +8.30) on $50.00, P(profit) 0.4166, adj growth 64.9 bp · B EV +15.69 (adj +10.88) on $32.67, P(profit) 0.5294, adj growth 91.9 bp · C EV +4.85 (adj +3.26) on $17.86, P(profit) 0.395, adj growth 28.1 bp · R EV +1.92 (adj +1.35) on $2.00, P(profit) 0.0836, adj growth 41.7 bp

## NSH @ ANA  ·  10000 joint draws  ·  474 bet sides mapped, 27 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.564 / away 0.436

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
| Beckett Sennecke: 1+ goals YES | 33 | 0.413 | 0.391 | +0.067 | +0.045 | $10.44 | FUNDED_RESEARCH | $3 | ANA:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Steven Stamkos: 1+ goals NO | 62 | 0.689 | 0.671 | +0.053 | +0.034 | $14.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Nashville wins by over 2.5 goals NO | 86 | 0.912 | 0.884 | +0.044 | +0.015 | $14.51 | FUNDED_RESEARCH | $4 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mavrik Bourque: 1+ goals NO | 78 | 0.816 | 0.806 | +0.024 | +0.014 | $10.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV11NSHANA-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (19.84 vs 10.75 bp); relationships: KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.031); KXNHLSPREAD-26NOV11NSHANA-NSH3|no: MOSTLY_INDEPENDENT (phi 0.128); KXNHLGOAL-26NOV11NSHANA-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: ANA offense suppressed (<= 2 goals)
- **Steven Stamkos: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV11NSHANA-NSH2|no; why: higher confidence-adjusted growth (11.04 vs 6.45 bp); despite a smaller raw edge (+0.053 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.031); KXNHLSPREAD-26NOV11NSHANA-NSH3|no: MOSTLY_INDEPENDENT (phi 0.139); KXNHLGOAL-26NOV11NSHANA-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: NSH offense succeeds (4+ goals)
- **Nashville wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV11NSHANA-NSH2|no; why: Broad expression KXNHLSPREAD-26NOV11NSHANA-NSH3|no selected over player prop KXNHLAST-26NOV11NSHANA-NSHROREILLY90-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.77 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.128); KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.139); KXNHLGOAL-26NOV11NSHANA-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi 0.091); failure: NSH wins by 2+
- **Mavrik Bourque: 1+ goals NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no; why: Player prop expression KXNHLGOAL-26NOV11NSHANA-NSHMBOURQUE22-1|no selected over broad KXNHLTEAMTOTAL-26NOV11NSHANA-NSH4|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.91 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLSPREAD-26NOV11NSHANA-NSH3|no: MOSTLY_INDEPENDENT (phi 0.091); failure: NSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · decided (2+) 0.11.
- thesis ANA:OFFENSE_4PLUS (p 0.5711): highest fidelity KXNHLSPREAD-26NOV11NSHANA-NSH3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NSH:SUPPRESSED (p 0.4555): highest fidelity KXNHLTEAMTOTAL-26NOV11NSHANA-NSH4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no — Player prop expression KXNHLGOAL-26NOV11NSHANA-NSHMBOURQUE22-1|no selected over broad KXNHLTEAMTOTAL-26NOV11NSHANA-NSH4|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.91 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis ANA:WINS (p 0.6661): highest fidelity KXNHLSPREAD-26NOV11NSHANA-NSH2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV11NSHANA-ANA3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV11NSHANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2432, phi -0.24)
- KXNHLGOAL-26NOV11NSHANA-NSHSSTAMKOS91-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3175, phi -0.253)
- KXNHLSPREAD-26NOV11NSHANA-NSH3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NSH:WINS_BY_2PLUS (p 0.1556, phi -0.723)
- KXNHLGOAL-26NOV11NSHANA-NSHMBOURQUE22-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3175, phi -0.198)
- override: Player prop expression KXNHLGOAL-26NOV11NSHANA-NSHMBOURQUE22-1|no selected over broad KXNHLTEAMTOTAL-26NOV11NSHANA-NSH4|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.91 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLSPREAD-26NOV11NSHANA-NSH3|no selected over player prop KXNHLAST-26NOV11NSHANA-NSHROREILLY90-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.77 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +8.16 (adj +3.12) on $50.00, P(profit) 0.5812, adj growth 24.7 bp · B EV +4.29 (adj +2.59) on $50.00, P(profit) 0.6872, adj growth 23.7 bp · C EV +6.11 (adj +3.50) on $50.00, P(profit) 0.4498, adj growth 30.9 bp · R EV +0.79 (adj +0.46) on $7.00, P(profit) 0.4129, adj growth 16.9 bp

## PIT @ SJS  ·  10000 joint draws  ·  464 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.429 / away 0.571

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
| Pittsburgh over 3.5 goals scored NO | 50 | 0.569 | 0.532 | +0.051 | +0.015 | $3.12 | FUNDED_RESEARCH | $1 | PIT:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Pittsburgh wins by over 1.5 goals NO | 64 | 0.703 | 0.669 | +0.047 | +0.013 | $7.33 | FUNDED_RESEARCH | $2 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Alexander Wennberg: 1+ assists NO | 67 | 0.771 | 0.696 | +0.085 | +0.010 | $10.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Erik Karlsson: 1+ goals NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no; why: KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no has the higher standalone adjusted growth (4.84 vs 3.47 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.123); relationships: KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: REINFORCING (phi 0.176); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLAST-26NOV11PITSJ-SJAWENNBERG21-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: PIT offense succeeds (4+ goals)
- **Pittsburgh over 3.5 goals scored NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no; why: Broad expression KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no selected over player prop KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: REINFORCING (phi 0.176); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: REINFORCING (phi 0.531); KXNHLAST-26NOV11PITSJ-SJAWENNBERG21-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: PIT offense succeeds (4+ goals)
- **Pittsburgh wins by over 1.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no; why: Broad expression KXNHLSPREAD-26NOV11PITSJ-PIT2|no selected over player prop KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.94 vs 0.44 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: REINFORCING (phi 0.531); KXNHLAST-26NOV11PITSJ-SJAWENNBERG21-1|no: INTENTIONAL_DIVERSIFIER (phi -0.131); failure: PIT wins by 2+
- **Alexander Wennberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26NOV11PITSJ-4|no; why: wins across more scripts (relative breadth 1.007 vs 0.38); alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26NOV11PITSJ-PIT2|no: INTENTIONAL_DIVERSIFIER (phi -0.131); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4037): highest fidelity KXNHLSPREAD-26NOV11PITSJ-PIT2|no [DIRECT], best adjusted EV KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes — Broad expression KXNHLSPREAD-26NOV11PITSJ-PIT2|no selected over player prop KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.94 vs 0.44 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis PIT:SUPPRESSED (p 0.3636): highest fidelity KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no — Broad expression KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no selected over player prop KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis SJS:WINS (p 0.4876): highest fidelity KXNHLSPREAD-26NOV11PITSJ-PIT2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV11PITSJ-PITEKARLSSON65-1|no: FUNDED_RESEARCH; family TRUSTED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4203, phi -0.175)
- KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4203, phi -0.978)
- KXNHLSPREAD-26NOV11PITSJ-PIT2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:WINS_BY_2PLUS (p 0.2971, phi -1.0)
- KXNHLAST-26NOV11PITSJ-SJAWENNBERG21-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.6 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4037, phi -0.221)
- override: Broad expression KXNHLTEAMTOTAL-26NOV11PITSJ-PIT4|no selected over player prop KXNHLAST-26NOV11PITSJ-PITEMALKIN71-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26NOV11PITSJ-PIT2|no selected over player prop KXNHLAST-26NOV11PITSJ-SJTTOFFOLI73-1|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.94 vs 0.44 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +7.38 (adj +2.10) on $50.00, P(profit) 0.5315, adj growth 16.8 bp · B EV +2.74 (adj +0.74) on $40.94, P(profit) 0.6164, adj growth 6.5 bp · C EV +4.98 (adj +1.41) on $34.82, P(profit) 0.6458, adj growth 12.4 bp · R EV +0.39 (adj +0.16) on $8.00, P(profit) 0.6193, adj growth 5.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
