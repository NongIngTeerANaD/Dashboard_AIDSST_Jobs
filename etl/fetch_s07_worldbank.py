"""Fetch S07: World Bank SL.UEM.ADVN.ZS via REST API (no key required)."""
import logging
import requests
import pandas as pd
from etl._base import RAW_DIR, add_provenance, save_parquet, log

SOURCE_ID = "S07"
SOURCE_LICENSE = "CC BY 4.0"
SOURCE_URL = "https://data.worldbank.org/indicator/SL.UEM.ADVN.ZS"
COUNTRIES = "THA;SGP;IND;USA;GBR;DEU;FRA;AUS"
API_URL = (
    f"https://api.worldbank.org/v2/country/{COUNTRIES}"
    f"/indicator/SL.UEM.ADVN.ZS?format=json&date=2010:2025&per_page=200"
)

def run() -> None:
    resp = requests.get(API_URL, timeout=30)
    resp.raise_for_status()
    payload = resp.json()
    records = payload[1] if len(payload) > 1 else []
    rows = []
    for r in records:
        if r.get("value") is not None:
            rows.append({
                "country": r["country"]["value"],
                "country_code": r["countryiso3code"],
                "year": int(r["date"]),
                "unemployment_rate_pct": float(r["value"]),
            })
    df = pd.DataFrame(rows)
    df = add_provenance(df, SOURCE_ID, SOURCE_LICENSE, SOURCE_URL, "2010-2025")
    dest = RAW_DIR / "s07"; dest.mkdir(exist_ok=True)
    df.to_csv(dest / "worldbank_uem_advn.csv", index=False)
    save_parquet(df, "s07_uem_advanced")
    log.info("[S07] %d rows fetched", len(df))

if __name__ == "__main__":
    run()
