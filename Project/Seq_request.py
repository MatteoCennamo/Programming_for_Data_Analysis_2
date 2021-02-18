'''
------------- PROGRAMMING FOR DATA ANALYSIS 2 -------------

 +-------------------+
 |  Matteo  Cennamo  |
 |  Matilde Moreni   |
 +-------------------+


Sequantial vesion of the API request.
'''

import time
import memory_profiler
from Util import Util_functions as Uf


# Memory before method call
m1 = memory_profiler.memory_usage()

# Cities and API-key definition
CITIES = ['Toronto','New York City','Rio de Janeiro','Buenos Aires','Nuuk','London','Rome',' Oslo','Cairo',
          'Dubai','Moscow','Yakutsk','Cape Town','Nairobi','Tehran','New Delhi','Sydney','Honolulu', 'Tokyo','Beijing',]
APIKEY = '23df90be877fed80721f131eafff5c6a'

# Create list of URLs
urls = []
for city in CITIES:
    urls.append(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKEY}')

# Initialize LIST of data
responses = []

# Time before process
start = time.process_time()

# Process the queries
for url in urls:
    responses += [Uf.handleRequest(url)]

# Time after process
end = time.process_time()

# Memory after method call
m2 = memory_profiler.memory_usage()

# Compute memory usage and processing time
time_diff = end - start
mem_diff = m2[0] - m1[0]
print("It took {:2.3} Secs and {:2.3} Mb to execute this program.".format(time_diff, mem_diff))
