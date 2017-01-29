from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import String, Integer, Float

import settings


engine = create_engine(settings.DB_NAME)

Base = declarative_base()


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))
    balance = Column(Float, default=0)
    message = Column(String(255), default='Cake')


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
