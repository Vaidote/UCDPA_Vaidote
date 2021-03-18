# Import necessary libraries
import pandas as pd
pd.pandas.set_option('display.max_columns', 20)
pd.pandas.set_option('display.max.rows', 50)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
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

# Merge dataframes by combining two data tables
total_sales = pd.concat([sales, sales_nintendo], axis=0, ignore_index=True)
print(total_sales.shape)

# Display all columns and first 10 to 20 rows for visualisation
print(total_sales[10:21])

# Save total sales in single csv file
total_sales.to_csv("total_sales.csv", index=False)

# Sort on Rank column - ascending order by default
total_sales.sort_values(by=['Rank'], inplace=True)

# Inspect first and last 2 rows
print(total_sales.head(2))
print(total_sales.tail(2))

# inspect datatype
total_sales.info()

# Convert Year datatype from float to integer
total_sales["Year"] = total_sales["Year"].convert_dtypes()
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

# Create series True for NaN values
missing_year = pd.isnull(total_sales["Year"])

# Replace missing values using fillna()
total_sales["Year"].fillna(-99, inplace= True)
total_sales["Publisher"].fillna("No Publisher", inplace=True)

# Check for total missing values after data cleanup
print(total_sales.isnull().sum().sum())

# Year with the most copies sold globally
sales_grouped = total_sales.groupby('Year').sum()
sales_grouped_sorted = sales_grouped.sort_values("Global_Sales", ascending=False)
print(sales_grouped_sorted)

# List of sales region for top selling year
Year_Index = [2008, 2009, 2007]
NA_Sales = [351.44, 338.85, 312.05]
EU_Sales = [184.40, 191.59, 160.50]
JP_Sales = [60.26, 61.89, 60.29]
Other_Sales = [82.39, 74.77, 77.60]

# Sum sales across all regions in 2018
RegionSales = [NA_Sales,EU_Sales, JP_Sales, Other_Sales]
RegionSales = sum(map(np.array, RegionSales))
print("Total sales across all regions in 2018 : ", RegionSales[0])

# Calculate Market Share of EU Sales
EU_Market_Share = (EU_Sales[0] / RegionSales[0])*100
print(f"The Market Share of EU sales in 2018 is {EU_Market_Share:.0f} %")

# Create dictionary of lists
dict = {'Year':Year_Index, 'NA':NA_Sales, 'EU':EU_Sales, 'JP':JP_Sales, 'Other':Other_Sales}
TopSales = pd.DataFrame(dict)
TopSales.set_index('Year', inplace=True)
print(TopSales)

# Save dataframe in single csv file
TopSales.to_csv("Top_Sales", index=False)

# Visualise results
sns.countplot(data=total_sales, x='Year', palette=['#432371', '#FAAE7B'])

time_period = total_sales['Year'].nunique()
data = total_sales.groupby('Year').size().values

for index in range (time_period):
    plt.text(index,data[index], str(data[index]), ha='center', va='bottom', fontsize='small')

plt.xticks(rotation=65)
plt.title('Sales by year', fontsize=15)
plt.xlabel('Year', fontsize=15)
plt.ylabel('')
plt.show()



