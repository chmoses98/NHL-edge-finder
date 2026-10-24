# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-23T23:59:57Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +15.16 | +4.15 | +16.55 | 0.618 | -37.18 | -48.60 | 32.24 |
| B thesis-diversified (joint) ← optimiser card | 59.11 | +7.23 | +3.09 | +2.24 | 0.595 | -23.87 | -28.01 | 26.48 |
| C best expression per thesis | 64.62 | +6.61 | +1.93 | +6.72 | 0.616 | -21.07 | -30.18 | 16.90 |
| R FUNDED research stakes | 11.00 | +0.93 | +0.32 | +0.89 | 0.503 | -5.76 | -7.76 | 0.00 |

## MTL @ CHI  ·  10000 joint draws  ·  440 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.407 / away 0.593

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_MTL_win | p_overtime | goals | shots CHI/MTL | CHI/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.50 | 0.50 | 0.00 | 6.0 | 26.6/26.8 | 23.3/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.48 | 0.52 | 0.47 | 5.93 | 26.9/27.1 | 23.9/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.47 | 0.53 | 0.00 | 9.31 | 28.2/28.7 | 22.4/22.4 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.087 | 0.41 | 0.59 | 0.00 | 5.99 | 21.2/31.9 | 27.6/18.1 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.48 | 0.52 | 0.48 | 5.9 | 21.6/32.2 | 29.0/18.4 | even strength |
| MTL shot control · high event (8+) · decided (2+) | 0.058 | 0.36 | 0.64 | 0.00 | 9.28 | 22.5/33.5 | 26.3/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anton Frondell: 1+ goals YES | 21 | 0.250 | 0.237 | +0.028 | +0.016 | $4.86 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 58 | 0.686 | 0.614 | +0.089 | +0.017 | $14.03 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.84) | EVIDENCE_MIXED | D |
| Montreal wins by over 2.5 goals NO | 75 | 0.810 | 0.778 | +0.047 | +0.015 | $15.84 | FUNDED_RESEARCH | $4 | CHI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Montreal over 3.5 goals scored NO | 52 | 0.587 | 0.551 | +0.050 | +0.013 | $2.88 | FUNDED_RESEARCH | $1 | MTL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23MTLCHI-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (3.18 vs 3.17 bp); relationships: KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.081); KXNHLSPREAD-26OCT23MTLCHI-MTL3|no: MOSTLY_INDEPENDENT (phi 0.116); KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL4|no: MOSTLY_INDEPENDENT (phi 0.0); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT23MTLCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (2.58 vs 1.11 bp); relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.081); KXNHLSPREAD-26OCT23MTLCHI-MTL3|no: INTENTIONAL_DIVERSIFIER (phi -0.154); KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL4|no: MOSTLY_INDEPENDENT (phi -0.002); failure: CHI offense succeeds (4+ goals)
- **Montreal wins by over 2.5 goals NO** — thesis: CHI wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT23MTLCHI-MTL2|no; why: Broad expression KXNHLSPREAD-26OCT23MTLCHI-MTL3|no selected over player prop KXNHLAST-26OCT23MTLCHI-MTLCKREIDER22-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.88 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.116); KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.154); KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL4|no: DUPLICATIVE (phi 0.496); failure: MTL wins by 2+
- **Montreal over 3.5 goals scored NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no; why: Broad expression KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL4|no selected over player prop KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.82 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLSPREAD-26OCT23MTLCHI-MTL3|no: DUPLICATIVE (phi 0.496); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MTL:SUPPRESSED (p 0.3821): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no — Broad expression KXNHLSPREAD-26OCT23MTLCHI-MTL3|no selected over player prop KXNHLAST-26OCT23MTLCHI-MTLCKREIDER22-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.88 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis CHI:OFFENSE_4PLUS (p 0.3786): highest fidelity KXNHLSPREAD-26OCT23MTLCHI-MTL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.405): highest fidelity KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26OCT23MTLCHI-CHIAFRONDELL16-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.405, phi -0.214)
- KXNHLAST-26OCT23MTLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 16% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.1 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3786, phi -0.256)
- KXNHLSPREAD-26OCT23MTLCHI-MTL3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:WINS_BY_2PLUS (p 0.3006, phi -0.738)
- KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4027, phi -0.979)
- override: Broad expression KXNHLSPREAD-26OCT23MTLCHI-MTL3|no selected over player prop KXNHLAST-26OCT23MTLCHI-MTLCKREIDER22-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 1.00 vs 0.88 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLTEAMTOTAL-26OCT23MTLCHI-MTL4|no selected over player prop KXNHLAST-26OCT23MTLCHI-MTLCCAUFIELD13-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 1.00 vs 0.82 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.22 (adj +1.26) on $50.00, P(profit) 0.6391, adj growth 10.0 bp · B EV +3.96 (adj +1.12) on $37.60, P(profit) 0.6373, adj growth 9.8 bp · C EV +5.06 (adj +1.46) on $46.23, P(profit) 0.483, adj growth 12.8 bp · R EV +0.60 (adj +0.24) on $7.00, P(profit) 0.6745, adj growth 7.9 bp

