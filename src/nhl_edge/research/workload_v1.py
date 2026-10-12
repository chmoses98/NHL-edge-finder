"""WORKLOAD_V1: a sports-only research challenger for skater shots on goal and goalie saves (RESEARCH_ONLY).

Built to separate WORKLOAD (minutes by strength state, power-play / penalty-kill minutes of THIS matchup, overtime
minutes, the shots a goalie will face) from EFFICIENCY (shots per minute given the minutes, saves given the shots),
and to repair what the decomposition audit (``workload_audit``) found. Inputs are official NHL api-web / stats data in
``data/history/players`` only: no sportsbook, no Kalshi price, no market-derived quantity, directly or through another
model (the DATA_ONLY_V2 lambdas are not used either).

Skaters, per state s in {evreg (regulation even strength), pp, sh, ea (own net empty), en (opponent net empty), ot}:

    team seconds  ``team_states`` stretches every overtime game's timeline to 80:00 and books the phantom minutes to
                  one strength state; ``team_games`` removes the phantom (1200 - actual OT length) from the state whose
                  booked seconds exceed what the players' own shift presence implies, so shares are not deflated
    matchup       PP = league x (own drawn / league) x (opponent's taken / league), SH symmetric, EA / EN = league,
                  EV regulation = 3600 - PP - SH - EA - EN (team rates: half-life ``hl_team`` games, ``k_team``
                  pseudo-games); overtime = P(OT) x E[OT length] (league, point-in-time training constants)
    minutes       ``minutes_mode="share"``: share of the team's state seconds (half-life ``hl_share`` games,
                  ``k_share`` pseudo-games of the position mean) x the matchup's team seconds;
                  ``minutes_mode="direct"``: the player's own recent state minutes (same memory and shrinkage) x the
                  matchup ratio (PP x opponent's taken / league, SH x opponent's drawn / league, EV x its complement)
    rates         shots per 60 RELATIVE TO THE LEAGUE AT THE TIME (point-in-time league rate by position x state over
                  the last ``league_rows`` skater-games): index = (shots + k) / (league-rate expected shots + k), with
                  ``k_rate[s]`` minutes of prior; rate now = index x the league rate now. League shot volume fell
                  from 31.6 to 27.7 per team-game over 2021-26, so raw long-memory rates run high.
                  Overtime rate = EV rate x position OT multiplier (training)
    mean SOG      venue x (opponent shots-against factor)^beta_opp x sum_s minutes_s x rate_s / 60
    SOG           ~ NegBin(mean, alpha), alpha fit on the previous season's own residuals

Goalies (CONDITIONAL_ON_ACTUAL_STARTER for the save-fraction term, which uses the starter's identity):

    SA_net        league x (opponent SF / league) x (own SA / league) x venue (regulation, empty-net shots excluded;
                  optionally schedule-adjusted) + P(OT) x E[OT shots against | OT]
    SA_start      ~ NegBin(SA_net, alpha_sa); with probability p_pull the starter faces only f_pull of them
    sv            league save fraction (point-in-time) x the goalie's shrunk relative save fraction (``k_sv`` shots)
    saves | SA    ~ Binomial(SA_start, sv)

Everything at date D uses rows strictly before D; constants (position priors, OT multiplier, venue, alpha, p_pull,
f_pull, E[OT length]) are fit on seasons strictly before the evaluated season.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.research import workload_eval as E

MODEL_VERSION = "WORKLOAD_V1"
SOG_K = 16  # skater SOG pmf support 0..15 (15 = 15+)
SAVES_K = 80
SA_K = 90
REG_W = ("evreg", "pp", "sh", "ea", "en")
STATES_W = REG_W + ("ot",)
ON_ICE = {"evreg": 5.0, "pp": 5.0, "sh": 4.0, "ea": 6.0, "en": 5.0}  # skaters on the ice for the team in the state


@dataclass(frozen=True)
class WorkloadParams:
    minutes_mode: str = "share"  # "share" | "direct"
    hl_share: float = 6.0  # games; deployment memory
    k_share: float = 0.5  # pseudo-games of the position mean
    hl_rate: float = 60.0  # games; shot-rate memory
    k_rate: dict[str, float] = field(default_factory=lambda: {"evreg": 200.0, "pp": 30.0, "sh": 30.0, "ea": 5.0, "en": 5.0})  # minutes of prior
    league_rows: int = 20000  # skater-games per position in the point-in-time league shot rate
    beta_opp: float = 0.5  # exponent on the opponent's shots-against factor
    hl_opp: float = 25.0  # team-games; opponent shots-against memory (skater opponent adjustment)
    k_opp: float = 15.0
    hl_team: float = 20.0  # team-games; penalty drawing / taking memory
    k_team: float = 10.0
    # goalies
    hl_sa: float = 25.0  # team-games; shot-for / shot-against memory
    k_sa: float = 15.0
    schedule_adjust: bool = False
    k_sv: float = 2000.0  # shots of prior on the goalie's relative save fraction
    league_window: int = 1200  # team-games in the point-in-time league level (skater team tables)
    league_window_sa: int = 1200  # team-games in the point-in-time league shots-against level (goalies)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> WorkloadParams:
        base = asdict(cls())
        base.update({k: v for k, v in (d or {}).items() if k in base})
        return cls(**base)


# ---------------------------------------------------------------------------------------------------------------------
# point-in-time exponentially weighted sums
# ---------------------------------------------------------------------------------------------------------------------
def ew_prior_sums(groups: np.ndarray, X: np.ndarray, half_life: float) -> np.ndarray:
    """Rows must be sorted by (group, time). Returns, for each row, sum_{j earlier in the same group} d^(gap) X_j with
    d = 0.5^(1/half_life) and gap = number of the group's rows in between (0 for the previous row, i.e. weight 1); the
    row itself is NEVER included (point in time). NaN entries of X contribute nothing (the decay still advances).
    Vectorised as d^(k_i - 1) * sum_{j<i} d^(-k_j) X_j over the within-group rank k; falls back to a loop when a group
    is long enough for d^(-k) to overflow."""
    X = np.asarray(X, float)
    if X.ndim == 1:
        X = X[:, None]
    groups = np.asarray(groups)
    n = len(X)
    out = np.zeros_like(X)
    if n == 0:
        return out
    Xc = np.nan_to_num(X)
    d = 0.5 ** (1.0 / half_life)
    start = np.r_[True, groups[1:] != groups[:-1]]
    gidx = np.cumsum(start) - 1
    first = np.flatnonzero(start)
    k = np.arange(n) - first[gidx]
    if k.max() * np.log2(1.0 / d) > 900:
        acc = np.zeros(X.shape[1])
        for i in range(n):
            if start[i]:
                acc[:] = 0.0
            out[i] = acc
            acc = d * acc + Xc[i]
        return out
    Y = d ** (-k.astype(float))[:, None] * Xc
    excl = pd.DataFrame(Y).groupby(gidx).cumsum().to_numpy() - Y  # within-group sums over rows strictly before i
    out = excl * (d ** (k.astype(float) - 1.0))[:, None]
    out[start] = 0.0
    return out


def league_prior_mean(dates: np.ndarray, values: np.ndarray, query_dates: np.ndarray, window: int) -> np.ndarray:
    """Mean of the last ``window`` values dated strictly before each query date (``dates`` sorted ascending)."""
    cs = np.concatenate([[0.0], np.cumsum(values)])
    hi = np.searchsorted(dates, query_dates, side="left")
    lo = np.maximum(hi - window, 0)
    n = np.maximum(hi - lo, 1)
    m = (cs[hi] - cs[lo]) / n
    return np.where(hi > 0, m, np.nan)


def _div(a: np.ndarray, b: np.ndarray, fallback: np.ndarray | float) -> np.ndarray:
    a, b = np.asarray(a, float), np.asarray(b, float)
    with np.errstate(invalid="ignore", divide="ignore"):
        r = a / b
    return np.where(np.isfinite(r) & (b > 0), r, fallback)


# ---------------------------------------------------------------------------------------------------------------------
# tables
# ---------------------------------------------------------------------------------------------------------------------
def _date_int(s: pd.Series) -> np.ndarray:
    return s.astype(str).str.replace("-", "").str[:8].astype(int).to_numpy()


def ot_lengths(goals: pd.DataFrame, team_states: pd.DataFrame) -> pd.Series:
    """Seconds of regular-season overtime actually played, per game: the OT winner's clock, else 300 (shootout)."""
    ts = team_states[team_states["game_type"] == 2]
    ot_games = ts.loc[ts["n_seconds"] > 3600, "game_id"].unique()
    g = goals[(goals["period"] == 4)]
    if "game_type" in g.columns:
        g = g[g["game_type"] == 2]
    win = g.groupby("game_id")["t_s"].min() - 3600
    L = pd.Series(300.0, index=pd.Index(ot_games, name="game_id"))
    common = L.index.intersection(win.index)
    L.loc[common] = win.loc[common].clip(lower=1, upper=300).astype(float)
    return L


