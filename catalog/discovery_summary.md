# Kalshi NHL discovery summary

- discovered_at: `2026-10-13T23:40:02Z`  ontology: `2026.09.29.2`  requests: 160
- series enumerated: 15011; NHL series: 77; markets scanned: 5604

## Support states (coverage invariant)

| support | markets |
|---|---:|
| MODELABLE | 680 |
| BUILDABLE | 18 |
| RESEARCH | 4314 |
| UNMODELABLE | 547 |
| UNRESOLVED | 45 |

## NHL series

| series | family | support | fee | unopened | open | closed | settled | strike_types | parse |
|---|---|---|---|---:|---:|---:|---:|---|---|
| KXCANADACUP | season_champion | RESEARCH | quadratic/1 | 0 | 1 | 0 | 0 | None | {'low': 1} |
| KXCONNSMYTHE | season_awards | UNMODELABLE | quadratic_with_maker_fees/1 | 0 | 0 | 0 | 0 |  | {} |
| KXESPYNHL | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNEXTTEAMNHL | season_awards | UNMODELABLE | quadratic/1 | 0 | 263 | 0 | 0 | structured | {'low': 263} |
| KXNHL | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHL1P | period_winner | RESEARCH | quadratic/1 | 0 | 45 | 0 | 0 | structured | {'high': 45} |
| KXNHL1PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL1PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 31 | 0 | 0 | greater | {'high': 31} |
| KXNHL1PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 47 | 0 | 0 | greater | {'high': 47} |
| KXNHL1STTEAM | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2OT | game_multi_overtime | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2P | period_winner | RESEARCH | quadratic/1 | 0 | 54 | 0 | 0 | structured | {'high': 54} |
| KXNHL2PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 38 | 0 | 0 | greater | {'high': 38} |
| KXNHL2PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 64 | 0 | 0 | greater | {'high': 64} |
| KXNHL30COMEBACK | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL3P | period_winner | RESEARCH | quadratic/1 | 0 | 54 | 0 | 0 | structured | {'high': 54} |
| KXNHL3PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL3PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 36 | 0 | 0 | greater | {'high': 36} |
| KXNHL3PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 66 | 0 | 0 | greater | {'high': 66} |
| KXNHL4NATIONS | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLADAMS | season_awards | UNMODELABLE | quadratic/1 | 0 | 32 | 0 | 0 | custom | {'low': 32} |
| KXNHLANYGOAL | player_goals | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLAST | player_assists | RESEARCH | quadratic/1 | 0 | 639 | 0 | 0 | greater | {'high': 639} |
| KXNHLATLANTIC | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLCALDER | season_awards | UNMODELABLE | quadratic/1 | 0 | 40 | 0 | 0 | structured,custom | {'low': 40} |
| KXNHLCENTRAL | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLDRAFTPICK | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLDRAFTTOP | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLEAST | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 16 | 0 | 0 | structured | {'low': 16} |
| KXNHLEXPANSION | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 1 | 0 | 0 | None | {'low': 1} |
| KXNHLF10G | game_early_goal | RESEARCH | quadratic/1 | 0 | 12 | 0 | 0 | greater_or_equal | {'high': 12} |
| KXNHLFINALSEXACT | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLFIRSTGOAL | first_goal | RESEARCH | quadratic/1 | 0 | 363 | 0 | 0 | structured | {'high': 363} |
| KXNHLGAME | game_winner | MODELABLE | quadratic_with_maker_fees/1 | 0 | 102 | 0 | 0 | structured | {'high': 102} |
| KXNHLGOAL | player_goals | RESEARCH | quadratic/1 | 0 | 993 | 0 | 0 | greater | {'high': 993} |
| KXNHLHART | season_awards | UNMODELABLE | quadratic/1 | 0 | 28 | 0 | 0 | structured | {'low': 28} |
| KXNHLLINDSAY | UNRESOLVED | UNRESOLVED | quadratic/1 | 0 | 28 | 0 | 0 | structured | {'low': 28} |
| KXNHLMENTION | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLMETROPOLITAN | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLMVP | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLNEXTGM | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLNEXTTEAM | season_awards | UNMODELABLE | quadratic/1 | 0 | 33 | 0 | 0 | structured | {'low': 33} |
| KXNHLNORRIS | season_awards | UNMODELABLE | quadratic/1 | 0 | 30 | 0 | 0 | structured | {'low': 30} |
| KXNHLOT | game_overtime | BUILDABLE | quadratic/1 | 0 | 18 | 0 | 0 | greater | {'high': 18} |
| KXNHLOVERTIME | game_overtime | BUILDABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPACIFIC | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLPLAYOFF | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLPLAYOFFGOALS | season_player_stats | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPRES | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLPRICE | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPSEASONGOALS | UNRESOLVED | UNRESOLVED | quadratic/1 | 0 | 17 | 0 | 0 | greater | {'low': 17} |
| KXNHLPTS | player_points | RESEARCH | quadratic/1 | 0 | 863 | 0 | 0 | greater | {'high': 863} |
| KXNHLRECORDWORST | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLRETIRE | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLRICHARD | season_awards | UNMODELABLE | quadratic/1 | 0 | 40 | 0 | 0 | structured | {'low': 40} |
| KXNHLROSS | season_awards | UNMODELABLE | quadratic/1 | 0 | 40 | 0 | 0 | structured | {'low': 40} |
| KXNHLSAVE | goalie_saves | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | greater | {'high': 32} |
| KXNHLSAVES | goalie_saves | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSEASONGOALS | season_player_stats | RESEARCH | quadratic/1 | 0 | 86 | 0 | 0 | greater,structured | {'low': 86} |
| KXNHLSEASONPPTS | season_player_stats | RESEARCH | quadratic/1 | 0 | 90 | 0 | 0 | greater | {'low': 90} |
| KXNHLSEASONPTS | season_player_stats | RESEARCH | quadratic/1 | 0 | 320 | 0 | 0 | greater_or_equal | {'low': 320} |
| KXNHLSERIES | playoff_series | RESEARCH | quadratic_with_maker_fees/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESGAMES | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESOT | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESSCORE | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESSPREAD | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESTOTALGOAL | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESTOTALGOALS | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSPREAD | game_spread | MODELABLE | quadratic/1 | 0 | 140 | 0 | 0 | greater | {'high': 140} |
| KXNHLTEAMTOTAL | team_total | MODELABLE | quadratic/1 | 0 | 175 | 0 | 0 | greater | {'high': 175} |
| KXNHLTOTAL | game_total | MODELABLE | quadratic/1 | 0 | 263 | 0 | 0 | greater | {'high': 263} |
| KXNHLVEZINA | season_awards | UNMODELABLE | quadratic/1 | 0 | 40 | 0 | 0 | structured | {'low': 40} |
| KXNHLWEST | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 16 | 0 | 0 | structured | {'low': 16} |
| KXNHLWINS | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLWSTREAK | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXTEAMSINSC | season_champion | RESEARCH | quadratic/1 | 0 | 256 | 0 | 0 | custom | {'low': 256} |

## Title templates per series

### KXCANADACUP — Canada winning Stanley Cup
- (1) Will a Canadian team win the NAME® by the end of the # season?
- samples: KXCANADACUP-30
- sample fields: `{"ticker": "KXCANADACUP-30", "event_ticker": "KXCANADACUP-30", "market_type": "binary", "title": "Will a Canadian team win the Stanley Cup\u00ae by the end of the 2030 season?", "subtitle": "Before 2031", "yes_sub_title": "Before 2031", "no_sub_title": "Before 2031", "status": "active", "open_time": "2025-06-13T14:00:00Z", "close_time": "2030-06-30T03:59:00Z", "expected_expiration_time": "2030-06-30T14:00:00Z", "result": "", "rules_primary": "If a Canadian hockey team wins the Stanley Cup\u00ae after Issuance and before Jun 30, 2030, then the market resolves to Yes."}`

### KXCONNSMYTHE — Conn Smythe trophy

### KXESPYNHL — BEST NHL PLAYER‬

### KXNEXTTEAMNHL — Next Team NHL
- (230) What will be NAME's next team?
- (33) What will be Connor McDavid's next team?
- samples: KXNEXTTEAMNHL-26PLAINE92-WSH, KXNEXTTEAMNHL-26PLAINE92-WPG, KXNEXTTEAMNHL-26PLAINE92-VGK, KXNEXTTEAMNHL-26PLAINE92-VAN, KXNEXTTEAMNHL-26PLAINE92-UTA, KXNEXTTEAMNHL-26PLAINE92-TOR
- sample fields: `{"ticker": "KXNEXTTEAMNHL-26PLAINE92-WSH", "event_ticker": "KXNEXTTEAMNHL-26PLAINE92", "market_type": "binary", "title": "What will be Patrik Laine's next team?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-11T19:00:00Z", "close_time": "2026-11-01T04:59:00Z", "expected_expiration_time": "2026-11-01T15:00:00Z", "result": "", "rules_primary": "If Patrik Laine's next team is Washington Capitals before Nov 1, 2026, then `

### KXNHL — Stanley Cup
- (30) NAME win the #-# NAME® Finals?
- (1) NAME. NAME win the #-# NAME® Finals?
- (1) Will Montréal Canadiens win the #-# NAME® Finals?
- samples: KXNHL-27-WSH, KXNHL-27-WPG, KXNHL-27-VGK, KXNHL-27-VAN, KXNHL-27-UTA, KXNHL-27-TOR
- sample fields: `{"ticker": "KXNHL-27-WSH", "event_ticker": "KXNHL-27", "market_type": "binary", "title": "Will Washington Capitals win the 2026-27 Stanley Cup\u00ae Finals?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-06-15T03:40:00Z", "close_time": "2029-06-30T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If Washington Capitals wins the 2026-27 Stanley Cup\u00ae Finals, then the marke`

