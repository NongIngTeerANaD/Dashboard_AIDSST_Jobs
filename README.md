# Dashboard: วิเคราะห์ตลาดงานและ Skill Mismatch สาย AI / Data Science / Statistics

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/framework-Dash-cyan.svg)](https://dash.plotly.com/)
[![Plotly](https://img.shields.io/badge/charts-Plotly-3F4F75.svg)](https://plotly.com/)
[![License: Open Data](https://img.shields.io/badge/data-Open%20Data%20Only-green.svg)](#แหล่งข้อมูลและ-license)

> **ข้อสำคัญ:** Dashboard นี้ใช้เฉพาะข้อมูลเปิดที่ตรวจสอบ license แล้ว ไม่มีการแต่งข้อมูลหรือลิงก์ขึ้นเอง หากข้อมูลส่วนใดไม่มีแหล่งที่ตรวจสอบแล้ว จะแสดงสถานะ ⛔ "ไม่มีข้อมูลเปิด" แทนการใส่ค่าสมมติ

---

## ภาพรวม

Dashboard นี้ตอบคำถามหลัก 3 ข้อ สำหรับนักศึกษา อาจารย์ และผู้ออกแบบหลักสูตรสาย AI / Data Science / Statistics:

| Tab | คำถาม |
|-----|--------|
| **Tab 1** | มีผู้จบสายนี้กี่คน และเรียนมาด้วย skill อะไร? |
| **Tab 2** | ตลาดจ้างงานกี่ตำแหน่ง และต้องการ skill อะไร? |
| **Tab 3** | Skill ที่เรียนกับ skill ที่ตลาดต้องการต่างกันตรงไหน? (Skill Mismatch) |

**ผู้ใช้เป้าหมาย:** นักศึกษา · อาจารย์/ผู้ออกแบบหลักสูตร · นักวิเคราะห์ตลาดแรงงาน

---

## การติดตั้งและรัน

### ความต้องการ

- Python 3.11+
- pip

### ขั้นตอน

```bash
# 1. Clone repository
git clone https://github.com/NongIngTeerANaD/Dashboard_AIDSST_Jobs.git
cd Dashboard_AIDSST_Jobs

# 2. ติดตั้ง dependencies
pip install -r requirements.txt

# 3. รัน ETL pipeline (ดาวน์โหลดและเตรียมข้อมูล)
python -m etl.run_all

# 4. เปิด Dashboard
python -m app
```

เปิด browser ที่ `http://127.0.0.1:8050`

---

## โครงสร้างโปรเจกต์

```
Dashboard_AIDSST_Jobs/
├── app/                        # Dash application
│   ├── __main__.py             # Entry point
│   ├── layout.py               # Global layout & tabs
│   ├── callbacks/              # Dash callbacks (cross-filter, store)
│   └── charts/                 # Chart builder functions (Plotly)
│
├── etl/                        # ETL pipeline (fetch → clean → process)
│   ├── run_all.py              # Run all ETL steps in order
│   ├── fetch_*.py              # Download raw data from open sources
│   └── clean_*.py              # Clean & standardize raw data
│
├── data/
│   ├── raw/                    # Raw downloaded files (not committed if large)
│   ├── processed/              # Parquet/SQLite files used by the app
│   └── curated/                # Hand-curated CSVs (programs, courses, tuition)
│       ├── programs.csv        # University programs (user-maintained)
│       ├── courses.csv         # Required courses per program (user-maintained)
│       ├── skill_taxonomy.csv  # Skill mapping: course -> market skill
│       └── tuition.csv         # Tuition data (user-maintained, no open source)
│
├── tests/                      # Unit tests (metrics, ETL schema, callbacks)
│
├── BRD_Skill_Mismatch_Dashboard.md   # Business Requirements Document
├── labor-market-open-data-sources.md # Open data catalog (S01-S15, R01-R03)
├── requirements.txt
└── README.md
```

---

## ข้อมูลที่ใช้

ข้อมูลทั้งหมดมาจากแหล่งเปิดที่ตรวจสอบ license แล้ว ดูรายละเอียดฉบับเต็มใน [`labor-market-open-data-sources.md`](./labor-market-open-data-sources.md)

| แหล่ง | ใช้ใน | License | ขอบเขต |
|--------|--------|---------|--------|
| **S01** Indeed Job Postings Index | Tab 2 (T2-1) | CC BY 4.0 | US/EU/UK (ไม่มีไทย) |
| **S02** Indeed AI Tracker | Tab 2 (T2-2) | CC BY 4.0 | หลายประเทศ |
| **S03** O*NET Database 31.0 | Tab 2 (T2-2, T2-4), Tab 3 | CC BY 4.0 | สหรัฐฯ (อาชีพ/ทักษะ) |
| **S04** Anthropic Economic Index | Tab 2 (เสริม) | CC BY | หลายประเทศ ⚠️ ดู caveat |
| **S05** Stack Overflow Survey 2025 | Tab 2 (T2-2, T2-4) | ODbL 1.0 | หลายประเทศ (self-select) |
| **S06** ILOSTAT Bulk Download | Tab 2 (T2-1) | CC BY 4.0 | ทั่วโลก รวมไทย |
| **S07** World Bank / ILO Unemployment | Tab 1 (T1-3) | CC BY 4.0 | ทั่วโลก รวมไทย |
| **S08** Eurostat ICT Specialists | Tab 2 (T2-1) | Eurostat reuse | EU |
| **S09** Eurostat Graduates | Tab 1 (T1-1) | Eurostat reuse | EU |
| **S10** BLS OEWS May 2025 | Tab 2 (T2-1, T2-3, T2-4) | Public domain | สหรัฐฯ |
| **S11** ONS ASHE 2025 | Tab 2 (T2-4) | OGL v3.0 | สหราชอาณาจักร |
| **S12** ผู้สำเร็จการศึกษา ไทย (CEA/MHESI) | Tab 1 (T1-1) | CC Attribution | ไทย (ระดับกลุ่มสาขา) ⚠️ ถึงปี 2023 |
| **S13** ค่าจ้างเฉลี่ย ไทย (NSO) | Tab 2 (T2-4 อ้างอิง) | CC Attribution | ไทย ⚠️ ปี 2018-2019 |
| **S14** Singapore MOM Employment | Tab 1, Tab 2 | SG Open Data Licence v1.0 | สิงคโปร์ |
| **S15** Singapore GES (NTU/NUS/...) | Tab 1 (T1-3), Tab 2 (T2-4) | SG Open Data Licence v1.0 | สิงคโปร์ รายหลักสูตร |

### แหล่งที่รอตรวจ license (ปิดด้วย feature flag)

| แหล่ง | ใช้ใน | สถานะ |
|--------|--------|--------|
| **R01** ESCO v1.2.1 | Tab 3 (taxonomy) | ⏳ รอตรวจ license |
| **R02** DOL OFLC LCA | Tab 2 (T2-3) | ⏳ รอตรวจ license |
| **R03** NCES IPEDS | Tab 1 (T1-1 สหรัฐฯ) | ⏳ รอตรวจ license |

---

## ป้ายสถานะข้อมูล

| ป้าย | ความหมาย |
|------|----------|
| ✅ | ข้อมูลเปิดที่ตรวจสอบ license แล้ว |
| ⚠️ | ข้อมูลเก่ากว่า 3 ปี |
| 🧮 | ค่าประมาณ / อนุมาน |
| ✍️ | ข้อมูลที่ผู้ใช้เพิ่มเอง (curated CSV) |
| ⛔ | ไม่มีแหล่งข้อมูลเปิดที่ผ่านเกณฑ์ |

---

## ช่องว่างของข้อมูล (Data Gaps)

| หัวข้อ | สถานะ | แนวทาง |
|--------|--------|--------|
| ชื่อหลักสูตร + ผู้จบรายหลักสูตร (ไทย) | ⛔ ไม่มีแหล่งเปิด | ใช้ data/curated/programs.csv (ผู้ใช้กรอกเอง) |
| รายวิชาบังคับรายหลักสูตร | ⛔ ไม่มีแหล่งเปิดรวมศูนย์ | ใช้ data/curated/courses.csv |
| อัตรางานทำปีที่ 1/2/3 (ไทย) | ⛔ ไม่มีแหล่งเปิด | S15 (สิงคโปร์) + curated |
| ค่าเทอม (ไทย) | ⛔ ไม่มีแหล่งเปิด | data/curated/tuition.csv |
| ประกาศงาน/ตำแหน่งว่าง ไทย/อาเซียน | ⛔ ไม่มีแหล่งเปิด | ใช้ตัวแทน US/EU/SG + คำเตือน |
| รายชื่อบริษัทที่จ้าง | ⛔/⏳ | ระดับอุตสาหกรรม S10; รอ R02 |
| เงินเดือนสาย DS/AI ของไทย | ⛔ | S13 (อ้างอิงย้อนหลัง 2018-2019) |

---

## นิยาม Skill Mismatch Metrics

- **Supply share (s)** = หน่วยกิตรายวิชาที่แมป skill k / หน่วยกิตบังคับรวมของหลักสูตร c
- **Demand share (d)** = ความถี่/คะแนนความสำคัญของ skill k / ผลรวมทุก skill ในสายงาน r (normalize 0-1)
- **Gap Score** = `d - s`  (บวก = ตลาดต้องการมากกว่าที่สอน · ลบ = สอนมากกว่าตลาดต้องการ)
- **Coverage@N** = จำนวน skill ใน Top-N ของตลาดที่ s > 0 / N

สูตรทั้งหมดมี unit test ใน `tests/`

---

## ข้อกำหนดทางเทคนิค

| ID | ข้อกำหนด |
|----|----------|
| TR-01 | Python 3.11+ |
| TR-02 | Plotly (plotly.graph_objects / plotly.express) |
| TR-03 | Dash (callbacks + dcc.Store สำหรับ cross-filter) |
| TR-04 | pandas / polars · เก็บข้อมูลเป็น Parquet/SQLite |
| TR-05 | ETL pipeline แยกจากแอป (etl/ -> data/processed/) |
| TR-06 | ทุกตารางมี source_id, license, source_url, data_year, retrieved_at |
| TR-07 | ไม่ใช้ API key ไม่ต้อง login |
| TR-08 | รันด้วยคำสั่งเดียว: python -m app |
| TR-09 | ธีมสว่าง/มืด · สีหลากสี · ตัวอักษรไทยแสดงถูกต้อง |

---

## แผนการพัฒนา

| ระยะ | งาน | สถานะ |
|------|-----|--------|
| **M1** | โครงโปรเจกต์ + ETL + schema + provenance | กำลังดำเนินการ |
| **M2** | Global filters + Store + Tab 2 | รอ |
| **M3** | Tab 1 (S12/S14/S15 + curated + สถานะ ⛔) | รอ |
| **M4** | Skill taxonomy + Tab 3 + unit test | รอ |
| **M5** | Cross-filter ทั้งหมด + Methodology + ทดสอบ AC-01-AC-09 | รอ |

ดูความคืบหน้าแบบละเอียดได้ที่ PROJECT_STATUS.md

---

## เกณฑ์การยอมรับ

| AC | เกณฑ์ |
|----|--------|
| AC-01 | รันด้วยคำสั่งเดียว เปิด Dashboard 3 Tab ได้ในเครื่องใหม่ |
| AC-02 | เปลี่ยนตัวกรอง -> ทุกกราฟ 3 Tab อัปเดต (>= 5 test scenarios) |
| AC-03 | Cross-filter: คลิกกราฟ Tab 1 -> Tab 2 และ Tab 3 กรองตาม |
| AC-04 | ทุกกราฟแสดง source/license/ปีข้อมูล + ป้ายเตือนเมื่อเก่ากว่า 3 ปี |
| AC-05 | ข้อมูลที่ไม่มีแหล่งเปิดแสดง ⛔ ไม่มีค่าสมมติ |
| AC-06 | Tab 3 คำนวณ Gap Score ตามนิยามและผ่าน unit test |
| AC-07 | curated CSV ว่างหรือขาดคอลัมน์ -> ไม่แอปล่ม (แสดง ⛔) |
| AC-08 | ลิงก์ใน "แหล่งข้อมูล" ตรงกับแคตตาล็อก ไม่มีลิงก์นอกแคตตาล็อก |
| AC-09 | Response เมื่อเปลี่ยนตัวกรอง <= 2 วินาที |

---

*สร้างโดย Antigravity (AI coding agent) | ผู้ขอ: นักศึกษาสถิติ ปี 4 มหาวิทยาลัยขอนแก่น | v1.0 · 2026-10-05*
