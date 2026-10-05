"""Common helpers for Plotly charts and badges."""
from dash import html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px

# Theme color palettes (colorful, high contrast, readable)
PALETTE = px.colors.qualitative.Plotly
COLOR_PRIMARY = "#2C3E50"
COLOR_ACCENT = "#3498DB"
COLOR_SUCCESS = "#2ECC71"
COLOR_WARNING = "#F39C12"
COLOR_DANGER = "#E74C3C"

GRAPH_HEIGHT = 460

STATUS_ICONS = {
    "verified": "✅ ข้อมูลเปิดตรวจแล้ว",
    "old": "⚠️ เก่ากว่า 3 ปี",
    "estimated": "🧮 ค่าประมาณ / อนุมาน",
    "curated": "✍️ ข้อมูลที่ผู้ใช้เพิ่มเอง",
    "missing": "⛔ ไม่มีข้อมูลเปิด",
    "sample": "🧪 ข้อมูลตัวอย่างสาธิต (ไม่ใช่ข้อมูลจริง)",
}

def empty_chart_card(title: str, msg: str = "ไม่พบข้อมูลสำหรับตัวกรองนี้"):
    """Render empty state card per FR-G6 & AC-05."""
    return dbc.Card([
        dbc.CardHeader(html.H5(title, className="mb-0 text-secondary")),
        dbc.CardBody([
            html.Div([
                html.Span("⛔ ", style={"fontSize": "1.8rem"}),
                html.H6(msg, className="text-muted d-inline-block align-middle mb-0"),
            ], className="text-center py-5")
        ])
    ], className="h-100 shadow-sm")

def chart_card(title: str, fig: go.Figure, source_id: str, license_name: str, data_year: str, status: str = "verified", graph_id: str = None):
    """Wrap chart in a standardized Bootstrap Card with source badge."""
    from dash import dcc
    status_label = STATUS_ICONS.get(status, "✅ ข้อมูลเปิด")
    is_old = False
    try:
        years = [int(y) for y in str(data_year).split("-") if y.isdigit()]
        if years and max(years) < 2023:
            is_old = True
    except Exception:
        pass

    badge_elements = [
        html.Span(f"{status_label} · ", className="fw-semibold"),
        html.Span(f"แหล่ง: {source_id} · License: {license_name} · ปีข้อมูล: {data_year}"),
    ]
    if is_old:
        badge_elements.append(html.Span(" ⚠️ ข้อมูลอาจเก่ากว่า 3 ปี", className="text-warning fw-bold ms-2"))

    # Explicit height: without it a responsive dcc.Graph inside a flex card collapses to a thin strip.
    fig.update_layout(height=GRAPH_HEIGHT, autosize=True)
    graph_kwargs = {"figure": fig, "config": {"displayModeBar": True, "responsive": True},
                    "style": {"height": f"{GRAPH_HEIGHT}px", "width": "100%"}}
    if graph_id:
        graph_kwargs["id"] = graph_id

    return dbc.Card([
        dbc.CardHeader(html.H5(title, className="mb-0 text-primary")),
        dbc.CardBody([
            dcc.Graph(**graph_kwargs),
            html.Small(badge_elements, className=("text-danger fw-semibold" if status == "sample" else "text-muted") + " d-block mt-2 border-top pt-2")
        ])
    ], className="h-100 shadow-sm")
