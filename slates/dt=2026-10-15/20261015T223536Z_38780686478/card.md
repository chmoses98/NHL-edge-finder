# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-15T22:35:36Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +25.69 | +6.52 | +25.21 | 0.811 | -11.22 | -20.51 | 61.15 |
| B thesis-diversified (joint) ← optimiser card | 149.12 | +19.61 | +9.78 | +18.73 | 0.748 | -16.32 | -25.45 | 93.89 |
| C best expression per thesis | 150.01 | +25.58 | +9.88 | +23.67 | 0.746 | -19.78 | -30.90 | 92.22 |
| R FUNDED research stakes | 21.00 | +2.36 | +1.30 | +1.32 | 0.612 | -5.05 | -6.88 | 0.00 |

## BUF @ TOR  ·  10000 joint draws  ·  480 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.523 / away 0.477

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_BUF_win | p_overtime | goals | shots TOR/BUF | TOR/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.53 | 0.47 | 0.00 | 6.06 | 27.9/28.6 | 25.1/24.2 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.112 | 0.48 | 0.52 | 0.00 | 6.01 | 22.4/34.1 | 30.0/19.1 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.51 | 0.49 | 0.47 | 5.95 | 22.3/34.4 | 30.9/19.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.53 | 0.47 | 0.49 | 5.96 | 28.1/28.8 | 25.6/24.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.55 | 0.45 | 0.00 | 9.28 | 29.6/30.2 | 24.2/23.2 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.086 | 0.44 | 0.56 | 0.00 | 9.34 | 23.6/35.9 | 29.1/18.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Owen Power: 1+ goals NO | 86 | 0.911 | 0.897 | +0.043 | +0.029 | $6.66 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Gavin McKenna: 1+ assists NO | 69 | 0.771 | 0.728 | +0.066 | +0.023 | $6.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Teddy Blueger: 1+ goals YES | 10 | 0.128 | 0.120 | +0.022 | +0.013 | $1.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 60 | 0.643 | 0.631 | +0.027 | +0.015 | $3.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (16.41 vs 3.80 bp); despite a smaller raw edge (+0.043 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15BUFTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: BUF offense succeeds (4+ goals)
- **Gavin McKenna: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15BUFTOR-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (5.53 vs 0.79 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15BUFTOR-TORTBLUEGER73-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.056); KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense succeeds (4+ goals)
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15BUFTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (4.11 vs 0.50 bp); despite a smaller raw edge (+0.022 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no: INTENTIONAL_DIVERSIFIER (phi -0.056); KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: TOR offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no; why: Player prop expression KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.81 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT15BUFTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: BUF offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TOR:SUPPRESSED (p 0.367): highest fidelity KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no (same contract)
- thesis BUF:SUPPRESSED (p 0.3766): highest fidelity KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no (same contract)
- thesis TOR:NET_HIGH_VOLUME (p 0.3609): highest fidelity KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes (same contract)
- KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4018, phi -0.122)
- KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4186, phi -0.212)
- KXNHLGOAL-26OCT15BUFTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.367, phi -0.163)
- KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4018, phi -0.269)
- override: Player prop expression KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT15BUFTOR-BUFTTHOMPSON72-1|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.81 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.19 (adj +0.44) on $13.64, P(profit) 0.6955, adj growth 4.3 bp · B EV +1.33 (adj +0.66) on $17.62, P(profit) 0.522, adj growth 6.4 bp · C EV +2.01 (adj +0.66) on $20.39, P(profit) 0.6435, adj growth 6.2 bp · R EV +0.10 (adj +0.07) on $2.00, P(profit) 0.9115, adj growth 2.6 bp

