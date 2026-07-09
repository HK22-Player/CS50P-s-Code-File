# Harvard CS50P: Complete Portfolio & Capstone Project
This repository document my full journey through Harvard University's CS50P (Introduction to Programming with Python), showcasing weekly problem sets and a custom data analytics capstone engine.

## 🚀 Capstone Feature: AUTOMATE DATA ANALYZER (CLI Tool)
Located inside the `/Final Project` directory, this software bridges theoretical high school statistics with dynamic programmatic automation. 

* **Video Walkthrough:** [Watch the Application Demo on YouTube](https://youtu.be)

### 🎯 Motivation & Origin
During my eleventh grade at SMAK PENABUR, I achieved a 99% score in Advanced Statistics, specifically focusing on linear regression and correlation analysis. Realizing the excessive manual friction and time consumed during data cleaning and calculation, I developed this Python pipeline to automate descriptive analysis and project future trends instantly.

### 🛠️ Core Technical Features
1. **Automated Data Validation:** Functions as a strict programmatic gatekeeper. The system instantly rejects any uploaded file if it contains fewer than 3 rows, exhibits empty cells (Null/NaN), or includes text strings inside numerical data via rigorous `pd.to_numeric` parsing.
2. **Descriptive Statistics Module:** Once verified, the engine leverages the `pandas` library to calculate instant mathematical summaries, including Mean, Median, and Standard Deviation for user-selected variables.
3. **Linear Regression Analysis:** Utilizes the `scipy` library to compute the exact prediction formula ($Y = mX + c$), find the R-Squared correlation strength, calculate the P-Value, and output an automated conclusion regarding variable influence.

## 📂 Repository Structure
- `project.py`: The core application containing user prompts, data validation logic, and the statistical calculations.
- `test_project.py`: Dedicated test suite powered by `pytest` to ensure zero-fault behavior against both clean and corrupted datasets.
- `requirements.txt`: Manages external dependencies (`pandas`, `scipy`, `pytest`).
- `/Week 0` to `/Week 8`: Complete progression of weekly Harvard coursework and foundational code scripts.

## 📈 Academic Synchronicity
This codebase serves as the baseline for my multi-language comparative portfolio. The logical frameworks established here are currently being replicated across:
1. **CS50 SQL:** For advanced database querying and robust backend storage integrations.
2. **CS50R:** Utilizing R-language frameworks for superior statistical visualization.

---
*Maintained by Hoggen Edgard Oey — Prospective Computer Science & Statistics Undergraduate.*

