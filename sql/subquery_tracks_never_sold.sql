-- Created by Andy Green
-- Description: This query identifies tracks that have never been sold.

SELECT 
    t.TrackID AS "Track ID", 
    t.Name AS "Track Name", 
    t.Composer, 
    g.Name AS "Genre"
FROM 
    Track t
JOIN 
    Genre g ON t.GenreID = g.GenreID
WHERE 
    t.TrackId NOT IN (
        SELECT DISTINCT InvoiceLine.TrackId
        FROM InvoiceLine
    )
ORDER BY 
    "Track Name" ASC;
