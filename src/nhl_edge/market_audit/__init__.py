"""NHL historical market audit (RESEARCH_ONLY).

Offline, read-only research tooling over a copy of the ``data-archive`` branch. Nothing here writes to the
archive, places or routes a wager, changes a model, or changes a staking limit. Every output carries lineage
(archive manifest digest + code version) so a result can be reproduced from the same bytes.
"""

AUDIT_VERSION = "nhl-market-audit-1.0"

# Capture timing, measured on the archive (docs/research/nhl-market-audit/CAPTURE_COVERAGE.md): a tick is stamped with
# the capture START; the market board is fully written ~30-40 s later and the order books ~91-100 s later. A quote
# stamped t0 may therefore have been observed anywhere in [t0, t0 + window]. Point-in-time logic uses the UPPER bound
# (the instant the whole artifact existed) so a decision never consumes a quote that might post-date it.
MARKET_AVAILABLE_LAG_S = 45
ORDERBOOK_AVAILABLE_LAG_S = 105


# Games that START after the registry freeze are the PROSPECTIVE tier. Every consumer of the live panel that is not the predeclared
# looks must go through ``dev_only`` so that post-freeze games can never leak into a "LIVE" table (statistical review F5).
PROSPECTIVE_FREEZE_UTC = "2026-10-21T17:13:05Z"


def dev_only(panel):  # type: ignore[no-untyped-def]
    """Rows of a live panel whose game started before the prospective freeze."""
    import pandas as pd

    return panel[pd.to_datetime(panel["start_time_utc"], utc=True) < pd.Timestamp(PROSPECTIVE_FREEZE_UTC)]