### KXNHL1P — NHL 1st Period Winner
- (15) #st period tie
- (3) NAME wins the #st period
- (2) Dallas wins the #st period
- (2) Colorado wins the #st period
- (2) Washington wins the #st period
- (1) Montreal wins the #st period
- (1) Boston wins the #st period
- (1) Edmonton wins the #st period
- samples: KXNHL1P-26OCT14DALCOL-TIE, KXNHL1P-26OCT14DALCOL-DAL, KXNHL1P-26OCT14DALCOL-COL, KXNHL1P-26OCT14MTLWSH-WSH, KXNHL1P-26OCT14MTLWSH-TIE, KXNHL1P-26OCT14MTLWSH-MTL
- sample fields: `{"ticker": "KXNHL1P-26OCT14DALCOL-TIE", "event_ticker": "KXNHL1P-26OCT14DALCOL", "market_type": "binary", "title": "1st period tie", "yes_sub_title": "Tie", "no_sub_title": "Tie", "strike_type": "structured", "custom_strike": {"hockey_team": "570eabab-1214-4e50-a26c-880318169cce"}, "status": "active", "open_time": "2026-10-13T01:06:00Z", "close_time": "2026-10-17T00:30:00Z", "expected_expiration_time": "2026-10-15T03:30:00Z", "result": "", "rules_primary": "If neither team wins the 1st period of the Dallas vs Colorado NHL game originally scheduled for Oct 14, 2026, then the market resolves to `

### KXNHL1PBTTS — NHL Both Teams to Score in 1st Period

### KXNHL1PSPREAD — 1st Period Spread
- (3) NAME wins #st Period by over # goals
- (2) NAME R wins #st Period by over # goals
- (2) Dallas wins #st Period by over # goals
- (2) Colorado wins #st Period by over # goals
- (2) Washington wins #st Period by over # goals
- (1) Montreal wins #st Period by over # goals
- (1) Boston wins #st Period by over # goals
- (1) Edmonton wins #st Period by over # goals
- samples: KXNHL1PSPREAD-26OCT13TBNYR-NYR3, KXNHL1PSPREAD-26OCT14DALCOL-DAL2, KXNHL1PSPREAD-26OCT14DALCOL-COL2, KXNHL1PSPREAD-26OCT14MTLWSH-WSH2, KXNHL1PSPREAD-26OCT14MTLWSH-MTL2, KXNHL1PSPREAD-26OCT13BOSSJ-SJ2
- sample fields: `{"ticker": "KXNHL1PSPREAD-26OCT13TBNYR-NYR3", "event_ticker": "KXNHL1PSPREAD-26OCT13TBNYR", "market_type": "binary", "title": "New York R wins 1st Period by over 2.5 goals", "yes_sub_title": "New York R wins by over 2.5 goals", "no_sub_title": "New York R wins by over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "custom_strike": {"hockey_team": "9979553a-3962-4169-b2c3-510ba6d931d2"}, "status": "active", "open_time": "2026-10-13T23:37:19.953496Z", "close_time": "2026-10-15T23:15:00Z", "expected_expiration_time": "2026-10-14T05:15:00Z", "result": "", "rules_primary": "If New York `

### KXNHL1PTOTAL — NHL 1st Period Total
- (47) #st Period: Over # goals scored
- samples: KXNHL1PTOTAL-26OCT13TBNYR-5, KXNHL1PTOTAL-26OCT13TBNYR-4, KXNHL1PTOTAL-26OCT13SEAPHI-5, KXNHL1PTOTAL-26OCT13SEAPHI-4, KXNHL1PTOTAL-26OCT13WSHCAR-4, KXNHL1PTOTAL-26OCT14DALCOL-3
- sample fields: `{"ticker": "KXNHL1PTOTAL-26OCT13TBNYR-5", "event_ticker": "KXNHL1PTOTAL-26OCT13TBNYR", "market_type": "binary", "title": "1st Period: Over 4.5 goals scored", "yes_sub_title": "Over 4.5 goals", "no_sub_title": "Over 4.5 goals", "strike_type": "greater", "floor_strike": 4.5, "status": "active", "open_time": "2026-10-13T23:27:19.997856Z", "close_time": "2026-10-15T23:15:00Z", "expected_expiration_time": "2026-10-14T05:15:00Z", "result": "", "rules_primary": "If the teams collectively score more than 4.5 goals in the 1st Period of the Tampa Bay vs New York R NHL game originally scheduled for Oct 1`

### KXNHL1STTEAM — All NHL First Team

### KXNHL2OT — NHL Double Overtime

### KXNHL2P — NHL 2nd Period Winner
- (18) #nd period tie
- (4) NAME wins the #nd period
- (2) Dallas wins the #nd period
- (2) Colorado wins the #nd period
- (2) Washington wins the #nd period
- (2) Montreal wins the #nd period
- (1) Boston wins the #nd period
- (1) Edmonton wins the #nd period
- samples: KXNHL2P-26OCT14DALCOL-TIE, KXNHL2P-26OCT14DALCOL-DAL, KXNHL2P-26OCT14DALCOL-COL, KXNHL2P-26OCT14MTLWSH-WSH, KXNHL2P-26OCT14MTLWSH-TIE, KXNHL2P-26OCT14MTLWSH-MTL
- sample fields: `{"ticker": "KXNHL2P-26OCT14DALCOL-TIE", "event_ticker": "KXNHL2P-26OCT14DALCOL", "market_type": "binary", "title": "2nd period tie", "yes_sub_title": "Tie", "no_sub_title": "Tie", "strike_type": "structured", "custom_strike": {"hockey_team": "570eabab-1214-4e50-a26c-880318169cce"}, "status": "active", "open_time": "2026-10-13T01:06:00Z", "close_time": "2026-10-17T00:30:00Z", "expected_expiration_time": "2026-10-15T03:30:00Z", "result": "", "rules_primary": "If neither team wins the 2nd period of the Dallas vs Colorado NHL game originally scheduled for Oct 14, 2026, then the market resolves to `

### KXNHL2PBTTS — NHL Both Teams to Score in 2nd Period

### KXNHL2PSPREAD — 2nd Period Spread
- (4) NAME wins #nd Period by over # goals
- (2) Florida wins #nd Period by over # goals
- (2) Detroit wins #nd Period by over # goals
- (2) Dallas wins #nd Period by over # goals
- (2) Colorado wins #nd Period by over # goals
- (2) Washington wins #nd Period by over # goals
- (2) Montreal wins #nd Period by over # goals
- (1) Boston wins #nd Period by over # goals
- samples: KXNHL2PSPREAD-26OCT13FLACBJ-FLA3, KXNHL2PSPREAD-26OCT13NJDET-DET3, KXNHL2PSPREAD-26OCT14DALCOL-DAL2, KXNHL2PSPREAD-26OCT14DALCOL-COL2, KXNHL2PSPREAD-26OCT14MTLWSH-WSH2, KXNHL2PSPREAD-26OCT14MTLWSH-MTL2
- sample fields: `{"ticker": "KXNHL2PSPREAD-26OCT13FLACBJ-FLA3", "event_ticker": "KXNHL2PSPREAD-26OCT13FLACBJ", "market_type": "binary", "title": "Florida wins 2nd Period by over 2.5 goals", "yes_sub_title": "Florida wins by over 2.5 goals", "no_sub_title": "Florida wins by over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "custom_strike": {"hockey_team": "49b28762-c1b6-4962-a0cb-f1578510cad8"}, "status": "active", "open_time": "2026-10-13T23:35:25.547467Z", "close_time": "2026-10-15T22:15:00Z", "expected_expiration_time": "2026-10-14T04:15:00Z", "result": "", "rules_primary": "If Florida wins by `

### KXNHL2PTOTAL — 2nd Period Total
- (64) #nd Period: Over # goals scored
- samples: KXNHL2PTOTAL-26OCT13FLACBJ-6, KXNHL2PTOTAL-26OCT13TBNYR-5, KXNHL2PTOTAL-26OCT13TBNYR-4, KXNHL2PTOTAL-26OCT13NJDET-7, KXNHL2PTOTAL-26OCT13SEAPHI-5, KXNHL2PTOTAL-26OCT13SEAPHI-4
- sample fields: `{"ticker": "KXNHL2PTOTAL-26OCT13FLACBJ-6", "event_ticker": "KXNHL2PTOTAL-26OCT13FLACBJ", "market_type": "binary", "title": "2nd Period: Over 5.5 goals scored", "yes_sub_title": "Over 5.5 goals", "no_sub_title": "Over 5.5 goals", "strike_type": "greater", "floor_strike": 5.5, "status": "active", "open_time": "2026-10-13T23:35:30.907008Z", "close_time": "2026-10-15T22:15:00Z", "expected_expiration_time": "2026-10-14T04:15:00Z", "result": "", "rules_primary": "If the teams collectively score more than 5.5 goals in the 2nd Period of the Florida vs Columbus NHL game originally scheduled for Oct 13,`

### KXNHL30COMEBACK — NHL 3-0 Series Comeback

### KXNHL3P — NHL 3rd Period Winner
- (18) #rd period tie
- (4) NAME wins the #rd period
- (2) Dallas wins the #rd period
- (2) Colorado wins the #rd period
- (2) Washington wins the #rd period
- (2) Montreal wins the #rd period
- (1) Boston wins the #rd period
- (1) Edmonton wins the #rd period
- samples: KXNHL3P-26OCT14DALCOL-TIE, KXNHL3P-26OCT14DALCOL-DAL, KXNHL3P-26OCT14DALCOL-COL, KXNHL3P-26OCT14MTLWSH-WSH, KXNHL3P-26OCT14MTLWSH-TIE, KXNHL3P-26OCT14MTLWSH-MTL
- sample fields: `{"ticker": "KXNHL3P-26OCT14DALCOL-TIE", "event_ticker": "KXNHL3P-26OCT14DALCOL", "market_type": "binary", "title": "3rd period tie", "yes_sub_title": "Tie", "no_sub_title": "Tie", "strike_type": "structured", "custom_strike": {"hockey_team": "570eabab-1214-4e50-a26c-880318169cce"}, "status": "active", "open_time": "2026-10-13T01:06:00Z", "close_time": "2026-10-17T00:30:00Z", "expected_expiration_time": "2026-10-15T03:30:00Z", "result": "", "rules_primary": "If neither team wins the 3rd period (excluding overtime) of the Dallas vs Colorado NHL game originally scheduled for Oct 14, 2026, then th`

