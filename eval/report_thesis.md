# Thesis-card postmortem — RESEARCH_ONLY

evaluated 2026-10-03T01:42:03Z · thesis-postmortem-2.0 · rows (all generations) 1296

All P/L below is **FINAL_CARD_UNIQUE**: per game, only the decisions of the ONE latest complete pregame thesis-card snapshot. Repeated generations are in ALL_PROSPECTIVE_DECISIONS (calibration research, no P/L).

## Slate 2026-10-02: **PARTIAL — 1/5 games evaluated**

scheduled 5 · final 1 · settled 1 · events ingested 1 · thesis-evaluated 1 · final_card_complete False · postmortem_complete False

missing / pending:
- 2026020018: no official FINAL result yet
- 2026020019: no official FINAL result yet
- 2026020020: no official FINAL result yet
- 2026020021: game not started: the snapshot shown is the latest so far, not yet final

> INTERIM (PARTIAL — 1/5 games evaluated): covers evaluated games only; NOT the slate's final ROI

invariant final_card_n 4 <= sum(game card caps) 4: OK

### FINAL_CARD_UNIQUE

| view | bets | stake | P/L | ROI |
|---|---:|---:|---:|---:|
| nominal optimiser card (B) | 4 | 33.26 | -1.14 | -0.034 |
| FUNDED research stakes | 1 | 4.00 | +0.82 | 0.205 |

- THESIS: 2 distinct theses, hit rate 0.500 vs mean p 0.424 (Brier 0.231)
- EXPRESSION: thesis right + won 2 · right + lost 0 · wrong + won 0 · wrong + lost 2
  - by fidelity: DIRECT 2/2; FRAGILE 0/2
  - broad vs player: FRAGILE_PLAYER 2/4 (P/L -1.14)
- PRICE: mean CLV -0.0050 (n 4), mean adjusted EV at entry 0.0181
- MODEL: Brier raw 0.0248 · adjusted 0.0320 · Kalshi mid 0.0364 (n 4)
- PORTFOLIO: funded 1 · shadow on card 3 · mean |phi| among card pairs 0.038 · mean largest thesis share 0.759
- GOVERNANCE: funded player props 1 · shadow player props 3 · large-disagreement gates 1 · overrides 0


#### game 2026020017 NYR @ DET: EVALUATED · snapshot snap-1f536c999460c1ae8aca @ 2026-10-02T21:40:36Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT02NYRDET-DETJCOMPHER37-1|yes | SHADOW_ONLY | 0 | 5.35 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -5.35 |
| KXNHLGOAL-26OCT02NYRDET-NYROBJORKSTRAND28-1|no | FUNDED_RESEARCH | 4 | 14.53 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | -0.0050 | 2.97 |
| KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes | SHADOW_ONLY | 0 | 2.65 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -2.65 |
| KXNHLAST-26OCT02NYRDET-NYRPDOROFEYEV16-1|no | SHADOW_ONLY | 0 | 10.73 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | -0.0050 | 3.89 |

#### game 2026020018 WSH @ CAR: NOT_FINAL · snapshot snap-f36fcf4ff7fc968f8611 @ 2026-10-02T22:31:35Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes | FUNDED_RESEARCH | 2 | 7.49 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes | SHADOW_ONLY | 0 | 8.52 | - | - | - | FRAGILE | - | - |
| KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no | SHADOW_ONLY | 0 | 20.00 | - | - | - | DIRECT | - | - |
| KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes | SHADOW_ONLY | 0 | 4.55 | - | - | - | FRAGILE | - | - |

#### game 2026020019 BOS @ WPG: NOT_FINAL · snapshot snap-d894c0f94f16bf8871db @ 2026-10-02T23:22:37Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT02BOSWPG-BOSMKHUSNUTDINOV92-1|yes | SHADOW_ONLY | 0 | 8.25 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes | SHADOW_ONLY | 0 | 8.21 | - | - | - | FRAGILE | - | - |
| KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no | SHADOW_ONLY | 0 | 20.00 | - | - | - | DIRECT | - | - |
| KXNHLGOAL-26OCT02BOSWPG-WPGMSCHEIFELE55-1|yes | FUNDED_RESEARCH | 2 | 5.00 | - | - | - | DIRECT | - | - |

#### game 2026020020 STL @ DAL: NOT_FINAL · snapshot snap-00c8bda1cdf35f5d39cf @ 2026-10-03T00:15:35Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT02STLDAL-STLPSUTER22-1|yes | SHADOW_ONLY | 0 | 6.75 | - | - | - | FRAGILE | - | - |
| KXNHLGAME-26OCT02STLDAL-DAL|no | FUNDED_RESEARCH | 2 | 6.10 | - | - | - | STRUCTURAL | - | - |
| KXNHLGOAL-26OCT02STLDAL-DALMRANTANEN96-1|no | FUNDED_RESEARCH | 5 | 20.00 | - | - | - | DIRECT | - | - |
| KXNHLGOAL-26OCT02STLDAL-STLDHOLLOWAY81-1|yes | SHADOW_ONLY | 0 | 6.92 | - | - | - | FRAGILE | - | - |

