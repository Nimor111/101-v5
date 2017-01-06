from decorators.user_exists import user_exists
from database.modify_database import *
from subprocess import check_output
from settings.reservations import reservations
from settings.general_settings import PROJECTIONS
from decorators.log_info import log_info


@log_info
def finalize(user_id, projection_id, seats):
    for seat in seats:
        insert_reservation(user_id, projection_id, seat[0], seat[1])


@user_exists
def make_reservation(user, password=None):
    print("Hello, {}".format(user))
    tickets = int(input("Step 1 (User): Choose number of tickets>"))
    show_movies()
    movie = input("Step 2 (Movie) : Choose a movie> ")
    print(check_output(['py', 'database/modify_database.py',
                        "{}".format(movie)]).decode("utf-8").strip())
    projection = int(input("Step 3 (Projection): Choose a projection>"))
    proj = Projection(projection)
    proj.hall = PROJECTIONS[projection - 1].hall
    print("Available seats (marked with a dot):")
    print(PROJECTIONS[projection - 1])
    chosen_seats = []
    for seat in range(tickets):
        seats = input("Choose seat {}>".format(seat + 1))
        seats = tuple(map(int, seats.split(',')))
        while proj.is_free_seat(seats) is None:
            print("Invalid seats - max seat is (10 10)")
            seats = input("Choose seat {}>".format(seat + 1))
            seats = tuple(map(int, seats.split(',')))
        while proj.is_free_seat(seats) is False:
            print("This seat is already taken!")
            seats = input("Choose seat {}>".format(seat + 1))
            seats = tuple(map(int, seats.split(',')))
        with open("settings/reservations.py", "a") as f:
            f.write("    settings.general_settings.PROJECTIONS[{}]. \
reserve_seat({}, {})\n".format(projection - 1, seats[0], seats[1]))
        chosen_seats.append(seats)
    print("This is your reservation:")
    user_id = get_user_id(user)
    mp_info = get_movie_and_proj_info(movie, projection)
    print("Movie: {} {}".format(mp_info['name'], mp_info['rating']))
    print("Date and Time: {} {} ({})".format(mp_info['date_'],
                                             mp_info['time_'],
                                             mp_info['type']))
    print("Seats: {}".format(chosen_seats))
    end = input("Step 5 (Confirm - type 'finalize')>")
    while end != 'finalize':
        print("TYPE 'finalize' please.")
    finalize(user_id, projection, chosen_seats)
    print("Thanks.")
    logout(user)


def main():
    pass


if __name__ == '__main__':
    main()
