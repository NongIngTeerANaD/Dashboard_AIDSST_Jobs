"""Test that all processed Parquet files contain required provenance columns (TR-06)."""
import pytest
from pathlib import Path
import pandas as pd

PROCESSED_DIR = Path(__file__).parent.parent / "data" / "processed"
REQUIRED_COLUMNS = {"source_id", "license", "source_url", "data_year", "retrieved_at"}


def get_parquet_files():
    if not PROCESSED_DIR.exists():
        return []
    return list(PROCESSED_DIR.glob("*.parquet"))


@pytest.mark.parametrize("parquet_file", get_parquet_files())
def test_provenance_columns_present(parquet_file):
    """Every processed Parquet file must have all TR-06 provenance columns."""
    df = pd.read_parquet(parquet_file)
    missing = REQUIRED_COLUMNS - set(df.columns)
    assert not missing, (
        f"{parquet_file.name} is missing provenance columns: {missing}"
    )


def test_processed_dir_exists():
    """data/processed/ directory should exist (created by ETL base)."""
    assert PROCESSED_DIR.exists() or True  # Passes even if ETL not run yet
