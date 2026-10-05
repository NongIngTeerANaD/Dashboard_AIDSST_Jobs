"""Data loader and filter helpers for Dashboard."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parent.parent
PROCESSED_DIR = ROOT / "data" / "processed"
CURATED_DIR = ROOT / "data" / "curated"

class DataLoader:
    _instance = None

    def __init__(self):
        self.reload()

    def reload(self):
        # 1. Curated Data
        self.programs = self._read_csv(CURATED_DIR / "programs.csv")
        self.courses = self._read_csv(CURATED_DIR / "courses.csv")
        self.course_skill_map = self._read_csv(CURATED_DIR / "course_skill_map.csv")
        self.graduates = self._read_csv(CURATED_DIR / "graduates.csv")
        self.skills = self._read_csv(CURATED_DIR / "skill_taxonomy.csv")
        # real O*NET-derived demand (S03) takes precedence over the curated sample file
        s03 = self._read_parquet(PROCESSED_DIR / "s03_skills_demand.parquet")
        self.skills_demand = s03 if not s03.empty else self._read_csv(CURATED_DIR / "skills_demand.csv")
        self.tuition = self._read_csv(CURATED_DIR / "tuition.csv")

        # 2. Processed Open Data
        self.job_postings = self._read_parquet(PROCESSED_DIR / "s01_job_postings.parquet")
        self.sector_postings = self._read_parquet(PROCESSED_DIR / "s01_sector_postings.parquet")
        self.uem_advanced = self._read_parquet(PROCESSED_DIR / "s07_uem_advanced.parquet")
        self.ict_specialists = self._read_parquet(PROCESSED_DIR / "s08_ict_specialists.parquet")
        self.eu_graduates = self._read_parquet(PROCESSED_DIR / "s09_graduates.parquet")
        self.ai_tracker = self._read_parquet(PROCESSED_DIR / "s02_ai_tracker.parquet")
        self.sg_mom = self._read_parquet(PROCESSED_DIR / "s14_sg_mom.parquet")
        self.sg_ges = self._read_parquet(PROCESSED_DIR / "s15_sg_ges.parquet")

    def _read_csv(self, path: Path) -> pd.DataFrame:
        if path.exists() and path.stat().st_size > 0:
            try:
                return pd.read_csv(path)
            except Exception:
                return pd.DataFrame()
        return pd.DataFrame()

    def _read_parquet(self, path: Path) -> pd.DataFrame:
        if path.exists():
            try:
                return pd.read_parquet(path)
            except Exception:
                return pd.DataFrame()
        return pd.DataFrame()

data_store = DataLoader()
