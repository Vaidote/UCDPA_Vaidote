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

# Define function to insert separating line
def draw_line(x):
    return print("--" * x)


draw_line(30)

# Call out names of the columns
print(sales.columns, sales_nintendo.columns)
draw_line(30)

# Inspect shape of dataframes before merging
print(sales.shape, sales_nintendo.shape)
draw_line(30)

# Merge dataframes by combining two data tables
total_sales = pd.concat([sales, sales_nintendo], axis=0, ignore_index=True)
print(total_sales.shape)
draw_line(30)

# Display all columns and first 10 to 20 rows for visualisation
print(total_sales[10:21])
draw_line(30)

# Save total sales in single csv file
total_sales.to_csv("total_sales.csv", index=False)

# Sort on Rank column - ascending order by default
total_sales.sort_values(by=['Rank'], inplace=True)

# Inspect first and last 2 rows
print(total_sales.head(2))
print(total_sales.tail(2))
draw_line(30)

# inspect datatype
total_sales.info()
draw_line(30)

# Convert Year datatype from float to integer
total_sales["Year"] = total_sales["Year"].convert_dtypes()
total_sales.info()
draw_line(30)

# Remove duplicate values on column Rank
drop_duplicates = total_sales.drop_duplicates(subset=['Rank'])
print(total_sales.shape, drop_duplicates.shape)
draw_line(30)

# Check for any missing values
print(total_sales.isnull().values.any())
draw_line(30)

# Count missing values in each column
print(total_sales.isnull().sum())
draw_line(30)

# Count unique values in each column
print(total_sales.nunique())
draw_line(30)

# Year with the most copies sold globally
sales_grouped = total_sales.groupby('Year').sum().reset_index()
sales_grouped_sorted = sales_grouped.sort_values("Global_Sales", ascending=False)
print(sales_grouped_sorted.head(10))
draw_line(30)

# Replace missing values using fillna()
total_sales["Year"].fillna(2008, inplace=True)
total_sales["Publisher"].fillna("No Publisher", inplace=True)

# Check for total missing values after data cleanup
print(total_sales.isnull().sum().sum())
draw_line(30)

# List of sales region for top selling year
Year_Index = [2008, 2009, 2007]
NA_Sales = [351.44, 338.85, 312.05]
EU_Sales = [184.40, 191.59, 160.50]
JP_Sales = [60.26, 61.89, 60.29]
Other_Sales = [82.39, 74.77, 77.60]

# Return total sales across all regions in 2008
RegionSales = [NA_Sales, EU_Sales, JP_Sales, Other_Sales]
RegionSales = sum(map(np.array, RegionSales))
print("Total sales across all regions in 2008 is ", RegionSales[0]*1000, "copies")
draw_line(30)

# Calculate Market Share of EU Sales
EU_Market_Share = (EU_Sales[0] / RegionSales[0]) * 100
print(f"The Market Share of EU sales in 2008 is {EU_Market_Share:.0f} %")
draw_line(30)

# Create dictionary of lists
dict = {'Year': Year_Index, 'NA': NA_Sales, 'EU': EU_Sales, 'JP': JP_Sales, 'Other': Other_Sales}

# Access elements in dictionary
print("dict['Year ']: ", dict['Year'])
print("dict['Sales']: ", dict['NA'])
draw_line(30)

# Create new dataframe from dictionary
TopSales = pd.DataFrame(dict)
TopSales.set_index('Year', inplace=True)
print(TopSales)
draw_line(30)

# Return rows relating to Europe and Japan only

for index, row in TopSales.iterrows():
    print(index, row['EU'], row['JP'])

draw_line(30)

# Save dataframe in single csv file
TopSales.to_csv("Top_Sales", index=False)

# Visualise total sales by year using countplot
sns.countplot(data=total_sales, x='Year', palette="Paired")

time_period = total_sales['Year'].nunique()
data = total_sales.groupby('Year').size().values

for index in range(time_period):
    plt.text(index, data[index], str(data[index]), ha='center', va='bottom', fontsize='small')

plt.xticks(rotation=65)
plt.title('Sales by year (in millions)', fontsize=15)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Number of games', rotation=90)
plt.show()

# Create line plot for Regional sales by year
NA = total_sales.groupby('Year')['NA_Sales'].agg(np.sum)
NA = pd.DataFrame({'Year': NA.index, 'Sales': NA.values})
EU = total_sales.groupby('Year')['EU_Sales'].agg(np.sum)
EU = pd.DataFrame({'Year': EU.index, 'Sales': EU.values})
JP = total_sales.groupby('Year')['JP_Sales'].agg(np.sum)
JP = pd.DataFrame({'Year': JP.index, 'Sales': JP.values})
OS = total_sales.groupby('Year')['Other_Sales'].agg(np.sum)
OS = pd.DataFrame({'Year': OS.index, 'Sales': OS.values})

ax = plt.subplots(figsize=(15, 6))

ax = sns.lineplot(x='Year', y='Sales', data=NA, label='North America')
ax = sns.lineplot(x='Year', y='Sales', data=EU, label='Europe')
ax = sns.lineplot(x='Year', y='Sales', data=JP, label='Japan')
ax = sns.lineplot(x='Year', y='Sales', data=OS, label='Other')
ax.set_title("Regional Sales by Year", fontsize=15)
ax.set_xlabel("Years")
ax.set_ylabel("Sales (in millions)", rotation=90)
ax.set(ylim=(0, 450))

ax.xaxis.grid(False)
sns.despine(left=True)
plt.show()

# Looping through dataframe using iterators
# Global sales data for top 10 games by rank
sales_indexed = total_sales.set_index('Rank')
for index, row in sales_indexed.head(n=10).iterrows():
    print(index, row['Name'], row['Publisher'], row['Global_Sales'])
draw_line(30)

# Top ten publishers
top10_publishers = total_sales['Publisher'].value_counts().head(10)
ax = plt.subplots(figsize=(15,6))
sns.barplot(x=top10_publishers.values, y=top10_publishers.index, palette='cubehelix')
plt.title("Top 10 Publishers in the world", fontsize=15)
plt.xlabel('Number of games')
plt.show()

# Top ten sales by platform
top500 = total_sales.head(500)
x = np.array(top500["Genre"])
y = np.array(top500['Publisher'])
plt.scatter(x,y, color='red')
plt.title("Video game genres by publisher in Top 500 list")
plt.grid(True)
plt.show()





