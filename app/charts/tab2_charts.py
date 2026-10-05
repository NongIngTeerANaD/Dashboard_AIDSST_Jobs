"""Charts for Tab 2: ตลาดงาน & Skill ที่ต้องการ (T2-1 to T2-4)."""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app.data_loader import data_store
from app.charts.common import chart_card, empty_chart_card

ROLE_TO_SECTORS = {
    "data_science": ["Data & Analytics"],
    "data_analyst": ["Data & Analytics"],
    "statistics": ["Data & Analytics", "Scientific Research & Development"],
    "ai_ml": ["Software Development", "Data & Analytics"],
}


def _weekly(df: pd.DataFrame, group_cols: list, date_col: str = "date") -> pd.DataFrame:
    """Keep one point per 7 days *within each series* (the old global stride mixed series and zig-zagged)."""
    df = df.sort_values(group_cols + [date_col])
    return df[df.groupby(group_cols).cumcount() % 7 == 0]


def build_t2_1_postings(countries: list, year_range: list, roles: list = None):
    """T2-1: Indeed postings index by occupational sector (S01), sector chosen by the role filter."""
    title = "T2-1: ดัชนีความต้องการแรงงานรายสายอาชีพ (Indeed Job Postings Index)"
    df = data_store.sector_postings
    if df.empty:
        return empty_chart_card(title, msg="ยังไม่มีข้อมูลรายสายอาชีพ — รัน python -m etl.fetch_s01_sector")
    roles = roles or list(ROLE_TO_SECTORS)
    sectors = sorted({s for r in roles for s in ROLE_TO_SECTORS.get(r, [])})
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    sub = df[df["country_code"].isin(countries) & df["display_name"].isin(sectors)
             & (df["date"].dt.year >= year_range[0]) & (df["date"].dt.year <= year_range[1])]
    if sub.empty:
        return empty_chart_card(
            title,
            msg="ไม่มีข้อมูลประกาศงานของไทย/อาเซียน (Indeed มีเฉพาะ US, GB, DE, FR, AU) — เลือกประเทศดังกล่าวในตัวกรอง")
    sub = _weekly(sub, ["country_code", "display_name"])
    fig = px.line(
        sub, x="date", y="indeed_job_postings_index", color="display_name", line_dash="country_code",
        title="ดัชนีประกาศงานรายสายอาชีพ (ฐาน ก.พ. 2020 = 100)",
        labels={"date": "วันที่", "indeed_job_postings_index": "ดัชนีประกาศงาน", "country_code": "ประเทศ",
                "display_name": "สายอาชีพ (Indeed)"},
        category_orders={"display_name": sectors},
        color_discrete_sequence=px.colors.qualitative.Bold)
    fig.add_hline(y=100, line_dash="dot", line_color="gray", annotation_text="ฐาน = 100")
    fig.update_layout(hovermode="x unified", margin=dict(t=50, b=40, l=40, r=40),
                      legend=dict(orientation="h", y=-0.3, title=None))
    return chart_card(title, fig, source_id="S01 (Indeed Hiring Lab, sector files)", license_name="CC BY 4.0",
                      data_year=f"{year_range[0]}-{year_range[1]}", status="verified")


def build_t2_6_ict_specialists(countries: list, year_range: list):
    """T2-6: ICT specialists as % of total employment, Eurostat (S08). EU countries only."""
    title = "T2-6: สัดส่วนผู้เชี่ยวชาญด้าน ICT ในการจ้างงานทั้งหมด (Eurostat)"
    df = data_store.ict_specialists
    if df.empty:
        return empty_chart_card(title, msg="ยังไม่มีข้อมูล S08 — รัน python -m etl.fetch_s08_eurostat_ict")
    df = df.copy()
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    wanted = ["EU27_2020"] + [c for c in countries if c in ("DE", "FR")] + (["UK"] if "GB" in countries else [])
    sub = df[df["country_code"].isin(wanted) & df["year"].between(year_range[0], year_range[1])].dropna(subset=["ict_specialists_pct"])
    if sub.empty:
        return empty_chart_card(title)
    sub = sub.assign(area=sub["country_code"].replace({"EU27_2020": "EU27 (ค่ารวม)", "UK": "UK (ถึงปีที่ Eurostat มีข้อมูล)"}))
    fig = px.line(sub.sort_values(["area", "year"]), x="year", y="ict_specialists_pct", color="area", markers=True,
                  title="ผู้เชี่ยวชาญด้าน ICT (% ของการจ้างงานทั้งหมด)",
                  labels={"year": "ปี", "ict_specialists_pct": "% ของการจ้างงาน", "area": "ประเทศ/ภูมิภาค"},
                  color_discrete_sequence=px.colors.qualitative.Vivid)
    fig.update_xaxes(dtick=1)
    fig.update_layout(hovermode="x unified", margin=dict(t=50, b=40, l=40, r=20), legend=dict(orientation="h", y=-0.25, title=None))
    return chart_card(title, fig, source_id="S08 (Eurostat isoc_sks_itspt)", license_name="Eurostat reuse policy",
                      data_year=f"{int(sub['year'].min())}-{int(sub['year'].max())}", status="verified")


