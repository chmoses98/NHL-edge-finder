# Pregame snapshot audit, slate 2026-10-22

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
| 2026020154 | 2026-10-22T23:00:00Z | 8 | CONFIRMED/CONFIRMED | 13 / 13 | 13 | 5 | 0 |
| 2026020155 | 2026-10-22T23:00:00Z | 8 | CONFIRMED/CONFIRMED | 13 / 215 | 13 | 5 | 0 |
| 2026020156 | 2026-10-22T23:00:00Z | 8 | CONFIRMED/CONFIRMED | 13 / 13 | 13 | 5 | 0 |
| 2026020157 | 2026-10-22T23:00:00Z | 8 | CONFIRMED/CONFIRMED | 13 / 13 | 13 | 5 | 0 |
| 2026020158 | 2026-10-22T23:00:00Z | 8 | CONFIRMED/CONFIRMED | 13 / 13 | 13 | 5 | 0 |
| 2026020159 | 2026-10-22T23:30:00Z | 12 | CONFIRMED/CONFIRMED | 280 / 43 | 43 | 5 | 0 |
| 2026020160 | 2026-10-23T00:00:00Z | 17 | CONFIRMED/CONFIRMED | 310 / 73 | 73 | 5 | 0 |
| 2026020161 | 2026-10-23T00:00:00Z | 17 | CONFIRMED/CONFIRMED | 310 / 275 | 73 | 5 | 0 |
| 2026020162 | 2026-10-23T01:00:00Z | 23 | CONFIRMED/CONFIRMED | 31 / 133 | 31 | 18 | 0 |
| 2026020163 | 2026-10-23T01:00:00Z | 23 | CONFIRMED/PROBABLE | 31 / 133 | 31 | 18 | 0 |
| 2026020164 | 2026-10-23T02:00:00Z | 8 | CONFIRMED/CONFIRMED | 193 / 54 | 54 | 4 | 0 |
| 2026020165 | 2026-10-23T02:00:00Z | 8 | CONFIRMED/CONFIRMED | 91 / 193 | 54 | 4 | 0 |

## Projection-foundation runs

| archived | rows | confirmed active | newest capture age, min (min / max over games) |
|---|---|---|---|
| 2026-10-22T00:54:14Z | 1732 | 0 | 2 / 2 |
| 2026-10-22T18:50:01Z | 1732 | 13 | 3 / 3 |
| 2026-10-22T19:25:23Z | 1732 | 13 | 35 / 36 |
| 2026-10-22T22:46:41Z | 1743 | 177 | 5 / 5 |
| 2026-10-23T00:28:46Z | 584 | 3 | 18 / 18 |
| 2026-10-23T01:05:53Z | 292 | 0 | 4 / 4 |