def repair_ot_timeline(ts: pd.DataFrame, presence: pd.DataFrame) -> pd.DataFrame:
    """Remove the phantom seconds of regular-season OT games (timeline stretched to 4800 s) from the one state that
    holds them: the state whose booked seconds most exceed the players' shift presence / skaters on the ice.
    ``ts`` needs ``ot_len``; ``presence`` (game_id, team_id, p_ev, p_pp, p_sh, p_ea, p_en) = summed skater seconds."""
    t = ts.merge(presence, on=["game_id", "team_id"], how="left")
    cols = {"ev": "evreg", "pp": "pp", "sh": "sh", "ea": "ea", "en": "en"}
    excess = np.column_stack([t[f"sec_{s}"].to_numpy(float) - t[f"p_{s}"].fillna(0).to_numpy(float) / ON_ICE[w] for s, w in cols.items()])
    phantom = (t["n_seconds"] - 3600 - t["ot_len"]).clip(lower=0).to_numpy(float)
    fix = (t["game_type"].to_numpy() == 2) & (t["n_seconds"].to_numpy() > 3600) & t["p_ev"].notna().to_numpy()
    which = np.argmax(excess, axis=1)
    for j, s in enumerate(cols):
        m = fix & (which == j)
        v = t[f"sec_{s}"].to_numpy(float)
        v[m] = np.maximum(v[m] - phantom[m], 0.0)
        t[f"sec_{s}"] = v
    t["repaired"] = fix
    return t.drop(columns=[c for c in presence.columns if c.startswith("p_")])