## NYI @ OTT  ·  10000 joint draws  ·  458 bet sides mapped, 8 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.595 / away 0.405

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NYI_win | p_overtime | goals | shots OTT/NYI | OTT/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.66 | 0.34 | 0.00 | 5.98 | 26.8/26.8 | 23.9/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.44 | 5.9 | 26.9/26.6 | 23.5/23.6 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.097 | 0.69 | 0.31 | 0.00 | 6.02 | 31.9/21.0 | 18.3/27.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.64 | 0.36 | 0.00 | 9.23 | 28.5/28.2 | 23.1/21.5 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.57 | 0.43 | 0.46 | 5.82 | 31.8/21.5 | 18.4/28.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.60 | 0.40 | 0.00 | 3.42 | 25.5/25.5 | 24.0/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ondrej Palat: 1+ goals YES | 8 | 0.123 | 0.111 | +0.037 | +0.025 | $2.17 | FUNDED_RESEARCH | $1 | NYI:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Andre Burakovsky: 1+ assists NO | 75 | 0.841 | 0.793 | +0.078 | +0.030 | $7.05 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Jean-Gabriel Pageau: 1+ goals YES | 12 | 0.152 | 0.142 | +0.025 | +0.014 | $1.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-9|yes; why: higher confidence-adjusted growth (17.76 vs 0.39 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.909 vs 0.371); alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15NYIOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT15NYIOTT-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NYI offense suppressed (<= 2 goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (10.92 vs 1.11 bp); relationships: KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT15NYIOTT-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: OTT offense succeeds (4+ goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-9|yes; why: higher confidence-adjusted growth (3.91 vs 0.39 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.929 vs 0.371); alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT15NYIOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.349): highest fidelity KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.2978): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis OTT:OFFENSE_4PLUS (p 0.4381): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4937, phi -0.183)
- KXNHLAST-26OCT15NYIOTT-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4381, phi -0.17)
- KXNHLGOAL-26OCT15NYIOTT-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4937, phi -0.2)

portfolios: A EV +2.19 (adj +1.17) on $13.64, P(profit) 0.2495, adj growth 11.1 bp · B EV +1.93 (adj +1.07) on $10.53, P(profit) 0.2359, adj growth 10.2 bp · C EV +0.31 (adj +0.07) on $4.84, P(profit) 0.7505, adj growth 0.7 bp · R EV +0.44 (adj +0.30) on $1.00, P(profit) 0.1226, adj growth 10.8 bp

## SEA @ TBL  ·  10000 joint draws  ·  448 bet sides mapped, 36 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.702 / away 0.298

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_SEA_win | p_overtime | goals | shots TBL/SEA | TBL/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.131 | 0.67 | 0.33 | 0.00 | 5.95 | 32.8/21.1 | 18.5/28.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.120 | 0.57 | 0.43 | 0.49 | 5.86 | 33.0/21.4 | 18.3/29.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.63 | 0.37 | 0.00 | 6.0 | 27.2/26.6 | 23.7/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.54 | 0.46 | 0.48 | 5.96 | 27.4/26.7 | 23.5/24.0 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.074 | 0.71 | 0.29 | 0.00 | 9.23 | 34.6/22.5 | 18.0/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.62 | 0.38 | 0.00 | 9.26 | 28.8/28.1 | 22.8/22.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 1.5 goals NO | 51 | 0.645 | 0.554 | +0.118 | +0.027 | $3.67 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 65 | 0.764 | 0.687 | +0.099 | +0.021 | $1.79 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ goals NO | 59 | 0.642 | 0.627 | +0.035 | +0.021 | $3.57 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15SEATB-TB3|no; why: Broad expression KXNHLSPREAD-26OCT15SEATB-TB2|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-TB6|no because adjusted EV is 1.1 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT15SEATB-TB3|no: DUPLICATIVE (phi 0.749); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.191); failure: TBL wins by 2+
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15SEATB-TB2|no; why: Broad expression KXNHLSPREAD-26OCT15SEATB-TB3|no selected over player prop KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26OCT15SEATB-TB2|no: DUPLICATIVE (phi 0.749); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.172); failure: TBL wins by 2+
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no; why: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-2|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.81 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26OCT15SEATB-TB2|no: REINFORCING (phi 0.191); KXNHLSPREAD-26OCT15SEATB-TB3|no: REINFORCING (phi 0.172); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.13, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TBL:SUPPRESSED (p 0.3519): highest fidelity KXNHLTEAMTOTAL-26OCT15SEATB-TB4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no — Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-2|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.81 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis SEA:WINS (p 0.4106): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no — Broad expression KXNHLSPREAD-26OCT15SEATB-TB2|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-TB6|no because adjusted EV is 1.1 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis SEA:OFFENSE_4PLUS (p 0.2975): highest fidelity KXNHLTEAMTOTAL-26OCT15SEATB-SEA3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15SEATB-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT15SEATB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.0 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3548, phi -1.0)
- KXNHLSPREAD-26OCT15SEATB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 11.9 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3548, phi -0.749)
- KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4301, phi -0.243)
- override: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-2|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.81 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLSPREAD-26OCT15SEATB-TB2|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-TB6|no because adjusted EV is 1.1 pts higher while thesis capture is 1.00 vs 0.99 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- override: Broad expression KXNHLSPREAD-26OCT15SEATB-TB3|no selected over player prop KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no because adjusted EV differs by only 1.0 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.86 (adj +0.55) on $13.64, P(profit) 0.6438, adj growth 5.0 bp · B EV +1.29 (adj +0.36) on $9.03, P(profit) 0.6452, adj growth 3.5 bp · C EV +3.86 (adj +1.31) on $12.66, P(profit) 0.6196, adj growth 12.2 bp · R EV +0.43 (adj +0.12) on $3.00, P(profit) 0.7129, adj growth 4.4 bp

