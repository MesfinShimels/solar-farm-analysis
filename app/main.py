# main.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Summary Statistics
def summary_statistics(df):
    print("Summary Statistics:\n", df.describe())
    print("\nMissing Values:\n", df.isnull().sum())

# Time Series Analysis
def time_series_analysis(df):
    # Convert 'Timestamp' to datetime if it's not already
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    # Plotting Global Horizontal Irradiance (GHI) over time
    plt.figure(figsize=(10, 6))
    plt.plot(df['Timestamp'], df['GHI'], label='GHI', color='orange')
    plt.title('Global Horizontal Irradiance Over Time')
    plt.xlabel('Time')
    plt.ylabel('GHI (W/m²)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.show()

# Correlation Analysis
def correlation_analysis(df):
    # Correlation matrix
    correlation_matrix = df[['GHI', 'DNI', 'DHI', 'Tamb', 'TModA', 'TModB']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()

# Wind Analysis (Wind Roses)
def wind_analysis(df):
    # Plotting Wind Speed vs Wind Direction
    plt.figure(figsize=(8, 6))
    plt.scatter(df['WD'], df['WS'], c='blue', alpha=0.5)
    plt.title('Wind Speed vs Wind Direction')
    plt.xlabel('Wind Direction (°N)')
    plt.ylabel('Wind Speed (m/s)')
    plt.grid(True)
    plt.show()

# Temperature vs GHI
def temperature_vs_GHI(df):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Tamb', y='GHI', data=df, hue='Cleaning', palette='coolwarm')
    plt.title('Temperature vs Global Horizontal Irradiance (GHI)')
    plt.xlabel('Ambient Temperature (°C)')
    plt.ylabel('Global Horizontal Irradiance (W/m²)')
    plt.show()

# Main function to run the analysis
def main():
    # Load dataset
    file_path = 'path_to_your_data.csv'  # Replace with actual file path or URL to dataset
    df = load_data(file_path)

    # Perform analysis
    summary_statistics(df)
    time_series_analysis(df)
    correlation_analysis(df)
    wind_analysis(df)
    temperature_vs_GHI(df)

if __name__ == "__main__":
    main()
