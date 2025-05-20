import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data/owid-covid-data.csv")

# Display first few rows
print(df.head())

# Check data info
print(df.info())

# Clean: Drop rows where 'location' is null or not a country
df = df[df['continent'].notna()]

# Describe numeric columns
print(df.describe())

# Latest date in data
latest_date = df['date'].max()
print("Latest data date:", latest_date)

# Filter latest data only
latest_data = df[df['date'] == latest_date]

# Top 10 countries by total cases
top_cases = latest_data.sort_values(by='total_cases', ascending=False).head(10)
print(top_cases[['location', 'total_cases', 'total_deaths']])
