import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load CSV file into pandas DataFrame."""
    df = pd.read_csv(file_path, parse_dates=['Timestamp'], index_col='Timestamp')
    return df

def plot_boxplot(df, metric='GHI', countries=None):
    """Plot boxplot for selected metric and countries."""
    if countries:
        df_plot = df[df['Country'].isin(countries)]
    else:
        df_plot = df.copy()
    
    plt.figure(figsize=(10,6))
    sns.boxplot(x='Country', y=metric, data=df_plot, palette='Set2')
    plt.title(f'{metric} Distribution by Country')
    plt.ylabel(f'{metric} (W/m²)')
    plt.xlabel('Country')
    plt.tight_layout()
    return plt
