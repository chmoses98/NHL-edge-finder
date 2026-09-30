"""Player-game feature table and point-in-time player / team deployment state for PLAYER_SIM_V1.

``build_player_games`` turns the official per-game tables (``nhl_edge.data.player_events``) into ONE long table, one row
per skater-game, with every quantity the simulator's layers need, split by strength state:

    toi_<s>   seconds on ice          (EV, PP, SH, EA = own net empty, EN = opponent net empty, OT)
    ixg_<s>   individual expected goals from the shot-quality model (unblocked, non-empty-net attempts)
    g_<s>     goals, a1_<s> primary assists, a2_<s> secondary assists
    gfo_<s>   goals scored by TEAMMATES while this player was on the ice (the assist opportunity set)
    tsec_<s>  the team's seconds in that state in that game (share denominators)

``PlayerBook`` answers "what did we know about this player before date D?" from rows STRICTLY before D, exponentially
weighted by games-ago, with every rate shrunk toward a position prior (empirical Bayes: prior pseudo-exposure ``k``).
Deployment shares (share of the team's EV / PP / SH / ... time) use a SHORT half-life because roles change; talent
rates (ixG/60, finishing, assist involvement) use a LONG one because they are noisy. Every hyper-parameter lives in
``PlayerParams`` and is stored with the model version; they were chosen on a validation season (see
docs/research/PLAYER_SIM_V1.md), never on the evaluation seasons.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

import numpy as np
import pandas as pd

STATES = ("ev", "pp", "sh", "ea", "en")
GOAL_STATES = ("ev", "pp", "sh", "ea", "en", "ot")


@dataclass(frozen=True)
class PlayerParams:
    share_half_life: float = 6.0  # games; deployment share (role) memory
    rate_half_life: float = 60.0  # games; talent-rate memory
    max_games: int = 164
    prior_season_weight: float = 0.75  # extra multiplicative discount on rows from earlier seasons (rates)
    share_prior_games: float = 0.5  # pseudo-games of the position-mean share (selected on 2023-24: 0.5 beat 1.5)
    k_ixg_min: dict[str, float] = field(default_factory=lambda: {"ev": 300.0, "pp": 60.0, "sh": 60.0, "ea": 10.0})  # minutes of prior
    k_finish_xg: float = 40.0  # expected goals of prior on the finishing ratio (heavy shrinkage)
    use_finishing: bool = True
    k_a1: float = 25.0  # teammate on-ice goals of prior on P(A1 | on ice)
    k_a2: float = 45.0  # secondary assists are noisier: stronger shrinkage
    k_en: float = 6.0  # minutes of prior on empty-net scoring
    k_onice_goals: float = 12.0  # expected on-ice goals of prior on the on-ice goals-for ratio
    onice_beta: float = 1.0  # exponent of the on-ice GF ratio in the scorer weight (selected on 2023-24 over 0 and 0.5)
    fringe_prior: bool = True  # (selected on 2023-24) shrink toward the rates of players new to the league (replacement level), not the average regular
    fringe_games: float = 60.0  # the fringe prior's weight fades as a player accumulates games: w = fringe_games / (fringe_games + n)
    k_goal_copresence: float = -1.0  # goals of prior blending goal co-presence into time co-ice (< 0 = off; chosen on validation)
    toi_sigma: float = 0.14  # game-to-game log-sd of a player's ice time around its expectation
    p_early_exit: float = 0.008  # per player-game probability of leaving early (injury / ejection)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> PlayerParams:
        base = asdict(cls())
        base.update({k: v for k, v in (d or {}).items() if k in base})
        return cls(**base)


def pos_group(p: Any) -> str:
    return "D" if str(p or "").upper().startswith("D") else "F"


def build_player_games(players: pd.DataFrame, goals: pd.DataFrame, shots: pd.DataFrame, team_states: pd.DataFrame, xg: pd.Series | None = None) -> pd.DataFrame:
    """One row per skater-game (only games with usable shifts; the rest cannot split ice time by state)."""
    pl = players[players["shifts_ok"].fillna(False).astype(bool)].copy()
    pl["pos"] = pl["position"].map(pos_group)
    for s in STATES:
        pl[f"toi_{s}"] = pd.to_numeric(pl[f"toi_{s}_s"], errors="coerce").fillna(0.0)
    pl["toi_ot"] = pd.to_numeric(pl["toi_ot_s"], errors="coerce").fillna(0.0)
    key = ["game_id", "player_id"]
    # goals / assists by strength (OT goals are their own bucket: 3-on-3 deployment differs)
    g = goals.copy()
    g["st"] = np.where(g["period"] >= 4, "ot", g["strength"].astype(str).str.lower())
    agg = []
    for role, col in (("g", "scorer_id"), ("a1", "a1_id"), ("a2", "a2_id")):
        x = g[g[col].notna()].groupby(["game_id", col, "st"]).size().unstack("st", fill_value=0)
        x.columns = [f"{role}_{c}" for c in x.columns]
        x.index = x.index.set_names(key)
        agg.append(x)
    # teammates' goals while on ice (assist opportunity set), by state
    rows = []
    for r in g[g["for_on_ice"].notna()].itertuples(index=False):
        for p in r.for_on_ice:
            if int(p) != int(r.scorer_id or -1):
                rows.append((r.game_id, int(p), r.st))
    if rows:
        x = pd.DataFrame(rows, columns=["game_id", "player_id", "st"]).groupby(["game_id", "player_id", "st"]).size().unstack("st", fill_value=0)
        x.columns = [f"gfo_{c}" for c in x.columns]
        agg.append(x)
    # individual xG by state
    if xg is not None and len(shots):
        sh = shots.assign(xg=xg.values if isinstance(xg, pd.Series) else xg)
        sh = sh[sh["shooter_id"].notna()]
        sh["st"] = np.where(sh["period"] >= 4, "ot", sh["strength"].astype(str).str.lower())
        x = sh.groupby(["game_id", "shooter_id", "st"])["xg"].sum().unstack("st", fill_value=0.0)
        x.columns = [f"ixg_{c}" for c in x.columns]
        x.index = x.index.set_names(key)
        agg.append(x)
        x = sh[sh["kind"].isin(["GOAL", "SOG"])].groupby(["game_id", "shooter_id", "st"]).size().unstack("st", fill_value=0)
        x.columns = [f"isog_{c}" for c in x.columns]
        x.index = x.index.set_names(key)
        agg.append(x)
    out = pl.set_index(key)
    for a in agg:
        a = a[~a.index.duplicated()]
        out = out.join(a, how="left")
    out = out.reset_index()
    for pre in ("g", "a1", "a2", "gfo", "ixg", "isog"):
        for s in GOAL_STATES:
            c = f"{pre}_{s}"
            out[c] = pd.to_numeric(out[c], errors="coerce").fillna(0.0) if c in out.columns else 0.0
    tgf = g.groupby(["game_id", "team_id", "st"]).size().unstack("st", fill_value=0)
    tgf.columns = [f"tgf_{c}" for c in tgf.columns]
    out = out.merge(tgf.reset_index(), on=["game_id", "team_id"], how="left")
    for st_ in GOAL_STATES:
        c = f"tgf_{st_}"
        out[c] = pd.to_numeric(out[c], errors="coerce").fillna(0.0) if c in out.columns else 0.0
    ts = team_states.copy()
    ts = ts.rename(columns={f"sec_{s}": f"tsec_{s}" for s in STATES})
    ts["tsec_ot"] = 0.0
    out = out.merge(ts[["game_id", "team_id"] + [f"tsec_{s}" for s in STATES] + ["n_seconds"]], on=["game_id", "team_id"], how="left")
    out["tsec_ot"] = (pd.to_numeric(out["n_seconds"], errors="coerce").fillna(3600) - 3600).clip(lower=0)
    out["date_int"] = out["game_date"].astype(str).str.replace("-", "").str[:8].astype(int)
    keep = ["game_id", "game_date", "date_int", "season", "game_type", "team_id", "player_id", "name", "sweater", "position", "pos", "toi_s",
            "goals", "assists", "points", "sog", "a1", "a2"] + [f"toi_{s}" for s in STATES] + ["toi_ot"] + \
        [f"{p}_{s}" for p in ("g", "a1", "a2", "gfo", "ixg", "isog") for s in GOAL_STATES] + [f"tsec_{s}" for s in STATES] + ["tsec_ot"] + [f"tgf_{s}" for s in GOAL_STATES]
    return out[[c for c in keep if c in out.columns]].sort_values(["player_id", "date_int", "game_id"]).reset_index(drop=True)


@dataclass
class LeaguePriors:
    """Position-level rates from the training rows (per 60 minutes of the state, or per opportunity)."""

    ixg60: dict[tuple[str, str], float]
    a1: dict[tuple[str, str], float]
    a2: dict[tuple[str, str], float]
    en60: dict[str, float]
    share_median: dict[tuple[str, str], float]
    finish: float
    unassisted: dict[str, float]
    no_a2: dict[str, float]
    fringe: dict[str, dict[tuple[str, str], float]] = field(default_factory=dict)  # ixg60 / a1 / a2 / share of players new to the league

    def to_dict(self) -> dict[str, Any]:
        f = lambda d: {f"{k[0]}|{k[1]}" if isinstance(k, tuple) else k: v for k, v in d.items()}  # noqa: E731
        return {"ixg60": f(self.ixg60), "a1": f(self.a1), "a2": f(self.a2), "en60": self.en60, "share_median": f(self.share_median),
                "finish": self.finish, "unassisted": self.unassisted, "no_a2": self.no_a2, "fringe": {k: f(v) for k, v in self.fringe.items()}}

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> LeaguePriors:
        g = lambda x: {tuple(k.split("|")): float(v) for k, v in x.items()}  # noqa: E731
        return cls(g(d["ixg60"]), g(d["a1"]), g(d["a2"]), {k: float(v) for k, v in d["en60"].items()}, g(d["share_median"]), float(d["finish"]),
                   {k: float(v) for k, v in d["unassisted"].items()}, {k: float(v) for k, v in d["no_a2"].items()},
                   {k: g(v) for k, v in (d.get("fringe") or {}).items()})


def league_priors(pg: pd.DataFrame, goals: pd.DataFrame) -> LeaguePriors:
    ixg60, a1, a2, share = {}, {}, {}, {}
    en60 = {}
    for pos, d in pg.groupby("pos"):
        for s in ("ev", "pp", "sh", "ea"):
            t = d[f"toi_{s}"].sum() / 60.0
            ixg60[(pos, s)] = float(d[f"ixg_{s}"].sum() / t * 60.0) if t > 0 else 0.0
        for s in GOAL_STATES:
            opp = d[f"gfo_{s}"].sum()
            a1[(pos, s)] = float(d[f"a1_{s}"].sum() / opp) if opp > 0 else 0.2
            a2[(pos, s)] = float(d[f"a2_{s}"].sum() / opp) if opp > 0 else 0.15
        t = d["toi_en"].sum() / 60.0
        en60[pos] = float(d["g_en"].sum() / t * 60.0) if t > 0 else 0.0
        for s in ("ev", "pp", "sh", "ea", "en"):
            x = (d[f"toi_{s}"] / d[f"tsec_{s}"].replace(0, np.nan)).dropna()
            share[(pos, s)] = float(x.mean()) if len(x) else 0.0
        x = (d["toi_ot"] / d["tsec_ot"].replace(0, np.nan)).dropna()
        share[(pos, "ot")] = float(x.mean()) if len(x) else 0.0
    gsum = sum(pg[f"g_{s}"].sum() for s in ("ev", "pp", "sh", "ea"))
    xsum = sum(pg[f"ixg_{s}"].sum() for s in ("ev", "pp", "sh", "ea"))
    gg = goals.copy()
    gg["st"] = np.where(gg["period"] >= 4, "ot", gg["strength"].astype(str).str.lower())
    un, no2 = {}, {}
    for s, d in gg.groupby("st"):
        un[s] = float(d["a1_id"].isna().mean())
        has1 = d[d["a1_id"].notna()]
        no2[s] = float(has1["a2_id"].isna().mean()) if len(has1) else 0.3
    # fringe / replacement-level prior: the first 20 NHL games of players who debuted after the data window opened
    first_season = pg.groupby("player_id")["season"].transform("min")
    order = pg.sort_values(["player_id", "date_int"]).groupby("player_id").cumcount()
    fr = pg[(first_season > pg["season"].min()) & (order.reindex(pg.index) < 20)]
    fringe: dict[str, dict[tuple[str, str], float]] = {"ixg60": {}, "a1": {}, "a2": {}, "share": {}}
    for pos, d in fr.groupby("pos"):
        for s in ("ev", "pp", "sh", "ea"):
            t = d[f"toi_{s}"].sum() / 60.0
            fringe["ixg60"][(pos, s)] = float(d[f"ixg_{s}"].sum() / t * 60.0) if t > 0 else ixg60.get((pos, s), 0.0)
        for s in GOAL_STATES:
            opp = d[f"gfo_{s}"].sum()
            fringe["a1"][(pos, s)] = float(d[f"a1_{s}"].sum() / opp) if opp > 20 else a1.get((pos, s), 0.2)
            fringe["a2"][(pos, s)] = float(d[f"a2_{s}"].sum() / opp) if opp > 20 else a2.get((pos, s), 0.15)
        for s in ("ev", "pp", "sh", "ea", "en"):
            x = (d[f"toi_{s}"] / d[f"tsec_{s}"].replace(0, np.nan)).dropna()
            fringe["share"][(pos, s)] = float(x.mean()) if len(x) else share.get((pos, s), 0.0)
        x = (d["toi_ot"] / d["tsec_ot"].replace(0, np.nan)).dropna()
        fringe["share"][(pos, "ot")] = float(x.mean()) if len(x) else share.get((pos, "ot"), 0.0)
    return LeaguePriors(ixg60, a1, a2, en60, share, float(gsum / xsum) if xsum > 0 else 1.0, un, no2, fringe)


@dataclass
class PlayerProfile:
    """What was known about one skater before the game date. Rates are shrunk; ``n_games`` / flags carry uncertainty."""

    player_id: int
    pos: str
    n_games: int
    n_games_season: int
    last_team_id: int | None
    last_date_int: int | None
    share: dict[str, float]  # share of the team's time in each state (ev, pp, sh, ea, en, ot)
    ixg60: dict[str, float]  # shrunk individual xG per 60 at ev/pp/sh/ea
    finish: float  # shrunk goals / xG multiplier
    a1: dict[str, float]  # P(primary assist | a teammate scores while on ice), by state
    a2: dict[str, float]
    en60: float
    toi_mean_s: float  # recent all-situation TOI per game (for the packet)
    sog60: dict[str, float]
    flags: list[str] = field(default_factory=list)
    onice_rel: dict[str, float] = field(default_factory=lambda: {"ev": 1.0, "pp": 1.0})

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _ew(n: int, half_life: float) -> np.ndarray:
    """Weights for the last ``n`` games, most recent LAST."""
    k = np.arange(n)[::-1]
    return 0.5 ** (k / half_life)


class _Rows:
    """Column arrays of one player's rows, sorted by date, sliced by position (cheap point-in-time views)."""

    def __init__(self, d: pd.DataFrame):
        self.date = d["date_int"].to_numpy()
        self.cols = {c: d[c].to_numpy() for c in d.columns if c not in ("name", "game_date", "position")}

    def upto(self, date_int: int, max_games: int) -> tuple[int, int]:
        hi = int(np.searchsorted(self.date, date_int, side="left"))
        return max(0, hi - max_games), hi


