-- lists all records with a score >= 10
-- database name will be passed as an argument
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;