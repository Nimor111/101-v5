ORDER_BY_RATING = '''
    SELECT *
    FROM movies
    ORDER BY rating DESC
'''

SELECT_USERS = '''
    SELECT username || " " || password
    FROM users
'''
