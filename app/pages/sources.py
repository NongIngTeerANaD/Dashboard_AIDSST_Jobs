"""Tab 4: data sources, license and methodology (BRD AC-08)."""
from dash import html
import dash_bootstrap_components as dbc
from app.data_loader import data_store

_REAL = [
    ("S01", "Indeed Job Postings Index", "CC BY 4.0", "https://github.com/hiring-lab/job_postings_tracker", "job_postings"),
    ("S01", "Indeed Job Postings Index รายสายอาชีพ (Data & Analytics, Software Development ฯลฯ)", "CC BY 4.0", "https://github.com/hiring-lab/job_postings_tracker", "sector_postings"),
    ("S02", "Indeed AI Tracker", "CC BY 4.0", "https://github.com/hiring-lab/ai-tracker", "ai_tracker"),
    ("S14", "Singapore MOM: Employed residents by occupation/qualification", "Singapore Open Data Licence v1.0", "https://data.gov.sg/datasets/d_576bb1f46eabb041d8d966030170ec6f/view", "sg_mom"),
    ("S15", "Singapore Graduate Employment Survey", "Singapore Open Data Licence v1.0", "https://data.gov.sg/datasets/d_3c55210de27fcccda2ed0c63fdd2b352/view", "sg_ges"),
]

def build_sources_page():
    rows = []
    for sid, name, lic, url, attr in _REAL:
        df = getattr(data_store, attr, None)
        n = 0 if df is None else len(df)
        rows.append(html.Tr([html.Td(sid), html.Td(name), html.Td(lic),
                             html.Td(html.A("ลิงก์", href=url, target="_blank")),
                             html.Td(f"{n:,} แถว" if n else "⛔ ยังไม่โหลด")]))
    real_table = dbc.Table([html.Thead(html.Tr([html.Th(h) for h in ["รหัส", "ชุดข้อมูล", "License", "ที่มา", "สถานะในแอป"]])),
                            html.Tbody(rows)], bordered=True, hover=True, size="sm")
    sample_rows = []
    for name in ["programs", "graduates", "courses", "tuition", "skills_demand"]:
        df = getattr(data_store, name)
        n_s = int((df["source_id"] == "SAMPLE_DEMO").sum()) if "source_id" in df else 0
        sample_rows.append(html.Tr([html.Td(f"data/curated/{name}.csv"), html.Td(f"{len(df):,}"), html.Td(f"{n_s:,}")]))
    sample_table = dbc.Table([html.Thead(html.Tr([html.Th(h) for h in ["ไฟล์", "จำนวนแถว", "แถวที่เป็นตัวอย่างสาธิต"]])),
                              html.Tbody(sample_rows)], bordered=True, size="sm")
    return dbc.Container([
        dbc.Card(dbc.CardBody([html.H5("ข้อมูลเปิดที่ใช้อยู่จริง (ผ่านเกณฑ์ license)"), real_table,
                               html.Small("รายละเอียดเต็มของ S01–S15 อยู่ในไฟล์ labor-market-open-data-sources.md", className="text-muted")]), className="mb-3 shadow-sm"),
        dbc.Card(dbc.CardBody([html.H5("ข้อมูลตัวอย่างสาธิต (ไม่ใช่ข้อมูลจริง)", className="text-danger"), sample_table,
                               html.P("แถวที่ source_id = SAMPLE_DEMO เป็นตัวเลขสมมติเพื่อสาธิตกราฟ ห้ามอ้างอิงเป็นข้อเท็จจริง "
                                      "แทนที่ด้วยข้อมูลจริงตาม data/curated/README.md", className="mb-0")]), className="mb-3 shadow-sm border-danger"),
        dbc.Card(dbc.CardBody([
            html.H5("ระเบียบวิธีและข้อจำกัด"),
            html.Ul([
                html.Li("Supply share (s) = หน่วยกิตวิชาบังคับที่แมปกับ skill ÷ หน่วยกิตบังคับรวมของหลักสูตร"),
                html.Li("Demand share (d) = คะแนนความต้องการของ skill ÷ ผลรวมคะแนนของทุก skill ในสายงานที่เลือก"),
                html.Li("Gap Score = d − s (บวก = ตลาดต้องการมากกว่าที่สอน, ลบ = สอนมากกว่าตลาดต้องการ); Coverage@N = สัดส่วนของ Top-N skill ตลาดที่หลักสูตรสอน (s > 0)"),
                html.Li("Indeed Job Postings Index เป็นดัชนีสัมพัทธ์ (ฐาน 1 ก.พ. 2020) ไม่ใช่จำนวนตำแหน่งสัมบูรณ์ และไม่มีไทย/อาเซียน"),
                html.Li("เงินเดือน S15 เป็นของบัณฑิตสิงคโปร์จบใหม่ ใช้แทนตลาดไทยไม่ได้ และ P25/Median/P75 ไม่ใช่ระดับ Entry/Mid/Senior"),
                html.Li("ไม่มีแหล่งเปิดสำหรับ: อัตรามีงานทำปีที่ 1–3 รายหลักสูตร (ไทย), ค่าเทอม, รายชื่อบริษัท, ข้อความประกาศงาน"),
                html.Li("การแมปรายวิชา → skill เป็นการตีความ (ดู confidence ใน data/curated/course_skill_map.csv)"),
            ]),
        ]), className="shadow-sm"),
    ], fluid=True, className="p-0")
