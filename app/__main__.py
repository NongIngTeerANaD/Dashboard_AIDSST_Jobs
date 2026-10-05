"""Entry point: python -m app"""
import sys
import io

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "buffer"):
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from app.server import app as dash_app, server

if __name__ == "__main__":
    import os
    dash_app.run(debug=False, host="127.0.0.1", port=int(os.environ.get("PORT", "8077")))
