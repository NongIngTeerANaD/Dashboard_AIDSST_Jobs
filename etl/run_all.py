"""Run the full ETL pipeline in sequence.

Usage:
    python -m etl.run_all

Each fetch_*.py downloads raw data; each clean_*.py produces a
processed Parquet file in data/processed/ with required provenance
columns (TR-06): source_id, license, source_url, data_year, retrieved_at.
"""
import importlib
import logging
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

# Ordered list: (fetch_module, clean_module, source_id)
PIPELINE: list[tuple[str, str, str]] = [
    ("etl.fetch_s01_indeed_postings",  "etl.clean_s01", "S01"),
    ("etl.fetch_s01_sector",          "etl.clean_s01_sector", "S01-sector"),
    ("etl.fetch_s02_indeed_ai",        "etl.clean_s02", "S02"),
    ("etl.fetch_s03_onet",             "etl.clean_s03", "S03"),
    ("etl.fetch_s05_stackoverflow",    "etl.clean_s05", "S05"),
    ("etl.fetch_s06_ilostat",          "etl.clean_s06", "S06"),
    ("etl.fetch_s07_worldbank",        "etl.clean_s07", "S07"),
    ("etl.fetch_s08_eurostat_ict",     "etl.clean_s08", "S08"),
    ("etl.fetch_s09_eurostat_grad",    "etl.clean_s09", "S09"),
    ("etl.fetch_s10_bls_oews",         "etl.clean_s10", "S10"),
    ("etl.fetch_s11_ons_ashe",         "etl.clean_s11", "S11"),
    ("etl.fetch_s12_cea_thai",         "etl.clean_s12", "S12"),
    ("etl.fetch_s13_nso_thai",         "etl.clean_s13", "S13"),
    ("etl.fetch_s14_sg_mom",           "etl.clean_s14", "S14"),
    ("etl.fetch_s15_sg_ges",           "etl.clean_s15", "S15"),
]


def run():
    errors = []
    for fetch_mod, clean_mod, source_id in PIPELINE:
        for step, mod_name in [("fetch", fetch_mod), ("clean", clean_mod)]:
            log.info("[%s] %s starting…", source_id, step)
            try:
                mod = importlib.import_module(mod_name)
                mod.run()
                log.info("[%s] %s OK", source_id, step)
            except Exception as exc:
                log.error("[%s] %s FAILED: %s", source_id, step, exc)
                errors.append((source_id, step, exc))

    if errors:
        log.warning("Pipeline completed with %d error(s):", len(errors))
        for sid, step, exc in errors:
            log.warning("  [%s] %s: %s", sid, step, exc)
        sys.exit(1)
    else:
        log.info("Pipeline completed successfully.")


if __name__ == "__main__":
    run()
