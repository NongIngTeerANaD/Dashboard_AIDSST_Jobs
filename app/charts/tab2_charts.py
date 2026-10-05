"""Charts for Tab 2: ตลาดงาน & Skill ที่ต้องการ (T2-1 to T2-4)."""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app.data_loader import data_store
from app.charts.common import chart_card, empty_chart_card

def build_t2_1_postings(countries: list, year_range: list):
    """T2-1: ปริมาณตำแหน่งงานว่างและแนวโน้มความต้องการ (Indeed S01)."""
    df = data_store.job_postings
    if df.empty:
        return empty_chart_card("T2-1: ดัชนีความต้องการแรงงาน (Indeed Job Postings Index)")

    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["year"] = df["date"].dt.year
    sub = df[
        df["country_code"].isin(countries) &
        (df["year"] >= year_range[0]) &
        (df["year"] <= year_range[1])
    ]
    if sub.empty:
        return empty_chart_card(
            "T2-1: ดัชนีความต้องการแรงงาน (Indeed Job Postings Index)",
            msg="ไม่มีข้อมูลประกาศงานของไทย/อาเซียน (Indeed มีเฉพาะ US, GB, DE, FR, AU) — กรุณาเลือกประเทศดังกล่าวในตัวกรอง"
        )

    # Subsample weekly to make chart snappy and fast
    sub = sub.sort_values("date")
    sub_sampled = sub.iloc[::7]

    fig = px.line(
        sub_sampled,
        x="date",
        y="indeed_job_postings_index_SA",
        color="country_code",
        title="ดัชนีประกาศงาน Indeed Job Postings Index (ฐาน 1 ก.พ. 2020 = 100)",
        labels={
            "date": "วันที่",
            "indeed_job_postings_index_SA": "ดัชนีการจ้างงาน (ปรับฤดูกาล)",
            "country_code": "ประเทศ"
        },
        color_discrete_sequence=px.colors.qualitative.Dark24
    )
    fig.update_layout(hovermode="x unified", margin=dict(t=40, b=40, l=40, r=40))

    return chart_card(
        "T2-1: ดัชนีความต้องการแรงงาน (Indeed Job Postings Index)",
        fig,
        source_id="S01 (Indeed Hiring Lab)",
        license_name="CC BY 4.0",
        data_year=f"{year_range[0]}-{year_range[1]}",
        status="verified"
    )

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

def build_t2_3_employers(countries: list):
    """T2-3: การจ้างงานจำแนกตามกลุ่มอาชีพ/อุตสาหกรรม (S14 Singapore MOM)."""
    df_mom = data_store.sg_mom
    if df_mom.empty or "SG" not in countries:
        return empty_chart_card(
            "T2-3: โครงสร้างการจ้างงานตามกลุ่มอาชีพ",
            msg="ไม่มีแหล่งข้อมูลรายชื่อบริษัทเปิด — แสดงสถิติตามกลุ่มอาชีพ (Singapore MOM S14) เมื่อเลือกประเทศ SG"
        )

    # Latest year
    latest_yr = df_mom["year"].max()
    sub = df_mom[
        (df_mom["year"] == latest_yr) &
        (df_mom["sex"] == "Total") &
        (df_mom["highest_qualification_attained"] == "Total")
    ].dropna(subset=["employed"]).copy()

    if sub.empty:
        sub = df_mom.dropna(subset=["employed"]).head(10).copy()

    sub = sub.sort_values(by="employed", ascending=False).head(10)

    fig = px.treemap(
        sub,
        path=["occupation"],
        values="employed",
        title=f"จำนวนผู้มีงานทำจำแนกตามกลุ่มอาชีพในสิงคโปร์ (ปี {latest_yr})",
        color="employed",
        color_continuous_scale="Viridis",
    )
    fig.update_layout(margin=dict(t=40, b=20, l=20, r=20))

    return chart_card(
        "T2-3: โครงสร้างการจ้างงานตามกลุ่มอาชีพ",
        fig,
        source_id="S14 (Ministry of Manpower Singapore)",
        license_name="Singapore Open Data Licence v1.0",
        data_year=str(latest_yr),
        status="verified"
    )

def build_t2_4_salary(countries: list):
    """T2-4: ช่วงเงินเดือนเริ่มต้นและเปอร์เซ็นไทล์ (S15 Singapore GES)."""
    df_ges = data_store.sg_ges
    if df_ges.empty or "SG" not in countries:
        return empty_chart_card(
            "T2-4: ระดับเงินเดือนตามสายงาน",
            msg="ไม่มีแหล่งข้อมูลเงินเดือนสาย AI/DS ของไทยที่เป็น Open Data (มีข้อมูลเริ่มต้นรายหลักสูตรของสิงคโปร์ S15 เมื่อเลือกประเทศ SG)"
        )

    keyword_pat = "Data|Statistics|Computer|Analytics|Information"
    matched = df_ges[df_ges["degree"].str.contains(keyword_pat, case=False, na=False)].copy()
    if matched.empty:
        matched = df_ges.head(20).copy()

    latest_yr = matched["year"].max()
    sub = matched[matched["year"] == latest_yr].dropna(subset=["gross_monthly_median"]).copy()
    sub = sub.sort_values(by="gross_monthly_median", ascending=True).tail(8)

    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=sub["degree"],
        x=sub["gross_mthly_25_percentile"],
        name="ถึง P25",
        orientation="h",
        marker=dict(color="#3498DB")
    ))
    fig.add_trace(go.Bar(
        y=sub["degree"],
        x=sub["gross_monthly_median"] - sub["gross_mthly_25_percentile"],
        name="P25 → Median",
        orientation="h",
        marker=dict(color="#2ECC71")
    ))
    fig.add_trace(go.Bar(
        y=sub["degree"],
        x=sub["gross_mthly_75_percentile"] - sub["gross_monthly_median"],
        name="Median → P75",
        orientation="h",
        marker=dict(color="#F39C12")
    ))

    fig.update_layout(
        barmode="stack",
        title=f"เงินเดือนบัณฑิตจบใหม่รายเดือน (SGD) P25/Median/P75 (ปี {latest_yr}) — ไม่ใช่ระดับ Entry/Mid/Senior",
        xaxis=dict(title="เงินเดือนรวมรายเดือน (SGD)"),
        yaxis=dict(title="หลักสูตร"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(t=60, b=40, l=150, r=40)
    )

    return chart_card(
        "T2-4: ระดับเงินเดือนตามสายงาน",
        fig,
        source_id="S15 (Singapore Graduate Employment Survey)",
        license_name="Singapore Open Data Licence v1.0",
        data_year=str(latest_yr),
        status="verified"
    )
