-- Import database dump of hbtn_0d_tvshows and list all shows, displaying each show's title and genre_id. Shows without a genre display NULL.
-- Results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
