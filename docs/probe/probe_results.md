# Source probe

probed 2026-09-29T04:43:10+00:00 for date 2026-09-29

| name | status | ms | bytes | kind | note |
|---|---:|---:|---:|---|---|
| nhl_schedule_date | 200 | 55 | 84310 | json | nextStartDate, previousStartDate, gameWeek, oddsPartners, preSeasonStartDate, regularSeasonStartDate, regularSeasonEndDa |
| nhl_schedule_now | 200 | 80 | 84310 | json | nextStartDate, previousStartDate, gameWeek, oddsPartners, preSeasonStartDate, regularSeasonStartDate, regularSeasonEndDa |
| nhl_score_now | 200 | 65 | 18390 | json | prevDate, currentDate, nextDate, gameWeek, oddsPartners, games |
| nhl_score_date | 200 | 30 | 18390 | json | prevDate, currentDate, nextDate, gameWeek, oddsPartners, games |
| nhl_standings_now | 200 | 68 | 51555 | json | wildCardIndicator, standingsDateTimeUtc, standings |
| nhl_roster_tor | 200 | 206 | 10390 | json | forwards, defensemen, goalies |
| nhl_club_schedule_tor | 200 | 201 | 188381 | json | previousSeason, currentSeason, clubTimezone, clubUTCOffset, games |
| nhl_club_schedule_tor_2025 | 200 | 297 | 184101 | json | previousSeason, currentSeason, nextSeason, clubTimezone, clubUTCOffset, games |
| nhl_club_stats_tor | 200 | 208 | 17323 | json | season, gameType, skaters, goalies |
| nhl_boxscore_final_2025 | 200 | 111 | 13529 | json | id, season, gameType, limitedScoring, gameDate, venue, venueLocation, startTimeUTC |
| nhl_landing_final_2025 | 200 | 415 | 11355 | json | id, season, gameType, limitedScoring, gameDate, venue, venueLocation, startTimeUTC |
| nhl_pbp_final_2025 | 200 | 232 | 146277 | json | id, season, gameType, limitedScoring, gameDate, venue, venueLocation, startTimeUTC |
| nhl_right_rail_2025 | 200 | 399 | 4550 | json | seasonSeries, seasonSeriesWins, gameInfo, gameVideo, linescore, shotsByPeriod, teamGameStats, gameReports |
| nhl_boxscore_ot_sample | 200 | 306 | 13147 | json | id, season, gameType, limitedScoring, gameDate, venue, venueLocation, startTimeUTC |
| nhl_schedule_calendar | 200 | 124 | 12704 | json | endDate, nextStartDate, previousStartDate, startDate, teams |
| nhl_season_list | 200 | 106 | 982 | json | l, i, s, t, [, 1, 0, 9 |
| nhl_stats_team | 200 | 184 | 6664 | json | data, total |
| nhl_stats_team_summary_prev | 200 | 177 | 16854 | json | data, total |
| nhl_stats_team_summary_cur | 200 | 108 | 21 | json | data, total |
| nhl_stats_goalie_summary_prev | 200 | 170 | 38937 | json | data, total |
| nhl_stats_goalie_summary_cur | 200 | 102 | 21 | json | data, total |
| nhl_stats_season | 200 | 108 | 65173 | json | data, total |
| nhl_stats_game_prev | 200 | 161 | 1259 | json | data, total |
| mp_teams_2025 | 200 | 312 | 99689 | csv | team, season, name, team, position, situation, games_played, xGoalsPercentage |
| mp_teams_2026 | 404 | 198 | 196 | html | HTTPError 404 |
| mp_goalies_2025 | 200 | 266 | 93386 | csv | playerId, season, name, team, position, situation, games_played, icetime |
| mp_goalies_2026 | 200 | 114 | 489 | csv | playerId, season, name, team, position, situation, games_played, icetime |
| mp_skaters_2025 | 200 | 467 | 400000 | csv | playerId, season, name, team, position, situation, games_played, icetime |
| mp_lines_2025 | 200 | 405 | 400000 | csv | lineId, season, name, team, position, situation, games_played, icetime |
| mp_all_teams_gbg | 200 | 434 | 600000 | csv | team, season, name, gameId, playerTeam, opposingTeam, home_or_away, gameDate |
| mp_team_gbg_tor | 200 | 439 | 400000 | csv | team, season, name, gameId, playerTeam, opposingTeam, home_or_away, gameDate |
| mp_shots_2024_zip_head | 404 | 110 | 0 |  | HTTPError 404 |
| mp_shots_2025_zip_head | 404 | 108 | 0 |  | HTTPError 404 |
| mp_shots_pt_2024_head | 200 | 243 | 0 |  |  |
| mp_shots_pt_2025_head | 200 | 202 | 0 |  |  |
| mp_shots_pt_2007_2023_head | 404 | 222 | 0 |  | HTTPError 404 |
| mp_predictions_page | 200 | 47 | 20000 | html |  |
| espn_nhl_scoreboard | 200 | 116 | 72311 | json | leagues, events, provider |
| espn_nhl_teams | 200 | 228 | 136961 | json | sports |
| dailyfaceoff_goalies | 200 | 147 | 79561 | html |  |
| dailyfaceoff_goalies_date | 200 | 37 | 143349 | html |  |
| rotowire_goalies | 200 | 477 | 323650 | html |  |
| nhl_schedule_oct05 | 200 | 99 | 89222 | json | nextStartDate, previousStartDate, gameWeek, preSeasonStartDate, regularSeasonStartDate, regularSeasonEndDate, playoffEnd |
| nhl_injuries_espn | 200 | 227 | 1208404 | json | timestamp, status, season, injuries |
| kalshi_api_exchange_status | 200 | 130 | 667 | json | exchange_active, exchange_index_statuses, intra_exchange_transfers_active, trading_active |
| kalshi_api_series_sports | 200 | 399 | 3000000 | json-invalid |  |
| kalshi_api_series_kxnhlgame | 200 | 55 | 1569 | json | series |
| kalshi_api_markets_kxnhlgame_open | 200 | 249 | 157586 | json | cursor, markets |
| kalshi_api_markets_kxnhlgame_unopened | 200 | 97 | 27 | json | cursor, markets |
| kalshi_api_markets_kxnhlgame_settled | 200 | 115 | 99699 | json | cursor, markets |
| kalshi_api_events_kxnhlgame | 200 | 136 | 210323 | json | cursor, events, milestones |
| kalshi_api_markets_kxnhlspread_open | 200 | 126 | 124075 | json | cursor, markets |
| kalshi_api_markets_kxnhltotal_open | 200 | 142 | 203884 | json | cursor, markets |
| kalshi_api_filters_by_sport | 200 | 138 | 17500 | json | filters_by_sports, sport_ordering |
| kalshi_external_api_exchange_status | 200 | 204 | 667 | json | exchange_active, exchange_index_statuses, intra_exchange_transfers_active, trading_active |
| kalshi_external_api_series_sports | 200 | 974 | 3000000 | json-invalid |  |
| kalshi_external_api_series_kxnhlgame | 200 | 210 | 1569 | json | series |
| kalshi_external_api_markets_kxnhlgame_open | 200 | 457 | 157586 | json | cursor, markets |
| kalshi_external_api_markets_kxnhlgame_unopened | 200 | 224 | 27 | json | cursor, markets |
| kalshi_external_api_markets_kxnhlgame_settled | 200 | 382 | 99699 | json | cursor, markets |
| kalshi_external_api_events_kxnhlgame | 200 | 432 | 210323 | json | cursor, events, milestones |
| kalshi_external_api_markets_kxnhlspread_open | 200 | 359 | 124075 | json | cursor, markets |
| kalshi_external_api_markets_kxnhltotal_open | 200 | 471 | 203884 | json | cursor, markets |
| kalshi_external_api_filters_by_sport | 200 | 240 | 17500 | json | filters_by_sports, sport_ordering |
