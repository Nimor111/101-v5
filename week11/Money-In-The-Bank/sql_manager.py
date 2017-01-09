import sqlite3
from client import Client
from queries import *

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    cursor.execute(CREATE_TABLE)


def change_message(new_message, logged_user):
    cursor.execute(UPDATE_CLIENT_MESSAGE, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    cursor.execute(UPDATE_PASSWORD, (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password):
    cursor.execute(INSERT_USER, (username, password))
    conn.commit()


def login(username, password):
    cursor.execute(SELECT_LOGIN, (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
