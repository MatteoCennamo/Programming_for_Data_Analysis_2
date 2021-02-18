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
from matplotlib import pyplot as plt


# Load the dataframes
df_weather = pd.read_csv('./Assets/CSV_files/weather.csv')
df_pollution = pd.read_csv('./Assets/CSV_files/pollution.csv')

# Merge the two dataframes
df = pd.merge(df_weather, df_pollution, how = 'outer', on = ['lat', 'lon'])
print(df.head())
print(df.info())

def kelvin_to_celsius(kelvin):
    """Convert kelvin to Celsius. Return Celsius conversion of input."""
    temp_celsius = (kelvin - 273.15)
    return temp_celsius

df['feels_like'] = kelvin_to_celsius(df['feels_like'])
df['temp_min'] = kelvin_to_celsius(df['temp_min'])
df['temp_max'] = kelvin_to_celsius(df['temp_max'])
df["temp"] = kelvin_to_celsius(df["temp"])

df.set_index('name', inplace = True)

temp= pd.DataFrame(df[['temp', 'feels_like', 'temp_min', 'temp_max']])

plt.figure(figsize = (20, 8))
temp.plot.bar()
plt.xlabel('City', fontdict = {'size': 12})
plt.ylabel('Temperature [°C]', fontdict = {'size': 12})
plt.show()
