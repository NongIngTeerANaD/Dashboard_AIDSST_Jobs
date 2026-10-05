"""Fetch S01 (sector level): Indeed Job Postings Index by occupational sector (CC BY 4.0).

Real demand series per sector, e.g. 'Software Development' and 'Mathematics'
(Indeed's own grouping; title examples in sector-job-title-examples.csv).
Index is relative (base 1 Feb 2020 = 100), not absolute posting counts.
"""
import io
import requests
import pandas as pd
from etl._base import RAW_DIR, add_provenance, save_parquet, log

SOURCE_ID = "S01"
SOURCE_LICENSE = "CC BY 4.0"
SOURCE_URL = "https://github.com/hiring-lab/job_postings_tracker"
BASE = "https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master"
COUNTRIES = ["US", "GB", "DE", "FR", "AU"]
# Sectors relevant to AI / Data Science / Statistics careers (names as in Indeed's files)
KEEP_SECTORS = ["Software Development", "Data & Analytics", "Scientific Research & Development", "Banking & Finance"]


def run() -> None:
    dest = RAW_DIR / "s01_sector"
    dest.mkdir(exist_ok=True)
    frames = []
    for cc in COUNTRIES:
        try:
            r = requests.get(f"{BASE}/{cc}/job_postings_by_sector_{cc}.csv", timeout=120)
            r.raise_for_status()
            (dest / f"sector_{cc}.csv").write_bytes(r.content)
            df = pd.read_csv(io.BytesIO(r.content))
            df = df[(df["variable"] == "total postings")]
            frames.append(df)
            log.info("[S01-sector] %s: %d rows", cc, len(df))
        except Exception as exc:  # keep going if one country fails
            log.warning("[S01-sector] %s failed: %s", cc, exc)
    try:
        r = requests.get(f"{BASE}/sector-job-title-examples.csv", timeout=60)
        r.raise_for_status()
        (dest / "sector-job-title-examples.csv").write_bytes(r.content)
    except Exception as exc:
        log.warning("[S01-sector] title examples failed: %s", exc)
    if not frames:
        return
    all_ = pd.concat(frames, ignore_index=True)
    log.info("[S01-sector] sectors: %s", sorted(all_["display_name"].unique()))
    all_ = all_[all_["display_name"].isin(KEEP_SECTORS)].rename(columns={"jobcountry": "country_code"})
    all_ = add_provenance(all_, SOURCE_ID, SOURCE_LICENSE, SOURCE_URL, "2020-2026")
    save_parquet(all_, "s01_sector_postings")


if __name__ == "__main__":
    run()
