"""Create Dash app instance and expose Flask server."""
import os
import dash
import dash_bootstrap_components as dbc
import app.theme  # noqa: F401  (registers the default Plotly template)

_ASSETS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")

dash_app = dash.Dash(
    __name__,
    assets_folder=_ASSETS,
    use_pages=False,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    suppress_callback_exceptions=True,
    title="AIDSST Jobs · Skill Mismatch Dashboard",
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
