-- 8. Cities of California
-- lists all the cities of California in db hbtn_0d_usa
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
