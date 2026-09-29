"""NHL wager ACCOUNTING: what the owner actually placed on Kalshi, and what the exchange paid.

This package is deliberately walled off from everything else in ``nhl_edge``. It imports no model, simulator,
feature, pricing or recommendation code, and a test enforces that. A row here says "the owner placed this NHL
bet"; it never says "the NHL model recommended it". DATA_ONLY_V1 / DATA_ONLY_V2 stay RESEARCH_ONLY.

Rows arrive only from kalshi-bet-router, which reads the owner's own Kalshi fills (read-only exchange access).
Nothing here places, sizes, recommends or cancels an order.
"""
