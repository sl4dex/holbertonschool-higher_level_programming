-- 16. Say my name
-- lists all records of the table second_table with a non NULL name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
