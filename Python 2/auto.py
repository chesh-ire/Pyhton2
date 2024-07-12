import pandas as pd
import seaborn as sns



auto = pd.read_csv('Automobile_data.csv', na_values=["?"])


auto.head()


auto.describe()



sns.boxplot(x=auto['num-of-doors'], y=auto['horsepower'], hue=auto['fuel-type'])




sns.boxplot(x=auto['body-style'], y=auto['horsepower'], hue=auto['fuel-type'])




sns.countplot(x=auto['body-style'], hue=auto['fuel-type'])



sns.catplot(
    x="fuel-type",
    y="horsepower",
    hue="num-of-doors",
    col="drive-wheels",
    data=auto,
    kind="box",
    
)
# Box plot for 'horsepower' by 'fuel-type', colored by 'drive-wheels'

sns.boxplot(x=auto['fuel-type'], y=auto['horsepower'], hue=auto['drive-wheels'])