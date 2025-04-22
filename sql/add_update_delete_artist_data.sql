-- Created by Andy Green
-- Description: This query performs the following actions:
-- 1. Deletes an artist with ArtistID = 274.
-- 2. Updates the artist name with ArtistID = 275 to "Damien Marley".
-- 3. Inserts a new artist "Bob Marley" into the Artist table.

-- Deleting artist with ArtistID = 274
DELETE FROM Artist 
WHERE ArtistID = 274;

-- Updating artist name to "Damien Marley" where ArtistID = 275
UPDATE Artist 
SET Name = 'Damien Marley' 
WHERE ArtistID = 275;

-- Inserting a new artist "Bob Marley" into the Artist table
INSERT INTO Artist (Name) 
VALUES ('Bob Marley');
