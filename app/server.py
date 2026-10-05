"""Create Dash app instance and expose Flask server."""
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    use_pages=False,
    external_stylesheets=[dbc.themes.FLATLY],
    suppress_callback_exceptions=True,
    title="Dashboard: AI/DS/Stat Skill Mismatch",
)
server = app.server  # Expose Flask server for deployment

# Import layout after app is created (avoids circular imports)
from app.layout import layout  # noqa: E402
app.layout = layout
