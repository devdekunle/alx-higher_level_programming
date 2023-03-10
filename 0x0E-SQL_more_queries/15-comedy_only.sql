-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tvs.title
	FROM tv_shows tvs
	JOIN tv_show_genres tsg
	ON tvs.id = tsg.show_id
	JOIN tv_genres tvg
	ON tsg.genre_id = tvg.id
	WHERE tvg.name = 'Comedy'
	ORDER BY tvs.title;
