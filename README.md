# Education & EdTech Data Analyst Job Market Analysis (2025–2026)

## 🎯 Project Motivation & Background
As a data analyst and former educator looking to transition into the EdTech sector, I needed data-driven clarity on the current job market. I built this project to uncover common patterns, technical requirements, and core business problems across data roles in EdTech companies and educational institutions to guide targeted portfolio development and job hunting.

---

## ❓ Key Questions Answered by the Dashboard
This project and interactive Power BI dashboard directly answer critical market questions:
* **Which company types hire the most data analysts?**
* **Which seniority levels do job postings ask for the most?**
* **How do years of experience align with seniority?**
* **Where are data roles in Education located?**
* **How many remote vs. on-site roles exist?**
* **Is a specialized degree required?**
* **What are the most common business objectives tackled by data analysts in EdTech?**
* **Do education data jobs require AI or automation skills?**
* **Which technical skills are most in-demand?**

---

## 📊 Dashboard Preview

### Overview & Market Breakdown
![Dashboard Overview](Resources/overview.png)

### Technical Stack & AI Integration
![Skills & AI Breakdown](Resources/Skills.png)

---

## 🛠️ Tech Stack & Methodology
* **Data Collection & Engineering:** Custom Python automation scripts (`discover_careers.py`, `detect_ats.py`) utilizing DuckDuckGo search queries and Pandas to scrape and fingerprint Applicant Tracking Systems (ATS) for the GSV 150 top EdTech companies, alongside regional and startup lists.
* **ETL & Data Cleaning:** Location extraction, company categorization, seniority mapping, experience bracketing, and unpivoting technical skills.
* **Visualization:** Microsoft Power BI (DAX, custom measures, interactive mapping, and cross-filtering).

---

## 📂 Repository Structure
* `dashboard/` — Contains the Power BI file (`Final.pbix`) and clean analytical dataset (`Final.xlsx`).
* `data-collection/` — Contains the Python automation and ATS-detection scripts.
* `Resources/` — Image assets used for documentation previews.