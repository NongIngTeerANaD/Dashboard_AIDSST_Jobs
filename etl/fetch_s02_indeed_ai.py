"""Fetch S02: Indeed AI Tracker (CC BY 4.0)."""
import requests, pandas as pd, io
from etl._base import RAW_DIR, add_provenance, save_parquet, log

SOURCE_ID = "S02"
SOURCE_LICENSE = "CC BY 4.0"
SOURCE_URL = "https://github.com/hiring-lab/ai-tracker"

FILES = {
    "ai": "https://raw.githubusercontent.com/hiring-lab/ai-tracker/main/AI_posting.csv",
    "genai": "https://raw.githubusercontent.com/hiring-lab/ai-tracker/main/GenAI_posting.csv",
}

def run() -> None:
    dest = RAW_DIR / "s02"; dest.mkdir(exist_ok=True)
    dfs = []
    for name, url in FILES.items():
        try:
            resp = requests.get(url, timeout=30)
            resp.raise_for_status()
            df = pd.read_csv(io.StringIO(resp.text))
            df["tracker_type"] = name
            df.to_csv(dest / f"indeed_{name}.csv", index=False)
            dfs.append(df)
            log.info("[S02] %s: %d rows", name, len(df))
        except Exception as e:
            log.warning("[S02] %s failed: %s", name, e)
    if dfs:
        combined = pd.concat(dfs, ignore_index=True)
        combined = add_provenance(combined, SOURCE_ID, SOURCE_LICENSE, SOURCE_URL, "2020-2026")
        save_parquet(combined, "s02_ai_tracker")

if __name__ == "__main__":
    run()
