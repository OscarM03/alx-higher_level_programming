-- displays the average temp in desc order
SELECT city, AVG(value) AS avg_temp
FROM temparatures
GROUP BY city
ORDER BY avg_temp DESC;