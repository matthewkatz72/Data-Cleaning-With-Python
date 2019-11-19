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

# Making a list of missing value types excluding NA as NA and NaN are recognized as null
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("property-data.csv", na_values = missing_values)

#Looking at columns after adding a list of Null values 
print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())
