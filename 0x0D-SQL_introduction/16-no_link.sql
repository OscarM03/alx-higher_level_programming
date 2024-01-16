-- lists all the records of the table
-- database will be passed as argument
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;