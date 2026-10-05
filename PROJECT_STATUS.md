# PROJECT_STATUS.md — Dashboard วิเคราะห์ตลาดงานและ Skill Mismatch

อัปเดตล่าสุด: 2026-10-05

---

## สรุปสถานะโดยรวม

| ระยะ | สถานะ | รายละเอียด |
|------|--------|------------|
| M1 — โครงโปรเจกต์ + ETL | ✅ เสร็จแล้ว | scaffold โครงสร้างไฟล์, requirements.txt, ETL stubs, unit tests (13 passed) |
| M2 — Global filters + Tab 2 | ✅ เสร็จแล้ว | T2-1 Indeed Job Postings Index, T2-2 Skills in demand, T2-3 MOM Treemap, T2-4 Salary |
| M3 — Tab 1 | ✅ เสร็จแล้ว | T1-1 Graduates by Program/Year, T1-2 Course Sunburst, T1-3 Employment, T1-4 Tuition |
| M4 — Tab 3 + Unit tests | ✅ เสร็จแล้ว | T3-2 Skill Gap Heatmap, T3-3 Quadrant, T3-4 Top Gaps, T3-5 Coverage@5, 18/18 tests passed |
| M5 — Cross-filter + QA | ⏳ รอ | — |

---

## M1 — โครงโปรเจกต์ + ETL Pipeline

### เป้าหมาย
- สร้างโครงสร้างไดเรกทอรีตาม BRD ข้อ 3
- สร้าง `requirements.txt`
- สร้าง ETL stubs สำหรับทุกแหล่งข้อมูล (S01–S15 ที่เกี่ยวข้อง)
- สร้าง schema และ provenance columns (TR-06)
- สร้าง curated CSV templates (programs, courses, skill_taxonomy, tuition)
- สร้าง .gitignore สำหรับ data/raw/ และ data/processed/

### Checklist

#### โครงสร้างโปรเจกต์
- [x] README.md — เสร็จแล้ว (commit b943445)
- [x] requirements.txt
- [x] .gitignore
- [x] app/__main__.py (skeleton)
- [x] app/layout.py (skeleton)
- [x] app/callbacks/__init__.py
- [x] app/charts/__init__.py
- [x] etl/__init__.py
- [x] etl/run_all.py
- [x] tests/__init__.py

#### ETL — Fetch Scripts (download only, no scraping)
- [x] etl/fetch_s01_indeed_postings.py — Indeed Job Postings Index (GitHub CSV, CC BY 4.0)
- [x] etl/fetch_s02_indeed_ai.py — Indeed AI Tracker (GitHub CSV, CC BY 4.0)
- [x] etl/fetch_s03_onet.py — O*NET 31.0 (ZIP download, CC BY 4.0)
- [x] etl/fetch_s05_stackoverflow.py — Stack Overflow Survey 2025 (GitHub, ODbL 1.0)
- [x] etl/fetch_s06_ilostat.py — ILOSTAT Bulk Download (CC BY 4.0)
- [x] etl/fetch_s07_worldbank.py — World Bank API SL.UEM.ADVN.ZS (CC BY 4.0)
- [x] etl/fetch_s08_eurostat_ict.py — Eurostat isoc_sks_itspt API
- [x] etl/fetch_s09_eurostat_grad.py — Eurostat educ_uoe_grad02 API
- [x] etl/fetch_s10_bls_oews.py — BLS OEWS ZIP (Public domain)
- [x] etl/fetch_s11_ons_ashe.py — ONS ASHE 2025 (OGL v3.0)
- [x] etl/fetch_s12_cea_thai.py — CEA/MHESI ผู้สำเร็จการศึกษาไทย (data.go.th)
- [x] etl/fetch_s13_nso_thai.py — NSO ค่าจ้างไทย (data.go.th)
- [x] etl/fetch_s14_sg_mom.py — Singapore MOM Employment (data.gov.sg)
- [x] etl/fetch_s15_sg_ges.py — Singapore GES (data.gov.sg)

#### ETL — Clean Scripts
- [x] etl/clean_s01.py
- [x] etl/clean_s02.py
- [x] etl/clean_s03.py
- [x] etl/clean_s05.py
- [x] etl/clean_s06.py
- [x] etl/clean_s07.py
- [x] etl/clean_s08.py
- [x] etl/clean_s09.py
- [x] etl/clean_s10.py
- [x] etl/clean_s11.py
- [x] etl/clean_s12.py
- [x] etl/clean_s13.py
- [x] etl/clean_s14.py
- [x] etl/clean_s15.py

#### Curated Data Templates
- [x] data/curated/programs.csv (schema template)
- [x] data/curated/courses.csv (schema template)
- [x] data/curated/skill_taxonomy.csv (O*NET-based)
- [x] data/curated/tuition.csv (schema template)
- [x] data/curated/README.md (คำแนะนำการกรอกข้อมูล)

#### Unit Tests (M1 scope)
- [x] tests/test_provenance_schema.py — ตรวจสอบว่าทุก DataFrame มีคอลัมน์ provenance ครบ (TR-06)
- [x] tests/test_metrics.py — Gap Score, Coverage@N (เตรียม fixture ข้อมูลเล็ก)

---

## M2 — Global Filters + Tab 2 (ตลาดงาน)

### เป้าหมาย
- dcc.Store สถานะตัวกรองส่วนกลาง (FR-G1, FR-G2)
- Filter chips แสดง + ล้าง (FR-G4)
- URL query string sync (FR-G7)
- Tab 2 กราฟ T2-1 ถึง T2-4
- แสดงป้ายสถานะข้อมูลใต้กราฟ (FR-G5)