#### game 2026020021 ANA @ VGK: NOT_STARTED · snapshot snap-d23b54fd1627316506fe @ 2026-10-03T01:08:42Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT02ANAVGK-ANATWASHE42-1|yes | FUNDED_RESEARCH | 2 | 6.20 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT02ANAVGK-ANAAKILLORN17-1|yes | SHADOW_ONLY | 0 | 8.04 | - | - | - | FRAGILE | - | - |
| KXNHLAST-26OCT02ANAVGK-ANAAKILLORN17-1|yes | SHADOW_ONLY | 0 | 6.77 | - | - | - | DIRECT | - | - |
| KXNHLGOAL-26OCT02ANAVGK-VGKBBOWMAN42-1|yes | SHADOW_ONLY | 0 | 6.64 | - | - | - | FRAGILE | - | - |

## Slate 2026-10-01: **COMPLETE — 8/8 games evaluated**

scheduled 8 · final 8 · settled 8 · events ingested 8 · thesis-evaluated 8 · final_card_complete True · postmortem_complete True

invariant final_card_n 30 <= sum(game card caps) 32: OK

### FINAL_CARD_UNIQUE

| view | bets | stake | P/L | ROI |
|---|---:|---:|---:|---:|
| nominal optimiser card (B) | 30 | 253.01 | -11.32 | -0.045 |
| FUNDED research stakes | - | - | - | no research layer on these decisions (logged before nhl-card-1.1) |

- THESIS: 23 distinct theses, hit rate 0.391 vs mean p 0.400 (Brier 0.204)
- EXPRESSION: thesis right + won 7 · right + lost 4 · wrong + won 7 · wrong + lost 12
  - by fidelity: DIRECT 8/11; FRAGILE 2/15; STRUCTURAL 4/4
  - broad vs player: BROAD 4/4 (P/L +15.99); FRAGILE_PLAYER 10/26 (P/L -27.31)
- PRICE: mean CLV -0.0062 (n 30), mean adjusted EV at entry 0.0236
- MODEL: Brier raw 0.1302 · adjusted 0.1237 · Kalshi mid 0.1249 (n 30)
- PORTFOLIO: funded 0 · shadow on card 0 · mean |phi| among card pairs 0.063 · mean largest thesis share 0.491
- GOVERNANCE: funded player props 0 · shadow player props 0 · large-disagreement gates 0 · overrides 0


#### game 2026020009 PHI @ NJD: EVALUATED · snapshot snap-d3683f7e5e8476920334 @ 2026-10-01T22:57:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 2.33 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0100 | -2.33 |
| KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 2.25 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -2.25 |
| KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 2.81 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -2.81 |
| KXNHLGOAL-26OCT01PHINJ-NJSNOESEN11-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 1.92 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -1.92 |

#### game 2026020010 TBL @ NYR: EVALUATED · snapshot snap-d3683f7e5e8476920334 @ 2026-10-01T22:57:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no | LEGACY_NO_RESEARCH_LAYER | - | 9.14 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | -0.0050 | 6.97 |
| KXNHLSPREAD-26OCT01TBNYR-TB3|no | LEGACY_NO_RESEARCH_LAYER | - | 9.14 | True | True | THESIS_RIGHT_EXPRESSION_WON | STRUCTURAL | -0.0050 | 2.54 |
| KXNHLSPREAD-26OCT01TBNYR-TB2|no | LEGACY_NO_RESEARCH_LAYER | - | 3.28 | True | True | THESIS_RIGHT_EXPRESSION_WON | STRUCTURAL | -0.0050 | 1.57 |

#### game 2026020011 BUF @ CBJ: EVALUATED · snapshot snap-d3683f7e5e8476920334 @ 2026-10-01T22:57:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 4.65 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -4.65 |
| KXNHLGOAL-26OCT01BUFCBJ-CBJCGARLAND83-1|no | LEGACY_NO_RESEARCH_LAYER | - | 8.98 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0050 | 1.83 |
| KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no | LEGACY_NO_RESEARCH_LAYER | - | 4.78 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0150 | 2.97 |
| KXNHLGOAL-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no | LEGACY_NO_RESEARCH_LAYER | - | 4.43 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0050 | 2.22 |

