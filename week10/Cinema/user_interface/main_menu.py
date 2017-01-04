from decorators.user_exists import *
from settings.general_settings import PROJECTIONS


@user_exists
def make_reservation(user, password):
    pass


def main():
    make_reservation("Georgi Bojinov", "KIMmuriel15@FH")
    PROJECTIONS[0].reserve_seat(1, 1)
    print(PROJECTIONS[0])


if __name__ == '__main__':
    main()
