"""Charts for Tab 3: Skill Mismatch (T3-2 to T3-6)."""
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dash import html
import dash_bootstrap_components as dbc
from app.data_loader import data_store
from app.charts.common import chart_card, empty_chart_card
from app.metrics import supply_share, demand_share, gap_score, coverage_at_n

def compute_mismatch_table(countries: list, degrees: list, roles: list, program_id: str = None):
    """Calculate supply share s, demand share d, and gap score = d - s for each (program, skill)."""
    df_prog = data_store.programs
    df_courses = data_store.courses
    df_map = data_store.course_skill_map
    df_skills = data_store.skills
    df_demand = data_store.skills_demand

    if df_prog.empty or df_courses.empty or df_map.empty or df_skills.empty or df_demand.empty:
        return pd.DataFrame()

    m_prog = df_prog[
        df_prog["country"].isin(countries) &
        df_prog["degree_level"].isin(degrees) &
        df_prog["role_family"].isin(roles)
    ]
    if program_id:
        m_prog = m_prog[m_prog["program_id"] == program_id]
    if m_prog.empty:
        return pd.DataFrame()

    # 1. Calculate Supply Share (s) per program per skill
    # Total required credits per program
    total_creds = df_courses[df_courses["is_required"]].groupby("program_id")["credits"].sum().to_dict()

    # only required courses count toward supply (same basis as the denominator)
    course_with_skills = df_courses[df_courses["is_required"]].merge(df_map, on="course_code")
    # credits per (program_id, skill_id)
    prog_skill_creds = course_with_skills.groupby(["program_id", "skill_id"])["credits"].sum().reset_index()

    # 2. Calculate Demand Share (d) across selected roles
    sub_demand = df_demand[df_demand["role_family"].isin(roles)]
    if sub_demand.empty:
        return pd.DataFrame()
    total_demand_val = sub_demand["importance_or_freq"].sum()
    skill_demand_sum = sub_demand.groupby("skill_id")["importance_or_freq"].sum().reset_index()
    skill_demand_sum["d"] = skill_demand_sum["importance_or_freq"].apply(lambda v: demand_share(v, total_demand_val))

    # 3. Cartesian product of filtered programs x all skills
    all_skill_ids = df_skills["skill_id"].unique()
    rows = []
    for _, prog in m_prog.iterrows():
        pid = prog["program_id"]
        tot_c = total_creds.get(pid, 30) # default fallback if 0
        for sid in all_skill_ids:
            # find credits
            match_c = prog_skill_creds[
                (prog_skill_creds["program_id"] == pid) &
                (prog_skill_creds["skill_id"] == sid)
            ]
            creds = match_c["credits"].sum() if not match_c.empty else 0
            s = supply_share(creds, tot_c)

            match_d = skill_demand_sum[skill_demand_sum["skill_id"] == sid]
            d = match_d["d"].iloc[0] if not match_d.empty else 0.0

            gap = gap_score(d, s)
            rows.append({
                "program_id": pid,
                "program_name_th": prog["program_name_th"],
                "skill_id": sid,
                "credits": creds,
                "s": s,
                "d": d,
                "gap": gap
            })

    res = pd.DataFrame(rows)
    res = res.merge(df_skills[["skill_id", "skill_name", "category"]], on="skill_id")
    return res

def build_t3_2_heatmap(mismatch_df: pd.DataFrame):
    """T3-2: Heatmap Mismatch (Gap Score = d - s)."""
    if mismatch_df.empty:
        return empty_chart_card("T3-2: Heatmap ช่องว่างทักษะ (Skill Gap Heatmap)")

    pivot = mismatch_df.pivot(index="skill_name", columns="program_name_th", values="gap").fillna(0)

    fig = px.imshow(
        pivot,
        color_continuous_scale="RdBu_r",
        color_continuous_midpoint=0,
        labels=dict(x="หลักสูตร", y="ทักษะ", color="Gap Score (d - s)"),
        title="ช่องว่างทักษะ: สีแดง = ตลาดต้องการมากกว่าที่สอน (ขาด) · สีน้ำเงิน = สอนมากกว่าตลาดต้องการ (เกิน)",
        aspect="auto"
    )
    fig.update_layout(margin=dict(t=50, b=40, l=150, r=40))

    return chart_card(
        "T3-2: Heatmap ช่องว่างทักษะ (Skill Gap Heatmap)",
        fig,
        source_id="SAMPLE_DEMO",
        license_name="ตัวอย่างสาธิต (ไม่ใช่ข้อมูลจริง)",
        data_year="-",
        status="sample",
        graph_id="graph-t3-2",
    )

