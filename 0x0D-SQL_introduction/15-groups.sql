-- lists the number of records with the same score
-- database name will be passed as argument
SELECT score COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score DESC;