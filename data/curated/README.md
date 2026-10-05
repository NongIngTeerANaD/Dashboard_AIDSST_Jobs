# data/curated/ — คู่มือการกรอกข้อมูล

ไฟล์ในโฟลเดอร์นี้เป็น **ข้อมูลที่ผู้ใช้ต้องกรอกเอง** เนื่องจากไม่มีแหล่งข้อมูลเปิดที่ครอบคลุมในระดับรายหลักสูตรสำหรับประเทศไทย

กราฟที่ใช้ข้อมูลเหล่านี้จะแสดงป้าย ✍️ และกราฟที่ยังไม่มีข้อมูลจะแสดง ⛔

---

## ไฟล์และ Schema

### programs.csv — หลักสูตรที่เปิดสอน

| คอลัมน์ | ประเภท | คำอธิบาย | ตัวอย่าง |
|---------|--------|----------|---------|
| program_id | string | รหัสหลักสูตรที่ไม่ซ้ำกัน | KKU_STAT_BSC |
| program_name_th | string | ชื่อหลักสูตรภาษาไทย | วิทยาศาสตรบัณฑิต สาขาสถิติ |
| program_name_en | string | ชื่อหลักสูตรภาษาอังกฤษ | Bachelor of Science (Statistics) |
| institution | string | ชื่อสถาบัน | มหาวิทยาลัยขอนแก่น |
| country | string | รหัสประเทศ ISO 3166-1 | TH |
| degree_level | string | bachelor / master / phd | bachelor |
| role_family | string | ai_ml / data_science / statistics / data_analyst | statistics |
| source_id | string | แหล่งที่มาของข้อมูลนี้ | CURATED_USER |
| license | string | สิทธิ์การใช้ข้อมูล | Public (ข้อมูลจากเว็บสาธารณะของสถาบัน) |
| source_url | string | URL ที่ตรวจสอบข้อมูล | https://sci.kku.ac.th/stat/ |
| data_year | integer | ปีที่ข้อมูลนี้อ้างอิง | 2024 |
| retrieved_at | datetime | วันที่กรอก (ISO 8601) | 2026-10-05T17:00:00+07:00 |

### courses.csv — รายวิชาในหลักสูตร

| คอลัมน์ | ประเภท | คำอธิบาย |
|---------|--------|----------|
| program_id | string | ตรงกับ programs.csv |
| course_code | string | รหัสวิชา เช่น ST301 |
| course_name | string | ชื่อวิชาภาษาอังกฤษ |
| credits | integer | จำนวนหน่วยกิต |
| is_required | boolean | true = บังคับ, false = เลือก |
| source_id, license, source_url, data_year, retrieved_at | — | Provenance (เหมือน programs.csv) |

### skill_taxonomy.csv — Taxonomy ทักษะ (อิง O*NET)

| คอลัมน์ | ประเภท | คำอธิบาย |
|---------|--------|----------|
| skill_id | string | รหัสทักษะ เช่น SKL_PYTHON |
| skill_name | string | ชื่อทักษะ เช่น Python Programming |
| category | string | hard / tool / language / soft |
| taxonomy_ref | string | อ้างอิง O*NET element ID หรือ ESCO URI |
| source_id, license, source_url, data_year, retrieved_at | — | Provenance |

### course_skill_map.csv — การแมปรายวิชา → ทักษะ

| คอลัมน์ | ประเภท | คำอธิบาย |
|---------|--------|----------|
| course_code | string | ตรงกับ courses.csv |
| skill_id | string | ตรงกับ skill_taxonomy.csv |
| confidence | string | exact / keyword / manual |
| notes | string | หมายเหตุ (ถ้ามี) |

### tuition.csv — ค่าเทอม (ข้อมูลที่ผู้ใช้กรอกเอง)

⛔ ไม่มีแหล่งข้อมูลเปิดที่ผ่านเกณฑ์ — กรอกจากเว็บสถาบันโดยตรง และระบุ source_url

---

## ข้อกำหนด

1. **ห้ามแต่งข้อมูล** — กรอกเฉพาะข้อมูลที่อ้างอิงจากเอกสารหลักสูตรสาธารณะได้
2. **ต้องระบุ source_url** สำหรับทุกแถว
3. **ตรวจสอบสิทธิ์** ก่อนนำข้อมูลรายวิชาจากเอกสารของสถาบันมาใช้
4. ข้อมูลที่ว่างหรือขาดคอลัมน์จะแสดง ⛔ ในแดชบอร์ดโดยไม่ทำให้แอปล่ม (AC-07)
