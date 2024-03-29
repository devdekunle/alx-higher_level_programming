-- Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tvs.title
	FROM tv_shows tvs
	WHERE tvs.title NOT IN (
	SELECT tvs.title
	FROM tv_shows tvs
	JOIN tv_show_genres tsg
	ON tvs.id = tsg.show_id
	JOIN tv_genres tvg
	ON 	tsg.genre_id = tvg.id
	WHERE tvg.name = 'Comedy')
	ORDER BY tvs.title;

