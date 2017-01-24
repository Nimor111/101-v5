import sqlite3
from client import Client
from queries import *
import settings
import getpass
from validators import validate_password
from validators import encode_pass


conn = sqlite3.connect(settings.DB_NAME)
cursor = conn.cursor()


def drop_clients_table():
    cursor.execute(DROP_TABLE)


def create_clients_table():
    cursor.execute(CREATE_TABLE)


def change_message(new_message, logged_user):
    cursor.execute(UPDATE_CLIENT_MESSAGE, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    if not validate_password(logged_user.get_username(), new_pass):
        print("""Invalid password! - 8 symbols, special symbol, capital letter,
number""")
        new_pass = getpass.getpass("Enter a new password: ")
        while not validate_password(logged_user.get_username(), new_pass):
            print("""Invalid password! - 8 symbols, special symbol,
capital letter, number""")
            new_pass = getpass.getpass("Enter a new password: ")
    cursor.execute(UPDATE_PASSWORD, (encode_pass(new_pass),
                                     logged_user.get_id()))
    conn.commit()


def register(username, password):
    if not validate_password(username, password):
        print("""Invalid password! - 8 symbols, special symbol, capital letter,
number""")
        password = getpass.getpass("Enter a new password: ")
        while not validate_password(username, password):
            print("""Invalid password! - 8 symbols, special symbol,
capital letter, number""")
            password = getpass.getpass("Enter a new password: ")

    cursor.execute(INSERT_USER, (username, encode_pass(password)))
    conn.commit()


def login(username, password):
    cursor.execute(SELECT_LOGIN, (username, encode_pass(password)))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[2], user[3], user[4])
    else:
        return False