### KXNHL3PBTTS — NHL Both Teams to Score in 3rd Period

### KXNHL3PSPREAD — NHL 3rd Period Spread
- (4) NAME wins #rd Period by over # goals
- (2) Dallas wins #rd Period by over # goals
- (2) Colorado wins #rd Period by over # goals
- (2) Washington wins #rd Period by over # goals
- (2) Montreal wins #rd Period by over # goals
- (1) Boston wins #rd Period by over # goals
- (1) Edmonton wins #rd Period by over # goals
- (1) Calgary wins #rd Period by over # goals
- samples: KXNHL3PSPREAD-26OCT14DALCOL-DAL2, KXNHL3PSPREAD-26OCT14DALCOL-COL2, KXNHL3PSPREAD-26OCT14MTLWSH-WSH2, KXNHL3PSPREAD-26OCT14MTLWSH-MTL2, KXNHL3PSPREAD-26OCT13BOSSJ-SJ2, KXNHL3PSPREAD-26OCT13BOSSJ-BOS2
- sample fields: `{"ticker": "KXNHL3PSPREAD-26OCT14DALCOL-DAL2", "event_ticker": "KXNHL3PSPREAD-26OCT14DALCOL", "market_type": "binary", "title": "Dallas wins 3rd Period by over 1.5 goals", "yes_sub_title": "Dallas wins by over 1.5 goals", "no_sub_title": "Dallas wins by over 1.5 goals", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_team": "5cfee6b9-43ff-4dfa-8347-2b9de7ed51b6"}, "status": "active", "open_time": "2026-10-13T01:06:00Z", "close_time": "2026-10-17T00:30:00Z", "expected_expiration_time": "2026-10-15T03:30:00Z", "result": "", "rules_primary": "If Dallas wins by more than 1`

### KXNHL3PTOTAL — 3rd Period Total
- (66) #rd Period: Over # goals scored
- samples: KXNHL3PTOTAL-26OCT13TBNYR-5, KXNHL3PTOTAL-26OCT13TBNYR-4, KXNHL3PTOTAL-26OCT13SEAPHI-5, KXNHL3PTOTAL-26OCT13SEAPHI-4, KXNHL3PTOTAL-26OCT13WSHCAR-5, KXNHL3PTOTAL-26OCT13WSHCAR-4
- sample fields: `{"ticker": "KXNHL3PTOTAL-26OCT13TBNYR-5", "event_ticker": "KXNHL3PTOTAL-26OCT13TBNYR", "market_type": "binary", "title": "3rd Period: Over 4.5 goals scored", "yes_sub_title": "Over 4.5 goals", "no_sub_title": "Over 4.5 goals", "strike_type": "greater", "floor_strike": 4.5, "status": "active", "open_time": "2026-10-13T23:27:40.978718Z", "close_time": "2026-10-15T23:15:00Z", "expected_expiration_time": "2026-10-14T05:15:00Z", "result": "", "rules_primary": "If the teams collectively score more than 4.5 goals in the 3rd Period of the Tampa Bay vs New York R NHL game originally scheduled for Oct 1`

### KXNHL4NATIONS — 4 nations face off

### KXNHLADAMS — NHL Jack Adams Award
- (29) NAME: NAME wins
- (1) NAME: Todd McLellan wins
- (1) NAME: Peter DeBoer wins
- (1) NAME: NAME. Louis wins
- samples: KXNHLADAMS-27-TMCL, KXNHLADAMS-27-TGRE, KXNHLADAMS-27-SKEE, KXNHLADAMS-27-SCAR, KXNHLADAMS-27-SARN, KXNHLADAMS-27-RWAR
- sample fields: `{"ticker": "KXNHLADAMS-27-TMCL", "event_ticker": "KXNHLADAMS-27", "market_type": "binary", "title": "Jack Adams Award: Todd McLellan wins", "subtitle": "::", "yes_sub_title": "Todd McLellan", "no_sub_title": "Todd McLellan", "strike_type": "custom", "custom_strike": {"Person": "Todd McLellan"}, "status": "active", "open_time": "2026-09-28T22:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Todd McLellan wins the NHL Jack Adams Award in the 2026-27 NHL season, then the market resolves to Yes."}`

### KXNHLANYGOAL — Pro Hockey Goalscorer

### KXNHLAST — Pro Hockey Assists
- (594) NAME: #+ assists
- (3) Connor McDavid: #+ assists
- (2) NAME-Nygård: #+ assists
- (2) Charlie McAvoy: #+ assists
- (2) Jackson LaCombe: #+ assists
- (2) Ryan O'Reilly: #+ assists
- (2) Nathan MacKinnon: #+ assists
- (2) Jake DeBrusk: #+ assists
- samples: KXNHLAST-26OCT13NJDET-NJJHUGHES86-3, KXNHLAST-26OCT13TBNYR-NYRTKARTYE24-2, KXNHLAST-26OCT13NJDET-NJERODRIGUES17-2, KXNHLAST-26OCT13NJDET-DETEFINNIE58-2, KXNHLAST-26OCT13BUFMTL-BUFMSAMUELSSON23-2, KXNHLAST-26OCT13EDMLA-LASHELENIUS79-1
- sample fields: `{"ticker": "KXNHLAST-26OCT13NJDET-NJJHUGHES86-3", "event_ticker": "KXNHLAST-26OCT13NJDET", "market_type": "binary", "title": "Jack Hughes: 3+ assists", "yes_sub_title": "Jack Hughes: 3+", "no_sub_title": "Jack Hughes: 3+", "strike_type": "greater", "floor_strike": 2.5, "custom_strike": {"hockey_player": "b4724182-6ce5-4abc-962a-44fba35e8abf", "hockey_team": "25df3a21-8554-4e7d-a3cc-8633360d6d51"}, "status": "active", "open_time": "2026-10-13T23:32:12.561598Z", "close_time": "2026-10-15T22:00:00Z", "expected_expiration_time": "2026-10-14T04:00:00Z", "result": "", "rules_primary": "If Jack Hughe`

### KXNHLATLANTIC — NHL Atlantic Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLATLANTIC-27-TOR, KXNHLATLANTIC-27-TB, KXNHLATLANTIC-27-OTT, KXNHLATLANTIC-27-MTL, KXNHLATLANTIC-27-FLA, KXNHLATLANTIC-27-DET
- sample fields: `{"ticker": "KXNHLATLANTIC-27-TOR", "event_ticker": "KXNHLATLANTIC-27", "market_type": "binary", "title": "Will the Toronto Maple Leafs win the Atlantic Division?", "yes_sub_title": "Toronto Maple Leafs", "no_sub_title": "Toronto Maple Leafs", "strike_type": "structured", "custom_strike": {"hockey_team": "f61f9daa-407b-4c46-96e8-feee19cd6f51"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Toronto Maple Leafs win the 2026-27 NHL Atlantic Division, then the `

### KXNHLCALDER — NHL Calder Memorial Trophy
- (36) NAME: NAME wins
- (1) NAME: Viggo Björck wins
- (1) NAME: NAME-Nygård wins
- (1) NAME: Gavin McKenna wins
- (1) NAME: Adam Engström wins
- samples: KXNHLCALDER-27-ZBUIUM24, KXNHLCALDER-27-VEKLUND, KXNHLCALDER-27-VBJORCK, KXNHLCALDER-27-TLINDSTEIN, KXNHLCALDER-27-TIGINLA, KXNHLCALDER-27-TCONNELLY
- sample fields: `{"ticker": "KXNHLCALDER-27-ZBUIUM24", "event_ticker": "KXNHLCALDER-27", "market_type": "binary", "title": "Calder Memorial Trophy: Zeev Buium wins", "subtitle": "::", "yes_sub_title": "Zeev Buium", "no_sub_title": "Zeev Buium", "strike_type": "structured", "custom_strike": {"hockey_player": "4e4ad45c-1cda-4e0b-89c3-4e6c27740027"}, "status": "active", "open_time": "2026-09-30T17:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Zeev Buium wins the NHL Calder Memorial Trophy in the 2026-27 NHL season, then the ma`

### KXNHLCENTRAL — NHL Central Division Winner
- (7) Will the NAME win the NAME?
- (1) Will the St. NAME win the NAME?
- samples: KXNHLCENTRAL-27-WPG, KXNHLCENTRAL-27-UTA, KXNHLCENTRAL-27-STL, KXNHLCENTRAL-27-NSH, KXNHLCENTRAL-27-MIN, KXNHLCENTRAL-27-DAL
- sample fields: `{"ticker": "KXNHLCENTRAL-27-WPG", "event_ticker": "KXNHLCENTRAL-27", "market_type": "binary", "title": "Will the Winnipeg Jets win the Central Division?", "yes_sub_title": "Winnipeg Jets", "no_sub_title": "Winnipeg Jets", "strike_type": "structured", "custom_strike": {"hockey_team": "6f769f6d-161e-43d3-a586-db5451c5050e"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Winnipeg Jets win the 2026-27 NHL Central Division, then the market resolves to Yes."}`

### KXNHLDRAFTPICK — Pro Hockey Draft Pick

### KXNHLDRAFTTOP — Pro Hockey Top Pick

### KXNHLEAST — Eastern Conference Championship
- (16) Will the NAME win the NAME?
- samples: KXNHLEAST-27-WSH, KXNHLEAST-27-TOR, KXNHLEAST-27-TB, KXNHLEAST-27-PIT, KXNHLEAST-27-PHI, KXNHLEAST-27-OTT
- sample fields: `{"ticker": "KXNHLEAST-27-WSH", "event_ticker": "KXNHLEAST-27", "market_type": "binary", "title": "Will the Washington Capitals win the Eastern Conference Finals?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-07-06T20:00:00Z", "close_time": "2027-07-15T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Eastern Conference Finals, t`

