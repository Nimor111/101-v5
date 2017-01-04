import re
from database.modify_database import *


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
