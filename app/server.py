"""Create Dash app instance and expose Flask server."""
import dash
import dash_bootstrap_components as dbc

dash_app = dash.Dash(
    __name__,
    use_pages=False,
    external_stylesheets=[dbc.themes.FLATLY],
    suppress_callback_exceptions=True,
    title="Dashboard: AI/DS/Stat Skill Mismatch",
)
server = dash_app.server

# Import layout and set on app
from app.layout import layout  # noqa: E402
dash_app.layout = layout

# Register all callbacks
import app.callbacks  # noqa: F401, E402

# Ensure callback map is registered onto app
dash_app._setup_server()

app = dash_app