## VAN @ FLA  ·  10000 joint draws  ·  422 bet sides mapped, 36 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.715 / away 0.285

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_VAN_win | p_overtime | goals | shots FLA/VAN | FLA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.118 | 0.68 | 0.32 | 0.00 | 6.02 | 32.7/21.1 | 18.4/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.61 | 0.39 | 0.00 | 6.02 | 27.2/26.7 | 23.7/23.1 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.54 | 0.46 | 0.45 | 5.96 | 32.6/21.4 | 18.2/29.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.51 | 0.49 | 0.49 | 6.0 | 27.5/26.9 | 23.5/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.59 | 0.41 | 0.00 | 9.35 | 28.9/28.4 | 22.7/22.4 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.087 | 0.67 | 0.33 | 0.00 | 9.22 | 34.4/22.5 | 17.8/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Marco Rossi: 1+ goals YES | 17 | 0.250 | 0.228 | +0.070 | +0.049 | $4.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 61 | 0.701 | 0.677 | +0.074 | +0.050 | $7.05 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Jake DeBrusk: 1+ goals YES | 26 | 0.321 | 0.305 | +0.048 | +0.031 | $3.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_STRONGER | D |
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (34.15 vs 29.21 bp); relationships: KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: VAN offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes; why: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes has the higher standalone adjusted growth (24.00 vs 23.50 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.143); relationships: KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: FLA offense succeeds (4+ goals)
- **Jake DeBrusk: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes; why: Player prop expression KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes selected over broad KXNHLSPREAD-26OCT15VANFLA-FLA3|no because adjusted EV is 0.6 pts higher while thesis capture is 0.43 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3482): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.224): highest fidelity KXNHLSPREAD-26OCT15VANFLA-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15VANFLA-VAN2|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.2973): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4311, phi -0.238)
- KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4608, phi -0.244)
- KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4311, phi -0.274)
- override: Player prop expression KXNHLGOAL-26OCT15VANFLA-VANJDEBRUSK74-1|yes selected over broad KXNHLSPREAD-26OCT15VANFLA-FLA3|no because adjusted EV is 0.6 pts higher while thesis capture is 0.43 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.33 (adj +0.90) on $13.64, P(profit) 0.5357, adj growth 8.0 bp · B EV +3.32 (adj +2.27) on $15.45, P(profit) 0.4179, adj growth 21.7 bp · C EV +6.25 (adj +3.19) on $15.96, P(profit) 0.434, adj growth 29.5 bp · R EV +0.24 (adj +0.16) on $2.00, P(profit) 0.7005, adj growth 6.2 bp
equivalent contracts collapsed: KXNHLGAME-26OCT15VANFLA-VAN|yes == KXNHLGAME-26OCT15VANFLA-FLA|no

