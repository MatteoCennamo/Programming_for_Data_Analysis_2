'''
------------- PROGRAMMING FOR DATA ANALYSIS 2 -------------

 +-------------------+
 |  Matteo  Cennamo  |
 |  Matilde Moreni   |
 +-------------------+


This contains all the functions used in the project.
'''

import requests
import os


def handleRequest(url, *args, **kargs):
    '''Returns the data gathered by the 'url' request.'''
    try:
        # Get data from URL request
        data = requests.get(url, *args, **kargs)
        # If the response was successful, no Exception will be raised
        data.raise_for_status()
    except Exception as exception:
        print(f'\nAn exception occurred: {str(exception)}. Process PID: {os.getpid()}')
    else:
        print(f'\nSuccess! Process id: {os.getpid()}')
    return data

def writeFILE(data, path):
    '''Writes the data collected by 'request.get()' in the file specified by 'path'.'''
    with open(path, 'wb') as f:
        # Write the content of the data
        f.write(data.data.content)
