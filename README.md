# openFDA-human-drug
Script to get data from Human drug DB [https://open.fda.gov/downloads/] 

# How to get the data
* Clone the repository.
* Run python file to get the desired files.

  `python get-data.py`
 

This will download the desired json file in zipped format. You will be asked for to variables from where to start and where to end, which essentially means the starting and ending point of the files. the range of files is between 1 to 33.

Note: 

1. Each file ranges from 48M to 145M in zipped format.

2. This code is specific to only Human drug database.

3. Data will be downloaded in a new folder named  `files` .
