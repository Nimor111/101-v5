from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Client

from settings import DB_NAME

engine = create_engine(DB_NAME)

Session = sessionmaker(bind=engine)

session = Session()


def register(username, password):
    client = Client(username=username, password=password)
    session.add(client)
    session.commit()


def main():
    register('Pesho', '123')


if __name__ == '__main__':
    main()
