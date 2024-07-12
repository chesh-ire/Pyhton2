import numpy as np
import pandas as pd

# Load the dataset
churn_data = pd.read_csv('datasets/churn.csv', index_col=0)

# Print data types of columns
print(churn_data.dtypes)

# Check for duplicate rows
print(len(churn_data) - len(churn_data.drop_duplicates()))

# Check for duplicated customer IDs
df = churn_data['customerID'].duplicated()
print(sum(df))

# Check for missing values
print(churn_data.isnull().sum())

# Check for missing values in the 'totalcharges' column
print(churn_data['totalcharges'].isnull().sum())

# Calculate the mean of 'monthlycharges'
print(churn_data['monthlycharges'].mean())

# Find rows with a specific value in the 'dependents' column
print(churn_data.loc[churn_data['dependents'] == '1@#'])

# Check if there are any missing values in the dataset
print(churn_data.isnull().any())

# Fill missing values
churn_data = churn_data.apply(lambda x: x.fillna(x.median()) if x.dtype == 'float' else x.fillna(x.value_counts().index[0]))

print("........................................................")

# Check again if there are any missing values in the dataset
print(churn_data.isnull().any())
print()