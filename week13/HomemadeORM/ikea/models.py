import sqlite3

from ikea.base import Metabase


class BaseModel(metaclass=Metabase):

    db = sqlite3.connect("pesho.db")
    db.row_factory = sqlite3.Row
    c = db.cursor()

    __tablename__ = None

    @classmethod
    def create_all_tables(cls):
        print(vars(cls))

    @classmethod
    def create_obj(cls, *args, **kwargs):
        for k, v in kwargs.items():
            cls._fields[k].set_data(v)
        return cls
