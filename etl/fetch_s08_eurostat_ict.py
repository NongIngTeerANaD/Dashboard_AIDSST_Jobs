"""Fetch raw data for S08 · Eurostat isoc_sks_itspt.

Source: https://ec.europa.eu/eurostat/
License: Eurostat reuse policy

This module only downloads; no scraping or HTML parsing.
Run with: python -m etl.run_all  (calls run() below)
"""
import logging
from pathlib import Path
from etl._base import RAW_DIR, download_file, log

SOURCE_ID = "S08"
# TODO: Set the actual download URL(s) for this source
DOWNLOAD_URLS: list[tuple[str, str]] = [
    # (url, local_filename)
    # ("https://example.com/data.csv", "raw_s08.csv"),
]


def run() -> None:
    """Download all files for S08 · Eurostat isoc_sks_itspt."""
    dest_dir = RAW_DIR / "s08"
    dest_dir.mkdir(parents=True, exist_ok=True)
    if not DOWNLOAD_URLS:
        log.warning("[%s] No download URLs configured yet — skipping fetch.", SOURCE_ID)
        return
    for url, filename in DOWNLOAD_URLS:
        download_file(url, dest_dir / filename)


if __name__ == "__main__":
    run()
