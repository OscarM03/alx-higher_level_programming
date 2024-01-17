-- lists all genres of dexter
SELECT gt.name 
FROM tv_shows ts
INNER JOIN tv_show_genres tg ON ts.id = tg.show_id
INNER JOIN tv_genres gt ON tg.genre_id = gt.id
WHERE ts.id = 8
ORDER BY gt.name ASc;