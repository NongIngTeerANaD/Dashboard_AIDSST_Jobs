"""Fetch S08: Eurostat ICT specialists in employment (isoc_sks_itspt)."""
import requests, pandas as pd
from etl._base import RAW_DIR, add_provenance, save_parquet, log

SOURCE_ID = "S08"
SOURCE_LICENSE = "Eurostat reuse policy"
SOURCE_URL = "https://ec.europa.eu/eurostat/web/main/help/copyright-notice"
API_URL = (
    "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/isoc_sks_itspt"
    "?format=JSON&unit=PC_EMP&lang=en"
)

def run() -> None:
    resp = requests.get(API_URL, timeout=60)
    resp.raise_for_status()
    j = resp.json()
    dims = j["dimension"]
    geo_cats = dims["geo"]["category"]
    time_cats = dims["time"]["category"]
    geos = {v: k for k, v in geo_cats["index"].items()}
    times = {v: k for k, v in time_cats["index"].items()}
    values = j["value"]
    n_geo = len(geos); n_time = len(times)
    rows = []
    for idx_str, val in values.items():
        idx = int(idx_str)
        g = idx // n_time; t = idx % n_time
        rows.append({"country_code": geos[g], "year": int(times[t]), "ict_specialists_pct": val})
    df = pd.DataFrame(rows)
    df = add_provenance(df, SOURCE_ID, SOURCE_LICENSE, SOURCE_URL, "2004-2025")
    dest = RAW_DIR / "s08"; dest.mkdir(exist_ok=True)
    df.to_csv(dest / "eurostat_ict.csv", index=False)
    save_parquet(df, "s08_ict_specialists")
    log.info("[S08] %d rows fetched", len(df))

if __name__ == "__main__":
    run()