### KXNHLEXPANSION — NHL Expansion
- (1) NAME receive an NHL expansion team before #?
- samples: KXNHLEXPANSION-27JAN01HOU-Y
- sample fields: `{"ticker": "KXNHLEXPANSION-27JAN01HOU-Y", "event_ticker": "KXNHLEXPANSION-27JAN01HOU", "market_type": "binary", "title": "Will Houston receive an NHL expansion team before 2027?", "yes_sub_title": "Houston to get an expansion team before 2027", "no_sub_title": "Houston to get an expansion team before 2027", "status": "active", "open_time": "2026-09-01T01:00:00Z", "close_time": "2027-01-01T04:59:00Z", "expected_expiration_time": "2027-01-01T15:00:00Z", "result": "", "rules_primary": "If the NHL officially announces the award of an expansion team franchise to Houston before Jan 1, 2027, then the`

### KXNHLF10G — NHL Goal in First 10 Minutes
- (12) Either team to score in the first # minutes
- samples: KXNHLF10G-26OCT14DALCOL-Y, KXNHLF10G-26OCT14MTLWSH-Y, KXNHLF10G-26OCT13BOSSJ-Y, KXNHLF10G-26OCT13EDMLA-Y, KXNHLF10G-26OCT13CGYANA-Y, KXNHLF10G-26OCT13TORUTA-Y
- sample fields: `{"ticker": "KXNHLF10G-26OCT14DALCOL-Y", "event_ticker": "KXNHLF10G-26OCT14DALCOL", "market_type": "binary", "title": "Either team to score in the first 10 minutes", "yes_sub_title": "Goal in first 10 min", "no_sub_title": "Goal in first 10 min", "strike_type": "greater_or_equal", "floor_strike": 1, "status": "active", "open_time": "2026-10-13T01:06:00Z", "close_time": "2026-10-17T00:30:00Z", "expected_expiration_time": "2026-10-15T03:30:00Z", "result": "", "rules_primary": "If at least 1 goal is scored by either Dallas or Colorado during the first 10 minutes of the first period (from 0:00 elap`

### KXNHLFINALSEXACT — NHL Championship Series Score

### KXNHLFIRSTGOAL — NHL First Goal
- (341) NAME: NAME
- (1) JJ Peterka: NAME
- (1) Charlie McAvoy: NAME
- (1) Connor McDavid: NAME
- (1) Jackson LaCombe: NAME
- (1) A.J. Greer: NAME
- (1) MacKenzie Weegar: NAME
- (1) Jack McBain: NAME
- samples: KXNHLFIRSTGOAL-26OCT13STLOTT-OTTJDONOVAN56, KXNHLFIRSTGOAL-26OCT13VGKNSH-NSHVPINCHUK51, KXNHLFIRSTGOAL-26OCT13BOSSJ-BOSMLOHREI6, KXNHLFIRSTGOAL-26OCT13BOSSJ-BOSFBRUNET42, KXNHLFIRSTGOAL-26OCT13BOSSJ-SJZOSTAPCHUK63, KXNHLFIRSTGOAL-26OCT13BOSSJ-SJWSMITH2
- sample fields: `{"ticker": "KXNHLFIRSTGOAL-26OCT13STLOTT-OTTJDONOVAN56", "event_ticker": "KXNHLFIRSTGOAL-26OCT13STLOTT", "market_type": "binary", "title": "Jorian Donovan: First Goalscorer", "yes_sub_title": "Jorian Donovan", "no_sub_title": "Jorian Donovan", "strike_type": "structured", "custom_strike": {"hockey_player": "5252336e-d1a9-46ba-8e3d-bdb38381ed40", "hockey_team": "a2478063-2ded-4657-923b-e59de696ad21"}, "status": "active", "open_time": "2026-10-13T23:22:00Z", "close_time": "2026-10-15T23:30:00Z", "expected_expiration_time": "2026-10-14T05:30:00Z", "result": "", "rules_primary": "If Jorian Donovan`

### KXNHLGAME — NHL Game
- (12) NAME wins
- (4) Utah wins
- (4) Pittsburgh wins
- (4) Toronto wins
- (4) NAME R wins
- (4) Philadelphia wins
- (4) Colorado wins
- (3) Anaheim wins
- samples: KXNHLGAME-26OCT19PITUTA-UTA, KXNHLGAME-26OCT19PITUTA-PIT, KXNHLGAME-26OCT19SJTOR-TOR, KXNHLGAME-26OCT19SJTOR-SJ, KXNHLGAME-26OCT19ANANYR-NYR, KXNHLGAME-26OCT19ANANYR-ANA
- sample fields: `{"ticker": "KXNHLGAME-26OCT19PITUTA-UTA", "event_ticker": "KXNHLGAME-26OCT19PITUTA", "market_type": "binary", "title": "Utah wins", "yes_sub_title": "Utah", "no_sub_title": "Utah", "strike_type": "structured", "custom_strike": {"hockey_team": "7d20591d-c6fa-4b85-8d69-ff05fb3649ac"}, "status": "active", "open_time": "2026-10-13T01:06:00Z", "close_time": "2026-10-22T01:00:00Z", "expected_expiration_time": "2026-10-20T04:00:00Z", "result": "", "rules_primary": "If Utah wins the Pittsburgh vs Utah NHL game originally scheduled for Oct 19, 2026, then the market resolves to Yes."}`

### KXNHLGOAL — NHL Goalscorer
- (930) NAME: #+ goals
- (3) Connor McDavid: #+ goals
- (3) Ryan O'Reilly: #+ goals
- (3) Nathan MacKinnon: #+ goals
- (3) Jared McCann: #+ goals
- (3) Bobby McMann: #+ goals
- (3) Juraj Slafkovský: #+ goals
- (3) Alex DeBrincat: #+ goals
- samples: KXNHLGOAL-26OCT13VANNYI-NYIMKESSEL-1, KXNHLGOAL-26OCT13STLOTT-OTTJDONOVAN56-1, KXNHLGOAL-26OCT13TBNYR-TBJVIEL25-1, KXNHLGOAL-26OCT13FLACBJ-FLAUBALINSKIS26-1, KXNHLGOAL-26OCT13NJDET-NJJKOVACEVIC8-1, KXNHLGOAL-26OCT13VGKNSH-NSHVPINCHUK51-2
- sample fields: `{"ticker": "KXNHLGOAL-26OCT13VANNYI-NYIMKESSEL-1", "event_ticker": "KXNHLGOAL-26OCT13VANNYI", "market_type": "binary", "title": "Matthew Kessel: 1+ goals", "yes_sub_title": "Matthew Kessel: 1+", "no_sub_title": "Matthew Kessel: 1+", "strike_type": "greater", "floor_strike": 0.5, "custom_strike": {"hockey_player": "a30a6bf7-3c96-4e34-9434-afc39214bcba", "hockey_team": "03f52887-5bb7-4b51-954e-433f73474350"}, "status": "active", "open_time": "2026-10-13T23:37:00Z", "close_time": "2026-10-15T23:45:00Z", "expected_expiration_time": "2026-10-14T05:45:00Z", "result": "", "rules_primary": "If Matthew`

### KXNHLHART — NHL Hart Memorial Trophy
- (28) Who will win NAME?
- samples: KXNHLHART-27-WNYLANDER88, KXNHLHART-27-SCROSBY87, KXNHLHART-27-QHUGHES43, KXNHLHART-27-PDOROFEYEV16, KXNHLHART-27-NSUZUKI14, KXNHLHART-27-NMACKINNON29
- sample fields: `{"ticker": "KXNHLHART-27-WNYLANDER88", "event_ticker": "KXNHLHART-27", "market_type": "binary", "title": "Who will win Hart Memorial Trophy?", "subtitle": "::", "yes_sub_title": "William Nylander", "no_sub_title": "William Nylander", "strike_type": "structured", "custom_strike": {"hockey_player": "1d6e76e2-3553-4992-b4f1-14e075811859"}, "status": "active", "open_time": "2026-06-29T20:00:00Z", "close_time": "2027-06-30T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If William Nylander wins the NHL Hart Memorial Trophy in the 2026-27 NHL season, t`

### KXNHLLINDSAY — NHL Ted Lindsay Winner
- (26) NAME: NAME wins
- (1) NAME: Nathan MacKinnon wins
- (1) NAME: Connor McDavid wins
- samples: KXNHLLINDSAY-27-WNYLANDER88, KXNHLLINDSAY-27-SCROSBY87, KXNHLLINDSAY-27-QHUGHES43, KXNHLLINDSAY-27-PDOROFEYEV16, KXNHLLINDSAY-27-NSUZUKI14, KXNHLLINDSAY-27-NMACKINNON29
- sample fields: `{"ticker": "KXNHLLINDSAY-27-WNYLANDER88", "event_ticker": "KXNHLLINDSAY-27", "market_type": "binary", "title": "Ted Lindsay Award: William Nylander wins", "subtitle": "::", "yes_sub_title": "William Nylander", "no_sub_title": "William Nylander", "strike_type": "structured", "custom_strike": {"hockey_player": "1d6e76e2-3553-4992-b4f1-14e075811859"}, "status": "active", "open_time": "2026-10-08T02:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If William Nylander wins the NHL Ted Lindsay Award in the 2026-27 NHL `

### KXNHLMENTION — NHL Announcer Mentions

### KXNHLMETROPOLITAN — NHL Metropolitan Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLMETROPOLITAN-27-WSH, KXNHLMETROPOLITAN-27-PIT, KXNHLMETROPOLITAN-27-PHI, KXNHLMETROPOLITAN-27-NYR, KXNHLMETROPOLITAN-27-NYI, KXNHLMETROPOLITAN-27-NJ
- sample fields: `{"ticker": "KXNHLMETROPOLITAN-27-WSH", "event_ticker": "KXNHLMETROPOLITAN-27", "market_type": "binary", "title": "Will the Washington Capitals win the Metropolitan Division?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Metropolitan Div`

### KXNHLMVP — NHL Hart Memorial Trophy Winner

### KXNHLNEXTGM — Next NHL GM