def build_t2_5_ai_share(countries: list, year_range: list):
    """T2-5: share of postings mentioning AI/GenAI (S02, real data)."""
    title = "T2-5: สัดส่วนประกาศงานที่กล่าวถึง AI (Indeed AI Tracker)"
    df = data_store.ai_tracker
    if df.empty:
        return empty_chart_card(title)
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    sub = df[df["jobcountry"].isin(countries) & (df["date"].dt.year >= year_range[0]) & (df["date"].dt.year <= year_range[1])]
    if sub.empty:
        return empty_chart_card(title, msg="Indeed AI Tracker ไม่มีข้อมูลประเทศที่เลือก (มี AU CA DE FR GB IE IT NL US)")
    fig = px.line(sub.sort_values("date"), x="date", y="AI_share_postings", color="jobcountry",
                  title="ประกาศงานที่กล่าวถึง AI (% ของประกาศทั้งหมด)",
                  labels={"date": "เดือน", "AI_share_postings": "% ของประกาศงาน", "jobcountry": "ประเทศ"},
                  color_discrete_sequence=px.colors.qualitative.Vivid)
    fig.update_layout(hovermode="x unified", margin=dict(t=50, b=40, l=40, r=40))
    return chart_card(title, fig, source_id="S02 (Indeed Hiring Lab AI Tracker)", license_name="CC BY 4.0",
                      data_year=f"{year_range[0]}-{year_range[1]}", status="verified")

