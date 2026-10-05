"""Export a static HTML snapshot of all tabs (double-click to open, no server).
Run:  python export_static.py   ->  dashboard_snapshot.html
Static = default filters, no cross-filtering. Use `python -m app` for the interactive version."""
from dash import dcc
import app.server  # noqa: F401
from app.callbacks.tabs import update_tab_content
from app.layout import DEFAULT_FILTERS

def graphs(node, out):
    if isinstance(node, dcc.Graph):
        out.append(node.figure)
    ch = getattr(node, "children", None)
    if isinstance(ch, (list, tuple)):
        for c in ch:
            graphs(c, out)
    elif ch is not None and not isinstance(ch, (str, int, float)):
        graphs(ch, out)
    return out

TABS = [("tab-1", "Tab 1 · ผู้สำเร็จการศึกษา & Skill ที่เรียน"), ("tab-2", "Tab 2 · ตลาดงาน & Skill ที่ต้องการ"),
        ("tab-3", "Tab 3 · Skill Mismatch")]
parts, first = [], True
for tid, title in TABS:
    parts.append(f"<h2>{title}</h2><div class='grid'>")
    for fig in graphs(update_tab_content(tid, DEFAULT_FILTERS, {"program_id": None}), []):
        parts.append("<div class='card'>" + fig.to_html(full_html=False, include_plotlyjs=True if first else False) + "</div>")
        first = False
    parts.append("</div>")
page = ("<!doctype html><html lang='th'><head><meta charset='utf-8'><title>Dashboard Snapshot</title>"
        "<style>body{font-family:Segoe UI,Tahoma,sans-serif;margin:24px;background:#f6f7f9}"
        ".grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(560px,1fr));gap:16px}"
        ".card{background:#fff;border-radius:8px;padding:8px;box-shadow:0 1px 4px #0002}"
        ".warn{background:#fff3cd;padding:10px;border-radius:6px}</style></head><body>"
        "<h1>Dashboard วิเคราะห์ตลาดงานและ Skill Mismatch (snapshot)</h1>"
        "<p class='warn'>⚠️ ข้อมูลผู้จบ/รายวิชา/ค่าเทอม/ความต้องการ skill และ Tab 3 เป็นตัวอย่างสาธิต ไม่ใช่ข้อมูลจริง "
        "ข้อมูลจริง: Indeed (S01/S02) และสิงคโปร์ (S14/S15)</p>" + "".join(parts) + "</body></html>")
open("dashboard_snapshot.html", "w", encoding="utf-8").write(page)
print("wrote dashboard_snapshot.html")
