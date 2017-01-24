DROP_TABLE = '''
    DROP TABLE IF EXISTS CLIENTS
'''

CREATE_TABLE = '''
    CREATE TABLE IF NOT EXISTS CLIENTS
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
     username TEXT,
     password TEXT,
     balance REAL DEFAULT 0,
     message TEXT)
'''

UPDATE_CLIENT_MESSAGE = '''
    UPDATE clients
    SET message = ?
    WHERE id = ?
'''

UPDATE_PASSWORD = '''
    UPDATE clients
    SET password = ?
    WHERE id = ?
'''

SELECT_LOGIN = '''
    SELECT id, password, username, balance, message
    FROM clients
    WHERE username = ? AND password = ?
    LIMIT 1
'''

INSERT_USER = '''
    INSERT INTO clients (username, password)
    VALUES (?, ?)
'''

COUNT_CLIENTS = '''
    SELECT Count(*)
    FROM clients
    WHERE username = ? AND password = ?
'''
