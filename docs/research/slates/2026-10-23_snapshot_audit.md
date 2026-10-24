# Pregame snapshot audit, slate 2026-10-23

_Read-only audit of immutable records; no prediction or timestamp was changed._

Question answered: for every game of ``date``, which forecasts were GENUINELY available before puck drop, how old was the input
data when they were made, and which later artefacts are post-puck-drop or late-arriving? It reads immutable records only
(``predictions`` in data-archive; ``forecasts`` / ``runs`` in projection-data) and writes nothing back; no prediction, timestamp or
file is changed. "Available before puck drop" means ``archived_utc`` (the instant the record was written to its append-only ledger)
is at or before the scheduled start; ``generated_utc`` / ``predicted_at_utc`` is when the model ran, ``data_asof_utc`` /
``data_cutoff_utc`` the cut of its inputs. A record whose archive time is after the start is "late-arriving" even if it claims an
earlier model time.

A projection-foundation forecast row is written only when its content changed, so "last write" can be old while the last *evaluation* (a run that re-checked the game and found nothing new) is recent; both are shown.

| game | start (UTC) | V1 last pregame (min before) | V1 goalies H/A | PF last write: challenger / incumbent (min before) | PF last evaluation (min before) | lineup capture age at that run (min) | rows archived after start |
|---|---|---|---|---|---|---|---|
| 2026020160 | 2026-10-23T00:00:00Z | - | -/- | 310 / 73 | - | - | 0 |
| 2026020161 | 2026-10-23T00:00:00Z | - | -/- | 310 / 275 | - | - | 0 |
| 2026020162 | 2026-10-23T01:00:00Z | 23 | CONFIRMED/CONFIRMED | 31 / 133 | 31 | 18 | 0 |
| 2026020163 | 2026-10-23T01:00:00Z | 23 | CONFIRMED/PROBABLE | 31 / 133 | 31 | 18 | 0 |
| 2026020164 | 2026-10-23T02:00:00Z | 8 | CONFIRMED/CONFIRMED | 193 / 54 | 54 | 4 | 0 |
| 2026020165 | 2026-10-23T02:00:00Z | 8 | CONFIRMED/CONFIRMED | 91 / 193 | 54 | 4 | 0 |
| 2026020166 | 2026-10-24T00:00:00Z | 0 | CONFIRMED/CONFIRMED | 252 / 252 | 13 | 12 | 0 |
| 2026020167 | 2026-10-24T01:00:00Z | 12 | CONFIRMED/CONFIRMED | 312 / 312 | 18 | 16 | 0 |
| 2026020168 | 2026-10-24T17:00:02Z | 751 | PROJECTED/PROJECTED | - / - | - | - | 0 |
| 2026020169 | 2026-10-24T19:30:02Z | 901 | PROJECTED/PROJECTED | - / - | - | - | 0 |
| 2026020170 | 2026-10-24T23:00:02Z | 1111 | PROJECTED/PROJECTED | - / - | - | - | 0 |
| 2026020171 | 2026-10-24T23:00:02Z | 1111 | PROJECTED/PROJECTED | - / - | - | - | 0 |
| 2026020172 | 2026-10-24T23:00:02Z | 1111 | PROJECTED/PROJECTED | - / - | - | - | 0 |
| 2026020173 | 2026-10-24T23:00:02Z | 1111 | PROJECTED/PROJECTED | - / - | - | - | 0 |
| 2026020174 | 2026-10-24T23:00:02Z | 1111 | PROJECTED/PROJECTED | - / - | - | - | 0 |
| 2026020175 | 2026-10-24T23:00:02Z | 1111 | PROJECTED/PROJECTED | - / - | - | - | 0 |
| 2026020176 | 2026-10-24T23:00:02Z | 1111 | CONFIRMED/PROJECTED | - / - | - | - | 0 |

## Projection-foundation runs

| archived | rows | confirmed active | newest capture age, min (min / max over games) |
|---|---|---|---|
| 2026-10-23T00:28:46Z | 584 | 3 | 18 / 18 |
| 2026-10-23T01:05:53Z | 292 | 0 | 4 / 4 |
| 2026-10-23T15:17:54Z | 292 | 0 | 2 / 2 |
| 2026-10-23T18:07:50Z | 292 | 2 | 47 / 47 |
| 2026-10-23T19:47:31Z | 292 | 4 | 18 / 18 |
| 2026-10-23T21:15:40Z | 292 | 4 | 8 / 8 |
| 2026-10-23T22:23:52Z | 292 | 4 | 15 / 15 |
| 2026-10-23T22:47:08Z | 292 | 4 | 8 / 8 |
| 2026-10-23T23:20:46Z | 292 | 4 | 14 / 14 |
| 2026-10-23T23:47:00Z | 292 | 4 | 12 / 12 |
| 2026-10-24T00:16:53Z | 146 | 2 | 17 / 17 |
| 2026-10-24T00:42:08Z | 146 | 2 | 16 / 16 |
