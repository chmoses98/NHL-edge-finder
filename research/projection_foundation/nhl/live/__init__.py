"""NHL Projection Foundation: live shadow operation (research only, no betting authority).

    cd research/projection_foundation && python -m nhl.live.run --stage all --archive <projection-data checkout> [--dry-run]

Stages (each idempotent): capture -> project -> publish -> results -> settle -> score -> guard.
Everything is written to the append-only `projection-data` archive through pf_core (availability snapshots, pregame
forecast archive for the challenger AND the incumbent, outcomes, settlements, scorecards).
"""