def team_games(players: pd.DataFrame, team_states: pd.DataFrame, shots: pd.DataFrame, goals: pd.DataFrame) -> pd.DataFrame:
    """One row per (game, team): repaired state seconds, regulation / OT shots for and against (empty-net shots are
    excluded from 'against': goalies never face them), opponent id, OT length, date."""
    ts = team_states.copy()
    ts["date_int"] = _date_int(ts["game_date"])
    ts["opp_id"] = np.where(ts["is_home"], ts["away_team_id"], ts["home_team_id"])
    ts["clean"] = ts["n_seconds"] == 3600
    L = ot_lengths(goals, team_states)
    ts["ot_len"] = ts["game_id"].map(L).fillna(0.0)
    ts["ot_game"] = (ts["n_seconds"] > 3600) & (ts["game_type"] == 2)
    ok = players[players["shifts_ok"].fillna(False).astype(bool)]
    pres = ok.groupby(["game_id", "team_id"])[["toi_ev_s", "toi_pp_s", "toi_sh_s", "toi_ea_s", "toi_en_s"]].sum()
    pres.columns = ["p_ev", "p_pp", "p_sh", "p_ea", "p_en"]
    ts = repair_ot_timeline(ts, pres.reset_index())
    s = shots[shots["kind"].isin(["GOAL", "SOG"])].copy()
    s["def_team"] = np.where(s["is_home"], s["away_team_id"], s["home_team_id"])
    s["reg"] = s["period"] <= 3
    s = s[s["strength"] != "EN"]
    fa = s.groupby(["game_id", "def_team", "reg"]).size().unstack("reg", fill_value=0)
    fa.columns = ["sa_ot" if not c else "sa_reg" for c in fa.columns]
    fa.index = fa.index.set_names(["game_id", "team_id"])
    ts = ts.merge(fa.reset_index(), on=["game_id", "team_id"], how="left")
    for c in ("sa_reg", "sa_ot"):
        ts[c] = ts[c].fillna(0.0) if c in ts.columns else 0.0
    opp = ts[["game_id", "team_id", "sa_reg", "sa_ot"]].rename(columns={"team_id": "opp_id", "sa_reg": "sf_reg", "sa_ot": "sf_ot"})
    ts = ts.merge(opp, on=["game_id", "opp_id"], how="left")
    return ts.sort_values(["date_int", "game_id", "team_id"]).reset_index(drop=True)


def shots_ot_by_player(shots: pd.DataFrame) -> pd.DataFrame:
    s = shots[(shots["period"] == 4) & shots["kind"].isin(["GOAL", "SOG"]) & shots["shooter_id"].notna()]
    if "game_type" in s.columns:
        s = s[s["game_type"] == 2]
    return s.groupby(["game_id", "shooter_id"]).size().rename("sog_ot").reset_index().rename(columns={"shooter_id": "player_id"})


