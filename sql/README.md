# Overview
This README showcases my skills and experience in data analysis, with a focus on using SQL to clean, analyze, and optimize business processes. Below are several key tasks I have performed, showcasing my ability to provide actionable insights, improve decision-making, and optimize business strategies. These tasks span data cleaning, customer segmentation, sales performance analysis, and more, using SQL to extract and manipulate data from a database effectively.

# Skills Highlighted:
## SQL Queries:

- Proficient in SELECT, WHERE, HAVING, GROUP BY, and ORDER BY for data extraction and filtering.

- Experienced with JOIN for combining data from multiple tables.

## Data Cleaning & Transformation:

- Skilled in UPDATE for data modification (e.g., TRIM, handling NULL values).

## Aggregation & Analysis:

- Use of SUM(), COUNT(), and GROUP BY for customer segmentation and sales analysis.

- Experienced with DENSE_RANK() and OVER() for trend analysis and ranking.

## Advanced Techniques:

P- roficient in CTEs and WINDOW FUNCTIONS for modular and trend-based analysis.

## Performance Optimization:

- Able to create INDEXES for faster query execution and use EXPLAIN for query tuning.

## Data Integrity:

- Expertise in identifying and handling duplicate records using GROUP BY and HAVING.

# Key SQL Queries & Business Insights
## 1. Understanding the Database Structure
Task: Exploring and identifying the tables within the database.

```
SELECT name FROM sqlite_master WHERE type='table';
-- Business Insight: This allows me to understand the database schema, which is essential before diving into analysis.
```

## 2. Data Cleaning & Preparation
Task: Identifying missing data in customer information and filling in missing values to standardize the data.

```
SELECT * FROM customer WHERE country IS NULL;
UPDATE customer SET country = 'Unknown' WHERE country IS NULL;
-- Business Insight: Clean data is crucial for accurate analysis. By handling missing values, I ensure the data is complete, leading to more reliable insights for decision-making.
```

## 3. Customer Segmentation & Spending Patterns
Task: Analyzing customer spending patterns to identify high-value customers.

```
SELECT customerid, SUM(total) AS total_spent
FROM invoice
GROUP BY customerid
ORDER BY total_spent DESC;
-- Business Insight: This helps identify customers who spend the most, enabling targeted marketing and personalized loyalty programs.
```

## 4. Sales Performance Analysis
Task: Analyzing sales performance by genre to optimize inventory and marketing strategies.

```
SELECT g.name AS genre, SUM(il.unitprice * il.quantity) AS revenue
FROM invoiceline il
JOIN track t ON il.trackid = t.trackid
JOIN genre g ON t.genreid = g.genreid
GROUP BY genre
ORDER BY revenue DESC;
-- Business Insight: Understanding which genres generate the most revenue helps in inventory management and tailoring marketing efforts toward high-performing categories.
```

## 5. Pricing Strategy Optimization
Task: Optimizing pricing strategy by analyzing the revenue generated from different pricing tiers.

```
SELECT unitprice, COUNT(*) AS num_tracks, SUM(unitprice * quantity) AS total_revenue
FROM invoiceline
GROUP BY unitprice
ORDER BY total_revenue DESC;
-- Business Insight: By evaluating the relationship between pricing and revenue, businesses can adjust pricing strategies to maximize profitability.
```

## 6. Identifying Potential Duplicate Customers
Task: Detecting customers with duplicate entries based on name and city to ensure data integrity.

```
SELECT firstname, lastname, city, COUNT(*) AS num_occurrences
FROM customer
GROUP BY firstname, lastname, city
HAVING COUNT(*) > 1;
-- Business Insight: Identifying duplicates helps maintain clean customer records, which is essential for accurate reporting and communication.
```

## 7. Data Standardization
Task: Removing unnecessary white spaces and standardizing customer names.

```
UPDATE customer
SET firstname = TRIM(firstname),
    lastname = TRIM(lastname);
-- Business Insight: Standardized data ensures consistency, reduces errors, and improves the accuracy of analysis and reporting.
```

## 8. Total Revenue Per Customer
Task: Calculating the total revenue generated per customer to identify high-value clients.

```
WITH CustomerRevenue AS (
    SELECT customerid, SUM(total) AS total_spent
    FROM invoice
    GROUP BY customerid
)
SELECT customerid, total_spent
FROM CustomerRevenue
ORDER BY total_spent DESC
LIMIT 10;
-- Business Insight: This query helps in identifying top customers, providing insights for targeted loyalty programs and personalized marketing strategies.
```

## 9. Trend Analysis Using Window Functions
Task: Analyzing the sales trends of individual tracks using window functions to rank sales performance.

```
SELECT t.trackid, t.name, t.genreid,
       SUM(il.unitprice * il.quantity) AS revenue,
       DENSE_RANK() OVER (ORDER BY SUM(il.unitprice * il.quantity) DESC) AS sales_rank
FROM invoiceline il
JOIN track t ON il.trackid = t.trackid
GROUP BY t.trackid, t.name, t.genreid
ORDER BY sales_rank;
== Business Insight: Using window functions allows me to identify and rank the best-selling tracks, providing actionable insights for inventory management and marketing strategies.
```

## 10. Identifying Loyal Customers
Task: Finding customers who made more than 6 purchases, which indicates loyalty and a strong relationship with the business.

```
SELECT customerid, firstname, lastname
FROM customer
WHERE customerid IN (
    SELECT customerid FROM invoice GROUP BY customerid HAVING COUNT(*) > 6
);
-- Business Insight: Loyal customers are valuable assets. Targeting them for special offers and rewards can increase customer retention and lifetime value.
```

## 11. Creating Indexes for Performance Optimization
Task: Creating an index to optimize query performance on customer invoices.

```
CREATE INDEX idx_customer_invoice ON invoice(customerid);
-- Business Insight: Indexes speed up data retrieval, improving performance and ensuring that analysis is done efficiently, especially with large datasets.
```

# Conclusion
The SQL queries presented above demonstrate my ability to clean data, perform advanced analysis, and optimize business strategies. By leveraging SQL, I can extract valuable insights that drive informed decision-making, improve operational efficiency, and enhance customer relations. These skills are critical for any data analyst aiming to help businesses grow and achieve their goals.
