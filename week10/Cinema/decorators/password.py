import hashlib
import getpass
import base64
import re
from user_interface.validators import *


def encode_pass(pw):
    '''
    Hash password with an awesome mathematical algorithm
    '''
    t_sha = hashlib.sha512()
    pw = base64.b64encode(t_sha.digest())
    return pw


def validate_password(func):
    '''
    Decorator to validate password
    '''
    def accepter(password):
        while validate_pass(password) is False:
            print("""
            Invalid password! Must be 8 symbols long, contain at least one
            special symbol, and have at least one capital letter!
            """)
            password = input("Enter new password: ")
        return func(password)
    return accepter


def hash_password(func):
    '''
    Decorator to hash password
    '''
    def accepter(password):
        password = encode_pass(password)
        return func(password)
    return accepter


# @validate_password
# @hash_password
# def set_password(password):
#     return password


def main():
    # pw = '1A@abcde'
    # pw = set_password(pw)
    # print(pw)
    pass


if __name__ == '__main__':
    main()
