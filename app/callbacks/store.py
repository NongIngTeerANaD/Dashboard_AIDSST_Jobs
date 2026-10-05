"""Callbacks for global filter store and URL sync (FR-G2, FR-G7)."""
from dash import Input, Output, State, callback, ALL
import json
from urllib.parse import urlencode, parse_qs, urlparse


@callback(
    Output("store-filters", "data"),
    Input("filter-country", "value"),
    Input("filter-year", "value"),
    Input("filter-degree", "value"),
    Input("filter-role", "value"),
)
def update_store(country, year, degree, role):
    """Consolidate all filter inputs into the global store."""
    return {
        "country": country or [],
        "year_start": year[0] if year else 2020,
        "year_end": year[1] if year else 2025,
        "degree": degree or [],
        "role": role or [],
    }


@callback(
    Output("filter-chips", "children"),
    Input("store-filters", "data"),
)
def render_chips(filters):
    """Render active-filter chips (FR-G4)."""
    if not filters:
        return []
    from dash import html
    import dash_bootstrap_components as dbc

    chips = []
    if filters.get("country"):
        chips.append(dbc.Badge(f"ประเทศ: {', '.join(filters['country'])}",
                               color="primary", className="me-1"))
    if filters.get("year_start") or filters.get("year_end"):
        chips.append(dbc.Badge(
            f"ปี: {filters.get('year_start', '?')}–{filters.get('year_end', '?')}",
            color="info", className="me-1"))
    if filters.get("degree"):
        chips.append(dbc.Badge(f"ระดับ: {', '.join(filters['degree'])}",
                               color="success", className="me-1"))
    if filters.get("role"):
        chips.append(dbc.Badge(f"สายงาน: {', '.join(filters['role'])}",
                               color="warning", text_color="dark", className="me-1"))
    return chips