## NYR @ NJD  ·  10000 joint draws  ·  440 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.547 / away 0.453

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_NYR_win | p_overtime | goals | shots NJD/NYR | NJD/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.131 | 0.58 | 0.42 | 0.00 | 5.98 | 32.9/21.3 | 18.1/28.8 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.46 | 5.94 | 33.4/21.3 | 18.1/30.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.49 | 0.51 | 0.00 | 5.97 | 27.2/26.5 | 22.9/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.48 | 0.52 | 0.47 | 5.85 | 27.3/26.7 | 23.5/24.2 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.076 | 0.58 | 0.42 | 0.00 | 9.1 | 34.5/22.7 | 17.6/27.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.067 | 0.47 | 0.53 | 0.00 | 9.2 | 28.7/28.0 | 21.8/22.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Amadeus Lombardi: 1+ goals YES | 10 | 0.134 | 0.123 | +0.028 | +0.017 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 62 | 0.676 | 0.661 | +0.040 | +0.025 | $4.90 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 73 | 0.777 | 0.763 | +0.034 | +0.019 | $5.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Gabe Perreault: 1+ assists YES | 26 | 0.318 | 0.286 | +0.044 | +0.013 | $1.51 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_MIXED | D |
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15NYRNJ-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (6.32 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: NJD offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no; why: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no has the higher standalone adjusted growth (6.56 vs 5.69 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.001); relationships: KXNHLGOAL-26OCT15NYRNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: NJD offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15NYRNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: NJD offense succeeds (4+ goals)
- **Gabe Perreault: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15NYRNJ-NJ3|no; why: higher confidence-adjusted growth (1.81 vs 1.01 bp); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYRNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: NYR offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis NJD:SUPPRESSED (p 0.4082): highest fidelity KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NYR:OFFENSE_4PLUS (p 0.3588): highest fidelity KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.3697): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15NYRNJ-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4082, phi -0.176)
- KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3697, phi -0.255)
- KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3697, phi -0.229)
- KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4258, phi -0.268)
- override: Player prop expression KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.89 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.92 (adj +0.41) on $13.64, P(profit) 0.7396, adj growth 3.9 bp · B EV +1.20 (adj +0.64) on $13.59, P(profit) 0.5911, adj growth 6.2 bp · C EV +2.07 (adj +0.49) on $9.14, P(profit) 0.6073, adj growth 4.6 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.6763, adj growth 2.9 bp

## PHI @ DET  ·  10000 joint draws  ·  438 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.564 / away 0.436

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_PHI_win | p_overtime | goals | shots DET/PHI | DET/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.52 | 0.48 | 0.00 | 5.93 | 27.1/26.6 | 23.2/23.7 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.115 | 0.56 | 0.44 | 0.00 | 5.96 | 32.8/21.2 | 18.1/28.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.46 | 5.85 | 27.4/26.9 | 23.7/24.2 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.53 | 0.47 | 0.48 | 5.88 | 32.6/21.4 | 18.2/29.1 | even strength |
| DET shot control · low event (<=4) · tight (1-goal/OT) | 0.069 | 0.53 | 0.47 | 0.50 | 2.8 | 30.8/20.0 | 18.7/29.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.50 | 2.83 | 26.1/25.7 | 24.2/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nate Danielson: 1+ goals NO | 82 | 0.887 | 0.869 | +0.057 | +0.039 | $7.05 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 78 | 0.826 | 0.812 | +0.034 | +0.020 | $7.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Denver Barkey: 1+ goals YES | 14 | 0.173 | 0.164 | +0.025 | +0.015 | $1.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 20 | 0.233 | 0.224 | +0.022 | +0.013 | $1.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Nate Danielson: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (23.83 vs 2.79 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.017); failure: DET offense succeeds (4+ goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT15PHIDET-4|no; why: higher confidence-adjusted growth (5.27 vs 0.70 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.997 vs 0.344); alternative not eligible: confidence-adjusted EV +0.0066 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: PHI offense succeeds (4+ goals)
- **Denver Barkey: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (4.01 vs 2.15 bp); relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes; why: KXNHLGOAL-26OCT15PHIDET-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (2.15 vs 2.07 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.006); relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DET shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis DET:SUPPRESSED (p 0.4385): highest fidelity KXNHLTEAMTOTAL-26OCT15PHIDET-DET4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.328): highest fidelity KXNHLSPREAD-26OCT15PHIDET-DET3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:WINS (p 0.4845): highest fidelity KXNHLSPREAD-26OCT15PHIDET-DET3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT15PHIDET-DET4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.345, phi -0.161)
- KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.328, phi -0.177)
- KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4565, phi -0.187)
- KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4565, phi -0.23)

