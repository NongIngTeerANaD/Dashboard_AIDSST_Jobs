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

filter_bar = html.Div([
    dbc.Row([
        dbc.Col([html.Label("ประเทศ / ภูมิภาค"),
                 dcc.Dropdown(id="filter-country", options=_COUNTRY_OPTIONS, value=DEFAULT_FILTERS["country"], multi=True, placeholder="เลือกประเทศ…")], md=3),
        dbc.Col([html.Label("ช่วงปี"),
                 dcc.RangeSlider(id="filter-year", min=2018, max=2026, step=1,
                                 value=[DEFAULT_FILTERS["year_start"], DEFAULT_FILTERS["year_end"]],
                                 marks={y: str(y) for y in range(2018, 2027)},
                                 tooltip={"placement": "bottom", "always_visible": False})], md=3),
        dbc.Col([html.Label("ระดับการศึกษา"),
                 dcc.Dropdown(id="filter-degree", options=_DEGREE_OPTIONS, value=DEFAULT_FILTERS["degree"], multi=True, placeholder="เลือกระดับ…")], md=3),
        dbc.Col([html.Label("กลุ่มสายงาน"),
                 dcc.Dropdown(id="filter-role", options=_ROLE_OPTIONS, value=DEFAULT_FILTERS["role"], multi=True, placeholder="เลือกสายงาน…")], md=3),
    ], className="mb-2"),
    dbc.Row([
        dbc.Col(html.Div(id="filter-chips", className="d-flex flex-wrap gap-1 align-items-center"), md=8),
        dbc.Col([
            dbc.Button("ล้างการเลือกหลักสูตร", id="btn-clear-selection", color="warning", size="sm", outline=True, className="me-2"),
            dbc.Button("รีเซ็ตตัวกรอง", id="btn-clear-all", color="secondary", size="sm", outline=True),
        ], md=4, className="text-end"),
    ]),
], className="filterbar")

_NAV = [("nav-tab-1", "tab-1", "bi bi-mortarboard", "Tab 1 · ผู้สำเร็จการศึกษา"),
        ("nav-tab-2", "tab-2", "bi bi-briefcase", "Tab 2 · ตลาดงาน"),
        ("nav-tab-3", "tab-3", "bi bi-bar-chart-line", "Tab 3 · Skill Mismatch"),
        ("nav-tab-4", "tab-4", "bi bi-journal-text", "แหล่งข้อมูล & ระเบียบวิธี")]


def _programs_options():
    from app.data_loader import data_store
    df = data_store.programs
    if df.empty:
        return []
    return [{"label": r.program_name_th, "value": r.program_id} for r in df.itertuples()]


def _sample_warnings():
    from app.data_loader import data_store
    items = []
    for name in ["programs", "graduates", "courses", "tuition"]:
        df = getattr(data_store, name)
        if not df.empty and "source_id" in df and (df["source_id"] == "SAMPLE_DEMO").any():
            items.append(f"data/curated/{name}.csv: {(df['source_id'] == 'SAMPLE_DEMO').sum()} แถวเป็นตัวอย่างสาธิต")
    return items


sidebar = html.Div([
    html.Div("AI", className="brand"),
    *[dbc.Button(html.I(className=ico), id=nid, className="nav-ico", title=title, n_clicks=0) for nid, _, ico, title in _NAV],
    html.Div(className="spacer"),
    html.A(html.I(className="bi bi-github"), href="https://github.com/NongIngTeerANaD/Dashboard_AIDSST_Jobs", target="_blank",
           className="nav-ico", title="GitHub"),
], className="sidebar")

_warn = _sample_warnings()
topbar = html.Div([
    html.Div([html.Div("AIDSST·Jobs", className="logo"), html.Div("Dashboard", className="page")]),
    html.Div(html.Div([html.I(className="bi bi-search"),
                       dcc.Dropdown(id="search-program", options=_programs_options(), placeholder="ค้นหาหลักสูตร…", clearable=True)],
                      className="searchbar"), className="grow"),
    html.Span([html.I(), "TH"], className="chip-country", title="ตลาดเป้าหมาย: ประเทศไทย"),
    html.Div([
        dbc.Button([html.I(className="bi bi-bell"), html.Span(className="dot") if _warn else None], id="btn-bell", className="bell", n_clicks=0),
        dbc.Popover([dbc.PopoverHeader("การแจ้งเตือนข้อมูล"),
                     dbc.PopoverBody([html.Div("🧪 ข้อมูลตัวอย่างสาธิต (ไม่ใช่ข้อมูลจริง):", className="fw-semibold mb-1"),
                                      html.Ul([html.Li(w) for w in _warn] or [html.Li("ไม่มี")], className="small ps-3 mb-0")])],
                    target="btn-bell", trigger="legacy", placement="bottom"),
    ]),
    html.Div([html.Div("TK", className="avatar"), html.Span("สวัสดี Teeranad")], className="hello"),
], className="topbar")

layout = html.Div([
    dcc.Store(id="store-filters", data=DEFAULT_FILTERS),
    dcc.Store(id="store-selection", data={"program_id": None}),
    dcc.Download(id="download-mismatch"),
    dcc.Location(id="url", refresh=False),
    sidebar,
    html.Div([
        topbar,
        html.Div(id="hero-card"),
        html.Div([html.Strong("🧪 ข้อมูลบางส่วนเป็นตัวอย่างสาธิต: "),
                  "จำนวนผู้จบรายหลักสูตร รายวิชา ค่าเทอม และฝั่งหลักสูตรของ Tab 3 · ข้อมูลจริง (✅): Indeed, O*NET, World Bank, Eurostat, สิงคโปร์ MOM/GES · "
                  "คลิกแท่งหลักสูตรใน T1-1 / คอลัมน์ใน T3-2 หรือค้นหาหลักสูตรด้านบนเพื่อกรองทุกกราฟ"], className="alert-soft"),
        filter_bar,
        dbc.Tabs([
            dbc.Tab(label="Tab 1 · ผู้สำเร็จการศึกษา & Skill ที่เรียน", tab_id="tab-1"),
            dbc.Tab(label="Tab 2 · ตลาดงาน & Skill ที่ต้องการ", tab_id="tab-2"),
            dbc.Tab(label="Tab 3 · Skill Mismatch", tab_id="tab-3"),
            dbc.Tab(label="แหล่งข้อมูล & ระเบียบวิธี", tab_id="tab-4"),
        ], id="main-tabs", active_tab="tab-1", className="mb-3"),
        dcc.Loading(id="loading-main", type="circle", color="#8B5CF6", children=html.Div(id="tab-content", className="py-2")),
        html.Div("AIDSST·Jobs · ผู้ขอ: นักศึกษาสถิติ ปี 4 มหาวิทยาลัยขอนแก่น · ข้อมูลเปิด: CC BY 4.0, Singapore Open Data Licence, O*NET, Eurostat, OGL",
                 className="footer-note"),
    ], className="main"),
])