def skater_table(players: pd.DataFrame, tg: pd.DataFrame, shots: pd.DataFrame) -> pd.DataFrame:
    """One row per skater-game with the workload / efficiency quantities by WORKLOAD_V1 state (``t_*`` player
    seconds, ``s_*`` shots on goal, ``T_*`` team seconds; NaN where the game has no shift charts)."""
    p = players.copy()
    p["date_int"] = _date_int(p["game_date"])
    p["pos"] = np.where(p["position"].astype(str).str.upper().str.startswith("D"), "D", "F")
    p = p.merge(shots_ot_by_player(shots), on=["game_id", "player_id"], how="left")
    p["sog_ot"] = p["sog_ot"].fillna(0.0)
    t = tg[["game_id", "team_id", "opp_id", "clean", "repaired", "sec_ev", "sec_pp", "sec_sh", "sec_ea", "sec_en", "ot_len", "ot_game"]]
    p = p.merge(t, on=["game_id", "team_id"], how="left")
    ok = p["shifts_ok"].fillna(False).astype(bool)
    f = lambda c: pd.to_numeric(p[c], errors="coerce").where(ok)  # noqa: E731
    toi_ot = f("toi_ot_s").fillna(0.0).where(ok)
    p["t_evreg"] = (f("toi_ev_s") - toi_ot).clip(lower=0)
    p["t_pp"], p["t_sh"], p["t_ea"], p["t_en"] = f("toi_pp_s"), f("toi_sh_s"), f("toi_ea_s"), f("toi_en_s")
    p["t_ot"] = toi_ot
    sog_ot = p["sog_ot"].where(ok)
    p["s_evreg"] = (p["sog_ev"].where(ok) - sog_ot).clip(lower=0)
    p["s_pp"], p["s_sh"], p["s_ea"], p["s_en"] = (p[c].where(ok) for c in ("sog_pp", "sog_sh", "sog_ea", "sog_en"))
    p["s_ot"] = sog_ot
    otg = p["ot_game"].fillna(False).astype(bool)
    cl = ok & (p["clean"].fillna(False).astype(bool) | p["repaired"].fillna(False).astype(bool))
    p["share_ok"] = cl
    ot_len = p["ot_len"].fillna(0.0)
    p["T_evreg"] = (p["sec_ev"] - np.where(otg, ot_len, 0.0)).clip(lower=0).where(cl)
    p["T_pp"], p["T_sh"], p["T_ea"], p["T_en"] = (p[c].where(cl) for c in ("sec_pp", "sec_sh", "sec_ea", "sec_en"))
    otok = ok & otg & (ot_len > 0)
    p["T_ot"] = ot_len.where(otok)
    p["t_ot_share"] = p["t_ot"].where(otok)
    return p.sort_values(["player_id", "date_int", "game_id"]).reset_index(drop=True)


