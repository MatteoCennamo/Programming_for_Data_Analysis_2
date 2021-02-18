'''
------------- PROGRAMMING FOR DATA ANALYSIS 2 -------------

 +-------------------+
 |  Matteo  Cennamo  |
 |  Matilde Moreni   |
 +-------------------+


Multi-Threads version of the API request. It downloads the data
into < Assets/JSON_files > folder in .json format.
'''
import time
import requests
import os
import threading
import json

##   multithreading

class Url_Thread(threading.Thread):
    def __init__(self,url,city):
        super().__init__()
        self.city = city
        self.url = url


    def run(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            print (response.text)
            with open(self.city + ".json", "w") as write_file:
                #json.dump(response.text, write_file, indent = 6)
                write_file.write(response.text)
        except Exception as exception:
            print ( 'An exception occurred: ' + str (exception))
        else :
            print ( 'Success!' )


CITIES = ['Toronto','New York City','Rio de Janeiro','Buenos Aires','Nuuk','London','Rome','Oslo','Cairo',
          'Dubai','Moscow','Yakutsk','Cape Town','Nairobi','Tehran','New Delhi','Sydney','Honolulu', 'Tokyo','Beijing']

APIKEY = '23df90be877fed80721f131eafff5c6a'

urls = []
for city in CITIES:
    urls.append(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKEY}')
        
start = time.time()

threads = []
for i in range(len(urls)):
    thread = Url_Thread(urls[i],CITIES[i])
    thread.start() 
    threads.append(thread)

for thread in threads:
    thread.join()
end = time.time()
print('Took %.3f seconds' % (end - start))
