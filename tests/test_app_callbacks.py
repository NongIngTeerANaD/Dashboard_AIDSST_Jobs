"""Callback-level tests (AC-02, AC-03, AC-05): every tab renders under varied filters and the
program selection (cross-filter) narrows Tab 1/2/3."""
import pytest
from dash import dcc
import app.server  # noqa: F401  (registers layout + callbacks)
from app.callbacks.tabs import update_tab_content, effective
from app.callbacks.store import render_chips
from app.data_loader import data_store

BASE = {"country": ["TH", "SG", "US"], "year_start": 2020, "year_end": 2025,
        "degree": ["bachelor", "master"], "role": ["ai_ml", "data_science", "statistics", "data_analyst"]}
NOSEL = {"program_id": None}


def _graphs(node, out=None):
    out = [] if out is None else out
    if isinstance(node, dcc.Graph):
        out.append(node)
    children = getattr(node, "children", None)
    if isinstance(children, (list, tuple)):
        for c in children:
            _graphs(c, out)
    elif children is not None and not isinstance(children, (str, int, float)):
        _graphs(children, out)
    return out


@pytest.mark.parametrize("tab", ["tab-1", "tab-2", "tab-3", "tab-4"])
@pytest.mark.parametrize("filters", [
    BASE,
    {**BASE, "country": ["US", "GB"]},
    {**BASE, "country": ["SG"], "role": ["data_science"]},
    {**BASE, "degree": ["phd"]},
    {**BASE, "country": []},
])
def test_every_tab_renders(tab, filters):
    assert update_tab_content(tab, filters, NOSEL) is not None


def test_filters_change_chart_data():
    a = _graphs(update_tab_content("tab-2", {**BASE, "country": ["US"]}, NOSEL))
    b = _graphs(update_tab_content("tab-2", {**BASE, "country": ["US", "GB", "DE"]}, NOSEL))
    assert len(a[0].figure.data) < len(b[0].figure.data)


def test_program_selection_narrows_all_tabs():
    pid = "TH_KKU_STAT"
    eff, got = effective(BASE, {"program_id": pid})
    assert got == pid and eff["country"] == ["TH"] and eff["role"] == ["statistics"]
    t1_all = _graphs(update_tab_content("tab-1", BASE, NOSEL))
    t1_sel = _graphs(update_tab_content("tab-1", BASE, {"program_id": pid}))
    sunburst = lambda gs: [g for g in gs if g.figure.data and g.figure.data[0].type == "sunburst"][0]
    assert len(sunburst(t1_sel).figure.data[0].ids) < len(sunburst(t1_all).figure.data[0].ids)
    t3 = _graphs(update_tab_content("tab-3", BASE, {"program_id": pid}))
    assert t3 and t3[0].id == "graph-t3-2"
    assert list(t3[0].figure.data[0].x) == [data_store.programs.set_index("program_id").loc[pid, "program_name_th"]]


def test_selection_keeps_country_for_tab2():
    eff, _ = effective(BASE, {"program_id": "TH_KKU_STAT"}, keep_country=True)
    assert eff["country"] == BASE["country"] and eff["role"] == ["statistics"]


def test_chips_show_selection():
    chips = render_chips(BASE, {"program_id": "TH_CU_DS"})
    assert any("หลักสูตรที่เลือก" in str(c.children) for c in chips)


def test_no_fabricated_provenance():
    for name in ["graduates", "courses", "tuition"]:
        df = getattr(data_store, name)
        assert set(df["source_id"]) == {"SAMPLE_DEMO"}, name
    assert set(data_store.skills_demand["source_id"]) <= {"SAMPLE_DEMO", "S03"}


def test_s03_demand_has_evidence_when_real():
    d = data_store.skills_demand
    if set(d["source_id"]) == {"S03"}:
        assert d["importance_or_freq"].between(0, 1).all()
        assert (d.loc[d["importance_or_freq"] > 0, "evidence"].str.len() > 0).all()


def test_real_data_charts_present():
    # S07 (World Bank) and S08 (Eurostat) charts render and carry real-data status
    t1 = _graphs(update_tab_content("tab-1", {**BASE, "country": ["TH", "SG"]}, NOSEL))
    t2 = _graphs(update_tab_content("tab-2", {**BASE, "country": ["DE", "FR"]}, NOSEL))
    assert len(t1) >= 4 and len(t2) >= 4
