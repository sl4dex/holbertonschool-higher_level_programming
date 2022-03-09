-- 16. List shows and genres
-- lists all shows and all their genres (even if null)
SELECT tv_shows.title, tv_genres.name
FROM tv_show_genres
	RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	RIGHT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name
