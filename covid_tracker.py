"""COVID-19 Global Data Tracker Python Script"""
# Importing relevant libraries
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv('dataset/owid-covid-data.csv')

# 2. Clean data
df['date'] = pd.to_datetime(df['date'])
countries = ['Kenya', 'United States', 'India']
df_clean = df[df['location'].isin(countries)].copy()
df_clean.fillna(method='ffill', inplace=True)

# 3. EDA: Cases & Deaths
for country in countries:
    subset = df_clean[df_clean['location'] == country]
    plt.figure()
    plt.plot(subset['date'], subset['total_cases'], label=f"{country} Cases")
    plt.plot(subset['date'], subset['total_deaths'], label=f"{country} Deaths")
    plt.legend()
    plt.title(f"COVID-19 Trends in {country}")
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.show()

# 4. Vaccination Progress
for country in countries:
    subset = df_clean[df_clean['location'] == country]
    plt.figure()
    plt.plot(subset['date'], subset['total_vaccinations'], label=f"{country} Vaccinations")
    plt.legend()
    plt.title(f"Vaccination Rollout in {country}")
    plt.xlabel('Date')
    plt.ylabel('Total Vaccinations')
    plt.show()

# 5. Insights
latest_summary = df_clean[df_clean['date'] == df_clean['date'].max()]
for country in countries:
    data = latest_summary[latest_summary['location'] == country]
    print(f"{country}: Total Cases={int(data['total_cases'])}, Total Deaths={int(data['total_deaths'])}, Total Vaccinations={int(data['total_vaccinations'])}")
