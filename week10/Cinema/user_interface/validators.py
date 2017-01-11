import re
from database.modify_database import *
from user_interface.user import *
import decorators.password


def validate_pass(pw):
    '''
    Validate password - Capital letter, Symbol, Longer than 7 symbols
    '''
    if re.search(r'[A-Z]', pw) and re.search(r'[^0-9A-Za-z]', pw) \
       and len(pw) > 7:
        return True
    return False


def validate_username(username):
    '''
    Validate username - if there's such a username, prompt
    a different one to be entered
    '''
    users = get_users()
    users = [user['username'] for user in users]

    if username in users:
        username = input("Username exists. Enter new username: ")

    return username


def check_user(username):
    '''
    Check if user exists in the db - if not prompt for registration
    '''
    users = get_users()
    usernames = [person['username'] for person in users]

    if username not in usernames:
        print("You are not registered! Make an account!")
        user = input("Enter a username: ")
        password = input("Enter a password: ")
        new_user = User(user, password)
        insert_user(new_user)


def check_login(username, password):
    '''
    Check if user is inputting correct password
    '''
    users = get_users()
    pw = [person['password'] for person in users if person['username']
          == username][0]
    while decorators.password.encode_pass(password) \
            != decorators.password.encode_pass(pw):
        password = input("Incorrect pass! Enter again: ")
    print("Logging in...")
    login(username)
