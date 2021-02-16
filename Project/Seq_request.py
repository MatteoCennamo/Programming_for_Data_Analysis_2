'''
------------- PROGRAMMING FOR DATA ANALYSIS 2 -------------

 +-------------------+
 |  Matteo  Cennamo  |
 |  Matilde Moreni   |
 +-------------------+


Sequantial vesion of the API request.
'''

from Util import Util_functions as Uf


# file da cui ho visto come fare l'url 
https://mixedanalytics.com/knowledge-base/access-open-weather-api-data-in-google-sheets/
https://mixedanalytics.com/knowledge-base/import-financial-modeling-prep-stock-data-google-sheets/

 
 #tentativo 1
 
import requests
import time

cities = ['London', 'Tokyo']

urls = []
for city in cities:
    urls.append('api.openweathermap.org/data/2.5/weather'
                + city +
                'appid=23df90be877fed80721f131eafff5c6a')
start = time.time()
for url in urls:
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        print(response.text)
    except Exception as exception:
        print('An exception occurred: ' + str(exception))
    else:
        print('Success!')

end = time.time()
print('Took %.3f seconds' % (end - start))
  
