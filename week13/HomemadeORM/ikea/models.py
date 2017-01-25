import sqlite3

from ikea.base import Metabase
# from ikea.queries import create_table


class BaseModel(metaclass=Metabase):

    db = sqlite3.connect("pesho.db")
    db.row_factory = sqlite3.Row
    c = db.cursor()

    __tablename__ = None

    @classmethod
    def create_all_tables(cls):
        for reg in list(cls._registry):
            print(reg.__name__)

    @classmethod
    def create_obj(cls, *args, **kwargs):
        pass
