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
        color_discrete_sequence=px.colors.qualitative.Bold,
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
        path=["program_name_th", "category", "skill_name", "course_name"],
        values="credits",
        title="สัดส่วนหน่วยกิตรายวิชาจำแนกตามหมวดทักษะ (Sunburst)",
        color="category",
        color_discrete_sequence=px.colors.qualitative.Prism,
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
    keyword_pat = "Data|Statistics|Computer|Analytics|Information"
    matched = df_ges[df_ges["degree"].str.contains(keyword_pat, case=False, na=False)].copy()
    if matched.empty:
        matched = df_ges.head(20).copy()

    # Aggregate by degree (latest year)
    latest_yr = matched["year"].max()
    sub = matched[matched["year"] == latest_yr].dropna(subset=["employment_rate_overall"])
    sub = sub.sort_values(by="employment_rate_overall", ascending=True).tail(10)

    fig = px.bar(
        sub,
        x="employment_rate_overall",
        y="degree",
        orientation="h",
        color="university",
        title=f"อัตราการมีงานทำภาพรวมหลังจบ ~6 เดือน (ปี {latest_yr})",
        labels={"employment_rate_overall": "อัตราการได้งาน (%)", "degree": "หลักสูตร", "university": "มหาวิทยาลัย"},
        text="employment_rate_overall",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
    fig.update_layout(margin=dict(t=40, b=40, l=150, r=40))

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
        text="total_program",
        color_discrete_sequence=px.colors.qualitative.Safe
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
