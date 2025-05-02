-- Created by Andy Green  
-- Description: Use conditional statement to categorize purchases as High Value, Medium Value, or Low Value
-- Returns a custom column that labels value based on total purchase amounts

SELECT invoiceid, total,
    CASE 
        WHEN total > 5 THEN 'High-value purchase'
        WHEN total BETWEEN 3 AND 5 THEN 'Medium-value purchase'
        ELSE 'Low-value purchase'
    END AS purchase_category
FROM invoice;