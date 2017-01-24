import re
import hashlib
import base64


def validate_password(user, pw):
    if len(pw) > 8 and re.search(r'[A-Z]', pw) and re.search(r'[0-9]', pw) \
     and re.search(r'[^A-Za-z0-9]', pw) and user not in pw:
            return True
    return False


def encode_pass(pw):
    '''
    Hash password with an awesome mathematical algorithm
    '''
    hash_object = hashlib.sha256(pw.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig
