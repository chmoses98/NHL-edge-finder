"""Historical Kalshi ingestion (pagination, joining, no future-price leakage), V2 period pricing, and the V2 shadow arm's
guarantee that V1 output is identical with or without it."""

import json
import os
from pathlib import Path

import httpx
import numpy as np
import pandas as pd
import pytest

from nhl_edge.kalshi.client import KalshiClient, RateLimiter
from nhl_edge.research import kalshi_history as kh

REPO_DATA = Path(__file__).resolve().parents[1] / "data"


# ---------------------------------------------------------------------------------------------- Kalshi history
def _games() -> pd.DataFrame:
    return pd.DataFrame([
        {"game_id": 2025020010, "season": 2025, "game_type": 2, "game_date": "2025-10-09", "start_time_et": "2025-10-09T22:00:00", "home_abbrev": "VGK", "away_abbrev": "LAK"},
        {"game_id": 2025020011, "season": 2025, "game_type": 2, "game_date": "2025-10-09", "start_time_et": "2025-10-09T19:00:00", "home_abbrev": "NJD", "away_abbrev": "TBL"},
        {"game_id": 2024020011, "season": 2024, "game_type": 2, "game_date": "2024-10-12", "start_time_et": "2024-10-12T21:00:00", "home_abbrev": "UHC", "away_abbrev": "CHI"},
    ])


def test_game_join_handles_short_codes_and_utah_franchise_and_refuses_guesses():
    idx = kh.schedule_index(_games())
    g, why = kh.market_game({"event_ticker": "KXNHLGAME-25OCT09LAVGK"}, idx)
    assert why == "ok" and g["game_id"] == 2025020010
    g, _ = kh.market_game({"event_ticker": "KXNHLGAME-25OCT09TBNJ"}, idx)
    assert g["game_id"] == 2025020011
    g, _ = kh.market_game({"event_ticker": "KXNHLGAME-24OCT12CHIUTA"}, idx)
    assert g["game_id"] == 2024020011  # Utah Hockey Club (UHC) 2024-25 == Kalshi 'UTA'
    assert kh.market_game({"event_ticker": "KXNHLGAME-25OCT10LAVGK"}, idx)[0] is None  # wrong date: no guess
    assert kh.market_game({"event_ticker": "KXNHLGAME-25OCT09BOSVGK"}, idx)[0] is None  # wrong opponent
    assert kh.market_game({"event_ticker": "KXSTANLEYCUP-26"}, idx)[1] == "ticker not game-scoped"
    # start time is ET -> UTC
    assert idx[("2025-10-09", frozenset({"VGK", "LAK"}))]["start_ts"] == int(pd.Timestamp("2025-10-10T02:00:00Z").timestamp())


def test_horizon_quote_never_uses_a_candle_that_closed_after_the_instant():
    c = [{"end_period_ts": 1000, "yes_bid_close": 0.40, "yes_ask_close": 0.42},
         {"end_period_ts": 2000, "yes_bid_close": 0.60, "yes_ask_close": 0.62},
         {"end_period_ts": 3000, "yes_bid_close": 0.90, "yes_ask_close": 0.92}]
    q = kh.horizon_quote(c, 2999, 5000)
    assert q["end_period_ts"] == 2000 and q["mid"] == pytest.approx(0.61)
    assert kh.horizon_quote(c, 2000, 5000)["end_period_ts"] == 2000  # closing exactly at the instant is known at the instant
    assert kh.horizon_quote(c, 999, 5000) is None  # nothing existed yet
    assert kh.horizon_quote(c, 2999, 500) is None  # stale beyond the limit -> no quote rather than an old one


def test_horizon_quote_missing_sides_and_empty_markers():
    assert kh.horizon_quote([{"end_period_ts": 10, "yes_bid_close": None, "yes_ask_close": None}], 20, 100) is None
    q = kh.horizon_quote([{"end_period_ts": 10, "yes_bid_close": 0.0, "yes_ask_close": 0.30}], 20, 100)
    assert q["yes_bid"] is None and q["mid"] is None and q["yes_ask"] == pytest.approx(0.30)
    assert kh.horizon_quote([{"end_period_ts": float("nan"), "_empty": True}], 20, 100) is None


def test_slim_candle_reads_dollar_and_cent_payloads():
    a = kh._slim_candle({"end_period_ts": 5, "yes_bid": {"close_dollars": "0.5500"}, "yes_ask": {"close": 57}, "price": {"close": "0.56"}, "volume": 3})
    assert a["yes_bid_close"] == pytest.approx(0.55) and a["yes_ask_close"] == pytest.approx(0.57) and a["price_close"] == pytest.approx(0.56)


def test_candle_jobs_are_windowed_on_the_official_start_and_prioritised():
    idx = kh.schedule_index(_games())
    start = idx[("2025-10-09", frozenset({"VGK", "LAK"}))]["start_ts"]
    ms = [{"ticker": "KXNHLGAME-25OCT09LAVGK-VGK", "event_ticker": "KXNHLGAME-25OCT09LAVGK", "series_ticker": "KXNHLGAME"},
          {"ticker": "KXNHLTOTAL-25OCT09LAVGK-8", "event_ticker": "KXNHLTOTAL-25OCT09LAVGK", "series_ticker": "KXNHLTOTAL", "floor_strike": 7.5},
          {"ticker": "KXNHLTOTAL-25OCT09LAVGK-6", "event_ticker": "KXNHLTOTAL-25OCT09LAVGK", "series_ticker": "KXNHLTOTAL", "floor_strike": 5.5}]
    jobs = kh.candle_jobs(ms, idx, skip=set())
    assert [j["ticker"] for j in jobs][:2] == ["KXNHLGAME-25OCT09LAVGK-VGK"] * 2  # moneyline hourly + minute first
    assert jobs.index(next(j for j in jobs if j["ticker"].endswith("-6"))) < jobs.index(next(j for j in jobs if j["ticker"].endswith("-8")))
    m1 = next(j for j in jobs if j["interval"] == 1)
    assert m1["t1"] == start + 300 and m1["t0"] == start - kh.MINUTE_BEFORE_S
    assert not kh.candle_jobs(ms, idx, skip={("KXNHLGAME-25OCT09LAVGK-VGK", 60), ("KXNHLGAME-25OCT09LAVGK-VGK", 1)})[0]["ticker"].startswith("KXNHLGAME")


def test_historical_markets_paginate_and_merge_with_live(tmp_path, monkeypatch):
    pages = {None: {"markets": [{"ticker": "KXNHLGAME-25OCT09LAVGK-VGK", "event_ticker": "KXNHLGAME-25OCT09LAVGK", "result": "yes"}], "cursor": "c2"},
             "c2": {"markets": [{"ticker": "KXNHLGAME-25OCT09LAVGK-LA", "event_ticker": "KXNHLGAME-25OCT09LAVGK", "result": "no"}], "cursor": ""}}
    calls = []

    def handler(req: httpx.Request) -> httpx.Response:
        calls.append(str(req.url))
        if "/historical/markets" in req.url.path:
            return httpx.Response(200, json=pages[req.url.params.get("cursor")])
        if req.url.path.endswith("/markets"):
            return httpx.Response(200, json={"markets": [{"ticker": "KXNHLGAME-25OCT09LAVGK-VGK", "title": "live title", "result": ""}], "cursor": ""})
        return httpx.Response(404)

    client = KalshiClient(rate=RateLimiter(rate_per_s=1000), transport=httpx.MockTransport(handler))
    hist = tmp_path / "hist"
    (hist / "nhl").mkdir(parents=True)
    g = _games()
    g["final"], g["home_score"], g["away_score"], g["last_period_type"], g["home_win"] = True, 3, 2, "REG", True
    g.to_parquet(hist / "nhl" / "games_2025.parquet")
    assert kh.run_kalshi_history(tmp_path, hist, ["KXNHLGAME"], "2025-09-01", "2026-07-01", client=client) == 0
    rows = kh.read_jsonl_gz(tmp_path / "kalshi" / "markets_KXNHLGAME.jsonl.gz")
    by = {r["ticker"]: r for r in rows}
    assert len(rows) == 2 and by["KXNHLGAME-25OCT09LAVGK-VGK"]["_source"] == "both"
    assert by["KXNHLGAME-25OCT09LAVGK-VGK"]["result"] == "yes"  # historical wins over the live blank
    assert by["KXNHLGAME-25OCT09LAVGK-VGK"]["title"] == "live title"  # live fills gaps
    man = json.loads((tmp_path / "kalshi" / "MANIFEST.json").read_text())
    assert man["series"]["KXNHLGAME"]["join"] == {"ok": 2}
    assert sum("cursor=c2" in c for c in calls) == 1


# ---------------------------------------------------------------------------------------------- period pricing
def _contract(**kw):
    from nhl_edge.schemas.market import Contract

    base = dict(ticker="T", series_ticker="S", event_ticker="E", family="period_winner", scope="game", stat="winner", period="P1", settles_on="PERIOD",
                game_id=None, game_date="2026-09-29", team_id=None, opponent_team_id=None, game_team_ids=[1, 2], threshold=None, comparator=None,
                upper=None, support="RESEARCH", semantics_confidence="high", notes=[])
    fields = set(Contract.model_fields)
    return Contract(**{k: v for k, v in (base | kw).items() if k in fields})


