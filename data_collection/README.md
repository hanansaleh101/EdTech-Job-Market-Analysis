# Data Collection & ETL Pipeline

## 🎯 Overview
This directory contains the custom Python automation pipeline built to source and structure job market data for the Education & EdTech sector.

## 💻 Scripts
* **`discover_careers.py`**: Uses Python (`pandas` and DuckDuckGo search automation) to programmatically query company career pages while filtering out job aggregators (LinkedIn, Indeed) and bad domains.
* **`detect_ats.py`**: Scans extracted URLs to automatically identify and fingerprint underlying Applicant Tracking Systems (ATS) like Greenhouse, Lever, Ashby, and Workday.