import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file_path):
    """
    Load CSV data and fix Timestamp for Streamlit/PyArrow compatibility
    """
    df = pd.read_csv(file_path, parse_dates=["Timestamp"])
    if "Timestamp" in df.columns:
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce").dt.floor("s")
    return df

def get_top_regions(df, value_column="GHI", top_n=5):
    """
    Return top N regions (timestamps) by average value
    """
    if df.empty or value_column not in df.columns:
        return pd.DataFrame()
    return df.groupby("Timestamp")[value_column].mean().sort_values(ascending=False).head(top_n)
