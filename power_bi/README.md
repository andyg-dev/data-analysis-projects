# Power BI Sales Analysis Project - Adventure Works

Welcome to my Power BI Sales Analysis project! This project showcases the various Power BI skills I have developed by analyzing sales data for **Adventure Works**, a fictional company. In this project, I demonstrate skills in **data transformation, modeling, DAX**, and **visualizations** to create an insightful dashboard using sales data from the United States and other countries.

## Project Overview

The goal of this project is to create an interactive dashboard that provides insights into Adventure Works' sales performance, customers, and products. Key operations include:

- **Importing Sales Data** from multiple countries (United States and others).
- **ETL (Extract, Transform, Load)** process using Power Query to clean and prepare the data.
- **Creating Calculated Columns and Measures** using DAX.
- **Building Interactive Dashboards** with various visualizations.

## Skills Showcased

### 1. **Power Query & Data Transformation**

- **Importing Data**: Connected to Excel to load sales and customer data from the United States and other countries.
- **Appending Queries**: Combined multiple data sources for consistent analysis.
- **Standardizing/Normalizing Data**: Cleaned data by standardizing and normalizing product names, customer names, and sales territories to ensure consistency.
- **Removing Unnecessary Columns and Tables**: Cleared out irrelevant data to focus on essential fields.
- **Merging Queries**: Merged product rollup queries with the main product data query to ensure that product-related data is consistent and properly structured.
- **Creating Hierarchies**: Built hierarchical relationships for product categories and territories to enable drill-down analysis.

### 2. **Data Modeling**

- **Star Schema**: Designed a **star schema** to organize data effectively, with separate fact and dimension tables:
  - **Fact Table**: Sales data.
  - **Dimension Tables**: Customers, Order Date, Sales Territory, Product.
- **Relationships**: Created appropriate one-to-many relationships between tables to enable smooth navigation and data analysis.
- **Removing Redundant Data**: Deleted unnecessary tables and columns that didn’t contribute to the analysis.

### 3. **DAX (Data Analysis Expressions)**

- **Creating Measures**: Used DAX to create various measures, using **"IF, IN, SUM, YTD, QTD"**
- **Calculated Columns**: Created calculated columns such as **Concatenating Customer First and Last Names.**
- **KPI Measures**: Defined KPIs to track performance against targets, such as **sales targets**.

### 4. **Data Visualizations**

- **Interactive Dashboard**: Built an engaging dashboard with interactive features for the end user.
  - **Clustered Column Chart**: Visualized sales performance by continent.
  - **Stacked Bar Chart**: Showed total margin % and order quantity by product category.
  - **Line Chart**: Displayed trends in sales over time.
  - **KPI Visual**: Presented key performance indicators, including **target**, and **total sales**.
- **Drill-through**: Enabled drill-through functionality to allow users to explore detailed information for specific regions, country, and products.
- **Slicers**: Added slicers for users to filter data by **Continent**,and **Year**.
- **Canvas Background**: Customized the background of the report canvas to match the branding of Adventure Works.

### 5. **Publishing and Sharing**

- **Power BI Service**: Published the dashboard to Power BI Service to make it accessible online and shared it with stakeholders.

## Files Included

- **power_bi_sales_project.pbix**: The Power BI file that contains all data transformations, models, DAX measures, and visuals.
- **Screenshots**: Images of visuals in the dashboard, some DAX functions, star schema, and other relevant Power BI skills. 

## How to Use

1. Clone this repository to your local machine.
2. Open the **power_bi_sales_project.pbix** file in Power BI Desktop.
3. Review the data model and dashboard visualizations.
4. If you want to explore the data and models, feel free to interact with slicers and drill-through features in the dashboard.

## Conclusion

This project demonstrates my ability to effectively use Power BI to process and analyze large datasets, create insightful reports, and build interactive dashboards. I hope this project showcases my ability to perform key tasks like **data cleaning**, **data modeling**, and **visualization** using Power BI.

Feel free to explore the project and provide any feedback. 

---

**Technologies Used:**
- Power BI
- DAX (Data Analysis Expressions)
- Power Query (M Language)
- Star Schema Data Modeling

**Disclaimer:** All data used in this project is fictional and sourced from the Adventure Works database, which is a sample database used for training and demonstration purposes.