def build_t2_2_skills(roles: list):
    """T2-2: ทักษะที่ตลาดต้องการตามกลุ่มสายงาน (S03 / S02)."""
    df_demand = data_store.skills_demand
    df_skills = data_store.skills
    if df_demand.empty or df_skills.empty:
        return empty_chart_card("T2-2: ทักษะและเครื่องมือที่ตลาดต้องการสูงสุด")

    sub = df_demand[df_demand["role_family"].isin(roles)].copy()
    if sub.empty:
        return empty_chart_card("T2-2: ทักษะและเครื่องมือที่ตลาดต้องการสูงสุด")

    merged = sub.merge(df_skills, on="skill_id")
    # Average importance if multiple roles selected
    agg = merged.groupby(["skill_name", "category"], as_index=False)["importance_or_freq"].mean()
    agg = agg.sort_values(by="importance_or_freq", ascending=True)

    fig = px.bar(
        agg,
        x="importance_or_freq",
        y="skill_name",
        orientation="h",
        color="category",
        title="ความต้องการทักษะในตลาดงาน (คะแนนความสำคัญ 0 - 1)",
        labels={
            "importance_or_freq": "คะแนนความต้องการเฉลี่ย",
            "skill_name": "ทักษะ / เครื่องมือ",
            "category": "หมวดหมู่"
        },
        text="importance_or_freq",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    fig.update_layout(margin=dict(t=40, b=40, l=150, r=40))

    return chart_card(
        "T2-2: ทักษะและเครื่องมือที่ตลาดต้องการสูงสุด",
        fig,
        source_id="SAMPLE_DEMO (รอข้อมูลจริงจาก O*NET S03)",
        license_name="ตัวอย่างสาธิต (ไม่ใช่ข้อมูลจริง)",
        data_year="-",
        status="sample"
    )

def build_t2_3_employers(countries: list, year_range: list = None):
    """T2-3: employed residents by occupation (S14 Singapore MOM). No open employer list exists."""
    title = "T2-3: โครงสร้างการจ้างงานตามกลุ่มอาชีพ"
    df = data_store.sg_mom
    if df.empty or "SG" not in countries:
        return empty_chart_card(
            title, msg="ไม่มีแหล่งข้อมูลรายชื่อบริษัทเปิด — แสดงสถิติตามกลุ่มอาชีพ (Singapore MOM S14) เมื่อเลือกประเทศ SG")
    df = df.copy()
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["employed"] = pd.to_numeric(df["employed"], errors="coerce")
    ymax = year_range[1] if year_range else int(df["year"].max())
    yr = int(df[df["year"] <= ymax]["year"].max())
    sub = df[(df["year"] == yr) & (df["highest_qualification_attained"] == "degree")]
    sub = sub.groupby("occupation", as_index=False)["employed"].sum()  # male + female
    sub = sub[sub["employed"] > 0]
    if sub.empty:
        return empty_chart_card(title)
    fig = px.treemap(sub, path=["occupation"], values="employed", color="employed",
                     color_continuous_scale="Viridis",
                     title=f"ผู้มีงานทำวุฒิปริญญา แยกกลุ่มอาชีพ สิงคโปร์ (ปี {yr})")
    fig.update_traces(texttemplate="%{label}<br>%{value:,.0f}")
    fig.update_layout(margin=dict(t=50, b=20, l=20, r=20))
    return chart_card(title, fig, source_id="S14 (Ministry of Manpower Singapore)",
                      license_name="Singapore Open Data Licence v1.0", data_year=str(yr), status="verified")

_UNI_ABBR = {
    "National University of Singapore": "NUS", "Nanyang Technological University": "NTU",
    "Singapore Management University": "SMU", "Singapore University of Technology and Design": "SUTD",
    "Singapore University of Social Sciences": "SUSS", "Singapore Institute of Technology": "SIT",
}


def build_t2_4_salary(countries: list):
    """T2-4: ช่วงเงินเดือนเริ่มต้นและเปอร์เซ็นไทล์ (S15 Singapore GES)."""
    df_ges = data_store.sg_ges
    if df_ges.empty or "SG" not in countries:
        return empty_chart_card(
            "T2-4: ระดับเงินเดือนตามสายงาน",
            msg="ไม่มีแหล่งข้อมูลเงินเดือนสาย AI/DS ของไทยที่เป็น Open Data (มีข้อมูลเริ่มต้นรายหลักสูตรของสิงคโปร์ S15 เมื่อเลือกประเทศ SG)"
        )

    keyword_pat = "Data Science|Statistic|Analytics|Artificial Intelligence|Computer Science|Computing|Information Systems"
    matched = df_ges[df_ges["degree"].str.contains(keyword_pat, case=False, na=False)].copy()
    if matched.empty:
        matched = df_ges.head(20).copy()

    latest_yr = matched["year"].max()
    sub = matched[matched["year"] == latest_yr].dropna(subset=["gross_monthly_median"]).copy()
    sub = sub.sort_values(by="gross_monthly_median", ascending=True).tail(10)
    sub["label"] = sub["university"].map(_UNI_ABBR).fillna(sub["university"]) + " · " + sub["degree"].str.slice(0, 38)

    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=sub["label"],
        x=sub["gross_mthly_25_percentile"],
        name="ถึง P25",
        orientation="h",
        marker=dict(color="#3498DB")
    ))
    fig.add_trace(go.Bar(
        y=sub["label"],
        x=sub["gross_monthly_median"] - sub["gross_mthly_25_percentile"],
        name="P25 → Median",
        orientation="h",
        marker=dict(color="#2ECC71")
    ))
    fig.add_trace(go.Bar(
        y=sub["label"],
        x=sub["gross_mthly_75_percentile"] - sub["gross_monthly_median"],
        name="Median → P75",
        orientation="h",
        marker=dict(color="#F39C12")
    ))

    fig.update_layout(
        barmode="stack",
        title=f"เงินเดือนบัณฑิตจบใหม่ (SGD/เดือน) P25–Median–P75 ปี {latest_yr}",
        xaxis=dict(title="เงินเดือนรวมรายเดือน (SGD)"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(t=70, b=40, l=10, r=20), yaxis=dict(automargin=True, title=None)
    )

    return chart_card(
        "T2-4: ระดับเงินเดือนตามสายงาน",
        fig,
        source_id="S15 (Singapore Graduate Employment Survey)",
        license_name="Singapore Open Data Licence v1.0",
        data_year=str(latest_yr),
        status="verified"
    )
