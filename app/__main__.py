"""Entry point: python -m app"""
from app.server import app, server  # noqa: F401

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=8050)
