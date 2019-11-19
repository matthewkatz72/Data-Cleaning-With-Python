# Importing libraries
import pandas as pd
import numpy as np

# Read csv file into a pandas dataframe
df = pd.read_csv("property-data.csv")

# Take a look at the first few rows
print (df.head())
print ("\n==========\n")

#Looking at coloumns for null values
print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())
print ("\n==========\n")

# Making a list of missing value types excluding NA as NA and NaN are recognized as null
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("property-data.csv", na_values = missing_values)

#Looking at columns after adding a list of Null values
print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())
print ("\n==========\n")

# Detecting numbers
cnt=0
for row in df['OWN_OCCUPIED']:
    try:
        int(row)
        df.loc[cnt, 'OWN_OCCUPIED']=np.nan
    except ValueError:
        pass
    cnt+=1
print ("\n==========\n")

# Total missing values for each feature
print (df.isnull().sum())

# Any missing values?
print (df.isnull().values.any())

# Total number of missing values
print (df.isnull().sum().sum())

print ("\n==========\n")

# Location based replacements examples
df.loc[2,'ST_NUM'] = 125
df.loc[6,'ST_NUM'] = 200
df.loc[1,'SQ_FT'] = 1000
df.loc[7,'SQ_FT'] = 1025

print (df)
