"""Callbacks for rendering Tab 1, Tab 2, and Tab 3 based on global filters."""
from dash import Input, Output, callback, html
import dash_bootstrap_components as dbc
from app.charts.tab1_charts import (
    build_t1_1_graduates,
    build_t1_2_courses,
    build_t1_3_employment,
    build_t1_4_tuition,
)
from app.charts.tab2_charts import (
    build_t2_1_postings,
    build_t2_2_skills,
    build_t2_3_employers,
    build_t2_4_salary,
)
from app.charts.tab3_charts import (
    compute_mismatch_table,
    build_t3_2_heatmap,
    build_t3_3_quadrant,
    build_t3_4_top_gaps,
    build_t3_5_coverage,
)

@callback(
    Output("tab1-content", "children"),
    Input("store-filters", "data"),
)
def render_tab1(filters):
    if not filters:
        return html.Div("กำลังโหลดข้อมูล...", className="text-center py-4 text-muted")
    countries = filters.get("country", [])
    year_range = [filters.get("year_start", 2020), filters.get("year_end", 2025)]
    degrees = filters.get("degree", [])
    roles = filters.get("role", [])

    return dbc.Container([
        dbc.Row([
            dbc.Col(build_t1_1_graduates(countries, year_range, degrees, roles), lg=6, className="mb-4"),
            dbc.Col(build_t1_2_courses(countries, degrees, roles), lg=6, className="mb-4"),
        ]),
        dbc.Row([
            dbc.Col(build_t1_3_employment(countries), lg=6, className="mb-4"),
            dbc.Col(build_t1_4_tuition(countries, degrees, roles), lg=6, className="mb-4"),
        ])
    ], fluid=True, className="p-0")

@callback(
    Output("tab2-content", "children"),
    Input("store-filters", "data"),
)
def render_tab2(filters):
    if not filters:
        return html.Div("กำลังโหลดข้อมูล...", className="text-center py-4 text-muted")
    countries = filters.get("country", [])
    year_range = [filters.get("year_start", 2020), filters.get("year_end", 2025)]
    roles = filters.get("role", [])

    return dbc.Container([
        dbc.Row([
            dbc.Col(build_t2_1_postings(countries, year_range), lg=6, className="mb-4"),
            dbc.Col(build_t2_2_skills(roles), lg=6, className="mb-4"),
        ]),
        dbc.Row([
            dbc.Col(build_t2_3_employers(countries), lg=6, className="mb-4"),
            dbc.Col(build_t2_4_salary(countries), lg=6, className="mb-4"),
        ])
    ], fluid=True, className="p-0")

@callback(
    Output("tab3-content", "children"),
    Input("store-filters", "data"),
)
def render_tab3(filters):
    if not filters:
        return html.Div("กำลังโหลดข้อมูล...", className="text-center py-4 text-muted")
    countries = filters.get("country", [])
    degrees = filters.get("degree", [])
    roles = filters.get("role", [])

    mismatch_df = compute_mismatch_table(countries, degrees, roles)

    return dbc.Container([
        dbc.Row([
            dbc.Col(build_t3_2_heatmap(mismatch_df), lg=6, className="mb-4"),
            dbc.Col(build_t3_3_quadrant(mismatch_df), lg=6, className="mb-4"),
        ]),
        dbc.Row([
            dbc.Col(build_t3_4_top_gaps(mismatch_df), lg=6, className="mb-4"),
            dbc.Col(build_t3_5_coverage(mismatch_df), lg=6, className="mb-4"),
        ])
    ], fluid=True, className="p-0")
