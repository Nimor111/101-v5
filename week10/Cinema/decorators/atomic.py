from settings.sql_creation_settings import DB_NAME
import sqlite3


db = sqlite3.connect('../{}'.format(DB_NAME))
db.row_factory = sqlite3.Row
c = db.cursor()


def atomic(func):
    def accepter():
        try:
            func()
        except:
            db.rollback()
        finally:
            db.close()
    return accepter