#### game 2026020012 MIN @ NSH: EVALUATED · snapshot snap-0471fa40e0e6b13c7166 @ 2026-10-01T23:47:02Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 4.30 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -4.30 |
| KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no | LEGACY_NO_RESEARCH_LAYER | - | 13.84 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0050 | 1.27 |
| KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 2.58 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -2.58 |
| KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 3.29 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0100 | -3.29 |

#### game 2026020013 CHI @ UTA: EVALUATED · snapshot snap-87bced70acd8e8ac4de4 @ 2026-10-02T01:27:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 7.01 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -7.01 |
| KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 6.56 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0100 | -6.56 |
| KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no | LEGACY_NO_RESEARCH_LAYER | - | 18.55 | False | False | THESIS_WRONG_EXPRESSION_LOST | DIRECT | -0.0100 | -18.55 |
| KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 5.44 | True | True | THESIS_RIGHT_EXPRESSION_WON | FRAGILE | -0.0050 | 16.08 |

#### game 2026020014 SEA @ CGY: EVALUATED · snapshot snap-7c5f74c436d5f9a561e6 @ 2026-10-02T00:37:04Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no | LEGACY_NO_RESEARCH_LAYER | - | 15.33 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0050 | 2.92 |
| KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 3.90 | True | True | THESIS_RIGHT_EXPRESSION_WON | FRAGILE | -0.0050 | 32.79 |
| KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 3.17 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -3.17 |
| KXNHLGOAL-26OCT01SEACGY-CGYMTSYPLAKOV72-1|no | LEGACY_NO_RESEARCH_LAYER | - | 15.33 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | -0.0050 | 2.32 |

#### game 2026020015 EDM @ VAN: EVALUATED · snapshot snap-87bced70acd8e8ac4de4 @ 2026-10-02T01:27:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no | LEGACY_NO_RESEARCH_LAYER | - | 8.55 | False | False | THESIS_WRONG_EXPRESSION_LOST | DIRECT | -0.0050 | -8.55 |
| KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 8.07 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -8.07 |
| KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no | LEGACY_NO_RESEARCH_LAYER | - | 19.64 | False | False | THESIS_WRONG_EXPRESSION_LOST | DIRECT | -0.0150 | -19.64 |
| KXNHLSPREAD-26OCT01EDMVAN-EDM3|no | LEGACY_NO_RESEARCH_LAYER | - | 13.74 | True | False | THESIS_WRONG_EXPRESSION_WON | STRUCTURAL | -0.0050 | 6.02 |

#### game 2026020016 FLA @ SJS: EVALUATED · snapshot snap-87bced70acd8e8ac4de4 @ 2026-10-02T01:27:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 10.14 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -10.14 |
| KXNHLSPREAD-26OCT01FLASJ-FLA3|no | LEGACY_NO_RESEARCH_LAYER | - | 19.93 | True | True | THESIS_RIGHT_EXPRESSION_WON | STRUCTURAL | -0.0050 | 5.86 |
| KXNHLGOAL-26OCT01FLASJ-FLASREINHART13-1|no | LEGACY_NO_RESEARCH_LAYER | - | 19.93 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0000 | 9.14 |

## ALL_PROSPECTIVE_DECISIONS (calibration research; no P/L)

1296 scored rows = 165 unique logical wagers (repeat factor 7.85). every scored pregame decision of every generation (repeated observations of one wager are NOT independent; no P/L here).

| family | rows | unique | Brier all rows | Brier last obs | adjusted | Kalshi mid |
|---|---:|---:|---:|---:|---:|---:|
| first_goal | 1 | 1 | 0.0011 | 0.0011 | 0.0010 | 0.0009 |
| game_spread | 209 | 15 | 0.1394 | 0.1471 | 0.1545 | 0.1663 |
| game_total | 8 | 4 | 0.1985 | 0.1576 | 0.1506 | 0.1455 |
| game_winner | 76 | 9 | 0.2061 | 0.2025 | 0.2196 | 0.2346 |
| goalie_saves | 1 | 1 | 0.1465 | 0.1465 | 0.1861 | 0.2304 |
| player_assists | 288 | 36 | 0.2259 | 0.2229 | 0.2050 | 0.1977 |
| player_goals | 523 | 73 | 0.1212 | 0.1237 | 0.1235 | 0.1242 |
| player_points | 33 | 4 | 0.2597 | 0.2925 | 0.2878 | 0.2947 |
| team_total | 157 | 22 | 0.2031 | 0.2150 | 0.2211 | 0.2300 |

_Prospective thesis-card evidence. All P/L is FINAL_CARD_UNIQUE (one latest complete pregame snapshot per game). THESIS / EXPRESSION / PRICE / MODEL / PORTFOLIO / GOVERNANCE are kept separate: a right thesis expressed through a contract that lost is not a wrong prediction. A handful of games proves nothing; never tune to one slate._
