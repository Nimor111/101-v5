from decorators.user_exists import *


@user_exists
def make_reservation(user, password):
    pass


def main():
    make_reservation("Georgi Bojinov", "KIMmuriel15@FH")


if __name__ == '__main__':
    main()
