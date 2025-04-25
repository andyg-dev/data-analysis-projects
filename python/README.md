# Personal Project: Sales Data Analysis with Python

## Project Overview:

In this project, I demonstrated my ability to analyze sales data using Python, focusing on the entire data analysis process—starting from loading and cleaning the data to performing grouped analysis and creating visualizations to present key insights.

## Step 1: Loading and Understanding Your Data

The first step in any data analysis project is loading and understanding the data. Using the pandas library, I loaded a sales dataset and performed initial inspections to check the data structure and identify any issues.

**Code Example:**

```python
import pandas as pd

# Load the dataset into a pandas DataFrame
# Using Sales 2019 data for Adventure Works with the file name 'Sales 2019 and later.txt' which is tab-separated
df = pd.read_csv('Sales 2019 and later.txt', sep='\t')

# Display the first 5 rows
print(df.head())

# Get information about columns, data types, and non-null values
print(df.info())

Why it matters: Understanding the data structure helps identify issues like missing values or incorrect data types early on.

Step 2: Cleaning and Preparing the Data
Data often needs cleaning and transformation before analysis. In this step, I converted the OrderDate to datetime and created a new column, Total Price, to analyze the total sales value.

Code Example:

# Convert 'OrderDate' to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Create 'Total Price' by multiplying 'Order Quantity' and 'Unit Price'
df['Total Price'] = df['Order Quantity'] * df['Unit Price']

Why it matters: Correcting data types (e.g., dates) and creating new features (e.g., Total Price) makes the dataset more useful for analysis.

Step 3: Summarizing and Exploring Data
I generated summary statistics for numerical columns and checked for missing values to identify any data gaps that might affect analysis.

Code Example:

# Get summary statistics for numerical columns
print(df.describe())

# Check for missing values
print(df.isnull().sum())

Why it matters: Summary statistics and missing values help to quickly assess the dataset's integrity and determine further steps.

Step 4: Analyzing Data by Groups
I grouped the data by Sales Territory Region to calculate total sales for each region, allowing for regional comparisons.

Code Example:

# Group data by 'Sales Territory Region' and calculate total sales per region
region_sales = df.groupby('Sales Territory Region')['Total Price'].sum().reset_index()

# Display total sales by region
print(region_sales)

Why it matters: Grouping data enables you to analyze performance across different segments, which is valuable for strategic decision-making.

Step 5: Visualizing Your Findings
Finally, I created a bar chart to visualize total sales by region. Visualizations help convey insights more clearly and effectively.

Code Example:

import matplotlib.pyplot as plt
import seaborn as sns

# Create bar chart to visualize total sales by region
plt.figure(figsize=(10, 6))
sns.barplot(x='Sales Territory Region', y='Total Price', data=region_sales)
plt.title('Total Sales by Sales Territory Region')
plt.xlabel('Sales Territory Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

Why it matters: Visualizations make complex data more accessible and highlight trends that are not immediately obvious from raw numbers.

Skills Demonstrated:
Python Programming: Efficient data handling with pandas.

Data Cleaning: Handling missing values, converting data types, and creating new features.

Data Analysis: Summarizing data with describe() and performing group-based calculations.

Data Visualization: Creating clear, informative bar charts with matplotlib and seaborn.

This project showcases my ability to transform raw data into meaningful insights, making it ready for business decisions. It also demonstrates my proficiency in Python.

