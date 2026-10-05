"""Callbacks for global filter store, reset button, and filter chips."""
from dash import Input, Output, State, callback, ctx, no_update
import dash_bootstrap_components as dbc
from dash import html

DEFAULT_FILTERS = {
    "country": ["TH", "SG", "US"],
    "year_start": 2020,
    "year_end": 2025,
    "degree": ["bachelor", "master"],
    "role": ["ai_ml", "data_science", "statistics", "data_analyst"],
}

@callback(
    Output("filter-country", "value"),
    Output("filter-year", "value"),
    Output("filter-degree", "value"),
    Output("filter-role", "value"),
    Input("btn-clear-all", "n_clicks"),
    prevent_initial_call=True,
)
def reset_filters(n_clicks):
    """Reset all filter inputs to default values when reset button is clicked."""
    return (
        DEFAULT_FILTERS["country"],
        [DEFAULT_FILTERS["year_start"], DEFAULT_FILTERS["year_end"]],
        DEFAULT_FILTERS["degree"],
        DEFAULT_FILTERS["role"],
    )

@callback(
    Output("store-filters", "data"),
    Input("filter-country", "value"),
    Input("filter-year", "value"),
    Input("filter-degree", "value"),
    Input("filter-role", "value"),
)
def update_store(country, year, degree, role):
    """Consolidate filter inputs into global store."""
    return {
        "country": country or [],
        "year_start": year[0] if (year and len(year) == 2) else 2020,
        "year_end": year[1] if (year and len(year) == 2) else 2025,
        "degree": degree or [],
        "role": role or [],
    }

@callback(
    Output("store-selection", "data"),
    Input("graph-t1-1", "clickData"),
    Input("graph-t3-2", "clickData"),
    Input("btn-clear-selection", "n_clicks"),
    State("store-selection", "data"),
    prevent_initial_call=True,
)
def update_selection(click_t1, click_t3, n_clear, current):
    """Cross-filter: clicking a program (T1-1 bar or T3-2 heatmap column) selects it globally."""
    from app.data_loader import data_store
    trig = ctx.triggered_id
    cur = (current or {}).get("program_id")
    if trig == "btn-clear-selection":
        return {"program_id": None}
    pid = None
    try:
        if trig == "graph-t1-1" and click_t1:
            pid = click_t1["points"][0]["customdata"][0]
        elif trig == "graph-t3-2" and click_t3:
            name = click_t3["points"][0]["x"]
            m = data_store.programs[data_store.programs["program_name_th"] == name]
            pid = m["program_id"].iloc[0] if not m.empty else None
    except (KeyError, IndexError, TypeError):
        return no_update
    if pid is None:
        return no_update
    return {"program_id": None if pid == cur else pid}  # click again to deselect

@callback(
    Output("filter-chips", "children"),
    Input("store-filters", "data"),
    Input("store-selection", "data"),
)
def render_chips(filters, selection):
    """Render active-filter chips."""
    if not filters:
        return []

    chips = []
    pid = (selection or {}).get("program_id")
    if pid:
        from app.data_loader import data_store
        m = data_store.programs[data_store.programs["program_id"] == pid]
        if not m.empty:
            chips.append(dbc.Badge(f"หลักสูตรที่เลือก: {m['program_name_th'].iloc[0]}", color="warning", text_color="dark", className="me-1 px-2 py-1"))
    countries = filters.get("country", [])
    if countries:
        chips.append(dbc.Badge(f"ประเทศ: {', '.join(countries)}", color="primary", className="me-1 px-2 py-1"))

    y_start = filters.get("year_start")
    y_end = filters.get("year_end")
    if y_start and y_end:
        chips.append(dbc.Badge(f"ปี: {y_start}–{y_end}", color="info", className="me-1 px-2 py-1"))

    degrees = filters.get("degree", [])
    if degrees:
        deg_labels = {"bachelor": "ป.ตรี", "master": "ป.โท", "phd": "ป.เอก"}
        deg_str = ", ".join([deg_labels.get(d, d) for d in degrees])
        chips.append(dbc.Badge(f"ระดับ: {deg_str}", color="success", className="me-1 px-2 py-1"))

    roles = filters.get("role", [])
    if roles:
        role_labels = {
            "ai_ml": "AI/ML",
            "data_science": "Data Sci",
            "statistics": "Stats",
            "data_analyst": "Analytics",
        }
        role_str = ", ".join([role_labels.get(r, r) for r in roles])
        chips.append(dbc.Badge(f"สายงาน: {role_str}", color="dark", className="me-1 px-2 py-1"))

    return chips
