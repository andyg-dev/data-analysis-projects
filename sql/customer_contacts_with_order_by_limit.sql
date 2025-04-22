-- Created by Andy Green  
-- Description: Retrieve the first and last names, along with email addresses, of customers.  
-- Returns the top 15 customers ordered alphabetically by first name (ascending) and last name (descending).

SELECT
    FirstName AS "Customer First Name",
    LastName AS "Customer Last Name",
    Email AS "Email"
FROM
    Customer
ORDER BY
    FirstName ASC,
    LastName DESC
LIMIT 15;