# ---------------------------------------------------------------------------------------------------------------------
# constants fit on training seasons
# ---------------------------------------------------------------------------------------------------------------------
@dataclass
class TrainedConstants:
    share_prior: dict[str, dict[str, float]]  # pos -> state -> mean share of the team's state seconds
    minutes_prior: dict[str, dict[str, float]]  # pos -> state -> mean seconds per game
    rate_prior: dict[str, dict[str, float]]  # pos -> state -> shots per 60 (training average; fallback only)
    ot_mult: dict[str, float]  # pos -> OT shots per minute / EV-regulation shots per minute
    venue_sog: float  # home / away skater shot-rate ratio (sqrt applied each side)
    p_ot: float
    ot_len: float  # seconds | OT
    ot_sa: float  # shots against per team per OT game
    venue_sa: float  # away / home regulation shots faced ratio
    p_pull: float
    f_pull: float
    train_seasons: list[int]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def fit_constants(sk: pd.DataFrame, tg: pd.DataFrame, goalies: pd.DataFrame, seasons: list[int]) -> TrainedConstants:
    d = sk[sk["season"].isin(seasons) & (sk["game_type"] == 2)]
    share_prior, minutes_prior, rate_prior, ot_mult = {}, {}, {}, {}
    for pos, dd in d.groupby("pos"):
        cl = dd[dd["share_ok"]]
        share_prior[pos] = {s: float(cl[f"t_{s}"].sum() / max(cl[f"T_{s}"].sum(), 1.0)) for s in REG_W}
        minutes_prior[pos] = {s: float(cl[f"t_{s}"].mean()) for s in REG_W}
        o = dd[dd["T_ot"].notna()]
        share_prior[pos]["ot"] = float(o["t_ot"].sum() / max(o["T_ot"].sum(), 1.0))
        rate_prior[pos] = {s: float(dd[f"s_{s}"].sum() / max(dd[f"t_{s}"].sum() / 3600.0, 1e-9)) for s in STATES_W}
        ot_mult[pos] = float(rate_prior[pos]["ot"] / max(rate_prior[pos]["evreg"], 1e-9))
    tot = d.groupby("is_home").apply(lambda x: x["sog"].sum() / max(x["toi_s"].sum(), 1.0), include_groups=False)
    venue_sog = float(tot.get(True, 1.0) / tot.get(False, 1.0))
    t = tg[tg["season"].isin(seasons) & (tg["game_type"] == 2)]
    games = t.drop_duplicates("game_id")
    p_ot = float(games["ot_game"].mean())
    ot_len = float(games.loc[games["ot_game"], "ot_len"].mean())
    ot_sa = float(t.loc[t["ot_game"], "sa_ot"].mean())
    va = t.groupby("is_home")["sa_reg"].mean()
    venue_sa = float(va.get(False, 1.0) / va.get(True, 1.0))
    g = goalies[goalies["season"].isin(seasons) & (goalies["game_type"] == 2)]
    n_used = g[g["toi_s"].fillna(0) > 0].groupby(["game_id", "team_id"]).size()
    st = g[g["starter"].astype(bool)].copy()
    st["n_used"] = [int(n_used.get((a, b), 1)) for a, b in zip(st["game_id"], st["team_id"])]
    net = g.groupby(["game_id", "team_id"])["shots_against"].sum()
    st["net_sa"] = [float(net.get((a, b), np.nan)) for a, b in zip(st["game_id"], st["team_id"])]
    pulled = st[st["n_used"] > 1]
    p_pull = float((st["n_used"] > 1).mean())
    f_pull = float((pulled["shots_against"] / pulled["net_sa"].clip(lower=1)).mean()) if len(pulled) else 0.5
    return TrainedConstants(share_prior, minutes_prior, rate_prior, ot_mult, venue_sog, p_ot, ot_len, ot_sa, venue_sa, p_pull, f_pull,
                            sorted(int(s) for s in seasons))


# ---------------------------------------------------------------------------------------------------------------------
# skater predictions
# ---------------------------------------------------------------------------------------------------------------------
def team_minutes(tg: pd.DataFrame, prm: WorkloadParams) -> pd.DataFrame:
    """Point-in-time expected team seconds by state for each (game, team), plus the opponent penalty ratios."""
    t = tg.sort_values(["team_id", "date_int", "game_id"]).reset_index(drop=True)
    ok = (t["clean"] | t["repaired"]).to_numpy()
    X = np.column_stack([np.where(ok, t["sec_pp"], np.nan), np.where(ok, t["sec_sh"], np.nan), ok.astype(float)])
    S = ew_prior_sums(t["team_id"].to_numpy(), X, prm.hl_team)
    lt = tg[tg["clean"]].sort_values("date_int")
    dts, q = lt["date_int"].to_numpy(), t["date_int"].to_numpy()
    for c in ("sec_pp", "sec_ea", "sec_en"):
        t[f"lg_{c}"] = league_prior_mean(dts, lt[c].to_numpy(float), q, prm.league_window)
    lg = t["lg_sec_pp"]
    t["draw"] = (S[:, 0] + prm.k_team * lg) / (S[:, 2] + prm.k_team)
    t["take"] = (S[:, 1] + prm.k_team * lg) / (S[:, 2] + prm.k_team)
    o = t[["game_id", "team_id", "draw", "take"]].rename(columns={"team_id": "opp_id", "draw": "o_draw", "take": "o_take"})
    t = t.merge(o, on=["game_id", "opp_id"], how="left")
    t["o_take_ratio"] = (t["o_take"] / lg).fillna(1.0)
    t["o_draw_ratio"] = (t["o_draw"] / lg).fillna(1.0)
    t["E_pp"] = lg * (t["draw"] / lg) * t["o_take_ratio"]
    t["E_sh"] = lg * (t["take"] / lg) * t["o_draw_ratio"]
    t["E_ea"], t["E_en"] = t["lg_sec_ea"], t["lg_sec_en"]
    t["E_evreg"] = 3600.0 - t["E_pp"] - t["E_sh"] - t["E_ea"] - t["E_en"]
    lg_ev = 3600.0 - 2 * lg - t["E_ea"] - t["E_en"]
    t["ev_ratio"] = (t["E_evreg"] / lg_ev).fillna(1.0)
    return t[["game_id", "team_id", "E_evreg", "E_pp", "E_sh", "E_ea", "E_en", "o_take_ratio", "o_draw_ratio", "ev_ratio"]]


