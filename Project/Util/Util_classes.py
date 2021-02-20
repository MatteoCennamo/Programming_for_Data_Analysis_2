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
    def __init__(self, url, city):
        super().__init__()
        self.data = None     # stored data after request
        self.url = url       # URL with contains the content of the request
        self.city = city     # contains the name of the city
    
    def run(self):
        '''Makes the URL request and stores the data in '.data' attribute.'''
        self.data = Uf.handleRequest(self.url)
    
    def writeFILE(self, typ = None):
        '''Writes the data collected by the thread in a file identified by 
        'path'.'''
        if typ == None:
            typ = ''
        else:
            typ = f'_{str(typ)}'
        Uf.writeFILE(self.data, f'./Assets/JSON_files/{self.city.upper()}{typ}.json')
    
    def __repr__(self):
        out = f'''Parent PID: {os.getppid()}\nProcess PID: {os.getpid()}\nAttributes:
    -> .url: {self.url} ({type(self.url)})
    -> .data: {self.data} ({type(self.data)})
    -> .city: {self.city} ({type(self.city)}) 
    -> .type: {self.type}'''
        return out
