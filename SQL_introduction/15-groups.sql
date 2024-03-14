-- List the number of records with the same score, sorted by this number in descending order
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;