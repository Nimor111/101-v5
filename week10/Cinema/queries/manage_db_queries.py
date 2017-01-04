ORDER_BY_RATING = '''
    SELECT *
    FROM movies
    ORDER BY rating DESC
'''

SELECT_USERS = '''
    SELECT username, password
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
    SELECT movies.name, projections.time_, projections.type, projections.id
    FROM movies
    JOIN projections ON movies.id = projections.movie_id
    WHERE movies.id = ? AND projections.date_ = ?
    ORDER BY time_
'''

SET_LOGGED = '''
    UPDATE users
    SET logged = 1
    WHERE users.username = ?
'''

SET_LOGOUT = '''
    UPDATE users
    SET logged = 0
    WHERE users.username = ?
'''

SELECT_LOGGED = '''
    SELECT logged
    FROM users
    WHERE users.username = ?
'''