portfolios: A EV +0.98 (adj +0.35) on $13.64, P(profit) 0.6178, adj growth 3.4 bp · B EV +1.18 (adj +0.74) on $16.98, P(profit) 0.7761, adj growth 7.2 bp · C EV +1.21 (adj +0.48) on $23.21, P(profit) 0.6567, adj growth 4.6 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.8871, adj growth 3.7 bp

## WPG @ CHI  ·  10000 joint draws  ·  472 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.467 / away 0.533

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_WPG_win | p_overtime | goals | shots CHI/WPG | CHI/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.51 | 0.49 | 0.00 | 6.0 | 26.4/26.6 | 23.2/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.49 | 5.91 | 26.4/26.7 | 23.4/23.1 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.097 | 0.45 | 0.55 | 0.00 | 5.96 | 21.1/31.9 | 28.0/17.9 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.50 | 0.50 | 0.49 | 5.92 | 21.2/31.8 | 28.4/18.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.49 | 0.51 | 0.00 | 9.32 | 28.0/28.2 | 22.1/21.9 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.059 | 0.43 | 0.57 | 0.00 | 9.15 | 22.4/33.5 | 26.4/17.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 26 | 0.314 | 0.299 | +0.040 | +0.025 | $2.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Nino Niederreiter: 1+ assists NO | 80 | 0.875 | 0.832 | +0.063 | +0.021 | $6.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | WPG:SUPPRESSED | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Roman Kantserov: 1+ goals NO | 74 | 0.792 | 0.777 | +0.039 | +0.023 | $6.76 | FUNDED_RESEARCH | $2 | CHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Ryan Greene: 1+ goals YES | 13 | 0.162 | 0.152 | +0.024 | +0.015 | $1.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT15WPGCHI-CHIAVLASIC72-1|yes; why: higher confidence-adjusted growth (7.06 vs 0.18 bp); despite a smaller raw edge (+0.040 vs +0.080/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15WPGCHI-WPGNNIEDERREITER62-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: CHI offense suppressed (<= 2 goals)
- **Nino Niederreiter: 1+ assists NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15WPGCHI-WPGMSCHEIFELE55-1|no; why: higher confidence-adjusted growth (6.43 vs 0.18 bp); alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: WPG offense succeeds (4+ goals)
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no; why: Player prop expression KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.90 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT15WPGCHI-WPGNNIEDERREITER62-1|no: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: CHI offense succeeds (4+ goals)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (7.06 vs 3.89 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT15WPGCHI-WPGNNIEDERREITER62-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.3726): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4051): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no (same contract)
- thesis WPG:SUPPRESSED (p 0.4041): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4051, phi -0.274)
- KXNHLAST-26OCT15WPGCHI-WPGNNIEDERREITER62-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3743, phi -0.178)
- KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3726, phi -0.209)
- KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4051, phi -0.178)
- override: Player prop expression KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.90 vs 0.81 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.65 (adj +0.54) on $13.64, P(profit) 0.7142, adj growth 5.3 bp · B EV +1.51 (adj +0.78) on $17.62, P(profit) 0.4162, adj growth 7.5 bp · C EV +1.16 (adj +0.72) on $14.60, P(profit) 0.3135, adj growth 6.8 bp · R EV +0.10 (adj +0.06) on $2.00, P(profit) 0.7922, adj growth 2.4 bp