def build_t3_3_quadrant(mismatch_df: pd.DataFrame):
    """T3-3: Quadrant Chart (X = s สอน, Y = d ตลาดต้องการ)."""
    if mismatch_df.empty:
        return empty_chart_card("T3-3: กราฟ 4 จตุภาค (Quadrant Analysis)")

    # Average s and d across programs
    agg = mismatch_df.groupby(["skill_name", "category"], as_index=False).agg({"s": "mean", "d": "mean", "gap": "mean"})

    # Thresholds: mean of s and mean of d
    x_thresh = agg["s"].mean()
    y_thresh = agg["d"].mean()

    def get_quadrant(row):
        if row["s"] >= x_thresh and row["d"] >= y_thresh:
            return "1. ตรงความต้องการ (High Supply, High Demand)"
        elif row["s"] < x_thresh and row["d"] >= y_thresh:
            return "2. ขาดแคลน (Low Supply, High Demand)"
        elif row["s"] >= x_thresh and row["d"] < y_thresh:
            return "3. สอนเกินความต้องการ (High Supply, Low Demand)"
        else:
            return "4. ความสำคัญต่ำ (Low Supply, Low Demand)"

    agg["quadrant"] = agg.apply(get_quadrant, axis=1)

    fig = px.scatter(
        agg,
        x="s",
        y="d",
        color="quadrant",
        text="skill_name",
        title="การกระจายตัวของทักษะ: แกน X = สัดส่วนที่สอน (s), แกน Y = สัดส่วนที่ตลาดต้องการ (d)",
        labels={"s": "สัดส่วนที่สอน (Supply Share s)", "d": "สัดส่วนที่ตลาดต้องการ (Demand Share d)", "quadrant": "กลุ่มจตุภาค"},
        color_discrete_map={
            "1. ตรงความต้องการ (High Supply, High Demand)": "#2ECC71",
            "2. ขาดแคลน (Low Supply, High Demand)": "#E74C3C",
            "3. สอนเกินความต้องการ (High Supply, Low Demand)": "#F39C12",
            "4. ความสำคัญต่ำ (Low Supply, Low Demand)": "#95A5A6"
        }
    )
    fig.add_vline(x=x_thresh, line_dash="dash", line_color="gray", annotation_text="เกณฑ์ Supply เฉลี่ย")
    fig.add_hline(y=y_thresh, line_dash="dash", line_color="gray", annotation_text="เกณฑ์ Demand เฉลี่ย")
    fig.update_traces(textposition="top center", marker=dict(size=14))
    fig.update_layout(margin=dict(t=50, b=40, l=40, r=40))

    return chart_card(
        "T3-3: กราฟ 4 จตุภาค (Quadrant Analysis)",
        fig,
        source_id="SAMPLE_DEMO",
        license_name="ตัวอย่างสาธิต (ไม่ใช่ข้อมูลจริง)",
        data_year="-",
        status="sample"
    )

def build_t3_4_top_gaps(mismatch_df: pd.DataFrame):
    """T3-4: Top Gaps (ทักษะที่ขาดมากสุด vs เกินมากสุด)."""
    if mismatch_df.empty:
        return empty_chart_card("T3-4: ทักษะที่ขาดแคลนและเกินความต้องการสูงสุด")

    agg = mismatch_df.groupby("skill_name", as_index=False)["gap"].mean()
    top_shortage = agg.sort_values("gap", ascending=False).head(5)
    top_excess = agg.sort_values("gap", ascending=True).head(5)
    top_combined = pd.concat([top_shortage, top_excess]).drop_duplicates().sort_values("gap")

    top_combined["status"] = top_combined["gap"].apply(lambda g: "ตลาดต้องการมากกว่าที่สอน (ขาด)" if g > 0 else "สอนมากกว่าตลาดต้องการ (เกิน)")

    fig = px.bar(
        top_combined,
        x="gap",
        y="skill_name",
        orientation="h",
        color="status",
        title="อันดับทักษะที่มีช่องว่างสูงสุด (Gap Score = d - s)",
        labels={"gap": "Gap Score (บวก = ขาด, ลบ = เกิน)", "skill_name": "ทักษะ", "status": "สถานะช่องว่าง"},
        color_discrete_map={
            "ตลาดต้องการมากกว่าที่สอน (ขาด)": "#E74C3C",
            "สอนมากกว่าตลาดต้องการ (เกิน)": "#3498DB"
        },
        text="gap"
    )
    fig.update_traces(texttemplate="%{text:+.3f}", textposition="outside")
    fig.update_layout(margin=dict(t=40, b=40, l=150, r=40))

    return chart_card(
        "T3-4: ทักษะที่ขาดแคลนและเกินความต้องการสูงสุด",
        fig,
        source_id="SAMPLE_DEMO",
        license_name="ตัวอย่างสาธิต (ไม่ใช่ข้อมูลจริง)",
        data_year="-",
        status="sample"
    )

def build_t3_5_coverage(mismatch_df: pd.DataFrame):
    """T3-5: Coverage Score ต่อหลักสูตร (Coverage@N)."""
    if mismatch_df.empty:
        return empty_chart_card("T3-5: คะแนนความครอบคลุมทักษะ (Coverage@N)")

    # Top 5 market skills across all selected roles
    market_skills = mismatch_df.groupby("skill_name")["d"].mean().sort_values(ascending=False).head(5).index.tolist()

    records = []
    for prog, group in mismatch_df.groupby("program_name_th"):
        taught = set(group[group["s"] > 0]["skill_name"])
        cov = coverage_at_n(market_skills, taught)
        records.append({"program": prog, "coverage_pct": cov * 100})

    cov_df = pd.DataFrame(records).sort_values("coverage_pct", ascending=True)

    fig = px.bar(
        cov_df,
        x="coverage_pct",
        y="program",
        orientation="h",
        color="coverage_pct",
        color_continuous_scale="Teal",
        title=f"สัดส่วนความครอบคลุมทักษะ Top-{len(market_skills)} ที่ตลาดต้องการ (Coverage@5)",
        labels={"coverage_pct": "ความครอบคลุม (%)", "program": "หลักสูตร"},
        text="coverage_pct"
    )
    fig.update_traces(texttemplate="%{text:.0f}%", textposition="outside")
    fig.update_layout(xaxis=dict(range=[0, 115]), margin=dict(t=40, b=40, l=150, r=40))

    return chart_card(
        "T3-5: คะแนนความครอบคลุมทักษะ (Coverage@N)",
        fig,
        source_id="SAMPLE_DEMO",
        license_name="ตัวอย่างสาธิต (ไม่ใช่ข้อมูลจริง)",
        data_year="-",
        status="sample"
    )
