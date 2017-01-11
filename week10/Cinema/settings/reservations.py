import settings.general_settings


def reservations():
    settings.general_settings.PROJECTIONS[0].reserve_seat(2, 1)
    settings.general_settings.PROJECTIONS[1]. reserve_seat(1, 1) # Made by Georgi Bojinov
    settings.general_settings.PROJECTIONS[1]. reserve_seat(2, 2) # Made by Georgi Bojinov
