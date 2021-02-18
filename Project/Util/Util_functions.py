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
import json


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
        f.write(data.content)

def json2dict(path):
    '''Reads a '.json' file (provided in 'path'), writing the data in a 
    Pandas.DataFrame.'''
    with open(path, 'r') as f:
        data = json.load(f)
    return data

def flattenJson(d):
    '''Flatten a nested '.json' file into a dictionary of key-value pairs.'''
    out = {}
    for k, v in d.items():
        if isinstance(v, dict):
            app = flattenJson(v)
        elif isinstance(v, list) and isinstance(v[0], dict):
            app = flattenJson(v[0])
        else:
            app = {k: v}
        out.update(app)
    return out
