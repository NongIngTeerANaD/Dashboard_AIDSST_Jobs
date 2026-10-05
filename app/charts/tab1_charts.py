"""Charts for Tab 1: ผู้สำเร็จการศึกษา & Skill ที่เรียน (T1-1 to T1-4)."""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from app.data_loader import data_store
from app.charts.common import chart_card, empty_chart_card

def build_t1_1_graduates(countries: list, year_range: list, degrees: list, roles: list, highlight: str = None):
    """T1-1: หลักสูตรที่ผลิตบัณฑิตสาย AI/DS/Stat + จำนวนผู้จบต่อปี."""
    df_prog = data_store.programs
    df_grad = data_store.graduates
    if df_prog.empty or df_grad.empty:
        return empty_chart_card("T1-1: ปริมาณผู้สำเร็จการศึกษาตามหลักสูตรและแนวโน้มรายปี")

    # Filter programs
    m_prog = df_prog[
        df_prog["country"].isin(countries) &
        df_prog["degree_level"].isin(degrees) &
        df_prog["role_family"].isin(roles)
    ]
    if m_prog.empty:
        return empty_chart_card("T1-1: ปริมาณผู้สำเร็จการศึกษาตามหลักสูตรและแนวโน้มรายปี")

    # Merge with graduates
    merged = df_grad.merge(m_prog, on="program_id")
    merged = merged[
        (merged["year"] >= year_range[0]) &
        (merged["year"] <= year_range[1])
    ]
    if merged.empty:
        return empty_chart_card("T1-1: ปริมาณผู้สำเร็จการศึกษาตามหลักสูตรและแนวโน้มรายปี")

    # Group by program_name_th and year
    fig = px.bar(
        merged,
        x="year",
        y="graduates_count",
        color="program_name_th",
        barmode="group",
        title="จำนวนผู้สำเร็จการศึกษาจำแนกตามหลักสูตรและรายปี (คน)",
        labels={"year": "ปี", "graduates_count": "จำนวนผู้จบ (คน)", "program_name_th": "หลักสูตร"},
        text="graduates_count",
        custom_data=["program_id"],
    )
    fig.update_traces(textposition="outside", texttemplate="%{y}")
    if highlight:
        names = merged.loc[merged["program_id"] == highlight, "program_name_th"].unique().tolist()
        for tr in fig.data:
            tr.opacity = 1.0 if tr.name in names else 0.25
    fig.update_layout(xaxis=dict(tickmode="linear", dtick=1), margin=dict(t=40, b=40, l=40, r=40))

    src = m_prog["source_id"].iloc[0]
    lic = m_prog["license"].iloc[0]
    status = "sample" if "SAMPLE" in src else ("curated" if "CURATED" in src else "verified")
    return chart_card(
        "T1-1: ปริมาณผู้สำเร็จการศึกษาตามหลักสูตรและแนวโน้มรายปี",
        fig,
        source_id=src,
        license_name=lic,
        data_year=f"{year_range[0]}-{year_range[1]}",
        status=status,
        graph_id="graph-t1-1",
    )

def build_t1_2_courses(countries: list, degrees: list, roles: list, program_id: str = None):
    """T1-2: รายวิชาบังคับที่ตรงกับสาขางาน (Treemap / Sunburst)."""
    df_prog = data_store.programs
    df_courses = data_store.courses
    df_map = data_store.course_skill_map
    df_skills = data_store.skills

    if df_prog.empty or df_courses.empty or df_map.empty or df_skills.empty:
        return empty_chart_card("T1-2: โครงสร้างรายวิชาและทักษะที่สอนในหลักสูตร")

    m_prog = df_prog[
        df_prog["country"].isin(countries) &
        df_prog["degree_level"].isin(degrees) &
        df_prog["role_family"].isin(roles)
    ]
    if program_id:
        m_prog = m_prog[m_prog["program_id"] == program_id]
    if m_prog.empty:
        return empty_chart_card("T1-2: โครงสร้างรายวิชาและทักษะที่สอนในหลักสูตร")

    # Join courses -> map -> skills
    merged = df_courses.merge(m_prog[["program_id", "program_name_th"]], on="program_id")
    merged = merged.merge(df_map, on="course_code")
    merged = merged.merge(df_skills[["skill_id", "skill_name", "category"]], on="skill_id")

    if merged.empty:
        return empty_chart_card("T1-2: โครงสร้างรายวิชาและทักษะที่สอนในหลักสูตร")

    fig = px.sunburst(
        merged,
        path=["program_name_th", "category", "skill_name"],
        maxdepth=3,
        values="credits",
        title="สัดส่วนหน่วยกิตรายวิชาจำแนกตามหมวดทักษะ (Sunburst)",
        color="category",
    )
    fig.update_layout(margin=dict(t=40, b=20, l=20, r=20))

    return chart_card(
        "T1-2: โครงสร้างรายวิชาและทักษะที่สอนในหลักสูตร",
        fig,
        source_id="SAMPLE_DEMO",
        license_name="ตัวอย่างสาธิต (ไม่ใช่ข้อมูลจริง)",
        data_year="-",
        status="sample"
    )

