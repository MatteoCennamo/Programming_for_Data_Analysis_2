# Programming_for_Data_Analysis_2
Project for "Programming for Data Analysis 2". Multi-threading API requests and json - csv file storage.


## STRUCTURE
_**File or folder**_          | _**Type**_ | _**Description**_
------------------------------|------------|------------------------------------------------------------
< **Util** >                  | package    | functions and classes used in the project.
< **Assets** >                | directory  | saved files (.json, .csv, ...).
< **Seq_request.py** >        | program    | sequantial vesion of the API request.
< **MT_request.py** >         | program    | Multi-Threads version of the API request. It downloads the data into < Assets > directory in .json format.
< **Json2csv.py** >           | program    | reads .json files from < Assets > directory, converts the data into Pandas.DataFrame object and writes the data in .csv in < Assets > directory.

## UTIL
< Util > package is divided in two modules, one for the functions used in the programs and one for the classes:
_**Module**_                | _**Description**_
----------------------------|--------------------------------------
< **Util_classes** >        | contains the classes;
< **Util_functions** >      | contains the functions.

## ASSETS
< Assets > directory contains two sub-directories, divided according to the format of the file stored:
_**Folder**_            | _**Description**_
------------------------|----------------------------------------
< **JSON_files** >      | contains the files in .json format;
< **CSV_files** >       | contains the files in .csv format.

## API KEY
api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}
 < **APIKEY** > =  4c7fb4a66ea8116310c3af4e5c3f52fc
