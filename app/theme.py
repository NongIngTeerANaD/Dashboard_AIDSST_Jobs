"""Plotly template matching the soft-UI style (white canvas, light grid, red/blue/purple palette)."""
import plotly.graph_objects as go
import plotly.io as pio

COLORWAY = ["#E02020", "#30A0E0", "#8B5CF6", "#22C55E", "#F59E0B", "#EC4899", "#14B8A6", "#64748B"]
FONT = "Inter, 'Noto Sans Thai', 'Segoe UI', sans-serif"

pio.templates["soft_ui"] = go.layout.Template(layout=dict(
    font=dict(family=FONT, size=12, color="#1B1B1F"),
    paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF", colorway=COLORWAY,
    title=dict(font=dict(size=13, color="#6b6b75")),
    xaxis=dict(gridcolor="#F0F0F0", linecolor="#F0F0F0", zerolinecolor="#F0F0F0", tickfont=dict(size=11, color="#8A8A93")),
    yaxis=dict(gridcolor="#F0F0F0", linecolor="#F0F0F0", zerolinecolor="#F0F0F0", tickfont=dict(size=11, color="#8A8A93")),
    legend=dict(font=dict(size=11, color="#6b6b75")),
    hoverlabel=dict(bgcolor="#111", font=dict(color="#fff", family=FONT), bordercolor="#111"),
))
pio.templates.default = "soft_ui"
