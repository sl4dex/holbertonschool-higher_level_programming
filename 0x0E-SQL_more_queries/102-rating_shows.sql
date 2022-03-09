-- 19. Rotten tomatoes
-- lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT tv_shows.title, tv_show_ratings.rating
FROM tv_shows INNER JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
ORDER BY rating