### KXNHLNEXTTEAM — NHL Next Team
- (31) NAME' next team before Nov #, #: NAME
- (1) NAME' next team before Nov #, #: St. NAME
- (1) NAME' next team before Nov #, #: Retires / NAME
- samples: KXNHLNEXTTEAM-26QHUGHES43-WSH, KXNHLNEXTTEAM-26QHUGHES43-WPG, KXNHLNEXTTEAM-26QHUGHES43-VGK, KXNHLNEXTTEAM-26QHUGHES43-VAN, KXNHLNEXTTEAM-26QHUGHES43-UTA, KXNHLNEXTTEAM-26QHUGHES43-TOR
- sample fields: `{"ticker": "KXNHLNEXTTEAM-26QHUGHES43-WSH", "event_ticker": "KXNHLNEXTTEAM-26QHUGHES43", "market_type": "binary", "title": "Quinn Hughes' next team before Nov 1, 2026: Washington Capitals", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-26T00:00:00Z", "close_time": "2026-11-01T04:59:00Z", "expected_expiration_time": "2026-11-01T15:00:00Z", "result": "", "rules_primary": "If Quinn Hughes' \nnext team is the Washington Ca`

### KXNHLNORRIS — NHL James Norris Memorial Trophy
- (28) NAME: NAME wins
- (1) NAME: Jackson LaCombe wins
- (1) NAME: Charlie McAvoy wins
- samples: KXNHLNORRIS-27-ZWERENSKI8, KXNHLNORRIS-27-VHEDMAN77, KXNHLNORRIS-27-THARLEY55, KXNHLNORRIS-27-STHEODORE27, KXNHLNORRIS-27-RSANDIN38, KXNHLNORRIS-27-RJOSI59
- sample fields: `{"ticker": "KXNHLNORRIS-27-ZWERENSKI8", "event_ticker": "KXNHLNORRIS-27", "market_type": "binary", "title": "James Norris Memorial Trophy: Zach Werenski wins", "subtitle": "::", "yes_sub_title": "Zach Werenski", "no_sub_title": "Zach Werenski", "strike_type": "structured", "custom_strike": {"hockey_player": "036e0c69-c86a-4ab1-8f63-c6d55b72fe09"}, "status": "active", "open_time": "2026-09-01T19:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Zach Werenski wins the NHL James Norris Memorial Trophy in the 2026-`

### KXNHLOT — NHL Overtime
- (18) Game goes to overtime
- samples: KXNHLOT-26OCT14DALCOL-1, KXNHLOT-26OCT14MTLWSH-1, KXNHLOT-26OCT13BOSSJ-1, KXNHLOT-26OCT13EDMLA-1, KXNHLOT-26OCT13CGYANA-1, KXNHLOT-26OCT13TORUTA-1
- sample fields: `{"ticker": "KXNHLOT-26OCT14DALCOL-1", "event_ticker": "KXNHLOT-26OCT14DALCOL", "market_type": "binary", "title": "Game goes to overtime", "yes_sub_title": "Game goes to overtime", "no_sub_title": "Game goes to overtime", "strike_type": "greater", "floor_strike": 0.5, "status": "active", "open_time": "2026-10-13T01:06:00Z", "close_time": "2026-10-17T00:30:00Z", "expected_expiration_time": "2026-10-15T03:30:00Z", "result": "", "rules_primary": "If at least 1 overtime period is played in the Dallas vs Colorado NHL game originally scheduled for Oct 14, 2026, then the market resolves to Yes."}`

### KXNHLOVERTIME — NHL Overtime

### KXNHLPACIFIC — NHL Pacific Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLPACIFIC-27-VGK, KXNHLPACIFIC-27-VAN, KXNHLPACIFIC-27-SJ, KXNHLPACIFIC-27-SEA, KXNHLPACIFIC-27-LA, KXNHLPACIFIC-27-EDM
- sample fields: `{"ticker": "KXNHLPACIFIC-27-VGK", "event_ticker": "KXNHLPACIFIC-27", "market_type": "binary", "title": "Will the Vegas Golden Knights win the Pacific Division?", "yes_sub_title": "Vegas Golden Knights", "no_sub_title": "Vegas Golden Knights", "strike_type": "structured", "custom_strike": {"hockey_team": "d599b5cc-5e06-4679-9303-4d5dad7c4cce"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Vegas Golden Knights win the 2026-27 NHL Pacific Division, then the `

### KXNHLPLAYOFF — Playoff Qualifier
- (30) Will the NAME qualify for the playoffs in the #-# NHL season?
- (1) Will the St. NAME qualify for the playoffs in the #-# NHL season?
- (1) Will the Montréal Canadiens qualify for the playoffs in the #-# NHL season?
- samples: KXNHLPLAYOFF-27-WSH, KXNHLPLAYOFF-27-WPG, KXNHLPLAYOFF-27-VGK, KXNHLPLAYOFF-27-VAN, KXNHLPLAYOFF-27-UTA, KXNHLPLAYOFF-27-TOR
- sample fields: `{"ticker": "KXNHLPLAYOFF-27-WSH", "event_ticker": "KXNHLPLAYOFF-27", "market_type": "binary", "title": "Will the Washington Capitals qualify for the playoffs in the 2026-27 NHL season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-18T20:00:00Z", "close_time": "2027-04-25T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals qualify for the playoffs `

### KXNHLPLAYOFFGOALS — NHL Playoffs Goal Leader (by Round)

### KXNHLPRES — NHL President's Trophy Winner
- (30) Will the NAME win the Presidents' Trophy?
- (1) Will the St. NAME win the Presidents' Trophy?
- (1) Will the Montréal Canadiens win the Presidents' Trophy?
- samples: KXNHLPRES-27-WSH, KXNHLPRES-27-WPG, KXNHLPRES-27-VGK, KXNHLPRES-27-VAN, KXNHLPRES-27-UTA, KXNHLPRES-27-TOR
- sample fields: `{"ticker": "KXNHLPRES-27-WSH", "event_ticker": "KXNHLPRES-27", "market_type": "binary", "title": "Will the Washington Capitals win the Presidents' Trophy?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-14T20:00:00Z", "close_time": "2027-04-25T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Presidents' Trophy, then the market`

### KXNHLPRICE — NHL Ticket Prices

### KXNHLPSEASONGOALS — Player Goals Scored in Season
- (17) NAME: #+ goals in #-# NHL regular season?
- samples: KXNHLPSEASONGOALS-27MCELEBRINI71-60, KXNHLPSEASONGOALS-27MCELEBRINI71-55, KXNHLPSEASONGOALS-27MCELEBRINI71-50, KXNHLPSEASONGOALS-27MCELEBRINI71-45, KXNHLPSEASONGOALS-27MCELEBRINI71-40, KXNHLPSEASONGOALS-27MCELEBRINI71-35
- sample fields: `{"ticker": "KXNHLPSEASONGOALS-27MCELEBRINI71-60", "event_ticker": "KXNHLPSEASONGOALS-27MCELEBRINI71", "market_type": "binary", "title": "Macklin Celebrini: 60+ goals in 2026-27 NHL regular season?", "subtitle": "Macklin Celebrini", "yes_sub_title": "60+ goals", "no_sub_title": "60+ goals", "strike_type": "greater", "floor_strike": 59.5, "custom_strike": {"hockey_player": "264560c4-3624-4c01-924e-879a08799f16"}, "status": "active", "open_time": "2026-10-09T01:30:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If Mac`

### KXNHLPTS — Pro Hockey Points
- (800) NAME: #+ points
- (3) NAME-Nygård: #+ points
- (3) Charlie McAvoy: #+ points
- (3) Connor McDavid: #+ points
- (3) Jackson LaCombe: #+ points
- (3) Ryan O'Reilly: #+ points
- (3) Nathan MacKinnon: #+ points
- (3) Jared McCann: #+ points
- samples: KXNHLPTS-26OCT13NJDET-NJAMANTHA39-3, KXNHLPTS-26OCT13NJDET-NJERODRIGUES17-3, KXNHLPTS-26OCT13NJDET-DETMBRANDSEGGNYGRD28-3, KXNHLPTS-26OCT13NJDET-DETEFINNIE58-3, KXNHLPTS-26OCT13EDMLA-LASHELENIUS79-1, KXNHLPTS-26OCT13EDMLA-LAALEE47-1
- sample fields: `{"ticker": "KXNHLPTS-26OCT13NJDET-NJAMANTHA39-3", "event_ticker": "KXNHLPTS-26OCT13NJDET", "market_type": "binary", "title": "Anthony Mantha: 3+ points", "yes_sub_title": "Anthony Mantha: 3+", "no_sub_title": "Anthony Mantha: 3+", "strike_type": "greater", "floor_strike": 2.5, "custom_strike": {"hockey_player": "c7d2779d-ac11-42c1-8e4b-8e0115af6b4d", "hockey_team": "25df3a21-8554-4e7d-a3cc-8633360d6d51"}, "status": "active", "open_time": "2026-10-13T23:29:15.605112Z", "close_time": "2026-10-15T22:00:00Z", "expected_expiration_time": "2026-10-14T04:00:00Z", "result": "", "rules_primary": "If An`

### KXNHLRECORDWORST — Worst NHL Record
- (30) Will the NAME have the worst regular season record in the #-# season?
- (1) Will the St. NAME have the worst regular season record in the #-# season?
- (1) Will the Montréal Canadiens have the worst regular season record in the #-# season?
- samples: KXNHLRECORDWORST-27-WSH, KXNHLRECORDWORST-27-WPG, KXNHLRECORDWORST-27-VGK, KXNHLRECORDWORST-27-VAN, KXNHLRECORDWORST-27-UTA, KXNHLRECORDWORST-27-TOR
- sample fields: `{"ticker": "KXNHLRECORDWORST-27-WSH", "event_ticker": "KXNHLRECORDWORST-27", "market_type": "binary", "title": "Will the Washington Capitals have the worst regular season record in the 2026-27 season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-29T16:00:00Z", "close_time": "2027-05-31T14:00:00Z", "expected_expiration_time": "2027-05-01T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals have the `

### KXNHLRETIRE — NHL Retire

