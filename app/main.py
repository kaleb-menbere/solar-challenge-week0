import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, get_top_regions

# -------------------------
# App title
# -------------------------
st.set_page_config(page_title="Solar Data Discovery Dashboard", layout="wide")
st.title("🌞 Solar Data Discovery Dashboard")
st.markdown("""
Kickstart your AI Mastery with cross-country solar farm analysis.
Select countries and explore solar irradiance trends, temperatures, and wind conditions.
""")

# -------------------------
# Sidebar: Interactive filters
# -------------------------
st.sidebar.header("Filter Options")
countries = ["Benin", "SierraLeone", "Togo"]
selected_countries = st.sidebar.multiselect("Select countries:", countries, default=countries)

ghi_min, ghi_max = st.sidebar.slider(
    "GHI Range Filter (W/m²)", 0, 1500, (0, 1500)
)

top_n = st.sidebar.number_input("Top N regions to show:", min_value=1, max_value=20, value=5)

# -------------------------
# Load data
# -------------------------
data_dict = {}
for country in selected_countries:
    file_path = f"data/{country.lower()}_clean.csv"
    try:
        df = load_data(file_path)
        # Filter by GHI
        df = df[(df["GHI"] >= ghi_min) & (df["GHI"] <= ghi_max)]
        data_dict[country] = df
    except FileNotFoundError:
        st.warning(f"{file_path} not found.")
        data_dict[country] = pd.DataFrame()

# -------------------------
# Tabs
# -------------------------
tabs = st.tabs(["Summary Stats", "GHI Trends", "Boxplots", "Top Regions"])

# -------------------------
# Tab 1: Summary Stats
# -------------------------
with tabs[0]:
    st.header("Summary Statistics")
    for country, df in data_dict.items():
        if not df.empty:
            st.subheader(country)
            st.dataframe(df.describe())

# -------------------------
# Tab 2: GHI Trends
# -------------------------
with tabs[1]:
    st.header("GHI over Time")
    for country, df in data_dict.items():
        if not df.empty and "GHI" in df.columns:
            plt.figure(figsize=(10,4))
            sns.lineplot(x="Timestamp", y="GHI", data=df)
            plt.title(f"{country} GHI Trend")
            plt.xticks(rotation=45)
            st.pyplot(plt.gcf())
            plt.clf()

# -------------------------
# Tab 3: Boxplots
# -------------------------
with tabs[2]:
    st.header("GHI Distribution Across Countries")
    combined_df = pd.DataFrame()
    for country, df in data_dict.items():
        if not df.empty and "GHI" in df.columns:
            temp = df[["GHI"]].copy()
            temp["Country"] = country
            combined_df = pd.concat([combined_df, temp])
    if not combined_df.empty:
        plt.figure(figsize=(8,5))
        sns.boxplot(x="Country", y="GHI", data=combined_df)
        st.pyplot(plt.gcf())
        plt.clf()
    else:
        st.info("No data available for selected filters.")

# -------------------------
# Tab 4: Top Regions
# -------------------------
with tabs[3]:
    st.header(f"Top {top_n} Regions by Average GHI")
    for country, df in data_dict.items():
        if not df.empty and "GHI" in df.columns:
            top_regions = get_top_regions(df, value_column="GHI", top_n=top_n)
            st.subheader(country)
            st.dataframe(top_regions)

st.markdown("""
---
*Dashboard developed for MoonLight Energy Solutions Solar Data Discovery Challenge. developed by Kaleb*
""")