def opp_sa_factor(tg: pd.DataFrame, prm: WorkloadParams) -> pd.DataFrame:
    """Point-in-time opponent shots-against-per-game factor (regulation, all strengths) for each (game, team)."""
    t = tg.sort_values(["team_id", "date_int", "game_id"]).reset_index(drop=True)
    S = ew_prior_sums(t["team_id"].to_numpy(), np.column_stack([t["sa_reg"], np.ones(len(t))]), prm.hl_opp)
    lt = tg.sort_values("date_int")
    lg = league_prior_mean(lt["date_int"].to_numpy(), lt["sa_reg"].to_numpy(float), t["date_int"].to_numpy(), prm.league_window)
    t["lg"] = lg
    t["sa_rate"] = (S[:, 0] + prm.k_opp * lg) / (S[:, 1] + prm.k_opp)
    o = t[["game_id", "team_id", "sa_rate"]].rename(columns={"team_id": "opp_id", "sa_rate": "opp_sa_rate"})
    t = t.merge(o, on=["game_id", "opp_id"], how="left")
    t["opp_factor"] = (t["opp_sa_rate"] / t["lg"]).fillna(1.0)
    return t[["game_id", "team_id", "opp_factor"]]


def league_rates(sk: pd.DataFrame, window: int) -> pd.DataFrame:
    """Point-in-time league shots per 60 by position x state for every row of ``sk`` (last ``window`` skater-games of
    that position dated strictly before the row's date)."""
    out = pd.DataFrame(index=sk.index)
    for pos, d in sk.groupby("pos"):
        d = d.sort_values("date_int")
        dts = d["date_int"].to_numpy()
        q = sk.loc[sk["pos"] == pos, "date_int"].to_numpy()
        idx = sk.index[sk["pos"] == pos]
        for s in STATES_W:
            num = league_prior_mean(dts, d[f"s_{s}"].fillna(0).to_numpy(float), q, window)
            den = league_prior_mean(dts, d[f"t_{s}"].fillna(0).to_numpy(float), q, window)
            out.loc[idx, f"lgr_{s}"] = _div(num, den / 3600.0, np.nan)
    return out