class PlayerBook:
    """Point-in-time player profiles from the long player-game table (rows strictly before ``as_of``)."""

    def __init__(self, pg: pd.DataFrame, priors: LeaguePriors, params: PlayerParams | None = None):
        self.params = params or PlayerParams()
        self.priors = priors
        self.pg = pg
        self._by: dict[int, _Rows] = {int(k): _Rows(v.sort_values(["date_int", "game_id"])) for k, v in pg.groupby("player_id", sort=False)}
        self._cache: dict[tuple[int, int], PlayerProfile] = {}

    def rows_before(self, pid: int, date_int: int) -> pd.DataFrame:
        r = self._by.get(int(pid))
        if r is None:
            return self.pg.iloc[0:0]
        lo, hi = r.upto(date_int, self.params.max_games)
        return pd.DataFrame({k: v[lo:hi] for k, v in r.cols.items()})

    def profile(self, pid: int, date_int: int, pos_hint: str | None = None, season: int | None = None) -> PlayerProfile:
        key = (int(pid), int(date_int))
        if key in self._cache:
            return self._cache[key]
        prm, pri = self.params, self.priors
        r = self._by.get(int(pid))
        lo, hi = r.upto(date_int, prm.max_games) if r is not None else (0, 0)
        n = hi - lo
        col = (lambda c: np.asarray(r.cols[c][lo:hi], dtype=float)) if n else (lambda c: np.zeros(0))
        pos = str(r.cols["pos"][hi - 1]) if n else pos_group(pos_hint)
        flags: list[str] = []
        if n == 0:
            flags.append("NO_HISTORY")
        elif n < 20:
            flags.append("SMALL_SAMPLE")
        seasons = r.cols["season"][lo:hi] if n else np.zeros(0)
        cur_season = season if season is not None else (int(seasons[-1]) if n else None)
        n_season = int((seasons == cur_season).sum()) if n and cur_season is not None else 0
        # prior targets: the average player, blended toward replacement level when the player has little NHL history
        wf = prm.fringe_games / (prm.fringe_games + n) if (prm.fringe_prior and pri.fringe) else 0.0

        def target(kind: str, key: tuple[str, str], base: float) -> float:
            fv = pri.fringe.get(kind, {}).get(key) if wf else None
            return base if fv is None else (1 - wf) * base + wf * fv

        # deployment shares: short memory, shrunk to the position mean with ``share_prior_games`` pseudo-games
        share = {}
        ws = _ew(n, prm.share_half_life)
        for s in ("ev", "pp", "sh", "ea", "en", "ot"):
            med = target("share", (pos, s), pri.share_median.get((pos, s), 0.0))
            if n:
                den, num = col(f"tsec_{s}"), col(f"toi_{s}")
                ok = den > 0
                w = ws[ok]
                sh = ((w * (num[ok] / den[ok])).sum() + med * prm.share_prior_games) / (w.sum() + prm.share_prior_games)
            else:
                sh = med
            share[s] = float(sh)
        # talent rates: long memory, earlier seasons discounted, shrunk with pseudo-exposure
        wr = _ew(n, prm.rate_half_life)
        if n and cur_season is not None:
            wr = wr * np.where(seasons == cur_season, 1.0, prm.prior_season_weight)
        ixg60, sog60 = {}, {}
        for s in ("ev", "pp", "sh", "ea"):
            k = prm.k_ixg_min.get(s, 60.0)
            mins = float((wr * col(f"toi_{s}")).sum() / 60.0) if n else 0.0
            xg = float((wr * col(f"ixg_{s}")).sum()) if n else 0.0
            ixg60[s] = (xg + k * target("ixg60", (pos, s), pri.ixg60.get((pos, s), 0.0)) / 60.0) / (mins + k) * 60.0
            so = float((wr * col(f"isog_{s}")).sum()) if n else 0.0
            sog60[s] = so / mins * 60.0 if mins > 1 else float("nan")
        gs = float(sum((wr * col(f"g_{s}")).sum() for s in ("ev", "pp", "sh", "ea"))) if n else 0.0
        xs = float(sum((wr * col(f"ixg_{s}")).sum() for s in ("ev", "pp", "sh", "ea"))) if n else 0.0
        finish = (gs + prm.k_finish_xg * pri.finish) / (xs + prm.k_finish_xg) / max(pri.finish, 1e-6) if prm.use_finishing else 1.0
        a1, a2 = {}, {}
        for s in GOAL_STATES:
            opp = float((wr * col(f"gfo_{s}")).sum()) if n else 0.0
            x1 = float((wr * col(f"a1_{s}")).sum()) if n else 0.0
            x2 = float((wr * col(f"a2_{s}")).sum()) if n else 0.0
            p1 = target("a1", (pos, s), pri.a1.get((pos, s), 0.2))
            p2 = target("a2", (pos, s), pri.a2.get((pos, s), 0.15))
            a1[s] = (x1 + prm.k_a1 * p1) / (opp + prm.k_a1)
            a2[s] = (x2 + prm.k_a2 * p2) / (opp + prm.k_a2)
        # OT / EA / EN opportunity sets are tiny: borrow half from the player's EV involvement, scaled to the state
        for s in ("ea", "en", "ot"):
            a1[s] = 0.5 * a1[s] + 0.5 * a1["ev"] * pri.a1.get((pos, s), 0.2) / max(pri.a1.get((pos, "ev"), 0.2), 1e-6)
            a2[s] = 0.5 * a2[s] + 0.5 * a2["ev"] * pri.a2.get((pos, s), 0.15) / max(pri.a2.get((pos, "ev"), 0.15), 1e-6)
        en_min = float((wr * col("toi_en")).sum() / 60.0) if n else 0.0
        en_g = float((wr * col("g_en")).sum()) if n else 0.0
        en60 = (en_g + prm.k_en * pri.en60.get(pos, 0.0) / 60.0) / (en_min + prm.k_en) * 60.0
        # on-ice goals for, relative to what the team scored per minute in the same games (line / unit scoring effect)
        onice_rel = {}
        for s in ("ev", "pp"):
            if n:
                den = col(f"tsec_{s}")
                exp = np.where(den > 0, col(f"toi_{s}") * col(f"tgf_{s}") / np.maximum(den, 1.0), 0.0)
                onice = col(f"gfo_{s}") + col(f"g_{s}")
                onice_rel[s] = float(((wr * onice).sum() + prm.k_onice_goals) / ((wr * exp).sum() + prm.k_onice_goals))
            else:
                onice_rel[s] = 1.0
        toi = np.nan_to_num(col("toi_s")) if n else np.zeros(0)
        toi_mean = float((ws * toi).sum() / ws.sum()) if n else float("nan")
        last_team = int(r.cols["team_id"][hi - 1]) if n else None
        prof = PlayerProfile(int(pid), pos, n, n_season, last_team, int(r.cols["date_int"][hi - 1]) if n else None, share, ixg60, float(finish), a1, a2,
                             float(en60), toi_mean, sog60, flags, onice_rel)
        self._cache[key] = prof
        return prof