def build_t1_3_employment(countries: list):
    """T1-3: บัณฑิตที่มีงานทำ (Singapore GES S15 & curated)."""
    df_ges = data_store.sg_ges
    if df_ges.empty or "SG" not in countries:
        # If user selected only Thailand, show notice about Thai employment data
        return empty_chart_card(
            "T1-3: อัตราการมีงานทำของบัณฑิตหลังจบการศึกษา",
            msg="ไม่มีแหล่งข้อมูลเปิดระดับรายหลักสูตรสำหรับอัตรางานทำปีที่ 1-3 ของไทย (มีข้อมูลสิงคโปร์ S15 เมื่อเลือกประเทศ SG)"
        )

    # Filter tech/stat/data degrees
    keyword_pat = "Data Science|Statistic|Analytics|Artificial Intelligence|Computer Science|Computing|Information Systems"
    matched = df_ges[df_ges["degree"].str.contains(keyword_pat, case=False, na=False)].copy()
    if matched.empty:
        matched = df_ges.head(20).copy()

    # Aggregate by degree (latest year)
    latest_yr = matched["year"].max()
    sub = matched[matched["year"] == latest_yr].dropna(subset=["employment_rate_overall"])
    sub = sub.sort_values(by="employment_rate_overall", ascending=True).tail(12)
    abbr = {"National University of Singapore": "NUS", "Nanyang Technological University": "NTU",
            "Singapore Management University": "SMU", "Singapore University of Technology and Design": "SUTD",
            "Singapore University of Social Sciences": "SUSS", "Singapore Institute of Technology": "SIT"}
    sub["degree"] = sub["university"].map(abbr).fillna(sub["university"]) + " · " + sub["degree"].str.slice(0, 38)

    fig = px.bar(
        sub,
        x="employment_rate_overall",
        y="degree",
        orientation="h",
        color="university",
        title=f"อัตราการมีงานทำภาพรวมหลังจบ ~6 เดือน (ปี {latest_yr})",
        labels={"employment_rate_overall": "อัตราการได้งาน (%)", "degree": "หลักสูตร", "university": "มหาวิทยาลัย"},
        text="employment_rate_overall"
    )
    fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
    fig.update_layout(margin=dict(t=40, b=40, l=10, r=60), yaxis=dict(automargin=True, title=None),
                      xaxis=dict(range=[0, 108]), legend=dict(orientation="h", y=-0.2, title=None))

    return chart_card(
        "T1-3: อัตราการมีงานทำของบัณฑิตหลังจบการศึกษา",
        fig,
        source_id="S15 (Singapore MOE / data.gov.sg)",
        license_name="Singapore Open Data Licence v1.0",
        data_year=str(latest_yr),
        status="verified"
    )

def build_t1_4_tuition(countries: list, degrees: list, roles: list, program_id: str = None):
    """T1-4: ค่าเทอมตลอดหลักสูตร (แสดง ⛔ ถ้าไม่มีข้อมูล)."""
    df_prog = data_store.programs
    df_tuition = data_store.tuition
    if df_prog.empty or df_tuition.empty:
        return empty_chart_card("T1-4: ค่าเล่าเรียนและค่าธรรมเนียมตลอดหลักสูตร")

    m_prog = df_prog[
        df_prog["country"].isin(countries) &
        df_prog["degree_level"].isin(degrees) &
        df_prog["role_family"].isin(roles)
    ]
    if program_id:
        m_prog = m_prog[m_prog["program_id"] == program_id]
    if m_prog.empty:
        return empty_chart_card("T1-4: ค่าเล่าเรียนและค่าธรรมเนียมตลอดหลักสูตร")

    merged = df_tuition.merge(m_prog, on="program_id")
    if merged.empty:
        return empty_chart_card(
            "T1-4: ค่าเล่าเรียนและค่าธรรมเนียมตลอดหลักสูตร",
            msg="ไม่พบแหล่งข้อมูลเปิดสำหรับค่าเทอมในตัวกรองนี้ (ข้อมูล Curated ยังไม่ได้ระบุ)"
        )

    fig = px.bar(
        merged,
        x="program_name_th",
        y="total_program",
        color="institution",
        title="ค่าธรรมเนียมการศึกษาตลอดหลักสูตร (บาท)",
        labels={"total_program": "ค่าเทอมตลอดหลักสูตร (THB)", "program_name_th": "หลักสูตร", "institution": "สถาบัน"},
        text="total_program"
    )
    fig.update_traces(texttemplate="%{text:,.0f} ฿", textposition="outside")
    fig.update_layout(margin=dict(t=40, b=60, l=50, r=40))

    return chart_card(
        "T1-4: ค่าเล่าเรียนและค่าธรรมเนียมตลอดหลักสูตร",
        fig,
        source_id="SAMPLE_DEMO",
        license_name="ตัวอย่างสาธิต (ไม่ใช่ข้อมูลจริง)",
        data_year="-",
        status="sample"
    )


