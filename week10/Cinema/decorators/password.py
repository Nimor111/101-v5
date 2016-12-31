import hashlib
import getpass
import base64
import re


def encode_pass(pw):
    '''
    Hash password with an awesome mathematical algorithm
    '''
    t_sha = hashlib.sha512()
    pw = base64.b64encode(t_sha.digest())
    return pw


def validate_pass(pw):
    '''
    Validate password - Capital letter, Symbol, Longer than 7 symbols
    '''
    if re.search(r'[A-Z]', pw) and re.search(r'[^0-9A-Za-z]', pw) \
       and len(pw) > 7:
        return True
    return False


def validate_password(func):
    '''
    Decorator to validate password
    '''
    def accepter(password):
        if validate_pass(password):
            return func(password)
        return False
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
