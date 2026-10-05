"""Fetch S15: Singapore Graduate Employment Survey (GES) from data.gov.sg (SG Open Data Licence v1.0)."""
import requests, pandas as pd
from etl._base import RAW_DIR, add_provenance, save_parquet, log

SOURCE_ID = "S15"
SOURCE_LICENSE = "Singapore Open Data Licence v1.0"
SOURCE_URL = "https://data.gov.sg/datasets/d_3c55210de27fcccda2ed0c63fdd2b352/view"
API_URL = "https://data.gov.sg/api/action/datastore_search?resource_id=d_3c55210de27fcccda2ed0c63fdd2b352&limit=5000"

def run() -> None:
    dest = RAW_DIR / "s15"; dest.mkdir(exist_ok=True)
    resp = requests.get(API_URL, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    records = data["result"]["records"]
    df = pd.DataFrame(records)
    df.to_csv(dest / "sg_ges.csv", index=False)
    # clean numeric columns
    for col in ["employment_rate_overall", "employment_rate_ft_perm", "basic_monthly_mean", "basic_monthly_median", "gross_monthly_mean", "gross_monthly_median", "gross_mthly_25_percentile", "gross_mthly_75_percentile"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", "").replace("na", None).replace("-", None), errors="coerce")
    df = add_provenance(df, SOURCE_ID, SOURCE_LICENSE, SOURCE_URL, "2013-2024")
    save_parquet(df, "s15_sg_ges")
    log.info("[S15] %d rows saved", len(df))

if __name__ == "__main__":
    run()
