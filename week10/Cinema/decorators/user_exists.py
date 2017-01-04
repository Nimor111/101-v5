from functools import wraps
from queries.manage_db_queries import *
from database.modify_database import *
from user_interface.user import User, set_password, set_username
from decorators.password import encode_pass


def user_exists(func):
    def accepter(user, password):
        users = get_users()
        usernames = [person['username'] for person in users]

        if user not in usernames:
            print("You are not registered! Make an account!")
            user = input("Enter a username: ")
            password = input("Enter a password: ")
            new_user = User(user, password)
            insert_user(new_user)
        elif logged(user) is False:
            pw = [person['password'] for person in users if person['username']
                  == user][0]
            while encode_pass(password) == pw:
                password = input("Incorrect pass! Enter again: ")
            print("Logging in...")
            login(user)
        return func(user, password)
    return accepter
