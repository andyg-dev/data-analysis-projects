-- Created by Andy Green
-- Description: This query finds the average invoice totals greater than $5 for cities starting with "B".

SELECT 
    BillingCity AS "City", 
    ROUND(AVG(Total), 2) AS "Average Invoice Total"
FROM 
    Invoice
WHERE 
    BillingCity LIKE 'B%'  -- Filters cities starting with "B"
GROUP BY 
    BillingCity
HAVING 
    AVG(Total) > 5  -- Filters results where the average invoice total is greater than $5
ORDER BY 
    BillingCity ASC;
