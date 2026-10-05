"""Fetch S01: Indeed Job Postings Index from GitHub (CC BY 4.0)."""
import requests, pandas as pd, io
from etl._base import RAW_DIR, add_provenance, save_parquet, log

SOURCE_ID = "S01"
SOURCE_LICENSE = "CC BY 4.0"
SOURCE_URL = "https://github.com/hiring-lab/job_postings_tracker"

COUNTRY_FILES = {
    "US": "https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/US/aggregate_job_postings_US.csv",
    "GB": "https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/GB/aggregate_job_postings_GB.csv",
    "DE": "https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/DE/aggregate_job_postings_DE.csv",
    "FR": "https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/FR/aggregate_job_postings_FR.csv",
    "AU": "https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master/AU/aggregate_job_postings_AU.csv",
}

def run() -> None:
    dest = RAW_DIR / "s01"; dest.mkdir(exist_ok=True)
    dfs = []
    for country, url in COUNTRY_FILES.items():
        try:
            resp = requests.get(url, timeout=30)
            resp.raise_for_status()
            df = pd.read_csv(io.StringIO(resp.text))
            df["country_code"] = country
            df.to_csv(dest / f"indeed_postings_{country}.csv", index=False)
            dfs.append(df)
            log.info("[S01] %s: %d rows", country, len(df))
        except Exception as e:
            log.warning("[S01] %s failed: %s", country, e)
    if dfs:
        combined = pd.concat(dfs, ignore_index=True)
        combined = add_provenance(combined, SOURCE_ID, SOURCE_LICENSE, SOURCE_URL, "2020-2026")
        save_parquet(combined, "s01_job_postings")

if __name__ == "__main__":
    run()
