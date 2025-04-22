-- Created by Andy Green
-- Description: This query calculates the average spending amount of customers in each city.

SELECT
    BillingCity AS "City",
    ROUND(AVG(Total), 2) AS "Average Spending"
FROM
    Invoice i
GROUP BY
    BillingCity
ORDER BY
    "City" ASC;