### KXNHLRICHARD — NHL Maurice "Rocket" Richard Trophy
- (37) Maurice "Rocket" NAME: NAME wins
- (1) Maurice "Rocket" NAME: Nathan MacKinnon wins
- (1) Maurice "Rocket" NAME: Connor McDavid wins
- (1) Maurice "Rocket" NAME: Alex DeBrincat wins
- samples: KXNHLRICHARD-27-ZHYMAN18, KXNHLRICHARD-27-WNYLANDER88, KXNHLRICHARD-27-WJOHNSTON53, KXNHLRICHARD-27-TTHOMPSON72, KXNHLRICHARD-27-SSTAMKOS91, KXNHLRICHARD-27-SREINHART13
- sample fields: `{"ticker": "KXNHLRICHARD-27-ZHYMAN18", "event_ticker": "KXNHLRICHARD-27", "market_type": "binary", "title": "Maurice \"Rocket\" Richard Trophy: Zach Hyman wins", "subtitle": "::", "yes_sub_title": "Zach Hyman", "no_sub_title": "Zach Hyman", "strike_type": "structured", "custom_strike": {"hockey_player": "2c3d67df-721b-4ea4-8aee-dea4a9715c82"}, "status": "active", "open_time": "2026-09-01T19:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Zach Hyman wins the NHL Maurice \"Rocket\" Richard Award in the 2026-27 `

### KXNHLROSS — NHL Art Ross Trophy
- (38) NAME: NAME wins
- (1) NAME: Nathan MacKinnon wins
- (1) NAME: Connor McDavid wins
- samples: KXNHLROSS-27-WNYLANDER88, KXNHLROSS-27-WJOHNSTON53, KXNHLROSS-27-TTHOMPSON72, KXNHLROSS-27-TSTUTZLE18, KXNHLROSS-27-SREINHART13, KXNHLROSS-27-SJARVIS24
- sample fields: `{"ticker": "KXNHLROSS-27-WNYLANDER88", "event_ticker": "KXNHLROSS-27", "market_type": "binary", "title": "Art Ross Trophy: William Nylander wins", "subtitle": "::", "yes_sub_title": "William Nylander", "no_sub_title": "William Nylander", "strike_type": "structured", "custom_strike": {"hockey_player": "1d6e76e2-3553-4992-b4f1-14e075811859"}, "status": "active", "open_time": "2026-09-01T19:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If William Nylander wins the NHL Art Ross Trophy in the 2026-27 NHL season, th`

### KXNHLSAVE — Goaltender Saves
- (31) NAME: #+ saves
- (1) Leevi Meriläinen: #+ saves
- samples: KXNHLSAVE-26OCT13SEAPHI-SEAPGRUBAUER31-25, KXNHLSAVE-26OCT13BUFMTL-BUFULUUKKONEN1-25, KXNHLSAVE-26OCT13EDMLA-EDMDLEVI27-26, KXNHLSAVE-26OCT13BOSSJ-BOSJSWAYMAN1-25, KXNHLSAVE-26OCT13BOSSJ-SJYASKAROV30-25, KXNHLSAVE-26OCT13EDMLA-LADKUEMPER35-25
- sample fields: `{"ticker": "KXNHLSAVE-26OCT13SEAPHI-SEAPGRUBAUER31-25", "event_ticker": "KXNHLSAVE-26OCT13SEAPHI", "market_type": "binary", "title": "Philipp Grubauer: 25+ saves", "yes_sub_title": "Philipp Grubauer: 25+", "no_sub_title": "Philipp Grubauer: 25+", "strike_type": "greater", "floor_strike": 24.5, "custom_strike": {"hockey_player": "e69dc9e2-b350-4ce5-8cd9-9296af03e100", "hockey_team": "2ed1104c-eb5a-4175-9f05-0561caaa59d2"}, "status": "active", "open_time": "2026-10-13T22:52:00Z", "close_time": "2026-10-15T23:00:00Z", "expected_expiration_time": "2026-10-14T05:00:00Z", "result": "", "rules_primar`

### KXNHLSAVES — Pro Hockey Saves

### KXNHLSEASONGOALS — Player to score X Goals in Season
- (80) NAME: #+ goals in #-# NHL regular season?
- (2) Nathan MacKinnon: #+ goals in #-# NHL regular season?
- (2) Connor McDavid: #+ goals in #-# NHL regular season?
- (2) Alex DeBrincat: #+ goals in #-# NHL regular season?
- samples: KXNHLSEASONGOALS-27C20-WSMITH2, KXNHLSEASONGOALS-27C20-SCROSBY87, KXNHLSEASONGOALS-27C20-PKANE88, KXNHLSEASONGOALS-27C20-MSCHAEFER48, KXNHLSEASONGOALS-27C20-FNAZAR91, KXNHLSEASONGOALS-27C20-EMALKIN71
- sample fields: `{"ticker": "KXNHLSEASONGOALS-27C20-WSMITH2", "event_ticker": "KXNHLSEASONGOALS-27C20", "market_type": "binary", "title": "Will Smith: 20+ goals in 2026-27 NHL regular season?", "subtitle": "Will Smith:: SJ Sharks", "yes_sub_title": "Will Smith", "no_sub_title": "Will Smith", "strike_type": "greater", "floor_strike": 19.5, "custom_strike": {"hockey_player": "18850cdd-34e1-4d85-b612-2164e2edb066"}, "status": "active", "open_time": "2026-09-16T18:45:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If Will Smith scores `

### KXNHLSEASONPPTS — Season Player Points
- (84) NAME: #+ points in #-# NHL regular season?
- (3) Nathan MacKinnon: #+ points in #-# NHL regular season?
- (3) Connor McDavid: #+ points in #-# NHL regular season?
- samples: KXNHLSEASONPPTS-27C110-ZWERENSKI8, KXNHLSEASONPPTS-27C110-WNYLANDER88, KXNHLSEASONPPTS-27C110-WJOHNSTON53, KXNHLSEASONPPTS-27C110-TSTUTZLE18, KXNHLSEASONPPTS-27C110-SCROSBY87, KXNHLSEASONPPTS-27C110-NSUZUKI14
- sample fields: `{"ticker": "KXNHLSEASONPPTS-27C110-ZWERENSKI8", "event_ticker": "KXNHLSEASONPPTS-27C110", "market_type": "binary", "title": "Zach Werenski: 110+ points in 2026-27 NHL regular season?", "subtitle": "Zach Werenski:: Columbus Blue Jackets", "yes_sub_title": "Zach Werenski", "no_sub_title": "Zach Werenski", "strike_type": "greater", "floor_strike": 109.5, "custom_strike": {"hockey_player": "036e0c69-c86a-4ab1-8f63-c6d55b72fe09"}, "status": "active", "open_time": "2026-09-28T17:00:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_pr`

### KXNHLSEASONPTS — NHL Season Point Totals
- (10) Will the WSH Capitals NHL team earn at least # points in the #-# regular season?
- (10) Will the WPG Jets NHL team earn at least # points in the #-# regular season?
- (10) Will the VGK NAME NHL team earn at least # points in the #-# regular season?
- (10) Will the VAN Canucks NHL team earn at least # points in the #-# regular season?
- (10) Will the UTA Mammoth NHL team earn at least # points in the #-# regular season?
- (10) Will the TOR NAME NHL team earn at least # points in the #-# regular season?
- (10) Will the TB Lightning NHL team earn at least # points in the #-# regular season?
- (10) Will the STL Blues NHL team earn at least # points in the #-# regular season?
- samples: KXNHLSEASONPTS-27WSH-95, KXNHLSEASONPTS-27WSH-90, KXNHLSEASONPTS-27WSH-85, KXNHLSEASONPTS-27WSH-80, KXNHLSEASONPTS-27WSH-75, KXNHLSEASONPTS-27WSH-70
- sample fields: `{"ticker": "KXNHLSEASONPTS-27WSH-95", "event_ticker": "KXNHLSEASONPTS-27WSH", "market_type": "binary", "title": "Will the WSH Capitals NHL team earn at least 95 points in the 2026-27 regular season?", "yes_sub_title": "95+ points", "no_sub_title": "95+ points", "strike_type": "greater_or_equal", "floor_strike": 95, "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-26T00:47:00Z", "close_time": "2027-04-18T14:00:00Z", "expected_expiration_time": "2027-04-18T14:00:00Z", "result": "", "rules_primary": "If the WSH Capitals earn at le`

### KXNHLSERIES — NHL Series Winner

### KXNHLSERIESGAMES — NHL Series Total Games

### KXNHLSERIESOT — NHL Series Overtime

### KXNHLSERIESSCORE — NHL Series Exact Score

### KXNHLSERIESSPREAD — NHL Series Game Spread

### KXNHLSERIESTOTALGOAL — NHL Series Total Goals

### KXNHLSERIESTOTALGOALS — NHL Series Total Goals

### KXNHLSPREAD — NHL Spread
- (18) NAME wins by over # goals
- (6) Florida wins by over # goals
- (6) St. Louis wins by over # goals
- (6) NAME R wins by over # goals
- (6) Seattle wins by over # goals
- (6) Washington wins by over # goals
- (6) Detroit wins by over # goals
- (6) Buffalo wins by over # goals
- samples: KXNHLSPREAD-26OCT13FLACBJ-FLA5, KXNHLSPREAD-26OCT13FLACBJ-FLA4, KXNHLSPREAD-26OCT13STLOTT-STL5, KXNHLSPREAD-26OCT13STLOTT-STL4, KXNHLSPREAD-26OCT13TBNYR-NYR5, KXNHLSPREAD-26OCT13TBNYR-NYR4
- sample fields: `{"ticker": "KXNHLSPREAD-26OCT13FLACBJ-FLA5", "event_ticker": "KXNHLSPREAD-26OCT13FLACBJ", "market_type": "binary", "title": "Florida wins by over 4.5 goals", "yes_sub_title": "Florida wins by over 4.5 goals", "no_sub_title": "Florida wins by over 4.5 goals", "strike_type": "greater", "floor_strike": 4.5, "custom_strike": {"hockey_team": "49b28762-c1b6-4962-a0cb-f1578510cad8"}, "status": "active", "open_time": "2026-10-13T23:35:41Z", "close_time": "2026-10-15T22:15:00Z", "expected_expiration_time": "2026-10-14T04:15:00Z", "result": "", "rules_primary": "If Florida wins by over 4.5 goals in the `

