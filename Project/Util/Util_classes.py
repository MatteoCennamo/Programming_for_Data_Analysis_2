'''
------------- PROGRAMMING FOR DATA ANALYSIS 2 -------------

 +-------------------+
 |  Matteo  Cennamo  |
 |  Matilde Moreni   |
 +-------------------+


This contains all the classes used in the project.
'''

from Util import Util_functions as Uf
import threading
import os


class RequestThread(threading.Thread):
    '''< Thread > object which performs a request (.start method) with the 
    provided '.url'. Then it stores the data in '.data' attribute.'''
    def __init__(self, url):
        super().__init__()
        self.data = None     # stored data after request
        self.url = url       # URL with contains the content of the request

    def run(self, *args, **kargs):
        '''Makes the URL request and stores the data in '.data' attribute.'''
        self.data = Uf.handleRequest(self.url, *args, **kargs)
    
    def writeFILE(self, path):
        '''Writes the data collected by the thread in a file identified by 
        'path'.'''
        Uf.writeFILE(self.data, path)
    
    def __repr__(self):
        out = f'''Parent PID: {os.getppid()}\nProcess PID: {os.getpid()}\nAttributes:
    -> .url: {self.url} ({type(self.url)})
    -> .data: {self.data} ({type(self.data)})'''
        return out
