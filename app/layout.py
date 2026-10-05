"""Global layout: filter bar + 3-tab structure.

All text shown to users is in Thai; code/comments are in English.
"""
from dash import dcc, html
import dash_bootstrap_components as dbc

# ---------------------------------------------------------------------------
# Data-status badge helper
# ---------------------------------------------------------------------------
STATUS_ICONS = {
    "verified": "✅",
    "old":      "⚠️",
    "estimated": "🧮",
    "curated":  "✍️",
    "missing":  "⛔",
}


def source_badge(source_id: str, license_name: str, data_year: int | str,
                 status: str = "verified") -> html.Small:
    """Return a small text element for placing below a chart."""
    icon = STATUS_ICONS.get(status, "")
    return html.Small(
        f"{icon} แหล่ง: {source_id} · License: {license_name} · ปีข้อมูล: {data_year}",
        className="text-muted d-block mt-1",
    )


# ---------------------------------------------------------------------------
# Global filter bar
# ---------------------------------------------------------------------------
_COUNTRY_OPTIONS = [
    {"label": "ไทย",         "value": "TH"},
    {"label": "สิงคโปร์",   "value": "SG"},
    {"label": "สหรัฐอเมริกา", "value": "US"},
    {"label": "สหราชอาณาจักร", "value": "GB"},
    {"label": "ยุโรป (EU)",  "value": "EU"},
]

_DEGREE_OPTIONS = [
    {"label": "ปริญญาตรี", "value": "bachelor"},
    {"label": "ปริญญาโท",  "value": "master"},
    {"label": "ปริญญาเอก", "value": "phd"},
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
                html.Label("ประเทศ / ภูมิภาค", className="fw-semibold"),
                dcc.Dropdown(
                    id="filter-country",
                    options=_COUNTRY_OPTIONS,
                    value=["TH", "SG", "US"],
                    multi=True,
                    placeholder="เลือกประเทศ…",
                ),
            ], md=3),
            dbc.Col([
                html.Label("ช่วงปี", className="fw-semibold"),
                dcc.RangeSlider(
                    id="filter-year",
                    min=2018, max=2026, step=1,
                    value=[2020, 2025],
                    marks={y: str(y) for y in range(2018, 2027)},
                    tooltip={"placement": "bottom", "always_visible": False},
                ),
            ], md=3),
            dbc.Col([
                html.Label("ระดับการศึกษา", className="fw-semibold"),
                dcc.Dropdown(
                    id="filter-degree",
                    options=_DEGREE_OPTIONS,
                    value=["bachelor", "master"],
                    multi=True,
                    placeholder="เลือกระดับ…",
                ),
            ], md=3),
            dbc.Col([
                html.Label("กลุ่มสายงาน", className="fw-semibold"),
                dcc.Dropdown(
                    id="filter-role",
                    options=_ROLE_OPTIONS,
                    value=["ai_ml", "data_science", "statistics", "data_analyst"],
                    multi=True,
                    placeholder="เลือกสายงาน…",
                ),
            ], md=3),
        ], className="mb-2"),
        # Active filter chips row
        dbc.Row([
            dbc.Col(html.Div(id="filter-chips", className="d-flex flex-wrap gap-1"), md=10),
            dbc.Col(
                dbc.Button("ล้างทั้งหมด", id="btn-clear-all", color="secondary",
                           size="sm", outline=True),
                md=2, className="text-end",
            ),
        ]),
    ]),
    className="mb-3 shadow-sm",
)

# ---------------------------------------------------------------------------
# Main layout
# ---------------------------------------------------------------------------
layout = dbc.Container([
    # Hidden store for filter state
    dcc.Store(id="store-filters", storage_type="session"),
    # URL bar for shareable links (FR-G7)
    dcc.Location(id="url", refresh=False),

    # Header
    dbc.Row(dbc.Col(html.H3(
        "Dashboard: วิเคราะห์ตลาดงานและ Skill Mismatch · AI / Data Science / Statistics",
        className="my-3 text-primary",
    ))),

    # Global filter bar
    filter_bar,

    # Tabs
    dbc.Tabs([
        dbc.Tab(label="Tab 1 · ผู้สำเร็จการศึกษา & Skill ที่เรียน",
                tab_id="tab-1",
                children=html.Div(id="tab1-content", className="py-3")),
        dbc.Tab(label="Tab 2 · ตลาดงาน & Skill ที่ต้องการ",
                tab_id="tab-2",
                children=html.Div(id="tab2-content", className="py-3")),
        dbc.Tab(label="Tab 3 · Skill Mismatch",
                tab_id="tab-3",
                children=html.Div(id="tab3-content", className="py-3")),
    ], id="main-tabs", active_tab="tab-2"),

    html.Hr(),
    html.Footer(
        html.Small("ข้อมูลจากแหล่งเปิดที่ตรวจสอบ license แล้ว · "
                   "ดูรายละเอียดที่หน้า แหล่งข้อมูลและ License",
                   className="text-muted"),
        className="text-center mb-3",
    ),
], fluid=True)
