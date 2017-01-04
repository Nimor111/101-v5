from settings.sql_creation_settings import DB_NAME
from functools import wraps, partial
import sqlite3


db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


def atomic(func):

    @wraps(func)
    def accepter(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except:
            db.rollback()
    return accepter
