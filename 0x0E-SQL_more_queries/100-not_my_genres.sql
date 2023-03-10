-- Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tvg.name
FROM tv_genres tvg
WHERE tvg.name NOT IN (
SELECT tvg.name
	FROM tv_genres tvg
	JOIN tv_show_genres tsg
	ON tvg.id = tsg.genre_id
	JOIN tv_shows tvs
	ON tvs.id = tsg.show_id
	WHERE tvs.title = 'Dexter')
	ORDER BY tvg.name;
