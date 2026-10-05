"""Callbacks for rendering active tab based on global filters."""
from dash import Input, Output, State, callback, html, dcc
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
from app.data_loader import data_store
from app.pages.sources import build_sources_page
from app.charts.tab3_charts import (
    compute_mismatch_table,
    build_t3_2_heatmap,
    build_t3_3_quadrant,
    build_t3_4_top_gaps,
    build_t3_5_coverage,
)

def effective(filters: dict, selection: dict, keep_country: bool = False):
    """Apply the selected program (cross-filter) on top of global filters.

    Returns (filters_for_other_tabs, program_id). Tab 2/3 narrow to the program's
    country / degree / role family; Tab 1 charts narrow to the program itself.
    """
    pid = (selection or {}).get("program_id")
    if not pid:
        return filters, None
    m = data_store.programs[data_store.programs["program_id"] == pid]
    if m.empty:
        return filters, None
    p = m.iloc[0]
    eff = dict(filters)
    if not keep_country:
        eff["country"] = [p["country"]]
    eff["degree"] = [p["degree_level"]]
    eff["role"] = [p["role_family"]]
    return eff, pid

def render_tab1_view(filters: dict, selection: dict = None):
    filters_sel, pid = effective(filters, selection)
    countries = filters.get("country", ["TH", "SG", "US"])
    year_range = [filters.get("year_start", 2020), filters.get("year_end", 2025)]
    degrees = filters.get("degree", ["bachelor", "master"])
    roles = filters.get("role", ["ai_ml", "data_science", "statistics", "data_analyst"])

    return dbc.Container([
        dbc.Row([
            dbc.Col(build_t1_1_graduates(countries, year_range, degrees, roles, highlight=pid), lg=6, className="mb-4"),
            dbc.Col(build_t1_2_courses(countries, degrees, roles, program_id=pid), lg=6, className="mb-4"),
        ]),
        dbc.Row([
            dbc.Col(build_t1_3_employment(filters_sel.get("country", countries)), lg=6, className="mb-4"),
            dbc.Col(build_t1_4_tuition(countries, degrees, roles, program_id=pid), lg=6, className="mb-4"),
        ])
    ], fluid=True, className="p-0")

def render_tab2_view(filters: dict, selection: dict = None):
    # Tab 2: narrow to the program role family only (open job-market data does not exist for every country)
    filters, _ = effective(filters, selection, keep_country=True)
    countries = filters.get("country", ["TH", "SG", "US"])
    year_range = [filters.get("year_start", 2020), filters.get("year_end", 2025)]
    roles = filters.get("role", ["ai_ml", "data_science", "statistics", "data_analyst"])

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

def render_tab3_view(filters: dict, selection: dict = None):
    countries = filters.get("country", ["TH", "SG", "US"])
    degrees = filters.get("degree", ["bachelor", "master"])
    roles = filters.get("role", ["ai_ml", "data_science", "statistics", "data_analyst"])

    mismatch_df = compute_mismatch_table(countries, degrees, roles)
    filters, pid = effective(filters, selection)
    if pid:
        countries, degrees, roles = filters["country"], filters["degree"], filters["role"]
        mismatch_df = compute_mismatch_table(countries, degrees, roles, program_id=pid)

    return dbc.Container([
        dbc.Row(dbc.Col(dbc.Button("⬇ ดาวน์โหลดตาราง Gap Score (CSV)", id="btn-download-mismatch", color="primary", outline=True, size="sm", className="mb-3"))),
        dbc.Row([
            dbc.Col(build_t3_2_heatmap(mismatch_df), lg=6, className="mb-4"),
            dbc.Col(build_t3_3_quadrant(mismatch_df), lg=6, className="mb-4"),
        ]),
        dbc.Row([
            dbc.Col(build_t3_4_top_gaps(mismatch_df), lg=6, className="mb-4"),
            dbc.Col(build_t3_5_coverage(mismatch_df), lg=6, className="mb-4"),
        ])
    ], fluid=True, className="p-0")

@callback(
    Output("tab-content", "children"),
    Input("main-tabs", "active_tab"),
    Input("store-filters", "data"),
    Input("store-selection", "data"),
)
def update_tab_content(active_tab, filters, selection):
    if not filters:
        filters = {
            "country": ["TH", "SG", "US"],
            "year_start": 2020,
            "year_end": 2025,
            "degree": ["bachelor", "master"],
            "role": ["ai_ml", "data_science", "statistics", "data_analyst"],
        }

    if active_tab == "tab-1":
        return render_tab1_view(filters, selection)
    elif active_tab == "tab-3":
        return render_tab3_view(filters, selection)
    elif active_tab == "tab-4":
        return build_sources_page()
    else:  # tab-2 default
        return render_tab2_view(filters, selection)

@callback(
    Output("download-mismatch", "data"),
    Input("btn-download-mismatch", "n_clicks"),
    State("store-filters", "data"),
    State("store-selection", "data"),
    prevent_initial_call=True,
)
def download_mismatch(n_clicks, filters, selection):
    """Export the currently filtered Gap Score table (data of the Tab 3 charts) as CSV."""
    if not n_clicks or not filters:
        return None
    eff, pid = effective(filters, selection)
    df = compute_mismatch_table(eff["country"], eff["degree"], eff["role"], program_id=pid)
    if df.empty:
        return None
    df = df.assign(data_status="SAMPLE_DEMO (not real data)")
    return dcc.send_data_frame(df.to_csv, "skill_gap_filtered.csv", index=False, encoding="utf-8-sig")
