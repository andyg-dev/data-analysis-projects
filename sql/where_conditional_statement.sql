-- Created by Andy Green  
-- Description: Show customers who have made purchases more than $10
-- Returns a list of cusomter with their first and last name who have made purchases more than $10

SELECT customerid, firstname, lastname
FROM customer
WHERE customerid IN (SELECT customerid FROM invoice WHERE total > 10);