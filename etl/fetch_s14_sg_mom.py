"""Fetch S14: Singapore MOM Employed Residents from data.gov.sg (SG Open Data Licence v1.0)."""
import requests, pandas as pd
from etl._base import RAW_DIR, add_provenance, save_parquet, log

SOURCE_ID = "S14"
SOURCE_LICENSE = "Singapore Open Data Licence v1.0"
SOURCE_URL = "https://data.gov.sg/datasets/d_576bb1f46eabb041d8d966030170ec6f/view"
API_URL = "https://data.gov.sg/api/action/datastore_search?resource_id=d_576bb1f46eabb041d8d966030170ec6f&limit=5000"

def run() -> None:
    dest = RAW_DIR / "s14"; dest.mkdir(exist_ok=True)
    resp = requests.get(API_URL, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    records = data["result"]["records"]
    df = pd.DataFrame(records)
    df.to_csv(dest / "sg_mom.csv", index=False)
    if "employed" in df.columns:
        df["employed"] = pd.to_numeric(df["employed"].astype(str).str.replace(",", ""), errors="coerce")
    df = add_provenance(df, SOURCE_ID, SOURCE_LICENSE, SOURCE_URL, "2010-2024")
    save_parquet(df, "s14_sg_mom")
    log.info("[S14] %d rows saved", len(df))

if __name__ == "__main__":
    run()
