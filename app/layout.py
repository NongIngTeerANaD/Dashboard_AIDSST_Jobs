"""Global layout: filter bar + active tab container.

All text shown to users is in Thai; code/comments are in English.
"""
from dash import dcc, html
import dash_bootstrap_components as dbc

# Initial default filters
DEFAULT_FILTERS = {
    "country": ["TH", "SG", "US"],
    "year_start": 2020,
    "year_end": 2026,
    "degree": ["bachelor", "master"],
    "role": ["ai_ml", "data_science", "statistics", "data_analyst"],
}

_COUNTRY_OPTIONS = [
    {"label": "ไทย (TH)",            "value": "TH"},
    {"label": "สิงคโปร์ (SG)",        "value": "SG"},
    {"label": "สหรัฐอเมริกา (US)",    "value": "US"},
    {"label": "สหราชอาณาจักร (GB)",   "value": "GB"},
    {"label": "เยอรมนี (DE)",         "value": "DE"},
    {"label": "ฝรั่งเศส (FR)",        "value": "FR"},
    {"label": "ออสเตรเลีย (AU)",      "value": "AU"},
    {"label": "อินเดีย (IN)",         "value": "IN"},
]

_DEGREE_OPTIONS = [
    {"label": "ปริญญาตรี (Bachelor)", "value": "bachelor"},
    {"label": "ปริญญาโท (Master)",    "value": "master"},
    {"label": "ปริญญาเอก (Ph.D.)",    "value": "phd"},
]

_ROLE_OPTIONS = [
    {"label": "AI / Machine Learning",        "value": "ai_ml"},
    {"label": "Data Science",                 "value": "data_science"},
    {"label": "Statistics / Biostatistics",   "value": "statistics"},
    {"label": "Data Analyst / Engineer",      "value": "data_analyst"},
]

filter_bar = dbc.Card(
    dbc.CardBody([
        dbc.Row([
            dbc.Col([
                html.Label("ประเทศ / ภูมิภาค", className="fw-bold text-dark"),
                dcc.Dropdown(
                    id="filter-country",
                    options=_COUNTRY_OPTIONS,
                    value=DEFAULT_FILTERS["country"],
                    multi=True,
                    placeholder="เลือกประเทศ…",
                ),
            ], md=3),
            dbc.Col([
                html.Label("ช่วงปี (2018 - 2026)", className="fw-bold text-dark"),
                dcc.RangeSlider(
                    id="filter-year",
                    min=2018, max=2026, step=1,
                    value=[DEFAULT_FILTERS["year_start"], DEFAULT_FILTERS["year_end"]],
                    marks={y: str(y) for y in range(2018, 2027)},
                    tooltip={"placement": "bottom", "always_visible": False},
                ),
            ], md=3),
            dbc.Col([
                html.Label("ระดับการศึกษา", className="fw-bold text-dark"),
                dcc.Dropdown(
                    id="filter-degree",
                    options=_DEGREE_OPTIONS,
                    value=DEFAULT_FILTERS["degree"],
                    multi=True,
                    placeholder="เลือกระดับ…",
                ),
            ], md=3),
            dbc.Col([
                html.Label("กลุ่มสายงาน", className="fw-bold text-dark"),
                dcc.Dropdown(
                    id="filter-role",
                    options=_ROLE_OPTIONS,
                    value=DEFAULT_FILTERS["role"],
                    multi=True,
                    placeholder="เลือกสายงาน…",
                ),
            ], md=3),
        ], className="mb-2"),
        # Active filter chips row
        dbc.Row([
            dbc.Col(html.Div(id="filter-chips", className="d-flex flex-wrap gap-1 align-items-center"), md=8),
            dbc.Col([
                dbc.Button("ล้างการเลือกหลักสูตร", id="btn-clear-selection", color="warning",
                           size="sm", outline=True, className="me-2"),
                dbc.Button("รีเซ็ตตัวกรอง", id="btn-clear-all", color="secondary",
                           size="sm", outline=True),
            ], md=4, className="text-end"),
        ]),
    ]),
    className="mb-4 shadow-sm border-0 bg-light",
)

layout = dbc.Container([
    # Store for filter state with initial default data
    dcc.Store(id="store-filters", data=DEFAULT_FILTERS),
    dcc.Store(id="store-selection", data={"program_id": None}),
    dcc.Download(id="download-mismatch"),
    dcc.Location(id="url", refresh=False),

    # Header Banner
    dbc.Row(dbc.Col([
        html.Div([
            html.H2(
                "Dashboard วิเคราะห์ตลาดงานและ Skill Mismatch",
                className="fw-bold text-primary mb-1",
            ),
            html.P(
                "สายงาน AI / Data Science / Statistics · ข้อมูลจากแหล่งเปิดที่ตรวจสอบแล้ว (S01–S15) และข้อมูลหลักสูตร Curated",
                className="text-muted mb-0",
            ),
        ], className="py-3")
    ])),

    dbc.Alert([
        html.Strong("⚠️ ข้อมูลบางส่วนเป็นตัวอย่างสาธิต (ไม่ใช่ข้อมูลจริง): "),
        "จำนวนผู้จบ รายวิชา ค่าเทอม และคะแนนความต้องการ skill (กราฟที่ติดป้าย 🧪) · "
        "ข้อมูลจริง (✅) ได้แก่ Indeed Job Postings (S01/S02) และสิงคโปร์ MOM/GES (S14/S15) · "
        "เคล็ดลับ: คลิกแท่งหลักสูตรใน T1-1 หรือคอลัมน์ใน T3-2 เพื่อกรองทุกกราฟในทุกแท็บ",
    ], color="warning", className="py-2 small"),

    # Global filter bar
    filter_bar,

    # Navigation Tabs
    dbc.Tabs([
        dbc.Tab(label="Tab 1 · ผู้สำเร็จการศึกษา & Skill ที่เรียน", tab_id="tab-1", label_class_name="fw-semibold"),
        dbc.Tab(label="Tab 2 · ตลาดงาน & Skill ที่ต้องการ", tab_id="tab-2", label_class_name="fw-semibold"),
        dbc.Tab(label="Tab 3 · Skill Mismatch (วิเคราะห์ช่องว่างทักษะ)", tab_id="tab-3", label_class_name="fw-semibold"),
        dbc.Tab(label="แหล่งข้อมูล & ระเบียบวิธี", tab_id="tab-4", label_class_name="fw-semibold"),
    ], id="main-tabs", active_tab="tab-1", className="mb-3"),

    # Single container for active tab content (Never unmounted!)
    dcc.Loading(
        id="loading-main",
        type="circle",
        color="#3498DB",
        children=html.Div(id="tab-content", className="py-2")
    ),

    html.Hr(className="mt-5"),
    html.Footer(
        html.Div([
            html.Small(
                "ระบบวิเคราะห์ตลาดงานและทักษะ · ผู้ขอ: นักศึกษาสถิติ ปี 4 มหาวิทยาลัยขอนแก่น · "
                "ข้อมูลเปิดมาตรฐาน Open Data: CC BY 4.0, Singapore Open Data Licence, O*NET, Eurostat",
                className="text-muted"
            )
        ], className="text-center py-3"),
    ),
], fluid=True, className="px-4 py-2")
