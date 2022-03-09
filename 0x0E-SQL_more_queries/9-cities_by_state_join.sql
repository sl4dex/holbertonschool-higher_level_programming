-- 9. Cities by States
-- lists all cities and their state in db hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM  cities INNER JOIN states
ON states.id = cities.state_id
