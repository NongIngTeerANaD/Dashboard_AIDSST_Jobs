"""Hero card: flowing gradient + glass KPI tiles computed from the real (open) datasets."""
import pandas as pd
from dash import html
from app.data_loader import data_store

_SECTOR_COUNTRIES = {"US", "GB", "DE", "FR", "AU"}
_ISO3 = {"TH": "THA", "SG": "SGP", "US": "USA", "GB": "GBR", "DE": "DEU", "FR": "FRA", "AU": "AUS", "IN": "IND"}


def _delta_chip(delta, unit: str, digits: int = 1):
    """Spec: rising numbers red, falling numbers blue."""
    if delta is None or pd.isna(delta):
        return None
    up = delta >= 0
    return html.Span(f"{'▲' if up else '▼'} {abs(delta):.{digits}f}{unit}", className=f"delta {'up' if up else 'down'}")


def _kpi(label, value, src, delta=None, unit="", digits=1):
    return html.Div([
        html.Div(label, className="lbl"),
        html.Div([value, _delta_chip(delta, unit, digits)] if delta is not None else [value], className="val"),
        html.Div(src, className="src"),
    ], className="kpi")


def _sector_kpi(countries):
    df = data_store.sector_postings
    cs = [c for c in countries if c in _SECTOR_COUNTRIES]
    if df.empty or not cs:
        return _kpi("ดัชนีประกาศงาน Data & Analytics", "—", "เลือก US/GB/DE/AU เพื่อดูข้อมูล Indeed")
    d = df[(df["display_name"] == "Data & Analytics") & df["country_code"].isin(cs)].copy()
    d["date"] = pd.to_datetime(d["date"], errors="coerce")
    if d.empty:
        return _kpi("ดัชนีประกาศงาน Data & Analytics", "—", "ไม่มีข้อมูลประเทศที่เลือก")
    last = d["date"].max()
    now = d[d["date"] == last]["indeed_job_postings_index"].mean()
    prev = d[d["date"] == d[d["date"] <= last - pd.Timedelta(days=364)]["date"].max()]["indeed_job_postings_index"].mean()
    return _kpi("ดัชนีประกาศงาน Data & Analytics", f"{now:.0f}", f"Indeed (ฐาน ก.พ. 2020 = 100) · {last:%d %b %Y} · {', '.join(sorted(set(d['country_code'])))}",
                None if pd.isna(prev) else now - prev, " pt vs ปีก่อน", 0)


def _ai_kpi(countries):
    df = data_store.ai_tracker
    cs = [c for c in countries if c in set(df.get("jobcountry", []))]
    if df.empty or not cs:
        return _kpi("ประกาศงานที่กล่าวถึง AI", "—", "Indeed AI Tracker: เลือก US/GB/DE/FR/AU ฯลฯ")
    d = df[df["jobcountry"].isin(cs)].copy()
    d["date"] = pd.to_datetime(d["date"], errors="coerce")
    last = d["date"].max()
    now = d[d["date"] == last]["AI_share_postings"].mean()
    prev_d = d[d["date"] <= last - pd.Timedelta(days=364)]["date"].max()
    prev = d[d["date"] == prev_d]["AI_share_postings"].mean()
    return _kpi("ประกาศงานที่กล่าวถึง AI", f"{now:.1f}%", f"Indeed AI Tracker · {last:%b %Y} · {', '.join(sorted(set(d['country_code'] if 'country_code' in d else cs)))}",
                None if pd.isna(prev) else now - prev, " pp vs ปีก่อน", 1)


def _uem_kpi(countries):
    df = data_store.uem_advanced
    codes = [_ISO3[c] for c in countries if c in _ISO3]
    d = df[df["country_code"].isin(codes)].copy() if not df.empty else df
    if d is None or d.empty:
        return _kpi("ว่างงานผู้จบการศึกษาสูง", "—", "World Bank / ILO")
    d["year"] = pd.to_numeric(d["year"], errors="coerce")
    d = d.dropna(subset=["unemployment_rate_pct"])
    ly = int(d["year"].max())
    now = d[d["year"] == ly]["unemployment_rate_pct"].mean()
    prev = d[d["year"] == ly - 1]["unemployment_rate_pct"].mean()
    names = ", ".join(sorted(set(d[d["year"] == ly]["country"])))
    return _kpi("ว่างงานผู้จบการศึกษาสูง", f"{now:.1f}%", f"World Bank/ILO · {ly} · {names}",
                None if pd.isna(prev) else now - prev, " pp vs ปีก่อน", 1)


def _ict_kpi():
    df = data_store.ict_specialists
    d = df[df["country_code"] == "EU27_2020"].copy() if not df.empty else df
    if d is None or d.empty:
        return _kpi("ผู้เชี่ยวชาญ ICT ใน EU27", "—", "Eurostat")
    d["year"] = pd.to_numeric(d["year"], errors="coerce")
    ly = int(d["year"].max())
    now = float(d[d["year"] == ly]["ict_specialists_pct"].iloc[0])
    prev = d[d["year"] == ly - 1]["ict_specialists_pct"]
    return _kpi("ผู้เชี่ยวชาญ ICT ใน EU27", f"{now:.1f}%", f"Eurostat · {ly} · % ของการจ้างงาน",
                None if prev.empty else now - float(prev.iloc[0]), " pp vs ปีก่อน", 1)


def data_coverage():
    """(loaded, planned) open data sources actually present in the app."""
    checks = [data_store.job_postings, data_store.sector_postings, data_store.ai_tracker, data_store.uem_advanced,
              data_store.ict_specialists, data_store.eu_graduates, data_store.sg_mom, data_store.sg_ges]
    s03_real = (not data_store.skills_demand.empty) and (data_store.skills_demand["source_id"] == "S03").all()
    loaded = sum(1 for d in checks if not d.empty) + (1 if s03_real else 0)
    return loaded, 15


def build_hero(filters: dict):
    countries = (filters or {}).get("country", [])
    loaded, planned = data_coverage()
    pct = round(100 * loaded / planned)
    return html.Div([
        html.Div(className="blob b1"), html.Div(className="blob b2"), html.Div(className="blob b3"), html.Div(className="blob b4"),
        html.Div([
            html.H3("ภาพรวมตลาดงาน AI · Data Science · Statistics"),
            html.Div("ตัวเลขล่าสุดจากข้อมูลเปิด ปรับตามประเทศที่เลือกในตัวกรอง", className="sub"),
            html.Div([_sector_kpi(countries), _ai_kpi(countries), _uem_kpi(countries), _ict_kpi()], className="kpis"),
            html.Div([
                html.Div([html.Span("ความครอบคลุมของแหล่งข้อมูลเปิดในแอป"), html.Span(f"{loaded}/{planned} แหล่ง · {pct}%")], className="row1"),
                html.Div(html.Div(className="progress-fill", style={"width": f"{pct}%"}), className="progress-track"),
            ], className="cover"),
        ], className="glass"),
    ], className="hero")
