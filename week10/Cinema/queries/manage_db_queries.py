ORDER_BY_RATING = '''
    SELECT *
    FROM movies
    ORDER BY rating DESC
'''

SELECT_USERS = '''
    SELECT username || " " || password
    FROM users
'''

ORDER_BY_ONLY_ID = '''
    SELECT movies.name, projections.id, projections.time_, projections.date_,
    projections.type
    FROM movies
    JOIN projections ON movies.id = projections.movie_id
    WHERE movies.id = ?
    ORDER BY time_
'''

ORDER_BY_DATE_AND_ID = '''
    SELECT movies.name, projections.time_, projections.type
    FROM movies
    JOIN projections ON movies.id = projections.movie_id
    WHERE movies.id = ? AND projections.date_ = ?
    ORDER BY time_
'''
