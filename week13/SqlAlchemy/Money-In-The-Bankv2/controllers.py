from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Client

import settings

engine = create_engine(settings.DB_NAME)

Session = sessionmaker(bind=engine)

session = Session()


def register(username, password):
    client = Client(username=username, password=password)
    session.add(client)
    session.commit()


def login(username, password):
    query = session.query(Client).filter(username == Client.username,
                                         password == Client.password)
    return query.one()


def change_message(new_message, logged_user):
    session.query(Client).filter(logged_user.id == Client.id) \
            .update({'message': new_message})
    session.commit()


def change_password(new_password, logged_user):
    session.query(Client).filter(logged_user.id == Client.id) \
            .update({'password': new_password})
    session.commit()


def main():
    register('Pesho', '123')
    logged_user = login('Pesho', '123')
    change_message('Cake', logged_user)
    change_password('Pesho221', logged_user)


if __name__ == '__main__':
    main()
