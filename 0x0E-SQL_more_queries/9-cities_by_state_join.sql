-- script that lists all cities contained in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT c.id, c.name AS 'name', s.name AS 'name'
	FROM cities c
	JOIN states s
		ON 	c.state_id = s.id
	ORDER BY c.id;

