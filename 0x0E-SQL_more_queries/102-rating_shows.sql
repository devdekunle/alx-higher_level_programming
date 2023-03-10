-- Write a script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tvs.title, SUM(tsr.rate) AS 'rating'
	FROM tv_shows tvs
	JOIN tv_show_ratings tsr
	ON tvs.id = tsr.show_id
	GROUP BY tvs.title
	ORDER BY rating DESC;