ISO2_TO_ISO3 = {"TH": "THA", "SG": "SGP", "US": "USA", "GB": "GBR", "DE": "DEU", "FR": "FRA", "AU": "AUS", "IN": "IND"}


def build_t1_5_grad_unemployment(countries: list, year_range: list):
    """T1-5: unemployment rate of people with advanced education (World Bank / ILO modelled estimate, S07)."""
    title = "T1-5: อัตราว่างงานของผู้จบการศึกษาระดับสูง"
    df = data_store.uem_advanced
    if df.empty:
        return empty_chart_card(title, msg="ยังไม่มีข้อมูล S07 — รัน python -m etl.fetch_s07_worldbank")
    df = df.copy()
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    codes = [ISO2_TO_ISO3[c] for c in countries if c in ISO2_TO_ISO3]
    sub = df[df["country_code"].isin(codes) & df["year"].between(year_range[0], year_range[1])].dropna(subset=["unemployment_rate_pct"])
    if sub.empty:
        return empty_chart_card(title)
    sub = sub.sort_values(["country", "year"])
    fig = px.line(sub, x="year", y="unemployment_rate_pct", color="country", markers=True,
                  title="อัตราว่างงานของผู้มีการศึกษาระดับสูง (% ของกำลังแรงงานกลุ่มนี้)",
                  labels={"year": "ปี", "unemployment_rate_pct": "อัตราว่างงาน (%)", "country": "ประเทศ"})
    fig.update_xaxes(dtick=1)
    fig.update_layout(hovermode="x unified", margin=dict(t=50, b=40, l=40, r=20), legend=dict(orientation="h", y=-0.25, title=None))
    last = int(sub["year"].max())
    return chart_card(title, fig, source_id="S07 (World Bank SL.UEM.ADVN.ZS, ที่มา ILO)", license_name="CC BY 4.0",
                      data_year=f"{int(sub['year'].min())}-{last}", status="verified")


_FIELD_LABELS = {"F054": "คณิตศาสตร์และสถิติ", "F0542": "สถิติ", "F061": "ICT"}
_LEVEL_LABELS = {"ED6": "ป.ตรี", "ED7": "ป.โท", "ED8": "ป.เอก"}
_DEGREE_TO_LEVEL = {"bachelor": "ED6", "master": "ED7", "phd": "ED8"}


def build_t1_6_eu_graduates(countries: list, year_range: list, degrees: list):
    """T1-6: graduates in mathematics/statistics and ICT fields (Eurostat educ_uoe_grad02, S09). Europe only."""
    title = "T1-6: จำนวนผู้สำเร็จการศึกษาสาขาคณิตศาสตร์/สถิติ และ ICT (ยุโรป)"
    df = data_store.eu_graduates
    if df.empty:
        return empty_chart_card(title, msg="ยังไม่มีข้อมูล S09 — รัน python -m etl.fetch_s09_eurostat_grad")
    df = df.copy()
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    levels = [_DEGREE_TO_LEVEL[d] for d in degrees if d in _DEGREE_TO_LEVEL]
    areas = ["EU27_2020"] + [c for c in countries if c in ("DE", "FR")]
    sub = df[df["country_code"].isin(areas) & df["field"].isin(_FIELD_LABELS) & df["level"].isin(levels)
             & df["year"].between(year_range[0], year_range[1])].dropna(subset=["graduates"])
    if sub.empty:
        return empty_chart_card(title, msg="ไม่มีข้อมูลผู้จบตามตัวกรองที่เลือก (S09 มีถึงปี 2024; ระดับ ป.ตรี/โท/เอก)")
    sub = sub.assign(สาขา=sub["field"].map(_FIELD_LABELS), ระดับ=sub["level"].map(_LEVEL_LABELS),
                     พื้นที่=sub["country_code"].replace({"EU27_2020": "EU27"}))
    fig = px.line(sub.sort_values("year"), x="year", y="graduates", color="สาขา", line_dash="ระดับ",
                  facet_col="พื้นที่", facet_col_wrap=3, markers=True,
                  title="ผู้สำเร็จการศึกษา (คน/ปี) แยกสาขาและระดับ",
                  labels={"year": "ปี", "graduates": "จำนวนผู้จบ (คน)"})
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    fig.update_xaxes(dtick=2)
    fig.update_yaxes(matches=None)
    fig.update_layout(hovermode="x unified", margin=dict(t=60, b=40, l=40, r=20), legend=dict(orientation="h", y=-0.3, title=None))
    return chart_card(title, fig, source_id="S09 (Eurostat educ_uoe_grad02)", license_name="Eurostat reuse policy",
                      data_year=f"{int(sub['year'].min())}-{int(sub['year'].max())}", status="verified")
