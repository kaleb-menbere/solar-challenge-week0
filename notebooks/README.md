# Notebooks Folder

This folder contains Jupyter notebooks used for **data exploration, profiling, cleaning, and analysis** for the Solar Data Discovery Challenge.

## Structure
- `__init__.py`  
  Marks this folder as a Python package (optional for imports).

- `<country>_eda.ipynb`  
  Country-specific notebooks for exploratory data analysis (EDA).  
  - Examples:
    - `benin_eda.ipynb`
    - `sierraleone_eda.ipynb`
    - `togo_eda.ipynb`

### Purpose
1. Load raw solar datasets (`data/<country>.csv`).
2. Perform **summary statistics**, **missing value checks**, and **basic cleaning**.
3. Identify outliers and anomalies in GHI, DNI, DHI, and other sensor readings.
4. Visualize trends in:
   - Solar irradiance (GHI, DNI, DHI)
   - Module temperatures (TModA, TModB)
   - Wind speed and direction
   - Relative humidity and other environmental variables
5. Export cleaned datasets to `data/<country>_clean.csv`.

### Usage
1. Open the notebook in JupyterLab, Jupyter Notebook, or VSCode.
2. Update file paths if necessary.
3. Run the notebook step by step to replicate analysis.
4. Export results to CSV for use in Streamlit dashboards or cross-country comparisons.

---

**Tip:** Keep raw CSV files in `data/` and do not commit them to Git. Only commit cleaned CSVs if needed.
