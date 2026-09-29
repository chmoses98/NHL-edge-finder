"""Walk-forward evaluation on the synthetic 3-team league: point-in-time cutoff, baselines, end-to-end run + outputs."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from nhl_edge.data import history as H
from nhl_edge.features.ratings import last_game_date, league_rates, team_rating
from nhl_edge.research import walk_forward as W
from tests.test_history import install_fake_fetch, synthetic_moneypuck_csv, synthetic_nhl_payload, synthetic_schedule

SEASONS = (2023, 2024)


@pytest.fixture(scope="module")
def data():
    games = synthetic_schedule(SEASONS)
    tg = H.parse_moneypuck_csv(synthetic_moneypuck_csv(games))
    ng = pd.concat([H.parse_nhl_games(synthetic_nhl_payload(games, s, gt)) for s in SEASONS for gt in (2, 3)], ignore_index=True)
    return games, tg, ng


def _mid_season_game(ng: pd.DataFrame, season: int, home: str) -> pd.Series:
    d = ng[(ng["season"] == season) & (ng["game_type"] == 2) & (ng["home_abbrev"] == home)].sort_values("game_date")
    return d.iloc[len(d) // 2]


def _poison(log: pd.DataFrame, team: str, date_int: int, n: int = 5) -> pd.DataFrame:
    """Append absurd rows for ``team`` dated ``date_int`` and later: any leak would move the rating a lot."""
    rows = []
    for k in range(n):
        rows.append({"team": team, "opposingTeam": "BOS", "season": 2024, "game_id": 9_000_000 + k, "home_or_away": "HOME",
                     "gameDate": date_int + k, "date_int": date_int + k, "xGoalsFor": 40.0, "xGoalsAgainst": 0.1, "goalsFor": 40.0,
                     "goalsAgainst": 0.0, "iceTime": 3600.0, "minutes": 60.0, "situation": "all"})
    return pd.concat([log, pd.DataFrame(rows)], ignore_index=True).sort_values(["date_int", "game_id"]).reset_index(drop=True)


def test_build_gamelog_filters_and_canonical_teams(data):
    _, tg, _ = data
    log = W.build_gamelog(tg)
    assert (log["situation"] == "all").all()
    assert set(log["team"]) == {"TOR", "BOS", "TBL"} and "T.B" not in set(log["opposingTeam"])
    assert set(log["game_id"] // 10000 % 100) == {2}  # playoff rows excluded by default
    assert len(log) == 2 * 30 * 2
    assert len(W.build_gamelog(tg, include_playoffs=True)) == 2 * 31 * 2
    assert log["date_int"].is_monotonic_increasing


def test_ratings_are_point_in_time(data):
    _, tg, ng = data
    log = W.build_gamelog(tg)
    g = _mid_season_game(ng, 2024, "TOR")
    as_of = str(g["game_date"])
    cut = int(as_of.replace("-", ""))
    truncated = log[log["date_int"] < cut]
    poisoned = _poison(log, "TOR", cut)
    assert (poisoned["date_int"] >= cut).sum() > (log["date_int"] >= cut).sum()

    lg = league_rates(log, as_of, season=2024)
    assert lg == league_rates(truncated, as_of, season=2024) == league_rates(poisoned, as_of, season=2024)
    r_full = team_rating(log, "TOR", as_of, lg, current_season=2024)
    r_trunc = team_rating(truncated, "TOR", as_of, lg, current_season=2024)
    r_poison = team_rating(poisoned, "TOR", as_of, lg, current_season=2024)
    assert r_full == r_trunc == r_poison
    assert r_full.games_used > 0
    # the poison is visible one day later, so the equality above is a real cutoff and not an inert fixture
    later = pd.Timestamp(as_of) + pd.Timedelta(days=1)
    r_later = team_rating(poisoned, "TOR", later.strftime("%Y-%m-%d"), lg, current_season=2024)
    assert r_later.off_xg60 > r_full.off_xg60 + 0.5
    # own game row (dated as_of) is not the "last game"
    assert last_game_date(log, "TOR", as_of) < cut
    assert (log[(log["team"] == "TOR") & (log["date_int"] == cut)].shape[0]) == 1  # the game itself IS in the log


def test_predict_game_ignores_own_and_future_rows(data):
    _, tg, ng = data
    log = W.build_gamelog(tg)
    g = _mid_season_game(ng, 2024, "TBL")
    as_of = str(g["game_date"])
    cut = int(as_of.replace("-", ""))
    kw = dict(n_sims=300, base_seed=1)
    base = W.predict_game(log, "TBL", str(g["away_abbrev"]), as_of, 2024, int(g["game_id"]), **kw)
    poisoned = _poison(log, "TBL", cut)
    same = W.predict_game(poisoned, "TBL", str(g["away_abbrev"]), as_of, 2024, int(g["game_id"]), **kw)
    assert base == same
    # team_logs speed-up path gives identical numbers
    team_logs = {t: d for t, d in poisoned.groupby("team")}
    assert W.predict_game(poisoned, "TBL", str(g["away_abbrev"]), as_of, 2024, int(g["game_id"]), team_logs=team_logs, **kw) == base
    # and the leak would have mattered
    later = (pd.Timestamp(as_of) + pd.Timedelta(days=2)).strftime("%Y-%m-%d")
    leaked = W.predict_game(poisoned, "TBL", str(g["away_abbrev"]), later, 2024, int(g["game_id"]), **kw)
    assert leaked["lam_home"] > base["lam_home"] * 1.3
    assert base["home_goalie_factor"] == base["away_goalie_factor"] == 1.0
    assert abs(base["p_home_reg_win"] + base["p_away_reg_win"] + base["p_reg_tie"] - 1) < 1e-9
    assert base["p_reg_tie"] == base["p_overtime"] and 0 < base["p_home_win"] < 1
    assert base["seed"] == W.game_seed(int(g["game_id"]), 1)


def test_constant_home_baseline_is_strictly_prior(data):
    _, _, ng = data
    p = W.constant_home_baseline(ng)
    reg = ng[(ng["game_type"] == 2) & ng["final"].astype(bool)].sort_values(["game_date", "game_id"])
    first = reg.index[0]
    assert p.loc[first] == 0.5
    for idx in reg.index[[1, 7, 40, len(reg) - 1]]:
        gd = ng.at[idx, "game_date"]
        prior = reg[reg["game_date"] < gd]
        assert p.loc[idx] == pytest.approx(float(prior["home_win"].astype(float).mean()))
    # two games on one date must not see each other
    tiny = pd.DataFrame({"game_id": [1, 2, 3], "game_type": [2, 2, 2], "final": [True, True, True], "game_date": ["2024-10-10", "2024-10-12", "2024-10-12"],
                         "home_win": pd.array([True, True, False], dtype="boolean")})
    assert list(W.constant_home_baseline(tiny)) == [0.5, 1.0, 1.0]


def test_run_walk_forward_end_to_end(data, tmp_path: Path):
    _, tg, ng = data
    df, report = W.run_walk_forward(tg, ng, [2024], n_sims=500, base_seed=3)
    assert len(df) == 30 and report["n_games"] == 30
    assert report["skipped"] == {"not_regular_season": 1, "not_final": 0, "missing_score_or_period": 0, "unresolved_team": 0}
    assert report["test_seasons"] == [2024] and report["seasons_in_moneypuck_log"] == [2023, 2024]
    assert report["banner"] == W.BANNER and "1.0" in report["goalie_note"] and "No market comparison" in report["market_note"]
    assert report["n_games_cold_team"] == 0
    m = report["metrics"]
    for key in ("model", "league_poisson"):
        ml = m[key]["moneyline"]
        assert ml["n"] == 30 and 0 <= ml["brier"] <= 1 and np.isfinite(ml["log_loss"]) and 0 <= ml["ece"] <= 1
        assert sum(b["n"] for b in ml["calibration"]) == 30
        ot = m[key]["overtime"]
        assert ot["n"] == 30 and np.isfinite(ot["brier"]) and np.isfinite(ot["log_loss"])
        for line in ("5.5", "6.5"):
            t = m[key]["totals"][line]
            assert t["n"] == 30 and np.isfinite(t["brier"]) and np.isfinite(t["log_loss"])
        assert np.isfinite(m[key]["total"]["mae"]) and np.isfinite(m[key]["total"]["bias"])
    ch = m["constant_home"]["moneyline"]
    assert ch["n"] == 30 and np.isfinite(ch["brier"]) and 0 < ch["mean_p"] < 1
    assert set(report["by_season"]) == {"2024"} and report["by_season"]["2024"]["n"] == 30
    # probabilities are coherent and in range
    for c in ("p_home_win", "p_home_reg_win", "p_reg_tie", "p_over_5.5", "p_over_6.5", "league_poisson_p_home_win", "constant_home_p_home_win"):
        assert df[c].between(0, 1).all(), c
    assert (df["p_over_5.5"] >= df["p_over_6.5"]).all()
    assert np.allclose(df["p_reg_tie"], df["p_overtime"])
    assert df["expected_total"].between(3, 10).all()
    # the model carries team information: the strong team at home is favoured over the weak team at home
    tor_home = df[df["home"] == "TOR"]["p_home_win"].mean()
    tbl_home = df[df["home"] == "TBL"]["p_home_win"].mean()
    assert tor_home > tbl_home + 0.05
    # the naive baseline knows only home ice: its spread is Monte Carlo noise (SE ~ 0.022 at 500 draws), far below the model's
    assert df["league_poisson_p_home_win"].std() < 0.05 < df["p_home_win"].std()
    # outcomes joined from the official results
    src = ng.set_index("game_id")
    for r in df.itertuples():
        g = src.loc[r.game_id]
        assert r.y_home_win == int(bool(g["home_win"])) and r.y_total == int(g["home_score"] + g["away_score"])
        assert r.y_overtime == int(g["last_period_type"] != "REG")
    # the constant-home baseline joined to each game is the strictly-prior rate over BOTH seasons' results
    reg = ng[(ng["game_type"] == 2) & ng["final"].astype(bool)]
    for r in df.itertuples():
        prior = reg[reg["game_date"] < r.game_date]
        assert r.constant_home_p_home_win == pytest.approx(float(prior["home_win"].astype(float).mean()))
        assert len(prior) >= 30  # the 2023 season is always prior to a 2024 game
    # deterministic
    df2, _ = W.run_walk_forward(tg, ng, [2024], n_sims=500, base_seed=3)
    assert np.array_equal(df["p_home_win"].to_numpy(), df2["p_home_win"].to_numpy())
    # outputs
    paths = W.write_outputs(df, report, tmp_path / "research", "testrun")
    assert paths["json"].name == "walk_forward_testrun.json" and paths["markdown"].name == "WALK_FORWARD_V1.md"
    loaded = json.loads(paths["json"].read_text())
    assert loaded["run_id"] == "testrun" and loaded["metrics"]["model"]["moneyline"]["n"] == 30
    md = paths["markdown"].read_text()
    assert W.BANNER in md and "Goalie factors are fixed at 1.0" in md and "No market comparison" in md
    assert "| DATA_ONLY_V1 | 30 |" in md and "| constant_home | 30 |" in md and "| 2024 | 30 |" in md
    assert len(pd.read_csv(paths["games_csv"])) == 30


def test_max_games_and_empty_test_set(data, tmp_path: Path):
    _, tg, ng = data
    df, report = W.run_walk_forward(tg, ng, [2024], n_sims=200, max_games=5)
    assert len(df) == 5 and report["n_games"] == 5 and df["game_date"].is_monotonic_increasing
    df0, report0 = W.run_walk_forward(tg, ng, [2030], n_sims=200)
    assert df0.empty and report0["n_games"] == 0 and "metrics" not in report0
    paths = W.write_outputs(df0, report0, tmp_path / "r", "empty")
    assert "No games were scored" in paths["markdown"].read_text()


def test_cli_main(tmp_path: Path, monkeypatch, capsys):
    games = synthetic_schedule(SEASONS)
    install_fake_fetch(monkeypatch, games)
    hist = tmp_path / "history"
    assert H.run_history(hist, list(SEASONS))["n_errors"] == 0
    out = tmp_path / "docs"
    rc = W.main(["--history", str(hist), "--out", str(out), "--test-seasons", "2024", "--n-sims", "300", "--run", "cli"])
    assert rc == 0
    printed = json.loads(capsys.readouterr().out)
    assert printed["n_games"] == 30 and all(np.isfinite(v) for v in printed["moneyline_brier"].values())
    assert (out / "walk_forward_cli.json").exists() and (out / "walk_forward_cli_games.csv").exists() and (out / "WALK_FORWARD_V1.md").exists()
    assert W.main(["--history", str(tmp_path / "nothing"), "--out", str(out)]) == 2
