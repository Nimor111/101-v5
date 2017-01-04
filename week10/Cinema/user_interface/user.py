from user_interface.validators import *
from decorators.password import *


@validate_password
@hash_password
def set_password(password):
    return password


def set_username(username):
    return validate_username(username)


class User:

    def __init__(self, username, password):
        self.username = set_username(username)
        self.password = set_password(password)

    def __str__(self):
        return "{} : {}".format(self.username, self.password)

    def __repr__(self):
        return self.__str__()


def main():
    pass


if __name__ == '__main__':
    main()