### Checklist
- [ ] app/layout.py — global filter bar + tab structure
- [ ] app/callbacks/store.py — filter state management
- [ ] app/callbacks/tab2.py — Tab 2 callbacks
- [ ] app/charts/tab2_postings.py — T2-1 job postings trend
- [ ] app/charts/tab2_skills.py — T2-2 skills heatmap/bar
- [ ] app/charts/tab2_employers.py — T2-3 industry treemap
- [ ] app/charts/tab2_salary.py — T2-4 salary range plot
- [ ] tests/test_callbacks_tab2.py (>= 5 scenarios, AC-02)

---

## M3 — Tab 1 (ผู้สำเร็จการศึกษา)

### Checklist
- [ ] app/callbacks/tab1.py
- [ ] app/charts/tab1_graduates.py — T1-1 graduates by program/year
- [ ] app/charts/tab1_courses.py — T1-2 sunburst/treemap courses->skills
- [ ] app/charts/tab1_employment.py — T1-3 employment outcome
- [ ] app/charts/tab1_tuition.py — T1-4 tuition (⛔ หากไม่มี curated data)
- [ ] แสดง ⛔ เมื่อไม่มีข้อมูล curated (AC-05, AC-07)

---

## M4 — Skill Taxonomy + Tab 3 (Mismatch)

### Checklist
- [ ] data/curated/skill_taxonomy.csv — สร้างจาก O*NET
- [ ] etl/build_skill_map.py — แมป course -> skill_id (confidence: exact|keyword|manual)
- [ ] app/callbacks/tab3.py
- [ ] app/charts/tab3_heatmap.py — T3-2 Mismatch heatmap
- [ ] app/charts/tab3_quadrant.py — T3-3 Quadrant chart
- [ ] app/charts/tab3_top_gaps.py — T3-4 Top gap bars
- [ ] app/charts/tab3_coverage.py — T3-5 Coverage radar/bar
- [ ] app/charts/tab3_drilldown.py — T3-6 Drill-down panel
- [x] tests/test_metrics.py — Gap Score, Coverage@N unit tests (AC-06)

---

## M5 — Integration, QA, ส่งมอบ

### Checklist
- [ ] Cross-filter ทั้งหมด (AC-02, AC-03)
- [ ] app/pages/methodology.py — หน้า "ระเบียบวิธีและข้อจำกัด"
- [ ] app/pages/sources.py — หน้า "แหล่งข้อมูลและ License" (AC-08)
- [ ] ทดสอบ AC-01 ถึง AC-09 ครบ
- [ ] ทดสอบ Response time <= 2 วินาที (AC-09, NFR-01)
- [ ] ทดสอบ Thai font rendering (TR-09)
- [ ] ปุ่ม Export CSV + PNG (UX)
- [ ] dark/light theme toggle (TR-09)
- [ ] README อัปเดตขั้นตอนรันจริง

---

## บันทึกการเปลี่ยนแปลง

| วันที่ | ระยะ | รายละเอียด |
|--------|------|------------|
| 2026-10-05 | init | สร้าง README.md, commit เริ่มต้น (b943445) |
| 2026-10-05 | M1 | เริ่ม scaffold โครงสร้างโปรเจกต์ |
| 2026-10-05 | M1 | เสร็จ M1: scaffold ครบ, ETL stubs 14 แหล่ง, unit tests 13/13 ✅ |

---

## ข้อจำกัดและ Data Gaps ที่ต้องแจ้งผู้ใช้

1. **Tab 1 (ไทย)** พึ่งข้อมูล curated ที่ผู้ใช้ต้องกรอกเอง (ดู `data/curated/README.md`)
2. **Tab 2** ไม่มีข้อมูลตลาดงานไทย/อาเซียน ใช้ตัวแทน US/EU/SG
3. **เงินเดือนระดับ Entry/Mid/Senior** เป็นการอนุมาน (🧮) จาก OEWS percentile + O*NET job zones
4. **R01–R03** ปิดด้วย feature flag จนกว่าผู้ใช้ตรวจ license


| 2026-10-05 | M2-M4 | เชื่อมต่อข้อมูลจริง S01, S02, S14, S15 + Curated, สร้างกราฟ Plotly ครบทั้ง 3 Tab, แก้ไข Dash callback registration, ผ่านการทดสอบ 18/18 tests |


| 2026-10-05 | M5 | ตรวจพบข้อมูล curated (graduates/courses/tuition/skills_demand) เป็นตัวเลขสมมติที่ติดป้ายแหล่งจริง → เปลี่ยนเป็น SAMPLE_DEMO + ป้าย 🧪 + แบนเนอร์เตือน; เพิ่ม cross-filter (คลิกหลักสูตรใน T1-1/T3-2), Tab 4 แหล่งข้อมูล/ระเบียบวิธี, ปุ่ม CSV ใน Tab 3, แก้ supply share ให้นับเฉพาะวิชาบังคับ, แก้ป้าย T2-4, เพิ่ม tests/test_app_callbacks.py (43 tests ผ่าน), run_dashboard.bat/.sh |

## สิ่งที่ยังเหลือ
- แทนที่ข้อมูล SAMPLE_DEMO ด้วยข้อมูลจริง (ดู data/curated/SAMPLE_NOTICE.md); skills_demand ควรมาจาก O*NET (S03) จริง
- ETL ของ S03, S05–S13 ยังไม่ได้เชื่อมเข้าแอป (ต้องรันบนเครื่องที่เข้าถึงเว็บต้นทาง)
- ปุ่มส่งออก PNG, dark theme, ตรวจ AC-09 (<=2 วินาที) บนข้อมูลจริง
