-- Created by Andy Green
-- Description: This query generates a report that lists each customer along with their assigned support representative.

SELECT
    c.FirstName AS "Customer First Name",
    c.LastName AS "Customer Last Name",
    e.FirstName AS "Support Rep First Name",
    e.LastName AS "Support Rep Last Name"
FROM
    Customers c
JOIN
    Employee e ON c.SupportRepId = e.EmployeeId
ORDER BY
    e.LastName, c.LastName;