### KXNHLTEAMTOTAL — NHL Team Goals Scored During Game
- (17) NAME over # goals scored
- (10) Dallas over # goals scored
- (10) Colorado over # goals scored
- (10) Washington over # goals scored
- (10) Montreal over # goals scored
- (5) Boston over # goals scored
- (5) Edmonton over # goals scored
- (5) Calgary over # goals scored
- samples: KXNHLTEAMTOTAL-26OCT14DALCOL-DAL6, KXNHLTEAMTOTAL-26OCT14DALCOL-DAL5, KXNHLTEAMTOTAL-26OCT14DALCOL-DAL4, KXNHLTEAMTOTAL-26OCT14DALCOL-DAL3, KXNHLTEAMTOTAL-26OCT14DALCOL-DAL2, KXNHLTEAMTOTAL-26OCT14DALCOL-COL6
- sample fields: `{"ticker": "KXNHLTEAMTOTAL-26OCT14DALCOL-DAL6", "event_ticker": "KXNHLTEAMTOTAL-26OCT14DALCOL", "market_type": "binary", "title": "Dallas over 5.5 goals scored", "yes_sub_title": "Dallas over 5.5", "no_sub_title": "Dallas over 5.5", "strike_type": "greater", "floor_strike": 5.5, "custom_strike": {"hockey_team": "5cfee6b9-43ff-4dfa-8347-2b9de7ed51b6"}, "status": "active", "open_time": "2026-10-13T01:06:00Z", "close_time": "2026-10-17T00:30:00Z", "expected_expiration_time": "2026-10-15T03:30:00Z", "result": "", "rules_primary": "If Dallas scores over 5.5 goals in the Dallas vs Colorado NHL game `

### KXNHLTOTAL — NHL Total Goals
- (263) NAME: Over # goals scored
- samples: KXNHLTOTAL-26OCT13NJDET-12, KXNHLTOTAL-26OCT13NJDET-11, KXNHLTOTAL-26OCT15CGYVGK-9, KXNHLTOTAL-26OCT15CGYVGK-8, KXNHLTOTAL-26OCT15CGYVGK-7, KXNHLTOTAL-26OCT15CGYVGK-6
- sample fields: `{"ticker": "KXNHLTOTAL-26OCT13NJDET-12", "event_ticker": "KXNHLTOTAL-26OCT13NJDET", "market_type": "binary", "title": "Full Game: Over 11.5 goals scored", "yes_sub_title": "Over 11.5 goals scored", "no_sub_title": "Over 11.5 goals scored", "strike_type": "greater", "floor_strike": 11.5, "status": "active", "open_time": "2026-10-13T23:15:24Z", "close_time": "2026-10-15T22:00:00Z", "expected_expiration_time": "2026-10-14T04:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 11.5 goals in the New Jersey vs Detroit NHL game originally scheduled for Oct 13, 2026, the`

### KXNHLVEZINA — NHL Vezina Trophy
- (40) NAME: NAME wins
- samples: KXNHLVEZINA-27-YASKAROV30, KXNHLVEZINA-27-ULUUKKONEN1, KXNHLVEZINA-27-TDEMKO35, KXNHLVEZINA-27-SSKINNER74, KXNHLVEZINA-27-SMONTEMBEAULT35, KXNHLVEZINA-27-SKNIGHT30
- sample fields: `{"ticker": "KXNHLVEZINA-27-YASKAROV30", "event_ticker": "KXNHLVEZINA-27", "market_type": "binary", "title": "Vezina Trophy: Yaroslav Askarov wins", "subtitle": "::", "yes_sub_title": "Yaroslav Askarov", "no_sub_title": "Yaroslav Askarov", "strike_type": "structured", "custom_strike": {"hockey_player": "d9975a58-bdda-4de9-9933-549069713e00"}, "status": "active", "open_time": "2026-09-01T19:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Yaroslav Askarov wins the NHL Vezina Trophy in the 2026-27 NHL season, the`

### KXNHLWEST — Western Conference Champion
- (15) Will the NAME win the NAME?
- (1) Will the St. NAME win the NAME?
- samples: KXNHLWEST-27-WPG, KXNHLWEST-27-VGK, KXNHLWEST-27-VAN, KXNHLWEST-27-UTA, KXNHLWEST-27-STL, KXNHLWEST-27-SJ
- sample fields: `{"ticker": "KXNHLWEST-27-WPG", "event_ticker": "KXNHLWEST-27", "market_type": "binary", "title": "Will the Winnipeg Jets win the Western Conference Finals?", "subtitle": "Winnipeg Jets", "yes_sub_title": "Winnipeg Jets", "no_sub_title": "Winnipeg Jets", "strike_type": "structured", "custom_strike": {"hockey_team": "6f769f6d-161e-43d3-a586-db5451c5050e"}, "status": "active", "open_time": "2026-07-06T20:00:00Z", "close_time": "2027-07-15T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If the Winnipeg Jets win the 2026-27 NHL Western Conference Fina`

### KXNHLWINS — NHL wins 

### KXNHLWSTREAK — Longest NHL win streak in regular season
- (30) Will the NAME have the longest winning streak in the #-# NHL regular season?
- (1) Will the St. NAME have the longest winning streak in the #-# NHL regular season?
- (1) Will the Montréal Canadiens have the longest winning streak in the #-# NHL regular season?
- samples: KXNHLWSTREAK-27-WSH, KXNHLWSTREAK-27-WPG, KXNHLWSTREAK-27-VGK, KXNHLWSTREAK-27-VAN, KXNHLWSTREAK-27-UTA, KXNHLWSTREAK-27-TOR
- sample fields: `{"ticker": "KXNHLWSTREAK-27-WSH", "event_ticker": "KXNHLWSTREAK-27", "market_type": "binary", "title": "Will the Washington Capitals have the longest winning streak in the 2026-27 NHL regular season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-28T17:00:00Z", "close_time": "2027-04-18T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If Washington Capitals has the longes`

### KXTEAMSINSC — Teams in Stanley Cup
- (1) Will WSH Capitals vs WPG Jets be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs VGK NAME be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs VAN Canucks be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs UTA Mammoth be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs STL Blues be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs SJ Sharks be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs SEA Kraken be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs NSH Predators be the matchup in the #-# NAME?
- samples: KXTEAMSINSC-27-WSHWPG, KXTEAMSINSC-27-WSHVGK, KXTEAMSINSC-27-WSHVAN, KXTEAMSINSC-27-WSHUTA, KXTEAMSINSC-27-WSHSTL, KXTEAMSINSC-27-WSHSJ
- sample fields: `{"ticker": "KXTEAMSINSC-27-WSHWPG", "event_ticker": "KXTEAMSINSC-27", "market_type": "binary", "title": "Will WSH Capitals vs WPG Jets be the matchup in the 2026-27 Stanley Cup Final?", "yes_sub_title": "WSH Capitals vs WPG Jets", "no_sub_title": "WSH Capitals vs WPG Jets", "strike_type": "custom", "custom_strike": {"Matchup": "WSH Capitals vs WPG Jets"}, "status": "active", "open_time": "2026-09-11T22:00:00Z", "close_time": "2027-06-15T14:00:00Z", "expected_expiration_time": "2027-06-15T14:00:00Z", "result": "", "rules_primary": "If WSH Capitals vs WPG Jets is confirmed to be the matchup in t`

## UNRESOLVED samples

- `KXNHLLINDSAY-27-WNYLANDER88` — Ted Lindsay Award: William Nylander wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-SCROSBY87` — Ted Lindsay Award: Sidney Crosby wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-QHUGHES43` — Ted Lindsay Award: Quinn Hughes wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-PDOROFEYEV16` — Ted Lindsay Award: Pavel Dorofeyev wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-NSUZUKI14` — Ted Lindsay Award: Nick Suzuki wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-NMACKINNON29` — Ted Lindsay Award: Nathan MacKinnon wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-NKUCHEROV86` — Ted Lindsay Award: Nikita Kucherov wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MTKACHUK19` — Ted Lindsay Award: Matthew Tkachuk wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MRANTANEN96` — Ted Lindsay Award: Mikko Rantanen wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MMARNER93` — Ted Lindsay Award: Mitch Marner wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MCELEBRINI71` — Ted Lindsay Award: Macklin Celebrini wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-LDRAISAITL29` — Ted Lindsay Award: Leon Draisaitl wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-KKAPRIZOV97` — Ted Lindsay Award: Kirill Kaprizov wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-KCONNOR81` — Ted Lindsay Award: Kyle Connor wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-JHUGHES86` — Ted Lindsay Award: Jack Hughes wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-JEICHEL9` — Ted Lindsay Award: Jack Eichel wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-ISHESTERKIN31` — Ted Lindsay Award: Igor Shesterkin wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-DPASTRNAK88` — Ted Lindsay Award: David Pastrnak wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CMCDAVID97` — Ted Lindsay Award: Connor McDavid wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CMAKAR8` — Ted Lindsay Award: Cale Makar wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CHELLEBUYCK37` — Ted Lindsay Award: Connor Hellebuyck wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CCAUFIELD13` — Ted Lindsay Award: Cole Caufield wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CBEDARD98` — Ted Lindsay Award: Connor Bedard wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-BTKACHUK7` — Ted Lindsay Award: Brady Tkachuk wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-AVASILEVSKIY88` — Ted Lindsay Award: Andrei Vasilevskiy wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-APANARIN72` — Ted Lindsay Award: Artemi Panarin wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-AOVECHKIN8` — Ted Lindsay Award: Alex Ovechkin wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-AMATTHEWS34` — Ted Lindsay Award: Auston Matthews wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-60` — Macklin Celebrini: 60+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-55` — Macklin Celebrini: 55+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-50` — Macklin Celebrini: 50+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-45` — Macklin Celebrini: 45+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-40` — Macklin Celebrini: 40+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-35` — Macklin Celebrini: 35+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-30` — Macklin Celebrini: 30+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-25` — Macklin Celebrini: 25+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-20` — Macklin Celebrini: 20+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-55` — Alex Ovechkin: 55+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-50` — Alex Ovechkin: 50+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-40` — Alex Ovechkin: 40+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-35` — Alex Ovechkin: 35+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-30` — Alex Ovechkin: 30+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-25` — Alex Ovechkin: 25+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-20` — Alex Ovechkin: 20+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-15` — Alex Ovechkin: 15+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title

## Series decisions (hockey-related)

