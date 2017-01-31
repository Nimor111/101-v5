import sqlite3

from ikea.base import Metabase
from ikea.queries import create_table, insert, drop


class BaseModel(metaclass=Metabase):

    db = sqlite3.connect("pesho.db")
    db.row_factory = sqlite3.Row
    c = db.cursor()

    __tablename__ = None

    @classmethod
    def drop_tables(cls):
        for reg in list(cls._registry):
            BaseModel.c.execute(drop(reg))
        BaseModel.db.commit()

    @classmethod
    def create_all_tables(cls):
        BaseModel.drop_tables()
        for reg in list(cls._registry):
            BaseModel.c.execute(create_table(reg))
        BaseModel.db.commit()

    @classmethod
    def create_obj(cls, *args, **kwargs):
        print(insert(cls, *args, **kwargs))
        attrs = tuple([kwargs[key] for key in kwargs])
        BaseModel.c.execute(insert(cls, *args, **kwargs), attrs)
        BaseModel.db.commit()
