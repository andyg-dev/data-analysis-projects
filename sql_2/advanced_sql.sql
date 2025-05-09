--Understand the Database Structure
SELECT name FROM sqlite_master WHERE type='table';

-- Data Cleaning & Preparation
-- Business Reasoning: Clean data ensures more accurate insights for decision-making.

SELECT * FROM customer WHERE country IS NULL;
UPDATE customer SET country = 'Unknown' WHERE country IS NULL;

-- Customer Segmentation & SPending Patterns
-- Business Insights: Identify high-value customers for loyalty programs

SELECT customerid, SUM(total) AS total_spent
FROM invoice
GROUP BY customerid
ORDER BY total_spent DESC;

-- Sales Performance Analysis
-- Business Insights: Helps in optimizing inventory and marketing strategies

SELECT g.name AS genre, SUM(il.unitprice * il.quantity) AS revenue
FROM invoiceline il
JOIN track t ON il.trackid = t.trackid
JOIN genre g ON t.genreid = g.genreid
GROUP BY genre
ORDER BY revenue DESC;

-- Pricing Strategy Optimization
-- Business Insights: Determines which pricing strategy is most effective 
SELECT unitprice, COUNT(*) AS num_tracks, SUM(unitprice * quantity) AS total_revenue
FROM invoiceline
GROUP BY unitprice
ORDER BY total_revenue DESC;

-- Find potential duplicate customers (same name, city)
SELECT firstname, lastname, city, COUNT(*) AS num_occurrences
FROM customer
GROUP BY firstname, lastname, city
HAVING COUNT(*) > 1;

-- Remove unnecessary white spaces and standardize case
UPDATE customer
SET firstname = TRIM(firstname),
    lastname = TRIM(lastname);
	
-- Calculate total revenue per customer using CTE
WITH CustomerRevenue AS (
    SELECT customerid, SUM(total) AS total_spent
    FROM invoice
    GROUP BY customerid
)
SELECT customerid, total_spent
FROM CustomerRevenue
ORDER BY total_spent DESC
LIMIT 10;

-- Window FUnctions for Trend Analysis
SELECT t.trackid, t.name, t.genreid,
       SUM(il.unitprice * il.quantity) AS revenue,
       DENSE_RANK() OVER (ORDER BY SUM(il.unitprice * il.quantity) DESC) AS sales_rank
FROM invoiceline il
JOIN track t ON il.trackid = t.trackid
GROUP BY t.trackid, t.name, t.genreid
ORDER BY sales_rank;

-- Find customers who made more than 6 purchases
-- Business Acumen: This helps target loyal customers for marketing efforts

SELECT customerid, firstname, lastname
FROM customer
WHERE customerid IN (
    SELECT customerid FROM invoice GROUP BY customerid HAVING COUNT(*) > 6
);

-- Create an index for faster retrieval in invoices
CREATE INDEX idx_customer_invoice ON invoice(customerid);
