import hashlib
import getpass
import base64
import re


def encode_pass(pw):
    t_sha = hashlib.sha512()
    pw = base64.b64encode(t_sha.digest())
    return pw


def validate_pass(pw):
    if re.search(r'[A-Z]', pw) and re.search(r'[a-z]', pw) \
            and re.search(r'[0-9]', pw) and len(pw) > 7:
        return True
    return False


def main():
    pass
    # print(validate_pass('Pe1sho23'))
    # print(validate_pass('pesho'))
    # print(encode_pass('pesho'))


if __name__ == '__main__':
    main()
