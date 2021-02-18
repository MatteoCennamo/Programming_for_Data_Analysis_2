 # current data of Pollution 
 

 
# http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API key}
 
import time
import pandas as pd
import memory_profiler
from Util import Util_classes as Uc


# Load 'weather data'
df = pd.read_csv('./Assets/CSV_files/weather.csv')
# Create a DICTIONARY with: key = city; value = [lat, lon]
dictLocation = {}
for index, row in df.iterrows():
    dictLocation[row['name']] = [row['lat'], row['lon']]
  
  
APIKEY = '23df90be877fed80721f131eafff5c6a'

def main():
    # Create list of URLs and cities
    urls = []
    for city, loc in dictLocation.items():
        urls.append((f'http://api.openweathermap.org/data/2.5/air_pollution?lat={loc[0]}&lon={loc[1]}&appid={APIKEY}', city))
      
    # Create threads and launch them
    threads = []
    for url in urls:
        thread = Uc.RequestThread(*url)
        thread.start() 
        threads.append(thread)
    # Join the threads
    for thread in threads:
        thread.join()
    
    # Write the data in .json files
    for thread in threads:
        thread.writeFILE(typ = 'pollution')

if __name__ == '__main__':
    # Memory before program call
    m1 = memory_profiler.memory_usage()
    # Time before process
    start = time.process_time()
    
    main()
    
    # Time after process
    end = time.process_time()
    # Memory after program call
    m2 = memory_profiler.memory_usage()
    # Compute memory usage and processing time
    time_diff = end - start
    mem_diff = m2[0] - m1[0]
    print("It took {:2.4} Secs and {:2.3} Mb to execute this program.".format(
            time_diff, mem_diff))