## TBL @ COL  ·  10000 joint draws  ·  430 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.526 / away 0.474

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_TBL_win | p_overtime | goals | shots COL/TBL | COL/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.64 | 0.36 | 0.00 | 6.03 | 28.2/27.8 | 24.8/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.48 | 5.9 | 28.2/27.8 | 24.6/25.0 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.100 | 0.63 | 0.37 | 0.00 | 5.96 | 33.5/22.0 | 19.3/29.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.60 | 0.40 | 0.00 | 9.3 | 29.8/29.4 | 23.7/23.0 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.55 | 0.45 | 0.47 | 5.88 | 33.4/22.3 | 19.2/30.1 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.068 | 0.70 | 0.30 | 0.00 | 9.17 | 34.3/23.4 | 18.8/26.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Josh Manson: 1+ goals YES | 4 | 0.062 | 0.059 | +0.019 | +0.016 | $3.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ goals YES | 27 | 0.307 | 0.297 | +0.023 | +0.013 | $4.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Andrei Vasilevskiy: 28+ saves NO | 57 | 0.645 | 0.600 | +0.058 | +0.013 | $6.90 | FUNDED_RESEARCH | $2 | TBL:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 3.5 goals scored NO | 60 | 0.660 | 0.627 | +0.043 | +0.011 | $6.39 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Josh Manson: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes; why: higher confidence-adjusted growth (13.66 vs 1.77 bp); despite a smaller raw edge (+0.019 vs +0.023/contract); relationships: KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no: MOSTLY_INDEPENDENT (phi 0.027); KXNHLTEAMTOTAL-26OCT23TBCOL-TB4|no: MOSTLY_INDEPENDENT (phi 0.015); failure: COL offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ goals YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT23TBCOL-TB3|no; why: higher confidence-adjusted growth (1.77 vs 1.15 bp); despite a smaller raw edge (+0.023 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no: MOSTLY_INDEPENDENT (phi 0.039); KXNHLTEAMTOTAL-26OCT23TBCOL-TB4|no: MOSTLY_INDEPENDENT (phi 0.009); failure: COL offense suppressed (<= 2 goals)
- **Andrei Vasilevskiy: 28+ saves NO** — thesis: TBL net faces light volume (<= 25 shots; COL suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLTEAMTOTAL-26OCT23TBCOL-TB4|no: MOSTLY_INDEPENDENT (phi 0.047); failure: TBL net faces heavy volume (33+ shots; COL pressure)
- **Tampa Bay over 3.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT23TBCOL-TB3|no; why: alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no: MOSTLY_INDEPENDENT (phi 0.047); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.4376): highest fidelity KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes (same contract)
- thesis TBL:NET_LOW_VOLUME (p 0.2922): highest fidelity KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no (same contract)
- thesis TBL:SUPPRESSED (p 0.4558): highest fidelity KXNHLTEAMTOTAL-26OCT23TBCOL-TB4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT23TBCOL-TB4|no (same contract)
- KXNHLGOAL-26OCT23TBCOL-COLJMANSON42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3388, phi -0.091)
- KXNHLGOAL-26OCT23TBCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.3388, phi -0.234)
- KXNHLSAVE-26OCT23TBCOL-TBAVASILEVSKIY88-28|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis TBL:NET_HIGH_VOLUME (p 0.2738, phi -0.712)
- KXNHLTEAMTOTAL-26OCT23TBCOL-TB4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.329, phi -0.975)

portfolios: A EV +5.94 (adj +2.89) on $50.00, P(profit) 0.5904, adj growth 22.2 bp · B EV +3.27 (adj +1.97) on $21.51, P(profit) 0.5904, adj growth 16.7 bp · C EV +1.55 (adj +0.47) on $18.39, P(profit) 0.5661, adj growth 4.1 bp · R EV +0.34 (adj +0.08) on $4.00, P(profit) 0.4363, adj growth 2.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