## SJS @ NSH  ·  10000 joint draws  ·  460 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.542 / away 0.458

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_SJS_win | p_overtime | goals | shots NSH/SJS | NSH/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.53 | 0.47 | 0.00 | 6.04 | 27.9/27.9 | 24.5/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.50 | 0.50 | 0.47 | 6.01 | 27.7/27.7 | 24.5/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.55 | 0.45 | 0.00 | 9.29 | 29.3/29.2 | 23.4/22.7 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.068 | 0.58 | 0.42 | 0.00 | 5.97 | 32.2/22.0 | 18.9/28.0 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.067 | 0.50 | 0.50 | 0.00 | 6.0 | 22.3/32.8 | 29.1/18.9 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.55 | 0.45 | 0.47 | 5.86 | 32.6/22.4 | 19.4/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Juuse Saros: 26+ saves NO | 52 | 0.606 | 0.560 | +0.068 | +0.023 | $4.44 | FUNDED_RESEARCH | $2 | NSH:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mason Marchment: 1+ goals YES | 21 | 0.252 | 0.239 | +0.031 | +0.018 | $1.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 69 | 0.786 | 0.717 | +0.081 | +0.012 | $4.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Macklin Celebrini: 1+ assists NO | 42 | 0.569 | 0.450 | +0.131 | +0.013 | $2.26 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.75) | CALIBRATION_WARNING | D |
- **Juuse Saros: 26+ saves NO** — thesis: NSH net faces light volume (<= 25 shots; SJS suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.055); KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi -0.044); failure: NSH net faces heavy volume (33+ shots; SJS pressure)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15SJNSH-SJTTOFFOLI73-1|yes; why: higher confidence-adjusted growth (3.94 vs 2.48 bp); despite a smaller raw edge (+0.031 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSAVE-26OCT15SJNSH-NSHJSAROS74-26|no: MOSTLY_INDEPENDENT (phi 0.055); KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.084); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (1.57 vs 1.40 bp); despite a smaller raw edge (+0.081 vs +0.131/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLSAVE-26OCT15SJNSH-NSHJSAROS74-26|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.044); failure: SJS offense succeeds (4+ goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no; why: second expression of the same thesis: KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no has the higher standalone adjusted growth (1.57 vs 1.40 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.044); they share one thesis budget; relationships: KXNHLSAVE-26OCT15SJNSH-NSHJSAROS74-26|no: MOSTLY_INDEPENDENT (phi -0.044); KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.084); KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.044); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NSH:NET_LOW_VOLUME (p 0.3789): highest fidelity KXNHLSAVE-26OCT15SJNSH-NSHJSAROS74-26|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT15SJNSH-NSHJSAROS74-26|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.395): highest fidelity KXNHLAST-26OCT15SJNSH-SJTTOFFOLI73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.3851): highest fidelity KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSAVE-26OCT15SJNSH-NSHJSAROS74-26|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis NSH:NET_HIGH_VOLUME (p 0.1967, phi -0.543)
- KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3851, phi -0.221)
- KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 10.6 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.395, phi -0.204)
- KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 25% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.395, phi -0.274)

portfolios: A EV +2.50 (adj +0.48) on $13.64, P(profit) 0.5463, adj growth 4.5 bp · B EV +2.02 (adj +0.49) on $13.05, P(profit) 0.6385, adj growth 4.6 bp · C EV +1.95 (adj +0.60) on $15.70, P(profit) 0.5766, adj growth 5.6 bp · R EV +0.25 (adj +0.09) on $2.00, P(profit) 0.6059, adj growth 3.2 bp

