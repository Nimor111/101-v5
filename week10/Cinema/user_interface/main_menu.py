from decorators.user_exists import user_exists
import interface


@user_exists
def make_reservation(user, password):
    interface.PROJECTIONS[0].reserve_seat(9, 9)


def main():
    # interface.PROJECTIONS = "Pesho"
    # make_reservation("Georgi Bojinov", "KIMmuriel15@FH")
    print(interface.PROJECTIONS)


if __name__ == '__main__':
    main()
