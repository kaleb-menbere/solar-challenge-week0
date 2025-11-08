# app/main.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------
# Utility function to load data
# -------------------------
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=["Timestamp"])
    return df

# -------------------------
# App title
# -------------------------
st.title("Solar Data Discovery Dashboard 🌞")
st.markdown("""
Kickstart your AI Mastery with cross-country solar farm analysis.
Select countries and explore solar irradiance trends, temperatures, and wind conditions.
""")

# -------------------------
# Sidebar: Country selection
# -------------------------
st.sidebar.header("Filter Options")
countries = ["Benin", "SierraLeone", "Togo"]
selected_countries = st.sidebar.multiselect("Select countries:", countries, default=countries)

# -------------------------
# Load data
# -------------------------
data_dict = {}
for country in selected_countries:
    file_path = f"data/{country.lower()}_clean.csv"
    try:
        data_dict[country] = load_data(file_path)
    except FileNotFoundError:
        st.warning(f"{file_path} not found. Please make sure it exists.")
        data_dict[country] = pd.DataFrame()  # empty dataframe

# -------------------------
# Tabs for visualization
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
        if not df.empty:
            plt.figure(figsize=(10,4))
            sns.lineplot(x="Timestamp", y="GHI", data=df)
            plt.title(f"{country} GHI Trend")
            plt.xticks(rotation=45)
            st.pyplot(plt.gcf())
            plt.clf()

# -------------------------
# Tab 3: Boxplots for GHI
# -------------------------
with tabs[2]:
    st.header("GHI Distribution Across Countries")
    combined_df = pd.DataFrame()
    for country, df in data_dict.items():
        if not df.empty:
            temp = df[["GHI"]].copy()
            temp["Country"] = country
            combined_df = pd.concat([combined_df, temp])
    if not combined_df.empty:
        plt.figure(figsize=(8,5))
        sns.boxplot(x="Country", y="GHI", data=combined_df)
        st.pyplot(plt.gcf())
        plt.clf()

# -------------------------
# Tab 4: Top Regions by GHI
# -------------------------
with tabs[3]:
    st.header("Top Regions by Average GHI")
    for country, df in data_dict.items():
        if not df.empty:
            top_regions = df.groupby("Timestamp")["GHI"].mean().sort_values(ascending=False).head(5)
            st.subheader(country)
            st.dataframe(top_regions)

st.markdown("""
---
*Dashboard developed for MoonLight Energy Solutions Solar Data Discovery Challenge.*
""")
