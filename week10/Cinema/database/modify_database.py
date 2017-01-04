import sqlite3
from queries.manage_db_queries import *
from queries.create_db_queries import INSERT_USERS, INSERT_RESERVATIONS
from settings.sql_creation_settings import *
from sys import argv
from decorators.atomic import *


db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


@atomic
def show_movies():
    """
    Displays all movies ordered by rating ( descending )
    """
    c.execute(ORDER_BY_RATING)
    movies = c.fetchall()
    print('Current movies: ')
    for movie in range(len(movies)):
        print("[{}] - {} ({})".format(movie + 1, movies[movie]['name'],
                                      movies[movie]['rating']))


@atomic
def show_movie_projections():
    """
    Displays projections for given movie ordered by time
    """
    if len(argv) == 3:
        c.execute(ORDER_BY_DATE_AND_ID, (argv[1], argv[2]))
        projections = c.fetchall()
    else:
        c.execute(ORDER_BY_ONLY_ID, (argv[1], ))
        projections = c.fetchall()

    if len(argv) == 3:
        print("Projections for movie '{}' on date {}:"
              .format(projections[0]['name'], argv[2]))
        for projection in range(len(projections)):
            print("[{}] - {} ({})".format(projection + 1,
                                          projections[projection]['time_'],
                                          projections[projection]['type']))
    else:
        print("Projections for movie '{}':".format(projections[0]['name']))
        for projection in projections:
            print("[{}] - {} ({})".format(projection['id'],
                                          projection['time_'],
                                          projection['type']))


@atomic
def get_users():
    """
    Gets username and password for all users currently in db
    """
    c.execute(SELECT_USERS)
    users = c.fetchall()
    return users


@atomic
def login(username):
    """
    Login user into the system
    """
    c.execute(SET_LOGGED, (username, ))
    db.commit()


@atomic
def logout(username):
    """
    Logout user from the system
    """
    c.execute(SET_LOGOUT, (username, ))
    db.commit()


@atomic
def insert_user(user):
    """
    Insert a user into the database and log him in
    """
    c.execute(INSERT_USERS, (user.username, user.password))
    db.commit()
    login(user.username)


@atomic
def logged(username):
    """
    See if user is logged or not
    """
    c.execute(SELECT_LOGGED, (username, ))
    return c.fetchone()['logged'] == 1


@atomic
def insert_reservation(user, projection, row, col):
    """
    Insert a new reservation into the system
    """
    c.execute(INSERT_RESERVATIONS, (user, projection, row, col))
    db.commit()


def main():
    show_movie_projections()
    show_movies()
    db.close()


if __name__ == '__main__':
    main()
