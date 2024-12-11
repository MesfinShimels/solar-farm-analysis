import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
def load_data(file_name):
    try:
        # Build the path dynamically
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the script
        file_path = os.path.join(script_dir, file_name)
        
        # Load the CSV file
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"File '{file_name}' not found in the directory '{script_dir}'.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None

# Summary Statistics
def summary_statistics(df):
    if df is not None:
        print("Summary Statistics:\n", df.describe())
        print("\nMissing Values:\n", df.isnull().sum())

# Time Series Analysis
def time_series_analysis(df):
    if df is not None:
        try:
            df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
            if df['Timestamp'].isna().any():
                print("Some timestamps could not be converted. Please check the data.")
            else:
                plt.figure(figsize=(10, 6))
                plt.plot(df['Timestamp'], df['GHI'], label='GHI', color='orange')
                plt.title('Global Horizontal Irradiance Over Time')
                plt.xlabel('Time')
                plt.ylabel('GHI (W/m²)')
                plt.xticks(rotation=45)
                plt.grid(True)
                plt.legend()
                plt.show()
        except KeyError:
            print("'Timestamp' or 'GHI' column is missing in the dataset.")

# Correlation Analysis
def correlation_analysis(df):
    if df is not None:
        try:
            selected_columns = ['GHI', 'DNI', 'DHI', 'Tamb', 'TModA', 'TModB']
            correlation_matrix = df[selected_columns].corr()
            plt.figure(figsize=(8, 6))
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
            plt.title('Correlation Matrix')
            plt.show()
        except Exception as e:
            print(f"Error in correlation analysis: {e}")

# Wind Analysis (Wind Roses)
def wind_analysis(df):
    if df is not None:
        try:
            plt.figure(figsize=(8, 6))
            plt.scatter(df['WD'], df['WS'], c='blue', alpha=0.5)
            plt.title('Wind Speed vs Wind Direction')
            plt.xlabel('Wind Direction (°N)')
            plt.ylabel('Wind Speed (m/s)')
            plt.grid(True)
            plt.show()
        except KeyError:
            print("'WD' or 'WS' column is missing in the dataset.")

# Temperature vs GHI
def temperature_vs_GHI(df):
    if df is not None:
        try:
            sns.scatterplot(x='Tamb', y='GHI', data=df, hue='Cleaning', palette='coolwarm')
            plt.title('Temperature vs Global Horizontal Irradiance (GHI)')
            plt.xlabel('Ambient Temperature (°C)')
            plt.ylabel('Global Horizontal Irradiance (W/m²)')
            plt.show()
        except KeyError:
            print("'Tamb' or 'GHI' column is missing in the dataset.")

# Main function to run the analysis
def main():
    # Dataset file name (in the same directory as main.py)
    file_name = 'sierraleone-bumbuna.csv'
    
    # Load the dataset
    df = load_data(file_name)

    if df is not None:
        # Remove irrelevant columns
        df = df.drop(columns=['Comments'], errors='ignore')
        
        # Perform analysis
        summary_statistics(df)
        time_series_analysis(df)
        correlation_analysis(df)
        wind_analysis(df)
        temperature_vs_GHI(df)

if __name__ == "__main__":
    main()