def skater_predictions(sk: pd.DataFrame, tg: pd.DataFrame, c: TrainedConstants, prm: WorkloadParams) -> pd.DataFrame:
    """Expected minutes by state, shot rates and mean SOG for every row of ``sk`` (point in time)."""
    d = sk.reset_index(drop=True).copy()
    grp = d["player_id"].to_numpy()
    pos = d["pos"].to_numpy()
    n0 = len(d)
    d = d.merge(team_minutes(tg, prm), on=["game_id", "team_id"], how="left")
    d = d.merge(opp_sa_factor(tg, prm), on=["game_id", "team_id"], how="left")
    if len(d) != n0:
        raise ValueError("team tables are not unique per (game, team)")
    for s in ("E_evreg", "E_pp", "E_sh", "E_ea", "E_en"):
        d[s] = d[s].fillna(d[s].mean())
    # --- workload: minutes by state
    shok = d["share_ok"].to_numpy()
    if prm.minutes_mode == "share":
        Xs = np.column_stack([np.where(shok, d[f"t_{s}"], np.nan) for s in REG_W] + [np.where(shok, d[f"T_{s}"], np.nan) for s in REG_W] + [shok.astype(float)])
        Ss = ew_prior_sums(grp, Xs, prm.hl_share)
        w = Ss[:, -1]
        for j, s in enumerate(REG_W):
            prior = np.array([c.share_prior[p_][s] for p_ in pos])
            Tsum = Ss[:, len(REG_W) + j]
            avg_T = _div(Tsum, w, d[f"E_{s}"].to_numpy(float))
            avg_T = np.where(avg_T > 0, avg_T, np.maximum(d[f"E_{s}"].to_numpy(float), 1.0))
            share = (Ss[:, j] + prm.k_share * prior * avg_T) / (Tsum + prm.k_share * avg_T)
            d[f"share_{s}"] = share
            d[f"wl_toi_{s}"] = share * d[f"E_{s}"].to_numpy(float) / 60.0
    elif prm.minutes_mode == "direct":
        okm = d["t_evreg"].notna().to_numpy()
        Xs = np.column_stack([np.where(okm, d[f"t_{s}"], np.nan) for s in REG_W] + [okm.astype(float)])
        Ss = ew_prior_sums(grp, Xs, prm.hl_share)
        w = Ss[:, -1]
        ratio = {"evreg": d["ev_ratio"].to_numpy(float), "pp": d["o_take_ratio"].to_numpy(float), "sh": d["o_draw_ratio"].to_numpy(float),
                 "ea": np.ones(len(d)), "en": np.ones(len(d))}
        for j, s in enumerate(REG_W):
            prior = np.array([c.minutes_prior[p_][s] for p_ in pos])
            mins = (Ss[:, j] + prm.k_share * prior) / (w + prm.k_share)
            d[f"wl_toi_{s}"] = mins * ratio[s] / 60.0
    else:
        raise ValueError(f"unknown minutes_mode {prm.minutes_mode!r}")
    Xo = np.column_stack([d["t_ot_share"].to_numpy(float), d["T_ot"].to_numpy(float)])
    So = ew_prior_sums(grp, Xo, prm.hl_share * 3)  # OT is rarer: a longer memory in games
    prior_ot = np.array([c.share_prior[p_]["ot"] for p_ in pos])
    d["share_ot"] = (So[:, 0] + prm.k_share * prior_ot * c.ot_len) / (So[:, 1] + prm.k_share * c.ot_len)
    d["wl_toi_ot"] = d["share_ot"] * c.p_ot * c.ot_len / 60.0
    d["wl_toi"] = sum(d[f"wl_toi_{s}"] for s in STATES_W)
    # --- efficiency: shots per 60 relative to the league at the time
    lr = league_rates(d, prm.league_rows)
    for s in STATES_W:
        fb = np.array([c.rate_prior[p_][s] for p_ in pos])
        d[f"lgr_{s}"] = lr[f"lgr_{s}"].fillna(pd.Series(fb, index=d.index))
    Xr = np.column_stack([d[f"s_{s}"].to_numpy(float) for s in REG_W] + [d[f"t_{s}"].to_numpy(float) / 3600.0 * d[f"lgr_{s}"].to_numpy(float) for s in REG_W])
    Sr = ew_prior_sums(grp, Xr, prm.hl_rate)
    for j, s in enumerate(REG_W):
        k_shots = prm.k_rate[s] / 60.0 * d[f"lgr_{s}"].to_numpy(float)  # k minutes of league-rate shots
        idx = _div(Sr[:, j] + k_shots, Sr[:, len(REG_W) + j] + k_shots, 1.0)
        d[f"wl_index_{s}"] = idx
        d[f"wl_rate_{s}"] = idx * d[f"lgr_{s}"].to_numpy(float)
    d["wl_rate_ot"] = d["wl_rate_evreg"] * np.array([c.ot_mult[p_] for p_ in pos])
    venue = np.where(d["is_home"].to_numpy(bool), np.sqrt(c.venue_sog), 1.0 / np.sqrt(c.venue_sog))
    opp = np.power(np.clip(d["opp_factor"].to_numpy(float), 0.5, 2.0), prm.beta_opp)
    d["wl_adj"] = venue * opp
    d["wl_sog"] = d["wl_adj"] * sum(d[f"wl_toi_{s}"] * d[f"wl_rate_{s}"] for s in STATES_W) / 60.0
    return d


def baseline_sog(sk: pd.DataFrame, half_life: float = 10.0, k_games: float = 5.0) -> pd.Series:
    """Simple baseline: exponentially weighted SOG per game (half-life 10 games), 5 pseudo-games of the position mean
    of the player's own earlier rows' league (the full-table position mean: ~1.9 F / 1.2 D; a constant)."""
    grp = sk["player_id"].to_numpy()
    S = ew_prior_sums(grp, np.column_stack([sk["sog"].to_numpy(float), np.ones(len(sk))]), half_life)
    pm = sk.groupby("pos")["sog"].transform("mean").to_numpy()
    return pd.Series((S[:, 0] + k_games * pm) / (S[:, 1] + k_games), index=sk.index)


