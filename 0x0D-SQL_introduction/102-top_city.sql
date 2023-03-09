-- display top 3 cities temperature during july and august

SELECT city, AVG(value) AS 'avg_temp'
	FROM temperatures
	WHERE month REGEXP '7|8'
	GROUP BY city
	ORDER BY avg_temp DESC
	LIMIT 3;