- NHL  `KXNHLPSEASONGOALS` Player Goals Scored in Season — ticker prefix KXNHL
- NHL  `KXNHLATLANTIC` NHL Atlantic Division Winner — ticker prefix KXNHL
- NHL  `KXNHLSERIESSCORE` NHL Series Exact Score — ticker prefix KXNHL
- skip `KXWOMHOCKEY` Winter Olympics Men's Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHL1PSPREAD` 1st Period Spread — ticker prefix KXNHL
- NHL  `KXNHLTEAMTOTAL` NHL Team Goals Scored During Game — ticker prefix KXNHL
- skip `KXINTHOCKEY` International Hockey — no NHL marker
- NHL  `KXNHLNORRIS` NHL James Norris Memorial Trophy — ticker prefix KXNHL
- NHL  `KXNHLMVP` NHL Hart Memorial Trophy Winner — ticker prefix KXNHL
- NHL  `KXNHLANYGOAL` Pro Hockey Goalscorer — ticker prefix KXNHL
- NHL  `KXNEXTTEAMNHL` Next Team NHL — title mentions NHL
- skip `KXKHLGAME` KHL Game — non-NHL hockey marker 'KHL'
- skip `KXIIHFCHAMP` IIHF World Championship winner — non-NHL hockey marker 'IIHF'
- NHL  `KXNHL2PTOTAL` 2nd Period Total — ticker prefix KXNHL
- NHL  `KXNHL2PSPREAD` 2nd Period Spread — ticker prefix KXNHL
- skip `KXDELGAME` DEL Game — non-NHL hockey marker 'DEL '
- skip `KXAHLGAME` AHL Game — non-NHL hockey marker 'AHL'
- NHL  `KXNHLPRICE` NHL Ticket Prices — ticker prefix KXNHL
- NHL  `KXNHLDRAFTTOP` Pro Hockey Top Pick — ticker prefix KXNHL
- NHL  `KXNHLRECORDWORST` Worst NHL Record — ticker prefix KXNHL
- NHL  `KXNHLWINS` NHL wins  — ticker prefix KXNHL
- NHL  `KXNHL2P` NHL 2nd Period Winner — ticker prefix KXNHL
- NHL  `KXNHLCENTRAL` NHL Central Division Winner — ticker prefix KXNHL
- NHL  `KXNHL3PSPREAD` NHL 3rd Period Spread — ticker prefix KXNHL
- NHL  `KXNHLNEXTTEAM` NHL Next Team — ticker prefix KXNHL
- skip `KXWOWHOCKEY` Winter Olympics Women's Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLCALDER` NHL Calder Memorial Trophy — ticker prefix KXNHL
- skip `KXWOMHOCKEYGOAL` Olympic Hockey Goalscorer — non-NHL hockey marker 'OLYMPIC'
- skip `KXNCAAHGAME` College Hockey Game — non-NHL hockey marker 'NCAA'
- NHL  `KXNHLEXPANSION` NHL Expansion — ticker prefix KXNHL
- skip `KXWOHOCKEY` Winter Olympics Hockey — non-NHL hockey marker 'OLYMPIC'
- skip `KXWOMHOCKEYTOTAL` Winter Olympics Men's Hockey Goal Total — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLDRAFTPICK` Pro Hockey Draft Pick — ticker prefix KXNHL
- NHL  `KXNHL2OT` NHL Double Overtime — ticker prefix KXNHL
- NHL  `KXNHLF10G` NHL Goal in First 10 Minutes — ticker prefix KXNHL
- skip `KXIIHF` Who will win IIHF championship? — non-NHL hockey marker 'IIHF'
- NHL  `KXNHLPLAYOFFGOALS` NHL Playoffs Goal Leader (by Round) — ticker prefix KXNHL
- NHL  `KXNHLMETROPOLITAN` NHL Metropolitan Division Winner — ticker prefix KXNHL
- NHL  `KXTEAMSINSC` Teams in Stanley Cup — NHL trophy/futures marker
- skip `KXLIIGAGAME` Liiga Game — non-NHL hockey marker 'LIIGA'
- NHL  `KXNHLSEASONGOALS` Player to score X Goals in Season — ticker prefix KXNHL
- NHL  `KXESPYNHL` BEST NHL PLAYER‬ — title mentions NHL
- NHL  `KXNHLSERIES` NHL Series Winner — ticker prefix KXNHL
- skip `KXIIHFGAME` IIHF Game — non-NHL hockey marker 'IIHF'
- NHL  `KXNHLSERIESTOTALGOAL` NHL Series Total Goals — ticker prefix KXNHL
- NHL  `KXNHLSERIESSPREAD` NHL Series Game Spread — ticker prefix KXNHL
- NHL  `KXNHL` Stanley Cup — ticker prefix KXNHL
- NHL  `KXNHLPLAYOFF` Playoff Qualifier — ticker prefix KXNHL
- NHL  `KXNHLSAVES` Pro Hockey Saves — ticker prefix KXNHL
- NHL  `KXNHLSERIESGAMES` NHL Series Total Games — ticker prefix KXNHL
- NHL  `KXNHLTOTAL` NHL Total Goals — ticker prefix KXNHL
- NHL  `KXNHLPTS` Pro Hockey Points — ticker prefix KXNHL
- skip `KXNCAAHOCKEYGAME` College Hockey Game — non-NHL hockey marker 'NCAA'
- NHL  `KXNHL30COMEBACK` NHL 3-0 Series Comeback — ticker prefix KXNHL
- NHL  `KXNHLAST` Pro Hockey Assists — ticker prefix KXNHL
- NHL  `KXNHLPACIFIC` NHL Pacific Division Winner — ticker prefix KXNHL
- NHL  `KXNHLWEST` Western Conference Champion — ticker prefix KXNHL
- NHL  `KXNHLFIRSTGOAL` NHL First Goal — ticker prefix KXNHL
- NHL  `KXNHLPRES` NHL President's Trophy Winner — ticker prefix KXNHL
- NHL  `KXCANADACUP` Canada winning Stanley Cup — NHL trophy/futures marker
- skip `KXNLGAME` National League Game — no NHL marker
- skip `KXWOMHOCKEYFIRSTGOAL` Winter Olympics Hockey First Goal — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLSERIESOT` NHL Series Overtime — ticker prefix KXNHL
- NHL  `KXNHLOT` NHL Overtime — ticker prefix KXNHL
- skip `KXWOMHOCKEYMVP` Men's Winter Olympics Hockey MVP — non-NHL hockey marker 'OLYMPIC'
- skip `KXNCAAH` College Hockey National Champion — non-NHL hockey marker 'NCAA'
- NHL  `KXNHLSERIESTOTALGOALS` NHL Series Total Goals — ticker prefix KXNHL
- NHL  `KXNHL3PBTTS` NHL Both Teams to Score in 3rd Period — ticker prefix KXNHL
- NHL  `KXNHL4NATIONS` 4 nations face off — ticker prefix KXNHL
- NHL  `KXNHL1STTEAM` All NHL First Team — ticker prefix KXNHL
- NHL  `KXNHLRETIRE` NHL Retire — ticker prefix KXNHL
- NHL  `KXNHLSPREAD` NHL Spread — ticker prefix KXNHL
- NHL  `KXNHL1PBTTS` NHL Both Teams to Score in 1st Period — ticker prefix KXNHL
- skip `KXWOMHOCKEYFGOAL` Winter Olympics Hockey First Goal — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHL1P` NHL 1st Period Winner — ticker prefix KXNHL
- skip `KXEUCHLGAME` Champions League Hockey — non-NHL hockey marker 'CHL'
- NHL  `KXNHLLINDSAY` NHL Ted Lindsay Winner — ticker prefix KXNHL
- NHL  `KXNHLOVERTIME` NHL Overtime — ticker prefix KXNHL
- NHL  `KXNHLSAVE` Goaltender Saves — ticker prefix KXNHL
- skip `KXELHGAME` ELH Game — no NHL marker
- NHL  `KXNHL2PBTTS` NHL Both Teams to Score in 2nd Period — ticker prefix KXNHL
- NHL  `KXNHLEAST` Eastern Conference Championship — ticker prefix KXNHL
- NHL  `KXNHLROSS` NHL Art Ross Trophy — ticker prefix KXNHL
- skip `KXWOMHOCKEYSPREAD` Winter Olympics Men's Hockey Spread — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLVEZINA` NHL Vezina Trophy — ticker prefix KXNHL
- NHL  `KXNHLMENTION` NHL Announcer Mentions — ticker prefix KXNHL
- NHL  `KXNHLWSTREAK` Longest NHL win streak in regular season — ticker prefix KXNHL
- skip `KXEARNINGSMENTIONHLT` HILTON — no NHL marker
- NHL  `KXNHL3PTOTAL` 3rd Period Total — ticker prefix KXNHL
- skip `KXNCAAHOCKEY` College Hockey National Champion — non-NHL hockey marker 'NCAA'
- NHL  `KXNHLSEASONPTS` NHL Season Point Totals — ticker prefix KXNHL
- NHL  `KXNHLADAMS` NHL Jack Adams Award — ticker prefix KXNHL
- NHL  `KXNHLHART` NHL Hart Memorial Trophy — ticker prefix KXNHL
- NHL  `KXNHLFINALSEXACT` NHL Championship Series Score — ticker prefix KXNHL
- NHL  `KXNHLGAME` NHL Game — ticker prefix KXNHL
- NHL  `KXNHL1PTOTAL` NHL 1st Period Total — ticker prefix KXNHL
- NHL  `KXNHLSEASONPPTS` Season Player Points — ticker prefix KXNHL
- NHL  `KXCONNSMYTHE` Conn Smythe trophy — NHL trophy/futures marker
- NHL  `KXNHLGOAL` NHL Goalscorer — ticker prefix KXNHL
- NHL  `KXNHL3P` NHL 3rd Period Winner — ticker prefix KXNHL
- skip `KXSHLGAME` SHL Game — non-NHL hockey marker 'SHL'
- NHL  `KXNHLNEXTGM` Next NHL GM — ticker prefix KXNHL
- skip `KXWO-HOCKEY` Winter Olympics Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLRICHARD` NHL Maurice "Rocket" Richard Trophy — ticker prefix KXNHL
