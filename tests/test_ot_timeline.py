"""Overtime timeline regression (data.player_events): every strength-state second must be a second actually played.

Before the fix every overtime game was laid out to 80:00 and the seconds after the final whistle were booked to the
last strength state seen (2,918 regular-season OT team-game rows, 2021-26, all with n_seconds = 4800). Built from REAL
official payloads: 2025020001 (regulation, docs/probe/samples/player_game), 2025020008 (3-on-3 overtime winner),
2025020099 (overtime winner on a 4-on-3 power play), 2025020006 (shootout) in tests/fixtures/nhl_games, cross-checked
against the committed tables in data/history/players (derived from the same payloads by the old code). No network."""

from __future__ import annotations

import gzip
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from nhl_edge.data.player_events import STATES, _plays, derive_game, game_length_s, state_timeline

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "tests" / "fixtures" / "nhl_games"
SAMPLE = ROOT / "docs" / "probe" / "samples" / "player_game"
ST = ["sec_ev", "sec_pp", "sec_sh", "sec_ea", "sec_en"]
REG, OT3, OT_PP, SO = 2025020001, 2025020008, 2025020099, 2025020006


def _load(gid: int) -> tuple[dict, dict, dict]:
    out = []
    for k in ("boxscore", "pbp", "shiftcharts"):
        gz = FIX / f"nhl_{k}_{gid}.json.gz"
        if gz.exists():
            with gzip.open(gz, "rt", encoding="utf-8") as f:
                out.append(json.load(f))
        else:
            out.append(json.loads((SAMPLE / f"nhl_{k}_{gid}.json").read_text()))
    return out[0], out[1], out[2]


@pytest.fixture(scope="module")
def games() -> dict[int, dict[str, pd.DataFrame]]:
    return {gid: derive_game(*_load(gid), {"season": 2025, "game_type": 2}) for gid in (REG, OT3, OT_PP, SO)}


@pytest.fixture(scope="module")
def cached() -> dict[str, pd.DataFrame]:
    return {k: pd.read_parquet(ROOT / "data" / "history" / "players" / f"{k}_2025.parquet") for k in ("team_states", "players", "goals")}


def _ot_goal_t(goals: pd.DataFrame) -> int | None:
    g = goals[goals["period"] == 4]
    return int(g["t_s"].min()) if len(g) else None


def test_game_length_is_the_time_actually_played(games):
    assert games[REG]["team_states"]["n_seconds"].eq(3600).all()
    for gid in (OT3, OT_PP):
        t = _ot_goal_t(games[gid]["goals"])
        assert t is not None and 3600 < t < 3900
        assert games[gid]["team_states"]["n_seconds"].eq(t).all()  # the overtime winner ends the game
    assert games[SO]["team_states"]["n_seconds"].eq(3900).all()  # a shootout follows the full 5-minute overtime


def test_every_second_is_in_exactly_one_state_and_sums_to_the_real_length(games):
    for gid, t in games.items():
        ts = t["team_states"]
        assert (ts[ST].sum(axis=1) + ts["sec_unknown"] == ts["n_seconds"]).all(), gid
        assert (ts["sec_unknown"] == 0).all(), gid
        h, a = ts.set_index("is_home").loc[True], ts.set_index("is_home").loc[False]
        assert h["sec_pp"] == a["sec_sh"] and h["sec_sh"] == a["sec_pp"], gid  # one team's power play is the other's penalty kill


def test_overtime_seconds_land_in_the_states_the_play_by_play_says(games):
    plays = {gid: _plays(_load(gid)[1]) for gid in (OT3, OT_PP, SO)}
    for pl in plays.values():
        n = game_length_s(pl)
        h, a = state_timeline(pl, n)
        ot_h, ot_a = h[3600:], a[3600:]
        assert len(ot_h) == n - 3600 and (ot_h >= 0).all() and (ot_a >= 0).all()
        assert all(STATES[i] in ("EV", "PP", "SH", "EA", "EN") for i in np.unique(ot_h))
        # the mirror image holds every second: home PP <-> away SH
        pp, sh = STATES.index("PP"), STATES.index("SH")
        assert ((ot_h == pp) == (ot_a == sh)).all() and ((ot_h == sh) == (ot_a == pp)).all()
    # 3-on-3 winner: the overtime is even strength for both teams up to the goal
    h, _ = state_timeline(plays[OT3], game_length_s(plays[OT3]))
    assert (h[3600:] == STATES.index("EV")).mean() > 0.9
    # 4-on-3 winner: the scoring team is on the power play in the seconds before its goal, and both EV and PP occur
    g = derive_game(*_load(OT_PP), {})["goals"]
    g = g[g["period"] == 4].iloc[0]
    n = game_length_s(plays[OT_PP])
    h, a = state_timeline(plays[OT_PP], n)
    scorer = h if bool(g["is_home"]) else a
    assert g["strength"] == "PP" and scorer[int(g["t_s"]) - 1] == STATES.index("PP")
    assert {STATES[i] for i in np.unique(scorer[3600:])} >= {"EV", "PP"}


