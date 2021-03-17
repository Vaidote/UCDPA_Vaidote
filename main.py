# Import all the relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Find current working directory
print(os.getcwd())

# Import a csv files into a Pandas DataFrame
sales = pd.read_csv('/Users/vaidote/Documents/UCDPA_Vaidote/sales.csv')
sales_nintendo = pd.read_csv('/Users/vaidote/Documents/UCDPA_Vaidote/sales_nintendo.csv')

# Call out names of the columns
print(sales.columns, sales_nintendo.columns)

# Inspect shape of dataframes before merging
print(sales.shape, sales_nintendo.shape)

# Merge dataframes by combining two tables
total_sales = pd.concat([sales, sales_nintendo], axis=0, ignore_index=True)
print(total_sales.shape)

# Display all columns and first 10 to 20 rows for visualisation
pd.pandas.set_option('display.max_columns', 11)
print(total_sales[10:21])

# Sort on Rank column - ascending order by default
total_sales.sort_values(by=['Rank'], inplace=True)

# Inspect first and last 2 rows
print(total_sales.head(2))
print(total_sales.tail(2))

# inspect datatype
total_sales.info()

# Remove duplicate values on column Rank
drop_duplicates = total_sales.drop_duplicates(subset=['Rank'])
print(total_sales.shape, drop_duplicates.shape)

# Check for any missing values
print(total_sales.isnull().values.any())

# Count missing values in each column
print(total_sales.isnull().sum())

# Count unique values in each column
print(total_sales.nunique())

# Create series True forNaN values
missing_year = pd.isnull(total_sales["Year"])

# Filter and display data only with Year = NaN
print(total_sales[missing_year])

# Replace missing values using fillna()
total_sales["Year"].fillna("No Year", inplace= True)
total_sales["Publisher"].fillna("No Publisher", inplace= True)

# Check for total missing values after data cleanup
print(total_sales.isnull().sum().sum())

