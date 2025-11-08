# #import streamlit as st
# import pandas as pd
# from app.utils import load_data, plot_boxplot
# import matplotlib.pyplot as plt

# # App Title
# st.title("🌞 Solar Data Dashboard")

# # Sidebar: Country selection
# st.sidebar.header("Filter Options")
# selected_countries = st.sidebar.multiselect(
#     "Select Countries", 
#     options=['Benin','Togo','Sierra Leone'], 
#     default=['Benin','Togo','Sierra Leone']
# )

# # Sidebar: Metric selection
# metric = st.sidebar.selectbox("Select Metric for Boxplot", ['GHI', 'DNI', 'DHI'])

# # Load Data
# df = load_data("data/combined_clean.csv")  # Your cleaned CSV

# # Display basic info
# st.write("### Dataset Preview")
# st.dataframe(df.head())

# # Plot Boxplot
# st.write(f"### {metric} Distribution by Country")
# plt = plot_boxplot(df, metric=metric, countries=selected_countries)
# st.pyplot(plt.gcf())  # Display matplotlib figure in Streamlit

# # KPIs Table
# st.write("### Key Performance Indicators (Average Values)")
# kpi_cols = ['GHI','DNI','DHI','ModA','ModB','Tamb','RH','WS','WSgust']
# kpis = df[df['Country'].isin(selected_countries)][kpi_cols].mean().to_frame(name='Average').round(2)
# st.table(kpis)

# # Optional: add more visualizations like time series, scatter plots, heatmaps
