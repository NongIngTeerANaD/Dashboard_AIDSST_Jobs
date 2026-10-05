"""Fetch raw data for S15 · Singapore GES.

Source: https://data.gov.sg/datasets/d_3c55210de27fcccda2ed0c63fdd2b352/view
License: SG Open Data Licence v1.0

This module only downloads; no scraping or HTML parsing.
Run with: python -m etl.run_all  (calls run() below)
"""
import logging
from pathlib import Path
from etl._base import RAW_DIR, download_file, log

SOURCE_ID = "S15"
# TODO: Set the actual download URL(s) for this source
DOWNLOAD_URLS: list[tuple[str, str]] = [
    # (url, local_filename)
    # ("https://example.com/data.csv", "raw_s15.csv"),
]


def run() -> None:
    """Download all files for S15 · Singapore GES."""
    dest_dir = RAW_DIR / "s15"
    dest_dir.mkdir(parents=True, exist_ok=True)
    if not DOWNLOAD_URLS:
        log.warning("[%s] No download URLs configured yet — skipping fetch.", SOURCE_ID)
        return
    for url, filename in DOWNLOAD_URLS:
        download_file(url, dest_dir / filename)


if __name__ == "__main__":
    run()
