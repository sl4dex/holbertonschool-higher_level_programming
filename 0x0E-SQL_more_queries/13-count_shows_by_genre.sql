-- 13. Number of shows by genre
-- lists all shows in db hbtn_0d_tvshows and counts its genres
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC
