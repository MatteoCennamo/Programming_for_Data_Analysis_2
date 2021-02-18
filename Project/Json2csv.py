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
import pandas as pd
from Util import Util_functions as Uf

CITIES = ['Toronto','New York City','Rio de Janeiro','Buenos Aires','Nuuk','London',
          'Rome','Oslo','Cairo','Dubai','Moscow','Yakutsk','Cape Town','Nairobi',
          'Tehran','New Delhi','Sydney','Honolulu', 'Tokyo','Beijing']

for i in ['weather', 'pollution']:
    # Create an empty dataframe for weather conditions
    df = pd.DataFrame()
    for city in CITIES:
        # Load the data
        d = Uf.json2dict(f'./Assets/JSON_files/{city.upper()}_{i}.json')
        # Flatten the dictionary
        d = Uf.flattenJson(d)
        for k, v in d.items():
            d[k] = [v]
        # Add data to dataframe
        df = df.append(pd.DataFrame(d))
    df.reset_index()
    df.to_csv('./Assets/CSV_files/{i}.csv', index = False)