def coice_fractions(coice: pd.DataFrame, team_id: int, date_int: int, players: list[int], toi_by_game: pd.DataFrame | None = None,
                    half_life: float = 2.0, max_games: int = 8) -> dict[str, np.ndarray] | None:
    """F_s[i, j] = expected share of player i's state-s ice time spent WITH teammate j, from the team's last ``max_games``
    games strictly before ``date_int`` (most recent heaviest: lines change). Needs ``coice`` rows carrying ``date_int``
    and ``toi_by_game`` (game_id, player_id, toi_ev, toi_pp, toi_sh). Rows of players with no ice time in those games
    are NaN (the caller falls back to a share-proportional prior). None when the team has no prior games."""
    c = coice[(coice["team_id"] == team_id) & (coice["date_int"] < date_int)]
    if not len(c):
        return None
    gd = c.groupby("game_id")["date_int"].first().sort_values()
    games = list(gd.index[-max_games:])
    wmap = pd.Series(_ew(len(games), half_life), index=games)
    idx = pd.Series(np.arange(len(players)), index=pd.Index([int(p) for p in players]))
    n = len(players)
    cc = c[c["game_id"].isin(games)]
    i = idx.reindex(cc["p1"].astype(int).to_numpy()).to_numpy()
    j = idx.reindex(cc["p2"].astype(int).to_numpy()).to_numpy()
    ok = ~(np.isnan(i) | np.isnan(j))
    i, j = i[ok].astype(int), j[ok].astype(int)
    w = wmap.reindex(cc["game_id"].to_numpy()).to_numpy()[ok]
    out = {}
    tg = toi_by_game[toi_by_game["game_id"].isin(games)] if toi_by_game is not None else None
    if tg is not None:
        ti = idx.reindex(tg["player_id"].astype(int).to_numpy()).to_numpy()
        tok = ~np.isnan(ti)
        tw = wmap.reindex(tg["game_id"].to_numpy()).to_numpy()[tok]
        ti = ti[tok].astype(int)
    for s, col in (("ev", "shared_ev_s"), ("pp", "shared_pp_s"), ("sh", "shared_sh_s")):
        num = np.zeros((n, n))
        v = cc[col].to_numpy(float)[ok] * w
        np.add.at(num, (i, j), v)
        np.add.at(num, (j, i), v)
        den = np.zeros(n)
        if tg is not None:
            np.add.at(den, ti, tw * tg[f"toi_{s}"].to_numpy(float)[tok])
        with np.errstate(invalid="ignore", divide="ignore"):
            f = np.where(den[:, None] > 0, num / den[:, None], np.nan)
        out[s] = np.clip(f, 0.0, 1.0)
    return out


