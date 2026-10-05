"""Fetch S09: Eurostat graduates by field (educ_uoe_grad02) - Math/Stat/ICT fields."""
import requests, pandas as pd
from etl._base import RAW_DIR, add_provenance, save_parquet, log

SOURCE_ID = "S09"
SOURCE_LICENSE = "Eurostat reuse policy"
SOURCE_URL = "https://ec.europa.eu/eurostat/web/main/help/copyright-notice"
# Fields: F0541=Math, F0542=Statistics, F0613=Software/app dev
FIELDS = ["F0541", "F0542", "F0613", "F061"]
LEVELS = ["ED6", "ED7", "ED8"]   # Bachelor, Master, PhD

def _fetch_field_level(field: str, level: str) -> pd.DataFrame:
    url = (
        "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_grad02"
        f"?format=JSON&lang=en&isced11={level}&fieldedu={field}&sex=T"
    )
    resp = requests.get(url, timeout=60)
    if resp.status_code != 200:
        log.warning("[S09] HTTP %s for field=%s level=%s", resp.status_code, field, level)
        return pd.DataFrame()
    j = resp.json()
    dims = j["dimension"]
    geo_idx = {v: k for k, v in dims["geo"]["category"]["index"].items()}
    time_idx = {v: k for k, v in dims["time"]["category"]["index"].items()}
    values = j["value"]
    n_time = len(time_idx)
    rows = []
    for idx_str, val in values.items():
        idx = int(idx_str)
        g = idx // n_time; t = idx % n_time
        rows.append({"country_code": geo_idx[g], "year": int(time_idx[t]),
                     "field": field, "level": level, "graduates": val})
    return pd.DataFrame(rows)

def run() -> None:
    dfs = []
    for field in FIELDS:
        for level in LEVELS:
            dfs.append(_fetch_field_level(field, level))
    df = pd.concat([d for d in dfs if not d.empty], ignore_index=True)
    df = add_provenance(df, SOURCE_ID, SOURCE_LICENSE, SOURCE_URL, "2005-2024")
    dest = RAW_DIR / "s09"; dest.mkdir(exist_ok=True)
    df.to_csv(dest / "eurostat_graduates.csv", index=False)
    save_parquet(df, "s09_graduates")
    log.info("[S09] %d rows fetched", len(df))

if __name__ == "__main__":
    run()