# ---------------------------------------------------------------------------------------------------------------------
# goalie predictions
# ---------------------------------------------------------------------------------------------------------------------
def team_sa_expectation(tg: pd.DataFrame, c: TrainedConstants, prm: WorkloadParams) -> pd.DataFrame:
    """Point-in-time expected regulation shots against each (game, team) + expected OT shots."""
    t = tg.sort_values(["team_id", "date_int", "game_id"]).reset_index(drop=True)
    lt = tg.sort_values("date_int")
    t["lg"] = league_prior_mean(lt["date_int"].to_numpy(), lt["sa_reg"].to_numpy(float), t["date_int"].to_numpy(), prm.league_window_sa)
    sa, sf = t["sa_reg"].to_numpy(float), t["sf_reg"].to_numpy(float)
    if prm.schedule_adjust:
        # one multiplicative pass: each past game divided by that opponent's (unadjusted, point-in-time) factor
        S0 = ew_prior_sums(t["team_id"].to_numpy(), np.column_stack([sa, sf, np.ones(len(t))]), prm.hl_sa)
        sa0 = (S0[:, 0] + prm.k_sa * t["lg"]) / (S0[:, 2] + prm.k_sa)
        sf0 = (S0[:, 1] + prm.k_sa * t["lg"]) / (S0[:, 2] + prm.k_sa)
        f0 = pd.DataFrame({"game_id": t["game_id"], "opp_id": t["team_id"], "o_sf0": sf0 / t["lg"], "o_sa0": sa0 / t["lg"]})
        t = t.merge(f0, on=["game_id", "opp_id"], how="left")
        sa = sa / t["o_sf0"].fillna(1.0).clip(0.6, 1.6).to_numpy()
        sf = sf / t["o_sa0"].fillna(1.0).clip(0.6, 1.6).to_numpy()
    S = ew_prior_sums(t["team_id"].to_numpy(), np.column_stack([sa, sf, np.ones(len(t))]), prm.hl_sa)
    t["sa_rate"] = (S[:, 0] + prm.k_sa * t["lg"]) / (S[:, 2] + prm.k_sa)
    t["sf_rate"] = (S[:, 1] + prm.k_sa * t["lg"]) / (S[:, 2] + prm.k_sa)
    o = t[["game_id", "team_id", "sf_rate"]].rename(columns={"team_id": "opp_id", "sf_rate": "opp_sf_rate"})
    t = t.merge(o, on=["game_id", "opp_id"], how="left")
    venue = np.where(t["is_home"].to_numpy(bool), 1.0 / np.sqrt(c.venue_sa), np.sqrt(c.venue_sa))
    t["E_sa_reg"] = t["lg"] * (t["opp_sf_rate"] / t["lg"]) * (t["sa_rate"] / t["lg"]) * venue
    t["E_sa_net"] = t["E_sa_reg"] + c.p_ot * c.ot_sa
    return t[["game_id", "team_id", "E_sa_reg", "E_sa_net", "sa_rate", "lg"]]


def goalie_sv(goalies: pd.DataFrame, prm: WorkloadParams) -> pd.DataFrame:
    """Point-in-time shrunk save fraction of every goalie appearance (league level x relative, ``k_sv`` shots)."""
    g = goalies[goalies["toi_s"].fillna(0) > 0].copy()
    g["date_int"] = _date_int(g["game_date"])
    g = g.sort_values(["player_id", "date_int", "game_id"]).reset_index(drop=True)
    S = ew_prior_sums(g["player_id"].to_numpy(), np.column_stack([g["saves"].to_numpy(float), g["shots_against"].to_numpy(float)]), 200.0)
    lt = g.sort_values("date_int")
    sa_m = league_prior_mean(lt["date_int"].to_numpy(), lt["shots_against"].to_numpy(float), g["date_int"].to_numpy(), 5 * prm.league_window_sa)
    sv_m = league_prior_mean(lt["date_int"].to_numpy(), lt["saves"].to_numpy(float), g["date_int"].to_numpy(), 5 * prm.league_window_sa)
    g["lg_sv"] = _div(sv_m, sa_m, 0.905)
    g["sv_hat"] = (S[:, 0] + prm.k_sv * g["lg_sv"]) / (S[:, 1] + prm.k_sv)
    return g[["game_id", "player_id", "lg_sv", "sv_hat"]]


def goalie_saves_pmf(e_sa_full: np.ndarray, alpha_sa: float, sv: np.ndarray, c: TrainedConstants, K: int = SAVES_K) -> np.ndarray:
    """saves pmf: SA ~ NB(mean, alpha); with prob p_pull the starter faces f_pull of the mean; Binomial(SA, sv)."""
    full = E.binomial_mixture_pmf(E.nb_pmf(e_sa_full, alpha_sa, SA_K), sv, K)
    part = E.binomial_mixture_pmf(E.nb_pmf(e_sa_full * c.f_pull, alpha_sa, SA_K), sv, K)
    return (1.0 - c.p_pull) * full + c.p_pull * part
