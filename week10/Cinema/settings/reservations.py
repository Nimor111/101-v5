import settings.general_settings


def reservations():
    settings.general_settings.PROJECTIONS[0].reserve_seat(2, 1)
    settings.general_settings.PROJECTIONS[0].reserve_seat(3, 5)
    settings.general_settings.PROJECTIONS[0].reserve_seat(7, 8)
    settings.general_settings.PROJECTIONS[2].reserve_seat(1, 1)
    settings.general_settings.PROJECTIONS[2].reserve_seat(1, 2)
    settings.general_settings.PROJECTIONS[4].reserve_seat(2, 3)
    settings.general_settings.PROJECTIONS[4].reserve_seat(2, 4)
    settings.general_settings.PROJECTIONS[5]. reserve_seat(1, 1)
    settings.general_settings.PROJECTIONS[5]. reserve_seat(2, 2)
    settings.general_settings.PROJECTIONS[5]. reserve_seat(3, 3)
    settings.general_settings.PROJECTIONS[5]. reserve_seat(4, 4)
