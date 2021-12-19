import csv
import pandas as pd
import matplotlib.pyplot as plt

dataFile = open('./file.csv', 'w')

#create the csv file for conversion
writer = csv.writer(dataFile)

df = pd.read_csv('kt-p1-at_console_session_2021-12-09.csv', usecols=['data'])  
def hex_to_ascii(s):
    try:
        return bytearray.fromhex(s).decode()
    except ValueError:
        return None      # or s, or some other error handling

df['data']
print(df['data'].apply(hex_to_ascii))

writer.writerow(df['data'].apply(hex_to_ascii))
#Data Flitering
# dropping null value columns to avoid errors
#df.dropna(inplace = True)
 
# substring to be searched
#sub ='computed altitude: '
 
# creating and passing series to new columnd
#df["Index"] = df["data"].str.find(sub)
 
# display
#close a file
dataFile.close()