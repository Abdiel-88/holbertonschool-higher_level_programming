-- List all genres from hbtn_0d_tvshows and display the number of shows linked to each.
-- Do not display genres without shows linked. Sort results in descending order by number of shows linked.
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY genres.name
ORDER BY number_of_shows DESC, genre ASC;