def goal_copresence(goals: pd.DataFrame, team_id: int, date_int: int, players: list[int], half_life: float = 15.0,
                    max_games: int = 60) -> dict[str, tuple[np.ndarray, np.ndarray]]:
    """For the team's goals in its last ``max_games`` games strictly before ``date_int``: G[i, j] = share of the goals
    scored with player i on the ice that ALSO had teammate j on the ice (EV / PP), and n[i] = the weighted number of
    such goals. Goals happen disproportionately when strong players are on the ice, so this is the assist-opportunity
    structure that time-on-ice co-presence understates. Requires ``goals`` rows with ``date_int`` and ``for_on_ice``."""
    g = goals[(goals["team_id"] == team_id) & (goals["date_int"] < date_int) & goals["for_on_ice"].notna()]
    n = len(players)
    out = {}
    if not len(g):
        return out
    gd = g.groupby("game_id")["date_int"].first().sort_values()
    games = list(gd.index[-max_games:])
    wmap = dict(zip(games, _ew(len(games), half_life)))
    idx = {int(p): i for i, p in enumerate(players)}
    for s in ("ev", "pp"):
        gs = g[(g["game_id"].isin(games)) & (g["strength"].astype(str).str.lower() == s) & (g["period"] <= 3)]
        num = np.zeros((n, n))
        den = np.zeros(n)
        for r in gs.itertuples(index=False):
            on = [idx[int(p)] for p in r.for_on_ice if int(p) in idx]
            w = wmap[r.game_id]
            for i in on:
                den[i] += w
                for j in on:
                    if j != i:
                        num[i, j] += w
        with np.errstate(invalid="ignore", divide="ignore"):
            out[s] = (np.where(den[:, None] > 0, num / den[:, None], np.nan), den)
    return out
