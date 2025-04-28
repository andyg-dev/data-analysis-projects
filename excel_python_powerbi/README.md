# Productivity Trends Analysis Project
## Overview
This project focuses on analyzing productivity trends using detailed time-tracked data collected over 18 days in 2023. The data is recorded in small time blocks, as small as 5 minutes, and the project aimed to clean, categorize, and visualize this data to provide actionable insights into productivity.

## Technologies Used
### Python (Pandas): For data cleaning, transformation, and activity categorization.

### Excel (Power Query): For data transformation and cleanup before importing into Python.

### Power BI: For creating interactive reports and dashboards to visualize productivity trends.

## Project Details
### Data Cleaning:

Cleaned 1,000 rows of data by removing unnecessary entries and depersonalizing sensitive information.

Corrected time formats (e.g., "606-615" to proper start/end times) and standardized date-time columns.

Split combined date/time columns and applied formulas to handle inconsistencies in time notation (e.g., handling AM/PM formatting).

### Activity Categorization:

Created a Python script to automate the categorization of activities based on predefined keywords.

Merged activity categories with the data using exact keyword matching.

### Power BI Report:

Developed a series of Power BI visualizations, including bar charts and line graphs, to track productivity trends over time.

Implemented custom measures to calculate non-overlapping total time, as many activities were recorded within the same time block.

Designed interactive filters and slicers to allow users to analyze data by specific dates or over selected periods.

## Code Explanation
### Python Script
The provided Python script is used to clean the data, categorize activities, and merge the data with activity categories. Below is a summary of the main steps:

Data Import: Import the raw productivity data and activity category mapping from an Excel file.

Activity Categorization: Categorize activities based on matching keywords and add the category to the dataset.

Data Export: Save the cleaned and categorized data to a new Excel file.


`import pandas as pd
import os

# --- Configuration ---
excel_file_path = 'productivity_tracker_2023.xlsx'
data_sheet_name = 'data_cleanedup'
categories_sheet_name = 'activity_categories'
common_column = 'Activity'
column_to_join = 'Activity Category'
output_file_name = 'productivity_tracker_merged.xlsx'

# --- Data Loading ---
xls = pd.ExcelFile(excel_file_path)
df_data = xls.parse(data_sheet_name)
df_categories = xls.parse(categories_sheet_name)

# --- Exact Keyword Matching and Merging ---
category_lookup = df_categories.set_index(common_column)[column_to_join].to_dict()
category_keywords = df_categories[common_column].tolist()

# Match activities to categories
matched_categories = []
for index, row in df_data.iterrows():
    data_activity = str(row[common_column])
    found_category = None
    for keyword in category_keywords:
        if str(keyword) in data_activity:
            found_category = category_lookup.get(keyword)
            break
    matched_categories.append(found_category if found_category else "Other")

df_data[column_to_join] = matched_categories

# --- Save the Result ---
df_data.to_excel(output_file_name, index=False)
`

## Power BI Dashboard
The Power BI dashboard allows you to:

Visualize total time spent on each activity category over time using bar charts and line graphs.

Filter the data by specific dates or ranges using slicers.

Analyze non-overlapping time blocks with custom calculations to ensure accurate tracking of productivity.

## Installation and Setup
Clone this repository or download the project files.

Ensure that Python and Power BI Desktop are installed on your system.

Place the raw Excel data (productivity_tracker_2023.xlsx) in the project directory.

Run the Python script to clean and categorize the data.

Open the Power BI file (Productivity_Trend_Report.pbix) and connect it to the cleaned data.

## Conclusion
This project provides a comprehensive solution to analyze and visualize productivity trends over a short time period. The integration of Excel and Python for data processing and Power BI for reporting offers powerful insights into how activities change over time, helping optimize productivity tracking and resource allocation.

