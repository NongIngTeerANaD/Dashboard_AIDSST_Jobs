"""Clean and standardize raw data for S08 · Eurostat isoc_sks_itspt.

Produces: data/processed/s08_*.parquet with provenance columns (TR-06).
"""
import logging
from pathlib import Path
import pandas as pd
from etl._base import RAW_DIR, PROCESSED_DIR, add_provenance, save_parquet, log

SOURCE_ID = "S08"
SOURCE_LICENSE = "Eurostat reuse policy"
SOURCE_URL = "https://ec.europa.eu/eurostat/"
RAW_SUBDIR = RAW_DIR / "s08"


def run() -> None:
    """Read raw files, clean, add provenance, save to Parquet."""
    raw_files = list(RAW_SUBDIR.glob("*.csv"))
    if not raw_files:
        log.warning("[%s] No raw CSV files found in %s — skipping clean.", SOURCE_ID, RAW_SUBDIR)
        return

    dfs = []
    for f in raw_files:
        try:
            df = pd.read_csv(f, low_memory=False)
            # TODO: rename columns, filter rows, cast dtypes
            dfs.append(df)
        except Exception as exc:
            log.error("[%s] Failed to read %s: %s", SOURCE_ID, f.name, exc)

    if not dfs:
        return

    combined = pd.concat(dfs, ignore_index=True)
    # TODO: extract data_year from data or filename
    data_year = "unknown"
    combined = add_provenance(combined, SOURCE_ID, SOURCE_LICENSE, SOURCE_URL, data_year)
    save_parquet(combined, "s08")


if __name__ == "__main__":
    run()