def test_period_contracts_price_coherently_and_stay_partial():
    from nhl_edge.pricing.price_v2 import PERIOD_SUPPORT, price_contract_v2
    from nhl_edge.sim.engine import TeamParams
    from nhl_edge.sim.engine_v2 import load_params, simulate_game_v2

    res = simulate_game_v2(TeamParams(1, "H", 3.3), TeamParams(2, "A", 2.7), seed=9, n_sims=20000, params=load_params())
    for q in ("P1", "P2", "P3"):
        tie, s1 = price_contract_v2(_contract(period=q), res, 1, 2)
        home, _ = price_contract_v2(_contract(period=q, team_id=1), res, 1, 2)
        away, _ = price_contract_v2(_contract(period=q, team_id=2), res, 1, 2)
        assert tie.p + home.p + away.p == pytest.approx(1.0) and home.p > away.p and s1 == PERIOD_SUPPORT
        tots = [price_contract_v2(_contract(family="period_total", stat="total", period=q, threshold=x, comparator="gt"), res, 1, 2)[0].p for x in (0.5, 1.5, 2.5)]
        assert tots[0] > tots[1] > tots[2]
        sp, _ = price_contract_v2(_contract(family="period_spread", stat="margin", period=q, team_id=1, threshold=1.5, comparator="gt"), res, 1, 2)
        assert sp.p < home.p
    assert price_contract_v2(_contract(period="P1", team_id=99), res, 1, 2)[0].supported is False


# ---------------------------------------------------------------------------------------------- shadow arm vs V1
@pytest.mark.slow
def test_v1_output_is_identical_with_and_without_the_v2_shadow(tmp_path, monkeypatch):
    from nhl_edge.archive.ledger import Ledger
    from nhl_edge.workflows.simulate import run_simulate
    from tests.archive_fixture import NOW, build_archive

    out = {}
    for flag in ("0", "1"):
        monkeypatch.setenv("NHL_EDGE_V2_SHADOW", flag)
        root = tmp_path / f"a{flag}"
        build_archive(root)
        assert run_simulate(root, REPO_DATA, date="2026-09-29", n_sims=2000, now=NOW) == 0
        rows = sorted(Ledger(root).iter_rows("predictions"), key=lambda r: r["ticker"])
        out[flag] = [{k: v for k, v in r.items() if k not in ("prediction_id", "_run_id", "_observed_at_utc", "input_snapshot_ids")} for r in rows]
        slate = json.loads((root / "slates" / "latest" / "slate.json").read_text())
        if flag == "0":
            assert "v2_shadow" not in slate and not list(Ledger(root).iter_rows("predictions_v2"))
        else:
            v2 = slate["v2_shadow"]
            assert "error" not in v2, v2.get("error")
            assert v2["model_version"] == "DATA_ONLY_V2" and v2["role"] == "SHADOW" and v2["authority"] == "RESEARCH_ONLY"
            assert len(v2["blocks"]) == 5 and all(b["detail"]["ladder_violations"] == [] for b in v2["blocks"])
            rows2 = list(Ledger(root).iter_rows("predictions_v2"))
            assert rows2 and {r["model_version"] for r in rows2} == {"DATA_ONLY_V2"} and {r["authority"] for r in rows2} == {"RESEARCH_ONLY"}
            assert all(r["predicted_at_utc"].startswith("2026-09-29T15:00") for r in rows2)  # stamped with the run's true instant
            packet = json.loads((root / "slates" / "latest" / "packet.json").read_text())
            assert "v2_shadow" in packet and "DATA_ONLY_V2 shadow" in (root / "slates" / "latest" / "slate.md").read_text()
    assert out["0"] == out["1"]


def test_v2_failure_never_breaks_v1(tmp_path, monkeypatch):
    from nhl_edge.workflows import shadow_v2
    from nhl_edge.workflows.simulate import run_simulate
    from tests.archive_fixture import NOW, build_archive

    def boom(*a, **k):
        raise RuntimeError("synthetic V2 failure")

    monkeypatch.setattr(shadow_v2, "run_shadow", boom)
    monkeypatch.setenv("NHL_EDGE_V2_SHADOW", "1")
    root = tmp_path / "a"
    build_archive(root)
    assert run_simulate(root, REPO_DATA, date="2026-09-29", n_sims=500, now=NOW) == 0
    slate = json.loads((root / "slates" / "latest" / "slate.json").read_text())
    assert slate["coverage"]["contracts_joined"] == 14 and "synthetic V2 failure" in slate["v2_shadow"]["error"]
    assert np.isfinite([r["p_data_only"] for r in slate["contracts"] if r["p_data_only"] is not None]).all()
    assert os.environ["NHL_EDGE_V2_SHADOW"] == "1"
