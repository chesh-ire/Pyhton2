import pandas as pd
import matplotlib.pyplot as plt

# Reading the CSV file, parsing the 'Date' column as dates, and setting it as the index
data = pd.read_csv('datasets/FremontBridge.csv', index_col='Date', parse_dates=True)

# Renaming the columns
data.columns = ['Total', 'East', 'West']

# Displaying the first few rows of the DataFrame
data.head()


# Grouping the data by the day of the week and calculating the mean for each day
by_weekday = data.groupby(data.index.dayofweek).mean()

# Displaying the result
print(by_weekday)

# Renaming the index to represent the days of the week
by_weekday.index = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

# Plotting the data with different line styles
by_weekday.plot(style=[':', '--', '-'])

# Displaying the plot
plt.show()     # see if youneed this 






import numpy as np

# Create an array indicating whether each entry is a weekday or weekend
weekend_array = np.where(data.index.dayofweek < 5, 'Weekday', 'Weekend')

print(weekend_array)

# Group the data by the 'weekend_array' and time, then calculate the mean
by_time = data.groupby([weekend_array, data.index.time]).mean()

print(by_time)

# Plotting the weekday data
by_time.loc['Weekday'].plot(title='Weekdays', style=[':', '--', '-'])

# Display the plot
#plt.show()

# Plotting the weekend data
by_time.loc['Weekend'].plot(title='Weekends', style=[':', '--', '-'])

# Display the plot
#plt.show()

