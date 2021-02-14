# Programming_for_Data_Analysis_2
Project for "Programming for Data Analysis 2". Multi-threading API requests and json - csv file storage.


# STRUCTURE
1) < Util >:              package       functions and classes used in the project.
2) < Assets >:            directory     saved files (.json, .csv, ...).
3) < Seq_request.py >:    program       sequantial vesion of the API request.
4) < MT_request.py >:     program       Multi-Threads version of the API request. It downloads the data into < Assets > directory in .json format.
5) < Json2csv.py >:       program       reads .json files from < Assets > directory, converts the data into Pandas.DataFrame object and writes the 
                                        data in .csv in < Assets > directory.

# UTIL
< Util > package is divided in two modules, one for the functions used in the programs and one for the classes:
    (1) < Util_classes >:   contains the classes;
    (2) < Util_functions >: contains the functions.

# ASSETS
< Assets > directory contains two sub-directories, divided according to the format of the file stored:
    (1) < JSON_FILES >: contains the files in .json format;
    (2) < CSV.FILES >:  contains the files in .csv format.
