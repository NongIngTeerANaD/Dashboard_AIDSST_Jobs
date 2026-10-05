"""Fetch raw data for S05 · Stack Overflow Survey 2025.

Source: https://survey.stackoverflow.co/
License: ODbL 1.0

This module only downloads; no scraping or HTML parsing.
Run with: python -m etl.run_all  (calls run() below)
"""
import logging
from pathlib import Path
from etl._base import RAW_DIR, download_file, log

SOURCE_ID = "S05"
# TODO: Set the actual download URL(s) for this source
DOWNLOAD_URLS: list[tuple[str, str]] = [
    # (url, local_filename)
    # ("https://example.com/data.csv", "raw_s05.csv"),
]


def run() -> None:
    """Download all files for S05 · Stack Overflow Survey 2025."""
    dest_dir = RAW_DIR / "s05"
    dest_dir.mkdir(parents=True, exist_ok=True)
    if not DOWNLOAD_URLS:
        log.warning("[%s] No download URLs configured yet — skipping fetch.", SOURCE_ID)
        return
    for url, filename in DOWNLOAD_URLS:
        download_file(url, dest_dir / filename)


if __name__ == "__main__":
    run()
