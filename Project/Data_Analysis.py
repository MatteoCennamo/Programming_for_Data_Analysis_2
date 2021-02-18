'''
------------- PROGRAMMING FOR DATA ANALYSIS 2 -------------

 +-------------------+
 |  Matteo  Cennamo  |
 |  Matilde Moreni   |
 +-------------------+


This reads .csv files from < Assets/CSV_files > folder, then, performs simple 
data analysis of weather and pollution among cities.
'''
import pandas as pd
import statsmodels.formula.api as smf


# Load the dataframes
df_weather = pd.read_csv('./Assets/CSV_files/weather.csv')
df_pollution = pd.read_csv('./Assets/CSV_files/pollution.csv')

# Merge the two dataframes
df = pd.merge(df_weather, df_pollution, how = 'outer', on = ['lat', 'lon'])
print(df.head())
print(df.info())

# Perform linear regression
model = smf.ols('pm10 ~ temp + pressure + humidity + speed', df).fit()
