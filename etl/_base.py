"""Shared ETL utilities: provenance helpers, path constants, download helpers.

All ETL scripts must call add_provenance() on their output DataFrames
to satisfy TR-06: every table needs source_id, license, source_url,
data_year, retrieved_at columns.
"""
import hashlib
import logging
import os
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

log = logging.getLogger(__name__)

# Project-level paths
ROOT = Path(__file__).parent.parent
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
CURATED_DIR = ROOT / "data" / "curated"

# Ensure directories exist
RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
CURATED_DIR.mkdir(parents=True, exist_ok=True)


def add_provenance(
    df: pd.DataFrame,
    source_id: str,
    license_name: str,
    source_url: str,
    data_year: int | str,
) -> pd.DataFrame:
    """Add required provenance columns (TR-06)."""
    df = df.copy()
    df["source_id"] = source_id
    df["license"] = license_name
    df["source_url"] = source_url
    df["data_year"] = str(data_year)
    df["retrieved_at"] = datetime.now(tz=timezone.utc).isoformat()
    return df


def download_file(url: str, dest: Path, force: bool = False) -> Path:
    """Download a file to dest if it doesn't already exist (idempotent, NFR-05)."""
    if dest.exists() and not force:
        log.info("Cache hit: %s", dest.name)
        return dest
    log.info("Downloading %s -> %s", url, dest.name)
    resp = requests.get(url, stream=True, timeout=120)
    resp.raise_for_status()
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "wb") as f:
        for chunk in resp.iter_content(chunk_size=65536):
            f.write(chunk)
    _write_checksum(dest)
    return dest


def _write_checksum(path: Path) -> None:
    """Write SHA-256 checksum sidecar file (NFR-05)."""
    sha256 = hashlib.sha256(path.read_bytes()).hexdigest()
    path.with_suffix(path.suffix + ".sha256").write_text(sha256)


def save_parquet(df: pd.DataFrame, name: str) -> Path:
    """Save DataFrame to data/processed/<name>.parquet."""
    out = PROCESSED_DIR / f"{name}.parquet"
    df.to_parquet(out, index=False)
    log.info("Saved %s (%d rows)", out.name, len(df))
    return out
