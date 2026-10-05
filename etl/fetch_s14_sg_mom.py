"""Fetch raw data for S14 · Singapore MOM Employment.

Source: https://data.gov.sg/datasets/d_576bb1f46eabb041d8d966030170ec6f/view
License: SG Open Data Licence v1.0

This module only downloads; no scraping or HTML parsing.
Run with: python -m etl.run_all  (calls run() below)
"""
import logging
from pathlib import Path
from etl._base import RAW_DIR, download_file, log

SOURCE_ID = "S14"
# TODO: Set the actual download URL(s) for this source
DOWNLOAD_URLS: list[tuple[str, str]] = [
    # (url, local_filename)
    # ("https://example.com/data.csv", "raw_s14.csv"),
]


def run() -> None:
    """Download all files for S14 · Singapore MOM Employment."""
    dest_dir = RAW_DIR / "s14"
    dest_dir.mkdir(parents=True, exist_ok=True)
    if not DOWNLOAD_URLS:
        log.warning("[%s] No download URLs configured yet — skipping fetch.", SOURCE_ID)
        return
    for url, filename in DOWNLOAD_URLS:
        download_file(url, dest_dir / filename)


if __name__ == "__main__":
    run()
