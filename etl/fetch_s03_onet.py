"""Fetch S03: O*NET Database 31.0 (CC BY 4.0) + write an inventory of its files.

Step 1 (this script): download the official Excel bundle, extract it, and write
data/raw/s03/_inventory.txt listing every table with its columns and first rows.
Step 2 (clean_s03): the parser is written against that real layout.
"""
import zipfile
import pandas as pd
from etl._base import RAW_DIR, download_file, log

SOURCE_ID = "S03"
URL = "https://www.onetcenter.org/dl_files/database/db_31_0_excel.zip"


def run() -> None:
    dest = RAW_DIR / "s03"
    dest.mkdir(parents=True, exist_ok=True)
    try:
        z = download_file(URL, dest / "db_31_0_excel.zip")
    except Exception as exc:
        log.warning("[S03] download failed: %s", exc)
        return
    out = dest / "excel"
    if not out.exists():
        with zipfile.ZipFile(z) as zf:
            zf.extractall(out)
    lines = []
    for f in sorted(out.rglob("*.xlsx")):
        try:
            df = pd.read_excel(f, nrows=3)
            lines.append(f"## {f.relative_to(out)}\ncolumns: {list(df.columns)}\n{df.head(2).to_string()[:600]}\n")
        except Exception as exc:
            lines.append(f"## {f.name}: unreadable ({exc})\n")
    (dest / "_inventory.txt").write_text("\n".join(lines), encoding="utf-8")
    log.info("[S03] inventory written: %s (%d tables)", dest / "_inventory.txt", len(lines))


if __name__ == "__main__":
    run()
