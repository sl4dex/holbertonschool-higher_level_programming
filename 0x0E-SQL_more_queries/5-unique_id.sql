-- 5. Unique ID
-- creates the table unique_id with id unique default 1
CREATE TABLE IF NOT EXISTS unique_id
	(id INT DEFAULT 1 UNIQUE, name VARCHAR(256))
