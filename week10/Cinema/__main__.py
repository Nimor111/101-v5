from user_interface.main_menu import make_reservation, finalize, log_info
import settings.reservations
import settings.general_settings


def main():
    settings.reservations.reservations()
    make_reservation("Georgi Bojinov", "Ilikecake@")


if __name__ == '__main__':
    main()
