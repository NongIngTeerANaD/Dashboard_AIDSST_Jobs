"""Clean S03: O*NET 31.0 -> data/processed/s03_skills_demand.parquet (CC BY 4.0).

Demand score per (role_family, skill) in [0, 1]:
  * software evidence  = share of the role's representative O*NET occupations that list at least one
                         matching technology/software example (table 'Software Skills')
  * knowledge/skill    = mean normalised Importance ((IM - 1) / 4) from 'Knowledge' / 'Essential Skills'
  The score is the mean of the available components. Mapping is keyword based (confidence = 'keyword').
Role -> SOC mapping is an approximation: O*NET has no 'ML engineer' / 'AI engineer' occupation.
"""
import re
import pandas as pd
from etl._base import RAW_DIR, add_provenance, save_parquet, log

SOURCE_ID = "S03"
SOURCE_LICENSE = "CC BY 4.0"
SOURCE_URL = "https://www.onetcenter.org/database.html"

ROLE_SOC = {
    "data_science": ["15-2051.00"],                                   # Data Scientists
    "ai_ml": ["15-1221.00", "15-2051.00"],                            # Computer & Info Research Scientists + Data Scientists
    "statistics": ["15-2041.00", "15-2041.01"],                       # Statisticians, Biostatisticians
    "data_analyst": ["15-2051.01", "15-2031.00", "15-1243.01"],       # BI Analysts, OR Analysts, Data Warehousing Specialists
}

SOFTWARE_RULES = {  # skill_id -> regex on 'Workplace Example' (case-insensitive)
    "SK_PYTHON": r"^python$|^pandas$|^numpy$|^scipy$|^pyspark$|jupyter",
    "SK_R": r"^r$|^shiny$",
    "SK_SQL": r"sql|postgres|db2|teradata database|snowflake|redshift|bigquery|mongodb|microsoft access|oracle database",
    "SK_ML": r"scikit|xgboost|mlflow|machine learning|enterprise miner|knowledgeseeker",
    "SK_DEEP_LEARNING": r"tensorflow|pytorch|keras|mxnet",
    "SK_NLP": r"spacy|chatgpt|openai|nltk|hugging",
    "SK_DATA_VIZ": r"tableau|power bi|qlik|looker|business intelligence software|reporting software|sigmaplot",
    "SK_BIG_DATA": r"spark|hadoop|hive|kafka|mapreduce|apache pig|airflow|cassandra|elasticsearch",
    "SK_CLOUD_DEVOPS": r"amazon web services|aws|azure|google cloud|docker|kubernetes|jenkins|kubeflow|amazon elastic|amazon simple storage",
    "SK_STATS_INF": r"\bsas\b|spss|stata|minitab|statistica|\bjmp\b|statistical software|graphpad|ncss|systat|s-plus|bmdp|superanova|statxact|mplus|lisrel|hierarchical linear|rat-stats|datadesk|unistat|statgraphics",
    "SK_REGRESSION": r"eviews|limdep|microfit|gauss",
    "SK_TIME_SERIES": r"autobox|ts-wave|eviews",
}
# skill_id -> [(table, element name)] normalised Importance
IMPORTANCE_RULES = {
    "SK_MATH_OPT": [("Knowledge", "Mathematics"), ("Essential Skills", "Mathematics")],
    "SK_STATS_INF": [("Knowledge", "Mathematics")],
    "SK_COMM": [("Essential Skills", "Writing"), ("Essential Skills", "Speaking")],
    "SK_PROBLEM_SOLVING": [("Essential Skills", "Critical Thinking"), ("Essential Skills", "Complex Problem Solving")],
}


def _read(name: str) -> pd.DataFrame:
    files = list((RAW_DIR / "s03").rglob(f"{name}.xlsx"))
    if not files:
        raise FileNotFoundError(f"{name}.xlsx not found under data/raw/s03 (run etl.fetch_s03_onet)")
    return pd.read_excel(files[0])


def run() -> None:
    try:
        soft = _read("Software Skills")
        tables = {"Knowledge": _read("Knowledge"), "Essential Skills": _read("Essential Skills")}
    except FileNotFoundError as exc:
        log.warning("[S03] %s — skipping clean.", exc)
        return
    rows = []
    for role, socs in ROLE_SOC.items():
        found = soft["O*NET-SOC Code"].isin(socs).any()
        if not found:
            log.warning("[S03] role %s: none of %s found in O*NET 31.0 — skipped", role, socs)
            continue
        s_role = soft[soft["O*NET-SOC Code"].isin(socs)]
        for skill in set(SOFTWARE_RULES) | set(IMPORTANCE_RULES):
            parts, evidence = [], []
            if skill in SOFTWARE_RULES:
                pat = re.compile(SOFTWARE_RULES[skill], re.I)
                hit = s_role[s_role["Workplace Example"].astype(str).str.contains(pat)]
                parts.append(hit["O*NET-SOC Code"].nunique() / len(socs))
                if len(hit):
                    evidence.append("software: " + ", ".join(sorted(hit["Workplace Example"].astype(str).unique())[:6]))
            for table, elem in IMPORTANCE_RULES.get(skill, []):
                t = tables[table]
                v = t[(t["O*NET-SOC Code"].isin(socs)) & (t["Element Name"] == elem) & (t["Scale ID"] == "IM")]["Data Value"]
                if len(v):
                    parts.append(float(((v - 1) / 4).mean()))
                    evidence.append(f"{table}: {elem} (IM)")
            if parts:
                rows.append({"role_family": role, "skill_id": skill, "importance_or_freq": round(sum(parts) / len(parts), 4),
                             "evidence": "; ".join(evidence), "soc_codes": ",".join(socs)})
    if not rows:
        log.warning("[S03] no rows produced")
        return
    df = add_provenance(pd.DataFrame(rows), SOURCE_ID, SOURCE_LICENSE, SOURCE_URL, "O*NET 31.0")
    save_parquet(df, "s03_skills_demand")
    log.info("[S03] %d (role, skill) rows saved", len(df))


if __name__ == "__main__":
    run()
