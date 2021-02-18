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
import json

CITIES = ['Toronto','New York City','Rio de Janeiro','Buenos Aires','Nuuk','London','Rome',' Oslo','Cairo',
          'Dubai','Moscow','Yakutsk','Cape Town','Nairobi','Tehran','New Delhi','Sydney','Honolulu', 'Tokyo','Beijing',]

res= []
for city in CITIES:
        data = json.load(open("C:\\Users\\moren\\" + city + ".json"))
        for elm in data:
            res.append([city])

    
csv_file_path = 'Cities.csv'
fin_res = pd.DataFrame(res)
fin_res.columns= ['name','coord','weather','base','main','wind']   # !!
fin_res.to_csv(csv_file_path,index = False)