## STL @ MIN  ·  10000 joint draws  ·  460 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.560 / away 0.440

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_STL_win | p_overtime | goals | shots MIN/STL | MIN/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.58 | 0.42 | 0.00 | 6.04 | 27.7/27.4 | 23.9/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.55 | 0.45 | 0.46 | 5.99 | 27.7/27.6 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.58 | 0.42 | 0.00 | 9.3 | 29.3/29.1 | 23.3/22.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.081 | 0.66 | 0.34 | 0.00 | 6.01 | 32.7/21.9 | 19.2/28.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.53 | 0.47 | 0.48 | 5.93 | 32.7/22.1 | 18.9/29.3 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.061 | 0.62 | 0.38 | 0.00 | 9.21 | 34.7/23.4 | 18.4/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Rieger Lorenz: 1+ goals YES | 10 | 0.138 | 0.125 | +0.032 | +0.019 | $1.56 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 24 | 0.318 | 0.277 | +0.066 | +0.024 | $2.41 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Ryan Hartman: 1+ goals YES | 19 | 0.232 | 0.219 | +0.032 | +0.018 | $2.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ assists NO | 35 | 0.421 | 0.383 | +0.056 | +0.017 | $3.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.65) | EVIDENCE_MIXED | D |
- **Rieger Lorenz: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (7.89 vs 6.58 bp); despite a smaller raw edge (+0.032 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.131); KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT15STLMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.057); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (6.58 vs 4.60 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi 0.131); KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT15STLMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.07); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (6.58 vs 4.60 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.009); they share one thesis budget; relationships: KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT15STLMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.119); failure: MIN offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15STLMIN-MINQHUGHES43-2|no; why: higher confidence-adjusted growth (2.82 vs 2.25 bp); relationships: KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.057); KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.07); KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.119); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4345): highest fidelity KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3552): highest fidelity KXNHLAST-26OCT15STLMIN-STLPBROBERG6-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.3426): highest fidelity KXNHLAST-26OCT15STLMIN-MINQHUGHES43-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT15STLMIN-MINQHUGHES43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3426, phi -0.153)
- KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3426, phi -0.24)
- KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3426, phi -0.209)
- KXNHLAST-26OCT15STLMIN-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 35% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4345, phi -0.317)

portfolios: A EV +2.23 (adj +0.67) on $13.64, P(profit) 0.6676, adj growth 6.2 bp · B EV +1.91 (adj +0.85) on $9.26, P(profit) 0.5361, adj growth 8.1 bp · C EV +1.98 (adj +0.76) on $10.53, P(profit) 0.5074, adj growth 7.1 bp · R EV +0.30 (adj +0.18) on $1.00, P(profit) 0.1383, adj growth 6.2 bp

