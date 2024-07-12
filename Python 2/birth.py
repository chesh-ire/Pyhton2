import pandas as pd
import matplotlib.pyplot as plt


births = pd.read_csv('births.csv')


print(births.head())
print(births.dtypes)

print(births.describe())

# Total number of US births by year and gender
total_births_by_year_gender = births.pivot_table('births', index='year', columns='gender', aggfunc='sum').plot()
plt.ylabel('Total births per year')


# Average daily births by day of week and decade
births['decade'] = 10 * (births['year'] // 10)



Q1 = births['births'].quantile(0.25)
Q3 = births['births'].quantile(0.75)
IQR = Q3 - Q1

births = births[~((births['births'] < (Q1 - 1.5 * IQR)) | (births['births'] > (Q3 + 1.5 * IQR)))]


# Create datetime index
births.index = pd.to_datetime(10000 * births['year'] + 100 * births['month'] + births['day'], format='%Y%m%d')

# Add day of week column
births['dayofweek'] = births.index.dayofweek

# Display the cleaned DataFrame
print(births.head())

# Plot average daily births by day of week and decade
births.pivot_table('births', index='dayofweek', columns='decade', aggfunc='mean').plot()
plt.ylabel('Avg births by day')