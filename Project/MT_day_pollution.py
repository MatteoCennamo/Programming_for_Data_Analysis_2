 # current data of Pollution 
 

 
# http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API key}
 
import time
import memory_profiler
from Util import Util_classes as Uc


# Cities and API-key definition   # DA DEFINIRE DIZIONARIO CON CITTA-LAT-LON
#CITIES = ['Toronto','New York City','Rio de Janeiro','Buenos Aires','Nuuk', 
          'London','Rome','Oslo','Cairo','Dubai','Moscow','Yakutsk','Cape Town', 
          'Nairobi','Tehran','New Delhi','Sydney','Honolulu', 'Tokyo','Beijing',]
  
  
APIKEY = '23df90be877fed80721f131eafff5c6a'

def main():
    # Create list of URLs and cities
    urls = []
    for city in CITIES:
        urls.append((f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={APIKEY}', city))
      
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
 
 
 
 
