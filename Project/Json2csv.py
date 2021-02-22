'''
------------- PROGRAMMING FOR DATA ANALYSIS 2 -------------

 +-------------------+
 |  Matteo  Cennamo  |
 |  Matilde Moreni   |
 +-------------------+


This reads .json files from < Assets > directory, converts the
data into Pandas.DataFrame object and writes the data in .csv
in < Assets/CSV_files > folder.
'''
from os import path
import pandas as pd
from Util import Util_functions as Uf


CITIES = ['Toronto','New York','Rio de Janeiro','Buenos Aires','Nuuk','London',
          'Rome','Oslo','Cairo','Dubai','Moscow','Yakutsk','Cape Town','Nairobi',
          'Tehran','New Delhi','Sydney','Honolulu', 'Tokyo','Beijing']

for i in ['weather', 'pollution']: # , 'hist_weather'
    # Create an empty dataframe for weather conditions
    df = pd.DataFrame()
    for city in CITIES:
        # Create the path of the file
        p = f'./Assets/JSON_files/{city.upper()}_{i}.json'
        # Load the data
        if path.isfile(p):
            d = Uf.json2dict(p)
        else:
            print(f'{p} is NOT an existing file.')
            continue
        # Flatten the dictionary
        d = Uf.flattenJson(d)
        for k, v in d.items():
            d[k] = [v]
        # Add data to dataframe
        df = df.append(pd.DataFrame(d))
    df.reset_index()
    df.to_csv(f'./Assets/CSV_files/{i}.csv', index = False)
