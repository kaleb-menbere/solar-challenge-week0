# 🌞 10Academy Solar Challenge — Week 0

**Kickstart Your AI Mastery with Cross-Country Solar Farm Analysis**
📅 *November 05 – 12, 2025*

---

## 🧩 Overview

This repository is part of the **10Academy Artificial Intelligence Mastery Program — Week 0 Challenge**.
The challenge focuses on foundational skills in **Git, environment setup, data cleaning, exploratory data analysis (EDA)**, and **collaboration workflows** using real-world **solar farm datasets** from **Benin**, **Sierra Leone**, and **Togo**.

You will find my complete work for all Week 0 tasks organized in this repository, with detailed notebooks, visuals, and documentation.

---

## 🧱 Prerequisites

Before running the notebooks, ensure you have the following tools installed:

| Tool                 | Version | Purpose              | Check Command       |
| -------------------- | ------- | -------------------- | ------------------- |
| **Python**           | 3.10    | Core language        | `python --version`  |
| **pip**              | Latest  | Install dependencies | `pip --version`     |
| **Git**              | Latest  | Version control      | `git --version`     |
| **Jupyter Notebook** | Latest  | Run `.ipynb` files   | `jupyter --version` |

💡 *Tip:*
Install Jupyter if missing:

```bash
pip install notebook
```

---

## ⚙️ Environment Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/kaleb-menbere/solar-challenge-week0.git
cd solar-challenge-week0
```

### 2️⃣ Create and Activate a Virtual Environment

#### 🪟 Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

# 🧩 Task 1 — Git & Environment Setup

### 🎯 Objective

Set up a **clean, reproducible environment** that supports collaboration and continuous integration.

### 📘 Steps

1. Initialized repository and created `.gitignore`
2. Added `requirements.txt` and listed dependencies (pandas, numpy, matplotlib, seaborn)
3. Configured GitHub Actions workflow for CI testing (`.github/workflows/ci.yml`)
4. Documented setup and instructions in `README.md`
5. Verified CI pipeline builds successfully on push

### 🧾 Deliverables

* ✅ Virtual environment successfully configured
* ✅ CI pipeline passing
* ✅ Documentation complete

📁 Files:

```
.github/workflows/ci.yml  
requirements.txt  
.gitignore  
README.md  
```

✅ **Task 1 Completed Successfully**

---

# 🧩 Task 2 — Data Profiling, Cleaning & EDA

### 🎯 Objective

Explore, clean, and analyze solar datasets for **Benin**, **Togo**, and **Sierra Leone** to prepare them for comparison.

### 📘 Steps

#### 🔹 Data Profiling

* Loaded raw CSV datasets
* Checked data info, shape, and missing values
* Identified key variables: GHI, DNI, DHI, WS, WD, Tamb, RH, TModA, TModB

#### 🔹 Data Cleaning

* Handled missing values using **mean / interpolation imputation**
* Removed duplicates and corrected timestamp formats
* Detected and treated outliers using **Z-score filtering**
* Saved cleaned datasets locally (`data_cleaned/`)

#### 🔹 Exploratory Data Analysis (EDA)

* Generated summary statistics and distributions
* Plotted GHI, DNI, and DHI trends over time
* Visualized correlations between temperature, humidity, and irradiance
* Compared module performance (TModA vs TModB) before and after cleaning

#### 📊 Visuals Included

* Correlation heatmap
* Line plots (GHI/DNI/DHI vs Timestamp)
* Scatter plots (Tamb vs RH, WS vs WD)
* Boxplots for irradiance distributions

### 🧾 Deliverables

* `notebooks/benin_eda.ipynb`
* `notebooks/togo_eda.ipynb`
* `notebooks/sierra_leone_eda.ipynb`
* Cleaned CSVs stored locally
* EDA insights documented

✅ **Task 2 Completed Successfully**

---

# 🧩 Task 3 — Cross-Country Comparison

### 🎯 Objective

Compare solar performance metrics across **Benin**, **Sierra Leone**, and **Togo** to identify the best region for investment.

### 📘 Steps

1. Loaded cleaned datasets for all three countries
2. Computed mean, median, and standard deviation of GHI, DNI, and DHI
3. Created combined visualizations for country-level comparison
4. Ranked countries by solar potential
5. Performed optional ANOVA tests to validate statistical significance

#### 📊 Visuals Included

* Boxplots comparing GHI/DNI/DHI across countries
* Bar chart ranking average GHI
* Combined summary table of metrics

### 🧾 Deliverables

* `notebooks/compare_countries.ipynb`
* Statistical comparison table
* Cross-country comparison visualizations

✅ **Task 3 Completed Successfully**

---

# 🌟 Bonus Task — Interactive Dashboard *(Optional)*

### 🎯 Objective

Develop an interactive **Streamlit dashboard** to visualize solar data insights dynamically.

### 📘 Features

* Country selector dropdown
* Visual comparisons for GHI, DNI, DHI
* Summary metrics and trends
* Interactive charts for temperature and irradiance

#### 🧱 How to Run

```bash
streamlit run app/main.py
```

### 🧾 Deliverables

* `app/main.py`
* `dashboard_screenshots/`
* Optional Streamlit deployment link

🟡 **Bonus Task: In Progress / Optional**

---

## 🌿 Git Workflow

| Step | Command                                | Description                 |
| ---- | -------------------------------------- | --------------------------- |
| 1    | `git checkout -b <branch>`             | Create a new branch         |
| 2    | `git add .`                            | Stage changes               |
| 3    | `git commit -m "feat: task completed"` | Commit with message         |
| 4    | `git push origin <branch>`             | Push to GitHub              |
| 5    | PR                                     | Open Pull Request to `main` |

---

## ✅ Continuous Integration (CI)

Every push triggers GitHub Actions to:

* Install dependencies
* Verify environment setup
* Ensure reproducibility

Workflow File: `.github/workflows/ci.yml`

---

## 🧠 Project Structure

```
solar-challenge-week0/
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
│   ├── raw/
│   ├── cleaned/
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── togo_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   └── compare_countries.ipynb
├── app/
│   └── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧑‍💻 Author

**Kaleb Menbere**
🎓 Python & Web Developer
🌍 10Academy — Artificial Intelligence Mastery Program
📧 [GitHub Profile](https://github.com/kaleb-menbere)

---

✨ *All Week 0 Tasks Completed Successfully*

> “Clean data. Smart analysis. Clear insights.” 🚀

---
