"""Game-script / thesis engine and portfolio construction for RUN NHL (RESEARCH_ONLY).

The joint PLAYER_SIM_V1 draw (nhl-sim-2.0 team score path -> goal strength / scorer / assists -> goalie saves) is the
single source of simulated game outcomes. This package never simulates anything itself; it reads those draws and turns
them into a betting-card analysis:

    game / event distribution (per-draw features)          thesis.features
      -> game-script taxonomy (deterministic labels)        thesis.scripts
      -> thesis events + bet-to-script mapping              thesis.events, thesis.mapping
      -> market expression comparison                        thesis.expression
      -> same-game joint outcome matrix                      thesis.joint
      -> portfolio construction on the simulated P/L         thesis.portfolio
      -> card completion gate                                thesis.card
      -> prospective decision log + postmortem               thesis.postmortem

AUTHORITY: RESEARCH_ONLY. Nothing here places, routes or sizes a real wager; stakes are research suggestions for a
nominal bankroll, and every model family keeps its RESEARCH_ONLY authority.
"""

THESIS_VERSION = "nhl-thesis-1.0"
CARD_VERSION = "nhl-card-1.0"
PORTFOLIO_VERSION = "nhl-portfolio-1.0"
