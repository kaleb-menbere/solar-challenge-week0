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
Upload solar data files and explore solar irradiance trends, temperatures, and wind conditions.
""")

# -------------------------
# Sidebar: File upload and filters
# -------------------------
st.sidebar.header("Data Upload & Filter Options")

# File upload section
st.sidebar.subheader("Upload Solar Data Files")
uploaded_files = st.sidebar.file_uploader(
    "Choose CSV files", 
    type=["csv"], 
    accept_multiple_files=True,
    help="Upload one or more CSV files containing solar data with columns like 'GHI', 'Timestamp', etc."
)

# Filter options
st.sidebar.subheader("Data Filters")
ghi_min, ghi_max = st.sidebar.slider(
    "GHI Range Filter (W/m²)", 0, 1500, (0, 1500)
)

top_n = st.sidebar.number_input("Top N regions to show:", min_value=1, max_value=20, value=5)

# -------------------------
# Load data from uploaded files
# -------------------------
data_dict = {}

if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            # Use the filename (without extension) as the country name
            country_name = uploaded_file.name.replace('.csv', '').replace('_clean', '').title()
            
            # Load the data
            df = load_data(uploaded_file)
            
            # Filter by GHI if the column exists
            if "GHI" in df.columns:
                df = df[(df["GHI"] >= ghi_min) & (df["GHI"] <= ghi_max)]
            
            data_dict[country_name] = df
            st.sidebar.success(f"✅ Loaded {uploaded_file.name} as '{country_name}'")
            
        except Exception as e:
            st.sidebar.error(f"❌ Error loading {uploaded_file.name}: {str(e)}")
else:
    st.info("👆 Please upload one or more CSV files in the sidebar to get started.")

# -------------------------
# Tabs
# -------------------------
if data_dict:
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
            if not df.empty and "GHI" in df.columns and "Timestamp" in df.columns:
                plt.figure(figsize=(10,4))
                sns.lineplot(x="Timestamp", y="GHI", data=df)
                plt.title(f"{country} GHI Trend")
                plt.xticks(rotation=45)
                st.pyplot(plt.gcf())
                plt.clf()
            else:
                st.warning(f"No GHI or Timestamp data available for {country}")

    # -------------------------
    # Tab 3: Boxplots
    # -------------------------
    with tabs[2]:
        st.header("GHI Distribution Across Datasets")
        combined_df = pd.DataFrame()
        for country, df in data_dict.items():
            if not df.empty and "GHI" in df.columns:
                temp = df[["GHI"]].copy()
                temp["Dataset"] = country
                combined_df = pd.concat([combined_df, temp])
        if not combined_df.empty:
            plt.figure(figsize=(8,5))
            sns.boxplot(x="Dataset", y="GHI", data=combined_df)
            plt.title("GHI Distribution by Dataset")
            st.pyplot(plt.gcf())
            plt.clf()
        else:
            st.info("No GHI data available for selected filters.")

    # -------------------------
    # Tab 4: Top Regions
    # -------------------------
    with tabs[3]:
        st.header(f"Top {top_n} Regions by Average GHI")
        for country, df in data_dict.items():
            if not df.empty and "GHI" in df.columns:
                top_regions = get_top_regions(df, value_column="GHI", top_n=top_n)
                st.subheader(country)
                if not top_regions.empty:
                    st.dataframe(top_regions)
                else:
                    st.info(f"No region data available for {country}")

else:
    # Show placeholder when no files are uploaded
    st.warning("No data loaded. Please upload CSV files using the file uploader in the sidebar.")

st.markdown("""
---
*Dashboard developed for MoonLight Energy Solutions Solar Data Discovery Challenge. Developed by Kaleb*
""")