import csv
import pandas as pd

dataFile = open('./file.csv', 'w')

#create the csv file for conversion
writer = csv.writer(dataFile)

df = pd.read_csv('BIXS.csv', usecols=['data'])  
def hex_to_ascii(s):
    try:
        return bytearray.fromhex(s).decode()
    except ValueError:
        return None      # or s, or some other error handling

df['data']
print(df['data'].apply(hex_to_ascii))

writer.writerow(df['data'].apply(hex_to_ascii))

#close a file
dataFile.close()