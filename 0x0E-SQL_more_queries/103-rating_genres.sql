-- Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tvg.name, SUM(tsr.rate) AS 'rating'
	FROM tv_genres tvg
	JOIN tv_show_genres tsg
	ON tvg.id = tsg.genre_id
	JOIN tv_show_ratings tsr
	ON tsg.show_id = tsr.show_id
	GROUP BY tvg.name
	ORDER BY rating DESC;
