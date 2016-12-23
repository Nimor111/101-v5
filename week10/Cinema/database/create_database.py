import sqlite3
from queries.create_db_queries import *
from settings.sql_creation_settings import *

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


def create_database():
    c.execute(CREATE_MOVIES_TABLE)
    c.execute(CREATE_PROJECTIONS_TABLE)
    c.execute(CREATE_USERS_TABLE)
    c.execute(CREATE_RESERVATIONS_TABLE)


def drop_database():
    c.execute(DROP_MOVIES_TABLE)
    c.execute(DROP_PROJECTIONS_TABLE)
    c.execute(DROP_USERS_TABLE)
    c.execute(DROP_RESERVATIONS_TABLE)


def insert_movies():
    movies = [("The Hunger Games: Catching Fire", 7.9),
              ("Wreck-it Ralph", 7.8),
              ("Her", 8.3)]

    c.executemany(INSERT_MOVIES, movies)
    db.commit()


def insert_projections():
    projections = [(1, "3D", "2014-04-01", "19:10"),
                   (1, "2D", "2014-04-01", "19:00"),
                   (1, "4DX", "2014-04-02", "21:00"),
                   (3, "2D", "2014-04-05", "20:20"),
                   (2, "3D", "2014-04-02", "22:00"),
                   (2, "2D", "2014-04-02", "19:30")]

    c.executemany(INSERT_PROJECTIONS, projections)
    db.commit()


def insert_reservations():
    reservations = [(3, 1, 2, 1),
                    (3, 1, 3, 5),
                    (3, 1, 7, 8),
                    (2, 3, 1, 1),
                    (2, 3, 1, 2),
                    (5, 5, 2, 3),
                    (6, 5, 2, 4)]

    c.executemany(INSERT_RESERVATIONS, reservations)
    db.commit()


def insert_users():
    users = [("Rositsa Zlateva", "12345678"),
             ("Slavyana Monkova", "12345678"),



def main():
    drop_database()
    create_database()
    insert_movies()
    insert_projections()
    insert_reservations()


if __name__ == '__main__':
    main()