def test_only_the_phantom_seconds_disappear_compared_with_the_committed_tables(games, cached):
    old = cached["team_states"].set_index(["game_id", "team_id"])
    for gid in (OT3, OT_PP, SO):
        for r in games[gid]["team_states"].itertuples(index=False):
            o = old.loc[(gid, r.team_id)]
            assert int(o["n_seconds"]) == 4800  # the defect, as committed
            removed = {s: int(o[s]) - int(getattr(r, s)) for s in ST}
            assert sum(removed.values()) == 4800 - int(r.n_seconds), (gid, removed)
            assert sum(v != 0 for v in removed.values()) == 1 and min(removed.values()) >= 0, (gid, removed)
    reg = games[REG]["team_states"].set_index("team_id")
    for tid, r in reg.iterrows():
        assert (old.loc[(REG, tid), ST].astype(int).to_numpy() == r[ST].astype(int).to_numpy()).all()  # regulation games unchanged


def test_skater_lines_are_untouched_and_on_ice_counts_are_plausible(games, cached):
    cols = ["toi_s", "sog", "toi_ev_s", "toi_pp_s", "toi_sh_s", "toi_ea_s", "toi_en_s", "toi_ot_s", "sog_ev", "sog_pp"]
    old = cached["players"].set_index(["game_id", "player_id"])
    for gid, t in games.items():
        p = t["players"].set_index("player_id")
        o = old.loc[gid]
        assert (p[cols].astype(float).sort_index().to_numpy() == o.loc[p.index, cols].astype(float).sort_index().to_numpy()).all(), gid
        ts = t["team_states"].set_index("team_id")
        for tid, d in t["players"].groupby("team_id"):
            ratio = d["toi_ev_s"].sum() / ts.loc[tid, "sec_ev"]
            assert 4.6 <= ratio <= 5.01, (gid, tid, ratio)  # five skaters a side at EV, three in 3-on-3 overtime


def test_game_length_without_closing_events():
    def play(per, t, ptype="REG", code="1551", kind="faceoff"):
        return {"_period": per, "_ptype": ptype, "_t": (per - 1) * 1200 + t, "situationCode": code, "typeDescKey": kind}

    reg = [play(1, 0), play(3, 1190)]
    assert game_length_s(reg) == 3600
    ot_goal = reg + [play(4, 0, "OT", "1331"), play(4, 131, "OT", "1331", "goal")]
    assert game_length_s(ot_goal) == 3600 + 131
    shootout = reg + [play(4, 250, "OT", "1331"), play(5, 0, "SO", "0101", "shot-on-goal")]
    assert game_length_s(shootout) == 3900
    playoff_2ot = reg + [play(4, 1200, "OT"), play(5, 412, "OT", "1551", "goal")]
    assert game_length_s(playoff_2ot) == 4 * 1200 + 412


def test_effect_study_uses_the_production_team_minute_template_verbatim():
    from nhl_edge.research.ot_timeline_effect import production_team_minutes

    src = (ROOT / "src" / "nhl_edge" / "workflows" / "shadow_player.py").read_text()
    assert 'team_min = {"ev": 50.6, "pp": 4.4 * p_pp / 0.215, "sh": 4.4, "ea": 0.6, "en": 0.6, "ot": 1.2}' in src
    assert production_team_minutes(0.215) == {"ev": 50.6, "pp": 4.4, "sh": 4.4, "ea": 0.6, "en": 0.6, "ot": 1.2}
