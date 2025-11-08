# Scripts Folder

This folder contains Python scripts and utility modules used in the Solar Data Discovery Challenge.

## Structure
- `__init__.py`  
  Marks this folder as a Python package (optional for imports).

- `README.md`  
  Documentation for the folder.

- Utility scripts (optional):
  - Data processing scripts
  - Custom functions for cleaning, transforming, or aggregating datasets
  - Any one-off scripts that automate repetitive tasks

### Purpose
1. Support notebooks and the Streamlit dashboard with reusable code.
2. Maintain clean separation between analysis (notebooks) and reusable functions (scripts).
3. Automate preprocessing or exporting cleaned data.

### Usage
1. Import functions from scripts into notebooks or `app/main.py`.
   ```python
   from scripts.utils import load_data, get_top_regions
