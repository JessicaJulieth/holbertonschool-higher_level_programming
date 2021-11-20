-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_shows.name AS genre, tv_show_genres.genre_id AS number_of_shows
FROM tv_genres
INNER JOIN tv_shows_genres ON tv_genres.shows_id = tv_show_genres.genre_id
ORDER BY number_of_shows DES;
