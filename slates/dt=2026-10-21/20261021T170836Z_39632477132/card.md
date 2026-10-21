# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-21T17:08:36Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +12.87 | +3.43 | +16.93 | 0.611 | -36.49 | -47.61 | 27.41 |
| B thesis-diversified (joint) ← optimiser card | 72.66 | +6.39 | +3.23 | +7.68 | 0.628 | -27.30 | -38.75 | 28.63 |
| C best expression per thesis | 67.65 | +8.29 | +3.11 | +9.85 | 0.607 | -28.41 | -37.62 | 27.65 |
| R FUNDED research stakes | 17.00 | +1.22 | +0.54 | +0.73 | 0.600 | -7.33 | -10.09 | 0.00 |

## PHI @ BUF  ·  10000 joint draws  ·  518 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.629 / away 0.371

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_PHI_win | p_overtime | goals | shots BUF/PHI | BUF/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.120 | 0.66 | 0.34 | 0.00 | 5.99 | 32.6/20.8 | 18.1/28.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.59 | 0.41 | 0.00 | 6.01 | 27.0/26.6 | 23.4/23.1 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.49 | 5.88 | 32.3/21.0 | 17.8/28.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.53 | 0.47 | 0.47 | 5.88 | 27.0/26.6 | 23.5/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.58 | 0.42 | 0.00 | 9.24 | 28.6/28.1 | 22.5/21.8 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.066 | 0.65 | 0.35 | 0.00 | 9.19 | 34.0/22.4 | 17.7/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jiri Kulich: 1+ goals YES | 18 | 0.218 | 0.207 | +0.028 | +0.017 | $6.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 61 | 0.656 | 0.642 | +0.030 | +0.016 | $7.35 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 1.5 goals NO | 60 | 0.669 | 0.632 | +0.052 | +0.015 | $8.24 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo over 3.5 goals scored NO | 52 | 0.588 | 0.552 | +0.051 | +0.014 | $5.32 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT21PHIBUF-BUFJNORRIS9-1|yes; why: higher confidence-adjusted growth (4.14 vs 0.00 bp); alternative not eligible: confidence-adjusted EV +0.0005 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: INTENTIONAL_DIVERSIFIER (phi -0.183); KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: INTENTIONAL_DIVERSIFIER (phi -0.224); failure: BUF offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no; why: Player prop expression KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.82 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT21PHIBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: REINFORCING (phi 0.189); KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: REINFORCING (phi 0.256); failure: BUF offense succeeds (4+ goals)
- **Buffalo wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no; why: Broad expression KXNHLSPREAD-26OCT21PHIBUF-BUF2|no selected over player prop KXNHLAST-26OCT21PHIBUF-PHIDBARKEY86-1|yes because adjusted EV differs by only 0.0 pts while thesis capture is 0.94 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT21PHIBUF-BUFJKULICH20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.183); KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.189); KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: REINFORCING (phi 0.553); failure: BUF wins by 2+
- **Buffalo over 3.5 goals scored NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no; why: Broad expression KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFTTHOMPSON72-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT21PHIBUF-BUFJKULICH20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.224); KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.256); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: REINFORCING (phi 0.553); failure: BUF offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BUF:SUPPRESSED (p 0.3786): highest fidelity KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no — Player prop expression KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.82 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis BUF:OFFENSE_4PLUS (p 0.4027): highest fidelity KXNHLGOAL-26OCT21PHIBUF-BUFJKULICH20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT21PHIBUF-BUFJKULICH20-1|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3051): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF3|no [DIRECT], best adjusted EV KXNHLAST-26OCT21PHIBUF-PHIDBARKEY86-1|yes — Broad expression KXNHLSPREAD-26OCT21PHIBUF-BUF2|no selected over player prop KXNHLAST-26OCT21PHIBUF-PHIDBARKEY86-1|yes because adjusted EV differs by only 0.0 pts while thesis capture is 0.94 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT21PHIBUF-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3786, phi -0.214)
- KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4027, phi -0.261)
- KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3313, phi -1.0)
- KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4027, phi -0.981)
- override: Player prop expression KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 0.82 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFTTHOMPSON72-1|no because adjusted EV differs by only 0.1 pts while thesis capture is 1.00 vs 0.81 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26OCT21PHIBUF-BUF2|no selected over player prop KXNHLAST-26OCT21PHIBUF-PHIDBARKEY86-1|yes because adjusted EV differs by only 0.0 pts while thesis capture is 0.94 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +7.42 (adj +1.95) on $50.00, P(profit) 0.5157, adj growth 14.7 bp · B EV +2.44 (adj +1.07) on $27.01, P(profit) 0.5632, adj growth 9.4 bp · C EV +5.38 (adj +1.64) on $31.80, P(profit) 0.6357, adj growth 14.4 bp · R EV +0.54 (adj +0.18) on $7.00, P(profit) 0.6014, adj growth 5.6 bp

## FLA @ OTT  ·  10000 joint draws  ·  432 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_FLA_win | p_overtime | goals | shots OTT/FLA | OTT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.62 | 0.38 | 0.00 | 6.0 | 26.3/26.1 | 23.2/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.46 | 5.92 | 26.9/26.7 | 23.5/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.65 | 0.35 | 0.00 | 9.23 | 28.1/27.9 | 22.7/21.4 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.087 | 0.68 | 0.32 | 0.00 | 5.96 | 31.4/20.9 | 18.4/27.0 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.58 | 0.42 | 0.46 | 5.86 | 31.6/21.1 | 17.9/28.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.058 | 0.50 | 0.50 | 0.48 | 2.8 | 25.0/24.8 | 23.3/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 65 | 0.722 | 0.702 | +0.057 | +0.036 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 9 | 0.117 | 0.109 | +0.021 | +0.013 | $3.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 83 | 0.884 | 0.855 | +0.044 | +0.015 | $18.63 | FUNDED_RESEARCH | $5 | OTT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ridly Greig: 1+ goals YES | 16 | 0.195 | 0.184 | +0.026 | +0.015 | $3.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: higher confidence-adjusted growth (12.74 vs 3.81 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: MOSTLY_INDEPENDENT (phi 0.12); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: FLA offense succeeds (4+ goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: higher confidence-adjusted growth (4.14 vs 3.81 bp); despite a smaller raw edge (+0.021 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: MOSTLY_INDEPENDENT (phi 0.088); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: OTT offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: OTT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no has the higher standalone adjusted growth (3.81 vs 3.56 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.702); relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.12); KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.088); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.09); failure: FLA wins by 2+
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no has the higher standalone adjusted growth (3.81 vs 3.31 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.112); relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: MOSTLY_INDEPENDENT (phi 0.09); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4671): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.424): highest fidelity KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21FLAOTT-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:WINS (p 0.5829): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21FLAOTT-FLA2|no (same contract)
- KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3092, phi -0.232)
- KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3486, phi -0.142)
- KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.21, phi -0.702)
- KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3486, phi -0.195)

portfolios: A EV +5.45 (adj +1.48) on $50.00, P(profit) 0.7231, adj growth 12.7 bp · B EV +3.95 (adj +2.16) on $45.65, P(profit) 0.6934, adj growth 19.2 bp · C EV +2.90 (adj +1.47) on $35.85, P(profit) 0.5942, adj growth 13.3 bp · R EV +0.69 (adj +0.36) on $10.00, P(profit) 0.6559, adj growth 12.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