## UTA @ EDM  ·  10000 joint draws  ·  472 bet sides mapped, 21 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.489 / away 0.511

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_UTA_win | p_overtime | goals | shots EDM/UTA | EDM/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.63 | 0.37 | 0.00 | 6.01 | 27.6/27.5 | 24.6/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.115 | 0.63 | 0.37 | 0.00 | 9.48 | 29.4/29.4 | 24.0/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.47 | 6.03 | 28.0/27.8 | 24.5/24.5 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.080 | 0.68 | 0.32 | 0.00 | 6.07 | 32.5/22.0 | 19.3/28.0 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.067 | 0.69 | 0.31 | 0.00 | 9.5 | 34.3/23.3 | 18.6/26.1 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.060 | 0.55 | 0.45 | 0.47 | 5.97 | 32.8/22.2 | 19.1/29.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 16 | 0.216 | 0.200 | +0.047 | +0.030 | $2.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 9 | 0.127 | 0.116 | +0.032 | +0.020 | $1.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 65 | 0.703 | 0.689 | +0.037 | +0.023 | $6.09 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Leon Draisaitl: 1+ assists NO | 41 | 0.489 | 0.447 | +0.062 | +0.020 | $3.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.73) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (13.85 vs 5.64 bp); despite a smaller raw edge (+0.047 vs +0.102/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT15UTAEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (13.85 vs 9.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT15UTAEDM-EDMLDRAISAITL29-1|no: INTENTIONAL_DIVERSIFIER (phi -0.09); failure: EDM offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no; why: Player prop expression KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no selected over player prop KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.85 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT15UTAEDM-EDMLDRAISAITL29-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: UTA offense succeeds (4+ goals)
- **Leon Draisaitl: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (3.63 vs 3.45 bp); despite a smaller raw edge (+0.062 vs +0.098/contract); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: EDM offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.499): highest fidelity KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS (p 0.5762): highest fidelity KXNHLSPREAD-26OCT15UTAEDM-UTA2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.4009): highest fidelity KXNHLSPREAD-26OCT15UTAEDM-UTA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no — Player prop expression KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no selected over player prop KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.85 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2954, phi -0.201)
- KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2954, phi -0.135)
- KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3804, phi -0.249)
- KXNHLAST-26OCT15UTAEDM-EDMLDRAISAITL29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 27% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.499, phi -0.307)
- override: Player prop expression KXNHLGOAL-26OCT15UTAEDM-UTADGUENTHER11-1|no selected over player prop KXNHLAST-26OCT15UTAEDM-UTAVTROCHECK16-1|no because adjusted EV is 0.0 pts higher while thesis capture is 0.85 vs 0.91 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.47 (adj +0.63) on $13.64, P(profit) 0.4691, adj growth 5.8 bp · B EV +2.27 (adj +1.28) on $14.39, P(profit) 0.5601, adj growth 12.2 bp · C EV +4.76 (adj +1.60) on $22.98, P(profit) 0.6871, adj growth 14.9 bp · R EV +0.11 (adj +0.07) on $2.00, P(profit) 0.7034, adj growth 2.6 bp

## CGY @ VGK  ·  10000 joint draws  ·  472 bet sides mapped, 6 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.710 / away 0.290

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_CGY_win | p_overtime | goals | shots VGK/CGY | VGK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.73 | 0.27 | 0.00 | 6.03 | 28.5/28.0 | 25.5/23.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.115 | 0.81 | 0.19 | 0.00 | 6.0 | 33.8/22.0 | 19.8/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.55 | 0.45 | 0.46 | 5.89 | 28.4/27.8 | 24.4/24.9 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.60 | 0.40 | 0.44 | 5.88 | 33.8/22.4 | 19.4/30.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.74 | 0.26 | 0.00 | 9.23 | 29.9/29.3 | 24.3/22.5 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.080 | 0.80 | 0.20 | 0.00 | 9.2 | 35.6/23.2 | 19.4/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 68 | 0.740 | 0.724 | +0.045 | +0.029 | $5.29 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Trevor Connelly: 1+ assists NO | 64 | 0.777 | 0.685 | +0.120 | +0.028 | $5.29 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.085 | 0.076 | +0.021 | +0.012 | $1.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (8.45 vs 0.76 bp); alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.041); KXNHLGOAL-26OCT15CGYVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: VGK offense succeeds (4+ goals)
- **Trevor Connelly: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (7.88 vs 0.76 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0089 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.041); KXNHLGOAL-26OCT15CGYVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: VGK offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT15CGYVGK-VGKBMCNABB3-1|yes; why: higher confidence-adjusted growth (5.42 vs 0.00 bp); despite a smaller raw edge (+0.021 vs +0.044/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, VGK shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VGK:SUPPRESSED (p 0.2881): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis VGK:OFFENSE_4PLUS (p 0.5061): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5061, phi -0.21)
- KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.2 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5061, phi -0.212)
- KXNHLGOAL-26OCT15CGYVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2881, phi -0.107)

portfolios: A EV +1.37 (adj +0.38) on $13.64, P(profit) 0.5955, adj growth 3.7 bp · B EV +1.65 (adj +0.64) on $11.60, P(profit) 0.6187, adj growth 6.2 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.13 (adj +0.08) on $2.00, P(profit) 0.74, adj growth 3.2 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
