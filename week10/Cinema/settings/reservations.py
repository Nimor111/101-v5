import settings.general_settings


def reservations():
    settings.general_settings.PROJECTIONS[0].reserve_seat(2, 1)
