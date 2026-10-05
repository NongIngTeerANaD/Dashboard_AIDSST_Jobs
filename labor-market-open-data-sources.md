# แหล่งข้อมูลเปิด: ตลาดงานสาย AI / Data Science / Statistics

สร้างเมื่อ: 2026-10-05  
ตรวจลิงก์และ license ทุกแหล่งแล้ว (ดูช่อง 'ตรวจสอบ' ของแต่ละรายการ)


## 1. ผ่านเกณฑ์ Open Data

### S01 · Indeed Job Postings Index (Hiring Lab)

- **ผู้เผยแพร่:** Indeed Hiring Lab
- **หัวข้อ:** การจ้างงานและความต้องการแรงงาน, แนวโน้ม AI / ว่างงานบัณฑิต / อื่น ๆ
- **ภูมิภาค:** สหรัฐฯ, สหราชอาณาจักร, ยุโรป (EU), ประเทศอื่น (CA AU DE FR ฯลฯ) — โฟลเดอร์ในรีโป: AU, CA, DE, EA, ES, FR, GB, IE, IT, NL, US (ไม่มีไทย/อาเซียน)
- **License:** CC BY 4.0 ([ลิงก์](https://creativecommons.org/licenses/by/4.0/))
- **รูปแบบ:** CSV (GitHub)
- **ช่วงเวลา:** รายวัน (ค่าเฉลี่ย 7 วัน) ตั้งแต่ 1 ก.พ. 2020 · รีโปรีเฟรชทุกสัปดาห์ (ตาม README) · ความใหม่: ใหม่
- **รายละเอียด:** ดัชนีการเปลี่ยนแปลง (%) ของจำนวนประกาศงานบน Indeed เทียบฐาน 1 ก.พ. 2020 ระดับประเทศ รายกลุ่มอาชีพ (sector) และภูมิภาคย่อยในบางประเทศ ไฟล์ aggregate_job_postings_{รหัสประเทศ}.csv และ job_postings_by_sector_{รหัสประเทศ}.csv
- **ข้อควรระวัง:** เป็นดัชนีสัมพัทธ์ ไม่ใช่จำนวนตำแหน่งสัมบูรณ์ · กลุ่มอาชีพเป็นการจัดกลุ่มของ Indeed (ดู sector-job-title-examples.csv) — ยังไม่ได้ยืนยันว่ามี sector เฉพาะ data/AI · ต้องอ้างอิง Indeed Hiring Lab · อย่าใช้สำเนาใน FRED (เงื่อนไขต่างกัน)
- **ลิงก์:**
  - [dataset] หน้า dataset (GitHub รีโปทางการของ Hiring Lab): https://github.com/hiring-lab/job_postings_tracker
  - [license] CC BY 4.0: https://creativecommons.org/licenses/by/4.0/
- **อ้างอิง:** Indeed Hiring Lab, Indeed Job Postings Index, CC BY 4.0, https://github.com/hiring-lab/job_postings_tracker (เข้าถึง 2026-10-05)
- **ตรวจสอบ:** เปิดหน้ารีโปและอ่าน README/LICENSE 2026-10-05

### S02 · Indeed AI Tracker (สัดส่วนประกาศงานที่มีคำเกี่ยวกับ AI/GenAI)

- **ผู้เผยแพร่:** Indeed Hiring Lab
- **หัวข้อ:** การจ้างงานและความต้องการแรงงาน, ทักษะ, แนวโน้ม AI / ว่างงานบัณฑิต / อื่น ๆ
- **ภูมิภาค:** หลายประเทศ/ทั่วโลก — รายประเทศ (ตรวจคอลัมน์ jobcountry ในไฟล์เองว่ามีประเทศที่ต้องการหรือไม่)
- **License:** CC BY 4.0 ([ลิงก์](https://creativecommons.org/licenses/by/4.0/))
- **รูปแบบ:** CSV
- **ช่วงเวลา:** รายวัน (ค่าเฉลี่ย 7 วัน) · รีเฟรชรายเดือน (ตาม README) · ความใหม่: ใหม่
- **รายละเอียด:** สัดส่วน (%) ของประกาศงานที่มีคำสำคัญด้าน AI (เช่น Machine Learning, Data Science, Artificial Intelligence) และ Generative AI (เช่น Large Language Models) ไฟล์ AI_posting.csv และ GenAI_posting.csv คอลัมน์ date, jobcountry, xxx_share
- **ข้อควรระวัง:** เป็นสัดส่วนของประกาศ ไม่ใช่จำนวน · เป็นการจับคำสำคัญ จึงใช้เป็นตัวแทนของ 'ทักษะ/ความต้องการด้าน AI' ได้เพียงหยาบ ๆ
- **ลิงก์:**
  - [dataset] หน้า dataset (GitHub): https://github.com/hiring-lab/ai-tracker
  - [file] AI_posting.csv: https://github.com/hiring-lab/ai-tracker/blob/main/AI_posting.csv
- **อ้างอิง:** Indeed Hiring Lab, Indeed AI Tracker, CC BY 4.0, https://github.com/hiring-lab/ai-tracker (เข้าถึง 2026-10-05)
- **ตรวจสอบ:** เปิดหน้ารีโปและอ่าน README 2026-10-05

### S03 · O*NET Database 31.0 (ทักษะ ความรู้ งาน ระดับประสบการณ์ รายอาชีพ)

- **ผู้เผยแพร่:** U.S. Department of Labor, Employment and Training Administration (USDOL/ETA)
- **หัวข้อ:** ทักษะ, ระดับสายงาน, แนวโน้ม AI / ว่างงานบัณฑิต / อื่น ๆ
- **ภูมิภาค:** สหรัฐฯ — อาชีพในสหรัฐฯ (ระบบ O*NET-SOC) · ไม่มีเงินเดือนในฐานข้อมูลนี้
- **License:** CC BY 4.0 ([ลิงก์](https://www.onetcenter.org/license_db.html))
- **รูปแบบ:** CSV, XLSX, JSON, SQL, RDF
- **ช่วงเวลา:** รุ่น 31.0 · อัปเดตรายไตรมาส (หน้าเว็บอัปเดต 22 ก.ย. 2026) · ความใหม่: ใหม่
- **รายละเอียด:** ไฟล์สำคัญ: software_skills.csv (เทคโนโลยี/เครื่องมือ), essential_skills.csv, transferable_skills.csv, knowledge.csv, job_zones.csv (ระดับการเตรียมตัว/ประสบการณ์ของอาชีพ), education.csv, training_and_experience.csv, task_statements.csv, emerging_tasks.csv, job_titles.csv, occupation_data.csv
- **ข้อควรระวัง:** ข้อมูลมาจากหลายวิธี (ผู้ปฏิบัติงาน ผู้เชี่ยวชาญ และ big data ตามเอกสาร O*NET) ไม่ใช่ข้อความประกาศงานดิบ · ต้องเครดิต 'O*NET 31.0 Database' + USDOL/ETA, ลิงก์ license และระบุว่าแก้ไขอะไร · ใช้ชื่อ O*NET เป็นคำคุณศัพท์ตามเงื่อนไขเครื่องหมายการค้า
- **ลิงก์:**
  - [dataset] หน้า Database 31.0: https://www.onetcenter.org/database.html
  - [zip] ZIP ทั้งฐาน: https://www.onetcenter.org/dl_files/database/db_31_0_excel.zip
  - [csv] software_skills.csv: https://www.onetcenter.org/dl_files/database/db_31_0_csv/software_skills.csv
  - [csv] job_zones.csv: https://www.onetcenter.org/dl_files/database/db_31_0_csv/job_zones.csv
  - [csv] training_and_experience.csv: https://www.onetcenter.org/dl_files/database/db_31_0_csv/training_and_experience.csv
  - [csv] emerging_tasks.csv: https://www.onetcenter.org/dl_files/database/db_31_0_csv/emerging_tasks.csv
  - [license] เงื่อนไข license: https://www.onetcenter.org/license_db.html
- **อ้างอิง:** This page includes information from the O*NET 31.0 Database by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA). Used under the CC BY 4.0 license. O*NET is a trademark of USDOL/ETA.
- **ตรวจสอบ:** เปิดหน้า database.html (มีลิงก์ดาวน์โหลดและข้อความ license) 2026-10-05

### S04 · Anthropic Economic Index (การใช้ AI เทียบรายอาชีพ/งาน + Labor market impacts)

- **ผู้เผยแพร่:** Anthropic
- **หัวข้อ:** แนวโน้ม AI / ว่างงานบัณฑิต / อื่น ๆ, ทักษะ
- **ภูมิภาค:** หลายประเทศ/ทั่วโลก — จับคู่การสนทนากับ Claude เข้ากับงาน/อาชีพตาม O*NET · มีชุด labor_market_impacts (job exposure, task penetration)
- **License:** CC BY (ข้อมูล) ตาม README · ป้ายบน Hugging Face แสดง 'mit' ([ลิงก์](https://huggingface.co/datasets/Anthropic/EconomicIndex))
- **รูปแบบ:** CSV (ไฟล์ใน Hugging Face repo)
- **ช่วงเวลา:** หลายรุ่น: ล่าสุด release_2026_06_26 (ยังมี 2026-03-24, 2026-01-15, 2025-09-15, 2025-03-27, 2025-02-10) · ความใหม่: ใหม่
- **รายละเอียด:** ข้อมูลรวมที่แสดงว่างานแบบใดถูกใช้ AI ช่วยมาก (automation vs augmentation) แยกตามอาชีพ/ประเทศ ใช้ประกอบหัวข้อ 'ผลของ AI ต่อการจ้างงาน' เปิดดูได้โดยไม่ต้อง login
- **ข้อควรระวัง:** ข้อสังเกตผลประโยชน์ทับซ้อน: ชุดนี้จัดทำโดย Anthropic ซึ่งเป็นผู้พัฒนา Claude (ผู้ช่วยที่จัดทำหน้านี้) · สะท้อนการใช้งานผลิตภัณฑ์ของ Anthropic เท่านั้น ไม่ใช่ตลาดงานทั้งหมด · license ในข้อความ README (data=CC-BY, code=MIT) ไม่ตรงกับป้าย 'mit' บนหัวหน้า — ทั้งคู่อนุญาตให้ใช้ซ้ำ แนะนำให้อ้างอิงตาม README (CC BY) และระบุเวอร์ชันของ release
- **ลิงก์:**
  - [dataset] หน้า dataset (Hugging Face): https://huggingface.co/datasets/Anthropic/EconomicIndex
  - [folder] labor_market_impacts: https://huggingface.co/datasets/Anthropic/EconomicIndex/tree/main/labor_market_impacts
- **อ้างอิง:** Anthropic, The Anthropic Economic Index (Hugging Face: Anthropic/EconomicIndex), CC BY, https://huggingface.co/datasets/Anthropic/EconomicIndex (เข้าถึง 2026-10-05)
- **ตรวจสอบ:** เปิดหน้า dataset card และอ่านหัวข้อ License 2026-10-05 (ยังไม่ได้ดาวน์โหลดไฟล์ CSV รายตัว)

### S05 · Stack Overflow Annual Developer Survey (ดิบรายผู้ตอบ)

- **ผู้เผยแพร่:** Stack Overflow / Stack Exchange Inc.
- **หัวข้อ:** เงินเดือน, ทักษะ, ระดับสายงาน, แนวโน้ม AI / ว่างงานบัณฑิต / อื่น ๆ
- **ภูมิภาค:** หลายประเทศ/ทั่วโลก — ผู้ตอบจากหลายประเทศ (ปี 2025: 49,000+ คน จาก 177 ประเทศ ตามหน้าสรุปของไซต์ — ข้อความจากผลค้นหา)
- **License:** ODbL 1.0 (ข้อมูล) + DbCL 1.0 (เนื้อหาแต่ละเซลล์) ([ลิงก์](https://opendatacommons.org/licenses/odbl/1-0/))
- **รูปแบบ:** CSV (GitHub archive)
- **ช่วงเวลา:** ปี 2011–2025 (ล่าสุด 2025) · ความใหม่: ใหม่
- **รายละเอียด:** ภาษา/เครื่องมือที่ใช้ ประสบการณ์เขียนโค้ด การทำงานระยะไกล การใช้ AI และคอลัมน์ค่าตอบแทน (ตรวจชื่อคอลัมน์ในไฟล์ results.csv/schema ของแต่ละปี) กรองอาชีพ เช่น data scientist ได้ในบางปี
- **ข้อควรระวัง:** กลุ่มตัวอย่างสมัครใจ มี self-selection bias (ตามที่ repo ของ Stack Overflow ระบุ) ไม่เป็นตัวแทนตลาดงาน · ODbL เป็น share-alike: งานดัดแปลงที่เผยแพร่ต่อต้องใช้ ODbL และต้อง attribute · ค่าตอบแทนเป็นรายงานตนเอง
- **ลิงก์:**
  - [dataset] หน้ารวมทุกปี: https://survey.stackoverflow.co/
  - [files] ไฟล์ข้อมูลปี 2025: https://github.com/StackExchange/Survey/tree/main/packages/archive/2025
  - [license] ODbL 1.0: https://opendatacommons.org/licenses/odbl/1-0/
- **อ้างอิง:** Stack Overflow Annual Developer Survey 2025, ODbL 1.0, https://survey.stackoverflow.co/ (เข้าถึง 2026-10-05)
- **ตรวจสอบ:** เปิดหน้า survey.stackoverflow.co (ข้อความ license และลิงก์ Data & files) 2026-10-05

### S06 · ILOSTAT Bulk Download (สถิติแรงงานทั่วโลก)

- **ผู้เผยแพร่:** International Labour Organization (ILO)
- **หัวข้อ:** การจ้างงานและความต้องการแรงงาน, ผู้สำเร็จการศึกษา/วุฒิ, แนวโน้ม AI / ว่างงานบัณฑิต / อื่น ๆ
- **ภูมิภาค:** หลายประเทศ/ทั่วโลก, ไทย, สิงคโปร์ (อาเซียน), สหรัฐฯ, ยุโรป (EU) — หลายประเทศ แยกตาม indicator (~500 ไฟล์) หรือ ref_area (~700 ไฟล์) · ตรวจรหัสประเทศ (เช่น THA, SGP, IND) ใน table_of_contents เอง
- **License:** CC BY 4.0 (ยืนยันทางอ้อม — ดูหมายเหตุ) ([ลิงก์](https://creativecommons.org/licenses/by/4.0/))
- **รูปแบบ:** CSV.gz, dictionary CSV
- **ช่วงเวลา:** อัปเดตทุกวัน 12:00 (เวลา Europe/Paris) · ช่วงปีขึ้นกับตาราง · ความใหม่: ใหม่
- **รายละเอียด:** ตัวอย่างตาราง: การจ้างงานจำแนกตามเพศ/อายุ/อาชีพ (ISCO), ตามสถานภาพการทำงาน, ว่างงานจำแนกตามระดับการศึกษา ดาวน์โหลดฟรี ไม่ต้องสมัคร
- **ข้อควรระวัง:** หน้า bulk ไม่ระบุ license โดยตรง — ยืนยันจากประกาศนโยบาย Open Access ของ ILO (3 พ.ค. 2023: dataset ที่ผลิตตั้งแต่วันนั้นใช้ CC BY 4.0 ตามผลค้นหา ไม่ได้เปิดหน้าประกาศเอง) และจากหน้า World Bank ที่ระบุ CC BY-4.0 สำหรับข้อมูลที่ดึงจาก ILOSTAT bulk · dataset ก่อนวันดังกล่าวอาจไม่ได้รับ CC อัตโนมัติ · ข้อมูลอาชีพเป็นหมวด ISCO กว้าง ไม่ได้แยกเฉพาะ data scientist
- **ลิงก์:**
  - [dataset] หน้า Bulk download: https://ilostat.ilo.org/data/bulk/
- **อ้างอิง:** International Labour Organization, ILOSTAT, https://ilostat.ilo.org/data/ (เข้าถึง 2026-10-05) — license: CC BY 4.0
- **ตรวจสอบ:** เปิดหน้า bulk download และอ่านโครงสร้างไฟล์ 2026-10-05

### S07 · อัตราว่างงานของผู้มีการศึกษาระดับสูง (% ของกำลังแรงงานที่มีการศึกษาระดับสูง) — World Bank API (ที่มา ILO EMI)

- **ผู้เผยแพร่:** World Bank (ข้อมูลต้นทาง ILOSTAT)
- **หัวข้อ:** แนวโน้ม AI / ว่างงานบัณฑิต / อื่น ๆ, ผู้สำเร็จการศึกษา/วุฒิ
- **ภูมิภาค:** ไทย, สิงคโปร์ (อาเซียน), สหรัฐฯ, หลายประเทศ/ทั่วโลก — รายประเทศ · ตัวอย่างค่าจากการเรียก API วันที่ 5 ต.ค. 2026: ไทย 1.707% (2024), 1.712% (2023); สิงคโปร์ 3.312% (2024); อินเดีย 13.47% (2024); สหรัฐฯ 2.927% (2025)
- **License:** CC BY 4.0 (ตามที่ World Bank ระบุบนหน้า indicator) ([ลิงก์](https://data.worldbank.org/indicator/SL.UEM.ADVN.ZS))
- **รูปแบบ:** JSON (API), CSV, XML, Excel
- **ช่วงเวลา:** ปี 2018–2025 ที่ตรวจ (API lastupdated 2026-07-13) · ค่าปี 2025 ของไทย/สิงคโปร์/อินเดียยังว่าง · ความใหม่: ใหม่
- **รายละเอียด:** ตัวชี้วัด SL.UEM.ADVN.ZS ดึงผ่าน REST API ได้โดยไม่ต้องมี API key ใช้เทียบ 'ความยากในการหางานของผู้จบระดับสูง' ข้ามประเทศ
- **ข้อควรระวัง:** 'การศึกษาระดับสูง' ตามนิยาม ILO ไม่ใช่เฉพาะสาขาสถิติ/AI · ค่าบางปีเป็น null · ตัวเลขเป็นตัวอย่างวันที่ตรวจ อาจถูกปรับย้อนหลัง
- **ลิงก์:**
  - [api] API (ไทย สิงคโปร์ อินเดีย สหรัฐฯ): https://api.worldbank.org/v2/country/THA;SGP;IND;USA/indicator/SL.UEM.ADVN.ZS?format=json&date=2018:2025&per_page=40
  - [dataset] หน้า indicator + ปุ่มดาวน์โหลด: https://data.worldbank.org/indicator/SL.UEM.ADVN.ZS
- **อ้างอิง:** World Bank, Unemployment with advanced education (SL.UEM.ADVN.ZS); source: ILOSTAT (EMI), CC BY 4.0, https://data.worldbank.org/indicator/SL.UEM.ADVN.ZS (เข้าถึง 2026-10-05)
- **ตรวจสอบ:** เรียก API สำเร็จ + เปิดหน้า indicator 2026-10-05

### S08 · Eurostat — ICT specialists in employment (isoc_sks_itspt)

- **ผู้เผยแพร่:** Eurostat (EU Labour Force Survey)
- **หัวข้อ:** การจ้างงานและความต้องการแรงงาน
- **ภูมิภาค:** ยุโรป (EU) — ประเทศ EU/EFTA/ผู้สมัคร · EU27 ปี 2025: 5.0% ของการจ้างงานรวม (2024: 4.9%, 2023: 4.8%) จากการเรียก API
- **License:** Eurostat free re-use policy (Commission Decision 2011/833/EU) — ต้องระบุแหล่งที่มา ([ลิงก์](https://ec.europa.eu/eurostat/web/main/help/copyright-notice))
- **รูปแบบ:** JSON (API), TSV/CSV ผ่าน Eurostat bulk/API
- **ช่วงเวลา:** 2004–2025 (API updated 2026-04-17) · บางปีเป็นค่าประมาณ (flag e/be) · ความใหม่: ใหม่
- **รายละเอียด:** สัดส่วนและจำนวนผู้จ้างงานกลุ่ม ICT specialists ตามนิยาม ISCO-08 ของ Eurostat/OECD · ชุดพี่น้อง (ตามผลค้นหา ยังไม่ได้เรียก API): isoc_sks_itspe (ตามระดับการศึกษา), isoc_sks_itsps (ตามเพศ)
- **ข้อควรระวัง:** นิยาม ICT specialists กว้างกว่าสาย data/AI/statistics · ข้อมูลของประเทศนอก EU/EFTA/ผู้สมัคร (เช่น สหรัฐฯ ญี่ปุ่น จีน) ห้ามใช้เชิงพาณิชย์ตามเงื่อนไข Eurostat
- **ลิงก์:**
  - [api] API ตัวอย่าง (EU27, % ของการจ้างงาน): https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/isoc_sks_itspt?format=JSON&geo=EU27_2020&unit=PC_EMP&lang=en
  - [license] เงื่อนไขการใช้ซ้ำ: https://ec.europa.eu/eurostat/web/main/help/copyright-notice
- **อ้างอิง:** Eurostat, Employed ICT specialists - total [isoc_sks_itspt], DOI 10.2908/ISOC_SKS_ITSPT, เข้าถึง 2026-10-05
- **ตรวจสอบ:** เรียก API สำเร็จ + เปิดหน้า copyright notice 2026-10-05

### S09 · Eurostat — Graduates by level, programme orientation, sex and field (educ_uoe_grad02)

- **ผู้เผยแพร่:** Eurostat (UOE data collection)
- **หัวข้อ:** ผู้สำเร็จการศึกษา/วุฒิ
- **ภูมิภาค:** ยุโรป (EU) — EU27 + ประเทศสมาชิก/อื่น ๆ · ระดับ ISCED 6 (ตรี) 7 (โท) 8 (เอก) · สาขา ISCED-F รวม F0541 Mathematics, F0542 Statistics, F06 ICT (เช่น F0613 Software and applications development and analysis)
- **License:** Eurostat free re-use policy (Commission Decision 2011/833/EU) — ต้องระบุแหล่งที่มา ([ลิงก์](https://ec.europa.eu/eurostat/web/main/help/copyright-notice))
- **รูปแบบ:** JSON (API), TSV/CSV ผ่าน Eurostat
- **ช่วงเวลา:** 2005–2024 (API updated 2026-08-26) · ~1.7 ล้านค่าสังเกต · ความใหม่: ใหม่
- **รายละเอียด:** จำนวนผู้สำเร็จการศึกษาจำแนกตามระดับ ตรี/โท/เอก และสาขา — เป็นแหล่ง 'ผู้จบสาขาสถิติและ ICT' ที่ละเอียดที่สุดที่ตรวจพบในกลุ่มที่ผ่านเกณฑ์
- **ข้อควรระวัง:** ตัวอย่าง API ดึงเฉพาะ EU27 ปี 2024 รวมเพศ (ปรับ geo/time/sex เองได้) · flag 'd' = นิยามต่างกันตามประเทศ · ไม่มีข้อมูลตลาดงาน/เงินเดือน
- **ลิงก์:**
  - [api] API ตัวอย่าง (EU27, ปีล่าสุด): https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/educ_uoe_grad02?format=JSON&lang=en&geo=EU27_2020&lastTimePeriod=1&sex=T
  - [license] เงื่อนไขการใช้ซ้ำ: https://ec.europa.eu/eurostat/web/main/help/copyright-notice
- **อ้างอิง:** Eurostat, Graduates by education level, programme orientation, sex and field of education [educ_uoe_grad02], DOI 10.2908/EDUC_UOE_GRAD02, เข้าถึง 2026-10-05
- **ตรวจสอบ:** เรียก API สำเร็จ 2026-10-05

### S10 · BLS Occupational Employment and Wage Statistics (OEWS) — May 2025

- **ผู้เผยแพร่:** U.S. Bureau of Labor Statistics
- **หัวข้อ:** การจ้างงานและความต้องการแรงงาน, เงินเดือน, บริษัท/อุตสาหกรรม
- **ภูมิภาค:** สหรัฐฯ — สหรัฐฯ ระดับประเทศ/รัฐ/เมือง/อุตสาหกรรม · ค้นหาอาชีพ เช่น Data Scientists (SOC 15-2051 ตาม URL หน้าอาชีพของ BLS) Statisticians Mathematicians ในไฟล์
- **License:** Public domain (งานของรัฐบาลสหรัฐฯ; BLS ขอให้อ้างอิงแหล่ง) ([ลิงก์](https://www.bls.gov/opub/copyright-information.htm))
- **รูปแบบ:** XLSX (zip), TXT time series
- **ช่วงเวลา:** May 2025 (หน้า tables แก้ไขล่าสุด 15 พ.ค. 2026) · มีย้อนหลังถึง 1988 · ความใหม่: ใหม่
- **รายละเอียด:** จำนวนผู้จ้างงานและค่าจ้าง (ค่าเฉลี่ยและเปอร์เซ็นไทล์) รายอาชีพ รายอุตสาหกรรม (ตอบหัวข้อ 'ภาคอุตสาหกรรมที่จ้างสายนี้') และรายพื้นที่
- **ข้อควรระวัง:** ค่าจ้างเป็นดอลลาร์สหรัฐ · ไม่มีรายชื่อบริษัท มีเฉพาะระดับอุตสาหกรรม · ไม่แยกตามปีประสบการณ์ (ใช้เปอร์เซ็นไทล์ค่าจ้างเป็นตัวแทนช่วงเงินเดือนได้เฉพาะเชิงประมาณ)
- **ลิงก์:**
  - [dataset] หน้า OEWS Tables: https://www.bls.gov/oes/tables.htm
  - [xlsx] National (May 2025): https://www.bls.gov/oes/special-requests/oesm25nat.zip
  - [xlsx] National industry-specific (May 2025): https://www.bls.gov/oes/special-requests/oesm25in4.zip
  - [xlsx] All data (May 2025): https://www.bls.gov/oes/special-requests/oesm25all.zip
  - [license] BLS Copyright Information: https://www.bls.gov/opub/copyright-information.htm
- **อ้างอิง:** U.S. Bureau of Labor Statistics, Occupational Employment and Wage Statistics, May 2025, https://www.bls.gov/oes/tables.htm (เข้าถึง 2026-10-05)
- **ตรวจสอบ:** เปิดหน้า tables และหน้า copyright 2026-10-05 (ยังไม่ได้ดาวน์โหลด zip)

### S11 · ONS Annual Survey of Hours and Earnings (ASHE) 2025 — รายได้ตามอาชีพ (SOC 2020)

- **ผู้เผยแพร่:** Office for National Statistics (UK)
- **หัวข้อ:** เงินเดือน
- **ภูมิภาค:** สหราชอาณาจักร — สหราชอาณาจักร · แยกตามอาชีพ อุตสาหกรรม ภูมิภาค กลุ่มอายุ
- **License:** Open Government Licence v3.0 ([ลิงก์](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/))
- **รูปแบบ:** XLSX/CSV (ตาราง ASHE)
- **ช่วงเวลา:** เมษายน 2025 (provisional) · เผยแพร่ 23 ต.ค. 2025 · ความใหม่: ใหม่
- **รายละเอียด:** รายได้ตามอาชีพ SOC 2020 (ถึงระดับ 4-digit) ใช้ประมาณค่าจ้างของอาชีพคล้าย data/statistics ในอังกฤษ ดึงไฟล์ได้จากหน้า related data ของ bulletin
- **ข้อควรระวัง:** ปี 2025 เป็น provisional · ตั้งแต่ 2023 อาจเทียบกับ 2022 และก่อนหน้าไม่ได้ตรง ๆ · ปี 2021 เปลี่ยน SOC 2010→2020 (ขาดตอนของอนุกรม) · ค่าเป็นปอนด์ · หน้าไฟล์ related data เป็นลิงก์จากหน้า bulletin ยังไม่ได้เปิดตรวจแยก
- **ลิงก์:**
  - [dataset] หน้า bulletin ASHE 2025: https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/bulletins/annualsurveyofhoursandearnings/2025
  - [files] หน้า related data (ยังไม่ได้เปิดตรวจแยก): https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/bulletins/annualsurveyofhoursandearnings/2025/relateddata
  - [license] OGL v3.0: http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- **อ้างอิง:** Office for National Statistics, Employee earnings in the UK: 2025 (ASHE), released 23 October 2025, OGL v3.0
- **ตรวจสอบ:** เปิดหน้า bulletin (ข้อความ OGL ท้ายหน้า) 2026-10-05

### S12 · จำนวนผู้สำเร็จการศึกษา จำแนกตามกลุ่มสาขาวิชา 10 กลุ่ม (10 GROUP ISCED) — ประเทศไทย

- **ผู้เผยแพร่:** สำนักงานส่งเสริมเศรษฐกิจสร้างสรรค์ (CEA) · ข้อมูลต้นทาง สป.อว. (MHESI)
- **หัวข้อ:** ผู้สำเร็จการศึกษา/วุฒิ
- **ภูมิภาค:** ไทย — สถาบันอุดมศึกษาไทย (รัฐ เอกชน และนอกสังกัด) · จำแนกตามระดับ ปริญญาตรี/โท/เอก และกลุ่มสาขา UNESCO
- **License:** Creative Commons Attributions (ตามที่ data.go.th ระบุ ไม่ระบุเวอร์ชัน) ภายใต้ DGA Open Government License ([ลิงก์](https://data.go.th/en/pages/dga-open-government-license))
- **รูปแบบ:** CSV, XLSX (data dictionary)
- **ช่วงเวลา:** ปีการศึกษา 2561–2566 (ค.ศ. 2018–2023) · อัปเดต 2024-08-15 · ความใหม่: ⚠️ ระวัง (เก่า ~3 ปี)
- **รายละเอียด:** จำนวนผู้สำเร็จการศึกษาไทยรายกลุ่มสาขา (UNESCO ISCED 10 กลุ่ม) พร้อมระดับการศึกษา — แหล่งหลักสำหรับหัวข้อ 'ผู้สำเร็จการศึกษา ป.ตรี/โท/เอก' ของไทยที่ตรวจพบ
- **ข้อควรระวัง:** ข้อมูลล่าสุดปี 2566 (ค.ศ. 2023) ใกล้เกณฑ์ 3 ปี · จำแนกแค่ 10 กลุ่มสาขา — ต้องเปิดไฟล์ดูว่ามีกลุ่ม 'วิทยาศาสตร์ธรรมชาติ คณิตศาสตร์และสถิติ' และ 'ICT' แยกกันหรือไม่ (ยังไม่ได้ยืนยัน) · ข้อความ license ไม่ระบุเวอร์ชัน CC และยังไม่ได้อ่านไฟล์ PDF เงื่อนไข DGA
- **ลิงก์:**
  - [dataset] หน้า dataset (CSV + data dictionary): https://data.go.th/en/dataset/education-creative1
  - [license] เงื่อนไข DGA Open Government License (หน้าเว็บ มีลิงก์ PDF): https://data.go.th/en/pages/dga-open-government-license
- **อ้างอิง:** สำนักงานส่งเสริมเศรษฐกิจสร้างสรรค์ (องค์การมหาชน) / สป.อว., จำนวนผู้สำเร็จการศึกษา จำแนกตามกลุ่มสาขาวิชา 10 กลุ่ม, data.go.th, License: Creative Commons Attributions
- **ตรวจสอบ:** เปิดหน้า dataset 2026-10-05

### S13 · ค่าจ้างเฉลี่ยของลูกจ้าง (จำแนกตามระดับการศึกษา เพศ อายุ ภาค อุตสาหกรรม) — สำนักงานสถิติแห่งชาติ

- **ผู้เผยแพร่:** สำนักงานสถิติแห่งชาติ (NSO) ผ่าน data.go.th
- **หัวข้อ:** เงินเดือน
- **ภูมิภาค:** ไทย — ประเทศไทย · ที่มา: การสำรวจภาวะการทำงานของประชากร · หน่วย: บาทต่อเดือน
- **License:** Creative Commons Attributions (ตามที่ data.go.th ระบุ ไม่ระบุเวอร์ชัน) ([ลิงก์](https://data.go.th/en/pages/dga-open-government-license))
- **รูปแบบ:** CSV, JSON
- **ช่วงเวลา:** ปี 2561–2562 (ค.ศ. 2018–2019) · หน้า dataset แก้ไข 2026-09-24 แต่ปีข้อมูลสุดท้ายยังเป็น 2562 · ความใหม่: ⚠️ เก่ากว่า 3 ปี
- **รายละเอียด:** ค่าจ้างเฉลี่ยรายเดือนของลูกจ้างไทยตามระดับการศึกษา (รวมระดับอุดมศึกษา) ใช้เป็นเส้นฐานย้อนหลังเท่านั้น
- **ข้อควรระวัง:** ข้อมูลเก่ากว่า 3 ปี — ใช้เทียบเชิงประวัติเท่านั้น ห้ามใช้เป็นเงินเดือนปัจจุบัน · ไม่มีการแยกรายอาชีพ/สายงาน · ไม่พบชุดข้อมูลเปิดของไทยที่ใหม่กว่านี้ซึ่งผ่านเกณฑ์
- **ลิงก์:**
  - [dataset] หน้า dataset (CSV/JSON หลายไฟล์): https://data.go.th/en/dataset/0706_02_0019
- **อ้างอิง:** สำนักงานสถิติแห่งชาติ, ค่าจ้างเฉลี่ยของลูกจ้าง, data.go.th, License: Creative Commons Attributions
- **ตรวจสอบ:** เปิดหน้า dataset 2026-10-05

### S14 · Employed Residents Aged 15+ by Occupation, Highest Qualification Attained and Sex — Singapore

- **ผู้เผยแพร่:** Ministry of Manpower (MOM) ผ่าน data.gov.sg
- **หัวข้อ:** การจ้างงานและความต้องการแรงงาน, ผู้สำเร็จการศึกษา/วุฒิ
- **ภูมิภาค:** สิงคโปร์ (อาเซียน) — พลเมืองและผู้มีถิ่นฐานถาวรของสิงคโปร์ (ไม่รวมแรงงานต่างชาติ) · จัดตาม SSOC 2024 · เดือนอ้างอิง มิ.ย.
- **License:** Singapore Open Data Licence v1.0 (ใช้เชิงพาณิชย์/ดัดแปลงได้ ต้องใส่ข้อความอ้างอิงและลิงก์ license) ([ลิงก์](https://data.gov.sg/open-data-licence))
- **รูปแบบ:** CSV (117.9 KB), API (datastore_search)
- **ช่วงเวลา:** 2010–2025 · อัปเดต 27 มี.ค. 2026 · ความใหม่: ใหม่
- **รายละเอียด:** จำนวนผู้มีงานทำจำแนกตามหมวดอาชีพและวุฒิการศึกษาสูงสุด (รวมระดับปริญญา) 5 คอลัมน์: Year, Sex, Occupation, Highest Qualification Attained, Employed
- **ข้อควรระวัง:** หมวดอาชีพกว้าง (เช่น managers, professionals) ไม่เจาะเฉพาะ data/AI/statistics · เฉพาะ citizens/PR
- **ลิงก์:**
  - [dataset] หน้า dataset (ปุ่ม Download CSV): https://data.gov.sg/datasets/d_576bb1f46eabb041d8d966030170ec6f/view
  - [api] API (ตามตัวอย่างบนหน้า dataset; ยังไม่ได้เรียกตรวจ): https://data.gov.sg/api/action/datastore_search?resource_id=d_576bb1f46eabb041d8d966030170ec6f
  - [license] Singapore Open Data Licence: https://data.gov.sg/open-data-licence
- **อ้างอิง:** Contains information from Employed Residents Aged 15 Years & Over by Occupation, Highest Qualification Attained And Sex accessed 2026-10-05 from Ministry of Manpower (data.gov.sg) which is made available under the terms of the Singapore Open Data Licence version 1.0 https://data.gov.sg/open-data-licence
- **ตรวจสอบ:** เปิดหน้า dataset และหน้า license 2026-10-05

### S15 · Graduate Employment Survey — NTU, NUS, SIT, SMU, SUSS & SUTD (เงินเดือนเริ่มต้นรายหลักสูตร)

- **ผู้เผยแพร่:** Ministry of Education (MOE) สิงคโปร์ ผ่าน data.gov.sg
- **หัวข้อ:** เงินเดือน, แนวโน้ม AI / ว่างงานบัณฑิต / อื่น ๆ
- **ภูมิภาค:** สิงคโปร์ (อาเซียน) — บัณฑิตรายมหาวิทยาลัย/คณะ/หลักสูตร · สำรวจ ~6 เดือนหลังสอบจบ · เงินเดือนเป็นดอลลาร์สิงคโปร์
- **License:** Singapore Open Data Licence v1.0 (ใช้เชิงพาณิชย์/ดัดแปลงได้ ต้องใส่ข้อความอ้างอิงและลิงก์ license) ([ลิงก์](https://data.gov.sg/open-data-licence))
- **รูปแบบ:** CSV (226.2 KB), API (datastore_search)
- **ช่วงเวลา:** Nov 2013 – Mar 2025 · อัปเดต 5 มี.ค. 2026 · ความใหม่: ใหม่
- **รายละเอียด:** 12 คอลัมน์: Year, University, School, Degree, อัตราการมีงานทำรวม, อัตราการมีงานทำแบบเต็มเวลาประจำ, เงินเดือนพื้นฐาน (mean/median), เงินเดือนรวม gross (mean/median/25th/75th percentile) — ใช้ค้นหาหลักสูตรด้าน data science/AI/statistics ด้วยชื่อ Degree
- **ข้อควรระวัง:** เงินเดือนนับเฉพาะผู้ทำงานเต็มเวลาแบบประจำ · คอลัมน์ตัวเลขถูกระบุเป็น Text (มีค่า null/สัญลักษณ์พิเศษ ต้องทำความสะอาด) · บางหลักสูตรไม่มีข้อมูลเพราะกลุ่มตัวอย่างเล็ก/response rate ต่ำ · เป็นเงินเดือนแรกเข้า ไม่ใช่ตามประสบการณ์
- **ลิงก์:**
  - [dataset] หน้า dataset (ปุ่ม Download CSV): https://data.gov.sg/datasets/d_3c55210de27fcccda2ed0c63fdd2b352/view
  - [api] API (ตามตัวอย่างบนหน้า dataset; ยังไม่ได้เรียกตรวจ): https://data.gov.sg/api/action/datastore_search?resource_id=d_3c55210de27fcccda2ed0c63fdd2b352
  - [license] Singapore Open Data Licence: https://data.gov.sg/open-data-licence
- **อ้างอิง:** Contains information from Graduate Employment Survey - NTU, NUS, SIT, SMU, SUSS & SUTD accessed 2026-10-05 from Ministry of Education (data.gov.sg) which is made available under the terms of the Singapore Open Data Licence version 1.0 https://data.gov.sg/open-data-licence
- **ตรวจสอบ:** เปิดหน้า dataset (เห็นคอลัมน์และข้อมูลตัวอย่าง) 2026-10-05


## 2. ต้องตรวจสอบ license เพิ่มเติม

### R01 · ESCO (European Skills, Competences, Qualifications and Occupations) v1.2.1

- **ผู้เผยแพร่:** European Commission (DG EMPL)
- **หัวข้อ:** ทักษะ
- **ภูมิภาค:** ยุโรป (EU), หลายประเทศ/ทั่วโลก — อาชีพ (อิง ISCO-08) และทักษะ/สมรรถนะ 28 ภาษา
- **License:** ไม่พบข้อความ license ในหน้าที่เปิดตรวจ ([ลิงก์](https://esco.ec.europa.eu/en/use-esco/download))
- **รูปแบบ:** CSV, ODS, RDF/TTL, XML, JSON-LD
- **ช่วงเวลา:** v1.2.1 (หน้าระบุอัปเดต 10/12/2025) · ความใหม่: ใหม่
- **รายละเอียด:** อภิธานศัพท์อาชีพ-ทักษะที่ใช้ในตลาดงานยุโรป เหมาะใช้เป็นตัวจับคู่ชื่อทักษะ/อาชีพ
- **ข้อควรระวัง:** เหตุที่อยู่กลุ่มนี้: (1) ขั้นตอนดาวน์โหลดให้ยอมรับ privacy statement และกรอกอีเมลเพื่อรับลิงก์ ไม่ใช่ลิงก์ตรง (2) หน้าที่เปิดตรวจไม่แสดง license ชัดเจน — ต้องอ่านเงื่อนไขการใช้ซ้ำของ European Commission ก่อนนำไปใช้
- **ลิงก์:**
  - [dataset] หน้า Download ESCO: https://esco.ec.europa.eu/en/use-esco/download
- **อ้างอิง:** -
- **ตรวจสอบ:** เปิดหน้า download 2026-10-05

### R02 · DOL OFLC — LCA Disclosure Data (H-1B/H-1B1/E-3): ชื่อนายจ้าง ตำแหน่ง ค่าจ้าง ระดับค่าจ้าง I–IV

- **ผู้เผยแพร่:** U.S. Department of Labor, Office of Foreign Labor Certification
- **หัวข้อ:** เงินเดือน, บริษัท/อุตสาหกรรม, ระดับสายงาน
- **ภูมิภาค:** สหรัฐฯ — คำขอ Labor Condition Application ที่นายจ้างยื่น (รายละเอียดฟิลด์ตามแหล่งรองที่ค้นพบ: ชื่อนายจ้าง job title SOC ค่าจ้างที่เสนอ prevailing wage wage level worksite)
- **License:** ไม่พบข้อความ license บนหน้าที่เปิดตรวจ (เอกสารของรัฐบาลสหรัฐฯ) ([ลิงก์](https://www.dol.gov/agencies/eta/foreign-labor/performance))
- **รูปแบบ:** XLSX (รายไตรมาส/ปีงบประมาณ ตามแหล่งรอง)
- **ช่วงเวลา:** ไม่ได้ยืนยันปีล่าสุดจากหน้าที่เปิด · ความใหม่: ⚠️ ระวัง (เก่า ~3 ปี)
- **รายละเอียด:** เป็นแหล่งเดียวที่พบซึ่งมีชื่อนายจ้างรายบริษัทพร้อมค่าจ้างต่อตำแหน่ง (หัวข้อ 5 และ 7) แต่เป็นเฉพาะตำแหน่งที่สปอนเซอร์วีซ่าในสหรัฐฯ
- **ข้อควรระวัง:** เหตุที่อยู่กลุ่มนี้: หน้า DOL ที่เปิดตรวจแสดงรายการไฟล์ดาวน์โหลดไม่ครบในผลที่ดึงได้ และไม่มีข้อความ license/ลิขสิทธิ์ · ต้องตรวจเองว่าไฟล์ล่าสุดคือปีงบประมาณใด · ข้อมูลนายจ้างยื่นเอง ไม่ใช่ตัวแทนตลาดงานทั้งหมด · ห้ามใช้เว็บของบุคคลที่สามที่รวบรวมข้อมูลนี้แทน
- **ลิงก์:**
  - [dataset] หน้า Performance Data (Disclosure Data): https://www.dol.gov/agencies/eta/foreign-labor/performance
- **อ้างอิง:** -
- **ตรวจสอบ:** เปิดหน้า 2026-10-05 (ไม่เห็นรายการไฟล์ในผลที่ดึงได้)

### R03 · NCES IPEDS — Completions (ปริญญาตามสาขา CIP ของสถาบันในสหรัฐฯ)

- **ผู้เผยแพร่:** U.S. National Center for Education Statistics (NCES)
- **หัวข้อ:** ผู้สำเร็จการศึกษา/วุฒิ
- **ภูมิภาค:** สหรัฐฯ — จำนวนปริญญา/ประกาศนียบัตรรายสถาบัน ระดับรางวัล และรหัสสาขา CIP 6 หลัก
- **License:** ไม่พบข้อความ license บนหน้าที่เปิดตรวจ ([ลิงก์](https://nces.ed.gov/ipeds/use-the-data))
- **รูปแบบ:** CSV (zip), Access database
- **ช่วงเวลา:** Complete Data Files ตั้งแต่ปีเก็บข้อมูล 1980-81 (ปีล่าสุดไม่ได้ยืนยัน) · ความใหม่: ⚠️ ระวัง (เก่า ~3 ปี)
- **รายละเอียด:** ดาวน์โหลดไฟล์ข้อมูลสมบูรณ์หรือ Custom Data Files ได้ฟรีผ่าน IPEDS Data Center — ใช้นับผู้จบสาขา statistics / data science / computer science ตามรหัส CIP
- **ข้อควรระวัง:** เหตุที่อยู่กลุ่มนี้: หน้าไม่ระบุ license/สถานะ public domain ชัดเจน (โดยปกติเป็นข้อมูลของรัฐบาลสหรัฐฯ แต่ยังไม่ได้ยืนยันจากข้อความทางการ) · ไม่ได้ทดสอบดาวน์โหลดไฟล์จริง
- **ลิงก์:**
  - [dataset] หน้า Use the Data (Complete Data Files / Custom Data Files): https://nces.ed.gov/ipeds/use-the-data
- **อ้างอิง:** -
- **ตรวจสอบ:** เปิดหน้า 2026-10-05


## 3. ตัดออก (ไม่ผ่านเกณฑ์)

### X01 · สำเนา Indeed Job Postings Index บน FRED (St. Louis Fed)

- **ผู้เผยแพร่:** FRED
- **หัวข้อ:** การจ้างงานและความต้องการแรงงาน
- **ภูมิภาค:** สหรัฐฯ — -
- **License:** เงื่อนไขจำกัดการเผยแพร่ซ้ำ
- **รูปแบบ:** 
- **ช่วงเวลา:** - · ความใหม่: ใหม่
- **รายละเอียด:** หน้า FRED ระบุให้ติดต่อ Indeed เพื่อขออนุญาตใช้ข้อมูล ห้ามเผยแพร่ภายนอกเกินที่กำหนด และห้ามขาย/ส่งต่อให้บุคคลที่สาม
- **ข้อควรระวัง:** ตัดออก: เงื่อนไขขัดกับเกณฑ์ 'ไม่ต้องขออนุญาต/ใช้ซ้ำได้' — ให้ใช้ต้นฉบับ CC BY 4.0 (S01)
- **ลิงก์:**
- **อ้างอิง:** -
- **ตรวจสอบ:** อ่านจากผลค้นหา (หน้า FRED/ALFRED) 2026-10-05

### X02 · Internet Vacancy Index (ออสเตรเลีย) บน data.gov.au

- **ผู้เผยแพร่:** Dept. of Employment and Workplace Relations
- **หัวข้อ:** การจ้างงานและความต้องการแรงงาน
- **ภูมิภาค:** ประเทศอื่น (CA AU DE FR ฯลฯ) — -
- **License:** ไม่ระบุ (Not Specified)
- **รูปแบบ:** 
- **ช่วงเวลา:** - · ความใหม่: ⚠️ ระวัง (เก่า ~3 ปี)
- **รายละเอียด:** แคตตาล็อก data.gov.au แสดง License = 'Not Specified'
- **ข้อควรระวัง:** ตัดออกตามกฎ 'ไม่ระบุ license' (ไม่ได้เปิดดูหน้าของ jobsandskills.gov.au เพิ่มเติม)
- **ลิงก์:**
- **อ้างอิง:** -
- **ตรวจสอบ:** อ่านจากผลค้นหา 2026-10-05

### X03 · India Periodic Labour Force Survey (PLFS) Microdata

- **ผู้เผยแพร่:** MoSPI (microdata.gov.in)
- **หัวข้อ:** การจ้างงานและความต้องการแรงงาน, ผู้สำเร็จการศึกษา/วุฒิ
- **ภูมิภาค:** ประเทศอื่น (CA AU DE FR ฯลฯ) — -
- **License:** ไม่ได้ตรวจ
- **รูปแบบ:** 
- **ช่วงเวลา:** - · ความใหม่: ใหม่
- **รายละเอียด:** หน้า dataset ที่พบมีเมนู Login และปุ่ม 'Get Microdata'
- **ข้อควรระวัง:** ตัดออก: ยืนยันไม่ได้ว่าดาวน์โหลดได้โดยไม่ลงทะเบียน (ไม่ได้ทดลองดาวน์โหลด) — ข้อมูลอินเดียระดับรวมให้ดู S06/S07
- **ลิงก์:**
- **อ้างอิง:** -
- **ตรวจสอบ:** อ่านจากผลค้นหา 2026-10-05

### X04 · HESA (UK) — Graduates / Graduate Outcomes open data

- **ผู้เผยแพร่:** HESA (Jisc)
- **หัวข้อ:** ผู้สำเร็จการศึกษา/วุฒิ, เงินเดือน
- **ภูมิภาค:** สหราชอาณาจักร — -
- **License:** ผลค้นหาระบุ CC BY 4.0 แต่ตรวจเปิดหน้าไม่สำเร็จ
- **รูปแบบ:** 
- **ช่วงเวลา:** - · ความใหม่: ใหม่
- **รายละเอียด:** ตารางผู้สำเร็จการศึกษาและผลลัพธ์การมีงานทำตามสาขา
- **ข้อควรระวัง:** ตัดออกตามกฎ 'เปิดตรวจไม่ได้ให้ตัดออก': หน้า table ถูกบล็อกบอท และหน้าที่เปิดได้เป็นเนื้อหาเก่า (2016/17) ไม่แสดง license — ผู้ใช้ควรเปิดตรวจเองที่ hesa.ac.uk/data-and-analysis
- **ลิงก์:**
- **อ้างอิง:** -
- **ตรวจสอบ:** WebFetch ถูกบล็อก 2026-10-05

### X05 · OECD Education at a Glance / OECD Data Explorer (graduates by field)

- **ผู้เผยแพร่:** OECD
- **หัวข้อ:** ผู้สำเร็จการศึกษา/วุฒิ, แนวโน้ม AI / ว่างงานบัณฑิต / อื่น ๆ
- **ภูมิภาค:** หลายประเทศ/ทั่วโลก — -
- **License:** ยืนยันไม่ได้
- **รูปแบบ:** 
- **ช่วงเวลา:** - · ความใหม่: ใหม่
- **รายละเอียด:** มีข้อมูลผู้สำเร็จการศึกษาตามสาขาและการจ้างงานตามสาขา
- **ข้อควรระวัง:** ตัดออก: หน้า Terms ที่เปิดได้แสดงเฉพาะเมนูเว็บ (ไม่เห็นข้อความ license) และยังไม่ได้เปิดลิงก์ dataset รายตัว — ใช้ Eurostat (S09) สำหรับยุโรปแทน
- **ลิงก์:**
- **อ้างอิง:** -
- **ตรวจสอบ:** เปิดหน้า Terms 2026-10-05 (ข้อความ license ไม่ปรากฏ)

### X06 · รายงานการสำรวจภาวะการทำงานของประชากร (PDF) จาก NSO และสำเนา 'Open Development Mekong'

- **ผู้เผยแพร่:** NSO ไทย / Open Development Mekong
- **หัวข้อ:** การจ้างงานและความต้องการแรงงาน
- **ภูมิภาค:** ไทย — -
- **License:** ไม่ระบุ/Unclear
- **รูปแบบ:** PDF
- **ช่วงเวลา:** สำเนา ODM: ปี 2015 · ความใหม่: ⚠️ เก่ากว่า 3 ปี
- **รายละเอียด:** สำเนาบน Open Development Mekong ระบุ Copyright 'Unclear copyright' และ License 'unspecified' และข้อมูลปี 2015
- **ข้อควรระวัง:** ตัดออก: ไม่ระบุ license + เป็น PDF + ข้อมูลเก่า · ไม่ได้เปิดตรวจ PDF ของ NSO — ใช้ตารางใน data.go.th (S12–S13) แทน
- **ลิงก์:**
- **อ้างอิง:** -
- **ตรวจสอบ:** อ่านจากผลค้นหา 2026-10-05

### X07 · เว็บรวบรวมข้อมูล H-1B / เงินเดือนของบุคคลที่สาม (เช่น H1BData.info, Levels.fyi, Apify actors)

- **ผู้เผยแพร่:** ผู้ให้บริการเอกชน
- **หัวข้อ:** เงินเดือน, บริษัท/อุตสาหกรรม
- **ภูมิภาค:** สหรัฐฯ — -
- **License:** ไม่ระบุ/เป็นเงื่อนไขของเว็บ
- **รูปแบบ:** 
- **ช่วงเวลา:** - · ความใหม่: ใหม่
- **รายละเอียด:** รวบรวมจากไฟล์ของรัฐบาลสหรัฐฯ
- **ข้อควรระวัง:** ตัดออก: ไม่ใช่แหล่งต้นทาง ไม่ได้ยืนยัน license/ToS — ใช้ไฟล์ต้นทางจาก OFLC (R02) แทน
- **ลิงก์:**
- **อ้างอิง:** -
- **ตรวจสอบ:** อ่านจากผลค้นหา 2026-10-05

### X08 · รายงาน Graduate Employment Survey ของ MOE สิงคโปร์ (PDF) และบทความสรุปเงินเดือนของเว็บเอกชน/Statista

- **ผู้เผยแพร่:** MOE / เว็บเอกชน
- **หัวข้อ:** เงินเดือน
- **ภูมิภาค:** สิงคโปร์ (อาเซียน) — -
- **License:** ไม่ระบุ
- **รูปแบบ:** PDF
- **ช่วงเวลา:** - · ความใหม่: ใหม่
- **รายละเอียด:** ไฟล์ PDF รายมหาวิทยาลัย และบทความสรุป
- **ข้อควรระวัง:** ตัดออก: PDF เท่านั้น/ไม่ระบุ license/เนื้อหา premium — ใช้ชุด CSV บน data.gov.sg (S15) แทน
- **ลิงก์:**
- **อ้างอิง:** -
- **ตรวจสอบ:** อ่านจากผลค้นหา 2026-10-05


## ตารางครอบคลุมตามหัวข้อ

| หัวข้อ | แหล่งที่ใช้ | ช่องว่าง |
|---|---|---|
| 1. ปริมาณการจ้างงาน/ความต้องการแรงงาน | S01, S02, S06, S08, S10, S14 | ไม่พบข้อมูลประกาศงานของไทย/อาเซียนที่เป็น Open Data · ไม่มีชุดที่นับจำนวนตำแหน่ง 'Data Scientist/AI Engineer' รายประเทศแบบเปิดนอกจาก BLS (สหรัฐฯ) |
| 2. จำนวนผู้สำเร็จการศึกษา (ป.ตรี/โท/เอก) | S12, S09, S14, S07 | ไทย: จำแนกแค่ 10 กลุ่มสาขา (ยังไม่ยืนยันว่าแยกสถิติ/ICT) ข้อมูลล่าสุด 2023 · อาเซียนอื่น/อินเดีย/สหราชอาณาจักร/สหรัฐฯ: ไม่มีแหล่งที่ผ่านเกณฑ์ครบ (IPEDS อยู่กลุ่มตรวจสอบ HESA/OECD ตัดออก) |
| 3. เงินเดือนเริ่มต้นและช่วงเงินเดือนตามประสบการณ์ | S10, S11, S15, S05, S13 | ไม่พบเงินเดือนเริ่มต้นสายข้อมูล/AI ของไทยที่เป็น Open Data (S13 มีเฉพาะตามระดับการศึกษา ปี 2018–2019) · เงินเดือนตามปีประสบการณ์โดยตรงมีเฉพาะจากแบบสำรวจสมัครใจ (S05) หรือ LCA (R02 กลุ่มตรวจสอบ) |
| 4. ประเทศ/ภูมิภาค | S12, S13, S14, S15, S10, S03, S11, S08, S09, S01, S06, S07, S05 | ไทย: S12 S13 · สิงคโปร์: S14 S15 · สหรัฐฯ: S10 S03 · สหราชอาณาจักร: S11 S01 · ยุโรป: S08 S09 · ข้ามประเทศ: S06 S07 S05 · อินเดีย: ไม่มีแหล่งเฉพาะที่ผ่านเกณฑ์ (ใช้ S06/S07 ระดับรวม) · อาเซียนอื่น (มาเลเซีย เวียดนาม ฯลฯ): ไม่ได้ค้นเจาะรายประเทศในรอบนี้ |
| 5. บริษัท/องค์กรที่จ้างงาน | S10 | ไม่พบแหล่งข้อมูลเปิดที่ผ่านเกณฑ์สำหรับรายชื่อบริษัท ขนาด และอุตสาหกรรมของนายจ้างสายนี้ · S10 ให้ระดับอุตสาหกรรมของสหรัฐฯ เท่านั้น · รายชื่อนายจ้างพร้อมค่าจ้างมีเฉพาะ R02 (กลุ่มต้องตรวจสอบ license) |
| 6. ทักษะที่ระบุในใบสมัครงาน | S03, S05, S02, R01 | ไม่พบชุดข้อมูลเปิดของ 'ข้อความประกาศงาน' ที่ผ่านเกณฑ์ · S03 (ทักษะรายอาชีพ) และ S05 (เครื่องมือที่นักพัฒนาใช้) เป็นตัวแทนทางอ้อม · S02 วัดสัดส่วนประกาศที่มีคำเกี่ยวกับ AI เท่านั้น |
| 7. การแบ่งระดับสายงาน Entry/Mid/Senior | S03, S10, S05, R02 | ไม่พบแหล่งข้อมูลเปิดที่ให้เกณฑ์ปีประสบการณ์ ชื่อตำแหน่ง และเงินเดือนของแต่ละระดับครบในชุดเดียว · ใช้ประกอบ: S03 (Job Zones, Training and Experience, Job Titles), S10 (เปอร์เซ็นไทล์ค่าจ้างเป็นตัวแทนช่วง), S05 (ปีประสบการณ์ x ค่าตอบแทน) และ R02 (wage level I–IV; กลุ่มตรวจสอบ) — การกำหนดเส้นแบ่งระดับเป็นขั้นตอนวิเคราะห์ของผู้ใช้ ไม่ใช่ข้อมูลสำเร็จรูป |
| 8. ข้อมูลอื่นที่จำเป็น (AI, ตำแหน่งใหม่, ว่างงานบัณฑิต, remote) | S02, S04, S07, S15, S05, S03 | ตำแหน่งใหม่ (ML Engineer / AI Engineer / Biostatistician): ใช้ชื่อตำแหน่งใน S03 (job_titles/emerging_tasks) ค้นหา — ไม่มีชุดที่นับตำแหน่งใหม่โดยตรง · remote: มีเฉพาะคำถามใน S05 · ไม่พบ Hybrid/Remote tracker ของ Indeed ที่ยืนยัน license ในรอบนี้ |

## หมายเหตุ

- ทุกรายการในกลุ่ม 'ผ่านเกณฑ์' เก็บฟิลด์ license, license_url, citation ไว้แล้ว — เวลาเผยแพร่งานวิเคราะห์ให้ใส่ข้อความอ้างอิงตามฟิลด์ citation และตรวจ license ซ้ำที่หน้าต้นทาง
- อาชีพถูกจัดหมวดคนละระบบ: BLS/O*NET = SOC, ONS = SOC 2020 (UK), ILOSTAT/Eurostat = ISCO-08, สิงคโปร์ = SSOC 2024 — ต้องทำ crosswalk ก่อนเทียบข้ามประเทศ
- สกุลเงินและช่วงเวลาไม่ตรงกัน (USD, GBP, SGD, THB; ปีข้อมูล 2018–2026) — ปรับเป็นสกุลเดียวและปีเดียวกัน หรือเทียบเฉพาะอัตราส่วน/อันดับ
- ข้อมูลไทยที่พบเก่ากว่า/หยาบกว่าชาติอื่นอย่างชัดเจน (S13 ปี 2018–2019, S12 ถึงปี 2023) — อย่าสรุปเงินเดือนปัจจุบันของไทยจากแหล่งเหล่านี้
- ตัวเลขตัวอย่างใน S07 และ S08 มาจากการเรียก API วันที่ตรวจ ควรเรียกใหม่เมื่อใช้งานจริง
- S04 จัดทำโดย Anthropic ซึ่งเป็นผู้พัฒนา Claude ที่จัดทำหน้านี้ — ควรแจ้งไว้ในรายงานและเทียบกับแหล่งอื่นก่อนอ้างข้อสรุป
- รายการที่ 'ไม่ได้เปิดตรวจแยก' หรือ 'ยังไม่ได้ดาวน์โหลดไฟล์' ถูกระบุไว้ในช่อง verified/caveat ของแต่ละรายการ — ให้ AI ตัวถัดไปทดสอบดาวน์โหลดจริงก่อนวางไปป์ไลน์
